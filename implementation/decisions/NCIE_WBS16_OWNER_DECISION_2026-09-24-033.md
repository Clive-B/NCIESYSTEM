# NCIE WBS-16 Owner Decision — 2026-09-24-033

Status: `DECIDED — WBS-16-WP-009 IMPLEMENTATION AUTHORIZED / SOURCE RELEASE NOT AUTHORIZED`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-24-033`

Evidence type: `Self-Authorized Project Owner Decision`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-24`

## Authorized implementation

Implement `WBS-16-WP-009 — Supply Chain, Vulnerability and Security Recovery` strictly within the architecture approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-032`.

Authorized scope is limited to:

- immutable provider-neutral metadata contracts for artifact provenance, exact identity/version, integrity, dependency/build provenance, verification, quarantine, generated-code security gates, acceptance/revocation and distinct promotion/deployment references;
- immutable provider-neutral metadata contracts for vulnerability state, exact affected component/version, remediation/mitigation, exception lifecycle, risk-treatment references, independent review and security acceptance;
- immutable provider-neutral metadata contracts for compromised/unknown/known-good state, recovery-source provenance, quarantine, invalidation obligations, reconciliation, independent recovery review/security-recovery acceptance, restoration and reinstatement references;
- empty versioned registries for every policy, criterion, authority, exception, acceptance, review and revocation class defined in the decided pack;
- unassigned Human/institutional authority interfaces;
- fail-closed metadata evaluation for artifact, vulnerability and recovery-security state;
- no-artifact-action, no-remediation and no-recovery reference boundaries with no operational methods;
- synthetic false-authority, injection, self-approval, provenance/version, stale-state, silent-risk, compromised-recovery and stale-grant negative tests;
- deterministic standard-library unit, contract and negative-path tests;
- cumulative WP-001 through WP-008 regression;
- traceability to `HR9-23-1` through `HR9-25-1`; and
- local non-institutional, non-acceptance implementation evidence.

## Mandatory boundaries

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

All eighteen WP-009 non-waivable protections approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-032` remain mandatory.

The following semantic separations remain structurally mandatory:

- `ARTIFACT VERIFIED ≠ ARTIFACT ACCEPTED ≠ ARTIFACT PROMOTED ≠ DEPLOYED`;
- `VULNERABILITY DETECTED ≠ FINDING ≠ RISK ACCEPTED ≠ REMEDIATED ≠ SECURITY ACCEPTED`;
- `RECOVERY ≠ REAUTHORIZATION`;
- `RECOVERY ACCEPTED ≠ OPERATIONALLY RESTORED`; and
- `RESTORATION ≠ REINSTATEMENT`.

Generated executable code remains quarantined under WP-006 and `NOT_APPROVED_FOR_EXECUTION`. No producer, generator, Agent or implementer may self-approve where independent review is required.

## Required zero-capability state

The controlled implementation must preserve zero real artifact acceptance or quarantine release; zero promotion, deployment, publication or execution; zero artifact payload ingestion or repository interaction; zero live scanning, patching, remediation or mitigation; zero exception activation, risk acceptance or security acceptance; zero backup, snapshot, failover, recovery, restore, invalidation, rotation, live reconciliation, restoration, reauthorization or reinstatement; zero populated operational registries or authority assignments; zero operational severities, thresholds, deadlines, durations or recovery criteria; zero selected/activated products; zero governed production data; zero external destinations or cross-border transfers; and zero new dependencies, infrastructure or deployment.

Unknown or unverifiable artifact/recovery state fails closed and remains quarantined/ineligible. Current revocation, restriction, deletion, classification, provenance and security state takes precedence during synthetic reconciliation. Stale grants, expired permissions, revoked artifacts, credentials/sessions and ineligible Agent/model/Tool states cannot be restored.

Agent/model/Tool/VPF output, scanner output, repository/CI/CD metadata, Documents, logs, alerts, Evidence references, Memory and retrieved/external content remain untrusted and cannot create acceptance, risk decisions, known-good state or execution authority.

WBS-20 retains institutional Evidence, canonical provenance, audit and custody scope. WBS-23 retains repositories, CI/CD, scanners, promotion, deployment, patching, backup/recovery infrastructure and operational runbooks. NCIE-016 retains independent supply-chain/security/recovery verification and acceptance authority.

No WP-010 implementation is authorized. Every stop condition in the decided WP-009 pack remains binding. The fallback is `DENY / QUARANTINE / NO CAPABILITY`.

This decision authorizes local WP-009 implementation and verification only. It does not authorize source-control release, independent verification, accreditation, controlled acceptance, deployment or go-live.

## Provenance note

Codex recorded the natural-person identity, institutional-authority assertion and evidence type supplied by the user. Codex did not independently verify that identity, authority or the meaning of `Self-Authorized Project Owner Decision` beyond recording the user's statement.

VPF is applied behaviorally to Human-primary authority, least privilege, segregation of duties, provenance, minimization, sovereignty and African data residency. This record does not claim execution of a VPF runtime, signature, checksum, certificate, ledger, quarantine service, scanner, recovery action or residency-enforcement service.
