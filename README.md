# EverOS Cloud SDK for Python

Official Python client for the **EverOS Cloud Memory API**, published to PyPI as
[`everos-cloud-sdk`](https://pypi.org/project/everos-cloud-sdk/).

## Install

```sh
pip install everos-cloud-sdk           # latest stable
pip install --pre everos-cloud-sdk     # include pre-releases (release candidates)
```

You don't need this repository to use the SDK — just `pip install`. Install and
usage docs for each major version live on that version's branch (see below).

## Repository layout — one branch per major API version

The SDK source is **not** on `main`. Each major version of the API has its own
long-lived branch, and releases are tagged on it. `main` is an orientation page
only and carries no SDK code.

| Branch | API major | PyPI versions | Status |
|--------|-----------|---------------|--------|
| [`v1`](../../tree/v1) | v1 | `1.x` (pin `>=1,<2`) | current |
| `v2` (future) | v2 | `2.x` | — |

- **Use the SDK:** `pip install "everos-cloud-sdk>=1,<2"`, then read the README on
  the [`v1`](../../tree/v1) branch for auth + quickstart.
- **Browse source / file issues:** switch to the branch for your major.
- **Releases:** tagged `vX.Y.Z` on the matching version branch (e.g. `v1.0.0`);
  pre-releases like `v1.0.0-rc1` publish to PyPI but install only with `--pre`.

Majors are independent and may be incompatible — pick the branch matching the
version you depend on.

## Generated, not hand-edited

This SDK is generated from the EverOS OpenAPI contract by an internal factory.
Please file **issues** for bugs and requests — pull requests against generated
source are overwritten on the next release.
