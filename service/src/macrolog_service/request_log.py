"""Structured JSON log (FR-14, HLD 8.2).

Exactly one entry per request, WITHOUT image, IP address or user ID.

Fields: timestamp, request_id, endpoint, status, total + inference duration, model version,
file size + image dimensions, confidence level, warnings, estimated values (for monitoring).
Daily rotation, deletion after max. 90 days.
"""

from __future__ import annotations
