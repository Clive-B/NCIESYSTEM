"""Provider-neutral WP-004 mapping, delegation, privilege, and emergency contracts."""

from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from re import compile as compile_pattern
from typing import Final, Protocol

from .identity_assurance import AssuranceState
from .observability import ObservabilitySink, OperationalEvent, SignalCategory
from .security_authorization import (
    ALL_AUTHORIZATION_DIMENSIONS,
    AuthorizationEffect,
    CurrentAuthorizationDecision,
    CurrentAuthorizationRequest,
)
from .security_principals import PrincipalClass, SecurityPrincipal

ACCESS_CONTROL_BASELINE_VERSION: Final = "NCIE-WBS16-WP004-2026-09-23"
ACCESS_CONTROL_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-23-017"
ACCESS_CONTROL_IMPLEMENTATION_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-23-018"

_REFERENCE_PATTERN: Final = compile_pattern(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}")
_PROTECTED_REFERENCE_FRAGMENTS: Final = (
    "password",
    "secret",
    "credential_value",
    "token_value",
    "private_key",
)


class AccessControlContractError(ValueError):
    """Raised without echoing protected values when a WP-004 contract is invalid."""


def _validate_reference(value: str, label: str) -> None:
    if _REFERENCE_PATTERN.fullmatch(value) is None:
        raise AccessControlContractError(f"{label} is invalid")
    normalized = value.lower()
    if any(fragment in normalized for fragment in _PROTECTED_REFERENCE_FRAGMENTS):
        raise AccessControlContractError(f"{label} may not contain protected material")


def _validate_optional_reference(value: str | None, label: str) -> None:
    if value is not None:
        _validate_reference(value, label)


def _validate_instant(value: datetime, label: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise AccessControlContractError(f"{label} must include a timezone")


def _validate_window(starts_at: datetime, expires_at: datetime, label: str) -> None:
    _validate_instant(starts_at, f"{label} start")
    _validate_instant(expires_at, f"{label} expiry")
    if expires_at <= starts_at:
        raise AccessControlContractError(f"{label} expiry must follow its start")


def _validate_references(values: tuple[str, ...], label: str, *, required: bool = True) -> None:
    if required and not values:
        raise AccessControlContractError(f"{label} is required")
    if len(values) != len(set(values)):
        raise AccessControlContractError(f"{label} must not contain duplicates")
    for value in values:
        _validate_reference(value, label)


class MappingSubjectKind(StrEnum):
    ROLE = "ROLE"
    ATTRIBUTE = "ATTRIBUTE"


@dataclass(frozen=True, slots=True)
class AuthorizationMapping:
    """A version-bound grant shape; construction is not institutional assignment."""

    mapping_reference: str
    subject_kind: MappingSubjectKind
    subject_reference: str
    object_reference: str
    field_references: tuple[str, ...]
    action_reference: str
    purpose_reference: str
    classification_reference: str
    required_policy_attributes: tuple[tuple[str, str], ...]
    policy_version: str
    effective_from: datetime
    expires_at: datetime
    approval_decision_reference: str
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.mapping_reference, "Mapping reference"),
            (self.subject_reference, "Mapping subject reference"),
            (self.object_reference, "Mapping object reference"),
            (self.action_reference, "Mapping action reference"),
            (self.purpose_reference, "Mapping purpose reference"),
            (self.classification_reference, "Mapping classification reference"),
            (self.policy_version, "Mapping policy version"),
            (self.approval_decision_reference, "Mapping approval decision reference"),
        ):
            _validate_reference(value, label)
        _validate_references(self.field_references, "Mapping field reference", required=False)
        for key, value in self.required_policy_attributes:
            _validate_reference(key, "Required policy attribute name")
            _validate_reference(value, "Required policy attribute value")
        if len(self.required_policy_attributes) != len(set(self.required_policy_attributes)):
            raise AccessControlContractError("Required policy attributes must not be duplicated")
        _validate_window(self.effective_from, self.expires_at, "Mapping")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Mapping revocation")
            if self.revoked_at < self.effective_from:
                raise AccessControlContractError("Mapping cannot be revoked before it is effective")

    def is_current(self, at: datetime) -> bool:
        _validate_instant(at, "Mapping evaluation time")
        return self.effective_from <= at < self.expires_at and (
            self.revoked_at is None or at < self.revoked_at
        )

    def matches(self, request: CurrentAuthorizationRequest, at: datetime) -> bool:
        if request.principal is None or not self.is_current(at):
            return False
        subject_matches = (
            self.subject_reference in request.role_references
            if self.subject_kind is MappingSubjectKind.ROLE
            else self.subject_reference
            in {f"{key}:{value}" for key, value in request.policy_attributes}
        )
        return (
            subject_matches
            and self.object_reference == request.object_reference
            and set(request.field_references).issubset(self.field_references)
            and self.action_reference == request.action_reference
            and self.purpose_reference == request.purpose_reference
            and self.classification_reference == request.classification_reference
            and set(self.required_policy_attributes).issubset(request.policy_attributes)
            and self.policy_version == request.policy_version
        )


class AuthorizationMappingRegistry:
    """Immutable mapping view; the controlled reference instance is empty."""

    def __init__(self, mappings: tuple[AuthorizationMapping, ...] = ()) -> None:
        references = tuple(mapping.mapping_reference for mapping in mappings)
        if len(references) != len(set(references)):
            raise AccessControlContractError("Mapping references must be unique")
        self._mappings = mappings

    def current_matches(
        self, request: CurrentAuthorizationRequest, at: datetime
    ) -> tuple[AuthorizationMapping, ...]:
        return tuple(mapping for mapping in self._mappings if mapping.matches(request, at))

    def is_empty(self) -> bool:
        return not self._mappings


EMPTY_INSTITUTIONAL_MAPPING_REGISTRY: Final = AuthorizationMappingRegistry()


class VersionedMappingPolicyDecisionPoint:
    """Integrate current four-layer mapping evaluation with the WP-001 boundary."""

    def __init__(
        self,
        registry: AuthorizationMappingRegistry = EMPTY_INSTITUTIONAL_MAPPING_REGISTRY,
        *,
        clock: Callable[[], datetime] | None = None,
    ) -> None:
        self._registry = registry
        self._clock = clock or (lambda: datetime.now(UTC))

    def evaluate(self, request: CurrentAuthorizationRequest) -> CurrentAuthorizationDecision:
        try:
            matches = self._registry.current_matches(request, self._clock())
        except Exception:
            return self._decision(request, AuthorizationEffect.INDETERMINATE, "MAPPING_ERROR")
        if len(matches) == 1:
            return self._decision(request, AuthorizationEffect.PERMIT, "CURRENT_MAPPING_GRANT")
        if len(matches) > 1:
            return self._decision(request, AuthorizationEffect.INDETERMINATE, "AMBIGUOUS_MAPPING")
        return self._decision(request, AuthorizationEffect.DENY, "NO_CURRENT_MAPPING_GRANT")

    @staticmethod
    def _decision(
        request: CurrentAuthorizationRequest,
        effect: AuthorizationEffect,
        reason: str,
    ) -> CurrentAuthorizationDecision:
        return CurrentAuthorizationDecision(
            request_reference=request.request_reference,
            policy_version=request.policy_version,
            effect=effect,
            reason_code=reason,
            evaluated_dimensions=ALL_AUTHORIZATION_DIMENSIONS,
        )


class DelegationClass(StrEnum):
    AGENT_FOR_HUMAN = "AGENT_FOR_HUMAN"
    AGENT_TO_AGENT = "AGENT_TO_AGENT"
    SERVICE_TO_SERVICE = "SERVICE_TO_SERVICE"
    HUMAN_TO_HUMAN = "HUMAN_TO_HUMAN"


@dataclass(frozen=True, slots=True)
class DelegationClassRule:
    delegation_class: DelegationClass
    scope_binding: str
    expiry_boundary: str
    revocation_trigger: str
    acting_class: PrincipalClass
    effective_class: PrincipalClass


APPROVED_DELEGATION_CLASS_RULES: Final = {
    DelegationClass.AGENT_FOR_HUMAN: DelegationClassRule(
        DelegationClass.AGENT_FOR_HUMAN,
        "TASK_CONTRACT",
        "RUN_BOUND",
        "HUMAN_AUTHORIZATION_CHANGE",
        PrincipalClass.AGENT,
        PrincipalClass.HUMAN,
    ),
    DelegationClass.AGENT_TO_AGENT: DelegationClassRule(
        DelegationClass.AGENT_TO_AGENT,
        "SUBTASK",
        "SUBTASK_BOUND",
        "PARENT_RUN_REVOCATION",
        PrincipalClass.AGENT,
        PrincipalClass.AGENT,
    ),
    DelegationClass.SERVICE_TO_SERVICE: DelegationClassRule(
        DelegationClass.SERVICE_TO_SERVICE,
        "SERVICE_REGISTRATION",
        "SESSION_BOUND",
        "SERVICE_CREDENTIAL_REVOCATION",
        PrincipalClass.SERVICE,
        PrincipalClass.SERVICE,
    ),
    DelegationClass.HUMAN_TO_HUMAN: DelegationClassRule(
        DelegationClass.HUMAN_TO_HUMAN,
        "ACTING_DEPUTY",
        "TIME_BOXED",
        "DEPUTISATION_RECORD",
        PrincipalClass.HUMAN,
        PrincipalClass.HUMAN,
    ),
}


@dataclass(frozen=True, slots=True)
class DelegationEnvelope:
    delegation_reference: str
    delegation_class: DelegationClass
    acting_identity: SecurityPrincipal
    effective_principal: SecurityPrincipal
    delegated_scopes: tuple[str, ...]
    delegator_current_scopes: tuple[str, ...]
    delegate_eligible_scopes: tuple[str, ...]
    purpose_reference: str
    source_record_reference: str
    policy_version: str
    starts_at: datetime
    expires_at: datetime
    duration_policy_reference: str
    revoked_at: datetime | None = None
    parent_run_reference: str | None = None
    deputisation_record_reference: str | None = None
    authority_confirmed_delegable: bool = False
    human_authorization_changed: bool = False
    parent_run_revoked: bool = False
    service_credential_revoked: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.delegation_reference, "Delegation reference"),
            (self.purpose_reference, "Delegation purpose reference"),
            (self.source_record_reference, "Delegation source record reference"),
            (self.policy_version, "Delegation policy version"),
            (self.duration_policy_reference, "Delegation duration policy reference"),
        ):
            _validate_reference(value, label)
        for values, label in (
            (self.delegated_scopes, "Delegated scope"),
            (self.delegator_current_scopes, "Delegator current scope"),
            (self.delegate_eligible_scopes, "Delegate eligible scope"),
        ):
            _validate_references(values, label)
        _validate_optional_reference(self.parent_run_reference, "Parent Run reference")
        _validate_optional_reference(self.deputisation_record_reference, "Deputisation reference")
        _validate_window(self.starts_at, self.expires_at, "Delegation")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Delegation revocation")
        rule = APPROVED_DELEGATION_CLASS_RULES[self.delegation_class]
        if self.acting_identity.principal_class is not rule.acting_class:
            raise AccessControlContractError(
                "Acting identity class does not match delegation class"
            )
        if self.effective_principal.principal_class is not rule.effective_class:
            raise AccessControlContractError(
                "Effective principal class does not match delegation class"
            )
        if not set(self.delegated_scopes).issubset(self.delegator_current_scopes):
            raise AccessControlContractError("Delegation exceeds delegator current authority")
        if not set(self.delegated_scopes).issubset(self.delegate_eligible_scopes):
            raise AccessControlContractError("Delegation exceeds delegate eligibility")
        if self.delegation_class is DelegationClass.AGENT_TO_AGENT:
            if self.parent_run_reference is None:
                raise AccessControlContractError("Agent-to-Agent delegation requires parent Run")
        elif self.parent_run_reference is not None:
            raise AccessControlContractError("Transitive delegation is not approved for this class")
        if self.delegation_class is DelegationClass.HUMAN_TO_HUMAN:
            if self.deputisation_record_reference is None or not self.authority_confirmed_delegable:
                raise AccessControlContractError(
                    "Human deputisation requires a record and confirmed delegability"
                )


class DelegationValidationCode(StrEnum):
    VALID = "VALID"
    NOT_STARTED = "NOT_STARTED"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"
    POLICY_MISMATCH = "POLICY_MISMATCH"
    PURPOSE_MISMATCH = "PURPOSE_MISMATCH"
    SCOPE_NOT_DELEGATED = "SCOPE_NOT_DELEGATED"
    SOURCE_REVOCATION_TRIGGERED = "SOURCE_REVOCATION_TRIGGERED"


@dataclass(frozen=True, slots=True)
class DelegationValidationResult:
    valid: bool
    code: DelegationValidationCode
    acting_identity: SecurityPrincipal
    effective_principal: SecurityPrincipal
    expands_authority: bool = False


class DelegationEvaluator:
    def evaluate(
        self,
        envelope: DelegationEnvelope,
        *,
        requested_scope: str,
        purpose_reference: str,
        policy_version: str,
        at: datetime,
    ) -> DelegationValidationResult:
        _validate_reference(requested_scope, "Requested delegated scope")
        _validate_reference(purpose_reference, "Requested delegation purpose")
        _validate_reference(policy_version, "Requested delegation policy version")
        _validate_instant(at, "Delegation evaluation time")
        code = DelegationValidationCode.VALID
        if at < envelope.starts_at:
            code = DelegationValidationCode.NOT_STARTED
        elif at >= envelope.expires_at:
            code = DelegationValidationCode.EXPIRED
        elif envelope.revoked_at is not None and at >= envelope.revoked_at:
            code = DelegationValidationCode.REVOKED
        elif self._source_revoked(envelope):
            code = DelegationValidationCode.SOURCE_REVOCATION_TRIGGERED
        elif policy_version != envelope.policy_version:
            code = DelegationValidationCode.POLICY_MISMATCH
        elif purpose_reference != envelope.purpose_reference:
            code = DelegationValidationCode.PURPOSE_MISMATCH
        elif requested_scope not in envelope.delegated_scopes:
            code = DelegationValidationCode.SCOPE_NOT_DELEGATED
        return DelegationValidationResult(
            valid=code is DelegationValidationCode.VALID,
            code=code,
            acting_identity=envelope.acting_identity,
            effective_principal=envelope.effective_principal,
        )

    @staticmethod
    def _source_revoked(envelope: DelegationEnvelope) -> bool:
        if envelope.delegation_class is DelegationClass.AGENT_FOR_HUMAN:
            return envelope.human_authorization_changed
        if envelope.delegation_class is DelegationClass.AGENT_TO_AGENT:
            return envelope.parent_run_revoked
        if envelope.delegation_class is DelegationClass.SERVICE_TO_SERVICE:
            return envelope.service_credential_revoked
        return False


class PrivilegeClass(StrEnum):
    INFRASTRUCTURE_CONFIGURATION_ADMIN = "INFRASTRUCTURE_CONFIGURATION_ADMIN"
    IDENTITY_IAM_ADMIN = "IDENTITY_IAM_ADMIN"
    DATA_CONTENT_ADMIN = "DATA_CONTENT_ADMIN"


class ApprovalInterface(StrEnum):
    AUTHORIZATION = "AUTHORIZATION"
    AUTHORIZATION_AND_ACCEPTANCE = "AUTHORIZATION_AND_ACCEPTANCE"


APPROVED_PRIVILEGE_INTERFACES: Final = {
    PrivilegeClass.INFRASTRUCTURE_CONFIGURATION_ADMIN: ApprovalInterface.AUTHORIZATION,
    PrivilegeClass.IDENTITY_IAM_ADMIN: ApprovalInterface.AUTHORIZATION,
    PrivilegeClass.DATA_CONTENT_ADMIN: ApprovalInterface.AUTHORIZATION_AND_ACCEPTANCE,
}


@dataclass(frozen=True, slots=True)
class PrivilegedAccessRequest:
    request_reference: str
    requester: SecurityPrincipal
    privilege_class: PrivilegeClass
    target_reference: str
    action_references: tuple[str, ...]
    justification_reference: str
    policy_version: str
    requested_at: datetime
    expires_at: datetime
    duration_policy_reference: str
    step_up_evidence_reference: str
    assurance_state: AssuranceState
    content_justification_reference: str | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Privilege request reference"),
            (self.target_reference, "Privilege target reference"),
            (self.justification_reference, "Privilege justification reference"),
            (self.policy_version, "Privilege policy version"),
            (self.duration_policy_reference, "Privilege duration policy reference"),
            (self.step_up_evidence_reference, "Privilege step-up evidence reference"),
        ):
            _validate_reference(value, label)
        _validate_references(self.action_references, "Privilege action reference")
        _validate_optional_reference(
            self.content_justification_reference, "Content justification reference"
        )
        _validate_window(self.requested_at, self.expires_at, "Privilege request")
        if self.assurance_state is not AssuranceState.ELEVATED:
            raise AccessControlContractError("Privileged access requires elevated assurance")
        if (
            self.privilege_class is PrivilegeClass.DATA_CONTENT_ADMIN
            and self.content_justification_reference is None
        ):
            raise AccessControlContractError("Content administration requires justification")


@dataclass(frozen=True, slots=True)
class PrivilegedApprovalDecision:
    decision_reference: str
    request_reference: str
    approver: SecurityPrincipal
    authority_assignment_reference: str
    privilege_class: PrivilegeClass
    target_reference: str
    action_references: tuple[str, ...]
    policy_version: str
    approved: bool
    decided_at: datetime
    expires_at: datetime
    revoked_at: datetime | None = None
    acceptance_decision_reference: str | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.decision_reference, "Privilege decision reference"),
            (self.request_reference, "Privilege request reference"),
            (self.authority_assignment_reference, "Privilege authority assignment reference"),
            (self.target_reference, "Privilege target reference"),
            (self.policy_version, "Privilege policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.action_references, "Approved privilege action")
        _validate_optional_reference(
            self.acceptance_decision_reference, "Content acceptance decision reference"
        )
        _validate_window(self.decided_at, self.expires_at, "Privilege approval")
        if self.approver.principal_class is not PrincipalClass.HUMAN:
            raise AccessControlContractError("Privilege approver must be a Human principal")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Privilege approval revocation")
        if (
            self.privilege_class is PrivilegeClass.DATA_CONTENT_ADMIN
            and self.approved
            and self.acceptance_decision_reference is None
        ):
            raise AccessControlContractError("Content privilege requires Acceptance evidence")


class PrivilegedApprovalBoundary(Protocol):
    def decide(self, request: PrivilegedAccessRequest) -> PrivilegedApprovalDecision | None: ...


class UnassignedPrivilegedApprovalAuthority:
    """UNASSIGNED means no approval and no privilege grant."""

    def decide(self, request: PrivilegedAccessRequest) -> PrivilegedApprovalDecision | None:
        del request
        return None


class PrivilegeValidationCode(StrEnum):
    VALID = "VALID"
    NO_CURRENT_APPROVAL_AUTHORITY = "NO_CURRENT_APPROVAL_AUTHORITY"
    NOT_APPROVED = "NOT_APPROVED"
    REQUEST_MISMATCH = "REQUEST_MISMATCH"
    SELF_APPROVAL = "SELF_APPROVAL"
    APPROVAL_NOT_EFFECTIVE = "APPROVAL_NOT_EFFECTIVE"
    APPROVAL_EXPIRED = "APPROVAL_EXPIRED"
    APPROVAL_REVOKED = "APPROVAL_REVOKED"


@dataclass(frozen=True, slots=True)
class PrivilegeValidationResult:
    valid: bool
    code: PrivilegeValidationCode
    elevation: PrivilegeElevationContext | None = None


@dataclass(frozen=True, slots=True)
class PrivilegeElevationContext:
    request_reference: str
    approval_decision_reference: str
    acting_identity: SecurityPrincipal
    privilege_class: PrivilegeClass
    target_reference: str
    action_references: tuple[str, ...]
    starts_at: datetime
    expires_at: datetime
    policy_version: str


class PrivilegedAccessEvaluator:
    def __init__(self, authority: PrivilegedApprovalBoundary) -> None:
        self._authority = authority

    def evaluate(
        self, request: PrivilegedAccessRequest, *, at: datetime
    ) -> PrivilegeValidationResult:
        _validate_instant(at, "Privilege evaluation time")
        decision = self._authority.decide(request)
        if decision is None:
            return PrivilegeValidationResult(
                False, PrivilegeValidationCode.NO_CURRENT_APPROVAL_AUTHORITY
            )
        if not decision.approved:
            return PrivilegeValidationResult(False, PrivilegeValidationCode.NOT_APPROVED)
        if decision.approver == request.requester:
            return PrivilegeValidationResult(False, PrivilegeValidationCode.SELF_APPROVAL)
        if (
            decision.request_reference != request.request_reference
            or decision.privilege_class is not request.privilege_class
            or decision.target_reference != request.target_reference
            or decision.action_references != request.action_references
            or decision.policy_version != request.policy_version
            or decision.expires_at > request.expires_at
            or decision.decided_at < request.requested_at
        ):
            return PrivilegeValidationResult(False, PrivilegeValidationCode.REQUEST_MISMATCH)
        if at < decision.decided_at:
            return PrivilegeValidationResult(False, PrivilegeValidationCode.APPROVAL_NOT_EFFECTIVE)
        if at >= decision.expires_at:
            return PrivilegeValidationResult(False, PrivilegeValidationCode.APPROVAL_EXPIRED)
        if decision.revoked_at is not None and at >= decision.revoked_at:
            return PrivilegeValidationResult(False, PrivilegeValidationCode.APPROVAL_REVOKED)
        return PrivilegeValidationResult(
            True,
            PrivilegeValidationCode.VALID,
            PrivilegeElevationContext(
                request.request_reference,
                decision.decision_reference,
                request.requester,
                request.privilege_class,
                request.target_reference,
                request.action_references,
                decision.decided_at,
                decision.expires_at,
                request.policy_version,
            ),
        )


class EmergencyClass(StrEnum):
    IDENTITY_ACCESS_SUSPENSION = "IDENTITY_ACCESS_SUSPENSION"
    AGENT_MODEL_TOOL_SUSPENSION = "AGENT_MODEL_TOOL_SUSPENSION"
    INFRASTRUCTURE_BREAK_GLASS_ADMIN = "INFRASTRUCTURE_BREAK_GLASS_ADMIN"


class EmergencyTriggerClass(StrEnum):
    DECLARED_SECURITY_EMERGENCY = "DECLARED_SECURITY_EMERGENCY"
    DECLARED_OPERATIONAL_EMERGENCY = "DECLARED_OPERATIONAL_EMERGENCY"


class EmergencyAction(StrEnum):
    SUSPEND = "SUSPEND"
    CONTAIN = "CONTAIN"
    ADMINISTER = "ADMINISTER"


_EMERGENCY_TRIGGER: Final = {
    EmergencyClass.IDENTITY_ACCESS_SUSPENSION: EmergencyTriggerClass.DECLARED_SECURITY_EMERGENCY,
    EmergencyClass.AGENT_MODEL_TOOL_SUSPENSION: (EmergencyTriggerClass.DECLARED_SECURITY_EMERGENCY),
    EmergencyClass.INFRASTRUCTURE_BREAK_GLASS_ADMIN: (
        EmergencyTriggerClass.DECLARED_OPERATIONAL_EMERGENCY
    ),
}

_EMERGENCY_ACTIONS: Final = {
    EmergencyClass.IDENTITY_ACCESS_SUSPENSION: frozenset(
        {EmergencyAction.SUSPEND, EmergencyAction.CONTAIN}
    ),
    EmergencyClass.AGENT_MODEL_TOOL_SUSPENSION: frozenset(
        {EmergencyAction.SUSPEND, EmergencyAction.CONTAIN}
    ),
    EmergencyClass.INFRASTRUCTURE_BREAK_GLASS_ADMIN: frozenset(
        {EmergencyAction.ADMINISTER, EmergencyAction.CONTAIN}
    ),
}


@dataclass(frozen=True, slots=True)
class EmergencyDeclaration:
    declaration_reference: str
    emergency_class: EmergencyClass
    trigger_class: EmergencyTriggerClass
    declared_by: SecurityPrincipal
    target_reference: str
    purpose_reference: str
    decision_reference: str
    declared_at: datetime
    expires_at: datetime
    duration_policy_reference: str
    policy_version: str
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.declaration_reference, "Emergency declaration reference"),
            (self.target_reference, "Emergency target reference"),
            (self.purpose_reference, "Emergency purpose reference"),
            (self.decision_reference, "Emergency decision reference"),
            (self.duration_policy_reference, "Emergency duration policy reference"),
            (self.policy_version, "Emergency policy version"),
        ):
            _validate_reference(value, label)
        _validate_window(self.declared_at, self.expires_at, "Emergency declaration")
        if self.declared_by.principal_class is not PrincipalClass.HUMAN:
            raise AccessControlContractError("Emergency declaration requires Human authority")
        if self.trigger_class is not _EMERGENCY_TRIGGER[self.emergency_class]:
            raise AccessControlContractError("Emergency trigger does not match its class")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Emergency revocation")


@dataclass(frozen=True, slots=True)
class EmergencyEligibilityDecision:
    eligibility_reference: str
    emergency_class: EmergencyClass
    eligible_operator: SecurityPrincipal
    authority_holder: SecurityPrincipal
    target_reference: str
    eligible: bool
    effective_from: datetime
    expires_at: datetime
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.eligibility_reference, "Emergency eligibility reference")
        _validate_reference(self.target_reference, "Emergency eligibility target")
        _validate_window(self.effective_from, self.expires_at, "Emergency eligibility")
        if self.authority_holder.principal_class is not PrincipalClass.HUMAN:
            raise AccessControlContractError("Emergency Authority must be Human")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Emergency eligibility revocation")


class EmergencyEligibilityBoundary(Protocol):
    def resolve(
        self, declaration: EmergencyDeclaration, operator: SecurityPrincipal
    ) -> EmergencyEligibilityDecision | None: ...


class UnassignedEmergencyEligibility:
    """Zero eligibility roster: every attempted activation is denied."""

    def resolve(
        self, declaration: EmergencyDeclaration, operator: SecurityPrincipal
    ) -> EmergencyEligibilityDecision | None:
        del declaration, operator
        return None


@dataclass(frozen=True, slots=True)
class EmergencyAccessRequest:
    request_reference: str
    declaration: EmergencyDeclaration
    operator: SecurityPrincipal
    action: EmergencyAction
    requested_at: datetime
    expires_at: datetime
    step_up_evidence_reference: str
    assurance_state: AssuranceState

    def __post_init__(self) -> None:
        _validate_reference(self.request_reference, "Emergency access request reference")
        _validate_reference(self.step_up_evidence_reference, "Emergency step-up reference")
        _validate_window(self.requested_at, self.expires_at, "Emergency access request")
        if self.expires_at > self.declaration.expires_at:
            raise AccessControlContractError("Emergency request exceeds declaration expiry")
        if self.action not in _EMERGENCY_ACTIONS[self.declaration.emergency_class]:
            raise AccessControlContractError("Emergency action exceeds containment boundary")
        if self.assurance_state is not AssuranceState.ELEVATED:
            raise AccessControlContractError("Emergency access requires elevated assurance")


class EmergencyValidationCode(StrEnum):
    VALID = "VALID"
    NO_ELIGIBLE_EMERGENCY_AUTHORITY = "NO_ELIGIBLE_EMERGENCY_AUTHORITY"
    ELIGIBILITY_MISMATCH = "ELIGIBILITY_MISMATCH"
    NOT_STARTED = "NOT_STARTED"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"


@dataclass(frozen=True, slots=True)
class EmergencyActivationResult:
    valid: bool
    code: EmergencyValidationCode
    activation_reference: str | None = None
    auto_expires_at: datetime | None = None


class EmergencyAccessEvaluator:
    def __init__(self, eligibility: EmergencyEligibilityBoundary) -> None:
        self._eligibility = eligibility

    def evaluate(
        self, request: EmergencyAccessRequest, *, at: datetime
    ) -> EmergencyActivationResult:
        _validate_instant(at, "Emergency evaluation time")
        declaration = request.declaration
        eligibility = self._eligibility.resolve(declaration, request.operator)
        if eligibility is None or not eligibility.eligible:
            return EmergencyActivationResult(
                False, EmergencyValidationCode.NO_ELIGIBLE_EMERGENCY_AUTHORITY
            )
        if (
            eligibility.emergency_class is not declaration.emergency_class
            or eligibility.eligible_operator != request.operator
            or eligibility.authority_holder != declaration.declared_by
            or eligibility.target_reference != declaration.target_reference
        ):
            return EmergencyActivationResult(False, EmergencyValidationCode.ELIGIBILITY_MISMATCH)
        if at < declaration.declared_at or at < eligibility.effective_from:
            return EmergencyActivationResult(False, EmergencyValidationCode.NOT_STARTED)
        if at >= min(declaration.expires_at, request.expires_at, eligibility.expires_at):
            return EmergencyActivationResult(False, EmergencyValidationCode.EXPIRED)
        if (declaration.revoked_at is not None and at >= declaration.revoked_at) or (
            eligibility.revoked_at is not None and at >= eligibility.revoked_at
        ):
            return EmergencyActivationResult(False, EmergencyValidationCode.REVOKED)
        return EmergencyActivationResult(
            True,
            EmergencyValidationCode.VALID,
            activation_reference=request.request_reference,
            auto_expires_at=min(declaration.expires_at, request.expires_at, eligibility.expires_at),
        )


@dataclass(frozen=True, slots=True)
class EmergencyNotificationObligation:
    activation_reference: str
    domain_accountable_authority_reference: str | None
    assurance_audit_reference: str | None

    def __post_init__(self) -> None:
        _validate_reference(self.activation_reference, "Emergency activation reference")
        _validate_optional_reference(
            self.domain_accountable_authority_reference,
            "Domain Accountable Authority reference",
        )
        _validate_optional_reference(self.assurance_audit_reference, "Assurance/Audit reference")

    def is_complete(self) -> bool:
        return (
            self.domain_accountable_authority_reference is not None
            and self.assurance_audit_reference is not None
        )


class PostEventDisposition(StrEnum):
    REINSTATE = "REINSTATE"
    KEEP_CONTAINED = "KEEP_CONTAINED"
    REFER_FOR_PERMANENT_DECISION = "REFER_FOR_PERMANENT_DECISION"


@dataclass(frozen=True, slots=True)
class EmergencyPostEventReview:
    review_reference: str
    activation_reference: str
    reviewer: SecurityPrincipal
    operator: SecurityPrincipal
    declaring_authority: SecurityPrincipal
    reviewed_at: datetime
    disposition: PostEventDisposition
    scope_confirmed: bool
    expiry_revocation_confirmed: bool
    effects_reviewed: bool
    restoration_evidence_reference: str | None

    def __post_init__(self) -> None:
        _validate_reference(self.review_reference, "Post-event review reference")
        _validate_reference(self.activation_reference, "Reviewed activation reference")
        _validate_optional_reference(
            self.restoration_evidence_reference, "Restoration evidence reference"
        )
        _validate_instant(self.reviewed_at, "Post-event review time")
        if self.reviewer.principal_class is not PrincipalClass.HUMAN:
            raise AccessControlContractError("Post-event reviewer must be Human")

    def supports_disposition(self, notification: EmergencyNotificationObligation) -> bool:
        independent = self.reviewer not in {self.operator, self.declaring_authority}
        restoration_ready = (
            self.disposition is not PostEventDisposition.REINSTATE
            or self.restoration_evidence_reference is not None
        )
        return (
            independent
            and notification.activation_reference == self.activation_reference
            and notification.is_complete()
            and self.scope_confirmed
            and self.expiry_revocation_confirmed
            and self.effects_reviewed
            and restoration_ready
        )


class AccessControlSignals:
    """Emit minimized operational signals; never institutional Evidence or decisions."""

    def __init__(self, sink: ObservabilitySink) -> None:
        self._sink = sink

    def emit(
        self,
        *,
        correlation_id: str,
        contract_class: str,
        outcome: str,
        reason_code: str,
    ) -> None:
        _validate_reference(correlation_id, "Signal correlation reference")
        _validate_reference(contract_class, "Signal contract class")
        _validate_reference(outcome, "Signal outcome")
        _validate_reference(reason_code, "Signal reason code")
        self._sink.emit_event(
            OperationalEvent(
                category=SignalCategory.SECURITY_CONDITION,
                name="security.access_control.decision",
                correlation_id=correlation_id,
                attributes=(
                    ("contract_class", contract_class),
                    ("outcome", outcome),
                    ("reason_code", reason_code),
                ),
            )
        )
