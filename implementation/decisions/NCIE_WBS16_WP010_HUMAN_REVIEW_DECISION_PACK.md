# NCIE WBS-16-WP-010 Human Review Decision Pack

Status: `DECIDED — W16-D30-A THROUGH W16-D34-A; ARCHITECTURE APPROVED / IMPLEMENTATION NOT AUTHORIZED`

Prepared: `2026-09-25`

Decided: `2026-09-25`

Decision evidence: `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`

Work package: `WBS-16-WP-010 — Security Verification Handover and WBS-16 Implementation Closure`

Decision scope:

- `HR9-26-1` — test-acceptance authority, tester/verifier independence, acceptance/sign-off boundaries and the nine NCIE-009 security test classes;
- `HR9-27-1` — complete disposition of every Blocking and Non-Blocking HR9 item;
- `HR9-1-1` / `HR8-10-1` — confirmation of the recorded security-architecture and WBS-16 implementation-closure authority;
- `HR9-28-1` — validation that the approved upstream skeletal-baseline resolution remains valid; and
- the separate final Human decision required after WP-010 implementation and evidence.

This pack records architecture decisions only. It does not implement WP-010, execute an NCIE-016 test, create institutional Evidence or a Finding, assign a tester/verifier/acceptor, accept residual risk, accredit security, close WBS-16, authorize a downstream workstream, deploy anything or authorize go-live.

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

## 1. Source-grounded findings

### 1.1 NCIE-009 Chapter 26

NCIE-009 §26.1 specifies exactly nine mandatory security test classes:

1. `SEC-T1 — IAM Bypass`: Chapters 5–6; authentication/authorization cannot be bypassed or confused-deputy'd.
2. `SEC-T2 — Privilege Escalation`: Chapters 8–9; ordinary/emergency elevation cannot exceed its scoped, time-boxed grant.
3. `SEC-T3 — Cross-Context Leakage`: Chapter 17; retrieval/Context isolation across User/Room/Investigation boundaries holds under adversarial query.
4. `SEC-T4 — Sandbox Escape`: Chapter 14; the Agent Runtime sandbox boundary cannot be breached from within a Run.
5. `SEC-T5 — Prompt Injection`: Chapter 17 and NCIE-007 Chapter 25; untrusted content cannot become system/policy authority.
6. `SEC-T6 — DLP Bypass`: Chapter 18; classification/DLP controls hold across all five data paths in NCIE-009 Table 25.
7. `SEC-T7 — Tool Misuse`: Chapter 16; Tool invocation cannot proceed without current actor/action/target authorization.
8. `SEC-T8 — Recovery/Revocation Failure`: Chapters 10, 22 and 25; revoked credentials and restored state cannot reactivate stale authority.
9. `SEC-T9 — Supply-Chain Compromise`: Chapter 23; unverified or tampered artifacts are quarantined rather than deployed.

NCIE-009 marks every class `TEST SPECIFIED`. It states `TEST SPECIFIED ≠ TEST EXECUTED`, assigns the Accountable Authority Class and Security Test Owner as `to be assigned`, and hands detailed test-case authoring, automation and execution to NCIE-016. `HR9-26-1` remains Blocking until the test acceptance authority, tester independence and required classes are confirmed.

### 1.2 NCIE-016 verification boundary

NCIE-016 owns detailed test-case design, controlled execution governance, Requirements Traceability Matrix, result/evidence model and acceptance/sign-off matrix. It specifies:

- verification, validation and acceptance are distinct;
- executor, witness, reviewer and approver are distinct roles whose required independence scales with risk;
- a security or recovery test requires an independent reviewer;
- the executor is never an approver merely because they ran the test;
- specification prose and local implementation evidence cannot be represented as controlled execution, PASS, validation or acceptance; and
- security-test independence/acceptance (`HR16-19-1`), execution independence/sign-off (`HR16-31-1`) and final/conditional acceptance authority (`HR16-32-1`) remain open Human decisions.

No controlled source assigns the NCIE-016 Security Test Owner, independent tester, independent verifier, witness, acceptance authority, security accreditor or final/conditional acceptance authority. WP-010 must not invent them.

### 1.3 Existing WBS-16 authority and closure boundary

`NCIE-WBS16-OWNER-DECISION-2026-09-19-011` recorded W16-D5-A and W16-D6-A. For the scoped NCIE-009/WBS-16 development target, W16-D5-A records the Project Owner as:

- chapter-level security-architecture sign-off authority;
- acceptance authority for NCIE-009 as a development specification; and
- WBS-16 implementation-completion closure authority.

The same decision requires applicable evidence and a review record from a qualified Human Security Architecture Reviewer who is not the author/implementer and has no material conflict. It expressly leaves NCIE-016 test acceptance, security accreditation, production risk acceptance, operational releases and go-live separate and unassigned.

The controlled WBS-16 completion criteria require a separate Human decision approving or rejecting the completion report. Implementation authority for WP-010 cannot itself satisfy that final closure gate.

### 1.4 HR9-28-1 skeletal baseline

NCIE-009 records `HR9-28-1` as `RESOLVED BY UPSTREAM BASELINE (Non-Blocking)`: the approved NCIE-009 Skeletal v0.1 and its production directive authorized controlled full expansion. Review of WP-001 through WP-009 found subordinate provider-neutral implementations and explicit deferrals; no package added, removed, merged, split or renumbered an NCIE-009 chapter or changed the skeletal architecture. The existing resolution therefore remains valid. A new Human baseline decision is required only if a material controlled architecture change is identified.

## 2. Mandatory state and authority separation

The following states must never be collapsed:

`TEST SPECIFIED ≠ LOCALLY IMPLEMENTATION-TESTED ≠ CONTROLLED NCIE-016 TEST EXECUTED ≠ INDEPENDENTLY VERIFIED ≠ ACCEPTED`.

`LOCAL TEST PASS ≠ INDEPENDENT VERIFICATION ≠ SECURITY ACCREDITATION ≠ CONTROLLED ACCEPTANCE ≠ DEPLOYMENT ≠ GO-LIVE`.

The pack uses these exact states:

| State | Meaning | Does not establish |
|---|---|---|
| `TEST SPECIFIED` | A controlled source states what must be tested | Implementation, execution, pass or acceptance |
| `LOCALLY IMPLEMENTATION-TESTED` | Deterministic local tests exercised the bounded reference implementation | Controlled environment execution, independence, accreditation or acceptance |
| `CONTROLLED NCIE-016 TEST PENDING` | NCIE-016 test design/execution, environment, tools, data and authorities remain outstanding | Failure; it records that controlled execution has not occurred |
| `INDEPENDENTLY VERIFIED` | A qualified, authorized and independent verifier has reviewed controlled results | Accreditation, institutional acceptance, deployment or go-live |
| `ACCEPTED` | The assigned Human/institutional acceptance authority has issued a current, scoped decision | Deployment or go-live unless separately authorized |

Current WP-010 preparation may use only the first three states. No item is `INDEPENDENTLY VERIFIED` or `ACCEPTED`.

## 3. Decision W16-D30 — HR9-26-1 security-test authority, independence and nine test classes

### Option A — Provider-neutral verification-handover contracts with all controlled roles unassigned

Approve:

- the exact nine NCIE-009 test classes `SEC-T1` through `SEC-T9`, without addition, deletion, renaming or false execution claims;
- immutable test-specification, local-coverage, controlled-test-prerequisite, test-state and handover metadata;
- distinct interfaces for test specifier, local implementer/tester, controlled NCIE-016 executor, witness, independent verifier/reviewer, security accreditor and acceptance authority;
- a prohibition on generator, author, implementer or producing Agent self-verification/self-approval where independence is required;
- empty controlled registries for tester assignments, verifier assignments, witnesses, environments, tools, products, data sets/corpora, test thresholds, acceptance criteria, accreditation authorities and acceptance authorities;
- fail-closed state evaluation: missing, stale, conflicted, self-reviewed, unqualified or unassigned authority can never yield `INDEPENDENTLY VERIFIED` or `ACCEPTED`; and
- handover of controlled case design, adversarial execution, results, institutional Evidence and sign-off to NCIE-016/WBS-24.

Local WP-001 through WP-009 tests may be mapped as `LOCALLY IMPLEMENTATION-TESTED` only for the reference contracts they actually exercise. They cannot be relabelled as execution or success of the NCIE-009 test class in a controlled environment.

Implications:

- WP-010 can prove traceability and state separation without selecting a test product or creating an acceptance authority.
- All nine controlled test classes remain `CONTROLLED NCIE-016 TEST PENDING`.
- No controlled test can execute and no result can be independently verified or accepted through WP-010.
- NCIE-016 `HR16-19-1`, `HR16-31-1` and `HR16-32-1` remain downstream gates.

### Option B — Institution-supplied controlled testing and acceptance model

The Project Owner supplies or references the exact:

- NCIE-016 Security Test Owner and Accountable test-acceptance authority;
- executor, witness, independent verifier/reviewer, accreditor and final/conditional acceptance authority;
- qualifications, conflicts, segregation-of-duties and deputisation rules;
- controlled environments, security-testing tools, scanners, corpora, fixtures and data classes;
- pass/fail/block criteria, severity/defect thresholds, retest and exception rules;
- Evidence/custody system, destinations, retention, residency and cross-border boundaries; and
- effective dates, expiry, revocation and change-control process.

Implication: these assignments could support later NCIE-016/WBS-24 preparation and execution under separate authority. They still would not authorize WP-010 to execute a controlled test, accredit security or accept WBS-16.

### Option C — Knowing deferral

Keep `HR9-26-1` open. The nine classes remain `TEST SPECIFIED`; local implementation tests retain their existing status; every controlled test, independent-verification and acceptance state remains pending. WP-010 implementation and WBS-16 implementation closure remain blocked.

### Recommendation

Recorded selection: `W16-D30: A` under `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`.

It preserves the exact source taxonomy, tester/verifier independence and Human-primary acceptance while avoiding fabricated authorities, products, environments, thresholds or execution claims.

## 4. SEC-T1 through SEC-T9 handover matrix

All authorities and operational prerequisites named below remain `UNASSIGNED / UNSPECIFIED`. The “local tests” column identifies implementation evidence, not institutional Evidence and not controlled NCIE-016 execution.

| Test | Source requirement | Implemented control domains | Existing local implementation tests | Remaining controlled/adversarial requirement | Independent roles required | Environment/tool/data prerequisites | Acceptance authority | Current state |
|---|---|---|---|---|---|---|---|---|
| `SEC-T1` IAM Bypass | NCIE-009 Ch.5–6: authentication/authorization cannot be bypassed or confused-deputy'd | WP-001 four-layer deny-by-default authorization; WP-003 issuer/proofing/assurance/session controls; WP-004 mappings/delegation controls | `test_decision_requires_all_four_dimensions`; `test_missing_and_error_decisions_fail_closed`; `test_unbound_issuer_cannot_issue_a_live_session`; stale/mismatched mapping and delegation tests | Attempt bypass and confused-deputy paths through a composed, controlled identity/authentication/authorization deployment | Independent security executor and verifier; executor/implementer cannot accept | Controlled IAM stack, identity fixtures, attack cases and instrumentation — all unspecified | NCIE-016 test acceptance authority — unassigned | `TEST SPECIFIED`; `LOCALLY IMPLEMENTATION-TESTED`; `CONTROLLED NCIE-016 TEST PENDING` |
| `SEC-T2` Privilege Escalation | NCIE-009 Ch.8–9: ordinary/emergency elevation cannot exceed scoped, time-boxed grant | WP-004 privilege, emergency eligibility, expiry, revocation, containment and post-event review contracts | unassigned privilege authority; negative privilege paths; emergency trigger/containment; auto-expiry/revocation tests | Exercise horizontal/vertical escalation, grant reuse, expiry, revocation, nested delegation and break-glass abuse against operational PAM controls | Independent executor, witness/reviewer and verifier | Controlled PAM/IAM, time source, session fixtures, audit capture and attack corpus — unspecified | NCIE-016/security acceptance authority — unassigned | `TEST SPECIFIED`; `LOCALLY IMPLEMENTATION-TESTED`; `CONTROLLED NCIE-016 TEST PENDING` |
| `SEC-T3` Cross-Context Leakage | NCIE-009 Ch.17: User/Room/Investigation isolation under adversarial query | WP-006 eight context classes, empty exception registry and no retrieval/transfer; WP-007 disclosure controls | empty context registry denies; current authorization required; revoked/expired exception denies; same-context boundary has no retrieval path | Adversarial semantic retrieval, cache, Memory, inference and mixed-authority leakage testing across real configured context stores | Independent executor and verifier with privacy/security review | Controlled Context/Memory/retrieval stack, synthetic representative corpus, isolation instrumentation — unspecified | NCIE-016 test acceptance authority — unassigned | `TEST SPECIFIED`; `LOCALLY IMPLEMENTATION-TESTED`; `CONTROLLED NCIE-016 TEST PENDING` |
| `SEC-T4` Sandbox Escape | NCIE-009 Ch.14: Agent Runtime sandbox cannot be breached from a Run | WP-006 zero Agent activation/execution, symbolic resource ceilings, generated-code quarantine and no network capability | missing primitive denies; capability flags rejected; generated-code operation flags rejected; no route/Tool/transfer capability | Execute adversarial escape, resource abuse, filesystem/process/network boundary and persistence tests against an approved Agent runtime sandbox | Independent security executor/verifier; implementer cannot self-verify | Approved sandbox/runtime, host isolation, monitoring, escape corpus and safe test environment — all unspecified | NCIE-016 test acceptance/accreditation authority — unassigned | `TEST SPECIFIED`; local **contract boundary** implementation-tested; `CONTROLLED NCIE-016 TEST PENDING` |
| `SEC-T5` Prompt Injection | NCIE-009 Ch.17 and NCIE-007 Ch.25: untrusted content cannot become authority | WP-006 untrusted-origin semantics; WP-008 false-authority detection paths; WP-009 artifact/recovery state protection | every untrusted origin has no instruction authority; prompt injection cannot change detection, artifact or recovery state | Execute direct/indirect/multistage injection, retrieval poisoning, Tool-routing and authority-forgery corpus against an approved Agent/model stack | Independent adversarial tester and verifier; corpus producer cannot be sole approver | Approved model/Agent/runtime, controlled corpus, Tool mocks, telemetry and data controls — unspecified | NCIE-016 test acceptance authority — unassigned | `TEST SPECIFIED`; `LOCALLY IMPLEMENTATION-TESTED`; `CONTROLLED NCIE-016 TEST PENDING` |
| `SEC-T6` DLP Bypass | NCIE-009 Ch.18/Table 25: controls hold across all five paths | WP-007 five DLP paths, classification floor, no-output/no-reveal boundaries and empty channel/destination registries | exact five paths; empty DLP registry denies; expired/revoked disclosure denies; unassigned authority denies; protected-value/no-output tests | Test export, API, display, Agent/Tool handoff and protected-identity reveal paths with encoding, inference, aggregation and channel-bypass attacks | Independent security/privacy executor and verifier | Approved DLP paths/product if selected, minimized synthetic data corpus, channel fixtures, privacy controls — unspecified | NCIE-016 plus assigned privacy/security acceptance authority — unassigned | `TEST SPECIFIED`; `LOCALLY IMPLEMENTATION-TESTED`; `CONTROLLED NCIE-016 TEST PENDING` |
| `SEC-T7` Tool Misuse | NCIE-009 Ch.16: no invocation without current actor/action/target authorization | WP-006 four Tool classes, empty registry, high-risk predicate, no invocation/network/external destination | empty Tool registry denies; current exact authorization required; high-disclosure approval required; synthetic eligible Tool still cannot invoke | Exercise confused deputy, argument substitution, target drift, replay, chained Tool, connector and external-system misuse against approved Tools | Independent executor/verifier; Tool owner consulted but cannot self-accept | Approved Tool/connector sandbox, mocks, credentials scoped for testing, targets and telemetry — unspecified | NCIE-016 test acceptance authority — unassigned | `TEST SPECIFIED`; `LOCALLY IMPLEMENTATION-TESTED`; `CONTROLLED NCIE-016 TEST PENDING` |
| `SEC-T8` Recovery/Revocation Failure | NCIE-009 Ch.10, 22, 25: restored state cannot reactivate stale authority | WP-003 revocation/reproofing; WP-008 recovery handoff; WP-009 quarantine, reconciliation and non-restoration of stale state | recovery invalidates old sessions; revoked/expired sessions fail closed; recovery cannot authorize; reconciliation preserves current revocation/restriction/deletion/classification/security state | Execute revocation propagation, credential/session invalidation, backup/restore, failover and reconciliation against an approved recovery environment | Independent recovery/security executor, witness and verifier | Approved identity/session/recovery platforms, known-good fixtures, snapshots, time source and isolated environment — unspecified | NCIE-016 recovery/security acceptance authority — unassigned | `TEST SPECIFIED`; `LOCALLY IMPLEMENTATION-TESTED`; `CONTROLLED NCIE-016 TEST PENDING` |
| `SEC-T9` Supply-Chain Compromise | NCIE-009 Ch.23: unverified/tampered artifacts are quarantined, not deployed | WP-006 generated-code quarantine; WP-009 provenance/version/integrity, review, quarantine, revocation and no-artifact-action boundaries | unverified/version-substituted/stale artifacts quarantined; generated code inherits quarantine; producer/implementer cannot be independent reviewer; no promotion/deployment methods | Tamper, provenance substitution, dependency/build compromise, signature/SBOM mismatch and revocation tests across approved repository/CI-CD/promotion controls | Independent supply-chain/security tester and verifier | Approved repository, build/CI-CD, signing/SBOM/scanner tools, test artifacts and isolated promotion target — unspecified | NCIE-016 supply-chain/security acceptance authority — unassigned | `TEST SPECIFIED`; `LOCALLY IMPLEMENTATION-TESTED`; `CONTROLLED NCIE-016 TEST PENDING` |

No row may advance to `INDEPENDENTLY VERIFIED` or `ACCEPTED` without separately assigned current authorities and controlled NCIE-016 evidence.

## 5. Decision W16-D31 — HR9-27-1 complete HR9 disposition

### Option A — Approve the complete disposition register with explicit downstream gates

Approve the register in §5.1 as the complete WP-010 disposition of all 28 HR9 items. “Resolved” or “implemented” applies only to the approved provider-neutral development/contract architecture. It does not convert an explicitly deferred operational assignment into approval.

Implications:

- no silence is treated as approval;
- each operational deferral retains an owner class/downstream gate and fail-closed interim behavior;
- `HR9-26-1` proceeds only under W16-D30-A;
- `HR9-27-1` is resolved for WBS-16 implementation-closure preparation, not for approval of NCIE-009 v1.0 as a controlled document; and
- the final WBS-16 closure decision remains separate.

### Option B — Return specified dispositions for correction

The Project Owner identifies each row to amend and supplies the corrected state, exact scope, accountable owner/downstream gate and interim behavior. Unchanged rows remain as recorded. WP-010 implementation remains blocked until the corrections are complete and non-conflicting.

Implication: only the identified rows may change; no omitted row, operational authority or capability is inferred, and the current deny/no-capability state continues.

### Option C — Knowing deferral

Keep `HR9-27-1` open. Every unresolved authority/product/threshold remains unavailable and fails closed. WP-010 implementation and WBS-16 implementation closure remain blocked.

Implication: WBS-16 remains `IN PROGRESS`; neither the existing local evidence nor silence resolves the consolidated register.

### Recommendation

Recorded selection: `W16-D31: A` under `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`, consistent with the existing decisions resolving the contract-level architecture through WP-009 while preserving every operational assignment and downstream dependency that the sources do not supply.

### 5.1 Complete HR9 disposition register

| HR item | Source classification | Current disposition | Controlled basis | Owner/downstream gate still required | Fail-closed interim behavior |
|---|---|---|---|---|---|
| `HR9-1-1` / `HR8-10-1` | Blocking | `RESOLVED` for NCIE-009/WBS-16 development by W16-D5-A; final closure act still pending | `...-011`; WP-002 implemented | Qualified independent Human Security Architecture Reviewer record, then separate Project Owner closure decision; NCIE-016 acceptance/accreditation remain separate | No final closure, verification, accreditation or acceptance claim without the required records |
| `HR9-2-1` | Blocking | `RESOLVED / IMPLEMENTED` for conservative development risk posture | W16-D6-A; WP-002 | Production risk/exception authority and operational assessment remain unassigned | No silent risk acceptance; unknown/out-of-appetite state denies or stops |
| `HR9-3-1` | Blocking | `RESOLVED FOR CONTRACT ARCHITECTURE / IMPLEMENTED`; provider binding explicitly deferred | W16-D2-A and D7-A; WP-001/WP-003 | Institutional IAM/identity owner and authoritative providers; WBS-23 operational integration | Unbound source authenticates no principal; zero live identity capability |
| `HR9-4-1` | Blocking | `RESOLVED FOR SYMBOLIC CONTRACTS / IMPLEMENTED`; proofing strength and enrollment holders deferred | W16-D8-A; WP-003 | Institutional enrollment/proofing authority, providers and criteria | No proofing/enrollment or verified identity when authority/criteria are absent |
| `HR9-5-1` | Blocking | `RESOLVED FOR SYMBOLIC ASSURANCE / IMPLEMENTED`; factors, triggers and thresholds deferred | W16-D9-A; WP-003 | IAM/security owner; operational factors, levels and step-up triggers | Assurance never creates authorization; unspecified trigger/factor denies operational use |
| `HR9-6-1` | Blocking | `RESOLVED FOR FOUR-LAYER MODEL / IMPLEMENTED`; institutional mappings deferred | W16-D3-A and D11-A; WP-001/WP-004 | Institutional authorization owner and approved role/attribute/action/purpose mappings | Empty registry means zero grants and deny |
| `HR9-7-1` | Blocking | `RESOLVED / IMPLEMENTED` as four contract-eligible delegation classes; activation deferred | W16-D12-A; WP-004 | Delegation authority and exact delegation records | No active delegation; missing/stale/revoked scope denies |
| `HR9-8-1` | Blocking | `RESOLVED / IMPLEMENTED` as three privilege classes; approvers/holders deferred | W16-D13-A; WP-004 | Privileged-access authority/PAM owner; WBS-23 operational controls | No privilege assignment or elevation |
| `HR9-9-1` | Blocking | `RESOLVED / IMPLEMENTED` as three emergency classes; eligibility/activation deferred | W16-D14-A; WP-004 | Incident/emergency authority, eligible triggers and review owner | No break-glass eligibility or activation |
| `HR9-10-1` | Blocking | `RESOLVED FOR EXPLICIT-EXPIRY CONTRACTS / IMPLEMENTED`; durations/issuers/products deferred | W16-D10-A; WP-003 | IAM/session owner and credential/session provider | No issued credential/session; expired/revoked/unbound state denies |
| `HR9-11-1` | Blocking | `RESOLVED FOR OPAQUE CONTRACTS / IMPLEMENTED`; custodians/exceptions/products deferred | W16-D15-A; WP-005 | Secrets/key authority and WBS-23 KMS/HSM/secret infrastructure | No protected material, custody act or exception; prohibited surfaces deny |
| `HR9-12-1` | Non-Blocking | `RESOLVED FOR CONCEPTUAL POLICY / IMPLEMENTED`; algorithms, parameters and products explicitly deferred | W16-D16-A; WP-005 | Cryptographic policy authority and WBS-23 implementation | Empty crypto-policy registry denies; no cryptographic execution claim |
| `HR9-13-1` | Blocking | `RESOLVED FOR LOGICAL ZONES/EGRESS / IMPLEMENTED`; routes, destinations and infrastructure deferred | W16-D17-A; WP-005 | Network/security authority and WBS-23 | Empty egress registry, no destination/route/network capability, cross-border deny |
| `HR9-14-1` | Blocking | `RESOLVED FOR ENVELOPES/QUARANTINE / IMPLEMENTED`; runtime, thresholds, reviewers and activation deferred | W16-D18-A; WP-006 | Agent Factory/security owner, WBS-23 runtime and independent review | Zero Agent capability; generated executable code quarantined `NOT_APPROVED_FOR_EXECUTION` |
| `HR9-15-1` | Blocking | `RESOLVED FOR ELIGIBILITY CONTRACTS / IMPLEMENTED`; providers/models/routes/data combinations deferred | W16-D19-A; WP-006 | Provider/model security, privacy/residency authority and WBS-23 | Empty registry; zero routes; governed/external/cross-border use denied |
| `HR9-16-1` | Blocking | `RESOLVED` as four Tool classes / `IMPLEMENTED`; registrations/approvals deferred | W16-D20-A; WP-006 | Tool/connector owners, approval authorities and WBS-23 integration | Zero registered or invokable Tools |
| `HR9-17-1` | Blocking | `RESOLVED FOR STRICT ISOLATION / IMPLEMENTED`; exceptions/transfers deferred | W16-D21-A; WP-006 | Context/Memory, privacy and residency authorities | Empty exception registry; zero retrieval/transfer capability |
| `HR9-18-1` | Blocking | `RESOLVED FOR FIVE PATHS/CONTRACTS / IMPLEMENTED`; DLP policies, channels, authorities and operations deferred | W16-D22-A; WP-007 | Privacy/security owner and WBS-23 DLP operations | Empty registries; no output/disclosure/channel/destination |
| `HR9-19-1` | Blocking | `RESOLVED FOR ACCESS/ESCALATION CONTRACTS / IMPLEMENTED`; real identity classes/authority deferred | W16-D23-A; WP-007 | Privacy/protected-identity authority and applicable legal/consent owner | No Protected Reveal or real protected-identity processing; Human decision required |
| `HR9-20-1` | Non-Blocking | `RESOLVED FOR METADATA CONTRACTS / IMPLEMENTED`; access, retention/legal hold and stores downstream-assigned | W16-D24-A; WP-008 | WBS-20 canonical audit/Evidence/custody; WBS-23 operational logging; policy authorities | Eleven relevant registries remain empty; no persistent log/audit/Evidence store or period |
| `HR9-21-1` | Non-Blocking | `RESOLVED FOR FIVE DETECTION CATEGORIES / IMPLEMENTED`; monitoring owner, severity and routes deferred | W16-D25-A; WP-008 | WBS-23 monitoring/SIEM; severity/escalation authorities | No monitor/poll/stream/correlation or alert/page; symbolic severity creates no authority |
| `HR9-22-1` | Blocking | `RESOLVED FOR INCIDENT-CONTROL CONTRACTS / IMPLEMENTED`; command, notification and containment deferred | W16-D26-A; WP-008 | WBS-23 incident operations/runbooks and assigned command/notification/containment authorities | No incident declaration/command/send/page/containment/recovery execution |
| `HR9-23-1` | Blocking | `RESOLVED FOR ARTIFACT CONTRACTS / IMPLEMENTED`; acceptance/repository/promotion/deployment downstream-assigned | W16-D27-A; WP-009 | WBS-23 repository/CI-CD/operations and NCIE-016 independent review | Unverified/compromised/revoked/stale artifacts quarantined; zero artifact action |
| `HR9-24-1` | Blocking | `RESOLVED FOR VULNERABILITY/EXCEPTION CONTRACTS / IMPLEMENTED`; severity, deadlines, remediation and risk authority deferred | W16-D28-A; WP-009 | Vulnerability/risk authorities, WBS-23 operations, NCIE-016 verification | No scan/patch/remediation/exception/risk acceptance/security acceptance |
| `HR9-25-1` | Blocking | `RESOLVED FOR RECOVERY CONTRACTS / IMPLEMENTED`; recovery infrastructure and acceptance downstream-assigned | W16-D29-A; WP-009 | WBS-23 recovery infrastructure/runbooks and NCIE-016 independent recovery verification/acceptance | Unknown/unverifiable state quarantined; no backup/restore/recovery/restoration/reauthorization/reinstatement |
| `HR9-26-1` | Blocking | `RESOLVED FOR PROVIDER-NEUTRAL HANDOVER`; implementation and all controlled execution/verification/acceptance remain pending | W16-D30-A under `...-035` | NCIE-016 `HR16-19-1`, `HR16-31-1`, `HR16-32-1`; WBS-24 | Nine tests remain specified/local-only; controlled execution/verification/acceptance unavailable |
| `HR9-27-1` | Blocking | `RESOLVED` for the complete twenty-eight-item WBS-16 disposition register | W16-D31-A under `...-035` | WP-010 implementation report, independent Human review and final Project Owner closure decision remain later gates | No silence equals approval; WP-010 implementation and closure remain unauthorized |
| `HR9-28-1` | Non-Blocking | `RESOLVED BY UPSTREAM BASELINE`; reviewed and still valid | Approved NCIE-009 Skeletal v0.1 and directive | New Human decision only upon identified material architecture change | If validity becomes uncertain, stop WP-010 and retain current deny/no-capability state |

## 6. Decision W16-D32 — confirm HR9-1-1 / HR8-10-1 scoped closure authority

### Option A — Confirm W16-D5-A remains current and require its independent-review input

Confirm that `NCIE-WBS16-OWNER-DECISION-2026-09-19-011` remains the controlling development-stage authority:

- Project Owner / Clive Ebo Barton-Odro remains the scoped WBS-16 implementation-completion closure authority;
- a qualified Human Security Architecture Reviewer, independent of the author/implementer and free of material conflict, must produce the required review record before final closure;
- Codex remains Responsible implementer only and cannot approve, independently verify, accredit, accept or close its own work;
- every sign-off remains target/scope/version/time bound; and
- NCIE-016 test acceptance, accreditation, production acceptance, deployment and go-live remain separate and unassigned.

Implication: WP-010 may later prepare an implementation-closure recommendation, but the Project Owner cannot issue final closure until the required independent Human review record and WP-010 evidence exist.

### Option B — Amend the scoped authority model

Supply the exact replacement Accountable authority, qualified independent reviewer requirements, target/scope/version, effective time, expiry/revocation, conflict rules and transition treatment. Until the amendment is complete and consistent, the existing model remains controlling and no final closure occurs.

Implication: a material amendment requires a new, exact Human authority record and corresponding WP-010 traceability updates; this pack cannot infer the replacement.

### Option C — Defer confirmation

Do not confirm or amend W16-D5-A. WP-010 implementation and final WBS-16 closure remain blocked; no substitute authority may be inferred.

Implication: existing WP-001 through WP-009 controls remain intact, but no implementation-closure recommendation may proceed.

### Recommendation

Recorded selection: `W16-D32: A` under `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`. No controlled source shows revocation, expiry, conflict or material change to W16-D5-A, and its independent-review requirement preserves segregation of duties.

## 7. Decision W16-D33 — HR9-28-1 skeletal-baseline validity

### Option A — Confirm the existing upstream resolution remains valid

Record that WP-001 through WP-009 did not invalidate the approved NCIE-009 skeletal structure. No new baseline approval is required. Any later material chapter/scope/architecture change triggers a stop and new Human review.

Implication: WP-010 may rely on the existing skeletal baseline without manufacturing a redundant approval decision.

### Option B — Identify a material invalidating architecture change

Record the exact changed chapter, controlled source, version, contradiction and impact. Stop affected WP-010 preparation/implementation and return for a new Human skeletal-baseline decision before proceeding.

Implication: the affected traceability and closure scope remains blocked until the new baseline decision is recorded and predecessor impacts are reconciled.

### Option C — Defer the validity determination

Treat the baseline as unconfirmed for WP-010. Preserve all implemented deny/no-capability boundaries, but do not implement WP-010 or recommend WBS-16 closure.

Implication: no architecture is reversed, but no reliance on `HR9-28-1` is permitted for closure.

### Recommendation

Recorded selection: `W16-D33: A` under `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`. The controlled record shows subordinate implementation and explicit deferral, not a change to the NCIE-009 skeletal architecture.

## 8. Decision W16-D34 — final Human WBS-16 closure gate

### Option A — Require a separate post-implementation closure decision

After separately authorized WP-010 implementation and local evidence, require a new Project Owner decision that:

- identifies the exact WP-010 completion report and source version/commit;
- confirms the qualified independent Human Security Architecture Reviewer record required by W16-D5-A;
- accepts or rejects the implementation-closure recommendation and all stated limitations/deferred items; and
- if approving, uses no status broader than the maximum status in §15.

Implication: implementation authorization, local work completion and final Human closure remain three separate acts; the future result can be approved, rejected or returned with conditions.

### Option B — Treat WP-010 implementation authorization as automatic closure

This would merge authorization to perform work with acceptance of its unknown future result, bypass the required independent-review input and collapse implementation into acceptance.

Implication: this option conflicts with W16-D5-A and the controlled completion criteria and is therefore not recommended.

### Option C — Leave closure indefinitely undecided

WP-010 may be implemented only if separately authorized, but WBS-16 remains `IN PROGRESS` until a later closure decision is requested and issued.

Implication: downstream consumers may use only the bounded implementation artifacts explicitly authorized for them; no WBS-16 closure status exists.

### Recommendation

Recorded selection: `W16-D34: A` under `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`. A separate final Human decision is required by W16-D5-A and controlled completion criterion 20. Option B is not aligned with the existing architecture.

## 9. WP-001 through WP-009 reconciliation

Each row records local implementation evidence only. “Remote verified” means the Git branch hash was checked; it is not independent security verification.

| WP | Human decisions | Implementation authority | Source-release authority | Local evidence / cumulative tests | Released implementation commit | Reconciled state |
|---|---|---|---|---|---|---|
| WP-001 | W16-D1-A–D4-A, `...-008` | `...-009` | `...-010` | `LOCAL-WBS16-WP001-20260918-001`; 40/40 | `9c6b0047c13567b1bf04682b93af8abaaf2672e0` | Work complete, source released, operational IAM absent |
| WP-002 | W16-D5-A–D6-A, `...-011` | `...-012` | `...-013` | `LOCAL-WBS16-WP002-20260919-001`; 52/52 | `9ec291a6044bf8c837da514ed2cb693da0477357` | Work complete, source released, production risk acceptance absent |
| WP-003 | W16-D7-A–D10-A, `...-014` | `...-015` | `...-016` | `LOCAL-WBS16-WP003-20260919-001`; 68/68 | `e271c92f5bb7350dfd4d84fb8c5ab7573456fe3b` | Work complete, source released, provider/live authentication absent |
| WP-004 | W16-D11-A–D14-A, `...-017` | `...-018` | `...-019` | `LOCAL-WBS16-WP004-20260923-001`; 86/86 | `48a25e6751a2c6c51a2e00c124d7c714a9b95499` | Work complete, source released, zero grants/elevations/emergency activation |
| WP-005 | W16-D15-A–D17-A, `...-020` | `...-021` | `...-022` | `LOCAL-WBS16-WP005-20260923-001`; 105/105 | `f098e6e14114b88784db9381624beb3e99916bf4` | Work complete, source released, no secret/crypto/network operation |
| WP-006 | W16-D18-A–D21-A, `...-023` | `...-024` | `...-025` | `LOCAL-WBS16-WP006-20260924-001`; 134/134 | `1cb857ef7bafd6ab5c7ef10f1c6926bf1d8e845b` | Work complete, source released, zero Agent/model/Tool/context capability |
| WP-007 | W16-D22-A–D23-A, `...-026` | `...-027` | `...-028` | `LOCAL-WBS16-WP007-20260924-001`; 172/172 | `72b542ff5b583516862c658fcd8480603d6f2a32` | Work complete, source released, zero disclosure/reveal/transfer |
| WP-008 | W16-D24-A–D26-A, `...-029` | `...-030` | `...-031` | `LOCAL-WBS16-WP008-20260924-001`; 224/224 | `ba126b73eb3dea4fd55cfb59b11e43a42623d33c` | Work complete, source released, zero operational logging/monitoring/incident action |
| WP-009 | W16-D27-A–D29-A, `...-032` | `...-033` | `...-034` | `LOCAL-WBS16-WP009-20260924-001`; 280/280 | `a3a222bea9bf0ed00b82ac4d69d19526eed5b9f4` | Work complete, source released, zero artifact/remediation/recovery action |

No WP-001 through WP-009 decision is changed by this pack. Their empty registries, unassigned authorities, zero-capability boundaries, exclusions and downstream gates remain binding.

## 10. Consolidated traceability model

WP-010 should require one immutable traceability row per controlled requirement using this structure:

`SOURCE REQUIREMENT → HUMAN DECISION → IMPLEMENTATION TARGET → LOCAL TEST → LOCAL EVIDENCE → DEFERRED AUTHORITY → DOWNSTREAM CONSUMER`.

Minimum fields:

| Field | Required content | Fail-closed rule |
|---|---|---|
| Requirement | NCIE document, chapter/table/HR/test ID and controlled version | Missing/ambiguous source means `UNTRACED / HUMAN REVIEW REQUIRED` |
| Human decision | Evidence reference, option, target, scope, version and date | No decision may be inferred from code, test output or silence |
| Implementation | Exact module/document and bounded control domain | Missing target means not implemented |
| Local test | Exact test identifier and asserted boundary | A passing test cannot be broadened beyond what it exercised |
| Evidence | Local run/evidence reference and source commit | Reference is not institutional Evidence or custody |
| Deferred authority | Exact unassigned authority/product/threshold/environment | Omission cannot be interpreted as approval |
| Downstream consumer | WBS-20, WBS-23, NCIE-016/WBS-24 or named Human gate | No downstream action is authorized by the handover |
| State | One of the explicit states in §2 | State transitions require the appropriate separate authority/evidence |

Traceability must be bidirectional: every requirement reaches a disposition, and every implementation/test/evidence item points back to its source and decision.

## 11. WBS-16 completion-criteria review

| # | Controlled criterion | Current preparation finding |
|---|---|---|
| 1 | WP-001–WP-010 locally work complete or expressly reassigned | `BLOCKED` — WP-010 is not implemented |
| 2 | Every package has scope/implementation authority, traceability and local evidence | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY` for WP-001–WP-009; `BLOCKED` for WP-010 |
| 3 | HR9-1-1/HR8-10-1 identifies closure authority | `SATISFIED` by W16-D5-A as confirmed by W16-D32-A under `...-035`; later WP-010 evidence and independent review remain closure prerequisites |
| 4 | HR9-2-1 appetite/threat assumptions approved and traced | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY`; production risk treatment remains unassigned |
| 5 | Every Blocking HR9 item resolved or knowingly deferred with owner/gate/interim behavior | `SATISFIED` for architecture disposition by W16-D31-A under `...-035`; WP-010 implementation and final closure remain pending |
| 6 | Every Non-Blocking HR9 item explicitly dispositioned | `SATISFIED` by W16-D31-A and W16-D33-A under `...-035` |
| 7 | Identity/auth/session/authorization/delegation/privilege/break-glass contracts complete and fail closed | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY` |
| 8 | Provider/source binding approved/implemented or explicitly deferred with no operational claim | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY`; operational binding deferred |
| 9 | No implicit grant path | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY` |
| 10 | Secrets/crypto/network controls implemented at approved layer; infrastructure handed to WBS-23 | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY`; operational layer `DEFERRED TO DOWNSTREAM AUTHORITY` |
| 11 | Agent/model/Tool/Context/DLP/protected-identity controls preserve boundaries | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY` |
| 12 | Logging/detection/incident contracts preserve semantic separation | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY`; operations deferred |
| 13 | Artifact/vulnerability/recovery controls preserve provenance/quarantine/revocation/reconciliation | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY`; operations deferred |
| 14 | Local harnesses cover SEC-T1–T9 intent with NCIE-016 distinction | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY` by §4 mapping; controlled tests pending |
| 15 | Typing/lint/format/compilation/regression/reproducibility pass | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY` through WP-009: 280/280 tests and gates passed; WP-010 rerun pending |
| 16 | Local closure requires no live credential/data/provider/product/infrastructure unless approved | `SATISFIED FOR LOCAL IMPLEMENTATION ONLY` |
| 17 | Consolidated traceability exists | `BLOCKED` — model proposed here; WP-010 artifact not implemented |
| 18 | WBS-20/WBS-23/NCIE-016 handovers are explicit | `BLOCKED` — boundaries proposed here; WP-010 handover artifact not implemented |
| 19 | Completion report lists limitations, residual risks and deferrals | `BLOCKED` — WP-010 completion report not implemented |
| 20 | Separate Human approval of completion report | `REQUIRES HUMAN DECISION` after WP-010, per W16-D34-A recommendation |

No current criterion supports declaring WBS-16 complete.

## 12. Consolidated unresolved/deferred-item register

| Domain | Must remain unassigned/unspecified | Exact downstream owner/gate | Interim behavior |
|---|---|---|---|
| Authority assignments | NCIE-016 testers/verifiers/acceptors; IAM, enrollment, proofing, assurance, authorization, delegation, privileged/break-glass, secrets, crypto, network, Agent/model/Tool, DLP/privacy, logging, severity, incident, artifact, vulnerability/risk and recovery authorities | Applicable competent Human authority; NCIE-008 decision rights; NCIE-016/WBS-24 for test roles | No authority and no capability; no self-approval |
| Provider/product selections | Identity/credential/session providers; secret/KMS/HSM/PKI; crypto products; network/security gateways; Agent/model providers; DLP/SIEM/monitoring/incident products; registries/CI-CD/scanners/SBOM/signing; vulnerability and recovery products | WBS-23 plus separate product/provider decisions and security review | No adapter, route, endpoint, repository, scanner or product activation |
| Operational IAM | Authoritative sources/providers, proofing, factor sets, triggers, durations, mappings, grants, privilege holders and emergency eligibility | IAM/security owners and WBS-23 | Zero live principals/credentials/sessions/grants/elevation |
| Cryptographic policy | Algorithms, key sizes, profiles, certificates, key hierarchy implementation and custodians | Cryptographic authority and WBS-23 | Empty operational policy; no cryptographic execution claim |
| Logging/SIEM | Stores, access, retention/legal hold, sinks, destinations, SIEM product and custody | WBS-20 for canonical audit/Evidence/custody; WBS-23 for operations | Synthetic non-persistent metadata only; no production log store |
| Monitoring/incident operations | Polling/streaming/correlation, rules, severity thresholds, routes, paging, recipients, command, notification and containment rights | WBS-23 operational controls/runbooks and assigned Human authorities | No monitoring, alert delivery, incident declaration or response execution |
| DLP/privacy operations | DLP policies/products, protected-identity sources, legal/consent basis, channels, destinations and exception authorities | Privacy/legal/security authority and WBS-23 | No disclosure, reveal, output, destination or transfer |
| Agent/model/Tool activation | Agent runtimes/ceilings, provider/model routes, Tools/connectors, credentials, endpoints and cross-context exceptions | WBS-23 plus separate security/provider/Tool decisions | Zero Agent execution, routes, Tool invocation or context transfer |
| Artifact/scanner/CI-CD operations | Repositories, builds, signing/SBOM, scanners, gates, quarantine release, promotion/deployment | WBS-23 and NCIE-016 independent review | Quarantine; no acceptance, promotion, deployment or execution |
| Vulnerability governance | Severity taxonomy, thresholds, deadlines, exception duration, remediation authority and risk acceptance | Competent vulnerability/risk authority; WBS-23; NCIE-016 | No scanning/remediation/exception activation/risk acceptance/security acceptance |
| Recovery infrastructure | Backups/snapshots, RPO/RTO, failover, restore, invalidation/rotation and reconciliation execution | WBS-23 recovery infrastructure/runbooks; NCIE-016 recovery verification | Unknown state quarantined; no recovery/restoration/reauthorization/reinstatement |
| Residency/cross-border | Approved regions, destinations, transfer purpose/legal authority and external processors | Competent sovereignty/privacy authority before WBS-23 integration | African data-residency boundary; cross-border deny by default |
| WBS-20 | Institutional Evidence, canonical provenance/audit, custody, retention/legal hold and defensibility | WBS-20 decision/implementation authority | WBS-16 references only; creates no institutional Evidence/Finding |
| WBS-23 | Repositories, CI-CD, scanners, IAM/security products, logging/monitoring/SIEM, patching, incident/recovery infrastructure and runbooks | WBS-23 decision/implementation authority | No infrastructure or operational control activation |
| NCIE-016/WBS-24 | Test design, controlled execution, environments/tools/data, Evidence/results, independent verification and acceptance matrix | `HR16-19-1`, `HR16-31-1`, `HR16-32-1` and other applicable NCIE-016 decisions | All nine controlled security tests pending; no verification/acceptance claim |
| Accreditation | Accreditor, criteria, evidence set, scope and validity | Separately assigned security accreditation authority | Not accredited |
| Controlled acceptance | Final/conditional acceptance authority and criteria | NCIE-016/NCIE-008 controlled acceptance gate | Not accepted |
| Deployment | Environments, release/promotion authority and operational readiness | WBS-23 and separate deployment authority | Not deployed; no production-readiness claim |
| Go-live | Go-live authority, readiness criteria and operational ownership | Separate institutional go-live decision | Not live; no go-live claim |

## 13. Exact downstream handover boundaries

### 13.1 WBS-20 — Evidence, Provenance & Audit

WP-010 may hand over requirement/decision/test/evidence **references**, local run metadata and custody requirements. WBS-20 retains:

- institutional Evidence creation and canonical evidence identifiers;
- authoritative provenance, audit and custody records;
- tamper protection, retention, legal hold, disclosure and defensibility; and
- Evidence/Finding relationship controls.

WP-010 must not create a canonical Evidence store, custody claim, institutional Finding or retention/legal-hold policy.

### 13.2 WBS-23 — DevSecOps, infrastructure and operational controls

WP-010 may hand over interface requirements, empty registries, unresolved products/parameters and fail-closed operational prerequisites. WBS-23 retains:

- identity/security products and operational integrations;
- secret/key, crypto and network infrastructure;
- Agent/model/Tool runtime infrastructure;
- DLP, logging, SIEM, monitoring, alerting, paging and incident operations;
- repositories, builds, CI/CD, signing/SBOM and scanners;
- vulnerability scanning, patching/remediation and operational exceptions; and
- backup, recovery, failover, reconciliation, restoration and runbooks.

The handover grants WBS-23 no implementation or activation authority.

### 13.3 NCIE-016 / WBS-24 — independent testing, verification and acceptance

WP-010 may hand over the nine test-class mappings, local implementation evidence, limitations and controlled prerequisites. NCIE-016/WBS-24 retains:

- detailed controlled test cases and adversarial corpus;
- environment/tool/data selection and control;
- controlled execution and rerun governance;
- witness, executor, reviewer and verifier independence;
- result/evidence and defect governance;
- independent security/recovery/supply-chain verification; and
- the acceptance/sign-off matrix.

WP-010 cannot mark a controlled test executed or passed, claim independent verification, assign acceptance authority, accredit security or accept WBS-16.

## 14. Approved WP-010 non-waivable protections

1. Human-primary authority remains mandatory.
2. `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.
3. The five test states in §2 remain structurally distinct.
4. Local tests are never represented as NCIE-016 controlled execution.
5. Controlled execution is never represented as independent verification without an independent verifier.
6. Independent verification is never represented as accreditation or acceptance.
7. Acceptance is never represented as deployment or go-live.
8. The exact nine SEC-T classes are preserved without false additions, omissions or passes.
9. Generator, Agent, author, implementer or executor cannot self-approve where independence is required.
10. Tester, verifier, accreditor and acceptance authorities remain unassigned unless a separate current Human decision assigns them.
11. Every requirement/decision/implementation/test/evidence mapping is exact, versioned and non-authoritative beyond its scope.
12. Silence, missing evidence or an omitted HR item is never approval.
13. Every deferral names its owner/downstream gate and fail-closed interim behavior.
14. No test product, provider, environment, corpus, threshold or operational assignment is invented.
15. No governed production data, live credentials, external destination or cross-border transfer is used.
16. WP-010 creates no institutional Evidence, Finding, accreditation or acceptance record.
17. WBS-20, WBS-23 and NCIE-016/WBS-24 responsibilities remain segregated.
18. WBS-16 closure requires a separate final Human decision after WP-010 implementation evidence and the required independent Human review record.

## 15. Exact proposed WP-010 implementation scope

Only after explicit W16-D30 through W16-D34 selections and a separate decision naming and releasing WP-010 may implementation include:

- a consolidated, versioned WBS-16 traceability artifact covering WP-001 through WP-010;
- an immutable provider-neutral registry of the exact nine SEC-T specifications and explicit test states;
- mappings from each SEC-T class to existing local tests, limitations and controlled prerequisites;
- empty versioned registries/interfaces for controlled tester, witness, verifier, accreditor and acceptance assignments;
- fail-closed validation preventing state escalation, self-review, unassigned authority and false acceptance claims;
- the complete HR9 disposition and unresolved/deferred-item register;
- explicit WBS-20, WBS-23 and NCIE-016/WBS-24 handover artifacts;
- a reproducible dependency/configuration inventory;
- deterministic standard-library local tests of traceability completeness, exact nine-class preservation, state separation, empty assignments and negative paths;
- cumulative WP-001 through WP-009 regression and existing quality/template gates;
- local implementation evidence clearly labelled non-institutional and non-independent; and
- a WBS-16 implementation-completion report plus a separate final Human closure decision pack.

### Exclusions

WP-010 must not:

- execute any NCIE-016/WBS-24 controlled test or adversarial campaign;
- mark any SEC-T class controlled-executed, passed, independently verified or accepted;
- assign a tester, witness, verifier, accreditor, acceptance authority or downstream operational owner;
- select or activate a test tool, scanner, SIEM, CI/CD, artifact, IAM, DLP, vulnerability, backup/recovery or other product/provider;
- create institutional Evidence, Findings, accreditation or acceptance;
- process governed production data, real credentials, real protected identities or live security events;
- connect to an external system, destination or cross-border path;
- change WP-001 through WP-009 decisions or capabilities;
- implement WBS-20, WBS-23, WBS-24 or any later scope;
- declare WBS-16 complete, production-ready, accredited, accepted, deployed or live; or
- add a dependency, infrastructure or deployment.

### Stop conditions

Stop the affected scope and return for Human decision if:

1. any W16-D30 through W16-D34 selection or separate WP-010 implementation authority is absent, ambiguous or conflicting;
2. the authoritative NCIE repository, branch, predecessor chain or WP-001–WP-009 evidence is missing/inconsistent;
3. a material architecture change may invalidate `HR9-28-1`;
4. the SEC-T taxonomy differs from the exact nine NCIE-009 classes;
5. a local test would be represented as NCIE-016 controlled execution or independent verification;
6. an acceptance, accreditation, deployment or go-live state would be inferred;
7. a tester/verifier/acceptor or operational authority would need to be invented or self-assigned;
8. an unresolved HR9 item lacks exact owner, downstream gate or fail-closed interim behavior;
9. governed/live data, credentials, identities, security events or external systems would be required;
10. a product, provider, environment, threshold, corpus, destination, transfer or dependency must be selected;
11. institutional Evidence or a Finding would be created;
12. a WP-001 through WP-009 decision or zero-capability boundary would be weakened;
13. downstream WBS-20/WBS-23/NCIE-016 work would be implemented or authorized; or
14. any request would close WBS-16 without the separate final Human decision and required independent-review record.

Fallback: `DENY / NO CAPABILITY`.

### Local completion criteria

WP-010 may be reported locally work-complete only when:

1. recorded W16-D30 through W16-D34 selections and a separate implementation release are represented without expansion;
2. all nine SEC-T classes are reproduced exactly once and mapped bidirectionally;
3. all SEC-T states remain `TEST SPECIFIED`, `LOCALLY IMPLEMENTATION-TESTED` where evidence exists, and `CONTROLLED NCIE-016 TEST PENDING`;
4. no row is marked `INDEPENDENTLY VERIFIED` or `ACCEPTED`;
5. every HR9 item has an explicit disposition, owner/downstream gate and interim behavior;
6. every WP-001 through WP-009 decision, implementation authority, local evidence and release commit reconciles without changing its scope;
7. every controlled tester/verifier/accreditor/acceptor registry remains empty and every authority interface unassigned;
8. self-approval, state escalation, missing traceability and false-authority paths fail closed;
9. WBS-20, WBS-23 and NCIE-016/WBS-24 handovers are explicit and non-authorizing;
10. dependency/configuration inventory is reproducible with no new dependency;
11. strict typing, lint, formatting, in-memory compilation, cumulative regression and template verification pass;
12. no governed data, live credential, external system, destination, cross-border transfer, product, infrastructure or deployment is introduced;
13. the completion report states every limitation and deferred item without accreditation/acceptance claims; and
14. the separate final Human closure pack is prepared but not decided by Codex.

## 16. Maximum permissible recommendation

If WP-010 is separately authorized, implemented and all local completion criteria pass, its maximum recommendation is:

`WBS-16 — IMPLEMENTATION COMPLETE / DOWNSTREAM-READY; INDEPENDENT SECURITY VERIFICATION, ACCREDITATION, CONTROLLED ACCEPTANCE AND GO-LIVE PENDING`.

That recommendation must not be represented as:

- production readiness;
- security accreditation;
- successful NCIE-016 verification;
- operational IAM, Zero Trust, DLP, SIEM, monitoring, incident response or recovery;
- controlled acceptance;
- artifact promotion or deployment;
- deployment; or
- go-live.

The status becomes an approved WBS-16 closure status only if the separate final Human decision under W16-D34-A is later issued after the required independent Human Security Architecture Reviewer record. Until then WBS-16 remains `IN PROGRESS`.

## 17. Recorded Project Owner decisions

- `W16-D30: A` — approved provider-neutral SEC-T1–SEC-T9 verification-handover/state contracts, empty assignment registries and zero controlled execution/verification/acceptance capability.
- `W16-D31: A` — approved the complete HR9 disposition register with explicit downstream gates and fail-closed interim behavior.
- `W16-D32: A` — confirmed W16-D5-A remains current, including the independent Human Security Architecture Reviewer prerequisite and separate authority boundaries.
- `W16-D33: A` — confirmed `HR9-28-1` remains resolved by the upstream skeletal baseline because no material invalidating architecture change is present.
- `W16-D34: A` — preserved a separate final Human WBS-16 closure decision after WP-010 implementation evidence and independent-review input.

These selections were recorded under `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`. They approve architecture only and do not authorize WP-010 implementation. A separate explicit implementation decision naming `WBS-16-WP-010 — Security Verification Handover and WBS-16 Implementation Closure` remains required.

## 18. Source traceability and VPF boundary

Primary controlled sources:

- NCIE-009 Chapters 1, 26, 27 and 28; Table 34; `HR9-1-1`, `HR9-26-1`, `HR9-27-1`, `HR9-28-1`;
- NCIE-008 `HR8-10-1` and its decision-right/separation-of-duties architecture;
- NCIE-016 Chapters 2, 19, 31, 32 and 40; `HR16-19-1`, `HR16-31-1`, `HR16-32-1`;
- `implementation/WBS16_REMAINING_SCOPE_AND_COMPLETION_CRITERIA.md`;
- `implementation/NCIE-017_CONTROLLED_IMPLEMENTATION_PLAN.md`;
- WP-001 through WP-009 decision packs, owner decisions, implementation/local-run/source-release evidence and tests; and
- `handoff.md` at repository HEAD `866b6849ecde6bc4f667e8458d6f9c257982ff30` during preparation.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, provenance, consent/dignity, minimization, sovereignty, African data residency and deny-by-default cross-border transfer. No VPF runtime, checksum, signature, certificate, ledger, scheduled audit, PADCA/Omnis service, quarantine action or residency-enforcement service is claimed to have executed.

## 19. Decision record

- Preparation date: `2026-09-25`
- Decision date: `2026-09-25`
- Decision authority: `Project Owner / Clive Ebo Barton-Odro` (user-supplied assertion recorded; not independently verified by Codex)
- Decision evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`
- Recorded selections: `W16-D30-A / W16-D31-A / W16-D32-A / W16-D33-A / W16-D34-A`
- WP-010 implementation authority: `NOT AUTHORIZED`
- WBS-16 closure: `NOT DECLARED`
- Controlled NCIE-016 execution: `NOT PERFORMED`
- Independent verification: `NOT CLAIMED`
- Accreditation: `NOT CLAIMED`
- Controlled acceptance: `NOT CLAIMED`
- Deployment/go-live: `NOT AUTHORIZED`
