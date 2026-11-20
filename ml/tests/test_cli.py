from macrolog_ml.cli import STEPS, build_parser
from macrolog_ml.evaluate.decision import MARGIN_KCAL


def test_cli_knows_all_pipeline_steps():
    parser = build_parser()
    for step in STEPS:
        assert parser.parse_args([step, "--config", "x.yaml"]).step == step


def test_margin():
    assert MARGIN_KCAL == 5.0
