# NCIE WBS-16 Owner Decision — 2026-09-24-030

Status: `APPROVED — WBS-16-WP-008 CONTROLLED IMPLEMENTATION AUTHORIZED`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-24-030`

Evidence type: `Self-Authorized Project Owner Decision`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-24`

## Authorized scope

Implementation of `WBS-16-WP-008 — Security Logging, Detection and Incident-Control Contracts` is authorized strictly within the architecture approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-029`.

Authorized scope is limited to:

- immutable provider-neutral contracts for minimized security events, the five approved detection categories, triage/escalation results, symbolic severity, incident lifecycle stages, notification obligations, containment requests and restoration/reinstatement reviews;
- empty versioned registries for security-log access, retention/legal hold, assurance assignments, detection rules, escalation routes, severity governance, incident command, notifications/destinations, containment rights, emergency eligibility and restoration/reinstatement authority;
- unassigned Human/institutional authority interfaces;
- fail-closed metadata evaluation for log access, retention policy, detection, triage, incident declaration, notification, containment and restoration/reinstatement;
- an in-memory, non-persistent synthetic test collector that cannot become an audit, provenance or Evidence store;
- a no-monitor reference boundary with no polling, streaming, product integration or external source;
- a no-alert/no-page notification boundary with no recipient, destination or send capability;
- a no-incident-command boundary capable only of returning `DENY` or `HUMAN_DECISION_REQUIRED`;
- a no-containment/no-recovery boundary with no execution method;
- synthetic prompt-injection and false-authority tests preserving WP-006 and WP-007 untrusted-content semantics;
- minimized, non-authoritative security signals;
- deterministic standard-library unit, contract and negative-path tests;
- cumulative WP-001 through WP-007 regression; and
- traceability and local implementation evidence.

## Mandatory boundary

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

All fourteen non-waivable protections approved under decision `...-029` remain mandatory.

The following separations remain structurally enforced:

- `SIGNAL ≠ SECURITY EVENT ≠ DETECTION/ALERT ≠ INCIDENT ≠ EVIDENCE ≠ FINDING ≠ HUMAN DECISION ≠ EXECUTION AUTHORITY`;
- `SEVERITY ≠ AUTHORITY`;
- `INCIDENT DECLARED ≠ CONTAINMENT AUTHORIZED ≠ CONTAINMENT EXECUTED`;
- `CONTAINMENT EFFECTIVE ≠ RECOVERY AUTHORIZED ≠ REINSTATEMENT AUTHORIZED`;
- `RECOVERY ≠ REAUTHORIZATION`; and
- `RESTORATION ≠ REINSTATEMENT`.

## Zero-capability conditions

The controlled implementation must preserve zero real logs or production security events; zero persistent log/audit/Evidence storage; zero institutional Evidence or Findings; zero retention or legal-hold durations; zero operational severity taxonomy or thresholds; zero monitoring, polling, streaming or live correlation; zero alert delivery or paging; zero recipients, destinations or sending; zero real incident declaration or incident command; zero containment, suspension, revocation or isolation execution; zero recovery, restoration or reinstatement execution; zero operational authority assignments; zero security products; zero governed production data; zero external destinations or cross-border transfers; and zero new dependencies, infrastructure or deployment.

Security-event metadata must contain no secrets, credentials, tokens, keys, raw prompts, private chain-of-thought, real protected identity values, governed payloads, Document/Memory/Evidence payloads or precise sensitive Tool-result content.

Agent/model/Tool/VPF output, logs, alerts, Documents, Evidence references, Memory, web/API content and other retrieved/external content remain untrusted data and cannot create or modify authority, severity, incident state, containment permission or reinstatement authority.

WBS-20 retains institutional Evidence, canonical audit, provenance and custody scope. WBS-23 retains operational logging, observability, SIEM, monitoring, paging, infrastructure and deployment scope. NCIE-016 retains independent security-verification and acceptance authority.

No WP-009 or later WBS-16 implementation is authorized. A stop condition in the decided WP-008 Human Review Decision Pack returns the affected scope for Human decision. The fallback remains `DENY / NO CAPABILITY`.

## Provenance note

Codex recorded the identity, authority assertion, authorization text and evidence type supplied directly by the user. Codex did not independently verify the natural-person identity or institutional authority beyond recording that supplied statement.

VPF is applied behaviorally to Human-primary authority, least privilege, provenance, minimization, explainability, sovereignty and African data-residency constraints. This record claims no VPF runtime, signature, checksum, certificate, ledger, monitoring, alerting, incident action or residency-enforcement execution.
