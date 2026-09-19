# WBS-16-WP-002 Security Governance, Risk and Threat Baseline

Status: `WORK COMPLETE — LOCALLY VERIFIED; SECURITY ACCREDITATION AND ACCEPTANCE PENDING`

Prepared and implemented: `2026-09-19`

Decision prerequisites: SATISFIED by W16-D5-A and W16-D6-A under `NCIE-WBS16-OWNER-DECISION-2026-09-19-011`.

Implementation authority: `NCIE-WBS16-OWNER-DECISION-2026-09-19-012`.

Source-control release authority: `NCIE-WBS16-OWNER-DECISION-2026-09-19-013`.

## 1. Objective

Implement provider-neutral security-governance authority, independent-review, control-ownership, development-risk-appetite, threat-assumption and treatment contracts that fail closed without assigning production risk acceptance, accreditation or operational authority.

## 2. Implemented scope

1. Exact target, scope and version contracts for governed security acts.
2. Time-bounded and revocable authority assignments with an immutable local registry view.
3. Single-current-Accountable validation for the three approved Project Owner acts.
4. Qualified independent security-architecture review records and conflict/self-review rejection.
5. Security-control ownership contracts with currentness, expiry and revocation semantics.
6. Versioned W16-D6-A risk appetite across nine domains and nine explicit threat assumptions.
7. Fail-closed development-risk evaluation with no residual-risk acceptance path.
8. Bounded local experimentation only for synthetic or non-governed data without production credentials, external activation or cross-border transfer.
9. Time-bounded risk-treatment plans that cannot represent acceptance.
10. Standard-library tests, cumulative regression, traceability and local evidence.

## 3. Explicit exclusions

- Production risk acceptance or security exception acceptance.
- Security accreditation, NCIE-016 test acceptance or operational acceptance.
- Deployment, infrastructure, network or external-system activation.
- IAM/provider/product selection, credentials, live identities or governed production data.
- Persistent governance registry, workflow engine, audit store or security product.
- WP-003 identity lifecycle/authentication/session capabilities or later WBS-16 domains.
- Production acceptance or go-live authority.

## 4. Completed tasks

| Task | Implemented activity | Local evidence |
|---|---|---|
| `WBS-16-WP-002-T-001` | Governed target and authority-assignment contracts | Exact scope/version, expiry, revocation and duplicate-authority tests |
| `WBS-16-WP-002-T-002` | Independent-review and decision validation | Missing, self, conflicted, non-supporting and mismatched-review tests |
| `WBS-16-WP-002-T-003` | Security-control ownership contracts | Role, currentness and expiry validation |
| `WBS-16-WP-002-T-004` | Nine-domain development risk-appetite baseline | Completeness and no-appetite assertions |
| `WBS-16-WP-002-T-005` | Nine approved threat assumptions | Exact version/evidence and complete-enum assertions |
| `WBS-16-WP-002-T-006` | Fail-closed development-risk evaluator | Governed-data, credentials, external, cross-border, exception and unknown-domain denial tests |
| `WBS-16-WP-002-T-007` | Non-accepting risk-treatment contract | Mandatory future review and no permanent-acceptance state |
| `WBS-16-WP-002-T-008` | Full local quality and regression execution | `LOCAL-WBS16-WP002-20260919-001` |

## 5. Completion criteria and result

All twelve criteria in the approved decision pack passed locally:

1. W16-D5-A and W16-D6-A are represented without broader authority.
2. Authority/decision records bind holder, role, target, scope, version, decision and time.
3. Exactly one current Accountable authority is required.
4. Author/implementer self-acceptance and conflicted review fail closed.
5. Missing, stale, revoked, ambiguous and out-of-scope authority fails closed.
6. The risk/threat baseline is versioned and decision-traceable.
7. No-appetite domains cannot become accepted risk.
8. Unknown domains, exception requests and cross-border transfer deny or stop.
9. Positive and negative paths are tested.
10. WP-001 and all earlier WBS-15 regression tests pass.
11. Evidence remains local implementation evidence, not independent verification.
12. No excluded provider, credential, live data, infrastructure, deployment, accreditation or operational authority was introduced.

## 6. Stop conditions

Stop and request Human direction if a change requires actual risk acceptance, a security exception, production or accreditation authority, a named reviewer/registry integration, persistent governance data, provider selection, governed data, external activation, deployment, a new dependency or any WP-003 capability.

## 7. Downstream boundary

WP-002 satisfies the governance/risk prerequisites for later controlled WBS-16 packages. It does not satisfy their identity, privilege, secrets, network, DLP, incident, recovery or independent-test decisions. The next planned increment is WP-003, which requires a separate Human decision pack and implementation release.

## 8. VPF boundary

VPF requirements are applied behaviorally to Human-primary authority, least privilege, explainability, provenance, minimization, African data residency and deny-by-default cross-border transfer. No VPF runtime, validator, signature, ledger, residency-control service or accreditation is implemented or claimed.
