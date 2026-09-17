# NCIE WBS-15 Toolchain Owner Decision Record

Evidence reference: `NCIE-WBS15-OWNER-DECISION-2026-09-17-002`

- Decision authority supplied: `Project Owner / Clive Ebo Barton-Odro`
- Decision date supplied: `2026-09-17`
- Evidence type supplied: `Self-Authorized Project Owner Decision`
- Conditions supplied: `None`
- Recorded by Codex: `2026-09-17`
- Independent identity/authority verification: `NOT PERFORMED`

## Approved decision

- Python version: `3.14.7`.
- Python distribution source: official Python distribution.
- Python package source: PyPI.
- Dependency-control condition: all dependency versions must be locked before commitment.

## Scope and boundaries

This decision authorizes installation and local use of the approved Python toolchain for `WBS-15-WP-001`, creation of an isolated project environment, resolution of approved development/runtime dependencies from PyPI, production of a dependency lock with hashes where supported, and execution of local implementation tests.

It does not authorize production deployment, live credentials, production data, external NCIE integrations, security acceptance, NCIE-016 acceptance or go-live. The natural-person identity and institutional authority assertion are recorded as supplied by the user and were not independently verified by Codex.

## Initial environment observation

A sandboxed `winget` version/search probe on 2026-09-17 failed before installation with Windows error `A specified logon session does not exist`. No toolchain or dependency was installed by that failed probe. The approved installation must therefore use an explicitly authorized elevated execution context.
