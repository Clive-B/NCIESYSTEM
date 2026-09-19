"""Provider-neutral identity lifecycle, assurance, and session contracts."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from re import compile as compile_pattern
from typing import Final, Protocol

from .security_principals import (
    AuthoritativeSourceCategory,
    PrincipalClass,
    SecurityPrincipal,
    authoritative_source_for,
)

IDENTITY_ASSURANCE_BASELINE_VERSION: Final = "NCIE-WBS16-WP003-2026-09-19"
IDENTITY_ASSURANCE_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-19-014"
IDENTITY_ASSURANCE_IMPLEMENTATION_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-19-015"
_OPAQUE_REFERENCE_PATTERN: Final = compile_pattern(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}")


class IdentityAssuranceContractError(ValueError):
    """Raised without echoing protected values when a contract is invalid."""


def _validate_reference(value: str, label: str) -> None:
    if _OPAQUE_REFERENCE_PATTERN.fullmatch(value) is None:
        raise IdentityAssuranceContractError(f"{label} is invalid")


def _validate_instant(value: datetime, label: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise IdentityAssuranceContractError(f"{label} must include a timezone")


class ProofingState(StrEnum):
    UNBOUND = "UNBOUND"
    SOURCE_ATTESTED = "SOURCE_ATTESTED"
    INSTITUTIONALLY_VERIFIED = "INSTITUTIONALLY_VERIFIED"
    ENHANCED_SENSITIVE = "ENHANCED_SENSITIVE"


class EnrollmentAuthorityClass(StrEnum):
    IDENTITY_LIFECYCLE_APPROVER = "IDENTITY_LIFECYCLE_APPROVER"
    AUTHORITATIVE_SOURCE_OWNER = "AUTHORITATIVE_SOURCE_OWNER"


class IdentityLifecycleState(StrEnum):
    PENDING_ENROLLMENT = "PENDING_ENROLLMENT"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    REACTIVATION_PENDING = "REACTIVATION_PENDING"
    RECOVERY_PENDING = "RECOVERY_PENDING"


class IdentityLifecycleAction(StrEnum):
    ACTIVATE = "ACTIVATE"
    UPDATE = "UPDATE"
    SUSPEND = "SUSPEND"
    TERMINATE = "TERMINATE"
    REQUEST_REACTIVATION = "REQUEST_REACTIVATION"
    REACTIVATE = "REACTIVATE"
    START_RECOVERY = "START_RECOVERY"
    COMPLETE_RECOVERY = "COMPLETE_RECOVERY"
    RECORD_DUPLICATE = "RECORD_DUPLICATE"


class AssuranceState(StrEnum):
    UNVERIFIED = "UNVERIFIED"
    BASELINE = "BASELINE"
    ELEVATED = "ELEVATED"
    RECOVERY_REPROOFED = "RECOVERY_REPROOFED"


class AssuranceContext(StrEnum):
    STANDARD_SESSION = "STANDARD_SESSION"
    PRIVILEGED_ACCESS = "PRIVILEGED_ACCESS"
    BREAK_GLASS = "BREAK_GLASS"
    HIGH_RISK_ACTION = "HIGH_RISK_ACTION"
    POST_RECOVERY = "POST_RECOVERY"


class CredentialReferenceClass(StrEnum):
    HUMAN = "HUMAN"
    WORKLOAD = "WORKLOAD"
    AGENT = "AGENT"
    SERVICE = "SERVICE"
    SESSION_DEVICE = "SESSION_DEVICE"
    PRIVILEGED = "PRIVILEGED"
    VALIDATOR = "VALIDATOR"


class RevocationState(StrEnum):
    CURRENT = "CURRENT"
    REVOKED = "REVOKED"


class RevocationCause(StrEnum):
    IDENTITY_SUSPENDED = "IDENTITY_SUSPENDED"
    IDENTITY_TERMINATED = "IDENTITY_TERMINATED"
    RECOVERY_STARTED = "RECOVERY_STARTED"
    SOURCE_INVALIDATED = "SOURCE_INVALIDATED"
    CREDENTIAL_REVOKED = "CREDENTIAL_REVOKED"


class AssuranceValidationCode(StrEnum):
    VALID = "VALID"
    IDENTITY_NOT_ACTIVE = "IDENTITY_NOT_ACTIVE"
    CREDENTIAL_REVOKED = "CREDENTIAL_REVOKED"
    SESSION_REVOKED = "SESSION_REVOKED"
    CREDENTIAL_EXPIRED = "CREDENTIAL_EXPIRED"
    SESSION_EXPIRED = "SESSION_EXPIRED"
    SESSION_EXCEEDS_CREDENTIAL = "SESSION_EXCEEDS_CREDENTIAL"
    PRINCIPAL_MISMATCH = "PRINCIPAL_MISMATCH"
    CREDENTIAL_BINDING_MISMATCH = "CREDENTIAL_BINDING_MISMATCH"
    CREDENTIAL_ASSURANCE_INSUFFICIENT = "CREDENTIAL_ASSURANCE_INSUFFICIENT"
    AUDIENCE_MISMATCH = "AUDIENCE_MISMATCH"
    SCOPE_MISSING = "SCOPE_MISSING"
    ASSURANCE_INSUFFICIENT = "ASSURANCE_INSUFFICIENT"
    STEP_UP_EVIDENCE_MISSING = "STEP_UP_EVIDENCE_MISSING"
    EMERGENCY_TRIGGER_MISSING = "EMERGENCY_TRIGGER_MISSING"
    FRESHNESS_POLICY_MISSING = "FRESHNESS_POLICY_MISSING"


_PROOFING_REQUIREMENT: Final[dict[PrincipalClass, ProofingState]] = {
    PrincipalClass.HUMAN: ProofingState.INSTITUTIONALLY_VERIFIED,
    PrincipalClass.WORKLOAD: ProofingState.SOURCE_ATTESTED,
    PrincipalClass.AGENT: ProofingState.SOURCE_ATTESTED,
    PrincipalClass.SERVICE: ProofingState.SOURCE_ATTESTED,
    PrincipalClass.SESSION_DEVICE: ProofingState.SOURCE_ATTESTED,
    PrincipalClass.PRIVILEGED: ProofingState.ENHANCED_SENSITIVE,
    PrincipalClass.VALIDATOR: ProofingState.SOURCE_ATTESTED,
}

_ASSURANCE_REQUIREMENT: Final[dict[AssuranceContext, AssuranceState]] = {
    AssuranceContext.STANDARD_SESSION: AssuranceState.BASELINE,
    AssuranceContext.PRIVILEGED_ACCESS: AssuranceState.ELEVATED,
    AssuranceContext.BREAK_GLASS: AssuranceState.ELEVATED,
    AssuranceContext.HIGH_RISK_ACTION: AssuranceState.ELEVATED,
    AssuranceContext.POST_RECOVERY: AssuranceState.RECOVERY_REPROOFED,
}

_ASSURANCE_RANK: Final[dict[AssuranceState, int]] = {
    AssuranceState.UNVERIFIED: 0,
    AssuranceState.BASELINE: 1,
    AssuranceState.ELEVATED: 2,
    AssuranceState.RECOVERY_REPROOFED: 2,
}


def required_proofing_for(principal_class: PrincipalClass) -> ProofingState:
    return _PROOFING_REQUIREMENT[principal_class]


@dataclass(frozen=True, slots=True)
class ProofingRecord:
    record_reference: str
    principal: SecurityPrincipal
    proofing_state: ProofingState
    evidence_references: tuple[str, ...]
    source_owner_reference: str
    recorded_at: datetime
    agent_owner_reference: str | None = None
    purpose_reference: str | None = None
    version_reference: str | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.record_reference, "Proofing record reference")
        _validate_reference(self.source_owner_reference, "Source owner reference")
        _validate_instant(self.recorded_at, "Proofing record time")
        for evidence_reference in self.evidence_references:
            _validate_reference(evidence_reference, "Proofing evidence reference")
        if not self.evidence_references:
            raise IdentityAssuranceContractError("Proofing evidence reference is required")
        if self.proofing_state is not required_proofing_for(self.principal.principal_class):
            raise IdentityAssuranceContractError("Proofing state does not match principal class")
        if self.principal.principal_class is PrincipalClass.AGENT:
            if (
                not self.agent_owner_reference
                or not self.purpose_reference
                or not self.version_reference
            ):
                raise IdentityAssuranceContractError(
                    "Agent proofing requires owner, purpose, and version references"
                )
        if self.principal.principal_class is PrincipalClass.SERVICE and not self.purpose_reference:
            raise IdentityAssuranceContractError("Service proofing requires a purpose reference")
        for optional_reference in (
            self.agent_owner_reference,
            self.purpose_reference,
            self.version_reference,
        ):
            if optional_reference is not None:
                _validate_reference(optional_reference, "Proofing metadata reference")


@dataclass(frozen=True, slots=True)
class LifecycleRequest:
    request_reference: str
    principal: SecurityPrincipal
    current_state: IdentityLifecycleState
    action: IdentityLifecycleAction
    requested_at: datetime
    proofing_record: ProofingRecord | None = None
    recovery_assurance: AssuranceState | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.request_reference, "Lifecycle request reference")
        _validate_instant(self.requested_at, "Lifecycle request time")


@dataclass(frozen=True, slots=True)
class EnrollmentAuthorityDecision:
    approved: bool
    authority_class: EnrollmentAuthorityClass
    decision_reference: str
    authority_holder_reference: str

    def __post_init__(self) -> None:
        _validate_reference(self.decision_reference, "Enrollment decision reference")
        _validate_reference(self.authority_holder_reference, "Authority holder reference")


class EnrollmentAuthorityBoundary(Protocol):
    def decide(self, request: LifecycleRequest) -> EnrollmentAuthorityDecision | None:
        """Return an explicit current decision or fail closed with no decision."""


class UnassignedEnrollmentAuthority:
    """No operational holders are assigned by W16-D8-A."""

    def decide(self, request: LifecycleRequest) -> EnrollmentAuthorityDecision | None:
        del request
        return None


@dataclass(frozen=True, slots=True)
class LifecycleResult:
    allowed: bool
    resulting_state: IdentityLifecycleState
    reason_code: str
    invalidate_prior_sessions: bool = False
    requires_new_assurance: bool = False
    restores_prior_privilege: bool = False
    human_review_required: bool = False


class IdentityLifecycleCoordinator:
    """Validate lifecycle transitions without performing provider operations."""

    _authority_actions: Final = frozenset(
        {
            IdentityLifecycleAction.ACTIVATE,
            IdentityLifecycleAction.REACTIVATE,
            IdentityLifecycleAction.COMPLETE_RECOVERY,
        }
    )

    def __init__(self, authority: EnrollmentAuthorityBoundary) -> None:
        self._authority = authority

    def evaluate(self, request: LifecycleRequest) -> LifecycleResult:
        if request.action is IdentityLifecycleAction.RECORD_DUPLICATE:
            return LifecycleResult(
                False,
                request.current_state,
                "DUPLICATE_REQUIRES_HUMAN_REVIEW_NO_AUTOMERGE",
                human_review_required=True,
            )
        transitions: dict[
            tuple[IdentityLifecycleState, IdentityLifecycleAction], IdentityLifecycleState
        ] = {
            (IdentityLifecycleState.PENDING_ENROLLMENT, IdentityLifecycleAction.ACTIVATE): (
                IdentityLifecycleState.ACTIVE
            ),
            (IdentityLifecycleState.ACTIVE, IdentityLifecycleAction.UPDATE): (
                IdentityLifecycleState.ACTIVE
            ),
            (IdentityLifecycleState.ACTIVE, IdentityLifecycleAction.SUSPEND): (
                IdentityLifecycleState.SUSPENDED
            ),
            (IdentityLifecycleState.ACTIVE, IdentityLifecycleAction.TERMINATE): (
                IdentityLifecycleState.TERMINATED
            ),
            (IdentityLifecycleState.SUSPENDED, IdentityLifecycleAction.REQUEST_REACTIVATION): (
                IdentityLifecycleState.REACTIVATION_PENDING
            ),
            (IdentityLifecycleState.REACTIVATION_PENDING, IdentityLifecycleAction.REACTIVATE): (
                IdentityLifecycleState.ACTIVE
            ),
            (IdentityLifecycleState.ACTIVE, IdentityLifecycleAction.START_RECOVERY): (
                IdentityLifecycleState.RECOVERY_PENDING
            ),
            (IdentityLifecycleState.RECOVERY_PENDING, IdentityLifecycleAction.COMPLETE_RECOVERY): (
                IdentityLifecycleState.ACTIVE
            ),
        }
        destination = transitions.get((request.current_state, request.action))
        if destination is None:
            return LifecycleResult(False, request.current_state, "INVALID_LIFECYCLE_TRANSITION")
        if request.action in self._authority_actions:
            if request.proofing_record is None:
                return LifecycleResult(False, request.current_state, "PROOFING_RECORD_REQUIRED")
            if request.proofing_record.principal != request.principal:
                return LifecycleResult(False, request.current_state, "PROOFING_PRINCIPAL_MISMATCH")
            decision = self._authority.decide(request)
            if decision is None or not decision.approved:
                return LifecycleResult(False, request.current_state, "CURRENT_AUTHORITY_REQUIRED")
        if (
            request.action is IdentityLifecycleAction.COMPLETE_RECOVERY
            and request.recovery_assurance is not AssuranceState.RECOVERY_REPROOFED
        ):
            return LifecycleResult(False, request.current_state, "RECOVERY_REPROOFING_REQUIRED")
        invalidate = request.action in {
            IdentityLifecycleAction.SUSPEND,
            IdentityLifecycleAction.TERMINATE,
            IdentityLifecycleAction.REACTIVATE,
            IdentityLifecycleAction.START_RECOVERY,
            IdentityLifecycleAction.COMPLETE_RECOVERY,
        }
        requires_new_assurance = request.action in {
            IdentityLifecycleAction.REACTIVATE,
            IdentityLifecycleAction.COMPLETE_RECOVERY,
        }
        return LifecycleResult(
            True,
            destination,
            "VALID",
            invalidate_prior_sessions=invalidate,
            requires_new_assurance=requires_new_assurance,
        )


@dataclass(frozen=True, slots=True)
class CredentialReferenceMetadata:
    credential_reference: str
    credential_class: CredentialReferenceClass
    principal: SecurityPrincipal
    scopes: tuple[str, ...]
    audiences: tuple[str, ...]
    issued_at: datetime
    expires_at: datetime
    assurance_state: AssuranceState
    policy_version: str
    duration_policy_reference: str
    revocation_state: RevocationState = RevocationState.CURRENT

    def __post_init__(self) -> None:
        _validate_reference(self.credential_reference, "Credential reference")
        if self.credential_class.value != self.principal.principal_class.value:
            raise IdentityAssuranceContractError("Credential class does not match principal class")
        _validate_bounded_metadata(
            self.scopes,
            self.audiences,
            self.issued_at,
            self.expires_at,
            self.policy_version,
            self.duration_policy_reference,
        )


@dataclass(frozen=True, slots=True)
class SessionMetadata:
    session_reference: str
    base_principal: SecurityPrincipal
    issuer_source: AuthoritativeSourceCategory
    scopes: tuple[str, ...]
    audiences: tuple[str, ...]
    issued_at: datetime
    expires_at: datetime
    assurance_state: AssuranceState
    policy_version: str
    duration_policy_reference: str
    credential_reference: str
    binding_reference: str
    replay_policy_reference: str
    revocation_state: RevocationState = RevocationState.CURRENT

    def __post_init__(self) -> None:
        _validate_reference(self.session_reference, "Session reference")
        _validate_reference(self.credential_reference, "Credential reference")
        _validate_reference(self.binding_reference, "Session binding reference")
        _validate_reference(self.replay_policy_reference, "Replay policy reference")
        if self.issuer_source is not AuthoritativeSourceCategory.AUTHENTICATION_SESSION_ISSUER:
            raise IdentityAssuranceContractError("Session issuer source is invalid")
        _validate_bounded_metadata(
            self.scopes,
            self.audiences,
            self.issued_at,
            self.expires_at,
            self.policy_version,
            self.duration_policy_reference,
        )


def _validate_bounded_metadata(
    scopes: tuple[str, ...],
    audiences: tuple[str, ...],
    issued_at: datetime,
    expires_at: datetime,
    policy_version: str,
    duration_policy_reference: str,
) -> None:
    if not scopes or not audiences:
        raise IdentityAssuranceContractError("Explicit scope and audience are required")
    for reference in (*scopes, *audiences):
        _validate_reference(reference, "Scope or audience reference")
    _validate_instant(issued_at, "Issue time")
    _validate_instant(expires_at, "Expiry time")
    if expires_at <= issued_at:
        raise IdentityAssuranceContractError("Explicit expiry must follow issue time")
    _validate_reference(policy_version, "Policy version")
    _validate_reference(duration_policy_reference, "Duration policy reference")


class SessionIssuerBoundary(Protocol):
    def issue(
        self,
        *,
        principal: SecurityPrincipal,
        credential: CredentialReferenceMetadata,
    ) -> SessionMetadata | None:
        """Return bounded metadata only; concrete issuance remains deferred."""


class UnboundSessionIssuer:
    """Fail closed while provider, factor, duration, and issuer choices are deferred."""

    def issue(
        self,
        *,
        principal: SecurityPrincipal,
        credential: CredentialReferenceMetadata,
    ) -> SessionMetadata | None:
        del principal, credential
        return None


@dataclass(frozen=True, slots=True)
class AssuranceRequest:
    context: AssuranceContext
    audience: str
    required_scope: str
    evaluated_at: datetime
    step_up_evidence_reference: str | None = None
    emergency_trigger_reference: str | None = None
    freshness_policy_reference: str | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.audience, "Audience")
        _validate_reference(self.required_scope, "Required scope")
        _validate_instant(self.evaluated_at, "Assurance evaluation time")
        for reference in (
            self.step_up_evidence_reference,
            self.emergency_trigger_reference,
            self.freshness_policy_reference,
        ):
            if reference is not None:
                _validate_reference(reference, "Assurance evidence reference")


@dataclass(frozen=True, slots=True)
class AssuranceValidationResult:
    valid: bool
    code: AssuranceValidationCode
    authorizes_action: bool = False


class AssuranceEvaluator:
    """Validate authentication/session assurance; never authorize an action."""

    def evaluate(
        self,
        *,
        lifecycle_state: IdentityLifecycleState,
        credential: CredentialReferenceMetadata,
        session: SessionMetadata,
        request: AssuranceRequest,
    ) -> AssuranceValidationResult:
        checks = (
            (
                lifecycle_state is not IdentityLifecycleState.ACTIVE,
                AssuranceValidationCode.IDENTITY_NOT_ACTIVE,
            ),
            (
                credential.revocation_state is RevocationState.REVOKED,
                AssuranceValidationCode.CREDENTIAL_REVOKED,
            ),
            (
                session.revocation_state is RevocationState.REVOKED,
                AssuranceValidationCode.SESSION_REVOKED,
            ),
            (
                request.evaluated_at >= credential.expires_at,
                AssuranceValidationCode.CREDENTIAL_EXPIRED,
            ),
            (
                request.evaluated_at >= session.expires_at,
                AssuranceValidationCode.SESSION_EXPIRED,
            ),
            (
                session.expires_at > credential.expires_at,
                AssuranceValidationCode.SESSION_EXCEEDS_CREDENTIAL,
            ),
            (
                session.base_principal != credential.principal,
                AssuranceValidationCode.PRINCIPAL_MISMATCH,
            ),
            (
                session.credential_reference != credential.credential_reference,
                AssuranceValidationCode.CREDENTIAL_BINDING_MISMATCH,
            ),
            (
                _ASSURANCE_RANK[credential.assurance_state]
                < _ASSURANCE_RANK[session.assurance_state],
                AssuranceValidationCode.CREDENTIAL_ASSURANCE_INSUFFICIENT,
            ),
            (
                request.audience not in session.audiences
                or request.audience not in credential.audiences,
                AssuranceValidationCode.AUDIENCE_MISMATCH,
            ),
            (
                request.required_scope not in session.scopes
                or request.required_scope not in credential.scopes,
                AssuranceValidationCode.SCOPE_MISSING,
            ),
        )
        for failed, code in checks:
            if failed:
                return AssuranceValidationResult(False, code)
        required = _ASSURANCE_REQUIREMENT[request.context]
        if (
            request.context is AssuranceContext.POST_RECOVERY
            and session.assurance_state is not AssuranceState.RECOVERY_REPROOFED
        ) or _ASSURANCE_RANK[session.assurance_state] < _ASSURANCE_RANK[required]:
            return AssuranceValidationResult(False, AssuranceValidationCode.ASSURANCE_INSUFFICIENT)
        if (
            request.context
            in {
                AssuranceContext.PRIVILEGED_ACCESS,
                AssuranceContext.BREAK_GLASS,
                AssuranceContext.HIGH_RISK_ACTION,
            }
            and request.step_up_evidence_reference is None
        ):
            return AssuranceValidationResult(
                False, AssuranceValidationCode.STEP_UP_EVIDENCE_MISSING
            )
        if (
            request.context is AssuranceContext.BREAK_GLASS
            and request.emergency_trigger_reference is None
        ):
            return AssuranceValidationResult(
                False, AssuranceValidationCode.EMERGENCY_TRIGGER_MISSING
            )
        if (
            request.context is AssuranceContext.HIGH_RISK_ACTION
            and request.freshness_policy_reference is None
        ):
            return AssuranceValidationResult(
                False, AssuranceValidationCode.FRESHNESS_POLICY_MISSING
            )
        return AssuranceValidationResult(True, AssuranceValidationCode.VALID)


@dataclass(frozen=True, slots=True)
class RevocationDirective:
    directive_reference: str
    principal_reference: str
    cause: RevocationCause
    effective_at: datetime
    session_references: tuple[str, ...]
    token_references: tuple[str, ...]
    cache_references: tuple[str, ...]

    def __post_init__(self) -> None:
        _validate_reference(self.directive_reference, "Revocation directive reference")
        _validate_reference(self.principal_reference, "Principal reference")
        _validate_instant(self.effective_at, "Revocation effective time")
        if not self.session_references or not self.token_references or not self.cache_references:
            raise IdentityAssuranceContractError(
                "Revocation must address sessions, tokens, and caches"
            )
        for reference in (
            *self.session_references,
            *self.token_references,
            *self.cache_references,
        ):
            _validate_reference(reference, "Revocation target reference")


def validate_session_derivation(
    session_principal: SecurityPrincipal, base_principal: SecurityPrincipal
) -> bool:
    """Session/device identities are usable only as derivatives of a base identity."""

    return (
        session_principal.principal_class is PrincipalClass.SESSION_DEVICE
        and session_principal.source_category
        is authoritative_source_for(PrincipalClass.SESSION_DEVICE)
        and base_principal.principal_class is not PrincipalClass.SESSION_DEVICE
    )
