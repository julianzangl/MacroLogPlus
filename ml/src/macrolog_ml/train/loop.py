"""Training loop (HLD 3.6): AdamW, warm-up + cosine decay, mixed precision on GPU,
2 epochs head-only then full network, batch size 32, max 40 epochs,
checkpoint selection by lowest validation energy MAE, 5 fixed seeds per variant,
deterministic settings where supported, resumable checkpoints (Colab), ≤ 2 h per run."""

from __future__ import annotations
