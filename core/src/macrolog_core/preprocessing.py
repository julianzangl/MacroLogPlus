"""Image preprocessing – the ONLY implementation for training, evaluation and serving (HLD 3.4).

Pipeline: decode RGB → centre crop 1:1 → resize 224×224 → ImageNet normalisation.
Training-only augmentation: horizontal/vertical flip, rotation by multiples of 90°,
light colour jitter. Deliberately NO zoom / random crop / scaling – visible size encodes portion.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import torch
    from PIL import Image

IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)
INPUT_SIZE = 224
# upper bound against decompression bombs (HLD 7)
MAX_IMAGE_PIXELS = 40_000_000


def decode_image(image_bytes: bytes) -> Image.Image:
    """Decode JPEG bytes in memory into an RGB PIL image. Raise ValueError if invalid."""
    raise NotImplementedError


def center_crop_square(image: Image.Image) -> Image.Image:
    """Centre crop to aspect ratio 1:1 (matches the overlay frame of the app's capture aid)."""
    raise NotImplementedError


def preprocess(image: Image.Image) -> torch.Tensor:
    """Crop, resize and normalise one image → tensor of shape (3, 224, 224)."""
    raise NotImplementedError


def train_augmentation():
    """Return the training-only augmentation transform (applied before `preprocess`)."""
    raise NotImplementedError
