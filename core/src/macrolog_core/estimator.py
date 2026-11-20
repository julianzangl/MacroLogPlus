"""Public Python API of the inference core (HLD 5.4).

    model   = load_model(registry_path, version)  # verifies manifest, loads weights
    result  = model.estimate(image_bytes)         # one image (inference service)
    results = model.estimate_batch(images)        # many images (evaluation)

`estimate()` is stateless and deterministic: same image + same model version → same output.
TS-08 compares both paths on 20 validation images (tolerance < 1e-4).
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from macrolog_core.types import EstimateResult


class Estimator:
    version: str

    def estimate(self, image_bytes: bytes) -> EstimateResult:
        raise NotImplementedError

    def estimate_batch(self, images: Sequence[bytes]) -> list[EstimateResult]:
        raise NotImplementedError


def load_model(registry_path: Path, version: str, device: str = "cpu") -> Estimator:
    raise NotImplementedError
