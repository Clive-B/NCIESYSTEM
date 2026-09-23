# WBS-16-WP-004 Authorization Mapping, Delegation, Privileged and Emergency Access

Status: `WORK COMPLETE — LOCALLY VERIFIED; ZERO LIVE GRANTS`

Decision prerequisites: W16-D11-A through W16-D14-A under `NCIE-WBS16-OWNER-DECISION-2026-09-23-017`.

Implementation authority: `NCIE-WBS16-OWNER-DECISION-2026-09-23-018`.

Source-control release authority: `NCIE-WBS16-OWNER-DECISION-2026-09-23-019`.

## 1. Objective

Implement provider-neutral mapping, delegation, privilege and emergency-access contracts that preserve current authorization, strict non-expansion, expiry/revocation, independent review and `UNASSIGNED = NO GRANT / DENY` without populating or activating access.

## 2. Implemented scope

1. Versioned role/attribute mapping entries covering object, field, action and purpose dimensions.
2. An immutable empty institutional mapping registry and current mapping decision point integrated with the WP-001 enforcement contract.
3. Exact rules for the four NCIE-009 Table 11 delegation classes.
4. Acting-identity/effective-principal attribution and intersection-only delegation scope.
5. Exact classes and approval interfaces for the three NCIE-009 Table 13 privilege classes.
6. Privileged request, Human approval-decision, elevation-context, explicit-expiry and revocation contracts.
7. An unassigned privileged-approval boundary that returns no decision and grants no elevation.
8. Exact triggers and containment actions for the three NCIE-009 Table 15 emergency classes.
9. Emergency declaration, eligibility, access-request, auto-expiry, revocation, notification and independent post-event review contracts.
10. An unassigned emergency-eligibility boundary with a zero roster and no activation.
11. Minimized, non-authoritative access-control signals.
12. Deterministic unit/contract and negative-path tests, cumulative regression, traceability and evidence.

## 3. Explicit exclusions

- Institution-specific mapping, permission, delegation, privilege, eligibility or access grant.
- Operational approver, Privileged Access Owner, Emergency Authority, Break-Glass Operator, eligibility roster or reviewer assignment.
- Numeric duration, threshold, freshness window or review cadence.
- Provider, credential, token, secret, live session, external service or persistent store.
- Infrastructure, governed production data, deployment, accreditation, controlled acceptance or go-live.
- WP-005 or any later WBS-16 capability.

## 4. Completion result

All eighteen completion criteria in the decided Human Review pack are represented and locally verified. The controlled reference state has:

- zero institution-specific mappings;
- zero grants;
- zero active delegations;
- zero privileged authorities/elevations;
- zero emergency eligibility assignments/activations; and
- fail-closed denial for every missing, stale, expired, revoked, mismatched, ambiguous or unassigned authority path.

Local verification passed strict mypy, Ruff lint/format, compilation, 86 cumulative tests and the WBS-15 template verifier. This is implementation evidence only, not independent security verification or acceptance.

## 5. Stop boundary

Stop for a new Human decision before populating any institutional mapping or assignment, selecting numeric policy, adding a provider/credential/session/store/infrastructure, activating access, implementing WP-005, or claiming Evidence, accreditation, acceptance, deployment or go-live.

## 6. VPF boundary

VPF influenced Human-primary authority, least privilege, provenance, minimization and sovereignty safeguards. No VPF runtime, validator, signature, ledger, residency-control service or enforcement action is implemented or claimed.
