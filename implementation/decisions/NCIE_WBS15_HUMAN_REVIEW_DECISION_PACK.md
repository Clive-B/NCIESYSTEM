# NCIE WBS-15 Human Review Decision Pack

Status: FOR HUMAN DECISION — NO DECISION RECORDED

Purpose: obtain only the minimum Human-controlled decisions required to move the affected WBS-15 scope from `BLOCKED` to `DEPENDENCY-READY`. This pack does not itself approve any option.

## Authority and source references

- Master Production Instruction rules 5-10: architecture fidelity, no silent invention, scoped blockers, safe scaffolding, and change control.
- NCIE-017 Chapter 6 / `HR17-6-1`: WBS hierarchy and identifier convention.
- NCIE-017 Chapter 15 / `HR17-15-1`: foundation technology decisions that block sequencing.
- NCIE-004 Chapter 5 / `TD-5-1`: primary backend runtime.
- NCIE-004 Chapter 35: Blocking decisions must close before the affected technology is treated as settled; Non-Blocking Proposed Design Defaults may support provisional development without becoming institutional technology approval.
- VPF behavioral boundary: Human authority remains primary; sovereignty and production approval cannot be inferred from technical success.

## Decision D1 — Primary backend runtime

Source blocker: NCIE-004 `TD-5-1`; NCIE-017 `HR17-15-1`.

Decision required: select the primary backend runtime family for the first WBS-15 implementation increment.

### Option A — Python, type-checked

- Matches the NCIE-004 proposed/default position for domain and AI-adjacent services.
- Allows the NCIE-004 FastAPI proposal (`TD-5-2`) to be used provisionally.
- Does not approve a Python version, package source, production hosting model, or procurement decision.

### Option B — TypeScript/Node.js

- Matches the NCIE-004 alternative where frontend-adjacent team unification is preferred.
- Would require the implementation plan and test-tool mapping to use the Node.js backend path.
- Does not approve a Node.js version, package source, production hosting model, or procurement decision.

### Option C — Another runtime

- Requires a change request under Master Production Instruction rule 10.
- The request must record affected NCIE references, alternatives, implementation/test/security impact, and rollback implications before coding.

Recommendation: **Option A**, because it is the documented NCIE-004 primary proposed/default position and aligns with the planned domain/AI-adjacent services. This is a recommendation only.

Decision record:

- Selected option: `PENDING`
- Decision authority: `PENDING`
- Decision date: `PENDING`
- Conditions/limitations: `PENDING`
- Evidence or meeting reference: `PENDING`

## Decision D2 — Scope of WBS-15 implementation authorization

Source blocker: NCIE-017 `HR17-15-1`.

Decision required: confirm whether Codex may begin a local/development WBS-15 foundation increment after D1 is approved.

### Option A — Approve scoped development implementation

Authorizes:

- repository/application structure;
- backend service template using the D1 runtime;
- configuration model with secret references only;
- health/readiness interfaces;
- structured logging and OpenTelemetry instrumentation hooks;
- local unit and contract tests;
- implementation evidence and traceability.

Does not authorize:

- production hosting or deployment;
- live credentials, production data, or external-system access;
- institutional approval of Kubernetes, cloud, database, identity provider, SIEM, DLP, HSM/KMS, or other blocked product choices;
- WBS-16 security controls being treated as complete;
- NCIE-016 acceptance or go-live.

### Option B — Defer WBS-15 implementation

- Leaves WBS-15 `BLOCKED`.
- Only independent WBS-22 safe scaffolding may continue.

### Option C — Approve a different scope

- Requires the approving Human to state included outputs and explicit exclusions.
- Any architectural deviation requires a formal change request.

Recommendation: **Option A**, limited exactly to the listed development artifacts and exclusions.

Decision record:

- Selected option: `PENDING`
- Decision authority: `PENDING`
- Decision date: `PENDING`
- Conditions/limitations: `PENDING`
- Evidence or meeting reference: `PENDING`

## Decision D3 — Subordinate work-package identifier convention

Source blocker: NCIE-017 `HR17-6-1`.

NCIE-017 already fixes the hierarchy `Programme → Workstream → Epic → Work Package → Task` and the workstream IDs `WBS-15` through `WBS-24`. The decision below does not renumber them.

### Option A — Approve hierarchical subordinate identifiers

- Work package: `WBS-15-WP-001`
- Task: `WBS-15-WP-001-T-001`
- Equivalent patterns apply beneath the other existing WBS workstream IDs.
- IDs are stable after assignment; retired IDs are not reused.

### Option B — Retain workstream-only identifiers temporarily

- Implementation artifacts continue to reference `WBS-15` plus descriptive scope.
- No subordinate controlled ID is assigned until a later Human decision.

### Option C — Approve another convention

- The approving Human supplies the exact stable format.
- Existing `WBS-15` through `WBS-24` identifiers remain unchanged.

Recommendation: **Option A**, because it implements the hierarchy already specified by NCIE-017 while preserving all existing identifiers.

Decision record:

- Selected option: `PENDING`
- Decision authority: `PENDING`
- Decision date: `PENDING`
- Conditions/limitations: `PENDING`
- Evidence or meeting reference: `PENDING`

## Decision D4 — Reconciled suite-register provenance gap

Source issue: the controlled ZIP contains all 18 Final Docs and supporting reports but not `NCIE_Documentation_Suite_Production_Ready_v3_0_RECONCILED`, which the Master Production Instruction names as suite-index authority.

### Option A — Approve a hashed external companion

- Treat the existing repository copy as a separately controlled companion to the immutable ZIP.
- Current DOCX SHA-256: `45D87C6C9765D1FFDFA665539CAA34F07577B4CBFA6E1632411520CB4B110424`.
- Current PDF SHA-256: `DB3432C9ED4EA86FCFA60C5C871A54DFFE6E923E514CF4CF4725042FB730169B`.
- Record the approving authority in the decision evidence.
- Do not silently alter the existing ZIP.

### Option B — Issue a new versioned production corpus

- A Human-controlled process publishes a new archive version containing the reconciled register.
- Record the new archive identifier and SHA-256; preserve the current archive as historical provenance.

### Option C — Defer index reconciliation

- Current source-grounded scopes may continue only where the Master Production Instruction and exact Final Doc filenames independently establish authority.
- Any scope needing disputed suite-index metadata remains blocked.

Recommendation: **Option B** for the cleanest long-term provenance; **Option A** is the minimum non-destructive decision for immediate controlled implementation.

Decision record:

- Selected option: `PENDING`
- Decision authority: `PENDING`
- Decision date: `PENDING`
- Conditions/limitations: `PENDING`
- Evidence or meeting reference: `PENDING`

## Consolidated authorization

No option becomes effective through this draft. An authorized Human must record selections, identity/authority, date, conditions, and an evidence reference. Codex may then update the controlled handoff and begin only the scope released by those decisions.

Suggested concise response format:

```text
D1: A
D2: A
D3: A
D4: A
Decision authority: [authorized role/name]
Decision date: [YYYY-MM-DD]
Conditions: [none or stated conditions]
Evidence reference: [meeting/minute/ticket/reference]
```
