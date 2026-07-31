"""Offline unit tests for the EverOS facade — the API layer is mocked, no network."""
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from everos_cloud import EverOS, EverOSAPIError, EverOSError, EverOSStorageError
from everos_cloud.exceptions import ApiException
from everos_cloud.models import AddInput, EditInput, MessageItem, SearchInput


def _client(memory=None, storage=None):
    c = EverOS("sk-test")
    if memory is not None:
        c.memory = memory
    if storage is not None:
        c.storage = storage
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
    assert isinstance(msg.timestamp, int)   # defaults to now
    # string content shorthand became a Content wrapper
    assert msg.content is not None


def test_message_passthrough_and_explicit_fields():
    mem = MagicMock()
    mem.add_memory.return_value = SimpleNamespace(data=None)
    c = _client(memory=mem)
    c.add(session_id="s1", messages=[
        {"sender_id": "u9", "role": "assistant", "timestamp": 1700000000, "content": "hi"},
    ])
    msg = mem.add_memory.call_args.args[0].messages[0]
    assert msg.sender_id == "u9" and msg.role == "assistant" and msg.timestamp == 1700000000


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
