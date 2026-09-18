"""Provider-neutral application extension contracts for local ASGI composition."""

from dataclasses import dataclass
from typing import Any, Protocol

from .request_context import RequestContext


class RouteRegistrationError(ValueError):
    """Raised when an application route violates the foundation contract."""


@dataclass(frozen=True, slots=True)
class ApplicationResponse:
    status_code: int
    payload: dict[str, Any]


class ApplicationHandler(Protocol):
    async def __call__(self, context: RequestContext) -> ApplicationResponse:
        """Handle a request only after foundation boundaries complete."""


@dataclass(frozen=True, slots=True)
class RouteDefinition:
    method: str
    path: str
    handler: ApplicationHandler
    requires_authenticated_identity: bool = True

    def key(self) -> tuple[str, str]:
        return self.method.upper(), self.path


class RouteRegistry:
    def __init__(self) -> None:
        self._routes: dict[tuple[str, str], RouteDefinition] = {}

    def register(self, route: RouteDefinition) -> None:
        method, path = route.key()
        if not method or not path.startswith("/"):
            raise RouteRegistrationError("Route requires a method and absolute path")
        if path.startswith("/health/"):
            raise RouteRegistrationError("Application routes cannot replace platform probes")
        key = method, path
        if key in self._routes:
            raise RouteRegistrationError("Route is already registered")
        self._routes[key] = route

    def resolve(self, method: str, path: str) -> RouteDefinition | None:
        return self._routes.get((method.upper(), path))
