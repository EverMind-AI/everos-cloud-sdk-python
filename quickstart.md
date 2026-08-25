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
kb = client.create_kb("Employee Handbook", description="HR policies")
kb_id = kb.id

# ── Ingest a document ─────────────────────────────────────────────────────────
# `content` takes a plain string for inline text. Omit category_id to let the
# server auto-classify. Returns the 202 ack: status="queued" + task_id.
ack = client.ingest_document(kb_id, "Leave policy", "Employees accrue 20 days...")

# ── Wait for it to be processed ───────────────────────────────────────────────
# Polls GET /tasks/{task_id} until the task reaches a terminal state. Raises
# EverOSError if the task fails or outlives the timeout.
task = client.wait_task(ack.task_id, timeout=300)
print(task.status)                    # "success"

# ── Ingest a non-text file ────────────────────────────────────────────────────
# Upload it first; the returned object_key is the content `uri`.
object_key = client.upload("handbook.pdf")
client.ingest_document(kb_id, "Handbook", {
    "type": "pdf", "uri": object_key, "name": "handbook.pdf",
})

# ── Search it ─────────────────────────────────────────────────────────────────
hits = client.search_kb(kb_id, "how much leave do I get", top_k=5)

# ── Browse and maintain ───────────────────────────────────────────────────────
docs = client.list_documents(kb_id, page=1, page_size=20)
client.update_document(kb_id, doc_id, category_id="cat-2")   # metadata only
client.delete_document(kb_id, doc_id)
client.update_kb(kb_id, description="HR policies (2026)")
client.delete_kb(kb_id)               # deletes the kb and everything in it
```

## Async tasks

Every async operation (memory add, document ingest) reports progress through the
task API. `status` is one of `queued` / `processing` / `pending` / `success` /
`failed` — and it is an **open set**, so treat an unrecognized value as terminal
only when `finished_at` is present (which is what `wait_task` does).

```python
task = client.get_task(task_id)                 # one task
page = client.list_tasks(status="failed")       # filter by status / session / window
task = client.wait_task(task_id, interval=2)    # poll to completion

# Inspect a failure instead of raising on it
task = client.wait_task(task_id, raise_on_failure=False)
if task.status == "failed":
    print(task.error)
```

## Memory tags

Tags are scoped by the memory ids themselves — no `app_id` / `project_id`.

```python
client.bind_tags("episode", ["mem-1", "mem-2"], ["onboarding"])   # add
client.unbind_tags("episode", ["mem-1"], ["onboarding"])          # remove
client.replace_tags("episode", ["mem-2"], ["archived"])           # overwrite
```

Every method returns the endpoint's `.data`. Failures raise `EverOSError`
(`EverOSAPIError` for HTTP errors, `EverOSStorageError` for uploads, and a plain
`EverOSError` for a task that fails or outlives its `wait_task` timeout — the last
task seen is on the error's `.task`). Set a
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
| `bind_tags` / `unbind_tags` / `replace_tags` | `POST /api/v2/memory/tag/*` | Add / remove / overwrite tags on memory ids. |
| `create_kb(name, ...)` | `POST /api/v2/knowledge_bases` | Create a knowledge base. |
| `list_kbs(...)` | `GET /api/v2/knowledge_bases` | Paginated list. |
| `get_kb` / `update_kb` / `delete_kb` | `GET/PATCH/DELETE .../{kb_id}` | Read, patch, delete (cascades). |
| `search_kb(kb_id, query, ...)` | `POST .../{kb_id}/search` | Search one knowledge base. |
| `ingest_document(kb_id, title, content, ...)` | `POST/PUT .../documents` | Async (202 + `task_id`); `doc_id=` replaces in place. |
| `list_documents` / `get_document` | `GET .../documents[/{doc_id}]` | Browse ingested documents. |
| `update_document` / `delete_document` | `PATCH/DELETE .../documents/{doc_id}` | Patch title / category; delete a document. |
| `get_task(task_id)` | `GET /api/v2/tasks/{task_id}` | One task's status. |
| `list_tasks(...)` | `GET /api/v2/tasks` | Filter by status / session / time window. |
| `wait_task(task_id, ...)` | polls `GET /api/v2/tasks/{task_id}` | Blocks until terminal, backing off between polls and riding out transient 429/5xx; raises on failure/timeout. |

## Low-level typed client (advanced)

`EverOS` wraps the generated clients, all four exposed as attributes: `client.memory`,
`client.storage`, `client.knowledge`, `client.tasks`.

**One rule to keep straight**: some facade methods share a name with the generated
method they wrap — `client.list_documents(kb_id)` and
`client.knowledge.list_documents(kb_id)` take the same arguments. They differ in what
they return: the facade hands back the `.data` payload, the generated client hands back
the envelope. That holds for every method on both sides, so `.data` is the only
adjustment when you drop down. Reach for them when you want typed
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
