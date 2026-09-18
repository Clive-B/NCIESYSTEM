# NCIE WBS-16 Owner Decision — 2026-09-18-008

Status: `DECIDED — W16-D1-A / W16-D2-A / W16-D3-A / W16-D4-A`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-18-008`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-18`

Conditions: None.

## Decision selections

### W16-D1-A — HR17-16-1 bounded first increment

Approve `WBS-16-WP-001 Security Principal and Authorization Contract Foundation` as the bounded, local, provider-neutral first WBS-16 increment described in the Human Review decision pack.

WBS-15 satisfies the predecessor condition. The package must remain dependency-free and framework-neutral on the approved Python 3.14.7 foundation, and may define security contracts and fail-closed reference behavior only.

### W16-D2-A — HR9-3-1 principal categories

Confirm the seven NCIE-009 principal classes and their logical authoritative-source categories:

1. Human identity — institutional identity source.
2. Workload identity — deployment/orchestration platform.
3. Agent identity — Agent Factory/Registry.
4. Service identity — service registration.
5. Session/device identity — authentication session issuer.
6. Privileged identity — privileged-access-management authority.
7. Validator identity — VPF validator registration.

Provider, product, tenant, registry instance and identifier-format choices remain deferred. No additional institution-specific principal class is approved for WP-001. Unknown, unbound or mismatched sources authenticate no principal, and no principal class may substitute for another.

### W16-D3-A — HR9-6-1 four-layer authorization

Approve the current, deny-by-default authorization model across object, field, action and purpose dimensions. Role and attribute inputs may be represented only as future extension data; no role mapping, attribute mapping, permission or policy grant is approved for WP-001.

The reference model uses `PERMIT`, `DENY` and `INDETERMINATE` outcomes. Missing, stale, invalid, error and `INDETERMINATE` results are enforced as deny. Remembered or cached authorization is not current authority.

### W16-D4-A — HR9-27-1 scoped deferral

For WP-001 only, `HR9-1-1`, `HR9-2-1`, `HR9-4-1`, `HR9-5-1` and `HR9-7-1` through `HR9-26-1` remain open and unresolved but do not block the contract-only package because their governed capabilities remain excluded.

This is a scoped deferral, not resolution of those items and not approval of NCIE-009 v1.0. Any deferred capability requires a new Human decision before it enters scope. `HR8-10-1` remains unresolved, and the historical upstream resolution of `HR9-28-1` is unchanged.

## Authority boundary

This decision satisfies the Human decision prerequisites for the prepared WP-001 scope. It does **not** authorize implementation.

A separate explicit Project Owner decision naming `WBS-16-WP-001` is required before source code, tests or implementation evidence may be created for the package.

No IAM provider, credential/session handling, access grant, external system, infrastructure change, live identity data, production deployment, security accreditation, controlled acceptance or go-live is authorized.

## Provenance note

Codex recorded the natural-person identity and institutional-authority assertion supplied by the user. Codex did not independently verify that identity or authority.
