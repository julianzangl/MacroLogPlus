"""Data checks + versioned exclusion list (HLD 3.2).

Rules: missing/unreadable images, contradicting metadata (ingredient sum vs. total),
non-positive mass or energy (pre-check: 240 of 5,006 dishes), energy density > 9 kcal/g.
Every exclusion is logged with rule + reason → ml/data/exclusions.csv (part of the data version).
"""

from __future__ import annotations
