<div align="center" id="readme-top">

![EverOS banner](https://github.com/user-attachments/assets/8e217d39-5d15-4c6c-9b54-3e83add4e0f2)

<h3 align="center">☁️ Managed long-term memory for AI agents — the official <b>Cloud</b> Python SDK</h3>

<p align="center">
  <a href="https://x.com/evermind"><img src="https://img.shields.io/badge/EverMind-000000?labelColor=gray&style=for-the-badge&logo=x&logoColor=white" alt="X"></a>
  <a href="https://huggingface.co/EverMind-AI"><img src="https://img.shields.io/badge/🤗_HuggingFace-EverMind-F5C842?labelColor=gray&style=for-the-badge" alt="HuggingFace"></a>
  <a href="https://discord.gg/gYep5nQRZJ"><img src="https://img.shields.io/badge/Discord-EverMind-404EED?labelColor=gray&style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <a href="https://pypi.org/project/everos-cloud/"><img src="https://img.shields.io/pypi/v/everos-cloud?color=2DABC2&style=for-the-badge" alt="PyPI"></a>
  <img src="https://img.shields.io/pypi/pyversions/everos-cloud?style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/license-Apache--2.0-green?style=for-the-badge" alt="License">
</p>

[Website](https://evermind.ai) · [Documentation](https://docs.evermind.ai) · [Console](https://everos.evermind.ai)

</div>

<br>

> **Which package?** This is **EverOS Cloud** — the managed SaaS client (`pip install everos-cloud`).
>
> Want to self-host? Use the open-source [`everos`](https://pypi.org/project/everos/) library instead.

# EverOS Cloud — Python SDK

Give your AI agents memory that persists across sessions — managed, searchable, and typed.
Add a conversation; EverOS turns it into structured, retrievable memory you can query in one call.

## Why EverOS Cloud

- **Self-evolving memory** — memory doesn't just pile up, it improves. Background
  consolidation merges related episodes and refines user profiles over time, so recall
  gets sharper the more your agent is used.
- **Structured memory, not chat logs** — extracts episodes, user profiles, and reusable
  agent cases & skills from raw conversations, so retrieval returns meaning, not transcripts.
- **Retrieval that fits the query** — keyword, vector, hybrid (default), or agentic multi-step search.
- **Multimodal** — attach images, audio, and documents to any message.
- **Built for production** — fully managed (no vector DB or extraction pipeline to run),
  with low-latency retrieval and high-concurrency throughput. The engineering guarantees
  you don't get from self-hosting.
- **Fully typed (pydantic v2)** — every request/response is a typed model with full hints,
  so you get editor autocomplete and validation instead of raw dicts.

## Install

```sh
pip install everos-cloud
```

> Pre-releases need `--pre`: `pip install --pre everos-cloud`.
>
> Upgrading from the 0.4.x client? 1.x is a rewrite with a new API surface — see the
> [migration guide](https://docs.evermind.ai/api-reference/sdk-migration-1x). Pin
> `everos-cloud<1` to stay on the old client.

## Quickstart

Get an API key from the [EverOS Console](https://everos.evermind.ai), then:

```python
from everos_cloud import EverOS

with EverOS(api_key="sk-...") as client:
    client.add(session_id="session-1", messages=[
        {"sender_id": "user-1", "role": "user", "content": "I love hiking in the mountains"},
    ])

    results = client.search("outdoor hobbies", user_id="user-1")
    print(results)
```

**Full usage** — every memory operation, profile editing, and multimodal upload — is in
**[quickstart.md](https://github.com/EverMind-AI/everos-cloud-sdk-python/blob/v1/quickstart.md)**.
Prefer typed control? The generated low-level client is exposed as `client.memory` / `client.storage`.

## Documentation

- [Full SDK usage](https://github.com/EverMind-AI/everos-cloud-sdk-python/blob/v1/quickstart.md)
- [Quickstart](https://docs.evermind.ai/cloud/quickstart)
- [API Reference](https://docs.evermind.ai/api-reference/introduction)
- [Core Concepts](https://docs.evermind.ai/cloud/concepts/memory-lifecycle)

<p align="right"><a href="#readme-top">back to top</a></p>
