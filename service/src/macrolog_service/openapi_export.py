"""Export the OpenAPI document to docs/api/openapi.json (ADR 0001 §1).

uv run python -m macrolog_service.openapi_export          # write
uv run python -m macrolog_service.openapi_export --check  # CI: fail if outdated
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from pathlib import Path

from macrolog_service.main import create_app

DEFAULT_OUT = Path("docs/api/openapi.json")


def render() -> str:
    spec = create_app(load_model=False).openapi()
    return json.dumps(spec, indent=2, ensure_ascii=False) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--check", action="store_true", help="fail if the file is outdated")
    args = parser.parse_args(argv)

    text = render()
    if args.check:
        current = args.out.read_text(encoding="utf-8") if args.out.exists() else ""
        if current != text:
            print(
                f"{args.out} is outdated – run: uv run python -m macrolog_service.openapi_export",
                file=sys.stderr,
            )
            return 1
        print(f"{args.out} is up to date")
        return 0
    args.out.write_text(text, encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
