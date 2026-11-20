"""PyTorch dataset with TEST LOCK (HLD 3.3, TS-07).

Every requested dish ID is checked against the official test list. Test dishes are only
loaded in mode `final_test`, which only starts if a freeze tag (freeze-vX.Y) exists in the
repository AND the working tree is clean. Otherwise the run aborts with an error.
"""

from __future__ import annotations

from enum import StrEnum


class Mode(StrEnum):
    TRAIN = "train"
    VALIDATION = "validation"
    FINAL_TEST = "final_test"


class TestLockError(RuntimeError):
    """Raised when official test data is requested outside of `final_test` (TS-07)."""
