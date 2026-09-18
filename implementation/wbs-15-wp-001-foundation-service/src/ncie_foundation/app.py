"""Dependency-free ASGI foundation for NCIE WBS-15-WP-001."""

import json
import os
from collections.abc import Awaitable, Callable
from datetime import UTC, datetime
from typing import Any

from .authorization import AuthorizationBoundary, DenyAllAuthorization
from .config import FoundationSettings
from .correlation import correlation_id_from_headers
from .readiness import ReadinessBoundary, StaticReadiness
from .telemetry import NoOpTelemetryHooks, TelemetryContext, TelemetryHooks

Scope = dict[str, Any]
Message = dict[str, Any]
Receive = Callable[[], Awaitable[Message]]
Send = Callable[[Message], Awaitable[None]]


class FoundationApp:
    def __init__(
        self,
        *,
        settings: FoundationSettings | None = None,
        authorization: AuthorizationBoundary | None = None,
        telemetry: TelemetryHooks | None = None,
        readiness: ReadinessBoundary | None = None,
        application_dependencies_ready: bool | None = None,
    ) -> None:
        if readiness is not None and application_dependencies_ready is not None:
            raise ValueError("Specify readiness or application_dependencies_ready, not both")
        self._settings = settings or FoundationSettings.from_environment(os.environ)
        self._authorization = authorization or DenyAllAuthorization()
        self._telemetry = telemetry or NoOpTelemetryHooks()
        self._readiness = readiness or StaticReadiness(
            ready=False
            if application_dependencies_ready is None
            else application_dependencies_ready
        )

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        del receive
        if scope.get("type") != "http":
            return

        method = str(scope.get("method", "GET")).upper()
        path = str(scope.get("path", "/"))
        headers = list(scope.get("headers", []))
        correlation_id = correlation_id_from_headers(headers)
        context = TelemetryContext(correlation_id=correlation_id)
        self._telemetry.request_started(context, method=method, path=path)

        if method == "GET" and path == "/health/live":
            status_code = 200
            payload = self._health_payload(status="UP", ready=None)
        elif method == "GET" and path == "/health/ready":
            application_dependencies_ready = self._readiness.snapshot().ready
            status_code = 200 if application_dependencies_ready else 503
            payload = self._health_payload(
                status="READY" if application_dependencies_ready else "NOT_READY",
                ready=application_dependencies_ready,
            )
        elif correlation_id is None:
            status_code = 400
            payload = self._problem(
                status=status_code,
                title="Missing correlation ID",
                detail="X-Correlation-ID is required for non-probe requests",
                correlation_id=None,
            )
        else:
            authorization = self._authorization.authorize(
                correlation_id=correlation_id,
                method=method,
                path=path,
            )
            if not authorization.allowed:
                status_code = 403
                payload = self._problem(
                    status=status_code,
                    title="Authorization denied",
                    detail=authorization.reason,
                    correlation_id=correlation_id,
                )
            else:
                status_code = 404
                payload = self._problem(
                    status=status_code,
                    title="Route not found",
                    detail="No application route is registered in the foundation package",
                    correlation_id=correlation_id,
                )

        await self._send_json(send, status_code, payload, correlation_id)
        self._telemetry.request_finished(context, status_code=status_code)

    def _health_payload(self, *, status: str, ready: bool | None) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "category": "PLATFORM_HEALTH",
            "service": self._settings.service_name,
            "environment": self._settings.environment_name,
            "status": status,
            "lastUpdated": datetime.now(tz=UTC).isoformat(),
            "authoritativeBusinessState": False,
            "businessCorrectness": "NOT_ESTABLISHED",
            "testAcceptance": "PENDING",
            "productionAcceptance": "PENDING",
        }
        if ready is not None:
            payload["ready"] = ready
        return payload

    @staticmethod
    def _problem(
        *,
        status: int,
        title: str,
        detail: str,
        correlation_id: str | None,
    ) -> dict[str, Any]:
        return {
            "type": "about:blank",
            "title": title,
            "status": status,
            "detail": detail,
            "correlationId": correlation_id,
        }

    @staticmethod
    async def _send_json(
        send: Send,
        status_code: int,
        payload: dict[str, Any],
        correlation_id: str | None,
    ) -> None:
        response_headers: list[tuple[bytes, bytes]] = [
            (b"content-type", b"application/json"),
            (b"cache-control", b"no-store"),
        ]
        if correlation_id is not None:
            response_headers.append((b"x-correlation-id", correlation_id.encode("utf-8")))
        await send(
            {
                "type": "http.response.start",
                "status": status_code,
                "headers": response_headers,
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8"),
            }
        )


app = FoundationApp()
