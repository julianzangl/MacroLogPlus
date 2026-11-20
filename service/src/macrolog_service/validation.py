"""Upload validation (SRS 4.5.1, HLD 5.2/5.3): content type image/jpeg (415), body ≤ 10 MB read
with a size limit (413), decodable image with plausible dimensions + pixel cap (400).
The photo is read as raw request body (no multipart) and kept in memory only (FR-14)."""

from __future__ import annotations
