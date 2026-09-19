# WBS-16-WP-003 Traceability

Status: `IMPLEMENTED AND LOCALLY VERIFIED`

| Requirement or decision | Implementation | Verification | Boundary |
|---|---|---|---|
| Follow-on `HR9-3-1` / W16-D7-A | Existing seven `PrincipalClass` and `AuthoritativeSourceCategory` mappings; derivative-session validator | Seven-class completeness, mismatch and derivative-session tests | No provider/source instance or protocol |
| `HR9-4-1` / W16-D8-A | `ProofingState`, `ProofingRecord`, lifecycle states/actions and enrollment-authority boundary | Tier mismatch, required Agent/service metadata, invalid transition, duplicate and unassigned-authority tests | No operational holder, live evidence, enrollment or recovery |
| `HR9-5-1` / W16-D9-A | `AssuranceState`, `AssuranceContext`, `AssuranceEvaluator` | Standard, insufficient, step-up, emergency, freshness and post-recovery tests | No factors, biometrics, numeric thresholds or authorization grant |
| `HR9-10-1` / W16-D10-A | Seven credential-reference classes, `CredentialReferenceMetadata`, `SessionMetadata`, binding/replay-policy references and unbound issuer | Explicit scope/audience/expiry/policy, revocation, binding and no-issuance tests | No credential material, issuer, replay algorithm, numeric duration, refresh or live session |
| Immediate invalidation | `RevocationDirective` and lifecycle invalidation result | Suspension/recovery plus session/token/cache completeness tests | Directive contract only; no external propagation executed |
| Recovery non-inheritance | Recovery-reproofed requirement and prior-session invalidation | Missing reproofing denies; valid symbolic completion invalidates prior sessions | No old privilege restoration; privilege remains WP-004 |
| Authentication/authorization separation | `AssuranceValidationResult.authorizes_action` fixed false | Valid standard assurance still does not authorize | WP-001 authorization remains independently required |
| WBS-15/WP-001/WP-002 integration | Existing source tree and public exports | Strict typing, lint, format, compile, 68 cumulative tests and template verifier | No runtime dependency or framework change |

Implementation evidence is recorded under `evidence/IMPLEMENTATION_20260919_001.md`; local execution evidence is recorded under `evidence/LOCAL_RUN_20260919_001.md`.

Controlled source release evidence is recorded under `evidence/SOURCE_CONTROL_RELEASE_20260919_001.md`.
