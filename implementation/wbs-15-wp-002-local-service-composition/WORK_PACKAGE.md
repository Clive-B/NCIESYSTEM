# WBS-15-WP-002 Local Service Composition and Lifecycle Contracts

Status: `WORK COMPLETE — LOCAL IMPLEMENTATION CHECKS PASSED; CONTROLLED ACCEPTANCE PENDING`

Preparation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-001`

Implementation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-002`

Predecessor: `WBS-15-WP-001` (`WORK COMPLETE`; controlled NCIE-016 verification and acceptance remain pending)

## 1. Objective

Continue the approved WBS-15 foundation by defining a deterministic local composition boundary for the existing NCIE foundation service. The package will make the foundation ready to host later authorized capabilities without selecting or implementing security providers, databases, external connectors, domain rules, production infrastructure, or production deployment.

The intended outcome is a locally testable composition root and lifecycle/readiness contract that preserves the fail-closed, non-authoritative boundaries established by WP-001.

## 2. Authority and status boundary

This document originated as the prepared proposal and was explicitly released for implementation by D5-A under `NCIE-WBS15-OWNER-DECISION-2026-09-18-002`.

The authorized local implementation is complete and the specified checks passed. This does not establish WBS-15 workstream completion, WBS-16 security completion, NCIE-016 acceptance, operational readiness, production acceptance, or go-live authority.

## 3. Implemented scope

1. A typed application-composition root that binds the existing WP-001 settings, authorization boundary, telemetry hooks, and readiness state.
2. A provider-neutral lifecycle contract for bounded local startup and shutdown behavior.
3. A dependency-readiness registry that:
   - begins fail-closed;
   - requires explicit positive state for every registered required dependency;
   - exposes aggregate platform readiness only;
   - does not expose credentials, protected values, sensitive topology, or provider-specific details;
   - cannot represent business correctness, institutional Evidence, Human approval, test acceptance, production acceptance, or go-live state.
4. Deterministic in-process request and lifecycle harnesses for local development and tests; no network listener is required.
5. Startup configuration validation using secret references only and without resolving live secret values.
6. Standard-library unit and contract tests covering composition, lifecycle, readiness aggregation, authorization defaulting, correlation handling, and status-boundary preservation.
7. Updated package traceability and local implementation evidence.

## 4. Explicitly excluded

- Production deployment, hosting, environment provisioning, containers, orchestration, CI/CD runners, or infrastructure topology.
- A network-facing development or production server dependency.
- FastAPI, Uvicorn, or any other new runtime dependency unless separately justified, approved, version-locked, hash-locked where supported, and recorded.
- Authentication provider integration, identity lifecycle, production authorization policy, role assignment, or a claim of WBS-16 completion.
- Database, cache, queue, object storage, persistence, migration, or schema selection.
- External APIs, connectors, provider discovery, governed data, production data, or live credentials.
- Institutional Evidence, custody, ledger, audit-store, domain Finding, Decision, detection, KPI, threshold, or regulated workflow implementation.
- ARGUS, memory, agent, model, RPA, PADCA, Omnis, or VPF runtime implementation.
- Brand, navigation, breakpoint, accessibility-conformance, or production UI decisions.
- Controlled NCIE-016 test execution, acceptance, accreditation, or go-live.

## 5. Technology boundary

- Language/toolchain: the already approved Python `3.14.7` toolchain and PyPI source decision under `NCIE-WBS15-OWNER-DECISION-2026-09-17-002`.
- Runtime dependencies: none proposed.
- Development dependencies: preserve the existing exact-version and hash-locked WP-001 development environment unless a separately reviewed change is required.
- Data: synthetic, non-governed test values only.
- External services and network access during tests: none.

If implementation cannot satisfy the package using this boundary, work must stop at the affected task and return a scoped Human decision request. No convenient technology default may be substituted.

## 6. Completed task breakdown

| Task | Implemented scope | Completion evidence |
|---|---|---|
| `WBS-15-WP-002-T-001` | Confirm source traceability, invariants, and test mapping | Reviewed traceability matrix with no unresolved scope ambiguity |
| `WBS-15-WP-002-T-002` | Implement typed composition root | Unit tests demonstrate explicit dependency injection and deny-by-default authorization |
| `WBS-15-WP-002-T-003` | Implement lifecycle and aggregate readiness contracts | Tests demonstrate fail-closed startup/readiness and bounded status output |
| `WBS-15-WP-002-T-004` | Implement deterministic in-process harness | Contract tests exercise startup, request, and shutdown without external services or a network listener |
| `WBS-15-WP-002-T-005` | Verify quality and preserve evidence | Strict typing, lint, format, compilation, unit/contract tests, changed-artifact list, and local evidence record |

## 7. Acceptance criteria for the implementation increment

The package may be marked `WORK COMPLETE` locally only when all of the following are evidenced:

1. The application can be composed from explicit, typed foundation dependencies.
2. Missing or invalid required configuration fails closed without exposing a protected value.
3. Authorization remains deny-by-default when no later approved policy implementation is supplied.
4. Readiness remains false until every registered required dependency explicitly reports ready.
5. Readiness and health payloads retain the existing non-authoritative and acceptance-pending fields.
6. Lifecycle transitions are deterministic, bounded, and locally testable.
7. Correlation identifiers and telemetry hooks continue to behave as specified by WP-001.
8. No runtime dependency, live secret, governed data, external service, or network listener is introduced.
9. Strict mypy, Ruff lint, Ruff format, compilation, and all package unit/contract tests pass in the approved locked environment.
10. Traceability and evidence clearly state that controlled NCIE-016 verification and all production authority remain pending.

## 8. Stop conditions

Stop the affected work and request Human direction if implementation would require:

- a new runtime or development dependency;
- a server/framework selection;
- a database, identity provider, secret manager, telemetry exporter, queue, cache, connector, hosting platform, or deployment target;
- live or governed data;
- a change to an open HR decision;
- an assertion that a platform signal constitutes Evidence, approval, a Finding, a Decision, acceptance, or production readiness.

## 9. Human release

The implementation-release decision was:

> Approve `WBS-15-WP-002` for local implementation exactly within this prepared scope, using the existing approved Python 3.14.7 toolchain and locked development environment, with no new runtime dependency and all exclusions preserved.

That decision was supplied and recorded under `NCIE-WBS15-OWNER-DECISION-2026-09-18-002`. No further authority is inferred from it.

## 10. VPF boundary

VPF informs the package behaviorally through Human-primary authority, least privilege, provenance, explainability, data minimization, dignity, and African data-sovereignty constraints. No VPF runtime, signature, checksum seal, certificate, ledger, PADCA/Omnis service, residency enforcement, or production control is claimed or implemented by this package.
