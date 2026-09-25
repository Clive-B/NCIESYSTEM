"""Provider-neutral WP-010 verification handover and closure-preparation contracts."""

from dataclasses import dataclass
from enum import StrEnum
from re import compile as compile_pattern
from typing import Final, Protocol

VERIFICATION_HANDOVER_BASELINE_VERSION: Final = "NCIE-WBS16-WP010-2026-09-25"
VERIFICATION_HANDOVER_DECISION_EVIDENCE: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-25-035"
VERIFICATION_HANDOVER_IMPLEMENTATION_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-25-036"
VERIFICATION_HANDOVER_SOURCE_RELEASE_AUTHORITY: Final = "NCIE-WBS16-OWNER-DECISION-2026-09-25-037"

_REFERENCE_PATTERN: Final = compile_pattern(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,159}")
_DENY_SENTINELS: Final = frozenset({"unassigned", "unspecified", "unknown"})


class VerificationHandoverContractError(ValueError):
    """Raised when a WP-010 metadata contract violates a controlled boundary."""


def _validate_reference(value: str, label: str) -> None:
    if _REFERENCE_PATTERN.fullmatch(value) is None or value.lower() in _DENY_SENTINELS:
        raise VerificationHandoverContractError(f"{label} is invalid")


def _validate_references(values: tuple[str, ...], label: str, *, required: bool = True) -> None:
    if required and not values:
        raise VerificationHandoverContractError(f"{label} is required")
    if len(values) != len(set(values)):
        raise VerificationHandoverContractError(f"{label} must not contain duplicates")
    for value in values:
        _validate_reference(value, label)


class SecurityTestId(StrEnum):
    SEC_T1 = "SEC-T1"
    SEC_T2 = "SEC-T2"
    SEC_T3 = "SEC-T3"
    SEC_T4 = "SEC-T4"
    SEC_T5 = "SEC-T5"
    SEC_T6 = "SEC-T6"
    SEC_T7 = "SEC-T7"
    SEC_T8 = "SEC-T8"
    SEC_T9 = "SEC-T9"


class TestState(StrEnum):
    TEST_SPECIFIED = "TEST_SPECIFIED"
    LOCALLY_IMPLEMENTATION_TESTED = "LOCALLY_IMPLEMENTATION_TESTED"
    CONTROLLED_NCIE016_TEST_EXECUTED = "CONTROLLED_NCIE016_TEST_EXECUTED"
    INDEPENDENTLY_VERIFIED = "INDEPENDENTLY_VERIFIED"
    ACCEPTED = "ACCEPTED"


class VerificationDisposition(StrEnum):
    DENY = "DENY"
    LOCAL_EVIDENCE_ONLY = "LOCAL_EVIDENCE_ONLY"
    CONTROLLED_NCIE016_TEST_PENDING = "CONTROLLED_NCIE016_TEST_PENDING"
    HUMAN_DECISION_REQUIRED = "HUMAN_DECISION_REQUIRED"


class Wbs16WorkstreamState(StrEnum):
    IN_PROGRESS = "IN_PROGRESS"
    IMPLEMENTATION_COMPLETE_DOWNSTREAM_READY_RECOMMENDATION = (
        "IMPLEMENTATION_COMPLETE_DOWNSTREAM_READY_RECOMMENDATION"
    )


class HrDispositionState(StrEnum):
    RESOLVED_IMPLEMENTED = "RESOLVED_IMPLEMENTED"
    RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED = "RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED"
    RESOLVED_DOWNSTREAM_ASSIGNED = "RESOLVED_DOWNSTREAM_ASSIGNED"
    RESOLVED_PROVIDER_NEUTRAL_HANDOVER = "RESOLVED_PROVIDER_NEUTRAL_HANDOVER"
    RESOLVED_COMPLETE_DISPOSITION = "RESOLVED_COMPLETE_DISPOSITION"
    RESOLVED_BY_UPSTREAM_BASELINE = "RESOLVED_BY_UPSTREAM_BASELINE"


class DownstreamConsumer(StrEnum):
    WBS20 = "WBS-20"
    WBS23 = "WBS-23"
    NCIE016_WBS24 = "NCIE-016-WBS-24"
    FINAL_HUMAN_CLOSURE = "FINAL-HUMAN-CLOSURE"


class ControlledAssignmentClass(StrEnum):
    TEST_EXECUTOR = "TEST_EXECUTOR"
    WITNESS = "WITNESS"
    INDEPENDENT_REVIEWER_VERIFIER = "INDEPENDENT_REVIEWER_VERIFIER"
    SECURITY_ACCREDITOR = "SECURITY_ACCREDITOR"
    ACCEPTANCE_AUTHORITY = "ACCEPTANCE_AUTHORITY"
    CONTROLLED_ENVIRONMENT = "CONTROLLED_ENVIRONMENT"
    TEST_TOOL_PRODUCT = "TEST_TOOL_PRODUCT"
    TEST_DATA_CORPUS = "TEST_DATA_CORPUS"
    TEST_THRESHOLD = "TEST_THRESHOLD"
    ACCEPTANCE_CRITERION = "ACCEPTANCE_CRITERION"


class NonWaivableVerificationProtection(StrEnum):
    HUMAN_PRIMARY_AUTHORITY = "HUMAN_PRIMARY_AUTHORITY"
    UNASSIGNED_DENY_NO_CAPABILITY = "UNASSIGNED_DENY_NO_CAPABILITY"
    FIVE_TEST_STATES_SEPARATE = "FIVE_TEST_STATES_SEPARATE"
    LOCAL_NOT_CONTROLLED_EXECUTION = "LOCAL_NOT_CONTROLLED_EXECUTION"
    EXECUTION_NOT_INDEPENDENT_VERIFICATION = "EXECUTION_NOT_INDEPENDENT_VERIFICATION"
    VERIFICATION_NOT_ACCREDITATION_ACCEPTANCE = "VERIFICATION_NOT_ACCREDITATION_ACCEPTANCE"
    ACCEPTANCE_NOT_DEPLOYMENT_GO_LIVE = "ACCEPTANCE_NOT_DEPLOYMENT_GO_LIVE"
    EXACT_NINE_TEST_CLASSES = "EXACT_NINE_TEST_CLASSES"
    NO_SELF_APPROVAL = "NO_SELF_APPROVAL"
    CONTROLLED_AUTHORITIES_UNASSIGNED = "CONTROLLED_AUTHORITIES_UNASSIGNED"
    EXACT_VERSIONED_TRACEABILITY = "EXACT_VERSIONED_TRACEABILITY"
    SILENCE_NOT_APPROVAL = "SILENCE_NOT_APPROVAL"
    DEFERRAL_OWNER_GATE_INTERIM = "DEFERRAL_OWNER_GATE_INTERIM"
    NO_PRODUCT_ENVIRONMENT_THRESHOLD_INVENTION = "NO_PRODUCT_ENVIRONMENT_THRESHOLD_INVENTION"
    NO_GOVERNED_EXTERNAL_CROSS_BORDER_DATA = "NO_GOVERNED_EXTERNAL_CROSS_BORDER_DATA"
    NO_INSTITUTIONAL_EVIDENCE_FINDING_ACCEPTANCE = "NO_INSTITUTIONAL_EVIDENCE_FINDING_ACCEPTANCE"
    DOWNSTREAM_RESPONSIBILITIES_SEGREGATED = "DOWNSTREAM_RESPONSIBILITIES_SEGREGATED"
    SEPARATE_FINAL_HUMAN_CLOSURE = "SEPARATE_FINAL_HUMAN_CLOSURE"


ALL_VERIFICATION_HANDOVER_PROTECTIONS: Final = frozenset(NonWaivableVerificationProtection)


@dataclass(frozen=True, slots=True)
class EmptyControlledRegistry:
    registry_class: ControlledAssignmentClass
    version: str = VERIFICATION_HANDOVER_BASELINE_VERSION
    entry_references: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.version, "Registry version")
        _validate_references(self.entry_references, "Registry entry reference", required=False)
        if self.entry_references:
            raise VerificationHandoverContractError(
                "WP-010 controlled assignment and prerequisite registries must be empty"
            )

    def is_empty(self) -> bool:
        return not self.entry_references


ALL_EMPTY_CONTROLLED_REGISTRIES: Final = tuple(
    EmptyControlledRegistry(registry_class) for registry_class in ControlledAssignmentClass
)


class VerificationAuthorityBoundary(Protocol):
    def assignment_for(self, assignment_class: ControlledAssignmentClass) -> str | None: ...


class UnassignedVerificationAuthorities:
    """Expose no controlled testing, verification, accreditation or acceptance authority."""

    def assignment_for(self, assignment_class: ControlledAssignmentClass) -> str | None:
        del assignment_class
        return None


@dataclass(frozen=True, slots=True)
class SecurityTestSpecification:
    test_id: SecurityTestId
    test_class_name: str
    source_requirement_references: tuple[str, ...]
    implemented_control_domains: tuple[str, ...]
    local_test_references: tuple[str, ...]
    local_evidence_references: tuple[str, ...]
    limitation_references: tuple[str, ...]
    remaining_controlled_test_reference: str
    required_independent_role_references: tuple[str, ...]
    prerequisite_references: tuple[str, ...]
    acceptance_authority_reference: str | None = None
    test_specified: bool = True
    locally_implementation_tested: bool = True
    controlled_ncie016_test_executed: bool = False
    independently_verified: bool = False
    accepted: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.test_class_name, "Test-class name")
        _validate_references(self.source_requirement_references, "Source requirement")
        _validate_references(self.implemented_control_domains, "Control domain")
        _validate_references(self.local_test_references, "Local test reference")
        _validate_references(self.local_evidence_references, "Local evidence reference")
        _validate_references(self.limitation_references, "Limitation reference")
        _validate_reference(
            self.remaining_controlled_test_reference, "Remaining controlled-test reference"
        )
        _validate_references(
            self.required_independent_role_references, "Independent-role reference"
        )
        _validate_references(self.prerequisite_references, "Prerequisite reference")
        if self.acceptance_authority_reference is not None:
            raise VerificationHandoverContractError(
                "WP-010 acceptance authority must remain unassigned"
            )
        if not self.test_specified:
            raise VerificationHandoverContractError("Every SEC-T class must remain specified")
        if self.controlled_ncie016_test_executed or self.independently_verified or self.accepted:
            raise VerificationHandoverContractError(
                "WP-010 cannot claim controlled execution, verification or acceptance"
            )

    @property
    def states(self) -> tuple[TestState, ...]:
        states = [TestState.TEST_SPECIFIED]
        if self.locally_implementation_tested:
            states.append(TestState.LOCALLY_IMPLEMENTATION_TESTED)
        return tuple(states)


def _security_test(
    test_id: SecurityTestId,
    name: str,
    sources: tuple[str, ...],
    domains: tuple[str, ...],
    tests: tuple[str, ...],
    evidence: tuple[str, ...],
    limitations: tuple[str, ...],
    remaining: str,
    roles: tuple[str, ...],
    prerequisites: tuple[str, ...],
) -> SecurityTestSpecification:
    return SecurityTestSpecification(
        test_id=test_id,
        test_class_name=name,
        source_requirement_references=sources,
        implemented_control_domains=domains,
        local_test_references=tests,
        local_evidence_references=evidence,
        limitation_references=limitations,
        remaining_controlled_test_reference=remaining,
        required_independent_role_references=roles,
        prerequisite_references=prerequisites,
    )


SECURITY_TEST_CLASS_REGISTRY: Final = (
    _security_test(
        SecurityTestId.SEC_T1,
        "IAM-Bypass",
        ("NCIE-009-Ch5", "NCIE-009-Ch6"),
        ("WP001-authorization", "WP003-identity-session", "WP004-access-control"),
        ("test-decision-four-dimensions", "test-unbound-issuer", "test-stale-mapping-deny"),
        ("LOCAL-WBS16-WP001-20260918-001", "LOCAL-WBS16-WP004-20260923-001"),
        ("no-live-iam", "no-composed-controlled-deployment"),
        "controlled-iam-bypass-confused-deputy-campaign",
        ("independent-security-executor", "independent-security-verifier"),
        ("controlled-iam-stack", "synthetic-identity-fixtures", "attack-corpus"),
    ),
    _security_test(
        SecurityTestId.SEC_T2,
        "Privilege-Escalation",
        ("NCIE-009-Ch8", "NCIE-009-Ch9"),
        ("WP004-privileged-access", "WP004-emergency-access"),
        ("test-unassigned-privilege", "test-emergency-auto-expiry", "test-revocation-current"),
        ("LOCAL-WBS16-WP004-20260923-001",),
        ("no-live-pam", "no-emergency-activation"),
        "controlled-privilege-break-glass-abuse-campaign",
        ("independent-security-executor", "independent-security-verifier", "witness"),
        ("controlled-pam-stack", "session-fixtures", "controlled-time-source"),
    ),
    _security_test(
        SecurityTestId.SEC_T3,
        "Cross-Context-Leakage",
        ("NCIE-009-Ch17",),
        ("WP006-context-isolation", "WP007-disclosure-control"),
        ("test-empty-context-deny", "test-revoked-context-exception", "test-no-retrieval"),
        ("LOCAL-WBS16-WP006-20260924-001", "LOCAL-WBS16-WP007-20260924-001"),
        ("no-context-store", "no-semantic-retrieval-runtime"),
        "controlled-cross-context-adversarial-retrieval-campaign",
        ("independent-security-executor", "independent-privacy-security-verifier"),
        ("controlled-context-store", "synthetic-retrieval-corpus", "isolation-instrumentation"),
    ),
    _security_test(
        SecurityTestId.SEC_T4,
        "Sandbox-Escape",
        ("NCIE-009-Ch14",),
        ("WP006-agent-runtime-boundary", "WP006-generated-code-quarantine"),
        ("test-missing-primitives-deny", "test-capability-flags-rejected", "test-no-network"),
        ("LOCAL-WBS16-WP006-20260924-001",),
        ("contract-boundary-only", "no-agent-runtime-sandbox"),
        "controlled-sandbox-escape-resource-persistence-campaign",
        ("independent-security-executor", "independent-security-verifier"),
        ("approved-sandbox-runtime", "isolated-host", "escape-corpus"),
    ),
    _security_test(
        SecurityTestId.SEC_T5,
        "Prompt-Injection",
        ("NCIE-009-Ch17", "NCIE-007-Ch25"),
        ("WP006-untrusted-content", "WP008-false-authority", "WP009-state-protection"),
        (
            "test-untrusted-no-authority",
            "test-injection-no-detection-change",
            "test-injection-no-state-change",
        ),
        ("LOCAL-WBS16-WP006-20260924-001", "LOCAL-WBS16-WP009-20260924-001"),
        ("no-live-agent-model", "no-controlled-injection-corpus"),
        "controlled-direct-indirect-multistage-injection-campaign",
        ("independent-adversarial-tester", "independent-security-verifier"),
        ("approved-agent-model-runtime", "controlled-injection-corpus", "tool-mocks"),
    ),
    _security_test(
        SecurityTestId.SEC_T6,
        "DLP-Bypass",
        ("NCIE-009-Ch18", "NCIE-009-Table25"),
        ("WP007-five-dlp-paths", "WP007-no-output-reveal"),
        ("test-exact-five-dlp-paths", "test-empty-dlp-deny", "test-unassigned-disclosure-deny"),
        ("LOCAL-WBS16-WP007-20260924-001",),
        ("no-live-dlp", "no-governed-data", "no-output-channel"),
        "controlled-five-path-dlp-bypass-campaign",
        ("independent-security-privacy-executor", "independent-security-privacy-verifier"),
        ("approved-dlp-paths", "minimized-synthetic-corpus", "channel-fixtures"),
    ),
    _security_test(
        SecurityTestId.SEC_T7,
        "Tool-Misuse",
        ("NCIE-009-Ch16",),
        ("WP006-tool-classification", "WP006-no-invocation-gateway"),
        ("test-empty-tool-deny", "test-tool-current-authorization", "test-eligible-tool-no-invoke"),
        ("LOCAL-WBS16-WP006-20260924-001",),
        ("zero-tools", "no-connector-runtime", "no-external-system"),
        "controlled-tool-confused-deputy-target-drift-campaign",
        ("independent-security-executor", "independent-security-verifier"),
        ("approved-tool-sandbox", "connector-mocks", "synthetic-targets"),
    ),
    _security_test(
        SecurityTestId.SEC_T8,
        "Recovery-Revocation-Failure",
        ("NCIE-009-Ch10", "NCIE-009-Ch22", "NCIE-009-Ch25"),
        ("WP003-revocation", "WP008-recovery-handoff", "WP009-reconciliation"),
        (
            "test-recovery-invalidates-sessions",
            "test-recovery-cannot-authorize",
            "test-no-stale-restoration",
        ),
        ("LOCAL-WBS16-WP003-20260919-001", "LOCAL-WBS16-WP009-20260924-001"),
        ("no-live-recovery", "no-credential-rotation", "no-backup-platform"),
        "controlled-revocation-restore-reconciliation-campaign",
        ("independent-recovery-executor", "independent-recovery-security-verifier", "witness"),
        ("approved-recovery-platform", "known-good-fixtures", "isolated-recovery-environment"),
    ),
    _security_test(
        SecurityTestId.SEC_T9,
        "Supply-Chain-Compromise",
        ("NCIE-009-Ch23",),
        ("WP006-generated-code-quarantine", "WP009-artifact-provenance-quarantine"),
        (
            "test-unverified-artifact-quarantine",
            "test-version-substitution-quarantine",
            "test-no-self-review",
        ),
        ("LOCAL-WBS16-WP006-20260924-001", "LOCAL-WBS16-WP009-20260924-001"),
        ("no-repository", "no-ci-cd", "no-scanner-signing-sbom"),
        "controlled-tamper-provenance-build-compromise-campaign",
        ("independent-supply-chain-tester", "independent-supply-chain-verifier"),
        ("approved-repository-ci-cd", "test-artifacts", "isolated-promotion-target"),
    ),
)


@dataclass(frozen=True, slots=True)
class AuthorityParticipation:
    executor_reference: str
    reviewer_reference: str
    approver_reference: str
    independently_assigned: bool

    def __post_init__(self) -> None:
        for value, label in (
            (self.executor_reference, "Executor reference"),
            (self.reviewer_reference, "Reviewer reference"),
            (self.approver_reference, "Approver reference"),
        ):
            _validate_reference(value, label)
        if (
            len({self.executor_reference, self.reviewer_reference, self.approver_reference}) != 3
            or not self.independently_assigned
        ):
            raise VerificationHandoverContractError(
                "Controlled executor, reviewer and approver must be independently assigned"
            )


@dataclass(frozen=True, slots=True)
class TestStateClaim:
    test_id: SecurityTestId
    requested_state: TestState
    local_evidence_reference: str | None = None
    controlled_result_reference: str | None = None

    def __post_init__(self) -> None:
        if self.local_evidence_reference is not None:
            _validate_reference(self.local_evidence_reference, "Local evidence reference")
        if self.controlled_result_reference is not None:
            _validate_reference(self.controlled_result_reference, "Controlled result reference")


@dataclass(frozen=True, slots=True)
class VerificationEvaluation:
    disposition: VerificationDisposition
    current_states: tuple[TestState, ...]
    controlled_test_pending: bool
    creates_authority: bool = False
    creates_acceptance: bool = False


class VerificationStateEvaluator:
    """Allow local evidence labels only; all later states fail closed in WP-010."""

    def evaluate(
        self,
        claim: TestStateClaim,
        authorities: VerificationAuthorityBoundary,
    ) -> VerificationEvaluation:
        specification = next(
            item for item in SECURITY_TEST_CLASS_REGISTRY if item.test_id is claim.test_id
        )
        if claim.requested_state is TestState.TEST_SPECIFIED:
            return VerificationEvaluation(
                VerificationDisposition.CONTROLLED_NCIE016_TEST_PENDING,
                (TestState.TEST_SPECIFIED,),
                True,
            )
        if claim.requested_state is TestState.LOCALLY_IMPLEMENTATION_TESTED:
            if claim.local_evidence_reference is None:
                return VerificationEvaluation(VerificationDisposition.DENY, (), True)
            return VerificationEvaluation(
                VerificationDisposition.LOCAL_EVIDENCE_ONLY,
                specification.states,
                True,
            )
        required = (
            ControlledAssignmentClass.TEST_EXECUTOR,
            ControlledAssignmentClass.INDEPENDENT_REVIEWER_VERIFIER,
            ControlledAssignmentClass.ACCEPTANCE_AUTHORITY,
        )
        if any(authorities.assignment_for(role) is None for role in required):
            return VerificationEvaluation(
                VerificationDisposition.HUMAN_DECISION_REQUIRED,
                specification.states,
                True,
            )
        return VerificationEvaluation(VerificationDisposition.DENY, specification.states, True)


@dataclass(frozen=True, slots=True)
class Hr9DispositionRecord:
    hr_id: str
    source_classification: str
    disposition: HrDispositionState
    decision_reference: str
    downstream_gate_references: tuple[str, ...]
    interim_behavior_reference: str

    def __post_init__(self) -> None:
        for value, label in (
            (self.hr_id, "HR9 identifier"),
            (self.source_classification, "Source classification"),
            (self.decision_reference, "Decision reference"),
            (self.interim_behavior_reference, "Interim behavior reference"),
        ):
            _validate_reference(value, label)
        _validate_references(self.downstream_gate_references, "Downstream gate")


def _hr(
    number: int,
    disposition: HrDispositionState,
    decision: str,
    gates: tuple[str, ...],
    interim: str,
    *,
    blocking: bool = True,
) -> Hr9DispositionRecord:
    return Hr9DispositionRecord(
        f"HR9-{number}-1",
        "Blocking" if blocking else "Non-Blocking",
        disposition,
        decision,
        gates,
        interim,
    )


HR9_DISPOSITION_REGISTRY: Final = (
    _hr(
        1,
        HrDispositionState.RESOLVED_IMPLEMENTED,
        "W16-D5-A",
        ("independent-human-review", "final-human-closure"),
        "no-closure-without-review",
    ),
    _hr(
        2,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D6-A",
        ("production-risk-authority",),
        "no-silent-risk-acceptance",
    ),
    _hr(
        3,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D7-A",
        ("institutional-iam-owner", "WBS-23"),
        "unbound-source-deny",
    ),
    _hr(
        4,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D8-A",
        ("enrollment-proofing-authority",),
        "no-proofing-enrollment",
    ),
    _hr(
        5,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D9-A",
        ("iam-security-owner",),
        "unspecified-assurance-deny",
    ),
    _hr(
        6,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D11-A",
        ("authorization-owner",),
        "empty-mapping-zero-grants",
    ),
    _hr(
        7,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D12-A",
        ("delegation-authority",),
        "no-active-delegation",
    ),
    _hr(
        8,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D13-A",
        ("privileged-access-authority", "WBS-23"),
        "no-privilege-elevation",
    ),
    _hr(
        9,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D14-A",
        ("emergency-authority",),
        "no-break-glass-activation",
    ),
    _hr(
        10,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D10-A",
        ("session-credential-owner",),
        "no-live-session-credential",
    ),
    _hr(
        11,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D15-A",
        ("secrets-key-authority", "WBS-23"),
        "no-secret-key-operation",
    ),
    _hr(
        12,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D16-A",
        ("cryptographic-policy-authority", "WBS-23"),
        "empty-crypto-policy-deny",
        blocking=False,
    ),
    _hr(
        13,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D17-A",
        ("network-security-authority", "WBS-23"),
        "no-route-egress-transfer",
    ),
    _hr(
        14,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D18-A",
        ("agent-security-owner", "WBS-23"),
        "zero-agent-generated-code-quarantine",
    ),
    _hr(
        15,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D19-A",
        ("provider-model-authority", "WBS-23"),
        "empty-route-cross-border-deny",
    ),
    _hr(
        16,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D20-A",
        ("tool-connector-authority", "WBS-23"),
        "zero-tool-invocation",
    ),
    _hr(
        17,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D21-A",
        ("context-memory-authority",),
        "zero-context-transfer",
    ),
    _hr(
        18,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D22-A",
        ("privacy-security-authority", "WBS-23"),
        "no-disclosure-output",
    ),
    _hr(
        19,
        HrDispositionState.RESOLVED_IMPLEMENTED_OPERATIONAL_DEFERRED,
        "W16-D23-A",
        ("protected-identity-authority",),
        "no-protected-reveal",
    ),
    _hr(
        20,
        HrDispositionState.RESOLVED_DOWNSTREAM_ASSIGNED,
        "W16-D24-A",
        ("WBS-20", "WBS-23"),
        "no-persistent-log-audit-store",
        blocking=False,
    ),
    _hr(
        21,
        HrDispositionState.RESOLVED_DOWNSTREAM_ASSIGNED,
        "W16-D25-A",
        ("WBS-23",),
        "no-monitor-alert-page",
        blocking=False,
    ),
    _hr(
        22,
        HrDispositionState.RESOLVED_DOWNSTREAM_ASSIGNED,
        "W16-D26-A",
        ("WBS-23",),
        "no-incident-command-containment",
    ),
    _hr(
        23,
        HrDispositionState.RESOLVED_DOWNSTREAM_ASSIGNED,
        "W16-D27-A",
        ("WBS-23", "NCIE-016-WBS-24"),
        "artifact-quarantine-no-action",
    ),
    _hr(
        24,
        HrDispositionState.RESOLVED_DOWNSTREAM_ASSIGNED,
        "W16-D28-A",
        ("WBS-23", "NCIE-016-WBS-24"),
        "no-remediation-risk-acceptance",
    ),
    _hr(
        25,
        HrDispositionState.RESOLVED_DOWNSTREAM_ASSIGNED,
        "W16-D29-A",
        ("WBS-23", "NCIE-016-WBS-24"),
        "no-recovery-restoration",
    ),
    _hr(
        26,
        HrDispositionState.RESOLVED_PROVIDER_NEUTRAL_HANDOVER,
        "W16-D30-A",
        ("NCIE-016-WBS-24",),
        "controlled-tests-pending",
    ),
    _hr(
        27,
        HrDispositionState.RESOLVED_COMPLETE_DISPOSITION,
        "W16-D31-A",
        ("WP-010-report", "final-human-closure"),
        "implementation-and-closure-pending",
    ),
    _hr(
        28,
        HrDispositionState.RESOLVED_BY_UPSTREAM_BASELINE,
        "W16-D33-A",
        ("material-change-review",),
        "stop-if-baseline-invalidated",
        blocking=False,
    ),
)


@dataclass(frozen=True, slots=True)
class WorkPackageTraceabilityRecord:
    work_package: str
    source_requirement_references: tuple[str, ...]
    human_decision_references: tuple[str, ...]
    implementation_target_references: tuple[str, ...]
    local_test_references: tuple[str, ...]
    local_evidence_references: tuple[str, ...]
    deferred_authority_references: tuple[str, ...]
    downstream_consumers: tuple[DownstreamConsumer, ...]
    state_reference: str

    def __post_init__(self) -> None:
        _validate_reference(self.work_package, "Work package")
        _validate_references(self.source_requirement_references, "Source requirement")
        _validate_references(self.human_decision_references, "Human decision")
        _validate_references(self.implementation_target_references, "Implementation target")
        _validate_references(self.local_test_references, "Local test")
        _validate_references(self.local_evidence_references, "Local evidence")
        _validate_references(self.deferred_authority_references, "Deferred authority")
        if not self.downstream_consumers:
            raise VerificationHandoverContractError("Downstream consumer is required")
        _validate_reference(self.state_reference, "State reference")


class BidirectionalTraceabilityRegistry:
    def __init__(self, entries: tuple[WorkPackageTraceabilityRecord, ...]) -> None:
        packages = tuple(entry.work_package for entry in entries)
        if packages != tuple(f"WBS-16-WP-{number:03d}" for number in range(1, 11)):
            raise VerificationHandoverContractError(
                "Traceability must contain WP-001 through WP-010 exactly once and in order"
            )
        self._entries = entries

    @property
    def entries(self) -> tuple[WorkPackageTraceabilityRecord, ...]:
        return self._entries

    def by_work_package(self, work_package: str) -> WorkPackageTraceabilityRecord | None:
        return next((entry for entry in self._entries if entry.work_package == work_package), None)

    def by_requirement(
        self, requirement_reference: str
    ) -> tuple[WorkPackageTraceabilityRecord, ...]:
        return tuple(
            entry
            for entry in self._entries
            if requirement_reference in entry.source_requirement_references
        )

    def by_implementation_target(
        self, implementation_target_reference: str
    ) -> tuple[WorkPackageTraceabilityRecord, ...]:
        return tuple(
            entry
            for entry in self._entries
            if implementation_target_reference in entry.implementation_target_references
        )


_WP_DECISIONS: Final = (
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-18-008",
        "NCIE-WBS16-OWNER-DECISION-2026-09-18-009",
        "NCIE-WBS16-OWNER-DECISION-2026-09-18-010",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-19-011",
        "NCIE-WBS16-OWNER-DECISION-2026-09-19-012",
        "NCIE-WBS16-OWNER-DECISION-2026-09-19-013",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-19-014",
        "NCIE-WBS16-OWNER-DECISION-2026-09-19-015",
        "NCIE-WBS16-OWNER-DECISION-2026-09-19-016",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-23-017",
        "NCIE-WBS16-OWNER-DECISION-2026-09-23-018",
        "NCIE-WBS16-OWNER-DECISION-2026-09-23-019",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-23-020",
        "NCIE-WBS16-OWNER-DECISION-2026-09-23-021",
        "NCIE-WBS16-OWNER-DECISION-2026-09-23-022",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-023",
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-024",
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-025",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-026",
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-027",
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-028",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-029",
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-030",
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-031",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-032",
        "NCIE-WBS16-OWNER-DECISION-2026-09-24-033",
        "NCIE-WBS16-OWNER-DECISION-2026-09-25-034",
    ),
    (
        "NCIE-WBS16-OWNER-DECISION-2026-09-25-035",
        "NCIE-WBS16-OWNER-DECISION-2026-09-25-036",
        "NCIE-WBS16-OWNER-DECISION-2026-09-25-037",
    ),
)
_WP_EVIDENCE: Final = (
    "LOCAL-WBS16-WP001-20260918-001",
    "LOCAL-WBS16-WP002-20260919-001",
    "LOCAL-WBS16-WP003-20260919-001",
    "LOCAL-WBS16-WP004-20260923-001",
    "LOCAL-WBS16-WP005-20260923-001",
    "LOCAL-WBS16-WP006-20260924-001",
    "LOCAL-WBS16-WP007-20260924-001",
    "LOCAL-WBS16-WP008-20260924-001",
    "LOCAL-WBS16-WP009-20260924-001",
    "LOCAL-WBS16-WP010-20260925-001",
)


def _wp_trace(number: int) -> WorkPackageTraceabilityRecord:
    architecture, implementation, release = _WP_DECISIONS[number - 1]
    consumers: tuple[DownstreamConsumer, ...] = (
        (DownstreamConsumer.WBS20, DownstreamConsumer.WBS23, DownstreamConsumer.NCIE016_WBS24)
        if number >= 8
        else (DownstreamConsumer.WBS23, DownstreamConsumer.NCIE016_WBS24)
    )
    if number == 10:
        consumers = (
            DownstreamConsumer.WBS20,
            DownstreamConsumer.WBS23,
            DownstreamConsumer.NCIE016_WBS24,
            DownstreamConsumer.FINAL_HUMAN_CLOSURE,
        )
    return WorkPackageTraceabilityRecord(
        work_package=f"WBS-16-WP-{number:03d}",
        source_requirement_references=(f"NCIE-009-WP{number:03d}-scope",),
        human_decision_references=(architecture, implementation, release),
        implementation_target_references=(f"ncie-foundation-wp{number:03d}",),
        local_test_references=(f"test-wbs16-wp{number:03d}",),
        local_evidence_references=(_WP_EVIDENCE[number - 1],),
        deferred_authority_references=(f"wp{number:03d}-operational-authorities",),
        downstream_consumers=consumers,
        state_reference=(
            "work-complete-controlled-source-released"
            if number < 10
            else "local-implementation-evidence-pending-final-human-closure"
        ),
    )


WBS16_TRACEABILITY_REGISTRY: Final = BidirectionalTraceabilityRegistry(
    tuple(_wp_trace(number) for number in range(1, 11))
)


@dataclass(frozen=True, slots=True)
class DownstreamHandover:
    consumer: DownstreamConsumer
    responsibility_references: tuple[str, ...]
    prohibited_wp010_claim_references: tuple[str, ...]
    grants_authority: bool = False

    def __post_init__(self) -> None:
        _validate_references(self.responsibility_references, "Handover responsibility")
        _validate_references(self.prohibited_wp010_claim_references, "Prohibited WP-010 claim")
        if self.grants_authority:
            raise VerificationHandoverContractError("A WP-010 handover cannot grant authority")


DOWNSTREAM_HANDOVERS: Final = (
    DownstreamHandover(
        DownstreamConsumer.WBS20,
        (
            "institutional-evidence",
            "canonical-provenance-audit",
            "custody-retention-legal-hold",
            "defensibility",
        ),
        ("no-institutional-evidence", "no-finding", "no-custody-claim"),
    ),
    DownstreamHandover(
        DownstreamConsumer.WBS23,
        (
            "infrastructure-products-providers",
            "operational-security-controls",
            "ci-cd-scanners-deployment",
            "monitoring-incident-recovery",
        ),
        ("no-infrastructure-activation", "no-deployment", "no-operational-runbook-execution"),
    ),
    DownstreamHandover(
        DownstreamConsumer.NCIE016_WBS24,
        (
            "controlled-test-design",
            "adversarial-execution",
            "environment-tool-data-governance",
            "verification-evidence-acceptance",
        ),
        (
            "no-controlled-execution-claim",
            "no-independent-verification-claim",
            "no-acceptance-claim",
        ),
    ),
)


@dataclass(frozen=True, slots=True)
class DependencyConfigurationInventory:
    python_reference: str
    runtime_dependencies: tuple[str, ...]
    development_dependencies: tuple[str, ...]
    environment_reference: str
    external_system_references: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _validate_reference(self.python_reference, "Python reference")
        _validate_references(self.runtime_dependencies, "Runtime dependency", required=False)
        _validate_references(self.development_dependencies, "Development dependency")
        _validate_reference(self.environment_reference, "Environment reference")
        _validate_references(self.external_system_references, "External system", required=False)
        if self.runtime_dependencies or self.external_system_references:
            raise VerificationHandoverContractError(
                "WP-010 permits no runtime dependency or external system"
            )


DEPENDENCY_CONFIGURATION_INVENTORY: Final = DependencyConfigurationInventory(
    python_reference="python-3.14",
    runtime_dependencies=(),
    development_dependencies=("mypy-2.3.1", "ruff-0.16.8"),
    environment_reference="local-controlled-non-production",
)


@dataclass(frozen=True, slots=True)
class CompletionRecommendation:
    recommendation_reference: str
    current_workstream_state: Wbs16WorkstreamState
    independent_security_verification_pending: bool
    accreditation_pending: bool
    controlled_acceptance_pending: bool
    go_live_pending: bool
    approved_closure: bool = False

    def __post_init__(self) -> None:
        _validate_reference(self.recommendation_reference, "Recommendation reference")
        if self.current_workstream_state is not Wbs16WorkstreamState.IN_PROGRESS:
            raise VerificationHandoverContractError("WBS-16 must remain IN_PROGRESS")
        if self.approved_closure or not all(
            (
                self.independent_security_verification_pending,
                self.accreditation_pending,
                self.controlled_acceptance_pending,
                self.go_live_pending,
            )
        ):
            raise VerificationHandoverContractError(
                "WP-010 may produce only the bounded pending closure recommendation"
            )


MAXIMUM_WBS16_COMPLETION_RECOMMENDATION: Final = CompletionRecommendation(
    recommendation_reference="wbs16-implementation-complete-downstream-ready-recommendation",
    current_workstream_state=Wbs16WorkstreamState.IN_PROGRESS,
    independent_security_verification_pending=True,
    accreditation_pending=True,
    controlled_acceptance_pending=True,
    go_live_pending=True,
)
