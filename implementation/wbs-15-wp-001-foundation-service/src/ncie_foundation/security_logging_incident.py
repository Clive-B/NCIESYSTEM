"""Inert security logging, detection and incident-control contracts for WP-008."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from re import compile as compile_pattern
from typing import Final, Protocol

from .agent_model_tool_context_security import UntrustedContentOrigin
from .security_authorization import AuthorizationEffect, CurrentAuthorizationDecision

SECURITY_INCIDENT_BASELINE_VERSION: Final = "NCIE-WBS16-WP008-2026-09-24"
SECURITY_INCIDENT_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-24-029"
SECURITY_INCIDENT_IMPLEMENTATION_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-24-030"

_REFERENCE_PATTERN: Final = compile_pattern(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}")
_DENY_SENTINELS: Final = frozenset({"unassigned", "unspecified", "unknown"})
_PROHIBITED_FRAGMENTS: Final = (
    "-----begin",
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
    "token_value",
    "tool_result_content",
)


class SecurityIncidentContractError(ValueError):
    """Raised without echoing prohibited input when a WP-008 contract is invalid."""


def _validate_reference(value: str, label: str) -> None:
    normalized = value.lower()
    if (
        _REFERENCE_PATTERN.fullmatch(value) is None
        or normalized in _DENY_SENTINELS
        or any(fragment in normalized for fragment in _PROHIBITED_FRAGMENTS)
    ):
        raise SecurityIncidentContractError(f"{label} is invalid or contains prohibited material")


def _validate_optional_reference(value: str | None, label: str) -> None:
    if value is not None:
        _validate_reference(value, label)


def _validate_references(values: tuple[str, ...], label: str, *, required: bool = True) -> None:
    if required and not values:
        raise SecurityIncidentContractError(f"{label} is required")
    if len(values) != len(set(values)):
        raise SecurityIncidentContractError(f"{label} must not contain duplicates")
    for value in values:
        _validate_reference(value, label)


def _validate_instant(value: datetime, label: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise SecurityIncidentContractError(f"{label} must include a timezone")


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


class SecurityEventOutcome(StrEnum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    UNKNOWN = "UNKNOWN"
    INDETERMINATE = "INDETERMINATE"


class DetectionCategory(StrEnum):
    IDENTITY_ACCESS_ANOMALY = "IDENTITY_ACCESS_ANOMALY"
    EXFILTRATION_INDICATOR = "EXFILTRATION_INDICATOR"
    AGENT_ABUSE = "AGENT_ABUSE"
    PROMPT_INJECTION_INDICATOR = "PROMPT_INJECTION_INDICATOR"
    NETWORK_ANOMALY = "NETWORK_ANOMALY"


class TriageDisposition(StrEnum):
    NO_MATCH = "NO_MATCH"
    TRIAGE_REQUIRED = "TRIAGE_REQUIRED"
    HUMAN_DECISION_REQUIRED = "HUMAN_DECISION_REQUIRED"
    INDETERMINATE_DENY = "INDETERMINATE_DENY"


class IncidentLifecycleStage(StrEnum):
    DETECTION = "DETECTION"
    TRIAGE = "TRIAGE"
    CONTAINMENT = "CONTAINMENT"
    REVOCATION = "REVOCATION"
    ISOLATION = "ISOLATION"
    EVIDENCE_PRESERVATION_REQUEST = "EVIDENCE_PRESERVATION_REQUEST"
    NOTIFICATION_OBLIGATION = "NOTIFICATION_OBLIGATION"
    RECOVERY_HANDOFF = "RECOVERY_HANDOFF"
    RESTORATION_REINSTATEMENT_REVIEW = "RESTORATION_REINSTATEMENT_REVIEW"


INCIDENT_LIFECYCLE_ORDER: Final = tuple(IncidentLifecycleStage)


class ControlDisposition(StrEnum):
    DENY = "DENY"
    HUMAN_DECISION_REQUIRED = "HUMAN_DECISION_REQUIRED"


class NonWaivableSecurityIncidentProtection(StrEnum):
    HUMAN_PRIMARY_AUTHORITY = "HUMAN_PRIMARY_AUTHORITY"
    CURRENT_FOUR_LAYER_AUTHORIZATION = "CURRENT_FOUR_LAYER_AUTHORIZATION"
    METADATA_NOT_DISCLOSURE_AUTHORITY = "METADATA_NOT_DISCLOSURE_AUTHORITY"
    TELEMETRY_LOG_AUDIT_PROVENANCE_SEPARATION = "TELEMETRY_LOG_AUDIT_PROVENANCE_SEPARATION"
    MINIMIZATION_BY_CONSTRUCTION = "MINIMIZATION_BY_CONSTRUCTION"
    SEVERITY_CONFIDENCE_MATCH_NOT_AUTHORITY = "SEVERITY_CONFIDENCE_MATCH_NOT_AUTHORITY"
    SEGREGATION_NO_SELF_APPROVAL_OR_POOLING = "SEGREGATION_NO_SELF_APPROVAL_OR_POOLING"
    TEMPORARY_EXACT_REVIEWED_EMERGENCY_CONTAINMENT = (
        "TEMPORARY_EXACT_REVIEWED_EMERGENCY_CONTAINMENT"
    )
    FAIL_CLOSED_CURRENTNESS = "FAIL_CLOSED_CURRENTNESS"
    PRESERVE_HISTORY_AND_PROVENANCE = "PRESERVE_HISTORY_AND_PROVENANCE"
    RECOVERY_NOT_REAUTHORIZATION = "RECOVERY_NOT_REAUTHORIZATION"
    DENY_UNKNOWN_CROSS_BORDER = "DENY_UNKNOWN_CROSS_BORDER"
    AUDIT_ASSURANCE_REQUIRED = "AUDIT_ASSURANCE_REQUIRED"
    SYNTHETIC_LOCAL_ONLY = "SYNTHETIC_LOCAL_ONLY"


ALL_SECURITY_INCIDENT_PROTECTIONS: Final = frozenset(NonWaivableSecurityIncidentProtection)


class Wp008AuthorityClass(StrEnum):
    SECURITY_LOG_ACCESS_RETENTION = "SECURITY_LOG_ACCESS_RETENTION"
    SECURITY_LOGGING_OWNER = "SECURITY_LOGGING_OWNER"
    INDEPENDENT_ASSURANCE_AUDIT = "INDEPENDENT_ASSURANCE_AUDIT"
    DETECTION_MONITORING_OWNER = "DETECTION_MONITORING_OWNER"
    DETECTION_RULE_APPROVER = "DETECTION_RULE_APPROVER"
    TRIAGE_OWNER = "TRIAGE_OWNER"
    ESCALATION_GOVERNANCE = "ESCALATION_GOVERNANCE"
    SEVERITY_GOVERNANCE = "SEVERITY_GOVERNANCE"
    INCIDENT_DECLARATION = "INCIDENT_DECLARATION"
    INCIDENT_RESPONSE_OWNER = "INCIDENT_RESPONSE_OWNER"
    INCIDENT_COMMAND = "INCIDENT_COMMAND"
    EMERGENCY_ELIGIBILITY = "EMERGENCY_ELIGIBILITY"
    CONTAINMENT_REQUEST = "CONTAINMENT_REQUEST"
    CONTAINMENT_APPROVAL = "CONTAINMENT_APPROVAL"
    CONTAINMENT_EXECUTION = "CONTAINMENT_EXECUTION"
    NOTIFICATION = "NOTIFICATION"
    EVIDENCE_PRESERVATION_CUSTODY = "EVIDENCE_PRESERVATION_CUSTODY"
    CONTAINMENT_EFFECTIVENESS = "CONTAINMENT_EFFECTIVENESS"
    RECOVERY_RESTORATION_REINSTATEMENT = "RECOVERY_RESTORATION_REINSTATEMENT"
    INDEPENDENT_POST_EVENT_REVIEW = "INDEPENDENT_POST_EVENT_REVIEW"
    PERMANENT_DISPOSITION = "PERMANENT_DISPOSITION"


class Wp008AuthorityBoundary(Protocol):
    def assignment_for(self, authority_class: Wp008AuthorityClass) -> str | None: ...


class UnassignedWp008Authorities:
    """Expose no security-log, detection, incident or recovery authority assignment."""

    def assignment_for(self, authority_class: Wp008AuthorityClass) -> str | None:
        del authority_class
        return None


@dataclass(frozen=True, slots=True)
class SecuritySignal:
    """Minimized observation; never an event, alert, incident, Evidence or authority."""

    signal_reference: str
    correlation_reference: str
    source_class_reference: str
    condition_reference: str
    observed_at: datetime
    policy_version: str
    authoritative: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.signal_reference, "Signal reference"),
            (self.correlation_reference, "Signal correlation reference"),
            (self.source_class_reference, "Signal source-class reference"),
            (self.condition_reference, "Signal condition reference"),
            (self.policy_version, "Signal policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.observed_at, "Signal observation time")
        if self.authoritative:
            raise SecurityIncidentContractError("WP-008 signals must be non-authoritative")


@dataclass(frozen=True, slots=True)
class SecurityEvent:
    """Synthetic minimized event metadata, distinct from logs, Evidence and incidents."""

    event_reference: str
    correlation_reference: str
    source_reference: str
    occurred_at: datetime
    observed_at: datetime
    actor_class_reference: str
    actor_reference: str
    target_class_reference: str
    target_reference: str
    action_class_reference: str
    outcome: SecurityEventOutcome
    classification_reference: str
    residency_reference: str
    access_policy_reference: str
    retention_policy_reference: str
    policy_version: str
    provenance_references: tuple[str, ...]
    source_signal_references: tuple[str, ...] = ()
    authorization_reference: str | None = None
    delegation_reference: str | None = None
    approval_reference: str | None = None
    integrity_control_reference: str | None = None
    sensitive_access: bool = False
    governing_metadata_revoked: bool = False
    synthetic: bool = True
    authoritative: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.event_reference, "Event reference"),
            (self.correlation_reference, "Event correlation reference"),
            (self.source_reference, "Event source reference"),
            (self.actor_class_reference, "Actor-class reference"),
            (self.actor_reference, "Actor reference"),
            (self.target_class_reference, "Target-class reference"),
            (self.target_reference, "Target reference"),
            (self.action_class_reference, "Action-class reference"),
            (self.classification_reference, "Event classification reference"),
            (self.residency_reference, "Event residency reference"),
            (self.access_policy_reference, "Event access-policy reference"),
            (self.retention_policy_reference, "Event retention-policy reference"),
            (self.policy_version, "Event policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.provenance_references, "Event provenance reference")
        _validate_references(
            self.source_signal_references, "Source signal reference", required=False
        )
        _validate_optional_reference(self.authorization_reference, "Authorization reference")
        _validate_optional_reference(self.delegation_reference, "Delegation reference")
        _validate_optional_reference(self.approval_reference, "Approval reference")
        _validate_optional_reference(
            self.integrity_control_reference, "Integrity-control reference"
        )
        _validate_instant(self.occurred_at, "Event occurrence time")
        _validate_instant(self.observed_at, "Event observation time")
        if self.observed_at < self.occurred_at:
            raise SecurityIncidentContractError(
                "Event observation time must not precede occurrence time"
            )
        if not self.synthetic or self.authoritative:
            raise SecurityIncidentContractError(
                "WP-008 events must be synthetic and non-authoritative"
            )


@dataclass(frozen=True, slots=True)
class EvidenceReference:
    """Opaque prospective WBS-20 reference; this object is not Evidence."""

    reference: str

    def __post_init__(self) -> None:
        _validate_reference(self.reference, "Evidence reference")


@dataclass(frozen=True, slots=True)
class FindingReference:
    """Opaque prospective institutional reference; this object is not a Finding."""

    reference: str

    def __post_init__(self) -> None:
        _validate_reference(self.reference, "Finding reference")


@dataclass(frozen=True, slots=True)
class HumanDecisionReference:
    """Opaque reference that cannot itself create a Human decision or authority."""

    reference: str

    def __post_init__(self) -> None:
        _validate_reference(self.reference, "Human-decision reference")


@dataclass(frozen=True, slots=True)
class ExecutionAuthorityReference:
    """Opaque reference that cannot itself create execution capability."""

    reference: str

    def __post_init__(self) -> None:
        _validate_reference(self.reference, "Execution-authority reference")


@dataclass(frozen=True, slots=True)
class SeverityReference:
    severity_class_reference: str | None
    policy_version: str
    assigning_authority_reference: str | None = None
    effective_at: datetime | None = None
    expires_at: datetime | None = None
    revoked: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.policy_version, "Severity policy version")
        _validate_optional_reference(self.severity_class_reference, "Severity-class reference")
        _validate_optional_reference(
            self.assigning_authority_reference, "Severity assigning-authority reference"
        )
        if self.effective_at is not None:
            _validate_instant(self.effective_at, "Severity effective time")
        if self.expires_at is not None:
            _validate_instant(self.expires_at, "Severity expiry")
        if (self.effective_at is None) != (self.expires_at is None):
            raise SecurityIncidentContractError(
                "Severity effective and expiry times must be specified together"
            )
        if (
            self.effective_at is not None
            and self.expires_at is not None
            and self.expires_at <= self.effective_at
        ):
            raise SecurityIncidentContractError("Severity expiry must follow effective time")

    @property
    def is_unspecified(self) -> bool:
        return self.severity_class_reference is None


UNSPECIFIED_SEVERITY: Final = SeverityReference(
    severity_class_reference=None,
    policy_version=SECURITY_INCIDENT_BASELINE_VERSION,
)


@dataclass(frozen=True, slots=True)
class DetectionResult:
    detection_reference: str
    correlation_reference: str
    category: DetectionCategory
    source_event_references: tuple[str, ...]
    rule_reference: str
    policy_version: str
    provenance_references: tuple[str, ...]
    evaluated_at: datetime
    quality_state_reference: str
    severity: SeverityReference
    triage_disposition: TriageDisposition
    rule_current: bool = False
    authoritative: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.detection_reference, "Detection reference"),
            (self.correlation_reference, "Detection correlation reference"),
            (self.rule_reference, "Detection-rule reference"),
            (self.policy_version, "Detection policy version"),
            (self.quality_state_reference, "Detection quality-state reference"),
        ):
            _validate_reference(value, label)
        _validate_references(self.source_event_references, "Detection source-event reference")
        _validate_references(self.provenance_references, "Detection provenance reference")
        _validate_instant(self.evaluated_at, "Detection evaluation time")
        if self.authoritative:
            raise SecurityIncidentContractError("A WP-008 detection is non-authoritative")


@dataclass(frozen=True, slots=True)
class TriageResult:
    triage_reference: str
    detection_reference: str
    disposition: TriageDisposition
    reason_code: str
    severity: SeverityReference
    policy_version: str
    authoritative: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.triage_reference, "Triage reference"),
            (self.detection_reference, "Triage detection reference"),
            (self.reason_code, "Triage reason code"),
            (self.policy_version, "Triage policy version"),
        ):
            _validate_reference(value, label)
        if self.authoritative:
            raise SecurityIncidentContractError("A WP-008 triage result is non-authoritative")


@dataclass(frozen=True, slots=True)
class IncidentCandidate:
    candidate_reference: str
    correlation_reference: str
    detection_references: tuple[str, ...]
    requested_stage: IncidentLifecycleStage
    policy_version: str
    provenance_references: tuple[str, ...]
    declared: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.candidate_reference, "Incident-candidate reference"),
            (self.correlation_reference, "Incident correlation reference"),
            (self.policy_version, "Incident-candidate policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.detection_references, "Candidate detection reference")
        _validate_references(self.provenance_references, "Candidate provenance reference")
        if self.declared:
            raise SecurityIncidentContractError("WP-008 cannot declare an incident")


@dataclass(frozen=True, slots=True)
class NotificationObligation:
    obligation_reference: str
    incident_candidate_reference: str
    trigger_stage: IncidentLifecycleStage
    policy_version: str
    classification_reference: str
    recipient_role_class_reference: str | None = None
    destination_class_reference: str | None = None
    channel_class_reference: str | None = None
    due_policy_reference: str | None = None
    fulfilled: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.obligation_reference, "Notification-obligation reference"),
            (self.incident_candidate_reference, "Notification candidate reference"),
            (self.policy_version, "Notification policy version"),
            (self.classification_reference, "Notification classification reference"),
        ):
            _validate_reference(value, label)
        _validate_optional_reference(
            self.recipient_role_class_reference, "Notification recipient-role-class reference"
        )
        _validate_optional_reference(
            self.destination_class_reference, "Notification destination-class reference"
        )
        _validate_optional_reference(
            self.channel_class_reference, "Notification channel-class reference"
        )
        _validate_optional_reference(self.due_policy_reference, "Notification due-policy reference")
        if self.fulfilled:
            raise SecurityIncidentContractError(
                "WP-008 cannot represent an operationally fulfilled notification"
            )


@dataclass(frozen=True, slots=True)
class ContainmentRequest:
    request_reference: str
    incident_candidate_reference: str
    requester_reference: str
    target_reference: str
    target_class_reference: str
    action_reference: str
    trigger_reference: str
    purpose_reference: str
    requested_at: datetime
    expires_at: datetime
    policy_version: str
    emergency: bool = False
    authorized: bool = False
    executed: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Containment request reference"),
            (self.incident_candidate_reference, "Containment candidate reference"),
            (self.requester_reference, "Containment requester reference"),
            (self.target_reference, "Containment target reference"),
            (self.target_class_reference, "Containment target-class reference"),
            (self.action_reference, "Containment action reference"),
            (self.trigger_reference, "Containment trigger reference"),
            (self.purpose_reference, "Containment purpose reference"),
            (self.policy_version, "Containment policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.requested_at, "Containment request time")
        _validate_instant(self.expires_at, "Containment expiry")
        if self.expires_at <= self.requested_at:
            raise SecurityIncidentContractError("Containment expiry must follow request time")
        if self.authorized or self.executed:
            raise SecurityIncidentContractError("WP-008 cannot authorize or execute containment")


@dataclass(frozen=True, slots=True)
class ContainmentEffectivenessConfirmation:
    confirmation_reference: str
    containment_request_reference: str
    confirmer_authority_reference: str | None
    confirmed_at: datetime
    effective: bool = False
    authoritative: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.confirmation_reference, "Effectiveness confirmation reference")
        _validate_reference(
            self.containment_request_reference, "Effectiveness containment-request reference"
        )
        _validate_optional_reference(
            self.confirmer_authority_reference, "Effectiveness confirmer-authority reference"
        )
        _validate_instant(self.confirmed_at, "Effectiveness confirmation time")
        if self.effective or self.authoritative:
            raise SecurityIncidentContractError(
                "WP-008 cannot confirm operational containment effectiveness"
            )


@dataclass(frozen=True, slots=True)
class RecoveryHandoff:
    handoff_reference: str
    incident_candidate_reference: str
    containment_confirmation_reference: str
    preservation_request_reference: str
    policy_version: str
    recovery_authorized: bool = False
    reauthorization_created: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.handoff_reference, "Recovery-handoff reference"),
            (self.incident_candidate_reference, "Recovery candidate reference"),
            (
                self.containment_confirmation_reference,
                "Recovery containment-confirmation reference",
            ),
            (self.preservation_request_reference, "Recovery preservation-request reference"),
            (self.policy_version, "Recovery policy version"),
        ):
            _validate_reference(value, label)
        if self.recovery_authorized or self.reauthorization_created:
            raise SecurityIncidentContractError(
                "WP-008 recovery cannot authorize execution or recreate authorization"
            )


@dataclass(frozen=True, slots=True)
class RestorationReinstatementReview:
    review_reference: str
    incident_candidate_reference: str
    containment_request_reference: str
    containment_effectiveness_reference: str
    preservation_request_reference: str
    reviewer_reference: str
    requester_reference: str
    approver_reference: str
    executor_reference: str
    reviewed_at: datetime
    policy_version: str
    independent: bool
    restoration_authorized: bool = False
    reinstatement_authorized: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.review_reference, "Restoration-review reference"),
            (self.incident_candidate_reference, "Restoration candidate reference"),
            (self.containment_request_reference, "Restoration containment-request reference"),
            (
                self.containment_effectiveness_reference,
                "Restoration effectiveness reference",
            ),
            (self.preservation_request_reference, "Restoration preservation reference"),
            (self.reviewer_reference, "Restoration reviewer reference"),
            (self.requester_reference, "Restoration requester reference"),
            (self.approver_reference, "Restoration approver reference"),
            (self.executor_reference, "Restoration executor reference"),
            (self.policy_version, "Restoration policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.reviewed_at, "Restoration review time")
        participants = {
            self.requester_reference,
            self.approver_reference,
            self.executor_reference,
        }
        if not self.independent or self.reviewer_reference in participants:
            raise SecurityIncidentContractError(
                "Restoration review must be independent of request, approval and execution"
            )
        if self.restoration_authorized or self.reinstatement_authorized:
            raise SecurityIncidentContractError(
                "WP-008 cannot authorize restoration or reinstatement"
            )


@dataclass(frozen=True, slots=True)
class SecurityLogAccessRule:
    rule_reference: str
    object_reference: str
    field_references: tuple[str, ...]
    action_reference: str
    purpose_reference: str
    classification_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.rule_reference, "Log-access rule reference"),
            (self.object_reference, "Log-access object reference"),
            (self.action_reference, "Log-access action reference"),
            (self.purpose_reference, "Log-access purpose reference"),
            (self.classification_reference, "Log-access classification reference"),
            (self.policy_version, "Log-access policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.field_references, "Log-access field reference")


@dataclass(frozen=True, slots=True)
class RetentionLegalHoldRule:
    rule_reference: str
    classification_reference: str
    retention_policy_reference: str
    legal_hold_policy_reference: str | None
    policy_version: str
    effective_at: datetime
    expires_at: datetime
    revoked: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.rule_reference, "Retention rule reference"),
            (self.classification_reference, "Retention classification reference"),
            (self.retention_policy_reference, "Retention-policy reference"),
            (self.policy_version, "Retention rule policy version"),
        ):
            _validate_reference(value, label)
        _validate_optional_reference(
            self.legal_hold_policy_reference, "Legal-hold policy reference"
        )
        _validate_instant(self.effective_at, "Retention effective time")
        _validate_instant(self.expires_at, "Retention rule expiry")
        if self.expires_at <= self.effective_at:
            raise SecurityIncidentContractError("Retention rule expiry must follow effective time")


@dataclass(frozen=True, slots=True)
class AssuranceAssignment:
    assignment_reference: str
    assurance_scope_reference: str
    holder_reference: str
    reporting_route_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.assignment_reference, "Assurance assignment reference"),
            (self.assurance_scope_reference, "Assurance scope reference"),
            (self.holder_reference, "Assurance holder reference"),
            (self.reporting_route_reference, "Assurance reporting-route reference"),
            (self.policy_version, "Assurance policy version"),
        ):
            _validate_reference(value, label)


@dataclass(frozen=True, slots=True)
class DetectionRule:
    rule_reference: str
    category: DetectionCategory
    quality_state_reference: str
    policy_version: str
    effective_at: datetime
    expires_at: datetime
    revoked: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.rule_reference, "Detection-rule reference"),
            (self.quality_state_reference, "Detection quality-state reference"),
            (self.policy_version, "Detection-rule policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.effective_at, "Detection-rule effective time")
        _validate_instant(self.expires_at, "Detection-rule expiry")
        if self.expires_at <= self.effective_at:
            raise SecurityIncidentContractError("Detection-rule expiry must follow effective time")


@dataclass(frozen=True, slots=True)
class EscalationRoute:
    route_reference: str
    category: DetectionCategory
    triage_owner_reference: str
    escalation_authority_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.route_reference, "Escalation-route reference"),
            (self.triage_owner_reference, "Triage-owner reference"),
            (self.escalation_authority_reference, "Escalation-authority reference"),
            (self.policy_version, "Escalation policy version"),
        ):
            _validate_reference(value, label)


@dataclass(frozen=True, slots=True)
class SeverityGovernanceRule:
    rule_reference: str
    severity_class_reference: str
    assigning_authority_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.rule_reference, "Severity-governance rule reference"),
            (self.severity_class_reference, "Severity-class reference"),
            (self.assigning_authority_reference, "Severity authority reference"),
            (self.policy_version, "Severity-governance policy version"),
        ):
            _validate_reference(value, label)


@dataclass(frozen=True, slots=True)
class IncidentCommandAssignment:
    assignment_reference: str
    commander_reference: str
    scope_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.assignment_reference, "Incident-command assignment reference"),
            (self.commander_reference, "Incident commander reference"),
            (self.scope_reference, "Incident-command scope reference"),
            (self.policy_version, "Incident-command policy version"),
        ):
            _validate_reference(value, label)


@dataclass(frozen=True, slots=True)
class NotificationDestinationRule:
    rule_reference: str
    recipient_role_class_reference: str
    destination_class_reference: str
    channel_class_reference: str
    residency_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.rule_reference, "Notification rule reference"),
            (self.recipient_role_class_reference, "Notification role-class reference"),
            (self.destination_class_reference, "Notification destination-class reference"),
            (self.channel_class_reference, "Notification channel-class reference"),
            (self.residency_reference, "Notification residency reference"),
            (self.policy_version, "Notification policy version"),
        ):
            _validate_reference(value, label)


@dataclass(frozen=True, slots=True)
class ContainmentRight:
    right_reference: str
    requester_reference: str
    approver_reference: str
    executor_reference: str
    action_reference: str
    target_class_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.right_reference, "Containment-right reference"),
            (self.requester_reference, "Containment-right requester reference"),
            (self.approver_reference, "Containment-right approver reference"),
            (self.executor_reference, "Containment-right executor reference"),
            (self.action_reference, "Containment-right action reference"),
            (self.target_class_reference, "Containment-right target-class reference"),
            (self.policy_version, "Containment-right policy version"),
        ):
            _validate_reference(value, label)
        if len({self.requester_reference, self.approver_reference, self.executor_reference}) != 3:
            raise SecurityIncidentContractError(
                "Containment requester, approver and executor must be segregated"
            )


@dataclass(frozen=True, slots=True)
class EmergencyEligibilityRule:
    rule_reference: str
    trigger_reference: str
    target_class_reference: str
    action_reference: str
    authority_reference: str
    policy_version: str
    effective_at: datetime
    expires_at: datetime
    revoked: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.rule_reference, "Emergency-eligibility rule reference"),
            (self.trigger_reference, "Emergency trigger reference"),
            (self.target_class_reference, "Emergency target-class reference"),
            (self.action_reference, "Emergency action reference"),
            (self.authority_reference, "Emergency authority reference"),
            (self.policy_version, "Emergency policy version"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.effective_at, "Emergency eligibility effective time")
        _validate_instant(self.expires_at, "Emergency eligibility expiry")
        if self.expires_at <= self.effective_at:
            raise SecurityIncidentContractError(
                "Emergency eligibility expiry must follow effective time"
            )


@dataclass(frozen=True, slots=True)
class RestorationAuthorityAssignment:
    assignment_reference: str
    reviewer_reference: str
    restoration_authority_reference: str
    reinstatement_authority_reference: str
    target_class_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.assignment_reference, "Restoration assignment reference"),
            (self.reviewer_reference, "Restoration reviewer reference"),
            (self.restoration_authority_reference, "Restoration authority reference"),
            (self.reinstatement_authority_reference, "Reinstatement authority reference"),
            (self.target_class_reference, "Restoration target-class reference"),
            (self.policy_version, "Restoration policy version"),
        ):
            _validate_reference(value, label)
        if self.reviewer_reference in {
            self.restoration_authority_reference,
            self.reinstatement_authority_reference,
        }:
            raise SecurityIncidentContractError(
                "Independent reviewer cannot be a restoration or reinstatement authority"
            )


def _validate_registry(version: str, references: tuple[str, ...], label: str) -> None:
    _validate_reference(version, f"{label} version")
    if len(references) != len(set(references)):
        raise SecurityIncidentContractError(f"{label} references must be unique")


@dataclass(frozen=True, slots=True)
class SecurityLogAccessRegistry:
    version: str
    entries: tuple[SecurityLogAccessRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.rule_reference for entry in self.entries),
            "Log-access registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class RetentionLegalHoldRegistry:
    version: str
    entries: tuple[RetentionLegalHoldRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.rule_reference for entry in self.entries),
            "Retention/legal-hold registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class AssuranceAssignmentRegistry:
    version: str
    entries: tuple[AssuranceAssignment, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.assignment_reference for entry in self.entries),
            "Assurance registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class DetectionRuleRegistry:
    version: str
    entries: tuple[DetectionRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.rule_reference for entry in self.entries),
            "Detection-rule registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class EscalationRouteRegistry:
    version: str
    entries: tuple[EscalationRoute, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.route_reference for entry in self.entries),
            "Escalation-route registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class SeverityGovernanceRegistry:
    version: str
    entries: tuple[SeverityGovernanceRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.rule_reference for entry in self.entries),
            "Severity-governance registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class IncidentCommandRegistry:
    version: str
    entries: tuple[IncidentCommandAssignment, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.assignment_reference for entry in self.entries),
            "Incident-command registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class NotificationDestinationRegistry:
    version: str
    entries: tuple[NotificationDestinationRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.rule_reference for entry in self.entries),
            "Notification/destination registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class ContainmentRightsRegistry:
    version: str
    entries: tuple[ContainmentRight, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.right_reference for entry in self.entries),
            "Containment-rights registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class EmergencyEligibilityRegistry:
    version: str
    entries: tuple[EmergencyEligibilityRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.rule_reference for entry in self.entries),
            "Emergency-eligibility registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


@dataclass(frozen=True, slots=True)
class RestorationAuthorityRegistry:
    version: str
    entries: tuple[RestorationAuthorityAssignment, ...] = ()

    def __post_init__(self) -> None:
        _validate_registry(
            self.version,
            tuple(entry.assignment_reference for entry in self.entries),
            "Restoration/reinstatement registry",
        )

    def is_empty(self) -> bool:
        return not self.entries


EMPTY_SECURITY_LOG_ACCESS_REGISTRY: Final = SecurityLogAccessRegistry(
    SECURITY_INCIDENT_BASELINE_VERSION
)
EMPTY_RETENTION_LEGAL_HOLD_REGISTRY: Final = RetentionLegalHoldRegistry(
    SECURITY_INCIDENT_BASELINE_VERSION
)
EMPTY_ASSURANCE_ASSIGNMENT_REGISTRY: Final = AssuranceAssignmentRegistry(
    SECURITY_INCIDENT_BASELINE_VERSION
)
EMPTY_DETECTION_RULE_REGISTRY: Final = DetectionRuleRegistry(SECURITY_INCIDENT_BASELINE_VERSION)
EMPTY_ESCALATION_ROUTE_REGISTRY: Final = EscalationRouteRegistry(SECURITY_INCIDENT_BASELINE_VERSION)
EMPTY_SEVERITY_GOVERNANCE_REGISTRY: Final = SeverityGovernanceRegistry(
    SECURITY_INCIDENT_BASELINE_VERSION
)
EMPTY_INCIDENT_COMMAND_REGISTRY: Final = IncidentCommandRegistry(SECURITY_INCIDENT_BASELINE_VERSION)
EMPTY_NOTIFICATION_DESTINATION_REGISTRY: Final = NotificationDestinationRegistry(
    SECURITY_INCIDENT_BASELINE_VERSION
)
EMPTY_CONTAINMENT_RIGHTS_REGISTRY: Final = ContainmentRightsRegistry(
    SECURITY_INCIDENT_BASELINE_VERSION
)
EMPTY_EMERGENCY_ELIGIBILITY_REGISTRY: Final = EmergencyEligibilityRegistry(
    SECURITY_INCIDENT_BASELINE_VERSION
)
EMPTY_RESTORATION_AUTHORITY_REGISTRY: Final = RestorationAuthorityRegistry(
    SECURITY_INCIDENT_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class ControlResult:
    disposition: ControlDisposition
    reason_code: str
    capability_available: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.reason_code, "Control-result reason code")
        if self.capability_available:
            raise SecurityIncidentContractError("WP-008 exposes no operational capability")


@dataclass(frozen=True, slots=True)
class SecurityLogAccessRequest:
    request_reference: str
    event_reference: str
    actor_reference: str
    object_reference: str
    field_references: tuple[str, ...]
    action_reference: str
    purpose_reference: str
    classification_reference: str
    access_policy_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Log-access request reference"),
            (self.event_reference, "Log-access event reference"),
            (self.actor_reference, "Log-access actor reference"),
            (self.object_reference, "Log-access object reference"),
            (self.action_reference, "Log-access action reference"),
            (self.purpose_reference, "Log-access purpose reference"),
            (self.classification_reference, "Log-access classification reference"),
            (self.access_policy_reference, "Log-access policy reference"),
            (self.policy_version, "Log-access policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.field_references, "Log-access field reference")


class DenyAllSecurityLogAccessBoundary:
    """Evaluate metadata only; expose no log query, read, disclosure or export path."""

    def __init__(
        self,
        registry: SecurityLogAccessRegistry = EMPTY_SECURITY_LOG_ACCESS_REGISTRY,
        authorities: Wp008AuthorityBoundary | None = None,
    ) -> None:
        self._registry = registry
        self._authorities = authorities or UnassignedWp008Authorities()

    def evaluate(
        self,
        request: SecurityLogAccessRequest,
        authorization: CurrentAuthorizationDecision | None,
    ) -> ControlResult:
        if not _current_permit(
            authorization,
            request_reference=request.request_reference,
            policy_version=request.policy_version,
        ):
            return ControlResult(ControlDisposition.DENY, "CURRENT_AUTHORIZATION_REQUIRED")
        if (
            self._authorities.assignment_for(Wp008AuthorityClass.SECURITY_LOG_ACCESS_RETENTION)
            is None
        ):
            return ControlResult(ControlDisposition.DENY, "LOG_ACCESS_AUTHORITY_UNASSIGNED")
        if self._registry.is_empty():
            return ControlResult(ControlDisposition.DENY, "LOG_ACCESS_POLICY_UNASSIGNED")
        return ControlResult(ControlDisposition.DENY, "LOG_ACCESS_CAPABILITY_ABSENT")


@dataclass(frozen=True, slots=True)
class RetentionEvaluationRequest:
    request_reference: str
    event_reference: str
    classification_reference: str
    retention_policy_reference: str
    legal_hold_policy_reference: str | None
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Retention request reference"),
            (self.event_reference, "Retention event reference"),
            (self.classification_reference, "Retention classification reference"),
            (self.retention_policy_reference, "Retention-policy reference"),
            (self.policy_version, "Retention request policy version"),
        ):
            _validate_reference(value, label)
        _validate_optional_reference(
            self.legal_hold_policy_reference, "Retention legal-hold reference"
        )


class DenyAllRetentionBoundary:
    """Evaluate policy metadata without storage, deletion, disposition or legal-hold action."""

    def __init__(
        self,
        registry: RetentionLegalHoldRegistry = EMPTY_RETENTION_LEGAL_HOLD_REGISTRY,
    ) -> None:
        self._registry = registry

    def evaluate(self, request: RetentionEvaluationRequest) -> ControlResult:
        del request
        if self._registry.is_empty():
            return ControlResult(ControlDisposition.DENY, "RETENTION_POLICY_UNASSIGNED")
        return ControlResult(ControlDisposition.DENY, "RETENTION_OPERATION_CAPABILITY_ABSENT")


@dataclass(frozen=True, slots=True)
class DetectionRequest:
    request_reference: str
    detection_reference: str
    event: SecurityEvent
    category: DetectionCategory
    rule_reference: str
    quality_state_reference: str
    behavior_references: tuple[str, ...]
    content_origin: UntrustedContentOrigin
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Detection request reference"),
            (self.detection_reference, "Detection reference"),
            (self.rule_reference, "Detection-rule reference"),
            (self.quality_state_reference, "Detection quality-state reference"),
            (self.policy_version, "Detection request policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(
            self.behavior_references, "Detection behavior reference", required=False
        )


class NoMonitorBoundary:
    """Evaluate one supplied synthetic event; provide no polling, streaming or source access."""

    def __init__(
        self,
        registry: DetectionRuleRegistry = EMPTY_DETECTION_RULE_REGISTRY,
    ) -> None:
        self._registry = registry

    def evaluate(self, request: DetectionRequest, *, at: datetime) -> DetectionResult:
        _validate_instant(at, "Detection evaluation time")
        return DetectionResult(
            detection_reference=request.detection_reference,
            correlation_reference=request.event.correlation_reference,
            category=request.category,
            source_event_references=(request.event.event_reference,),
            rule_reference=request.rule_reference,
            policy_version=request.policy_version,
            provenance_references=request.event.provenance_references,
            evaluated_at=at,
            quality_state_reference=request.quality_state_reference,
            severity=UNSPECIFIED_SEVERITY,
            triage_disposition=TriageDisposition.INDETERMINATE_DENY,
            rule_current=False,
        )


class FailClosedTriageBoundary:
    def __init__(
        self,
        escalation_registry: EscalationRouteRegistry = EMPTY_ESCALATION_ROUTE_REGISTRY,
        severity_registry: SeverityGovernanceRegistry = EMPTY_SEVERITY_GOVERNANCE_REGISTRY,
    ) -> None:
        self._escalation_registry = escalation_registry
        self._severity_registry = severity_registry

    def evaluate(self, result: DetectionResult) -> TriageResult:
        if not result.rule_current:
            reason = "DETECTION_RULE_NOT_CURRENT"
            disposition = TriageDisposition.INDETERMINATE_DENY
        elif self._severity_registry.is_empty():
            reason = "SEVERITY_GOVERNANCE_UNASSIGNED"
            disposition = TriageDisposition.HUMAN_DECISION_REQUIRED
        elif self._escalation_registry.is_empty():
            reason = "ESCALATION_ROUTE_UNASSIGNED"
            disposition = TriageDisposition.HUMAN_DECISION_REQUIRED
        else:
            reason = "TRIAGE_CAPABILITY_ABSENT"
            disposition = TriageDisposition.HUMAN_DECISION_REQUIRED
        return TriageResult(
            triage_reference=f"triage:{result.detection_reference}",
            detection_reference=result.detection_reference,
            disposition=disposition,
            reason_code=reason,
            severity=UNSPECIFIED_SEVERITY,
            policy_version=result.policy_version,
        )


class NoIncidentCommandBoundary:
    """Return only deny or Human-decision-required; never declare or command an incident."""

    def __init__(
        self,
        registry: IncidentCommandRegistry = EMPTY_INCIDENT_COMMAND_REGISTRY,
        authorities: Wp008AuthorityBoundary | None = None,
    ) -> None:
        self._registry = registry
        self._authorities = authorities or UnassignedWp008Authorities()

    def evaluate(self, candidate: IncidentCandidate) -> ControlResult:
        del candidate
        if self._authorities.assignment_for(Wp008AuthorityClass.INCIDENT_DECLARATION) is None:
            return ControlResult(
                ControlDisposition.HUMAN_DECISION_REQUIRED,
                "INCIDENT_DECLARATION_AUTHORITY_UNASSIGNED",
            )
        if self._registry.is_empty():
            return ControlResult(ControlDisposition.DENY, "INCIDENT_COMMAND_UNASSIGNED")
        return ControlResult(ControlDisposition.DENY, "INCIDENT_COMMAND_CAPABILITY_ABSENT")


class NoNotificationBoundary:
    """Evaluate an obligation without recipients, destinations, send, page or alert capability."""

    def __init__(
        self,
        registry: NotificationDestinationRegistry = EMPTY_NOTIFICATION_DESTINATION_REGISTRY,
    ) -> None:
        self._registry = registry

    def evaluate(self, obligation: NotificationObligation) -> ControlResult:
        if (
            obligation.recipient_role_class_reference is None
            or obligation.destination_class_reference is None
            or obligation.channel_class_reference is None
        ):
            return ControlResult(ControlDisposition.DENY, "NOTIFICATION_DESTINATION_UNASSIGNED")
        if self._registry.is_empty():
            return ControlResult(ControlDisposition.DENY, "NOTIFICATION_ROUTE_UNASSIGNED")
        return ControlResult(ControlDisposition.DENY, "NOTIFICATION_SEND_CAPABILITY_ABSENT")


class NoContainmentRecoveryBoundary:
    """Metadata evaluation only; deliberately exposes no execution method."""

    def __init__(
        self,
        containment_registry: ContainmentRightsRegistry = EMPTY_CONTAINMENT_RIGHTS_REGISTRY,
        emergency_registry: EmergencyEligibilityRegistry = EMPTY_EMERGENCY_ELIGIBILITY_REGISTRY,
        restoration_registry: RestorationAuthorityRegistry = EMPTY_RESTORATION_AUTHORITY_REGISTRY,
    ) -> None:
        self._containment_registry = containment_registry
        self._emergency_registry = emergency_registry
        self._restoration_registry = restoration_registry

    def evaluate_containment(
        self,
        request: ContainmentRequest,
        authorization: CurrentAuthorizationDecision | None,
    ) -> ControlResult:
        if not _current_permit(
            authorization,
            request_reference=request.request_reference,
            policy_version=request.policy_version,
        ):
            return ControlResult(ControlDisposition.DENY, "CURRENT_AUTHORIZATION_REQUIRED")
        if request.emergency and self._emergency_registry.is_empty():
            return ControlResult(ControlDisposition.DENY, "EMERGENCY_ELIGIBILITY_UNASSIGNED")
        if self._containment_registry.is_empty():
            return ControlResult(ControlDisposition.DENY, "CONTAINMENT_RIGHT_UNASSIGNED")
        return ControlResult(ControlDisposition.DENY, "CONTAINMENT_EXECUTION_CAPABILITY_ABSENT")

    def evaluate_restoration(
        self,
        review: RestorationReinstatementReview,
        authorization: CurrentAuthorizationDecision | None,
    ) -> ControlResult:
        if not _current_permit(
            authorization,
            request_reference=review.review_reference,
            policy_version=review.policy_version,
        ):
            return ControlResult(ControlDisposition.DENY, "NEW_AUTHORIZATION_REQUIRED")
        if self._restoration_registry.is_empty():
            return ControlResult(
                ControlDisposition.HUMAN_DECISION_REQUIRED,
                "RESTORATION_REINSTATEMENT_AUTHORITY_UNASSIGNED",
            )
        return ControlResult(ControlDisposition.DENY, "RESTORATION_REINSTATEMENT_CAPABILITY_ABSENT")


class SyntheticSecurityEventCollector:
    """Process-local test collector with no persistence, audit, provenance or Evidence semantics."""

    persistent: Final = False
    authoritative: Final = False
    evidence_store: Final = False
    audit_store: Final = False
    provenance_store: Final = False

    def __init__(self) -> None:
        self._events: list[SecurityEvent] = []

    def collect(self, event: SecurityEvent) -> None:
        if not event.synthetic or event.authoritative:
            raise SecurityIncidentContractError(
                "Collector accepts synthetic non-authoritative events only"
            )
        self._events.append(event)

    def snapshot(self) -> tuple[SecurityEvent, ...]:
        return tuple(self._events)

    def clear(self) -> None:
        self._events.clear()


@dataclass(frozen=True, slots=True)
class UntrustedSecurityControlClaim:
    claim_reference: str
    origin: UntrustedContentOrigin
    asserted_severity_reference: str | None = None
    asserted_incident_reference: str | None = None
    asserted_authority_reference: str | None = None
    asserted_destination_reference: str | None = None

    def __post_init__(self) -> None:
        _validate_reference(self.claim_reference, "Untrusted claim reference")
        _validate_optional_reference(
            self.asserted_severity_reference, "Asserted severity reference"
        )
        _validate_optional_reference(
            self.asserted_incident_reference, "Asserted incident reference"
        )
        _validate_optional_reference(
            self.asserted_authority_reference, "Asserted authority reference"
        )
        _validate_optional_reference(
            self.asserted_destination_reference, "Asserted destination reference"
        )


def evaluate_untrusted_security_claim(claim: UntrustedSecurityControlClaim) -> ControlResult:
    del claim
    return ControlResult(ControlDisposition.DENY, "UNTRUSTED_CONTENT_CANNOT_CREATE_AUTHORITY")
