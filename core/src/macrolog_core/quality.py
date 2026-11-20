"""Image quality warnings (HLD 3.8): too dark, blurry, implausible values (> 9 kcal/g)."""

from __future__ import annotations

MAX_ENERGY_DENSITY_KCAL_PER_G = 9.0  # pure fat


def brightness(image) -> float:
    raise NotImplementedError


def sharpness(image) -> float:
    """e.g. variance of the Laplacian."""
    raise NotImplementedError
