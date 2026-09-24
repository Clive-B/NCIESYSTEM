"""Deterministic local and negative-path tests for WBS-16-WP-006."""

import unittest
from dataclasses import replace
from datetime import UTC, datetime, timedelta

from ncie_foundation.agent_model_tool_context_security import (
    AGENT_SECURITY_DECISION_EVIDENCE,
    AGENT_SECURITY_IMPLEMENTATION_AUTHORITY,
    ALL_RESOURCE_CEILING_DIMENSIONS,
    EMPTY_AGENT_PRIMITIVE_REGISTRY,
    EMPTY_CROSS_CONTEXT_EXCEPTION_REGISTRY,
    EMPTY_MODEL_ELIGIBILITY_REGISTRY,
    EMPTY_TOOL_ELIGIBILITY_REGISTRY,
    AgentDefinition,
    AgentPrimitive,
    AgentPrimitiveClass,
    AgentPrimitiveRegistry,
    AgentSecurityCeiling,
    AgentSecurityContractError,
    BoundaryDisposition,
    ContextAccessRequest,
    ContextClass,
    CrossContextException,
    CrossContextExceptionRegistry,
    DenyAllCrossContextBoundary,
    GeneratedCodeQuarantineMetadata,
    GeneratedCodeState,
    InstitutionalAuthorityClass,
    ModelEligibilityRegistry,
    ModelLifecycleState,
    ModelProviderEligibility,
    ModelRouteRequest,
    NoInvocationToolGateway,
    NoRouteModelGateway,
    PromptInjectionBoundary,
    ResourceCeilingDimension,
    SecurityBoundarySignal,
    ToolEligibility,
    ToolEligibilityRegistry,
    ToolRequest,
    ToolRiskClass,
    ToolRiskPredicate,
    UnassignedInstitutionalAuthorities,
    UntrustedContentOrigin,
    UntrustedInstructionSignal,
    ZeroCapabilityAgentFactory,
)
from ncie_foundation.security_authorization import (
    ALL_AUTHORIZATION_DIMENSIONS,
    AuthorizationEffect,
    CurrentAuthorizationDecision,
)


class Wbs16Wp006SecurityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 24, 12, tzinfo=UTC)
        self.later = self.now + timedelta(hours=1)

    def authorization(
        self,
        request_reference: str,
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

    def ceiling(self) -> AgentSecurityCeiling:
        return AgentSecurityCeiling(
            ceiling_reference="synthetic-ceiling",
            policy_version="synthetic-policy-v1",
            resource_limit_references=tuple(
                (dimension, f"limit:{dimension.value.lower()}")
                for dimension in ALL_RESOURCE_CEILING_DIMENSIONS
            ),
        )

    def definition(self) -> AgentDefinition:
        return AgentDefinition(
            definition_reference="synthetic-definition",
            purpose_reference="synthetic-purpose",
            task_reference="synthetic-task",
            input_schema_reference="schema:input",
            output_schema_reference="schema:output",
            model_reference="model:synthetic",
            tool_references=("tool:synthetic",),
            data_class_references=("data:synthetic",),
            context_reference="context:synthetic",
            execution_runtime_reference="runtime:synthetic-inert",
            authorization_policy_reference="policy:synthetic",
            delegation_depth_policy_reference="delegation:none",
            egress_policy_reference="egress:none",
            persistence_policy_reference="persistence:none",
            vpf_profile_reference="vpf:synthetic-profile",
            ceiling=self.ceiling(),
            provenance_reference="provenance:synthetic",
            evaluation_reference="evaluation:synthetic",
            expiry_policy_reference="expiry:synthetic",
        )

    def agent_registry(self) -> AgentPrimitiveRegistry:
        entries = (
            AgentPrimitive("schema:input", AgentPrimitiveClass.SCHEMA, "synthetic-policy-v1"),
            AgentPrimitive("schema:output", AgentPrimitiveClass.SCHEMA, "synthetic-policy-v1"),
            AgentPrimitive("model:synthetic", AgentPrimitiveClass.MODEL, "synthetic-policy-v1"),
            AgentPrimitive("tool:synthetic", AgentPrimitiveClass.TOOL, "synthetic-policy-v1"),
            AgentPrimitive("data:synthetic", AgentPrimitiveClass.DATA_CLASS, "synthetic-policy-v1"),
            AgentPrimitive("context:synthetic", AgentPrimitiveClass.CONTEXT, "synthetic-policy-v1"),
            AgentPrimitive(
                "runtime:synthetic-inert",
                AgentPrimitiveClass.EXECUTION_RUNTIME,
                "synthetic-policy-v1",
            ),
            AgentPrimitive("policy:synthetic", AgentPrimitiveClass.POLICY, "synthetic-policy-v1"),
        )
        return AgentPrimitiveRegistry("synthetic-registry-v1", entries)

    def model_request(self) -> ModelRouteRequest:
        return ModelRouteRequest(
            request_reference="synthetic-model-request",
            provider_reference="provider:synthetic",
            model_reference="model:synthetic",
            deployment_reference="deployment:synthetic",
            data_class_reference="data:synthetic",
            classification_reference="classification:synthetic",
            purpose_reference="purpose:synthetic",
            task_reference="task:synthetic",
            residency_reference="residency:synthetic-african",
            retention_reuse_policy_reference="retention:synthetic",
            security_assurance_reference="assurance:synthetic",
            tool_requirement_reference="tools:none",
            output_policy_reference="output:synthetic",
            policy_version="synthetic-policy-v1",
        )

    def model_registry(self) -> ModelEligibilityRegistry:
        request = self.model_request()
        return ModelEligibilityRegistry(
            "synthetic-registry-v1",
            (
                ModelProviderEligibility(
                    combination_reference="combination:synthetic",
                    provider_reference=request.provider_reference,
                    model_reference=request.model_reference,
                    deployment_reference=request.deployment_reference,
                    data_class_reference=request.data_class_reference,
                    classification_reference=request.classification_reference,
                    purpose_reference=request.purpose_reference,
                    task_reference=request.task_reference,
                    residency_reference=request.residency_reference,
                    retention_reuse_policy_reference=request.retention_reuse_policy_reference,
                    security_assurance_reference=request.security_assurance_reference,
                    tool_requirement_reference=request.tool_requirement_reference,
                    output_policy_reference=request.output_policy_reference,
                    lifecycle_state=ModelLifecycleState.APPROVED_ACTIVE,
                    policy_version=request.policy_version,
                ),
            ),
        )

    def tool_request(
        self,
        risk_class: ToolRiskClass = ToolRiskClass.READ_ONLY_LOW_DISCLOSURE_RISK,
        *,
        predicates: tuple[ToolRiskPredicate, ...] = (),
        approval: str | None = None,
    ) -> ToolRequest:
        return ToolRequest(
            request_reference="synthetic-tool-request",
            actor_reference="actor:synthetic",
            delegation_chain_reference="delegation:none",
            tool_reference="tool:synthetic",
            tool_version_reference="tool-version:synthetic",
            risk_class=risk_class,
            action_reference="action:synthetic",
            target_reference="target:synthetic",
            purpose_reference="purpose:synthetic",
            policy_version="synthetic-policy-v1",
            task_reference="task:synthetic",
            context_reference="context:synthetic",
            input_schema_reference="schema:input",
            output_schema_reference="schema:output",
            classification_ceiling_reference="classification:synthetic",
            assurance_reference="assurance:synthetic",
            correlation_reference="correlation:synthetic",
            idempotency_reference="idempotency:synthetic",
            expiry_reference="expiry:synthetic",
            risk_predicates=predicates,
            high_risk_approval_reference=approval,
        )

    def tool_registry(self, request: ToolRequest) -> ToolEligibilityRegistry:
        return ToolEligibilityRegistry(
            "synthetic-registry-v1",
            (
                ToolEligibility(
                    tool_reference=request.tool_reference,
                    tool_version_reference=request.tool_version_reference,
                    risk_class=request.risk_class,
                    action_reference=request.action_reference,
                    target_reference=request.target_reference,
                    purpose_reference=request.purpose_reference,
                    policy_version=request.policy_version,
                ),
            ),
        )

    def context_request(self) -> ContextAccessRequest:
        return ContextAccessRequest(
            request_reference="synthetic-context-request",
            actor_reference="actor:synthetic",
            source_context_reference="context:source",
            source_context_class=ContextClass.PRIVATE_USER,
            destination_context_reference="context:destination",
            destination_context_class=ContextClass.SITUATION_TASK,
            data_class_reference="data:synthetic",
            purpose_reference="purpose:synthetic",
            field_references=("field:synthetic",),
            classification_reference="classification:synthetic",
            temporal_mode_reference="temporal:current",
            source_scope_reference="scope:synthetic",
            relevance_policy_reference="relevance:synthetic",
            minimum_necessary_filter_reference="filter:synthetic",
            policy_version="synthetic-policy-v1",
        )

    def context_exception(self) -> CrossContextException:
        request = self.context_request()
        return CrossContextException(
            exception_reference="exception:synthetic",
            source_context_reference=request.source_context_reference,
            source_context_class=request.source_context_class,
            destination_context_reference=request.destination_context_reference,
            destination_context_class=request.destination_context_class,
            data_class_reference=request.data_class_reference,
            purpose_reference=request.purpose_reference,
            actor_reference=request.actor_reference,
            accountable_human_reference="human:synthetic",
            field_references=request.field_references,
            classification_reference=request.classification_reference,
            legal_consent_authority_references=("authority:synthetic",),
            source_authorization_reference="authorization:source",
            destination_authorization_reference="authorization:destination",
            minimum_necessary_justification_reference="justification:synthetic",
            processing_destination_reference="destination:processing",
            storage_destination_reference="destination:storage",
            residency_reference="residency:synthetic-african",
            source_owner_decision_reference="decision:source-owner",
            destination_owner_decision_reference="decision:destination-owner",
            independent_review_reference="review:synthetic",
            provenance_reference="provenance:synthetic",
            audit_reference="audit:synthetic",
            downstream_dependency_references=("dependency:synthetic",),
            deletion_reconciliation_reference="obligation:synthetic",
            effective_at=self.now,
            expires_at=self.later,
            policy_version=request.policy_version,
        )

    def test_provenance_and_all_controlled_registries_are_empty(self) -> None:
        self.assertEqual(
            AGENT_SECURITY_DECISION_EVIDENCE,
            "NCIE-WBS16-OWNER-DECISION-2026-09-24-023",
        )
        self.assertEqual(
            AGENT_SECURITY_IMPLEMENTATION_AUTHORITY,
            "NCIE-WBS16-OWNER-DECISION-2026-09-24-024",
        )
        self.assertTrue(EMPTY_AGENT_PRIMITIVE_REGISTRY.is_empty())
        self.assertTrue(EMPTY_MODEL_ELIGIBILITY_REGISTRY.is_empty())
        self.assertTrue(EMPTY_TOOL_ELIGIBILITY_REGISTRY.is_empty())
        self.assertTrue(EMPTY_CROSS_CONTEXT_EXCEPTION_REGISTRY.is_empty())

    def test_all_institutional_authorities_are_unassigned(self) -> None:
        boundary = UnassignedInstitutionalAuthorities()
        for authority_class in InstitutionalAuthorityClass:
            self.assertIsNone(boundary.assignment_for(authority_class))

    def test_resource_dimensions_are_symbolic_and_complete(self) -> None:
        self.assertEqual(set(ALL_RESOURCE_CEILING_DIMENSIONS), set(ResourceCeilingDimension))
        self.assertEqual(len(self.ceiling().resource_limit_references), 8)

    def test_missing_resource_dimension_is_rejected(self) -> None:
        with self.assertRaises(AgentSecurityContractError):
            replace(
                self.ceiling(),
                resource_limit_references=self.ceiling().resource_limit_references[:-1],
            )

    def test_agent_capability_flag_is_rejected(self) -> None:
        with self.assertRaises(AgentSecurityContractError):
            replace(self.ceiling(), network_access_allowed=True)

    def test_controlled_factory_denies_missing_primitives(self) -> None:
        result = ZeroCapabilityAgentFactory().validate(self.definition())
        self.assertEqual(result.disposition, BoundaryDisposition.DENIED)
        self.assertFalse(result.capability_granted)
        self.assertFalse(result.external_operation_executed)

    def test_synthetic_definition_validation_still_creates_no_capability(self) -> None:
        result = ZeroCapabilityAgentFactory(self.agent_registry()).validate(self.definition())
        self.assertEqual(result.disposition, BoundaryDisposition.VALIDATED_NO_CAPABILITY)
        self.assertFalse(result.capability_granted)
        self.assertFalse(result.external_operation_executed)

    def test_generated_code_is_quarantine_metadata_only(self) -> None:
        metadata = GeneratedCodeQuarantineMetadata(
            "artifact:synthetic", "provenance:synthetic", "synthetic-policy-v1"
        )
        self.assertEqual(metadata.state, GeneratedCodeState.NOT_APPROVED_FOR_EXECUTION)
        self.assertFalse(metadata.generated)
        self.assertFalse(metadata.executed)

    def test_generated_code_operation_flags_are_rejected(self) -> None:
        with self.assertRaises(AgentSecurityContractError):
            GeneratedCodeQuarantineMetadata(
                "artifact:synthetic",
                "provenance:synthetic",
                "synthetic-policy-v1",
                loaded=True,
            )

    def test_empty_model_registry_returns_no_route(self) -> None:
        request = self.model_request()
        result = NoRouteModelGateway().evaluate(
            request, self.authorization(request.request_reference)
        )
        self.assertEqual(result.reason_code, "NO_ELIGIBLE_MODEL_ROUTE")
        self.assertFalse(result.external_operation_executed)

    def test_model_gateway_requires_current_exact_authorization(self) -> None:
        request = self.model_request()
        gateway = NoRouteModelGateway(self.model_registry())
        for authorization in (
            None,
            self.authorization("stale-request"),
            self.authorization(request.request_reference, effect=AuthorizationEffect.DENY),
        ):
            self.assertEqual(
                gateway.evaluate(request, authorization).reason_code,
                "CURRENT_AUTHORIZATION_REQUIRED",
            )

    def test_even_synthetic_eligible_model_has_no_route_capability(self) -> None:
        request = self.model_request()
        result = NoRouteModelGateway(self.model_registry()).evaluate(
            request, self.authorization(request.request_reference)
        )
        self.assertEqual(result.reason_code, "MODEL_GATEWAY_HAS_NO_ROUTE_CAPABILITY")
        self.assertFalse(result.capability_granted)

    def test_model_eligibility_is_residency_and_retention_exact(self) -> None:
        request = replace(self.model_request(), residency_reference="residency:different")
        result = NoRouteModelGateway(self.model_registry()).evaluate(
            request, self.authorization(request.request_reference)
        )
        self.assertEqual(result.reason_code, "NO_ELIGIBLE_MODEL_ROUTE")

    def test_exact_four_tool_classes_are_defined(self) -> None:
        self.assertEqual(
            {risk.value for risk in ToolRiskClass},
            {
                "READ_ONLY_LOW_DISCLOSURE_RISK",
                "READ_ONLY_HIGH_DISCLOSURE_RISK",
                "STATE_CHANGING_REVERSIBLE",
                "STATE_CHANGING_CONSEQUENTIAL",
            },
        )

    def test_empty_tool_registry_denies_without_invocation(self) -> None:
        request = self.tool_request()
        result = NoInvocationToolGateway().evaluate(
            request, self.authorization(request.request_reference)
        )
        self.assertEqual(result.reason_code, "TOOL_NOT_REGISTERED_OR_ELIGIBLE")
        self.assertFalse(result.external_operation_executed)

    def test_tool_gateway_requires_current_exact_authorization(self) -> None:
        request = self.tool_request()
        result = NoInvocationToolGateway(self.tool_registry(request)).evaluate(request, None)
        self.assertEqual(result.reason_code, "CURRENT_AUTHORIZATION_REQUIRED")

    def test_high_disclosure_tool_requires_approval_then_unassigned_authority_denies(self) -> None:
        request = self.tool_request(ToolRiskClass.READ_ONLY_HIGH_DISCLOSURE_RISK)
        gateway = NoInvocationToolGateway(self.tool_registry(request))
        authorization = self.authorization(request.request_reference)
        self.assertEqual(
            gateway.evaluate(request, authorization).reason_code, "HIGH_RISK_APPROVAL_REQUIRED"
        )
        with_approval = replace(request, high_risk_approval_reference="approval:synthetic")
        self.assertEqual(
            gateway.evaluate(with_approval, authorization).reason_code,
            "HIGH_RISK_AUTHORITY_UNASSIGNED",
        )

    def test_low_class_tool_with_code_predicate_is_high_risk(self) -> None:
        request = self.tool_request(predicates=(ToolRiskPredicate.CODE_EXECUTION,))
        result = NoInvocationToolGateway(self.tool_registry(request)).evaluate(
            request, self.authorization(request.request_reference)
        )
        self.assertEqual(result.reason_code, "HIGH_RISK_APPROVAL_REQUIRED")

    def test_even_synthetic_low_risk_tool_cannot_be_invoked(self) -> None:
        request = self.tool_request()
        result = NoInvocationToolGateway(self.tool_registry(request)).evaluate(
            request, self.authorization(request.request_reference)
        )
        self.assertEqual(result.reason_code, "TOOL_GATEWAY_HAS_NO_INVOCATION_CAPABILITY")
        self.assertFalse(result.external_operation_executed)

    def test_every_untrusted_origin_has_no_instruction_authority(self) -> None:
        boundary = PromptInjectionBoundary()
        for origin in UntrustedContentOrigin:
            result = boundary.evaluate(
                UntrustedInstructionSignal(
                    f"content:{origin.value.lower()}",
                    origin,
                    instruction_shaped=True,
                    requests_policy_change=True,
                )
            )
            self.assertEqual(result.reason_code, "UNTRUSTED_INSTRUCTION_HAS_NO_AUTHORITY")
            self.assertFalse(result.capability_granted)

    def test_untrusted_plain_data_remains_non_authoritative(self) -> None:
        result = PromptInjectionBoundary().evaluate(
            UntrustedInstructionSignal(
                "content:synthetic", UntrustedContentOrigin.DOCUMENT, instruction_shaped=False
            )
        )
        self.assertEqual(result.disposition, BoundaryDisposition.VALIDATED_NO_CAPABILITY)
        self.assertFalse(result.capability_granted)

    def test_context_taxonomy_contains_exact_eight_classes(self) -> None:
        self.assertEqual(len(ContextClass), 8)

    def test_empty_context_registry_denies_without_retrieval_or_transfer(self) -> None:
        request = self.context_request()
        result = DenyAllCrossContextBoundary().evaluate(
            request,
            self.authorization(request.request_reference),
            at=self.now,
        )
        self.assertEqual(result.reason_code, "NO_CROSS_CONTEXT_EXCEPTION")
        self.assertFalse(result.external_operation_executed)

    def test_context_boundary_requires_current_authorization(self) -> None:
        request = self.context_request()
        result = DenyAllCrossContextBoundary().evaluate(request, None, at=self.now)
        self.assertEqual(result.reason_code, "CURRENT_AUTHORIZATION_REQUIRED")

    def test_current_synthetic_exception_still_cannot_transfer(self) -> None:
        request = self.context_request()
        registry = CrossContextExceptionRegistry(
            "synthetic-registry-v1", (self.context_exception(),)
        )
        result = DenyAllCrossContextBoundary(registry).evaluate(
            request,
            self.authorization(request.request_reference),
            at=self.now,
        )
        self.assertEqual(result.reason_code, "CROSS_CONTEXT_TRANSFER_CAPABILITY_ABSENT")
        self.assertFalse(result.capability_granted)

    def test_expired_or_revoked_context_exception_denies(self) -> None:
        request = self.context_request()
        authorization = self.authorization(request.request_reference)
        for exception in (
            self.context_exception(),
            replace(self.context_exception(), revoked=True),
        ):
            registry = CrossContextExceptionRegistry("synthetic-registry-v1", (exception,))
            at = self.later if not exception.revoked else self.now
            result = DenyAllCrossContextBoundary(registry).evaluate(request, authorization, at=at)
            self.assertEqual(result.reason_code, "CONTEXT_EXCEPTION_NOT_CURRENT")

    def test_same_context_has_no_direct_retrieval_path(self) -> None:
        request = self.context_request()
        request = replace(
            request,
            destination_context_reference=request.source_context_reference,
            destination_context_class=request.source_context_class,
        )
        result = DenyAllCrossContextBoundary().evaluate(
            request,
            self.authorization(request.request_reference),
            at=self.now,
        )
        self.assertEqual(result.reason_code, "NO_CONTEXT_RETRIEVAL_CAPABILITY")

    def test_minimized_signal_cannot_be_authoritative(self) -> None:
        signal = SecurityBoundarySignal(
            "correlation:synthetic",
            "boundary:synthetic",
            BoundaryDisposition.DENIED,
            "NO_CAPABILITY",
            "synthetic-policy-v1",
        )
        self.assertFalse(signal.authoritative)
        with self.assertRaises(AgentSecurityContractError):
            replace(signal, authoritative=True)

    def test_protected_reference_input_is_rejected_without_echo(self) -> None:
        candidate = "secret_value=do-not-echo"
        with self.assertRaises(AgentSecurityContractError) as caught:
            AgentPrimitive(candidate, AgentPrimitiveClass.MODEL, "synthetic-policy-v1")
        self.assertNotIn("do-not-echo", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
