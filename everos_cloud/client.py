"""High-level ergonomic client for the EverOS Cloud Memory API.

A thin, hand-maintained facade over the generated ``MemoryApi`` / ``StorageApi``:
plain kwargs / dicts in, response ``.data`` out. The generated typed client stays
available via ``client.memory`` / ``client.storage`` for full control.

    from everos_cloud import EverOS

    client = EverOS(api_key="sk-...")
    client.add(session_id="s1", messages=[{"role": "user", "content": "I love hiking"}])
    hits = client.search("outdoor hobbies")

Errors: every failure raised by this facade derives from :class:`EverOSError` —
``EverOSAPIError`` for memory HTTP errors, ``EverOSStorageError`` for object-upload
failures.
"""
from __future__ import annotations

import mimetypes
import os
import time
from typing import Any, Mapping, Sequence, Union

import urllib3

from everos_cloud import ApiClient, Configuration, MemoryApi, StorageApi
from everos_cloud.exceptions import ApiException
from everos_cloud.models import (
    AddInput,
    AddOperation,
    Content,
    DeleteInput,
    DeleteOperation,
    EditInput,
    EditInputOperationsInner,
    FlushInput,
    GetInput,
    MessageItem,
    SearchInput,
    SignObjectItem,
    SignRequest,
    UpdateOperation,
)

__all__ = ["EverOS", "EverOSError", "EverOSAPIError", "EverOSStorageError"]

DEFAULT_TIMEOUT = 60.0  # seconds; agentic search / LLM rerank can be slow

_OP_CLASSES = {"add": AddOperation, "update": UpdateOperation, "delete": DeleteOperation}

_IMAGE_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"}
_VIDEO_EXT = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v"}

MessageLike = Union[MessageItem, Mapping[str, Any]]


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
