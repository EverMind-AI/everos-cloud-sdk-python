"""High-level ergonomic client for the EverOS Cloud Memory API.

A thin, hand-maintained facade over the generated API clients: plain kwargs / dicts
in, response ``.data`` out. Every generated client stays available for full control —
``client.memory``, ``client.storage``, ``client.knowledge``, ``client.tasks`` — and the
facade covers the high-traffic calls of each.

    from everos_cloud import EverOS

    client = EverOS(api_key="sk-...")
    client.add(session_id="s1", messages=[{"role": "user", "content": "I love hiking"}])
    hits = client.search("outdoor hobbies")

Naming: the nine methods 1.0.0 shipped are bare verbs and stay that way — ``add`` /
``search`` / ``get`` / ``flush`` / ``edit`` / ``delete`` (memory), ``presign`` /
``upload`` (storage), ``close``. They are public API and cannot be renamed. Memory
methods added since follow the same bare-verb shape so the memory group stays one
style and each name is the last segment of its route — ``update`` / ``delete_by_ids``
/ ``feedback`` (1.2.0), ``context`` (1.3.0). Every other resource carries its name as a prefix — ``kb_`` /
``doc_`` / ``task_`` / ``tag_`` — so completion groups by resource and no facade method
collides with the generated method it wraps. The memory-space purge (1.3.0) is a memory
route but a multi-call flow, so it takes a prefix like ``task_``: ``purge_request`` /
``purge_confirm`` / ``purge_get`` / ``purge_wait``.

Errors: every failure raised by this facade derives from :class:`EverOSError` —
``EverOSAPIError`` for HTTP errors, ``EverOSStorageError`` for object-upload failures,
and a plain ``EverOSError`` for a task or purge that fails or outlives its wait timeout.
"""
from __future__ import annotations

import json
import mimetypes
import os
import time
from typing import Any, Mapping, Sequence, Union

import urllib3

from everos_cloud import ApiClient, Configuration, KnowledgeApi, MemoryApi, StorageApi, TasksApi
from everos_cloud.exceptions import ApiException
from everos_cloud.models import (
    AddInput,
    AddOperation,
    Content,
    ContentItem,
    ContextInput,
    DeleteByIdsInput,
    DeleteInput,
    DeleteOperation,
    DocIngestBody,
    DocPatchBody,
    EditInput,
    EditInputOperationsInner,
    EpisodePatch,
    FeedbackInput,
    FlushInput,
    GetInput,
    KbCreateInput,
    KbPatchBody,
    MessageItem,
    PurgeConfirmInput,
    PurgeRequestData,
    PurgeRequestInput,
    Reason,
    SearchBody,
    SearchInput,
    SignObjectItem,
    SignRequest,
    TagBindInput,
    TagReplaceInput,
    TagUnbindInput,
    UpdateInput,
    UpdateOperation,
)

__all__ = ["EverOS", "EverOSError", "EverOSAPIError", "EverOSStorageError"]

DEFAULT_TIMEOUT = 60.0  # seconds; agentic search / LLM rerank can be slow
DEFAULT_TASK_TIMEOUT = 300.0  # seconds to wait for an async task before giving up
DEFAULT_TASK_INTERVAL = 2.0  # seconds before the first task re-poll
DEFAULT_TASK_MAX_INTERVAL = 15.0  # ceiling for the backoff between task polls
DEFAULT_PURGE_TIMEOUT = 1800.0  # seconds; a purge of a large memory space takes minutes

# Statuses worth retrying DURING a poll rather than aborting the whole wait. A long
# ingest polled at a fixed interval is itself a source of 429s, and a wait that dies
# on one blip is worse than useless — the caller has no way to resume it.
_TRANSIENT_STATUS = frozenset({429, 500, 502, 503, 504})

# Generated method name -> the facade method that covers it. Used only to answer an
# AttributeError helpfully: the generated per-endpoint docs (docs/*.md) are the largest
# body of documentation and they describe ONLY the generated clients, so a reader who
# arrives from there types `client.create_knowledge_base(...)` and would otherwise get a
# bare AttributeError with nowhere to go.
_FACADE_FOR = {
    "add_memory": "add", "search_memory": "search", "get_memory": "get",
    "flush_memory": "flush", "edit_profile": "edit", "delete_memory": "delete",
    "update_memory": "update", "delete_memories_by_ids": "delete_by_ids",
    "submit_feedback": "feedback", "retrieve_context": "context",
    "sign_objects": "presign",
    "bind_tags": "tag_bind", "unbind_tags": "tag_unbind", "replace_tags": "tag_replace",
    "create_knowledge_base": "kb_create", "list_knowledge_bases": "kb_list",
    "get_knowledge_base": "kb_get", "update_knowledge_base": "kb_update",
    "delete_knowledge_base": "kb_delete", "search_knowledge": "kb_search",
    "create_document": "doc_ingest", "replace_document": "doc_ingest",
    "list_documents": "doc_list", "get_document": "doc_get",
    "update_document": "doc_update", "delete_document": "doc_delete",
    "get_task_status": "task_get", "list_tasks": "task_list",
    "request_purge": "purge_request", "confirm_purge": "purge_confirm",
    "get_purge_job": "purge_get",
}
_API_ATTRS = ("memory", "storage", "knowledge", "tasks")

# Statuses the gateway reports as finished. Deliberately paired with a `finished_at`
# check in `_task_finished`: `status` is an OPEN set on a response field (a new
# terminal state such as `cancelled` must not make `task_wait` spin until timeout),
# and the contract documents `finished_at` as "absent while the task is not in a
# terminal state" — so the timestamp, not the enum, is the load-bearing signal.
_TERMINAL_TASK_STATUS = frozenset({"success", "failed"})
# Same reasoning for purge jobs, whose terminal statuses are spelled differently.
_TERMINAL_PURGE_STATUS = frozenset({"succeeded", "failed"})

_OP_CLASSES = {"add": AddOperation, "update": UpdateOperation, "delete": DeleteOperation}

_IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"}
_VIDEO_EXT = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v"}

MessageLike = Union[MessageItem, Mapping[str, Any]]
ContentLike = Union[ContentItem, Mapping[str, Any], str]
ReasonLike = Union[Reason, Mapping[str, Any], str]


def _guess_file_type(name: str) -> str:
    ext = os.path.splitext(name)[1].lower()
    if ext in _IMAGE_EXT:
        return "image"
    if ext in _VIDEO_EXT:
        return "video"
    return "file"


def _clean(**kwargs: Any) -> dict:
    """Drop ``None`` values so model defaults (e.g. search ``method='hybrid'``) survive.

    Use this only where materializing the model default is what you want. For a field
    whose default is a non-None SENTINEL — ``DocIngestBody.category_id`` defaults to
    ``""``, which the contract distinguishes from "omitted" — pass the argument through
    verbatim instead: the generated ``to_dict`` excludes ``None``, so an explicit
    ``None`` is what keeps the key off the wire, while dropping the kwarg here would
    put the sentinel ON it.
    """
    return {k: v for k, v in kwargs.items() if v is not None}


def _task_finished(item: Any) -> bool:
    """Has this task reached a terminal state?

    Checks ``finished_at`` as well as the status enum on purpose. ``status`` is an
    open set on a response field — the gateway can add a terminal state the installed
    SDK has never heard of, and treating that as "still running" would make
    :meth:`EverOS.wait_task` spin until it times out. ``finished_at`` is documented as
    absent until the task is terminal, so it answers the question directly.
    """
    if getattr(item, "finished_at", None) is not None:
        return True
    return getattr(item, "status", None) in _TERMINAL_TASK_STATUS


def _purge_finished(job: Any) -> bool:
    """Has this purge job ended? Same rule as :func:`_task_finished`."""
    if getattr(job, "finished_at", None) is not None:
        return True
    return getattr(job, "status", None) in _TERMINAL_PURGE_STATUS


def _scope_text(scope: tuple) -> str:
    """``("project", "a1", "p1")`` -> ``"project a1/p1"``, for messages."""
    kind, app_id, project_id = scope
    ids = "/".join(x for x in (app_id, project_id) if x)
    return f"{kind} {ids}" if ids else str(kind)


def _purge_failure(job: Any) -> str:
    """The stores that failed, with their errors, for the exception message."""
    failed = [
        f"{getattr(s, 'store', '?')}: {getattr(s, 'error', None) or 'no reason given'}"
        for s in (getattr(job, "steps", None) or [])
        if getattr(s, "state", None) == "failed"
    ]
    return "; ".join(failed) or "no reason given"


class EverOSError(Exception):
    """Base class for every error raised by the EverOS facade."""


def _error_fields(body: Any) -> tuple[str | None, str | None]:
    """``(code, message)`` from an error body, or ``(None, None)``.

    The API answers errors in a few shapes: the memory engine's envelope
    ``{"request_id": ..., "error": {"code": ..., "message": ...}}``, a flat
    ``{"code": ..., "message": ...}`` from the gateway's own checks, and
    ``{"error": "<text>"}`` from its quota check (message only). Anything else
    (empty, not JSON, an HTML page from a proxy) yields ``None`` rather than raising:
    this runs while an error is already being reported.
    """
    if isinstance(body, (bytes, bytearray)):
        body = body.decode("utf-8", "replace")
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except ValueError:
            return None, None
    if not isinstance(body, Mapping):
        return None, None
    err = body.get("error")
    if isinstance(err, str):
        return None, err
    src = err if isinstance(err, Mapping) else body
    code, message = src.get("code"), src.get("message")
    return (code if isinstance(code, str) else None, message if isinstance(message, str) else None)


class EverOSAPIError(EverOSError):
    """A memory endpoint returned an HTTP error (wraps the SDK's ``ApiException``).

    ``status`` is the HTTP status and ``body`` the raw response body. ``code`` and
    ``message`` are read from the body when it carries them, so a caller can branch on
    the error rather than the status alone — e.g. ``"purge_in_progress"`` (a write
    during a purge: retry once it ends) versus another 409. Both are ``None`` when the
    body does not say.
    """

    def __init__(self, status: Any, body: Any = None) -> None:
        self.status = status
        self.body = body
        self.code, self.message = _error_fields(body)
        detail = f" code={self.code}" if self.code else ""
        super().__init__(f"EverOS API error: status={status}{detail}" + (f": {self.message}" if self.message else ""))


class EverOSStorageError(EverOSError):
    """The storage (object-sign) endpoint returned a non-zero business status."""

    def __init__(self, status: int, error: Any = None) -> None:
        super().__init__(f"EverOS storage error: status={status} error={error}")
        self.status = status
        self.error = error


class EverOS:
    """Ergonomic wrapper around the EverOS Cloud Memory API.

    ``timeout`` (seconds) applies to every request; override per client. Note the
    ergonomic defaults in :meth:`add`: a message without ``timestamp`` is stamped
    with the current time, and without ``sender_id`` defaults to its ``role`` — pass
    them explicitly when backfilling historical or multi-party conversations.
    """

    def __init__(
        self,
        api_key: str,
        *,
        host: str | None = None,
        app_id: str = "default",
        project_id: str = "default",
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:
        cfg = Configuration(access_token=api_key)
        if host:
            cfg.host = host
        self._api_client = ApiClient(cfg)
        # Escape hatches: the generated low-level clients, for anything the facade omits.
        self.memory = MemoryApi(self._api_client)
        self.storage = StorageApi(self._api_client)
        self.knowledge = KnowledgeApi(self._api_client)
        self.tasks = TasksApi(self._api_client)
        self._app_id = app_id
        self._project_id = project_id
        self._timeout = timeout

    def __getattr__(self, name: str) -> Any:
        """Point a generated method name at where it actually lives.

        Python calls this only after normal lookup fails, so it costs nothing on the
        happy path. Reads ``__dict__`` directly rather than ``getattr`` to stay safe
        during ``__init__`` and to avoid recursing through itself.
        """
        for attr in _API_ATTRS:
            api = self.__dict__.get(attr)
            if api is not None and hasattr(api, name):
                facade = _FACADE_FOR.get(name)
                hint = f"The facade covers it as `client.{facade}(...)`. " if facade else ""
                raise AttributeError(
                    f"{type(self).__name__!r} has no attribute {name!r} — that is a "
                    f"generated method name, not a facade one. {hint}"
                    f"The generated client is at `client.{attr}.{name}(...)`, which "
                    f"returns the response envelope rather than its `.data`."
                )
        raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")

    # -- lifecycle -----------------------------------------------------------
    def __enter__(self) -> "EverOS":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()

    def close(self) -> None:
        """Release pooled HTTP connections. (The generated ApiClient has no close().)"""
        pool = getattr(self._api_client.rest_client, "pool_manager", None)
        if pool is not None:
            pool.clear()

    # -- helpers -------------------------------------------------------------
    def _scope(self, app_id: str | None, project_id: str | None) -> dict:
        return {"app_id": app_id or self._app_id, "project_id": project_id or self._project_id}

    def _call(self, fn: Any, *args: Any, **kwargs: Any) -> Any:
        """Invoke a generated method with the client timeout, normalizing errors."""
        kwargs.setdefault("_request_timeout", self._timeout)
        try:
            return fn(*args, **kwargs)
        except ApiException as exc:  # pragma: no cover - exercised via integration
            raise EverOSAPIError(exc.status, getattr(exc, "body", None)) from exc

    @staticmethod
    def _to_message(m: MessageLike) -> MessageItem:
        if isinstance(m, MessageItem):
            return m
        m = dict(m)
        content = m.get("content")
        if not isinstance(content, Content):
            content = Content(content)
        role = m.get("role", "user")
        return MessageItem(
            **_clean(
                sender_id=m.get("sender_id") or role,
                sender_name=m.get("sender_name"),
                role=role,
                timestamp=m["timestamp"] if m.get("timestamp") is not None else int(time.time() * 1000),
                content=content,
                tool_calls=m.get("tool_calls"),
                tool_call_id=m.get("tool_call_id"),
            )
        )

    @staticmethod
    def _to_operation(op: Any) -> EditInputOperationsInner:
        if isinstance(op, EditInputOperationsInner):
            return op
        op = dict(op)
        cls = _OP_CLASSES.get(op.get("action"))
        if cls is None:
            raise ValueError(f"unknown edit operation action: {op.get('action')!r}")
        return EditInputOperationsInner(cls(**op))

    @staticmethod
    def _to_reason(reason: ReasonLike | None) -> Reason | None:
        """``"redundant"`` / ``{"code": ..., "note": ...}`` / ``Reason`` -> ``Reason``."""
        if reason is None or isinstance(reason, Reason):
            return reason
        if isinstance(reason, str):
            return Reason(code=reason)
        return Reason(**reason)

    @staticmethod
    def _to_content(content: ContentLike) -> ContentItem:
        """Coerce a document body into a ``ContentItem``.

        A plain string is the common case and becomes inline text. Pass a dict for
        anything else — notably an object already uploaded through :meth:`upload`,
        whose ``object_key`` is the ``uri``::

            {"type": "pdf", "uri": client.upload("handbook.pdf"), "name": "handbook.pdf"}
        """
        if isinstance(content, ContentItem):
            return content
        if isinstance(content, str):
            return ContentItem(type="text", text=content)
        return ContentItem(**dict(content))

    # -- memory --------------------------------------------------------------
    def add(
        self,
        session_id: str,
        messages: Sequence[MessageLike],
        *,
        mode: str | None = None,
        async_mode: bool | None = None,
        app_id: str | None = None,
        project_id: str | None = None,
    ) -> Any:
        """Add conversation messages to a session. Returns the ``AddData`` result."""
        payload = AddInput(
            **_clean(
                session_id=session_id,
                messages=[self._to_message(m) for m in messages],
                mode=mode,
                async_mode=async_mode,
                **self._scope(app_id, project_id),
            )
        )
        return self._call(self.memory.add_memory, payload).data

    def search(
        self,
        query: str,
        *,
        method: str | None = None,
        top_k: int | None = None,
        user_id: str | None = None,
        agent_id: str | None = None,
        include_profile: bool | None = None,
        min_score: float | None = None,
        radius: float | None = None,
        enable_llm_rerank: bool | None = None,
        filters: Any = None,
        app_id: str | None = None,
        project_id: str | None = None,
    ) -> Any:
        """Search memories (keyword / vector / hybrid / agentic). Returns ``SearchData``."""
        payload = SearchInput(
            **_clean(
                query=query,
                method=method,
                top_k=top_k,
                user_id=user_id,
                agent_id=agent_id,
                include_profile=include_profile,
                min_score=min_score,
                radius=radius,
                enable_llm_rerank=enable_llm_rerank,
                filters=filters,
                **self._scope(app_id, project_id),
            )
        )
        return self._call(self.memory.search_memory, payload).data

    def context(
        self,
        query: str,
        *,
        user_id: str,
        top_k: int | None = None,
        include_profile: bool | None = None,
        filters: Any = None,
        app_id: str | None = None,
        project_id: str | None = None,
    ) -> Any:
        """Context Retrieval: an LLM searches in rounds until the evidence suffices.

        Returns ``SearchData``, the same shape as :meth:`search` — memories, not an
        answer. ``episodes[].cited`` marks the ones the model's answer rested on, and
        ``score`` is a rank-fusion score, not comparable with search scores. User owners
        only. The server caps the loop at 45 s and returns what it found so far, which
        fits the client's default 60 s timeout; a client built with a shorter timeout
        should raise it for this call's sake.
        """
        payload = ContextInput(
            **_clean(
                query=query,
                user_id=user_id,
                top_k=top_k,
                include_profile=include_profile,
                filters=filters,
                **self._scope(app_id, project_id),
            )
        )
        return self._call(self.memory.retrieve_context, payload).data

    def get(
        self,
        memory_type: str,
        *,
        user_id: str | None = None,
        agent_id: str | None = None,
        page: int | None = None,
        page_size: int | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        filters: Any = None,
        app_id: str | None = None,
        project_id: str | None = None,
    ) -> Any:
        """Get memories (paginated) by type. Returns ``GetData``."""
        payload = GetInput(
            **_clean(
                memory_type=memory_type,
                user_id=user_id,
                agent_id=agent_id,
                page=page,
                page_size=page_size,
                sort_by=sort_by,
                sort_order=sort_order,
                filters=filters,
                **self._scope(app_id, project_id),
            )
        )
        return self._call(self.memory.get_memory, payload).data

    def flush(self, session_id: str, *, app_id: str | None = None, project_id: str | None = None) -> Any:
        """Force extraction for a session. Returns ``FlushData``."""
        payload = FlushInput(**_clean(session_id=session_id, **self._scope(app_id, project_id)))
        # Method name is being cleaned up (flush_api_v2_memory_flush_post -> flush_memory);
        # call whichever the installed SDK exposes so the facade survives the rename.
        fn = getattr(self.memory, "flush_memory", None) or self.memory.flush_api_v2_memory_flush_post
        return self._call(fn, payload).data

    def edit(
        self,
        user_id: str,
        operations: Sequence[Any],
        *,
        app_id: str | None = None,
        project_id: str | None = None,
    ) -> Any:
        """Bulk-edit a user's profile. ``operations`` are dicts (``action`` add/update/delete)."""
        payload = EditInput(
            **_clean(
                user_id=user_id,
                operations=[self._to_operation(op) for op in operations],
                **self._scope(app_id, project_id),
            )
        )
        return self._call(self.memory.edit_profile, payload).data

    def delete(
        self,
        *,
        user_id: str | None = None,
        agent_id: str | None = None,
        session_id: str | None = None,
        app_id: str | None = None,
        project_id: str | None = None,
    ) -> Any:
        """Scoped soft-delete of memories. Returns ``DeleteData``."""
        payload = DeleteInput(
            **_clean(
                user_id=user_id,
                agent_id=agent_id,
                session_id=session_id,
                **self._scope(app_id, project_id),
            )
        )
        return self._call(self.memory.delete_memory, payload).data

    # -- single-memory edits -------------------------------------------------
    # These target memories by id, so like the tag calls they carry NO app_id /
    # project_id and `_scope` does not apply. Facade names are the last segment of
    # the route: /memory/update -> update, /memory/delete_by_ids -> delete_by_ids,
    # /memory/feedback -> feedback.
    def update(
        self,
        memory_id: str,
        *,
        episode: str | None = None,
        summary: str | None = None,
        subject: str | None = None,
        reason: ReasonLike | None = None,
        user_id: str | None = None,
        memory_type: str = "episode",
    ) -> Any:
        """Patch one episode's ``episode`` text, ``summary`` and/or ``subject``.

        Only the fields you pass change (last write wins). ``reason`` is a code such as
        ``"wrong_subject"`` or ``{"code": ..., "note": ...}``. Returns ``UpdateData``,
        whose ``unchanged`` is true when the patch matched what was stored.

        ``user_id`` limits the edit to that user's memory: a memory owned by anyone else
        is a 404, exactly like a missing one. In an agent tool, set it from your own
        session (the signed-in user), never from model output, so a wrong or invented
        ``memory_id`` cannot reach another user's memory.

        Profile items are edited with :meth:`edit`, not here.
        """
        patch = _clean(episode=episode, summary=summary, subject=subject)
        if not patch:
            raise ValueError("update needs at least one of episode / summary / subject")
        payload = UpdateInput(
            **_clean(
                memory_type=memory_type,
                memory_id=memory_id,
                patch=EpisodePatch(**patch),
                reason=self._to_reason(reason),
                user_id=user_id,
            )
        )
        return self._call(self.memory.update_memory, payload).data

    def delete_by_ids(
        self,
        memory_ids: Sequence[str],
        *,
        reason: ReasonLike | None = None,
        user_id: str | None = None,
        memory_type: str = "episode",
    ) -> Any:
        """Soft-delete 1-50 memories by id. Returns ``DeleteByIdsData``.

        Ids that do not exist are skipped; one malformed id fails the whole batch (422).
        ``deleted`` on the result counts what this call removed, so a 0 means nothing
        was. ``user_id`` deletes only that user's memories: ids owned by anyone else are
        skipped like missing ones. As with :meth:`update`, set it from your own session,
        never from model output. To clear a whole user / agent / session, use
        :meth:`delete`.
        """
        payload = DeleteByIdsInput(
            **_clean(
                memory_type=memory_type,
                memory_ids=list(memory_ids),
                reason=self._to_reason(reason),
                user_id=user_id,
            )
        )
        return self._call(self.memory.delete_memories_by_ids, payload).data

    def feedback(
        self,
        memory_id: str,
        rating: str,
        *,
        reason: str | None = None,
        note: str | None = None,
        suggestion: str | None = None,
        item_id: str | None = None,
        memory_type: str = "episode",
    ) -> Any:
        """Rate a memory ``"positive"`` or ``"negative"``. Returns ``FeedbackData``.

        ``reason`` (a code such as ``"outdated"``), ``note`` and ``suggestion`` go with a
        negative rating only. ``item_id`` names the item inside a profile memory. This
        only records the rating — nothing is edited; use :meth:`update` /
        :meth:`delete_by_ids` to change the memory itself.
        """
        payload = FeedbackInput(
            **_clean(
                memory_type=memory_type,
                memory_id=memory_id,
                item_id=item_id,
                rating=rating,
                reason=reason,
                note=note,
                suggestion=suggestion,
            )
        )
        return self._call(self.memory.submit_feedback, payload).data

    # -- memory tags ---------------------------------------------------------
    # Tag calls carry NO app_id / project_id: the scope of a tag operation is the
    # memory ids themselves, so `_scope` deliberately does not apply here.
    def tag_bind(self, memory_type: str, memory_ids: Sequence[str], tags: Sequence[str]) -> Any:
        """Add ``tags`` to the given memories, keeping the tags they already carry."""
        payload = TagBindInput(memory_type=memory_type, memory_ids=list(memory_ids), tags=list(tags))
        return self._call(self.memory.bind_tags, payload).data

    def tag_unbind(self, memory_type: str, memory_ids: Sequence[str], tags: Sequence[str]) -> Any:
        """Remove ``tags`` from the given memories, leaving their other tags in place."""
        payload = TagUnbindInput(memory_type=memory_type, memory_ids=list(memory_ids), tags=list(tags))
        return self._call(self.memory.unbind_tags, payload).data

    def tag_replace(self, memory_type: str, memory_ids: Sequence[str], tags: Sequence[str]) -> Any:
        """Overwrite the given memories' tags with ``tags`` — existing tags are dropped."""
        payload = TagReplaceInput(memory_type=memory_type, memory_ids=list(memory_ids), tags=list(tags))
        return self._call(self.memory.replace_tags, payload).data

    # -- knowledge base ------------------------------------------------------
    # Knowledge calls are scoped by `kb_id` in the path, not by app_id / project_id —
    # those fields do not exist on any knowledge request body. Categories and topics
    # are lower-traffic; reach them through `client.knowledge`.
    def kb_create(self, name: str, *, description: str | None = None, owner_id: str | None = None) -> Any:
        """Create a knowledge base. Returns ``KbData``."""
        # Two different rules in one call, both about keeping unset fields OFF the wire:
        # `description` is non-nullable with a "" default, so it must be passed through —
        # an explicit None is excluded by to_dict, while dropping the kwarg would send "".
        # `owner_id` IS nullable, so to_dict keeps an explicitly-set None as `null`; there
        # the kwarg has to be dropped instead. The contract says "omit" for both.
        payload = KbCreateInput(name=name, description=description, **_clean(owner_id=owner_id))
        return self._call(self.knowledge.create_knowledge_base, payload).data

    def kb_list(
        self,
        *,
        page: int | None = None,
        page_size: int | None = None,
        owner_id: str | None = None,
    ) -> Any:
        """List knowledge bases (paginated). Returns ``KbListData``."""
        return self._call(
            self.knowledge.list_knowledge_bases,
            **_clean(page=page, page_size=page_size, owner_id=owner_id),
        ).data

    def kb_get(self, kb_id: str) -> Any:
        """Get one knowledge base. Returns ``KbData``."""
        return self._call(self.knowledge.get_knowledge_base, kb_id).data

    def kb_update(self, kb_id: str, *, name: str | None = None, description: str | None = None) -> Any:
        """Patch a knowledge base's name / description. Returns ``KbData``."""
        payload = KbPatchBody(**_clean(name=name, description=description))
        return self._call(self.knowledge.update_knowledge_base, kb_id, payload).data

    def kb_delete(self, kb_id: str) -> Any:
        """Delete a knowledge base and everything in it. Returns ``KbDeleteData``."""
        return self._call(self.knowledge.delete_knowledge_base, kb_id).data

    def kb_search(
        self,
        kb_id: str,
        query: str,
        *,
        method: str | None = None,
        top_k: int | None = None,
        score_threshold: float | None = None,
        include: Any = None,
        filters: Any = None,
    ) -> Any:
        """Search one knowledge base. Returns ``KbSearchData``."""
        payload = SearchBody(
            **_clean(
                query=query,
                method=method,
                top_k=top_k,
                score_threshold=score_threshold,
                include=include,
                filters=filters,
            )
        )
        return self._call(self.knowledge.search_knowledge, kb_id, payload).data

    def doc_ingest(
        self,
        kb_id: str,
        title: str,
        content: ContentLike,
        *,
        category_id: str | None = None,
        doc_id: str | None = None,
    ) -> Any:
        """Ingest a document — create one, or replace ``doc_id`` in place if given.

        ``content`` takes a plain string for inline text, or a dict for any other
        media (see :meth:`_to_content`). Omit ``category_id`` to let the server
        auto-classify.

        Ingest is ALWAYS asynchronous: the gateway validates, enqueues, and answers
        202 with ``status='queued'`` and a ``task_id``. The document id is minted
        downstream, so it is NOT in this response — pass the ``task_id`` to
        :meth:`task_wait` to follow the work, e.g.::

            ack = client.doc_ingest(kb_id, "Handbook", text)
            task = client.task_wait(ack.task_id)

        Returns ``DocIngestData`` (``status`` + ``task_id``).
        """
        # category_id is passed through rather than `_clean`ed: its model default is
        # "", and the contract reads "omit for LLM auto-classify" — so an unset category
        # must leave the key OFF the wire, which an explicit None does and dropping the
        # kwarg does not.
        payload = DocIngestBody(
            title=title, content=self._to_content(content), category_id=category_id
        )
        if doc_id is not None:
            return self._call(self.knowledge.replace_document, kb_id, doc_id, payload).data
        return self._call(self.knowledge.create_document, kb_id, payload).data

    def doc_list(
        self,
        kb_id: str,
        *,
        category_id: str | None = None,
        page: int | None = None,
        page_size: int | None = None,
    ) -> Any:
        """List a knowledge base's documents (paginated). Returns ``DocListData``."""
        return self._call(
            self.knowledge.list_documents,
            kb_id,
            **_clean(category_id=category_id, page=page, page_size=page_size),
        ).data

    def doc_get(self, kb_id: str, doc_id: str) -> Any:
        """Get one document. Returns ``DocData``."""
        return self._call(self.knowledge.get_document, kb_id, doc_id).data

    def doc_update(
        self,
        kb_id: str,
        doc_id: str,
        *,
        title: str | None = None,
        category_id: str | None = None,
    ) -> Any:
        """Patch a document's title / category — metadata only, no re-ingest.

        To change a document's CONTENT, call :meth:`doc_ingest` with ``doc_id``:
        that replaces it and re-runs extraction asynchronously.
        """
        fields = _clean(title=title, category_id=category_id)
        if not fields:
            raise ValueError("update_document needs at least one of title / category_id")
        payload = DocPatchBody(**fields)
        return self._call(self.knowledge.update_document, kb_id, doc_id, payload).data

    def doc_delete(self, kb_id: str, doc_id: str) -> Any:
        """Delete one document and its derived topics. Returns ``DocDeleteData``."""
        return self._call(self.knowledge.delete_document, kb_id, doc_id).data

    # -- async tasks ---------------------------------------------------------
    def task_get(self, task_id: str) -> Any:
        """Read one async task's status. Returns ``TaskItem``."""
        return self._call(self.tasks.get_task_status, task_id).data

    def task_list(
        self,
        *,
        page: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        session_id: str | None = None,
        start: Any = None,
        end: Any = None,
    ) -> Any:
        """List async tasks (paginated, filterable). Returns the list data."""
        return self._call(
            self.tasks.list_tasks,
            **_clean(
                page=page,
                page_size=page_size,
                status=status,
                session_id=session_id,
                start=start,
                end=end,
            ),
        ).data

    def task_wait(
        self,
        task_id: str,
        *,
        timeout: float = DEFAULT_TASK_TIMEOUT,
        interval: float = DEFAULT_TASK_INTERVAL,
        max_interval: float = DEFAULT_TASK_MAX_INTERVAL,
        raise_on_failure: bool = True,
    ) -> Any:
        """Poll ``task_id`` until it finishes and return the terminal ``TaskItem``.

        Backs off from ``interval`` up to ``max_interval`` between polls, so a slow
        ingest costs a handful of requests rather than one every ``interval`` for the
        whole ``timeout`` window. Transient failures (429 / 5xx) are retried on the
        same schedule instead of aborting the wait — the caller cannot resume a wait
        that dies halfway, so a rate-limit blip must not end it.

        Raises ``EverOSError`` if the task fails (unless ``raise_on_failure=False``,
        which returns the failed item instead) or if it is still unfinished at
        ``timeout``; the last ``TaskItem`` seen, if any, is on the error's ``.task``.
        A non-transient HTTP error propagates as ``EverOSAPIError``, as does a
        transient one that outlives the deadline.
        """
        item = self._poll(
            lambda: self.task_get(task_id),
            _task_finished,
            what=f"task {task_id}",
            attr="task",
            timeout=timeout,
            interval=interval,
            max_interval=max_interval,
        )
        if raise_on_failure and getattr(item, "status", None) == "failed":
            reason = getattr(item, "error", None) or getattr(item, "error_code", None) or "no reason given"
            err = EverOSError(f"task {task_id} failed: {reason}")
            err.task = item
            raise err
        return item

    def _poll(
        self,
        fetch: Any,
        finished: Any,
        *,
        what: str,
        attr: str,
        timeout: float,
        interval: float,
        max_interval: float,
    ) -> Any:
        """Call ``fetch`` until ``finished(item)``, with backoff; the loop behind every wait.

        Backs off from ``interval`` up to ``max_interval``. A transient failure (429 /
        5xx) is retried on the same schedule; any other HTTP error, or a transient one
        past the deadline, propagates as ``EverOSAPIError``. Still unfinished at
        ``timeout`` raises ``EverOSError`` with the last item seen on ``err.<attr>``.
        """
        deadline = time.monotonic() + timeout
        delay = interval
        item = None
        while True:
            try:
                item = fetch()
            except EverOSAPIError as exc:
                # Out of budget, or not the kind of failure that will pass: give up.
                if exc.status not in _TRANSIENT_STATUS or time.monotonic() >= deadline:
                    raise
            else:
                if finished(item):
                    return item
                if time.monotonic() >= deadline:
                    err = EverOSError(
                        f"{what} still {getattr(item, 'status', 'unknown')!r} after {timeout}s"
                    )
                    setattr(err, attr, item)
                    raise err
            time.sleep(delay)
            delay = min(delay * 2, max_interval) if delay else delay

    # -- memory-space purge --------------------------------------------------
    # Permanent: there is no undo. The API makes a purge two calls on purpose (a nonce
    # from step 1, confirmed within 5 minutes) so that one mistaken call cannot wipe a
    # memory space, and the facade keeps them two: there is deliberately no one-call
    # purge. For the same reason the scope ids never come from the client's
    # app_id / project_id defaults: what gets purged is always written at the call site.
    def purge_request(
        self,
        scope: str,
        *,
        app_id: str | None = None,
        project_id: str | None = None,
    ) -> Any:
        """Step 1 of 2: ask to purge. **Deletes nothing.** Returns ``PurgeRequestData``.

        ``scope`` is ``"space"`` (the whole memory space of this API key), ``"app"``
        (pass ``app_id``) or ``"project"`` (pass ``app_id`` and ``project_id``); each
        takes exactly its own ids, and a missing or extra one is a 422. The result's
        ``summary`` counts what would be deleted right now; check it, then pass the
        result (or its ``nonce``) to :meth:`purge_confirm` before ``expires_at``
        (5 minutes). Counting can take up to about 30 seconds on a large memory space;
        a count that did not finish is ``None`` and ``summary.complete`` is false, so
        check ``complete`` before trusting the numbers.
        """
        payload = PurgeRequestInput(**_clean(scope=scope, app_id=app_id, project_id=project_id))
        return self._call(self.memory.request_purge, payload).data

    def purge_confirm(self, request: PurgeRequestData | str) -> Any:
        """Step 2 of 2: start the purge. **Permanent.** Returns the queued ``PurgeJobData``.

        Pass the result of :meth:`purge_request` (recommended) or just its ``nonce``.
        The scope is the one the nonce was issued for. The nonce works once, only with
        the same API key; an unknown, expired or used one is a 404 and nothing happens.
        Until the job ends, every write to the memory space is a 409. Follow it with
        :meth:`purge_wait` or :meth:`purge_get`.

        Only one purge runs per memory space. Confirming while one is queued or running
        uses up the nonce and returns THAT job, whatever its scope, without queuing
        yours. Given the request result, this method checks the returned job against
        the scope you asked for and raises ``EverOSError`` (the running job on
        ``.job``) when they differ: wait for it to end, then call :meth:`purge_request`
        again. Given a bare nonce it cannot tell, so compare ``job.scope`` yourself.
        """
        nonce = request if isinstance(request, str) else getattr(request, "nonce", None)
        if not isinstance(nonce, str):
            raise TypeError("purge_confirm takes the purge_request() result or its nonce string")
        job = self._call(self.memory.confirm_purge, PurgeConfirmInput(nonce=nonce)).data
        if not isinstance(request, str):
            asked = (request.scope, getattr(request, "app_id", None), getattr(request, "project_id", None))
            got = (getattr(job, "scope", None), getattr(job, "app_id", None), getattr(job, "project_id", None))
            if got != asked:
                err = EverOSError(
                    f"another purge is already {getattr(job, 'status', 'running')!r} in this "
                    f"memory space (job {getattr(job, 'job_id', '?')}, scope {_scope_text(got)}); "
                    f"yours ({_scope_text(asked)}) was not queued and its nonce is used up. "
                    "Wait for that job to end, then call purge_request again."
                )
                err.job = job
                raise err
        return job

    def purge_get(self, job_id: str) -> Any:
        """Read a purge job. Returns ``PurgeJobData`` (``status``, per-store ``steps``)."""
        return self._call(self.memory.get_purge_job, job_id).data

    def purge_wait(
        self,
        job_id: str,
        *,
        timeout: float = DEFAULT_PURGE_TIMEOUT,
        interval: float = DEFAULT_TASK_INTERVAL,
        max_interval: float = DEFAULT_TASK_MAX_INTERVAL,
        raise_on_failure: bool = True,
    ) -> Any:
        """Poll a purge job until it ends and return the terminal ``PurgeJobData``.

        Same polling as :meth:`task_wait`. Raises ``EverOSError`` naming the failed
        stores if the job fails (unless ``raise_on_failure=False``, which returns it), or
        if it is still running at ``timeout``; the last job seen is on the error's
        ``.job``. Timing out only ends the wait, not the purge, which keeps running on
        the server (it fails on its own only after repeated retries, within about two
        hours): call ``purge_wait`` again to keep waiting. A purge that failed partway
        stays partly done: request a new one.
        """
        job = self._poll(
            lambda: self.purge_get(job_id),
            _purge_finished,
            what=f"purge {job_id}",
            attr="job",
            timeout=timeout,
            interval=interval,
            max_interval=max_interval,
        )
        if raise_on_failure and getattr(job, "status", None) == "failed":
            err = EverOSError(f"purge {job_id} failed: {_purge_failure(job)}")
            err.job = job
            raise err
        return job

    # -- storage -------------------------------------------------------------
    def presign(self, objects: Sequence[Any]) -> Any:
        """Presign objects for direct-to-S3 upload (advanced/batch, up to 50).

        Returns the ``SignResponse`` data; raises ``EverOSStorageError`` on a
        non-zero business status. Most callers want :meth:`upload` instead.
        """
        items = [o if isinstance(o, SignObjectItem) else SignObjectItem(**o) for o in objects]
        envelope = self._call(self.storage.sign_objects, SignRequest(object_list=items))
        if envelope.status != 0:
            raise EverOSStorageError(envelope.status, getattr(envelope, "error", None))
        return envelope.result.data

    def upload(
        self,
        path: str,
        *,
        file_type: str | None = None,
        file_id: str | None = None,
        file_name: str | None = None,
    ) -> str:
        """Upload a local file end to end and return its ``object_key``.

        Presigns the object, POSTs the bytes straight to S3, and returns the
        ``object_key`` you then reference in a message's multimodal content.
        ``file_type`` (image / file / video) is inferred from the extension if omitted.
        The whole file is read into memory — fine for images/docs, mind large videos.
        """
        file_name = file_name or os.path.basename(path)
        file_id = file_id or file_name
        file_type = file_type or _guess_file_type(file_name)
        with open(path, "rb") as fh:
            body = fh.read()

        data = self.presign([{"file_id": file_id, "file_name": file_name, "file_type": file_type}])
        obj = data.object_list[0]
        signed = obj.object_signed_info

        status = self._s3_post(signed.url, dict(signed.fields), file_name, body, self._timeout)
        if status not in (200, 201, 204):
            raise EverOSStorageError(status, "direct-to-S3 upload failed")
        return obj.object_key

    @staticmethod
    def _s3_post(url: str, fields: dict, filename: str, body: bytes, timeout: float = DEFAULT_TIMEOUT) -> int:
        """POST a presigned multipart form to S3. The ``file`` field must come last."""
        content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
        form = dict(fields)
        form["file"] = (filename, body, content_type)  # urllib3: (filename, data, content_type)
        resp = urllib3.PoolManager().request("POST", url, fields=form, timeout=timeout)
        return resp.status
