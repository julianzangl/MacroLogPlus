"""API contract v1 – single source of truth (ADR 0001, HLD 5.2).

FastAPI exports these models as OpenAPI 3.1 (docs/api/openapi.json); the app generates its
TypeScript types from that file. Never edit app types by hand – change this module instead.
Within v1 only additive changes are allowed.
"""

from __future__ import annotations

from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Variant = Literal["A", "B", "C"]
ConfidenceLevel = Literal["high", "medium", "low"]
WarningCode = Literal["unusual_image", "low_light", "blurry", "implausible_values"]
HealthStatus = Literal["ok", "loading"]
ProblemCode = Literal[
    "invalid_image",
    "invalid_image_dimensions",
    "unauthorized",
    "not_found",
    "method_not_allowed",
    "payload_too_large",
    "unsupported_media_type",
    "validation_error",
    "rate_limited",
    "internal_error",
    "model_unavailable",
]


class _Model(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Interval(_Model):
    """Point estimate with 80 % prediction interval (unrounded, base units)."""

    value: float
    lower: float
    upper: float


class FactorRange(_Model):
    """Multipliers for the interval when the mass is known: total × lower … total × upper."""

    lower: float
    upper: float


class ModelRef(_Model):
    version: str = Field(description="Semantic version of the active model")
    variant: Variant


class Estimate(_Model):
    mass_g: Interval
    energy_kcal: Interval
    fat_g: Interval
    carbs_g: Interval
    protein_g: Interval


class PerGram(_Model):
    energy_kcal: float = Field(description="kcal per g")
    fat_g: float = Field(description="g per g")
    carbs_g: float = Field(description="g per g")
    protein_g: float = Field(description="g per g")


class KnownMassFactors(_Model):
    energy_kcal: FactorRange
    fat_g: FactorRange
    carbs_g: FactorRange
    protein_g: FactorRange


class EstimateResponse(_Model):
    request_id: str = Field(description="UUIDv4, also sent as X-Request-ID header")
    model: ModelRef
    coverage: float = Field(description="Nominal coverage of all intervals, e.g. 0.8")
    estimate: Estimate
    per_gram: PerGram
    known_mass_factors: KnownMassFactors
    confidence_level: ConfidenceLevel
    warnings: list[WarningCode] = Field(
        description="Machine codes; clients must ignore unknown codes"
    )


class HealthResponse(_Model):
    status: HealthStatus
    model_version: str | None


class TargetValues(_Model):
    mass_g: float
    energy_kcal: float
    fat_g: float
    carbs_g: float
    protein_g: float


class DatasetInfo(_Model):
    name: str
    license: str
    url: str
    data_version: str = Field(description="Short hash of the data manifest")


class CoverageInfo(_Model):
    nominal: float
    validation: float = Field(description="Empirical coverage on the validation set")


class ModelInfoResponse(_Model):
    version: str
    variant: Variant
    trained_at: date
    dataset: DatasetInfo
    coverage: CoverageInfo
    validation_mae: TargetValues = Field(description="MAE on the validation set (g / kcal)")
    validation_mae_percent: TargetValues = Field(
        description="MAE relative to the mean reference value, as fraction (0.36 = 36 %)"
    )
    model_card_summary: str = Field(description="Short German summary, maintained by the ML team")


class Problem(BaseModel):
    """RFC 9457 problem details (media type application/problem+json)."""

    type: str = Field(description="URI of the problem description (docs/api/problems.md)")
    title: str
    status: int
    detail: str = Field(description="Developer-facing only – never shown to users")
    code: ProblemCode
    request_id: str
