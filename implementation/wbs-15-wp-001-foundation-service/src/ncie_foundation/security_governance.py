"""Provider-neutral WBS-16 security governance and development-risk contracts."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Final

SECURITY_GOVERNANCE_BASELINE_VERSION: Final = "NCIE-WBS16-WP002-2026-09-19"
SECURITY_GOVERNANCE_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-19-011"


class GovernanceContractError(ValueError):
    """Raised without echoing protected values when a governance contract is invalid."""


def _validate_reference(value: str, label: str) -> None:
    if not value.strip() or len(value) > 128 or any(ord(character) < 32 for character in value):
        raise GovernanceContractError(f"{label} is invalid")


def _validate_instant(value: datetime, label: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise GovernanceContractError(f"{label} must include a timezone")


class GovernedAct(StrEnum):
    CHAPTER_SECURITY_ARCHITECTURE_SIGN_OFF = "CHAPTER_SECURITY_ARCHITECTURE_SIGN_OFF"
    NCIE009_DEVELOPMENT_SPECIFICATION_ACCEPTANCE = "NCIE009_DEVELOPMENT_SPECIFICATION_ACCEPTANCE"
    WBS16_IMPLEMENTATION_COMPLETION = "WBS16_IMPLEMENTATION_COMPLETION"


class InstitutionalRole(StrEnum):
    PROJECT_OWNER = "PROJECT_OWNER"
    SECURITY_ARCHITECTURE_REVIEWER = "SECURITY_ARCHITECTURE_REVIEWER"
    RESPONSIBLE_IMPLEMENTER = "RESPONSIBLE_IMPLEMENTER"
    SECURITY_CONTROL_OWNER = "SECURITY_CONTROL_OWNER"


class GovernanceDecision(StrEnum):
    APPROVE = "APPROVE"
    CONDITIONALLY_APPROVE = "CONDITIONALLY_APPROVE"
    REJECT = "REJECT"
    RETURN_FOR_WORK = "RETURN_FOR_WORK"


class ReviewRecommendation(StrEnum):
    SUPPORT = "SUPPORT"
    DO_NOT_SUPPORT = "DO_NOT_SUPPORT"
    RETURN_FOR_WORK = "RETURN_FOR_WORK"


class GovernanceValidationCode(StrEnum):
    VALID = "VALID"
    NO_CURRENT_AUTHORITY = "NO_CURRENT_AUTHORITY"
    MULTIPLE_CURRENT_AUTHORITIES = "MULTIPLE_CURRENT_AUTHORITIES"
    WRONG_AUTHORITY_ROLE = "WRONG_AUTHORITY_ROLE"
    DECIDER_NOT_CURRENT_AUTHORITY = "DECIDER_NOT_CURRENT_AUTHORITY"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    REVIEWER_ROLE_INVALID = "REVIEWER_ROLE_INVALID"
    REVIEW_TARGET_MISMATCH = "REVIEW_TARGET_MISMATCH"
    REVIEW_NOT_INDEPENDENT = "REVIEW_NOT_INDEPENDENT"
    REVIEW_CONFLICT = "REVIEW_CONFLICT"
    REVIEW_AFTER_DECISION = "REVIEW_AFTER_DECISION"
    REVIEW_DOES_NOT_SUPPORT_APPROVAL = "REVIEW_DOES_NOT_SUPPORT_APPROVAL"


@dataclass(frozen=True, slots=True)
class GovernedTarget:
    target_reference: str
    scope_reference: str
    version: str

    def __post_init__(self) -> None:
        _validate_reference(self.target_reference, "Target reference")
        _validate_reference(self.scope_reference, "Scope reference")
        _validate_reference(self.version, "Target version")


@dataclass(frozen=True, slots=True)
class AuthorityAssignment:
    assignment_reference: str
    holder_reference: str
    institutional_role: InstitutionalRole
    governed_act: GovernedAct
    target: GovernedTarget
    effective_from: datetime
    effective_until: datetime | None = None
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.assignment_reference, "Assignment reference")
        _validate_reference(self.holder_reference, "Authority holder reference")
        _validate_instant(self.effective_from, "Effective-from time")
        if self.effective_until is not None:
            _validate_instant(self.effective_until, "Effective-until time")
            if self.effective_until <= self.effective_from:
                raise GovernanceContractError("Authority expiry must follow its effective time")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Revocation time")
            if self.revoked_at < self.effective_from:
                raise GovernanceContractError("Authority cannot be revoked before it is effective")

    def is_current(self, at: datetime) -> bool:
        _validate_instant(at, "Authority evaluation time")
        if at < self.effective_from:
            return False
        if self.effective_until is not None and at >= self.effective_until:
            return False
        return self.revoked_at is None or at < self.revoked_at


@dataclass(frozen=True, slots=True)
class SecurityArchitectureReview:
    review_reference: str
    reviewer_reference: str
    reviewer_role: InstitutionalRole
    target: GovernedTarget
    reviewed_at: datetime
    recommendation: ReviewRecommendation
    author_or_implementer_references: tuple[str, ...]
    independent: bool
    material_conflict: bool

    def __post_init__(self) -> None:
        _validate_reference(self.review_reference, "Review reference")
        _validate_reference(self.reviewer_reference, "Reviewer reference")
        _validate_instant(self.reviewed_at, "Review time")
        for actor_reference in self.author_or_implementer_references:
            _validate_reference(actor_reference, "Author or implementer reference")


@dataclass(frozen=True, slots=True)
class GovernanceDecisionRecord:
    decision_reference: str
    governed_act: GovernedAct
    target: GovernedTarget
    decision: GovernanceDecision
    decider_reference: str
    decided_at: datetime
    review: SecurityArchitectureReview | None

    def __post_init__(self) -> None:
        _validate_reference(self.decision_reference, "Decision reference")
        _validate_reference(self.decider_reference, "Decider reference")
        _validate_instant(self.decided_at, "Decision time")


@dataclass(frozen=True, slots=True)
class GovernanceValidationResult:
    valid: bool
    code: GovernanceValidationCode


class AuthorityRegistry:
    """Immutable local view of authority assignments; it grants no authority itself."""

    def __init__(self, assignments: tuple[AuthorityAssignment, ...]) -> None:
        self._assignments = assignments

    def current_for(
        self,
        *,
        governed_act: GovernedAct,
        target: GovernedTarget,
        at: datetime,
    ) -> tuple[AuthorityAssignment, ...]:
        return tuple(
            assignment
            for assignment in self._assignments
            if assignment.governed_act is governed_act
            and assignment.target == target
            and assignment.is_current(at)
        )


class GovernanceDecisionValidator:
    """Validate recorded authority and independent review without accepting a target."""

    def __init__(self, registry: AuthorityRegistry) -> None:
        self._registry = registry

    def validate(self, record: GovernanceDecisionRecord) -> GovernanceValidationResult:
        authorities = self._registry.current_for(
            governed_act=record.governed_act,
            target=record.target,
            at=record.decided_at,
        )
        if not authorities:
            return GovernanceValidationResult(False, GovernanceValidationCode.NO_CURRENT_AUTHORITY)
        if len(authorities) != 1:
            return GovernanceValidationResult(
                False, GovernanceValidationCode.MULTIPLE_CURRENT_AUTHORITIES
            )
        authority = authorities[0]
        if authority.institutional_role is not InstitutionalRole.PROJECT_OWNER:
            return GovernanceValidationResult(False, GovernanceValidationCode.WRONG_AUTHORITY_ROLE)
        if authority.holder_reference != record.decider_reference:
            return GovernanceValidationResult(
                False, GovernanceValidationCode.DECIDER_NOT_CURRENT_AUTHORITY
            )
        review = record.review
        if review is None:
            return GovernanceValidationResult(False, GovernanceValidationCode.REVIEW_REQUIRED)
        if review.reviewer_role is not InstitutionalRole.SECURITY_ARCHITECTURE_REVIEWER:
            return GovernanceValidationResult(False, GovernanceValidationCode.REVIEWER_ROLE_INVALID)
        if review.target != record.target:
            return GovernanceValidationResult(
                False, GovernanceValidationCode.REVIEW_TARGET_MISMATCH
            )
        if not review.independent:
            return GovernanceValidationResult(
                False, GovernanceValidationCode.REVIEW_NOT_INDEPENDENT
            )
        if (
            review.material_conflict
            or review.reviewer_reference == record.decider_reference
            or review.reviewer_reference in review.author_or_implementer_references
            or record.decider_reference in review.author_or_implementer_references
        ):
            return GovernanceValidationResult(False, GovernanceValidationCode.REVIEW_CONFLICT)
        if review.reviewed_at > record.decided_at:
            return GovernanceValidationResult(False, GovernanceValidationCode.REVIEW_AFTER_DECISION)
        if (
            record.decision
            in (GovernanceDecision.APPROVE, GovernanceDecision.CONDITIONALLY_APPROVE)
            and review.recommendation is not ReviewRecommendation.SUPPORT
        ):
            return GovernanceValidationResult(
                False, GovernanceValidationCode.REVIEW_DOES_NOT_SUPPORT_APPROVAL
            )
        return GovernanceValidationResult(True, GovernanceValidationCode.VALID)


@dataclass(frozen=True, slots=True)
class SecurityControlOwnership:
    control_reference: str
    owner_reference: str
    owner_role: InstitutionalRole
    target: GovernedTarget
    effective_from: datetime
    effective_until: datetime | None = None
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.control_reference, "Security control reference")
        _validate_reference(self.owner_reference, "Security control owner reference")
        if self.owner_role is not InstitutionalRole.SECURITY_CONTROL_OWNER:
            raise GovernanceContractError("Security control owner role is invalid")
        _validate_instant(self.effective_from, "Control ownership effective time")
        if self.effective_until is not None:
            _validate_instant(self.effective_until, "Control ownership expiry")
            if self.effective_until <= self.effective_from:
                raise GovernanceContractError("Control ownership expiry must follow effective time")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Control ownership revocation time")
            if self.revoked_at < self.effective_from:
                raise GovernanceContractError(
                    "Control ownership cannot be revoked before it is effective"
                )

    def is_current(self, at: datetime) -> bool:
        _validate_instant(at, "Control ownership evaluation time")
        if at < self.effective_from:
            return False
        if self.effective_until is not None and at >= self.effective_until:
            return False
        return self.revoked_at is None or at < self.revoked_at


class RiskDomain(StrEnum):
    HUMAN_AUTHORITY_AND_PROVENANCE = "HUMAN_AUTHORITY_AND_PROVENANCE"
    UNAUTHORIZED_ACCESS_AND_PRIVILEGE = "UNAUTHORIZED_ACCESS_AND_PRIVILEGE"
    PROTECTED_DATA_OR_SECRET_DISCLOSURE = "PROTECTED_DATA_OR_SECRET_DISCLOSURE"
    AFRICAN_DATA_RESIDENCY_AND_CROSS_BORDER = "AFRICAN_DATA_RESIDENCY_AND_CROSS_BORDER"
    SUPPLY_CHAIN_AND_ARTIFACT_INTEGRITY = "SUPPLY_CHAIN_AND_ARTIFACT_INTEGRITY"
    SECURITY_CONTROL_BYPASS = "SECURITY_CONTROL_BYPASS"
    AVAILABILITY_AND_DELIVERY_CONTINUITY = "AVAILABILITY_AND_DELIVERY_CONTINUITY"
    LOCAL_EXPERIMENTATION = "LOCAL_EXPERIMENTATION"
    RESIDUAL_IMPLEMENTATION_RISK = "RESIDUAL_IMPLEMENTATION_RISK"


class RiskAppetiteLevel(StrEnum):
    NONE = "NONE"
    LOW = "LOW"
    LIMITED = "LIMITED"


@dataclass(frozen=True, slots=True)
class RiskAppetiteEntry:
    domain: RiskDomain
    appetite: RiskAppetiteLevel
    interim_response: str

    def __post_init__(self) -> None:
        _validate_reference(self.interim_response, "Interim risk response")


APPROVED_DEVELOPMENT_RISK_APPETITE: Final[tuple[RiskAppetiteEntry, ...]] = (
    RiskAppetiteEntry(
        RiskDomain.HUMAN_AUTHORITY_AND_PROVENANCE, RiskAppetiteLevel.NONE, "DENY_OR_STOP"
    ),
    RiskAppetiteEntry(
        RiskDomain.UNAUTHORIZED_ACCESS_AND_PRIVILEGE, RiskAppetiteLevel.NONE, "ZERO_GRANTS"
    ),
    RiskAppetiteEntry(
        RiskDomain.PROTECTED_DATA_OR_SECRET_DISCLOSURE,
        RiskAppetiteLevel.NONE,
        "ISOLATE_MINIMIZE_DENY",
    ),
    RiskAppetiteEntry(
        RiskDomain.AFRICAN_DATA_RESIDENCY_AND_CROSS_BORDER,
        RiskAppetiteLevel.NONE,
        "DENY_UNAPPROVED_TRANSFER",
    ),
    RiskAppetiteEntry(
        RiskDomain.SUPPLY_CHAIN_AND_ARTIFACT_INTEGRITY,
        RiskAppetiteLevel.NONE,
        "QUARANTINE_OR_REJECT",
    ),
    RiskAppetiteEntry(
        RiskDomain.SECURITY_CONTROL_BYPASS, RiskAppetiteLevel.NONE, "STOP_FOR_HUMAN_DECISION"
    ),
    RiskAppetiteEntry(
        RiskDomain.AVAILABILITY_AND_DELIVERY_CONTINUITY, RiskAppetiteLevel.LOW, "SAFE_DEGRADATION"
    ),
    RiskAppetiteEntry(
        RiskDomain.LOCAL_EXPERIMENTATION,
        RiskAppetiteLevel.LIMITED,
        "SYNTHETIC_ISOLATED_NON_PRODUCTION",
    ),
    RiskAppetiteEntry(
        RiskDomain.RESIDUAL_IMPLEMENTATION_RISK, RiskAppetiteLevel.LOW, "RECORD_TREAT_AND_VERIFY"
    ),
)


class ThreatAssumption(StrEnum):
    NO_PLACEMENT_OR_PRIOR_SUCCESS_TRUST = "NO_PLACEMENT_OR_PRIOR_SUCCESS_TRUST"
    EXTERNAL_CREDENTIAL_INSIDER_AND_THIRD_PARTY_THREATS = (
        "EXTERNAL_CREDENTIAL_INSIDER_AND_THIRD_PARTY_THREATS"
    )
    AGENT_MODEL_TOOL_MANIPULATION = "AGENT_MODEL_TOOL_MANIPULATION"
    CURRENT_SECURITY_STATE_CAN_CHANGE = "CURRENT_SECURITY_STATE_CAN_CHANGE"
    CROSS_CONTEXT_PATHS_ARE_HOSTILE = "CROSS_CONTEXT_PATHS_ARE_HOSTILE"
    SUPPLY_CHAIN_AND_RECOVERY_MAY_BE_COMPROMISED = "SUPPLY_CHAIN_AND_RECOVERY_MAY_BE_COMPROMISED"
    UNKNOWN_SECURITY_STATE_FAILS_CLOSED = "UNKNOWN_SECURITY_STATE_FAILS_CLOSED"
    LOCAL_TEST_IS_NOT_SECURITY_ACCEPTANCE = "LOCAL_TEST_IS_NOT_SECURITY_ACCEPTANCE"
    OPERATIONAL_ASSUMPTIONS_REQUIRE_LATER_VALIDATION = (
        "OPERATIONAL_ASSUMPTIONS_REQUIRE_LATER_VALIDATION"
    )


APPROVED_THREAT_ASSUMPTIONS: Final[tuple[ThreatAssumption, ...]] = tuple(ThreatAssumption)


class RiskEvaluationDisposition(StrEnum):
    WITHIN_DEVELOPMENT_BOUNDARY = "WITHIN_DEVELOPMENT_BOUNDARY"
    DENY = "DENY"
    STOP_AND_REVIEW = "STOP_AND_REVIEW"
    TREATMENT_REQUIRED = "TREATMENT_REQUIRED"


@dataclass(frozen=True, slots=True)
class DevelopmentRiskRequest:
    risk_reference: str
    domain: RiskDomain
    target: GovernedTarget
    synthetic_or_non_governed_data_only: bool
    production_credentials_present: bool
    external_activation: bool
    cross_border_transfer: bool
    exception_requested: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.risk_reference, "Risk reference")


@dataclass(frozen=True, slots=True)
class RiskEvaluationResult:
    within_development_boundary: bool
    disposition: RiskEvaluationDisposition
    reason_code: str


class DevelopmentRiskEvaluator:
    """Evaluate only the approved local-development boundary; never accept residual risk."""

    def evaluate(self, request: DevelopmentRiskRequest) -> RiskEvaluationResult:
        if request.exception_requested:
            return RiskEvaluationResult(
                False, RiskEvaluationDisposition.STOP_AND_REVIEW, "EXCEPTION_AUTHORITY_UNASSIGNED"
            )
        if request.cross_border_transfer:
            return RiskEvaluationResult(
                False,
                RiskEvaluationDisposition.DENY,
                "CROSS_BORDER_TRANSFER_NOT_AUTHORIZED_IN_WP002",
            )
        if request.production_credentials_present:
            return RiskEvaluationResult(
                False, RiskEvaluationDisposition.DENY, "PRODUCTION_CREDENTIALS_EXCLUDED"
            )
        if request.external_activation:
            return RiskEvaluationResult(
                False, RiskEvaluationDisposition.DENY, "EXTERNAL_ACTIVATION_EXCLUDED"
            )
        if not isinstance(request.domain, RiskDomain):
            return RiskEvaluationResult(
                False, RiskEvaluationDisposition.STOP_AND_REVIEW, "UNKNOWN_RISK_DOMAIN"
            )
        if request.domain is RiskDomain.LOCAL_EXPERIMENTATION:
            if not request.synthetic_or_non_governed_data_only:
                return RiskEvaluationResult(
                    False, RiskEvaluationDisposition.DENY, "GOVERNED_DATA_EXCLUDED"
                )
            return RiskEvaluationResult(
                True,
                RiskEvaluationDisposition.WITHIN_DEVELOPMENT_BOUNDARY,
                "BOUNDED_LOCAL_EXPERIMENT",
            )
        appetite = next(
            entry.appetite
            for entry in APPROVED_DEVELOPMENT_RISK_APPETITE
            if entry.domain is request.domain
        )
        if appetite is RiskAppetiteLevel.NONE:
            return RiskEvaluationResult(False, RiskEvaluationDisposition.DENY, "NO_RISK_APPETITE")
        return RiskEvaluationResult(
            False,
            RiskEvaluationDisposition.TREATMENT_REQUIRED,
            "RISK_TREATMENT_REQUIRED_NOT_ACCEPTED",
        )


class RiskTreatment(StrEnum):
    AVOID = "AVOID"
    MITIGATE = "MITIGATE"
    MONITOR_PENDING_VERIFICATION = "MONITOR_PENDING_VERIFICATION"


@dataclass(frozen=True, slots=True)
class RiskTreatmentPlan:
    plan_reference: str
    risk_reference: str
    owner_reference: str
    target: GovernedTarget
    treatment: RiskTreatment
    recorded_at: datetime
    review_due_at: datetime

    def __post_init__(self) -> None:
        _validate_reference(self.plan_reference, "Risk treatment plan reference")
        _validate_reference(self.risk_reference, "Risk reference")
        _validate_reference(self.owner_reference, "Risk treatment owner reference")
        _validate_instant(self.recorded_at, "Risk treatment record time")
        _validate_instant(self.review_due_at, "Risk treatment review time")
        if self.review_due_at <= self.recorded_at:
            raise GovernanceContractError("Risk treatment review must follow its record time")
