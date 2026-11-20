"""FastAPI application factory. Run: `uvicorn macrolog_service.main:app`."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from macrolog_service.auth import API_KEY_HEADER
from macrolog_service.config import Settings
from macrolog_service.errors import PROBLEM_MEDIA_TYPE, install_error_handlers
from macrolog_service.request_id import RequestIdMiddleware
from macrolog_service.routes import router
from macrolog_service.state import ModelState

API_TITLE = "MacroLog+ Inferenzdienst"
API_VERSION = "1.0.0"  # version of the API contract (ADR 0001), not of the package


def _custom_openapi(app: FastAPI) -> dict[str, Any]:
    """OpenAPI 3.1 with API-key security and RFC 9457 media type for error responses."""
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(
        title=API_TITLE,
        version=API_VERSION,
        description="API contract v1 between the MacroLog+ app and the inference service.",
        routes=app.routes,
    )
    schema.setdefault("components", {})["securitySchemes"] = {
        "ApiKeyAuth": {"type": "apiKey", "in": "header", "name": API_KEY_HEADER}
    }
    schema["security"] = [{"ApiKeyAuth": []}]
    for path in schema.get("paths", {}).values():
        for operation in path.values():
            for status, response in operation.get("responses", {}).items():
                content = response.get("content", {})
                is_problem = "Problem" in str(content.get("application/json", {}))
                if int(status) >= 400 and is_problem:
                    content[PROBLEM_MEDIA_TYPE] = content.pop("application/json")
    app.openapi_schema = schema
    return schema


def create_app(settings: Settings | None = None, load_model: bool = True) -> FastAPI:
    settings = settings or Settings.from_env()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.settings = settings
        app.state.model = ModelState()
        if load_model and settings.model_version:
            # TODO(#22): load from registry, verify manifest, warm-up (HLD 2.3)
            pass
        yield

    app = FastAPI(title=API_TITLE, version=API_VERSION, lifespan=lifespan)
    app.add_middleware(RequestIdMiddleware)
    install_error_handlers(app)
    app.include_router(router)
    app.openapi = lambda: _custom_openapi(app)  # type: ignore[method-assign]
    return app


app = create_app()
