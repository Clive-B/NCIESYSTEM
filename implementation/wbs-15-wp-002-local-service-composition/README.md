# WBS-15-WP-002 Implementation Location

Status: `WORK COMPLETE — LOCAL IMPLEMENTATION CHECKS PASSED; CONTROLLED ACCEPTANCE PENDING`

The WP-002 implementation extends the existing cumulative foundation package under:

`implementation/wbs-15-wp-001-foundation-service/src/ncie_foundation/`

Primary modules:

- `composition.py`
- `lifecycle.py`
- `readiness.py`
- `harness.py`

The package remains in the existing source tree so WP-002 composes the WP-001 contracts directly without creating a duplicate package or adding a path/runtime dependency.

Tests are under `implementation/wbs-15-wp-001-foundation-service/tests/`. Run all WP-001/WP-002 checks from that foundation-service directory using the approved locked environment:

```text
.venv\Scripts\python -m mypy src tests
.venv\Scripts\python -m ruff check src tests
.venv\Scripts\python -m ruff format --check src tests
.venv\Scripts\python -m compileall -q src tests
set PYTHONPATH=src
.venv\Scripts\python -m unittest discover -s tests -v
```

These are local implementation checks, not controlled NCIE-016 verification or production acceptance.
