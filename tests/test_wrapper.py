"""Unit tests for the version-agnostic wrapper (no network)."""

from __future__ import annotations

import httpx
import pytest

import kion_sdk
import kion_sdk.v3_16
from kion_sdk._wrapper.transport import (
    AsyncQueryStringRewriteTransport,
    QueryStringRewriteTransport,
)


def test_normalize_server_url() -> None:
    assert (
        kion_sdk.normalize_server_url("https://k.example.com")
        == "https://k.example.com/api"
    )
    assert (
        kion_sdk.normalize_server_url("https://k.example.com/")
        == "https://k.example.com/api"
    )
    assert (
        kion_sdk.normalize_server_url("https://k.example.com/api")
        == "https://k.example.com/api"
    )
    assert (
        kion_sdk.normalize_server_url("https://k.example.com/api/")
        == "https://k.example.com/api"
    )


def _capture_sync(path: str) -> str:
    captured: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = str(request.url)
        return httpx.Response(200, json={})

    transport = QueryStringRewriteTransport(httpx.MockTransport(handler))
    with httpx.Client(
        transport=transport, base_url="https://k.example.com/api"
    ) as client:
        client.get(path)
    return captured["url"]


def test_qs_transport_rewrites_synthetic_path() -> None:
    assert (
        _capture_sync("/v3/account/__qs__/account-type/aws")
        == "https://k.example.com/api/v3/account?account-type=aws"
    )


def test_qs_transport_merges_existing_query() -> None:
    url = _capture_sync("/v3/thing/__qs__/kind/x?page=2")
    assert "kind=x" in url and "page=2" in url


def test_qs_transport_passthrough_when_no_marker() -> None:
    assert _capture_sync("/v3/project/42") == "https://k.example.com/api/v3/project/42"


async def test_async_qs_transport_rewrites() -> None:
    captured: dict[str, str] = {}

    async def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = str(request.url)
        return httpx.Response(200, json={})

    transport = AsyncQueryStringRewriteTransport(httpx.MockTransport(handler))
    async with httpx.AsyncClient(
        transport=transport, base_url="https://k.example.com/api"
    ) as client:
        await client.post("/v3/account/__qs__/account-type/azure")
    assert captured["url"] == "https://k.example.com/api/v3/account?account-type=azure"


def test_new_client_requires_credentials() -> None:
    with pytest.raises(ValueError):
        kion_sdk.new_client(kion_sdk.v3_16, "https://k.example.com")


def test_new_client_normalizes_and_authenticates() -> None:
    client = kion_sdk.new_client(
        kion_sdk.v3_16, "https://k.example.com", api_key="app_1_x"
    )
    hc = client.get_httpx_client()
    assert (
        str(hc.base_url) == "https://k.example.com/api/"
    )  # httpx appends the trailing slash
    assert any(k.lower() == "authorization" for k in hc.headers)


def test_new_client_token_wins_over_api_key() -> None:
    client = kion_sdk.new_client(
        kion_sdk.v3_16, "https://k.example.com", api_key="app_1_x", token="tok"
    )
    assert client.get_httpx_client().headers["Authorization"] == "Bearer tok"


def test_error_helpers() -> None:
    assert kion_sdk.is_not_found(httpx.Response(404))
    assert not kion_sdk.is_not_found(httpx.Response(200))
    assert kion_sdk.is_auth_error(httpx.Response(401))
    assert kion_sdk.is_auth_error(httpx.Response(403))
    assert kion_sdk.is_conflict(httpx.Response(409))
    assert kion_sdk.status_code(httpx.Response(500)) == 500
    assert kion_sdk.status_code(object()) is None


def test_kion_releases_match_kion_versions() -> None:
    # A v3_NN release is a Kion tag in that minor (3.NN.P) or its unreleased
    # support branch; master is free-form.
    import re

    assert set(kion_sdk.KION_RELEASES) == set(kion_sdk.KION_VERSIONS)
    for sub, minor in kion_sdk.KION_VERSIONS.items():
        rel = kion_sdk.kion_release(sub)
        assert rel, f"no release stamped for {sub}"
        if sub == "master":
            continue
        assert (
            re.fullmatch(re.escape(minor) + r"\.\d+", rel)
            or rel == f"support-{minor}.x"
        ), (sub, rel)
    assert kion_sdk.kion_release("v9_99") is None
