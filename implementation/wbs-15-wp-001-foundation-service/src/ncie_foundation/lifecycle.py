"""Provider-neutral deterministic lifecycle contracts for local composition."""

from enum import StrEnum
from typing import Protocol


class LifecycleState(StrEnum):
    CREATED = "CREATED"
    STARTING = "STARTING"
    STARTED = "STARTED"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    FAILED = "FAILED"


class LifecycleTransitionError(RuntimeError):
    """Raised when a lifecycle transition is invalid or cannot complete."""


class LifecycleComponent(Protocol):
    async def start(self) -> None:
        """Start one bounded local component."""

    async def stop(self) -> None:
        """Stop one bounded local component."""


class ServiceLifecycle:
    """Start in declaration order, stop in reverse, and expose explicit state."""

    def __init__(self, components: tuple[LifecycleComponent, ...] = ()) -> None:
        self._components = components
        self._started_components: list[LifecycleComponent] = []
        self._state = LifecycleState.CREATED

    @property
    def state(self) -> LifecycleState:
        return self._state

    async def start(self) -> None:
        if self._state not in {LifecycleState.CREATED, LifecycleState.STOPPED}:
            raise LifecycleTransitionError(f"Cannot start lifecycle from {self._state}")

        self._state = LifecycleState.STARTING
        self._started_components = []
        try:
            for component in self._components:
                await component.start()
                self._started_components.append(component)
        except Exception as error:
            await self._rollback_started_components()
            self._state = LifecycleState.FAILED
            raise LifecycleTransitionError(
                "Lifecycle startup failed and was rolled back"
            ) from error
        self._state = LifecycleState.STARTED

    async def stop(self) -> None:
        if self._state is not LifecycleState.STARTED:
            raise LifecycleTransitionError(f"Cannot stop lifecycle from {self._state}")

        self._state = LifecycleState.STOPPING
        first_error: Exception | None = None
        for component in reversed(self._started_components):
            try:
                await component.stop()
            except Exception as error:
                if first_error is None:
                    first_error = error
        self._started_components = []
        if first_error is not None:
            self._state = LifecycleState.FAILED
            raise LifecycleTransitionError("Lifecycle shutdown failed") from first_error
        self._state = LifecycleState.STOPPED

    async def _rollback_started_components(self) -> None:
        for component in reversed(self._started_components):
            try:
                await component.stop()
            except Exception:
                # The original startup error remains authoritative for this local boundary.
                pass
        self._started_components = []
