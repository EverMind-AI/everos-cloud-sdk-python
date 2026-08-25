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

## Knowledge bases

A knowledge base is a searchable document library. Ingest is **always asynchronous**:
the gateway answers `202` with a `task_id`, and the document id is minted downstream —
so poll the task to know when the document is queryable.

```python
from everos_cloud import EverOS

client = EverOS(api_key="sk-...")

# ── Create a knowledge base ───────────────────────────────────────────────────
kb = client.kb_create("Employee Handbook", description="HR policies")
kb_id = kb.id

# ── Ingest a document ─────────────────────────────────────────────────────────
# `content` takes a plain string for inline text. Omit category_id to let the
# server auto-classify. Returns the 202 ack: status="queued" + task_id.
ack = client.doc_ingest(kb_id, "Leave policy", "Employees accrue 20 days...")

# ── Wait for it to be processed ───────────────────────────────────────────────
# Polls GET /tasks/{task_id} until the task reaches a terminal state. Raises
# EverOSError if the task fails or outlives the timeout.
task = client.task_wait(ack.task_id, timeout=300)
print(task.status)                    # "success"

# ── Ingest a non-text file ────────────────────────────────────────────────────
# Upload it first; the returned object_key is the content `uri`.
object_key = client.upload("handbook.pdf")
client.doc_ingest(kb_id, "Handbook", {
    "type": "pdf", "uri": object_key, "name": "handbook.pdf",
})

# ── Search it ─────────────────────────────────────────────────────────────────
hits = client.kb_search(kb_id, "how much leave do I get", top_k=5)

# ── Browse and maintain ───────────────────────────────────────────────────────
docs = client.doc_list(kb_id, page=1, page_size=20)
client.doc_update(kb_id, doc_id, category_id="cat-2")   # metadata only
client.doc_delete(kb_id, doc_id)
client.kb_update(kb_id, description="HR policies (2026)")
client.kb_delete(kb_id)               # deletes the kb and everything in it
```

## Async tasks

Every async operation (memory add, document ingest) reports progress through the
task API. `status` is one of `queued` / `processing` / `pending` / `success` /
`failed` — and it is an **open set**, so treat an unrecognized value as terminal
only when `finished_at` is present (which is what `task_wait` does).

```python
task = client.task_get(task_id)                 # one task
page = client.task_list(status="failed")       # filter by status / session / window
task = client.task_wait(task_id, interval=2)    # poll to completion

# Inspect a failure instead of raising on it
task = client.task_wait(task_id, raise_on_failure=False)
if task.status == "failed":
    print(task.error)
```

## Memory tags

Tags are scoped by the memory ids themselves — no `app_id` / `project_id`.

```python
client.tag_bind("episode", ["mem-1", "mem-2"], ["onboarding"])   # add
client.tag_unbind("episode", ["mem-1"], ["onboarding"])          # remove
client.tag_replace("episode", ["mem-2"], ["archived"])           # overwrite
```

Every method returns the endpoint's `.data`. Failures raise `EverOSError`
(`EverOSAPIError` for HTTP errors, `EverOSStorageError` for uploads, and a plain
`EverOSError` for a task that fails or outlives its `task_wait` timeout — the last
task seen is on the error's `.task`). Set a
per-client request timeout with `EverOS(api_key=..., timeout=30)`, or use it as a
context manager (`with EverOS(...) as client:`) to release connections on exit.

## Method reference

New facade methods are named `<resource>_<verb>`, so typing `client.kb` / `client.doc` /
`client.task` / `client.tag` lists everything for that resource. The nine methods 1.0.0
shipped are bare verbs with no prefix (`add` / `search` / `get` / `flush` / `edit` /
`delete` for memory, `presign` / `upload` for storage, plus `close`) — that split is
historical, not a rule: those names are public API since 1.0.0 and cannot be changed.

| Method | Endpoint | Notes |
|---|---|---|
| `add(session_id, messages, ...)` | `POST /api/v2/memory/add` | Async by default (202 `queued`); `async_mode=False` for sync 200. |
| `flush(session_id)` | `POST /api/v2/memory/flush` | Force extraction for a session. |
| `get(memory_type, ...)` | `POST /api/v2/memory/get` | Paginated list by `memory_type`. |
| `search(query, ...)` | `POST /api/v2/memory/search` | Keyword / vector / hybrid / agentic. |
| `edit(user_id, operations)` | `POST /api/v2/memory/edit` | Bulk profile add / update / delete. |
| `delete(...)` | `POST /api/v2/memory/delete` | Scoped soft-delete. |
| `upload(path)` | `POST /api/v2/object/sign` + S3 | Presign + direct-to-S3, returns `object_key`. |
| `tag_bind` / `tag_unbind` / `tag_replace` | `POST /api/v2/memory/tag/*` | Add / remove / overwrite tags on memory ids. |
| `kb_create(name, ...)` | `POST /api/v2/knowledge_bases` | Create a knowledge base. |
| `kb_list(...)` | `GET /api/v2/knowledge_bases` | Paginated list. |
| `kb_get` / `kb_update` / `kb_delete` | `GET/PATCH/DELETE .../{kb_id}` | Read, patch, delete (cascades). |
| `kb_search(kb_id, query, ...)` | `POST .../{kb_id}/search` | Search one knowledge base. |
| `doc_ingest(kb_id, title, content, ...)` | `POST/PUT .../documents` | Async (202 + `task_id`); `doc_id=` replaces in place. |
| `doc_list` / `doc_get` | `GET .../documents[/{doc_id}]` | Browse ingested documents. |
| `doc_update` / `doc_delete` | `PATCH/DELETE .../documents/{doc_id}` | Patch title / category; delete a document. |
| `task_get(task_id)` | `GET /api/v2/tasks/{task_id}` | One task's status. |
| `task_list(...)` | `GET /api/v2/tasks` | Filter by status / session / time window. |
| `task_wait(task_id, ...)` | polls `GET /api/v2/tasks/{task_id}` | Blocks until terminal, backing off between polls and riding out transient 429/5xx; raises on failure/timeout. |

## Low-level typed client (advanced)

`EverOS` wraps the generated clients, all four exposed as attributes: `client.memory`,
`client.storage`, `client.knowledge`, `client.tasks`.

No facade method shares a name with a generated one, so there is never a question
about which layer a call went through. When you do drop down, the envelope is the only
difference: `client.knowledge.list_documents(kb_id).data` is what `client.doc_list(kb_id)`
returns. Reach for them when you want typed
models, full control, or an endpoint the facade does not cover — knowledge-base
*categories* and document *topics* live only there:

```python
client.knowledge.create_category(kb_id, {"name": "Policies"})
client.knowledge.list_topics(kb_id, doc_id)
client.tasks.get_task_stats()
```

Use them directly when you want typed models and full control
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
