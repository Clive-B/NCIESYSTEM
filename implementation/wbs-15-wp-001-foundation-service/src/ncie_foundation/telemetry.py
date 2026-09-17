"""Provider-neutral telemetry hooks for later OpenTelemetry integration."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class TelemetryContext:
    correlation_id: str | None
    trace_id: str | None = None


class TelemetryHooks(Protocol):
    def request_started(self, context: TelemetryContext, *, method: str, path: str) -> None:
        """Observe request start without changing request authority."""

    def request_finished(self, context: TelemetryContext, *, status_code: int) -> None:
        """Observe request completion without creating audit or Evidence state."""


class NoOpTelemetryHooks:
    def request_started(self, context: TelemetryContext, *, method: str, path: str) -> None:
        del context, method, path

    def request_finished(self, context: TelemetryContext, *, status_code: int) -> None:
        del context, status_code
