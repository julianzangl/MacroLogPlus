"""Service configuration from environment variables (SRS 4.5.3). Secrets never in the repo."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB (FR-13, TS-06)


@dataclass(frozen=True)
class Settings:
    registry_path: Path
    model_version: str | None
    api_keys: tuple[str, ...]
    rate_limit_per_minute: int
    log_dir: Path

    @classmethod
    def from_env(cls) -> Settings:
        keys = tuple(k for k in os.environ.get("API_KEYS", "").split(",") if k)
        return cls(
            registry_path=Path(os.environ.get("REGISTRY_PATH", "/registry")),
            model_version=os.environ.get("MODEL_VERSION") or None,
            api_keys=keys,
            rate_limit_per_minute=int(os.environ.get("RATE_LIMIT_PER_MINUTE", "30")),
            log_dir=Path(os.environ.get("LOG_DIR", "/logs")),
        )
