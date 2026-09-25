# WBS-16 Remaining Scope and Completion Criteria

Status: `FOR HUMAN REVIEW — PLANNING ONLY; NO FURTHER IMPLEMENTATION AUTHORITY`

Prepared: `2026-09-19`

Current workstream state: `IN PROGRESS — WBS-16-WP-001 THROUGH WP-007 WORK COMPLETE / LOCALLY VERIFIED`

## 1. Current baseline

`WBS-16-WP-001 Security Principal and Authorization Contract Foundation` is locally work-complete under decisions `NCIE-WBS16-OWNER-DECISION-2026-09-18-008` and `...-009`. Its implementation and evidence were pushed under `...-010`.

WP-001 established:

- seven provider-neutral principal/source categories;
- four-layer object, field, action and purpose authorization contracts;
- current, deny-by-default decision semantics;
- a zero-grant reference policy;
- fail-closed enforcement; and
- minimized, non-authoritative security-condition signals.

WP-001 did not select or activate an identity provider, credentials, sessions, roles, permissions, privileged access, secrets, networks, security products, external systems or production controls. W16-D4-A deferred all other HR9 items for WP-001 only; it did not resolve them for WBS-16 completion.

## 2. Required work packages and current disposition

### WBS-16-WP-002 — Security Governance, Risk and Threat Baseline

Status: `WORK COMPLETE — LOCALLY VERIFIED` under implementation authority `NCIE-WBS16-OWNER-DECISION-2026-09-19-012`; implementation commit `9ec291a6044bf8c837da514ed2cb693da0477357` pushed under `...-013`; independent verification, accreditation and acceptance remain pending.

Purpose: establish the accountable security authority, institutional risk appetite, threat assumptions, control ownership and the rules for accepting or deferring security decisions before broader controls are implemented.

Implemented scope:

- security-architecture acceptance and chapter/control-domain sign-off boundaries;
- institutional risk-appetite and threat-assumption register;
- control-owner and exception/risk-acceptance interfaces;
- explicit separation of implementation evidence, security verification, accreditation and acceptance; and
- local governance-contract tests and traceability.

Satisfied decisions:

- `HR9-1-1`, together with its upstream duplicate `HR8-10-1`: acceptance and security-architecture sign-off authority;
- `HR9-2-1`: institutional risk appetite and unresolved threat assumptions; and
- explicit implementation authority for WP-002.

Excluded: accreditation, production risk acceptance, live incident command and security-product selection.

### WBS-16-WP-003 — Identity Lifecycle, Authentication and Session Assurance

Status: `WORK COMPLETE — LOCALLY VERIFIED` under decisions `NCIE-WBS16-OWNER-DECISION-2026-09-19-014` and implementation authority `...-015`; operational IAM, independent verification, accreditation and acceptance remain pending.

Purpose: implement provider-neutral proofing, enrollment/lifecycle, authentication-assurance, step-up, recovery, session and credential-state contracts without silently selecting a provider.

Proposed scope:

- proofing/enrollment/lifecycle state machine and revocation propagation;
- assurance-level and step-up contracts;
- session/credential state, expiry and reauthentication contracts;
- fail-closed recovery and stale-authority rejection; and
- local identity-bypass and recovery/revocation tests.

Satisfied decisions for this increment:

- `HR9-4-1`: proofing strength per applicable identity class and enrollment authority;
- `HR9-5-1`: assurance levels, factor-class policy and step-up triggers;
- `HR9-10-1`: session assurance/expiry policy and credential classes;
- follow-on disposition of `HR9-3-1`: remain provider-neutral or authorize specific source/provider bindings; and
- explicit implementation authority for WP-003 under `...-015`.

Excluded unless separately approved: named provider, live credentials, real users, production sessions and recovery operations.

### WBS-16-WP-004 — Authorization Mapping, Delegation, Privileged and Emergency Access

Status: `WORK COMPLETE — LOCALLY VERIFIED` under architecture decision `NCIE-WBS16-OWNER-DECISION-2026-09-23-017` and implementation authority `...-018`; operational assignment, activation, independent verification, accreditation and acceptance remain pending.

Purpose: extend the WP-001 zero-grant model with approved role/attribute mapping contracts, bounded delegation, privileged-access and break-glass controls while retaining least privilege and current authorization.

Proposed scope:

- versioned role/attribute-to-policy mapping model;
- delegation/effective-principal envelope and non-expansion rules;
- privileged-access request, approval, expiry and revocation contracts;
- break-glass eligibility, trigger, time-box, containment and review contracts; and
- privilege-escalation and stale-delegation negative tests.

Satisfied decisions:

- follow-on `HR9-6-1` decision approving actual institution-specific role/attribute mappings or explicitly retaining zero grants;
- `HR9-7-1`: permitted and prohibited delegation classes;
- `HR9-8-1`: privileged-access classes and approval authority;
- `HR9-9-1`: break-glass authority, eligible emergencies and post-event review rules; and
- explicit implementation authority for WP-004.

Implemented disposition: the versioned mapping registry is empty; all four delegation classes, three privileged-access classes and three emergency classes are contract-defined; unassigned privileged/emergency authority boundaries deny; no role assignment, delegation, privilege or emergency access is populated or activated.

### WBS-16-WP-005 — Secrets, Cryptography and Network Zero-Trust Contracts

Status: `WORK COMPLETE — LOCALLY VERIFIED` under architecture decision `...-020` and implementation authority `...-021`.

Purpose: implement the logical secrets/key, cryptographic-policy and network trust/egress controls required by NCIE-017 §16.2 without selecting infrastructure silently.

Implemented scope:

- opaque protected-reference and non-executing lifecycle/exception contracts;
- key separation and cryptographic-policy metadata;
- network trust-zone, service-boundary and egress-policy contracts;
- deny-by-default exception handling; and
- local secret-leakage, invalid-policy and unauthorized-egress tests.

Satisfied decisions:

- `HR9-11-1`: secrets/key custodial authority and exception policy;
- `HR9-12-1`: provider-neutral protection, hierarchy, separation and agility contracts with concrete cryptographic policy deferred;
- `HR9-13-1`: network trust zones, Agent/external egress classes and exception authority;
- W16-D15-A through W16-D17-A under `NCIE-WBS16-OWNER-DECISION-2026-09-23-020`; and
- explicit implementation authority under `NCIE-WBS16-OWNER-DECISION-2026-09-23-021`.

Excluded unless separately approved: secret manager, KMS/HSM, certificates, live keys, firewall, service mesh, network or cloud deployment.

Implemented disposition: all authority and operational registries are empty; cryptographic concepts contain no algorithms or products; logical zones and egress contracts create no destination, route or connection; no protected material or external/cross-border operation exists.

### WBS-16-WP-006 — Agent, Model, Tool and Context Isolation Security

Purpose: define and enforce provider-neutral security envelopes for Agent generation/runtime, model/provider use, Tool invocation and cross-context access.

Proposed scope:

- Agent Factory ceilings and generated-code review gates;
- runtime/sandbox, resource and egress envelopes;
- provider-security and restricted-data/provider policy contracts;
- high-risk Tool classification and current actor/action/target authorization;
- Context/Memory isolation and governed cross-context exceptions; and
- local sandbox-boundary, Tool-misuse, prompt-injection and cross-context negative tests.

Architecture decisions satisfied under `NCIE-WBS16-OWNER-DECISION-2026-09-24-023`:

- `HR9-14-1`: W16-D18-A, provider-neutral Agent/runtime ceilings, zero activation and prohibited generated-code execution;
- `HR9-15-1`: W16-D19-A, empty provider/model/data-combination registry and zero routes;
- `HR9-16-1`: W16-D20-A, four Tool classes and zero registered/invokable Tools; and
- `HR9-17-1`: W16-D21-A, strict isolation, empty exception registry and zero cross-context transfer.

Implementation authority was subsequently granted by `NCIE-WBS16-OWNER-DECISION-2026-09-24-024`. WP-006 is locally work-complete with 134 cumulative tests and all local quality, compilation and template-verification gates passing. The controlled registries remain empty and every Agent, route, Tool and cross-context capability remains absent.

No Agent, model, Tool, provider or cross-context exception is activated by this package without separate current authorization.

### WBS-16-WP-007 — DLP, Disclosure and Protected-Identity Controls

Purpose: implement classification-aware disclosure prevention and protected-identity access/escalation contracts across approved data paths.

Proposed scope:

- DLP policy classes and disclosure-decision contracts;
- redaction/minimization and output-channel controls;
- protected-identity access and privacy-escalation contracts;
- exception provenance without exposing protected values; and
- local DLP-bypass, mixed-authorization and protected-identity negative tests.

Decision and implementation status:

- `HR9-18-1`: W16-D22-A approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-026`;
- `HR9-19-1`: W16-D23-A approved under the same evidence; and
- explicit implementation authority was granted under `NCIE-WBS16-OWNER-DECISION-2026-09-24-027`.

The decided Human Review Decision Pack is recorded at `implementation/decisions/NCIE_WBS16_WP007_HUMAN_REVIEW_DECISION_PACK.md`. WP-007 is locally work-complete with 172 cumulative tests and all local quality, compilation and template-verification gates passing. All six controlled registries, channels, destinations and operational authorities remain empty or unassigned. No output, disclosure, reveal, real identity processing or cross-border capability exists.

Excluded: live protected identities, production data, disclosure approval or privacy accreditation.

### WBS-16-WP-008 — Security Logging, Detection and Incident-Control Contracts

Purpose: implement the security-event, detection, escalation and incident-control semantics needed for later operational products and runbooks.

Proposed scope:

- minimized security-event schema and access/retention metadata;
- detection/severity/escalation contracts;
- incident-state, containment-right and notification-obligation contracts;
- strict separation of operational signals, Findings, Evidence and Human Decisions; and
- local event-minimization, severity-routing and unauthorized-containment tests.

Decision status:

- `HR9-20-1`: W16-D24-A approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-029`;
- `HR9-21-1`: W16-D25-A approved under the same evidence;
- `HR9-22-1`: W16-D26-A approved under the same evidence;
- the WBS-20 Evidence, WBS-23 observability/infrastructure and NCIE-016 independent-verification boundaries are preserved; and
- exact implementation authority was granted under `NCIE-WBS16-OWNER-DECISION-2026-09-24-030`.

The decided Human Review Decision Pack is recorded at `implementation/decisions/NCIE_WBS16_WP008_HUMAN_REVIEW_DECISION_PACK.md`. WP-008 is locally work-complete with 224 cumulative tests and all local quality, in-memory compilation and template-verification gates passing. All eleven controlled registries, operational authority assignments, retention periods, severity thresholds, recipients, destinations and products remain empty, unassigned or unspecified. No persistent logging, monitoring, alerting, incident declaration, notification or response action is authorized.

Excluded: SIEM/DLP product, persistent audit store, live monitoring, paging, incident command activation or institutional Finding creation.

### WBS-16-WP-009 — Supply Chain, Vulnerability and Security Recovery

Purpose: implement provider-neutral artifact acceptance, remediation/exception and compromised-state recovery controls.

Proposed scope:

- artifact provenance, verification, quarantine and generated-code gate contracts;
- vulnerability/patch/remediation and risk-exception lifecycle;
- compromised backup/state handling and post-recovery reconciliation;
- revocation preservation through restore/recovery; and
- local tamper, unpatched-risk and recovery/revocation negative tests.

Required decisions:

- `HR9-23-1`: artifact-acceptance authority and generated-code security-gate criteria;
- `HR9-24-1`: remediation governance and unpatched-vulnerability risk-acceptance authority;
- `HR9-25-1`: security-recovery acceptance and compromised-state handling;
- downstream boundary with WBS-23 delivery/infrastructure and NCIE-016 testing; and
- explicit implementation authority for WP-009.

Excluded: hosted CI/CD, artifact registry, vulnerability scanner, backup platform, production patching or recovery execution.

The decided Human Review Decision Pack is recorded at `implementation/decisions/NCIE_WBS16_WP009_HUMAN_REVIEW_DECISION_PACK.md`. W16-D27-A through W16-D29-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-032`, the exact zero-capability implementation was released under `...-033`, and controlled source release was authorized under `...-034`. WP-009 is locally work-complete with thirty empty controlled registries, forty-two unassigned authority classes, synthetic metadata and inert no-artifact-action/no-remediation/no-recovery boundaries; 280 cumulative tests pass. All eighteen protections and mandatory semantic separations remain binding. Push execution is pending.

### WBS-16-WP-010 — Security Verification Handover and WBS-16 Closure

Purpose: consolidate traceability, reproduce the complete WBS-16 source scope, map all nine NCIE-009 security test classes, hand controlled execution to NCIE-016 and produce the Human closure report.

Proposed scope:

- cumulative WBS-16 requirement/decision/source/test traceability;
- reproducible dependency and configuration inventory;
- local contract/adversarial harnesses for `SEC-T1` through `SEC-T9`;
- explicit `TEST SPECIFIED`, local implementation-test and controlled NCIE-016 test states;
- unresolved/deferred-item register and downstream handover; and
- WBS-16 completion report and separate Human closure pack.

Required decisions:

- `HR9-26-1`: test-acceptance authority, tester independence and the nine required test classes;
- final `HR9-27-1` disposition for every remaining Blocking and Non-Blocking HR9 item;
- confirmed `HR9-1-1` / `HR8-10-1` WBS-16 closure authority;
- explicit implementation authority for WP-010; and
- a later, separate Human decision approving or rejecting WBS-16 implementation closure.

`HR9-28-1` remains resolved by the approved upstream skeletal baseline and requires no new decision unless the controlled architecture itself changes.

## 3. Controlled sequence

1. WP-002 governance/risk baseline.
2. WP-003 identity/authentication/session assurance.
3. WP-004 authorization mapping/delegation/privileged access.
4. WP-005 secrets/cryptography/network Zero Trust.
5. WP-006 Agent/model/Tool/context isolation.
6. WP-007 DLP/disclosure/protected identity.
7. WP-008 logging/detection/incident controls.
8. WP-009 supply chain/vulnerability/recovery.
9. WP-010 cumulative verification handover and closure report.

WP-004, WP-005 and WP-008 collectively satisfy NCIE-017 §16.2's privileged-access, secrets/network and audit-prerequisite block. No later workstream may consume WBS-16 as an operational security posture until the applicable set is complete and independently verified.

## 4. Cross-cutting Human decisions

In addition to the HR items assigned above, every package requires:

1. explicit scope and implementation authority;
2. a decision whenever provider-neutral contracts would become a named product, provider, tenant, algorithm, infrastructure or live-data integration;
3. an African data-residency and cross-border disposition before any governed identity/security data is sent to an external system;
4. explicit ownership for exceptions, risk acceptance and consequential containment actions;
5. separation-of-duties and independent-review disposition where implementer and verifier could otherwise coincide; and
6. a stop-and-review decision for any new dependency or technology.

No package approval may be inferred from this plan.

## 5. Proposed WBS-16 completion criteria

WBS-16 may be recommended as implementation-complete/downstream-ready only when all of the following are true:

1. WP-001 through WP-010 are locally `WORK COMPLETE`, or an authorized closure decision explicitly removes/reassigns a package without leaving its control domain unowned.
2. Every package has recorded scope authority, implementation authority, source, traceability and actual local test evidence.
3. `HR9-1-1` / `HR8-10-1` identifies the authorized security-architecture and WBS-16 closure authority.
4. Institutional risk appetite and threat assumptions under `HR9-2-1` are approved and traceable to implemented controls.
5. Every Blocking HR9 item is resolved or explicitly and knowingly deferred by the competent Human authority with exact scope, interim fail-closed behavior, owner and downstream gate recorded.
6. Every Non-Blocking HR9 item is resolved or explicitly dispositioned; silence is not treated as approval.
7. Principal classes, proofing, lifecycle, authentication, sessions, authorization, delegation, privileged access and break-glass contracts are complete and fail closed.
8. Provider/source binding is either approved and implemented or explicitly deferred with provider-neutral interfaces and no operational IAM claim.
9. No implicit role, attribute, permission, delegation, exception or emergency grant exists; every grant path requires current, traceable authority.
10. Secrets, key, cryptographic and network Zero-Trust controls are implemented at the approved layer, with any product/infrastructure responsibility explicitly handed to WBS-23.
11. Agent, model, Tool, Context/Memory, DLP and protected-identity controls preserve isolation, minimization, current authorization and sovereignty boundaries.
12. Security logging, detection and incident contracts preserve the separation among operational signal, Evidence, Finding, Human Decision and execution authority.
13. Artifact, vulnerability, exception and recovery controls preserve provenance, quarantine, revocation and post-recovery reconciliation.
14. Local negative-path and adversarial harnesses cover the intent of `SEC-T1` through `SEC-T9`, while evidence clearly distinguishes local implementation tests from controlled NCIE-016 execution.
15. Strict typing, lint, formatting, compilation, cumulative regression and reproducibility checks pass in the approved environment with no floating or undeclared dependency.
16. No live credential, protected identity, governed production data, external provider, security product or infrastructure is required for local closure unless separately approved and evidenced.
17. Consolidated traceability maps each NCIE-009 control domain and HR decision to implementation, tests, evidence, owner and downstream consumer.
18. WBS-20, WBS-23 and NCIE-016 handovers explicitly identify what remains for Evidence/audit infrastructure, deployment/operations and independent security verification.
19. A completion report lists all limitations, residual risks, deferred HR items and provider/infrastructure gaps without implying accreditation or acceptance.
20. A separately authorized Human approves the WBS-16 completion report.

## 6. Proposed closure status boundary

If the criteria pass, the maximum WBS-16 status should be:

`WBS-16 — IMPLEMENTATION COMPLETE / DOWNSTREAM-READY; INDEPENDENT SECURITY VERIFICATION, ACCREDITATION, CONTROLLED ACCEPTANCE AND GO-LIVE PENDING`

This status must not be represented as:

- NCIE-009 document approval unless its own approval authority acts;
- successful execution of the NCIE-016 controlled security programme;
- operational IAM, Zero Trust, DLP, SIEM, incident response or recovery;
- production readiness, security accreditation, acceptance or go-live; or
- execution of VPF runtime, validator, signature, ledger, residency-enforcement or other declarative infrastructure.

## 7. Immediate next review gate

W16-D5-A (`HR9-1-1` / scoped `HR8-10-1`) and W16-D6-A (`HR9-2-1`) were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-19-011`, and WP-002 was implemented under `...-012`. Its local evidence is recorded under `implementation/wbs-16-wp-002-security-governance-risk-threat/`.

W16-D11-A through W16-D14-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-23-017`, and the exact provider-neutral WP-004 implementation was released under `...-018`. WP-004 is locally work-complete with evidence under `implementation/wbs-16-wp-004-authorization-delegation-privileged-emergency/`. Institutional mappings, permissions, delegations, privileged/emergency authorities, holders, eligibility, numeric policy and activation remain unassigned; `UNASSIGNED = NO GRANT / DENY`.

W16-D15-A through W16-D17-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-23-020`, and the exact provider-neutral WP-005 implementation was released under `...-021`. WP-005 is locally work-complete with evidence under `implementation/wbs-16-wp-005-secrets-cryptography-network-zero-trust/`. Operational authorities, protected material, cryptographic parameters/products, destinations, routes, exception grants and networking remain absent; `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

W16-D18-A through W16-D21-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-023`, and the exact zero-capability WP-006 implementation was released under `...-024`. WP-006 is locally work-complete with four empty controlled registries, unassigned operational authorities, inert Agent/model/Tool/Context boundaries and 134 passing cumulative tests.

W16-D22-A and W16-D23-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-026`, and the exact zero-output/no-reveal WP-007 implementation was released under `...-027`. WP-007 is locally work-complete with six empty controlled registries, unassigned operational authorities, inert DLP/protected-identity/privacy-escalation boundaries and 172 passing cumulative tests. No real protected identity, governed data, disclosure, exception, channel, destination, cross-border transfer, product/provider, dependency or infrastructure has been introduced.

W16-D24-A through W16-D26-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-029`, the exact zero-capability WP-008 implementation was released under `...-030`, and controlled source release was authorized under `...-031`. WP-008 is locally work-complete with eleven empty controlled registries, unassigned operational authorities, minimized synthetic metadata, a non-persistent test collector and inert logging/detection/incident-control boundaries; 224 cumulative tests passed. Commit `ba126b73eb3dea4fd55cfb59b11e43a42623d33c` was pushed to `origin/main` and independently verified. All semantic separations and fourteen non-waivable protections remain intact. No real log/event/incident, persistent store, Evidence/Finding, period, threshold, destination, monitoring/notification/response operation, product/provider, dependency or infrastructure was introduced.

W16-D27-A through W16-D29-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-032`, owner decision `...-033` released the exact WP-009 contract-only implementation, and `...-034` authorized controlled source release. WP-009 is locally work-complete with thirty empty registries, forty-two unassigned authority classes, eighteen structural protections, inert boundaries and 280 passing cumulative tests. Artifact acceptance/promotion/deployment, vulnerability remediation/risk acceptance and recovery/restoration/reauthorization/reinstatement remain unavailable. Push execution is pending and WP-010 work is not authorized. `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, consent, identity dignity, minimization, provenance, sovereignty and African data-residency constraints. No VPF runtime enforcement is claimed.
