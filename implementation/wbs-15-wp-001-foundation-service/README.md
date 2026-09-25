# WBS-15 Foundation Service

Status: `WBS-15 — IMPLEMENTATION COMPLETE / DOWNSTREAM-READY; CONTROLLED VERIFICATION AND ACCEPTANCE PENDING` under owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-18-006`.

WBS-16 status: WP-001 through WP-009 are locally work-complete. WP-009 is implemented under `NCIE-WBS16-OWNER-DECISION-2026-09-24-033`; controlled source release has not been authorized. Independent security verification, accreditation and acceptance remain pending.

Authority: owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-17-001` released the scoped WBS-15 package using type-annotated Python. This package does not authorize production hosting, live credentials, production data, external integrations, security acceptance or go-live.

WP-002 implementation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-002` released local service composition, lifecycle, aggregate readiness and in-process harness work without new runtime dependencies.

WP-003 through WP-005 implementation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-005` released request/identity-interface/extension contracts, neutral observability semantics, reproducibility and closure-evidence work. Owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-18-006` subsequently approved WBS-15 implementation closure and downstream readiness.

## Implemented scope

- dependency-free ASGI service foundation;
- liveness and readiness interfaces with explicit business-correctness and acceptance boundaries;
- mandatory correlation ID handling for non-probe requests;
- problem-details-style error envelopes;
- secret-reference-only configuration parsing;
- structured, classification-aware logging without protected values;
- OpenTelemetry-compatible telemetry hook protocol without selecting/exporting to a provider;
- deny-by-default authorization extension boundary;
- standard-library unit and contract tests.

WP-002 adds:

- typed local service composition;
- deterministic lifecycle state and rollback contracts;
- aggregate fail-closed required-dependency readiness;
- startup configuration validation through the composition boundary;
- a deterministic in-process test harness with no network listener.

WP-003 adds typed request contexts, explicit identity-interface states, protected route registration/dispatch, configuration-schema validation and service-version metadata while leaving IAM to WBS-16.

WP-004 adds five distinct provider-neutral observability categories, typed event/metric/trace contracts, protected-attribute rejection and in-memory test collection while leaving products/deployment to WBS-23.

WP-005 adds the canonical source-tree template manifest, offline clean-environment verification, consolidated traceability, downstream handover and the Human-approved completion report.

WBS-16-WP-001 adds seven provider-neutral security-principal/source categories, four-layer current-authorization contracts, a zero-grant deny-all policy decision point, fail-closed enforcement adaptation and minimized non-authoritative security-decision signals. It adds no provider, credentials, sessions, role assignments, permissions or access grants.

WBS-16-WP-002 adds provider-neutral security-governance authority, independent-review, control-ownership, risk-appetite, threat-assumption and treatment contracts plus fail-closed local-development evaluation. It does not accept production risk, perform accreditation, grant an exception or deploy a control.

WBS-16-WP-003 adds provider-neutral identity proofing and lifecycle states, unassigned enrollment-authority and session-issuer boundaries, symbolic assurance/step-up rules, explicit-expiry credential/session metadata, recovery and revocation propagation contracts, and fail-closed validation. It selects no provider, issues no credential, performs no live authentication and grants no authorization.

WBS-16-WP-004 adds a versioned four-layer authorization-mapping contract with an empty institutional registry, four bounded delegation classes, three privileged-access classes, three emergency-access classes, unassigned approval/eligibility boundaries, expiry/revocation and independent-review contracts, and minimized non-authoritative signals. It populates no institutional mapping or grant and activates no delegation, privilege or emergency capability.

WBS-16-WP-005 adds opaque protected-material references, non-executing lifecycle metadata, unassigned custodial/policy/exception/assurance interfaces, prohibited-surface controls, conceptual cryptographic protection/hierarchy/separation contracts, seven logical zones, five egress classes, Agent/external ceiling evaluation and minimized signals. Its controlled cryptographic and egress registries are empty; it handles no protected material and activates no cryptography, network path or exception.

WBS-16-WP-006 adds provider-neutral Agent ceilings, generated-code quarantine, model/provider eligibility, the four source-defined Tool classes and strict Context isolation contracts. Its four controlled registries are empty; all Human/institutional authority interfaces are unassigned; and its Agent Factory, Model Gateway, Tool Gateway and cross-context boundary validate only synthetic metadata while granting and executing no capability.

WBS-16-WP-007 adds the five approved DLP paths, disclosure decisions, output-channel and protected-identity handling contracts. Its six controlled registries are empty; disclosure and privacy authorities are unassigned; and its no-output, no-reveal and Human-escalation boundaries evaluate only synthetic metadata while disclosing, retrieving, unmasking, speaking, exporting and transmitting nothing.

WBS-16-WP-008 adds minimized security-event metadata, five detection categories, symbolic severity, incident-control references, eleven empty registries, unassigned authorities, a non-persistent synthetic collector and inert no-monitor/no-notification/no-incident-command/no-containment-recovery boundaries. It creates no real log, alert, incident, notification, containment or recovery capability.

WBS-16-WP-009 adds artifact provenance/version/integrity, dependency/build provenance, verification/quarantine, vulnerability/remediation/exception/risk-treatment and compromised-state/recovery-security contracts. Its thirty controlled registries are empty; all forty-two authority classes are unassigned; and its no-artifact-action, no-remediation and no-recovery boundaries evaluate synthetic metadata while accepting, promoting, deploying, scanning, patching, recovering, restoring, reauthorizing and reinstating nothing.

FastAPI remains an NCIE-004 Proposed Design Default allowed by D1-A. It is not added because this package currently needs no runtime dependency and no FastAPI route has yet been authorized. The ASGI boundary is directly adaptable to FastAPI without changing the governed contracts in this package.

Python 3.14.7 and PyPI were approved under `NCIE-WBS15-OWNER-DECISION-2026-09-17-002`. Development dependencies are fully version- and hash-locked in `requirements-dev.lock` for CPython 3.14 on Windows x86-64.

The default readiness response is `503 NOT_READY`. A caller constructing the application must explicitly assert that its application dependencies are ready; even then, the response continues to state that test and production acceptance are pending.

## Local verification

Use the approved Python 3.14.7 interpreter and install only the locked development environment:

```text
python -m venv .venv
.venv\Scripts\python -m pip install --require-hashes -r requirements-dev.lock
```

Once an approved Python toolchain is available, run from this directory:

```text
set PYTHONPATH=src
python -m unittest discover -s tests -v
```

PowerShell equivalent:

```text
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

Quality checks:

```text
.venv\Scripts\python -m mypy src tests
.venv\Scripts\python -m ruff check src tests
.venv\Scripts\python -m ruff format --check src tests
```

Successful local checks produce implementation evidence. WBS-15 closure is established separately by owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-18-006`; the checks do not establish NCIE-016 system verification, security accreditation, production acceptance or go-live.
