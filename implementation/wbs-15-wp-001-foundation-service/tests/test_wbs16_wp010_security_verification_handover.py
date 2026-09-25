"""Deterministic local-only tests for WBS-16-WP-010."""

import unittest
from dataclasses import FrozenInstanceError, replace

from ncie_foundation.security_verification_handover import (
    ALL_EMPTY_CONTROLLED_REGISTRIES,
    ALL_VERIFICATION_HANDOVER_PROTECTIONS,
    DEPENDENCY_CONFIGURATION_INVENTORY,
    DOWNSTREAM_HANDOVERS,
    HR9_DISPOSITION_REGISTRY,
    MAXIMUM_WBS16_COMPLETION_RECOMMENDATION,
    SECURITY_TEST_CLASS_REGISTRY,
    VERIFICATION_HANDOVER_DECISION_EVIDENCE,
    VERIFICATION_HANDOVER_IMPLEMENTATION_AUTHORITY,
    VERIFICATION_HANDOVER_SOURCE_RELEASE_AUTHORITY,
    WBS16_TRACEABILITY_REGISTRY,
    AuthorityParticipation,
    BidirectionalTraceabilityRegistry,
    ControlledAssignmentClass,
    DownstreamConsumer,
    EmptyControlledRegistry,
    HrDispositionState,
    NonWaivableVerificationProtection,
    SecurityTestId,
    TestState,
    TestStateClaim,
    UnassignedVerificationAuthorities,
    VerificationDisposition,
    VerificationHandoverContractError,
    VerificationStateEvaluator,
    Wbs16WorkstreamState,
)


class Wbs16Wp010SecurityVerificationHandoverTests(unittest.TestCase):
    def test_decision_and_implementation_authority_are_exact(self) -> None:
        self.assertEqual(
            VERIFICATION_HANDOVER_DECISION_EVIDENCE,
            "NCIE-WBS16-OWNER-DECISION-2026-09-25-035",
        )
        self.assertEqual(
            VERIFICATION_HANDOVER_IMPLEMENTATION_AUTHORITY,
            "NCIE-WBS16-OWNER-DECISION-2026-09-25-036",
        )
        self.assertEqual(
            VERIFICATION_HANDOVER_SOURCE_RELEASE_AUTHORITY,
            "NCIE-WBS16-OWNER-DECISION-2026-09-25-037",
        )

    def test_exact_nine_security_test_classes_are_preserved(self) -> None:
        self.assertEqual(
            tuple(item.test_id for item in SECURITY_TEST_CLASS_REGISTRY), tuple(SecurityTestId)
        )
        self.assertEqual(
            tuple(item.test_class_name for item in SECURITY_TEST_CLASS_REGISTRY),
            (
                "IAM-Bypass",
                "Privilege-Escalation",
                "Cross-Context-Leakage",
                "Sandbox-Escape",
                "Prompt-Injection",
                "DLP-Bypass",
                "Tool-Misuse",
                "Recovery-Revocation-Failure",
                "Supply-Chain-Compromise",
            ),
        )

    def test_all_security_tests_remain_controlled_ncie016_pending(self) -> None:
        for specification in SECURITY_TEST_CLASS_REGISTRY:
            self.assertTrue(specification.test_specified)
            self.assertTrue(specification.locally_implementation_tested)
            self.assertFalse(specification.controlled_ncie016_test_executed)
            self.assertFalse(specification.independently_verified)
            self.assertFalse(specification.accepted)
            self.assertIsNone(specification.acceptance_authority_reference)

    def test_five_test_states_are_distinct(self) -> None:
        self.assertEqual(len(TestState), 5)
        self.assertEqual(len({state.value for state in TestState}), 5)

    def test_security_test_registry_and_records_are_immutable(self) -> None:
        with self.assertRaises(TypeError):
            SECURITY_TEST_CLASS_REGISTRY[0] = SECURITY_TEST_CLASS_REGISTRY[1]  # type: ignore[index]
        with self.assertRaises(FrozenInstanceError):
            SECURITY_TEST_CLASS_REGISTRY[0].accepted = True  # type: ignore[misc]

    def test_false_controlled_execution_claim_is_rejected(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            replace(SECURITY_TEST_CLASS_REGISTRY[0], controlled_ncie016_test_executed=True)

    def test_false_independent_verification_claim_is_rejected(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            replace(SECURITY_TEST_CLASS_REGISTRY[0], independently_verified=True)

    def test_false_acceptance_claim_is_rejected(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            replace(SECURITY_TEST_CLASS_REGISTRY[0], accepted=True)

    def test_acceptance_authority_cannot_be_invented(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            replace(
                SECURITY_TEST_CLASS_REGISTRY[0],
                acceptance_authority_reference="synthetic-acceptor",
            )

    def test_exact_ten_controlled_registries_are_empty(self) -> None:
        self.assertEqual(len(ALL_EMPTY_CONTROLLED_REGISTRIES), 10)
        self.assertEqual(
            {registry.registry_class for registry in ALL_EMPTY_CONTROLLED_REGISTRIES},
            set(ControlledAssignmentClass),
        )
        self.assertTrue(all(registry.is_empty() for registry in ALL_EMPTY_CONTROLLED_REGISTRIES))

    def test_populated_controlled_registry_is_rejected(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            EmptyControlledRegistry(
                ControlledAssignmentClass.TEST_EXECUTOR,
                entry_references=("synthetic-executor",),
            )

    def test_all_controlled_authorities_are_unassigned(self) -> None:
        authorities = UnassignedVerificationAuthorities()
        self.assertTrue(
            all(authorities.assignment_for(item) is None for item in ControlledAssignmentClass)
        )

    def test_self_review_and_self_approval_are_rejected(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            AuthorityParticipation(
                executor_reference="same-actor",
                reviewer_reference="same-actor",
                approver_reference="same-actor",
                independently_assigned=True,
            )

    def test_unassigned_independence_is_rejected(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            AuthorityParticipation(
                executor_reference="executor",
                reviewer_reference="reviewer",
                approver_reference="approver",
                independently_assigned=False,
            )

    def test_local_state_requires_exact_local_evidence(self) -> None:
        result = VerificationStateEvaluator().evaluate(
            TestStateClaim(SecurityTestId.SEC_T1, TestState.LOCALLY_IMPLEMENTATION_TESTED),
            UnassignedVerificationAuthorities(),
        )
        self.assertEqual(result.disposition, VerificationDisposition.DENY)
        self.assertTrue(result.controlled_test_pending)

    def test_local_evidence_never_becomes_controlled_execution(self) -> None:
        result = VerificationStateEvaluator().evaluate(
            TestStateClaim(
                SecurityTestId.SEC_T1,
                TestState.LOCALLY_IMPLEMENTATION_TESTED,
                local_evidence_reference="LOCAL-WBS16-WP001-20260918-001",
            ),
            UnassignedVerificationAuthorities(),
        )
        self.assertEqual(result.disposition, VerificationDisposition.LOCAL_EVIDENCE_ONLY)
        self.assertNotIn(TestState.CONTROLLED_NCIE016_TEST_EXECUTED, result.current_states)
        self.assertFalse(result.creates_authority)
        self.assertFalse(result.creates_acceptance)

    def test_later_test_states_require_human_decision_and_remain_pending(self) -> None:
        evaluator = VerificationStateEvaluator()
        for state in (
            TestState.CONTROLLED_NCIE016_TEST_EXECUTED,
            TestState.INDEPENDENTLY_VERIFIED,
            TestState.ACCEPTED,
        ):
            result = evaluator.evaluate(
                TestStateClaim(SecurityTestId.SEC_T9, state),
                UnassignedVerificationAuthorities(),
            )
            self.assertEqual(result.disposition, VerificationDisposition.HUMAN_DECISION_REQUIRED)
            self.assertTrue(result.controlled_test_pending)
            self.assertFalse(result.creates_acceptance)

    def test_all_eighteen_non_waivable_protections_are_structural(self) -> None:
        self.assertEqual(len(ALL_VERIFICATION_HANDOVER_PROTECTIONS), 18)
        self.assertEqual(
            ALL_VERIFICATION_HANDOVER_PROTECTIONS,
            frozenset(NonWaivableVerificationProtection),
        )

    def test_complete_twenty_eight_item_hr9_disposition_registry(self) -> None:
        self.assertEqual(len(HR9_DISPOSITION_REGISTRY), 28)
        self.assertEqual(
            tuple(item.hr_id for item in HR9_DISPOSITION_REGISTRY),
            tuple(f"HR9-{number}-1" for number in range(1, 29)),
        )
        for item in HR9_DISPOSITION_REGISTRY:
            self.assertTrue(item.downstream_gate_references)
            self.assertTrue(item.interim_behavior_reference)

    def test_hr9_26_27_and_28_have_decided_states(self) -> None:
        by_id = {item.hr_id: item for item in HR9_DISPOSITION_REGISTRY}
        self.assertEqual(
            by_id["HR9-26-1"].disposition,
            HrDispositionState.RESOLVED_PROVIDER_NEUTRAL_HANDOVER,
        )
        self.assertEqual(
            by_id["HR9-27-1"].disposition,
            HrDispositionState.RESOLVED_COMPLETE_DISPOSITION,
        )
        self.assertEqual(
            by_id["HR9-28-1"].disposition,
            HrDispositionState.RESOLVED_BY_UPSTREAM_BASELINE,
        )

    def test_traceability_contains_wp001_through_wp010_exactly_once(self) -> None:
        self.assertEqual(
            tuple(item.work_package for item in WBS16_TRACEABILITY_REGISTRY.entries),
            tuple(f"WBS-16-WP-{number:03d}" for number in range(1, 11)),
        )

    def test_traceability_rows_have_all_eight_required_dimensions(self) -> None:
        for item in WBS16_TRACEABILITY_REGISTRY.entries:
            self.assertTrue(item.source_requirement_references)
            self.assertTrue(item.human_decision_references)
            self.assertTrue(item.implementation_target_references)
            self.assertTrue(item.local_test_references)
            self.assertTrue(item.local_evidence_references)
            self.assertTrue(item.deferred_authority_references)
            self.assertTrue(item.downstream_consumers)
            self.assertTrue(item.state_reference)

    def test_traceability_is_bidirectional(self) -> None:
        wp010 = WBS16_TRACEABILITY_REGISTRY.by_work_package("WBS-16-WP-010")
        self.assertIsNotNone(wp010)
        assert wp010 is not None
        requirement = wp010.source_requirement_references[0]
        target = wp010.implementation_target_references[0]
        self.assertEqual(WBS16_TRACEABILITY_REGISTRY.by_requirement(requirement), (wp010,))
        self.assertEqual(WBS16_TRACEABILITY_REGISTRY.by_implementation_target(target), (wp010,))

    def test_missing_traceability_work_package_is_rejected(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            BidirectionalTraceabilityRegistry(WBS16_TRACEABILITY_REGISTRY.entries[:-1])

    def test_traceability_records_empty_results_for_unknown_references(self) -> None:
        self.assertEqual(WBS16_TRACEABILITY_REGISTRY.by_requirement("missing-reference"), ())
        self.assertEqual(WBS16_TRACEABILITY_REGISTRY.by_implementation_target("missing-target"), ())

    def test_exact_three_downstream_handovers_preserve_boundaries(self) -> None:
        self.assertEqual(
            tuple(item.consumer for item in DOWNSTREAM_HANDOVERS),
            (
                DownstreamConsumer.WBS20,
                DownstreamConsumer.WBS23,
                DownstreamConsumer.NCIE016_WBS24,
            ),
        )
        self.assertTrue(all(not item.grants_authority for item in DOWNSTREAM_HANDOVERS))

    def test_dependency_inventory_has_no_runtime_dependency_or_external_system(self) -> None:
        self.assertEqual(DEPENDENCY_CONFIGURATION_INVENTORY.runtime_dependencies, ())
        self.assertEqual(DEPENDENCY_CONFIGURATION_INVENTORY.external_system_references, ())
        self.assertEqual(
            DEPENDENCY_CONFIGURATION_INVENTORY.development_dependencies,
            ("mypy-2.3.1", "ruff-0.16.8"),
        )

    def test_maximum_recommendation_keeps_wbs16_in_progress(self) -> None:
        recommendation = MAXIMUM_WBS16_COMPLETION_RECOMMENDATION
        self.assertEqual(recommendation.current_workstream_state, Wbs16WorkstreamState.IN_PROGRESS)
        self.assertFalse(recommendation.approved_closure)
        self.assertTrue(recommendation.independent_security_verification_pending)
        self.assertTrue(recommendation.accreditation_pending)
        self.assertTrue(recommendation.controlled_acceptance_pending)
        self.assertTrue(recommendation.go_live_pending)

    def test_completion_recommendation_cannot_claim_closure(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            replace(MAXIMUM_WBS16_COMPLETION_RECOMMENDATION, approved_closure=True)

    def test_completion_recommendation_cannot_claim_verification_complete(self) -> None:
        with self.assertRaises(VerificationHandoverContractError):
            replace(
                MAXIMUM_WBS16_COMPLETION_RECOMMENDATION,
                independent_security_verification_pending=False,
            )


if __name__ == "__main__":
    unittest.main()
