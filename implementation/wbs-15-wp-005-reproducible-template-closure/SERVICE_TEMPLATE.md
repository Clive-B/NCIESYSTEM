# NCIE WBS-15 Canonical Source-Tree Service Template

Status: `IMPLEMENTED LOCALLY — WBS-15 CLOSURE APPROVED; CONTROLLED ACCEPTANCE PENDING`

## Canonical layout

```text
wbs-15-wp-001-foundation-service/
  pyproject.toml
  requirements-dev.lock
  src/ncie_foundation/
    app.py
    authorization.py
    composition.py
    config.py
    correlation.py
    harness.py
    lifecycle.py
    observability.py
    readiness.py
    request_context.py
    routing.py
    structured_logging.py
    telemetry.py
  tests/
```

The cumulative source tree implements WP-001 through WP-004. WP-005 controls its reproducibility, manifest, verification, traceability and handover evidence.

## Controlled local procedure

1. Use the approved official Python 3.14.7 interpreter.
2. Create a fresh virtual environment.
3. Install `requirements-dev.lock` with `--require-hashes`; use approved/local artifacts and `--no-index` when performing the recorded offline verification.
4. Set `PYTHONPATH=src` for source-tree execution.
5. Run strict mypy, Ruff lint, Ruff format-check, compilation and unit/contract tests.
6. Run `verify_template.py` from the WP-005 directory.

## Foundation behavior

- Framework-neutral ASGI application boundary.
- No runtime third-party dependency.
- Secret references only; no live-secret resolution.
- Health and readiness remain non-authoritative platform signals.
- Identity is an interface; default state is unresolved and protected routes fail closed.
- Authorization is an extension boundary; default behavior denies.
- Observability is provider-neutral; products and deployment remain WBS-23.
- Local harness uses no network listener.

## Handover boundaries

- WBS-16 must implement IAM and approved authorization policy.
- WBS-23 must select and deploy observability/infrastructure products.
- NCIE-016 must perform controlled verification and acceptance.
- WBS-15 closure was approved under `NCIE-WBS15-OWNER-DECISION-2026-09-18-006`; downstream work still requires its own decisions and authority.
