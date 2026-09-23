# WBS-16-WP-004 Traceability

Status: `IMPLEMENTED AND LOCALLY VERIFIED`

| Requirement or decision | Implementation | Verification | Boundary |
|---|---|---|---|
| `HR9-6-1` / W16-D11-A | `AuthorizationMapping`, immutable `AuthorizationMappingRegistry`, empty controlled registry and `VersionedMappingPolicyDecisionPoint` | Empty denial, exact synthetic match, attribute/consent reference, stale, revoked, mismatch and ambiguity tests | No institution-specific mapping or grant |
| WP-001 integration | Existing `CurrentAuthorizationRequest`, four dimensions and `PolicyEnforcementPoint` | Empty mapping decision enforced as deny; exact synthetic fixture exercises contract | Current authorization only; no remembered authority |
| `HR9-7-1` / W16-D12-A | Four `DelegationClass` rules and `DelegationEnvelope` | Taxonomy, class identity, intersection scope, attribution, expiry/revocation and source-trigger tests | No delegation issuance or activation |
| Non-expansion | Delegated scope must be a subset of delegator authority and delegate eligibility | Authority-amplification construction rejection | `expands_authority` remains false |
| Human deputisation | Governed record and confirmed delegability required | Missing record/delegability rejection | No deputy or non-delegable list invented |
| `HR9-8-1` / W16-D13-A | Three `PrivilegeClass` values, exact approval interfaces, request/decision/elevation contracts | Class/interface, elevated-assurance, justification, Acceptance, self-approval, expiry and revocation tests | No operational approver or privilege holder |
| Unassigned privilege authority | `UnassignedPrivilegedApprovalAuthority` | Every reference elevation attempt denies with `NO_CURRENT_APPROVAL_AUTHORITY` | Zero privilege grants/elevations |
| `HR9-9-1` / W16-D14-A | Three `EmergencyClass` values, exact trigger/action ceilings and bounded declarations | Trigger mismatch, action overreach, explicit expiry and revocation tests | No declared live emergency or containment execution |
| Zero eligibility | `UnassignedEmergencyEligibility` | Every reference activation attempt denies with `NO_ELIGIBLE_EMERGENCY_AUTHORITY` | No Emergency Authority/operator/roster |
| Notification/review | `EmergencyNotificationObligation` and `EmergencyPostEventReview` | Incomplete notification, self-review and restoration-evidence negative tests | No notification sent or reviewer assigned |
| Minimized signals | `AccessControlSignals` using existing operational event contract | Bounded attributes, protected-reference rejection, all authority flags false | No persistent audit or institutional Evidence claim |
| Decision provenance | Baseline/decision/implementation constants | Exact `...-017` and `...-018` assertions | No authority beyond WP-004 |

Implementation evidence is recorded under `evidence/IMPLEMENTATION_20260923_001.md`; local execution evidence is recorded under `evidence/LOCAL_RUN_20260923_001.md`.

Controlled source-release evidence is recorded under `evidence/SOURCE_CONTROL_RELEASE_20260923_001.md`.
