"""Problem details (RFC 9457) for every error response (ADR 0001 §5, HLD 5.3).

Never expose internal details such as stack traces – they only go to the service log.
"""

from __future__ import annotations

import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from macrolog_service.request_id import REQUEST_ID_HEADER, get_request_id
from macrolog_service.schemas import Problem, ProblemCode

PROBLEM_MEDIA_TYPE = "application/problem+json"
PROBLEM_TYPE_BASE = "https://github.com/julianzangl/MacroLogPlus/blob/main/docs/api/problems.md"

PROBLEMS: dict[ProblemCode, tuple[int, str]] = {
    "invalid_image": (400, "Invalid image"),
    "invalid_image_dimensions": (400, "Invalid image dimensions"),
    "unauthorized": (401, "Unauthorized"),
    "not_found": (404, "Not found"),
    "method_not_allowed": (405, "Method not allowed"),
    "payload_too_large": (413, "Payload too large"),
    "unsupported_media_type": (415, "Unsupported media type"),
    "validation_error": (422, "Validation error"),
    "rate_limited": (429, "Too many requests"),
    "internal_error": (500, "Internal error"),
    "model_unavailable": (503, "Model unavailable"),
}
_CODE_BY_STATUS: dict[int, ProblemCode] = {404: "not_found", 405: "method_not_allowed"}

logger = logging.getLogger(__name__)


class ApiError(Exception):
    """Raise anywhere in a request to return a problem response."""

    def __init__(
        self,
        code: ProblemCode,
        detail: str | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.code = code
        self.status, self.title = PROBLEMS[code]
        self.detail = detail or self.title
        self.headers = headers or {}
        super().__init__(f"{code}: {self.detail}")


def problem_response(
    request: Request,
    code: ProblemCode,
    detail: str | None = None,
    headers: dict[str, str] | None = None,
) -> JSONResponse:
    status, title = PROBLEMS[code]
    body = Problem(
        type=f"{PROBLEM_TYPE_BASE}#{code}",
        title=title,
        status=status,
        detail=detail or title,
        code=code,
        request_id=get_request_id(request),
    )
    # set here as well: unhandled errors are rendered outside of RequestIdMiddleware
    all_headers = {**(headers or {}), REQUEST_ID_HEADER: body.request_id}
    return JSONResponse(
        body.model_dump(),
        status_code=status,
        headers=all_headers,
        media_type=PROBLEM_MEDIA_TYPE,
    )


def install_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(ApiError)
    async def _api_error(request: Request, exc: ApiError) -> JSONResponse:
        return problem_response(request, exc.code, exc.detail, exc.headers)

    @app.exception_handler(StarletteHTTPException)
    async def _http_error(request: Request, exc: StarletteHTTPException) -> JSONResponse:
        code = _CODE_BY_STATUS.get(exc.status_code, "internal_error")
        return problem_response(request, code)

    @app.exception_handler(RequestValidationError)
    async def _validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
        return problem_response(request, "validation_error")

    @app.exception_handler(Exception)
    async def _unhandled(request: Request, exc: Exception) -> JSONResponse:
        logger.exception("unhandled error", extra={"request_id": get_request_id(request)})
        return problem_response(request, "internal_error")
