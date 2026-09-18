import asyncio
import unittest

from ncie_foundation.authorization import AuthorizationResult
from ncie_foundation.composition import compose_foundation_service
from ncie_foundation.config import ConfigurationError
from ncie_foundation.harness import InProcessHarness
from ncie_foundation.request_context import IdentityContext, IdentityState, RequestContext
from ncie_foundation.routing import (
    ApplicationResponse,
    RouteDefinition,
    RouteRegistrationError,
    RouteRegistry,
)


class AllowAuthorization:
    def authorize(self, *, correlation_id: str, method: str, path: str) -> AuthorizationResult:
        del correlation_id, method, path
        return AuthorizationResult(allowed=True, reason="synthetic local-test authorization")


class AuthenticatedIdentity:
    def resolve(
        self,
        *,
        correlation_id: str,
        method: str,
        path: str,
        headers: tuple[tuple[bytes, bytes], ...],
    ) -> IdentityContext:
        del correlation_id, method, path, headers
        return IdentityContext(
            state=IdentityState.AUTHENTICATED,
            subject_reference="synthetic-subject-reference",
        )


class CapturingHandler:
    def __init__(self) -> None:
        self.contexts: list[RequestContext] = []

    async def __call__(self, context: RequestContext) -> ApplicationResponse:
        self.contexts.append(context)
        return ApplicationResponse(
            status_code=200,
            payload={
                "category": "LOCAL_TEST_RESPONSE",
                "authoritativeBusinessState": False,
            },
        )


class RequestIdentityAndRoutingTests(unittest.TestCase):
    @staticmethod
    def environment() -> dict[str, str]:
        return {
            "NCIE_SERVICE_NAME": "ncie-wp003-test",
            "NCIE_SERVICE_VERSION": "0.0.0-test",
            "NCIE_ENVIRONMENT": "local-test",
            "NCIE_CONFIG_SCHEMA_VERSION": "1",
        }

    def test_protected_route_fails_closed_with_default_unresolved_identity(self) -> None:
        handler = CapturingHandler()
        routes = RouteRegistry()
        routes.register(RouteDefinition(method="GET", path="/protected", handler=handler))
        service = compose_foundation_service(
            self.environment(), authorization=AllowAuthorization(), routes=routes
        )
        harness = InProcessHarness(service)

        response = asyncio.run(
            harness.request("/protected", correlation_id="corr-wp003-unresolved")
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.payload["title"], "Identity unresolved")
        self.assertEqual(handler.contexts, [])

    def test_route_handler_receives_bounded_typed_context_after_boundaries(self) -> None:
        handler = CapturingHandler()
        routes = RouteRegistry()
        routes.register(RouteDefinition(method="GET", path="/protected", handler=handler))
        service = compose_foundation_service(
            self.environment(),
            authorization=AllowAuthorization(),
            identity=AuthenticatedIdentity(),
            routes=routes,
        )
        harness = InProcessHarness(service)

        response = asyncio.run(
            harness.request(
                "/protected",
                correlation_id="corr-wp003-authenticated",
                headers=(
                    (b"x-ncie-purpose-reference", b"local-contract-test"),
                    (b"x-ncie-data-classification", b"SYNTHETIC"),
                ),
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(handler.contexts), 1)
        context = handler.contexts[0]
        self.assertEqual(context.correlation_id, "corr-wp003-authenticated")
        self.assertEqual(context.purpose_reference, "local-contract-test")
        self.assertEqual(context.data_classification, "SYNTHETIC")
        self.assertEqual(context.identity.state, IdentityState.AUTHENTICATED)
        self.assertIn((b"x-ncie-service-version", b"0.0.0-test"), response.headers)

    def test_missing_correlation_prevents_handler_execution(self) -> None:
        handler = CapturingHandler()
        routes = RouteRegistry()
        routes.register(
            RouteDefinition(
                method="GET",
                path="/local-public-shape",
                handler=handler,
                requires_authenticated_identity=False,
            )
        )
        service = compose_foundation_service(
            self.environment(), authorization=AllowAuthorization(), routes=routes
        )
        response = asyncio.run(InProcessHarness(service).request("/local-public-shape"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(handler.contexts, [])

    def test_authorization_remains_required_after_identity_resolution(self) -> None:
        handler = CapturingHandler()
        routes = RouteRegistry()
        routes.register(RouteDefinition(method="GET", path="/protected", handler=handler))
        service = compose_foundation_service(
            self.environment(), identity=AuthenticatedIdentity(), routes=routes
        )
        response = asyncio.run(
            InProcessHarness(service).request("/protected", correlation_id="corr-wp003-denied")
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(handler.contexts, [])

    def test_routes_cannot_replace_probes_or_duplicate_an_endpoint(self) -> None:
        handler = CapturingHandler()
        routes = RouteRegistry()
        with self.assertRaises(RouteRegistrationError):
            routes.register(RouteDefinition(method="GET", path="/health/live", handler=handler))

        routes.register(RouteDefinition(method="GET", path="/one", handler=handler))
        with self.assertRaises(RouteRegistrationError):
            routes.register(RouteDefinition(method="GET", path="/one", handler=handler))

    def test_identity_state_does_not_accept_subject_for_unresolved_identity(self) -> None:
        with self.assertRaises(ValueError):
            IdentityContext(
                state=IdentityState.UNRESOLVED,
                subject_reference="prohibited-subject-reference",
            )

    def test_unsupported_configuration_schema_fails_explicitly(self) -> None:
        environment = self.environment()
        environment["NCIE_CONFIG_SCHEMA_VERSION"] = "999"
        with self.assertRaises(ConfigurationError):
            compose_foundation_service(environment)


if __name__ == "__main__":
    unittest.main()
