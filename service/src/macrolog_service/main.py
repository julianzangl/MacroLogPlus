"""FastAPI application factory. Run: `uvicorn macrolog_service.main:app`."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from macrolog_service import __version__
from macrolog_service.config import Settings
from macrolog_service.errors import install_error_handlers
from macrolog_service.routes import router
from macrolog_service.state import ModelState


def create_app(settings: Settings | None = None, load_model: bool = True) -> FastAPI:
    settings = settings or Settings.from_env()

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        app.state.settings = settings
        app.state.model = ModelState()
        if load_model and settings.model_version:
            # TODO: load from registry, verify manifest, warm-up (HLD 2.3)
            pass
        yield

    app = FastAPI(title="MacroLog+ Inferenzdienst", version=__version__, lifespan=lifespan)
    install_error_handlers(app)
    app.include_router(router)
    return app


app = create_app()
