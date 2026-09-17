"""Configuration model with references to secrets, never secret values."""

from collections.abc import Mapping
from dataclasses import dataclass


class ConfigurationError(ValueError):
    """Raised when configuration violates the WBS-15 safety boundary."""


@dataclass(frozen=True, slots=True)
class SecretReference:
    name: str
    reference: str


@dataclass(frozen=True, slots=True)
class FoundationSettings:
    service_name: str
    environment_name: str
    secret_references: tuple[SecretReference, ...]

    @classmethod
    def from_environment(cls, environment: Mapping[str, str]) -> FoundationSettings:
        forbidden = sorted(key for key in environment if key.startswith("NCIE_SECRET_VALUE"))
        if forbidden:
            raise ConfigurationError(
                "Literal secret configuration is prohibited; use NCIE_SECRET_REFS identifiers only"
            )

        references: list[SecretReference] = []
        raw_references = environment.get("NCIE_SECRET_REFS", "")
        for item in filter(None, (part.strip() for part in raw_references.split(","))):
            name, separator, reference = item.partition("=")
            if not separator or not name.strip() or not reference.strip():
                raise ConfigurationError(
                    "NCIE_SECRET_REFS entries must use NAME=REFERENCE without literal values"
                )
            references.append(SecretReference(name=name.strip(), reference=reference.strip()))

        return cls(
            service_name=environment.get("NCIE_SERVICE_NAME", "ncie-foundation-service"),
            environment_name=environment.get("NCIE_ENVIRONMENT", "local-development"),
            secret_references=tuple(references),
        )
