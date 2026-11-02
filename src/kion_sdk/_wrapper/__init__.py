"""Version-agnostic wrapper for the generated Kion clients."""

from .client import new_client
from .errors import is_auth_error, is_conflict, is_not_found, status_code
from .urls import normalize_server_url
from .versions import KION_RELEASES, KION_VERSIONS, kion_release, kion_version

__all__ = [
    "KION_RELEASES",
    "KION_VERSIONS",
    "is_auth_error",
    "is_conflict",
    "is_not_found",
    "kion_release",
    "kion_version",
    "new_client",
    "normalize_server_url",
    "status_code",
]
