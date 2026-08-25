"""Offline unit tests for the EverOS facade — the API layer is mocked, no network."""
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from everos_cloud import EverOS, EverOSAPIError, EverOSError, EverOSStorageError
from everos_cloud.exceptions import ApiException
from everos_cloud.models import (
    AddInput,
    DocIngestBody,
    DocIngestData,
    EditInput,
    KbCreateInput,
    KbPatchBody,
    MessageItem,
    SearchBody,
    SearchInput,
    TagBindInput,
    TagReplaceInput,
    TagUnbindInput,
)


def _client(memory=None, storage=None, knowledge=None, tasks=None):
    c = EverOS("sk-test")
    if memory is not None:
        c.memory = memory
    if storage is not None:
        c.storage = storage
    if knowledge is not None:
        c.knowledge = knowledge
    if tasks is not None:
        c.tasks = tasks
    return c


def test_add_builds_payload_and_returns_data():
    mem = MagicMock()
    mem.add_memory.return_value = SimpleNamespace(data="ADD_RESULT")
    c = _client(memory=mem)

    out = c.add(session_id="s1", messages=[{"role": "user", "content": "I love hiking"}])

    assert out == "ADD_RESULT"
    payload = mem.add_memory.call_args.args[0]
    assert isinstance(payload, AddInput)
    assert payload.session_id == "s1"
    assert payload.app_id == "default" and payload.project_id == "default"
    msg = payload.messages[0]
    assert isinstance(msg, MessageItem)
    assert msg.role == "user"
    assert msg.sender_id == "user"          # defaults to role when omitted
    assert msg.timestamp >= 1_000_000_000_000   # defaults to now, in unix milliseconds
    # string content shorthand became a Content wrapper
    assert msg.content is not None


def test_message_passthrough_and_explicit_fields():
    mem = MagicMock()
    mem.add_memory.return_value = SimpleNamespace(data=None)
    c = _client(memory=mem)
    c.add(session_id="s1", messages=[
        {"sender_id": "u9", "role": "assistant", "timestamp": 1700000000000, "content": "hi"},
    ])
    msg = mem.add_memory.call_args.args[0].messages[0]
    assert msg.sender_id == "u9" and msg.role == "assistant" and msg.timestamp == 1700000000000


def test_search_drops_none_so_defaults_survive():
    mem = MagicMock()
    mem.search_memory.return_value = SimpleNamespace(data="S")
    c = _client(memory=mem)

    assert c.search("outdoor hobbies") == "S"
    payload = mem.search_memory.call_args.args[0]
    assert isinstance(payload, SearchInput)
    assert payload.query == "outdoor hobbies"
    assert payload.method == "hybrid"       # model default preserved (not overwritten with None)


def test_get_and_delete():
    mem = MagicMock()
    mem.get_memory.return_value = SimpleNamespace(data="G")
    mem.delete_memory.return_value = SimpleNamespace(data="D")
    c = _client(memory=mem)

    assert c.get("episode", page=2) == "G"
    assert mem.get_memory.call_args.args[0].memory_type == "episode"
    assert mem.get_memory.call_args.args[0].page == 2

    assert c.delete(user_id="u1", session_id="s1") == "D"
    dp = mem.delete_memory.call_args.args[0]
    assert dp.user_id == "u1" and dp.session_id == "s1"


def test_edit_wraps_operations():
    mem = MagicMock()
    mem.edit_profile.return_value = SimpleNamespace(data="E")
    c = _client(memory=mem)

    c.edit("u1", [{"action": "add", "type": "explicit_info",
                   "data": {"category": "hobby", "description": "hiking"}, "reason": "x"}])
    payload = mem.edit_profile.call_args.args[0]
    assert isinstance(payload, EditInput)
    assert payload.user_id == "u1"
    assert len(payload.operations) == 1


def test_edit_rejects_unknown_action():
    c = _client(memory=MagicMock())
    with pytest.raises(ValueError):
        c.edit("u1", [{"action": "nope", "type": "explicit_info", "data": {}}])


def test_flush_prefers_flush_memory_when_present():
    calls = {}

    def new_flush(p, **kw):
        calls["new"] = p
        return SimpleNamespace(data="NEW")

    def old_flush(p, **kw):
        calls["old"] = p
        return SimpleNamespace(data="OLD")

    mem = SimpleNamespace(flush_memory=new_flush, flush_api_v2_memory_flush_post=old_flush)
    assert _client(memory=mem).flush("s1") == "NEW"
    assert "new" in calls and "old" not in calls


def test_flush_falls_back_to_generated_name():
    mem = SimpleNamespace(
        flush_api_v2_memory_flush_post=lambda p, **kw: SimpleNamespace(data="OLD"),
    )
    assert _client(memory=mem).flush("s1") == "OLD"


def test_presign_success_returns_data():
    storage = MagicMock()
    storage.sign_objects.return_value = SimpleNamespace(status=0, result=SimpleNamespace(data="SIGNED"))
    c = _client(storage=storage)
    assert c.presign([{"file_id": "f1", "file_name": "a.jpg", "file_type": "image"}]) == "SIGNED"


def test_presign_raises_on_business_error():
    storage = MagicMock()
    storage.sign_objects.return_value = SimpleNamespace(status=2018, error="validation failed")
    c = _client(storage=storage)
    with pytest.raises(EverOSStorageError) as ei:
        c.presign([{"file_id": "f1", "file_name": "a.jpg", "file_type": "image"}])
    assert ei.value.status == 2018


def test_custom_scope_defaults_propagate():
    mem = MagicMock()
    mem.add_memory.return_value = SimpleNamespace(data=None)
    c = EverOS("sk-test", app_id="myapp", project_id="proj")
    c.memory = mem
    c.add(session_id="s1", messages=[{"role": "user", "content": "hi"}])
    payload = mem.add_memory.call_args.args[0]
    assert payload.app_id == "myapp" and payload.project_id == "proj"


def _signed_envelope(object_key="k1", url="https://s3.example/upload", fields=None):
    signed = SimpleNamespace(url=url, fields=fields or {"key": "abc", "policy": "xyz"}, max_size=100)
    obj = SimpleNamespace(object_key=object_key, object_signed_info=signed)
    return SimpleNamespace(status=0, result=SimpleNamespace(data=SimpleNamespace(object_list=[obj])))


def test_upload_end_to_end(tmp_path):
    storage = MagicMock()
    storage.sign_objects.return_value = _signed_envelope(object_key="obj-123")
    c = _client(storage=storage)
    captured = {}

    def fake_post(url, fields, filename, body, timeout=None):
        captured.update(url=url, fields=fields, filename=filename, body=body, timeout=timeout)
        return 204

    c._s3_post = fake_post
    f = tmp_path / "photo.jpg"
    f.write_bytes(b"BYTES")

    key = c.upload(str(f))

    assert key == "obj-123"
    req = storage.sign_objects.call_args.args[0]
    assert req.object_list[0].file_type == "image"        # inferred from .jpg
    assert req.object_list[0].file_name == "photo.jpg"
    assert captured["body"] == b"BYTES"
    assert captured["filename"] == "photo.jpg"
    assert "key" in captured["fields"]                    # presigned form fields forwarded


def test_upload_raises_on_s3_failure(tmp_path):
    storage = MagicMock()
    storage.sign_objects.return_value = _signed_envelope()
    c = _client(storage=storage)
    c._s3_post = lambda *a: 403
    f = tmp_path / "doc.pdf"
    f.write_bytes(b"x")
    with pytest.raises(EverOSStorageError):
        c.upload(str(f))


def test_guess_file_type():
    from everos_cloud.client import _guess_file_type
    assert _guess_file_type("a.PNG") == "image"
    assert _guess_file_type("clip.mp4") == "video"
    assert _guess_file_type("report.pdf") == "file"
    assert _guess_file_type("noext") == "file"


def test_memory_api_error_is_wrapped():
    mem = MagicMock()
    mem.search_memory.side_effect = ApiException(status=401, reason="unauthorized")
    c = _client(memory=mem)
    with pytest.raises(EverOSAPIError) as ei:
        c.search("q")
    assert ei.value.status == 401
    assert isinstance(ei.value, EverOSError)          # unified hierarchy


def test_timeout_is_applied_to_calls():
    mem = MagicMock()
    mem.get_memory.return_value = SimpleNamespace(data=None)
    c = EverOS("sk-test", timeout=5)
    c.memory = mem
    c.get("episode")
    assert mem.get_memory.call_args.kwargs.get("_request_timeout") == 5


def test_storage_error_is_in_hierarchy():
    assert issubclass(EverOSStorageError, EverOSError)


def test_close_and_context_manager_do_not_raise():
    # exercises __enter__/__exit__ -> close() against the real generated ApiClient
    with EverOS("sk-test"):
        pass
    EverOS("sk-test").close()  # idempotent / direct


# ── generated clients are attached ───────────────────────────────────────────
def test_every_generated_client_is_exposed():
    """Regression: `client.knowledge` / `client.tasks` used to raise AttributeError.

    The facade only attached MemoryApi and StorageApi, so the whole knowledge and
    tasks surface was unreachable through the documented `client.<group>` handle.
    """
    from everos_cloud import KnowledgeApi, MemoryApi, StorageApi, TasksApi

    c = EverOS("sk-test")
    assert isinstance(c.memory, MemoryApi)
    assert isinstance(c.storage, StorageApi)
    assert isinstance(c.knowledge, KnowledgeApi)
    assert isinstance(c.tasks, TasksApi)


# ── memory tags ──────────────────────────────────────────────────────────────
def test_tag_calls_build_inputs_and_return_data():
    mem = MagicMock()
    mem.bind_tags.return_value = SimpleNamespace(data="B")
    mem.unbind_tags.return_value = SimpleNamespace(data="U")
    mem.replace_tags.return_value = SimpleNamespace(data="R")
    c = _client(memory=mem)

    assert c.bind_tags("episode", ["m1", "m2"], ["work"]) == "B"
    assert c.unbind_tags("episode", ["m1"], ["work"]) == "U"
    assert c.replace_tags("profile", ["m3"], ["home", "work"]) == "R"

    bind = mem.bind_tags.call_args.args[0]
    assert isinstance(bind, TagBindInput)
    assert bind.memory_type == "episode" and bind.memory_ids == ["m1", "m2"] and bind.tags == ["work"]
    assert isinstance(mem.unbind_tags.call_args.args[0], TagUnbindInput)
    replace = mem.replace_tags.call_args.args[0]
    assert isinstance(replace, TagReplaceInput)
    assert replace.tags == ["home", "work"]


def test_tag_inputs_carry_no_scope():
    """Tag scope is the memory ids, so app_id / project_id must not be injected."""
    mem = MagicMock()
    mem.bind_tags.return_value = SimpleNamespace(data=None)
    c = EverOS("sk-test", app_id="myapp", project_id="proj")
    c.memory = mem
    c.bind_tags("episode", ["m1"], ["t"])
    payload = mem.bind_tags.call_args.args[0]
    assert not hasattr(payload, "app_id") or payload.app_id is None
    assert not hasattr(payload, "project_id") or payload.project_id is None


# ── knowledge base ───────────────────────────────────────────────────────────
def test_create_kb_builds_input_and_drops_none():
    kb = MagicMock()
    kb.create_knowledge_base.return_value = SimpleNamespace(data="KB")
    c = _client(knowledge=kb)

    assert c.create_kb("Handbook") == "KB"
    payload = kb.create_knowledge_base.call_args.args[0]
    assert isinstance(payload, KbCreateInput)
    assert payload.name == "Handbook"
    # Unset optionals must not reach the wire (see the wire-level tests below).
    assert payload.description is None and payload.owner_id is None


def test_kb_crud_passes_path_params_positionally():
    kb = MagicMock()
    for name in ("get_knowledge_base", "update_knowledge_base", "delete_knowledge_base"):
        getattr(kb, name).return_value = SimpleNamespace(data=name)
    c = _client(knowledge=kb)

    assert c.get_kb("kb-1") == "get_knowledge_base"
    assert kb.get_knowledge_base.call_args.args == ("kb-1",)

    assert c.update_kb("kb-1", description="notes") == "update_knowledge_base"
    args = kb.update_knowledge_base.call_args.args
    assert args[0] == "kb-1"
    assert isinstance(args[1], KbPatchBody) and args[1].description == "notes"

    assert c.delete_kb("kb-1") == "delete_knowledge_base"
    assert kb.delete_knowledge_base.call_args.args == ("kb-1",)


def test_list_kbs_omits_unset_query_params():
    kb = MagicMock()
    kb.list_knowledge_bases.return_value = SimpleNamespace(data="L")
    c = _client(knowledge=kb)

    assert c.list_kbs(page=2) == "L"
    kwargs = kb.list_knowledge_bases.call_args.kwargs
    assert kwargs["page"] == 2
    assert "page_size" not in kwargs and "owner_id" not in kwargs   # None dropped, server defaults win


def test_search_kb_builds_body():
    kb = MagicMock()
    kb.search_knowledge.return_value = SimpleNamespace(data="HITS")
    c = _client(knowledge=kb)

    assert c.search_kb("kb-1", "onboarding", top_k=5) == "HITS"
    args = kb.search_knowledge.call_args.args
    assert args[0] == "kb-1"
    assert isinstance(args[1], SearchBody)
    assert args[1].query == "onboarding" and args[1].top_k == 5


# ── document ingest (the 202 + task_id flow) ─────────────────────────────────
def test_ingest_document_creates_by_default():
    kb = MagicMock()
    ack = DocIngestData(status="queued", task_id="req-abc123")
    kb.create_document.return_value = SimpleNamespace(data=ack)
    c = _client(knowledge=kb)

    out = c.ingest_document("kb-1", "Handbook", "body text", category_id="cat-1")

    # Regression: on 1.1.0rc1 the generated DocIngestData required `id`, so this very
    # ack — the only shape the gateway sends — raised a client-side ValidationError.
    assert out.status == "queued" and out.task_id == "req-abc123"
    assert out.id is None
    args = kb.create_document.call_args.args
    assert args[0] == "kb-1"
    assert isinstance(args[1], DocIngestBody)
    assert args[1].title == "Handbook"
    # a plain string is wrapped as inline text content
    assert args[1].content.type == "text" and args[1].content.text == "body text"
    assert args[1].category_id == "cat-1"
    kb.replace_document.assert_not_called()


def test_ingest_document_replaces_when_doc_id_given():
    kb = MagicMock()
    kb.replace_document.return_value = SimpleNamespace(data="REPLACED")
    c = _client(knowledge=kb)

    assert c.ingest_document("kb-1", "T", "C", doc_id="doc-9") == "REPLACED"
    args = kb.replace_document.call_args.args
    assert args[0] == "kb-1" and args[1] == "doc-9"
    assert isinstance(args[2], DocIngestBody)
    kb.create_document.assert_not_called()


def test_document_reads():
    kb = MagicMock()
    kb.list_documents.return_value = SimpleNamespace(data="DOCS")
    kb.get_document.return_value = SimpleNamespace(data="DOC")
    c = _client(knowledge=kb)

    assert c.list_documents("kb-1", page_size=50) == "DOCS"
    assert kb.list_documents.call_args.args == ("kb-1",)
    assert kb.list_documents.call_args.kwargs["page_size"] == 50
    assert "category_id" not in kb.list_documents.call_args.kwargs

    assert c.get_document("kb-1", "doc-1") == "DOC"
    assert kb.get_document.call_args.args == ("kb-1", "doc-1")


# ── async tasks ──────────────────────────────────────────────────────────────
def _task(status, finished_at=None, error=None):
    return SimpleNamespace(id="t1", status=status, finished_at=finished_at, error=error, error_code=None)


def test_get_task_and_list_tasks():
    tasks = MagicMock()
    tasks.get_task_status.return_value = SimpleNamespace(data=_task("processing"))
    tasks.list_tasks.return_value = SimpleNamespace(data="LIST")
    c = _client(tasks=tasks)

    assert c.get_task("t1").status == "processing"
    assert tasks.get_task_status.call_args.args == ("t1",)

    assert c.list_tasks(status="failed") == "LIST"
    kwargs = tasks.list_tasks.call_args.kwargs
    assert kwargs["status"] == "failed"
    assert "session_id" not in kwargs and "page" not in kwargs


def test_wait_task_polls_until_terminal():
    tasks = MagicMock()
    tasks.get_task_status.side_effect = [
        SimpleNamespace(data=_task("queued")),
        SimpleNamespace(data=_task("processing")),
        SimpleNamespace(data=_task("success", finished_at="2026-08-25T00:00:00Z")),
    ]
    c = _client(tasks=tasks)

    out = c.wait_task("t1", interval=0)

    assert out.status == "success"
    assert tasks.get_task_status.call_count == 3


def test_wait_task_treats_pending_as_still_running():
    """`pending` was missing from the status enum in rc1 (ECA-847); it is NOT terminal."""
    tasks = MagicMock()
    tasks.get_task_status.side_effect = [
        SimpleNamespace(data=_task("pending")),
        SimpleNamespace(data=_task("success", finished_at="2026-08-25T00:00:00Z")),
    ]
    c = _client(tasks=tasks)
    assert c.wait_task("t1", interval=0).status == "success"
    assert tasks.get_task_status.call_count == 2


def test_wait_task_stops_on_unknown_terminal_status():
    """`status` is an open set: a state this SDK never heard of must not spin.

    `finished_at` is documented as absent until the task is terminal, so it — not
    the enum — decides. Without this, a future `cancelled` would poll to timeout.
    """
    tasks = MagicMock()
    tasks.get_task_status.return_value = SimpleNamespace(
        data=_task("cancelled", finished_at="2026-08-25T00:00:00Z")
    )
    c = _client(tasks=tasks)

    out = c.wait_task("t1", interval=0)

    assert out.status == "cancelled"
    assert tasks.get_task_status.call_count == 1


def test_wait_task_raises_on_failure_and_carries_the_task():
    tasks = MagicMock()
    failed = _task("failed", finished_at="2026-08-25T00:00:00Z", error="parser blew up")
    tasks.get_task_status.return_value = SimpleNamespace(data=failed)
    c = _client(tasks=tasks)

    with pytest.raises(EverOSError) as ei:
        c.wait_task("t1", interval=0)
    assert "parser blew up" in str(ei.value)
    assert ei.value.task is failed


def test_wait_task_can_return_the_failed_task_instead():
    tasks = MagicMock()
    tasks.get_task_status.return_value = SimpleNamespace(
        data=_task("failed", finished_at="2026-08-25T00:00:00Z", error="boom")
    )
    c = _client(tasks=tasks)
    assert c.wait_task("t1", interval=0, raise_on_failure=False).status == "failed"


def test_wait_task_times_out():
    tasks = MagicMock()
    tasks.get_task_status.return_value = SimpleNamespace(data=_task("processing"))
    c = _client(tasks=tasks)

    with pytest.raises(EverOSError) as ei:
        c.wait_task("t1", timeout=0, interval=0)
    assert "processing" in str(ei.value)
    assert ei.value.task.status == "processing"


def test_task_finished_helper():
    from everos_cloud.client import _task_finished
    assert _task_finished(_task("success"))
    assert _task_finished(_task("failed"))
    assert _task_finished(_task("anything", finished_at="2026-08-25T00:00:00Z"))
    assert not _task_finished(_task("queued"))
    assert not _task_finished(_task("processing"))
    assert not _task_finished(_task("pending"))


# ── error normalization on the new surfaces ──────────────────────────────────
def test_knowledge_and_task_errors_are_wrapped():
    kb = MagicMock()
    kb.list_knowledge_bases.side_effect = ApiException(status=429, reason="rate limited")
    tasks = MagicMock()
    tasks.get_task_status.side_effect = ApiException(status=503, reason="unavailable")
    c = _client(knowledge=kb, tasks=tasks)

    with pytest.raises(EverOSAPIError) as ei:
        c.list_kbs()
    assert ei.value.status == 429

    with pytest.raises(EverOSAPIError) as ei:
        c.get_task("t1")
    assert ei.value.status == 503


def test_timeout_applies_to_knowledge_and_tasks():
    kb = MagicMock()
    kb.list_knowledge_bases.return_value = SimpleNamespace(data=None)
    tasks = MagicMock()
    tasks.get_task_stats.return_value = SimpleNamespace(data=None)
    c = EverOS("sk-test", timeout=7)
    c.knowledge, c.tasks = kb, tasks

    c.list_kbs()
    assert kb.list_knowledge_bases.call_args.kwargs.get("_request_timeout") == 7


def test_to_content_coerces_string_dict_and_passthrough():
    from everos_cloud.client import EverOS as _E
    from everos_cloud.models import ContentItem

    text = _E._to_content("hello")
    assert isinstance(text, ContentItem) and text.type == "text" and text.text == "hello"

    # an uploaded object: its object_key rides in `uri`
    obj = _E._to_content({"type": "pdf", "uri": "obj-123", "name": "handbook.pdf"})
    assert obj.type == "pdf" and obj.uri == "obj-123"

    existing = ContentItem(type="image", uri="obj-9")
    assert _E._to_content(existing) is existing


def test_document_patch_and_delete():
    kb = MagicMock()
    kb.update_document.return_value = SimpleNamespace(data="PATCHED")
    kb.delete_document.return_value = SimpleNamespace(data="DELETED")
    c = _client(knowledge=kb)

    assert c.update_document("kb-1", "doc-1", category_id="cat-2") == "PATCHED"
    args = kb.update_document.call_args.args
    assert args[0] == "kb-1" and args[1] == "doc-1"
    assert args[2].category_id == "cat-2" and args[2].title is None   # metadata only

    assert c.delete_document("kb-1", "doc-1") == "DELETED"
    assert kb.delete_document.call_args.args == ("kb-1", "doc-1")


def test_wait_task_rides_out_a_transient_rate_limit():
    """A 429 mid-poll must not end the wait: the caller cannot resume one."""
    tasks = MagicMock()
    tasks.get_task_status.side_effect = [
        SimpleNamespace(data=_task("processing")),
        ApiException(status=429, reason="rate limited"),
        ApiException(status=503, reason="unavailable"),
        SimpleNamespace(data=_task("success", finished_at="2026-08-25T00:00:00Z")),
    ]
    c = _client(tasks=tasks)

    assert c.wait_task("t1", interval=0).status == "success"
    assert tasks.get_task_status.call_count == 4


def test_wait_task_does_not_retry_a_permanent_error():
    tasks = MagicMock()
    tasks.get_task_status.side_effect = ApiException(status=404, reason="no such task")
    c = _client(tasks=tasks)

    with pytest.raises(EverOSAPIError) as ei:
        c.wait_task("t1", interval=0)
    assert ei.value.status == 404
    assert tasks.get_task_status.call_count == 1     # no pointless retries


def test_wait_task_gives_up_on_a_transient_error_past_the_deadline():
    tasks = MagicMock()
    tasks.get_task_status.side_effect = ApiException(status=429, reason="rate limited")
    c = _client(tasks=tasks)

    with pytest.raises(EverOSAPIError) as ei:
        c.wait_task("t1", timeout=0, interval=0)
    assert ei.value.status == 429


def test_wait_task_backs_off_up_to_the_ceiling():
    tasks = MagicMock()
    tasks.get_task_status.return_value = SimpleNamespace(data=_task("processing"))
    c = _client(tasks=tasks)
    slept = []

    import everos_cloud.client as mod
    real_sleep = mod.time.sleep
    mod.time.sleep = slept.append
    try:
        with pytest.raises(EverOSError):
            c.wait_task("t1", timeout=0.001, interval=1, max_interval=4)
    finally:
        mod.time.sleep = real_sleep
    # first gap is `interval`, then doubling, capped at max_interval
    assert slept[:1] == [1]
    assert all(s <= 4 for s in slept)


def test_update_document_rejects_an_empty_patch():
    kb = MagicMock()
    c = _client(knowledge=kb)
    with pytest.raises(ValueError):
        c.update_document("kb-1", "doc-1")
    kb.update_document.assert_not_called()


# ── wire-level: what actually leaves the process ─────────────────────────────
# These assert on `to_dict()`, i.e. the serialized request body, not just the model.
# A model field whose default is a non-None sentinel is invisible at the model level
# and only shows up here.
def test_unset_category_id_stays_off_the_wire():
    """`DocIngestBody.category_id` defaults to "" and the contract reads
    "omit for LLM auto-classify" — so an unset category must not be serialized."""
    kb = MagicMock()
    kb.create_document.return_value = SimpleNamespace(data=None)
    c = _client(knowledge=kb)

    c.ingest_document("kb-1", "T", "text")
    body = kb.create_document.call_args.args[1].to_dict()
    assert "category_id" not in body, body

    c.ingest_document("kb-1", "T", "text", category_id="cat-1")
    body = kb.create_document.call_args.args[1].to_dict()
    assert body["category_id"] == "cat-1"


def test_unset_kb_description_stays_off_the_wire():
    kb = MagicMock()
    kb.create_knowledge_base.return_value = SimpleNamespace(data=None)
    c = _client(knowledge=kb)

    c.create_kb("Handbook")
    body = kb.create_knowledge_base.call_args.args[0].to_dict()
    assert "description" not in body and "owner_id" not in body, body

    c.create_kb("Handbook", description="HR")
    assert kb.create_knowledge_base.call_args.args[0].to_dict()["description"] == "HR"


def test_search_kb_does_materialize_its_defaults():
    """Deliberate contrast with the two above: SearchBody's defaults ARE the server's
    defaults, so sending them is a no-op — and memory `search` already behaves this way."""
    kb = MagicMock()
    kb.search_knowledge.return_value = SimpleNamespace(data=None)
    c = _client(knowledge=kb)

    c.search_kb("kb-1", "q")
    body = kb.search_knowledge.call_args.args[1].to_dict()
    assert body["method"] == "hybrid" and body["top_k"] == 10
