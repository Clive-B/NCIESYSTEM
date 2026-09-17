"""Authorization extension boundary for the later WBS-16 implementation."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class AuthorizationResult:
    allowed: bool
    reason: str


class AuthorizationBoundary(Protocol):
    """A narrow boundary that WBS-16 can implement without changing the app."""

    def authorize(self, *, correlation_id: str, method: str, path: str) -> AuthorizationResult:
        """Return the current authorization decision for one request."""


class DenyAllAuthorization:
    """Fail closed until WBS-16 supplies an approved implementation."""

    def authorize(self, *, correlation_id: str, method: str, path: str) -> AuthorizationResult:
        del correlation_id, method, path
        return AuthorizationResult(
            allowed=False,
            reason="WBS-16 authorization implementation is not available",
        )
