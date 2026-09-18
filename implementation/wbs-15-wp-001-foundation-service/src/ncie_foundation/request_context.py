"""Request and identity interfaces for the framework-neutral foundation."""

from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol

Header = tuple[bytes, bytes]


class IdentityState(StrEnum):
    ANONYMOUS = "ANONYMOUS"
    UNRESOLVED = "UNRESOLVED"
    AUTHENTICATED = "AUTHENTICATED"


@dataclass(frozen=True, slots=True)
class IdentityContext:
    state: IdentityState
    subject_reference: str | None = None

    def __post_init__(self) -> None:
        if self.state is IdentityState.AUTHENTICATED and not self.subject_reference:
            raise ValueError("Authenticated identity requires a subject reference")
        if self.state is not IdentityState.AUTHENTICATED and self.subject_reference is not None:
            raise ValueError("Only authenticated identity may carry a subject reference")


class IdentityBoundary(Protocol):
    """Interface for the future WBS-16 identity implementation."""

    def resolve(
        self,
        *,
        correlation_id: str,
        method: str,
        path: str,
        headers: tuple[Header, ...],
    ) -> IdentityContext:
        """Resolve identity without granting roles, permissions or authority."""


class UnresolvedIdentityBoundary:
    """Fail-closed identity boundary until WBS-16 supplies an implementation."""

    def resolve(
        self,
        *,
        correlation_id: str,
        method: str,
        path: str,
        headers: tuple[Header, ...],
    ) -> IdentityContext:
        del correlation_id, method, path, headers
        return IdentityContext(state=IdentityState.UNRESOLVED)


@dataclass(frozen=True, slots=True)
class RequestContext:
    correlation_id: str
    method: str
    path: str
    purpose_reference: str
    data_classification: str
    identity: IdentityContext


def bounded_header_value(
    headers: tuple[Header, ...],
    name: bytes,
    *,
    default: str,
    maximum_length: int = 128,
) -> str:
    target = name.lower()
    for key, value in headers:
        if key.lower() == target:
            decoded = value.decode("utf-8", errors="replace").strip()
            if not decoded:
                return default
            return decoded[:maximum_length]
    return default
