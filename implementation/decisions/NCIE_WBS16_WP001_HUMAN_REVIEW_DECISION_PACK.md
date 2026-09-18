# NCIE WBS-16-WP-001 Human Review Decision Pack

Status: `DECIDED — W16-D1-A / W16-D2-A / W16-D3-A / W16-D4-A; IMPLEMENTATION RELEASED SEPARATELY UNDER ...-009`

Prepared: `2026-09-18`

Proposed work package: `WBS-16-WP-001 Security Principal and Authorization Contract Foundation`

## 1. Purpose

This pack identifies the minimum Human decisions required to release a first, local, provider-neutral WBS-16 increment without silently deciding the wider NCIE-009 security programme.

The controlling open items are:

- `HR17-16-1`: confirm governance/security implementation prerequisites;
- `HR9-3-1`: confirm the authoritative identity source for each principal class and any additional institution-specific classes;
- `HR9-6-1`: approve the authorization policy model and disposition unresolved role/attribute mappings; and
- `HR9-27-1`: explicitly decide which other Blocking HR9 items may remain open for this narrowly bounded increment.

Approval of architecture choices in this pack does **not** authorize implementation. A separate owner decision must release the prepared work package.

## 2. Why these are the minimum decisions

The first increment is deliberately limited to typed principal/source contracts, current-authorization request/decision contracts, a deny-all reference policy decision point, an enforcement adapter to the WBS-15 boundary, bounded non-authoritative security signals, and local tests.

It will not perform identity proofing, authentication, credential or session issuance, user enrollment, provider integration, role assignment, permission grants, delegation, privileged or break-glass access, secrets/key handling, network control, DLP, incident response, security accreditation, deployment or production operation.

Therefore:

- `HR9-3-1` is required because even provider-neutral principal contracts must preserve the authoritative source and non-substitution boundary for each principal class.
- `HR9-6-1` is required because the authorization contract must fix the decision dimensions and fail-closed semantics before code can represent them.
- `HR9-27-1` is required as a scoped deferral decision so no other Blocking HR9 item is silently treated as resolved or bypassed.
- `HR17-16-1` is required to confirm that this is the permitted first WBS-16 increment and that WBS-15 is its satisfied predecessor.

## 3. Decision W16-D1 — HR17-16-1 prerequisites and first-increment boundary

### Option A — Approve the bounded prerequisite set (recommended)

Confirm that:

1. WBS-15 implementation closure satisfies the predecessor condition for this package.
2. `WBS-16-WP-001` may remain local, provider-neutral, dependency-free and framework-neutral, using the approved Python 3.14.7 environment and existing WBS-15 contracts.
3. The increment may define security contracts and fail-closed reference behavior only; it may not activate IAM, credentials, sessions, access grants, external systems, infrastructure or production controls.
4. No later WBS may consume WP-001 as a complete security posture. NCIE-017 §16.2's secrets, network, privileged-access and audit prerequisite block remains pending.
5. Project Owner / Clive Ebo Barton-Odro is the accountable Human authority for this increment's scope decisions. Codex may become the responsible implementer only under a separate explicit implementation authorization. Independent security verification, accreditation and acceptance remain unassigned and pending.

### Option B — Expand the first increment

Define the additional security capabilities to include. This requires resolving every newly applicable HR9 item before implementation authorization.

### Option C — Defer

Keep WBS-16 blocked and preserve the prepared package without implementation.

Recommendation: **W16-D1-A**.

## 4. Decision W16-D2 — HR9-3-1 principal classes and authoritative-source categories

### Option A — Confirm logical source categories; defer products (recommended)

Confirm the NCIE-009 Table 4 taxonomy for WP-001:

| Principal class | Authoritative source category | WP-001 treatment |
|---|---|---|
| Human identity | Institutional identity source | Interface only; no provider or person enrolled |
| Workload identity | Deployment/orchestration platform | Interface only; platform selection deferred |
| Agent identity | Agent Factory/Registry | Interface only; no Agent runtime activated |
| Service identity | Service registration | Local contract only; no production registration |
| Session/device identity | Authentication session issuer | Interface only; no session or credential issued |
| Privileged identity | Privileged-access-management authority | Interface only; PAM selection deferred |
| Validator identity | VPF validator registration | Interface only; no VPF runtime or validator activated |

Also confirm:

- no additional institution-specific principal class is approved for WP-001;
- an unknown or unbound source resolves to no authenticated/authorized principal;
- no principal class may substitute for another; and
- product, tenant, registry instance, identifier format and provider binding remain separate future decisions.

### Option B — Require concrete source/provider selections now

Supply the approved source or provider for every applicable principal class and the authority for its use. This broadens the package and may trigger technology, infrastructure, residency and procurement decisions.

### Option C — Defer

Do not implement principal/source contracts.

Recommendation: **W16-D2-A**.

## 5. Decision W16-D3 — HR9-6-1 authorization policy model

### Option A — Approve the four-layer hybrid model with zero grants (recommended)

Approve a current, deny-by-default authorization model with:

- role and attribute inputs where later approved;
- object-, field-, action- and purpose-level decision dimensions;
- classification and consent constraints where later supplied by authoritative sources;
- an explicit `PERMIT`, `DENY` or `INDETERMINATE` decision result;
- `DENY` enforcement for missing, stale, invalid, error or `INDETERMINATE` results;
- evaluation at time of use, with no remembered or cached decision treated as current authority; and
- no role mapping, attribute mapping, permission or policy grant in WP-001.

All institution-specific role/attribute mappings remain unresolved. Their interim state is the empty grant set, which denies access and grants no authority.

### Option B — Return with a different model

Specify the replacement decision dimensions, enforcement semantics and source authority. The replacement must still comply with upstream zero-trust and deny-by-default requirements.

### Option C — Defer

Retain the WBS-15 deny-all boundary and do not implement an authorization decision contract.

Recommendation: **W16-D3-A**.

## 6. Decision W16-D4 — HR9-27-1 scoped disposition of remaining HR9 items

### Option A — Approve scoped deferral for WP-001 (recommended)

Confirm that `HR9-1-1`, `HR9-2-1`, `HR9-4-1`, `HR9-5-1` and `HR9-7-1` through `HR9-26-1` remain open and unresolved, but do not block this contract-only package because their governed capabilities are excluded.

The interim behavior is absence of capability and fail-closed denial—not an invented security default. This disposition:

- applies only to WP-001;
- does not approve NCIE-009 v1.0 as a whole;
- does not resolve `HR8-10-1`, which NCIE-009 identifies as the corresponding acceptance-authority question for `HR9-1-1`;
- does not change the already-resolved historical status of `HR9-28-1`; and
- requires a new Human decision before any deferred capability enters scope.

### Option B — Require additional HR9 decisions before WP-001

List the additional HR9 IDs and required choices. WP-001 remains blocked until they are resolved.

### Option C — Defer all WBS-16 work

Preserve the package without implementation.

Recommendation: **W16-D4-A**.

## 7. Consolidated decision record

- W16-D1 selection: `A — bounded, provider-neutral first increment`
- W16-D2 selection: `A — seven principal categories confirmed; provider choice deferred`
- W16-D3 selection: `A — four-layer, deny-by-default authorization with zero grants`
- W16-D4 selection: `A — remaining HR9 decisions deferred for WP-001 only`
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`
- Decision date: `2026-09-18`
- Conditions: `None`
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-18-008`

## 8. Separate implementation release required

W16-D1 through W16-D4 were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-18-008`. Implementation was subsequently released under `NCIE-WBS16-OWNER-DECISION-2026-09-18-009`. The separation between architecture decisions and implementation authority is preserved in the two evidence records.

No decision in this pack authorizes external provider selection, dependency addition, infrastructure change, live identity data, credential handling, production deployment, security accreditation, controlled acceptance or go-live.

## 9. Source traceability

- NCIE-017 Chapter 16 and `HR17-16-1`.
- NCIE-009 Chapters 3 and 6, Tables 4 and 9, `HR9-3-1` and `HR9-6-1`.
- NCIE-009 Chapter 27 and `HR9-27-1`.
- WBS-15 downstream handover and owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-18-006`.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, identity non-substitution, data minimization and African data-sovereignty constraints. This pack does not claim execution of any VPF runtime control.
