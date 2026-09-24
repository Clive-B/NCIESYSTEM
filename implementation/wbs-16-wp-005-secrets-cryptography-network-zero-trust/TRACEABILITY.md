# WBS-16-WP-005 Traceability

Status: `IMPLEMENTED AND LOCALLY VERIFIED`

| Requirement or decision | Implementation | Verification | Boundary |
|---|---|---|---|
| `HR9-11-1` / W16-D15-A | `OpaqueProtectedReference`, lifecycle-event metadata and unassigned custodial boundary | Literal/protected-reference rejection and zero-authority lifecycle denial | No protected material or lifecycle execution |
| Custody/policy/review/assurance separation | Distinct custodial, policy-approval, exception-review and independent-assurance interfaces | All controlled authority interfaces return no decision/attestation | No operational holder invented |
| Prohibited surfaces | `ProhibitedSurface` and `ProhibitedSurfaceEvaluator` | Every prohibited surface and plaintext fallback denies; exception flag remains false | No protected value is inspected |
| Exception policy | Time-bounded request/decision contracts and unassigned authority evaluator | Missing authority, self-approval, mismatch, expiry and revocation paths fail closed | Zero exception grants |
| `HR9-12-1` / W16-D16-A | Three protection scopes, three conceptual hierarchy tiers, four separation dimensions and agility reference | Exact taxonomy, complete separation and mismatch tests | No algorithm, parameter, key, profile or product |
| Current crypto policy | Immutable registry and `CryptographicPolicyEvaluator` bound to current authorization | Empty, missing, stale, revoked, mismatched and unauthorized paths deny | Controlled registry is empty; no cryptography executes |
| `HR9-13-1` / W16-D17-A | Seven `TrustZone` labels and source-defined `ServiceBoundaryClass` rules | Exact zone/boundary taxonomy and forbidden AI/Agent-to-data checks | No network topology or route |
| Egress classes | Five `EgressClass` values and exact policy metadata | Empty registry, gateway, policy, boundary and ambiguity negative paths | Zero destinations and allow entries |
| Agent/external ceiling | `AgentEgressCeiling` and current-authorization/provider/residency checks | Any false ceiling denies; cross-border path requires separate Human authorization | No Agent internet access, external call or transfer |
| Minimized signals | `SecurityProtectionSignals` over existing operational-event contract | Bounded attributes; all Evidence/finding/decision flags false | No persistent audit or institutional Evidence |
| Decision provenance | Baseline/decision/implementation constants | Exact `...-020` and `...-021` assertions | No authority beyond WP-005 |

Implementation evidence is recorded under `evidence/IMPLEMENTATION_20260923_001.md`; local execution evidence is recorded under `evidence/LOCAL_RUN_20260923_001.md`.

Controlled source-release evidence is recorded under `evidence/SOURCE_CONTROL_RELEASE_20260924_001.md`.
