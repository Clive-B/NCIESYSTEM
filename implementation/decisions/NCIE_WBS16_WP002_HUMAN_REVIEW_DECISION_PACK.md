# NCIE WBS-16-WP-002 Human Review Decision Pack

Status: `DECIDED — W16-D5-A / W16-D6-A; IMPLEMENTATION RELEASED SEPARATELY UNDER ...-012`

Prepared: `2026-09-19`

Decided: `2026-09-19`

Proposed work package: `WBS-16-WP-002 Security Governance, Risk and Threat Baseline`

## 1. Purpose

This pack presents the minimum Human decisions required before WP-002 may be considered for a separate implementation release. It covers:

- `HR9-1-1`, together with its upstream duplicate `HR8-10-1`: acceptance authority for NCIE-009 and chapter-level security-architecture sign-off authority; and
- `HR9-2-1`: institutional risk appetite and the unresolved threat assumptions that the WBS-16 security baseline must preserve.

Selecting options in this pack resolves architecture/governance prerequisites only. It does **not** authorize source implementation, external services, production controls, security accreditation, operational acceptance or go-live.

## 2. Controlling source findings

The source chain establishes the following constraints:

1. NCIE-009 enforces approved institutional authority; it does not create acceptance, sign-off or risk-acceptance authority.
2. Acceptance is a distinct institutional act. It cannot be inferred from implementation, local test success, independent review, accreditation or another approval.
3. Every decision binds to an identified Human or institutional function, an exact target, scope, version and time.
4. The acceptance approver must not be the author/implementer of the same target. A reviewer must be appropriately qualified, independent and free of material conflict.
5. Exactly one Accountable authority applies to each governed function unless a separately approved exception permits otherwise.
6. NCIE-009 requires Zero Trust, least privilege, assume breach, defense in depth and explicit current verification. It identifies external attackers, compromised credentials, malicious or compromised insiders, compromised third-party providers and adversarial or unintentionally harmful Agent/model behavior as threat actors.
7. A security control, test result, VPF disposition or generated statement is not Human approval or institutional acceptance.

## 3. Decision W16-D5 — HR9-1-1 / HR8-10-1 acceptance and sign-off authority

### Option A — Project Owner acceptance with independent technical review (recommended)

Approve the following scoped authority model for NCIE-009 and WBS-16:

| Governed act | Accountable / sign-off authority | Required input | Boundary |
|---|---|---|---|
| Chapter-level NCIE-009 security-architecture sign-off | Project Owner / Clive Ebo Barton-Odro | Chapter evidence and a review record from a qualified Human Security Architecture Reviewer who is not the author/implementer | Sign-off applies only to the named chapter, version and scope |
| Acceptance of NCIE-009 as a development specification | Project Owner / Clive Ebo Barton-Odro | All 28 chapter dispositions, consolidated HR register, independent review record and limitations statement | Does not constitute accreditation or operational acceptance |
| WBS-16 implementation-completion closure | Project Owner / Clive Ebo Barton-Odro | WP-010 completion report, traceability, local test evidence, residual-risk register and independent-verification handover | Maximum status remains implementation-complete/downstream-ready |
| Implementation of an authorized WP | Codex as Responsible implementer only when separately authorized | Exact package implementation release | Codex holds no approval, acceptance, assurance or risk-acceptance authority |

Under this option:

- the Project Owner is the single Accountable acceptance/sign-off authority for the scoped development targets;
- the independent reviewer provides technical review evidence but does not acquire institutional acceptance authority merely by reviewing;
- the author/implementer cannot sign off or accept their own work;
- a reviewer identity, qualification, independence declaration, target and review time must be recorded before the dependent final sign-off;
- material changes to a signed target require re-review and reapproval;
- absence, expiry or conflict of the required authority/reviewer evidence fails closed; and
- security accreditation, NCIE-016 test acceptance, production risk acceptance, operational capability release and go-live authority remain separate and unassigned.

This selection resolves `HR9-1-1` for the NCIE-009/WBS-16 development scope and instantiates `HR8-10-1` only for that scope. It does not resolve acceptance authorities for other NCIE-series documents or operational capability releases.

### Option B — Split Project Owner acceptance from a separate chapter-sign-off authority

The Project Owner remains the acceptance authority for NCIE-009 as a whole and WBS-16 implementation closure, while a separately named institutional Security Architecture Approver becomes the Accountable chapter-level sign-off authority.

Selection requires the Human reviewer to supply the institutional function and current holder, scope, effective date, deputisation/vacancy rule and independence constraints. Until those details are recorded, chapter-level sign-off remains unavailable and WP-002 implementation must represent it as unassigned.

### Option C — Defer authority assignment

Keep `HR9-1-1` / `HR8-10-1` open. WP-002 and any acceptance/sign-off dependent work remain blocked; WP-001's deny-by-default foundation is preserved without extension.

Recommendation: **W16-D5-A**, because it assigns a clear Human Accountable authority for the current development stage while preserving independent technical review, segregation of duties and separate future accreditation/production authorities.

## 4. Decision W16-D6 — HR9-2-1 risk appetite and threat assumptions

### Option A — Approve the conservative, fail-closed development posture (recommended)

Approve the following institutional risk-appetite statement for WBS-16 development:

> NCIE has no appetite for knowingly accepting loss of Human authority, unauthorized access or privilege, cross-context disclosure, protected-data or secret exposure, stale authority, untraceable consequential action, unapproved cross-border transfer, or bypass of current security decisions. For the controlled local-development stage, NCIE accepts limited delivery friction and reduced availability when necessary to preserve fail-closed security. Bounded experimentation is permissible only with synthetic or non-governed data, no production credentials, no external activation and no claim of operational acceptance.

For this statement, `no appetite` means the risk may not be knowingly accepted as normal operation. It does not claim that occurrence probability is zero. Any future exception requires separately assigned Human risk-acceptance authority, exact scope, rationale, compensating controls, expiry and review; WP-002 does not grant that authority.

| Risk domain | Appetite for the controlled WBS-16 development stage | Required interim response |
|---|---|---|
| Human authority, decision provenance and non-substitution | None | Deny or stop when authority is missing, stale, ambiguous or technically inferred |
| Unauthorized access, privilege escalation and break-glass misuse | None | Zero grants unless a later package carries current explicit authority |
| Cross-context, protected-identity, confidential-data or secret disclosure | None | Isolate, minimize and deny unknown or unauthorized disclosure |
| African data residency and cross-border transfer | None without separately evidenced authorization | Keep governed identity/security data local; deny unapproved external transfer |
| Supply-chain or artifact-integrity uncertainty | None for trusted/releasable status | Quarantine or reject unverified artifacts; do not infer provenance |
| Security-control bypass or untraceable consequential action | None | Stop and require a governed Human decision |
| Availability and delivery continuity | Low | Prefer safe degradation or denial over insecure continuity |
| Local experimentation | Limited | Synthetic/non-governed data only; isolated, reversible and non-production |
| Residual implementation risk | Low and explicitly bounded | Record owner, scope, evidence, treatment, expiry and downstream verification gate |

Approve these threat assumptions for the WBS-16 baseline:

1. No identity, network location, workload, service, Agent, model, Tool, data path, artifact, provider or restored state is trusted solely by placement or prior success.
2. External attackers, stolen or stale credentials, malicious or compromised insiders and compromised third parties are in scope.
3. Agents, models and Tools may behave adversarially or be manipulated, including through prompt injection and Tool misuse.
4. Authorization, consent, classification, delegation and security state can change; prior or cached state is not current authority.
5. Cross-context access and mixed-authority data paths are hostile unless explicitly and currently authorized.
6. Dependencies, generated code, build artifacts and recovery media may be compromised until provenance and current eligibility are verified.
7. Missing, indeterminate, conflicting or unverifiable security state fails closed.
8. Local test success does not establish independent security verification, accreditation, production readiness or acceptance.
9. External-provider, production-load and operational threat assumptions remain unvalidated until the corresponding provider, infrastructure and deployment decisions are separately approved and tested.

Quantitative thresholds, named control products and domain-specific exception authorities remain for their applicable later HR9 decisions. Their absence must not be interpreted as permission or residual-risk acceptance.

### Option B — Approve a tailored risk posture

Return an amended appetite table or threat-assumption list. Every relaxation must identify the affected domain, permissible exposure, decision authority, compensating controls, duration and downstream verification requirement. Implementation remains blocked until the amendments are precise enough to encode and test.

### Option C — Defer risk appetite and threat assumptions

Keep `HR9-2-1` open. WP-002 and later control packages remain blocked because Codex may not invent institutional risk tolerance.

Recommendation: **W16-D6-A**, because it turns the existing Zero-Trust and Human-primary boundaries into an explicit development-stage posture without claiming that production risk has been assessed or accepted.

## 5. Proposed WP-002 implementation boundary

With W16-D5-A and W16-D6-A now decided, a later, separate implementation authorization may release a bounded package containing:

- provider-neutral authority-assignment, sign-off-target and decision-evidence contracts;
- risk-appetite, threat-assumption, risk-disposition and control-owner contracts;
- validation of target/scope/version binding, current authority, single accountability and segregation of duties;
- fail-closed handling for missing, stale, conflicted or unassigned authority and unknown risk disposition;
- local negative-path tests and traceability to the two decisions; and
- an explicit handover for later accreditation, operational risk acceptance, incident command and NCIE-016 independent testing.

The package would exclude:

- approval or modification of NCIE-009 itself;
- assignment of production, accreditation, NCIE-016 test-acceptance or operational-release authority;
- acceptance of any actual residual risk or security exception;
- IAM/provider/product selection, credentials, live identities or governed production data;
- deployment, infrastructure, external-system activation or production control; and
- implementation of WP-003 or any later WBS-16 control domain.

## 6. Proposed WP-002 acceptance criteria

WP-002 may be reported locally work-complete only if:

1. the recorded W16-D5 and W16-D6 selections are represented without broadening their scope;
2. every authority/decision record binds holder, role, target, scope, version, decision and time;
3. exactly one Accountable authority applies to each represented governed function;
4. author/implementer self-acceptance and conflicted review are rejected;
5. missing, stale, revoked, ambiguous or out-of-scope authority fails closed;
6. risk appetite and threat assumptions are versioned and traceable;
7. `no appetite` domains cannot be silently converted into accepted risk;
8. unknown risk disposition, missing exception authority and unapproved transfer resolve to denial/stop;
9. tests demonstrate the negative paths as well as valid contract construction;
10. WP-001 regressions and all approved local quality gates pass;
11. evidence distinguishes local implementation testing from independent security verification; and
12. no excluded provider, credential, live data, infrastructure, deployment, accreditation or operational authority is introduced.

## 7. Recorded decision

- W16-D5 selection: `A — Project Owner acceptance with independent technical review`
- W16-D6 selection: `A — conservative, fail-closed risk posture`
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`
- Decision date: `2026-09-19`
- Conditions: `None`
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-19-011`

The decision is recorded in `implementation/decisions/NCIE_WBS16_OWNER_DECISION_2026-09-19-011.md`. The exact WP-002 scope was subsequently released for implementation under `NCIE-WBS16-OWNER-DECISION-2026-09-19-012`; that release did not authorize production risk acceptance, accreditation, deployment, commit or push.

## 8. Source traceability and VPF boundary

- NCIE-009 Chapter 1 and `HR9-1-1`.
- NCIE-009 Chapter 2 and `HR9-2-1`.
- NCIE-009 Chapter 27 deduplication and Blocking-scope rules.
- NCIE-008 Chapters 4, 5, 6, 9 and 10, including `HR8-10-1`.
- `implementation/WBS16_REMAINING_SCOPE_AND_COMPLETION_CRITERIA.md`.
- Owner decisions `NCIE-WBS16-OWNER-DECISION-2026-09-18-008` through `...-010` and `NCIE-WBS16-OWNER-DECISION-2026-09-19-011` through `...-012`.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, provenance, dignity, minimization, African data residency and deny-by-default cross-border transfer. No VPF runtime, signature, ledger, validator, residency control or enforcement service is claimed to have executed.
