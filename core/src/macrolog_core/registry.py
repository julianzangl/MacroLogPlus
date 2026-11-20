"""Model registry access (HLD 2.5, 5.4).

registry/<semver>/
    weights.pt              state_dict: ResNet-50 + regression head
    config.yaml             variant, preprocessing, scales
    calibration.json        q per target, q_pg, confidence thresholds
    reference_features.npy  training features for σ(x)
    metrics.json            validation, test, latency
    model_card.md
    manifest.json           SHA-256 of all files, git commit, data hash

Versions are immutable and never overwritten (rollback = activate an older version).
"""

from __future__ import annotations

from pathlib import Path

ARTIFACT_FILES = (
    "weights.pt",
    "config.yaml",
    "calibration.json",
    "reference_features.npy",
    "metrics.json",
    "model_card.md",
)


def verify_manifest(artifact_dir: Path) -> None:
    """Check SHA-256 of every artifact file against manifest.json; raise on mismatch."""
    raise NotImplementedError


def write_manifest(artifact_dir: Path, git_commit: str, data_hash: str) -> None:
    raise NotImplementedError
