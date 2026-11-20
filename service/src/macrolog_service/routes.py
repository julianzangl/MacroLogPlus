"""REST endpoints under /v1 (HLD 5.2)."""

from __future__ import annotations

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from macrolog_service.errors import ApiError
from macrolog_service.schemas import EstimateResponse, HealthResponse, ModelInfoResponse

router = APIRouter(prefix="/v1")


@router.get("/health", response_model=HealthResponse)
async def health(request: Request):
    state = request.app.state.model
    if not state.ready:
        body = HealthResponse(status="loading", model_version=None)
        return JSONResponse(body.model_dump(), status_code=503)
    return HealthResponse(status="ok", model_version=state.estimator.version)


@router.get("/model", response_model=ModelInfoResponse)
async def model_info(request: Request):
    # TODO: version, variant, training date, validation MAE, coverage, model card summary
    raise ApiError(503, "model not loaded")


@router.post("/estimate", response_model=EstimateResponse)
async def estimate(request: Request):
    # TODO: auth → validation → macrolog_core estimate → response + log (HLD 4.2 steps 4–6)
    raise ApiError(503, "model not loaded")
