import asyncio
import unittest

from ncie_foundation.composition import compose_foundation_service
from ncie_foundation.config import ConfigurationError
from ncie_foundation.harness import InProcessHarness
from ncie_foundation.lifecycle import (
    LifecycleState,
    LifecycleTransitionError,
    ServiceLifecycle,
)
from ncie_foundation.readiness import ReadinessError, ReadinessRegistry
from ncie_foundation.telemetry import TelemetryContext


class RecordingComponent:
    def __init__(
        self,
        name: str,
        events: list[str],
        *,
        fail_start: bool = False,
        fail_stop: bool = False,
    ) -> None:
        self._name = name
        self._events = events
        self._fail_start = fail_start
        self._fail_stop = fail_stop

    async def start(self) -> None:
        self._events.append(f"start:{self._name}")
        if self._fail_start:
            raise RuntimeError("synthetic startup failure")

    async def stop(self) -> None:
        self._events.append(f"stop:{self._name}")
        if self._fail_stop:
            raise RuntimeError("synthetic shutdown failure")


class RecordingTelemetry:
    def __init__(self) -> None:
        self.events: list[tuple[str, str | None, int | None]] = []

    def request_started(self, context: TelemetryContext, *, method: str, path: str) -> None:
        self.events.append((f"start:{method}:{path}", context.correlation_id, None))

    def request_finished(self, context: TelemetryContext, *, status_code: int) -> None:
        self.events.append(("finish", context.correlation_id, status_code))


class ReadinessRegistryTests(unittest.TestCase):
    def test_registry_fails_closed_until_every_required_dependency_is_ready(self) -> None:
        registry = ReadinessRegistry()
        self.assertFalse(registry.snapshot().ready)

        registry.register_required("lifecycle")
        registry.register_required("future-boundary")
        registry.set_ready("lifecycle", ready=True)
        snapshot = registry.snapshot()
        self.assertFalse(snapshot.ready)
        self.assertEqual(snapshot.required_count, 2)
        self.assertEqual(snapshot.ready_count, 1)

        registry.set_ready("future-boundary", ready=True)
        self.assertTrue(registry.snapshot().ready)

    def test_registry_rejects_duplicate_and_unknown_dependencies(self) -> None:
        registry = ReadinessRegistry()
        registry.register_required("lifecycle")
        with self.assertRaises(ReadinessError):
            registry.register_required("lifecycle")
        with self.assertRaises(ReadinessError):
            registry.set_ready("unknown", ready=True)


class LifecycleTests(unittest.TestCase):
    def test_lifecycle_starts_in_order_and_stops_in_reverse(self) -> None:
        events: list[str] = []
        lifecycle = ServiceLifecycle(
            (
                RecordingComponent("first", events),
                RecordingComponent("second", events),
            )
        )

        asyncio.run(lifecycle.start())
        self.assertEqual(lifecycle.state, LifecycleState.STARTED)
        asyncio.run(lifecycle.stop())
        self.assertEqual(lifecycle.state, LifecycleState.STOPPED)
        self.assertEqual(
            events,
            ["start:first", "start:second", "stop:second", "stop:first"],
        )

    def test_startup_failure_rolls_back_and_enters_failed_state(self) -> None:
        events: list[str] = []
        lifecycle = ServiceLifecycle(
            (
                RecordingComponent("started", events),
                RecordingComponent("failed", events, fail_start=True),
            )
        )

        with self.assertRaises(LifecycleTransitionError):
            asyncio.run(lifecycle.start())
        self.assertEqual(lifecycle.state, LifecycleState.FAILED)
        self.assertEqual(events, ["start:started", "start:failed", "stop:started"])

    def test_invalid_transition_is_rejected(self) -> None:
        lifecycle = ServiceLifecycle()
        with self.assertRaises(LifecycleTransitionError):
            asyncio.run(lifecycle.stop())


class CompositionAndHarnessTests(unittest.TestCase):
    @staticmethod
    def environment() -> dict[str, str]:
        return {
            "NCIE_SERVICE_NAME": "ncie-composition-test",
            "NCIE_ENVIRONMENT": "local-test",
            "NCIE_SECRET_REFS": "signing=secret-ref://local/signing",
        }

    def test_composed_service_is_not_ready_before_start(self) -> None:
        service = compose_foundation_service(self.environment())
        harness = InProcessHarness(service)

        response = asyncio.run(harness.request("/health/ready"))
        self.assertEqual(response.status_code, 503)
        self.assertFalse(response.payload["ready"])
        self.assertEqual(response.payload["businessCorrectness"], "NOT_ESTABLISHED")
        self.assertEqual(response.payload["productionAcceptance"], "PENDING")

    def test_start_and_stop_control_aggregate_readiness(self) -> None:
        service = compose_foundation_service(self.environment())
        harness = InProcessHarness(service)

        asyncio.run(harness.start())
        ready = asyncio.run(harness.request("/health/ready"))
        self.assertEqual(ready.status_code, 200)
        self.assertTrue(ready.payload["ready"])
        self.assertEqual(ready.payload["testAcceptance"], "PENDING")

        asyncio.run(harness.stop())
        stopped = asyncio.run(harness.request("/health/ready"))
        self.assertEqual(stopped.status_code, 503)
        self.assertFalse(stopped.payload["ready"])

    def test_additional_required_dependency_remains_fail_closed(self) -> None:
        service = compose_foundation_service(
            self.environment(), required_dependencies=("future-approved-boundary",)
        )
        harness = InProcessHarness(service)

        asyncio.run(harness.start())
        not_ready = asyncio.run(harness.request("/health/ready"))
        self.assertEqual(not_ready.status_code, 503)

        service.readiness.set_ready("future-approved-boundary", ready=True)
        ready = asyncio.run(harness.request("/health/ready"))
        self.assertEqual(ready.status_code, 200)

        service.readiness.set_ready("future-approved-boundary", ready=False)
        not_ready_again = asyncio.run(harness.request("/health/ready"))
        self.assertEqual(not_ready_again.status_code, 503)
        asyncio.run(harness.stop())

    def test_composition_defaults_to_deny_and_preserves_correlation_and_telemetry(self) -> None:
        telemetry = RecordingTelemetry()
        service = compose_foundation_service(self.environment(), telemetry=telemetry)
        harness = InProcessHarness(service)

        response = asyncio.run(harness.request("/application", correlation_id="corr-wp002-test"))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.payload["title"], "Authorization denied")
        self.assertIn((b"x-correlation-id", b"corr-wp002-test"), response.headers)
        self.assertEqual(
            telemetry.events,
            [
                ("start:GET:/application", "corr-wp002-test", None),
                ("finish", "corr-wp002-test", 403),
            ],
        )

    def test_startup_failure_keeps_readiness_closed(self) -> None:
        events: list[str] = []
        service = compose_foundation_service(
            self.environment(),
            lifecycle_components=(RecordingComponent("failed", events, fail_start=True),),
        )
        harness = InProcessHarness(service)

        with self.assertRaises(LifecycleTransitionError):
            asyncio.run(harness.start())
        response = asyncio.run(harness.request("/health/ready"))
        self.assertEqual(response.status_code, 503)
        self.assertFalse(response.payload["ready"])

    def test_literal_secret_value_is_rejected_without_echo(self) -> None:
        prohibited = "do-not-echo-this-value"
        with self.assertRaises(ConfigurationError) as captured:
            compose_foundation_service({"NCIE_SECRET_VALUE_SIGNING": prohibited})
        self.assertNotIn(prohibited, str(captured.exception))


if __name__ == "__main__":
    unittest.main()
