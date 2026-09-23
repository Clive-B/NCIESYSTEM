# NCIE WBS-16 Owner Decision — 2026-09-23-017

Status: `DECIDED — W16-D11-A / W16-D12-A / W16-D13-A / W16-D14-A; WP-004 IMPLEMENTATION NOT AUTHORIZED`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-23-017`

Evidence type: `Self-Authorized Project Owner Decision`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-23`

## Decision selections

### W16-D11-A — follow-on HR9-6-1 authorization mappings

Define versioned four-layer mapping contracts and retain zero institution-specific role/attribute mappings and zero grants.

The contract boundary may represent current object-, field-, action- and purpose-level authorization mappings. It does not populate an institutional mapping, assign a role or attribute, grant a permission or authorize access. Undefined, incomplete, expired, revoked, stale, mismatched or indeterminate mappings remain `NO GRANT / DENY`.

### W16-D12-A — HR9-7-1 delegation classes

Approve the four NCIE-009 Table 11 delegation classes as contract-eligible under strict non-expansion controls:

1. Agent acting for Human Principal — Task Contract scope, Run-bound, immediate revocation on Human authorization change.
2. Agent-to-Agent delegation — Subtask scope, Subtask-bound, immediate revocation on parent Run revocation.
3. Service-to-service delegation — service-registration scope, Session-bound, immediate revocation on service-credential revocation.
4. Human-to-Human delegation — NCIE-008 acting/deputy scope, time-boxed under NCIE-008 §5.2, revocable through the governed deputisation record.

No delegation is activated. Contract eligibility does not create a deputisation, delegation token, effective-principal session or credential transfer. Delegation may only narrow current authority and cannot expand it, substitute a technical identity for Human authority, remove a required Human approval or survive its scope, expiry or revocation boundary.

### W16-D13-A — HR9-8-1 privileged-access classes

Approve the three NCIE-009 Table 13 privileged-access classes and their approval interfaces:

1. Infrastructure/configuration admin — named system/configuration scope through the NCIE-008 Authorization decision-right.
2. Identity/IAM admin — named identity-management scope through the NCIE-008 Authorization decision-right.
3. Data/content admin — named content scope, content-specific justification and the NCIE-008 Authorization plus Acceptance interfaces.

Operational approvers, Privileged Access Owner, privilege holders, target assignments, elevations and numeric durations remain unassigned. No privilege is granted. Missing current authority, approval, exact scope, explicit expiry or revocation state remains `NO GRANT / DENY`.

### W16-D14-A — HR9-9-1 emergency/break-glass classes

Approve the three NCIE-009 Table 15 emergency/break-glass classes as contract classes:

1. Identity/access emergency suspension — declared security emergency, named identity/session scope, time-boxed auto-expiry and independent NCIE-008 Chapter 22 review.
2. Agent/model/Tool emergency suspension — declared security emergency, named Agent/model/Tool scope, time-boxed auto-expiry and independent NCIE-008 Chapter 22 review.
3. Infrastructure break-glass admin — declared operational emergency, named system scope, time-boxed auto-expiry and independent NCIE-008 Chapter 22 review.

Emergency Authorities, Break-Glass Operators, eligibility rosters, declaration thresholds, notification assignments, independent post-event reviewer assignments and numeric durations remain unassigned. No emergency is declared, no break-glass session is opened and no containment action is activated. Unassigned or incomplete eligibility and authority remain `NO GRANT / DENY`.

## Conditions

All institution-specific role/attribute mappings, permissions, delegations, privileged-access authorities, privilege holders, Emergency Authorities, Break-Glass Operators, eligibility rosters, numeric durations and operational assignments remain unassigned.

`UNASSIGNED` means `NO GRANT / DENY`.

This decision defines architecture only and does not authorize WP-004 implementation or activate any access capability.

## Authority boundary

This decision satisfies the Human architecture-decision prerequisites for WBS-16-WP-004 only. A separate explicit Project Owner decision naming `WBS-16-WP-004 Authorization Mapping, Delegation, Privileged and Emergency Access` and its exact implementation scope is required before source code, tests or implementation evidence may be created for that package.

No role, attribute, permission, access grant, delegation, privilege, emergency eligibility, emergency declaration, break-glass access, credential, session, provider, infrastructure, external system, deployment, security accreditation, controlled acceptance or go-live is assigned, created, activated or authorized.

The Project Owner's existing NCIE-009 development-specification sign-off and WBS-16 implementation-closure authority is not expanded into an operational privileged-access, break-glass, production-risk, accreditation or go-live authority by this record.

## Provenance note

Codex recorded the natural-person identity, institutional-authority assertion and evidence type supplied by the user. Codex did not independently verify that identity, authority or the meaning of `Self-Authorized Project Owner Decision` beyond recording the user's statement.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, provenance, identity dignity, minimization, African data residency and deny-by-default cross-border transfer. This record does not claim execution of any VPF runtime, signature, checksum, certificate, ledger, validator, residency-control service or enforcement action.
