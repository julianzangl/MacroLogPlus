"""Request IDs (ADR 0001 §6): one UUIDv4 per request, generated server-side.

Stored on `request.state.request_id` and returned in the `X-Request-ID` response header.
Client-supplied IDs are ignored so that log correlation cannot be spoofed.
"""

from __future__ import annotations

import uuid

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

REQUEST_ID_HEADER = "X-Request-ID"


def get_request_id(request: Request) -> str:
    rid = getattr(request.state, "request_id", None)
    if rid is None:
        rid = str(uuid.uuid4())
        request.state.request_id = rid
    return rid


class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request.state.request_id = str(uuid.uuid4())
        response = await call_next(request)
        response.headers[REQUEST_ID_HEADER] = request.state.request_id
        return response
