# NCIE WBS-16 Owner Decision — 2026-09-23-018

Status: `DECIDED — WBS-16-WP-004 IMPLEMENTATION AUTHORIZED`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-23-018`

Evidence type: `Self-Authorized Project Owner Decision`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-23`

## Authorized implementation

Authorize implementation of `WBS-16-WP-004 — Authorization Mapping, Delegation, Privileged and Emergency Access` strictly within the architecture approved under `NCIE-WBS16-OWNER-DECISION-2026-09-23-017`.

Authorized scope is limited to:

- provider-neutral, versioned role/attribute mapping contracts with an empty institutional mapping registry;
- current four-layer mapping evaluation integrated with the existing fail-closed authorization boundary;
- the four approved delegation contract classes with strict non-expansion enforcement;
- acting-identity and effective-principal attribution;
- privileged-access request, approval-decision, elevation, expiry and revocation contracts for the three approved classes;
- emergency/break-glass declaration, eligibility, containment, expiry, revocation, notification and independent-review contracts for the three approved emergency classes;
- minimized, non-authoritative security signals;
- local deterministic unit/contract and negative-path tests; and
- traceability and implementation evidence.

## Mandatory boundary

`UNASSIGNED = NO GRANT / DENY`.

No institution-specific role/attribute mapping, permission, delegation, privilege, emergency eligibility or access grant may be populated or activated.

No operational approver, Privileged Access Owner, Emergency Authority, Break-Glass Operator, eligibility roster or independent post-event reviewer may be invented or assigned.

No numeric duration, threshold, freshness window or review cadence may be invented.

No IAM/PAM provider, credential, token, secret, live session, external service, persistent store, infrastructure, governed production data or deployment is authorized.

No WP-005 or later WBS-16 implementation is authorized.

If any stop condition in the decided WP-004 Human Review Decision Pack is encountered, the affected scope stops for Human decision. The fallback state is `DENY / NO CAPABILITY`, not a permissive default.

## Provenance note

Codex recorded the natural-person identity, institutional-authority assertion and evidence type supplied by the user. Codex did not independently verify that identity, authority or the meaning of `Self-Authorized Project Owner Decision` beyond recording the user's statement.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, provenance, identity dignity, minimization, African data residency and deny-by-default cross-border transfer. This record does not claim execution of any VPF runtime, signature, checksum, certificate, ledger, validator, residency-control service or enforcement action.
