"""Contract tests (ADR 0001 §1): example JSONs in docs/api must match the Pydantic models."""

import json
from pathlib import Path

import pytest

from macrolog_service.errors import PROBLEM_TYPE_BASE, PROBLEMS
from macrolog_service.openapi_export import DEFAULT_OUT, render
from macrolog_service.schemas import (
    EstimateResponse,
    HealthResponse,
    ModelInfoResponse,
    Problem,
)

REPO = Path(__file__).resolve().parents[2]
API_DOCS = REPO / "docs" / "api"


@pytest.mark.parametrize(
    ("file", "model"),
    [
        ("estimate-response.example.json", EstimateResponse),
        ("health-response.example.json", HealthResponse),
        ("model-info-response.example.json", ModelInfoResponse),
        ("error-response.example.json", Problem),
    ],
)
def test_examples_match_models(file, model):
    model.model_validate(json.loads((API_DOCS / file).read_text(encoding="utf-8")))


def test_openapi_export_is_up_to_date():
    assert (REPO / DEFAULT_OUT).read_text(encoding="utf-8") == render(), (
        "run: uv run python -m macrolog_service.openapi_export"
    )


def test_every_problem_code_is_documented():
    problems_md = (API_DOCS / "problems.md").read_text(encoding="utf-8")
    for code in PROBLEMS:
        assert f"### {code}\n" in problems_md, f"missing section for {code}"
    assert PROBLEM_TYPE_BASE.endswith("docs/api/problems.md")


def test_error_responses_use_problem_media_type():
    spec = json.loads(render())
    for path, ops in spec["paths"].items():
        for method, op in ops.items():
            for status, response in op["responses"].items():
                if int(status) < 400:
                    continue
                health_loading = path == "/v1/health" and status == "503"
                expected = "application/json" if health_loading else "application/problem+json"
                assert list(response["content"]) == [expected], (method, path, status)
