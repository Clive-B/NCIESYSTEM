"""Zero-output DLP, disclosure and protected-identity contracts for WP-007."""

from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum, StrEnum
from re import compile as compile_pattern
from typing import Final, Protocol

from .agent_model_tool_context_security import UntrustedContentOrigin
from .security_authorization import AuthorizationEffect, CurrentAuthorizationDecision

DATA_LOSS_PRIVACY_BASELINE_VERSION: Final = "NCIE-WBS16-WP007-2026-09-24"
DATA_LOSS_PRIVACY_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-24-026"
DATA_LOSS_PRIVACY_IMPLEMENTATION_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-24-027"

_REFERENCE_PATTERN: Final = compile_pattern(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}")
_DENY_SENTINELS: Final = frozenset({"unassigned", "unspecified", "unknown"})
_PROTECTED_FRAGMENTS: Final = (
    "-----begin",
    "credential_value",
    "identity_value",
    "passport_number",
    "private_key",
    "secret_value",
    "token_value",
)


class DataLossPrivacyContractError(ValueError):
    """Raised without echoing protected input when a WP-007 contract is invalid."""


def _validate_reference(value: str, label: str) -> None:
    normalized = value.lower()
    if (
        _REFERENCE_PATTERN.fullmatch(value) is None
        or normalized in _DENY_SENTINELS
        or any(fragment in normalized for fragment in _PROTECTED_FRAGMENTS)
    ):
        raise DataLossPrivacyContractError(f"{label} is invalid or contains protected material")


def _validate_optional_reference(value: str | None, label: str) -> None:
    if value is not None:
        _validate_reference(value, label)


def _validate_references(values: tuple[str, ...], label: str, *, required: bool = True) -> None:
    if required and not values:
        raise DataLossPrivacyContractError(f"{label} is required")
    if len(values) != len(set(values)):
        raise DataLossPrivacyContractError(f"{label} must not contain duplicates")
    for value in values:
        _validate_reference(value, label)


def _validate_instant(value: datetime, label: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise DataLossPrivacyContractError(f"{label} must include a timezone")


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


class ClassificationTier(IntEnum):
    PUBLIC = 1
    INTERNAL = 2
    PROTECTED = 3
    SENSITIVE = 4


class DlpPath(StrEnum):
    TOOL_INVOCATION_INPUT_OUTPUT = "TOOL_INVOCATION_INPUT_OUTPUT"
    EXPORT_FILE_REPORT_API_RESPONSE = "EXPORT_FILE_REPORT_API_RESPONSE"
    MODEL_INPUT_CONTEXT_ASSEMBLY = "MODEL_INPUT_CONTEXT_ASSEMBLY"
    VOICE_SPOKEN_OUTPUT = "VOICE_SPOKEN_OUTPUT"
    AGENT_TO_AGENT_HANDOFF = "AGENT_TO_AGENT_HANDOFF"


class DlpDisposition(StrEnum):
    DENY = "DENY"
    INDETERMINATE = "INDETERMINATE"
    MASK_REQUIRED = "MASK_REQUIRED"
    REDACTION_REQUIRED = "REDACTION_REQUIRED"
    SUPPRESSION_REQUIRED = "SUPPRESSION_REQUIRED"
    MINIMIZATION_REQUIRED = "MINIMIZATION_REQUIRED"
    HUMAN_REVIEW_REQUIRED = "HUMAN_REVIEW_REQUIRED"
    EXCEPTION_REQUIRED = "EXCEPTION_REQUIRED"
    POLICY_CHECK_SATISFIED = "POLICY_CHECK_SATISFIED"


class DlpProcessingStage(StrEnum):
    CLASSIFICATION_FLOOR = "CLASSIFICATION_FLOOR"
    MINIMUM_NECESSARY = "MINIMUM_NECESSARY"
    MASKING_TOKENIZATION = "MASKING_TOKENIZATION"
    REDACTION = "REDACTION"
    SUPPRESSION = "SUPPRESSION"
    RECLASSIFICATION = "RECLASSIFICATION"
    RECIPIENT_AUTHORIZATION = "RECIPIENT_AUTHORIZATION"
    CHANNEL_DESTINATION = "CHANNEL_DESTINATION"
    DISCLOSURE_AUTHORITY = "DISCLOSURE_AUTHORITY"


DLP_PROCESSING_ORDER: Final = tuple(DlpProcessingStage)


class DisclosureEffect(StrEnum):
    PERMIT = "PERMIT"
    DENY = "DENY"
    INDETERMINATE = "INDETERMINATE"


class OutputChannelClass(StrEnum):
    PROTECTED_VISUAL_DISPLAY = "PROTECTED_VISUAL_DISPLAY"
    FILE_EXPORT = "FILE_EXPORT"
    REPORT_EXPORT = "REPORT_EXPORT"
    API_RESPONSE = "API_RESPONSE"
    TOOL_INPUT_OUTPUT = "TOOL_INPUT_OUTPUT"
    MODEL_PROMPT_CONTEXT_INPUT = "MODEL_PROMPT_CONTEXT_INPUT"
    VOICE_SPOKEN_OUTPUT = "VOICE_SPOKEN_OUTPUT"
    AGENT_TO_AGENT_HANDOFF = "AGENT_TO_AGENT_HANDOFF"


class ProtectedIdentityHandlingClass(StrEnum):
    OPAQUE_PROTECTED_REFERENCE_ONLY = "OPAQUE_PROTECTED_REFERENCE_ONLY"
    AGGREGATE_OR_COUNT_ONLY = "AGGREGATE_OR_COUNT_ONLY"
    MASKED_OR_TOKENIZED = "MASKED_OR_TOKENIZED"
    PROTECTED_REVEAL = "PROTECTED_REVEAL"
    INFERRED_PROTECTED_IDENTITY_EQUIVALENT = "INFERRED_PROTECTED_IDENTITY_EQUIVALENT"


class DataTransformClass(StrEnum):
    MASK = "MASK"
    TOKENIZE = "TOKENIZE"
    REDACT = "REDACT"
    AGGREGATE = "AGGREGATE"
    SUPPRESS = "SUPPRESS"


class PrivacyEscalationDisposition(StrEnum):
    HUMAN_DECISION_REQUIRED = "HUMAN_DECISION_REQUIRED"


class PrivacyEscalationReason(StrEnum):
    PROTECTED_REVEAL = "PROTECTED_REVEAL"
    INFERRED_EQUIVALENT = "INFERRED_EQUIVALENT"
    MIXED_CLASSIFICATION = "MIXED_CLASSIFICATION"
    MIXED_RECIPIENT_AUTHORITY = "MIXED_RECIPIENT_AUTHORITY"
    VOICE_DISCLOSURE = "VOICE_DISCLOSURE"
    EXPORT_OR_EXTERNAL_PATH = "EXPORT_OR_EXTERNAL_PATH"
    LEGAL_CONSENT_OR_PURPOSE_UNCLEAR = "LEGAL_CONSENT_OR_PURPOSE_UNCLEAR"
    RESIDENCY_OR_CROSS_BORDER_UNKNOWN = "RESIDENCY_OR_CROSS_BORDER_UNKNOWN"
    LINKAGE_OR_REIDENTIFICATION_RISK = "LINKAGE_OR_REIDENTIFICATION_RISK"
    AUTHORITY_OR_AUDIT_UNAVAILABLE = "AUTHORITY_OR_AUDIT_UNAVAILABLE"


class Wp007AuthorityClass(StrEnum):
    CLASSIFICATION = "CLASSIFICATION"
    DLP_POLICY = "DLP_POLICY"
    DLP_DISCLOSURE_SECURITY_OWNER = "DLP_DISCLOSURE_SECURITY_OWNER"
    DISCLOSURE = "DISCLOSURE"
    VISUAL_DISPLAY_DISCLOSURE = "VISUAL_DISPLAY_DISCLOSURE"
    VOICE_SPOKEN_DISCLOSURE = "VOICE_SPOKEN_DISCLOSURE"
    EXPORT_API_DISCLOSURE = "EXPORT_API_DISCLOSURE"
    CHANNEL_DESTINATION_APPROVAL = "CHANNEL_DESTINATION_APPROVAL"
    DATA_DOMAIN_OWNER = "DATA_DOMAIN_OWNER"
    PROTECTED_IDENTITY_ACCESS = "PROTECTED_IDENTITY_ACCESS"
    PROTECTED_REVEAL = "PROTECTED_REVEAL"
    PRIVACY_SECURITY_OWNER = "PRIVACY_SECURITY_OWNER"
    PRIVACY_CONSENT_LEGAL_BASIS = "PRIVACY_CONSENT_LEGAL_BASIS"
    PRIVACY_ESCALATION = "PRIVACY_ESCALATION"
    DISCLOSURE_EXCEPTION = "DISCLOSURE_EXCEPTION"
    RESIDENCY_SOVEREIGNTY_CROSS_BORDER = "RESIDENCY_SOVEREIGNTY_CROSS_BORDER"
    EXCEPTION_RENEWAL_REVOCATION = "EXCEPTION_RENEWAL_REVOCATION"
    INDEPENDENT_PRIVACY_SECURITY_REVIEW = "INDEPENDENT_PRIVACY_SECURITY_REVIEW"
    ASSURANCE_AUDIT = "ASSURANCE_AUDIT"


class Wp007AuthorityBoundary(Protocol):
    def assignment_for(self, authority_class: Wp007AuthorityClass) -> str | None: ...


class UnassignedWp007Authorities:
    """No DLP, disclosure, privacy or exception authority is operationally assigned."""

    def assignment_for(self, authority_class: Wp007AuthorityClass) -> str | None:
        del authority_class
        return None


@dataclass(frozen=True, slots=True)
class FieldClassification:
    field_reference: str
    tier: ClassificationTier
    provenance_reference: str

    def __post_init__(self) -> None:
        _validate_reference(self.field_reference, "Field reference")
        _validate_reference(self.provenance_reference, "Classification provenance reference")


def classification_floor(fields: tuple[FieldClassification, ...]) -> ClassificationTier:
    if not fields:
        raise DataLossPrivacyContractError("At least one classified field is required")
    return max(field.tier for field in fields)


@dataclass(frozen=True, slots=True)
class ClassificationTransform:
    field_reference: str
    transform_class: DataTransformClass
    source_tier: ClassificationTier
    resulting_tier: ClassificationTier
    policy_reference: str

    def __post_init__(self) -> None:
        _validate_reference(self.field_reference, "Transform field reference")
        _validate_reference(self.policy_reference, "Transform policy reference")
        if self.resulting_tier < self.source_tier:
            raise DataLossPrivacyContractError(
                "Masking, tokenization, redaction or aggregation cannot lower classification"
            )


@dataclass(frozen=True, slots=True)
class DlpRule:
    rule_reference: str
    path: DlpPath
    maximum_classification: ClassificationTier
    channel_classes: tuple[OutputChannelClass, ...]
    disposition: DlpDisposition
    policy_version: str

    def __post_init__(self) -> None:
        _validate_reference(self.rule_reference, "DLP rule reference")
        _validate_reference(self.policy_version, "DLP rule policy version")
        if not self.channel_classes or len(self.channel_classes) != len(set(self.channel_classes)):
            raise DataLossPrivacyContractError("DLP channel classes must be present and unique")


@dataclass(frozen=True, slots=True)
class DlpRuleRegistry:
    version: str
    entries: tuple[DlpRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "DLP registry version")
        refs = tuple(entry.rule_reference for entry in self.entries)
        if len(refs) != len(set(refs)):
            raise DataLossPrivacyContractError("DLP rule references must be unique")

    def is_empty(self) -> bool:
        return not self.entries

    def exact_match(self, request: DisclosureRequest) -> DlpRule | None:
        floor = classification_floor(request.fields)
        for entry in self.entries:
            if (
                entry.path is request.path
                and entry.rule_reference == request.dlp_rule_reference
                and request.channel_class in entry.channel_classes
                and floor <= entry.maximum_classification
                and entry.policy_version == request.policy_version
            ):
                return entry
        return None


EMPTY_DLP_RULE_REGISTRY: Final = DlpRuleRegistry(DATA_LOSS_PRIVACY_BASELINE_VERSION)


@dataclass(frozen=True, slots=True)
class ChannelDestinationPolicy:
    channel_reference: str
    channel_class: OutputChannelClass
    destination_reference: str
    residency_reference: str
    classification_ceiling: ClassificationTier
    policy_version: str
    active: bool = False
    cross_border_allowed: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.channel_reference, "Channel reference"),
            (self.destination_reference, "Destination reference"),
            (self.residency_reference, "Residency reference"),
            (self.policy_version, "Channel policy version"),
        ):
            _validate_reference(value, label)


@dataclass(frozen=True, slots=True)
class ChannelDestinationRegistry:
    version: str
    entries: tuple[ChannelDestinationPolicy, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Channel registry version")
        refs = tuple(entry.channel_reference for entry in self.entries)
        if len(refs) != len(set(refs)):
            raise DataLossPrivacyContractError("Channel references must be unique")

    def is_empty(self) -> bool:
        return not self.entries

    def exact_match(self, request: DisclosureRequest) -> ChannelDestinationPolicy | None:
        floor = classification_floor(request.fields)
        for entry in self.entries:
            if (
                entry.channel_reference == request.channel_reference
                and entry.channel_class is request.channel_class
                and entry.destination_reference == request.destination_reference
                and entry.residency_reference == request.residency_reference
                and floor <= entry.classification_ceiling
                and entry.policy_version == request.policy_version
                and entry.active
                and entry.cross_border_allowed == request.cross_border
            ):
                return entry
        return None


EMPTY_CHANNEL_DESTINATION_REGISTRY: Final = ChannelDestinationRegistry(
    DATA_LOSS_PRIVACY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class DisclosureAuthorityAssignment:
    assignment_reference: str
    recipient_references: tuple[str, ...]
    channel_class: OutputChannelClass
    purpose_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.assignment_reference, "Disclosure assignment reference"),
            (self.purpose_reference, "Disclosure purpose reference"),
            (self.policy_version, "Disclosure assignment policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.recipient_references, "Disclosure recipient reference")


@dataclass(frozen=True, slots=True)
class DisclosureAuthorityRegistry:
    version: str
    entries: tuple[DisclosureAuthorityAssignment, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Disclosure authority registry version")
        refs = tuple(entry.assignment_reference for entry in self.entries)
        if len(refs) != len(set(refs)):
            raise DataLossPrivacyContractError("Disclosure assignments must be unique")

    def is_empty(self) -> bool:
        return not self.entries

    def exact_match(
        self,
        request: DisclosureRequest,
        decision: DisclosureAuthorityDecision,
    ) -> DisclosureAuthorityAssignment | None:
        for entry in self.entries:
            if (
                entry.assignment_reference == decision.assignment_reference
                and set(entry.recipient_references) == set(request.recipient_references)
                and entry.channel_class is request.channel_class
                and entry.purpose_reference == request.purpose_reference
                and entry.policy_version == request.policy_version
            ):
                return entry
        return None


EMPTY_DISCLOSURE_AUTHORITY_REGISTRY: Final = DisclosureAuthorityRegistry(
    DATA_LOSS_PRIVACY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class DisclosureAuthorityDecision:
    decision_reference: str
    request_reference: str
    assignment_reference: str
    effect: DisclosureEffect
    decided_at: datetime
    expires_at: datetime
    policy_version: str
    reason_code: str
    revoked: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.decision_reference, "Disclosure decision reference"),
            (self.request_reference, "Disclosure request reference"),
            (self.assignment_reference, "Disclosure assignment reference"),
            (self.policy_version, "Disclosure decision policy version"),
            (self.reason_code, "Disclosure decision reason code"),
        ):
            _validate_reference(value, label)
        _validate_instant(self.decided_at, "Disclosure decision time")
        _validate_instant(self.expires_at, "Disclosure decision expiry")
        if self.expires_at <= self.decided_at:
            raise DataLossPrivacyContractError(
                "Disclosure decision expiry must follow decision time"
            )


@dataclass(frozen=True, slots=True)
class RecipientAuthorization:
    recipient_reference: str
    decision: CurrentAuthorizationDecision

    def __post_init__(self) -> None:
        _validate_reference(self.recipient_reference, "Recipient reference")


@dataclass(frozen=True, slots=True)
class DisclosureRequest:
    request_reference: str
    correlation_reference: str
    actor_reference: str
    delegation_reference: str
    recipient_references: tuple[str, ...]
    object_reference: str
    fields: tuple[FieldClassification, ...]
    minimum_necessary_field_references: tuple[str, ...]
    action_reference: str
    purpose_reference: str
    task_reference: str
    context_reference: str
    path: DlpPath
    channel_reference: str
    channel_class: OutputChannelClass
    destination_reference: str
    residency_reference: str
    retention_policy_reference: str
    reuse_policy_reference: str
    dlp_rule_reference: str
    minimization_plan_reference: str
    audit_reference: str
    downstream_handling_reference: str
    effective_at: datetime
    expires_at: datetime
    policy_version: str
    provenance_references: tuple[str, ...]
    masking_plan_reference: str | None = None
    redaction_plan_reference: str | None = None
    suppression_plan_reference: str | None = None
    exception_reference: str | None = None
    legal_basis_reference: str | None = None
    consent_reference: str | None = None
    revoked: bool = False
    cross_border: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Disclosure request reference"),
            (self.correlation_reference, "Disclosure correlation reference"),
            (self.actor_reference, "Disclosure actor reference"),
            (self.delegation_reference, "Disclosure delegation reference"),
            (self.object_reference, "Disclosure object reference"),
            (self.action_reference, "Disclosure action reference"),
            (self.purpose_reference, "Disclosure purpose reference"),
            (self.task_reference, "Disclosure task reference"),
            (self.context_reference, "Disclosure context reference"),
            (self.channel_reference, "Disclosure channel reference"),
            (self.destination_reference, "Disclosure destination reference"),
            (self.residency_reference, "Disclosure residency reference"),
            (self.retention_policy_reference, "Disclosure retention-policy reference"),
            (self.reuse_policy_reference, "Disclosure reuse-policy reference"),
            (self.dlp_rule_reference, "Disclosure DLP-rule reference"),
            (self.minimization_plan_reference, "Disclosure minimization-plan reference"),
            (self.audit_reference, "Disclosure audit reference"),
            (self.downstream_handling_reference, "Downstream-handling reference"),
            (self.policy_version, "Disclosure policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.recipient_references, "Disclosure recipient reference")
        _validate_references(
            self.minimum_necessary_field_references,
            "Minimum-necessary field reference",
        )
        _validate_references(self.provenance_references, "Disclosure provenance reference")
        _validate_optional_reference(self.legal_basis_reference, "Legal-basis reference")
        _validate_optional_reference(self.consent_reference, "Consent reference")
        _validate_optional_reference(self.masking_plan_reference, "Masking-plan reference")
        _validate_optional_reference(self.redaction_plan_reference, "Redaction-plan reference")
        _validate_optional_reference(self.suppression_plan_reference, "Suppression-plan reference")
        _validate_optional_reference(self.exception_reference, "Disclosure exception reference")
        _validate_instant(self.effective_at, "Disclosure effective time")
        _validate_instant(self.expires_at, "Disclosure expiry")
        if self.expires_at <= self.effective_at:
            raise DataLossPrivacyContractError("Disclosure expiry must follow effective time")
        field_refs = tuple(field.field_reference for field in self.fields)
        if not field_refs or len(field_refs) != len(set(field_refs)):
            raise DataLossPrivacyContractError("Classified fields must be present and unique")
        if not set(self.minimum_necessary_field_references).issubset(field_refs):
            raise DataLossPrivacyContractError(
                "Minimum-necessary fields must be a subset of classified fields"
            )


class NoOutputReason(StrEnum):
    REQUEST_NOT_CURRENT = "REQUEST_NOT_CURRENT"
    CURRENT_AUTHORIZATION_REQUIRED = "CURRENT_AUTHORIZATION_REQUIRED"
    RECIPIENT_AUTHORIZATION_REQUIRED = "RECIPIENT_AUTHORIZATION_REQUIRED"
    MINIMIZATION_REQUIRED = "MINIMIZATION_REQUIRED"
    NO_DLP_RULE = "NO_DLP_RULE"
    DLP_CONTROL_REQUIRED = "DLP_CONTROL_REQUIRED"
    NO_ACTIVE_CHANNEL_DESTINATION = "NO_ACTIVE_CHANNEL_DESTINATION"
    CROSS_BORDER_DENIED = "CROSS_BORDER_DENIED"
    DISCLOSURE_AUTHORITY_UNASSIGNED = "DISCLOSURE_AUTHORITY_UNASSIGNED"
    DISCLOSURE_DECISION_NOT_CURRENT = "DISCLOSURE_DECISION_NOT_CURRENT"
    POLICY_SATISFIED_NO_OUTPUT_CAPABILITY = "POLICY_SATISFIED_NO_OUTPUT_CAPABILITY"
    UNTRUSTED_AUTHORITY_CLAIM = "UNTRUSTED_AUTHORITY_CLAIM"


@dataclass(frozen=True, slots=True)
class NoOutputResult:
    reason: NoOutputReason
    classification_floor: ClassificationTier
    dlp_disposition: DlpDisposition
    disclosure_effect: DisclosureEffect = DisclosureEffect.DENY
    output_emitted: bool = False
    serialized: bool = False
    spoken: bool = False
    exported: bool = False
    transmitted: bool = False
    api_released: bool = False
    agent_handoff: bool = False

    def __post_init__(self) -> None:
        if any(
            (
                self.output_emitted,
                self.serialized,
                self.spoken,
                self.exported,
                self.transmitted,
                self.api_released,
                self.agent_handoff,
            )
        ):
            raise DataLossPrivacyContractError("WP-007 cannot emit or transmit output")


class NoOutputDlpBoundary:
    """Evaluate metadata without accepting or returning any content payload."""

    def __init__(
        self,
        dlp_rules: DlpRuleRegistry = EMPTY_DLP_RULE_REGISTRY,
        channels: ChannelDestinationRegistry = EMPTY_CHANNEL_DESTINATION_REGISTRY,
        disclosure_authorities: DisclosureAuthorityRegistry = EMPTY_DISCLOSURE_AUTHORITY_REGISTRY,
    ) -> None:
        self._dlp_rules = dlp_rules
        self._channels = channels
        self._disclosure_authorities = disclosure_authorities

    def evaluate(
        self,
        request: DisclosureRequest,
        actor_authorization: CurrentAuthorizationDecision | None,
        recipient_authorizations: tuple[RecipientAuthorization, ...],
        disclosure_decision: DisclosureAuthorityDecision | None,
        *,
        at: datetime,
    ) -> NoOutputResult:
        _validate_instant(at, "Disclosure evaluation time")
        floor = classification_floor(request.fields)
        if request.revoked or not (request.effective_at <= at < request.expires_at):
            return NoOutputResult(NoOutputReason.REQUEST_NOT_CURRENT, floor, DlpDisposition.DENY)
        if not _current_permit(
            actor_authorization,
            request_reference=request.request_reference,
            policy_version=request.policy_version,
        ):
            return NoOutputResult(
                NoOutputReason.CURRENT_AUTHORIZATION_REQUIRED, floor, DlpDisposition.DENY
            )
        recipient_map = {
            item.recipient_reference: item.decision for item in recipient_authorizations
        }
        if len(recipient_map) != len(recipient_authorizations) or set(recipient_map) != set(
            request.recipient_references
        ):
            return NoOutputResult(
                NoOutputReason.RECIPIENT_AUTHORIZATION_REQUIRED, floor, DlpDisposition.DENY
            )
        if not all(
            _current_permit(
                decision,
                request_reference=request.request_reference,
                policy_version=request.policy_version,
            )
            for decision in recipient_map.values()
        ):
            return NoOutputResult(
                NoOutputReason.RECIPIENT_AUTHORIZATION_REQUIRED, floor, DlpDisposition.DENY
            )
        if set(request.minimum_necessary_field_references) != {
            field.field_reference for field in request.fields
        }:
            return NoOutputResult(
                NoOutputReason.MINIMIZATION_REQUIRED,
                floor,
                DlpDisposition.MINIMIZATION_REQUIRED,
            )
        rule = self._dlp_rules.exact_match(request)
        if rule is None:
            return NoOutputResult(NoOutputReason.NO_DLP_RULE, floor, DlpDisposition.DENY)
        if rule.disposition is not DlpDisposition.POLICY_CHECK_SATISFIED:
            return NoOutputResult(NoOutputReason.DLP_CONTROL_REQUIRED, floor, rule.disposition)
        if request.cross_border:
            return NoOutputResult(NoOutputReason.CROSS_BORDER_DENIED, floor, DlpDisposition.DENY)
        if self._channels.exact_match(request) is None:
            return NoOutputResult(
                NoOutputReason.NO_ACTIVE_CHANNEL_DESTINATION, floor, DlpDisposition.DENY
            )
        if disclosure_decision is None:
            return NoOutputResult(
                NoOutputReason.DISCLOSURE_AUTHORITY_UNASSIGNED,
                floor,
                DlpDisposition.HUMAN_REVIEW_REQUIRED,
            )
        if self._disclosure_authorities.exact_match(request, disclosure_decision) is None:
            return NoOutputResult(
                NoOutputReason.DISCLOSURE_AUTHORITY_UNASSIGNED,
                floor,
                DlpDisposition.HUMAN_REVIEW_REQUIRED,
            )
        if (
            disclosure_decision.request_reference != request.request_reference
            or disclosure_decision.policy_version != request.policy_version
            or disclosure_decision.effect is not DisclosureEffect.PERMIT
            or disclosure_decision.revoked
            or not (disclosure_decision.decided_at <= at < disclosure_decision.expires_at)
        ):
            return NoOutputResult(
                NoOutputReason.DISCLOSURE_DECISION_NOT_CURRENT,
                floor,
                DlpDisposition.DENY,
            )
        return NoOutputResult(
            NoOutputReason.POLICY_SATISFIED_NO_OUTPUT_CAPABILITY,
            floor,
            DlpDisposition.POLICY_CHECK_SATISFIED,
        )


@dataclass(frozen=True, slots=True)
class OpaqueProtectedIdentityReference:
    reference: str
    handling_class: ProtectedIdentityHandlingClass
    classification: ClassificationTier
    policy_version: str

    def __post_init__(self) -> None:
        _validate_reference(self.reference, "Protected-identity reference")
        if not self.reference.startswith("identity-ref:"):
            raise DataLossPrivacyContractError(
                "Protected identity must use the opaque identity-ref namespace"
            )
        _validate_reference(self.policy_version, "Protected-identity policy version")
        if self.classification < ClassificationTier.PROTECTED:
            raise DataLossPrivacyContractError(
                "Protected identity cannot be classified below PROTECTED"
            )


@dataclass(frozen=True, slots=True)
class ProtectedIdentityAccessRule:
    rule_reference: str
    handling_class: ProtectedIdentityHandlingClass
    purpose_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        _validate_reference(self.rule_reference, "Protected-identity rule reference")
        _validate_reference(self.purpose_reference, "Protected-identity purpose reference")
        _validate_reference(self.policy_version, "Protected-identity rule policy version")


@dataclass(frozen=True, slots=True)
class ProtectedIdentityAccessRegistry:
    version: str
    entries: tuple[ProtectedIdentityAccessRule, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Protected-identity registry version")
        refs = tuple(entry.rule_reference for entry in self.entries)
        if len(refs) != len(set(refs)):
            raise DataLossPrivacyContractError("Protected-identity rules must be unique")

    def is_empty(self) -> bool:
        return not self.entries


EMPTY_PROTECTED_IDENTITY_ACCESS_REGISTRY: Final = ProtectedIdentityAccessRegistry(
    DATA_LOSS_PRIVACY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class PrivacyAuthorityAssignment:
    assignment_reference: str
    authority_class: Wp007AuthorityClass
    policy_version: str

    def __post_init__(self) -> None:
        _validate_reference(self.assignment_reference, "Privacy assignment reference")
        _validate_reference(self.policy_version, "Privacy assignment policy version")


@dataclass(frozen=True, slots=True)
class PrivacyAuthorityRegistry:
    version: str
    entries: tuple[PrivacyAuthorityAssignment, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Privacy authority registry version")
        refs = tuple(entry.assignment_reference for entry in self.entries)
        if len(refs) != len(set(refs)):
            raise DataLossPrivacyContractError("Privacy authority assignments must be unique")

    def is_empty(self) -> bool:
        return not self.entries


EMPTY_PRIVACY_AUTHORITY_REGISTRY: Final = PrivacyAuthorityRegistry(
    DATA_LOSS_PRIVACY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class NoRevealResult:
    reason_code: str
    revealed: bool = False
    retrieved: bool = False
    unmasked: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.reason_code, "No-reveal reason code")
        if self.revealed or self.retrieved or self.unmasked:
            raise DataLossPrivacyContractError("WP-007 cannot retrieve, unmask or reveal identity")


class NoRevealProtectedIdentityBoundary:
    def __init__(
        self,
        registry: ProtectedIdentityAccessRegistry = EMPTY_PROTECTED_IDENTITY_ACCESS_REGISTRY,
    ) -> None:
        self._registry = registry

    def evaluate(
        self,
        reference: OpaqueProtectedIdentityReference,
        authorization: CurrentAuthorizationDecision | None,
        *,
        request_reference: str,
        purpose_reference: str,
        audit_boundary_available: bool,
    ) -> NoRevealResult:
        _validate_reference(request_reference, "Protected-identity request reference")
        _validate_reference(purpose_reference, "Protected-identity purpose reference")
        if not _current_permit(
            authorization,
            request_reference=request_reference,
            policy_version=reference.policy_version,
        ):
            return NoRevealResult("CURRENT_AUTHORIZATION_REQUIRED")
        if not audit_boundary_available:
            return NoRevealResult("REQUIRED_AUDIT_BOUNDARY_UNAVAILABLE")
        if self._registry.is_empty():
            return NoRevealResult("NO_PROTECTED_IDENTITY_ACCESS_RULE")
        return NoRevealResult("PROTECTED_IDENTITY_REVEAL_CAPABILITY_ABSENT")


@dataclass(frozen=True, slots=True)
class PrivacyEscalationRequest:
    request_reference: str
    correlation_reference: str
    reasons: tuple[PrivacyEscalationReason, ...]
    policy_version: str

    def __post_init__(self) -> None:
        _validate_reference(self.request_reference, "Privacy escalation request reference")
        _validate_reference(self.correlation_reference, "Privacy escalation correlation reference")
        _validate_reference(self.policy_version, "Privacy escalation policy version")
        if not self.reasons or len(self.reasons) != len(set(self.reasons)):
            raise DataLossPrivacyContractError("Escalation reasons must be present and unique")


@dataclass(frozen=True, slots=True)
class PrivacyEscalationResult:
    disposition: PrivacyEscalationDisposition
    decision_created: bool = False
    authority_assigned: bool = False

    def __post_init__(self) -> None:
        if self.decision_created or self.authority_assigned:
            raise DataLossPrivacyContractError("Privacy escalation cannot create authority")


class PrivacyEscalationBoundary:
    def escalate(self, request: PrivacyEscalationRequest) -> PrivacyEscalationResult:
        del request
        return PrivacyEscalationResult(PrivacyEscalationDisposition.HUMAN_DECISION_REQUIRED)


class NonWaivableProtection(StrEnum):
    HUMAN_PRIMARY_AUTHORITY = "HUMAN_PRIMARY_AUTHORITY"
    CURRENT_FOUR_LAYER_AUTHORIZATION = "CURRENT_FOUR_LAYER_AUTHORIZATION"
    NO_CLASSIFICATION_DOWNGRADE = "NO_CLASSIFICATION_DOWNGRADE"
    UNKNOWN_MEANS_DENY = "UNKNOWN_MEANS_DENY"
    NO_SELF_APPROVAL_OR_IMPLICIT_RENEWAL = "NO_SELF_APPROVAL_OR_IMPLICIT_RENEWAL"
    NO_PROTECTED_MATERIAL_IN_OUTPUT = "NO_PROTECTED_MATERIAL_IN_OUTPUT"
    NO_UNAPPROVED_CROSS_BORDER_TRANSFER = "NO_UNAPPROVED_CROSS_BORDER_TRANSFER"
    NO_DIRECT_MEMORY_OR_PERMISSION_POOLING = "NO_DIRECT_MEMORY_OR_PERMISSION_POOLING"
    NO_UNAUDITED_PROTECTED_REVEAL = "NO_UNAUDITED_PROTECTED_REVEAL"
    NO_REAL_IDENTITY_OR_GOVERNED_DATA = "NO_REAL_IDENTITY_OR_GOVERNED_DATA"


ALL_NON_WAIVABLE_PROTECTIONS: Final = frozenset(NonWaivableProtection)


@dataclass(frozen=True, slots=True)
class DisclosureException:
    exception_reference: str
    exception_type_reference: str
    requester_reference: str
    accountable_human_reference: str
    approver_reference: str
    object_reference: str
    field_references: tuple[str, ...]
    classification: ClassificationTier
    handling_class: ProtectedIdentityHandlingClass
    recipient_references: tuple[str, ...]
    purpose_reference: str
    channel_reference: str
    destination_reference: str
    residency_reference: str
    legal_basis_reference: str
    consent_reference: str
    authorization_reference: str
    dlp_decision_reference: str
    disclosure_decision_reference: str
    minimization_plan_reference: str
    compensating_control_references: tuple[str, ...]
    independent_review_reference: str
    provenance_reference: str
    audit_reference: str
    deletion_reconciliation_reference: str
    effective_at: datetime
    expires_at: datetime
    policy_version: str
    protections: frozenset[NonWaivableProtection] = ALL_NON_WAIVABLE_PROTECTIONS
    revoked: bool = False
    creates_capability: bool = False
    repeals_policy: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.exception_reference, "Exception reference"),
            (self.exception_type_reference, "Exception type reference"),
            (self.requester_reference, "Exception requester reference"),
            (self.accountable_human_reference, "Accountable Human reference"),
            (self.approver_reference, "Exception approver reference"),
            (self.object_reference, "Exception object reference"),
            (self.purpose_reference, "Exception purpose reference"),
            (self.channel_reference, "Exception channel reference"),
            (self.destination_reference, "Exception destination reference"),
            (self.residency_reference, "Exception residency reference"),
            (self.legal_basis_reference, "Exception legal-basis reference"),
            (self.consent_reference, "Exception consent reference"),
            (self.authorization_reference, "Exception authorization reference"),
            (self.dlp_decision_reference, "Exception DLP decision reference"),
            (self.disclosure_decision_reference, "Exception disclosure decision reference"),
            (self.minimization_plan_reference, "Exception minimization-plan reference"),
            (self.independent_review_reference, "Independent review reference"),
            (self.provenance_reference, "Exception provenance reference"),
            (self.audit_reference, "Exception audit reference"),
            (self.deletion_reconciliation_reference, "Deletion obligation reference"),
            (self.policy_version, "Exception policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.field_references, "Exception field reference")
        _validate_references(self.recipient_references, "Exception recipient reference")
        _validate_references(self.compensating_control_references, "Compensating-control reference")
        _validate_instant(self.effective_at, "Exception effective time")
        _validate_instant(self.expires_at, "Exception expiry")
        if self.expires_at <= self.effective_at:
            raise DataLossPrivacyContractError("Exception expiry must follow effective time")
        if self.requester_reference == self.approver_reference:
            raise DataLossPrivacyContractError("An exception cannot be self-approved")
        if self.protections != ALL_NON_WAIVABLE_PROTECTIONS:
            raise DataLossPrivacyContractError("Every non-waivable protection must remain present")
        if self.creates_capability or self.repeals_policy:
            raise DataLossPrivacyContractError(
                "An exception cannot create capability or repeal policy"
            )

    def is_current(self, at: datetime) -> bool:
        _validate_instant(at, "Exception evaluation time")
        return not self.revoked and self.effective_at <= at < self.expires_at


@dataclass(frozen=True, slots=True)
class DisclosureExceptionRegistry:
    version: str
    entries: tuple[DisclosureException, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Exception registry version")
        refs = tuple(entry.exception_reference for entry in self.entries)
        if len(refs) != len(set(refs)):
            raise DataLossPrivacyContractError("Exception references must be unique")

    def is_empty(self) -> bool:
        return not self.entries


EMPTY_DISCLOSURE_EXCEPTION_REGISTRY: Final = DisclosureExceptionRegistry(
    DATA_LOSS_PRIVACY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class UntrustedDisclosureClaim:
    claim_reference: str
    origin: UntrustedContentOrigin
    claims_public: bool = False
    claims_authorized: bool = False
    claims_consented: bool = False
    claims_exception: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.claim_reference, "Untrusted disclosure claim reference")


def evaluate_untrusted_disclosure_claim(claim: UntrustedDisclosureClaim) -> NoOutputResult:
    del claim
    return NoOutputResult(
        NoOutputReason.UNTRUSTED_AUTHORITY_CLAIM,
        ClassificationTier.SENSITIVE,
        DlpDisposition.DENY,
    )


@dataclass(frozen=True, slots=True)
class DataLossPrivacySignal:
    correlation_reference: str
    boundary_reference: str
    reason_code: str
    policy_version: str
    authoritative: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.correlation_reference, "Signal correlation reference"),
            (self.boundary_reference, "Signal boundary reference"),
            (self.reason_code, "Signal reason code"),
            (self.policy_version, "Signal policy version"),
        ):
            _validate_reference(value, label)
        if self.authoritative:
            raise DataLossPrivacyContractError("WP-007 signals are non-authoritative")
