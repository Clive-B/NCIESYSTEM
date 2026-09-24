# WBS-16-WP-008 Traceability

| Requirement / decision | Implementation | Verification | Deferred / unassigned |
|---|---|---|---|
| HR9-20-1 / W16-D24-A | `security_logging_incident.py`: minimized synthetic Security Event, separate opaque references, log-access/retention/assurance registries, fail-closed access and retention boundaries, in-memory synthetic collector | Schema-exclusion, immutability, current four-layer authorization, empty-registry, no-period, no-persistence/audit/Evidence tests | Real logs, stores, access policies, retention/legal-hold periods, disclosure, assurance holders and WBS-20 audit/Evidence capability |
| HR9-21-1 / W16-D25-A | Exact five categories, source-behavior references without a sixth category, symbolic severity, detection/escalation/severity registries, no-monitor and fail-closed triage boundaries | Exact-taxonomy, behavior-reference, unassigned severity, stale rule, no poll/stream/connect and false-authority tests | Rules, owners, analytic methods, thresholds, operational severity, routes, monitoring, correlation, alerting and paging |
| HR9-22-1 / W16-D26-A | Ordered lifecycle, incident candidate, notification obligation, containment request, effectiveness metadata, recovery handoff, restoration review and separate zero-capability boundaries | Lifecycle-order, no declaration/command/send/execute, explicit-expiry, segregation, effectiveness, reauthorization and independent-review negative tests | Incident declaration/command, recipients/destinations, containment rights, emergency eligibility, recovery/restoration/reinstatement authority and all execution |
| Fourteen non-waivable protections | Structural type separation; empty registries; unassigned authority; current authorization; minimized references; segregated roles; deny-only/Human-review results | Registry/authority enumeration, distinct-type, prohibited-field, untrusted-origin, self-approval and capability-surface tests | Operational enforcement, WBS-20 Evidence/audit, WBS-23 infrastructure and NCIE-016 verification/acceptance |
| WP-001 through WP-007 non-bypass | Reuses `CurrentAuthorizationDecision` and `UntrustedContentOrigin`; no grant, output, network or external capability | Cumulative standard-library regression and template verifier | Production integration, source-control release, accreditation, acceptance and go-live |

Architecture evidence: `NCIE-WBS16-OWNER-DECISION-2026-09-24-029`.

Implementation evidence: `NCIE-WBS16-OWNER-DECISION-2026-09-24-030`.

Local run evidence: `evidence/LOCAL_RUN_20260924_001.md` after final verification.

Source-control release evidence: not authorized or created.
