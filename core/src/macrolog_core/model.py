"""Model construction (HLD 3.5): ResNet-50 (ImageNet weights, torchvision) + small regression head.

Variants differ only in the number/meaning of outputs k (A: 4, B: 5, C: 5).
Softplus at the output prevents negative values. Variant is a config value only (FR-16).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from macrolog_core.types import Variant

if TYPE_CHECKING:
    from torch import nn

FEATURE_DIM = 2048


def build_model(variant: Variant, pretrained: bool = True) -> nn.Module:
    """Build ResNet-50 backbone + regression head for the given variant.

    The module should expose both the 2048-dim features (needed for σ(x), HLD 3.8)
    and the k outputs.
    """
    raise NotImplementedError
