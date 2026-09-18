# WBS-16-WP-001 Security Principal and Authorization Contract Foundation

Status: `WORK COMPLETE — LOCALLY VERIFIED; SECURITY ACCREDITATION AND ACCEPTANCE PENDING`

Prepared: `2026-09-18`

Decision prerequisite: SATISFIED by W16-D1-A through W16-D4-A under `NCIE-WBS16-OWNER-DECISION-2026-09-18-008`.

Implementation authority: `NCIE-WBS16-OWNER-DECISION-2026-09-18-009`.

Source-control release authority: `NCIE-WBS16-OWNER-DECISION-2026-09-18-010`.

## 1. Objective

Extend the WBS-15 provider-neutral identity and authorization boundaries into typed WBS-16 security contracts that preserve principal-class separation, current authorization, four-layer decisions and deny-by-default enforcement without selecting or activating an IAM provider.

## 2. Controlled scope

WP-001 implements:

1. A typed `SecurityPrincipal` model with the seven approved principal classes and opaque source references.
2. An `IdentitySourceBoundary` protocol that cannot authenticate an unknown, unbound or mismatched source.
3. Typed current-authorization inputs covering principal, object/resource, field set, action, purpose, correlation and policy-version context.
4. Typed `PERMIT`, `DENY` and `INDETERMINATE` decisions with bounded, non-sensitive reason codes.
5. A `PolicyDecisionPoint` protocol and a dependency-free deny-all reference implementation.
6. A `PolicyEnforcementPoint` adapter to the existing WBS-15 `AuthorizationBoundary` so missing, stale, invalid, error and indeterminate decisions fail closed.
7. Provider-neutral, non-authoritative security-decision signals using the existing observability contracts without audit-retention or Evidence claims.
8. Standard-library unit and contract tests, traceability and local implementation evidence.

## 3. Explicit exclusions

- IAM vendor, identity-provider product, tenant or external service.
- Login, authentication factors, tokens, credentials, sessions, reauthentication or recovery.
- Identity proofing, enrollment, provisioning, suspension or termination workflows.
- Institutional role catalogue, role assignments, attribute mappings, permissions or access grants.
- Delegation, impersonation, privileged access or break-glass behavior.
- Secret/key management, cryptographic product selection, network segmentation or egress controls.
- Agent activation, model/provider security, Tool authorization, DLP or protected-identity disclosure.
- Persistent audit store, retention policy, institutional Evidence or WBS-20 implementation.
- Infrastructure, deployment, live identities/data, security accreditation, controlled acceptance or go-live.
- Any new dependency or technology unless separately justified and approved.

## 4. Completed tasks

| Task | Implemented activity | Evidence |
|---|---|---|
| `WBS-16-WP-001-T-001` | Define principal classes, opaque references and non-substitution validation | Unit tests for every class and mismatch path |
| `WBS-16-WP-001-T-002` | Define identity-source resolution protocol and fail-closed unbound implementation | Unknown/unbound source tests |
| `WBS-16-WP-001-T-003` | Define four-layer authorization request and decision contracts | Schema/type tests for object, field, action and purpose dimensions |
| `WBS-16-WP-001-T-004` | Implement deny-all policy decision point | Missing/no-policy/error paths deny |
| `WBS-16-WP-001-T-005` | Adapt decisions to the WBS-15 authorization enforcement boundary | Protected-route regression and bypass-negative tests |
| `WBS-16-WP-001-T-006` | Emit bounded neutral decision signals | Minimization and non-authority tests |
| `WBS-16-WP-001-T-007` | Produce traceability and local run evidence | Strict typing, lint, format, compilation and cumulative tests |

## 5. Completion criteria and result

WP-001 may be reported `WORK COMPLETE` for its local scope only when:

1. The four prerequisite Human decisions and separate implementation authority are recorded.
2. No unapproved dependency or technology is introduced.
3. All seven principal classes remain distinct and no class substitutes for another.
4. Unknown, unbound or mismatched identity sources authenticate no principal.
5. Authorization explicitly evaluates object, field, action and purpose dimensions.
6. No role, attribute, permission or policy grant exists in the reference implementation.
7. Missing, stale, invalid, error and `INDETERMINATE` decisions are enforced as deny.
8. Prior or cached authorization is never represented as current authority.
9. Security signals contain no credentials, tokens, secrets, protected identity values or authoritative Evidence claim.
10. Existing WBS-15 behavior remains regression-clean.
11. Strict typing, lint, formatting, compilation and all unit/contract tests pass locally.
12. Evidence states that authentication, IAM activation, the remaining HR9 decisions, security accreditation, controlled acceptance and go-live remain pending.

All twelve criteria passed under `LOCAL-WBS16-WP001-20260918-001`. This result is local implementation evidence and is not security accreditation or controlled acceptance.

## 6. Stop conditions

Stop and request Human direction if the work requires a provider, identifier format with institutional consequences, live identity, credential/token/session handling, actual role or attribute mapping, access grant, persistent security log, new dependency, infrastructure, network control, secret/key handling, external service or broader HR9 decision.

## 7. Downstream sequence

WP-001 establishes contracts only. A later authorized WBS-16 package must resolve the applicable proofing/authentication, delegation, privileged-access, secrets, network and audit prerequisites before any later workstream consumes WBS-16 as an operational security posture.

## 8. VPF boundary

VPF requirements are applied behaviorally to Human authority, least privilege, identity separation, explainability, minimization and sovereignty. No VPF runtime, validator, ledger, signature, residency enforcement or accreditation is implemented or claimed by this package.
