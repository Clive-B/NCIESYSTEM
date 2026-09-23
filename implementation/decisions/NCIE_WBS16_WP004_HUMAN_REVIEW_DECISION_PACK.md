# NCIE WBS-16-WP-004 Human Review Decision Pack

Status: `DECIDED — W16-D11-A / W16-D12-A / W16-D13-A / W16-D14-A; IMPLEMENTATION RELEASED SEPARATELY UNDER ...-018`

Prepared: `2026-09-23`

Decided: `2026-09-23`

Proposed work package: `WBS-16-WP-004 Authorization Mapping, Delegation, Privileged and Emergency Access`

## 1. Review purpose and authority boundary

This pack presents the Human decisions required before WP-004 may be considered for a separate implementation release. It covers:

- follow-on `HR9-6-1`: disposition of institution-specific role/attribute mappings after WP-001 approved the four-layer authorization model with an empty grant set;
- `HR9-7-1`: permitted and prohibited delegation classes;
- `HR9-8-1`: privileged-access classes and approval authority; and
- `HR9-9-1`: break-glass authority, eligible emergency classes and post-event review rules.

This pack was prepared for Human review and now records the Project Owner selections evidenced by `NCIE-WBS16-OWNER-DECISION-2026-09-23-017`. Nothing in the decision or this pack:

- makes or infers a Human decision;
- assigns a role, attribute, permission, privilege, access grant, deputy, approver, Emergency Authority, operator or reviewer;
- activates delegation, privileged access or break-glass access;
- selects an IAM/PAM provider, infrastructure, product, tenant or external system;
- creates an identity, credential, token, session or live policy; or
- authorizes implementation, source changes, deployment, accreditation, acceptance or go-live.

The four architecture decisions are now recorded. WP-004 implementation still requires a separate, exact implementation authorization.

## 2. Controlling baseline

The controlled source chain establishes the following non-negotiable conditions:

1. `AUTHENTICATED IDENTITY ≠ AUTHORIZED ACTION`; `TECHNICAL IDENTITY ≠ INSTITUTIONAL GOVERNANCE ROLE`; `DELEGATED TASK ≠ HUMAN CREDENTIAL DELEGATION`; `REMEMBERED AUTHORIZATION ≠ CURRENT AUTHORIZATION`; and `BREAK-GLASS ≠ PERMANENT PRIVILEGE`.
2. Authorization is evaluated currently at object, field, action and purpose layers. Missing, stale, invalid, erroneous or indeterminate authority denies access.
3. WP-001 contains no role mapping, attribute mapping, permission or policy grant. Its empty grant set remains the operative fail-closed baseline.
4. Defining a role class, attribute type, delegation class, privilege class or emergency class does not assign it to a holder and does not grant access.
5. Every institutional decision binds to a specific target, scope and version. Revocation ends its prospective validity. Prior practice or informal custom is not evidence of current assignment.
6. Delegation never expands authority. Acting identity and effective principal remain separately attributable, and reusable Human credentials are never copied into Agent or runtime Context.
7. Administrative privilege and substantive content authority are separate grants and separate audit subjects.
8. Ordinary privilege is scoped and time-bounded. Emergency access is scoped, temporary, notified, auditable and independently post-reviewed.
9. A technical/service identity may perform a Responsible function but cannot be Accountable or Approver. Human-primary institutional authority is preserved.
10. The approved WP-002 authority for NCIE-009 development sign-off and WBS-16 implementation closure does not silently create operational authorization, privileged-access, break-glass, accreditation, production-risk or go-live authority.
11. WP-003 approved symbolic assurance and explicit-expiry contracts only. It did not approve factors, numeric durations, operational holders, credentials, sessions or access.
12. No later workstream may treat WP-004 contracts as an operational security posture or as evidence that any person or system has access.

## 3. Definition is not assignment

The following distinction controls every option in this pack:

| Definition permitted for a later authorized WP-004 | Assignment or activation prohibited by this pack |
|---|---|
| Role/attribute schema and versioned mapping-entry shape | Populating an institution-specific role/attribute-to-permission grant |
| Delegation class, scope ceiling, expiry type and revocation trigger | Creating a deputisation, delegation token, effective-principal session or active delegation |
| Privilege class, request/approval record shape, scope and expiry requirements | Naming an approver, approving a request or elevating a principal |
| Emergency class, declaration record, containment scope and review requirements | Declaring an emergency, naming an eligible holder, opening a break-glass session or executing containment |
| Abstract authority class or interface | Mapping that class to an actual office, person, service identity or technical account |

Until a competent Human authority makes and evidences the separate assignment, the implementation meaning is `UNASSIGNED`, `NO GRANT` and `DENY`.

## 4. Decision W16-D11 — follow-on HR9-6-1 role/attribute mapping disposition

### 4.1 Exact source-grounded authorization model

NCIE-009 Table 9 fixes these decision layers; WP-001 already implemented their current, deny-by-default contract form:

| Authorization layer | Exact decision basis | Exact enforcement point | Default |
|---|---|---|---|
| Object-level | Current role/attribute grant | Policy enforcement point at access | Deny |
| Field-level | NCIE-003 classification + current grant | Policy enforcement point at field read | Deny |
| Action-level | Current role/attribute grant for the specific action | Policy enforcement point at action invocation | Deny |
| Purpose-level | Declared purpose consistent with classification/consent | Policy enforcement point at request time | Deny |

The source assigns approval of the policy model and role/attribute mappings to an `Accountable Authority Class (to be assigned)` and identifies an `Authorization Architecture Owner (to be assigned)`. No controlled source supplies an institution-specific role catalogue, attribute catalogue, mapping set or operational holder for those functions.

### 4.2 Human disposition options and implications

#### Option A — Define mapping contracts and retain zero institutional grants (recommended)

Authorize a later WP-004 implementation to define only a versioned mapping contract capable of representing:

- the four source-fixed authorization layers;
- an opaque role or attribute reference;
- exact target/object and optional field set;
- exact action;
- declared purpose and applicable classification/consent reference;
- policy version, effective time, explicit expiry and revocation state;
- approving-decision reference; and
- `PERMIT`, `DENY` or `INDETERMINATE` evaluation compatible with WP-001.

Retain an empty institution-specific mapping set. No role, attribute, permission or access grant is approved. Undefined, incomplete, expired, revoked, stale, mismatched or indeterminate mappings deny.

Implication: WP-004 can implement and test the mapping boundary without inventing institutional policy. All protected access continues to fail closed because the grant set remains empty.

#### Option B — Supply institution-specific mappings for review

The Human authority supplies each proposed mapping with the exact role/attribute, target/object, fields, action, purpose, classification/consent constraints, policy version, effective time, expiry, revocation conditions and competent approving authority.

Implication: the package must be revised and re-reviewed before implementation. A role name or attribute definition alone is insufficient. No supplied mapping becomes a grant merely by appearing in a draft or test fixture.

#### Option C — Defer WP-004 authorization mapping

Keep the mapping capability unimplemented and preserve WP-001's deny-all reference behavior.

Implication: WP-004 and any dependent privileged/delegated access remain blocked.

Recommendation: `W16-D11-A` because it preserves the controlled four-layer model, least privilege and current authorization while refusing to fabricate institutional mappings.

### 4.3 Items that must remain institutionally unassigned

- Institution-specific role and attribute catalogues.
- Every role/attribute-to-object/field/action/purpose mapping.
- Authorization Architecture Owner and operational mapping approver.
- Actual assignment of any defined role or attribute to a Human, Agent, workload, service, session/device, privileged or validator principal.
- Numeric mapping lifetime or review cadence not supplied by an authoritative Human policy.

## 5. Decision W16-D12 — HR9-7-1 delegation classes and boundaries

### 5.1 Exact source-grounded delegation classes

NCIE-009 Table 11 presents the following four classes for Human confirmation:

| Delegation class | Exact scope binding | Exact expiry | Exact revocation |
|---|---|---|---|
| Agent acting for Human Principal | Task Contract scope (NCIE-007) | Run-bound | Immediate on Human authorization change |
| Agent-to-Agent delegation | Subtask scope (NCIE-007 Ch.13) | Subtask-bound | Immediate on parent Run revocation |
| Service-to-service delegation | Service registration scope | Session-bound | Immediate on service credential revocation |
| Human-to-Human delegation (e.g. deputisation) | NCIE-008 Ch.5 acting/deputy scope | Time-boxed per NCIE-008 §5.2 | Per NCIE-008 deputisation record |

NCIE-008 further requires a recorded, time-boxed deputisation before a deputy may act for an Accountable or Approver role. A vacancy suspends the dependent decision right; it does not transfer authority by default. Whether any authority is legally or institutionally non-delegable remains an unresolved institutional question under `HR8-2-1` and must not be invented here.

### 5.2 Human disposition options and implications

#### Option A — Approve all four as eligible contract classes under non-expansion controls (recommended)

Approve the four Table 11 rows as representable delegation classes, subject to all of these boundaries:

1. `eligible class` does not mean `active delegation`.
2. A delegation is valid only with a current, attributable delegator, delegate, acting identity, effective principal, exact scope, purpose, policy version, start, explicit expiry and revocation source.
3. The effective authority is the intersection of the delegator's current authority, the delegate's current eligibility and the delegation's narrower scope. It can never be their union and can never exceed any input ceiling.
4. The delegated actor cannot impersonate the delegator outside the stated scope. Provenance preserves both identities on every action.
5. Delegation cannot copy or expose a reusable Human credential, cannot remove a required Human approval, and cannot convert an Agent, service or technical identity into a governance authority.
6. Nested delegation is allowed only where the source-fixed class explicitly supports it and each hop narrows scope and expiry. Agent-to-Agent delegation remains subordinate to its parent Run; no other transitive delegation is inferred.
7. Human-to-Human deputisation denies unless a current governed deputisation record exists and the delegated authority is not designated non-delegable. Pending `HR8-2-1`, no non-delegable authority list is fabricated.
8. Expiry, parent revocation, credential revocation, delegator authorization change, lifecycle invalidation or any missing current-state input immediately ends usable delegated authority.

The following are prohibited: credential sharing; implied or customary delegation; open-ended delegation; anonymous effective principals; delegation beyond scope, purpose or expiry; authority amplification; substitution of technical identity for Human authority; automatic inheritance through vacancy; and reuse after revocation.

Implication: a later WP-004 can implement provider-neutral delegation envelopes and negative tests, but no actual delegation can be created or exercised.

#### Option B — Approve a narrower subset

The Human reviewer identifies which Table 11 classes are permitted and which are prohibited, with reasons and any additional non-expansion constraint. Any omitted class is denied.

Implication: WP-004 implements only the confirmed subset and must reject the rest. Human-to-Human delegation remains unavailable unless its deputisation and non-delegability conditions are expressly resolved.

#### Option C — Prohibit/defer all delegation

No delegation class is implemented beyond an explicit denial result.

Implication: direct current authorization remains the only permitted authorization path; WP-004 cannot claim delegated-operation readiness.

Recommendation: `W16-D12-A` for contract eligibility only, because it preserves the exact NCIE-009 taxonomy and allows safe enforcement testing without activating any delegation or expanding authority.

### 5.3 Items that must remain institutionally unassigned

- Any delegator, delegate, deputy or effective-principal assignment.
- The list of legally or institutionally non-delegable authorities under `HR8-2-1`.
- Any current deputisation record or operational delegation approval holder.
- Any numeric duration beyond the source-fixed run-, subtask-, session- or expressly time-boxed boundary.

## 6. Decision W16-D13 — HR9-8-1 privileged-access classes and authority

### 6.1 Exact source-grounded privileged-access classes

NCIE-009 Table 13 fixes the ordinary privileged-elevation choices as follows:

| Privilege class | Exact elevation trigger | Exact scope | Exact approval interface |
|---|---|---|---|
| Infrastructure/configuration admin | Elevation request | Named system/config scope | NCIE-008 Ch.4 Authorization decision-right |
| Identity/IAM admin | Elevation request | Named identity-management scope | NCIE-008 Ch.4 Authorization decision-right |
| Data/content admin (distinct from infra admin) | Elevation request + content-specific justification | Named content scope | NCIE-008 Ch.4 Authorization + Ch.10 Acceptance |

NCIE-009 requires bounded scope and duration, session controls and privileged-specific audit. It assigns approval to an `Accountable Authority Class (to be assigned)` and ownership to a `Privileged Access Owner (to be assigned)`. NCIE-008 `HR8-20-1` still requires institutional confirmation of the privileged-access approval authority. These holders cannot be inferred from the Project Owner's development-specification sign-off authority.

### 6.2 Human disposition options and implications

#### Option A — Approve the three classes and approval interfaces; leave operational holders unassigned (recommended)

Authorize a later WP-004 to represent the three Table 13 classes and enforce:

- a current request by an attributable requester;
- exact named scope and requested actions;
- justification, with content-specific justification mandatory for data/content administration;
- current approval-decision reference from the applicable, separately assigned Human authority;
- requester/approver separation under NCIE-008 (`Approver ≠ requester`);
- elevated assurance from WP-003 without treating assurance as authorization;
- explicit start and expiry with no default or indefinite duration;
- immediate expiry/revocation enforcement and stale-grant rejection;
- separate acting identity, ordinary identity and privileged elevation context;
- administration/content separation; and
- minimized privileged-event provenance without secrets or protected content.

No operational approval authority or privilege holder is assigned. Consequently, the reference contract must deny every actual elevation until the competent Human authority is separately assigned and supplies a current approval.

Implication: WP-004 can implement and test privileged-access request/decision boundaries, including expiry and revocation, while granting no privilege.

#### Option B — Supply operational authority assignments and policy

The Human authority supplies, for each privilege class, the approving institutional function/current holder, Privileged Access Owner, permitted targets/actions, assurance policy, maximum duration, revocation authority, review/audit obligation and any prohibited targets.

Implication: this materially broadens the operational policy and requires a revised pack. It still does not itself approve an elevation or authorize live PAM.

#### Option C — Defer ordinary privileged access

Keep all privileged-elevation paths unavailable.

Implication: privileged requests deny and later persistence/infrastructure work dependent on operational privileged access remains blocked.

Recommendation: `W16-D13-A` because it captures the exact architecture without converting an unresolved authority class into an invented holder or a live grant.

### 6.3 Authority, expiry and revocation boundary

- Authority: only the applicable current NCIE-008 decision-right holder may approve; no such operational holder is assigned by this pack.
- Expiry: every elevation requires an explicit expiry; absence of expiry or an approved duration policy denies. No numeric duration is invented.
- Revocation: revocation, base-identity/lifecycle invalidation, authority change, policy-version change, scope mismatch, session expiry or loss of required assurance ends use immediately from its effective time.
- Renewal: no automatic rollover. A later elevation requires a fresh request and current decision.
- Content: infrastructure/IAM privilege confers no substantive content access. Content administration additionally requires its source-fixed content justification and Acceptance interface.

### 6.4 Items that must remain institutionally unassigned

- Privileged Access Owner.
- Operational Accountable authority/approver for each privilege class.
- Requesters, privileged identities, target systems and content scopes.
- Numeric maximum duration, assurance freshness window and review cadence.
- PAM provider, credential mechanism, session broker and audit platform.

## 7. Decision W16-D14 — HR9-9-1 break-glass authority, triggers and review

### 7.1 Exact source-grounded emergency classes

NCIE-009 Table 15 presents these classes for Human confirmation:

| Emergency class | Exact trigger | Exact scope | Exact expiry | Exact post-event review |
|---|---|---|---|---|
| Identity/access emergency suspension | Declared security emergency | Named identity/session scope | Time-boxed, auto-expiring | Independent NCIE-008 Ch.22 review |
| Agent/model/Tool emergency suspension | Declared security emergency | Named Agent/model/Tool scope | Time-boxed, auto-expiring | Independent NCIE-008 Ch.22 review |
| Infrastructure break-glass admin | Declared operational emergency | Named system scope | Time-boxed, auto-expiring | Independent NCIE-008 Ch.22 review |

NCIE-008 permits an Emergency Authority to trigger only a bounded, scoped suspension or containment action for safety, security or integrity reasons. It requires actor, target, scope, trigger and time to be logged, mandatory notification to the affected domain's Accountable Authority, and independent post-event review. The acting Emergency Authority cannot alone decide reinstatement or permanent disposition.

NCIE-009 assigns the `Emergency Authority`, `Break-Glass Operator` and target-specific post-event authorities as `to be assigned`. NCIE-008 `HR8-20-1` and `HR8-22-1` remain the institutional assignment gates.

### 7.2 Human disposition options and implications

#### Option A — Approve all three emergency contract classes; retain zero eligibility assignments (recommended)

Authorize a later WP-004 to model the three Table 15 classes with these mandatory controls:

1. A trigger exists only through a current, attributable emergency declaration stating `security` or `operational`, reason, exact target, exact containment purpose, decision reference and declaration time.
2. Eligibility requires a separately assigned, current Emergency Authority for that exact class and scope. With no assignment, every request denies.
3. The first two classes permit suspension/containment only; they do not grant content access or permanent revocation. Infrastructure break-glass permits only the expressly approved administrative actions within the named system scope.
4. Every grant or containment instruction has an explicit start and expiry and must auto-expire. Missing expiry, indefinite duration or absent approved duration policy denies. No numeric time limit is invented.
5. Emergency authority cannot exceed the target, purpose, action or time in the declaration; cannot bypass non-waivable controls; cannot expose reusable credentials; and cannot become standing privilege.
6. Revocation, expiry, withdrawal of the declaration, loss of actor eligibility, lifecycle invalidation or containment completion ends authority immediately.
7. Every attempt and action produces minimized, attributable provenance for actor, effective principal where applicable, target, scope, trigger, time, decision reference and outcome; no secret or protected content is logged.
8. Mandatory notification goes to the affected domain's Accountable Authority and Assurance/Audit interface. If those destinations are unassigned, the technical event remains contained and is flagged incomplete; no permanent disposition may follow.
9. An independent Human reviewer, never the acting Emergency Authority alone, reviews necessity, scope, actions, expiry/revocation, effects and restoration evidence before reinstatement or permanent disposition.
10. Restoration does not recreate prior sessions, privileges or stale authorization. Any reinstatement or permanent change requires its own current governed decision.

Implication: WP-004 can implement fail-closed emergency-control contracts and adversarial tests. No person becomes eligible, no emergency is declared, no break-glass session opens and no containment action executes.

#### Option B — Supply eligibility, trigger and time policies

The Human authority supplies the eligible institutional functions/current holders for each class, authoritative declaration criteria, maximum duration, revocation authority, notification recipients and independent post-event reviewer assignments.

Implication: the package must be revised and reviewed against `HR8-20-1`, `HR8-22-1`, separation of duties, residency and operational-control dependencies. The policy still does not itself activate emergency access.

#### Option C — Defer all break-glass/emergency access

Keep every emergency access path unavailable.

Implication: WP-004 may represent only denial. Operational emergency-access readiness remains blocked; no ordinary privilege path may be relabelled as break-glass.

Recommendation: `W16-D14-A` because it preserves the source-defined containment architecture and mandatory independent review while refusing to invent eligible authorities, emergencies or numeric limits.

### 7.3 Items that must remain institutionally unassigned

- Emergency Authority for each target class.
- Break-Glass Operator and every eligible requester/actor roster.
- Domain Accountable Authority and independent post-event reviewer for each target class, except where separately evidenced by a future competent decision.
- Concrete declaration thresholds, numeric maximum duration, notification endpoints and on-call arrangements.
- Any standing credential, recovery secret, privileged identity, live session, target system or containment mechanism.

## 8. Consolidated Project Owner decision

The Project Owner selected the recommended architecture dispositions:

| Decision | Recommended option | What it would permit after a separate implementation release | What remains denied/unassigned |
|---|---|---|---|
| W16-D11 / HR9-6-1 | A | Versioned four-layer mapping contracts | All institutional mappings and grants |
| W16-D12 / HR9-7-1 | A | Four source-defined delegation envelopes and non-expansion validation | All actual delegations/deputisations |
| W16-D13 / HR9-8-1 | A | Three source-defined privileged-request/decision contracts | All approvers, privilege holders and elevations |
| W16-D14 / HR9-9-1 | A | Three source-defined emergency contracts, containment and review workflow boundaries | All eligibility, declarations, sessions and emergency actions |

This decision is coherent with the controlled NCIE architecture because it extends the WP-001 zero-grant, current-authorization model; consumes WP-002 governance without broadening its authority; consumes WP-003 assurance/expiry semantics without issuing a session; preserves Zero Trust and least privilege; and keeps every missing institutional assignment fail-closed.

The selections define architecture only. They do not authorize WP-004 implementation, populate any mapping, assign any authority or activate any access capability.

## 9. Exact proposed WP-004 implementation boundary

Only after all four applicable architecture decisions are expressly recorded and a separate implementation release is issued, WP-004 may be limited to:

1. A provider-neutral, versioned role/attribute mapping schema with an empty institutional mapping registry.
2. Current mapping evaluation integrated with WP-001 object/field/action/purpose requests and fail-closed enforcement.
3. Delegation-envelope contracts for the four approved Table 11 classes, including acting identity, effective principal, scope, purpose, expiry, policy version and revocation source.
4. Non-expansion calculation that can only narrow authority and cannot create a grant absent a current underlying grant.
5. Privileged-request, approval-decision, elevation-context, expiry and revocation contracts for the three Table 13 classes, with an unassigned approval-authority boundary that denies actual elevation.
6. Emergency-declaration, eligibility, containment, auto-expiry, revocation, notification and post-event-review contracts for the three Table 15 classes, with unassigned authority/operator/reviewer boundaries that deny activation.
7. Minimized, provider-neutral security signals for attempts and decisions, without persistent audit-store or institutional Evidence claims.
8. Local unit/contract tests for missing authority, privilege escalation, scope expansion, stale mapping, delegated impersonation, revocation, expiry, self-approval, emergency overreach and post-event-review separation.
9. Traceability to the exact selected decision record, NCIE-009 Tables 9/11/13/15, NCIE-008 decision-right/SoD/emergency rules, and the WP-001 through WP-003 contracts.

Implementation must use synthetic identifiers and in-memory/local deterministic fixtures only. The reference behavior must issue no permission, delegation, privilege or break-glass grant.

## 10. Explicit WP-004 exclusions

- Institution-specific role/attribute catalogue content or mapping entries.
- Assignment of any role, attribute, permission, deputy, delegation, privilege or access grant.
- Live policy administration or authorization of an actual protected resource.
- IAM/PAM provider, directory, tenant, broker, workflow product, audit product or infrastructure selection.
- Identity, credential, token, certificate, secret, authenticator, recovery code or live session creation.
- Delegation token/session issuance, impersonation or Human credential handling.
- Privileged-session brokering, just-in-time elevation, standing access or content access.
- Emergency declaration, eligibility roster, break-glass credential, containment execution, notification delivery, reinstatement or permanent disposition.
- Numeric timeout/duration/freshness policy not explicitly supplied by a competent Human decision.
- Persistent governance, authorization, audit or Evidence store.
- External service, network, deployment, production data, governed identity data or cross-border transfer.
- Security exception/risk acceptance, independent verification, accreditation, controlled acceptance or go-live.
- WP-005 or any later WBS-16 control domain.

## 11. WP-004 stop conditions

Preparation and any later authorized implementation must stop for Human direction if:

1. any of W16-D11 through W16-D14 lacks an explicit recorded selection;
2. a requested change would populate an actual mapping or assign a holder, permission, delegation, privilege, emergency eligibility or access grant;
3. a non-delegable institutional authority must be identified but `HR8-2-1` has not supplied it;
4. an operational privileged/break-glass authority or independent reviewer must be assigned but `HR8-20-1` / `HR8-22-1` evidence is absent;
5. a duration, trigger threshold, factor, freshness window or review cadence would have to be guessed;
6. a request would permit scope union, transitive authority expansion, credential sharing, standing privilege, self-approval or self-review;
7. current identity, lifecycle, assurance, authorization, policy version, expiry or revocation state cannot be verified;
8. provider/product selection, external activation, persistent data, infrastructure, network, secret, live identity/session or governed data enters scope;
9. the implementation would claim institutional Evidence, independent verification, accreditation, acceptance, operational readiness or go-live; or
10. the controlled NCIE source or an approved predecessor decision materially changes.

The stop result is `DENY / NO CAPABILITY`, not a temporary permissive default.

## 12. Proposed WP-004 completion criteria

WP-004 may be reported locally `WORK COMPLETE` only if all of the following are evidenced after a separate implementation authorization:

1. The exact Human selections for W16-D11 through W16-D14 and the separate implementation release are recorded and represented without expansion.
2. The institution-specific mapping registry is empty; no role, attribute, permission or access grant exists.
3. Every authorization evaluation covers current object, field, action and purpose inputs and fails closed for missing, stale, invalid, revoked, expired, mismatched, error or indeterminate state.
4. Defining a role/attribute, delegation, privilege or emergency class cannot assign it or activate access.
5. All four approved delegation classes enforce their exact source scope, expiry and revocation semantics.
6. Delegated authority is never greater than the intersection of current underlying authority, delegate eligibility and delegation scope; both acting identity and effective principal remain attributable.
7. Human credentials cannot be copied into Agent/runtime Context, and technical identity cannot become Human/institutional authority.
8. All three privileged classes enforce exact named scope, current approval interface, requester/approver separation, explicit expiry, revocation and admin/content separation.
9. With privileged approval authority unassigned, every attempted actual elevation denies.
10. All three emergency classes enforce exact trigger class, named scope, explicit auto-expiry, revocation, containment ceiling, notification obligation and independent-review interface.
11. With Emergency Authority, operator or required review authority unassigned, activation and permanent disposition deny.
12. Expiry, revocation, authority change, lifecycle invalidation and policy-version change take effect without reuse of stale grants, sessions or cached decisions.
13. Negative tests demonstrate rejection of privilege escalation, scope expansion, open-ended delegation, credential delegation, self-approval, self-review, standing break-glass, missing expiry and stale authority.
14. Security signals are minimized and make no persistent-audit, Evidence or Human-decision claim.
15. No excluded provider, identity, credential, live session, governed data, external service, infrastructure or deployment is introduced.
16. Strict typing, lint, formatting, compilation, cumulative regression and reproducibility checks pass in the approved local environment.
17. Evidence distinguishes local contract testing from NCIE-016 controlled security testing, independent verification, accreditation and acceptance.
18. Traceability identifies every residual institutional assignment and operational dependency without treating silence as approval.

The maximum permissible status would be:

`WBS-16-WP-004 — WORK COMPLETE / LOCALLY VERIFIED; ZERO LIVE GRANTS; OPERATIONAL AUTHORITY ASSIGNMENT, INDEPENDENT SECURITY VERIFICATION, ACCREDITATION AND ACCEPTANCE PENDING`

## 13. Project Owner decision record

- W16-D11 selection: `A — define versioned four-layer mapping contracts; retain zero institutional mappings and zero grants`
- W16-D12 selection: `A — approve the four source-defined delegation classes as contract-eligible under strict non-expansion controls; activate no delegation`
- W16-D13 selection: `A — approve the three source-defined privileged-access classes and approval interfaces; operational approvers, privilege holders and elevations remain unassigned`
- W16-D14 selection: `A — approve the three source-defined emergency/break-glass contract classes; retain zero eligibility assignments and no emergency activation`
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`
- Decision date: `2026-09-23`
- Conditions: `All institution-specific role/attribute mappings, permissions, delegations, privileged-access authorities, privilege holders, Emergency Authorities, Break-Glass Operators, eligibility rosters, numeric durations and operational assignments remain unassigned. UNASSIGNED means NO GRANT / DENY.`
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-23-017`
- Evidence type: `Self-Authorized Project Owner Decision`
- Separate WP-004 implementation authorization: `GRANTED UNDER NCIE-WBS16-OWNER-DECISION-2026-09-23-018`
- WP-004 source-control release authorization: `GRANTED UNDER NCIE-WBS16-OWNER-DECISION-2026-09-23-019`

## 14. Source traceability

- NCIE-009 Chapter 6, Table 9 and `HR9-6-1` — current four-layer authorization and unresolved mappings.
- NCIE-009 Chapter 7, Table 11 and `HR9-7-1` — delegation classes, scope, expiry and revocation.
- NCIE-009 Chapter 8, Table 13 and `HR9-8-1` — ordinary privileged-access classes and approval interfaces.
- NCIE-009 Chapter 9, Table 15 and `HR9-9-1` — emergency classes, triggers, scope, expiry and independent review.
- NCIE-008 Chapters 3–6 — abstract Human role classes, decision-right binding, revocation, RACI, deputisation and separation of duties.
- NCIE-008 Chapters 20 and 22, including `HR8-20-1` and `HR8-22-1` — privileged/break-glass authority and emergency governance.
- NCIE-006/007 boundaries cited by NCIE-009 — delegated authorization, Human credential separation, Task/Run/Subtask scope and admin/content separation.
- `implementation/decisions/NCIE_WBS16_WP001_HUMAN_REVIEW_DECISION_PACK.md` and its approved zero-grant authorization baseline.
- `implementation/decisions/NCIE_WBS16_WP002_HUMAN_REVIEW_DECISION_PACK.md` and owner decision `NCIE-WBS16-OWNER-DECISION-2026-09-19-011`.
- `implementation/decisions/NCIE_WBS16_WP003_HUMAN_REVIEW_DECISION_PACK.md` and owner decision `NCIE-WBS16-OWNER-DECISION-2026-09-19-014`.
- `implementation/WBS16_REMAINING_SCOPE_AND_COMPLETION_CRITERIA.md`.

## 15. VPF boundary and postflight

VPF was applied behaviorally to Human-primary authority, least privilege, explainability, provenance, identity dignity, data minimization, African data residency and deny-by-default cross-border transfer. Its influence is reflected in the zero-live-grant recommendation, explicit unassigned-authority treatment and refusal to infer runtime enforcement.

No VPF runtime, validator, checksum, signature, certificate, ledger, PADCA/Omnis service, residency enforcement, quarantine action, scheduled audit or production control is claimed to have executed.
