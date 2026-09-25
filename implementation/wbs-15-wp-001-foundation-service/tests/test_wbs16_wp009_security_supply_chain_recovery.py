"""Deterministic metadata-only tests for WBS-16-WP-009."""

import unittest
from dataclasses import FrozenInstanceError, fields, replace
from datetime import UTC, datetime, timedelta

from ncie_foundation.agent_model_tool_context_security import UntrustedContentOrigin
from ncie_foundation.security_authorization import (
    ALL_AUTHORIZATION_DIMENSIONS,
    AuthorizationEffect,
    CurrentAuthorizationDecision,
)
from ncie_foundation.security_supply_chain_recovery import (
    ALL_SUPPLY_CHAIN_RECOVERY_PROTECTIONS,
    ALL_WP009_CONTROLLED_REGISTRIES,
    SUPPLY_CHAIN_RECOVERY_DECISION_EVIDENCE,
    SUPPLY_CHAIN_RECOVERY_IMPLEMENTATION_AUTHORITY,
    UNSPECIFIED_VULNERABILITY_SEVERITY,
    ArtifactAcceptanceRecord,
    ArtifactDeploymentReference,
    ArtifactEligibilityEvaluator,
    ArtifactIntegrityState,
    ArtifactPromotionReference,
    ArtifactProvenanceMetadata,
    ArtifactQuarantineRecord,
    ArtifactRevocationRecord,
    ArtifactTransitionReferences,
    ArtifactVerificationRecord,
    ControlledRegistry,
    GeneratedCodeSecurityGateRecord,
    IndependentRecoveryReview,
    InvalidationObligation,
    MitigationRecord,
    NoArtifactActionBoundary,
    NoRecoveryBoundary,
    NoRemediationBoundary,
    OperationalRestorationReference,
    ReauthorizationReference,
    RecoveryAuthorityReferences,
    RecoveryIntegrityState,
    RecoveryReconciliationRecord,
    RecoveryResultReference,
    RecoverySecurityEvaluator,
    RecoverySourceMetadata,
    ReinstatementReference,
    RemediationRecord,
    ResidualRiskAcceptanceRecord,
    SecurityAcceptanceRecord,
    SecurityExceptionRecord,
    SecurityRecoveryAcceptanceRecord,
    SupplyChainControlResult,
    SupplyChainDisposition,
    SupplyChainRecoveryContractError,
    SymbolicVulnerabilitySeverity,
    UnassignedWp009Authorities,
    UntrustedSupplyChainClaim,
    VulnerabilityLifecycleState,
    VulnerabilityRecord,
    VulnerabilityTreatmentEvaluator,
    Wp009AuthorityClass,
    evaluate_untrusted_supply_chain_claim,
)


class Wbs16Wp009SecuritySupplyChainRecoveryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.now = datetime(2026, 9, 24, 16, tzinfo=UTC)
        self.later = self.now + timedelta(hours=1)
        self.tomorrow = self.now + timedelta(days=1)

    def populated_registry(self, name: str) -> ControlledRegistry:
        return ControlledRegistry(name, "synthetic-policy-v1", ("entry:synthetic",))

    def authorization(self, request_reference: str) -> CurrentAuthorizationDecision:
        return CurrentAuthorizationDecision(
            request_reference=request_reference,
            policy_version="synthetic-policy-v1",
            effect=AuthorizationEffect.PERMIT,
            reason_code="SYNTHETIC_TEST_DECISION",
            evaluated_dimensions=ALL_AUTHORIZATION_DIMENSIONS,
        )

    def artifact(
        self,
        *,
        integrity_state: ArtifactIntegrityState = ArtifactIntegrityState.VERIFIED_METADATA_ONLY,
        generated_code: bool = False,
    ) -> ArtifactProvenanceMetadata:
        return ArtifactProvenanceMetadata(
            artifact_reference="artifact:synthetic",
            artifact_class_reference="artifact-class:synthetic",
            exact_version_reference="version:synthetic-v1",
            source_reference="source:synthetic",
            producer_class_reference="producer-class:synthetic",
            producing_process_reference="process:synthetic",
            integrity_reference="integrity:synthetic",
            dependency_manifest_reference="dependencies:synthetic",
            build_reference="build:synthetic",
            builder_class_reference="builder-class:synthetic",
            build_input_references=("build-input:synthetic",),
            provenance_policy_version="synthetic-policy-v1",
            residency_reference="residency:africa-synthetic",
            integrity_state=integrity_state,
            generated_code=generated_code,
        )

    def verification(
        self,
        *,
        version: str = "version:synthetic-v1",
        reviewer: str = "reviewer:synthetic-independent",
        verified: bool = True,
    ) -> ArtifactVerificationRecord:
        return ArtifactVerificationRecord(
            verification_reference="verification:synthetic",
            artifact_reference="artifact:synthetic",
            exact_version_reference=version,
            criteria_reference="criteria:synthetic",
            reviewer_reference=reviewer,
            producer_reference="producer:synthetic",
            implementer_reference="implementer:synthetic",
            verified_at=self.now,
            policy_version="synthetic-policy-v1",
            verified=verified,
            independent=True,
        )

    def acceptance(
        self,
        *,
        version: str = "version:synthetic-v1",
        effective_at: datetime | None = None,
        expires_at: datetime | None = None,
        revoked: bool = False,
    ) -> ArtifactAcceptanceRecord:
        return ArtifactAcceptanceRecord(
            acceptance_reference="acceptance:synthetic",
            artifact_reference="artifact:synthetic",
            exact_version_reference=version,
            scope_reference="scope:synthetic",
            authority_reference="authority:synthetic-unassigned",
            effective_at=effective_at or self.now,
            expires_at=expires_at or self.tomorrow,
            policy_version="synthetic-policy-v1",
            accepted=True,
            revoked=revoked,
        )

    def vulnerability(
        self,
        *,
        state: VulnerabilityLifecycleState = VulnerabilityLifecycleState.UNRESOLVED,
    ) -> VulnerabilityRecord:
        return VulnerabilityRecord(
            vulnerability_reference="vulnerability:synthetic",
            affected_artifact_reference="artifact:synthetic",
            affected_component_reference="component:synthetic",
            exact_version_reference="version:synthetic-v1",
            source_reference="source:synthetic",
            detected_at=self.now,
            known_at=self.now,
            provenance_references=("provenance:synthetic",),
            policy_version="synthetic-policy-v1",
            state=state,
        )

    def exception(self, **overrides: object) -> SecurityExceptionRecord:
        values: dict[str, object] = {
            "exception_reference": "exception:synthetic",
            "vulnerability_reference": "vulnerability:synthetic",
            "affected_component_reference": "component:synthetic",
            "exact_version_reference": "version:synthetic-v1",
            "scope_reference": "scope:synthetic",
            "requester_reference": "requester:synthetic",
            "reviewer_reference": "reviewer:synthetic-independent",
            "approver_reference": "approver:synthetic",
            "compensating_control_references": ("control:synthetic",),
            "effective_at": self.now,
            "expires_at": self.tomorrow,
            "policy_version": "synthetic-policy-v1",
        }
        values.update(overrides)
        return SecurityExceptionRecord(**values)  # type: ignore[arg-type]

    def recovery_source(
        self,
        *,
        state: RecoveryIntegrityState = RecoveryIntegrityState.UNKNOWN,
        quarantined: bool = True,
    ) -> RecoverySourceMetadata:
        return RecoverySourceMetadata(
            recovery_source_reference="recovery-source:synthetic",
            source_class_reference="source-class:synthetic-backup",
            exact_version_reference="version:synthetic-v1",
            integrity_reference="integrity:synthetic",
            creation_context_reference="creation-context:synthetic",
            classification_reference="classification:synthetic",
            residency_reference="residency:africa-synthetic",
            provenance_references=("provenance:synthetic",),
            policy_version="synthetic-policy-v1",
            integrity_state=state,
            quarantined=quarantined,
        )

    def reconciliation(
        self,
        *,
        current_state_available: bool = True,
        version: str = "version:synthetic-v1",
    ) -> RecoveryReconciliationRecord:
        return RecoveryReconciliationRecord(
            reconciliation_reference="reconciliation:synthetic",
            recovery_source_reference="recovery-source:synthetic",
            exact_version_reference=version,
            current_state_reference="current-state:synthetic",
            revocation_references=("revocation:current",),
            restriction_references=("restriction:current",),
            deletion_references=("deletion:current",),
            classification_references=("classification:current",),
            provenance_references=("provenance:current",),
            security_state_references=("security-state:current",),
            stale_grant_references=("grant:stale",),
            expired_permission_references=("permission:expired",),
            revoked_artifact_references=("artifact:revoked",),
            invalid_credential_session_references=("session:invalid",),
            ineligible_agent_model_tool_references=("agent:ineligible",),
            policy_version="synthetic-policy-v1",
            current_state_available=current_state_available,
        )

    def recovery_review(self) -> IndependentRecoveryReview:
        return IndependentRecoveryReview(
            review_reference="recovery-review:synthetic",
            recovery_source_reference="recovery-source:synthetic",
            reconciliation_reference="reconciliation:synthetic",
            reviewer_reference="reviewer:synthetic-independent",
            requester_reference="requester:synthetic",
            executor_reference="executor:synthetic",
            reviewed_at=self.now,
            policy_version="synthetic-policy-v1",
            independent=True,
        )

    def test_decision_provenance_and_thirty_registries_are_empty(self) -> None:
        self.assertEqual(
            SUPPLY_CHAIN_RECOVERY_DECISION_EVIDENCE,
            "NCIE-WBS16-OWNER-DECISION-2026-09-24-032",
        )
        self.assertEqual(
            SUPPLY_CHAIN_RECOVERY_IMPLEMENTATION_AUTHORITY,
            "NCIE-WBS16-OWNER-DECISION-2026-09-24-033",
        )
        self.assertEqual(len(ALL_WP009_CONTROLLED_REGISTRIES), 30)
        self.assertTrue(all(registry.is_empty() for registry in ALL_WP009_CONTROLLED_REGISTRIES))
        self.assertEqual(
            len({registry.registry_class for registry in ALL_WP009_CONTROLLED_REGISTRIES}),
            30,
        )

    def test_all_eighteen_non_waivable_protections_are_structural(self) -> None:
        self.assertEqual(len(ALL_SUPPLY_CHAIN_RECOVERY_PROTECTIONS), 18)

    def test_all_wp009_authorities_are_unassigned(self) -> None:
        authorities = UnassignedWp009Authorities()
        for authority_class in Wp009AuthorityClass:
            self.assertIsNone(authorities.assignment_for(authority_class))

    def test_registry_is_immutable_and_duplicate_entries_are_rejected(self) -> None:
        registry = ALL_WP009_CONTROLLED_REGISTRIES[0]
        with self.assertRaises(FrozenInstanceError):
            registry.version = "changed"  # type: ignore[misc]
        with self.assertRaises(SupplyChainRecoveryContractError):
            ControlledRegistry("registry:synthetic", "version:synthetic", ("x:1", "x:1"))

    def test_artifact_metadata_is_minimized_synthetic_and_immutable(self) -> None:
        artifact = self.artifact()
        names = {field.name for field in fields(ArtifactProvenanceMetadata)}
        for prohibited in (
            "payload",
            "source_code",
            "credential",
            "token",
            "private_key",
            "repository_endpoint",
        ):
            self.assertNotIn(prohibited, names)
        self.assertTrue(artifact.synthetic)
        self.assertFalse(artifact.authoritative)
        with self.assertRaises(FrozenInstanceError):
            artifact.authoritative = True  # type: ignore[misc]

    def test_artifact_payload_fragment_is_rejected_without_echo(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError) as raised:
            replace(self.artifact(), source_reference="source_payload:do-not-echo")
        self.assertNotIn("do-not-echo", str(raised.exception))

    def test_unverified_artifact_is_quarantined(self) -> None:
        result = ArtifactEligibilityEvaluator().evaluate(
            self.artifact(integrity_state=ArtifactIntegrityState.UNVERIFIED),
            None,
            None,
            None,
            at=self.now,
        )
        self.assertEqual(result.disposition, SupplyChainDisposition.QUARANTINE)
        self.assertEqual(result.reason_code, "ARTIFACT_INTEGRITY_UNVERIFIED")

    def test_generated_code_inherits_wp006_quarantine(self) -> None:
        result = ArtifactEligibilityEvaluator().evaluate(
            self.artifact(generated_code=True), self.verification(), None, None, at=self.now
        )
        self.assertEqual(result.disposition, SupplyChainDisposition.QUARANTINE)
        self.assertEqual(result.reason_code, "GENERATED_CODE_GATE_UNASSIGNED")

    def test_artifact_quarantine_cannot_be_released(self) -> None:
        quarantine = ArtifactQuarantineRecord(
            "quarantine:synthetic",
            "artifact:synthetic",
            "version:synthetic-v1",
            "reason:unverifiable",
            self.now,
            "synthetic-policy-v1",
        )
        self.assertTrue(quarantine.quarantined)
        self.assertFalse(quarantine.released)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(quarantine, released=True)

    def test_generated_code_gate_cannot_self_approve_or_pass(self) -> None:
        gate = GeneratedCodeSecurityGateRecord(
            "gate:synthetic",
            "artifact:generated-synthetic",
            "version:synthetic-v1",
            "criteria:synthetic",
            "reviewer:synthetic-independent",
            "generator:synthetic",
            "implementer:synthetic",
            "synthetic-policy-v1",
        )
        self.assertFalse(gate.passed)
        self.assertFalse(gate.execution_approved)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(gate, reviewer_reference="generator:synthetic")
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(gate, passed=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(gate, execution_approved=True)

    def test_producer_cannot_be_independent_reviewer(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            self.verification(reviewer="producer:synthetic")

    def test_implementer_cannot_be_independent_reviewer(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            self.verification(reviewer="implementer:synthetic")

    def test_version_substitution_is_quarantined(self) -> None:
        evaluator = ArtifactEligibilityEvaluator(
            provenance_registry=self.populated_registry("provenance-policy:synthetic"),
            verification_registry=self.populated_registry("verification-policy:synthetic"),
        )
        result = evaluator.evaluate(
            self.artifact(),
            self.verification(version="version:synthetic-v2"),
            self.acceptance(),
            None,
            at=self.now,
        )
        self.assertEqual(result.reason_code, "ARTIFACT_VERSION_SUBSTITUTION_DENIED")

    def test_stale_acceptance_is_quarantined(self) -> None:
        evaluator = ArtifactEligibilityEvaluator(
            provenance_registry=self.populated_registry("provenance-policy:synthetic"),
            verification_registry=self.populated_registry("verification-policy:synthetic"),
        )
        stale = self.acceptance(
            effective_at=self.now - timedelta(days=2),
            expires_at=self.now - timedelta(days=1),
        )
        result = evaluator.evaluate(self.artifact(), self.verification(), stale, None, at=self.now)
        self.assertEqual(result.disposition, SupplyChainDisposition.QUARANTINE)
        self.assertEqual(result.reason_code, "ARTIFACT_ACCEPTANCE_NOT_CURRENT")

    def test_current_synthetic_acceptance_still_has_no_authority(self) -> None:
        evaluator = ArtifactEligibilityEvaluator(
            provenance_registry=self.populated_registry("provenance-policy:synthetic"),
            verification_registry=self.populated_registry("verification-policy:synthetic"),
            acceptance_registry=self.populated_registry("acceptance-policy:synthetic"),
        )
        acceptance = self.acceptance()
        result = evaluator.evaluate(
            self.artifact(),
            self.verification(),
            acceptance,
            self.authorization(acceptance.acceptance_reference),
            at=self.now,
        )
        self.assertEqual(result.disposition, SupplyChainDisposition.HUMAN_DECISION_REQUIRED)
        self.assertEqual(result.reason_code, "ARTIFACT_ACCEPTANCE_AUTHORITY_UNASSIGNED")

    def test_revocation_is_prospective_and_preserves_history(self) -> None:
        record = ArtifactRevocationRecord(
            "revocation:synthetic",
            "acceptance:synthetic",
            "artifact:synthetic",
            "version:synthetic-v1",
            self.now,
            "authority:synthetic-unassigned",
            "synthetic-policy-v1",
        )
        self.assertTrue(record.prospective)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(record, prospective=False)

    def test_verified_accepted_promoted_and_deployed_are_distinct_types_and_fields(self) -> None:
        self.assertIsNot(ArtifactVerificationRecord, ArtifactAcceptanceRecord)
        self.assertIsNot(ArtifactAcceptanceRecord, ArtifactPromotionReference)
        self.assertIsNot(ArtifactPromotionReference, ArtifactDeploymentReference)
        transition = ArtifactTransitionReferences(
            "artifact:synthetic",
            "version:synthetic-v1",
            acceptance_reference="acceptance:synthetic",
        )
        self.assertFalse(transition.promoted)
        self.assertFalse(transition.deployed)

    def test_distinct_promotion_and_deployment_records_cannot_execute(self) -> None:
        promotion = ArtifactPromotionReference(
            "promotion:synthetic",
            "artifact:synthetic",
            "version:synthetic-v1",
            "acceptance:synthetic",
        )
        deployment = ArtifactDeploymentReference(
            "deployment:synthetic",
            "artifact:synthetic",
            "version:synthetic-v1",
            "promotion:synthetic",
        )
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(promotion, promoted=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(deployment, deployed=True)

    def test_wp009_cannot_mark_promotion_or_deployment(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            ArtifactTransitionReferences(
                "artifact:synthetic", "version:synthetic-v1", promoted=True
            )
        with self.assertRaises(SupplyChainRecoveryContractError):
            ArtifactTransitionReferences(
                "artifact:synthetic", "version:synthetic-v1", deployed=True
            )

    def test_no_artifact_action_boundary_has_no_action_methods(self) -> None:
        boundary = NoArtifactActionBoundary()
        for method in (
            "accept",
            "release",
            "promote",
            "deploy",
            "publish",
            "execute",
            "upload",
            "download",
            "delete",
            "alter",
        ):
            self.assertFalse(hasattr(boundary, method))

    def test_vulnerability_severity_is_symbolic_and_unspecified(self) -> None:
        severity = UNSPECIFIED_VULNERABILITY_SEVERITY
        self.assertIsNone(severity.severity_class_reference)
        self.assertFalse(severity.operational_threshold_selected)
        with self.assertRaises(SupplyChainRecoveryContractError):
            SymbolicVulnerabilitySeverity(
                "severity:synthetic",
                "synthetic-policy-v1",
                operational_threshold_selected=True,
            )

    def test_vulnerability_detected_finding_risk_remediation_acceptance_are_distinct(self) -> None:
        self.assertIsNot(VulnerabilityRecord, ResidualRiskAcceptanceRecord)
        self.assertIsNot(VulnerabilityRecord, RemediationRecord)
        self.assertIsNot(RemediationRecord, SecurityAcceptanceRecord)
        self.assertFalse(self.vulnerability().authoritative_finding)

    def test_stale_vulnerability_denies(self) -> None:
        result = VulnerabilityTreatmentEvaluator().evaluate(
            self.vulnerability(state=VulnerabilityLifecycleState.STALE), at=self.now
        )
        self.assertEqual(result.disposition, SupplyChainDisposition.DENY)
        self.assertEqual(result.reason_code, "VULNERABILITY_STATE_STALE_OR_INDETERMINATE")

    def test_empty_vulnerability_policy_requires_remediation_without_accepting_risk(self) -> None:
        result = VulnerabilityTreatmentEvaluator().evaluate(self.vulnerability(), at=self.now)
        self.assertEqual(result.disposition, SupplyChainDisposition.REMEDIATION_REQUIRED)
        self.assertEqual(result.reason_code, "VULNERABILITY_POLICY_UNASSIGNED")

    def test_remediation_version_mismatch_denies(self) -> None:
        remediation = RemediationRecord(
            "remediation:synthetic",
            "vulnerability:synthetic",
            "component:synthetic",
            "version:synthetic-v2",
            "artifact:proposed-synthetic",
            None,
            "synthetic-policy-v1",
        )
        evaluator = VulnerabilityTreatmentEvaluator(
            policy_registry=self.populated_registry("vulnerability-policy:synthetic")
        )
        result = evaluator.evaluate(self.vulnerability(), remediation, at=self.now)
        self.assertEqual(result.reason_code, "REMEDIATION_VERSION_MISMATCH")

    def test_remediation_cannot_be_completed_verified_or_security_accepted(self) -> None:
        for field_name in ("reported_complete", "independently_verified", "security_accepted"):
            values = {
                "remediation_reference": "remediation:synthetic",
                "vulnerability_reference": "vulnerability:synthetic",
                "affected_component_reference": "component:synthetic",
                "exact_version_reference": "version:synthetic-v1",
                "proposed_artifact_reference": "artifact:proposed-synthetic",
                "verification_reference": None,
                "policy_version": "synthetic-policy-v1",
                field_name: True,
            }
            with self.assertRaises(SupplyChainRecoveryContractError):
                RemediationRecord(**values)  # type: ignore[arg-type]

    def test_mitigation_is_distinct_and_cannot_be_applied_or_verified(self) -> None:
        mitigation = MitigationRecord(
            "mitigation:synthetic",
            "vulnerability:synthetic",
            "component:synthetic",
            "version:synthetic-v1",
            ("control:synthetic",),
            "synthetic-policy-v1",
        )
        self.assertIsNot(MitigationRecord, RemediationRecord)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(mitigation, applied=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(mitigation, independently_verified=True)

    def test_exception_request_review_and_approval_are_segregated(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            self.exception(reviewer_reference="requester:synthetic")

    def test_exception_cannot_activate_or_auto_renew(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            self.exception(active=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            self.exception(auto_renewed=True)

    def test_expired_exception_fails_closed(self) -> None:
        exception = self.exception(
            effective_at=self.now - timedelta(days=2),
            expires_at=self.now - timedelta(days=1),
        )
        evaluator = VulnerabilityTreatmentEvaluator(
            policy_registry=self.populated_registry("vulnerability-policy:synthetic"),
            exception_registry=self.populated_registry("exception-policy:synthetic"),
        )
        result = evaluator.evaluate(self.vulnerability(), exception=exception, at=self.now)
        self.assertEqual(result.disposition, SupplyChainDisposition.DENY)
        self.assertEqual(result.reason_code, "EXCEPTION_NOT_CURRENT")

    def test_residual_risk_cannot_be_accepted(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            ResidualRiskAcceptanceRecord(
                "risk-acceptance:synthetic",
                "vulnerability:synthetic",
                "component:synthetic",
                "version:synthetic-v1",
                "authority:synthetic-unassigned",
                "synthetic-policy-v1",
                accepted=True,
            )

    def test_silent_risk_acceptance_is_prohibited(self) -> None:
        evaluator = VulnerabilityTreatmentEvaluator(
            policy_registry=self.populated_registry("vulnerability-policy:synthetic")
        )
        result = evaluator.evaluate(self.vulnerability(), at=self.now)
        self.assertEqual(result.reason_code, "UNRESOLVED_VULNERABILITY_DENY")
        self.assertNotEqual(result.disposition, SupplyChainDisposition.HUMAN_DECISION_REQUIRED)

    def test_security_acceptance_cannot_be_granted(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            SecurityAcceptanceRecord(
                "security-acceptance:synthetic",
                "artifact:synthetic",
                "version:synthetic-v1",
                "verification:synthetic",
                "authority:synthetic-unassigned",
                "synthetic-policy-v1",
                accepted=True,
            )

    def test_no_remediation_boundary_has_no_operational_methods(self) -> None:
        boundary = NoRemediationBoundary()
        for method in ("scan", "patch", "mitigate", "waive", "close", "modify"):
            self.assertFalse(hasattr(boundary, method))

    def test_unknown_recovery_state_is_quarantined(self) -> None:
        result = RecoverySecurityEvaluator().evaluate(self.recovery_source(), None, None)
        self.assertEqual(result.disposition, SupplyChainDisposition.QUARANTINE)
        self.assertEqual(result.reason_code, "RECOVERY_STATE_COMPROMISED_OR_UNKNOWN")

    def test_compromised_recovery_source_cannot_leave_quarantine(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            self.recovery_source(state=RecoveryIntegrityState.COMPROMISED, quarantined=False)

    def test_recovery_source_cannot_assert_authoritative_known_good(self) -> None:
        source = self.recovery_source(state=RecoveryIntegrityState.KNOWN_GOOD_REFERENCE_ONLY)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(source, authoritative_known_good=True)

    def test_current_security_state_is_preserved_in_reconciliation(self) -> None:
        reconciliation = self.reconciliation()
        self.assertTrue(reconciliation.current_state_available)
        self.assertEqual(reconciliation.revocation_references, ("revocation:current",))
        self.assertEqual(reconciliation.restriction_references, ("restriction:current",))
        self.assertEqual(reconciliation.deletion_references, ("deletion:current",))
        self.assertEqual(reconciliation.classification_references, ("classification:current",))
        self.assertEqual(reconciliation.provenance_references, ("provenance:current",))
        self.assertEqual(reconciliation.security_state_references, ("security-state:current",))

    def test_reconciliation_cannot_restore_stale_authority(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(self.reconciliation(), restored_stale_authority=True)

    def test_reconciliation_tracks_all_prohibited_restoration_classes(self) -> None:
        reconciliation = self.reconciliation()
        self.assertEqual(reconciliation.stale_grant_references, ("grant:stale",))
        self.assertEqual(reconciliation.expired_permission_references, ("permission:expired",))
        self.assertEqual(reconciliation.revoked_artifact_references, ("artifact:revoked",))
        self.assertEqual(reconciliation.invalid_credential_session_references, ("session:invalid",))
        self.assertEqual(
            reconciliation.ineligible_agent_model_tool_references, ("agent:ineligible",)
        )

    def test_unavailable_current_state_requires_reconciliation(self) -> None:
        evaluator = RecoverySecurityEvaluator(
            source_registry=self.populated_registry("source-policy:synthetic"),
            known_good_registry=self.populated_registry("known-good-policy:synthetic"),
        )
        source = self.recovery_source(
            state=RecoveryIntegrityState.KNOWN_GOOD_REFERENCE_ONLY,
            quarantined=False,
        )
        result = evaluator.evaluate(
            source, self.reconciliation(current_state_available=False), None
        )
        self.assertEqual(result.disposition, SupplyChainDisposition.RECONCILIATION_REQUIRED)
        self.assertEqual(result.reason_code, "CURRENT_SECURITY_STATE_REQUIRED")

    def test_recovery_version_substitution_denies(self) -> None:
        evaluator = RecoverySecurityEvaluator(
            source_registry=self.populated_registry("source-policy:synthetic"),
            known_good_registry=self.populated_registry("known-good-policy:synthetic"),
        )
        source = self.recovery_source(
            state=RecoveryIntegrityState.KNOWN_GOOD_REFERENCE_ONLY,
            quarantined=False,
        )
        result = evaluator.evaluate(
            source, self.reconciliation(version="version:synthetic-v2"), None
        )
        self.assertEqual(result.reason_code, "RECOVERY_VERSION_SUBSTITUTION_DENIED")

    def test_invalidation_is_obligation_only(self) -> None:
        obligation = InvalidationObligation(
            "obligation:synthetic",
            "recovery-source:synthetic",
            "credential:opaque-synthetic",
            "key:opaque-synthetic",
            "session:opaque-synthetic",
            "synthetic-policy-v1",
        )
        self.assertFalse(obligation.executed)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(obligation, executed=True)

    def test_invalidation_obligation_requires_an_opaque_target(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            InvalidationObligation(
                "obligation:synthetic",
                "recovery-source:synthetic",
                None,
                None,
                None,
                "synthetic-policy-v1",
            )

    def test_recovery_review_must_be_independent(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(
                self.recovery_review(),
                reviewer_reference="requester:synthetic",
            )

    def test_recovery_review_cannot_grant_security_acceptance(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(self.recovery_review(), security_recovery_accepted=True)

    def test_recovery_acceptance_restoration_reauthorization_are_separate(self) -> None:
        references = RecoveryAuthorityReferences("recovery:synthetic", "synthetic-policy-v1")
        self.assertIsNone(references.security_recovery_acceptance_reference)
        self.assertIsNone(references.restoration_reference)
        self.assertIsNone(references.reauthorization_reference)
        self.assertIsNone(references.reinstatement_reference)

    def test_recovery_restoration_reauthorization_reinstatement_are_distinct_types(self) -> None:
        recovery = RecoveryResultReference(
            "recovery:synthetic",
            "recovery-source:synthetic",
            "version:synthetic-v1",
        )
        acceptance = SecurityRecoveryAcceptanceRecord(
            "recovery-acceptance:synthetic",
            "recovery-source:synthetic",
            "version:synthetic-v1",
            "reconciliation:synthetic",
            "recovery-review:synthetic",
            "authority:synthetic-unassigned",
            "synthetic-policy-v1",
        )
        restoration = OperationalRestorationReference(
            "restoration:synthetic",
            "recovery:synthetic",
            "recovery-acceptance:synthetic",
        )
        reauthorization = ReauthorizationReference(
            "reauthorization:synthetic",
            "recovery:synthetic",
            "authorization:current-synthetic",
        )
        reinstatement = ReinstatementReference(
            "reinstatement:synthetic",
            "restoration:synthetic",
            "reauthorization:synthetic",
        )
        self.assertEqual(
            len(
                {
                    type(recovery),
                    type(acceptance),
                    type(restoration),
                    type(reauthorization),
                    type(reinstatement),
                }
            ),
            5,
        )
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(recovery, completed=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(acceptance, accepted=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(restoration, restored=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(reauthorization, reauthorized=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(reinstatement, reinstated=True)

    def test_recovery_authority_references_cannot_execute_state_changes(self) -> None:
        base = RecoveryAuthorityReferences("recovery:synthetic", "synthetic-policy-v1")
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(base, recovered=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(base, operationally_restored=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(base, reauthorized=True)
        with self.assertRaises(SupplyChainRecoveryContractError):
            replace(base, reinstated=True)

    def test_recovery_authority_evaluation_requires_current_authorization(self) -> None:
        references = RecoveryAuthorityReferences("recovery:synthetic", "synthetic-policy-v1")
        result = RecoverySecurityEvaluator().evaluate_authority(references, None)
        self.assertEqual(result.disposition, SupplyChainDisposition.DENY)
        self.assertEqual(result.reason_code, "CURRENT_RECOVERY_AUTHORIZATION_REQUIRED")

    def test_current_authorization_cannot_replace_unassigned_recovery_authorities(self) -> None:
        references = RecoveryAuthorityReferences("recovery:synthetic", "synthetic-policy-v1")
        result = RecoverySecurityEvaluator().evaluate_authority(
            references, self.authorization(references.recovery_reference)
        )
        self.assertEqual(result.disposition, SupplyChainDisposition.HUMAN_DECISION_REQUIRED)
        self.assertEqual(
            result.reason_code,
            "RECOVERY_RESTORATION_REINSTATEMENT_AUTHORITY_UNASSIGNED",
        )

    def test_no_recovery_boundary_has_no_operational_methods(self) -> None:
        boundary = NoRecoveryBoundary()
        for method in (
            "backup",
            "snapshot",
            "restore",
            "failover",
            "rotate",
            "invalidate",
            "reconcile",
            "reinstate",
        ):
            self.assertFalse(hasattr(boundary, method))

    def test_every_untrusted_origin_cannot_create_authority_or_known_good_state(self) -> None:
        for origin in UntrustedContentOrigin:
            claim = UntrustedSupplyChainClaim(
                "claim:synthetic",
                origin,
                asserted_acceptance_reference="acceptance:false",
                asserted_risk_acceptance_reference="risk-acceptance:false",
                asserted_known_good_reference="known-good:false",
                asserted_execution_authority_reference="authority:false",
            )
            result = evaluate_untrusted_supply_chain_claim(claim)
            self.assertEqual(result.disposition, SupplyChainDisposition.DENY)
            self.assertFalse(result.capability_created)

    def test_prompt_injection_cannot_change_artifact_or_recovery_state(self) -> None:
        claim = UntrustedSupplyChainClaim(
            "claim:prompt-injection",
            UntrustedContentOrigin.MODEL_OUTPUT,
            asserted_acceptance_reference="acceptance:false",
            asserted_known_good_reference="known-good:false",
        )
        result = evaluate_untrusted_supply_chain_claim(claim)
        self.assertEqual(result.reason_code, "UNTRUSTED_CONTENT_CANNOT_CREATE_AUTHORITY")

    def test_control_result_cannot_create_capability(self) -> None:
        with self.assertRaises(SupplyChainRecoveryContractError):
            SupplyChainControlResult(
                SupplyChainDisposition.DENY,
                "CAPABILITY_MUST_REMAIN_ABSENT",
                capability_created=True,
            )

    def test_boundaries_expose_no_network_product_or_external_destination(self) -> None:
        for boundary in (
            NoArtifactActionBoundary(),
            NoRemediationBoundary(),
            NoRecoveryBoundary(),
        ):
            for name in (
                "network",
                "endpoint",
                "provider",
                "repository",
                "scanner",
                "cicd",
                "destination",
                "client",
            ):
                self.assertFalse(hasattr(boundary, name))


if __name__ == "__main__":
    unittest.main()
