from pathlib import Path

from fastapi.testclient import TestClient

from macrolog_service.config import Settings
from macrolog_service.main import create_app


def _client() -> TestClient:
    settings = Settings(
        registry_path=Path("/nonexistent"),
        model_version=None,
        api_keys=("test-key",),
        rate_limit_per_minute=30,
        log_dir=Path("/tmp"),
    )
    return TestClient(create_app(settings, load_model=False))


def test_health_reports_loading_without_model():
    with _client() as client:
        res = client.get("/v1/health")
    assert res.status_code == 503
    assert res.json() == {"status": "loading", "model_version": None}
    assert res.headers["X-Request-ID"]


def test_estimate_without_model_returns_problem_details():
    with _client() as client:
        res = client.post("/v1/estimate", content=b"", headers={"Content-Type": "image/jpeg"})
    assert res.status_code == 503
    assert res.headers["content-type"] == "application/problem+json"
    assert res.headers["Retry-After"] == "10"
    body = res.json()
    assert body["code"] == "model_unavailable"
    assert body["status"] == 503
    assert body["type"].endswith("problems.md#model_unavailable")
    assert body["request_id"] == res.headers["X-Request-ID"]


def test_unknown_path_returns_problem_details():
    with _client() as client:
        res = client.get("/v1/does-not-exist")
    assert res.status_code == 404
    assert res.headers["content-type"] == "application/problem+json"
    assert res.json()["code"] == "not_found"


def test_request_ids_are_unique_and_not_taken_from_client():
    with _client() as client:
        a = client.get("/v1/health", headers={"X-Request-ID": "spoofed"})
        b = client.get("/v1/health")
    assert a.headers["X-Request-ID"] != "spoofed"
    assert a.headers["X-Request-ID"] != b.headers["X-Request-ID"]
