# NCIE WBS-16 Owner Decision — 2026-09-19-011

Status: `DECIDED — W16-D5-A / W16-D6-A`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-19-011`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-19`

Conditions: None.

## Decision selections

### W16-D5-A — HR9-1-1 / HR8-10-1 acceptance and sign-off authority

Approve Project Owner acceptance with independent technical review for the NCIE-009/WBS-16 development scope:

- Project Owner / Clive Ebo Barton-Odro is the single Accountable chapter-level NCIE-009 security-architecture sign-off authority, the acceptance authority for NCIE-009 as a development specification, and the WBS-16 implementation-completion closure authority.
- Chapter-level and final acceptance require the applicable evidence and a review record from a qualified Human Security Architecture Reviewer who is not the author/implementer and has no material conflict.
- Codex may act only as Responsible implementer when separately authorized and holds no approval, acceptance, assurance or risk-acceptance authority.
- Every sign-off binds to the named target, scope, version and time; material change requires re-review and reapproval.
- Missing, expired, conflicted or out-of-scope authority/reviewer evidence fails closed.

This resolves `HR9-1-1` for the NCIE-009/WBS-16 development scope and instantiates `HR8-10-1` only for that scope. Acceptance authorities for other NCIE-series documents, NCIE-016 test acceptance, security accreditation, production risk acceptance, operational capability releases and go-live remain separate and unassigned.

### W16-D6-A — HR9-2-1 conservative, fail-closed risk posture

Approve the conservative, fail-closed development-stage risk posture defined in the WP-002 Human Review decision pack.

NCIE has no appetite for knowingly accepting loss of Human authority, unauthorized access or privilege, cross-context disclosure, protected-data or secret exposure, stale authority, untraceable consequential action, unapproved cross-border transfer, or bypass of current security decisions. Limited delivery friction and reduced availability are acceptable when required to preserve fail-closed security. Local experimentation is limited to isolated, reversible, non-production use with synthetic or non-governed data, no production credentials and no external activation.

The approved baseline threat assumptions include external attackers, stolen or stale credentials, malicious or compromised insiders, compromised third parties, adversarial or manipulated Agents/models/Tools, prompt injection, cross-context attacks, compromised dependencies/artifacts/recovery media, changing authorization/security state, and fail-closed handling of missing, indeterminate, conflicting or unverifiable security state.

`No appetite` does not assert zero probability. It prohibits knowingly treating the risk as normal accepted operation. Any future exception or residual-risk acceptance requires separately assigned Human authority, exact scope, rationale, compensating controls, expiry and review. Quantitative thresholds, named products, domain-specific exception authorities and production risk acceptance remain for later decisions.

## Authority boundary

This decision satisfies the Human decision prerequisites for preparing the exact WP-002 implementation scope. It does **not** authorize implementation.

A separate explicit Project Owner decision naming `WBS-16-WP-002 Security Governance, Risk and Threat Baseline` is required before source code, tests or implementation evidence may be created for that package.

No provider selection, credential or live-identity handling, governed production data, external-system activation, infrastructure change, production deployment, security accreditation, operational acceptance or go-live is authorized.

## Provenance note

Codex recorded the natural-person identity and institutional-authority assertion supplied by the user. Codex did not independently verify that identity or authority.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, provenance, data minimization, African data residency and deny-by-default cross-border transfer. This record does not claim execution of any VPF runtime control.
