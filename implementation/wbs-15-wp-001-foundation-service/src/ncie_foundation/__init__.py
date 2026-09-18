"""NCIE WBS-15 local foundation service."""

from .app import FoundationApp, app
from .composition import ComposedFoundationService, compose_foundation_service
from .harness import InProcessHarness, InProcessResponse
from .lifecycle import LifecycleComponent, LifecycleState, ServiceLifecycle
from .readiness import ReadinessRegistry, ReadinessSnapshot

__all__ = [
    "ComposedFoundationService",
    "FoundationApp",
    "InProcessHarness",
    "InProcessResponse",
    "LifecycleComponent",
    "LifecycleState",
    "ReadinessRegistry",
    "ReadinessSnapshot",
    "ServiceLifecycle",
    "app",
    "compose_foundation_service",
]
