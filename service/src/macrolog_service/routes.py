"""REST endpoints under /v1 (HLD 5.2, ADR 0001)."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from macrolog_service.errors import ApiError
from macrolog_service.schemas import (
    EstimateResponse,
    HealthResponse,
    ModelInfoResponse,
    Problem,
)

router = APIRouter(prefix="/v1")

MODEL_UNAVAILABLE_RETRY_AFTER_S = "10"


def _problems(*statuses: int) -> dict[int | str, dict[str, Any]]:
    """Document problem responses in OpenAPI (media type is fixed in main._custom_openapi)."""
    return {s: {"model": Problem} for s in (401, 429, 500, *statuses)}


@router.get(
    "/health",
    response_model=HealthResponse,
    responses={503: {"model": HealthResponse, "description": "Model is loading"}, **_problems()},
)
async def health(request: Request):
    state = request.app.state.model
    if not state.ready:
        body = HealthResponse(status="loading", model_version=None)
        return JSONResponse(body.model_dump(), status_code=503)
    return HealthResponse(status="ok", model_version=state.estimator.version)


@router.get("/model", response_model=ModelInfoResponse, responses=_problems(503))
async def model_info(request: Request):
    # TODO(#22): version, variant, training date, dataset, coverage, MAE, model card summary
    raise ApiError("model_unavailable", headers={"Retry-After": MODEL_UNAVAILABLE_RETRY_AFTER_S})


@router.post(
    "/estimate",
    response_model=EstimateResponse,
    responses=_problems(400, 413, 415, 503),
    openapi_extra={
        "requestBody": {
            "required": True,
            "description": "Raw JPEG bytes (no multipart), max. 10 MB, edges 224–4096 px",
            "content": {"image/jpeg": {"schema": {"type": "string", "format": "binary"}}},
        }
    },
)
async def estimate(request: Request):
    # TODO(#21, #22): auth → validation → macrolog_core estimate → response
    # (+ Cache-Control: no-store) → request log (HLD 4.2 steps 4–6)
    raise ApiError("model_unavailable", headers={"Retry-After": MODEL_UNAVAILABLE_RETRY_AFTER_S})
