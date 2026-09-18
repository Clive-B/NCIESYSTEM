# NCIE WBS-15 Foundation Boundary and Remaining-Package Preparation Owner Decision Record

Evidence reference: `NCIE-WBS15-OWNER-DECISION-2026-09-18-004`

- Decision authority supplied: `Project Owner / Clive Ebo Barton-Odro`
- Decision date supplied: `2026-09-18`
- Evidence type supplied: `Self-Authorized Project Owner Decision`
- Conditions supplied: `None beyond the stated boundaries`
- Recorded by Codex: `2026-09-18`
- Independent identity/authority verification: `NOT PERFORMED`

## Confirmed foundation boundaries

1. **Application:** retain the framework-neutral ASGI foundation for WBS-15. Defer application-framework selection until a later authorized scope requires it.
2. **Identity:** WBS-15 may provide identity and request-context interfaces with fail-closed defaults. IAM provider, identity lifecycle, roles, permissions and policy implementation remain WBS-16.
3. **Observability:** WBS-15 may implement provider-neutral observability semantics, contracts and local test collectors. Product selection, collectors, stores, dashboards, alerting and deployment remain WBS-23.
4. **Tooling:** retain Python `3.14.7`, virtual environments and locked pip requirements. No additional tooling or dependency may be introduced unless a demonstrated need is documented and separately approved.

## HR17-15-1 disposition

`HR17-15-1` is `RESOLVED FOR THE WBS-15 FOUNDATION BOUNDARY` by the decisions above. This resolution does not decide downstream IAM, infrastructure, production observability, hosting, deployment, database, connector or application-framework choices.

## Authorized action

Codex is authorized to prepare the following reviewable work packages:

- `WBS-15-WP-003` — Request, Identity and Application Extension Contracts;
- `WBS-15-WP-004` — Observability Semantic Foundation;
- `WBS-15-WP-005` — Reproducible Service Template and WBS-15 Closure.

Preparation includes work-package definitions, task breakdowns, traceability plans, acceptance criteria, exclusions, stop conditions and Human implementation-release decision material.

## Status and restrictions

- Authorization is for **PREPARATION ONLY**. WP-003, WP-004 and WP-005 implementation remains `NOT STARTED` until separately released by an authorized Human.
- WBS-15 remains `IN PROGRESS`; this decision does not itself satisfy the proposed completion criteria.
- No production deployment, external-system activation, governed data, live credentials, unapproved technology, new dependency, IAM implementation, infrastructure change or controlled NCIE-016 acceptance is authorized.
- VPF is applied behaviorally only; no VPF runtime, signature, ledger, PADCA/Omnis service or residency enforcement is claimed.

The natural-person identity and institutional authority assertion are recorded as supplied by the user and were not independently verified by Codex.
