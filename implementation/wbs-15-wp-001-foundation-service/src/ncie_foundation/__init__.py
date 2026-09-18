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
from .security_authorization import (
    AuthorizationDimension,
    AuthorizationEffect,
    CurrentAuthorizationDecision,
    CurrentAuthorizationRequest,
    DenyAllPolicyDecisionPoint,
    PolicyDecisionPoint,
    PolicyEnforcementPoint,
    SecurityDecisionSignals,
    WBS15AuthorizationAdapter,
)
from .security_principals import (
    AuthoritativeSourceCategory,
    IdentitySourceBoundary,
    PrincipalClass,
    SecurityPrincipal,
    UnboundIdentitySource,
    authoritative_source_for,
)

__all__ = [
    "ApplicationResponse",
    "AuthoritativeSourceCategory",
    "AuthorizationDimension",
    "AuthorizationEffect",
    "ComposedFoundationService",
    "CurrentAuthorizationDecision",
    "CurrentAuthorizationRequest",
    "DenyAllPolicyDecisionPoint",
    "FoundationApp",
    "FoundationObservabilityHooks",
    "IdentityContext",
    "IdentitySourceBoundary",
    "IdentityState",
    "InMemoryObservabilitySink",
    "InProcessHarness",
    "InProcessResponse",
    "LifecycleComponent",
    "LifecycleState",
    "MetricObservation",
    "OperationalEvent",
    "PolicyDecisionPoint",
    "PolicyEnforcementPoint",
    "PrincipalClass",
    "ReadinessRegistry",
    "ReadinessSnapshot",
    "RequestContext",
    "RouteDefinition",
    "RouteRegistry",
    "SecurityDecisionSignals",
    "SecurityPrincipal",
    "ServiceLifecycle",
    "SignalCategory",
    "TraceSpan",
    "UnboundIdentitySource",
    "WBS15AuthorizationAdapter",
    "app",
    "authoritative_source_for",
    "compose_foundation_service",
]
