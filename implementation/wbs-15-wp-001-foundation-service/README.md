# WBS-15 Foundation Service

Status: `WBS-15-WP-001` and `WBS-15-WP-002` WORK COMPLETE for their local implementation scopes; controlled verification and acceptance pending.

Authority: owner decision `NCIE-WBS15-OWNER-DECISION-2026-09-17-001` released the scoped WBS-15 package using type-annotated Python. This package does not authorize production hosting, live credentials, production data, external integrations, security acceptance or go-live.

WP-002 implementation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-002` released local service composition, lifecycle, aggregate readiness and in-process harness work without new runtime dependencies.

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

Successful local checks produce implementation evidence only. They do not establish NCIE-016 system verification or production acceptance.
