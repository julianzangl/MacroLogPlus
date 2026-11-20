"""Target preparation (HLD 3.4): totals, per-gram values and training scales."""

from __future__ import annotations

from collections.abc import Mapping


def per_gram(totals: Mapping[str, float], mass_g: float) -> dict[str, float]:
    """Per-gram values = total / reference mass (kcal/g resp. g/g)."""
    raise NotImplementedError


def compute_scales(train_targets) -> dict[str, float]:
    """Mean of every target on the TRAINING split only; stored with the config."""
    raise NotImplementedError


def outputs_to_totals(outputs, variant) -> dict[str, float]:
    """Convert raw model outputs of variant A/B/C into totals (+ mass, per gram where available).

    B: totals = mass × per gram.  C: per gram = total / estimated mass.
    """
    raise NotImplementedError
