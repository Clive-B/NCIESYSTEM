"""Provider-neutral WBS-16 security principal and source contracts."""

from dataclasses import dataclass
from enum import StrEnum
from typing import Final, Protocol


class PrincipalClass(StrEnum):
    HUMAN = "HUMAN"
    WORKLOAD = "WORKLOAD"
    AGENT = "AGENT"
    SERVICE = "SERVICE"
    SESSION_DEVICE = "SESSION_DEVICE"
    PRIVILEGED = "PRIVILEGED"
    VALIDATOR = "VALIDATOR"


class AuthoritativeSourceCategory(StrEnum):
    INSTITUTIONAL_IDENTITY_SOURCE = "INSTITUTIONAL_IDENTITY_SOURCE"
    DEPLOYMENT_ORCHESTRATION_PLATFORM = "DEPLOYMENT_ORCHESTRATION_PLATFORM"
    AGENT_FACTORY_REGISTRY = "AGENT_FACTORY_REGISTRY"
    SERVICE_REGISTRATION = "SERVICE_REGISTRATION"
    AUTHENTICATION_SESSION_ISSUER = "AUTHENTICATION_SESSION_ISSUER"
    PRIVILEGED_ACCESS_MANAGEMENT = "PRIVILEGED_ACCESS_MANAGEMENT"
    VPF_VALIDATOR_REGISTRATION = "VPF_VALIDATOR_REGISTRATION"


_EXPECTED_SOURCE: Final[dict[PrincipalClass, AuthoritativeSourceCategory]] = {
    PrincipalClass.HUMAN: AuthoritativeSourceCategory.INSTITUTIONAL_IDENTITY_SOURCE,
    PrincipalClass.WORKLOAD: AuthoritativeSourceCategory.DEPLOYMENT_ORCHESTRATION_PLATFORM,
    PrincipalClass.AGENT: AuthoritativeSourceCategory.AGENT_FACTORY_REGISTRY,
    PrincipalClass.SERVICE: AuthoritativeSourceCategory.SERVICE_REGISTRATION,
    PrincipalClass.SESSION_DEVICE: AuthoritativeSourceCategory.AUTHENTICATION_SESSION_ISSUER,
    PrincipalClass.PRIVILEGED: AuthoritativeSourceCategory.PRIVILEGED_ACCESS_MANAGEMENT,
    PrincipalClass.VALIDATOR: AuthoritativeSourceCategory.VPF_VALIDATOR_REGISTRATION,
}


class PrincipalContractError(ValueError):
    """Raised without echoing protected values when a principal contract is invalid."""


def authoritative_source_for(principal_class: PrincipalClass) -> AuthoritativeSourceCategory:
    return _EXPECTED_SOURCE[principal_class]


def _validate_opaque_reference(value: str) -> None:
    if not value.strip() or len(value) > 128 or any(ord(character) < 32 for character in value):
        raise PrincipalContractError("Opaque principal reference is invalid")


@dataclass(frozen=True, slots=True)
class SecurityPrincipal:
    principal_class: PrincipalClass
    source_category: AuthoritativeSourceCategory
    opaque_subject_reference: str

    def __post_init__(self) -> None:
        _validate_opaque_reference(self.opaque_subject_reference)
        if self.source_category is not authoritative_source_for(self.principal_class):
            raise PrincipalContractError(
                "Principal class does not match its authoritative source category"
            )


class IdentitySourceBoundary(Protocol):
    """Provider-neutral identity source; resolution does not grant authorization."""

    def resolve(
        self,
        *,
        principal_class: PrincipalClass,
        source_category: AuthoritativeSourceCategory,
        opaque_subject_reference: str,
    ) -> SecurityPrincipal | None:
        """Return a source-bound principal or fail closed with no principal."""


class UnboundIdentitySource:
    """Fail closed while all provider and registry bindings remain deferred."""

    def resolve(
        self,
        *,
        principal_class: PrincipalClass,
        source_category: AuthoritativeSourceCategory,
        opaque_subject_reference: str,
    ) -> SecurityPrincipal | None:
        del principal_class, source_category, opaque_subject_reference
        return None
