# EverOS Cloud SDK — Quickstart

Full usage for the Python client of the **EverOS Cloud Memory API** (v2). For an
overview and install, see the [README](README.md).

> **This code is generated** from the EverOS OpenAPI contract. Please file bugs and
> feature requests as issues — pull requests against the generated source will be
> overwritten on the next release. Corrections flow through the internal SDK factory.

## Install

```sh
pip install everos-cloud
```

Release candidates need `--pre`: `pip install --pre everos-cloud==1.0.0rc1`.

> **Upgrading from 0.4.x?** `everos-cloud` 1.0.0 is a **rewrite, not an increment**. The
> 0.x line was a different client (httpx-based, hand-maintained); 1.x is generated from
> the EverOS OpenAPI contract and has a different API surface — client classes, method
> names, and model types all changed. The import path (`everos_cloud`) is unchanged.
> Pin `everos-cloud<1` if you are not ready to migrate.

## Authentication

All requests use your EverOS API key as a bearer token:

```python
from everos_cloud import Configuration
config = Configuration(access_token="sk-...")   # sent as: Authorization: Bearer sk-...
```

The default host is `https://api.evermind.ai`; override with `Configuration(host=...)`.

## Quickstart

The snippet below exercises the six Memory endpoints. Every Memory call takes a
single typed input model and returns a typed response envelope (`result.data`).
Object storage lives on a separate `StorageApi` (see below).

```python
from everos_cloud import ApiClient, Configuration, MemoryApi
from everos_cloud.models import (
    AddInput, MessageItem, Content, SearchInput, GetInput, DeleteInput,
    EditInput, AddOperation, EditInputOperationsInner, FlushInput,
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

    # ── Flush a session (force boundary detection + extraction) ────────────────
    # Extraction is normally async; flush forces it for a session and returns
    # status "extracted" or "no_extraction". The generated method name mirrors
    # the operationId.
    flushed = memory.flush_api_v2_memory_flush_post(FlushInput(session_id="session-1"))
    print(flushed.data.status)                      # "extracted" | "no_extraction"
```

## Uploading multimodal data (`StorageApi`)

Attaching images, audio, or documents to a message is a two-step flow: ask the
API to presign an upload, then `POST` the bytes directly to S3 using the returned
form fields. The sign endpoint lives on `StorageApi`.

Unlike the Memory endpoints, `sign_objects` returns the raw MMS envelope: business
outcome is carried in `status` (`0` means success) and the payload in
`result.data` — check `status == 0` before reading it.

```python
import requests
from everos_cloud import ApiClient, Configuration, StorageApi
from everos_cloud.models import SignRequest, SignObjectItem

config = Configuration(access_token="sk-...")

with ApiClient(config) as client:
    storage = StorageApi(client)

    # ── Presign uploads (≤ 50 objects; each file_id unique) ────────────────────
    # file_type: image | file | video
    envelope = storage.sign_objects(SignRequest(
        object_list=[
            SignObjectItem(file_id="file-1", file_name="photo.jpg", file_type="image"),
        ],
    ))

    if envelope.status != 0:                        # 0 == success; see status codes below
        raise RuntimeError(f"sign failed: status={envelope.status} error={envelope.error}")

    # ── Upload the bytes straight to S3 with the presigned POST form ───────────
    for obj in envelope.result.data.object_list:
        signed = obj.object_signed_info             # url + fields + maxSize
        with open("photo.jpg", "rb") as fh:
            resp = requests.post(
                signed.url,
                data=signed.fields,                 # presigned form fields
                files={"file": fh},
            )
        resp.raise_for_status()                     # 204 from S3 on success
        print(obj.object_key)                       # reference this key back in /add
```

Non-zero `status` values surface business errors rather than raising — common
ones are `2018` (validation failed), `1012` (bad/expired token), `1002`
(unsupported `file_type`), and `1007` (more than 50 objects). See the `signObjects`
description in `openapi.json` for the full list.

## Methods

`MemoryApi` mirrors the v2 endpoints:

| Method | Endpoint | Notes |
|---|---|---|
| `add_memory(AddInput)` | `POST /api/v2/memory/add` | Async by default (202 `queued`); `async_mode=False` for sync 200. |
| `search_memory(SearchInput)` | `POST /api/v2/memory/search` | Keyword / vector / hybrid / agentic. |
| `get_memory(GetInput)` | `POST /api/v2/memory/get` | Paginated list by `memory_type`. |
| `delete_memory(DeleteInput)` | `POST /api/v2/memory/delete` | Scoped soft-delete. |
| `edit_profile(EditInput)` | `POST /api/v2/memory/edit` | Bulk profile add/update/delete operations. |
| `flush_api_v2_memory_flush_post(FlushInput)` | `POST /api/v2/memory/flush` | Force boundary detection + extraction for a session. |

`StorageApi` covers object upload:

| Method | Endpoint | Notes |
|---|---|---|
| `sign_objects(SignRequest)` | `POST /api/v1/object/sign` | Presign ≤ 50 objects for direct-to-S3 upload; returns the MMS envelope (`status == 0` on success). |

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
