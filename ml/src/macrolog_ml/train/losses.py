"""Losses (HLD 3.6): mean absolute error per target, normalised with the training scale.
B: per-gram error weighted with the reference mass (same unit as a total).
B and C weight the mass error equally."""

from __future__ import annotations
