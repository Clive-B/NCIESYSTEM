# WBS-16-WP-002 Traceability

Status: `IMPLEMENTED AND LOCALLY VERIFIED`

| Requirement or decision | Implementation | Verification | Boundary |
|---|---|---|---|
| `HR9-1-1` / scoped `HR8-10-1` / W16-D5-A | `GovernedTarget`, `AuthorityAssignment`, `AuthorityRegistry`, `GovernanceDecisionRecord` and `GovernanceDecisionValidator` | Exact target/version, one-current-authority, holder, expiry, revocation and missing/duplicate tests | Validation does not perform institutional acceptance |
| W16-D5-A independent review | `SecurityArchitectureReview` and review validation codes | Missing, wrong-role, mismatched, non-independent, conflicted, self-review, late and non-supporting paths | No reviewer is assigned or activated by code |
| W16-D5-A control ownership | `SecurityControlOwnership` | Required role, exact target, currentness, expiry and revocation | No production control owner or persistent registry |
| `HR9-2-1` / W16-D6-A | Versioned `APPROVED_DEVELOPMENT_RISK_APPETITE` and `APPROVED_THREAT_ASSUMPTIONS` | Nine-domain and nine-assumption completeness checks | Development posture only; no production risk assessment |
| No-appetite and fail-closed posture | `DevelopmentRiskEvaluator` | Unauthorized-access, governed-data, credential, external, cross-border, exception and unknown-domain tests | Evaluator cannot accept residual risk or an exception |
| Limited local experimentation | `LOCAL_EXPERIMENTATION` boundary | Synthetic/non-governed local path succeeds; every broader path denies | No live data, external activation or deployment |
| Residual-risk handling | `RiskTreatmentPlan` with avoid/mitigate/monitor-pending-verification only | Mandatory future-review test | Treatment is not risk acceptance |
| WBS-15/WP-001 integration | Existing source tree and public package exports | Strict typing, lint, format, compile, 52 cumulative tests and template verifier | No runtime dependency or framework change |

Implementation evidence is recorded under `evidence/IMPLEMENTATION_20260919_001.md`; local execution evidence is recorded under `evidence/LOCAL_RUN_20260919_001.md`.
