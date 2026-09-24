"""Deterministic metadata-only tests for WBS-16-WP-008."""

import unittest
from dataclasses import FrozenInstanceError, fields, replace
from datetime import UTC, datetime, timedelta

from ncie_foundation.agent_model_tool_context_security import UntrustedContentOrigin
from ncie_foundation.security_authorization import (
    ALL_AUTHORIZATION_DIMENSIONS,
    AuthorizationEffect,
    CurrentAuthorizationDecision,
)
from ncie_foundation.security_logging_incident import (
    ALL_SECURITY_INCIDENT_PROTECTIONS,
    EMPTY_ASSURANCE_ASSIGNMENT_REGISTRY,
    EMPTY_CONTAINMENT_RIGHTS_REGISTRY,
    EMPTY_DETECTION_RULE_REGISTRY,
    EMPTY_EMERGENCY_ELIGIBILITY_REGISTRY,
    EMPTY_ESCALATION_ROUTE_REGISTRY,
    EMPTY_INCIDENT_COMMAND_REGISTRY,
    EMPTY_NOTIFICATION_DESTINATION_REGISTRY,
    EMPTY_RESTORATION_AUTHORITY_REGISTRY,
    EMPTY_RETENTION_LEGAL_HOLD_REGISTRY,
    EMPTY_SECURITY_LOG_ACCESS_REGISTRY,
    EMPTY_SEVERITY_GOVERNANCE_REGISTRY,
    INCIDENT_LIFECYCLE_ORDER,
    SECURITY_INCIDENT_DECISION_EVIDENCE,
    SECURITY_INCIDENT_IMPLEMENTATION_AUTHORITY,
    UNSPECIFIED_SEVERITY,
    ContainmentEffectivenessConfirmation,
    ContainmentRequest,
    ControlDisposition,
    DenyAllRetentionBoundary,
    DenyAllSecurityLogAccessBoundary,
    DetectionCategory,
    DetectionRequest,
    DetectionResult,
    EvidenceReference,
    ExecutionAuthorityReference,
    FailClosedTriageBoundary,
    FindingReference,
    HumanDecisionReference,
    IncidentCandidate,
    IncidentLifecycleStage,
    NoContainmentRecoveryBoundary,
    NoIncidentCommandBoundary,
    NoMonitorBoundary,
    NoNotificationBoundary,
    NotificationObligation,
    RecoveryHandoff,
    RestorationReinstatementReview,
    RetentionEvaluationRequest,
    SecurityEvent,
    SecurityEventOutcome,
    SecurityIncidentContractError,
    SecurityLogAccessRequest,
    SecuritySignal,
    SeverityReference,
    SyntheticSecurityEventCollector,
    TriageDisposition,
    UnassignedWp008Authorities,
    UntrustedSecurityControlClaim,
    Wp008AuthorityClass,
    evaluate_untrusted_security_claim,
)


class Wbs16Wp008SecurityLoggingIncidentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 24, 15, tzinfo=UTC)
        self.later = self.now + timedelta(hours=1)

    def authorization(
        self,
        request_reference: str,
        *,
        effect: AuthorizationEffect = AuthorizationEffect.PERMIT,
        policy_version: str = "synthetic-policy-v1",
    ) -> CurrentAuthorizationDecision:
        return CurrentAuthorizationDecision(
            request_reference=request_reference,
            policy_version=policy_version,
            effect=effect,
            reason_code="SYNTHETIC_TEST_DECISION",
            evaluated_dimensions=ALL_AUTHORIZATION_DIMENSIONS,
        )

    def event(self) -> SecurityEvent:
        return SecurityEvent(
            event_reference="event:synthetic",
            correlation_reference="correlation:synthetic",
            source_reference="source:synthetic-test",
            occurred_at=self.now,
            observed_at=self.now,
            actor_class_reference="actor-class:synthetic",
            actor_reference="actor:opaque-synthetic",
            target_class_reference="target-class:synthetic",
            target_reference="target:opaque-synthetic",
            action_class_reference="action-class:synthetic",
            outcome=SecurityEventOutcome.INDETERMINATE,
            classification_reference="classification:synthetic",
            residency_reference="residency:africa-synthetic",
            access_policy_reference="access-policy:synthetic",
            retention_policy_reference="retention-policy:synthetic",
            policy_version="synthetic-policy-v1",
            provenance_references=("provenance-reference:synthetic",),
            source_signal_references=("signal:synthetic",),
        )

    def detection_request(
        self,
        *,
        origin: UntrustedContentOrigin = UntrustedContentOrigin.MODEL_OUTPUT,
    ) -> DetectionRequest:
        return DetectionRequest(
            request_reference="detection-request:synthetic",
            detection_reference="detection:synthetic",
            event=self.event(),
            category=DetectionCategory.PROMPT_INJECTION_INDICATOR,
            rule_reference="rule:synthetic-unassigned",
            quality_state_reference="quality:synthetic-unknown",
            behavior_references=("behavior:tool-synthetic", "behavior:data-synthetic"),
            content_origin=origin,
            policy_version="synthetic-policy-v1",
        )

    def detection_result(self, *, current: bool = False) -> DetectionResult:
        return DetectionResult(
            detection_reference="detection:synthetic",
            correlation_reference="correlation:synthetic",
            category=DetectionCategory.PROMPT_INJECTION_INDICATOR,
            source_event_references=("event:synthetic",),
            rule_reference="rule:synthetic",
            policy_version="synthetic-policy-v1",
            provenance_references=("provenance-reference:synthetic",),
            evaluated_at=self.now,
            quality_state_reference="quality:synthetic",
            severity=UNSPECIFIED_SEVERITY,
            triage_disposition=TriageDisposition.INDETERMINATE_DENY,
            rule_current=current,
        )

    def candidate(self) -> IncidentCandidate:
        return IncidentCandidate(
            candidate_reference="incident-candidate:synthetic",
            correlation_reference="correlation:synthetic",
            detection_references=("detection:synthetic",),
            requested_stage=IncidentLifecycleStage.TRIAGE,
            policy_version="synthetic-policy-v1",
            provenance_references=("provenance-reference:synthetic",),
        )

    def containment_request(self, *, emergency: bool = False) -> ContainmentRequest:
        return ContainmentRequest(
            request_reference="containment-request:synthetic",
            incident_candidate_reference="incident-candidate:synthetic",
            requester_reference="requester:synthetic",
            target_reference="target:synthetic",
            target_class_reference="target-class:synthetic",
            action_reference="action:synthetic-containment",
            trigger_reference="trigger:synthetic",
            purpose_reference="purpose:synthetic",
            requested_at=self.now,
            expires_at=self.later,
            policy_version="synthetic-policy-v1",
            emergency=emergency,
        )

    def restoration_review(self) -> RestorationReinstatementReview:
        return RestorationReinstatementReview(
            review_reference="restoration-review:synthetic",
            incident_candidate_reference="incident-candidate:synthetic",
            containment_request_reference="containment-request:synthetic",
            containment_effectiveness_reference="effectiveness:synthetic-unconfirmed",
            preservation_request_reference="preservation-request:wbs20-synthetic",
            reviewer_reference="reviewer:synthetic-independent",
            requester_reference="requester:synthetic",
            approver_reference="approver:synthetic",
            executor_reference="executor:synthetic",
            reviewed_at=self.now,
            policy_version="synthetic-policy-v1",
            independent=True,
        )

    def test_decision_provenance_and_eleven_controlled_registries_are_empty(self) -> None:
        self.assertEqual(
            SECURITY_INCIDENT_DECISION_EVIDENCE,
            "NCIE-WBS16-OWNER-DECISION-2026-09-24-029",
        )
        self.assertEqual(
            SECURITY_INCIDENT_IMPLEMENTATION_AUTHORITY,
            "NCIE-WBS16-OWNER-DECISION-2026-09-24-030",
        )
        registries = (
            EMPTY_SECURITY_LOG_ACCESS_REGISTRY,
            EMPTY_RETENTION_LEGAL_HOLD_REGISTRY,
            EMPTY_ASSURANCE_ASSIGNMENT_REGISTRY,
            EMPTY_DETECTION_RULE_REGISTRY,
            EMPTY_ESCALATION_ROUTE_REGISTRY,
            EMPTY_SEVERITY_GOVERNANCE_REGISTRY,
            EMPTY_INCIDENT_COMMAND_REGISTRY,
            EMPTY_NOTIFICATION_DESTINATION_REGISTRY,
            EMPTY_CONTAINMENT_RIGHTS_REGISTRY,
            EMPTY_EMERGENCY_ELIGIBILITY_REGISTRY,
            EMPTY_RESTORATION_AUTHORITY_REGISTRY,
        )
        self.assertEqual(len(registries), 11)
        self.assertTrue(all(registry.is_empty() for registry in registries))
        self.assertEqual(len(ALL_SECURITY_INCIDENT_PROTECTIONS), 14)

    def test_exact_five_detection_categories(self) -> None:
        self.assertEqual(len(DetectionCategory), 5)

    def test_detection_categories_match_source_taxonomy(self) -> None:
        self.assertEqual(
            {category.value for category in DetectionCategory},
            {
                "IDENTITY_ACCESS_ANOMALY",
                "EXFILTRATION_INDICATOR",
                "AGENT_ABUSE",
                "PROMPT_INJECTION_INDICATOR",
                "NETWORK_ANOMALY",
            },
        )

    def test_tool_and_data_behavior_do_not_create_sixth_category(self) -> None:
        request = self.detection_request()
        self.assertEqual(len(request.behavior_references), 2)
        self.assertEqual(len(DetectionCategory), 5)

    def test_incident_lifecycle_order_is_explicit(self) -> None:
        self.assertEqual(INCIDENT_LIFECYCLE_ORDER, tuple(IncidentLifecycleStage))
        self.assertEqual(len(INCIDENT_LIFECYCLE_ORDER), 9)

    def test_all_wp008_authorities_are_unassigned(self) -> None:
        boundary = UnassignedWp008Authorities()
        for authority_class in Wp008AuthorityClass:
            self.assertIsNone(boundary.assignment_for(authority_class))

    def test_signal_is_minimized_non_authoritative_and_immutable(self) -> None:
        signal = SecuritySignal(
            "signal:synthetic",
            "correlation:synthetic",
            "source-class:synthetic",
            "condition:synthetic",
            self.now,
            "synthetic-policy-v1",
        )
        self.assertFalse(signal.authoritative)
        self.assertFalse(hasattr(signal, "payload"))
        with self.assertRaises(FrozenInstanceError):
            signal.authoritative = True  # type: ignore[misc]

    def test_security_event_contains_metadata_not_payload_fields(self) -> None:
        names = {field.name for field in fields(SecurityEvent)}
        for prohibited in (
            "secret",
            "credential",
            "token",
            "key",
            "prompt",
            "chain_of_thought",
            "identity_value",
            "payload",
            "document",
            "memory",
            "evidence",
            "tool_result",
        ):
            self.assertNotIn(prohibited, names)

    def test_security_event_must_be_synthetic(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.event(), synthetic=False)

    def test_security_event_cannot_be_authoritative(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.event(), authoritative=True)

    def test_security_event_rejects_observation_before_occurrence(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.event(), observed_at=self.now - timedelta(seconds=1))

    def test_protected_reference_fragment_is_rejected_without_echo(self) -> None:
        protected = "secret_value:do-not-echo"
        with self.assertRaises(SecurityIncidentContractError) as raised:
            replace(self.event(), actor_reference=protected)
        self.assertNotIn(protected, str(raised.exception))

    def test_signal_event_detection_and_incident_are_distinct_types(self) -> None:
        signal = SecuritySignal(
            "signal:synthetic",
            "correlation:synthetic",
            "source-class:synthetic",
            "condition:synthetic",
            self.now,
            "synthetic-policy-v1",
        )
        detection = self.detection_result()
        candidate = self.candidate()
        self.assertIsNot(type(signal), type(self.event()))
        self.assertIsNot(type(self.event()), type(detection))
        self.assertIsNot(type(detection), type(candidate))

    def test_evidence_finding_decision_and_authority_references_are_distinct(self) -> None:
        references = (
            EvidenceReference("evidence-reference:synthetic"),
            FindingReference("finding-reference:synthetic"),
            HumanDecisionReference("human-decision-reference:synthetic"),
            ExecutionAuthorityReference("execution-authority-reference:synthetic"),
        )
        self.assertEqual(len({type(item) for item in references}), 4)

    def test_evidence_reference_has_no_payload_or_custody(self) -> None:
        reference = EvidenceReference("evidence-reference:synthetic")
        self.assertFalse(hasattr(reference, "payload"))
        self.assertFalse(hasattr(reference, "custody"))

    def test_unspecified_severity_has_no_operational_taxonomy(self) -> None:
        self.assertTrue(UNSPECIFIED_SEVERITY.is_unspecified)
        self.assertIsNone(UNSPECIFIED_SEVERITY.assigning_authority_reference)
        self.assertFalse(hasattr(UNSPECIFIED_SEVERITY, "score"))
        self.assertFalse(hasattr(UNSPECIFIED_SEVERITY, "threshold"))

    def test_partial_severity_window_is_rejected(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            SeverityReference(
                "severity:synthetic",
                "synthetic-policy-v1",
                effective_at=self.now,
            )

    def test_current_four_layer_authorization_does_not_grant_log_access(self) -> None:
        request = SecurityLogAccessRequest(
            request_reference="log-access-request:synthetic",
            event_reference="event:synthetic",
            actor_reference="actor:synthetic",
            object_reference="security-log:synthetic",
            field_references=("field:event-reference",),
            action_reference="action:read",
            purpose_reference="purpose:synthetic",
            classification_reference="classification:synthetic",
            access_policy_reference="access-policy:synthetic",
            policy_version="synthetic-policy-v1",
        )
        result = DenyAllSecurityLogAccessBoundary().evaluate(
            request,
            self.authorization(request.request_reference),
        )
        self.assertEqual(result.disposition, ControlDisposition.DENY)
        self.assertEqual(result.reason_code, "LOG_ACCESS_AUTHORITY_UNASSIGNED")

    def test_missing_current_authorization_denies_log_access_first(self) -> None:
        request = SecurityLogAccessRequest(
            "log-access-request:synthetic",
            "event:synthetic",
            "actor:synthetic",
            "security-log:synthetic",
            ("field:event-reference",),
            "action:read",
            "purpose:synthetic",
            "classification:synthetic",
            "access-policy:synthetic",
            "synthetic-policy-v1",
        )
        result = DenyAllSecurityLogAccessBoundary().evaluate(request, None)
        self.assertEqual(result.reason_code, "CURRENT_AUTHORIZATION_REQUIRED")

    def test_mismatched_authorization_denies_log_access(self) -> None:
        request = SecurityLogAccessRequest(
            "log-access-request:synthetic",
            "event:synthetic",
            "actor:synthetic",
            "security-log:synthetic",
            ("field:event-reference",),
            "action:read",
            "purpose:synthetic",
            "classification:synthetic",
            "access-policy:synthetic",
            "synthetic-policy-v1",
        )
        result = DenyAllSecurityLogAccessBoundary().evaluate(
            request,
            self.authorization("different-request"),
        )
        self.assertEqual(result.reason_code, "CURRENT_AUTHORIZATION_REQUIRED")

    def test_retention_and_legal_hold_have_no_operation(self) -> None:
        request = RetentionEvaluationRequest(
            "retention-request:synthetic",
            "event:synthetic",
            "classification:synthetic",
            "retention-policy:synthetic-unassigned",
            None,
            "synthetic-policy-v1",
        )
        result = DenyAllRetentionBoundary().evaluate(request)
        self.assertEqual(result.disposition, ControlDisposition.DENY)
        self.assertEqual(result.reason_code, "RETENTION_POLICY_UNASSIGNED")

    def test_retention_request_has_no_period_or_duration(self) -> None:
        names = {field.name for field in fields(RetentionEvaluationRequest)}
        self.assertNotIn("retention_days", names)
        self.assertNotIn("duration", names)
        self.assertNotIn("delete_at", names)

    def test_no_monitor_boundary_returns_indeterminate_deny(self) -> None:
        result = NoMonitorBoundary().evaluate(self.detection_request(), at=self.now)
        self.assertEqual(result.triage_disposition, TriageDisposition.INDETERMINATE_DENY)
        self.assertFalse(result.rule_current)
        self.assertTrue(result.severity.is_unspecified)

    def test_no_monitor_boundary_has_no_poll_stream_or_connect_method(self) -> None:
        boundary = NoMonitorBoundary()
        for method in ("poll", "stream", "connect", "subscribe", "monitor"):
            self.assertFalse(hasattr(boundary, method))

    def test_detection_is_non_authoritative(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.detection_result(), authoritative=True)

    def test_stale_rule_fails_triage_closed(self) -> None:
        result = FailClosedTriageBoundary().evaluate(self.detection_result(current=False))
        self.assertEqual(result.disposition, TriageDisposition.INDETERMINATE_DENY)
        self.assertEqual(result.reason_code, "DETECTION_RULE_NOT_CURRENT")

    def test_current_synthetic_rule_still_requires_human_severity_governance(self) -> None:
        result = FailClosedTriageBoundary().evaluate(self.detection_result(current=True))
        self.assertEqual(result.disposition, TriageDisposition.HUMAN_DECISION_REQUIRED)
        self.assertEqual(result.reason_code, "SEVERITY_GOVERNANCE_UNASSIGNED")

    def test_severity_never_creates_authority(self) -> None:
        severity = SeverityReference(
            "severity:synthetic-symbolic",
            "synthetic-policy-v1",
            "authority-reference:synthetic",
            self.now,
            self.later,
        )
        self.assertFalse(hasattr(severity, "authorize"))
        self.assertFalse(hasattr(severity, "execute"))

    def test_incident_candidate_cannot_be_declared(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.candidate(), declared=True)

    def test_no_incident_command_returns_human_decision_required(self) -> None:
        result = NoIncidentCommandBoundary().evaluate(self.candidate())
        self.assertEqual(result.disposition, ControlDisposition.HUMAN_DECISION_REQUIRED)
        self.assertEqual(result.reason_code, "INCIDENT_DECLARATION_AUTHORITY_UNASSIGNED")

    def test_no_incident_command_has_no_declare_or_command_method(self) -> None:
        boundary = NoIncidentCommandBoundary()
        self.assertFalse(hasattr(boundary, "declare"))
        self.assertFalse(hasattr(boundary, "command"))

    def test_notification_obligation_has_no_recipient_or_destination(self) -> None:
        obligation = NotificationObligation(
            "notification-obligation:synthetic",
            "incident-candidate:synthetic",
            IncidentLifecycleStage.NOTIFICATION_OBLIGATION,
            "synthetic-policy-v1",
            "classification:synthetic",
        )
        self.assertIsNone(obligation.recipient_role_class_reference)
        self.assertIsNone(obligation.destination_class_reference)
        self.assertIsNone(obligation.channel_class_reference)

    def test_notification_boundary_denies_and_has_no_send_or_page(self) -> None:
        obligation = NotificationObligation(
            "notification-obligation:synthetic",
            "incident-candidate:synthetic",
            IncidentLifecycleStage.NOTIFICATION_OBLIGATION,
            "synthetic-policy-v1",
            "classification:synthetic",
        )
        boundary = NoNotificationBoundary()
        result = boundary.evaluate(obligation)
        self.assertEqual(result.disposition, ControlDisposition.DENY)
        self.assertFalse(hasattr(boundary, "send"))
        self.assertFalse(hasattr(boundary, "page"))
        self.assertFalse(hasattr(boundary, "alert"))

    def test_notification_cannot_be_marked_fulfilled(self) -> None:
        obligation = NotificationObligation(
            "notification-obligation:synthetic",
            "incident-candidate:synthetic",
            IncidentLifecycleStage.NOTIFICATION_OBLIGATION,
            "synthetic-policy-v1",
            "classification:synthetic",
        )
        with self.assertRaises(SecurityIncidentContractError):
            replace(obligation, fulfilled=True)

    def test_containment_request_cannot_be_authorized_or_executed(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.containment_request(), authorized=True)
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.containment_request(), executed=True)

    def test_containment_requires_current_authorization(self) -> None:
        result = NoContainmentRecoveryBoundary().evaluate_containment(
            self.containment_request(), None
        )
        self.assertEqual(result.reason_code, "CURRENT_AUTHORIZATION_REQUIRED")

    def test_empty_containment_rights_deny(self) -> None:
        request = self.containment_request()
        result = NoContainmentRecoveryBoundary().evaluate_containment(
            request,
            self.authorization(request.request_reference),
        )
        self.assertEqual(result.reason_code, "CONTAINMENT_RIGHT_UNASSIGNED")

    def test_empty_emergency_eligibility_denies_before_containment(self) -> None:
        request = self.containment_request(emergency=True)
        result = NoContainmentRecoveryBoundary().evaluate_containment(
            request,
            self.authorization(request.request_reference),
        )
        self.assertEqual(result.reason_code, "EMERGENCY_ELIGIBILITY_UNASSIGNED")

    def test_no_containment_recovery_boundary_has_no_execution_methods(self) -> None:
        boundary = NoContainmentRecoveryBoundary()
        for method in (
            "execute",
            "contain",
            "suspend",
            "revoke",
            "isolate",
            "recover",
            "restore",
            "reinstate",
        ):
            self.assertFalse(hasattr(boundary, method))

    def test_effectiveness_cannot_be_operationally_confirmed(self) -> None:
        confirmation = ContainmentEffectivenessConfirmation(
            "effectiveness:synthetic",
            "containment-request:synthetic",
            None,
            self.now,
        )
        with self.assertRaises(SecurityIncidentContractError):
            replace(confirmation, effective=True)

    def test_recovery_handoff_cannot_authorize_or_reauthorize(self) -> None:
        handoff = RecoveryHandoff(
            "recovery-handoff:synthetic",
            "incident-candidate:synthetic",
            "effectiveness:synthetic-unconfirmed",
            "preservation-request:wbs20-synthetic",
            "synthetic-policy-v1",
        )
        with self.assertRaises(SecurityIncidentContractError):
            replace(handoff, recovery_authorized=True)
        with self.assertRaises(SecurityIncidentContractError):
            replace(handoff, reauthorization_created=True)

    def test_restoration_review_requires_independent_reviewer(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            replace(
                self.restoration_review(),
                reviewer_reference="requester:synthetic",
            )

    def test_restoration_and_reinstatement_cannot_be_authorized(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.restoration_review(), restoration_authorized=True)
        with self.assertRaises(SecurityIncidentContractError):
            replace(self.restoration_review(), reinstatement_authorized=True)

    def test_restoration_requires_new_current_authorization(self) -> None:
        result = NoContainmentRecoveryBoundary().evaluate_restoration(
            self.restoration_review(), None
        )
        self.assertEqual(result.reason_code, "NEW_AUTHORIZATION_REQUIRED")

    def test_empty_restoration_authority_requires_human_decision(self) -> None:
        review = self.restoration_review()
        result = NoContainmentRecoveryBoundary().evaluate_restoration(
            review,
            self.authorization(review.review_reference),
        )
        self.assertEqual(result.disposition, ControlDisposition.HUMAN_DECISION_REQUIRED)
        self.assertEqual(
            result.reason_code,
            "RESTORATION_REINSTATEMENT_AUTHORITY_UNASSIGNED",
        )

    def test_collector_is_in_memory_synthetic_and_non_persistent(self) -> None:
        collector = SyntheticSecurityEventCollector()
        collector.collect(self.event())
        self.assertEqual(collector.snapshot(), (self.event(),))
        self.assertFalse(collector.persistent)
        self.assertFalse(collector.authoritative)
        self.assertFalse(collector.evidence_store)
        self.assertFalse(collector.audit_store)
        self.assertFalse(collector.provenance_store)

    def test_collector_has_no_persist_export_or_evidence_methods(self) -> None:
        collector = SyntheticSecurityEventCollector()
        for method in ("persist", "save", "export", "write", "create_evidence", "audit"):
            self.assertFalse(hasattr(collector, method))

    def test_collector_snapshot_is_immutable_and_clear_is_process_local(self) -> None:
        collector = SyntheticSecurityEventCollector()
        collector.collect(self.event())
        snapshot = collector.snapshot()
        self.assertIsInstance(snapshot, tuple)
        collector.clear()
        self.assertEqual(collector.snapshot(), ())
        self.assertEqual(len(snapshot), 1)

    def test_every_untrusted_origin_cannot_create_control_authority(self) -> None:
        for origin in UntrustedContentOrigin:
            claim = UntrustedSecurityControlClaim(
                claim_reference=f"claim:{origin.value.lower()}",
                origin=origin,
                asserted_severity_reference="severity:asserted",
                asserted_incident_reference="incident:asserted",
                asserted_authority_reference="authority:asserted",
                asserted_destination_reference="destination:asserted",
            )
            result = evaluate_untrusted_security_claim(claim)
            self.assertEqual(result.disposition, ControlDisposition.DENY)
            self.assertFalse(result.capability_available)

    def test_prompt_injection_output_cannot_change_detection_outcome(self) -> None:
        request = self.detection_request(origin=UntrustedContentOrigin.MODEL_OUTPUT)
        result = NoMonitorBoundary().evaluate(request, at=self.now)
        self.assertEqual(result.triage_disposition, TriageDisposition.INDETERMINATE_DENY)
        self.assertTrue(result.severity.is_unspecified)

    def test_control_result_cannot_expose_capability(self) -> None:
        with self.assertRaises(SecurityIncidentContractError):
            from ncie_foundation.security_logging_incident import ControlResult

            ControlResult(ControlDisposition.DENY, "SYNTHETIC_REASON", True)

    def test_no_boundary_exposes_network_or_external_destination(self) -> None:
        boundaries = (
            DenyAllSecurityLogAccessBoundary(),
            DenyAllRetentionBoundary(),
            NoMonitorBoundary(),
            FailClosedTriageBoundary(),
            NoIncidentCommandBoundary(),
            NoNotificationBoundary(),
            NoContainmentRecoveryBoundary(),
        )
        for boundary in boundaries:
            for method in ("connect", "request", "post", "publish", "subscribe", "transfer"):
                self.assertFalse(hasattr(boundary, method))


if __name__ == "__main__":
    unittest.main()
