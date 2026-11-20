"""Pydantic response models = API contract (HLD 5.2).

Keep in sync with app/src/services/api/types.ts and docs/api/*.example.json.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

Variant = Literal["A", "B", "C"]
ConfidenceLevel = Literal["hoch", "mittel", "niedrig"]


class IntervalOut(BaseModel):
    value: float
    lower: float
    upper: float


class FactorRangeOut(BaseModel):
    lower: float
    upper: float


class ModelRef(BaseModel):
    version: str
    variant: Variant


class EstimateOut(BaseModel):
    mass_g: IntervalOut
    energy_kcal: IntervalOut
    fat_g: IntervalOut
    carbs_g: IntervalOut
    protein_g: IntervalOut


class PerGramOut(BaseModel):
    energy_kcal: float
    fat_g: float
    carbs_g: float
    protein_g: float


class KnownMassFactorsOut(BaseModel):
    energy_kcal: FactorRangeOut
    fat_g: FactorRangeOut
    carbs_g: FactorRangeOut
    protein_g: FactorRangeOut


class EstimateResponse(BaseModel):
    request_id: str
    model: ModelRef
    coverage: float
    estimate: EstimateOut
    per_gram: PerGramOut
    known_mass_factors: KnownMassFactorsOut
    confidence_level: ConfidenceLevel
    warnings: list[str]


class HealthResponse(BaseModel):
    status: Literal["ok", "loading"]
    model_version: str | None


class ModelInfoResponse(BaseModel):
    version: str
    variant: Variant
    trained_at: str
    validation_mae: dict[str, float]
    coverage: float
    model_card_summary: str


class ErrorBody(BaseModel):
    code: int
    message: str
    request_id: str


class ErrorResponse(BaseModel):
    error: ErrorBody
