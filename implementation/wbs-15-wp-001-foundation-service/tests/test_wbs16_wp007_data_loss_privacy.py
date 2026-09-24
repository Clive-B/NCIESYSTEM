"""Deterministic metadata-only tests for WBS-16-WP-007."""

import unittest
from dataclasses import replace
from datetime import UTC, datetime, timedelta

from ncie_foundation.agent_model_tool_context_security import UntrustedContentOrigin
from ncie_foundation.data_loss_privacy import (
    ALL_NON_WAIVABLE_PROTECTIONS,
    DATA_LOSS_PRIVACY_DECISION_EVIDENCE,
    DATA_LOSS_PRIVACY_IMPLEMENTATION_AUTHORITY,
    DLP_PROCESSING_ORDER,
    EMPTY_CHANNEL_DESTINATION_REGISTRY,
    EMPTY_DISCLOSURE_AUTHORITY_REGISTRY,
    EMPTY_DISCLOSURE_EXCEPTION_REGISTRY,
    EMPTY_DLP_RULE_REGISTRY,
    EMPTY_PRIVACY_AUTHORITY_REGISTRY,
    EMPTY_PROTECTED_IDENTITY_ACCESS_REGISTRY,
    ChannelDestinationPolicy,
    ChannelDestinationRegistry,
    ClassificationTier,
    ClassificationTransform,
    DataLossPrivacyContractError,
    DataLossPrivacySignal,
    DataTransformClass,
    DisclosureAuthorityAssignment,
    DisclosureAuthorityDecision,
    DisclosureAuthorityRegistry,
    DisclosureEffect,
    DisclosureException,
    DisclosureExceptionRegistry,
    DisclosureRequest,
    DlpDisposition,
    DlpPath,
    DlpProcessingStage,
    DlpRule,
    DlpRuleRegistry,
    FieldClassification,
    NonWaivableProtection,
    NoOutputDlpBoundary,
    NoOutputReason,
    NoRevealProtectedIdentityBoundary,
    OpaqueProtectedIdentityReference,
    OutputChannelClass,
    PrivacyAuthorityRegistry,
    PrivacyEscalationBoundary,
    PrivacyEscalationDisposition,
    PrivacyEscalationReason,
    PrivacyEscalationRequest,
    ProtectedIdentityAccessRegistry,
    ProtectedIdentityAccessRule,
    ProtectedIdentityHandlingClass,
    RecipientAuthorization,
    UnassignedWp007Authorities,
    UntrustedDisclosureClaim,
    Wp007AuthorityClass,
    classification_floor,
    evaluate_untrusted_disclosure_claim,
)
from ncie_foundation.security_authorization import (
    ALL_AUTHORIZATION_DIMENSIONS,
    AuthorizationEffect,
    CurrentAuthorizationDecision,
)


class Wbs16Wp007DataLossPrivacyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 24, 12, tzinfo=UTC)
        self.later = self.now + timedelta(hours=1)

    def authorization(
        self,
        request_reference: str = "synthetic-disclosure-request",
        *,
        effect: AuthorizationEffect = AuthorizationEffect.PERMIT,
    ) -> CurrentAuthorizationDecision:
        return CurrentAuthorizationDecision(
            request_reference=request_reference,
            policy_version="synthetic-policy-v1",
            effect=effect,
            reason_code="SYNTHETIC_TEST_DECISION",
            evaluated_dimensions=ALL_AUTHORIZATION_DIMENSIONS,
        )

    def request(
        self,
        *,
        recipients: tuple[str, ...] = ("recipient:synthetic",),
        minimum_fields: tuple[str, ...] = ("field:alpha", "field:beta"),
        cross_border: bool = False,
        channel_class: OutputChannelClass = OutputChannelClass.PROTECTED_VISUAL_DISPLAY,
    ) -> DisclosureRequest:
        return DisclosureRequest(
            request_reference="synthetic-disclosure-request",
            correlation_reference="correlation:synthetic",
            actor_reference="actor:synthetic",
            delegation_reference="delegation:none",
            recipient_references=recipients,
            object_reference="object:synthetic",
            fields=(
                FieldClassification("field:alpha", ClassificationTier.INTERNAL, "provenance:alpha"),
                FieldClassification("field:beta", ClassificationTier.PROTECTED, "provenance:beta"),
            ),
            minimum_necessary_field_references=minimum_fields,
            action_reference="action:synthetic",
            purpose_reference="purpose:synthetic",
            task_reference="task:synthetic",
            context_reference="context:synthetic",
            path=DlpPath.TOOL_INVOCATION_INPUT_OUTPUT,
            channel_reference="channel:synthetic",
            channel_class=channel_class,
            destination_reference="destination:synthetic-local",
            residency_reference="residency:synthetic-african",
            retention_policy_reference="retention:synthetic",
            reuse_policy_reference="reuse:synthetic",
            dlp_rule_reference="dlp-rule:synthetic",
            minimization_plan_reference="minimization:synthetic",
            audit_reference="audit:synthetic",
            downstream_handling_reference="handling:synthetic",
            effective_at=self.now,
            expires_at=self.later + timedelta(hours=1),
            policy_version="synthetic-policy-v1",
            provenance_references=("provenance:synthetic",),
            legal_basis_reference="legal-basis:synthetic",
            consent_reference="consent:synthetic",
            cross_border=cross_border,
        )

    def dlp_registry(self) -> DlpRuleRegistry:
        return DlpRuleRegistry(
            "synthetic-registry-v1",
            (
                DlpRule(
                    "dlp-rule:synthetic",
                    DlpPath.TOOL_INVOCATION_INPUT_OUTPUT,
                    ClassificationTier.SENSITIVE,
                    (OutputChannelClass.PROTECTED_VISUAL_DISPLAY,),
                    DlpDisposition.POLICY_CHECK_SATISFIED,
                    "synthetic-policy-v1",
                ),
            ),
        )

    def channel_registry(self, *, cross_border_allowed: bool = False) -> ChannelDestinationRegistry:
        return ChannelDestinationRegistry(
            "synthetic-registry-v1",
            (
                ChannelDestinationPolicy(
                    "channel:synthetic",
                    OutputChannelClass.PROTECTED_VISUAL_DISPLAY,
                    "destination:synthetic-local",
                    "residency:synthetic-african",
                    ClassificationTier.SENSITIVE,
                    "synthetic-policy-v1",
                    active=True,
                    cross_border_allowed=cross_border_allowed,
                ),
            ),
        )

    def authority_registry(
        self, recipients: tuple[str, ...] = ("recipient:synthetic",)
    ) -> DisclosureAuthorityRegistry:
        return DisclosureAuthorityRegistry(
            "synthetic-registry-v1",
            (
                DisclosureAuthorityAssignment(
                    "authority-assignment:synthetic",
                    recipients,
                    OutputChannelClass.PROTECTED_VISUAL_DISPLAY,
                    "purpose:synthetic",
                    "synthetic-policy-v1",
                ),
            ),
        )

    def disclosure_decision(
        self, *, effect: DisclosureEffect = DisclosureEffect.PERMIT, revoked: bool = False
    ) -> DisclosureAuthorityDecision:
        return DisclosureAuthorityDecision(
            "disclosure-decision:synthetic",
            "synthetic-disclosure-request",
            "authority-assignment:synthetic",
            effect,
            self.now,
            self.later,
            "synthetic-policy-v1",
            "SYNTHETIC_TEST_DECISION",
            revoked=revoked,
        )

    def recipients(
        self,
        refs: tuple[str, ...] = ("recipient:synthetic",),
        *,
        deny_last: bool = False,
    ) -> tuple[RecipientAuthorization, ...]:
        values: list[RecipientAuthorization] = []
        for index, reference in enumerate(refs):
            effect = (
                AuthorizationEffect.DENY
                if deny_last and index == len(refs) - 1
                else AuthorizationEffect.PERMIT
            )
            values.append(RecipientAuthorization(reference, self.authorization(effect=effect)))
        return tuple(values)

    def boundary(
        self, recipients: tuple[str, ...] = ("recipient:synthetic",)
    ) -> NoOutputDlpBoundary:
        return NoOutputDlpBoundary(
            self.dlp_registry(), self.channel_registry(), self.authority_registry(recipients)
        )

    def exception(self) -> DisclosureException:
        return DisclosureException(
            exception_reference="exception:synthetic",
            exception_type_reference="exception-type:synthetic",
            requester_reference="requester:synthetic",
            accountable_human_reference="human:synthetic",
            approver_reference="approver:synthetic",
            object_reference="object:synthetic",
            field_references=("field:synthetic",),
            classification=ClassificationTier.PROTECTED,
            handling_class=ProtectedIdentityHandlingClass.MASKED_OR_TOKENIZED,
            recipient_references=("recipient:synthetic",),
            purpose_reference="purpose:synthetic",
            channel_reference="channel:synthetic",
            destination_reference="destination:synthetic-local",
            residency_reference="residency:synthetic-african",
            legal_basis_reference="legal-basis:synthetic",
            consent_reference="consent:synthetic",
            authorization_reference="authorization:synthetic",
            dlp_decision_reference="dlp-decision:synthetic",
            disclosure_decision_reference="disclosure-decision:synthetic",
            minimization_plan_reference="minimization:synthetic",
            compensating_control_references=("control:synthetic",),
            independent_review_reference="review:synthetic",
            provenance_reference="provenance:synthetic",
            audit_reference="audit:synthetic",
            deletion_reconciliation_reference="reconciliation:synthetic",
            effective_at=self.now,
            expires_at=self.later,
            policy_version="synthetic-policy-v1",
        )

    def test_decision_provenance_and_six_controlled_registries_are_empty(self) -> None:
        self.assertEqual(
            DATA_LOSS_PRIVACY_DECISION_EVIDENCE,
            "NCIE-WBS16-OWNER-DECISION-2026-09-24-026",
        )
        self.assertEqual(
            DATA_LOSS_PRIVACY_IMPLEMENTATION_AUTHORITY,
            "NCIE-WBS16-OWNER-DECISION-2026-09-24-027",
        )
        for registry in (
            EMPTY_DLP_RULE_REGISTRY,
            EMPTY_CHANNEL_DESTINATION_REGISTRY,
            EMPTY_DISCLOSURE_AUTHORITY_REGISTRY,
            EMPTY_PROTECTED_IDENTITY_ACCESS_REGISTRY,
            EMPTY_PRIVACY_AUTHORITY_REGISTRY,
            EMPTY_DISCLOSURE_EXCEPTION_REGISTRY,
        ):
            self.assertTrue(registry.is_empty())

    def test_exact_five_dlp_paths(self) -> None:
        self.assertEqual(len(DlpPath), 5)

    def test_exact_nine_dlp_dispositions(self) -> None:
        self.assertEqual(len(DlpDisposition), 9)

    def test_all_wp007_authorities_are_unassigned(self) -> None:
        boundary = UnassignedWp007Authorities()
        for authority in Wp007AuthorityClass:
            self.assertIsNone(boundary.assignment_for(authority))

    def test_classification_floor_uses_most_protective_field(self) -> None:
        self.assertEqual(classification_floor(self.request().fields), ClassificationTier.PROTECTED)

    def test_empty_classification_set_is_rejected(self) -> None:
        with self.assertRaises(DataLossPrivacyContractError):
            classification_floor(())

    def test_transform_cannot_declassify(self) -> None:
        for transform in DataTransformClass:
            with self.assertRaises(DataLossPrivacyContractError):
                ClassificationTransform(
                    "field:synthetic",
                    transform,
                    ClassificationTier.SENSITIVE,
                    ClassificationTier.PROTECTED,
                    "policy:synthetic",
                )

    def test_transform_may_preserve_or_raise_classification(self) -> None:
        transformed = ClassificationTransform(
            "field:synthetic",
            DataTransformClass.MASK,
            ClassificationTier.PROTECTED,
            ClassificationTier.PROTECTED,
            "policy:synthetic",
        )
        self.assertEqual(transformed.resulting_tier, ClassificationTier.PROTECTED)

    def test_request_carries_metadata_and_no_content_payload_field(self) -> None:
        request = self.request()
        self.assertFalse(hasattr(request, "content"))
        self.assertFalse(hasattr(request, "payload"))
        self.assertFalse(hasattr(request, "prompt"))

    def test_processing_order_is_explicit_and_deterministic(self) -> None:
        self.assertEqual(
            DLP_PROCESSING_ORDER,
            (
                DlpProcessingStage.CLASSIFICATION_FLOOR,
                DlpProcessingStage.MINIMUM_NECESSARY,
                DlpProcessingStage.MASKING_TOKENIZATION,
                DlpProcessingStage.REDACTION,
                DlpProcessingStage.SUPPRESSION,
                DlpProcessingStage.RECLASSIFICATION,
                DlpProcessingStage.RECIPIENT_AUTHORIZATION,
                DlpProcessingStage.CHANNEL_DESTINATION,
                DlpProcessingStage.DISCLOSURE_AUTHORITY,
            ),
        )

    def test_expired_or_revoked_disclosure_candidate_denies(self) -> None:
        for request, evaluated_at in (
            (replace(self.request(), expires_at=self.later), self.later),
            (replace(self.request(), revoked=True), self.now),
        ):
            result = self.boundary().evaluate(
                request,
                self.authorization(),
                self.recipients(),
                self.disclosure_decision(),
                at=evaluated_at,
            )
            self.assertEqual(result.reason, NoOutputReason.REQUEST_NOT_CURRENT)

    def test_minimum_necessary_must_be_subset(self) -> None:
        with self.assertRaises(DataLossPrivacyContractError):
            self.request(minimum_fields=("field:not-present",))

    def test_controlled_empty_dlp_registry_denies(self) -> None:
        request = self.request()
        result = NoOutputDlpBoundary().evaluate(
            request,
            self.authorization(),
            self.recipients(),
            None,
            at=self.now,
        )
        self.assertEqual(result.reason, NoOutputReason.NO_DLP_RULE)
        self.assertFalse(result.output_emitted)

    def test_actor_authorization_is_current_and_exact(self) -> None:
        request = self.request()
        result = self.boundary().evaluate(
            request,
            self.authorization("stale-request"),
            self.recipients(),
            self.disclosure_decision(),
            at=self.now,
        )
        self.assertEqual(result.reason, NoOutputReason.CURRENT_AUTHORIZATION_REQUIRED)

    def test_mixed_recipient_authority_is_not_pooled(self) -> None:
        refs = ("recipient:alpha", "recipient:beta")
        request = self.request(recipients=refs)
        result = self.boundary(refs).evaluate(
            request,
            self.authorization(),
            self.recipients(refs, deny_last=True),
            self.disclosure_decision(),
            at=self.now,
        )
        self.assertEqual(result.reason, NoOutputReason.RECIPIENT_AUTHORIZATION_REQUIRED)

    def test_missing_recipient_decision_denies(self) -> None:
        request = self.request(recipients=("recipient:alpha", "recipient:beta"))
        result = self.boundary(request.recipient_references).evaluate(
            request,
            self.authorization(),
            self.recipients(("recipient:alpha",)),
            self.disclosure_decision(),
            at=self.now,
        )
        self.assertEqual(result.reason, NoOutputReason.RECIPIENT_AUTHORIZATION_REQUIRED)

    def test_non_minimized_candidate_denies(self) -> None:
        request = self.request(minimum_fields=("field:alpha",))
        result = self.boundary().evaluate(
            request,
            self.authorization(),
            self.recipients(),
            self.disclosure_decision(),
            at=self.now,
        )
        self.assertEqual(result.reason, NoOutputReason.MINIMIZATION_REQUIRED)

    def test_no_active_channel_denies(self) -> None:
        request = self.request()
        boundary = NoOutputDlpBoundary(
            self.dlp_registry(), ChannelDestinationRegistry("synthetic-empty-v1")
        )
        result = boundary.evaluate(
            request, self.authorization(), self.recipients(), None, at=self.now
        )
        self.assertEqual(result.reason, NoOutputReason.NO_ACTIVE_CHANNEL_DESTINATION)

    def test_cross_border_always_denies(self) -> None:
        request = self.request(cross_border=True)
        boundary = NoOutputDlpBoundary(
            self.dlp_registry(), self.channel_registry(cross_border_allowed=True)
        )
        result = boundary.evaluate(
            request, self.authorization(), self.recipients(), None, at=self.now
        )
        self.assertEqual(result.reason, NoOutputReason.CROSS_BORDER_DENIED)

    def test_unassigned_disclosure_authority_denies(self) -> None:
        request = self.request()
        boundary = NoOutputDlpBoundary(self.dlp_registry(), self.channel_registry())
        result = boundary.evaluate(
            request,
            self.authorization(),
            self.recipients(),
            self.disclosure_decision(),
            at=self.now,
        )
        self.assertEqual(result.reason, NoOutputReason.DISCLOSURE_AUTHORITY_UNASSIGNED)

    def test_revoked_expired_and_denied_disclosure_decisions_fail_closed(self) -> None:
        request = self.request()
        for decision, at in (
            (self.disclosure_decision(revoked=True), self.now),
            (self.disclosure_decision(), self.later),
            (self.disclosure_decision(effect=DisclosureEffect.DENY), self.now),
        ):
            result = self.boundary().evaluate(
                request, self.authorization(), self.recipients(), decision, at=at
            )
            self.assertEqual(result.reason, NoOutputReason.DISCLOSURE_DECISION_NOT_CURRENT)

    def test_even_fully_synthetic_policy_match_has_no_output_capability(self) -> None:
        request = self.request()
        result = self.boundary().evaluate(
            request,
            self.authorization(),
            self.recipients(),
            self.disclosure_decision(),
            at=self.now,
        )
        self.assertEqual(result.reason, NoOutputReason.POLICY_SATISFIED_NO_OUTPUT_CAPABILITY)
        self.assertFalse(result.output_emitted)
        self.assertFalse(result.serialized)
        self.assertFalse(result.spoken)
        self.assertFalse(result.exported)
        self.assertFalse(result.transmitted)
        self.assertFalse(result.api_released)
        self.assertFalse(result.agent_handoff)

    def test_protected_identity_reference_is_opaque_and_protected(self) -> None:
        reference = OpaqueProtectedIdentityReference(
            "identity-ref:synthetic",
            ProtectedIdentityHandlingClass.OPAQUE_PROTECTED_REFERENCE_ONLY,
            ClassificationTier.PROTECTED,
            "synthetic-policy-v1",
        )
        self.assertTrue(reference.reference.startswith("identity-ref:"))

    def test_protected_identity_cannot_be_public_or_internal(self) -> None:
        with self.assertRaises(DataLossPrivacyContractError):
            OpaqueProtectedIdentityReference(
                "identity-ref:synthetic",
                ProtectedIdentityHandlingClass.OPAQUE_PROTECTED_REFERENCE_ONLY,
                ClassificationTier.INTERNAL,
                "synthetic-policy-v1",
            )

    def test_no_reveal_boundary_requires_current_authorization(self) -> None:
        reference = OpaqueProtectedIdentityReference(
            "identity-ref:synthetic",
            ProtectedIdentityHandlingClass.MASKED_OR_TOKENIZED,
            ClassificationTier.PROTECTED,
            "synthetic-policy-v1",
        )
        result = NoRevealProtectedIdentityBoundary().evaluate(
            reference,
            None,
            request_reference="synthetic-disclosure-request",
            purpose_reference="purpose:synthetic",
            audit_boundary_available=True,
        )
        self.assertEqual(result.reason_code, "CURRENT_AUTHORIZATION_REQUIRED")

    def test_unavailable_audit_boundary_denies_reveal(self) -> None:
        reference = OpaqueProtectedIdentityReference(
            "identity-ref:synthetic",
            ProtectedIdentityHandlingClass.PROTECTED_REVEAL,
            ClassificationTier.SENSITIVE,
            "synthetic-policy-v1",
        )
        result = NoRevealProtectedIdentityBoundary().evaluate(
            reference,
            self.authorization(),
            request_reference="synthetic-disclosure-request",
            purpose_reference="purpose:synthetic",
            audit_boundary_available=False,
        )
        self.assertEqual(result.reason_code, "REQUIRED_AUDIT_BOUNDARY_UNAVAILABLE")
        self.assertFalse(result.revealed)

    def test_empty_access_registry_denies_reveal(self) -> None:
        reference = OpaqueProtectedIdentityReference(
            "identity-ref:synthetic",
            ProtectedIdentityHandlingClass.MASKED_OR_TOKENIZED,
            ClassificationTier.PROTECTED,
            "synthetic-policy-v1",
        )
        result = NoRevealProtectedIdentityBoundary().evaluate(
            reference,
            self.authorization(),
            request_reference="synthetic-disclosure-request",
            purpose_reference="purpose:synthetic",
            audit_boundary_available=True,
        )
        self.assertEqual(result.reason_code, "NO_PROTECTED_IDENTITY_ACCESS_RULE")

    def test_synthetic_access_rule_still_cannot_reveal(self) -> None:
        reference = OpaqueProtectedIdentityReference(
            "identity-ref:synthetic",
            ProtectedIdentityHandlingClass.MASKED_OR_TOKENIZED,
            ClassificationTier.PROTECTED,
            "synthetic-policy-v1",
        )
        registry = ProtectedIdentityAccessRegistry(
            "synthetic-registry-v1",
            (
                ProtectedIdentityAccessRule(
                    "access-rule:synthetic",
                    ProtectedIdentityHandlingClass.MASKED_OR_TOKENIZED,
                    "purpose:synthetic",
                    "synthetic-policy-v1",
                ),
            ),
        )
        result = NoRevealProtectedIdentityBoundary(registry).evaluate(
            reference,
            self.authorization(),
            request_reference="synthetic-disclosure-request",
            purpose_reference="purpose:synthetic",
            audit_boundary_available=True,
        )
        self.assertEqual(result.reason_code, "PROTECTED_IDENTITY_REVEAL_CAPABILITY_ABSENT")
        self.assertFalse(result.retrieved)
        self.assertFalse(result.unmasked)

    def test_privacy_escalation_only_requires_human_decision(self) -> None:
        request = PrivacyEscalationRequest(
            "escalation:synthetic",
            "correlation:synthetic",
            (PrivacyEscalationReason.PROTECTED_REVEAL,),
            "synthetic-policy-v1",
        )
        result = PrivacyEscalationBoundary().escalate(request)
        self.assertEqual(result.disposition, PrivacyEscalationDisposition.HUMAN_DECISION_REQUIRED)
        self.assertFalse(result.decision_created)
        self.assertFalse(result.authority_assigned)

    def test_all_non_waivable_protections_are_present(self) -> None:
        self.assertEqual(ALL_NON_WAIVABLE_PROTECTIONS, frozenset(NonWaivableProtection))
        self.assertEqual(len(ALL_NON_WAIVABLE_PROTECTIONS), 10)

    def test_exception_requires_all_non_waivable_protections(self) -> None:
        with self.assertRaises(DataLossPrivacyContractError):
            replace(
                self.exception(),
                protections=frozenset(
                    ALL_NON_WAIVABLE_PROTECTIONS
                    - {NonWaivableProtection.NO_REAL_IDENTITY_OR_GOVERNED_DATA}
                ),
            )

    def test_exception_cannot_be_self_approved_or_create_capability(self) -> None:
        with self.assertRaises(DataLossPrivacyContractError):
            replace(self.exception(), approver_reference="requester:synthetic")
        with self.assertRaises(DataLossPrivacyContractError):
            replace(self.exception(), creates_capability=True)
        with self.assertRaises(DataLossPrivacyContractError):
            replace(self.exception(), repeals_policy=True)

    def test_exception_expiry_and_revocation_are_fail_closed(self) -> None:
        exception = self.exception()
        self.assertTrue(exception.is_current(self.now))
        self.assertFalse(exception.is_current(self.later))
        self.assertFalse(replace(exception, revoked=True).is_current(self.now))

    def test_controlled_exception_registry_is_empty(self) -> None:
        self.assertTrue(DisclosureExceptionRegistry("synthetic-empty-v1").is_empty())

    def test_every_untrusted_origin_cannot_create_disclosure_authority(self) -> None:
        for origin in UntrustedContentOrigin:
            result = evaluate_untrusted_disclosure_claim(
                UntrustedDisclosureClaim(
                    f"claim:{origin.value.lower()}",
                    origin,
                    claims_public=True,
                    claims_authorized=True,
                    claims_consented=True,
                    claims_exception=True,
                )
            )
            self.assertEqual(result.reason, NoOutputReason.UNTRUSTED_AUTHORITY_CLAIM)
            self.assertEqual(result.disclosure_effect, DisclosureEffect.DENY)
            self.assertFalse(result.output_emitted)

    def test_signal_is_minimized_and_non_authoritative(self) -> None:
        signal = DataLossPrivacySignal(
            "correlation:synthetic",
            "boundary:synthetic",
            "DENY_NO_CAPABILITY",
            "synthetic-policy-v1",
        )
        self.assertFalse(signal.authoritative)
        with self.assertRaises(DataLossPrivacyContractError):
            replace(signal, authoritative=True)

    def test_protected_material_reference_is_rejected_without_echo(self) -> None:
        candidate = "identity_value=do-not-echo"
        with self.assertRaises(DataLossPrivacyContractError) as caught:
            FieldClassification(candidate, ClassificationTier.PROTECTED, "provenance:synthetic")
        self.assertNotIn("do-not-echo", str(caught.exception))

    def test_privacy_authority_registry_can_only_hold_metadata(self) -> None:
        registry = PrivacyAuthorityRegistry("synthetic-empty-v1")
        self.assertTrue(registry.is_empty())


if __name__ == "__main__":
    unittest.main()
