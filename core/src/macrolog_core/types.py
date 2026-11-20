"""Core data types shared by service and pipeline (HLD 5.2, 5.4)."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Literal

TOTAL_TARGETS: tuple[str, ...] = ("energy_kcal", "fat_g", "carbs_g", "protein_g")
MASS_TARGET = "mass_g"
ALL_TARGETS: tuple[str, ...] = (MASS_TARGET, *TOTAL_TARGETS)

# language-neutral codes; the app renders "hoch/mittel/niedrig" (ADR 0001 §3)
ConfidenceLevel = Literal["high", "medium", "low"]


class Variant(StrEnum):
    """Model variants (HLD 3.5). Same architecture, only the regression head differs."""

    A = "A"  # 4 totals directly – comparison only
    B = "B"  # mass + 4 per-gram values, totals = mass × per gram
    C = "C"  # 4 totals + mass as auxiliary task

    @property
    def num_outputs(self) -> int:
        return 4 if self is Variant.A else 5

    @property
    def predicts_mass(self) -> bool:
        return self is not Variant.A


@dataclass(frozen=True)
class Interval:
    value: float
    lower: float
    upper: float


@dataclass(frozen=True)
class EstimateResult:
    """Result of `Estimator.estimate()` – maps 1:1 onto the JSON response (HLD 5.2)."""

    model_version: str
    variant: Variant
    coverage: float
    estimate: dict[str, Interval]
    per_gram: dict[str, float]
    known_mass_factors: dict[str, tuple[float, float]]
    confidence_level: ConfidenceLevel
    warnings: list[str] = field(default_factory=list)
    # 2048-dim ResNet-50 feature vector; only kept for batch evaluation / monitoring
    features: list[float] | None = None
