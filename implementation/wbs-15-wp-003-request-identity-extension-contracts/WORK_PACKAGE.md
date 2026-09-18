# WBS-15-WP-003 Request, Identity and Application Extension Contracts

Status: `WORK COMPLETE — LOCAL IMPLEMENTATION CHECKS PASSED; CONTROLLED ACCEPTANCE PENDING`

Preparation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-004`

Implementation authority: `NCIE-WBS15-OWNER-DECISION-2026-09-18-005`

Predecessors: `WBS-15-WP-001` and `WBS-15-WP-002` (`WORK COMPLETE` for their local scopes)

## 1. Objective

Make the framework-neutral ASGI foundation capable of hosting later authorized NCIE capabilities through typed request, identity and application-extension contracts while preserving correlation, default-deny authorization and Human-primary authority.

## 2. Confirmed boundary

- Retain the dependency-free ASGI foundation for WBS-15.
- Provide identity interfaces and fail-closed defaults only.
- Defer framework choice and all IAM implementation.
- Use Python 3.14.7, virtual environments and the existing locked pip development environment.

## 3. Implemented scope

1. A typed request context carrying correlation ID, method, path, purpose reference, data-classification marker and identity context.
2. Explicit identity states such as `ANONYMOUS`, `UNRESOLVED` and `AUTHENTICATED`, with authenticated state accepted only from a future approved identity boundary.
3. A provider-neutral identity-resolution protocol and default unresolved implementation.
4. A provider-neutral application-route registration and dispatch contract for local/in-process use.
5. Enforcement that protected application routes cannot bypass correlation, identity-resolution or authorization boundaries.
6. Separation of platform probes from application routes and authoritative business state.
7. Standard problem-response and service-version metadata contracts.
8. Explicit configuration-schema version validation.
9. Unit and contract tests using synthetic, non-governed values only.

## 4. Explicitly excluded

- FastAPI or any other framework/server selection.
- Network listener or production API endpoint.
- Identity provider, login, token validation, session handling, user provisioning or credential lifecycle.
- Role, permission, policy or privileged-access implementation.
- Database, connector, domain route, Evidence, Finding, Decision or regulated workflow.
- Production deployment, infrastructure, controlled acceptance or go-live.

## 5. Completed tasks

| Task | Prepared scope | Required local evidence |
|---|---|---|
| `WBS-15-WP-003-T-001` | Finalize request/identity/route invariants and traceability | Reviewed contract matrix |
| `WBS-15-WP-003-T-002` | Implement typed request and identity interfaces | Unit tests for all identity states and validation rules |
| `WBS-15-WP-003-T-003` | Implement extension/route registry and dispatch boundary | Tests proving registration, dispatch and non-bypass behavior |
| `WBS-15-WP-003-T-004` | Integrate correlation, default-deny authorization and errors | Regression and negative-path contract tests |
| `WBS-15-WP-003-T-005` | Verify quality and preserve evidence | Strict typing, lint, format, compilation, tests and evidence record |

## 6. Completion criteria

WP-003 may be marked locally `WORK COMPLETE` only when:

1. Every application request receives a typed context.
2. Missing correlation or unresolved identity fails closed where the route requires protection.
3. No application handler can be invoked before the applicable foundation boundaries run.
4. Identity state does not create roles, permissions or institutional authority.
5. Platform probes remain distinguishable from application/business state.
6. Configuration-schema incompatibility fails explicitly.
7. No framework, server, IAM product, new dependency, live credential, governed data or external service is introduced.
8. All WP-001–WP-003 regression and quality checks pass.
9. Evidence states that WBS-16 and NCIE-016 remain pending.

## 7. Stop conditions

Stop and request Human direction if implementation requires a framework/server, token format, identity provider, role model, new dependency, external service, governed data or change to a downstream WBS-16 decision.

## 8. Human release

The prepared scope was released under `NCIE-WBS15-OWNER-DECISION-2026-09-18-005`. No authority beyond this package is inferred.

## 9. VPF boundary

VPF informs least privilege, identity minimization, explainability, provenance and Human-primary authority behaviorally. No VPF identity, watermark, signature, runtime or enforcement service is implemented or claimed.
