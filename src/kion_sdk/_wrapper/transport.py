"""Query-string rewrite transport.

Portal's Swagger 2.0 allows two operations on the same method+path
discriminated by a query value (e.g. ``POST /v3/account?account-type=aws`` vs
``azure``). OpenAPI 3.0 forbids that, so ``preprocess/fixspec`` promotes each
variant to a synthetic distinct path under ``/__qs__/`` (e.g.
``/v3/account/__qs__/account-type/aws``). These transports rewrite that
synthetic path back to a real query string before the request goes out — the
Python analogue of the go lane's ``queryStringRewriter``. Without them requests
would hit the synthetic (non-existent) URL and Kion would 404.
"""

from __future__ import annotations

import httpx

# MUST match queryStringPathMarker in preprocess/main.go and the go lane's client.go.
_MARKER = "/__qs__/"


def _rewrite_url(url: httpx.URL) -> httpx.URL:
    """Return ``url`` with a ``/__qs__/key/value/...`` path segment folded back
    into query parameters. Returns the URL unchanged if the marker is absent."""
    path = url.path
    idx = path.find(_MARKER)
    if idx < 0:
        return url
    suffix = path[idx + len(_MARKER) :]
    new_path = path[:idx] or "/"
    parts = suffix.split("/")
    new_url = url.copy_with(path=new_path)
    # Merge onto any existing query params (Set semantics, like the go lane).
    for i in range(0, len(parts) - 1, 2):
        new_url = new_url.copy_set_param(parts[i], parts[i + 1])
    return new_url


class QueryStringRewriteTransport(httpx.BaseTransport):
    """Sync transport wrapper that folds ``/__qs__/`` markers into query params."""

    def __init__(self, inner: httpx.BaseTransport) -> None:
        self._inner = inner

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.url = _rewrite_url(request.url)
        return self._inner.handle_request(request)

    def close(self) -> None:
        self._inner.close()


class AsyncQueryStringRewriteTransport(httpx.AsyncBaseTransport):
    """Async counterpart of :class:`QueryStringRewriteTransport`."""

    def __init__(self, inner: httpx.AsyncBaseTransport) -> None:
        self._inner = inner

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        request.url = _rewrite_url(request.url)
        return await self._inner.handle_async_request(request)

    async def aclose(self) -> None:
        await self._inner.aclose()
