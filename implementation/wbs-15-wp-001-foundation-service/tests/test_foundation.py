import asyncio
import io
import json
import logging
import unittest
from typing import Any

from ncie_foundation.app import FoundationApp
from ncie_foundation.config import ConfigurationError, FoundationSettings
from ncie_foundation.structured_logging import NcieJsonFormatter


def request(
    app: FoundationApp,
    path: str,
    *,
    correlation_id: str | None = None,
) -> tuple[int, dict[str, Any], list[tuple[bytes, bytes]]]:
    messages: list[dict[str, Any]] = []
    headers: list[tuple[bytes, bytes]] = []
    if correlation_id is not None:
        headers.append((b"x-correlation-id", correlation_id.encode("utf-8")))

    async def receive() -> dict[str, Any]:
        return {"type": "http.request", "body": b"", "more_body": False}

    async def send(message: dict[str, Any]) -> None:
        messages.append(message)

    asyncio.run(
        app(
            {"type": "http", "method": "GET", "path": path, "headers": headers},
            receive,
            send,
        )
    )
    start, body = messages
    return start["status"], json.loads(body["body"]), start["headers"]


class FoundationAppTests(unittest.TestCase):
    def setUp(self) -> None:
        self.settings = FoundationSettings.from_environment(
            {"NCIE_SERVICE_NAME": "test-service", "NCIE_ENVIRONMENT": "local-test"}
        )
        self.app = FoundationApp(settings=self.settings)

    def test_liveness_does_not_claim_business_correctness_or_acceptance(self) -> None:
        status, payload, _ = request(self.app, "/health/live")
        self.assertEqual(status, 200)
        self.assertEqual(payload["category"], "PLATFORM_HEALTH")
        self.assertFalse(payload["authoritativeBusinessState"])
        self.assertEqual(payload["businessCorrectness"], "NOT_ESTABLISHED")
        self.assertEqual(payload["productionAcceptance"], "PENDING")

    def test_readiness_fails_closed_until_application_dependencies_exist(self) -> None:
        status, payload, _ = request(self.app, "/health/ready")
        self.assertEqual(status, 503)
        self.assertFalse(payload["ready"])
        self.assertEqual(payload["status"], "NOT_READY")
        self.assertEqual(payload["testAcceptance"], "PENDING")

    def test_explicit_local_readiness_still_does_not_claim_acceptance(self) -> None:
        ready_app = FoundationApp(
            settings=self.settings,
            application_dependencies_ready=True,
        )
        status, payload, _ = request(ready_app, "/health/ready")
        self.assertEqual(status, 200)
        self.assertTrue(payload["ready"])
        self.assertEqual(payload["testAcceptance"], "PENDING")

    def test_non_probe_request_requires_correlation_id(self) -> None:
        status, payload, _ = request(self.app, "/application")
        self.assertEqual(status, 400)
        self.assertEqual(payload["title"], "Missing correlation ID")
        self.assertIsNone(payload["correlationId"])

    def test_default_authorization_fails_closed_and_echoes_correlation(self) -> None:
        status, payload, headers = request(self.app, "/application", correlation_id="corr-test-001")
        self.assertEqual(status, 403)
        self.assertEqual(payload["title"], "Authorization denied")
        self.assertIn((b"x-correlation-id", b"corr-test-001"), headers)


class ConfigurationTests(unittest.TestCase):
    def test_secret_references_are_parsed_without_values(self) -> None:
        settings = FoundationSettings.from_environment(
            {"NCIE_SECRET_REFS": "database=secret://database,signing=secret://signing"}
        )
        self.assertEqual(len(settings.secret_references), 2)
        self.assertEqual(settings.secret_references[0].name, "database")

    def test_literal_secret_configuration_is_rejected(self) -> None:
        with self.assertRaises(ConfigurationError):
            FoundationSettings.from_environment({"NCIE_SECRET_VALUE_DATABASE": "prohibited"})


class StructuredLoggingTests(unittest.TestCase):
    def test_formatter_emits_bounded_operational_fields(self) -> None:
        stream = io.StringIO()
        handler = logging.StreamHandler(stream)
        handler.setFormatter(NcieJsonFormatter())
        logger = logging.getLogger("ncie-foundation-test")
        logger.handlers = [handler]
        logger.setLevel(logging.INFO)
        logger.propagate = False

        logger.info("request completed", extra={"correlation_id": "corr-test-002"})
        payload = json.loads(stream.getvalue())
        self.assertEqual(payload["correlationId"], "corr-test-002")
        self.assertFalse(payload["protectedValuesIncluded"])
        self.assertEqual(payload["classification"], "NOT_SET")


if __name__ == "__main__":
    unittest.main()
