# NCIE-017 Controlled Implementation Plan

Status: IN PROGRESS (controlled implementation); TEST PENDING; ACCEPTANCE PENDING

Controlling execution instruction: `NCIE_to_Codex_Master_Production_Instruction_v1_0`

Controlled implementation corpus: `NCIE PRODUCTION SUIT.zip`

## 1. Preflight record

- Corpus SHA-256: `0AF83D97990F18668D7E4A14DD80191E1575C6ADEF2E7EC692B1137B301EE846`.
- Master instruction PDF SHA-256: `12DF841D9E2D083ADC83709A39210D1F942E005C3765465C5DA28BD06EBB8FB2`.
- Corpus inventory: 18/18 current `Final Docs` PDFs and 38 supporting files are readable.
- The 18 controlled PDFs in the archive byte-match the repository copies under `Final Docs/`.
- The archive contains the Implementation Entry Gate, amendment verification reports, and change registers.
- The archive does not contain `NCIE_Documentation_Suite_Production_Ready_v3_0_RECONCILED`; a repository copy exists outside the controlled archive. This is a suite-index provenance gap. It does not block the scoped work below because the Master Production Instruction enumerates all 18 current filenames and those exact artifacts are present and readable, but the external copy is not treated as part of the controlled archive.
- Repository at preflight: documentation/generation scripts only; no application source tree, dependency manifest, build manifest, or CI configuration existed. Branch `main` matched `origin/main` at commit `3b3edc2f159ed9b35bdfce27b848be9f6b2d2280` before this increment.
- Pre-existing untracked artifact `NCIE_to_Claude_Master_Production_Instruction_v1_0.pdf` is outside this increment and remains untouched.
- Available local scaffold runtime: Node.js `v25.1.0`, npm `11.6.2`. This increment adds no third-party dependency and performs no network access.

## 2. Authority and status boundary

The Master Production Instruction governs execution behavior and expressly authorizes dependency-ready, source-grounded implementation. NCIE-017 remains substantive sequencing authority. Its historical statement that the roadmap itself did not start implementation is preserved as a document-status boundary; this increment relies on the later Master Production Instruction for execution authority. Neither source is treated as test pass, production acceptance, or go-live authority.

NCIE-017 defines controlled workstream identifiers at `WBS-15` through `WBS-24`. D3-A under `NCIE-WBS15-OWNER-DECISION-2026-09-17-001` approved stable subordinate work-package and task identifiers without renumbering those workstreams. WP-003 through WP-005 are permitted identifiers, but preparation does not itself authorize implementation.

## 3. Workstream readiness and blocker handling

| WBS | Preflight state | Exact dependency or blocker | Permitted action now |
|---|---|---|---|
| WBS-15 Foundation / Platform | IMPLEMENTATION COMPLETE / DOWNSTREAM-READY — CONTROLLED VERIFICATION AND ACCEPTANCE PENDING | D9-A approved under `NCIE-WBS15-OWNER-DECISION-2026-09-18-006`; WP-001 through WP-005 work-complete | Preserve the closure boundary; do not infer security accreditation, production deployment, acceptance or go-live authority. |
| WBS-16 Security, IAM & Governance | IN PROGRESS — WP-001 THROUGH WP-010 WORK COMPLETE / LOCALLY VERIFIED / CONTROLLED SOURCE RELEASED | WP-010 released under `...-037`; no WBS-16 closure decision exists | Preserve zero grants/capabilities and exact test-state separation; require the separate final Human closure decision. |
| WBS-17 Data, Database & Storage | BLOCKED | WBS-15/WBS-16 predecessors; `HR17-17-1`; upstream HR14 family | No physical schema or persistence selection. |
| WBS-18 API, Integration & Connector | BLOCKED | WBS-16/WBS-17 predecessors; `HR17-18-1`; provider/source discovery | No connector or external contract implementation. |
| WBS-19 ARGUS, Memory, Agent & AI | BLOCKED | WBS-16/WBS-17 predecessors; `HR17-19-1`; Gate A/B, sandbox, and sovereignty prerequisites | No Agent/AI activation or runtime implementation. |
| WBS-20 Evidence, Provenance & Audit | BLOCKED | WBS-16/WBS-17 predecessors; `HR17-20-1`; upstream HR10 family | No institutional Evidence state or custody implementation. |
| WBS-21 Functional Modules | BLOCKED | WBS-17/WBS-18/WBS-20 predecessors; `HR17-21-1`; upstream HR13 rules/KPIs | No domain rules, thresholds, Findings, or Decisions. |
| WBS-22 UX/UI & Design System | DEPENDENCY-READY (scaffold scope only) | NCIE-017 §22.1 permits early design-system/shell work with mock states; `HR17-22-1`, `HR12-5-1`, and `HR12-8-1` are Non-Blocking for the stated interim primitives | Build a reversible, framework-neutral semantic contract and mock shell fixture. |
| WBS-23 DevSecOps / Infrastructure | BLOCKED | WBS-15/WBS-16 predecessors; `HR17-23-1`; hosting/source-control/platform decisions | No environment topology, pipeline, runner, or deployment target. |
| WBS-24 Testing / Verification | TEST PENDING | Workstream-specific implementation plus NCIE-016 environment/authority prerequisites | Local structural checks may run; they are implementation evidence, not execution of the controlled NCIE-016 acceptance programme. |

## 4. WBS-22 safe-scaffold boundary

Included:

- NCIE-012 Chapter 5 shell composition primitives.
- NCIE-012 Chapters 7-8 brand-neutral token taxonomy and semantic/accessibility component states.
- Explicit separation of control availability, authorization state, Human approval state, and Evidence state.
- Explicit mock-data provenance and non-authoritative labels.
- Local deterministic structural checks with no external service or governed data.

Excluded and blocked:

- Brand palette, logo, font, imagery, and icon brand: `HR12-7-1`.
- Top-level navigation labels/terminology: `HR12-4-1`.
- Supported form factors and breakpoints: `HR12-6-1`.
- Named accessibility conformance level and representative-user acceptance: `HR12-29-1`, `HR16-22-1`.
- Live authorization, Evidence, governance, Agent, VPF, API, or domain state.
- React/package selection as an institutional commitment. NCIE-004 `TD-6-1` remains a Non-Blocking Proposed Design Default; this scaffold stays framework-neutral and reversible.

Minimum Human decisions needed to unblock the excluded scopes are the decisions named by the HR items above. No default is selected in their place.

## 4A. WBS-15-WP-001 released scope

The Project Owner selections D1-A, D2-A, D3-A and D4-A were supplied and recorded on 2026-09-17 under `NCIE-WBS15-OWNER-DECISION-2026-09-17-001`. Codex recorded the supplied authority assertion but did not independently verify identity or institutional authority.

Authorized implementation is limited to local repository/application structure, a type-annotated Python service foundation, secret-reference configuration, health/readiness interfaces, structured logging, telemetry hooks, unit/contract tests and traceability. Production hosting, live credentials/data, external integrations, blocked product selections, WBS-16 completion, acceptance and go-live remain excluded.

The implementation exists under `implementation/wbs-15-wp-001-foundation-service/`. Python 3.14.7 and PyPI were approved under `NCIE-WBS15-OWNER-DECISION-2026-09-17-002`; development dependencies are exact-version and SHA-256 locked. Strict mypy, Ruff lint/format, compilation and 8 unit/contract tests passed locally under run `LOCAL-WBS15-WP001-20260917-002`. The package is `WORK COMPLETE`; controlled NCIE-016 verification and acceptance remain pending.

## 4B. WBS-15-WP-002 prepared scope

Owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-18-001` authorized preparation of `WBS-15-WP-002`. D5-A under `NCIE-WBS15-OWNER-DECISION-2026-09-18-002` subsequently released the exact prepared scope for local implementation.

The prepared package is `WBS-15-WP-002 Local Service Composition and Lifecycle Contracts`. It proposes a typed local composition root, provider-neutral lifecycle contract, aggregate fail-closed readiness registry, configuration startup validation, deterministic in-process test harness, tests, traceability and evidence. It proposes no new runtime dependency and preserves the approved Python 3.14.7 and locked-development-environment boundary.

The package explicitly excludes production deployment, network server selection, security-provider integration, databases, connectors, live credentials/data, institutional Evidence, domain rules, ARGUS/AI runtime, infrastructure, and controlled acceptance. The authorized source scope is implemented with no new dependency. Strict typing, lint, formatting, compilation and all 19 combined WP-001/WP-002 tests passed under `LOCAL-WBS15-WP002-20260918-001`. Package status is `WORK COMPLETE`; controlled NCIE-016 verification and acceptance remain pending.

## 4C. WBS-15 remaining foundation packages

Owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-18-004` resolves `HR17-15-1` for the WBS-15 foundation boundary: retain framework-neutral ASGI; provide identity interfaces while deferring IAM to WBS-16; implement neutral observability semantics while deferring products/deployment to WBS-23; retain Python 3.14.7, virtual environments and locked pip without additional tooling absent a separately approved demonstrated need.

The same decision authorizes preparation only of:

- `WBS-15-WP-003` — Request, Identity and Application Extension Contracts;
- `WBS-15-WP-004` — Observability Semantic Foundation;
- `WBS-15-WP-005` — Reproducible Service Template and WBS-15 Closure.

Owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-18-005` released all three packages in controlled order. WP-003 implemented request, identity-interface and route-extension contracts; WP-004 implemented provider-neutral observability semantics; WP-005 completed offline clean-environment reproducibility, consolidated traceability, downstream handover and the completion report. The clean run passed strict typing/lint/format/compilation, 31 cumulative tests and the template verifier. All three packages are locally `WORK COMPLETE`.

Owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-18-006` approved D9-A. WBS-15 is therefore `IMPLEMENTATION COMPLETE / DOWNSTREAM-READY; CONTROLLED VERIFICATION AND ACCEPTANCE PENDING`. The WBS-16 predecessor condition is satisfied. Owner decision `NCIE-WBS16-OWNER-DECISION-2026-09-18-008` subsequently satisfied the scoped WP-001 decisions, and `NCIE-WBS16-OWNER-DECISION-2026-09-18-009` released their exact implementation scope. All deferred HR9 capabilities, security accreditation, production deployment, controlled acceptance and go-live remain pending.

## 4D. WBS-16-WP-001 implemented scope

The first WBS-16 increment is prepared as `WBS-16-WP-001 Security Principal and Authorization Contract Foundation`. It is limited to provider-neutral principal/source contracts, four-layer current-authorization contracts, deny-all reference behavior, enforcement adaptation, bounded neutral signals and local tests. It introduces no IAM provider, credential/session handling, role mapping, access grant, infrastructure, persistent audit store or production control.

Owner decision `NCIE-WBS16-OWNER-DECISION-2026-09-18-008` approves W16-D1-A through W16-D4-A: the bounded first-increment prerequisites, seven provider-neutral principal categories, four-layer deny-by-default authorization with zero grants, and scoped deferral of all remaining HR9 decisions for WP-001 only. Owner decision `NCIE-WBS16-OWNER-DECISION-2026-09-18-009` released that exact package for implementation.

WP-001 is locally `WORK COMPLETE`. It implements typed principal/source and current-authorization contracts, the zero-grant deny-all decision point, fail-closed WBS-15 enforcement adaptation and minimized security signals. Strict typing/lint/format/compilation passed across the controlled scope; 40 cumulative tests and the WBS-15 template verifier passed. No provider, credential, session, role/attribute mapping, permission, access grant, external service, infrastructure or deployment was introduced. The broader WBS-16 workstream, deferred HR9 decisions, independent security verification, accreditation and controlled acceptance remain open.

## 4E. WBS-16 remaining controlled sequence

The review-only remaining-scope plan is recorded in `implementation/WBS16_REMAINING_SCOPE_AND_COMPLETION_CRITERIA.md`. It proposes WP-002 through WP-010 in controlled order: governance/risk; identity/authentication/session; authorization/delegation/privileged access; secrets/cryptography/network; Agent/model/Tool/context isolation; DLP/protected identity; logging/detection/incident controls; supply chain/vulnerability/recovery; and cumulative security-verification handover/closure.

The plan itself authorizes no package. Each requires its named HR9 decisions and a separate implementation release. WP-002 through WP-010 received those separate authorities. WP-010 architecture decisions W16-D30-A through W16-D34-A were recorded under `NCIE-WBS16-OWNER-DECISION-2026-09-25-035`, the bounded contract-only implementation was released under `...-036`, and controlled source release was authorized under `...-037`. WBS-16 remains `IN PROGRESS`; the separate final Human closure decision remains absent. Its maximum recommendation retains independent verification, accreditation, controlled acceptance and go-live as pending.

The decided WP-009 Human Review Decision Pack is recorded at `implementation/decisions/NCIE_WBS16_WP009_HUMAN_REVIEW_DECISION_PACK.md`. W16-D27-A through W16-D29-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-032`, owner decision `...-033` released the exact zero-capability implementation, and `...-034` authorized controlled source release. WP-009 is `WORK COMPLETE / CONTROLLED SOURCE RELEASED`: thirty empty registries, forty-two unassigned authority classes, immutable synthetic contracts, fail-closed evaluators and inert no-artifact-action/no-remediation/no-recovery boundaries are implemented. Strict typing, lint, formatting and in-memory compilation passed; 280 cumulative tests and the template verifier passed. Implementation commit `a3a222bea9bf0ed00b82ac4d69d19526eed5b9f4` was pushed to `origin/main` and independently verified. No artifact action, vulnerability/risk acceptance, remediation, recovery, product selection, dependency, infrastructure or deployment was introduced.

The decided WP-010 Human Review Decision Pack is recorded at `implementation/decisions/NCIE_WBS16_WP010_HUMAN_REVIEW_DECISION_PACK.md`. Owner decision `...-035` approved W16-D30-A through W16-D34-A, `...-036` released the exact contract-only implementation, and `...-037` authorized controlled source release. WP-010 is `WORK COMPLETE / CONTROLLED SOURCE RELEASED` at implementation commit `3ca9a4457bf271c6c964bde172ca4d914498d872`: nine SEC-T specifications, five distinct states, ten empty registries, unassigned authorities, eighteen protections, twenty-eight HR9 dispositions, bidirectional WP traceability and three downstream handovers are implemented. Strict typing, lint, formatting and in-memory compilation passed across 39 files; 310 cumulative tests and the template verifier passed. No controlled test, independent verification, accreditation, acceptance, product/environment selection, deployment, go-live or WBS-16 closure occurred. The final Human closure pack remains `UNDECIDED`.

W16-D5-A (`HR9-1-1` / scoped `HR8-10-1`) and W16-D6-A (`HR9-2-1`) were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-19-011`. Owner decision `...-012` released WP-002 for implementation. WP-002 is locally `WORK COMPLETE`: provider-neutral authority, independent-review, control-ownership, risk-appetite, threat-assumption, risk-treatment and fail-closed development-risk contracts are implemented; 52 cumulative tests and the local quality/template gates passed. No production risk acceptance, accreditation, provider, credential, governed production data, external activation, infrastructure or deployment was introduced.

Owner decision `NCIE-WBS16-OWNER-DECISION-2026-09-19-013` authorized the controlled commit and push of the exact WP-002 implementation, traceability and evidence increment. Commit `9ec291a6044bf8c837da514ed2cb693da0477357` was pushed successfully to `origin/main` and matched the remote branch on independent verification. The release grants no broader implementation, accreditation, deployment or go-live authority.

W16-D15-A through W16-D17-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-23-020`; owner decision `...-021` released the exact WP-005 contract-only implementation. WP-005 is locally `WORK COMPLETE`: opaque references, non-executing lifecycle metadata, unassigned authority interfaces, prohibited-surface controls, conceptual cryptographic policy, seven logical zones, five egress classes and fail-closed evaluation are implemented. The controlled cryptographic/egress registries are empty; 105 cumulative tests and all local quality/template gates passed. No protected material, algorithm/product, authority assignment, destination, route, exception grant, network activation, external call or cross-border transfer was introduced. WP-006 through WP-010 were later separately released and locally completed; WP-010 source release and final WBS-16 closure remain unauthorized.

W16-D18-A through W16-D21-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-023`; owner decision `...-024` released the exact WP-006 implementation. WP-006 is locally `WORK COMPLETE`: provider-neutral immutable contracts, four empty registries, unassigned authority interfaces and inert Agent/model/Tool/Context boundaries are implemented. Strict typing, lint, formatting and compilation passed; 134 cumulative tests and the template verifier passed. `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`; no Agent, generated executable code, provider/model route, Tool, cross-context transfer, network, governed production data, dependency, infrastructure or deployment was introduced.

W16-D22-A and W16-D23-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-026`; owner decision `...-027` released the exact WP-007 implementation. WP-007 is locally `WORK COMPLETE`: provider-neutral immutable contracts, six empty registries, unassigned authorities and inert no-output/no-reveal/Human-escalation boundaries are implemented. Strict typing, lint, formatting and compilation passed; 172 cumulative tests and the template verifier passed. No real identity, governed data, disclosure, output, reveal, channel, destination, exception, cross-border transfer, product/provider, network capability, dependency, infrastructure or deployment was introduced. WP-008 through WP-010 were later separately released and locally completed; WP-010 source release and final WBS-16 closure remain unauthorized.

W16-D24-A through W16-D26-A were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-24-029`; owner decision `...-030` released the exact WP-008 zero-capability implementation, and `...-031` authorized its controlled source release. WP-008 is locally `WORK COMPLETE / CONTROLLED SOURCE RELEASED`: immutable provider-neutral metadata contracts, eleven empty registries, unassigned authorities, a synthetic non-persistent collector and inert no-monitor/no-notification/no-incident-command/no-containment-recovery boundaries are implemented. Strict typing, lint, formatting and in-memory compilation passed; 224 cumulative tests and the template verifier passed. Commit `ba126b73eb3dea4fd55cfb59b11e43a42623d33c` was pushed to `origin/main` and independently verified. No real log/event/incident, persistent audit/Evidence store, retention period, severity taxonomy/threshold, monitoring, alerting, paging, notification, response execution, operational assignment, product/provider, external destination, dependency, infrastructure or deployment was introduced. WP-009 and WP-010 were later separately released and locally completed; WP-010 source release and final WBS-16 closure remain unauthorized.

W16-D7-A (follow-on `HR9-3-1`), W16-D8-A (`HR9-4-1`), W16-D9-A (`HR9-5-1`) and W16-D10-A (`HR9-10-1`) were approved under `NCIE-WBS16-OWNER-DECISION-2026-09-19-014`. Owner decision `...-015` released their exact provider-neutral implementation scope. WP-003 is locally `WORK COMPLETE`: symbolic proofing/lifecycle/assurance, explicit-expiry session/credential metadata, recovery/revocation and fail-closed authority/issuer contracts are implemented; 68 cumulative tests and local quality/template gates passed. No provider, credential issuance, live authentication, operational IAM, infrastructure or deployment was introduced. WP-004 through WP-009 were subsequently released and locally completed under their own recorded decisions; WP-010 remains blocked.

## 5. Verification mapping

| Controlled test reference | Mapping for this increment | Status |
|---|---|---|
| NCIE-012 `UX-T3` Keyboard/Screen-Reader | Structural checks for landmarks, accessible names, explicit disabled state, and non-colour text cues | TEST PENDING under NCIE-016; local checks may execute |
| NCIE-012 `UX-T4` Responsive | No breakpoint is implemented because `HR12-6-1` is open | BLOCKED for controlled execution |
| NCIE-012 `UX-T5` Security-State | Mock fixture keeps availability separate from authorization and labels state non-authoritative | TEST PENDING under NCIE-016; local checks may execute |
| NCIE-012 `UX-T8` Regression | Local Node test protects the scaffold invariants | TEST PENDING under NCIE-016; local check may execute |
| NCIE-016 Chapter 22 | Accessibility level and representative-user groups require `HR16-22-1` | BLOCKED for acceptance/conformance claim |

Local test success means only that the checked scaffold invariants held in the recorded local run. It does not establish accessibility conformance, representative-user validation, security validation, production acceptance, or go-live authority.

## 6. Increment evidence requirements

At increment close, record:

- changed artifacts and the exact WBS/NCIE references;
- local command, runtime, time, and actual result;
- unresolved limitations and blocker status;
- security/provenance observations;
- next dependency-ready scope.
