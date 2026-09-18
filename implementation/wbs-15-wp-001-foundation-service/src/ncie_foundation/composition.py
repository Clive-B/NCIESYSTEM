"""Typed local composition root for the NCIE foundation service."""

from collections.abc import Mapping
from dataclasses import dataclass

from .app import FoundationApp
from .authorization import AuthorizationBoundary, DenyAllAuthorization
from .config import FoundationSettings
from .lifecycle import LifecycleComponent, ServiceLifecycle
from .readiness import ReadinessRegistry
from .request_context import IdentityBoundary, UnresolvedIdentityBoundary
from .routing import RouteRegistry
from .telemetry import NoOpTelemetryHooks, TelemetryHooks

LIFECYCLE_DEPENDENCY = "foundation-lifecycle"


@dataclass(slots=True)
class ComposedFoundationService:
    settings: FoundationSettings
    readiness: ReadinessRegistry
    lifecycle: ServiceLifecycle
    app: FoundationApp

    async def start(self) -> None:
        try:
            await self.lifecycle.start()
        except Exception:
            self.readiness.set_ready(LIFECYCLE_DEPENDENCY, ready=False)
            raise
        self.readiness.set_ready(LIFECYCLE_DEPENDENCY, ready=True)

    async def stop(self) -> None:
        self.readiness.set_ready(LIFECYCLE_DEPENDENCY, ready=False)
        await self.lifecycle.stop()


def compose_foundation_service(
    environment: Mapping[str, str],
    *,
    authorization: AuthorizationBoundary | None = None,
    telemetry: TelemetryHooks | None = None,
    lifecycle_components: tuple[LifecycleComponent, ...] = (),
    required_dependencies: tuple[str, ...] = (),
    identity: IdentityBoundary | None = None,
    routes: RouteRegistry | None = None,
) -> ComposedFoundationService:
    """Compose a local service without resolving secrets or selecting providers."""

    settings = FoundationSettings.from_environment(environment)
    readiness = ReadinessRegistry()
    readiness.register_required(LIFECYCLE_DEPENDENCY)
    for dependency in required_dependencies:
        readiness.register_required(dependency)

    lifecycle = ServiceLifecycle(lifecycle_components)
    application = FoundationApp(
        settings=settings,
        authorization=authorization or DenyAllAuthorization(),
        telemetry=telemetry or NoOpTelemetryHooks(),
        readiness=readiness,
        identity=identity or UnresolvedIdentityBoundary(),
        routes=routes or RouteRegistry(),
    )
    return ComposedFoundationService(
        settings=settings,
        readiness=readiness,
        lifecycle=lifecycle,
        app=application,
    )
