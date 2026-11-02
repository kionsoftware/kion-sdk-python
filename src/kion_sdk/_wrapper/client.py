"""Client factory: build a configured, version-specific Kion client.

Mirrors the go lane's per-version ``New(baseURL, opts...)`` — it normalizes the
base URL (``/api``), wires bearer/API-key auth, and installs the query-string
rewrite transport on both the sync and async HTTP clients.
"""

from __future__ import annotations

from typing import Any

import httpx

from .transport import AsyncQueryStringRewriteTransport, QueryStringRewriteTransport
from .urls import normalize_server_url


def _resolve_auth_client(version: Any) -> Any:
    """Accept a ``kion_sdk.<vN>`` module, its ``.client`` module, or the
    ``AuthenticatedClient`` class itself, and return the class."""
    client_mod = getattr(version, "client", None)
    if client_mod is not None and hasattr(client_mod, "AuthenticatedClient"):
        return client_mod.AuthenticatedClient
    if hasattr(version, "AuthenticatedClient"):
        return version.AuthenticatedClient
    return version


def new_client(
    version: Any,
    base_url: str,
    *,
    api_key: str | None = None,
    token: str | None = None,
    verify: bool = True,
    timeout: float | httpx.Timeout = 30.0,
    raise_on_unexpected_status: bool = False,
    **httpx_args: Any,
) -> Any:
    """Build an ``AuthenticatedClient`` for a Kion API version.

    ``version`` is a ``kion_sdk.<vN>`` module (e.g. ``import kion_sdk.v3_16``) or
    its ``AuthenticatedClient`` class. Both ``api_key`` and ``token`` authenticate
    via ``Authorization: Bearer <value>``; ``token`` wins if both are supplied.
    The returned client's sync and async transports fold ``/__qs__/`` synthetic
    paths back into real query strings.
    """
    auth_cls = _resolve_auth_client(version)
    secret = token or api_key
    if not secret:
        raise ValueError("new_client requires either api_key or token")

    server = normalize_server_url(base_url)
    to = timeout if isinstance(timeout, httpx.Timeout) else httpx.Timeout(timeout)

    client = auth_cls(
        base_url=server,
        token=secret,
        prefix="Bearer",
        timeout=to,
        verify_ssl=verify,
        raise_on_unexpected_status=raise_on_unexpected_status,
    )

    # Inject our own httpx clients so we control the transport. We add the auth
    # header here (rather than relying on the client's lazy builder) because
    # set_*_httpx_client bypasses that builder.
    headers = {"Authorization": f"Bearer {secret}"}
    client.set_httpx_client(
        httpx.Client(
            base_url=server,
            headers=headers,
            timeout=to,
            transport=QueryStringRewriteTransport(httpx.HTTPTransport(verify=verify)),
            **httpx_args,
        )
    )
    client.set_async_httpx_client(
        httpx.AsyncClient(
            base_url=server,
            headers=headers,
            timeout=to,
            transport=AsyncQueryStringRewriteTransport(
                httpx.AsyncHTTPTransport(verify=verify)
            ),
            **httpx_args,
        )
    )
    return client
