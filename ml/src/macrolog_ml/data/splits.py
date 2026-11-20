"""Grouped splits (HLD 3.3): ~15 % of the plate groups of the official train split
(fixed seed) become the validation set; a group is always entirely in one subset.
Group candidates across the official train/test border are discarded and documented."""

from __future__ import annotations

VALIDATION_FRACTION = 0.15
