"""Four-layer, current and deny-by-default WBS-16 authorization contracts."""

from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol

from .authorization import AuthorizationBoundary, AuthorizationResult
from .observability import ObservabilitySink, OperationalEvent, SignalCategory
from .security_principals import SecurityPrincipal

type PolicyAttribute = tuple[str, str]


class AuthorizationContractError(ValueError):
    """Raised without echoing protected values when an authorization contract is invalid."""


class AuthorizationEffect(StrEnum):
    PERMIT = "PERMIT"
    DENY = "DENY"
    INDETERMINATE = "INDETERMINATE"


class AuthorizationDimension(StrEnum):
    OBJECT = "OBJECT"
    FIELD = "FIELD"
    ACTION = "ACTION"
    PURPOSE = "PURPOSE"


ALL_AUTHORIZATION_DIMENSIONS = (
    AuthorizationDimension.OBJECT,
    AuthorizationDimension.FIELD,
    AuthorizationDimension.ACTION,
    AuthorizationDimension.PURPOSE,
)

_PROTECTED_ATTRIBUTE_FRAGMENTS = (
    "credential",
    "password",
    "secret",
    "token",
    "protected_identity",
)


def _validate_reference(value: str, label: str) -> None:
    if not value.strip() or len(value) > 128 or any(ord(character) < 32 for character in value):
        raise AuthorizationContractError(f"{label} is invalid")


@dataclass(frozen=True, slots=True)
class CurrentAuthorizationRequest:
    request_reference: str
    correlation_id: str
    principal: SecurityPrincipal | None
    object_reference: str
    field_references: tuple[str, ...]
    action_reference: str
    purpose_reference: str
    classification_reference: str
    policy_version: str
    role_references: tuple[str, ...] = ()
    policy_attributes: tuple[PolicyAttribute, ...] = ()

    def __post_init__(self) -> None:
        for label, value in (
            ("Request reference", self.request_reference),
            ("Correlation ID", self.correlation_id),
            ("Object reference", self.object_reference),
            ("Action reference", self.action_reference),
            ("Purpose reference", self.purpose_reference),
            ("Classification reference", self.classification_reference),
            ("Policy version", self.policy_version),
        ):
            _validate_reference(value, label)
        for field_reference in self.field_references:
            _validate_reference(field_reference, "Field reference")
        for role_reference in self.role_references:
            _validate_reference(role_reference, "Role reference")
        for key, value in self.policy_attributes:
            _validate_reference(key, "Policy attribute name")
            _validate_reference(value, "Policy attribute value")
            if any(fragment in key.lower() for fragment in _PROTECTED_ATTRIBUTE_FRAGMENTS):
                raise AuthorizationContractError("Protected policy attribute is prohibited")


@dataclass(frozen=True, slots=True)
class CurrentAuthorizationDecision:
    request_reference: str
    policy_version: str
    effect: AuthorizationEffect
    reason_code: str
    evaluated_dimensions: tuple[AuthorizationDimension, ...]

    def __post_init__(self) -> None:
        _validate_reference(self.request_reference, "Decision request reference")
        _validate_reference(self.policy_version, "Decision policy version")
        _validate_reference(self.reason_code, "Decision reason code")
        if set(self.evaluated_dimensions) != set(ALL_AUTHORIZATION_DIMENSIONS):
            raise AuthorizationContractError(
                "Authorization decision must evaluate object, field, action and purpose"
            )
        if len(self.evaluated_dimensions) != len(ALL_AUTHORIZATION_DIMENSIONS):
            raise AuthorizationContractError("Authorization dimensions must not be duplicated")


class PolicyDecisionPoint(Protocol):
    def evaluate(self, request: CurrentAuthorizationRequest) -> CurrentAuthorizationDecision:
        """Evaluate current authorization without relying on remembered authority."""


class DenyAllPolicyDecisionPoint:
    """Reference policy with an empty grant set."""

    def evaluate(self, request: CurrentAuthorizationRequest) -> CurrentAuthorizationDecision:
        return CurrentAuthorizationDecision(
            request_reference=request.request_reference,
            policy_version=request.policy_version,
            effect=AuthorizationEffect.DENY,
            reason_code="NO_POLICY_GRANT",
            evaluated_dimensions=ALL_AUTHORIZATION_DIMENSIONS,
        )


class PolicyEnforcementPoint:
    """Enforce only a current, complete and explicit permit decision."""

    def enforce(
        self,
        request: CurrentAuthorizationRequest,
        decision: CurrentAuthorizationDecision,
    ) -> AuthorizationResult:
        if decision.request_reference != request.request_reference:
            return AuthorizationResult(allowed=False, reason="STALE_OR_MISMATCHED_DECISION")
        if decision.policy_version != request.policy_version:
            return AuthorizationResult(allowed=False, reason="STALE_OR_MISMATCHED_POLICY")
        if decision.effect is not AuthorizationEffect.PERMIT:
            return AuthorizationResult(allowed=False, reason=decision.reason_code)
        if request.principal is None:
            return AuthorizationResult(allowed=False, reason="NO_SOURCE_BOUND_PRINCIPAL")
        return AuthorizationResult(allowed=True, reason=decision.reason_code)


class SecurityDecisionSignals:
    """Emit minimized operational signals; this is not an audit or Evidence store."""

    def __init__(self, sink: ObservabilitySink) -> None:
        self._sink = sink

    def emit(
        self,
        request: CurrentAuthorizationRequest,
        decision: CurrentAuthorizationDecision,
        result: AuthorizationResult,
    ) -> None:
        principal_class = "NONE"
        if request.principal is not None:
            principal_class = request.principal.principal_class.value
        self._sink.emit_event(
            OperationalEvent(
                category=SignalCategory.SECURITY_CONDITION,
                name="security.authorization.decision",
                correlation_id=request.correlation_id,
                attributes=(
                    ("effect", decision.effect.value),
                    ("reason_code", result.reason),
                    ("principal_class", principal_class),
                    ("allowed", result.allowed),
                ),
            )
        )


class WBS15AuthorizationAdapter(AuthorizationBoundary):
    """Apply the WBS-16 deny-all model through the existing WBS-15 boundary."""

    def __init__(
        self,
        decision_point: PolicyDecisionPoint | None = None,
        *,
        signals: SecurityDecisionSignals | None = None,
    ) -> None:
        self._decision_point = decision_point or DenyAllPolicyDecisionPoint()
        self._enforcement_point = PolicyEnforcementPoint()
        self._signals = signals

    def authorize(self, *, correlation_id: str, method: str, path: str) -> AuthorizationResult:
        request = CurrentAuthorizationRequest(
            request_reference=correlation_id,
            correlation_id=correlation_id,
            principal=None,
            object_reference=path,
            field_references=(),
            action_reference=method,
            purpose_reference="NOT_SPECIFIED",
            classification_reference="NOT_CLASSIFIED",
            policy_version="wbs16-wp001-zero-grants",
        )
        try:
            decision = self._decision_point.evaluate(request)
            result = self._enforcement_point.enforce(request, decision)
        except Exception:
            decision = CurrentAuthorizationDecision(
                request_reference=request.request_reference,
                policy_version=request.policy_version,
                effect=AuthorizationEffect.INDETERMINATE,
                reason_code="POLICY_EVALUATION_ERROR",
                evaluated_dimensions=ALL_AUTHORIZATION_DIMENSIONS,
            )
            result = self._enforcement_point.enforce(request, decision)
        if self._signals is not None:
            self._signals.emit(request, decision, result)
        return result
