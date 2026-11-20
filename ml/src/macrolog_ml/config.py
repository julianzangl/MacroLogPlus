"""Load and validate YAML configs (configs/*.yaml).

The variant is a config value only (FR-16).
"""

from __future__ import annotations

from pathlib import Path


def load_config(path: Path) -> dict:
    raise NotImplementedError
