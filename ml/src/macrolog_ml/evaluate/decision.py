"""Decision rule with 5 kcal margin (HLD 3.7, TS-09).

interval entirely < −5  → first variant better
interval entirely > +5  → second variant better
interval entirely within ±5 → equivalent
otherwise → undecided
"""

from __future__ import annotations

from enum import StrEnum

MARGIN_KCAL = 5.0


class Decision(StrEnum):
    FIRST_BETTER = "first_better"
    SECOND_BETTER = "second_better"
    EQUIVALENT = "equivalent"
    UNDECIDED = "undecided"


def decide(lower: float, upper: float, margin: float = MARGIN_KCAL) -> Decision:
    raise NotImplementedError
