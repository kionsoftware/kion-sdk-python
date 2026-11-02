"""Version-agnostic error helpers (mirror the go lane's ``IsNotFound`` etc.).

They work on both a ``*_detailed`` ``Response`` (which carries ``.status_code``)
and an ``errors.UnexpectedStatus`` raised when a client is created with
``raise_on_unexpected_status=True``.
"""

from __future__ import annotations

from typing import Any


def status_code(obj: Any) -> int | None:
    """Return the HTTP status of a Response or UnexpectedStatus, else ``None``."""
    sc = getattr(obj, "status_code", None)
    if sc is None:
        return None
    try:
        return int(sc)
    except (TypeError, ValueError):
        return None


def is_not_found(obj: Any) -> bool:
    """True if ``obj`` represents a 404."""
    return status_code(obj) == 404


def is_auth_error(obj: Any) -> bool:
    """True if ``obj`` represents a 401 or 403."""
    return status_code(obj) in (401, 403)


def is_conflict(obj: Any) -> bool:
    """True if ``obj`` represents a 409."""
    return status_code(obj) == 409
