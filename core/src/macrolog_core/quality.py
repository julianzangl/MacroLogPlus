"""Image quality warnings (HLD 3.8, ADR 0001 §4).

Warning codes: "low_light", "blurry", "implausible_values" (> 9 kcal/g); "unusual_image" comes
from the calibration (σ(x) above the 95th validation percentile).
"""

from __future__ import annotations

MAX_ENERGY_DENSITY_KCAL_PER_G = 9.0  # pure fat


def brightness(image) -> float:
    raise NotImplementedError


def sharpness(image) -> float:
    """e.g. variance of the Laplacian."""
    raise NotImplementedError
