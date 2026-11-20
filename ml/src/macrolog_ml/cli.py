"""Command line entry point: `macrolog-ml <step> --config <yaml>` (HLD 2.5).

Steps: prepare → split → train → evaluate → calibrate → release.
Every step reads a versioned YAML config and writes into a run directory.
Runs on Google Colab (CUDA) or locally on Apple Silicon (MPS).
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence

STEPS = ("prepare", "split", "train", "evaluate", "calibrate", "release")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="macrolog-ml", description=__doc__)
    sub = parser.add_subparsers(dest="step", required=True)
    for step in STEPS:
        p = sub.add_parser(step)
        p.add_argument("--config", required=True, help="path to YAML config")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    raise NotImplementedError(f"step '{args.step}' is not implemented yet")


if __name__ == "__main__":
    raise SystemExit(main())
