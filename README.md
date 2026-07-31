# EverOS Cloud SDK for Python

Official Python client for the **EverOS Cloud Memory API**, published to PyPI as
[`everos-cloud`](https://pypi.org/project/everos-cloud/).

## Install

```sh
pip install everos-cloud            # latest stable
pip install --pre everos-cloud      # include pre-releases (release candidates)
```

You don't need this repository to use the SDK — just `pip install`.

## Repository layout — one branch per major API version

Each major version of the API has its own long-lived branch, and releases are
tagged on it. **The default branch is [`v1`](../../tree/v1)** — start there for
authentication and usage.

| Branch | API major | PyPI versions | Status |
|--------|-----------|---------------|--------|
| [`v1`](../../tree/v1) | v2 API | `1.x` (pin `>=1,<2`) | current · **default** |
| `v2` (future) | future | `2.x` | — |

Majors are independent and may be incompatible — pick the branch matching the
version you depend on.

## Generated, not hand-edited

This SDK is generated from the EverOS OpenAPI contract by an internal factory.
Please file **issues** for bugs and requests — pull requests against generated
source are overwritten on the next release.
