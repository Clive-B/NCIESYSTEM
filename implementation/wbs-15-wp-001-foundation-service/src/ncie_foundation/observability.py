"""Provider-neutral NCIE observability semantics and local test collectors."""

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Protocol

from .telemetry import TelemetryContext

type AttributeValue = str | int | float | bool | None
type Attributes = tuple[tuple[str, AttributeValue], ...]


class SignalCategory(StrEnum):
    PLATFORM_HEALTH = "PLATFORM_HEALTH"
    DATA_PIPELINE_HEALTH = "DATA_PIPELINE_HEALTH"
    SECTOR_NETWORK_CONDITION = "SECTOR_NETWORK_CONDITION"
    ARGUS_QUALITY = "ARGUS_QUALITY"
    SECURITY_CONDITION = "SECURITY_CONDITION"


class ObservabilityContractError(ValueError):
    """Raised when telemetry violates minimization or authority boundaries."""


PROTECTED_KEY_FRAGMENTS = (
    "secret",
    "password",
    "credential",
    "token",
    "full_prompt",
    "evidence_payload",
    "protected_identity",
)


def _validate_signal(name: str, classification: str, attributes: Attributes) -> None:
    if not name.strip() or not classification.strip():
        raise ObservabilityContractError("Signal name and classification are required")
    for key, _value in attributes:
        normalized = key.lower()
        if any(fragment in normalized for fragment in PROTECTED_KEY_FRAGMENTS):
            raise ObservabilityContractError("Protected telemetry attribute is prohibited")


@dataclass(frozen=True, slots=True)
class OperationalEvent:
    category: SignalCategory
    name: str
    correlation_id: str | None
    classification: str = "OPERATIONAL"
    attributes: Attributes = ()
    authoritative_evidence: bool = field(default=False, init=False)
    institutional_finding: bool = field(default=False, init=False)
    institutional_decision: bool = field(default=False, init=False)

    def __post_init__(self) -> None:
        _validate_signal(self.name, self.classification, self.attributes)


@dataclass(frozen=True, slots=True)
class MetricObservation:
    category: SignalCategory
    name: str
    value: int | float
    correlation_id: str | None = None
    classification: str = "OPERATIONAL"
    attributes: Attributes = ()
    authoritative_evidence: bool = field(default=False, init=False)

    def __post_init__(self) -> None:
        _validate_signal(self.name, self.classification, self.attributes)


@dataclass(frozen=True, slots=True)
class TraceSpan:
    category: SignalCategory
    name: str
    correlation_id: str | None
    trace_id: str | None = None
    classification: str = "OPERATIONAL"
    attributes: Attributes = ()
    authoritative_evidence: bool = field(default=False, init=False)

    def __post_init__(self) -> None:
        _validate_signal(self.name, self.classification, self.attributes)


class ObservabilitySink(Protocol):
    def emit_event(self, event: OperationalEvent) -> None: ...

    def observe_metric(self, metric: MetricObservation) -> None: ...

    def record_span(self, span: TraceSpan) -> None: ...


class InMemoryObservabilitySink:
    """Deterministic collector for local tests; not an Evidence or audit store."""

    def __init__(self) -> None:
        self._events: list[OperationalEvent] = []
        self._metrics: list[MetricObservation] = []
        self._spans: list[TraceSpan] = []

    def emit_event(self, event: OperationalEvent) -> None:
        self._events.append(event)

    def observe_metric(self, metric: MetricObservation) -> None:
        self._metrics.append(metric)

    def record_span(self, span: TraceSpan) -> None:
        self._spans.append(span)

    def events(self) -> tuple[OperationalEvent, ...]:
        return tuple(self._events)

    def metrics(self) -> tuple[MetricObservation, ...]:
        return tuple(self._metrics)

    def spans(self) -> tuple[TraceSpan, ...]:
        return tuple(self._spans)


class FoundationObservabilityHooks:
    """Adapt foundation request hooks to neutral platform-health signals."""

    def __init__(self, sink: ObservabilitySink) -> None:
        self._sink = sink

    def request_started(self, context: TelemetryContext, *, method: str, path: str) -> None:
        self._sink.emit_event(
            OperationalEvent(
                category=SignalCategory.PLATFORM_HEALTH,
                name="foundation.request.started",
                correlation_id=context.correlation_id,
                attributes=(("method", method), ("path", path)),
            )
        )

    def request_finished(self, context: TelemetryContext, *, status_code: int) -> None:
        self._sink.observe_metric(
            MetricObservation(
                category=SignalCategory.PLATFORM_HEALTH,
                name="foundation.request.completed",
                value=1,
                correlation_id=context.correlation_id,
                attributes=(("status_code", status_code),),
            )
        )
        self._sink.record_span(
            TraceSpan(
                category=SignalCategory.PLATFORM_HEALTH,
                name="foundation.request",
                correlation_id=context.correlation_id,
                trace_id=context.trace_id,
                attributes=(("status_code", status_code),),
            )
        )
