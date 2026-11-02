"""kion-sdk — typed Python SDK for the Kion API.

Like the go lane, one installable package ships a sub-package per supported Kion
release (``kion_sdk.v3_14`` … ``kion_sdk.v3_17``, plus ``kion_sdk.master``). Import
the version matching your Kion instance and build a client with ``new_client``:

    import kion_sdk
    import kion_sdk.v3_16
    from kion_sdk.v3_16.api.project import get_project

    client = kion_sdk.new_client(kion_sdk.v3_16, "https://kion.example.com",
                                 api_key="app_128_...")
    resp = get_project.sync_detailed(client=client, id=42)
    if kion_sdk.is_not_found(resp):
        ...

Both ``api_key`` and a bearer ``token`` authenticate via ``Authorization: Bearer``;
the base URL is normalized to the ``/api`` suffix and Kion's query-string-
discriminated endpoints are handled transparently.
"""

from ._wrapper import (
    KION_RELEASES,
    KION_VERSIONS,
    is_auth_error,
    is_conflict,
    is_not_found,
    kion_release,
    kion_version,
    new_client,
    normalize_server_url,
    status_code,
)

__all__ = [
    "new_client",
    "normalize_server_url",
    "is_not_found",
    "is_auth_error",
    "is_conflict",
    "status_code",
    "KION_VERSIONS",
    "kion_version",
    "KION_RELEASES",
    "kion_release",
    "__version__",
]

__version__ = "0.14.0"
