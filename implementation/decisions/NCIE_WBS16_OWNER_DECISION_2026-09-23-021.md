# NCIE WBS-16 Owner Decision — 2026-09-23-021

Status: `DECIDED — WBS-16-WP-005 IMPLEMENTATION AUTHORIZED`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-23-021`

Evidence type: `Self-Authorized Project Owner Decision`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-23`

## Authorized implementation

Authorize implementation of `WBS-16-WP-005 — Secrets, Cryptography and Network Zero-Trust Contracts` strictly within the architecture approved under `NCIE-WBS16-OWNER-DECISION-2026-09-23-020`.

Authorized scope is limited to:

- opaque secret/key/certificate reference contracts that reject literal or protected material;
- provider-neutral secret/key lifecycle-event contracts without executing lifecycle operations;
- abstract custodial, policy, exception-review and assurance interfaces that remain operationally unassigned and denying;
- prohibited-surface and exception-policy evaluation;
- provider-neutral cryptographic protection-scope, conceptual key-hierarchy, separation and crypto-agility contracts;
- fail-closed cryptographic-policy evaluation;
- the approved seven logical Zero-Trust zone labels and source-defined service-boundary contracts;
- the approved provider-neutral egress classes and deny-by-default evaluation;
- Agent/external egress ceiling evaluation across sandbox, Task Contract, identity, destination, classification, purpose, retention, residency/sovereignty and current authorization;
- provider-neutral exception request/decision metadata with unassigned granting authority;
- minimized, non-authoritative security-condition signals;
- local deterministic unit/contract and negative-path tests; and
- traceability and local implementation evidence.

## Mandatory boundary

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

The controlled reference configuration must contain zero live secrets or keys, certificates or credentials, operational custodians or exception authorities, cryptographic algorithms/profiles or products, destination allow-list entries, network routes or external connections, and network/egress exception grants.

No secret, key, certificate, token, credential or protected production value may be created, read, copied, stored, logged, transmitted or processed.

No secret manager, Vault, KMS/HSM, CA, PKI product, cryptographic implementation, firewall, service mesh, gateway product, cloud/network platform or infrastructure may be selected or activated.

No algorithm, key length, cipher/profile, certificate profile, numeric rotation/lifetime policy or other unspecified cryptographic parameter may be invented.

No Agent internet access, external destination, model/provider activation, Tool invocation, cross-border transfer or live networking is authorized.

No WP-006 or later WBS-16 implementation is authorized.

If a stop condition in the decided WP-005 Human Review Decision Pack is encountered, the affected scope stops for Human decision. The fallback state remains `DENY / NO CAPABILITY`.

## Provenance note

Codex recorded the natural-person identity, institutional-authority assertion and evidence type supplied by the user. Codex did not independently verify that identity, authority or the meaning of `Self-Authorized Project Owner Decision` beyond recording the user's statement.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, provenance, minimization, African data residency and deny-by-default cross-border transfer. This record does not claim execution of any VPF runtime, signature, checksum, certificate, ledger, validator, residency-control service or enforcement action.
