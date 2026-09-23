import unittest
from datetime import UTC, datetime, timedelta

from ncie_foundation.access_control import (
    ACCESS_CONTROL_BASELINE_VERSION,
    ACCESS_CONTROL_DECISION_EVIDENCE,
    ACCESS_CONTROL_IMPLEMENTATION_AUTHORITY,
    APPROVED_DELEGATION_CLASS_RULES,
    APPROVED_PRIVILEGE_INTERFACES,
    EMPTY_INSTITUTIONAL_MAPPING_REGISTRY,
    AccessControlContractError,
    AccessControlSignals,
    ApprovalInterface,
    AuthorizationMapping,
    AuthorizationMappingRegistry,
    DelegationClass,
    DelegationEnvelope,
    DelegationEvaluator,
    DelegationValidationCode,
    EmergencyAccessEvaluator,
    EmergencyAccessRequest,
    EmergencyAction,
    EmergencyClass,
    EmergencyDeclaration,
    EmergencyEligibilityDecision,
    EmergencyNotificationObligation,
    EmergencyPostEventReview,
    EmergencyTriggerClass,
    EmergencyValidationCode,
    MappingSubjectKind,
    PostEventDisposition,
    PrivilegeClass,
    PrivilegedAccessEvaluator,
    PrivilegedAccessRequest,
    PrivilegedApprovalDecision,
    PrivilegeValidationCode,
    UnassignedEmergencyEligibility,
    UnassignedPrivilegedApprovalAuthority,
    VersionedMappingPolicyDecisionPoint,
)
from ncie_foundation.identity_assurance import AssuranceState
from ncie_foundation.observability import InMemoryObservabilitySink, SignalCategory
from ncie_foundation.security_authorization import (
    AuthorizationEffect,
    CurrentAuthorizationRequest,
    PolicyEnforcementPoint,
)
from ncie_foundation.security_principals import (
    PrincipalClass,
    SecurityPrincipal,
    authoritative_source_for,
)


class FixedPrivilegeAuthority:
    def __init__(self, decision: PrivilegedApprovalDecision | None) -> None:
        self._decision = decision

    def decide(self, request: PrivilegedAccessRequest) -> PrivilegedApprovalDecision | None:
        del request
        return self._decision


class FixedEmergencyEligibility:
    def __init__(self, decision: EmergencyEligibilityDecision | None) -> None:
        self._decision = decision

    def resolve(
        self, declaration: EmergencyDeclaration, operator: SecurityPrincipal
    ) -> EmergencyEligibilityDecision | None:
        del declaration, operator
        return self._decision


class AccessControlTests(unittest.TestCase):
    now = datetime(2026, 9, 23, 12, 0, tzinfo=UTC)

    @staticmethod
    def principal(principal_class: PrincipalClass, reference: str) -> SecurityPrincipal:
        return SecurityPrincipal(
            principal_class=principal_class,
            source_category=authoritative_source_for(principal_class),
            opaque_subject_reference=reference,
        )

    @classmethod
    def authorization_request(
        cls,
        *,
        roles: tuple[str, ...] = ("synthetic-role",),
        attributes: tuple[tuple[str, str], ...] = (),
        policy_version: str = "synthetic-policy-v1",
    ) -> CurrentAuthorizationRequest:
        return CurrentAuthorizationRequest(
            request_reference="synthetic-authorization-request",
            correlation_id="synthetic-correlation",
            principal=cls.principal(PrincipalClass.HUMAN, "synthetic-human"),
            object_reference="synthetic-object",
            field_references=("synthetic-field",),
            action_reference="synthetic-action",
            purpose_reference="synthetic-purpose",
            classification_reference="SYNTHETIC",
            policy_version=policy_version,
            role_references=roles,
            policy_attributes=attributes,
        )

    @classmethod
    def mapping(
        cls,
        *,
        mapping_reference: str = "synthetic-mapping",
        revoked_at: datetime | None = None,
        expires_at: datetime | None = None,
    ) -> AuthorizationMapping:
        return AuthorizationMapping(
            mapping_reference=mapping_reference,
            subject_kind=MappingSubjectKind.ROLE,
            subject_reference="synthetic-role",
            object_reference="synthetic-object",
            field_references=("synthetic-field",),
            action_reference="synthetic-action",
            purpose_reference="synthetic-purpose",
            classification_reference="SYNTHETIC",
            required_policy_attributes=(),
            policy_version="synthetic-policy-v1",
            effective_from=cls.now - timedelta(minutes=1),
            expires_at=expires_at or cls.now + timedelta(minutes=30),
            approval_decision_reference="synthetic-decision",
            revoked_at=revoked_at,
        )

    @classmethod
    def privilege_request(
        cls,
        privilege_class: PrivilegeClass = PrivilegeClass.INFRASTRUCTURE_CONFIGURATION_ADMIN,
    ) -> PrivilegedAccessRequest:
        return PrivilegedAccessRequest(
            request_reference="synthetic-privilege-request",
            requester=cls.principal(PrincipalClass.HUMAN, "synthetic-requester"),
            privilege_class=privilege_class,
            target_reference="synthetic-target",
            action_references=("synthetic-admin-action",),
            justification_reference="synthetic-justification",
            policy_version="synthetic-policy-v1",
            requested_at=cls.now - timedelta(minutes=1),
            expires_at=cls.now + timedelta(minutes=30),
            duration_policy_reference="synthetic-duration-policy",
            step_up_evidence_reference="synthetic-step-up",
            assurance_state=AssuranceState.ELEVATED,
            content_justification_reference=(
                "synthetic-content-justification"
                if privilege_class is PrivilegeClass.DATA_CONTENT_ADMIN
                else None
            ),
        )

    @classmethod
    def privilege_decision(
        cls,
        request: PrivilegedAccessRequest,
        *,
        approver: SecurityPrincipal | None = None,
        expires_at: datetime | None = None,
        revoked_at: datetime | None = None,
    ) -> PrivilegedApprovalDecision:
        return PrivilegedApprovalDecision(
            decision_reference="synthetic-privilege-decision",
            request_reference=request.request_reference,
            approver=approver
            or cls.principal(PrincipalClass.HUMAN, "synthetic-independent-approver"),
            authority_assignment_reference="synthetic-authority-assignment",
            privilege_class=request.privilege_class,
            target_reference=request.target_reference,
            action_references=request.action_references,
            policy_version=request.policy_version,
            approved=True,
            decided_at=cls.now - timedelta(seconds=30),
            expires_at=expires_at or request.expires_at,
            revoked_at=revoked_at,
            acceptance_decision_reference=(
                "synthetic-acceptance-decision"
                if request.privilege_class is PrivilegeClass.DATA_CONTENT_ADMIN
                else None
            ),
        )

    @classmethod
    def declaration(
        cls,
        emergency_class: EmergencyClass = EmergencyClass.IDENTITY_ACCESS_SUSPENSION,
        *,
        revoked_at: datetime | None = None,
    ) -> EmergencyDeclaration:
        trigger = (
            EmergencyTriggerClass.DECLARED_OPERATIONAL_EMERGENCY
            if emergency_class is EmergencyClass.INFRASTRUCTURE_BREAK_GLASS_ADMIN
            else EmergencyTriggerClass.DECLARED_SECURITY_EMERGENCY
        )
        return EmergencyDeclaration(
            declaration_reference="synthetic-emergency-declaration",
            emergency_class=emergency_class,
            trigger_class=trigger,
            declared_by=cls.principal(PrincipalClass.HUMAN, "synthetic-declaring-authority"),
            target_reference="synthetic-emergency-target",
            purpose_reference="synthetic-containment-purpose",
            decision_reference="synthetic-emergency-decision",
            declared_at=cls.now - timedelta(minutes=1),
            expires_at=cls.now + timedelta(minutes=20),
            duration_policy_reference="synthetic-duration-policy",
            policy_version="synthetic-policy-v1",
            revoked_at=revoked_at,
        )

    @classmethod
    def emergency_request(
        cls,
        declaration: EmergencyDeclaration,
        operator: SecurityPrincipal,
        *,
        action: EmergencyAction = EmergencyAction.CONTAIN,
    ) -> EmergencyAccessRequest:
        return EmergencyAccessRequest(
            request_reference="synthetic-emergency-request",
            declaration=declaration,
            operator=operator,
            action=action,
            requested_at=cls.now - timedelta(seconds=30),
            expires_at=cls.now + timedelta(minutes=10),
            step_up_evidence_reference="synthetic-emergency-step-up",
            assurance_state=AssuranceState.ELEVATED,
        )

    def test_authority_and_decision_evidence_are_exact(self) -> None:
        self.assertEqual(ACCESS_CONTROL_BASELINE_VERSION, "NCIE-WBS16-WP004-2026-09-23")
        self.assertTrue(ACCESS_CONTROL_DECISION_EVIDENCE.endswith("-017"))
        self.assertTrue(ACCESS_CONTROL_IMPLEMENTATION_AUTHORITY.endswith("-018"))

    def test_controlled_mapping_registry_is_empty_and_denies_through_wp001_boundary(self) -> None:
        self.assertTrue(EMPTY_INSTITUTIONAL_MAPPING_REGISTRY.is_empty())
        request = self.authorization_request()
        decision = VersionedMappingPolicyDecisionPoint(clock=lambda: self.now).evaluate(request)
        result = PolicyEnforcementPoint().enforce(request, decision)
        self.assertEqual(decision.effect, AuthorizationEffect.DENY)
        self.assertEqual(decision.reason_code, "NO_CURRENT_MAPPING_GRANT")
        self.assertFalse(result.allowed)

    def test_current_exact_synthetic_mapping_can_exercise_contract_only(self) -> None:
        request = self.authorization_request()
        decision = VersionedMappingPolicyDecisionPoint(
            AuthorizationMappingRegistry((self.mapping(),)),
            clock=lambda: self.now,
        ).evaluate(request)
        self.assertEqual(decision.effect, AuthorizationEffect.PERMIT)
        self.assertTrue(PolicyEnforcementPoint().enforce(request, decision).allowed)

    def test_stale_revoked_mismatched_and_ambiguous_mapping_fail_closed(self) -> None:
        request = self.authorization_request()
        cases = (
            (
                AuthorizationMappingRegistry(
                    (self.mapping(expires_at=self.now - timedelta(seconds=1)),)
                ),
                request,
                AuthorizationEffect.DENY,
            ),
            (
                AuthorizationMappingRegistry(
                    (self.mapping(revoked_at=self.now - timedelta(seconds=1)),)
                ),
                request,
                AuthorizationEffect.DENY,
            ),
            (
                AuthorizationMappingRegistry((self.mapping(),)),
                self.authorization_request(policy_version="different-policy"),
                AuthorizationEffect.DENY,
            ),
            (
                AuthorizationMappingRegistry(
                    (
                        self.mapping(mapping_reference="synthetic-mapping-one"),
                        self.mapping(mapping_reference="synthetic-mapping-two"),
                    )
                ),
                request,
                AuthorizationEffect.INDETERMINATE,
            ),
        )
        for registry, evaluated_request, expected in cases:
            with self.subTest(expected=expected):
                decision = VersionedMappingPolicyDecisionPoint(
                    registry, clock=lambda: self.now
                ).evaluate(evaluated_request)
                self.assertEqual(decision.effect, expected)

    def test_attribute_mapping_requires_exact_current_attribute(self) -> None:
        mapping = AuthorizationMapping(
            mapping_reference="synthetic-attribute-mapping",
            subject_kind=MappingSubjectKind.ATTRIBUTE,
            subject_reference="department:synthetic",
            object_reference="synthetic-object",
            field_references=("synthetic-field",),
            action_reference="synthetic-action",
            purpose_reference="synthetic-purpose",
            classification_reference="SYNTHETIC",
            required_policy_attributes=(("consent", "synthetic-consent-reference"),),
            policy_version="synthetic-policy-v1",
            effective_from=self.now - timedelta(minutes=1),
            expires_at=self.now + timedelta(minutes=30),
            approval_decision_reference="synthetic-approval",
        )
        registry = AuthorizationMappingRegistry((mapping,))
        missing = VersionedMappingPolicyDecisionPoint(registry, clock=lambda: self.now).evaluate(
            self.authorization_request(attributes=(("department", "synthetic"),))
        )
        exact = VersionedMappingPolicyDecisionPoint(registry, clock=lambda: self.now).evaluate(
            self.authorization_request(
                attributes=(
                    ("department", "synthetic"),
                    ("consent", "synthetic-consent-reference"),
                )
            )
        )
        self.assertEqual(missing.effect, AuthorizationEffect.DENY)
        self.assertEqual(exact.effect, AuthorizationEffect.PERMIT)

    def test_all_four_delegation_rules_preserve_source_boundaries(self) -> None:
        self.assertEqual(set(APPROVED_DELEGATION_CLASS_RULES), set(DelegationClass))
        self.assertEqual(
            APPROVED_DELEGATION_CLASS_RULES[DelegationClass.AGENT_FOR_HUMAN].expiry_boundary,
            "RUN_BOUND",
        )
        self.assertEqual(
            APPROVED_DELEGATION_CLASS_RULES[DelegationClass.AGENT_TO_AGENT].revocation_trigger,
            "PARENT_RUN_REVOCATION",
        )
        self.assertEqual(
            APPROVED_DELEGATION_CLASS_RULES[DelegationClass.SERVICE_TO_SERVICE].scope_binding,
            "SERVICE_REGISTRATION",
        )
        self.assertEqual(
            APPROVED_DELEGATION_CLASS_RULES[DelegationClass.HUMAN_TO_HUMAN].expiry_boundary,
            "TIME_BOXED",
        )

    def test_delegation_attribution_and_non_expansion_are_enforced(self) -> None:
        actor = self.principal(PrincipalClass.AGENT, "synthetic-agent")
        effective = self.principal(PrincipalClass.HUMAN, "synthetic-human")
        envelope = DelegationEnvelope(
            delegation_reference="synthetic-delegation",
            delegation_class=DelegationClass.AGENT_FOR_HUMAN,
            acting_identity=actor,
            effective_principal=effective,
            delegated_scopes=("synthetic-narrow-scope",),
            delegator_current_scopes=("synthetic-narrow-scope", "synthetic-other-scope"),
            delegate_eligible_scopes=("synthetic-narrow-scope",),
            purpose_reference="synthetic-purpose",
            source_record_reference="synthetic-task-contract",
            policy_version="synthetic-policy-v1",
            starts_at=self.now - timedelta(minutes=1),
            expires_at=self.now + timedelta(minutes=5),
            duration_policy_reference="synthetic-run-bound-policy",
        )
        result = DelegationEvaluator().evaluate(
            envelope,
            requested_scope="synthetic-narrow-scope",
            purpose_reference="synthetic-purpose",
            policy_version="synthetic-policy-v1",
            at=self.now,
        )
        self.assertTrue(result.valid)
        self.assertEqual(result.acting_identity, actor)
        self.assertEqual(result.effective_principal, effective)
        self.assertFalse(result.expands_authority)
        with self.assertRaises(AccessControlContractError):
            DelegationEnvelope(
                delegation_reference="synthetic-expanded-delegation",
                delegation_class=DelegationClass.AGENT_FOR_HUMAN,
                acting_identity=actor,
                effective_principal=effective,
                delegated_scopes=("synthetic-unowned-scope",),
                delegator_current_scopes=("synthetic-other-scope",),
                delegate_eligible_scopes=("synthetic-unowned-scope",),
                purpose_reference="synthetic-purpose",
                source_record_reference="synthetic-task-contract",
                policy_version="synthetic-policy-v1",
                starts_at=self.now,
                expires_at=self.now + timedelta(minutes=5),
                duration_policy_reference="synthetic-policy",
            )

    def test_delegation_revocation_expiry_scope_purpose_and_policy_fail_closed(self) -> None:
        envelope = DelegationEnvelope(
            delegation_reference="synthetic-delegation",
            delegation_class=DelegationClass.SERVICE_TO_SERVICE,
            acting_identity=self.principal(PrincipalClass.SERVICE, "synthetic-acting-service"),
            effective_principal=self.principal(
                PrincipalClass.SERVICE, "synthetic-effective-service"
            ),
            delegated_scopes=("synthetic-scope",),
            delegator_current_scopes=("synthetic-scope",),
            delegate_eligible_scopes=("synthetic-scope",),
            purpose_reference="synthetic-purpose",
            source_record_reference="synthetic-service-registration",
            policy_version="synthetic-policy-v1",
            starts_at=self.now - timedelta(minutes=1),
            expires_at=self.now + timedelta(minutes=1),
            duration_policy_reference="synthetic-session-bound-policy",
            service_credential_revoked=True,
        )
        evaluator = DelegationEvaluator()
        self.assertEqual(
            evaluator.evaluate(
                envelope,
                requested_scope="synthetic-scope",
                purpose_reference="synthetic-purpose",
                policy_version="synthetic-policy-v1",
                at=self.now,
            ).code,
            DelegationValidationCode.SOURCE_REVOCATION_TRIGGERED,
        )
        self.assertEqual(
            evaluator.evaluate(
                envelope,
                requested_scope="synthetic-scope",
                purpose_reference="different-purpose",
                policy_version="synthetic-policy-v1",
                at=self.now,
            ).code,
            DelegationValidationCode.SOURCE_REVOCATION_TRIGGERED,
        )
        self.assertEqual(
            evaluator.evaluate(
                envelope,
                requested_scope="synthetic-scope",
                purpose_reference="synthetic-purpose",
                policy_version="synthetic-policy-v1",
                at=self.now + timedelta(minutes=2),
            ).code,
            DelegationValidationCode.EXPIRED,
        )

    def test_human_deputisation_and_agent_nesting_require_source_records(self) -> None:
        human_one = self.principal(PrincipalClass.HUMAN, "synthetic-human-one")
        human_two = self.principal(PrincipalClass.HUMAN, "synthetic-human-two")
        with self.assertRaises(AccessControlContractError):
            DelegationEnvelope(
                "synthetic-human-delegation",
                DelegationClass.HUMAN_TO_HUMAN,
                human_one,
                human_two,
                ("synthetic-scope",),
                ("synthetic-scope",),
                ("synthetic-scope",),
                "synthetic-purpose",
                "synthetic-source-record",
                "synthetic-policy",
                self.now,
                self.now + timedelta(minutes=1),
                "synthetic-duration-policy",
            )
        agent_one = self.principal(PrincipalClass.AGENT, "synthetic-agent-one")
        agent_two = self.principal(PrincipalClass.AGENT, "synthetic-agent-two")
        with self.assertRaises(AccessControlContractError):
            DelegationEnvelope(
                "synthetic-agent-delegation",
                DelegationClass.AGENT_TO_AGENT,
                agent_one,
                agent_two,
                ("synthetic-scope",),
                ("synthetic-scope",),
                ("synthetic-scope",),
                "synthetic-purpose",
                "synthetic-source-record",
                "synthetic-policy",
                self.now,
                self.now + timedelta(minutes=1),
                "synthetic-duration-policy",
            )

    def test_three_privilege_classes_have_exact_approval_interfaces(self) -> None:
        self.assertEqual(set(APPROVED_PRIVILEGE_INTERFACES), set(PrivilegeClass))
        self.assertEqual(
            APPROVED_PRIVILEGE_INTERFACES[PrivilegeClass.INFRASTRUCTURE_CONFIGURATION_ADMIN],
            ApprovalInterface.AUTHORIZATION,
        )
        self.assertEqual(
            APPROVED_PRIVILEGE_INTERFACES[PrivilegeClass.IDENTITY_IAM_ADMIN],
            ApprovalInterface.AUTHORIZATION,
        )
        self.assertEqual(
            APPROVED_PRIVILEGE_INTERFACES[PrivilegeClass.DATA_CONTENT_ADMIN],
            ApprovalInterface.AUTHORIZATION_AND_ACCEPTANCE,
        )

    def test_unassigned_privileged_authority_means_no_grant(self) -> None:
        result = PrivilegedAccessEvaluator(UnassignedPrivilegedApprovalAuthority()).evaluate(
            self.privilege_request(), at=self.now
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.code, PrivilegeValidationCode.NO_CURRENT_APPROVAL_AUTHORITY)
        self.assertIsNone(result.elevation)

    def test_current_privilege_contract_and_negative_paths(self) -> None:
        request = self.privilege_request()
        valid = PrivilegedAccessEvaluator(
            FixedPrivilegeAuthority(self.privilege_decision(request))
        ).evaluate(request, at=self.now)
        self.assertTrue(valid.valid)
        self.assertEqual(
            valid.elevation.action_references if valid.elevation else (), request.action_references
        )
        self_approved = PrivilegedAccessEvaluator(
            FixedPrivilegeAuthority(self.privilege_decision(request, approver=request.requester))
        ).evaluate(request, at=self.now)
        expired = PrivilegedAccessEvaluator(
            FixedPrivilegeAuthority(
                self.privilege_decision(request, expires_at=self.now - timedelta(seconds=1))
            )
        ).evaluate(request, at=self.now)
        revoked = PrivilegedAccessEvaluator(
            FixedPrivilegeAuthority(
                self.privilege_decision(request, revoked_at=self.now - timedelta(seconds=1))
            )
        ).evaluate(request, at=self.now)
        self.assertEqual(self_approved.code, PrivilegeValidationCode.SELF_APPROVAL)
        self.assertEqual(expired.code, PrivilegeValidationCode.APPROVAL_EXPIRED)
        self.assertEqual(revoked.code, PrivilegeValidationCode.APPROVAL_REVOKED)

    def test_content_admin_requires_separate_justification_and_acceptance(self) -> None:
        with self.assertRaises(AccessControlContractError):
            PrivilegedAccessRequest(
                request_reference="synthetic-content-request",
                requester=self.principal(PrincipalClass.HUMAN, "synthetic-requester"),
                privilege_class=PrivilegeClass.DATA_CONTENT_ADMIN,
                target_reference="synthetic-content",
                action_references=("synthetic-content-action",),
                justification_reference="synthetic-justification",
                policy_version="synthetic-policy",
                requested_at=self.now,
                expires_at=self.now + timedelta(minutes=1),
                duration_policy_reference="synthetic-duration-policy",
                step_up_evidence_reference="synthetic-step-up",
                assurance_state=AssuranceState.ELEVATED,
            )
        request = self.privilege_request(PrivilegeClass.DATA_CONTENT_ADMIN)
        with self.assertRaises(AccessControlContractError):
            PrivilegedApprovalDecision(
                decision_reference="synthetic-decision",
                request_reference=request.request_reference,
                approver=self.principal(PrincipalClass.HUMAN, "synthetic-approver"),
                authority_assignment_reference="synthetic-authority",
                privilege_class=request.privilege_class,
                target_reference=request.target_reference,
                action_references=request.action_references,
                policy_version=request.policy_version,
                approved=True,
                decided_at=self.now,
                expires_at=self.now + timedelta(minutes=1),
            )

    def test_emergency_classes_enforce_trigger_and_containment_action(self) -> None:
        for emergency_class in EmergencyClass:
            with self.subTest(emergency_class=emergency_class):
                declaration = self.declaration(emergency_class)
                if emergency_class is EmergencyClass.INFRASTRUCTURE_BREAK_GLASS_ADMIN:
                    self.assertEqual(
                        declaration.trigger_class,
                        EmergencyTriggerClass.DECLARED_OPERATIONAL_EMERGENCY,
                    )
                else:
                    self.assertEqual(
                        declaration.trigger_class,
                        EmergencyTriggerClass.DECLARED_SECURITY_EMERGENCY,
                    )
        with self.assertRaises(AccessControlContractError):
            EmergencyDeclaration(
                declaration_reference="synthetic-invalid-trigger",
                emergency_class=EmergencyClass.IDENTITY_ACCESS_SUSPENSION,
                trigger_class=EmergencyTriggerClass.DECLARED_OPERATIONAL_EMERGENCY,
                declared_by=self.principal(PrincipalClass.HUMAN, "synthetic-authority"),
                target_reference="synthetic-target",
                purpose_reference="synthetic-purpose",
                decision_reference="synthetic-decision",
                declared_at=self.now,
                expires_at=self.now + timedelta(minutes=1),
                duration_policy_reference="synthetic-duration-policy",
                policy_version="synthetic-policy",
            )
        with self.assertRaises(AccessControlContractError):
            self.emergency_request(
                self.declaration(EmergencyClass.IDENTITY_ACCESS_SUSPENSION),
                self.principal(PrincipalClass.HUMAN, "synthetic-operator"),
                action=EmergencyAction.ADMINISTER,
            )

    def test_unassigned_emergency_eligibility_means_no_activation(self) -> None:
        declaration = self.declaration()
        operator = self.principal(PrincipalClass.HUMAN, "synthetic-operator")
        result = EmergencyAccessEvaluator(UnassignedEmergencyEligibility()).evaluate(
            self.emergency_request(declaration, operator), at=self.now
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.code, EmergencyValidationCode.NO_ELIGIBLE_EMERGENCY_AUTHORITY)
        self.assertIsNone(result.activation_reference)

    def test_emergency_contract_auto_expires_and_revocation_is_current(self) -> None:
        declaration = self.declaration()
        operator = self.principal(PrincipalClass.HUMAN, "synthetic-operator")
        eligibility = EmergencyEligibilityDecision(
            eligibility_reference="synthetic-eligibility",
            emergency_class=declaration.emergency_class,
            eligible_operator=operator,
            authority_holder=self.principal(PrincipalClass.HUMAN, "synthetic-declaring-authority"),
            target_reference=declaration.target_reference,
            eligible=True,
            effective_from=self.now - timedelta(minutes=1),
            expires_at=self.now + timedelta(minutes=15),
        )
        request = self.emergency_request(declaration, operator)
        evaluator = EmergencyAccessEvaluator(FixedEmergencyEligibility(eligibility))
        valid = evaluator.evaluate(request, at=self.now)
        expired = evaluator.evaluate(request, at=request.expires_at)
        self.assertTrue(valid.valid)
        self.assertEqual(valid.auto_expires_at, request.expires_at)
        self.assertEqual(expired.code, EmergencyValidationCode.EXPIRED)
        revoked_declaration = self.declaration(revoked_at=self.now - timedelta(seconds=1))
        revoked_request = self.emergency_request(revoked_declaration, operator)
        revoked = EmergencyAccessEvaluator(
            FixedEmergencyEligibility(
                EmergencyEligibilityDecision(
                    eligibility_reference="synthetic-revoked-eligibility",
                    emergency_class=revoked_declaration.emergency_class,
                    eligible_operator=operator,
                    authority_holder=eligibility.authority_holder,
                    target_reference=revoked_declaration.target_reference,
                    eligible=True,
                    effective_from=self.now - timedelta(minutes=1),
                    expires_at=self.now + timedelta(minutes=10),
                )
            )
        ).evaluate(revoked_request, at=self.now)
        self.assertEqual(revoked.code, EmergencyValidationCode.REVOKED)

    def test_post_event_disposition_requires_notification_independence_and_restoration(
        self,
    ) -> None:
        operator = self.principal(PrincipalClass.HUMAN, "synthetic-operator")
        declarer = self.principal(PrincipalClass.HUMAN, "synthetic-declarer")
        reviewer = self.principal(PrincipalClass.HUMAN, "synthetic-reviewer")
        complete = EmergencyNotificationObligation(
            activation_reference="synthetic-activation",
            domain_accountable_authority_reference="synthetic-domain-authority",
            assurance_audit_reference="synthetic-assurance-audit",
        )
        incomplete = EmergencyNotificationObligation(
            activation_reference="synthetic-activation",
            domain_accountable_authority_reference=None,
            assurance_audit_reference=None,
        )
        review = EmergencyPostEventReview(
            review_reference="synthetic-review",
            activation_reference="synthetic-activation",
            reviewer=reviewer,
            operator=operator,
            declaring_authority=declarer,
            reviewed_at=self.now,
            disposition=PostEventDisposition.REINSTATE,
            scope_confirmed=True,
            expiry_revocation_confirmed=True,
            effects_reviewed=True,
            restoration_evidence_reference="synthetic-restoration-evidence",
        )
        self.assertTrue(review.supports_disposition(complete))
        self.assertFalse(review.supports_disposition(incomplete))
        self_review = EmergencyPostEventReview(
            review_reference="synthetic-self-review",
            activation_reference="synthetic-activation",
            reviewer=operator,
            operator=operator,
            declaring_authority=declarer,
            reviewed_at=self.now,
            disposition=PostEventDisposition.KEEP_CONTAINED,
            scope_confirmed=True,
            expiry_revocation_confirmed=True,
            effects_reviewed=True,
            restoration_evidence_reference=None,
        )
        self.assertFalse(self_review.supports_disposition(complete))

    def test_access_control_signals_are_minimized_and_non_authoritative(self) -> None:
        sink = InMemoryObservabilitySink()
        AccessControlSignals(sink).emit(
            correlation_id="synthetic-correlation",
            contract_class="PRIVILEGED_ACCESS",
            outcome="DENY",
            reason_code="NO_CURRENT_APPROVAL_AUTHORITY",
        )
        event = sink.events()[0]
        self.assertEqual(event.category, SignalCategory.SECURITY_CONDITION)
        self.assertFalse(event.authoritative_evidence)
        self.assertFalse(event.institutional_finding)
        self.assertFalse(event.institutional_decision)
        self.assertEqual(
            event.attributes,
            (
                ("contract_class", "PRIVILEGED_ACCESS"),
                ("outcome", "DENY"),
                ("reason_code", "NO_CURRENT_APPROVAL_AUTHORITY"),
            ),
        )
        with self.assertRaises(AccessControlContractError) as caught:
            AccessControlSignals(sink).emit(
                correlation_id="synthetic-correlation",
                contract_class="credential_value=protected-material",
                outcome="DENY",
                reason_code="INVALID",
            )
        self.assertNotIn("protected-material", str(caught.exception))


if __name__ == "__main__":
    unittest.main()
