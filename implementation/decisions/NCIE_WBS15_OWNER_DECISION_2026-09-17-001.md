# NCIE WBS-15 Owner Decision Record

Evidence reference: `NCIE-WBS15-OWNER-DECISION-2026-09-17-001`

- Decision authority supplied: `Project Owner / Clive Ebo Barton-Odro`
- Decision date supplied: `2026-09-17`
- Evidence type supplied: `Self-Authorized Project Owner Decision`
- Conditions supplied: `None`
- Recorded by Codex: `2026-09-17`
- Independent identity/authority verification: `NOT PERFORMED`

## Decisions

| Decision | Selection | Effect |
|---|---|---|
| D1 | A | Python, type-checked, is the primary backend runtime family. FastAPI may be used provisionally under NCIE-004 `TD-5-2`; no package/version, production host or procurement decision is implied. |
| D2 | A | WBS-15 local/development implementation is authorized only for the scoped foundation artifacts and exclusions in the decision pack. |
| D3 | A | Subordinate identifiers use `WBS-15-WP-001` and `WBS-15-WP-001-T-001` patterns without renumbering existing WBS IDs. |
| D4 | A | The existing reconciled v3.0 register DOCX/PDF are approved as hashed external companions; the controlled ZIP remains unmodified. |

## D4 companion hashes

- DOCX SHA-256: `45D87C6C9765D1FFDFA665539CAA34F07577B4CBFA6E1632411520CB4B110424`
- PDF SHA-256: `DB3432C9ED4EA86FCFA60C5C871A54DFFE6E923E514CF4CF4725042FB730169B`

## Authorized scope

- repository/application structure;
- Python backend service template;
- configuration model using secret references only;
- health/readiness interfaces;
- structured logging and OpenTelemetry-compatible hooks;
- local unit/contract tests;
- implementation evidence and traceability.

## Excluded scope

- production hosting, deployment or go-live;
- live credentials, production data or external-system access;
- institutional approval of Kubernetes, cloud, database, identity provider, SIEM, DLP, HSM/KMS or other blocked products;
- declaring WBS-16 security controls complete;
- NCIE-016 acceptance or production acceptance.

This record releases only `WBS-15-WP-001` within the scope above. Technical success does not expand Human authority or establish acceptance. The natural-person identity and institutional authority assertion are recorded as supplied by the user and were not independently verified by Codex.
