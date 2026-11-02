"""Server URL normalization (mirrors the go lane's ``NormalizeServerURL``)."""

from __future__ import annotations


def normalize_server_url(base_url: str) -> str:
    """Force the Kion ``/api`` suffix, tolerating a trailing slash.

    ``https://kion.example.com`` and ``https://kion.example.com/`` both become
    ``https://kion.example.com/api``; an existing ``/api`` suffix is left alone.
    """
    server = base_url.rstrip("/")
    if not server.endswith("/api"):
        server += "/api"
    return server
