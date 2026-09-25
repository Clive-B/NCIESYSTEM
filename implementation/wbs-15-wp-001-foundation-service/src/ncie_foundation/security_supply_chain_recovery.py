"""Inert supply-chain, vulnerability and security-recovery contracts for WP-009."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from re import compile as compile_pattern
from typing import Final, Protocol

from .agent_model_tool_context_security import UntrustedContentOrigin
from .security_authorization import AuthorizationEffect, CurrentAuthorizationDecision

SUPPLY_CHAIN_RECOVERY_BASELINE_VERSION: Final = "NCIE-WBS16-WP009-2026-09-24"
SUPPLY_CHAIN_RECOVERY_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-24-032"
SUPPLY_CHAIN_RECOVERY_IMPLEMENTATION_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-24-033"

_REFERENCE_PATTERN: Final = compile_pattern(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}")
_DENY_SENTINELS: Final = frozenset({"unassigned", "unspecified", "unknown"})
_PROHIBITED_FRAGMENTS: Final = (
    "-----begin",
    "artifact_payload",
    "chain_of_thought",
    "credential_value",
    "document_payload",
    "evidence_payload",
    "identity_value",
    "memory_payload",
    "password",
    "private_key",
    "prompt_text",
    "raw_prompt",
    "secret_value",
    "source_payload",
    "token_value",
    "tool_result_content",
)


class SupplyChainRecoveryContractError(ValueError):
    """Raised without echoing prohibited input when a WP-009 contract is invalid."""


def _validate_reference(value: str, label: str) -> None:
    normalized = value.lower()
    if (
        _REFERENCE_PATTERN.fullmatch(value) is None
        or normalized in _DENY_SENTINELS
        or any(fragment in normalized for fragment in _PROHIBITED_FRAGMENTS)
    ):
        raise SupplyChainRecoveryContractError(
            f"{label} is invalid or contains prohibited material"
        )


def _validate_optional_reference(value: str | None, label: str) -> None:
    if value is not None:
        _validate_reference(value, label)


def _validate_references(values: tuple[str, ...], label: str, *, required: bool = True) -> None:
    if required and not values:
        raise SupplyChainRecoveryContractError(f"{label} is required")
    if len(values) != len(set(values)):
        raise SupplyChainRecoveryContractError(f"{label} must not contain duplicates")
    for value in values:
        _validate_reference(value, label)


def _validate_instant(value: datetime, label: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise SupplyChainRecoveryContractError(f"{label} must include a timezone")


def _validate_window(effective_at: datetime, expires_at: datetime, label: str) -> None:
    _validate_instant(effective_at, f"{label} effective time")
    _validate_instant(expires_at, f"{label} expiry")
    if expires_at <= effective_at:
        raise SupplyChainRecoveryContractError(f"{label} expiry must follow effective time")


def _current_permit(
    decision: CurrentAuthorizationDecision | None,
    *,
    request_reference: str,
    policy_version: str,
) -> bool:
    return bool(
        decision is not None
        and decision.request_reference == request_reference
        and decision.policy_version == policy_version
        and decision.effect is AuthorizationEffect.PERMIT
    )


class SupplyChainDisposition(StrEnum):
    DENY = "DENY"
    QUARANTINE = "QUARANTINE"
    HUMAN_DECISION_REQUIRED = "HUMAN_DECISION_REQUIRED"
    REMEDIATION_REQUIRED = "REMEDIATION_REQUIRED"
    RECONCILIATION_REQUIRED = "RECONCILIATION_REQUIRED"
    INDETERMINATE_DENY = "INDETERMINATE_DENY"


class ArtifactIntegrityState(StrEnum):
    UNVERIFIED = "UNVERIFIED"
    VERIFICATION_REQUIRED = "VERIFICATION_REQUIRED"
    VERIFIED_METADATA_ONLY = "VERIFIED_METADATA_ONLY"
    COMPROMISED = "COMPROMISED"
    INDETERMINATE = "INDETERMINATE"


class ArtifactLifecycleState(StrEnum):
    UNVERIFIED = "UNVERIFIED"
    VERIFICATION_REQUIRED = "VERIFICATION_REQUIRED"
    VERIFIED_METADATA_ONLY = "VERIFIED_METADATA_ONLY"
    QUARANTINED = "QUARANTINED"
    COMPROMISED = "COMPROMISED"
    REVOKED = "REVOKED"
    INDETERMINATE_DENY = "INDETERMINATE_DENY"


class VulnerabilityLifecycleState(StrEnum):
    REPORTED = "REPORTED"
    DETECTED = "DETECTED"
    TRIAGE_REQUIRED = "TRIAGE_REQUIRED"
    REMEDIATION_REQUIRED = "REMEDIATION_REQUIRED"
    MITIGATION_REVIEW_REQUIRED = "MITIGATION_REVIEW_REQUIRED"
    EXCEPTION_REVIEW_REQUIRED = "EXCEPTION_REVIEW_REQUIRED"
    VERIFICATION_REQUIRED = "VERIFICATION_REQUIRED"
    UNRESOLVED = "UNRESOLVED"
    STALE = "STALE"
    INDETERMINATE_DENY = "INDETERMINATE_DENY"


class RecoveryIntegrityState(StrEnum):
    KNOWN_GOOD_REFERENCE_ONLY = "KNOWN_GOOD_REFERENCE_ONLY"
    UNKNOWN = "UNKNOWN"
    SUSPECTED_COMPROMISED = "SUSPECTED_COMPROMISED"
    COMPROMISED = "COMPROMISED"
    QUARANTINED = "QUARANTINED"
    VERIFICATION_REQUIRED = "VERIFICATION_REQUIRED"
    INDETERMINATE_DENY = "INDETERMINATE_DENY"


class NonWaivableSupplyChainRecoveryProtection(StrEnum):
    HUMAN_PRIMARY_AUTHORITY = "HUMAN_PRIMARY_AUTHORITY"
    CURRENT_FOUR_LAYER_AUTHORIZATION = "CURRENT_FOUR_LAYER_AUTHORIZATION"
    EXACT_PROVENANCE_VERSION_INTEGRITY = "EXACT_PROVENANCE_VERSION_INTEGRITY"
    ARTIFACT_STAGE_SEPARATION = "ARTIFACT_STAGE_SEPARATION"
    GENERATED_CODE_WP006_QUARANTINE = "GENERATED_CODE_WP006_QUARANTINE"
    INDEPENDENCE_NO_SELF_APPROVAL = "INDEPENDENCE_NO_SELF_APPROVAL"
    COMPROMISED_REVOKED_UNVERIFIABLE_QUARANTINE = "COMPROMISED_REVOKED_UNVERIFIABLE_QUARANTINE"
    ACCEPTANCE_EXACT_REVOCABLE_NO_DEPLOYMENT = "ACCEPTANCE_EXACT_REVOCABLE_NO_DEPLOYMENT"
    VULNERABILITY_STAGE_SEPARATION = "VULNERABILITY_STAGE_SEPARATION"
    SEVERITY_SCANNER_TIME_NOT_AUTHORITY = "SEVERITY_SCANNER_TIME_NOT_AUTHORITY"
    EXCEPTION_EXACT_EXPIRING_REVIEWED = "EXCEPTION_EXACT_EXPIRING_REVIEWED"
    STALE_OR_UNASSIGNED_TREATMENT_DENIES = "STALE_OR_UNASSIGNED_TREATMENT_DENIES"
    UNKNOWN_RECOVERY_STATE_COMPROMISED = "UNKNOWN_RECOVERY_STATE_COMPROMISED"
    RECOVERY_PRESERVES_CURRENT_SECURITY_STATE = "RECOVERY_PRESERVES_CURRENT_SECURITY_STATE"
    INVALIDATION_OBLIGATION_NOT_EXECUTION = "INVALIDATION_OBLIGATION_NOT_EXECUTION"
    RECOVERY_RESTORATION_REAUTHORIZATION_SEPARATION = (
        "RECOVERY_RESTORATION_REAUTHORIZATION_SEPARATION"
    )
    WBS20_WBS23_NCIE016_BOUNDARIES = "WBS20_WBS23_NCIE016_BOUNDARIES"
    SYNTHETIC_MINIMIZED_RESIDENCY_DENY = "SYNTHETIC_MINIMIZED_RESIDENCY_DENY"


ALL_SUPPLY_CHAIN_RECOVERY_PROTECTIONS: Final = frozenset(NonWaivableSupplyChainRecoveryProtection)


class Wp009AuthorityClass(StrEnum):
    ARTIFACT_ACCEPTANCE = "ARTIFACT_ACCEPTANCE"
    SUPPLY_CHAIN_SECURITY_OWNER = "SUPPLY_CHAIN_SECURITY_OWNER"
    PROVENANCE_INTEGRITY_POLICY = "PROVENANCE_INTEGRITY_POLICY"
    ARTIFACT_VERIFICATION = "ARTIFACT_VERIFICATION"
    VERIFICATION_CRITERIA_APPROVAL = "VERIFICATION_CRITERIA_APPROVAL"
    QUARANTINE = "QUARANTINE"
    QUARANTINE_RELEASE = "QUARANTINE_RELEASE"
    INDEPENDENT_ENGINEERING_REVIEW = "INDEPENDENT_ENGINEERING_REVIEW"
    INDEPENDENT_SECURITY_REVIEW = "INDEPENDENT_SECURITY_REVIEW"
    GENERATED_CODE_SECURITY_GATE = "GENERATED_CODE_SECURITY_GATE"
    ARTIFACT_ACCEPTANCE_REVOCATION = "ARTIFACT_ACCEPTANCE_REVOCATION"
    PROMOTION = "PROMOTION"
    DEPLOYMENT = "DEPLOYMENT"
    DEPLOYMENT_EXECUTION = "DEPLOYMENT_EXECUTION"
    VULNERABILITY_MANAGEMENT_OWNER = "VULNERABILITY_MANAGEMENT_OWNER"
    VULNERABILITY_TRIAGE = "VULNERABILITY_TRIAGE"
    VULNERABILITY_SEVERITY = "VULNERABILITY_SEVERITY"
    REMEDIATION = "REMEDIATION"
    PATCH_REQUEST = "PATCH_REQUEST"
    PATCH_APPROVAL = "PATCH_APPROVAL"
    PATCH_EXECUTION = "PATCH_EXECUTION"
    MITIGATION_APPROVAL = "MITIGATION_APPROVAL"
    EXCEPTION_REVIEW = "EXCEPTION_REVIEW"
    EXCEPTION_APPROVAL = "EXCEPTION_APPROVAL"
    EXCEPTION_REVOCATION = "EXCEPTION_REVOCATION"
    RESIDUAL_RISK_ACCEPTANCE = "RESIDUAL_RISK_ACCEPTANCE"
    FINDING = "FINDING"
    REMEDIATION_VERIFICATION = "REMEDIATION_VERIFICATION"
    SECURITY_ACCEPTANCE = "SECURITY_ACCEPTANCE"
    RECOVERY_SECURITY_OWNER = "RECOVERY_SECURITY_OWNER"
    COMPROMISED_STATE_DETERMINATION = "COMPROMISED_STATE_DETERMINATION"
    KNOWN_GOOD_DETERMINATION = "KNOWN_GOOD_DETERMINATION"
    RECOVERY_REQUEST = "RECOVERY_REQUEST"
    RECOVERY_APPROVAL = "RECOVERY_APPROVAL"
    RECOVERY_EXECUTION = "RECOVERY_EXECUTION"
    INVALIDATION_ROTATION = "INVALIDATION_ROTATION"
    POST_RECOVERY_RECONCILIATION = "POST_RECOVERY_RECONCILIATION"
    INDEPENDENT_RECOVERY_REVIEW = "INDEPENDENT_RECOVERY_REVIEW"
    SECURITY_RECOVERY_ACCEPTANCE = "SECURITY_RECOVERY_ACCEPTANCE"
    OPERATIONAL_RESTORATION = "OPERATIONAL_RESTORATION"
    REAUTHORIZATION = "REAUTHORIZATION"
    REINSTATEMENT = "REINSTATEMENT"


class Wp009AuthorityBoundary(Protocol):
    def assignment_for(self, authority_class: Wp009AuthorityClass) -> str | None: ...


class UnassignedWp009Authorities:
    """Expose no artifact, vulnerability, recovery or reinstatement authority."""

    def assignment_for(self, authority_class: Wp009AuthorityClass) -> str | None:
        del authority_class
        return None


@dataclass(frozen=True, slots=True)
class ControlledRegistry:
    """Versioned immutable registry; WP-009 controlled instances are empty."""

    registry_class: str
    version: str
    entry_references: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.registry_class, "Registry class")
        _validate_reference(self.version, "Registry version")
        _validate_references(self.entry_references, "Registry entry reference", required=False)

    def is_empty(self) -> bool:
        return not self.entry_references


def _empty_registry(registry_class: str) -> ControlledRegistry:
    return ControlledRegistry(registry_class, SUPPLY_CHAIN_RECOVERY_BASELINE_VERSION)


EMPTY_ARTIFACT_PROVENANCE_POLICY_REGISTRY: Final = _empty_registry("artifact-provenance-policy")
EMPTY_ARTIFACT_INTEGRITY_VERSION_REGISTRY: Final = _empty_registry(
    "artifact-integrity-version-policy"
)
EMPTY_DEPENDENCY_BUILD_PROVENANCE_REGISTRY: Final = _empty_registry(
    "dependency-build-provenance-policy"
)
EMPTY_ARTIFACT_VERIFICATION_CRITERIA_REGISTRY: Final = _empty_registry(
    "artifact-verification-criteria"
)
EMPTY_ARTIFACT_QUARANTINE_REGISTRY: Final = _empty_registry("artifact-quarantine-policy")
EMPTY_GENERATED_CODE_GATE_REGISTRY: Final = _empty_registry("generated-code-security-gate")
EMPTY_ARTIFACT_REVIEW_ASSIGNMENT_REGISTRY: Final = _empty_registry(
    "artifact-independent-review-assignment"
)
EMPTY_ARTIFACT_ACCEPTANCE_REGISTRY: Final = _empty_registry("artifact-acceptance")
EMPTY_ARTIFACT_ACCEPTANCE_REVOCATION_REGISTRY: Final = _empty_registry(
    "artifact-acceptance-revocation"
)
EMPTY_VULNERABILITY_POLICY_REGISTRY: Final = _empty_registry("vulnerability-policy")
EMPTY_VULNERABILITY_SEVERITY_REGISTRY: Final = _empty_registry("vulnerability-severity-governance")
EMPTY_REMEDIATION_REQUIREMENT_REGISTRY: Final = _empty_registry("remediation-requirement")
EMPTY_COMPENSATING_CONTROL_REGISTRY: Final = _empty_registry("compensating-control")
EMPTY_EXCEPTION_ELIGIBILITY_REGISTRY: Final = _empty_registry("exception-eligibility")
EMPTY_SECURITY_EXCEPTION_REGISTRY: Final = _empty_registry("security-exception")
EMPTY_RESIDUAL_RISK_ACCEPTANCE_REGISTRY: Final = _empty_registry("residual-risk-acceptance")
EMPTY_VULNERABILITY_REVIEW_ASSIGNMENT_REGISTRY: Final = _empty_registry(
    "vulnerability-independent-review-assignment"
)
EMPTY_SECURITY_ACCEPTANCE_REGISTRY: Final = _empty_registry("security-acceptance")
EMPTY_RECOVERY_SOURCE_CRITERIA_REGISTRY: Final = _empty_registry("recovery-source-criteria")
EMPTY_KNOWN_GOOD_CRITERIA_REGISTRY: Final = _empty_registry("known-good-criteria")
EMPTY_COMPROMISED_STATE_RULE_REGISTRY: Final = _empty_registry("compromised-state-rule")
EMPTY_RECOVERY_QUARANTINE_REGISTRY: Final = _empty_registry("recovery-quarantine-policy")
EMPTY_INVALIDATION_OBLIGATION_REGISTRY: Final = _empty_registry("invalidation-obligation-policy")
EMPTY_RECONCILIATION_REQUIREMENT_REGISTRY: Final = _empty_registry(
    "post-recovery-reconciliation-requirement"
)
EMPTY_RECOVERY_AUTHORITY_REGISTRY: Final = _empty_registry("recovery-authority")
EMPTY_RECOVERY_REVIEW_ASSIGNMENT_REGISTRY: Final = _empty_registry(
    "independent-recovery-review-assignment"
)
EMPTY_SECURITY_RECOVERY_ACCEPTANCE_REGISTRY: Final = _empty_registry("security-recovery-acceptance")
EMPTY_RESTORATION_AUTHORITY_REGISTRY: Final = _empty_registry("restoration-authority")
EMPTY_REAUTHORIZATION_AUTHORITY_REGISTRY: Final = _empty_registry("reauthorization-authority")
EMPTY_REINSTATEMENT_AUTHORITY_REGISTRY: Final = _empty_registry("reinstatement-authority")

ALL_WP009_CONTROLLED_REGISTRIES: Final = (
    EMPTY_ARTIFACT_PROVENANCE_POLICY_REGISTRY,
    EMPTY_ARTIFACT_INTEGRITY_VERSION_REGISTRY,
    EMPTY_DEPENDENCY_BUILD_PROVENANCE_REGISTRY,
    EMPTY_ARTIFACT_VERIFICATION_CRITERIA_REGISTRY,
    EMPTY_ARTIFACT_QUARANTINE_REGISTRY,
    EMPTY_GENERATED_CODE_GATE_REGISTRY,
    EMPTY_ARTIFACT_REVIEW_ASSIGNMENT_REGISTRY,
    EMPTY_ARTIFACT_ACCEPTANCE_REGISTRY,
    EMPTY_ARTIFACT_ACCEPTANCE_REVOCATION_REGISTRY,
    EMPTY_VULNERABILITY_POLICY_REGISTRY,
    EMPTY_VULNERABILITY_SEVERITY_REGISTRY,
    EMPTY_REMEDIATION_REQUIREMENT_REGISTRY,
    EMPTY_COMPENSATING_CONTROL_REGISTRY,
    EMPTY_EXCEPTION_ELIGIBILITY_REGISTRY,
    EMPTY_SECURITY_EXCEPTION_REGISTRY,
    EMPTY_RESIDUAL_RISK_ACCEPTANCE_REGISTRY,
    EMPTY_VULNERABILITY_REVIEW_ASSIGNMENT_REGISTRY,
    EMPTY_SECURITY_ACCEPTANCE_REGISTRY,
    EMPTY_RECOVERY_SOURCE_CRITERIA_REGISTRY,
    EMPTY_KNOWN_GOOD_CRITERIA_REGISTRY,
    EMPTY_COMPROMISED_STATE_RULE_REGISTRY,
    EMPTY_RECOVERY_QUARANTINE_REGISTRY,
    EMPTY_INVALIDATION_OBLIGATION_REGISTRY,
    EMPTY_RECONCILIATION_REQUIREMENT_REGISTRY,
    EMPTY_RECOVERY_AUTHORITY_REGISTRY,
    EMPTY_RECOVERY_REVIEW_ASSIGNMENT_REGISTRY,
    EMPTY_SECURITY_RECOVERY_ACCEPTANCE_REGISTRY,
    EMPTY_RESTORATION_AUTHORITY_REGISTRY,
    EMPTY_REAUTHORIZATION_AUTHORITY_REGISTRY,
    EMPTY_REINSTATEMENT_AUTHORITY_REGISTRY,
)


@dataclass(frozen=True, slots=True)
class ArtifactProvenanceMetadata:
    artifact_reference: str
    artifact_class_reference: str
    exact_version_reference: str
    source_reference: str
    producer_class_reference: str
    producing_process_reference: str
    integrity_reference: str
    dependency_manifest_reference: str
    build_reference: str
    builder_class_reference: str
    build_input_references: tuple[str, ...]
    provenance_policy_version: str
    residency_reference: str
    integrity_state: ArtifactIntegrityState
    generated_code: bool = False
    synthetic: bool = True
    authoritative: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.artifact_reference, "Artifact reference"),
            (self.artifact_class_reference, "Artifact-class reference"),
            (self.exact_version_reference, "Artifact exact-version reference"),
            (self.source_reference, "Artifact source reference"),
            (self.producer_class_reference, "Artifact producer-class reference"),
            (self.producing_process_reference, "Artifact producing-process reference"),
            (self.integrity_reference, "Artifact integrity reference"),
            (self.dependency_manifest_reference, "Dependency-manifest reference"),
            (self.build_reference, "Build reference"),
            (self.builder_class_reference, "Builder-class reference"),
            (self.provenance_policy_version, "Provenance policy version"),
            (self.residency_reference, "Artifact residency reference"),
        ):
            _validate_reference(value, label)
        _validate_references(self.build_input_references, "Build-input reference")
        if not self.synthetic or self.authoritative:
            raise SupplyChainRecoveryContractError(
                "WP-009 artifact metadata must be synthetic and non-authoritative"
            )


@dataclass(frozen=True, slots=True)
class ArtifactVerificationRecord:
    verification_reference: str
    artifact_reference: str
    exact_version_reference: str
    criteria_reference: str
    reviewer_reference: str
    producer_reference: str
    implementer_reference: str
    verified_at: datetime
    policy_version: str
    verified: bool
    independent: bool
    synthetic: bool = True
    authoritative: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.verification_reference, "Artifact-verification reference"),
            (self.artifact_reference, "Verified artifact reference"),
            (self.exact_version_reference, "Verified exact-version reference"),
            (self.criteria_reference, "Verification-criteria reference"),
            (self.reviewer_reference, "Artifact reviewer reference"),
            (self.producer_reference, "Artifact producer reference"),
            (self.implementer_reference, "Artifact implementer reference"),
            (self.policy_version, "Artifact-verification policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.verified_at, "Artifact-verification time")
        if not self.independent or self.reviewer_reference in {
            self.producer_reference,
            self.implementer_reference,
        }:
            raise SupplyChainRecoveryContractError(
                "Artifact review must be independent of producer and implementer"
            )
        if not self.synthetic or self.authoritative:
            raise SupplyChainRecoveryContractError(
                "WP-009 verification metadata must be synthetic and non-authoritative"
            )


@dataclass(frozen=True, slots=True)
class ArtifactAcceptanceRecord:
    acceptance_reference: str
    artifact_reference: str
    exact_version_reference: str
    scope_reference: str
    authority_reference: str
    effective_at: datetime
    expires_at: datetime
    policy_version: str
    accepted: bool
    revoked: bool = False
    synthetic: bool = True
    authoritative: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.acceptance_reference, "Artifact-acceptance reference"),
            (self.artifact_reference, "Accepted artifact reference"),
            (self.exact_version_reference, "Accepted exact-version reference"),
            (self.scope_reference, "Artifact-acceptance scope reference"),
            (self.authority_reference, "Artifact-acceptance authority reference"),
            (self.policy_version, "Artifact-acceptance policy version"),
        ):
            _validate_reference(value, label)
        _validate_window(self.effective_at, self.expires_at, "Artifact acceptance")
        if not self.synthetic or self.authoritative:
            raise SupplyChainRecoveryContractError(
                "WP-009 acceptance metadata must be synthetic and non-authoritative"
            )


@dataclass(frozen=True, slots=True)
class ArtifactRevocationRecord:
    revocation_reference: str
    acceptance_reference: str
    artifact_reference: str
    exact_version_reference: str
    revoked_at: datetime
    authority_reference: str
    policy_version: str
    prospective: bool = True

    def __post_init__(self) -> None:
        for value, label in (
            (self.revocation_reference, "Artifact-revocation reference"),
            (self.acceptance_reference, "Revoked acceptance reference"),
            (self.artifact_reference, "Revoked artifact reference"),
            (self.exact_version_reference, "Revoked exact-version reference"),
            (self.authority_reference, "Artifact-revocation authority reference"),
            (self.policy_version, "Artifact-revocation policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.revoked_at, "Artifact-revocation time")
        if not self.prospective:
            raise SupplyChainRecoveryContractError(
                "Artifact revocation cannot erase historical acceptance metadata"
            )


@dataclass(frozen=True, slots=True)
class ArtifactQuarantineRecord:
    quarantine_reference: str
    artifact_reference: str
    exact_version_reference: str
    reason_code: str
    entered_at: datetime
    policy_version: str
    quarantined: bool = True
    released: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.quarantine_reference, "Artifact-quarantine reference"),
            (self.artifact_reference, "Quarantined artifact reference"),
            (self.exact_version_reference, "Quarantined exact-version reference"),
            (self.reason_code, "Artifact-quarantine reason"),
            (self.policy_version, "Artifact-quarantine policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.entered_at, "Artifact-quarantine entry time")
        if not self.quarantined or self.released:
            raise SupplyChainRecoveryContractError("WP-009 artifact quarantine cannot be released")


@dataclass(frozen=True, slots=True)
class GeneratedCodeSecurityGateRecord:
    gate_reference: str
    artifact_reference: str
    exact_version_reference: str
    criteria_reference: str
    reviewer_reference: str
    generator_reference: str
    implementer_reference: str
    policy_version: str
    passed: bool = False
    execution_approved: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.gate_reference, "Generated-code gate reference"),
            (self.artifact_reference, "Generated artifact reference"),
            (self.exact_version_reference, "Generated artifact exact-version reference"),
            (self.criteria_reference, "Generated-code gate criteria reference"),
            (self.reviewer_reference, "Generated-code reviewer reference"),
            (self.generator_reference, "Generated-code generator reference"),
            (self.implementer_reference, "Generated-code implementer reference"),
            (self.policy_version, "Generated-code gate policy version"),
        ):
            _validate_reference(value, label)
        if self.reviewer_reference in {
            self.generator_reference,
            self.implementer_reference,
        }:
            raise SupplyChainRecoveryContractError(
                "Generated-code review must be independent of generator and implementer"
            )
        if self.passed or self.execution_approved:
            raise SupplyChainRecoveryContractError(
                "Generated code remains NOT_APPROVED_FOR_EXECUTION under WP-006"
            )


@dataclass(frozen=True, slots=True)
class ArtifactPromotionReference:
    promotion_reference: str
    artifact_reference: str
    exact_version_reference: str
    acceptance_reference: str
    promoted: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.promotion_reference, "Artifact-promotion reference"),
            (self.artifact_reference, "Promotion artifact reference"),
            (self.exact_version_reference, "Promotion exact-version reference"),
            (self.acceptance_reference, "Promotion acceptance reference"),
        ):
            _validate_reference(value, label)
        if self.promoted:
            raise SupplyChainRecoveryContractError("WP-009 cannot promote an artifact")


@dataclass(frozen=True, slots=True)
class ArtifactDeploymentReference:
    deployment_reference: str
    artifact_reference: str
    exact_version_reference: str
    promotion_reference: str
    deployed: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.deployment_reference, "Artifact-deployment reference"),
            (self.artifact_reference, "Deployment artifact reference"),
            (self.exact_version_reference, "Deployment exact-version reference"),
            (self.promotion_reference, "Deployment promotion reference"),
        ):
            _validate_reference(value, label)
        if self.deployed:
            raise SupplyChainRecoveryContractError("WP-009 cannot deploy an artifact")


@dataclass(frozen=True, slots=True)
class ArtifactTransitionReferences:
    artifact_reference: str
    exact_version_reference: str
    acceptance_reference: str | None = None
    promotion_reference: str | None = None
    deployment_reference: str | None = None
    promoted: bool = False
    deployed: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.artifact_reference, "Transition artifact reference")
        _validate_reference(self.exact_version_reference, "Transition version reference")
        _validate_optional_reference(self.acceptance_reference, "Transition acceptance reference")
        _validate_optional_reference(self.promotion_reference, "Promotion reference")
        _validate_optional_reference(self.deployment_reference, "Deployment reference")
        if self.promoted or self.deployed:
            raise SupplyChainRecoveryContractError("WP-009 cannot promote or deploy an artifact")


@dataclass(frozen=True, slots=True)
class SymbolicVulnerabilitySeverity:
    severity_class_reference: str | None
    policy_version: str
    assigning_authority_reference: str | None = None
    operational_threshold_selected: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.policy_version, "Vulnerability-severity policy version")
        _validate_optional_reference(
            self.severity_class_reference, "Vulnerability-severity class reference"
        )
        _validate_optional_reference(
            self.assigning_authority_reference,
            "Vulnerability-severity assigning-authority reference",
        )
        if self.operational_threshold_selected:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot select an operational vulnerability threshold"
            )


UNSPECIFIED_VULNERABILITY_SEVERITY: Final = SymbolicVulnerabilitySeverity(
    None, SUPPLY_CHAIN_RECOVERY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class VulnerabilityRecord:
    vulnerability_reference: str
    affected_artifact_reference: str
    affected_component_reference: str
    exact_version_reference: str
    source_reference: str
    detected_at: datetime
    known_at: datetime
    provenance_references: tuple[str, ...]
    policy_version: str
    state: VulnerabilityLifecycleState
    severity: SymbolicVulnerabilitySeverity = UNSPECIFIED_VULNERABILITY_SEVERITY
    synthetic: bool = True
    authoritative_finding: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.vulnerability_reference, "Vulnerability reference"),
            (self.affected_artifact_reference, "Affected artifact reference"),
            (self.affected_component_reference, "Affected component reference"),
            (self.exact_version_reference, "Affected exact-version reference"),
            (self.source_reference, "Vulnerability source reference"),
            (self.policy_version, "Vulnerability policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.detected_at, "Vulnerability detection time")
        _validate_instant(self.known_at, "Vulnerability knowledge time")
        _validate_references(self.provenance_references, "Vulnerability provenance reference")
        if self.known_at < self.detected_at:
            raise SupplyChainRecoveryContractError(
                "Vulnerability knowledge time must not precede detection time"
            )
        if not self.synthetic or self.authoritative_finding:
            raise SupplyChainRecoveryContractError(
                "WP-009 vulnerability metadata cannot be an institutional Finding"
            )


@dataclass(frozen=True, slots=True)
class RemediationRecord:
    remediation_reference: str
    vulnerability_reference: str
    affected_component_reference: str
    exact_version_reference: str
    proposed_artifact_reference: str
    verification_reference: str | None
    policy_version: str
    reported_complete: bool = False
    independently_verified: bool = False
    security_accepted: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.remediation_reference, "Remediation reference"),
            (self.vulnerability_reference, "Remediation vulnerability reference"),
            (self.affected_component_reference, "Remediation component reference"),
            (self.exact_version_reference, "Remediation exact-version reference"),
            (self.proposed_artifact_reference, "Remediation proposed-artifact reference"),
            (self.policy_version, "Remediation policy version"),
        ):
            _validate_reference(value, label)
        _validate_optional_reference(self.verification_reference, "Remediation verification")
        if self.reported_complete or self.independently_verified or self.security_accepted:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot complete, verify or security-accept remediation"
            )


@dataclass(frozen=True, slots=True)
class MitigationRecord:
    mitigation_reference: str
    vulnerability_reference: str
    affected_component_reference: str
    exact_version_reference: str
    compensating_control_references: tuple[str, ...]
    policy_version: str
    applied: bool = False
    independently_verified: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.mitigation_reference, "Mitigation reference"),
            (self.vulnerability_reference, "Mitigation vulnerability reference"),
            (self.affected_component_reference, "Mitigation component reference"),
            (self.exact_version_reference, "Mitigation exact-version reference"),
            (self.policy_version, "Mitigation policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(
            self.compensating_control_references, "Mitigation compensating-control reference"
        )
        if self.applied or self.independently_verified:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot apply or verify a live mitigation"
            )


@dataclass(frozen=True, slots=True)
class SecurityExceptionRecord:
    exception_reference: str
    vulnerability_reference: str
    affected_component_reference: str
    exact_version_reference: str
    scope_reference: str
    requester_reference: str
    reviewer_reference: str
    approver_reference: str
    compensating_control_references: tuple[str, ...]
    effective_at: datetime
    expires_at: datetime
    policy_version: str
    active: bool = False
    revoked: bool = False
    auto_renewed: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.exception_reference, "Security-exception reference"),
            (self.vulnerability_reference, "Exception vulnerability reference"),
            (self.affected_component_reference, "Exception component reference"),
            (self.exact_version_reference, "Exception exact-version reference"),
            (self.scope_reference, "Exception scope reference"),
            (self.requester_reference, "Exception requester reference"),
            (self.reviewer_reference, "Exception reviewer reference"),
            (self.approver_reference, "Exception approver reference"),
            (self.policy_version, "Exception policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.compensating_control_references, "Compensating-control reference")
        _validate_window(self.effective_at, self.expires_at, "Security exception")
        if len({self.requester_reference, self.reviewer_reference, self.approver_reference}) != 3:
            raise SupplyChainRecoveryContractError(
                "Exception request, review and approval must be segregated"
            )
        if self.active or self.auto_renewed:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot activate or auto-renew a security exception"
            )


@dataclass(frozen=True, slots=True)
class ResidualRiskAcceptanceRecord:
    acceptance_reference: str
    vulnerability_reference: str
    affected_component_reference: str
    exact_version_reference: str
    authority_reference: str
    policy_version: str
    accepted: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.acceptance_reference, "Residual-risk acceptance reference"),
            (self.vulnerability_reference, "Risk-acceptance vulnerability reference"),
            (self.affected_component_reference, "Risk-acceptance component reference"),
            (self.exact_version_reference, "Risk-acceptance exact-version reference"),
            (self.authority_reference, "Risk-acceptance authority reference"),
            (self.policy_version, "Risk-acceptance policy version"),
        ):
            _validate_reference(value, label)
        if self.accepted:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot accept vulnerability or residual risk"
            )


@dataclass(frozen=True, slots=True)
class SecurityAcceptanceRecord:
    acceptance_reference: str
    target_reference: str
    exact_version_reference: str
    verification_reference: str
    authority_reference: str
    policy_version: str
    accepted: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.acceptance_reference, "Security-acceptance reference"),
            (self.target_reference, "Security-acceptance target reference"),
            (self.exact_version_reference, "Security-acceptance exact-version reference"),
            (self.verification_reference, "Security-acceptance verification reference"),
            (self.authority_reference, "Security-acceptance authority reference"),
            (self.policy_version, "Security-acceptance policy version"),
        ):
            _validate_reference(value, label)
        if self.accepted:
            raise SupplyChainRecoveryContractError("WP-009 cannot security-accept a target")


@dataclass(frozen=True, slots=True)
class RecoverySourceMetadata:
    recovery_source_reference: str
    source_class_reference: str
    exact_version_reference: str
    integrity_reference: str
    creation_context_reference: str
    classification_reference: str
    residency_reference: str
    provenance_references: tuple[str, ...]
    policy_version: str
    integrity_state: RecoveryIntegrityState
    quarantined: bool = True
    synthetic: bool = True
    authoritative_known_good: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.recovery_source_reference, "Recovery-source reference"),
            (self.source_class_reference, "Recovery-source class reference"),
            (self.exact_version_reference, "Recovery-source exact-version reference"),
            (self.integrity_reference, "Recovery-source integrity reference"),
            (self.creation_context_reference, "Recovery creation-context reference"),
            (self.classification_reference, "Recovery classification reference"),
            (self.residency_reference, "Recovery residency reference"),
            (self.policy_version, "Recovery-source policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.provenance_references, "Recovery provenance reference")
        if not self.synthetic or self.authoritative_known_good:
            raise SupplyChainRecoveryContractError(
                "WP-009 recovery metadata must be synthetic and cannot assert known-good authority"
            )
        if self.integrity_state is not RecoveryIntegrityState.KNOWN_GOOD_REFERENCE_ONLY:
            if not self.quarantined:
                raise SupplyChainRecoveryContractError(
                    "Unknown or compromised recovery state must remain quarantined"
                )


@dataclass(frozen=True, slots=True)
class InvalidationObligation:
    obligation_reference: str
    recovery_source_reference: str
    credential_reference: str | None
    key_reference: str | None
    session_reference: str | None
    policy_version: str
    executed: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.obligation_reference, "Invalidation-obligation reference")
        _validate_reference(
            self.recovery_source_reference, "Invalidation recovery-source reference"
        )
        _validate_optional_reference(self.credential_reference, "Credential reference")
        _validate_optional_reference(self.key_reference, "Key reference")
        _validate_optional_reference(self.session_reference, "Session reference")
        _validate_reference(self.policy_version, "Invalidation policy version")
        if not any((self.credential_reference, self.key_reference, self.session_reference)):
            raise SupplyChainRecoveryContractError(
                "Invalidation obligation requires at least one opaque reference"
            )
        if self.executed:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot execute credential, key or session invalidation"
            )


@dataclass(frozen=True, slots=True)
class RecoveryReconciliationRecord:
    reconciliation_reference: str
    recovery_source_reference: str
    exact_version_reference: str
    current_state_reference: str
    revocation_references: tuple[str, ...]
    restriction_references: tuple[str, ...]
    deletion_references: tuple[str, ...]
    classification_references: tuple[str, ...]
    provenance_references: tuple[str, ...]
    security_state_references: tuple[str, ...]
    stale_grant_references: tuple[str, ...]
    expired_permission_references: tuple[str, ...]
    revoked_artifact_references: tuple[str, ...]
    invalid_credential_session_references: tuple[str, ...]
    ineligible_agent_model_tool_references: tuple[str, ...]
    policy_version: str
    current_state_available: bool
    live_reconciled: bool = False
    restored_stale_authority: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.reconciliation_reference, "Reconciliation reference"),
            (self.recovery_source_reference, "Reconciliation recovery-source reference"),
            (self.exact_version_reference, "Reconciliation exact-version reference"),
            (self.current_state_reference, "Current security-state reference"),
            (self.policy_version, "Reconciliation policy version"),
        ):
            _validate_reference(value, label)
        for values, label in (
            (self.revocation_references, "Current revocation reference"),
            (self.restriction_references, "Current restriction reference"),
            (self.deletion_references, "Current deletion reference"),
            (self.classification_references, "Current classification reference"),
            (self.provenance_references, "Current provenance reference"),
            (self.security_state_references, "Current security-state item reference"),
            (self.stale_grant_references, "Stale grant reference"),
            (self.expired_permission_references, "Expired permission reference"),
            (self.revoked_artifact_references, "Revoked artifact reference"),
            (
                self.invalid_credential_session_references,
                "Invalid credential/session reference",
            ),
            (
                self.ineligible_agent_model_tool_references,
                "Ineligible Agent/model/Tool reference",
            ),
        ):
            _validate_references(values, label, required=False)
        if self.live_reconciled or self.restored_stale_authority:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot reconcile a live system or restore stale authority"
            )


@dataclass(frozen=True, slots=True)
class IndependentRecoveryReview:
    review_reference: str
    recovery_source_reference: str
    reconciliation_reference: str
    reviewer_reference: str
    requester_reference: str
    executor_reference: str
    reviewed_at: datetime
    policy_version: str
    independent: bool
    security_recovery_accepted: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.review_reference, "Recovery-review reference"),
            (self.recovery_source_reference, "Recovery-review source reference"),
            (self.reconciliation_reference, "Recovery-review reconciliation reference"),
            (self.reviewer_reference, "Recovery reviewer reference"),
            (self.requester_reference, "Recovery requester reference"),
            (self.executor_reference, "Recovery executor reference"),
            (self.policy_version, "Recovery-review policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.reviewed_at, "Recovery-review time")
        if not self.independent or self.reviewer_reference in {
            self.requester_reference,
            self.executor_reference,
        }:
            raise SupplyChainRecoveryContractError(
                "Recovery review must be independent of request and execution"
            )
        if self.security_recovery_accepted:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot grant security-recovery acceptance"
            )


@dataclass(frozen=True, slots=True)
class RecoveryAuthorityReferences:
    recovery_reference: str
    policy_version: str
    security_recovery_acceptance_reference: str | None = None
    restoration_reference: str | None = None
    reauthorization_reference: str | None = None
    reinstatement_reference: str | None = None
    recovered: bool = False
    operationally_restored: bool = False
    reauthorized: bool = False
    reinstated: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.recovery_reference, "Recovery reference")
        _validate_reference(self.policy_version, "Recovery-authority policy version")
        _validate_optional_reference(
            self.security_recovery_acceptance_reference,
            "Security-recovery acceptance reference",
        )
        _validate_optional_reference(self.restoration_reference, "Restoration reference")
        _validate_optional_reference(self.reauthorization_reference, "Reauthorization reference")
        _validate_optional_reference(self.reinstatement_reference, "Reinstatement reference")
        if any(
            (
                self.recovered,
                self.operationally_restored,
                self.reauthorized,
                self.reinstated,
            )
        ):
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot recover, restore, reauthorize or reinstate"
            )


@dataclass(frozen=True, slots=True)
class RecoveryResultReference:
    recovery_reference: str
    recovery_source_reference: str
    exact_version_reference: str
    completed: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.recovery_reference, "Recovery-result reference")
        _validate_reference(self.recovery_source_reference, "Recovery-result source reference")
        _validate_reference(self.exact_version_reference, "Recovery-result version reference")
        if self.completed:
            raise SupplyChainRecoveryContractError("WP-009 cannot complete recovery")


@dataclass(frozen=True, slots=True)
class SecurityRecoveryAcceptanceRecord:
    acceptance_reference: str
    recovery_source_reference: str
    exact_version_reference: str
    reconciliation_reference: str
    independent_review_reference: str
    authority_reference: str
    policy_version: str
    accepted: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.acceptance_reference, "Security-recovery acceptance reference"),
            (self.recovery_source_reference, "Accepted recovery-source reference"),
            (self.exact_version_reference, "Accepted recovery exact-version reference"),
            (self.reconciliation_reference, "Recovery reconciliation reference"),
            (self.independent_review_reference, "Independent recovery-review reference"),
            (self.authority_reference, "Security-recovery acceptance authority reference"),
            (self.policy_version, "Security-recovery acceptance policy version"),
        ):
            _validate_reference(value, label)
        if self.accepted:
            raise SupplyChainRecoveryContractError(
                "WP-009 cannot grant security-recovery acceptance"
            )


@dataclass(frozen=True, slots=True)
class OperationalRestorationReference:
    restoration_reference: str
    recovery_reference: str
    security_recovery_acceptance_reference: str
    restored: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.restoration_reference, "Operational-restoration reference")
        _validate_reference(self.recovery_reference, "Restoration recovery reference")
        _validate_reference(
            self.security_recovery_acceptance_reference,
            "Restoration security-recovery acceptance reference",
        )
        if self.restored:
            raise SupplyChainRecoveryContractError("WP-009 cannot operationally restore a system")


@dataclass(frozen=True, slots=True)
class ReauthorizationReference:
    reauthorization_reference: str
    recovery_reference: str
    current_authorization_reference: str
    reauthorized: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.reauthorization_reference, "Reauthorization reference")
        _validate_reference(self.recovery_reference, "Reauthorization recovery reference")
        _validate_reference(self.current_authorization_reference, "Current authorization reference")
        if self.reauthorized:
            raise SupplyChainRecoveryContractError("WP-009 cannot reauthorize access")


@dataclass(frozen=True, slots=True)
class ReinstatementReference:
    reinstatement_reference: str
    restoration_reference: str
    reauthorization_reference: str
    reinstated: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.reinstatement_reference, "Reinstatement reference")
        _validate_reference(self.restoration_reference, "Reinstatement restoration reference")
        _validate_reference(
            self.reauthorization_reference, "Reinstatement reauthorization reference"
        )
        if self.reinstated:
            raise SupplyChainRecoveryContractError("WP-009 cannot reinstate access")


@dataclass(frozen=True, slots=True)
class SupplyChainControlResult:
    disposition: SupplyChainDisposition
    reason_code: str
    capability_created: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.reason_code, "Supply-chain control reason")
        if self.capability_created:
            raise SupplyChainRecoveryContractError("WP-009 cannot create operational capability")


class ArtifactEligibilityEvaluator:
    """Fail-closed metadata evaluator with no artifact-action method."""

    def __init__(
        self,
        *,
        provenance_registry: ControlledRegistry = EMPTY_ARTIFACT_PROVENANCE_POLICY_REGISTRY,
        verification_registry: ControlledRegistry = EMPTY_ARTIFACT_VERIFICATION_CRITERIA_REGISTRY,
        acceptance_registry: ControlledRegistry = EMPTY_ARTIFACT_ACCEPTANCE_REGISTRY,
        generated_code_registry: ControlledRegistry = EMPTY_GENERATED_CODE_GATE_REGISTRY,
        authorities: Wp009AuthorityBoundary | None = None,
    ) -> None:
        self._provenance_registry = provenance_registry
        self._verification_registry = verification_registry
        self._acceptance_registry = acceptance_registry
        self._generated_code_registry = generated_code_registry
        self._authorities = authorities or UnassignedWp009Authorities()

    def evaluate(
        self,
        artifact: ArtifactProvenanceMetadata,
        verification: ArtifactVerificationRecord | None,
        acceptance: ArtifactAcceptanceRecord | None,
        authorization: CurrentAuthorizationDecision | None,
        *,
        at: datetime,
    ) -> SupplyChainControlResult:
        _validate_instant(at, "Artifact evaluation time")
        if artifact.integrity_state is not ArtifactIntegrityState.VERIFIED_METADATA_ONLY:
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "ARTIFACT_INTEGRITY_UNVERIFIED"
            )
        if artifact.generated_code and self._generated_code_registry.is_empty():
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "GENERATED_CODE_GATE_UNASSIGNED"
            )
        if self._provenance_registry.is_empty():
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "PROVENANCE_POLICY_UNASSIGNED"
            )
        if verification is None or not verification.verified:
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "ARTIFACT_VERIFICATION_REQUIRED"
            )
        if (
            verification.artifact_reference != artifact.artifact_reference
            or verification.exact_version_reference != artifact.exact_version_reference
        ):
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "ARTIFACT_VERSION_SUBSTITUTION_DENIED"
            )
        if self._verification_registry.is_empty():
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "VERIFICATION_CRITERIA_UNASSIGNED"
            )
        if acceptance is None:
            return SupplyChainControlResult(
                SupplyChainDisposition.HUMAN_DECISION_REQUIRED,
                "ARTIFACT_ACCEPTANCE_REQUIRED",
            )
        if (
            acceptance.artifact_reference != artifact.artifact_reference
            or acceptance.exact_version_reference != artifact.exact_version_reference
        ):
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "ACCEPTANCE_VERSION_MISMATCH"
            )
        if (
            acceptance.revoked
            or not acceptance.accepted
            or not (acceptance.effective_at <= at < acceptance.expires_at)
        ):
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "ARTIFACT_ACCEPTANCE_NOT_CURRENT"
            )
        if not _current_permit(
            authorization,
            request_reference=acceptance.acceptance_reference,
            policy_version=acceptance.policy_version,
        ):
            return SupplyChainControlResult(
                SupplyChainDisposition.DENY, "CURRENT_AUTHORIZATION_REQUIRED"
            )
        if self._authorities.assignment_for(Wp009AuthorityClass.ARTIFACT_ACCEPTANCE) is None:
            return SupplyChainControlResult(
                SupplyChainDisposition.HUMAN_DECISION_REQUIRED,
                "ARTIFACT_ACCEPTANCE_AUTHORITY_UNASSIGNED",
            )
        if self._acceptance_registry.is_empty():
            return SupplyChainControlResult(
                SupplyChainDisposition.DENY, "ARTIFACT_ACCEPTANCE_REGISTRY_EMPTY"
            )
        return SupplyChainControlResult(
            SupplyChainDisposition.DENY, "ARTIFACT_ACTION_CAPABILITY_ABSENT"
        )


class VulnerabilityTreatmentEvaluator:
    """Fail-closed treatment evaluator with no scan, patch, waiver or closure method."""

    def __init__(
        self,
        *,
        policy_registry: ControlledRegistry = EMPTY_VULNERABILITY_POLICY_REGISTRY,
        exception_registry: ControlledRegistry = EMPTY_SECURITY_EXCEPTION_REGISTRY,
        risk_registry: ControlledRegistry = EMPTY_RESIDUAL_RISK_ACCEPTANCE_REGISTRY,
        authorities: Wp009AuthorityBoundary | None = None,
    ) -> None:
        self._policy_registry = policy_registry
        self._exception_registry = exception_registry
        self._risk_registry = risk_registry
        self._authorities = authorities or UnassignedWp009Authorities()

    def evaluate(
        self,
        vulnerability: VulnerabilityRecord,
        remediation: RemediationRecord | None = None,
        exception: SecurityExceptionRecord | None = None,
        risk_acceptance: ResidualRiskAcceptanceRecord | None = None,
        *,
        at: datetime,
    ) -> SupplyChainControlResult:
        _validate_instant(at, "Vulnerability evaluation time")
        if vulnerability.state in {
            VulnerabilityLifecycleState.STALE,
            VulnerabilityLifecycleState.INDETERMINATE_DENY,
        }:
            return SupplyChainControlResult(
                SupplyChainDisposition.DENY, "VULNERABILITY_STATE_STALE_OR_INDETERMINATE"
            )
        if self._policy_registry.is_empty():
            return SupplyChainControlResult(
                SupplyChainDisposition.REMEDIATION_REQUIRED, "VULNERABILITY_POLICY_UNASSIGNED"
            )
        if remediation is not None and (
            remediation.affected_component_reference != vulnerability.affected_component_reference
            or remediation.exact_version_reference != vulnerability.exact_version_reference
        ):
            return SupplyChainControlResult(
                SupplyChainDisposition.DENY, "REMEDIATION_VERSION_MISMATCH"
            )
        if exception is not None:
            if exception.exact_version_reference != vulnerability.exact_version_reference:
                return SupplyChainControlResult(
                    SupplyChainDisposition.DENY, "EXCEPTION_VERSION_MISMATCH"
                )
            if exception.revoked or not (exception.effective_at <= at < exception.expires_at):
                return SupplyChainControlResult(
                    SupplyChainDisposition.DENY, "EXCEPTION_NOT_CURRENT"
                )
            if self._exception_registry.is_empty():
                return SupplyChainControlResult(
                    SupplyChainDisposition.DENY, "EXCEPTION_REGISTRY_EMPTY"
                )
        if risk_acceptance is not None:
            if risk_acceptance.exact_version_reference != vulnerability.exact_version_reference:
                return SupplyChainControlResult(
                    SupplyChainDisposition.DENY, "RISK_ACCEPTANCE_VERSION_MISMATCH"
                )
            if (
                self._authorities.assignment_for(Wp009AuthorityClass.RESIDUAL_RISK_ACCEPTANCE)
                is None
            ):
                return SupplyChainControlResult(
                    SupplyChainDisposition.HUMAN_DECISION_REQUIRED,
                    "RISK_ACCEPTANCE_AUTHORITY_UNASSIGNED",
                )
            if self._risk_registry.is_empty():
                return SupplyChainControlResult(
                    SupplyChainDisposition.DENY, "RISK_ACCEPTANCE_REGISTRY_EMPTY"
                )
        return SupplyChainControlResult(
            SupplyChainDisposition.REMEDIATION_REQUIRED, "UNRESOLVED_VULNERABILITY_DENY"
        )


class RecoverySecurityEvaluator:
    """Fail-closed recovery evaluator with no backup, restore or reinstatement method."""

    def __init__(
        self,
        *,
        source_registry: ControlledRegistry = EMPTY_RECOVERY_SOURCE_CRITERIA_REGISTRY,
        known_good_registry: ControlledRegistry = EMPTY_KNOWN_GOOD_CRITERIA_REGISTRY,
        reconciliation_registry: ControlledRegistry = EMPTY_RECONCILIATION_REQUIREMENT_REGISTRY,
        acceptance_registry: ControlledRegistry = EMPTY_SECURITY_RECOVERY_ACCEPTANCE_REGISTRY,
        recovery_authority_registry: ControlledRegistry = EMPTY_RECOVERY_AUTHORITY_REGISTRY,
        restoration_registry: ControlledRegistry = EMPTY_RESTORATION_AUTHORITY_REGISTRY,
        reauthorization_registry: ControlledRegistry = EMPTY_REAUTHORIZATION_AUTHORITY_REGISTRY,
        reinstatement_registry: ControlledRegistry = EMPTY_REINSTATEMENT_AUTHORITY_REGISTRY,
        authorities: Wp009AuthorityBoundary | None = None,
    ) -> None:
        self._source_registry = source_registry
        self._known_good_registry = known_good_registry
        self._reconciliation_registry = reconciliation_registry
        self._acceptance_registry = acceptance_registry
        self._recovery_authority_registry = recovery_authority_registry
        self._restoration_registry = restoration_registry
        self._reauthorization_registry = reauthorization_registry
        self._reinstatement_registry = reinstatement_registry
        self._authorities = authorities or UnassignedWp009Authorities()

    def evaluate(
        self,
        source: RecoverySourceMetadata,
        reconciliation: RecoveryReconciliationRecord | None,
        review: IndependentRecoveryReview | None,
    ) -> SupplyChainControlResult:
        if source.integrity_state is not RecoveryIntegrityState.KNOWN_GOOD_REFERENCE_ONLY:
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "RECOVERY_STATE_COMPROMISED_OR_UNKNOWN"
            )
        if source.quarantined:
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "RECOVERY_SOURCE_REMAINS_QUARANTINED"
            )
        if self._source_registry.is_empty() or self._known_good_registry.is_empty():
            return SupplyChainControlResult(
                SupplyChainDisposition.QUARANTINE, "KNOWN_GOOD_CRITERIA_UNASSIGNED"
            )
        if reconciliation is None or not reconciliation.current_state_available:
            return SupplyChainControlResult(
                SupplyChainDisposition.RECONCILIATION_REQUIRED,
                "CURRENT_SECURITY_STATE_REQUIRED",
            )
        if reconciliation.recovery_source_reference != source.recovery_source_reference:
            return SupplyChainControlResult(SupplyChainDisposition.DENY, "RECOVERY_SOURCE_MISMATCH")
        if reconciliation.exact_version_reference != source.exact_version_reference:
            return SupplyChainControlResult(
                SupplyChainDisposition.DENY, "RECOVERY_VERSION_SUBSTITUTION_DENIED"
            )
        if self._reconciliation_registry.is_empty():
            return SupplyChainControlResult(
                SupplyChainDisposition.RECONCILIATION_REQUIRED,
                "RECONCILIATION_REQUIREMENTS_UNASSIGNED",
            )
        if review is None:
            return SupplyChainControlResult(
                SupplyChainDisposition.HUMAN_DECISION_REQUIRED,
                "INDEPENDENT_RECOVERY_REVIEW_REQUIRED",
            )
        if (
            self._authorities.assignment_for(Wp009AuthorityClass.SECURITY_RECOVERY_ACCEPTANCE)
            is None
        ):
            return SupplyChainControlResult(
                SupplyChainDisposition.HUMAN_DECISION_REQUIRED,
                "SECURITY_RECOVERY_ACCEPTANCE_AUTHORITY_UNASSIGNED",
            )
        if self._acceptance_registry.is_empty():
            return SupplyChainControlResult(
                SupplyChainDisposition.DENY, "SECURITY_RECOVERY_ACCEPTANCE_REGISTRY_EMPTY"
            )
        return SupplyChainControlResult(
            SupplyChainDisposition.DENY, "RECOVERY_OPERATION_CAPABILITY_ABSENT"
        )

    def evaluate_authority(
        self,
        references: RecoveryAuthorityReferences,
        authorization: CurrentAuthorizationDecision | None,
    ) -> SupplyChainControlResult:
        if not _current_permit(
            authorization,
            request_reference=references.recovery_reference,
            policy_version=references.policy_version,
        ):
            return SupplyChainControlResult(
                SupplyChainDisposition.DENY, "CURRENT_RECOVERY_AUTHORIZATION_REQUIRED"
            )
        required_authorities = (
            Wp009AuthorityClass.RECOVERY_APPROVAL,
            Wp009AuthorityClass.SECURITY_RECOVERY_ACCEPTANCE,
            Wp009AuthorityClass.OPERATIONAL_RESTORATION,
            Wp009AuthorityClass.REAUTHORIZATION,
            Wp009AuthorityClass.REINSTATEMENT,
        )
        if any(
            self._authorities.assignment_for(authority_class) is None
            for authority_class in required_authorities
        ):
            return SupplyChainControlResult(
                SupplyChainDisposition.HUMAN_DECISION_REQUIRED,
                "RECOVERY_RESTORATION_REINSTATEMENT_AUTHORITY_UNASSIGNED",
            )
        registries = (
            self._recovery_authority_registry,
            self._acceptance_registry,
            self._restoration_registry,
            self._reauthorization_registry,
            self._reinstatement_registry,
        )
        if any(registry.is_empty() for registry in registries):
            return SupplyChainControlResult(
                SupplyChainDisposition.DENY,
                "RECOVERY_RESTORATION_REINSTATEMENT_REGISTRY_EMPTY",
            )
        return SupplyChainControlResult(
            SupplyChainDisposition.DENY, "RECOVERY_OPERATION_CAPABILITY_ABSENT"
        )


class NoArtifactActionBoundary:
    """Expose metadata evaluation only; no artifact mutation or transfer method exists."""

    def __init__(self, evaluator: ArtifactEligibilityEvaluator | None = None) -> None:
        self._evaluator = evaluator or ArtifactEligibilityEvaluator()

    def evaluate(
        self,
        artifact: ArtifactProvenanceMetadata,
        verification: ArtifactVerificationRecord | None,
        acceptance: ArtifactAcceptanceRecord | None,
        authorization: CurrentAuthorizationDecision | None,
        *,
        at: datetime,
    ) -> SupplyChainControlResult:
        return self._evaluator.evaluate(artifact, verification, acceptance, authorization, at=at)


class NoRemediationBoundary:
    """Expose treatment evaluation only; no scanning or live-system modification method exists."""

    def __init__(self, evaluator: VulnerabilityTreatmentEvaluator | None = None) -> None:
        self._evaluator = evaluator or VulnerabilityTreatmentEvaluator()

    def evaluate(
        self,
        vulnerability: VulnerabilityRecord,
        remediation: RemediationRecord | None = None,
        exception: SecurityExceptionRecord | None = None,
        risk_acceptance: ResidualRiskAcceptanceRecord | None = None,
        *,
        at: datetime,
    ) -> SupplyChainControlResult:
        return self._evaluator.evaluate(
            vulnerability,
            remediation,
            exception,
            risk_acceptance,
            at=at,
        )


class NoRecoveryBoundary:
    """Expose recovery-security evaluation only; no operational recovery method exists."""

    def __init__(self, evaluator: RecoverySecurityEvaluator | None = None) -> None:
        self._evaluator = evaluator or RecoverySecurityEvaluator()

    def evaluate(
        self,
        source: RecoverySourceMetadata,
        reconciliation: RecoveryReconciliationRecord | None,
        review: IndependentRecoveryReview | None,
    ) -> SupplyChainControlResult:
        return self._evaluator.evaluate(source, reconciliation, review)


@dataclass(frozen=True, slots=True)
class UntrustedSupplyChainClaim:
    claim_reference: str
    origin: UntrustedContentOrigin
    asserted_acceptance_reference: str | None = None
    asserted_risk_acceptance_reference: str | None = None
    asserted_known_good_reference: str | None = None
    asserted_execution_authority_reference: str | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.claim_reference, "Untrusted supply-chain claim reference")
        _validate_optional_reference(
            self.asserted_acceptance_reference, "Asserted artifact-acceptance reference"
        )
        _validate_optional_reference(
            self.asserted_risk_acceptance_reference, "Asserted risk-acceptance reference"
        )
        _validate_optional_reference(
            self.asserted_known_good_reference, "Asserted known-good reference"
        )
        _validate_optional_reference(
            self.asserted_execution_authority_reference,
            "Asserted execution-authority reference",
        )


def evaluate_untrusted_supply_chain_claim(
    claim: UntrustedSupplyChainClaim,
) -> SupplyChainControlResult:
    del claim
    return SupplyChainControlResult(
        SupplyChainDisposition.DENY, "UNTRUSTED_CONTENT_CANNOT_CREATE_AUTHORITY"
    )
