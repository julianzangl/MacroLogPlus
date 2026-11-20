"""Holds the loaded model. On startup: load MODEL_VERSION from the registry, verify SHA-256,
run a warm-up inference – only then /v1/health reports "ok" (HLD 2.3)."""

from __future__ import annotations

from dataclasses import dataclass

from macrolog_core.estimator import Estimator


@dataclass
class ModelState:
    estimator: Estimator | None = None

    @property
    def ready(self) -> bool:
        return self.estimator is not None
