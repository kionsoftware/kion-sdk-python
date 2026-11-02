# kion-sdk (Python)

Typed Python SDK for the [Kion](https://kion.io) API, generated from Kion's
OpenAPI spec with [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

Like the Go SDK, one installable package (`kion-sdk`) ships a **sub-package per
supported Kion release** — `kion_sdk.v3_14` … `kion_sdk.v3_17`, plus
`kion_sdk.master` (unreleased dev; GitLab mirror only — not on GitHub). Import the version matching your Kion
instance. Each endpoint has sync and async variants.

> This lane is part of the **kion-sdk monorepo** and is published to its own repo
> by CI. `src/kion_sdk/<version>/` is generated (openapi-python-client); the
> hand-written wrapper lives in `src/kion_sdk/_wrapper/`.

## Install

```bash
pip install kion-sdk          # from the internal index / built wheel
```

## Quick start

```python
import kion_sdk
import kion_sdk.v3_16
from kion_sdk.v3_16.api.project import get_project

client = kion_sdk.new_client(
    kion_sdk.v3_16, "https://kion.example.com", api_key="app_128_..."
)

resp = get_project.sync_detailed(client=client, id=42)
if kion_sdk.is_not_found(resp):
    ...
else:
    project = resp.parsed

# async is available on every endpoint:
#   resp = await get_project.asyncio_detailed(client=client, id=42)
```

`new_client` normalizes the base URL to the `/api` suffix, wires
`Authorization: Bearer <value>` auth (pass `api_key=` or `token=`; `token` wins),
and installs a transport that transparently handles Kion's query-string-
discriminated endpoints. It accepts `verify=`, `timeout=`, and extra
`httpx` kwargs.

## Error handling

Version-agnostic helpers work on a `*_detailed` `Response` or an
`errors.UnexpectedStatus`:

```python
kion_sdk.is_not_found(resp)   # 404
kion_sdk.is_auth_error(resp)  # 401 / 403
kion_sdk.is_conflict(resp)    # 409
kion_sdk.status_code(resp)    # raw int, or None
```

## Development (in the monorepo)

```bash
make -C python help
make gen LANG=python VERSION=v3_16   # from the monorepo root: regenerate one version
make -C python test                  # wrapper unit tests
make -C python lint
```

Generation reads the shared, language-agnostic spec at `../spec/<v>/openapi3.json`
(produced by `../preprocess`).
