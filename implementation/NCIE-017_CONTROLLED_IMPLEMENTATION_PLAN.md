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

NCIE-017 defines controlled workstream identifiers at `WBS-15` through `WBS-24`, but its lower-level identifier convention remains blocked by `HR17-6-1`. This plan therefore does not fabricate a subordinate controlled work-package ID. The first increment is referenced by its existing authority and scope: **WBS-22 / NCIE-017 Chapter 22.1 safe scaffold**.

## 3. Workstream readiness and blocker handling

| WBS | Preflight state | Exact dependency or blocker | Permitted action now |
|---|---|---|---|
| WBS-15 Foundation / Platform | IN PROGRESS | D1-A/D2-A/D3-A recorded under `NCIE-WBS15-OWNER-DECISION-2026-09-17-001` | Implement `WBS-15-WP-001` local Python foundation within the recorded exclusions. |
| WBS-16 Security, IAM & Governance | BLOCKED | WBS-15 predecessor; `HR17-16-1`; upstream HR9 family | No security implementation or policy default. |
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
