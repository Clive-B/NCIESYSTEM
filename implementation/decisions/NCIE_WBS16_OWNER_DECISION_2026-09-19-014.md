# NCIE WBS-16 Owner Decision — 2026-09-19-014

Status: `DECIDED — W16-D7-A / W16-D8-A / W16-D9-A / W16-D10-A`

Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-19-014`

Decision authority: Project Owner / Clive Ebo Barton-Odro

Decision date: `2026-09-19`

Conditions: None.

## Decision selections

### W16-D7-A — follow-on HR9-3-1 authoritative sources

Retain the seven logical authoritative-source categories approved under W16-D2-A and defer every concrete provider, product, tenant, registry instance, identifier format and protocol choice.

No additional principal class is approved. Unknown, unbound or mismatched sources yield no usable identity; session/device identity is derivative and cannot replace its base identity; and source resolution, proofing or authentication confers no authorization or governance role.

This resolves `HR9-3-1` for the WP-003 logical-contract scope only. Concrete provider/source binding and residency acceptance remain operational IAM blockers.

### W16-D8-A — HR9-4-1 symbolic proofing tiers

Approve the four provider-neutral proofing states and class mapping in the WP-003 decision pack:

1. `UNBOUND` — no usable identity.
2. `SOURCE_ATTESTED` — source-bounded technical identity only.
3. `INSTITUTIONALLY_VERIFIED` — eligibility for baseline authentication subject to current lifecycle/assurance state.
4. `ENHANCED_SENSITIVE` — enhanced proofing input only; no privilege or authorization grant.

Approve the `Identity Lifecycle Approver` and `Authoritative Source Owner` authority classes while leaving their operational institutional holders unassigned. Consequently, no live enrollment, reactivation or recovery may succeed; missing authority fails closed; evidence remains opaque; duplicate identities cannot be merged automatically; and recovery/reactivation cannot restore prior privileges, sessions or assurance.

This satisfies the proofing-tier and enrollment-authority-class prerequisites for WP-003 only. `HR9-4-1` remains operationally open for authority-holder assignment, evidence rules and live enrollment.

### W16-D9-A — HR9-5-1 symbolic assurance and step-up

Approve the four provider-neutral assurance states `UNVERIFIED`, `BASELINE`, `ELEVATED` and `RECOVERY_REPROOFED`, together with the NCIE-009 context matrix:

- standard session requires `BASELINE`;
- privileged access requires `ELEVATED` following a privilege-elevation request;
- break-glass requires `ELEVATED` plus a separately governed emergency trigger;
- a high-risk consequential action requires `ELEVATED` and current/fresh assurance under the applicable future policy; and
- a post-recovery session requires `RECOVERY_REPROOFED` and cannot inherit its prior state.

Authentication assurance remains separate from current authorization. Missing, expired, stale, insufficient or indeterminate assurance denies the protected context. No factor set, biometric use, numeric threshold or freshness window is approved.

This satisfies the assurance taxonomy and trigger matrix for WP-003 only. `HR9-5-1` remains operationally open for approved factors, numeric thresholds and freshness policy.

### W16-D10-A — HR9-10-1 explicit-expiry contracts

Approve seven opaque credential-reference metadata classes aligned to the seven principal classes, with no credential material. Every session/credential metadata record must bind principal class, authoritative source, scope, audience, issue time, explicit expiry time, assurance state, policy version and revocation state.

No indefinite/default-duration session, numeric lifetime, idle timeout, refresh window or freshness threshold is approved. Absence of an approved duration/policy reference prevents issuance. Refresh/reauthentication requires new evaluation; revocation and lifecycle invalidation propagate immediately; a session cannot exceed its base identity/credential validity; and Human credential material is prohibited from Agent Context, prompts, logs, events and source code.

This satisfies the credential-class and expiry-contract prerequisites for WP-003 only. `HR9-10-1` remains operationally open for numeric timing, concrete issuer and credential/session policy.

## Authority boundary

This decision satisfies the Human architecture-decision prerequisites for preparing the exact provider-neutral WP-003 implementation scope. It does **not** authorize implementation.

A separate explicit Project Owner decision naming `WBS-16-WP-003 Identity Lifecycle, Authentication and Session Assurance` is required before source code, tests or implementation evidence may be created for that package.

No IAM provider, live identity, proofing evidence, credential material, enrollment/login/authentication/session operation, factor set, numeric duration, role mapping, permission, access grant, delegation, privileged access, break-glass activation, external system, infrastructure, deployment, security accreditation, controlled acceptance or go-live is authorized.

## Provenance note

Codex recorded the natural-person identity and institutional-authority assertion supplied by the user. Codex did not independently verify that identity or authority.

VPF is applied behaviorally to Human-primary authority, identity dignity/non-substitution, consent, least privilege, explainability, protected-value minimization, provenance, African data residency and deny-by-default cross-border transfer. This record does not claim execution of any VPF runtime control.
