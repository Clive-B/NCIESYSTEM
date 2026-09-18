import asyncio
import unittest

from ncie_foundation.composition import compose_foundation_service
from ncie_foundation.harness import InProcessHarness
from ncie_foundation.observability import (
    FoundationObservabilityHooks,
    InMemoryObservabilitySink,
    MetricObservation,
    ObservabilityContractError,
    OperationalEvent,
    SignalCategory,
    TraceSpan,
)


class ObservabilitySemanticTests(unittest.TestCase):
    def test_all_five_signal_categories_are_explicit_and_distinct(self) -> None:
        self.assertEqual(
            {category.value for category in SignalCategory},
            {
                "PLATFORM_HEALTH",
                "DATA_PIPELINE_HEALTH",
                "SECTOR_NETWORK_CONDITION",
                "ARGUS_QUALITY",
                "SECURITY_CONDITION",
            },
        )
        self.assertNotEqual(
            SignalCategory.PLATFORM_HEALTH,
            SignalCategory.SECTOR_NETWORK_CONDITION,
        )

    def test_signals_are_non_authoritative_by_construction(self) -> None:
        event = OperationalEvent(
            category=SignalCategory.SECURITY_CONDITION,
            name="synthetic.security.condition",
            correlation_id="corr-wp004-authority",
        )
        metric = MetricObservation(
            category=SignalCategory.DATA_PIPELINE_HEALTH,
            name="synthetic.pipeline.lag",
            value=1,
        )
        span = TraceSpan(
            category=SignalCategory.ARGUS_QUALITY,
            name="synthetic.argus.operation",
            correlation_id=None,
        )
        self.assertFalse(event.authoritative_evidence)
        self.assertFalse(event.institutional_finding)
        self.assertFalse(event.institutional_decision)
        self.assertFalse(metric.authoritative_evidence)
        self.assertFalse(span.authoritative_evidence)

    def test_protected_attribute_is_rejected_without_value_echo(self) -> None:
        protected_value = "do-not-echo-sensitive-value"
        with self.assertRaises(ObservabilityContractError) as captured:
            OperationalEvent(
                category=SignalCategory.PLATFORM_HEALTH,
                name="synthetic.protected.test",
                correlation_id=None,
                attributes=(("access_token", protected_value),),
            )
        self.assertNotIn(protected_value, str(captured.exception))

    def test_in_memory_sink_preserves_category_and_correlation(self) -> None:
        sink = InMemoryObservabilitySink()
        event = OperationalEvent(
            category=SignalCategory.SECTOR_NETWORK_CONDITION,
            name="synthetic.network.condition",
            correlation_id="corr-wp004-sector",
            classification="SYNTHETIC",
        )
        sink.emit_event(event)
        self.assertEqual(sink.events(), (event,))
        self.assertEqual(sink.events()[0].category, SignalCategory.SECTOR_NETWORK_CONDITION)
        self.assertEqual(sink.events()[0].correlation_id, "corr-wp004-sector")
        self.assertEqual(sink.metrics(), ())
        self.assertEqual(sink.spans(), ())

    def test_foundation_hooks_emit_platform_signals_only(self) -> None:
        sink = InMemoryObservabilitySink()
        service = compose_foundation_service(
            {
                "NCIE_SERVICE_NAME": "ncie-wp004-test",
                "NCIE_ENVIRONMENT": "local-test",
            },
            telemetry=FoundationObservabilityHooks(sink),
        )
        response = asyncio.run(
            InProcessHarness(service).request("/health/live", correlation_id="corr-wp004-platform")
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(sink.events()), 1)
        self.assertEqual(len(sink.metrics()), 1)
        self.assertEqual(len(sink.spans()), 1)
        categories = (
            tuple(signal.category for signal in sink.events())
            + tuple(signal.category for signal in sink.metrics())
            + tuple(signal.category for signal in sink.spans())
        )
        self.assertTrue(all(category is SignalCategory.PLATFORM_HEALTH for category in categories))
        self.assertEqual(sink.events()[0].correlation_id, "corr-wp004-platform")


if __name__ == "__main__":
    unittest.main()
