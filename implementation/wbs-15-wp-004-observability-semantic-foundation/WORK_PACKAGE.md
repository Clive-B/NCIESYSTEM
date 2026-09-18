# WBS-15-WP-004 Observability Semantic Foundation

Status: `WORK COMPLETE — LOCAL IMPLEMENTATION CHECKS PASSED; CONTROLLED ACCEPTANCE PENDING`

Preparation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-004`

Implementation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-005`

Predecessors: `WBS-15-WP-001` and `WBS-15-WP-002`; WP-003 contracts must be preserved if WP-003 is implemented first.

## 1. Objective

Implement provider-neutral observability semantics and locally testable contracts so later infrastructure can attach approved products without changing NCIE's meaning, classification or authority boundaries.

## 2. Confirmed boundary

- Implement neutral semantics, protocols and in-memory test collectors now.
- Defer collectors, stores, dashboards, alerting, SLO enforcement and product deployment to WBS-23.
- Add no runtime or development dependency.

## 3. Implemented scope

1. Five non-collapsible signal categories:
   - `PLATFORM_HEALTH`;
   - `DATA_PIPELINE_HEALTH`;
   - `SECTOR_NETWORK_CONDITION`;
   - `ARGUS_QUALITY`;
   - `SECURITY_CONDITION`.
2. Typed operational-event, metric and trace/span contracts.
3. Correlation propagation fields for request and later event boundaries.
4. Data-classification, minimization and redaction metadata.
5. Prohibition of secret, credential or protected-payload fields in bounded telemetry attributes.
6. Explicit flags stating that telemetry is not institutional Evidence, a Finding, a Decision, Human approval or acceptance.
7. In-memory test collectors that perform no network or file export.
8. Integration with existing logging and telemetry hooks without selecting a provider.
9. Unit, contract and semantic-separation regression tests.

## 4. Explicitly excluded

- OpenTelemetry SDK/Collector, Prometheus, Grafana, Alertmanager, APM or log-store dependencies.
- Exporters, network sinks, dashboards, production alerting or SLO enforcement.
- SIEM, security operations, VPF/PADCA/Omnis telemetry or production residency enforcement.
- Full prompts, Evidence payloads, protected identity, secret values or sensitive tool parameters.
- Production deployment, infrastructure changes or controlled acceptance.

## 5. Completed tasks

| Task | Prepared scope | Required local evidence |
|---|---|---|
| `WBS-15-WP-004-T-001` | Finalize observability taxonomy and prohibited conflations | Reviewed semantic matrix |
| `WBS-15-WP-004-T-002` | Implement typed event/metric/trace contracts | Construction and validation tests |
| `WBS-15-WP-004-T-003` | Implement minimization/redaction boundary | Protected-field rejection and redaction tests |
| `WBS-15-WP-004-T-004` | Implement in-memory collectors and integrate hooks | Deterministic capture and correlation tests |
| `WBS-15-WP-004-T-005` | Verify category separation and preserve evidence | Full regression, semantic negative tests and evidence |

## 6. Completion criteria

WP-004 may be marked locally `WORK COMPLETE` only when:

1. Every emitted signal has exactly one governed category.
2. Platform health cannot be represented as sector/network condition.
3. Telemetry cannot represent Evidence, Findings, Decisions, approval or acceptance.
4. Secret/protected fields are rejected or safely excluded without echoing values.
5. Correlation is preserved by local collectors.
6. Tests use no network, external service, governed data or live credential.
7. No product, exporter or new dependency is selected.
8. All cumulative regression and quality checks pass.
9. Evidence states that WBS-23 deployment and NCIE-016 verification remain pending.

## 7. Stop conditions

Stop and request Human direction if implementation requires an SDK, exporter, monitoring product, external sink, persistence, production SLO, sensitive payload or new dependency.

## 8. Human release

The prepared scope was released under `NCIE-WBS15-OWNER-DECISION-2026-09-18-005`. No deployment or product-selection authority is inferred.

## 9. VPF boundary

VPF informs minimization, provenance, explainability, sovereignty and Human authority behaviorally. The package must not imply that VPF runtime telemetry or enforcement exists.
