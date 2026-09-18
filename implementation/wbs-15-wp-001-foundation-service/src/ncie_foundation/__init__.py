"""NCIE WBS-15 local foundation service."""

from .app import FoundationApp, app
from .composition import ComposedFoundationService, compose_foundation_service
from .harness import InProcessHarness, InProcessResponse
from .lifecycle import LifecycleComponent, LifecycleState, ServiceLifecycle
from .observability import (
    FoundationObservabilityHooks,
    InMemoryObservabilitySink,
    MetricObservation,
    OperationalEvent,
    SignalCategory,
    TraceSpan,
)
from .readiness import ReadinessRegistry, ReadinessSnapshot
from .request_context import IdentityContext, IdentityState, RequestContext
from .routing import ApplicationResponse, RouteDefinition, RouteRegistry

__all__ = [
    "ApplicationResponse",
    "ComposedFoundationService",
    "FoundationApp",
    "FoundationObservabilityHooks",
    "IdentityContext",
    "IdentityState",
    "InMemoryObservabilitySink",
    "InProcessHarness",
    "InProcessResponse",
    "LifecycleComponent",
    "LifecycleState",
    "MetricObservation",
    "OperationalEvent",
    "ReadinessRegistry",
    "ReadinessSnapshot",
    "RequestContext",
    "RouteDefinition",
    "RouteRegistry",
    "ServiceLifecycle",
    "SignalCategory",
    "TraceSpan",
    "app",
    "compose_foundation_service",
]
