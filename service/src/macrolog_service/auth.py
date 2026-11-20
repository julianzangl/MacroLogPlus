"""API key check (FR-13, TS-06, HLD 7): header X-API-Key, constant-time comparison
(hmac.compare_digest), keys exchangeable via env. Rate limiting per key → ratelimit.py."""

from __future__ import annotations

API_KEY_HEADER = "X-API-Key"


def require_api_key() -> None:
    """FastAPI dependency – raise ApiError(401) for missing/invalid key."""
    raise NotImplementedError
