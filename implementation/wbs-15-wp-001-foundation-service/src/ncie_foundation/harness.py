"""Deterministic in-process harness with no network listener or external service."""

import json
from dataclasses import dataclass
from typing import Any

from .composition import ComposedFoundationService


@dataclass(frozen=True, slots=True)
class InProcessResponse:
    status_code: int
    payload: dict[str, Any]
    headers: tuple[tuple[bytes, bytes], ...]


class InProcessHarness:
    def __init__(self, service: ComposedFoundationService) -> None:
        self._service = service

    async def start(self) -> None:
        await self._service.start()

    async def stop(self) -> None:
        await self._service.stop()

    async def request(
        self,
        path: str,
        *,
        method: str = "GET",
        correlation_id: str | None = None,
        headers: tuple[tuple[bytes, bytes], ...] = (),
    ) -> InProcessResponse:
        messages: list[dict[str, Any]] = []
        request_headers = list(headers)
        if correlation_id is not None:
            request_headers.append((b"x-correlation-id", correlation_id.encode("utf-8")))

        async def receive() -> dict[str, Any]:
            return {"type": "http.request", "body": b"", "more_body": False}

        async def send(message: dict[str, Any]) -> None:
            messages.append(message)

        await self._service.app(
            {"type": "http", "method": method, "path": path, "headers": request_headers},
            receive,
            send,
        )
        if len(messages) != 2:
            raise RuntimeError("In-process application emitted an invalid response sequence")
        start, body = messages
        return InProcessResponse(
            status_code=int(start["status"]),
            payload=json.loads(body["body"]),
            headers=tuple(start["headers"]),
        )
