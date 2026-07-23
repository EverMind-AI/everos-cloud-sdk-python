# EverOS Cloud SDK for Python

Official Python client for the **EverOS Cloud Memory API** (v2).

> **This code is generated** from the EverOS OpenAPI contract. Please file bugs and
> feature requests as issues — pull requests against the generated source will be
> overwritten on the next release. Corrections flow through the internal SDK factory.

## Install

```sh
pip install everos-cloud-sdk
```

## Authentication

All requests use your EverOS API key as a bearer token:

```python
from everos_cloud_sdk import Configuration
config = Configuration(access_token="sk-...")   # sent as: Authorization: Bearer sk-...
```

The default host is `https://api.evermind.ai`; override with `Configuration(host=...)`.

## Quickstart

The snippet below exercises all five endpoints. Every call takes a single typed
input model and returns a typed response envelope (`result.data`).

```python
from everos_cloud_sdk import ApiClient, Configuration, MemoryApi
from everos_cloud_sdk.models import (
    AddInput, MessageItem, Content, SearchInput, GetInput, DeleteInput,
    EditInput, AddOperation, EditInputOperationsInner,
)

config = Configuration(access_token="sk-...")

with ApiClient(config) as client:
    memory = MemoryApi(client)

    # ── Add messages ──────────────────────────────────────────────────────────
    # Async by default: returns HTTP 202 with status "queued" and extraction runs
    # in the background. Pass async_mode=False to write synchronously and surface
    # write errors directly.
    memory.add_memory(AddInput(
        session_id="session-1",
        messages=[
            MessageItem(
                sender_id="user-1",
                role="user",                       # user | assistant | tool
                timestamp=1700000000,
                content=Content("I love hiking in the mountains"),
            )
        ],
    ))

    # ── Search memories ───────────────────────────────────────────────────────
    # method: keyword | vector | hybrid (default) | agentic
    result = memory.search_memory(SearchInput(
        query="outdoor hobbies",
        method="hybrid",
        top_k=10,
        include_profile=True,
    ))
    print(result.data)

    # ── Get memories (paginated) ──────────────────────────────────────────────
    # memory_type: episode | profile | agent_case | agent_skill
    page = memory.get_memory(GetInput(
        memory_type="episode",
        page=1,
        page_size=20,
        sort_order="desc",                         # by timestamp (default)
    ))
    print(page.data)

    # ── Edit profile (bulk, Cloud-only) ───────────────────────────────────────
    # 1–50 operations; each must be wrapped in EditInputOperationsInner.
    # action: add | update | delete   ·   type: explicit_info | implicit_traits
    memory.edit_profile(EditInput(
        user_id="user-1",
        operations=[
            EditInputOperationsInner(AddOperation(
                action="add",
                type="explicit_info",
                data={"category": "hobby", "description": "Enjoys hiking in the mountains"},
                reason="Stated in session-1",
            )),
        ],
    ))

    # ── Delete memories (scoped soft-delete, Cloud-only) ──────────────────────
    # Scope the delete by any combination of user_id / agent_id / session_id.
    memory.delete_memory(DeleteInput(user_id="user-1", session_id="session-1"))
```

## Methods

`MemoryApi` mirrors the v2 endpoints:

| Method | Endpoint | Notes |
|---|---|---|
| `add_memory(AddInput)` | `POST /api/v2/memory/add` | Async by default (202 `queued`); `async_mode=False` for sync 200. |
| `search_memory(SearchInput)` | `POST /api/v2/memory/search` | Keyword / vector / hybrid / agentic. |
| `get_memory(GetInput)` | `POST /api/v2/memory/get` | Paginated list by `memory_type`. |
| `delete_memory(DeleteInput)` | `POST /api/v2/memory/delete` | Scoped soft-delete. |
| `edit_profile(EditInput)` | `POST /api/v2/memory/edit` | Bulk profile add/update/delete operations. |

### A note on message `content`

`MessageItem.content` accepts either a plain string or a list of content items. In
this SDK both are passed through the `Content` wrapper:

```python
Content("hello")                          # plain text (shorthand)
Content([ContentItem(type="text", text="hello")])   # explicit item list
```

Either serializes to the correct wire shape.

## Links

- API reference: per-endpoint and model docs under [`docs/`](docs/).
- Issues: https://github.com/EverMind-AI/everos-cloud-sdk-python/issues
