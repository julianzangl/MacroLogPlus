"""macrolog_core – shared inference core of MacroLog+ (HLD 2.4).

Single implementation of preprocessing, model construction, output conversion and
conformal calibration. Used by the inference service *and* the ML pipeline so that
training, evaluation and production compute identical values (FR-15, TS-08).
"""

from macrolog_core.types import (
    MASS_TARGET,
    TOTAL_TARGETS,
    ConfidenceLevel,
    EstimateResult,
    Interval,
    Variant,
)

__version__ = "0.1.0"

__all__ = [
    "MASS_TARGET",
    "TOTAL_TARGETS",
    "ConfidenceLevel",
    "EstimateResult",
    "Interval",
    "Variant",
    "__version__",
]
