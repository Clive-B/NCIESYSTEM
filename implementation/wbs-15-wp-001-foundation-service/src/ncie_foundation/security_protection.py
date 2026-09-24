"""Provider-neutral WP-005 secrets, cryptography, and Zero-Trust contracts."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from re import compile as compile_pattern
from typing import Final, Protocol

from .observability import ObservabilitySink, OperationalEvent, SignalCategory
from .security_authorization import AuthorizationEffect, CurrentAuthorizationDecision

SECURITY_PROTECTION_BASELINE_VERSION: Final = "NCIE-WBS16-WP005-2026-09-23"
SECURITY_PROTECTION_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-23-020"
SECURITY_PROTECTION_IMPLEMENTATION_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-23-021"

_REFERENCE_PATTERN: Final = compile_pattern(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}")
_PROTECTED_REFERENCE_FRAGMENTS: Final = (
    "-----begin",
    "credential_value",
    "private_key",
    "secret_value",
    "token_value",
)
_DENY_SENTINELS: Final = frozenset({"unassigned", "unspecified", "unknown"})


class SecurityProtectionContractError(ValueError):
    """Raised without echoing protected input when a WP-005 contract is invalid."""


def _validate_reference(value: str, label: str) -> None:
    normalized = value.lower()
    if (
        _REFERENCE_PATTERN.fullmatch(value) is None
        or any(fragment in normalized for fragment in _PROTECTED_REFERENCE_FRAGMENTS)
        or normalized in _DENY_SENTINELS
    ):
        raise SecurityProtectionContractError(f"{label} is invalid or contains protected material")


def _validate_optional_reference(value: str | None, label: str) -> None:
    if value is not None:
        _validate_reference(value, label)


def _validate_references(values: tuple[str, ...], label: str, *, required: bool = True) -> None:
    if required and not values:
        raise SecurityProtectionContractError(f"{label} is required")
    if len(values) != len(set(values)):
        raise SecurityProtectionContractError(f"{label} must not contain duplicates")
    for value in values:
        _validate_reference(value, label)


def _validate_instant(value: datetime, label: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise SecurityProtectionContractError(f"{label} must include a timezone")


def _validate_window(starts_at: datetime, expires_at: datetime, label: str) -> None:
    _validate_instant(starts_at, f"{label} start")
    _validate_instant(expires_at, f"{label} expiry")
    if expires_at <= starts_at:
        raise SecurityProtectionContractError(f"{label} expiry must follow its start")


class ProtectedReferenceClass(StrEnum):
    SECRET = "SECRET"
    KEY = "KEY"
    CERTIFICATE = "CERTIFICATE"


@dataclass(frozen=True, slots=True)
class OpaqueProtectedReference:
    """Metadata-only reference; it cannot contain protected material."""

    reference: str
    reference_class: ProtectedReferenceClass
    policy_version: str

    def __post_init__(self) -> None:
        _validate_reference(self.reference, "Protected-material reference")
        if not self.reference.startswith("ref:"):
            raise SecurityProtectionContractError(
                "Protected-material reference must use the opaque ref namespace"
            )
        _validate_reference(self.policy_version, "Protected-material policy version")


class LifecycleAction(StrEnum):
    REQUEST = "REQUEST"
    ISSUE_REFERENCE = "ISSUE_REFERENCE"
    ACCESS_REFERENCE = "ACCESS_REFERENCE"
    ROTATE_REFERENCE = "ROTATE_REFERENCE"
    EXPIRE_REFERENCE = "EXPIRE_REFERENCE"
    REVOKE_REFERENCE = "REVOKE_REFERENCE"


@dataclass(frozen=True, slots=True)
class ProtectedLifecycleEventContract:
    """Describes lifecycle evidence metadata without executing an operation."""

    event_reference: str
    material_reference: OpaqueProtectedReference
    action: LifecycleAction
    requester_reference: str
    purpose_reference: str
    classification_reference: str
    policy_version: str
    requested_at: datetime
    custodial_authority_reference: str | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.event_reference, "Lifecycle event reference"),
            (self.requester_reference, "Lifecycle requester reference"),
            (self.purpose_reference, "Lifecycle purpose reference"),
            (self.classification_reference, "Lifecycle classification reference"),
            (self.policy_version, "Lifecycle policy version"),
        ):
            _validate_reference(value, label)
        _validate_optional_reference(
            self.custodial_authority_reference, "Custodial authority reference"
        )
        _validate_instant(self.requested_at, "Lifecycle request time")


@dataclass(frozen=True, slots=True)
class LifecycleAuthorityDecision:
    decision_reference: str
    event_reference: str
    authority_assignment_reference: str
    approved: bool
    decided_at: datetime
    expires_at: datetime
    policy_version: str
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.decision_reference, "Lifecycle decision reference"),
            (self.event_reference, "Lifecycle event reference"),
            (self.authority_assignment_reference, "Lifecycle authority assignment reference"),
            (self.policy_version, "Lifecycle decision policy version"),
        ):
            _validate_reference(value, label)
        _validate_window(self.decided_at, self.expires_at, "Lifecycle authority decision")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Lifecycle authority revocation")


class CustodialAuthorityBoundary(Protocol):
    def decide(
        self, event: ProtectedLifecycleEventContract
    ) -> LifecycleAuthorityDecision | None: ...


class UnassignedCustodialAuthority:
    """No operational custodian exists; every lifecycle request remains unavailable."""

    def decide(self, event: ProtectedLifecycleEventContract) -> LifecycleAuthorityDecision | None:
        del event
        return None


class PolicyApprovalBoundary(Protocol):
    def approve_policy(self, policy_reference: str) -> str | None: ...


class IndependentAssuranceBoundary(Protocol):
    def attest(self, contract_reference: str) -> str | None: ...


class UnassignedPolicyApprovalAuthority:
    """No policy approver is assigned; no approval reference can be produced."""

    def approve_policy(self, policy_reference: str) -> str | None:
        _validate_reference(policy_reference, "Policy reference")
        return None


class UnassignedIndependentAssurance:
    """No assurance holder is assigned; no attestation can be produced."""

    def attest(self, contract_reference: str) -> str | None:
        _validate_reference(contract_reference, "Assurance contract reference")
        return None


class LifecycleValidationCode(StrEnum):
    VALID_CONTRACT = "VALID_CONTRACT"
    NO_CURRENT_CUSTODIAL_AUTHORITY = "NO_CURRENT_CUSTODIAL_AUTHORITY"
    NOT_APPROVED = "NOT_APPROVED"
    DECISION_MISMATCH = "DECISION_MISMATCH"
    DECISION_NOT_EFFECTIVE = "DECISION_NOT_EFFECTIVE"
    DECISION_EXPIRED = "DECISION_EXPIRED"
    DECISION_REVOKED = "DECISION_REVOKED"


@dataclass(frozen=True, slots=True)
class LifecycleValidationResult:
    allowed: bool
    code: LifecycleValidationCode
    operation_executed: bool = False


class ProtectedLifecycleEvaluator:
    def __init__(self, authority: CustodialAuthorityBoundary) -> None:
        self._authority = authority

    def evaluate(
        self, event: ProtectedLifecycleEventContract, *, at: datetime
    ) -> LifecycleValidationResult:
        _validate_instant(at, "Lifecycle evaluation time")
        decision = self._authority.decide(event)
        if decision is None:
            return LifecycleValidationResult(
                False, LifecycleValidationCode.NO_CURRENT_CUSTODIAL_AUTHORITY
            )
        if not decision.approved:
            return LifecycleValidationResult(False, LifecycleValidationCode.NOT_APPROVED)
        if (
            decision.event_reference != event.event_reference
            or decision.policy_version != event.policy_version
        ):
            return LifecycleValidationResult(False, LifecycleValidationCode.DECISION_MISMATCH)
        if at < decision.decided_at:
            return LifecycleValidationResult(False, LifecycleValidationCode.DECISION_NOT_EFFECTIVE)
        if at >= decision.expires_at:
            return LifecycleValidationResult(False, LifecycleValidationCode.DECISION_EXPIRED)
        if decision.revoked_at is not None and at >= decision.revoked_at:
            return LifecycleValidationResult(False, LifecycleValidationCode.DECISION_REVOKED)
        return LifecycleValidationResult(True, LifecycleValidationCode.VALID_CONTRACT)


class ProhibitedSurface(StrEnum):
    SOURCE_CODE = "SOURCE_CODE"
    PROMPT = "PROMPT"
    AGENT_CONTEXT = "AGENT_CONTEXT"
    GENERATED_CODE = "GENERATED_CODE"
    LOG = "LOG"
    TELEMETRY = "TELEMETRY"
    TEST_FIXTURE = "TEST_FIXTURE"
    DOCUMENTATION = "DOCUMENTATION"
    UNCONTROLLED_EXPORT = "UNCONTROLLED_EXPORT"


class ExposureValidationCode(StrEnum):
    CLEAR = "CLEAR"
    PROTECTED_MATERIAL_PROHIBITED = "PROTECTED_MATERIAL_PROHIBITED"
    PLAINTEXT_FALLBACK_PROHIBITED = "PLAINTEXT_FALLBACK_PROHIBITED"


@dataclass(frozen=True, slots=True)
class ExposureAssessment:
    allowed: bool
    code: ExposureValidationCode
    exception_permitted: bool = False


class ProhibitedSurfaceEvaluator:
    """Consumes classification flags only; it never accepts or inspects protected values."""

    def evaluate(
        self,
        *,
        surface: ProhibitedSurface,
        protected_material_present: bool,
        plaintext_fallback_requested: bool = False,
    ) -> ExposureAssessment:
        del surface
        if protected_material_present:
            return ExposureAssessment(False, ExposureValidationCode.PROTECTED_MATERIAL_PROHIBITED)
        if plaintext_fallback_requested:
            return ExposureAssessment(False, ExposureValidationCode.PLAINTEXT_FALLBACK_PROHIBITED)
        return ExposureAssessment(True, ExposureValidationCode.CLEAR)


@dataclass(frozen=True, slots=True)
class SecurityExceptionRequest:
    request_reference: str
    requester_reference: str
    scope_references: tuple[str, ...]
    purpose_reference: str
    classification_reference: str
    residency_reference: str
    compensating_control_references: tuple[str, ...]
    policy_version: str
    starts_at: datetime
    expires_at: datetime
    prohibited_surface: ProhibitedSurface | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Exception request reference"),
            (self.requester_reference, "Exception requester reference"),
            (self.purpose_reference, "Exception purpose reference"),
            (self.classification_reference, "Exception classification reference"),
            (self.residency_reference, "Exception residency reference"),
            (self.policy_version, "Exception policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.scope_references, "Exception scope reference")
        _validate_references(self.compensating_control_references, "Compensating control reference")
        _validate_window(self.starts_at, self.expires_at, "Exception request")


@dataclass(frozen=True, slots=True)
class SecurityExceptionDecision:
    decision_reference: str
    request_reference: str
    approver_reference: str
    authority_assignment_reference: str
    approved: bool
    decided_at: datetime
    expires_at: datetime
    policy_version: str
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.decision_reference, "Exception decision reference"),
            (self.request_reference, "Exception request reference"),
            (self.approver_reference, "Exception approver reference"),
            (self.authority_assignment_reference, "Exception authority assignment reference"),
            (self.policy_version, "Exception decision policy version"),
        ):
            _validate_reference(value, label)
        _validate_window(self.decided_at, self.expires_at, "Exception decision")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Exception revocation")


class ExceptionAuthorityBoundary(Protocol):
    def decide(self, request: SecurityExceptionRequest) -> SecurityExceptionDecision | None: ...


class UnassignedExceptionAuthority:
    def decide(self, request: SecurityExceptionRequest) -> SecurityExceptionDecision | None:
        del request
        return None


class ExceptionValidationCode(StrEnum):
    VALID_CONTRACT = "VALID_CONTRACT"
    NO_CURRENT_EXCEPTION_AUTHORITY = "NO_CURRENT_EXCEPTION_AUTHORITY"
    NOT_APPROVED = "NOT_APPROVED"
    SELF_APPROVAL = "SELF_APPROVAL"
    DECISION_MISMATCH = "DECISION_MISMATCH"
    DECISION_NOT_EFFECTIVE = "DECISION_NOT_EFFECTIVE"
    DECISION_EXPIRED = "DECISION_EXPIRED"
    DECISION_REVOKED = "DECISION_REVOKED"
    ABSOLUTE_PROHIBITION = "ABSOLUTE_PROHIBITION"


@dataclass(frozen=True, slots=True)
class ExceptionValidationResult:
    allowed: bool
    code: ExceptionValidationCode
    capability_activated: bool = False


class SecurityExceptionEvaluator:
    def __init__(self, authority: ExceptionAuthorityBoundary) -> None:
        self._authority = authority

    def evaluate(
        self, request: SecurityExceptionRequest, *, at: datetime
    ) -> ExceptionValidationResult:
        _validate_instant(at, "Exception evaluation time")
        if request.prohibited_surface is not None:
            return ExceptionValidationResult(False, ExceptionValidationCode.ABSOLUTE_PROHIBITION)
        decision = self._authority.decide(request)
        if decision is None:
            return ExceptionValidationResult(
                False, ExceptionValidationCode.NO_CURRENT_EXCEPTION_AUTHORITY
            )
        if not decision.approved:
            return ExceptionValidationResult(False, ExceptionValidationCode.NOT_APPROVED)
        if decision.approver_reference == request.requester_reference:
            return ExceptionValidationResult(False, ExceptionValidationCode.SELF_APPROVAL)
        if (
            decision.request_reference != request.request_reference
            or decision.policy_version != request.policy_version
            or decision.expires_at > request.expires_at
        ):
            return ExceptionValidationResult(False, ExceptionValidationCode.DECISION_MISMATCH)
        if at < decision.decided_at:
            return ExceptionValidationResult(False, ExceptionValidationCode.DECISION_NOT_EFFECTIVE)
        if at >= decision.expires_at:
            return ExceptionValidationResult(False, ExceptionValidationCode.DECISION_EXPIRED)
        if decision.revoked_at is not None and at >= decision.revoked_at:
            return ExceptionValidationResult(False, ExceptionValidationCode.DECISION_REVOKED)
        return ExceptionValidationResult(True, ExceptionValidationCode.VALID_CONTRACT)


class ProtectionScope(StrEnum):
    AT_REST = "AT_REST"
    IN_TRANSIT = "IN_TRANSIT"
    SENSITIVE_FIELD = "SENSITIVE_FIELD"


class KeyHierarchyTier(StrEnum):
    ROOT = "ROOT"
    INTERMEDIATE = "INTERMEDIATE"
    DATA_ENCRYPTION = "DATA_ENCRYPTION"


class SeparationDimension(StrEnum):
    SENSITIVITY_CLASSIFICATION = "SENSITIVITY_CLASSIFICATION"
    PURPOSE_DOMAIN = "PURPOSE_DOMAIN"
    ENVIRONMENT = "ENVIRONMENT"
    CUSTODIAL_BOUNDARY = "CUSTODIAL_BOUNDARY"


ALL_SEPARATION_DIMENSIONS: Final = tuple(SeparationDimension)


@dataclass(frozen=True, slots=True)
class CryptographicPolicyContract:
    """Policy metadata only; it contains no algorithm, profile, product, or key."""

    policy_reference: str
    policy_version: str
    protection_scope: ProtectionScope
    hierarchy_tier: KeyHierarchyTier
    separation_dimensions: tuple[SeparationDimension, ...]
    agility_successor_reference: str
    effective_from: datetime
    expires_at: datetime
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.policy_reference, "Cryptographic policy reference")
        _validate_reference(self.policy_version, "Cryptographic policy version")
        _validate_reference(self.agility_successor_reference, "Agility successor reference")
        if set(self.separation_dimensions) != set(ALL_SEPARATION_DIMENSIONS) or len(
            self.separation_dimensions
        ) != len(ALL_SEPARATION_DIMENSIONS):
            raise SecurityProtectionContractError(
                "Cryptographic policy must preserve every approved separation dimension"
            )
        _validate_window(self.effective_from, self.expires_at, "Cryptographic policy")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Cryptographic policy revocation")

    def is_current(self, at: datetime) -> bool:
        _validate_instant(at, "Cryptographic policy evaluation time")
        return self.effective_from <= at < self.expires_at and (
            self.revoked_at is None or at < self.revoked_at
        )


class CryptographicPolicyRegistry:
    def __init__(self, policies: tuple[CryptographicPolicyContract, ...] = ()) -> None:
        references = tuple(policy.policy_reference for policy in policies)
        if len(references) != len(set(references)):
            raise SecurityProtectionContractError("Cryptographic policy references must be unique")
        self._policies = policies

    def resolve(
        self, policy_reference: str, policy_version: str
    ) -> CryptographicPolicyContract | None:
        _validate_reference(policy_reference, "Cryptographic policy reference")
        _validate_reference(policy_version, "Cryptographic policy version")
        matches = tuple(
            policy
            for policy in self._policies
            if policy.policy_reference == policy_reference
            and policy.policy_version == policy_version
        )
        return matches[0] if len(matches) == 1 else None

    def is_empty(self) -> bool:
        return not self._policies


EMPTY_CRYPTOGRAPHIC_POLICY_REGISTRY: Final = CryptographicPolicyRegistry()


@dataclass(frozen=True, slots=True)
class CryptographicPolicyRequest:
    request_reference: str
    policy_reference: str
    policy_version: str
    protection_scope: ProtectionScope
    hierarchy_tier: KeyHierarchyTier
    required_separation_dimensions: tuple[SeparationDimension, ...]
    authorization_decision: CurrentAuthorizationDecision

    def __post_init__(self) -> None:
        _validate_reference(self.request_reference, "Cryptographic request reference")
        _validate_reference(self.policy_reference, "Cryptographic policy reference")
        _validate_reference(self.policy_version, "Cryptographic policy version")
        if not self.required_separation_dimensions or len(
            self.required_separation_dimensions
        ) != len(set(self.required_separation_dimensions)):
            raise SecurityProtectionContractError(
                "Required separation dimensions must be unique and non-empty"
            )


class CryptographicValidationCode(StrEnum):
    VALID_CONTRACT = "VALID_CONTRACT"
    NO_CURRENT_AUTHORIZATION = "NO_CURRENT_AUTHORIZATION"
    NO_CURRENT_CRYPTOGRAPHIC_POLICY = "NO_CURRENT_CRYPTOGRAPHIC_POLICY"
    POLICY_NOT_EFFECTIVE = "POLICY_NOT_EFFECTIVE"
    POLICY_EXPIRED_OR_REVOKED = "POLICY_EXPIRED_OR_REVOKED"
    PROTECTION_SCOPE_MISMATCH = "PROTECTION_SCOPE_MISMATCH"
    KEY_TIER_MISMATCH = "KEY_TIER_MISMATCH"
    SEPARATION_REQUIREMENT_MISMATCH = "SEPARATION_REQUIREMENT_MISMATCH"


@dataclass(frozen=True, slots=True)
class CryptographicValidationResult:
    allowed: bool
    code: CryptographicValidationCode
    cryptography_executed: bool = False


class CryptographicPolicyEvaluator:
    def __init__(
        self, registry: CryptographicPolicyRegistry = EMPTY_CRYPTOGRAPHIC_POLICY_REGISTRY
    ) -> None:
        self._registry = registry

    def evaluate(
        self, request: CryptographicPolicyRequest, *, at: datetime
    ) -> CryptographicValidationResult:
        _validate_instant(at, "Cryptographic evaluation time")
        authorization = request.authorization_decision
        if (
            authorization.effect is not AuthorizationEffect.PERMIT
            or authorization.request_reference != request.request_reference
            or authorization.policy_version != request.policy_version
        ):
            return CryptographicValidationResult(
                False, CryptographicValidationCode.NO_CURRENT_AUTHORIZATION
            )
        policy = self._registry.resolve(request.policy_reference, request.policy_version)
        if policy is None:
            return CryptographicValidationResult(
                False, CryptographicValidationCode.NO_CURRENT_CRYPTOGRAPHIC_POLICY
            )
        if at < policy.effective_from:
            return CryptographicValidationResult(
                False, CryptographicValidationCode.POLICY_NOT_EFFECTIVE
            )
        if not policy.is_current(at):
            return CryptographicValidationResult(
                False, CryptographicValidationCode.POLICY_EXPIRED_OR_REVOKED
            )
        if policy.protection_scope is not request.protection_scope:
            return CryptographicValidationResult(
                False, CryptographicValidationCode.PROTECTION_SCOPE_MISMATCH
            )
        if policy.hierarchy_tier is not request.hierarchy_tier:
            return CryptographicValidationResult(
                False, CryptographicValidationCode.KEY_TIER_MISMATCH
            )
        if not set(request.required_separation_dimensions).issubset(policy.separation_dimensions):
            return CryptographicValidationResult(
                False, CryptographicValidationCode.SEPARATION_REQUIREMENT_MISMATCH
            )
        return CryptographicValidationResult(True, CryptographicValidationCode.VALID_CONTRACT)


class TrustZone(StrEnum):
    EDGE_API = "EDGE_API"
    APPLICATION = "APPLICATION"
    DATA = "DATA"
    AI = "AI"
    INTEGRATION = "INTEGRATION"
    SECURITY_OBSERVABILITY = "SECURITY_OBSERVABILITY"
    MANAGEMENT_GOVERNANCE = "MANAGEMENT_GOVERNANCE"


class EgressClass(StrEnum):
    NO_EGRESS = "NO_EGRESS"
    INTERNAL_GOVERNED_SERVICE = "INTERNAL_GOVERNED_SERVICE"
    MODEL_GATEWAY_ONLY = "MODEL_GATEWAY_ONLY"
    TOOL_GATEWAY_ONLY = "TOOL_GATEWAY_ONLY"
    EXPLICIT_EXTERNAL_DESTINATION = "EXPLICIT_EXTERNAL_DESTINATION"


class ServiceBoundaryClass(StrEnum):
    PUBLIC_OPERATOR_TO_EDGE_API = "PUBLIC_OPERATOR_TO_EDGE_API"
    EDGE_API_TO_APPLICATION = "EDGE_API_TO_APPLICATION"
    APPLICATION_TO_DATA = "APPLICATION_TO_DATA"
    APPLICATION_TO_AI_VIA_MODEL_GATEWAY = "APPLICATION_TO_AI_VIA_MODEL_GATEWAY"
    SECURITY_OBSERVABILITY_GOVERNANCE = "SECURITY_OBSERVABILITY_GOVERNANCE"
    MANAGEMENT_GOVERNANCE_CONTROL = "MANAGEMENT_GOVERNANCE_CONTROL"
    EPHEMERAL_AGENT_TO_MODEL_GATEWAY = "EPHEMERAL_AGENT_TO_MODEL_GATEWAY"
    EPHEMERAL_AGENT_TO_TOOL_GATEWAY = "EPHEMERAL_AGENT_TO_TOOL_GATEWAY"
    INTEGRATION_TO_EXPLICIT_EXTERNAL_DESTINATION = "INTEGRATION_TO_EXPLICIT_EXTERNAL_DESTINATION"


@dataclass(frozen=True, slots=True)
class ServiceBoundaryRule:
    boundary_class: ServiceBoundaryClass
    source_zone: TrustZone | None
    destination_zones: tuple[TrustZone, ...]
    maximum_egress_class: EgressClass
    gateway_required: bool


APPROVED_SERVICE_BOUNDARIES: Final = {
    ServiceBoundaryClass.PUBLIC_OPERATOR_TO_EDGE_API: ServiceBoundaryRule(
        ServiceBoundaryClass.PUBLIC_OPERATOR_TO_EDGE_API,
        None,
        (TrustZone.EDGE_API,),
        EgressClass.NO_EGRESS,
        False,
    ),
    ServiceBoundaryClass.EDGE_API_TO_APPLICATION: ServiceBoundaryRule(
        ServiceBoundaryClass.EDGE_API_TO_APPLICATION,
        TrustZone.EDGE_API,
        (TrustZone.APPLICATION,),
        EgressClass.INTERNAL_GOVERNED_SERVICE,
        False,
    ),
    ServiceBoundaryClass.APPLICATION_TO_DATA: ServiceBoundaryRule(
        ServiceBoundaryClass.APPLICATION_TO_DATA,
        TrustZone.APPLICATION,
        (TrustZone.DATA,),
        EgressClass.INTERNAL_GOVERNED_SERVICE,
        False,
    ),
    ServiceBoundaryClass.APPLICATION_TO_AI_VIA_MODEL_GATEWAY: ServiceBoundaryRule(
        ServiceBoundaryClass.APPLICATION_TO_AI_VIA_MODEL_GATEWAY,
        TrustZone.APPLICATION,
        (TrustZone.AI,),
        EgressClass.MODEL_GATEWAY_ONLY,
        True,
    ),
    ServiceBoundaryClass.SECURITY_OBSERVABILITY_GOVERNANCE: ServiceBoundaryRule(
        ServiceBoundaryClass.SECURITY_OBSERVABILITY_GOVERNANCE,
        TrustZone.SECURITY_OBSERVABILITY,
        (
            TrustZone.EDGE_API,
            TrustZone.APPLICATION,
            TrustZone.DATA,
            TrustZone.AI,
            TrustZone.INTEGRATION,
        ),
        EgressClass.INTERNAL_GOVERNED_SERVICE,
        False,
    ),
    ServiceBoundaryClass.MANAGEMENT_GOVERNANCE_CONTROL: ServiceBoundaryRule(
        ServiceBoundaryClass.MANAGEMENT_GOVERNANCE_CONTROL,
        TrustZone.MANAGEMENT_GOVERNANCE,
        tuple(TrustZone),
        EgressClass.INTERNAL_GOVERNED_SERVICE,
        False,
    ),
    ServiceBoundaryClass.EPHEMERAL_AGENT_TO_MODEL_GATEWAY: ServiceBoundaryRule(
        ServiceBoundaryClass.EPHEMERAL_AGENT_TO_MODEL_GATEWAY,
        TrustZone.AI,
        (TrustZone.AI,),
        EgressClass.MODEL_GATEWAY_ONLY,
        True,
    ),
    ServiceBoundaryClass.EPHEMERAL_AGENT_TO_TOOL_GATEWAY: ServiceBoundaryRule(
        ServiceBoundaryClass.EPHEMERAL_AGENT_TO_TOOL_GATEWAY,
        TrustZone.AI,
        (TrustZone.INTEGRATION,),
        EgressClass.TOOL_GATEWAY_ONLY,
        True,
    ),
    ServiceBoundaryClass.INTEGRATION_TO_EXPLICIT_EXTERNAL_DESTINATION: ServiceBoundaryRule(
        ServiceBoundaryClass.INTEGRATION_TO_EXPLICIT_EXTERNAL_DESTINATION,
        TrustZone.INTEGRATION,
        (TrustZone.INTEGRATION,),
        EgressClass.EXPLICIT_EXTERNAL_DESTINATION,
        True,
    ),
}


@dataclass(frozen=True, slots=True)
class EgressPolicyContract:
    policy_reference: str
    policy_version: str
    boundary_class: ServiceBoundaryClass
    egress_class: EgressClass
    destination_reference: str
    purpose_reference: str
    classification_reference: str
    retention_reference: str
    residency_reference: str
    effective_from: datetime
    expires_at: datetime
    revoked_at: datetime | None = None

    def __post_init__(self) -> None:
        for value, label in (
            (self.policy_reference, "Egress policy reference"),
            (self.policy_version, "Egress policy version"),
            (self.destination_reference, "Egress destination reference"),
            (self.purpose_reference, "Egress purpose reference"),
            (self.classification_reference, "Egress classification reference"),
            (self.retention_reference, "Egress retention reference"),
            (self.residency_reference, "Egress residency reference"),
        ):
            _validate_reference(value, label)
        if self.egress_class is EgressClass.NO_EGRESS:
            raise SecurityProtectionContractError("NO_EGRESS cannot create an allow entry")
        rule = APPROVED_SERVICE_BOUNDARIES[self.boundary_class]
        if self.egress_class is not rule.maximum_egress_class:
            raise SecurityProtectionContractError(
                "Egress class exceeds or conflicts with the service boundary"
            )
        _validate_window(self.effective_from, self.expires_at, "Egress policy")
        if self.revoked_at is not None:
            _validate_instant(self.revoked_at, "Egress policy revocation")

    def is_current(self, at: datetime) -> bool:
        _validate_instant(at, "Egress policy evaluation time")
        return self.effective_from <= at < self.expires_at and (
            self.revoked_at is None or at < self.revoked_at
        )


class EgressPolicyRegistry:
    def __init__(self, policies: tuple[EgressPolicyContract, ...] = ()) -> None:
        references = tuple(policy.policy_reference for policy in policies)
        if len(references) != len(set(references)):
            raise SecurityProtectionContractError("Egress policy references must be unique")
        self._policies = policies

    def matches(self, request: EgressEvaluationRequest) -> tuple[EgressPolicyContract, ...]:
        return tuple(
            policy
            for policy in self._policies
            if policy.policy_version == request.policy_version
            and policy.boundary_class is request.boundary_class
            and policy.egress_class is request.egress_class
            and policy.destination_reference == request.destination_reference
            and policy.purpose_reference == request.purpose_reference
            and policy.classification_reference == request.classification_reference
            and policy.retention_reference == request.retention_reference
            and policy.residency_reference == request.residency_reference
        )

    def is_empty(self) -> bool:
        return not self._policies


EMPTY_EGRESS_POLICY_REGISTRY: Final = EgressPolicyRegistry()


@dataclass(frozen=True, slots=True)
class AgentEgressCeiling:
    sandbox_permits: bool
    task_contract_permits: bool
    identity_permits: bool
    destination_eligible: bool
    classification_permits: bool
    purpose_permits: bool
    retention_permits: bool
    residency_sovereignty_permits: bool

    def permits(self) -> bool:
        return all(
            (
                self.sandbox_permits,
                self.task_contract_permits,
                self.identity_permits,
                self.destination_eligible,
                self.classification_permits,
                self.purpose_permits,
                self.retention_permits,
                self.residency_sovereignty_permits,
            )
        )


@dataclass(frozen=True, slots=True)
class EgressEvaluationRequest:
    request_reference: str
    correlation_id: str
    boundary_class: ServiceBoundaryClass
    source_zone: TrustZone | None
    destination_zone: TrustZone
    egress_class: EgressClass
    destination_reference: str
    service_identity_reference: str
    action_reference: str
    purpose_reference: str
    classification_reference: str
    retention_reference: str
    residency_reference: str
    policy_version: str
    authorization_decision: CurrentAuthorizationDecision
    gateway_reference: str | None = None
    agent_ceiling: AgentEgressCeiling | None = None
    external_boundary: bool = False
    cross_border: bool = False
    provider_eligible: bool = False
    human_cross_border_authorized: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Egress request reference"),
            (self.correlation_id, "Egress correlation reference"),
            (self.destination_reference, "Egress destination reference"),
            (self.service_identity_reference, "Egress service identity reference"),
            (self.action_reference, "Egress action reference"),
            (self.purpose_reference, "Egress purpose reference"),
            (self.classification_reference, "Egress classification reference"),
            (self.retention_reference, "Egress retention reference"),
            (self.residency_reference, "Egress residency reference"),
            (self.policy_version, "Egress policy version"),
        ):
            _validate_reference(value, label)
        _validate_optional_reference(self.gateway_reference, "Egress gateway reference")


class EgressValidationCode(StrEnum):
    VALID_CONTRACT = "VALID_CONTRACT"
    NO_CURRENT_AUTHORIZATION = "NO_CURRENT_AUTHORIZATION"
    BOUNDARY_MISMATCH = "BOUNDARY_MISMATCH"
    GATEWAY_REQUIRED = "GATEWAY_REQUIRED"
    NO_EGRESS = "NO_EGRESS"
    AGENT_CEILING_DENIED = "AGENT_CEILING_DENIED"
    NO_CURRENT_EGRESS_POLICY = "NO_CURRENT_EGRESS_POLICY"
    AMBIGUOUS_EGRESS_POLICY = "AMBIGUOUS_EGRESS_POLICY"
    POLICY_EXPIRED_OR_REVOKED = "POLICY_EXPIRED_OR_REVOKED"
    EXTERNAL_PROVIDER_INELIGIBLE = "EXTERNAL_PROVIDER_INELIGIBLE"
    EXTERNAL_BOUNDARY_REQUIRED = "EXTERNAL_BOUNDARY_REQUIRED"
    CROSS_BORDER_NOT_AUTHORIZED = "CROSS_BORDER_NOT_AUTHORIZED"


@dataclass(frozen=True, slots=True)
class EgressValidationResult:
    allowed: bool
    code: EgressValidationCode
    network_activated: bool = False


class EgressPolicyEvaluator:
    def __init__(self, registry: EgressPolicyRegistry = EMPTY_EGRESS_POLICY_REGISTRY) -> None:
        self._registry = registry

    def evaluate(self, request: EgressEvaluationRequest, *, at: datetime) -> EgressValidationResult:
        _validate_instant(at, "Egress evaluation time")
        authorization = request.authorization_decision
        if (
            authorization.effect is not AuthorizationEffect.PERMIT
            or authorization.request_reference != request.request_reference
            or authorization.policy_version != request.policy_version
        ):
            return EgressValidationResult(False, EgressValidationCode.NO_CURRENT_AUTHORIZATION)
        rule = APPROVED_SERVICE_BOUNDARIES[request.boundary_class]
        if (
            rule.source_zone is not request.source_zone
            or request.destination_zone not in rule.destination_zones
            or rule.maximum_egress_class is not request.egress_class
        ):
            return EgressValidationResult(False, EgressValidationCode.BOUNDARY_MISMATCH)
        if rule.gateway_required and request.gateway_reference is None:
            return EgressValidationResult(False, EgressValidationCode.GATEWAY_REQUIRED)
        if request.egress_class is EgressClass.NO_EGRESS:
            return EgressValidationResult(False, EgressValidationCode.NO_EGRESS)
        if (
            request.egress_class is EgressClass.EXPLICIT_EXTERNAL_DESTINATION
            and not request.external_boundary
        ):
            return EgressValidationResult(False, EgressValidationCode.EXTERNAL_BOUNDARY_REQUIRED)
        if request.agent_ceiling is not None and not request.agent_ceiling.permits():
            return EgressValidationResult(False, EgressValidationCode.AGENT_CEILING_DENIED)
        matches = self._registry.matches(request)
        if not matches:
            return EgressValidationResult(False, EgressValidationCode.NO_CURRENT_EGRESS_POLICY)
        if len(matches) != 1:
            return EgressValidationResult(False, EgressValidationCode.AMBIGUOUS_EGRESS_POLICY)
        if not matches[0].is_current(at):
            return EgressValidationResult(False, EgressValidationCode.POLICY_EXPIRED_OR_REVOKED)
        if request.external_boundary and not request.provider_eligible:
            return EgressValidationResult(False, EgressValidationCode.EXTERNAL_PROVIDER_INELIGIBLE)
        if request.cross_border and not request.human_cross_border_authorized:
            return EgressValidationResult(False, EgressValidationCode.CROSS_BORDER_NOT_AUTHORIZED)
        return EgressValidationResult(True, EgressValidationCode.VALID_CONTRACT)


class SecurityProtectionSignals:
    """Emit minimized condition signals; never Evidence or an operational control."""

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
        for value, label in (
            (correlation_id, "Signal correlation reference"),
            (contract_class, "Signal contract class"),
            (outcome, "Signal outcome"),
            (reason_code, "Signal reason code"),
        ):
            _validate_reference(value, label)
        self._sink.emit_event(
            OperationalEvent(
                category=SignalCategory.SECURITY_CONDITION,
                name="security.protection.condition",
                correlation_id=correlation_id,
                attributes=(
                    ("contract_class", contract_class),
                    ("outcome", outcome),
                    ("reason_code", reason_code),
                ),
            )
        )
