# NCIE WBS-16 Owner Decision — 2026-09-24-032

Status: `DECIDED — WBS-16-WP-009 ARCHITECTURE APPROVED / IMPLEMENTATION NOT AUTHORIZED`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-24-032`

Evidence type: `Self-Authorized Project Owner Decision`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-24`

## Decisions

- `W16-D27: A` — approve provider-neutral artifact provenance, verification, quarantine, generated-code security-gate, acceptance/revocation and independent-review contracts with empty controlled registries, unassigned authorities and zero artifact acceptance, promotion, deployment or execution capability.
- `W16-D28: A` — approve provider-neutral vulnerability, remediation, mitigation, exception and residual-risk treatment contracts with symbolic severity, empty controlled registries, unassigned authorities and zero remediation, exception activation, risk acceptance or security-acceptance capability.
- `W16-D29: A` — approve provider-neutral compromised-state, recovery-source, quarantine, reconciliation, independent-review and security-recovery acceptance contracts with empty controlled registries, unassigned authorities and zero backup, recovery, restoration, reauthorization or reinstatement capability.

## Mandatory boundary

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

All eighteen bounded WP-009 non-waivable protections in the decided Human Review Decision Pack are approved.

The following semantic separations remain mandatory:

- `ARTIFACT VERIFIED ≠ ARTIFACT ACCEPTED ≠ ARTIFACT PROMOTED ≠ DEPLOYED`;
- `VULNERABILITY DETECTED ≠ FINDING ≠ RISK ACCEPTED ≠ REMEDIATED ≠ SECURITY ACCEPTED`;
- `RECOVERY ≠ REAUTHORIZATION`;
- `RECOVERY ACCEPTED ≠ OPERATIONALLY RESTORED`; and
- `RESTORATION ≠ REINSTATEMENT`.

Generated executable code remains subject to the existing WP-006 quarantine and remains `NOT_APPROVED_FOR_EXECUTION`. No producer, generator, Agent or implementer may self-approve where independent review is required.

No artifact acceptance, quarantine release, promotion, deployment, publication or execution is authorized.

No vulnerability severity taxonomy, threshold, remediation deadline, exception duration or risk-acceptance criterion is selected. No vulnerability or residual risk is accepted. No scanning, patching, remediation, mitigation or live-system security action is authorized.

Unknown or unverifiable recovery state remains treated as compromised and quarantined. Recovery must preserve current revocation, restriction, deletion, classification, provenance and security state. No credential/key/session invalidation or rotation, backup, restore, failover, reconciliation, restoration, reauthorization or reinstatement operation is authorized.

No CI/CD, artifact registry, scanner, SBOM/signing, vulnerability-management, backup/recovery or related product/provider is selected or activated. No governed production data, external destination, cross-border transfer, infrastructure or deployment is authorized.

WBS-20 retains institutional Evidence, canonical provenance, audit and custody scope. WBS-23 retains repositories, CI/CD, scanners, promotion, deployment, patching, backup/recovery infrastructure and operational runbooks. NCIE-016 retains independent security/recovery verification and acceptance authority.

This decision defines architecture only. It does not authorize WP-009 implementation, source-control release, operational activation, independent verification, accreditation, controlled acceptance, deployment or go-live. No WP-010 implementation is authorized.

## Provenance note

Codex recorded the natural-person identity, institutional-authority assertion and evidence type supplied by the user. Codex did not independently verify that identity, authority or the meaning of `Self-Authorized Project Owner Decision` beyond recording the user's statement.

VPF is applied behaviorally to Human-primary authority, least privilege, segregation of duties, provenance, minimization, sovereignty and African data residency. This record does not claim execution of any VPF runtime, signature, checksum, certificate, ledger, quarantine action, scanner, recovery action or residency-enforcement service.
