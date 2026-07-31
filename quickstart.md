# EverOS Cloud SDK — Quickstart

Full usage for the Python client of the **EverOS Cloud Memory API** (v2). For an
overview and install, see the [README](README.md).

> **This code is generated** from the EverOS OpenAPI contract, but the ergonomic
> `EverOS` client below is hand-maintained. File bugs and feature requests as issues.

## Install

```sh
pip install everos-cloud
```

Release candidates need `--pre`: `pip install --pre everos-cloud`.

## Quickstart

`EverOS` is the recommended high-level client: plain kwargs / dicts in, the response
`.data` out. Get an API key from the [EverOS Console](https://everos.evermind.ai).

```python
from everos_cloud import EverOS

client = EverOS(api_key="sk-...")     # host defaults to https://api.evermind.ai

# ── Add messages ──────────────────────────────────────────────────────────────
# Async by default: validated and enqueued, extraction runs in the background.
# `content` accepts a plain string; `timestamp` defaults to now, `sender_id` to role.
client.add(session_id="session-1", messages=[
    {"sender_id": "user-1", "role": "user", "content": "I love hiking in the mountains"},
])

# ── Force extraction for a session ────────────────────────────────────────────
flushed = client.flush("session-1")
print(flushed.status)                 # "extracted" | "no_extraction"

# ── Get memories (paginated) ──────────────────────────────────────────────────
# memory_type: episode | profile | agent_case | agent_skill. Scope with user_id or agent_id.
page = client.get("episode", user_id="user-1", page=1, page_size=20)
print(page.episodes)

# ── Search ────────────────────────────────────────────────────────────────────
# method: keyword | vector | hybrid (default) | agentic. Scope with user_id or agent_id.
result = client.search("outdoor hobbies", user_id="user-1", top_k=10, include_profile=True)
print(result.episodes)

# ── Edit a user's profile (bulk) ──────────────────────────────────────────────
# action: add | update | delete   ·   type: explicit_info | implicit_traits
client.edit("user-1", operations=[
    {"action": "add", "type": "explicit_info",
     "data": {"category": "hobby", "description": "Enjoys hiking in the mountains"},
     "reason": "Stated in session-1"},
])

# ── Delete memories (scoped soft-delete) ──────────────────────────────────────
client.delete(user_id="user-1", session_id="session-1")

# ── Upload multimodal data ────────────────────────────────────────────────────
# Presigns + POSTs the file directly to S3, returns the object key you then
# reference in a message's multimodal content. file_type is inferred from the ext.
object_key = client.upload("photo.jpg")
```

Every method returns the endpoint's `.data`. Failures raise `EverOSError`
(`EverOSAPIError` for memory HTTP errors, `EverOSStorageError` for uploads). Set a
per-client request timeout with `EverOS(api_key=..., timeout=30)`, or use it as a
context manager (`with EverOS(...) as client:`) to release connections on exit.

## Method reference

| Method | Endpoint | Notes |
|---|---|---|
| `add(session_id, messages, ...)` | `POST /api/v2/memory/add` | Async by default (202 `queued`); `async_mode=False` for sync 200. |
| `flush(session_id)` | `POST /api/v2/memory/flush` | Force extraction for a session. |
| `get(memory_type, ...)` | `POST /api/v2/memory/get` | Paginated list by `memory_type`. |
| `search(query, ...)` | `POST /api/v2/memory/search` | Keyword / vector / hybrid / agentic. |
| `edit(user_id, operations)` | `POST /api/v2/memory/edit` | Bulk profile add / update / delete. |
| `delete(...)` | `POST /api/v2/memory/delete` | Scoped soft-delete. |
| `upload(path)` | `POST /api/v2/object/sign` + S3 | Presign + direct-to-S3, returns `object_key`. |

## Low-level typed client (advanced)

`EverOS` wraps the generated `MemoryApi` / `StorageApi`, exposed as `client.memory`
and `client.storage`. Use them directly when you want typed models and full control
— every request is a pydantic v2 model and every response a typed envelope
(`.data`). The full per-endpoint and model docs live under [`docs/`](docs/).

```python
from everos_cloud import ApiClient, Configuration, MemoryApi
from everos_cloud.models import AddInput, MessageItem, Content, SearchInput

config = Configuration(access_token="sk-...")

with ApiClient(config) as api:
    memory = MemoryApi(api)

    memory.add_memory(AddInput(
        session_id="session-1",
        messages=[MessageItem(
            sender_id="user-1", role="user", timestamp=1700000000000,
            content=Content("I love hiking in the mountains"),
        )],
    ))

    result = memory.search_memory(SearchInput(query="outdoor hobbies", method="hybrid"))
    print(result.data)
```

`MessageItem.content` accepts a plain string (shorthand for a single text item) or an
explicit list — both are passed through the `Content` wrapper:

```python
Content("hello")                                     # plain text
Content([ContentItem(type="text", text="hello")])    # explicit item list
```

## Links

- API reference: per-endpoint and model docs under [`docs/`](docs/).
- Issues: https://github.com/EverMind-AI/everos-cloud-sdk-python/issues
