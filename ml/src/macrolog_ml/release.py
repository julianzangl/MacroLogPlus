"""Pipeline step `release` (HLD 3.9): export artifact (state_dict, config, calibration,
reference features, metrics, checksums), model card, release check (SRS 4.3 targets,
TS-08 with the real model, latency on the project server), transfer to the registry via rsync."""

from __future__ import annotations
