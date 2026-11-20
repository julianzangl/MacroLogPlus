"""SHA-256 manifest of the mirrored Nutrition5k excerpt (HLD 3.1, 4.1.1).

Manifest (path, size, checksum per file) lives in git: ml/data/manifest.csv.
Every pipeline run verifies the data against it and aborts on mismatch.
Raw data never lives in the repository.
"""

from __future__ import annotations

from pathlib import Path


def build_manifest(data_root: Path) -> list[tuple[str, int, str]]:
    raise NotImplementedError


def verify(data_root: Path, manifest_path: Path) -> str:
    """Verify files and return the manifest hash (= data version)."""
    raise NotImplementedError
