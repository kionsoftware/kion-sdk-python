"""Kion API version metadata.

Lives in the wrapper (not in a generated `kion_sdk.<v>` package) because those
directories are deleted and re-created on every regeneration.
"""

from __future__ import annotations

from .releases import KION_RELEASES

# Which Kion release each generated sub-package targets. The SDK ships every
# supported Kion version at once — a single consumer routinely imports several —
# which is why the SDK's own version cannot be a Kion version.
KION_VERSIONS: dict[str, str] = {
    "v3_14": "3.14",
    "v3_15": "3.15",
    "v3_16": "3.16",
    "v3_17": "3.17",
}


def kion_version(sub_package: str) -> str | None:
    """Return the Kion release for a sub-package name (``"v3_16"`` -> ``"3.16"``)."""
    return KION_VERSIONS.get(sub_package)


def kion_release(sub_package: str) -> str | None:
    """Return the exact Kion release a sub-package was generated from (``"v3_17"`` -> ``"3.17.1"``)."""
    return KION_RELEASES.get(sub_package)
