"""High-level ergonomic client for the EverOS Cloud Memory API.

A thin, hand-maintained facade over the generated API clients: plain kwargs / dicts
in, response ``.data`` out. Every generated client stays available for full control —
``client.memory``, ``client.storage``, ``client.knowledge``, ``client.tasks`` — and the
facade covers the high-traffic calls of each.

    from everos_cloud import EverOS

    client = EverOS(api_key="sk-...")
    client.add(session_id="s1", messages=[{"role": "user", "content": "I love hiking"}])
    hits = client.search("outdoor hobbies")

Errors: every failure raised by this facade derives from :class:`EverOSError` —
``EverOSAPIError`` for HTTP errors, ``EverOSStorageError`` for object-upload failures,
and a plain ``EverOSError`` for a task that fails or outlives its wait timeout.
"""
from __future__ import annotations

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
    DeleteInput,
    DeleteOperation,
    DocIngestBody,
    DocPatchBody,
    EditInput,
    EditInputOperationsInner,
    FlushInput,
    GetInput,
    KbCreateInput,
    KbPatchBody,
    MessageItem,
    SearchBody,
    SearchInput,
    SignObjectItem,
    SignRequest,
    TagBindInput,
    TagReplaceInput,
    TagUnbindInput,
    UpdateOperation,
)

__all__ = ["EverOS", "EverOSError", "EverOSAPIError", "EverOSStorageError"]

DEFAULT_TIMEOUT = 60.0  # seconds; agentic search / LLM rerank can be slow
DEFAULT_TASK_TIMEOUT = 300.0  # seconds to wait for an async task before giving up
DEFAULT_TASK_INTERVAL = 2.0  # seconds between task polls

# Statuses the gateway reports as finished. Deliberately paired with a `finished_at`
# check in `_task_finished`: `status` is an OPEN set on a response field (a new
# terminal state such as `cancelled` must not make `wait_task` spin until timeout),
# and the contract documents `finished_at` as "absent while the task is not in a
# terminal state" — so the timestamp, not the enum, is the load-bearing signal.
_TERMINAL_TASK_STATUS = frozenset({"success", "failed"})

_OP_CLASSES = {"add": AddOperation, "update": UpdateOperation, "delete": DeleteOperation}

_IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"}
_VIDEO_EXT = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v"}

MessageLike = Union[MessageItem, Mapping[str, Any]]
ContentLike = Union[ContentItem, Mapping[str, Any], str]


def _guess_file_type(name: str) -> str:
    ext = os.path.splitext(name)[1].lower()
    if ext in _IMAGE_EXT:
        return "image"
    if ext in _VIDEO_EXT:
        return "video"
    return "file"


def _clean(**kwargs: Any) -> dict:
    """Drop ``None`` values so model defaults (e.g. search ``method='hybrid'``) survive."""
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


class EverOSError(Exception):
    """Base class for every error raised by the EverOS facade."""


class EverOSAPIError(EverOSError):
    """A memory endpoint returned an HTTP error (wraps the SDK's ``ApiException``)."""

    def __init__(self, status: Any, body: Any = None) -> None:
        super().__init__(f"EverOS API error: status={status}")
        self.status = status
        self.body = body


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

    # -- memory tags ---------------------------------------------------------
    # Tag calls carry NO app_id / project_id: the scope of a tag operation is the
    # memory ids themselves, so `_scope` deliberately does not apply here.
    def bind_tags(self, memory_type: str, memory_ids: Sequence[str], tags: Sequence[str]) -> Any:
        """Add ``tags`` to the given memories, keeping the tags they already carry."""
        payload = TagBindInput(memory_type=memory_type, memory_ids=list(memory_ids), tags=list(tags))
        return self._call(self.memory.bind_tags, payload).data

    def unbind_tags(self, memory_type: str, memory_ids: Sequence[str], tags: Sequence[str]) -> Any:
        """Remove ``tags`` from the given memories, leaving their other tags in place."""
        payload = TagUnbindInput(memory_type=memory_type, memory_ids=list(memory_ids), tags=list(tags))
        return self._call(self.memory.unbind_tags, payload).data

    def replace_tags(self, memory_type: str, memory_ids: Sequence[str], tags: Sequence[str]) -> Any:
        """Overwrite the given memories' tags with ``tags`` — existing tags are dropped."""
        payload = TagReplaceInput(memory_type=memory_type, memory_ids=list(memory_ids), tags=list(tags))
        return self._call(self.memory.replace_tags, payload).data

    # -- knowledge base ------------------------------------------------------
    # Knowledge calls are scoped by `kb_id` in the path, not by app_id / project_id —
    # those fields do not exist on any knowledge request body. Categories and topics
    # are lower-traffic; reach them through `client.knowledge`.
    def create_kb(self, name: str, *, description: str | None = None, owner_id: str | None = None) -> Any:
        """Create a knowledge base. Returns ``KbData``."""
        payload = KbCreateInput(**_clean(name=name, description=description, owner_id=owner_id))
        return self._call(self.knowledge.create_knowledge_base, payload).data

    def list_kbs(
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

    def get_kb(self, kb_id: str) -> Any:
        """Get one knowledge base. Returns ``KbData``."""
        return self._call(self.knowledge.get_knowledge_base, kb_id).data

    def update_kb(self, kb_id: str, *, name: str | None = None, description: str | None = None) -> Any:
        """Patch a knowledge base's name / description. Returns ``KbData``."""
        payload = KbPatchBody(**_clean(name=name, description=description))
        return self._call(self.knowledge.update_knowledge_base, kb_id, payload).data

    def delete_kb(self, kb_id: str) -> Any:
        """Delete a knowledge base and everything in it. Returns ``KbDeleteData``."""
        return self._call(self.knowledge.delete_knowledge_base, kb_id).data

    def search_kb(
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

    def ingest_document(
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
        :meth:`wait_task` to follow the work, e.g.::

            ack = client.ingest_document(kb_id, "Handbook", text)
            task = client.wait_task(ack.task_id)

        Returns ``DocIngestData`` (``status`` + ``task_id``).
        """
        payload = DocIngestBody(
            **_clean(title=title, content=self._to_content(content), category_id=category_id)
        )
        if doc_id is not None:
            return self._call(self.knowledge.replace_document, kb_id, doc_id, payload).data
        return self._call(self.knowledge.create_document, kb_id, payload).data

    def list_documents(
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

    def get_document(self, kb_id: str, doc_id: str) -> Any:
        """Get one document. Returns ``DocData``."""
        return self._call(self.knowledge.get_document, kb_id, doc_id).data

    def update_document(
        self,
        kb_id: str,
        doc_id: str,
        *,
        title: str | None = None,
        category_id: str | None = None,
    ) -> Any:
        """Patch a document's title / category — metadata only, no re-ingest.

        To change a document's CONTENT, call :meth:`ingest_document` with ``doc_id``:
        that replaces it and re-runs extraction asynchronously.
        """
        payload = DocPatchBody(**_clean(title=title, category_id=category_id))
        return self._call(self.knowledge.update_document, kb_id, doc_id, payload).data

    def delete_document(self, kb_id: str, doc_id: str) -> Any:
        """Delete one document and its derived topics. Returns ``DocDeleteData``."""
        return self._call(self.knowledge.delete_document, kb_id, doc_id).data

    # -- async tasks ---------------------------------------------------------
    def task(self, task_id: str) -> Any:
        """Read one async task's status. Returns ``TaskItem``."""
        return self._call(self.tasks.get_task_status, task_id).data

    def list_tasks(
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

    def wait_task(
        self,
        task_id: str,
        *,
        timeout: float = DEFAULT_TASK_TIMEOUT,
        interval: float = DEFAULT_TASK_INTERVAL,
        raise_on_failure: bool = True,
    ) -> Any:
        """Poll ``task_id`` until it finishes and return the terminal ``TaskItem``.

        Raises ``EverOSError`` if the task fails (unless ``raise_on_failure=False``,
        which returns the failed item instead) or if it is still running after
        ``timeout`` seconds. The raised error carries the last ``TaskItem`` seen on
        its ``.task`` attribute.
        """
        deadline = time.monotonic() + timeout
        item = None
        while True:
            item = self.task(task_id)
            if _task_finished(item):
                break
            if time.monotonic() >= deadline:
                err = EverOSError(
                    f"task {task_id} still {getattr(item, 'status', 'unknown')!r} "
                    f"after {timeout}s"
                )
                err.task = item
                raise err
            time.sleep(interval)

        if raise_on_failure and getattr(item, "status", None) == "failed":
            reason = getattr(item, "error", None) or getattr(item, "error_code", None) or "no reason given"
            err = EverOSError(f"task {task_id} failed: {reason}")
            err.task = item
            raise err
        return item

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
