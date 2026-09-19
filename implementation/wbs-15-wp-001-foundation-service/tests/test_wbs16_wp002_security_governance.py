import unittest
from datetime import UTC, datetime, timedelta
from typing import cast

from ncie_foundation.security_governance import (
    APPROVED_DEVELOPMENT_RISK_APPETITE,
    APPROVED_THREAT_ASSUMPTIONS,
    SECURITY_GOVERNANCE_BASELINE_VERSION,
    SECURITY_GOVERNANCE_DECISION_EVIDENCE,
    AuthorityAssignment,
    AuthorityRegistry,
    DevelopmentRiskEvaluator,
    DevelopmentRiskRequest,
    GovernanceContractError,
    GovernanceDecision,
    GovernanceDecisionRecord,
    GovernanceDecisionValidator,
    GovernanceValidationCode,
    GovernedAct,
    GovernedTarget,
    InstitutionalRole,
    ReviewRecommendation,
    RiskAppetiteLevel,
    RiskDomain,
    RiskEvaluationDisposition,
    RiskTreatment,
    RiskTreatmentPlan,
    SecurityArchitectureReview,
    SecurityControlOwnership,
    ThreatAssumption,
)


class SecurityGovernanceTests(unittest.TestCase):
    now = datetime(2026, 9, 19, 12, 0, tzinfo=UTC)

    @staticmethod
    def target(*, version: str = "1.0") -> GovernedTarget:
        return GovernedTarget(
            target_reference="ncie-009-chapter-1",
            scope_reference="security-architecture-sign-off",
            version=version,
        )

    @classmethod
    def assignment(
        cls,
        *,
        holder: str = "project-owner-reference",
        target: GovernedTarget | None = None,
        revoked_at: datetime | None = None,
    ) -> AuthorityAssignment:
        return AuthorityAssignment(
            assignment_reference="authority-assignment-reference",
            holder_reference=holder,
            institutional_role=InstitutionalRole.PROJECT_OWNER,
            governed_act=GovernedAct.CHAPTER_SECURITY_ARCHITECTURE_SIGN_OFF,
            target=target or cls.target(),
            effective_from=cls.now - timedelta(days=1),
            revoked_at=revoked_at,
        )

    @classmethod
    def review(
        cls,
        *,
        target: GovernedTarget | None = None,
        reviewer: str = "independent-reviewer-reference",
        reviewer_role: InstitutionalRole = InstitutionalRole.SECURITY_ARCHITECTURE_REVIEWER,
        reviewed_at: datetime | None = None,
        independent: bool = True,
        material_conflict: bool = False,
        recommendation: ReviewRecommendation = ReviewRecommendation.SUPPORT,
    ) -> SecurityArchitectureReview:
        return SecurityArchitectureReview(
            review_reference="review-reference",
            reviewer_reference=reviewer,
            reviewer_role=reviewer_role,
            target=target or cls.target(),
            reviewed_at=reviewed_at or cls.now - timedelta(hours=1),
            recommendation=recommendation,
            author_or_implementer_references=("responsible-implementer-reference",),
            independent=independent,
            material_conflict=material_conflict,
        )

    @classmethod
    def decision(
        cls,
        *,
        target: GovernedTarget | None = None,
        decider: str = "project-owner-reference",
        review: SecurityArchitectureReview | None = None,
    ) -> GovernanceDecisionRecord:
        resolved_target = target or cls.target()
        return GovernanceDecisionRecord(
            decision_reference="decision-reference",
            governed_act=GovernedAct.CHAPTER_SECURITY_ARCHITECTURE_SIGN_OFF,
            target=resolved_target,
            decision=GovernanceDecision.APPROVE,
            decider_reference=decider,
            decided_at=cls.now,
            review=review if review is not None else cls.review(target=resolved_target),
        )

    def test_exact_single_current_authority_and_independent_review_are_valid(self) -> None:
        validator = GovernanceDecisionValidator(AuthorityRegistry((self.assignment(),)))
        result = validator.validate(self.decision())
        self.assertTrue(result.valid)
        self.assertEqual(result.code, GovernanceValidationCode.VALID)

    def test_missing_duplicate_revoked_and_wrong_holder_authority_fail_closed(self) -> None:
        cases = (
            (
                AuthorityRegistry(()),
                self.decision(),
                GovernanceValidationCode.NO_CURRENT_AUTHORITY,
            ),
            (
                AuthorityRegistry(
                    (
                        self.assignment(),
                        AuthorityAssignment(
                            assignment_reference="second-assignment-reference",
                            holder_reference="second-owner-reference",
                            institutional_role=InstitutionalRole.PROJECT_OWNER,
                            governed_act=GovernedAct.CHAPTER_SECURITY_ARCHITECTURE_SIGN_OFF,
                            target=self.target(),
                            effective_from=self.now - timedelta(days=1),
                        ),
                    )
                ),
                self.decision(),
                GovernanceValidationCode.MULTIPLE_CURRENT_AUTHORITIES,
            ),
            (
                AuthorityRegistry((self.assignment(revoked_at=self.now - timedelta(hours=2)),)),
                self.decision(),
                GovernanceValidationCode.NO_CURRENT_AUTHORITY,
            ),
            (
                AuthorityRegistry((self.assignment(),)),
                self.decision(decider="unassigned-owner-reference"),
                GovernanceValidationCode.DECIDER_NOT_CURRENT_AUTHORITY,
            ),
        )
        for registry, decision, expected in cases:
            with self.subTest(expected=expected):
                result = GovernanceDecisionValidator(registry).validate(decision)
                self.assertFalse(result.valid)
                self.assertEqual(result.code, expected)

    def test_target_scope_and_version_do_not_expand(self) -> None:
        assignment = self.assignment(target=self.target(version="1.0"))
        changed_target = self.target(version="1.1")
        result = GovernanceDecisionValidator(AuthorityRegistry((assignment,))).validate(
            self.decision(target=changed_target, review=self.review(target=changed_target))
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.code, GovernanceValidationCode.NO_CURRENT_AUTHORITY)

    def test_missing_self_or_conflicted_review_cannot_support_acceptance(self) -> None:
        validator = GovernanceDecisionValidator(AuthorityRegistry((self.assignment(),)))
        missing = GovernanceDecisionRecord(
            decision_reference="decision-without-review",
            governed_act=GovernedAct.CHAPTER_SECURITY_ARCHITECTURE_SIGN_OFF,
            target=self.target(),
            decision=GovernanceDecision.APPROVE,
            decider_reference="project-owner-reference",
            decided_at=self.now,
            review=None,
        )
        cases = (
            (missing, GovernanceValidationCode.REVIEW_REQUIRED),
            (
                self.decision(review=self.review(reviewer="responsible-implementer-reference")),
                GovernanceValidationCode.REVIEW_CONFLICT,
            ),
            (
                self.decision(review=self.review(independent=False)),
                GovernanceValidationCode.REVIEW_NOT_INDEPENDENT,
            ),
            (
                self.decision(
                    review=self.review(reviewer_role=InstitutionalRole.RESPONSIBLE_IMPLEMENTER)
                ),
                GovernanceValidationCode.REVIEWER_ROLE_INVALID,
            ),
            (
                self.decision(review=self.review(target=self.target(version="1.1"))),
                GovernanceValidationCode.REVIEW_TARGET_MISMATCH,
            ),
            (
                self.decision(review=self.review(reviewed_at=self.now + timedelta(hours=1))),
                GovernanceValidationCode.REVIEW_AFTER_DECISION,
            ),
            (
                self.decision(review=self.review(material_conflict=True)),
                GovernanceValidationCode.REVIEW_CONFLICT,
            ),
            (
                self.decision(
                    review=self.review(recommendation=ReviewRecommendation.DO_NOT_SUPPORT)
                ),
                GovernanceValidationCode.REVIEW_DOES_NOT_SUPPORT_APPROVAL,
            ),
        )
        for decision, expected in cases:
            with self.subTest(expected=expected):
                result = validator.validate(decision)
                self.assertFalse(result.valid)
                self.assertEqual(result.code, expected)

        self_acceptance = GovernanceDecisionValidator(
            AuthorityRegistry((self.assignment(holder="responsible-implementer-reference"),))
        ).validate(
            self.decision(
                decider="responsible-implementer-reference",
                review=self.review(),
            )
        )
        self.assertFalse(self_acceptance.valid)
        self.assertEqual(self_acceptance.code, GovernanceValidationCode.REVIEW_CONFLICT)

    def test_authority_and_control_ownership_expire_fail_closed(self) -> None:
        expiry = self.now + timedelta(hours=1)
        assignment = AuthorityAssignment(
            assignment_reference="expiring-authority-reference",
            holder_reference="project-owner-reference",
            institutional_role=InstitutionalRole.PROJECT_OWNER,
            governed_act=GovernedAct.CHAPTER_SECURITY_ARCHITECTURE_SIGN_OFF,
            target=self.target(),
            effective_from=self.now,
            effective_until=expiry,
        )
        ownership = SecurityControlOwnership(
            control_reference="security-control-reference",
            owner_reference="control-owner-reference",
            owner_role=InstitutionalRole.SECURITY_CONTROL_OWNER,
            target=self.target(),
            effective_from=self.now,
            effective_until=expiry,
        )
        self.assertTrue(assignment.is_current(self.now))
        self.assertTrue(ownership.is_current(self.now))
        self.assertFalse(assignment.is_current(expiry))
        self.assertFalse(ownership.is_current(expiry))
        with self.assertRaises(GovernanceContractError):
            SecurityControlOwnership(
                control_reference="invalid-security-control-reference",
                owner_reference="invalid-control-owner-reference",
                owner_role=InstitutionalRole.RESPONSIBLE_IMPLEMENTER,
                target=self.target(),
                effective_from=self.now,
            )

    def test_governance_times_must_be_timezone_aware(self) -> None:
        with self.assertRaises(GovernanceContractError):
            AuthorityAssignment(
                assignment_reference="authority-assignment-reference",
                holder_reference="project-owner-reference",
                institutional_role=InstitutionalRole.PROJECT_OWNER,
                governed_act=GovernedAct.CHAPTER_SECURITY_ARCHITECTURE_SIGN_OFF,
                target=self.target(),
                effective_from=datetime(2026, 9, 19),
            )


class DevelopmentRiskTests(unittest.TestCase):
    @staticmethod
    def target() -> GovernedTarget:
        return GovernedTarget(
            target_reference="wbs-16-wp-002",
            scope_reference="local-development",
            version="1",
        )

    @classmethod
    def request(
        cls,
        *,
        domain: RiskDomain = RiskDomain.LOCAL_EXPERIMENTATION,
        synthetic_only: bool = True,
        credentials: bool = False,
        external: bool = False,
        cross_border: bool = False,
        exception: bool = False,
    ) -> DevelopmentRiskRequest:
        return DevelopmentRiskRequest(
            risk_reference="synthetic-risk-reference",
            domain=domain,
            target=cls.target(),
            synthetic_or_non_governed_data_only=synthetic_only,
            production_credentials_present=credentials,
            external_activation=external,
            cross_border_transfer=cross_border,
            exception_requested=exception,
        )

    def test_approved_appetite_and_threat_baselines_are_complete(self) -> None:
        self.assertEqual(SECURITY_GOVERNANCE_BASELINE_VERSION, "NCIE-WBS16-WP002-2026-09-19")
        self.assertEqual(
            SECURITY_GOVERNANCE_DECISION_EVIDENCE,
            "NCIE-WBS16-OWNER-DECISION-2026-09-19-011",
        )
        self.assertEqual(len(APPROVED_DEVELOPMENT_RISK_APPETITE), 9)
        self.assertEqual(
            {entry.domain for entry in APPROVED_DEVELOPMENT_RISK_APPETITE}, set(RiskDomain)
        )
        self.assertEqual(len(APPROVED_THREAT_ASSUMPTIONS), 9)
        self.assertEqual(set(APPROVED_THREAT_ASSUMPTIONS), set(ThreatAssumption))
        none_domains = {
            entry.domain
            for entry in APPROVED_DEVELOPMENT_RISK_APPETITE
            if entry.appetite is RiskAppetiteLevel.NONE
        }
        self.assertIn(RiskDomain.HUMAN_AUTHORITY_AND_PROVENANCE, none_domains)
        self.assertIn(RiskDomain.AFRICAN_DATA_RESIDENCY_AND_CROSS_BORDER, none_domains)

    def test_only_bounded_synthetic_local_experiment_is_within_boundary(self) -> None:
        result = DevelopmentRiskEvaluator().evaluate(self.request())
        self.assertTrue(result.within_development_boundary)
        self.assertEqual(result.disposition, RiskEvaluationDisposition.WITHIN_DEVELOPMENT_BOUNDARY)

    def test_governed_data_credentials_external_and_cross_border_paths_are_denied(self) -> None:
        cases = (
            (self.request(synthetic_only=False), "GOVERNED_DATA_EXCLUDED"),
            (self.request(credentials=True), "PRODUCTION_CREDENTIALS_EXCLUDED"),
            (self.request(external=True), "EXTERNAL_ACTIVATION_EXCLUDED"),
            (
                self.request(cross_border=True),
                "CROSS_BORDER_TRANSFER_NOT_AUTHORIZED_IN_WP002",
            ),
        )
        evaluator = DevelopmentRiskEvaluator()
        for request, reason in cases:
            with self.subTest(reason=reason):
                result = evaluator.evaluate(request)
                self.assertFalse(result.within_development_boundary)
                self.assertEqual(result.disposition, RiskEvaluationDisposition.DENY)
                self.assertEqual(result.reason_code, reason)

    def test_no_appetite_risk_is_denied_and_low_risk_requires_treatment(self) -> None:
        evaluator = DevelopmentRiskEvaluator()
        prohibited = evaluator.evaluate(
            self.request(domain=RiskDomain.UNAUTHORIZED_ACCESS_AND_PRIVILEGE)
        )
        low = evaluator.evaluate(self.request(domain=RiskDomain.RESIDUAL_IMPLEMENTATION_RISK))
        self.assertFalse(prohibited.within_development_boundary)
        self.assertEqual(prohibited.reason_code, "NO_RISK_APPETITE")
        self.assertFalse(low.within_development_boundary)
        self.assertEqual(low.disposition, RiskEvaluationDisposition.TREATMENT_REQUIRED)
        self.assertEqual(low.reason_code, "RISK_TREATMENT_REQUIRED_NOT_ACCEPTED")

    def test_exception_and_unknown_domain_stop_for_human_review(self) -> None:
        evaluator = DevelopmentRiskEvaluator()
        exception = evaluator.evaluate(self.request(exception=True))
        unknown_request = self.request()
        object.__setattr__(unknown_request, "domain", cast(RiskDomain, "UNKNOWN"))
        unknown = evaluator.evaluate(unknown_request)
        self.assertEqual(exception.disposition, RiskEvaluationDisposition.STOP_AND_REVIEW)
        self.assertEqual(exception.reason_code, "EXCEPTION_AUTHORITY_UNASSIGNED")
        self.assertEqual(unknown.disposition, RiskEvaluationDisposition.STOP_AND_REVIEW)
        self.assertEqual(unknown.reason_code, "UNKNOWN_RISK_DOMAIN")

    def test_risk_treatment_plan_cannot_claim_permanent_acceptance(self) -> None:
        recorded = datetime(2026, 9, 19, tzinfo=UTC)
        plan = RiskTreatmentPlan(
            plan_reference="risk-treatment-plan-reference",
            risk_reference="risk-reference",
            owner_reference="risk-treatment-owner-reference",
            target=self.target(),
            treatment=RiskTreatment.MITIGATE,
            recorded_at=recorded,
            review_due_at=recorded + timedelta(days=30),
        )
        self.assertEqual(plan.treatment, RiskTreatment.MITIGATE)
        with self.assertRaises(GovernanceContractError):
            RiskTreatmentPlan(
                plan_reference="invalid-risk-treatment-plan",
                risk_reference="risk-reference",
                owner_reference="risk-treatment-owner-reference",
                target=self.target(),
                treatment=RiskTreatment.MONITOR_PENDING_VERIFICATION,
                recorded_at=recorded,
                review_due_at=recorded,
            )


if __name__ == "__main__":
    unittest.main()
