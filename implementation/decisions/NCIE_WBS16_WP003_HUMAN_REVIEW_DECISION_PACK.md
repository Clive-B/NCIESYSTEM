# NCIE WBS-16-WP-003 Human Review Decision Pack

Status: `DECIDED — W16-D7-A / W16-D8-A / W16-D9-A / W16-D10-A; IMPLEMENTATION RELEASED UNDER ...-015`

Prepared: `2026-09-19`

Decided: `2026-09-19`

Proposed work package: `WBS-16-WP-003 Identity Lifecycle, Authentication and Session Assurance`

## 1. Purpose

This pack presents the minimum Human decisions required before WP-003 may be considered for a separate implementation release. It covers:

- follow-on `HR9-3-1`: whether the seven approved logical authoritative-source categories remain provider-neutral for WP-003;
- `HR9-4-1`: proofing strength per identity class and institutional enrollment authority;
- `HR9-5-1`: assurance levels and step-up triggers; and
- `HR9-10-1`: session assurance/expiry policy and credential classes.

Selecting options in this pack resolves architecture prerequisites for a local contract increment only. It does **not** authorize implementation, select an IAM provider, enroll an identity, issue a credential/session, grant access, activate an external system, accept security risk, accredit the system, deploy it or approve go-live.

## 2. Controlling source findings

The approved and controlled source chain establishes these constraints:

1. The seven principal classes remain non-equivalent: Human, workload, Agent, service, session/device, privileged and validator identity. No class may substitute for another.
2. Technical identity never constitutes an institutional governance role or Human approval.
3. Proofing is never inferred from voice, conversation, familiarity, ARGUS history or a prior session.
4. Proofing, enrollment, activation, update, suspension, termination, reactivation, recovery and duplicate-identity handling are distinct, traceable lifecycle events.
5. Suspension, termination and recovery must propagate immediate revocation/re-evaluation to dependent sessions, tokens and cached authorization state.
6. Authentication establishes identity assurance, not action authorization. Chapter 6 current authorization remains a separate mandatory decision.
7. The required assurance contexts are standard session, privileged access, break-glass access, high-risk consequential action and post-recovery session.
8. Human credentials must never be copied into Agent Context. An Agent acts only through its own separately governed identity/delegation boundary.
9. Every session/token requires explicit scope and audience. Continuity is not indefinite authority; expiry, refresh, revocation, binding and replay protection are governed states.
10. NCIE-009 deliberately supplies no default factor set, numeric authentication threshold or session duration. Codex may not invent one.

## 3. Decision W16-D7 — follow-on HR9-3-1 authoritative-source disposition

### Option A — Retain logical source categories and defer provider binding (recommended)

Carry the W16-D2-A taxonomy into WP-003 unchanged:

| Principal class | Approved logical authoritative-source category | WP-003 boundary |
|---|---|---|
| Human | Institutional identity source | Lifecycle/proofing interface only |
| Workload | Deployment/orchestration platform | Registration/attestation interface only |
| Agent | Agent Factory/Registry | Registration/lifecycle interface only |
| Service | Service registration | Registration/lifecycle interface only |
| Session/device | Authentication session issuer | Derived identity/session interface only |
| Privileged | Privileged-access-management authority | Enhanced-proofing interface only; no privilege |
| Validator | VPF validator registration | Registration/provenance interface only; no approval authority |

Also confirm that:

- no additional institution-specific principal class enters WP-003;
- provider, product, tenant, registry instance, identifier format and protocol remain deferred;
- an unbound, unknown or mismatched source yields no usable identity;
- session/device identity derives from a currently valid base identity and cannot replace it; and
- source resolution, proofing and authentication confer no authorization or governance role.

Implication: WP-003 can implement source-neutral lifecycle and assurance contracts with deterministic fail-closed behavior, but cannot authenticate a real user or connect to IAM.

If selected, this resolves `HR9-3-1` for the WP-003 logical-contract scope only; concrete source/provider binding remains an operational IAM blocker.

### Option B — Bind one or more concrete providers/sources now

Supply the approved product/provider, tenant or registry instance for each affected principal class, including residency, cross-border, procurement, protocol, identifier, operational-owner and security-acceptance decisions.

Implication: this materially broadens WP-003 beyond the prepared local scope and requires a revised work package before implementation authorization.

### Option C — Defer source disposition

Keep WP-003 blocked. WP-001 remains unbound and deny-by-default.

Recommendation: **W16-D7-A**.

## 4. Decision W16-D8 — HR9-4-1 proofing strength and enrollment authority

### Option A — Approve symbolic proofing tiers and unassigned operational holders (recommended)

Approve four provider-neutral proofing states:

| Proofing state | Meaning | Usable identity consequence |
|---|---|---|
| `UNBOUND` | No authoritative source or proofing evidence is currently bound | No identity; deny |
| `SOURCE_ATTESTED` | The approved logical source category attests the technical identity and its provenance | Eligible only for the source-bounded technical class; no Human or governance equivalence |
| `INSTITUTIONALLY_VERIFIED` | An institutional proofing process has verified the identity against approved evidence | Eligible for baseline authentication, subject to current lifecycle and assurance state |
| `ENHANCED_SENSITIVE` | Enhanced proofing is recorded for a sensitive/privileged identity context | Eligibility input only; grants no privilege or authorization |

Approve this minimum mapping for WP-003:

| Principal class | Required proofing contract state | Enrollment authority class |
|---|---|---|
| Human | `INSTITUTIONALLY_VERIFIED` | Human `Identity Lifecycle Approver` |
| Workload | `SOURCE_ATTESTED` | Human/institutional `Authoritative Source Owner` |
| Agent | `SOURCE_ATTESTED` with owner, purpose and version references | Human/institutional `Authoritative Source Owner` |
| Service | `SOURCE_ATTESTED` with owner and purpose references | Human/institutional `Authoritative Source Owner` |
| Session/device | Derived from a current proofed base identity and current issuer state | Session issuer may create the derivative record but holds no enrollment/approval authority |
| Privileged | `ENHANCED_SENSITIVE` | Human `Identity Lifecycle Approver`; actual privilege remains WP-004 |
| Validator | `SOURCE_ATTESTED` with registration/provenance reference | Human/institutional `Authoritative Source Owner`; registration is not Human approval |

For this local increment, the authority **classes** are approved but their operational institutional holders remain unassigned. Therefore:

- no real enrollment, reactivation or recovery can succeed;
- a missing/currently unassigned authority fails closed;
- evidence values remain opaque references and cannot contain protected identity data;
- duplicate-identity resolution cannot merge identities automatically; and
- recovery or reactivation cannot restore prior privilege, sessions or assurance automatically.

Implication: the package can encode and test the proofing/lifecycle rules while preserving zero live enrollments. A later Human decision must name and evidence current authority holders before operational use.

If selected, this satisfies the proofing-tier and enrollment-authority-class prerequisites for WP-003 only. `HR9-4-1` remains operationally open for authority-holder assignment, evidence rules and live enrollment.

### Option B — Assign operational enrollment authorities now

Supply the institutional function and current holder for `Identity Lifecycle Approver` and each applicable `Authoritative Source Owner`, together with scope, effective date, expiry/deputisation, segregation-of-duties and evidence rules.

Implication: holder assignment still does not authorize provider integration or live enrollment; those require a revised package and explicit release.

### Option C — Defer proofing/enrollment policy

Do not implement lifecycle/proofing contracts. WP-003 remains blocked.

Recommendation: **W16-D8-A**, because it establishes testable proofing semantics without fabricating institutional holders or processing live identity evidence.

## 5. Decision W16-D9 — HR9-5-1 assurance levels and step-up triggers

### Option A — Approve symbolic assurance levels and the NCIE-009 trigger matrix (recommended)

Approve four provider-neutral assurance states:

| Assurance state | Meaning |
|---|---|
| `UNVERIFIED` | No current authentication assurance; deny authenticated use |
| `BASELINE` | Current baseline authentication under an approved policy reference |
| `ELEVATED` | Stronger and/or more recent authentication required by a governed context |
| `RECOVERY_REPROOFED` | Current assurance established after recovery through fresh proofing; no pre-recovery assurance inherited |

Approve these minimum context requirements:

| Assurance context | Minimum symbolic requirement | Step-up trigger |
|---|---|---|
| Standard session | `BASELINE` | None beyond current policy evaluation |
| Privileged access | `ELEVATED` | Privilege-elevation request; actual privilege decision remains WP-004 |
| Break-glass access | `ELEVATED` plus governed emergency trigger | Emergency trigger; break-glass authority remains WP-004 |
| High-risk consequential action | `ELEVATED` and current/fresh under the applicable policy | Action classified high-risk |
| Post-recovery session | `RECOVERY_REPROOFED` | Recovery event; old assurance/session cannot be reused |

Also confirm:

- assurance is an input to current authorization, never authorization itself;
- missing, expired, stale, insufficient or indeterminate assurance denies the protected operation;
- factor sets, authenticators, biometric use and numeric thresholds/freshness windows remain unselected; and
- where a required numeric/factor policy is absent, no reference implementation may manufacture or claim the required assurance.

Implication: WP-003 can implement assurance-state and step-up contracts but cannot perform real authentication or satisfy a production assurance level.

If selected, this satisfies the assurance taxonomy and trigger matrix for WP-003 only. `HR9-5-1` remains operationally open for approved factor sets, numeric thresholds and freshness policy.

### Option B — Approve concrete factor sets and numeric thresholds now

Supply factor classes, combinations, permitted recovery factors, accessibility/accommodation rules, freshness thresholds and assurance mappings for every context.

Implication: this invokes technology, privacy, protected-identity, accessibility, provider and possibly biometric decisions beyond the prepared scope.

### Option C — Defer assurance policy

Do not implement assurance/step-up contracts. WP-003 remains blocked.

Recommendation: **W16-D9-A**.

## 6. Decision W16-D10 — HR9-10-1 session expiry and credential classes

### Option A — Approve explicit-expiry contracts with no default duration (recommended)

Approve provider-neutral metadata classes aligned to the seven principal classes:

1. Human authenticator reference.
2. Workload credential reference.
3. Agent credential reference.
4. Service credential reference.
5. Session/device credential reference.
6. Privileged credential reference.
7. Validator credential reference.

These are opaque metadata/reference classes only; WP-003 may not contain passwords, private keys, tokens, biometric templates, recovery secrets or other credential material.

Approve the following lifecycle policy:

- every session/credential record binds its principal class, authoritative source, scope, audience, issue time, explicit expiry time, assurance state, policy version and revocation state;
- no indefinite, implicit or default-duration session exists;
- WP-003 adopts no numeric lifetime, idle timeout, refresh window or freshness threshold;
- absence of an approved duration/policy reference prevents issuance in the fail-closed reference behavior;
- refresh or reauthentication creates a newly evaluated state and never extends stale authority automatically;
- suspension, termination, recovery, source invalidation or credential revocation immediately invalidates dependent session/token/cache state;
- a session cannot exceed the current validity/assurance of its base identity or issuing credential;
- session binding and replay-protection requirements are represented as contracts, while algorithms/products remain deferred; and
- Human credential material is prohibited from Agent Context, prompts, logs, events and source code.

Implication: WP-003 can validate lifecycle metadata and revocation propagation without issuing a usable credential or session. Operational issuance remains impossible until provider and timing policy decisions are separately approved.

If selected, this satisfies the credential-class and expiry-contract prerequisites for WP-003 only. `HR9-10-1` remains operationally open for numeric timing, concrete issuer and credential policy.

### Option B — Approve numeric timing and concrete credential policy now

Supply maximum/idle lifetimes, freshness and refresh windows, credential/secret forms, issuer rules, binding mechanism, replay controls and recovery timing by principal/context.

Implication: this broadens scope into provider, cryptography/secrets, infrastructure, privacy, operations and later HR9 decisions; a revised package is required.

### Option C — Defer session/credential policy

Do not implement session/credential lifecycle contracts. WP-003 remains blocked.

Recommendation: **W16-D10-A**.

## 7. Consolidated recommendation and implications

Recommended selection: **W16-D7-A / W16-D8-A / W16-D9-A / W16-D10-A**.

If approved, these choices would resolve the architecture prerequisites for a provider-neutral, non-operational contract increment. They deliberately produce:

- seven unchanged principal/source categories;
- zero live enrollments;
- zero usable credentials or sessions;
- no factor or biometric choice;
- no numeric duration or freshness threshold;
- no privilege, permission, delegation or authorization grant;
- fail-closed behavior wherever an operational holder, provider or policy value is absent; and
- explicit separation of identity proofing, authentication assurance, current authorization and Human governance authority.

The tradeoff is intentional: WP-003 becomes locally testable and downstream-shaping, but not operational IAM.

| HR item | Recommended WP-003 disposition | Still required before operational IAM |
|---|---|---|
| Follow-on `HR9-3-1` | Logical source mapping confirmed | Provider/source instances and residency acceptance |
| `HR9-4-1` | Proofing tiers and authority classes confirmed | Current authority holders, evidence policy and live workflow approval |
| `HR9-5-1` | Symbolic assurance/step-up matrix confirmed | Factors, numeric thresholds and freshness windows |
| `HR9-10-1` | Credential-reference classes and explicit-expiry semantics confirmed | Issuers, numeric timing and concrete credential/session policy |

## 8. Proposed implementation boundary

If the four decisions are approved, a later and separate implementation authorization may release a bounded package containing:

- typed proofing, enrollment and lifecycle-state contracts;
- validated transition rules for pending, active, suspended, terminated, reactivation and recovery states;
- opaque proofing/evidence references with protected-value minimization;
- enrollment-authority interfaces that remain unassigned/fail closed;
- the four symbolic assurance states and five context/step-up mappings;
- session/credential metadata classes with explicit scope, audience, policy version, issue/expiry and revocation fields;
- dependency/revocation-propagation contracts for sessions, tokens and cached authorization state;
- recovery rules that reject inherited pre-recovery assurance or privilege;
- provider-neutral session-binding/replay requirement markers;
- local identity-bypass, stale-state, recovery, expiry, source-mismatch and protected-value negative tests; and
- traceability and local implementation evidence.

The implementation would not include:

- an IAM provider, product, tenant, directory, PAM, registry or external API;
- real people, live identities, protected identity evidence or governed production data;
- password, token, key, biometric, certificate or recovery-secret material;
- actual enrollment, login, authentication, session issuance, refresh, recovery or revocation operation;
- factor selection, biometric decision, numeric duration/freshness threshold or production policy;
- role mapping, permission, access grant, delegation, privileged access or break-glass activation;
- persistent identity/session/audit storage, notification service or institutional Evidence creation;
- infrastructure, network, deployment, security accreditation, acceptance or go-live; or
- WP-004 or any later WBS-16 capability.

## 9. Proposed local completion criteria

WP-003 may be reported locally work-complete only if:

1. the recorded W16-D7 through W16-D10 selections are represented without scope expansion;
2. every principal remains bound to exactly one approved logical source category;
3. proofing, lifecycle, assurance and session states are distinct and versioned;
4. no conversation, voice, prior session or technical identity is accepted as Human proofing;
5. missing/unassigned enrollment authority prevents enrollment, reactivation and recovery;
6. invalid lifecycle transitions, automatic duplicate merging and reactivation of terminated identity fail closed;
7. authentication assurance cannot authorize an action or create a governance role;
8. insufficient, stale, missing or indeterminate assurance denies the protected context;
9. no session exists without explicit scope, audience, issue time, expiry time and policy version;
10. suspension, termination, recovery and revocation invalidate all represented dependent state immediately;
11. recovery cannot inherit pre-recovery assurance, session or privilege;
12. no protected value or credential material can enter contracts, errors, logs or test evidence;
13. no reference implementation issues a usable identity/session while provider, holder or timing policy remains absent;
14. WP-001/WP-002 and WBS-15 regressions plus typing, lint, formatting, compilation and reproducibility checks pass; and
15. evidence states that local tests are not IAM activation, independent security verification, accreditation, acceptance or go-live.

## 10. Stop conditions

Stop and request new Human direction if implementation would require any of the following:

1. a named provider, product, tenant, registry, directory, protocol or external identity service;
2. an additional principal class or a changed authoritative-source mapping;
3. a named operational enrollment/recovery authority holder or live workflow activation;
4. real identity/proofing data, protected identity attributes, biometrics or consent processing;
5. credential, authenticator, token, key, certificate, secret or recovery-material handling;
6. a factor set, factor strength, numeric proofing threshold, session duration, idle timeout, refresh window or freshness threshold;
7. a role/attribute mapping, permission, grant, delegation, privileged-access or break-glass decision;
8. persistent storage, audit/Evidence creation, notification, network, infrastructure or deployment;
9. a new dependency or technology; or
10. any claim of operational IAM, production risk acceptance, independent verification, accreditation, controlled acceptance or go-live.

## 11. Recorded decision

- W16-D7 selection: `A — retain logical source categories; defer provider binding`
- W16-D8 selection: `A — symbolic proofing tiers; operational holders unassigned`
- W16-D9 selection: `A — symbolic assurance levels and NCIE-009 step-up matrix`
- W16-D10 selection: `A — explicit-expiry contracts with no default duration`
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`
- Decision date: `2026-09-19`
- Conditions: `None`
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-19-014`

The decision is recorded in `implementation/decisions/NCIE_WBS16_OWNER_DECISION_2026-09-19-014.md`. The required second authorization was subsequently supplied as `NCIE-WBS16-OWNER-DECISION-2026-09-19-015`, releasing the exact provider-neutral WP-003 implementation scope while preserving every operational exclusion.

## 12. Source traceability and VPF boundary

- NCIE-009 Chapter 3, Table 4 and `HR9-3-1`.
- NCIE-009 Chapter 4, Table 6 and `HR9-4-1`.
- NCIE-009 Chapter 5, Table 7 and `HR9-5-1`.
- NCIE-009 Chapter 10, Table 17 and `HR9-10-1`.
- NCIE-009 Chapter 27 Blocking-scope register.
- NCIE-005 protected-identity/voice boundary.
- NCIE-006/007 current-authorization and runtime-identity boundaries.
- NCIE-008 Human-primary authority and segregation-of-duties rules.
- WBS-16 decisions `...-008` through `...-014` and the WP-001/WP-002 handovers.

VPF is applied behaviorally to Human-primary authority, identity dignity/non-substitution, consent, least privilege, explainability, protected-value minimization, provenance, African data residency and deny-by-default cross-border transfer. No VPF runtime, validator, signature, ledger, credential service, residency enforcement or accreditation is claimed to have executed.
