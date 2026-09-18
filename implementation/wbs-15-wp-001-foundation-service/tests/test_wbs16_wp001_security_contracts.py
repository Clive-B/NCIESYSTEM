import asyncio
import unittest
from typing import cast

from ncie_foundation.composition import compose_foundation_service
from ncie_foundation.harness import InProcessHarness
from ncie_foundation.observability import InMemoryObservabilitySink, SignalCategory
from ncie_foundation.routing import ApplicationResponse, RouteDefinition, RouteRegistry
from ncie_foundation.security_authorization import (
    ALL_AUTHORIZATION_DIMENSIONS,
    AuthorizationContractError,
    AuthorizationDimension,
    AuthorizationEffect,
    CurrentAuthorizationDecision,
    CurrentAuthorizationRequest,
    DenyAllPolicyDecisionPoint,
    PolicyEnforcementPoint,
    SecurityDecisionSignals,
    WBS15AuthorizationAdapter,
)
from ncie_foundation.security_principals import (
    AuthoritativeSourceCategory,
    PrincipalClass,
    PrincipalContractError,
    SecurityPrincipal,
    UnboundIdentitySource,
    authoritative_source_for,
)


class PublicShapeHandler:
    async def __call__(self, context: object) -> ApplicationResponse:
        del context
        return ApplicationResponse(status_code=200, payload={"status": "synthetic"})


class MissingDecisionPoint:
    def evaluate(self, request: CurrentAuthorizationRequest) -> CurrentAuthorizationDecision:
        del request
        return cast(CurrentAuthorizationDecision, None)


class ErrorDecisionPoint:
    def evaluate(self, request: CurrentAuthorizationRequest) -> CurrentAuthorizationDecision:
        del request
        raise RuntimeError("synthetic policy failure")


class SecurityPrincipalContractTests(unittest.TestCase):
    def test_seven_principal_classes_have_distinct_authoritative_sources(self) -> None:
        self.assertEqual(len(PrincipalClass), 7)
        sources = {authoritative_source_for(principal_class) for principal_class in PrincipalClass}
        self.assertEqual(len(sources), 7)
        self.assertEqual(
            authoritative_source_for(PrincipalClass.HUMAN),
            AuthoritativeSourceCategory.INSTITUTIONAL_IDENTITY_SOURCE,
        )

    def test_mismatched_source_is_rejected_without_echoing_reference(self) -> None:
        protected_reference = "opaque-do-not-echo"
        with self.assertRaises(PrincipalContractError) as captured:
            SecurityPrincipal(
                principal_class=PrincipalClass.HUMAN,
                source_category=AuthoritativeSourceCategory.AGENT_FACTORY_REGISTRY,
                opaque_subject_reference=protected_reference,
            )
        self.assertNotIn(protected_reference, str(captured.exception))

    def test_unbound_source_authenticates_no_principal(self) -> None:
        principal = UnboundIdentitySource().resolve(
            principal_class=PrincipalClass.SERVICE,
            source_category=AuthoritativeSourceCategory.SERVICE_REGISTRATION,
            opaque_subject_reference="synthetic-service-reference",
        )
        self.assertIsNone(principal)


class AuthorizationContractTests(unittest.TestCase):
    @staticmethod
    def principal() -> SecurityPrincipal:
        return SecurityPrincipal(
            principal_class=PrincipalClass.SERVICE,
            source_category=AuthoritativeSourceCategory.SERVICE_REGISTRATION,
            opaque_subject_reference="synthetic-service-reference",
        )

    @classmethod
    def request(cls, *, principal: SecurityPrincipal | None = None) -> CurrentAuthorizationRequest:
        return CurrentAuthorizationRequest(
            request_reference="request-reference",
            correlation_id="correlation-reference",
            principal=principal,
            object_reference="synthetic-object",
            field_references=("synthetic-field",),
            action_reference="synthetic-action",
            purpose_reference="synthetic-purpose",
            classification_reference="SYNTHETIC",
            policy_version="test-policy-version",
        )

    @staticmethod
    def decision(
        *,
        effect: AuthorizationEffect,
        request_reference: str = "request-reference",
        policy_version: str = "test-policy-version",
    ) -> CurrentAuthorizationDecision:
        return CurrentAuthorizationDecision(
            request_reference=request_reference,
            policy_version=policy_version,
            effect=effect,
            reason_code=f"SYNTHETIC_{effect.value}",
            evaluated_dimensions=ALL_AUTHORIZATION_DIMENSIONS,
        )

    def test_decision_requires_all_four_dimensions(self) -> None:
        with self.assertRaises(AuthorizationContractError):
            CurrentAuthorizationDecision(
                request_reference="request-reference",
                policy_version="test-policy-version",
                effect=AuthorizationEffect.DENY,
                reason_code="INCOMPLETE_DIMENSIONS",
                evaluated_dimensions=(AuthorizationDimension.OBJECT,),
            )

    def test_reference_policy_has_zero_grants_and_denies(self) -> None:
        request = self.request(principal=self.principal())
        self.assertEqual(request.role_references, ())
        self.assertEqual(request.policy_attributes, ())
        decision = DenyAllPolicyDecisionPoint().evaluate(request)
        result = PolicyEnforcementPoint().enforce(request, decision)
        self.assertEqual(decision.effect, AuthorizationEffect.DENY)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "NO_POLICY_GRANT")

    def test_only_current_complete_permit_with_principal_is_allowed(self) -> None:
        request = self.request(principal=self.principal())
        enforcement = PolicyEnforcementPoint()
        permitted = enforcement.enforce(
            request,
            self.decision(effect=AuthorizationEffect.PERMIT),
        )
        stale = enforcement.enforce(
            request,
            self.decision(
                effect=AuthorizationEffect.PERMIT,
                policy_version="stale-policy-version",
            ),
        )
        indeterminate = enforcement.enforce(
            request,
            self.decision(effect=AuthorizationEffect.INDETERMINATE),
        )
        no_principal = enforcement.enforce(
            self.request(),
            self.decision(effect=AuthorizationEffect.PERMIT),
        )
        self.assertTrue(permitted.allowed)
        self.assertFalse(stale.allowed)
        self.assertFalse(indeterminate.allowed)
        self.assertFalse(no_principal.allowed)

    def test_protected_policy_attribute_is_rejected_without_value_echo(self) -> None:
        protected_value = "sensitive-do-not-echo"
        with self.assertRaises(AuthorizationContractError) as captured:
            CurrentAuthorizationRequest(
                request_reference="request-reference",
                correlation_id="correlation-reference",
                principal=None,
                object_reference="synthetic-object",
                field_references=(),
                action_reference="synthetic-action",
                purpose_reference="synthetic-purpose",
                classification_reference="SYNTHETIC",
                policy_version="test-policy-version",
                policy_attributes=(("access_token", protected_value),),
            )
        self.assertNotIn(protected_value, str(captured.exception))

    def test_missing_and_error_decisions_fail_closed(self) -> None:
        for decision_point in (MissingDecisionPoint(), ErrorDecisionPoint()):
            with self.subTest(decision_point=type(decision_point).__name__):
                result = WBS15AuthorizationAdapter(decision_point).authorize(
                    correlation_id="corr-wbs16-policy-failure",
                    method="GET",
                    path="/public-shape",
                )
                self.assertFalse(result.allowed)
                self.assertEqual(result.reason, "POLICY_EVALUATION_ERROR")

    def test_wbs15_adapter_denies_and_emits_minimized_non_authoritative_signal(self) -> None:
        sink = InMemoryObservabilitySink()
        adapter = WBS15AuthorizationAdapter(signals=SecurityDecisionSignals(sink))
        routes = RouteRegistry()
        routes.register(
            RouteDefinition(
                method="GET",
                path="/public-shape",
                handler=PublicShapeHandler(),
                requires_authenticated_identity=False,
            )
        )
        service = compose_foundation_service(
            {
                "NCIE_SERVICE_NAME": "ncie-wbs16-wp001-test",
                "NCIE_ENVIRONMENT": "local-test",
            },
            authorization=adapter,
            routes=routes,
        )
        response = asyncio.run(
            InProcessHarness(service).request(
                "/public-shape",
                correlation_id="corr-wbs16-deny",
            )
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.payload["detail"], "NO_POLICY_GRANT")
        events = sink.events()
        self.assertEqual(len(events), 1)
        event = events[0]
        self.assertEqual(event.category, SignalCategory.SECURITY_CONDITION)
        self.assertFalse(event.authoritative_evidence)
        self.assertFalse(event.institutional_finding)
        self.assertFalse(event.institutional_decision)
        self.assertEqual(
            event.attributes,
            (
                ("effect", "DENY"),
                ("reason_code", "NO_POLICY_GRANT"),
                ("principal_class", "NONE"),
                ("allowed", False),
            ),
        )


if __name__ == "__main__":
    unittest.main()
