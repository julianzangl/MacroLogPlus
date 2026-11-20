from pathlib import Path

from fastapi.testclient import TestClient

from macrolog_service.config import Settings
from macrolog_service.main import create_app


def _settings() -> Settings:
    return Settings(
        registry_path=Path("/nonexistent"),
        model_version=None,
        api_keys=("test-key",),
        rate_limit_per_minute=30,
        log_dir=Path("/tmp"),
    )


def test_health_reports_loading_without_model():
    with TestClient(create_app(_settings(), load_model=False)) as client:
        res = client.get("/v1/health")
    assert res.status_code == 503
    assert res.json() == {"status": "loading", "model_version": None}


def test_estimate_without_model_returns_uniform_error():
    with TestClient(create_app(_settings(), load_model=False)) as client:
        res = client.post("/v1/estimate", content=b"", headers={"Content-Type": "image/jpeg"})
    assert res.status_code == 503
    body = res.json()["error"]
    assert body["code"] == 503
    assert body["request_id"]
