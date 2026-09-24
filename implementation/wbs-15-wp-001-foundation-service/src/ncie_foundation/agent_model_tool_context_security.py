"""Inert, provider-neutral security boundaries for WBS-16-WP-006."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from re import compile as compile_pattern
from typing import Final, Protocol

from .security_authorization import AuthorizationEffect, CurrentAuthorizationDecision

AGENT_SECURITY_BASELINE_VERSION: Final = "NCIE-WBS16-WP006-2026-09-24"
AGENT_SECURITY_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-24-023"
AGENT_SECURITY_IMPLEMENTATION_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-24-024"

_REFERENCE_PATTERN: Final = compile_pattern(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}")
_DENY_SENTINELS: Final = frozenset({"unassigned", "unspecified", "unknown"})
_PROTECTED_FRAGMENTS: Final = (
    "-----begin",
    "api_key",
    "credential_value",
    "private_key",
    "secret_value",
    "token_value",
)


class AgentSecurityContractError(ValueError):
    """Raised without echoing protected input when a WP-006 contract is invalid."""


def _validate_reference(value: str, label: str) -> None:
    normalized = value.lower()
    if (
        _REFERENCE_PATTERN.fullmatch(value) is None
        or normalized in _DENY_SENTINELS
        or any(fragment in normalized for fragment in _PROTECTED_FRAGMENTS)
    ):
        raise AgentSecurityContractError(f"{label} is invalid or contains protected material")


def _validate_references(values: tuple[str, ...], label: str, *, required: bool = True) -> None:
    if required and not values:
        raise AgentSecurityContractError(f"{label} is required")
    if len(values) != len(set(values)):
        raise AgentSecurityContractError(f"{label} must not contain duplicates")
    for value in values:
        _validate_reference(value, label)


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


def _validate_instant(value: datetime, label: str) -> None:
    if value.tzinfo is None or value.utcoffset() is None:
        raise AgentSecurityContractError(f"{label} must include a timezone")


class InstitutionalAuthorityClass(StrEnum):
    AGENT_FACTORY_SECURITY_CEILING = "AGENT_FACTORY_SECURITY_CEILING"
    EPHEMERAL_AGENT_ACTIVATION = "EPHEMERAL_AGENT_ACTIVATION"
    AGENT_REGISTRATION_PROMOTION = "AGENT_REGISTRATION_PROMOTION"
    AGENT_SUSPENSION_KILL = "AGENT_SUSPENSION_KILL"
    GENERATED_CODE_ENGINEERING_REVIEW = "GENERATED_CODE_ENGINEERING_REVIEW"
    GENERATED_CODE_SECURITY_REVIEW = "GENERATED_CODE_SECURITY_REVIEW"
    GENERATED_CODE_PROMOTION = "GENERATED_CODE_PROMOTION"
    MODEL_APPROVAL = "MODEL_APPROVAL"
    PROVIDER_SECURITY_ACCEPTANCE = "PROVIDER_SECURITY_ACCEPTANCE"
    RESTRICTED_DATA_PROVIDER_COMBINATION = "RESTRICTED_DATA_PROVIDER_COMBINATION"
    AFRICAN_DATA_RESIDENCY_CROSS_BORDER = "AFRICAN_DATA_RESIDENCY_CROSS_BORDER"
    PRIVACY_LEGAL_REVIEW = "PRIVACY_LEGAL_REVIEW"
    MODEL_PROVIDER_EMERGENCY_SUSPENSION = "MODEL_PROVIDER_EMERGENCY_SUSPENSION"
    INDEPENDENT_MODEL_SECURITY_EVALUATION = "INDEPENDENT_MODEL_SECURITY_EVALUATION"
    TOOL_RISK_CLASSIFICATION = "TOOL_RISK_CLASSIFICATION"
    TOOL_REGISTRATION_ELIGIBILITY = "TOOL_REGISTRATION_ELIGIBILITY"
    HIGH_RISK_DISCLOSURE_APPROVAL = "HIGH_RISK_DISCLOSURE_APPROVAL"
    CONSEQUENTIAL_ACTION_APPROVAL = "CONSEQUENTIAL_ACTION_APPROVAL"
    TOOL_EMERGENCY_SUSPENSION = "TOOL_EMERGENCY_SUSPENSION"
    TOOL_SECURITY_INDEPENDENT_REVIEW = "TOOL_SECURITY_INDEPENDENT_REVIEW"
    CROSS_CONTEXT_EXCEPTION = "CROSS_CONTEXT_EXCEPTION"
    SOURCE_CONTEXT_OWNER = "SOURCE_CONTEXT_OWNER"
    DESTINATION_CONTEXT_OWNER = "DESTINATION_CONTEXT_OWNER"
    PRIVACY_CONSENT_REVIEW = "PRIVACY_CONSENT_REVIEW"
    CLASSIFICATION_DISCLOSURE = "CLASSIFICATION_DISCLOSURE"
    INDEPENDENT_CONTEXT_SECURITY_REVIEW = "INDEPENDENT_CONTEXT_SECURITY_REVIEW"


class InstitutionalAuthorityBoundary(Protocol):
    def assignment_for(self, authority_class: InstitutionalAuthorityClass) -> str | None: ...


class UnassignedInstitutionalAuthorities:
    """No WP-006 operational authority holder is assigned."""

    def assignment_for(self, authority_class: InstitutionalAuthorityClass) -> str | None:
        del authority_class
        return None


class AgentPrimitiveClass(StrEnum):
    MODEL = "MODEL"
    TOOL = "TOOL"
    DATA_CLASS = "DATA_CLASS"
    CONTEXT = "CONTEXT"
    SCHEMA = "SCHEMA"
    POLICY = "POLICY"
    EXECUTION_RUNTIME = "EXECUTION_RUNTIME"


@dataclass(frozen=True, slots=True)
class AgentPrimitive:
    primitive_reference: str
    primitive_class: AgentPrimitiveClass
    policy_version: str

    def __post_init__(self) -> None:
        _validate_reference(self.primitive_reference, "Agent primitive reference")
        _validate_reference(self.policy_version, "Agent primitive policy version")


@dataclass(frozen=True, slots=True)
class AgentPrimitiveRegistry:
    version: str
    entries: tuple[AgentPrimitive, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Agent primitive registry version")
        references = tuple(entry.primitive_reference for entry in self.entries)
        if len(references) != len(set(references)):
            raise AgentSecurityContractError("Agent primitive references must be unique")

    def contains(self, reference: str, primitive_class: AgentPrimitiveClass) -> bool:
        return any(
            entry.primitive_reference == reference and entry.primitive_class is primitive_class
            for entry in self.entries
        )

    def is_empty(self) -> bool:
        return not self.entries


EMPTY_AGENT_PRIMITIVE_REGISTRY: Final = AgentPrimitiveRegistry(
    version=AGENT_SECURITY_BASELINE_VERSION
)


class ResourceCeilingDimension(StrEnum):
    RUNTIME = "RUNTIME"
    TOKENS = "TOKENS"
    MODEL_CALLS = "MODEL_CALLS"
    TOOL_CALLS = "TOOL_CALLS"
    CONCURRENCY = "CONCURRENCY"
    CONTEXT_VOLUME = "CONTEXT_VOLUME"
    COMPUTE = "COMPUTE"
    STORAGE = "STORAGE"


ALL_RESOURCE_CEILING_DIMENSIONS: Final = tuple(ResourceCeilingDimension)


@dataclass(frozen=True, slots=True)
class AgentSecurityCeiling:
    ceiling_reference: str
    policy_version: str
    resource_limit_references: tuple[tuple[ResourceCeilingDimension, str], ...]
    network_access_allowed: bool = False
    external_egress_allowed: bool = False
    persistent_memory_allowed: bool = False
    recursive_synthesis_allowed: bool = False
    self_registration_allowed: bool = False
    automatic_promotion_allowed: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.ceiling_reference, "Agent ceiling reference")
        _validate_reference(self.policy_version, "Agent ceiling policy version")
        dimensions = tuple(dimension for dimension, _ in self.resource_limit_references)
        if set(dimensions) != set(ALL_RESOURCE_CEILING_DIMENSIONS) or len(dimensions) != len(
            ALL_RESOURCE_CEILING_DIMENSIONS
        ):
            raise AgentSecurityContractError("Every resource ceiling dimension must appear once")
        for _, reference in self.resource_limit_references:
            _validate_reference(reference, "Resource limit reference")
        if any(
            (
                self.network_access_allowed,
                self.external_egress_allowed,
                self.persistent_memory_allowed,
                self.recursive_synthesis_allowed,
                self.self_registration_allowed,
                self.automatic_promotion_allowed,
            )
        ):
            raise AgentSecurityContractError("WP-006 Agent capabilities must remain disabled")


@dataclass(frozen=True, slots=True)
class AgentDefinition:
    definition_reference: str
    purpose_reference: str
    task_reference: str
    input_schema_reference: str
    output_schema_reference: str
    model_reference: str
    tool_references: tuple[str, ...]
    data_class_references: tuple[str, ...]
    context_reference: str
    execution_runtime_reference: str
    authorization_policy_reference: str
    delegation_depth_policy_reference: str
    egress_policy_reference: str
    persistence_policy_reference: str
    vpf_profile_reference: str
    ceiling: AgentSecurityCeiling
    provenance_reference: str
    evaluation_reference: str
    expiry_policy_reference: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.definition_reference, "Agent definition reference"),
            (self.purpose_reference, "Agent purpose reference"),
            (self.task_reference, "Agent task reference"),
            (self.input_schema_reference, "Agent input schema reference"),
            (self.output_schema_reference, "Agent output schema reference"),
            (self.model_reference, "Agent model reference"),
            (self.context_reference, "Agent context reference"),
            (self.execution_runtime_reference, "Agent execution-runtime reference"),
            (self.authorization_policy_reference, "Agent authorization policy reference"),
            (self.delegation_depth_policy_reference, "Agent delegation-depth policy reference"),
            (self.egress_policy_reference, "Agent egress policy reference"),
            (self.persistence_policy_reference, "Agent persistence policy reference"),
            (self.vpf_profile_reference, "Agent VPF profile reference"),
            (self.provenance_reference, "Agent provenance reference"),
            (self.evaluation_reference, "Agent evaluation reference"),
            (self.expiry_policy_reference, "Agent expiry policy reference"),
        ):
            _validate_reference(value, label)
        _validate_references(self.tool_references, "Agent Tool reference", required=False)
        _validate_references(self.data_class_references, "Agent data-class reference")


class GeneratedCodeState(StrEnum):
    NOT_APPROVED_FOR_EXECUTION = "NOT_APPROVED_FOR_EXECUTION"


@dataclass(frozen=True, slots=True)
class GeneratedCodeQuarantineMetadata:
    artifact_reference: str
    provenance_reference: str
    policy_version: str
    state: GeneratedCodeState = GeneratedCodeState.NOT_APPROVED_FOR_EXECUTION
    generated: bool = False
    compiled: bool = False
    imported: bool = False
    loaded: bool = False
    executed: bool = False
    promoted: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.artifact_reference, "Generated-code artifact reference")
        _validate_reference(self.provenance_reference, "Generated-code provenance reference")
        _validate_reference(self.policy_version, "Generated-code policy version")
        if any(
            (
                self.generated,
                self.compiled,
                self.imported,
                self.loaded,
                self.executed,
                self.promoted,
            )
        ):
            raise AgentSecurityContractError("Generated executable-code operations are prohibited")


class BoundaryDisposition(StrEnum):
    VALIDATED_NO_CAPABILITY = "VALIDATED_NO_CAPABILITY"
    DENIED = "DENIED"


@dataclass(frozen=True, slots=True)
class BoundaryResult:
    disposition: BoundaryDisposition
    reason_code: str
    capability_granted: bool = False
    external_operation_executed: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.reason_code, "Boundary reason code")
        if self.capability_granted or self.external_operation_executed:
            raise AgentSecurityContractError("WP-006 results cannot grant or execute capability")


class ZeroCapabilityAgentFactory:
    """Validate synthetic definitions without creating or activating an Agent."""

    def __init__(self, registry: AgentPrimitiveRegistry = EMPTY_AGENT_PRIMITIVE_REGISTRY) -> None:
        self._registry = registry

    def validate(self, definition: AgentDefinition) -> BoundaryResult:
        required: tuple[tuple[str, AgentPrimitiveClass], ...] = (
            (definition.input_schema_reference, AgentPrimitiveClass.SCHEMA),
            (definition.output_schema_reference, AgentPrimitiveClass.SCHEMA),
            (definition.model_reference, AgentPrimitiveClass.MODEL),
            (definition.context_reference, AgentPrimitiveClass.CONTEXT),
            (definition.execution_runtime_reference, AgentPrimitiveClass.EXECUTION_RUNTIME),
            (definition.authorization_policy_reference, AgentPrimitiveClass.POLICY),
        )
        required += tuple(
            (reference, AgentPrimitiveClass.TOOL) for reference in definition.tool_references
        )
        required += tuple(
            (reference, AgentPrimitiveClass.DATA_CLASS)
            for reference in definition.data_class_references
        )
        if not all(self._registry.contains(reference, kind) for reference, kind in required):
            return BoundaryResult(BoundaryDisposition.DENIED, "AGENT_PRIMITIVE_UNAVAILABLE")
        return BoundaryResult(
            BoundaryDisposition.VALIDATED_NO_CAPABILITY,
            "SYNTHETIC_DEFINITION_VALIDATED_NO_ACTIVATION",
        )


class ModelLifecycleState(StrEnum):
    CANDIDATE = "CANDIDATE"
    EVALUATED = "EVALUATED"
    APPROVED_ACTIVE = "APPROVED_ACTIVE"
    RESTRICTED = "RESTRICTED"
    SUSPENDED = "SUSPENDED"
    DEPRECATED = "DEPRECATED"
    RETIRED = "RETIRED"


@dataclass(frozen=True, slots=True)
class ModelProviderEligibility:
    combination_reference: str
    provider_reference: str
    model_reference: str
    deployment_reference: str
    data_class_reference: str
    classification_reference: str
    purpose_reference: str
    task_reference: str
    residency_reference: str
    retention_reuse_policy_reference: str
    security_assurance_reference: str
    tool_requirement_reference: str
    output_policy_reference: str
    lifecycle_state: ModelLifecycleState
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.combination_reference, "Model combination reference"),
            (self.provider_reference, "Provider reference"),
            (self.model_reference, "Model reference"),
            (self.deployment_reference, "Deployment reference"),
            (self.data_class_reference, "Model data-class reference"),
            (self.classification_reference, "Model classification reference"),
            (self.purpose_reference, "Model purpose reference"),
            (self.task_reference, "Model task reference"),
            (self.residency_reference, "Model residency reference"),
            (self.retention_reuse_policy_reference, "Model retention policy reference"),
            (self.security_assurance_reference, "Model assurance reference"),
            (self.tool_requirement_reference, "Model Tool requirement reference"),
            (self.output_policy_reference, "Model output policy reference"),
            (self.policy_version, "Model policy version"),
        ):
            _validate_reference(value, label)


@dataclass(frozen=True, slots=True)
class ModelEligibilityRegistry:
    version: str
    entries: tuple[ModelProviderEligibility, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Model eligibility registry version")
        references = tuple(entry.combination_reference for entry in self.entries)
        if len(references) != len(set(references)):
            raise AgentSecurityContractError("Model combination references must be unique")

    def is_empty(self) -> bool:
        return not self.entries

    def exact_match(self, request: ModelRouteRequest) -> ModelProviderEligibility | None:
        for entry in self.entries:
            if (
                entry.provider_reference == request.provider_reference
                and entry.model_reference == request.model_reference
                and entry.deployment_reference == request.deployment_reference
                and entry.data_class_reference == request.data_class_reference
                and entry.classification_reference == request.classification_reference
                and entry.purpose_reference == request.purpose_reference
                and entry.task_reference == request.task_reference
                and entry.residency_reference == request.residency_reference
                and entry.retention_reuse_policy_reference
                == request.retention_reuse_policy_reference
                and entry.security_assurance_reference == request.security_assurance_reference
                and entry.tool_requirement_reference == request.tool_requirement_reference
                and entry.output_policy_reference == request.output_policy_reference
                and entry.policy_version == request.policy_version
                and entry.lifecycle_state is ModelLifecycleState.APPROVED_ACTIVE
            ):
                return entry
        return None


EMPTY_MODEL_ELIGIBILITY_REGISTRY: Final = ModelEligibilityRegistry(
    version=AGENT_SECURITY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class ModelRouteRequest:
    request_reference: str
    provider_reference: str
    model_reference: str
    deployment_reference: str
    data_class_reference: str
    classification_reference: str
    purpose_reference: str
    task_reference: str
    residency_reference: str
    retention_reuse_policy_reference: str
    security_assurance_reference: str
    tool_requirement_reference: str
    output_policy_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Model-route request reference"),
            (self.provider_reference, "Model-route provider reference"),
            (self.model_reference, "Model-route model reference"),
            (self.deployment_reference, "Model-route deployment reference"),
            (self.data_class_reference, "Model-route data-class reference"),
            (self.classification_reference, "Model-route classification reference"),
            (self.purpose_reference, "Model-route purpose reference"),
            (self.task_reference, "Model-route task reference"),
            (self.residency_reference, "Model-route residency reference"),
            (self.retention_reuse_policy_reference, "Model-route retention policy reference"),
            (self.security_assurance_reference, "Model-route assurance reference"),
            (self.tool_requirement_reference, "Model-route Tool requirement reference"),
            (self.output_policy_reference, "Model-route output policy reference"),
            (self.policy_version, "Model-route policy version"),
        ):
            _validate_reference(value, label)


class NoRouteModelGateway:
    """Evaluate eligibility while exposing no provider adapter or call path."""

    def __init__(
        self, registry: ModelEligibilityRegistry = EMPTY_MODEL_ELIGIBILITY_REGISTRY
    ) -> None:
        self._registry = registry

    def evaluate(
        self,
        request: ModelRouteRequest,
        authorization: CurrentAuthorizationDecision | None,
    ) -> BoundaryResult:
        if not _current_permit(
            authorization,
            request_reference=request.request_reference,
            policy_version=request.policy_version,
        ):
            return BoundaryResult(BoundaryDisposition.DENIED, "CURRENT_AUTHORIZATION_REQUIRED")
        if self._registry.exact_match(request) is None:
            return BoundaryResult(BoundaryDisposition.DENIED, "NO_ELIGIBLE_MODEL_ROUTE")
        return BoundaryResult(BoundaryDisposition.DENIED, "MODEL_GATEWAY_HAS_NO_ROUTE_CAPABILITY")


class ToolRiskClass(StrEnum):
    READ_ONLY_LOW_DISCLOSURE_RISK = "READ_ONLY_LOW_DISCLOSURE_RISK"
    READ_ONLY_HIGH_DISCLOSURE_RISK = "READ_ONLY_HIGH_DISCLOSURE_RISK"
    STATE_CHANGING_REVERSIBLE = "STATE_CHANGING_REVERSIBLE"
    STATE_CHANGING_CONSEQUENTIAL = "STATE_CHANGING_CONSEQUENTIAL"


HIGH_RISK_TOOL_CLASSES: Final = frozenset(
    {
        ToolRiskClass.READ_ONLY_HIGH_DISCLOSURE_RISK,
        ToolRiskClass.STATE_CHANGING_CONSEQUENTIAL,
    }
)


class ToolRiskPredicate(StrEnum):
    PROTECTED_IDENTITY = "PROTECTED_IDENTITY"
    PRECISE_LOCATION = "PRECISE_LOCATION"
    RESTRICTED_EVIDENCE = "RESTRICTED_EVIDENCE"
    PROTECTED_MATERIAL = "PROTECTED_MATERIAL"
    SECURITY_CONTROL_OR_AUTHORIZATION = "SECURITY_CONTROL_OR_AUTHORIZATION"
    REGISTRY_MUTATION = "REGISTRY_MUTATION"
    EXTERNAL_DISCLOSURE_OR_EXPORT = "EXTERNAL_DISCLOSURE_OR_EXPORT"
    GRAPH_BLOCKING_TRACKING_OR_REGULATORY_ACTION = "GRAPH_BLOCKING_TRACKING_OR_REGULATORY_ACTION"
    CODE_EXECUTION = "CODE_EXECUTION"
    OPERATING_SYSTEM_ACCESS = "OPERATING_SYSTEM_ACCESS"
    DATABASE_ACCESS = "DATABASE_ACCESS"
    NETWORK_EGRESS_OR_EXTERNAL_ACTION = "NETWORK_EGRESS_OR_EXTERNAL_ACTION"
    MISSING_OR_INDETERMINATE = "MISSING_OR_INDETERMINATE"


HIGH_RISK_TOOL_PREDICATES: Final = frozenset(ToolRiskPredicate)


class ToolOutcomeState(StrEnum):
    NOT_INVOKED = "NOT_INVOKED"
    OUTCOME_UNKNOWN = "OUTCOME_UNKNOWN"


@dataclass(frozen=True, slots=True)
class ToolEligibility:
    tool_reference: str
    tool_version_reference: str
    risk_class: ToolRiskClass
    action_reference: str
    target_reference: str
    purpose_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.tool_reference, "Tool reference"),
            (self.tool_version_reference, "Tool version reference"),
            (self.action_reference, "Tool action reference"),
            (self.target_reference, "Tool target reference"),
            (self.purpose_reference, "Tool purpose reference"),
            (self.policy_version, "Tool policy version"),
        ):
            _validate_reference(value, label)


@dataclass(frozen=True, slots=True)
class ToolEligibilityRegistry:
    version: str
    entries: tuple[ToolEligibility, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Tool registry version")
        references = tuple(entry.tool_reference for entry in self.entries)
        if len(references) != len(set(references)):
            raise AgentSecurityContractError("Tool references must be unique")

    def is_empty(self) -> bool:
        return not self.entries

    def exact_match(self, request: ToolRequest) -> ToolEligibility | None:
        for entry in self.entries:
            if (
                entry.tool_reference == request.tool_reference
                and entry.tool_version_reference == request.tool_version_reference
                and entry.risk_class is request.risk_class
                and entry.action_reference == request.action_reference
                and entry.target_reference == request.target_reference
                and entry.purpose_reference == request.purpose_reference
                and entry.policy_version == request.policy_version
            ):
                return entry
        return None


EMPTY_TOOL_ELIGIBILITY_REGISTRY: Final = ToolEligibilityRegistry(
    version=AGENT_SECURITY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class ToolRequest:
    request_reference: str
    actor_reference: str
    delegation_chain_reference: str
    tool_reference: str
    tool_version_reference: str
    risk_class: ToolRiskClass
    action_reference: str
    target_reference: str
    purpose_reference: str
    policy_version: str
    task_reference: str
    context_reference: str
    input_schema_reference: str
    output_schema_reference: str
    classification_ceiling_reference: str
    assurance_reference: str
    correlation_reference: str
    idempotency_reference: str
    expiry_reference: str
    egress_destination_reference: str | None = None
    risk_predicates: tuple[ToolRiskPredicate, ...] = ()
    high_risk_approval_reference: str | None = None
    outcome_state: ToolOutcomeState = ToolOutcomeState.NOT_INVOKED

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Tool-request reference"),
            (self.actor_reference, "Tool actor reference"),
            (self.delegation_chain_reference, "Tool delegation-chain reference"),
            (self.tool_reference, "Tool reference"),
            (self.tool_version_reference, "Tool version reference"),
            (self.action_reference, "Tool action reference"),
            (self.target_reference, "Tool target reference"),
            (self.purpose_reference, "Tool purpose reference"),
            (self.policy_version, "Tool policy version"),
            (self.task_reference, "Tool task reference"),
            (self.context_reference, "Tool context reference"),
            (self.input_schema_reference, "Tool input schema reference"),
            (self.output_schema_reference, "Tool output schema reference"),
            (self.classification_ceiling_reference, "Tool classification ceiling reference"),
            (self.assurance_reference, "Tool assurance reference"),
            (self.correlation_reference, "Tool correlation reference"),
            (self.idempotency_reference, "Tool idempotency reference"),
            (self.expiry_reference, "Tool expiry reference"),
        ):
            _validate_reference(value, label)
        if len(self.risk_predicates) != len(set(self.risk_predicates)):
            raise AgentSecurityContractError("Tool risk predicates must not contain duplicates")
        if self.egress_destination_reference is not None:
            _validate_reference(
                self.egress_destination_reference, "Tool egress destination reference"
            )
        if self.high_risk_approval_reference is not None:
            _validate_reference(self.high_risk_approval_reference, "High-risk approval reference")
        if self.outcome_state is not ToolOutcomeState.NOT_INVOKED:
            raise AgentSecurityContractError(
                "WP-006 Tool requests cannot claim an invocation outcome"
            )


class NoInvocationToolGateway:
    """Evaluate exact Tool metadata while exposing no invocation mechanism."""

    def __init__(self, registry: ToolEligibilityRegistry = EMPTY_TOOL_ELIGIBILITY_REGISTRY) -> None:
        self._registry = registry

    def evaluate(
        self,
        request: ToolRequest,
        authorization: CurrentAuthorizationDecision | None,
    ) -> BoundaryResult:
        if not _current_permit(
            authorization,
            request_reference=request.request_reference,
            policy_version=request.policy_version,
        ):
            return BoundaryResult(BoundaryDisposition.DENIED, "CURRENT_AUTHORIZATION_REQUIRED")
        if self._registry.exact_match(request) is None:
            return BoundaryResult(BoundaryDisposition.DENIED, "TOOL_NOT_REGISTERED_OR_ELIGIBLE")
        high_risk = request.risk_class in HIGH_RISK_TOOL_CLASSES or any(
            predicate in HIGH_RISK_TOOL_PREDICATES for predicate in request.risk_predicates
        )
        if high_risk:
            if request.high_risk_approval_reference is None:
                return BoundaryResult(BoundaryDisposition.DENIED, "HIGH_RISK_APPROVAL_REQUIRED")
            return BoundaryResult(BoundaryDisposition.DENIED, "HIGH_RISK_AUTHORITY_UNASSIGNED")
        return BoundaryResult(
            BoundaryDisposition.DENIED, "TOOL_GATEWAY_HAS_NO_INVOCATION_CAPABILITY"
        )


class UntrustedContentOrigin(StrEnum):
    AGENT_OUTPUT = "AGENT_OUTPUT"
    MODEL_OUTPUT = "MODEL_OUTPUT"
    TOOL_OUTPUT = "TOOL_OUTPUT"
    EVIDENCE = "EVIDENCE"
    DOCUMENT = "DOCUMENT"
    MEMORY = "MEMORY"
    WEB = "WEB"
    API = "API"


@dataclass(frozen=True, slots=True)
class UntrustedInstructionSignal:
    content_reference: str
    origin: UntrustedContentOrigin
    instruction_shaped: bool
    requests_policy_change: bool = False
    requests_authority_change: bool = False
    requests_purpose_change: bool = False
    requests_target_change: bool = False
    requests_context_change: bool = False
    requests_egress_change: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.content_reference, "Untrusted-content reference")


class PromptInjectionBoundary:
    """Treat instruction-shaped external content as data with no authority."""

    def evaluate(self, signal: UntrustedInstructionSignal) -> BoundaryResult:
        attempted_control_change = any(
            (
                signal.requests_policy_change,
                signal.requests_authority_change,
                signal.requests_purpose_change,
                signal.requests_target_change,
                signal.requests_context_change,
                signal.requests_egress_change,
            )
        )
        if signal.instruction_shaped or attempted_control_change:
            return BoundaryResult(
                BoundaryDisposition.DENIED, "UNTRUSTED_INSTRUCTION_HAS_NO_AUTHORITY"
            )
        return BoundaryResult(
            BoundaryDisposition.VALIDATED_NO_CAPABILITY,
            "UNTRUSTED_DATA_CLASSIFIED_NO_AUTHORITY",
        )


class ContextClass(StrEnum):
    PRIVATE_USER = "PRIVATE_USER"
    SESSION_WORKSPACE = "SESSION_WORKSPACE"
    COLLABORATIVE_ROOM = "COLLABORATIVE_ROOM"
    INVESTIGATION = "INVESTIGATION"
    SITUATION_TASK = "SITUATION_TASK"
    AGENT_RUN = "AGENT_RUN"
    DECISION_TIME_HISTORICAL = "DECISION_TIME_HISTORICAL"
    INSTITUTIONAL_APPROVED_KNOWLEDGE = "INSTITUTIONAL_APPROVED_KNOWLEDGE"


@dataclass(frozen=True, slots=True)
class CrossContextException:
    exception_reference: str
    source_context_reference: str
    source_context_class: ContextClass
    destination_context_reference: str
    destination_context_class: ContextClass
    data_class_reference: str
    purpose_reference: str
    actor_reference: str
    accountable_human_reference: str
    field_references: tuple[str, ...]
    classification_reference: str
    legal_consent_authority_references: tuple[str, ...]
    source_authorization_reference: str
    destination_authorization_reference: str
    minimum_necessary_justification_reference: str
    processing_destination_reference: str
    storage_destination_reference: str
    residency_reference: str
    source_owner_decision_reference: str
    destination_owner_decision_reference: str
    independent_review_reference: str
    provenance_reference: str
    audit_reference: str
    downstream_dependency_references: tuple[str, ...]
    deletion_reconciliation_reference: str
    effective_at: datetime
    expires_at: datetime
    policy_version: str
    revoked: bool = False

    def __post_init__(self) -> None:
        for value, label in (
            (self.exception_reference, "Context exception reference"),
            (self.source_context_reference, "Source context reference"),
            (self.destination_context_reference, "Destination context reference"),
            (self.data_class_reference, "Context data-class reference"),
            (self.purpose_reference, "Context purpose reference"),
            (self.actor_reference, "Context actor reference"),
            (self.accountable_human_reference, "Accountable Human reference"),
            (self.classification_reference, "Context classification reference"),
            (self.source_authorization_reference, "Source authorization reference"),
            (self.destination_authorization_reference, "Destination authorization reference"),
            (
                self.minimum_necessary_justification_reference,
                "Minimum-necessary justification reference",
            ),
            (self.processing_destination_reference, "Processing destination reference"),
            (self.storage_destination_reference, "Storage destination reference"),
            (self.residency_reference, "Residency reference"),
            (self.source_owner_decision_reference, "Source-owner decision reference"),
            (self.destination_owner_decision_reference, "Destination-owner decision reference"),
            (self.independent_review_reference, "Independent review reference"),
            (self.provenance_reference, "Context provenance reference"),
            (self.audit_reference, "Context audit reference"),
            (
                self.deletion_reconciliation_reference,
                "Deletion/reconciliation obligation reference",
            ),
            (self.policy_version, "Context policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.field_references, "Context field reference")
        _validate_references(
            self.legal_consent_authority_references,
            "Legal/consent/authority reference",
        )
        _validate_references(
            self.downstream_dependency_references,
            "Downstream dependency reference",
        )
        _validate_instant(self.effective_at, "Context exception effective time")
        _validate_instant(self.expires_at, "Context exception expiry")
        if self.expires_at <= self.effective_at:
            raise AgentSecurityContractError("Context exception expiry must follow its start")
        if self.source_context_reference == self.destination_context_reference:
            raise AgentSecurityContractError("Cross-context exception requires distinct contexts")


@dataclass(frozen=True, slots=True)
class CrossContextExceptionRegistry:
    version: str
    entries: tuple[CrossContextException, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Context exception registry version")
        references = tuple(entry.exception_reference for entry in self.entries)
        if len(references) != len(set(references)):
            raise AgentSecurityContractError("Context exception references must be unique")

    def is_empty(self) -> bool:
        return not self.entries

    def exact_match(self, request: ContextAccessRequest) -> CrossContextException | None:
        for entry in self.entries:
            if (
                entry.source_context_reference == request.source_context_reference
                and entry.source_context_class is request.source_context_class
                and entry.destination_context_reference == request.destination_context_reference
                and entry.destination_context_class is request.destination_context_class
                and entry.data_class_reference == request.data_class_reference
                and entry.purpose_reference == request.purpose_reference
                and entry.actor_reference == request.actor_reference
                and entry.field_references == request.field_references
                and entry.classification_reference == request.classification_reference
                and entry.policy_version == request.policy_version
            ):
                return entry
        return None


EMPTY_CROSS_CONTEXT_EXCEPTION_REGISTRY: Final = CrossContextExceptionRegistry(
    version=AGENT_SECURITY_BASELINE_VERSION
)


@dataclass(frozen=True, slots=True)
class ContextAccessRequest:
    request_reference: str
    actor_reference: str
    source_context_reference: str
    source_context_class: ContextClass
    destination_context_reference: str
    destination_context_class: ContextClass
    data_class_reference: str
    purpose_reference: str
    field_references: tuple[str, ...]
    classification_reference: str
    temporal_mode_reference: str
    source_scope_reference: str
    relevance_policy_reference: str
    minimum_necessary_filter_reference: str
    policy_version: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.request_reference, "Context request reference"),
            (self.actor_reference, "Context actor reference"),
            (self.source_context_reference, "Source context reference"),
            (self.destination_context_reference, "Destination context reference"),
            (self.data_class_reference, "Context data-class reference"),
            (self.purpose_reference, "Context purpose reference"),
            (self.classification_reference, "Context classification reference"),
            (self.temporal_mode_reference, "Context temporal-mode reference"),
            (self.source_scope_reference, "Context source-scope reference"),
            (self.relevance_policy_reference, "Context relevance policy reference"),
            (
                self.minimum_necessary_filter_reference,
                "Context minimum-necessary filter reference",
            ),
            (self.policy_version, "Context policy version"),
        ):
            _validate_reference(value, label)
        _validate_references(self.field_references, "Context field reference")


class DenyAllCrossContextBoundary:
    """Expose no governed-data retrieval, Memory access or transfer path."""

    def __init__(
        self,
        registry: CrossContextExceptionRegistry = EMPTY_CROSS_CONTEXT_EXCEPTION_REGISTRY,
    ) -> None:
        self._registry = registry

    def evaluate(
        self,
        request: ContextAccessRequest,
        authorization: CurrentAuthorizationDecision | None,
        *,
        at: datetime,
    ) -> BoundaryResult:
        _validate_instant(at, "Context evaluation time")
        if not _current_permit(
            authorization,
            request_reference=request.request_reference,
            policy_version=request.policy_version,
        ):
            return BoundaryResult(BoundaryDisposition.DENIED, "CURRENT_AUTHORIZATION_REQUIRED")
        if request.source_context_reference == request.destination_context_reference:
            return BoundaryResult(BoundaryDisposition.DENIED, "NO_CONTEXT_RETRIEVAL_CAPABILITY")
        exception = self._registry.exact_match(request)
        if exception is None:
            return BoundaryResult(BoundaryDisposition.DENIED, "NO_CROSS_CONTEXT_EXCEPTION")
        if exception.revoked or not (exception.effective_at <= at < exception.expires_at):
            return BoundaryResult(BoundaryDisposition.DENIED, "CONTEXT_EXCEPTION_NOT_CURRENT")
        return BoundaryResult(
            BoundaryDisposition.DENIED, "CROSS_CONTEXT_TRANSFER_CAPABILITY_ABSENT"
        )


@dataclass(frozen=True, slots=True)
class SecurityBoundarySignal:
    """Minimized operational metadata; never authority, Evidence or governed content."""

    correlation_reference: str
    boundary_reference: str
    disposition: BoundaryDisposition
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
            raise AgentSecurityContractError("WP-006 operational signals are non-authoritative")
