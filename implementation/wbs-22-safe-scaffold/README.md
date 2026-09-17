# WBS-22 Safe Scaffold

Status: IN PROGRESS / safe scaffolding only. This directory is not a production UI and does not imply test pass or acceptance.

Authority:

- NCIE-017 Chapter 22.1 permits early design-system and shell work using mock states.
- NCIE-012 Chapters 5, 7, and 8 define shell composition, brand-neutral design-token categories, and semantic/accessibility component-state requirements.
- Master Production Instruction rules 7-9 permit scoped blocker handling and explicit, reversible scaffolding.

The scaffold deliberately has no external packages, branded visual values, breakpoint assumptions, institutional navigation labels, live data, or authoritative state. Files under `fixtures/` are test inputs only. Their mock labels must remain visible.

Run the local structural checks with:

```text
npm test
```

These checks are implementation evidence mapped to NCIE-012 `UX-T3`, `UX-T5`, and `UX-T8`. They are not controlled NCIE-016 test execution and cannot establish accessibility conformance or acceptance.
