# WP-010 Reproducible Dependency and Configuration Inventory

- Python contract target: `3.14`.
- Runtime dependencies: `none`.
- Existing development tools only: `mypy==2.3.1`, `ruff==0.16.8` under the existing exact/hash-locked environment.
- Test framework: Python standard-library `unittest`.
- Persistence: none.
- Network/external systems: none.
- Products/providers/scanners/environments/corpora: none selected.
- Governed production data, credentials, protected identities and live security events: none.
- Production authorization: `false`.
- Controlled acceptance: `PENDING`.

The executable metadata source is `DEPENDENCY_CONFIGURATION_INVENTORY` in `security_verification_handover.py`; it rejects runtime dependencies and external-system entries.
