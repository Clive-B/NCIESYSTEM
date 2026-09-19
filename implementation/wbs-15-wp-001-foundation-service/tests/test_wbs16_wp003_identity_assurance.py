import unittest
from datetime import UTC, datetime, timedelta

from ncie_foundation.identity_assurance import (
    IDENTITY_ASSURANCE_BASELINE_VERSION,
    IDENTITY_ASSURANCE_DECISION_EVIDENCE,
    IDENTITY_ASSURANCE_IMPLEMENTATION_AUTHORITY,
    AssuranceContext,
    AssuranceEvaluator,
    AssuranceRequest,
    AssuranceState,
    AssuranceValidationCode,
    CredentialReferenceClass,
    CredentialReferenceMetadata,
    EnrollmentAuthorityClass,
    EnrollmentAuthorityDecision,
    IdentityAssuranceContractError,
    IdentityLifecycleAction,
    IdentityLifecycleCoordinator,
    IdentityLifecycleState,
    LifecycleRequest,
    ProofingRecord,
    ProofingState,
    RevocationCause,
    RevocationDirective,
    RevocationState,
    SessionMetadata,
    UnassignedEnrollmentAuthority,
    UnboundSessionIssuer,
    required_proofing_for,
    validate_session_derivation,
)
from ncie_foundation.security_principals import (
    AuthoritativeSourceCategory,
    PrincipalClass,
    SecurityPrincipal,
    authoritative_source_for,
)


class ApprovingAuthority:
    def decide(self, request: LifecycleRequest) -> EnrollmentAuthorityDecision | None:
        del request
        return EnrollmentAuthorityDecision(
            approved=True,
            authority_class=EnrollmentAuthorityClass.IDENTITY_LIFECYCLE_APPROVER,
            decision_reference="synthetic-authority-decision",
            authority_holder_reference="synthetic-authority-holder",
        )


class IdentityAssuranceTests(unittest.TestCase):
    now = datetime(2026, 9, 19, 12, 0, tzinfo=UTC)

    @staticmethod
    def principal(principal_class: PrincipalClass = PrincipalClass.HUMAN) -> SecurityPrincipal:
        return SecurityPrincipal(
            principal_class,
            authoritative_source_for(principal_class),
            f"synthetic-{principal_class.value.lower()}-subject",
        )

    @classmethod
    def proofing(cls, principal: SecurityPrincipal | None = None) -> ProofingRecord:
        resolved = principal or cls.principal()
        return ProofingRecord(
            record_reference="synthetic-proofing-record",
            principal=resolved,
            proofing_state=required_proofing_for(resolved.principal_class),
            evidence_references=("synthetic-evidence-reference",),
            source_owner_reference="synthetic-source-owner",
            recorded_at=cls.now,
            agent_owner_reference=(
                "synthetic-agent-owner"
                if resolved.principal_class is PrincipalClass.AGENT
                else None
            ),
            purpose_reference=(
                "synthetic-purpose"
                if resolved.principal_class in {PrincipalClass.AGENT, PrincipalClass.SERVICE}
                else None
            ),
            version_reference=(
                "synthetic-version" if resolved.principal_class is PrincipalClass.AGENT else None
            ),
        )

    @classmethod
    def credential(
        cls,
        *,
        assurance: AssuranceState = AssuranceState.BASELINE,
        expires_at: datetime | None = None,
        revoked: bool = False,
    ) -> CredentialReferenceMetadata:
        principal = cls.principal()
        return CredentialReferenceMetadata(
            credential_reference="synthetic-credential-reference",
            credential_class=CredentialReferenceClass.HUMAN,
            principal=principal,
            scopes=("synthetic-scope",),
            audiences=("synthetic-audience",),
            issued_at=cls.now - timedelta(minutes=5),
            expires_at=expires_at or cls.now + timedelta(hours=1),
            assurance_state=assurance,
            policy_version="synthetic-policy-v1",
            duration_policy_reference="synthetic-duration-policy",
            revocation_state=RevocationState.REVOKED if revoked else RevocationState.CURRENT,
        )

    @classmethod
    def session(
        cls,
        *,
        assurance: AssuranceState = AssuranceState.BASELINE,
        expires_at: datetime | None = None,
        revoked: bool = False,
        credential_reference: str = "synthetic-credential-reference",
    ) -> SessionMetadata:
        return SessionMetadata(
            session_reference="synthetic-session-reference",
            base_principal=cls.principal(),
            issuer_source=AuthoritativeSourceCategory.AUTHENTICATION_SESSION_ISSUER,
            scopes=("synthetic-scope",),
            audiences=("synthetic-audience",),
            issued_at=cls.now - timedelta(minutes=1),
            expires_at=expires_at or cls.now + timedelta(minutes=30),
            assurance_state=assurance,
            policy_version="synthetic-policy-v1",
            duration_policy_reference="synthetic-duration-policy",
            credential_reference=credential_reference,
            binding_reference="synthetic-session-binding",
            replay_policy_reference="synthetic-replay-policy",
            revocation_state=RevocationState.REVOKED if revoked else RevocationState.CURRENT,
        )

    @classmethod
    def request(
        cls,
        context: AssuranceContext = AssuranceContext.STANDARD_SESSION,
        **references: str,
    ) -> AssuranceRequest:
        return AssuranceRequest(
            context=context,
            audience="synthetic-audience",
            required_scope="synthetic-scope",
            evaluated_at=cls.now,
            step_up_evidence_reference=references.get("step_up"),
            emergency_trigger_reference=references.get("emergency"),
            freshness_policy_reference=references.get("freshness"),
        )

    def test_baseline_and_authority_evidence_are_versioned(self) -> None:
        self.assertEqual(IDENTITY_ASSURANCE_BASELINE_VERSION, "NCIE-WBS16-WP003-2026-09-19")
        self.assertTrue(IDENTITY_ASSURANCE_DECISION_EVIDENCE.endswith("-014"))
        self.assertTrue(IDENTITY_ASSURANCE_IMPLEMENTATION_AUTHORITY.endswith("-015"))

    def test_all_seven_classes_have_approved_proofing_and_credential_classes(self) -> None:
        self.assertEqual(len(PrincipalClass), 7)
        self.assertEqual(
            {item.value for item in CredentialReferenceClass},
            {item.value for item in PrincipalClass},
        )
        self.assertEqual(
            required_proofing_for(PrincipalClass.HUMAN), ProofingState.INSTITUTIONALLY_VERIFIED
        )
        self.assertEqual(
            required_proofing_for(PrincipalClass.PRIVILEGED), ProofingState.ENHANCED_SENSITIVE
        )
        for principal_class in PrincipalClass:
            self.assertIsInstance(required_proofing_for(principal_class), ProofingState)

    def test_proofing_is_source_bound_and_wrong_tier_fails(self) -> None:
        with self.assertRaises(IdentityAssuranceContractError):
            ProofingRecord(
                record_reference="synthetic-proofing-record",
                principal=self.principal(PrincipalClass.HUMAN),
                proofing_state=ProofingState.SOURCE_ATTESTED,
                evidence_references=("synthetic-evidence-reference",),
                source_owner_reference="synthetic-owner",
                recorded_at=self.now,
            )
        with self.assertRaises(IdentityAssuranceContractError) as caught:
            ProofingRecord(
                record_reference="password=protected-value",
                principal=self.principal(PrincipalClass.HUMAN),
                proofing_state=ProofingState.INSTITUTIONALLY_VERIFIED,
                evidence_references=("synthetic-evidence-reference",),
                source_owner_reference="synthetic-owner",
                recorded_at=self.now,
            )
        self.assertNotIn("protected-value", str(caught.exception))
        with self.assertRaises(IdentityAssuranceContractError):
            ProofingRecord(
                record_reference="synthetic-proofing-record",
                principal=self.principal(PrincipalClass.HUMAN),
                proofing_state=ProofingState.INSTITUTIONALLY_VERIFIED,
                evidence_references=(),
                source_owner_reference="synthetic-owner",
                recorded_at=self.now,
            )

    def test_agent_and_service_proofing_require_governed_metadata(self) -> None:
        for principal_class in (PrincipalClass.AGENT, PrincipalClass.SERVICE):
            with self.subTest(principal_class=principal_class):
                with self.assertRaises(IdentityAssuranceContractError):
                    ProofingRecord(
                        record_reference="synthetic-proofing-record",
                        principal=self.principal(principal_class),
                        proofing_state=ProofingState.SOURCE_ATTESTED,
                        evidence_references=("synthetic-evidence-reference",),
                        source_owner_reference="synthetic-owner",
                        recorded_at=self.now,
                    )

    def test_unassigned_authority_blocks_live_activation(self) -> None:
        principal = self.principal()
        request = LifecycleRequest(
            request_reference="synthetic-enrollment-request",
            principal=principal,
            current_state=IdentityLifecycleState.PENDING_ENROLLMENT,
            action=IdentityLifecycleAction.ACTIVATE,
            requested_at=self.now,
            proofing_record=self.proofing(principal),
        )
        result = IdentityLifecycleCoordinator(UnassignedEnrollmentAuthority()).evaluate(request)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason_code, "CURRENT_AUTHORITY_REQUIRED")

    def test_approved_lifecycle_transitions_are_explicit_and_revoking(self) -> None:
        coordinator = IdentityLifecycleCoordinator(ApprovingAuthority())
        principal = self.principal()
        activation = coordinator.evaluate(
            LifecycleRequest(
                "synthetic-activation",
                principal,
                IdentityLifecycleState.PENDING_ENROLLMENT,
                IdentityLifecycleAction.ACTIVATE,
                self.now,
                self.proofing(principal),
            )
        )
        suspension = coordinator.evaluate(
            LifecycleRequest(
                "synthetic-suspension",
                principal,
                IdentityLifecycleState.ACTIVE,
                IdentityLifecycleAction.SUSPEND,
                self.now,
            )
        )
        reactivation = coordinator.evaluate(
            LifecycleRequest(
                "synthetic-reactivation",
                principal,
                IdentityLifecycleState.REACTIVATION_PENDING,
                IdentityLifecycleAction.REACTIVATE,
                self.now,
                self.proofing(principal),
            )
        )
        self.assertTrue(activation.allowed)
        self.assertEqual(activation.resulting_state, IdentityLifecycleState.ACTIVE)
        self.assertTrue(suspension.allowed)
        self.assertTrue(suspension.invalidate_prior_sessions)
        self.assertTrue(reactivation.allowed)
        self.assertTrue(reactivation.invalidate_prior_sessions)
        self.assertTrue(reactivation.requires_new_assurance)
        self.assertFalse(reactivation.restores_prior_privilege)

    def test_invalid_transition_and_duplicate_identity_fail_closed(self) -> None:
        coordinator = IdentityLifecycleCoordinator(ApprovingAuthority())
        invalid = coordinator.evaluate(
            LifecycleRequest(
                "synthetic-invalid-transition",
                self.principal(),
                IdentityLifecycleState.TERMINATED,
                IdentityLifecycleAction.ACTIVATE,
                self.now,
            )
        )
        duplicate = coordinator.evaluate(
            LifecycleRequest(
                "synthetic-duplicate",
                self.principal(),
                IdentityLifecycleState.ACTIVE,
                IdentityLifecycleAction.RECORD_DUPLICATE,
                self.now,
            )
        )
        self.assertFalse(invalid.allowed)
        self.assertFalse(duplicate.allowed)
        self.assertTrue(duplicate.human_review_required)

    def test_recovery_requires_reproofing_and_invalidates_old_sessions(self) -> None:
        principal = self.principal()
        base = LifecycleRequest(
            "synthetic-recovery-completion",
            principal,
            IdentityLifecycleState.RECOVERY_PENDING,
            IdentityLifecycleAction.COMPLETE_RECOVERY,
            self.now,
            self.proofing(principal),
        )
        coordinator = IdentityLifecycleCoordinator(ApprovingAuthority())
        self.assertFalse(coordinator.evaluate(base).allowed)
        complete = coordinator.evaluate(
            LifecycleRequest(
                "synthetic-recovery-completion",
                principal,
                IdentityLifecycleState.RECOVERY_PENDING,
                IdentityLifecycleAction.COMPLETE_RECOVERY,
                self.now,
                self.proofing(principal),
                AssuranceState.RECOVERY_REPROOFED,
            )
        )
        self.assertTrue(complete.allowed)
        self.assertTrue(complete.invalidate_prior_sessions)
        self.assertTrue(complete.requires_new_assurance)
        self.assertFalse(complete.restores_prior_privilege)

    def test_credential_and_session_require_scope_audience_and_explicit_expiry(self) -> None:
        with self.assertRaises(IdentityAssuranceContractError):
            CredentialReferenceMetadata(
                credential_reference="synthetic-reference",
                credential_class=CredentialReferenceClass.HUMAN,
                principal=self.principal(),
                scopes=(),
                audiences=("synthetic-audience",),
                issued_at=self.now,
                expires_at=self.now + timedelta(hours=1),
                assurance_state=AssuranceState.BASELINE,
                policy_version="synthetic-policy",
                duration_policy_reference="synthetic-duration-policy",
            )
        with self.assertRaises(IdentityAssuranceContractError):
            self.session(expires_at=self.now - timedelta(hours=1))

    def test_unbound_issuer_cannot_issue_a_live_session(self) -> None:
        principal = self.principal()
        self.assertIsNone(
            UnboundSessionIssuer().issue(principal=principal, credential=self.credential())
        )

    def test_standard_assurance_is_valid_but_never_authorizes_action(self) -> None:
        result = AssuranceEvaluator().evaluate(
            lifecycle_state=IdentityLifecycleState.ACTIVE,
            credential=self.credential(),
            session=self.session(),
            request=self.request(),
        )
        self.assertTrue(result.valid)
        self.assertFalse(result.authorizes_action)

    def test_inactive_revoked_expired_and_overlong_sessions_fail_closed(self) -> None:
        evaluator = AssuranceEvaluator()
        cases = (
            (
                IdentityLifecycleState.SUSPENDED,
                self.credential(),
                self.session(),
                AssuranceValidationCode.IDENTITY_NOT_ACTIVE,
            ),
            (
                IdentityLifecycleState.ACTIVE,
                self.credential(revoked=True),
                self.session(),
                AssuranceValidationCode.CREDENTIAL_REVOKED,
            ),
            (
                IdentityLifecycleState.ACTIVE,
                self.credential(),
                self.session(revoked=True),
                AssuranceValidationCode.SESSION_REVOKED,
            ),
            (
                IdentityLifecycleState.ACTIVE,
                self.credential(expires_at=self.now),
                self.session(expires_at=self.now - timedelta(seconds=1)),
                AssuranceValidationCode.CREDENTIAL_EXPIRED,
            ),
            (
                IdentityLifecycleState.ACTIVE,
                self.credential(expires_at=self.now + timedelta(minutes=10)),
                self.session(expires_at=self.now + timedelta(minutes=20)),
                AssuranceValidationCode.SESSION_EXCEEDS_CREDENTIAL,
            ),
            (
                IdentityLifecycleState.ACTIVE,
                self.credential(assurance=AssuranceState.BASELINE),
                self.session(assurance=AssuranceState.ELEVATED),
                AssuranceValidationCode.CREDENTIAL_ASSURANCE_INSUFFICIENT,
            ),
            (
                IdentityLifecycleState.ACTIVE,
                self.credential(),
                self.session(credential_reference="different-credential-reference"),
                AssuranceValidationCode.CREDENTIAL_BINDING_MISMATCH,
            ),
        )
        for state, credential, session, expected in cases:
            with self.subTest(expected=expected):
                result = evaluator.evaluate(
                    lifecycle_state=state,
                    credential=credential,
                    session=session,
                    request=self.request(),
                )
                self.assertFalse(result.valid)
                self.assertEqual(result.code, expected)

    def test_privileged_break_glass_and_high_risk_require_symbolic_inputs(self) -> None:
        evaluator = AssuranceEvaluator()
        credential = self.credential(assurance=AssuranceState.ELEVATED)
        session = self.session(assurance=AssuranceState.ELEVATED)
        cases = (
            (
                self.request(AssuranceContext.PRIVILEGED_ACCESS),
                AssuranceValidationCode.STEP_UP_EVIDENCE_MISSING,
            ),
            (
                self.request(AssuranceContext.BREAK_GLASS, step_up="synthetic-step-up"),
                AssuranceValidationCode.EMERGENCY_TRIGGER_MISSING,
            ),
            (
                self.request(AssuranceContext.HIGH_RISK_ACTION, step_up="synthetic-step-up"),
                AssuranceValidationCode.FRESHNESS_POLICY_MISSING,
            ),
        )
        for request, expected in cases:
            with self.subTest(expected=expected):
                result = evaluator.evaluate(
                    lifecycle_state=IdentityLifecycleState.ACTIVE,
                    credential=credential,
                    session=session,
                    request=request,
                )
                self.assertFalse(result.valid)
                self.assertEqual(result.code, expected)

    def test_post_recovery_requires_recovery_reproofed_state(self) -> None:
        evaluator = AssuranceEvaluator()
        insufficient = evaluator.evaluate(
            lifecycle_state=IdentityLifecycleState.ACTIVE,
            credential=self.credential(assurance=AssuranceState.ELEVATED),
            session=self.session(assurance=AssuranceState.ELEVATED),
            request=self.request(AssuranceContext.POST_RECOVERY),
        )
        self.assertFalse(insufficient.valid)
        self.assertEqual(insufficient.code, AssuranceValidationCode.ASSURANCE_INSUFFICIENT)

    def test_revocation_directive_requires_sessions_tokens_and_caches(self) -> None:
        directive = RevocationDirective(
            directive_reference="synthetic-revocation-directive",
            principal_reference="synthetic-principal-reference",
            cause=RevocationCause.IDENTITY_SUSPENDED,
            effective_at=self.now,
            session_references=("synthetic-session-reference",),
            token_references=("synthetic-token-reference",),
            cache_references=("synthetic-cache-reference",),
        )
        self.assertEqual(directive.cause, RevocationCause.IDENTITY_SUSPENDED)
        with self.assertRaises(IdentityAssuranceContractError):
            RevocationDirective(
                directive_reference="synthetic-invalid-directive",
                principal_reference="synthetic-principal-reference",
                cause=RevocationCause.IDENTITY_TERMINATED,
                effective_at=self.now,
                session_references=("synthetic-session-reference",),
                token_references=(),
                cache_references=("synthetic-cache-reference",),
            )

    def test_session_device_identity_is_derivative_only(self) -> None:
        session_principal = self.principal(PrincipalClass.SESSION_DEVICE)
        human = self.principal(PrincipalClass.HUMAN)
        self.assertTrue(validate_session_derivation(session_principal, human))
        self.assertFalse(validate_session_derivation(session_principal, session_principal))


if __name__ == "__main__":
    unittest.main()
