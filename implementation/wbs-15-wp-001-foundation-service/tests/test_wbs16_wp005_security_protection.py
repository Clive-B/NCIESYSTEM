"""Local contract and negative-path tests for WBS-16-WP-005."""

import unittest
from datetime import UTC, datetime, timedelta

from ncie_foundation.observability import InMemoryObservabilitySink, SignalCategory
from ncie_foundation.security_authorization import (
    ALL_AUTHORIZATION_DIMENSIONS,
    AuthorizationEffect,
    CurrentAuthorizationDecision,
)
from ncie_foundation.security_protection import (
    ALL_SEPARATION_DIMENSIONS,
    APPROVED_SERVICE_BOUNDARIES,
    EMPTY_CRYPTOGRAPHIC_POLICY_REGISTRY,
    EMPTY_EGRESS_POLICY_REGISTRY,
    SECURITY_PROTECTION_DECISION_EVIDENCE,
    SECURITY_PROTECTION_IMPLEMENTATION_AUTHORITY,
    AgentEgressCeiling,
    CryptographicPolicyContract,
    CryptographicPolicyEvaluator,
    CryptographicPolicyRegistry,
    CryptographicPolicyRequest,
    CryptographicValidationCode,
    EgressClass,
    EgressEvaluationRequest,
    EgressPolicyContract,
    EgressPolicyEvaluator,
    EgressPolicyRegistry,
    EgressValidationCode,
    ExceptionValidationCode,
    KeyHierarchyTier,
    LifecycleAction,
    LifecycleValidationCode,
    OpaqueProtectedReference,
    ProhibitedSurface,
    ProhibitedSurfaceEvaluator,
    ProtectedLifecycleEvaluator,
    ProtectedLifecycleEventContract,
    ProtectedReferenceClass,
    ProtectionScope,
    SecurityExceptionEvaluator,
    SecurityExceptionRequest,
    SecurityProtectionContractError,
    SecurityProtectionSignals,
    ServiceBoundaryClass,
    TrustZone,
    UnassignedCustodialAuthority,
    UnassignedExceptionAuthority,
    UnassignedIndependentAssurance,
    UnassignedPolicyApprovalAuthority,
)


class Wbs16Wp005SecurityProtectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 23, 12, tzinfo=UTC)
        self.later = self.now + timedelta(hours=1)

    def authorization(
        self,
        *,
        request_reference: str = "synthetic-request",
        policy_version: str = "synthetic-policy-v1",
        effect: AuthorizationEffect = AuthorizationEffect.PERMIT,
    ) -> CurrentAuthorizationDecision:
        return CurrentAuthorizationDecision(
            request_reference=request_reference,
            policy_version=policy_version,
            effect=effect,
            reason_code="SYNTHETIC_TEST_DECISION",
            evaluated_dimensions=ALL_AUTHORIZATION_DIMENSIONS,
        )

    def lifecycle_event(self) -> ProtectedLifecycleEventContract:
        return ProtectedLifecycleEventContract(
            event_reference="synthetic-event",
            material_reference=OpaqueProtectedReference(
                "ref:synthetic/key-001", ProtectedReferenceClass.KEY, "synthetic-policy-v1"
            ),
            action=LifecycleAction.REQUEST,
            requester_reference="synthetic-requester",
            purpose_reference="synthetic-purpose",
            classification_reference="synthetic-classification",
            policy_version="synthetic-policy-v1",
            requested_at=self.now,
        )

    def test_decision_provenance_and_controlled_registries_are_empty(self) -> None:
        self.assertEqual(
            SECURITY_PROTECTION_DECISION_EVIDENCE,
            "NCIE-WBS16-OWNER-DECISION-2026-09-23-020",
        )
        self.assertEqual(
            SECURITY_PROTECTION_IMPLEMENTATION_AUTHORITY,
            "NCIE-WBS16-OWNER-DECISION-2026-09-23-021",
        )
        self.assertTrue(EMPTY_CRYPTOGRAPHIC_POLICY_REGISTRY.is_empty())
        self.assertTrue(EMPTY_EGRESS_POLICY_REGISTRY.is_empty())

    def test_opaque_reference_rejects_literal_or_protected_material_without_echo(self) -> None:
        candidate = "secret_value=do-not-echo"
        with self.assertRaises(SecurityProtectionContractError) as caught:
            OpaqueProtectedReference(
                candidate, ProtectedReferenceClass.SECRET, "synthetic-policy-v1"
            )
        self.assertNotIn("do-not-echo", str(caught.exception))

    def test_unassigned_custody_denies_and_executes_nothing(self) -> None:
        result = ProtectedLifecycleEvaluator(UnassignedCustodialAuthority()).evaluate(
            self.lifecycle_event(), at=self.now
        )
        self.assertFalse(result.allowed)
        self.assertFalse(result.operation_executed)
        self.assertEqual(result.code, LifecycleValidationCode.NO_CURRENT_CUSTODIAL_AUTHORITY)

    def test_policy_and_assurance_interfaces_remain_unassigned(self) -> None:
        self.assertIsNone(UnassignedPolicyApprovalAuthority().approve_policy("synthetic-policy"))
        self.assertIsNone(UnassignedIndependentAssurance().attest("synthetic-contract"))

    def test_prohibited_surfaces_and_plaintext_fallback_cannot_be_excepted(self) -> None:
        evaluator = ProhibitedSurfaceEvaluator()
        for surface in ProhibitedSurface:
            assessment = evaluator.evaluate(surface=surface, protected_material_present=True)
            self.assertFalse(assessment.allowed)
            self.assertFalse(assessment.exception_permitted)
        plaintext = evaluator.evaluate(
            surface=ProhibitedSurface.UNCONTROLLED_EXPORT,
            protected_material_present=False,
            plaintext_fallback_requested=True,
        )
        self.assertFalse(plaintext.allowed)
        self.assertFalse(plaintext.exception_permitted)

    def test_unassigned_exception_authority_denies(self) -> None:
        request = SecurityExceptionRequest(
            request_reference="synthetic-exception",
            requester_reference="synthetic-requester",
            scope_references=("synthetic-scope",),
            purpose_reference="synthetic-purpose",
            classification_reference="synthetic-classification",
            residency_reference="africa-residency-required",
            compensating_control_references=("synthetic-control",),
            policy_version="synthetic-policy-v1",
            starts_at=self.now,
            expires_at=self.later,
        )
        result = SecurityExceptionEvaluator(UnassignedExceptionAuthority()).evaluate(
            request, at=self.now
        )
        self.assertFalse(result.allowed)
        self.assertFalse(result.capability_activated)
        self.assertEqual(result.code, ExceptionValidationCode.NO_CURRENT_EXCEPTION_AUTHORITY)

    def test_exception_cannot_target_an_absolute_prohibited_surface(self) -> None:
        request = SecurityExceptionRequest(
            request_reference="synthetic-exception",
            requester_reference="synthetic-requester",
            scope_references=("synthetic-scope",),
            purpose_reference="synthetic-purpose",
            classification_reference="synthetic-classification",
            residency_reference="africa-residency-required",
            compensating_control_references=("synthetic-control",),
            policy_version="synthetic-policy-v1",
            starts_at=self.now,
            expires_at=self.later,
            prohibited_surface=ProhibitedSurface.PROMPT,
        )
        result = SecurityExceptionEvaluator(UnassignedExceptionAuthority()).evaluate(
            request, at=self.now
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.code, ExceptionValidationCode.ABSOLUTE_PROHIBITION)

    def test_crypto_taxonomy_contains_only_approved_concepts(self) -> None:
        self.assertEqual(
            {scope.value for scope in ProtectionScope},
            {"AT_REST", "IN_TRANSIT", "SENSITIVE_FIELD"},
        )
        self.assertEqual(
            {tier.value for tier in KeyHierarchyTier},
            {"ROOT", "INTERMEDIATE", "DATA_ENCRYPTION"},
        )
        self.assertEqual(len(ALL_SEPARATION_DIMENSIONS), 4)

    def test_empty_crypto_policy_fails_closed_even_with_current_authorization(self) -> None:
        request = CryptographicPolicyRequest(
            request_reference="synthetic-request",
            policy_reference="synthetic-crypto-policy",
            policy_version="synthetic-policy-v1",
            protection_scope=ProtectionScope.SENSITIVE_FIELD,
            hierarchy_tier=KeyHierarchyTier.DATA_ENCRYPTION,
            required_separation_dimensions=ALL_SEPARATION_DIMENSIONS,
            authorization_decision=self.authorization(),
        )
        result = CryptographicPolicyEvaluator().evaluate(request, at=self.now)
        self.assertFalse(result.allowed)
        self.assertFalse(result.cryptography_executed)
        self.assertEqual(result.code, CryptographicValidationCode.NO_CURRENT_CRYPTOGRAPHIC_POLICY)

    def test_crypto_policy_contract_match_does_not_execute_cryptography(self) -> None:
        policy = CryptographicPolicyContract(
            policy_reference="synthetic-crypto-policy",
            policy_version="synthetic-policy-v1",
            protection_scope=ProtectionScope.SENSITIVE_FIELD,
            hierarchy_tier=KeyHierarchyTier.DATA_ENCRYPTION,
            separation_dimensions=ALL_SEPARATION_DIMENSIONS,
            agility_successor_reference="synthetic-successor-policy",
            effective_from=self.now,
            expires_at=self.later,
        )
        request = CryptographicPolicyRequest(
            request_reference="synthetic-request",
            policy_reference=policy.policy_reference,
            policy_version=policy.policy_version,
            protection_scope=policy.protection_scope,
            hierarchy_tier=policy.hierarchy_tier,
            required_separation_dimensions=ALL_SEPARATION_DIMENSIONS,
            authorization_decision=self.authorization(),
        )
        result = CryptographicPolicyEvaluator(CryptographicPolicyRegistry((policy,))).evaluate(
            request, at=self.now
        )
        self.assertTrue(result.allowed)
        self.assertFalse(result.cryptography_executed)
        self.assertEqual(result.code, CryptographicValidationCode.VALID_CONTRACT)

    def test_crypto_policy_rejects_missing_separation_dimension(self) -> None:
        with self.assertRaises(SecurityProtectionContractError):
            CryptographicPolicyContract(
                policy_reference="synthetic-crypto-policy",
                policy_version="synthetic-policy-v1",
                protection_scope=ProtectionScope.AT_REST,
                hierarchy_tier=KeyHierarchyTier.ROOT,
                separation_dimensions=ALL_SEPARATION_DIMENSIONS[:-1],
                agility_successor_reference="synthetic-successor-policy",
                effective_from=self.now,
                expires_at=self.later,
            )

    def test_seven_zones_and_source_defined_boundaries_are_exact(self) -> None:
        self.assertEqual(len(TrustZone), 7)
        self.assertEqual(
            {egress.value for egress in EgressClass},
            {
                "NO_EGRESS",
                "INTERNAL_GOVERNED_SERVICE",
                "MODEL_GATEWAY_ONLY",
                "TOOL_GATEWAY_ONLY",
                "EXPLICIT_EXTERNAL_DESTINATION",
            },
        )
        self.assertEqual(set(APPROVED_SERVICE_BOUNDARIES), set(ServiceBoundaryClass))
        application_data = APPROVED_SERVICE_BOUNDARIES[ServiceBoundaryClass.APPLICATION_TO_DATA]
        self.assertIs(application_data.source_zone, TrustZone.APPLICATION)
        self.assertEqual(application_data.destination_zones, (TrustZone.DATA,))
        self.assertNotIn(
            (TrustZone.AI, TrustZone.DATA),
            {
                (rule.source_zone, destination_zone)
                for rule in APPROVED_SERVICE_BOUNDARIES.values()
                for destination_zone in rule.destination_zones
            },
        )

    def egress_request(
        self,
        *,
        authorization: CurrentAuthorizationDecision | None = None,
        agent_ceiling: AgentEgressCeiling | None = None,
        gateway_reference: str | None = "synthetic-model-gateway",
        cross_border: bool = False,
        human_cross_border_authorized: bool = False,
    ) -> EgressEvaluationRequest:
        return EgressEvaluationRequest(
            request_reference="synthetic-request",
            correlation_id="synthetic-correlation",
            boundary_class=ServiceBoundaryClass.APPLICATION_TO_AI_VIA_MODEL_GATEWAY,
            source_zone=TrustZone.APPLICATION,
            destination_zone=TrustZone.AI,
            egress_class=EgressClass.MODEL_GATEWAY_ONLY,
            destination_reference="synthetic-model-destination",
            service_identity_reference="synthetic-service-identity",
            action_reference="synthetic-action",
            purpose_reference="synthetic-purpose",
            classification_reference="synthetic-classification",
            retention_reference="synthetic-retention-policy",
            residency_reference="africa-residency-required",
            policy_version="synthetic-policy-v1",
            authorization_decision=authorization or self.authorization(),
            gateway_reference=gateway_reference,
            agent_ceiling=agent_ceiling,
            cross_border=cross_border,
            human_cross_border_authorized=human_cross_border_authorized,
        )

    def egress_policy(self) -> EgressPolicyContract:
        return EgressPolicyContract(
            policy_reference="synthetic-egress-policy",
            policy_version="synthetic-policy-v1",
            boundary_class=ServiceBoundaryClass.APPLICATION_TO_AI_VIA_MODEL_GATEWAY,
            egress_class=EgressClass.MODEL_GATEWAY_ONLY,
            destination_reference="synthetic-model-destination",
            purpose_reference="synthetic-purpose",
            classification_reference="synthetic-classification",
            retention_reference="synthetic-retention-policy",
            residency_reference="africa-residency-required",
            effective_from=self.now,
            expires_at=self.later,
        )

    def test_empty_egress_registry_denies_and_activates_no_network(self) -> None:
        result = EgressPolicyEvaluator().evaluate(self.egress_request(), at=self.now)
        self.assertFalse(result.allowed)
        self.assertFalse(result.network_activated)
        self.assertEqual(result.code, EgressValidationCode.NO_CURRENT_EGRESS_POLICY)

    def test_gateway_and_current_authorization_are_required(self) -> None:
        evaluator = EgressPolicyEvaluator(EgressPolicyRegistry((self.egress_policy(),)))
        no_gateway = evaluator.evaluate(self.egress_request(gateway_reference=None), at=self.now)
        self.assertEqual(no_gateway.code, EgressValidationCode.GATEWAY_REQUIRED)
        denied = evaluator.evaluate(
            self.egress_request(authorization=self.authorization(effect=AuthorizationEffect.DENY)),
            at=self.now,
        )
        self.assertEqual(denied.code, EgressValidationCode.NO_CURRENT_AUTHORIZATION)

    def test_agent_egress_is_intersection_only(self) -> None:
        evaluator = EgressPolicyEvaluator(EgressPolicyRegistry((self.egress_policy(),)))
        denied_ceiling = AgentEgressCeiling(
            sandbox_permits=True,
            task_contract_permits=False,
            identity_permits=True,
            destination_eligible=True,
            classification_permits=True,
            purpose_permits=True,
            retention_permits=True,
            residency_sovereignty_permits=True,
        )
        result = evaluator.evaluate(self.egress_request(agent_ceiling=denied_ceiling), at=self.now)
        self.assertFalse(result.allowed)
        self.assertEqual(result.code, EgressValidationCode.AGENT_CEILING_DENIED)

    def test_cross_border_requires_separate_human_authorization(self) -> None:
        evaluator = EgressPolicyEvaluator(EgressPolicyRegistry((self.egress_policy(),)))
        result = evaluator.evaluate(self.egress_request(cross_border=True), at=self.now)
        self.assertFalse(result.allowed)
        self.assertEqual(result.code, EgressValidationCode.CROSS_BORDER_NOT_AUTHORIZED)

    def test_external_destination_class_requires_explicit_external_boundary(self) -> None:
        policy = EgressPolicyContract(
            policy_reference="synthetic-external-policy",
            policy_version="synthetic-policy-v1",
            boundary_class=(ServiceBoundaryClass.INTEGRATION_TO_EXPLICIT_EXTERNAL_DESTINATION),
            egress_class=EgressClass.EXPLICIT_EXTERNAL_DESTINATION,
            destination_reference="synthetic-external-destination",
            purpose_reference="synthetic-purpose",
            classification_reference="synthetic-classification",
            retention_reference="synthetic-retention-policy",
            residency_reference="africa-residency-required",
            effective_from=self.now,
            expires_at=self.later,
        )
        request = EgressEvaluationRequest(
            request_reference="synthetic-request",
            correlation_id="synthetic-correlation",
            boundary_class=policy.boundary_class,
            source_zone=TrustZone.INTEGRATION,
            destination_zone=TrustZone.INTEGRATION,
            egress_class=policy.egress_class,
            destination_reference=policy.destination_reference,
            service_identity_reference="synthetic-service-identity",
            action_reference="synthetic-action",
            purpose_reference=policy.purpose_reference,
            classification_reference=policy.classification_reference,
            retention_reference=policy.retention_reference,
            residency_reference=policy.residency_reference,
            policy_version=policy.policy_version,
            authorization_decision=self.authorization(),
            gateway_reference="synthetic-external-gateway",
        )
        result = EgressPolicyEvaluator(EgressPolicyRegistry((policy,))).evaluate(
            request, at=self.now
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.code, EgressValidationCode.EXTERNAL_BOUNDARY_REQUIRED)

    def test_exact_synthetic_policy_match_is_contract_only(self) -> None:
        evaluator = EgressPolicyEvaluator(EgressPolicyRegistry((self.egress_policy(),)))
        result = evaluator.evaluate(self.egress_request(), at=self.now)
        self.assertTrue(result.allowed)
        self.assertFalse(result.network_activated)
        self.assertEqual(result.code, EgressValidationCode.VALID_CONTRACT)

    def test_signals_are_minimized_and_non_authoritative(self) -> None:
        sink = InMemoryObservabilitySink()
        SecurityProtectionSignals(sink).emit(
            correlation_id="synthetic-correlation",
            contract_class="EGRESS",
            outcome="DENY",
            reason_code="NO_CURRENT_EGRESS_POLICY",
        )
        event = sink.events()[0]
        self.assertEqual(event.category, SignalCategory.SECURITY_CONDITION)
        self.assertFalse(event.authoritative_evidence)
        self.assertFalse(event.institutional_finding)
        self.assertFalse(event.institutional_decision)
        self.assertEqual(
            event.attributes,
            (
                ("contract_class", "EGRESS"),
                ("outcome", "DENY"),
                ("reason_code", "NO_CURRENT_EGRESS_POLICY"),
            ),
        )


if __name__ == "__main__":
    unittest.main()
