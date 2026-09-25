# NCIE WBS-16-WP-009 Human Review Decision Pack

Status: `DECIDED — ARCHITECTURE APPROVED / IMPLEMENTATION AUTHORIZED UNDER ...-033`

Prepared: `2026-09-24`

Work package: `WBS-16-WP-009 — Supply Chain, Vulnerability and Security Recovery`

Decision scope:

- `HR9-23-1` — artifact-acceptance authority, provenance, verification, quarantine and generated-code security-gate criteria;
- `HR9-24-1` — vulnerability, patch and remediation governance, exception lifecycle and unremediated-vulnerability risk-acceptance authority; and
- `HR9-25-1` — compromised-state handling, recovery security, restoration/reconciliation and security-recovery acceptance.

This pack presents the source-grounded choices and records the Project Owner selections in Section 16. The architecture decision did not itself authorize implementation; the later, separate `NCIE-WBS16-OWNER-DECISION-2026-09-24-033` released only the bounded scope in Section 11. Neither decision verifies or accepts an artifact, creates an institutional Finding, accepts risk, patches or restores a system, selects a product, or authorizes WP-010 or later work.

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

## 1. Source-grounded baseline

### 1.1 NCIE-009 Chapter 23 — supply-chain, dependency and artifact security

NCIE-009 requires software, model, Agent Pattern, Tool, image, package and dependency supply chains to preserve provenance and integrity. Artifact identity, version and provenance matter, but verification does not create deployment or execution authority.

Generated code has a security-review gate distinct from ordinary dependency scanning. A successful Agent run or VPF process does not satisfy that gate. Suspect artifacts are quarantined rather than provisionally deployed. NCIE-009 leaves the accountable authority class, Supply-Chain Security Owner, artifact-acceptance authority and generated-code gate criteria unresolved under Blocking item `HR9-23-1`.

NCIE-004 and NCIE-007 reinforce the ordered generated-code boundary:

`EPHEMERAL GENERATED ARTIFACT → ENGINEERING CHANGE CANDIDATE → ENGINEERING REVIEW → BUILD → SECURITY/TEST → APPROVAL → DEPLOYMENT → ELIGIBLE PRIMITIVE`.

WP-006 already implements generated-code quarantine and zero execution. WP-009 cannot weaken that predecessor state. The generator, producing Agent or implementer cannot approve its own output where independence is required.

### 1.2 NCIE-009 Chapter 24 and NCIE-008 Chapters 4 and 21 — vulnerability, remediation and exception governance

NCIE-009 requires discovery, triage, remediation, patching, compensating controls and verification to be ordered and traceable. Vulnerability severity does not itself accept risk. Residual-risk acceptance is a distinct Human-controlled decision-right act governed by NCIE-008.

NCIE-008 requires each Decision to bind an exact target, scope and version. Approval, authorization, acceptance, exception, Finding and consequential action remain separate acts. An exception request must state its scope, duration and compensating controls; its approver cannot be its requester; it does not repeal policy or create technical capability. Expiry requires fresh reassessment rather than automatic renewal, and revocation is prospective without erasing history.

NCIE-009 leaves remediation governance and the authority to accept risk for unpatched vulnerabilities unresolved under Blocking item `HR9-24-1`. Vulnerability severities, remediation deadlines, exception durations, prohibited exception classes, risk thresholds and operational owners are not supplied by the controlled source.

### 1.3 NCIE-009 Chapter 25 and NCIE-006/007 — compromised-state and recovery security

Recovery must reconcile current identities, authorizations, Agent/model/Tool eligibility, secrets and security state. A restored backup, snapshot, checkpoint or artifact cannot revive stale authority. Expired grants remain expired; revoked eligibility remains revoked; current deletion, restriction and classification state prevails.

An unknown-integrity backup or failover state is treated as compromised until independently verified. Restoration without verification is prohibited. Credential, key and session invalidation or rotation follows a recovery event that may have exposed them, but WP-009 may carry only references to those governed actions; it cannot perform them.

NCIE-009 leaves security-recovery acceptance authority and the compromised backup/state process unresolved under Blocking item `HR9-25-1`. NCIE-016 separately owns recovery verification, independent review evidence and acceptance/sign-off architecture. A backup test is not recovery validation, and a recovery exercise is not production recovery proof.

### 1.4 Existing controlled architecture

Any future WP-009 implementation remains subordinate to WP-001 through WP-008:

- current four-layer object/field/action/purpose authorization;
- empty institutional mappings, zero grants and unassigned authorities;
- explicit expiry, revocation and stale-authority rejection;
- zero Agent/model/Tool/Context capability;
- WP-006 generated-code quarantine and untrusted-content semantics;
- WP-007 no-disclosure/no-reveal and sovereignty controls;
- WP-008 separation of signal, event, alert, incident, Evidence, Finding, Human Decision and execution authority; and
- no operational logging, detection, incident command, containment, recovery or reinstatement capability.

## 2. Mandatory semantic separation

The following distinctions must be structural, not merely descriptive:

`ARTIFACT VERIFIED ≠ ARTIFACT ACCEPTED ≠ ARTIFACT PROMOTED ≠ DEPLOYED`.

`VULNERABILITY DETECTED ≠ FINDING ≠ RISK ACCEPTED ≠ REMEDIATED ≠ SECURITY ACCEPTED`.

`RECOVERY ≠ REAUTHORIZATION`.

`RESTORATION ≠ REINSTATEMENT`.

| Object or state | Bounded meaning | Does not independently create |
|---|---|---|
| Artifact provenance record | Metadata identifying source, producer class, version, integrity and dependency/build references | Verification, acceptance, promotion or deployment authority |
| Artifact verification result | A bounded check result against named criteria and exact artifact/version | Institutional acceptance, security assurance, promotion or execution |
| Quarantine state | Denial of eligibility pending a separate current decision | A Finding, rejection of unrelated versions, or permission to alter/delete the artifact |
| Artifact acceptance | A Human-governed act for an exact artifact/version/scope | Promotion, deployment, runtime eligibility or infrastructure authority |
| Promotion/deployment | Separately authorized operational acts | Security acceptance merely because execution succeeded |
| Vulnerability signal/state | Metadata that a potential weakness was reported or detected | A Finding, severity authority, risk acceptance or remediation closure |
| Finding | An institutional conclusion under NCIE-008 | Risk acceptance, patch authority, remediation completion or security acceptance |
| Exception/risk acceptance | A current Human act for exact risk, scope, version and validity | Remediation, policy repeal, deployment or permanent waiver |
| Remediation result | Metadata that a bounded change was reported complete | Independent verification, Finding closure or security acceptance |
| Recovery candidate/state | A bounded source or system state proposed for recovery handling | Known-good status, reauthorization, restoration or reinstatement |
| Recovery acceptance | A Human acceptance act based on independent recovery review | Operational restoration, restored grants, go-live or reinstatement |

Agent/model/Tool/VPF output, scanner output, repository metadata, CI/CD output, Documents, logs, alerts, Evidence references, Memory, web/API content and other retrieved/external content remain untrusted data. They cannot create or modify provenance authority, acceptance, severity, Finding state, risk acceptance, remediation closure, known-good state, restoration permission or reinstatement authority.

## 3. Decision W16-D27 — HR9-23-1 artifact acceptance and generated-code security gates

### Option A — Provider-neutral artifact-control contracts with empty authorities and zero promotion

Approve a contract-only baseline containing:

- immutable source/artifact identity, version, integrity and provenance references;
- dependency and build provenance references without selecting a build or SBOM product;
- verification-criteria and verification-result metadata bound to an exact artifact/version;
- symbolic artifact states such as `UNVERIFIED`, `VERIFICATION_REQUIRED`, `VERIFIED_METADATA_ONLY`, `QUARANTINED`, `COMPROMISED`, `REVOKED` and `INDETERMINATE_DENY`;
- separate Human-governed artifact-acceptance, promotion and deployment references;
- generated-code security-gate metadata that inherits WP-006 quarantine;
- independent engineering-review and security-review interfaces;
- revocation metadata for previously accepted artifacts; and
- fail-closed evaluation of missing, stale, conflicting, unverifiable or revoked metadata.

Approve empty versioned registries for provenance requirements, integrity/version rules, dependency/build provenance requirements, verification criteria, quarantine rules, generated-code gate criteria, independent reviewers, artifact-acceptance authorities and acceptance revocations. All Human and institutional authority interfaces remain unassigned.

The reference boundary has no method to accept, promote, deploy, execute, publish, upload, download, delete or alter an artifact. A compromised or unverifiable artifact returns quarantine/deny. A previously accepted artifact whose acceptance is expired, revoked, stale, version-mismatched or unsupported by current provenance loses eligibility but is not silently deleted or rewritten.

Implications:

- WP-009 can prove the semantic separation and fail-closed behavior using synthetic metadata only.
- WP-006 generated code remains quarantined; the generator, producing Agent and implementer cannot self-approve.
- Verification can be represented without claiming institutional acceptance or NCIE-016 assurance.
- No repository, scanner, CI/CD system, build system, promotion path, environment or deployment authority is invented.

### Option B — Institution-supplied operational artifact governance

The Project Owner supplies or references the exact:

- artifact classes and accepted source/provenance requirements;
- accountable artifact-acceptance authority and Supply-Chain Security Owner;
- independent engineering and security reviewers, including independence rules;
- integrity algorithms, version-reference rules and build/dependency provenance criteria;
- generated-code security-gate criteria and prohibited artifact classes;
- verification, quarantine, release-from-quarantine and revocation criteria;
- repositories, registries, build systems, scanners, SBOM platform and CI/CD systems;
- promotion/deployment authorities, target environments and segregation of duties;
- residency regions, external destinations and cross-border constraints; and
- effective dates, review cadence, expiry and revocation process.

Implication: a later separately authorized package could integrate concrete controls after WBS-23 operational design and NCIE-016 verification prerequisites exist. This option cannot be implemented from the current record because the assignments, products and criteria are absent.

### Option C — Knowing deferral

Explicitly defer `HR9-23-1`. Every unverified, unverifiable, compromised, generated, stale-version or revoked artifact remains quarantined and ineligible. No artifact may be accepted, promoted or deployed, and WP-009 cannot be declared implementation-complete.

### Recommendation

Recommend `W16-D27: A`.

It extends the existing provider-neutral, empty-registry architecture without weakening WP-006 quarantine. It preserves Human-primary acceptance, exact-version scope, independent review and the boundary between security verification and operational promotion/deployment while inventing no product or authority.

## 4. Artifact and supply-chain control model proposed under W16-D27-A

### 4.1 Minimum metadata

A synthetic artifact-control envelope may contain only:

- opaque artifact, source, producer-class and producing-process references;
- artifact class and exact version reference;
- integrity-reference type and opaque value reference, not a secret;
- dependency-manifest, build, builder-class and build-input references;
- provenance-policy and verification-criteria versions;
- generated-code marker and WP-006 quarantine reference;
- verification result, reviewer-class reference and review independence state;
- quarantine reason class and release-eligibility state;
- artifact-acceptance decision reference, exact scope and validity state;
- promotion/deployment references as absent or separately governed; and
- expiry, revocation, supersession, residency and provenance references.

It must not contain credentials, signing keys, secrets, raw source payloads, governed production data, private chain-of-thought, real protected identity values, repository credentials, deployment tokens or content that itself grants authority.

### 4.2 Independence and revocation

- Producing Agent or generator cannot verify, accept, promote or deploy its own output.
- The implementer cannot be the sole security reviewer or artifact acceptor where independent review is required.
- Engineering review, security review, artifact acceptance, promotion approval and deployment execution are separate roles and acts.
- Acceptance applies only to the exact artifact/version/scope recorded; it does not flow to rebuilt, modified, repackaged or later versions.
- Revocation is prospective, preserved in history and immediately removes future eligibility under the reference evaluator.
- Quarantine release requires a separate current Human-governed record; elapsed time or a new scan result cannot release an artifact automatically.

## 5. Decision W16-D28 — HR9-24-1 vulnerability, remediation, exception and risk acceptance

### Option A — Provider-neutral vulnerability-state contracts with no silent acceptance

Approve immutable contracts for:

- vulnerability-state metadata and exact affected artifact/component/version references;
- source, detection-time, knowledge-time and provenance references;
- symbolic severity and exploitability references without a taxonomy or threshold;
- remediation, mitigation, compensating-control and verification references as separate objects;
- exception request, review, approval, expiry, renewal and revocation states;
- residual/unremediated-risk acceptance references as a separate Human Decision class;
- current risk-treatment authority, independent reviewer and security-acceptance interfaces; and
- stale vulnerability, stale exception, version mismatch and unknown-state fail-closed behavior.

Approve empty versioned registries for vulnerability policies, severity governance, remediation requirements, patch requirements, compensating controls, exception eligibility, exception authorities, risk-treatment authorities, risk acceptances, independent reviewers and security-acceptance authorities. All authority interfaces remain unassigned.

No severity level, deadline, exception duration or automatic action is populated. The reference evaluator can return only bounded states such as deny, remediation required, Human decision required or indeterminate deny. It cannot create a Finding, accept risk, patch, mitigate, close, waive, promote, deploy or declare security acceptance.

Implications:

- Vulnerability lifecycle semantics can be tested without accepting risk or selecting a scanner.
- No unresolved vulnerability becomes silently accepted because a deadline elapsed, an exception became stale or a scanner stopped reporting it.
- Expired exceptions do not auto-renew; revoked exceptions remain historical but confer no current treatment.
- Remediation completion remains distinct from independent verification and security acceptance.

### Option B — Institution-supplied operational vulnerability governance

The Project Owner supplies or references the exact:

- Vulnerability Management Owner, accountable remediation authority and responsible engineering owners;
- vulnerability taxonomy, severity model, scoring sources and override authority;
- remediation/patch deadlines and escalation rules by exact class;
- mitigation and compensating-control acceptance criteria;
- exception eligibility, prohibited classes, maximum duration and renewal rules;
- exception requester, independent reviewer, approver and revocation authority;
- unremediated/residual-risk acceptance authority, appetite and decision criteria;
- Finding authority, remediation verifier and security-acceptance authority;
- scanners, dependency services, repositories, ticketing/workflow systems and data sources;
- affected environments, operational destinations and residency/cross-border constraints; and
- stale-record, re-scan, disclosure and emergency-patch procedures.

Implication: this supports later operational remediation only after separate product, environment, access, WBS-23 and NCIE-016 decisions. It would still not merge detection, Finding, risk acceptance, remediation or security acceptance.

### Option C — Knowing deferral

Explicitly defer `HR9-24-1`. No exception or risk acceptance exists. Every known unresolved, stale, version-ambiguous or unverifiable vulnerability state remains deny/remediation-required for affected artifact eligibility. WP-009 cannot be declared implementation-complete.

### Recommendation

Recommend `W16-D28: A`.

It preserves the NCIE-008 Decision and exception lifecycle, blocks silent risk acceptance, and permits only metadata-level fail-closed evaluation. It does not invent vulnerability severities, deadlines, durations, products, Finding authority or institutional risk appetite.

## 6. Vulnerability, remediation and exception semantics proposed under W16-D28-A

### 6.1 Vulnerability state

The bounded state model may represent `REPORTED`, `DETECTED`, `TRIAGE_REQUIRED`, `REMEDIATION_REQUIRED`, `MITIGATION_REVIEW_REQUIRED`, `EXCEPTION_REVIEW_REQUIRED`, `VERIFICATION_REQUIRED`, `UNRESOLVED`, `STALE` and `INDETERMINATE_DENY`. These are metadata states, not institutional Findings or risk decisions.

Every record must bind the exact affected artifact/component/version. Missing or conflicting version identity means the affected artifact is ineligible. A scanner result may update an observation only through a separately governed adapter; it cannot establish severity authority, a Finding, risk acceptance or closure.

### 6.2 Remediation and security acceptance

- A remediation proposal is not patch authority.
- A patch/build output is a new or changed artifact and re-enters provenance, verification and acceptance controls.
- A remediation-complete assertion is not independent verification.
- A clean re-scan is not a Finding closure or security acceptance.
- Security acceptance requires its own current Human authority and NCIE-016-governed verification inputs.
- Historical vulnerability, remediation and exception metadata is not erased by closure or supersession.

### 6.3 Exception lifecycle and stale handling

An exception must be exact, scoped, time-bounded, attributable, independently reviewed and revocable. It must reference compensating controls and current risk-treatment authority. It never creates a technical capability or repeals policy.

Until an exact duration and authority are assigned, no exception can become active. An expired, revoked, superseded, version-mismatched or otherwise stale exception provides no permission and cannot auto-renew. A stale vulnerability record cannot be treated as resolved; it returns `HUMAN_DECISION_REQUIRED / DENY` pending current evaluation.

No silence, workflow timeout, missing scan, lack of exploit observation, low symbolic severity, operational convenience or successful deployment constitutes risk acceptance.

## 7. Decision W16-D29 — HR9-25-1 compromised state and security recovery acceptance

### Option A — Provider-neutral recovery-security contracts with zero restoration capability

Approve immutable contracts for:

- known-good, unknown, suspected-compromised, compromised, quarantined and verification-required state metadata;
- backup, snapshot, checkpoint and artifact provenance/integrity/version references;
- quarantine-before-restoration and recovery-source eligibility evaluation;
- current revocation, restriction, deletion, classification and security-state references;
- credential, key and session invalidation/rotation obligation references without execution;
- recovery-plan, recovery-result and post-recovery reconciliation metadata;
- current authorization evaluation after recovery;
- independent recovery-review and security-recovery acceptance references; and
- separate operational restoration and reinstatement references.

Approve empty versioned registries for recovery-source criteria, known-good criteria, compromised-state rules, quarantine rules, invalidation obligations, reconciliation requirements, recovery authorities, independent recovery reviewers, security-recovery acceptance authorities, restoration authorities and reinstatement authorities. All Human and institutional authority interfaces remain unassigned.

The reference boundary has no method to back up, snapshot, recover, restore, fail over, rotate credentials, invalidate sessions, reconcile a live system, reinstate access or execute a runbook. Unknown or unverifiable state is treated as compromised and denied. A recovery result cannot restore authorization or operational service.

Implications:

- WP-009 can model the security boundary without touching a live or persistent system.
- Stale grants, revoked artifacts, ineligible Agents/models/Tools and compromised state cannot be revived by restoration.
- Credential/key/session actions remain obligation references routed to future authorized operations.
- Recovery acceptance remains distinct from operational restoration and NCIE-016 acceptance evidence.

### Option B — Institution-supplied operational recovery governance

The Project Owner supplies or references the exact:

- Resilience/Recovery Security Owner and accountable recovery authority;
- known-good and compromised-state criteria;
- approved backup, snapshot, artifact and key/credential provenance requirements;
- recovery-source stores, products, platforms, accounts, regions and environments;
- quarantine, malware/integrity verification and release criteria;
- credential/key/session invalidation and rotation authorities and procedures;
- reconciliation rules for identities, grants, revocations, eligibility, secrets and security state;
- recovery executor, independent recovery reviewer and security-recovery acceptance authority;
- restoration, service-return and reinstatement authorities;
- RPO/RTO and other recovery thresholds; and
- destinations, residency rules, cross-border constraints and runbooks.

Implication: a later operational package could perform recovery only after WBS-23 infrastructure/runbook authority and NCIE-016 scenario, independence and acceptance prerequisites are separately approved. No source allows these values to be inferred now.

### Option C — Knowing deferral

Explicitly defer `HR9-25-1`. Every unknown, suspected-compromised, compromised, stale or unverifiable source remains quarantined and ineligible. No recovery, restoration or reinstatement capability exists, and WP-009 cannot be declared implementation-complete.

### Recommendation

Recommend `W16-D29: A`.

It directly implements the source rule that unknown integrity is treated as compromised and preserves current authorization, revocation and eligibility state. It separates security-recovery acceptance from restoration/reinstatement while selecting no backup product, environment, threshold or operational authority.

## 8. Recovery, restoration and reconciliation model proposed under W16-D29-A

### 8.1 Recovery-source eligibility

A recovery candidate may be considered for Human review only when its metadata has exact source, version, integrity, creation-context, classification, residency and provenance references. `KNOWN_GOOD` is not inferred from age, location, readability, prior use, a successful backup job or a product label. Missing, stale, conflicting or unverifiable metadata means `COMPROMISED_OR_UNKNOWN / QUARANTINED / DENY`.

### 8.2 Quarantine and preservation

- Recovery candidates remain quarantined before restoration.
- Quarantine does not erase, overwrite or silently repair the candidate.
- Revocation and security-state history is preserved and carried into reconciliation.
- A previously accepted artifact that is now revoked remains revoked after recovery.
- Deleted/restricted identities and expired grants are not resurrected from a backup.
- Compromised or unknown credentials, keys and sessions generate obligation references only; WP-009 cannot invalidate or rotate them.

### 8.3 Post-recovery reconciliation

Reconciliation compares recovered metadata against current authoritative identity, authorization, revocation, classification, deletion, Agent/model/Tool/VPF eligibility, artifact acceptance and security-policy state. Current state wins. Contradiction or unavailable current state fails closed.

An independent recovery reviewer must be separate from the recovery requester/executor and cannot rely solely on the producing system's self-attestation. A security-recovery acceptance record must bind the exact recovered target/version/scope and current review inputs.

`RECOVERY ≠ REAUTHORIZATION`.

`RECOVERY ACCEPTED ≠ OPERATIONALLY RESTORED`.

`RESTORATION ≠ REINSTATEMENT`.

## 9. Authorities and operational values that remain UNASSIGNED / UNSPECIFIED

### 9.1 Human and institutional authorities

- accountable artifact-acceptance authority;
- Supply-Chain Security Owner;
- provenance/integrity policy owner;
- artifact verifier and verification-criteria approver;
- quarantine and release-from-quarantine authority;
- independent engineering reviewer;
- independent security reviewer;
- generated-code security-gate approver;
- artifact acceptance/revocation authority;
- promotion authority, deployment authority and deployment executor;
- Vulnerability Management Owner;
- vulnerability triage, severity and remediation authorities;
- patch requester, approver and executor;
- mitigation/compensating-control approver;
- exception requester, independent reviewer, approver and revoker;
- unremediated/residual-risk acceptance authority;
- Finding authority, remediation verifier and security-acceptance authority;
- Resilience/Recovery Security Owner;
- compromised-state determination authority;
- recovery-source and known-good determination authority;
- recovery requester, approver and executor;
- credential/key/session invalidation and rotation authorities;
- post-recovery reconciliation authority;
- independent recovery reviewer;
- security-recovery acceptance authority;
- operational restoration authority; and
- reinstatement and reauthorization authorities.

### 9.2 Criteria, classifications, thresholds and periods

- artifact classes and acceptance criteria;
- provenance and integrity algorithms/thresholds;
- dependency/build provenance and SBOM criteria;
- verification pass/fail criteria and required review depth;
- quarantine entry/release criteria and review cadence;
- generated-code gate criteria and prohibited artifact classes;
- vulnerability taxonomy, severities, scores and thresholds;
- exploitability, materiality and escalation thresholds;
- remediation and patch deadlines;
- mitigation and compensating-control sufficiency criteria;
- exception eligibility, prohibited classes, duration and renewal limits;
- risk appetite, residual-risk and unremediated-risk acceptance criteria;
- stale vulnerability/exception ages and re-evaluation cadence;
- known-good, compromised and recovery-source criteria;
- RPO, RTO and recovery/reconciliation thresholds;
- invalidation/rotation timing; and
- recovery acceptance, restoration and reinstatement criteria.

### 9.3 Products, repositories, systems, environments and destinations

- source-code hosts, artifact/package/container/model registries and repositories;
- dependency services, SBOM platforms and provenance/signing systems;
- build systems, CI/CD systems, runners and promotion pipelines;
- static, dynamic, dependency, secret, container, model and vulnerability scanners;
- vulnerability databases, feeds, ticketing and remediation workflow products;
- backup, snapshot, archive, replication, failover and recovery products;
- key/credential/session management products;
- development, test, security, staging, production, recovery and disaster-recovery environments;
- accounts, credentials, endpoints, networks, providers and regions;
- notification, disclosure, repository, scanner and recovery destinations;
- African or other data-residency region assignments;
- cross-border destinations, transfer mechanisms or exceptions; and
- operational teams, rosters, runbooks, schedules and assignments.

Until explicitly assigned: `DENY / QUARANTINE / NO ACCEPTANCE / NO PROMOTION / NO DEPLOYMENT / NO EXCEPTION / NO RISK ACCEPTANCE / NO PATCH / NO RECOVERY / NO RESTORATION / NO REINSTATEMENT`.

## 10. Proposed non-waivable WP-009 protections

1. Human-primary authority: generated output, products and external content cannot create acceptance, Findings, risk decisions, recovery status or execution authority.
2. Current four-layer authorization remains mandatory for every consequential action.
3. Artifact provenance, exact version and integrity references are mandatory; unverifiable or conflicting state fails closed.
4. Artifact verification, acceptance, promotion and deployment remain separate acts.
5. Generated code inherits WP-006 quarantine and cannot execute, self-approve or bypass independent review.
6. Producer, generator or implementer cannot be the sole verifier, acceptor, promoter or deployer where independence is required.
7. Compromised, revoked, stale-version or unverifiable artifacts remain quarantined and ineligible.
8. Artifact acceptance is exact-scope, exact-version, time-aware and revocable; it creates no deployment capability.
9. Vulnerability detection, Finding, risk acceptance, remediation and security acceptance remain separate acts.
10. Severity, scanner output, elapsed time, silence or operational convenience never creates authority or risk acceptance.
11. Exceptions are exact, scoped, time-bounded, independently reviewed, revocable and never auto-renewed or treated as policy repeal.
12. Expired, revoked, stale, ambiguous or unassigned remediation/exception/risk state means deny; unresolved risk is never silently accepted.
13. Unknown or unverifiable recovery state is treated as compromised and quarantined before any restoration consideration.
14. Recovery preserves revocation, restriction, deletion, classification, provenance and security-state history; stale grants or eligibility cannot be restored.
15. Credential/key/session invalidation and rotation remain separately authorized obligations; WP-009 cannot execute them.
16. Recovery acceptance, operational restoration, reauthorization and reinstatement remain separate Human-controlled acts with independent review.
17. WBS-20, WBS-23 and NCIE-016 boundaries remain intact; local records are not institutional Evidence, Findings, operations or acceptance.
18. Only minimized synthetic metadata is permitted locally; no governed production data or cross-border transfer is allowed. Unknown residency or destination means deny.

No option, exception or implementation shortcut may waive these protections within WP-009.

## 11. Exact proposed WP-009 implementation scope

The Project Owner subsequently issued the separate explicit implementation authorization `NCIE-WBS16-OWNER-DECISION-2026-09-24-033`. Under that authority, WP-009 may include only:

1. immutable provider-neutral metadata contracts for artifact provenance, integrity/version, dependency/build provenance, verification, quarantine, generated-code gates, acceptance/revocation and distinct promotion/deployment references;
2. immutable provider-neutral metadata contracts for vulnerability state, affected component/version, remediation/mitigation, exception lifecycle, risk-treatment references, independent review and security acceptance;
3. immutable provider-neutral metadata contracts for compromised/unknown/known-good state, recovery-source provenance, quarantine, invalidation obligations, reconciliation, recovery review/acceptance, restoration and reinstatement references;
4. empty versioned registries for every policy, criterion, authority, exception, acceptance, review and revocation class identified in this pack;
5. unassigned Human/institutional authority interfaces;
6. fail-closed metadata evaluation for artifact eligibility, verification, quarantine, acceptance validity, vulnerability treatment, exception validity, risk acceptance, recovery-source eligibility, reconciliation and recovery/restoration/reinstatement authority;
7. a no-artifact-action boundary with no accept, promote, deploy, publish, execute, upload, download or repository method;
8. a no-remediation boundary with no scan, patch, mitigate, waive, close or live-system method;
9. a no-recovery boundary with no backup, restore, failover, credential rotation, session invalidation, reconciliation or reinstatement method;
10. synthetic false-authority, prompt-injection, generated-code self-approval, provenance-conflict, stale-exception, silent-risk-acceptance, stale-grant and compromised-recovery tests;
11. deterministic standard-library unit, contract and negative-path tests only;
12. cumulative WP-001 through WP-008 regression;
13. traceability to `HR9-23-1` through `HR9-25-1`; and
14. local implementation evidence clearly marked non-institutional and non-acceptance.

## 12. Explicit exclusions

The proposed WP-009 package excludes:

- any real artifact acceptance, promotion, deployment, publication or execution;
- any real/generated artifact payload, source-code ingestion, package retrieval or repository interaction;
- CI/CD, artifact registry, dependency, SBOM, signing, provenance or scanner product selection/activation;
- live vulnerability scanning, ticketing, patching, remediation, mitigation or exception processing;
- a Finding, risk acceptance, policy waiver, security acceptance or residual-risk decision;
- live backup, snapshot, failover, recovery, restore, reconciliation, credential/key/session action or reinstatement;
- backup/recovery product, platform, store, environment or runbook selection/activation;
- populated authorities, criteria, thresholds, severities, deadlines, durations, repositories, environments or destinations;
- institutional Evidence, canonical audit/provenance, custody or Findings;
- governed production data or production-like protected values;
- provider, account, credential, endpoint, network, external-system or cross-border capability;
- new dependencies, infrastructure or deployment;
- independent verification, accreditation, controlled acceptance or go-live; and
- WP-010 or later WBS-16 implementation.

## 13. Stop conditions

Stop the affected scope and return for Human decision if work requires:

1. selecting or recording a Human-controlled option without an explicit Project Owner decision;
2. a real artifact, source repository, dependency, build, package, image, model, Agent Pattern or Tool payload;
3. acceptance, promotion, deployment, publication, execution or release from quarantine;
4. a concrete authority holder, reviewer, operator, team, roster or operational assignment;
5. an artifact criterion, integrity algorithm, severity, threshold, deadline, exception duration, risk appetite, RPO/RTO or recovery criterion;
6. a populated acceptance, exception, risk, recovery, restoration or reinstatement registry;
7. a repository, registry, CI/CD system, scanner, SBOM/signing service, vulnerability feed, backup/recovery platform or workflow product;
8. live scanning, patching, remediation, mitigation, exception, risk acceptance, recovery, restoration, reconciliation or credential/key/session action;
9. institutional Evidence, canonical provenance/audit, a Finding, Human Decision or acceptance claim;
10. governed production data, secrets, credentials, protected identity values or production-like payloads;
11. a provider, endpoint, account, network, environment, external destination or cross-border transfer;
12. weakening current authorization, independence, segregation of duties, minimization, provenance, sovereignty or a WP-001 through WP-008 boundary;
13. a new dependency, infrastructure or deployment;
14. an NCIE-016 verification/pass/assurance/acceptance claim; or
15. WP-010 or later implementation.

The fallback remains `DENY / NO CAPABILITY`.

## 14. Proposed local completion criteria

WP-009 could be declared locally implementation-complete only after all applicable criteria are evidenced:

1. The Project Owner has explicitly selected W16-D27, W16-D28 and W16-D29 options.
2. A separate Project Owner decision has released the exact WP-009 implementation scope.
3. Artifact verification, acceptance, promotion and deployment are structurally distinct.
4. Vulnerability detection, Finding, risk acceptance, remediation and security acceptance are structurally distinct.
5. Recovery, reauthorization, restoration and reinstatement are structurally distinct.
6. Exact artifact/component/version and provenance references are mandatory.
7. Dependency/build provenance is represented without a product or operational build.
8. Generated code remains quarantined under WP-006 and cannot self-approve or execute.
9. Producer/generator/implementer self-approval is rejected where independence is required.
10. Compromised, unverifiable, revoked, stale-version and conflicting artifacts fail closed.
11. Previously accepted artifacts can become ineligible through current expiry/revocation without history erasure.
12. Vulnerability severity is symbolic/unassigned and cannot trigger risk acceptance or operational action.
13. No remediation deadline, exception duration, threshold or risk appetite is invented.
14. Exceptions cannot activate without current exact authority, scope, validity and independent review.
15. Expired/revoked/stale exceptions fail closed and cannot auto-renew.
16. No unresolved vulnerability is silently risk-accepted.
17. Patch/remediation metadata cannot create independent verification, Finding closure or security acceptance.
18. Unknown or unverifiable recovery state is treated as compromised and quarantined.
19. Recovery-source provenance and exact version are mandatory.
20. Current revocation, restriction, deletion, classification and eligibility state survives recovery.
21. Stale grants, credentials, sessions, Agents, models, Tools, VPF eligibility and artifact acceptance are not restored.
22. Credential/key/session invalidation remains a non-executing reference only.
23. Post-recovery reconciliation fails closed when current authoritative state is unavailable or contradictory.
24. Recovery acceptance creates no operational restoration or reinstatement capability.
25. Every controlled registry is empty and every Human/institutional authority interface unassigned.
26. No artifact repository, scanner, CI/CD, SBOM, backup/recovery product, environment or external destination exists.
27. Only minimized synthetic metadata is used; no governed production data, secret or protected value exists.
28. African data residency remains deny-by-default for unknown or cross-border destinations.
29. Agent/model/Tool/VPF and retrieved/external content remain untrusted and non-authoritative.
30. Comprehensive synthetic negative tests cover false authority, self-approval, provenance conflict, version substitution, stale state, silent risk acceptance, exception auto-renewal, compromised recovery and stale-grant restoration.
31. Cumulative WP-001 through WP-008 regression passes.
32. Strict typing, lint, formatting, compilation, reproducibility and template-verification gates pass without a new dependency.
33. Traceability maps `HR9-23-1` through `HR9-25-1` to the selected decisions, contracts, tests, evidence and deferred authorities.
34. Local evidence states that it is not institutional Evidence, a Finding, artifact acceptance, risk acceptance, recovery proof, NCIE-016 verification, accreditation, controlled acceptance or go-live.

## 15. Downstream boundaries

### WBS-20 — Evidence, Provenance & Audit

WP-009 may carry opaque references to prospective provenance, Evidence, audit, custody, revocation and preservation records. It cannot create institutional Evidence, canonical provenance/audit, custody chains, Findings, defensibility claims or persistent stores. WBS-20/NCIE-010 retains those meanings and operations.

An artifact provenance envelope in WP-009 is security-control metadata, not the canonical institutional provenance record. A vulnerability or recovery record is not a Finding or Evidence merely because it is immutable.

### WBS-23 — DevSecOps, infrastructure and deployment

WP-009 may define provider-neutral adapters and obligation references only. WBS-23/NCIE-015 retains product selection and operation of repositories, build systems, CI/CD, scanners, SBOM/signing systems, vulnerability tooling, patching, environments, deployment/promotion, backup, restore, failover, secrets/key services, networks, infrastructure and runbooks.

Artifact acceptance under WP-009 cannot operate a WBS-23 promotion/deployment path. Security-recovery acceptance cannot operate a WBS-23 restore or service-return path.

### NCIE-016 — independent security verification and acceptance

Local WP-009 tests may verify contract shape and deterministic fail-closed behavior only. They do not execute NCIE-016 security, supply-chain or recovery scenarios; create test Evidence; establish scanner effectiveness; prove an artifact safe; prove remediation effective; validate production recovery; or grant acceptance/sign-off.

NCIE-016 retains independent security/recovery review, test evidence, verification matrices and acceptance/sign-off architecture. Its unresolved authority, tool, threshold, scenario and RPO/RTO items cannot be invented by WP-009.

## 16. Recorded Project Owner decision

- `W16-D27: A` — provider-neutral artifact provenance, verification, quarantine, generated-code security-gate, acceptance/revocation and independent-review contracts with empty controlled registries, unassigned authorities and zero artifact acceptance, promotion, deployment or execution capability.
- `W16-D28: A` — provider-neutral vulnerability, remediation, mitigation, exception and residual-risk treatment contracts with symbolic severity, empty controlled registries, unassigned authorities and zero remediation, exception activation, risk acceptance or security-acceptance capability.
- `W16-D29: A` — provider-neutral compromised-state, recovery-source, quarantine, reconciliation, independent-review and security-recovery acceptance contracts with empty controlled registries, unassigned authorities and zero backup, recovery, restoration, reauthorization or reinstatement capability.
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`.
- Decision date: `2026-09-24`.
- Conditions: `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`, all mandatory semantic separations in Section 2 and all eighteen non-waivable protections in Section 10.
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-24-032`.
- Evidence type: `Self-Authorized Project Owner Decision`.

This decision defines architecture only. The separately recorded `NCIE-WBS16-OWNER-DECISION-2026-09-24-033` later authorized only the exact Section 11 implementation scope. It authorizes no artifact acceptance, quarantine release, promotion, deployment, publication, execution, vulnerability/risk acceptance, remediation, recovery, restoration, reauthorization, reinstatement, product selection, source-control release, independent verification, accreditation, controlled acceptance or go-live. No WP-010 implementation is authorized.

## 17. Source traceability and VPF boundary

Primary controlled sources:

- NCIE-009 Chapters 23–25, Tables 31–33, SEC-T8/SEC-T9 and `HR9-23-1` through `HR9-25-1`;
- NCIE-008 Chapters 4, 5, 6, 21 and 23;
- NCIE-004 generated-code engineering, supply-chain and recovery boundaries;
- NCIE-006 recovery, reconciliation, historical provenance and current-authorization boundaries;
- NCIE-007 generated-code, Agent/model/Tool eligibility and checkpoint-recovery boundaries;
- NCIE-016 Chapters 19, 24, 30–32 and 37, including independent security/recovery verification and acceptance boundaries;
- NCIE-017 WBS-16, WBS-20, WBS-23 and WBS-24 sequencing boundaries;
- `implementation/WBS16_REMAINING_SCOPE_AND_COMPLETION_CRITERIA.md`; and
- the controlled WP-001 through WP-008 decisions, implementations and handovers.

VPF is applied behaviorally to Human-primary authority, least privilege, explainability, provenance, minimization, sovereignty, dignity and African data-residency/cross-border boundaries. The VPF configuration is not modified or redistributed. No VPF runtime, validator, checksum, signature, certificate, ledger, PADCA/Omnis exchange, quarantine action or residency-enforcement service is claimed to have executed.

## 18. Decision disposition

Disposition: `ARCHITECTURE APPROVED / BOUNDED IMPLEMENTATION AUTHORIZED UNDER ...-033`.

The Project Owner selections are recorded under evidence reference `NCIE-WBS16-OWNER-DECISION-2026-09-24-032`; bounded implementation authority is separately recorded under `...-033`. The completed local implementation creates no product integration, real artifact action, remediation, risk acceptance, recovery, institutional Evidence or Finding. Source-control release remains unauthorized.

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.
