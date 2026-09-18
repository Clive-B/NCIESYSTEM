"""Fail-closed aggregate readiness without provider-specific disclosure."""

from dataclasses import dataclass
from typing import Protocol


class ReadinessError(ValueError):
    """Raised when the readiness contract is used inconsistently."""


@dataclass(frozen=True, slots=True)
class ReadinessSnapshot:
    ready: bool
    required_count: int
    ready_count: int


class ReadinessBoundary(Protocol):
    def snapshot(self) -> ReadinessSnapshot:
        """Return aggregate platform readiness without protected details."""


class ReadinessRegistry:
    """Track required local dependencies and fail closed until all are ready."""

    def __init__(self) -> None:
        self._required: dict[str, bool] = {}

    def register_required(self, name: str) -> None:
        normalized = name.strip()
        if not normalized:
            raise ReadinessError("Required dependency name cannot be empty")
        if normalized in self._required:
            raise ReadinessError("Required dependency is already registered")
        self._required[normalized] = False

    def set_ready(self, name: str, *, ready: bool) -> None:
        normalized = name.strip()
        if normalized not in self._required:
            raise ReadinessError("Unknown required dependency")
        self._required[normalized] = ready

    def snapshot(self) -> ReadinessSnapshot:
        required_count = len(self._required)
        ready_count = sum(self._required.values())
        return ReadinessSnapshot(
            ready=required_count > 0 and ready_count == required_count,
            required_count=required_count,
            ready_count=ready_count,
        )


@dataclass(frozen=True, slots=True)
class StaticReadiness:
    """Compatibility adapter for the original WP-001 readiness input."""

    ready: bool

    def snapshot(self) -> ReadinessSnapshot:
        return ReadinessSnapshot(
            ready=self.ready,
            required_count=1,
            ready_count=1 if self.ready else 0,
        )
