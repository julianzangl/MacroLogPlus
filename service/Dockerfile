# Inference service image (HLD 2.7, 7): CPU-only torch, non-root, read-only rootfs in compose.
# Build context = repository root:  docker build -f service/Dockerfile .
FROM python:3.12-slim AS base

COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /usr/local/bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PROJECT_ENVIRONMENT=/opt/venv

WORKDIR /src
COPY pyproject.toml uv.lock .python-version ./
COPY core core
COPY ml/pyproject.toml ml/pyproject.toml
COPY service service
RUN uv sync --frozen --no-dev --no-editable --package macrolog-service

FROM python:3.12-slim
RUN useradd --system --uid 10001 app
COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" PYTHONUNBUFFERED=1
USER app
EXPOSE 8000
CMD ["uvicorn", "macrolog_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
