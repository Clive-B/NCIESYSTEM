# NCIE WBS-16-WP-008 Human Review Decision Pack

Status: `DECIDED — ARCHITECTURE APPROVED / NO IMPLEMENTATION AUTHORITY`

Prepared: `2026-09-24`

Work package: `WBS-16-WP-008 — Security Logging, Detection and Incident-Control Contracts`

Decision scope:

- `HR9-20-1` — security-log access, retention policy and independent assurance boundaries;
- `HR9-21-1` — monitoring ownership, detection/escalation classes and severity governance; and
- `HR9-22-1` — incident command, notification obligations, containment rights and restoration/recovery decision boundaries.

This pack prepares choices only. It does not decide an option, authorize implementation, activate monitoring, create a log or audit store, declare an incident, send a notification, execute containment or recovery, create institutional Evidence or Findings, select a product, or authorize WP-009 or later scope.

No WP-008 implementation is authorized by this pack.

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

## 1. Source-grounded baseline

### 1.1 NCIE-009 Chapter 20 — security logging

NCIE-009 Chapter 20 requires the following distinctions and constraints:

- operational telemetry, security audit evidence and canonical provenance serve different purposes and have different access and retention rules;
- a security log is not automatically an audit record, and neither is automatically the provenance record of record;
- logging does not authorize disclosure, and access to a security log is itself an authorization decision;
- secrets, raw prompts and raw protected data are minimized by construction rather than relying on later redaction;
- event, actor, target and time references are sufficient for the bounded security-event interface, with tamper-resistance and cross-source correlation deferred to the operational architecture;
- the accountable authority class, Security Logging Owner and NCIE-008 Chapter 23 Assurance/Audit holder remain to be assigned; and
- `HR9-20-1` is Non-Blocking for interim security-event capture, but still requires institutional confirmation of access, retention and the assurance interface.

### 1.2 NCIE-009 Chapter 21 — detection and monitoring

NCIE-009 Chapter 21 defines detection across these source categories:

1. identity/access anomalies;
2. exfiltration indicators;
3. Agent abuse;
4. prompt-injection indicators; and
5. network anomalies.

The chapter also requires suspicious Tool and data behavior to be observable through the applicable category and triage boundary. Each detection category has a triage path into Chapter 22 where warranted. An analytics alert may trigger response, but does not itself become institutional Evidence, a Finding or a Decision. Monitoring that unnecessarily collects sensitive payloads is itself a control failure.

The accountable authority class, Detection/Monitoring Owner, escalation classes and severity governance remain unassigned under `HR9-21-1`.

### 1.3 NCIE-009 Chapter 22 and NCIE-008 Chapter 22 — incident authority

The source incident sequence distinguishes detection, triage, containment, revocation, isolation, evidence preservation and notification. Containment may temporarily suspend an identity, Agent, Tool, model or session only under governed emergency authority; it is not an ad hoc security action.

Every emergency action requires actor, target, scope, trigger and time metadata and a notification obligation to the affected domain's Accountable Authority. The acting Emergency Authority cannot be the sole reinstating authority. Independent post-event review determines reinstatement or permanent disposition.

Historical state is preserved through containment. Recovery handoff occurs only after containment is confirmed effective, and `RECOVERY ≠ REAUTHORIZATION`.

The Emergency Authority, Incident Response Owner, responsible operator, notification obligations, containment rights and independent restoration/reinstatement authority remain unassigned. Because `HR9-22-1` is Blocking, operational incident command or containment cannot be activated without a Human decision.

### 1.4 Existing controlled architecture

WP-008 must remain subordinate to the controls already implemented in WP-001 through WP-007:

- current four-layer object/field/action/purpose authorization;
- empty institutional mappings and zero grants;
- unassigned privilege and emergency authorities;
- explicit expiry, revocation and stale-authority rejection;
- no secrets, protected values or unapproved egress;
- Agent/model/Tool/VPF and retrieved/external content remain untrusted;
- zero Agent/model/Tool/Context capability;
- zero disclosure, output, Protected Reveal or cross-border transfer capability; and
- all security/privacy signals remain minimized and non-authoritative.

No WP-008 contract may bypass or reinterpret those boundaries.

## 2. Mandatory semantic separation

The following objects must remain distinct. Transition from one to another requires the separately governed act stated below; labels or generated content cannot collapse the distinction.

| Object | Bounded meaning | Cannot independently become |
|---|---|---|
| Operational/security signal | Minimized, non-authoritative observation about a technical or policy condition | Security Event, alert, Incident, Evidence, Finding, Decision or authority |
| Security Event | Immutable metadata stating that a security-relevant occurrence was observed or reported | Detection conclusion, institutional Evidence, Incident or authorization |
| Detection/alert | Versioned analytic result linking source event references to a detection category and triage disposition | Finding, Human Decision, incident declaration or containment permission |
| Incident | A Human-governed incident record after the applicable declaration authority acts | Evidence, Finding, permanent revocation or execution authority merely because severity is high |
| Evidence | A governed WBS-20/NCIE-010 object with custody, provenance and admissibility semantics | Finding, Decision or authorization merely by existing |
| Finding | An accountable institutional conclusion issued through NCIE-008 Chapter 18 | Human Decision, containment execution or permanent disposition automatically |
| Human Decision | A current governed act bound to exact holder, target, scope, version, purpose and validity | Technical execution unless separately authorized and available |
| Containment/execution authority | Current, exact permission for a named Human/operator to perform a bounded action on a bounded target | Incident command, Finding authority, restoration authority or standing policy |

Required invariants:

`SIGNAL ≠ SECURITY EVENT ≠ DETECTION/ALERT ≠ INCIDENT ≠ EVIDENCE ≠ FINDING ≠ HUMAN DECISION ≠ EXECUTION AUTHORITY`.

`SEVERITY ≠ AUTHORITY`.

`INCIDENT DECLARED ≠ CONTAINMENT AUTHORIZED ≠ CONTAINMENT EXECUTED`.

`CONTAINMENT EFFECTIVE ≠ RECOVERY AUTHORIZED ≠ REINSTATEMENT AUTHORIZED`.

## 3. Decision W16-D24 — HR9-20-1 security-log access, retention and assurance

### Option A — Provider-neutral contract baseline with empty policies and zero persistence

Approve immutable, provider-neutral metadata contracts for:

- minimized security-event records;
- log classification and access-purpose references;
- current actor/object/field/action/purpose authorization references;
- access-decision, disclosure-decision and authority references as separate fields;
- retention-policy references with explicit effective/expiry/revocation metadata but no default duration;
- legal-hold, deletion and disposition references without implementing storage or deletion;
- correlation and provenance references;
- independent assurance request/recommendation metadata; and
- access, retention and assurance evaluation whose empty registries always deny.

Approve empty versioned registries for security-log access rules, retention rules, legal holds, disclosure rules and assurance assignments. Keep every authority interface unassigned. Implement no capture pipeline, persistent store, query capability, disclosure, export or deletion operation.

Implications:

- WP-008 can prove data minimization, separation of records and fail-closed access without storing a log.
- No retention duration, log destination, assurance holder or disclosure permission is invented.
- An unavailable required audit/assurance boundary returns deny/Human review required.
- WBS-20 still owns institutional Evidence, canonical audit/provenance, custody and persistence.
- WBS-23 still owns operational collection, storage, SIEM/observability products and infrastructure.

### Option B — Institution-supplied operational policy

The Project Owner supplies or references the exact:

- accountable security-log authority and Security Logging Owner;
- independent Assurance/Audit holder and reporting route;
- classification-to-access matrix and permitted purposes;
- retention, legal-hold, deletion and disposition periods;
- approved stores, regions and cross-border constraints;
- disclosure/export rules and destinations; and
- effective dates, review cadence and revocation process.

Implication: a later work package could implement concrete policy adapters, but only after technology, residency, storage, WBS-20 and WBS-23 prerequisites are separately authorized. This option is not implementable safely from the current record because those assignments and values are absent.

### Option C — Knowing deferral

Explicitly defer `HR9-20-1`. NCIE-009 says the item is Non-Blocking for ongoing security-event capture, but this controlled WP-008 scope authorizes no capture. Under this option, WP-008 would not implement access, retention or assurance contracts and could not satisfy the proposed WP-008 completion criteria.

### Recommendation

Recommend `W16-D24: A`.

It aligns with the existing empty-registry, provider-neutral architecture and allows deterministic contract testing without inventing retention periods, authority holders, stores or disclosure paths. It also preserves the WBS-20 Evidence/Audit and WBS-23 operational-infrastructure boundaries.

## 4. Minimized security-event contract proposed under W16-D24-A

A synthetic security-event envelope may contain only metadata such as:

- event, correlation, source and policy-version references;
- occurrence time and observation/knowledge time;
- actor/principal class and opaque actor reference;
- target class and opaque target reference;
- action/event class;
- outcome state: success, failure, unknown or indeterminate;
- classification and sensitive-access marker;
- current authorization/delegation/approval reference where applicable;
- source event/signal references;
- provenance and integrity-control references;
- residency/jurisdiction class reference;
- retention-policy and access-policy references; and
- expiry/revocation state of the governing metadata.

The contract must not contain:

- secrets, credentials, tokens, keys or authentication material;
- raw prompts, private chain-of-thought or model hidden state;
- real protected identity values or raw protected data;
- Document, Memory or Evidence payloads;
- precise sensitive Tool results or content bodies;
- notification addresses or operational endpoints; or
- any field whose value itself grants authority.

Unknown actor, target, action, purpose, classification, policy, residency, retention, authority or current-authorization state means deny/no access. Security-log access is not disclosure authority, and neither access nor retention metadata creates WBS-20 Evidence.

## 5. Decision W16-D25 — HR9-21-1 monitoring, detection/escalation and severity

### Option A — Source-category contracts with unassigned ownership and symbolic severity

Approve provider-neutral detection contracts for the five source categories in Section 1.2. NCIE-009 also requires coverage of suspicious Tool and data behavior but does not assign either a standalone class in its five-item class sentence. WP-008 therefore carries them only as source-behavior references and returns `HUMAN_DECISION_REQUIRED` for class assignment; it does not invent a sixth category.

Approve:

- immutable detection-rule and detection-result metadata;
- exact source-event references and provenance;
- explicit analytic confidence/quality-state references without numeric thresholds;
- triage and escalation dispositions that can request Human review but cannot declare an incident;
- a symbolic severity reference whose taxonomy and thresholds remain unassigned;
- current policy/effective/expiry/revocation metadata;
- separate rule-owner, monitoring-owner, triage-owner, severity-governance and assurance interfaces; and
- empty versioned detection-rule, escalation, severity-governance and monitoring-authority registries.

The reference boundary evaluates only synthetic metadata. It performs no monitoring, aggregation, polling, streaming, correlation against external data, alert delivery, paging or incident creation.

Implications:

- The five source-defined detection categories are testable without inventing thresholds or severity labels.
- An alert can return `TRIAGE_REQUIRED` or `HUMAN_DECISION_REQUIRED`, but cannot become a Finding, Decision, incident or containment grant.
- Unknown or stale rule, severity, owner or escalation route fails closed.
- Agent/model/Tool/VPF and external content cannot assert that an incident exists or change severity/route/authority.

### Option B — Institution-supplied operational monitoring governance

The Project Owner supplies or references:

- accountable and responsible monitoring owners;
- exact detection rules, analytic methods and validation requirements;
- severity taxonomy, thresholds and downgrade/upgrade authority;
- triage and escalation classes with response objectives;
- notification/paging routes and recipients;
- monitoring products, data sources, destinations and residency controls; and
- independent review, quality and false-positive governance.

Implication: this supports operational monitoring only after WBS-23 infrastructure and product decisions, current access authorization, approved data flows and NCIE-016 verification are separately released. None of those are authorized now.

### Option C — Knowing deferral

Explicitly defer `HR9-21-1`. NCIE-009 says this is Non-Blocking for the already specified detection categories, but without approved ownership/severity governance WP-008 could define only the raw category taxonomy and deny every triage/escalation outcome. It could not satisfy the complete WP-008 decision baseline.

### Recommendation

Recommend `W16-D25: A`.

It preserves the exact source categories and semantic separation while avoiding invented severity levels, thresholds, owners, products or destinations. It matches the existing NCIE pattern in which symbolic contracts precede operational assignment.

## 6. Detection, escalation and severity semantics proposed under W16-D25-A

### 6.1 Detection result

A detection result is immutable metadata linking:

- detection/rule/correlation references;
- one approved detection category;
- source security-event references;
- policy/version and provenance references;
- evaluation time and rule validity;
- classification and minimization disposition;
- quality/confidence-state reference;
- severity reference, which remains `UNSPECIFIED` unless governed; and
- triage disposition.

The proposed bounded reference dispositions are:

- `NO_MATCH`;
- `TRIAGE_REQUIRED`;
- `HUMAN_DECISION_REQUIRED`; and
- `INDETERMINATE_DENY`.

These are evaluation/routing states only. They do not declare an incident or authorize denial, quarantine or containment.

### 6.2 Severity governance

WP-008 must not invent labels, numeric ranges, thresholds, response times or automatic actions. A severity contract may carry an opaque severity-class reference, policy version, assigning-authority reference, effective/expiry times and revocation state. Until a current exact governance record exists:

- severity is `UNSPECIFIED`;
- no priority, paging, notification or containment right follows;
- no downgrade or closure is permitted; and
- the safe result is `HUMAN_DECISION_REQUIRED / NO CAPABILITY`.

Severity may inform triage but never creates incident, Finding, Decision or execution authority.

### 6.3 Injection and false-authority boundary

Instructions contained in logs, alerts, Documents, Evidence references, Memory, web/API content, Tool output, model output, Agent output or VPF output remain untrusted data. They cannot:

- change event classification or severity;
- suppress or close a detection;
- select a notification destination;
- declare an incident;
- approve containment or restoration; or
- manufacture Evidence, a Finding or a Human Decision.

## 7. Decision W16-D26 — HR9-22-1 incident command, notification and containment

### Option A — Governed lifecycle contracts with zero operational authority

Approve provider-neutral incident-control contracts representing the ordered source stages:

1. detection;
2. triage;
3. containment;
4. revocation;
5. isolation;
6. evidence-preservation request;
7. notification obligation;
8. recovery handoff after containment effectiveness is confirmed; and
9. independent restoration/reinstatement review.

Approve separate immutable metadata for:

- incident candidate and Human incident-declaration decision;
- ordinary incident command and emergency incident authority;
- notification obligations and delivery status, without a send path;
- containment request, Human authorization and execution receipt as distinct objects;
- temporary suspension scope, explicit expiry and revocation;
- preservation request references, without creating Evidence;
- containment-effectiveness confirmation;
- recovery handoff and restoration/reinstatement decision; and
- independent post-event review.

Approve empty versioned registries for incident-command assignments, notification obligations/destinations, containment rights, emergency eligibility and restoration/reinstatement authorities. All authority interfaces remain unassigned. Reference boundaries accept only synthetic metadata and can return only denial or `HUMAN_DECISION_REQUIRED`; they cannot declare an incident, send a notification, suspend a target, revoke access, isolate a component, preserve data, recover or reinstate.

Implications:

- The blocking source semantics can be represented without inventing command roles or executing response.
- Ordinary and emergency routes remain distinct.
- Emergency scope is temporary, exact and subject to independent post-event review.
- The requester, approver, executor and independent reviewer remain segregated.
- Recovery cannot recreate prior authorization, and the acting Emergency Authority cannot reinstate alone.

### Option B — Institution-supplied operational incident model

The Project Owner supplies or references:

- incident-declaration and incident-command authorities;
- ordinary and emergency eligibility by exact target/action class;
- containment rights and execution operators;
- notification obligations, recipients, channels, timing and legal/regulatory routes;
- severity-to-response mappings;
- containment effectiveness criteria;
- recovery, restoration and reinstatement authorities;
- post-event review and permanent-disposition authority; and
- products, runbooks, stores, destinations and residency controls.

Implication: this enables later operational design, but requires separate WBS-23 infrastructure/runbook authority, current institutional assignments and NCIE-016 verification. These prerequisites are not present.

### Option C — Defer the blocking incident decision

Defer `HR9-22-1`. Because the source marks it Blocking, no incident-command, containment, notification, recovery or reinstatement contract may be treated as institutionally settled. WP-008 cannot be implementation-complete under this option.

### Recommendation

Recommend `W16-D26: A`.

It captures the source lifecycle and segregation-of-duties rules while leaving all real command, notification, containment and restoration authority absent. It directly aligns with WP-004's existing unassigned emergency-access boundary and zero activation state.

## 8. Ordinary versus emergency incident authority

### Ordinary route

- Requires a current incident-declaration decision by an assigned accountable authority.
- Requires exact actor/action/target/purpose authorization for each consequential action.
- Requires separate request, approval and execution records.
- Cannot borrow emergency powers, pool permissions or infer authority from severity.
- Stale, expired, revoked, ambiguous or unassigned authority means deny.

### Emergency route

- Uses the existing WP-004 emergency-access class/eligibility boundary rather than inventing a parallel bypass.
- Requires an exact eligible emergency trigger and target class, current Human authority, bounded scope, explicit expiry and revocation handling.
- Creates only temporary suspension/containment authority, never permanent revocation or standing policy.
- Requires notification obligations and independent post-event review.
- Prohibits the acting Emergency Authority or executor from being the sole reinstating authority.
- If eligibility, auditability, expiry, independent review or current authorization is unavailable, the action denies.

No ordinary or emergency authority is assigned by this pack.

## 9. Notification-obligation boundary

A notification obligation contract may identify only:

- obligation, incident-candidate and policy references;
- trigger/stage reference;
- recipient-role class and destination-class reference;
- channel-class reference;
- content-minimization/classification policy references;
- accountable sender role reference;
- due-policy reference without an invented duration;
- current/fulfilled/failed/unknown status;
- provenance and audit references; and
- effective/expiry/revocation metadata.

No recipient, address, endpoint, paging service, delivery channel, timeframe or regulator is assigned. Creating an obligation does not send a notification. A delivery receipt is not proof that the recipient understood or acted. Unknown destination, residency, authority or classification means no delivery capability.

## 10. Restoration, recovery and reinstatement boundary

Restoration/reinstatement requires all of the following metadata to be current and exact:

- containment was separately authorized and recorded;
- containment effectiveness was confirmed by the assigned authority;
- evidence-preservation obligations were referred to WBS-20 and were not erased by remediation;
- an independent post-event review exists;
- the reviewer did not request, approve or execute the same containment action;
- recovery/restoration authority is assigned for the exact target and version;
- new four-layer authorization is evaluated; and
- expired, revoked or pre-incident grants are not revived.

`RECOVERY ≠ REAUTHORIZATION` and `RESTORATION ≠ REINSTATEMENT`.

An expired suspension does not automatically restore capability. The fallback is continued deny/no capability pending a current Human decision. WP-008 creates no restoration or reinstatement execution path.

## 11. Independent review and assurance boundary

The assurance interface is independent of:

- security-log owner and access approver;
- monitoring/detection rule owner;
- alert triage operator;
- incident commander;
- containment requester, approver and executor; and
- restoration/reinstatement decision-maker for the same action.

An assurance output is a recommendation or review record, not automatically institutional Evidence, a Finding, acceptance or remediation closure. Formal Evidence is WBS-20 scope; a Finding requires NCIE-008 Chapter 18 authority; independent security verification is NCIE-016 scope.

All assurance holders, review routes, sampling thresholds, cadence, evidence requirements and escalation destinations remain unassigned.

## 12. Authorities and operational values that remain UNASSIGNED / UNSPECIFIED

### Institutional authorities

- accountable security-log access/retention authority;
- Security Logging Owner;
- independent Assurance/Audit holder and reporting authority;
- Detection/Monitoring Owner;
- detection-rule approver and triage owner;
- escalation and severity-governance authorities;
- incident-declaration authority and Incident Response Owner;
- ordinary incident commander;
- Emergency Authority and emergency-eligibility authority;
- containment requester, approver and responsible executor;
- affected Domain Accountable Authority;
- notification owner/sender and legal/regulatory notification authority;
- evidence-preservation/custody authority;
- containment-effectiveness confirmer;
- recovery/restoration/reinstatement authority;
- independent post-event reviewer; and
- permanent revocation/disposition authority.

### Thresholds, periods and classifications

- retention, legal-hold, deletion and disposition periods;
- severity taxonomy, scores and thresholds;
- analytic confidence and correlation thresholds;
- triage, escalation, response, notification and acknowledgement times;
- emergency/suspension duration or default expiry;
- containment-effectiveness and recovery-readiness criteria;
- incident closure and reopening criteria;
- assurance cadence, sampling and materiality thresholds; and
- restoration/reinstatement waiting periods.

### Products, stores and destinations

- logging, SIEM, monitoring, analytics, paging and incident-management products;
- audit/log store, index, queue, cache, data lake or archive;
- dashboards, collectors, forwarders, agents, integrations and connectors;
- notification channels, addresses, recipients, regulators or external destinations;
- network routes, accounts, credentials, endpoints and provider regions;
- cross-border destination or exception; and
- operational runbooks, teams, rosters, on-call schedules and assignments.

Until explicitly assigned: `DENY / NO ACCESS / NO RETENTION OPERATION / NO ALERT DELIVERY / NO INCIDENT / NO CONTAINMENT / NO RECOVERY / NO REINSTATEMENT`.

## 13. Non-waivable WP-008 protections proposed for decision

1. Human-primary authority; signals, events, alerts, Agent/model/Tool/VPF output and products cannot create Findings, Decisions, incidents or execution authority.
2. Current four-layer authorization remains mandatory for every access and consequential action.
3. Logging, monitoring and incident metadata never authorize disclosure.
4. Telemetry, security log, audit and provenance remain distinct records.
5. Security-event metadata excludes secrets, raw prompts, raw protected values and governed payloads by construction.
6. Severity, confidence, correlation or rule match never creates authority.
7. No self-approval or permission pooling; requester, approver, executor and independent reviewer remain segregated.
8. Emergency containment is temporary, exact, explicitly expiring and independently reviewed.
9. Unknown, stale, expired, revoked, ambiguous or unassigned policy/authority means deny.
10. Historical state and provenance are preserved; remediation cannot erase or rewrite them.
11. Recovery does not reauthorize and reinstatement requires a separate current Human decision.
12. No cross-border transfer without a separately approved exact destination and current privacy/security/sovereignty authority.
13. Unavailable required audit/assurance capability means the affected consequential action denies.
14. WP-008 local work uses only synthetic metadata and creates no real incident, Evidence, Finding, notification or operational action.

No option or exception may waive these protections within WP-008.

## 14. Downstream boundaries

### WBS-20 — Evidence, Provenance & Audit

WP-008 may define references to prospective Evidence/audit/provenance objects, preservation requests and assurance handoffs. It cannot create institutional Evidence, custody chains, canonical audit records, Findings, defensibility claims, persistent stores or Evidence retention policy. Those remain WBS-20/NCIE-010 scope.

### WBS-23 — DevSecOps, observability and infrastructure

WP-008 may define provider-neutral interfaces for log ingestion, monitoring, alert delivery, notification and incident operations. It cannot select or activate products, collectors, SIEM, storage, dashboards, paging, network routes, accounts, endpoints, infrastructure, deployment or runbooks. Those remain WBS-23/NCIE-015 scope.

### NCIE-016 — independent security verification

Local WP-008 tests may verify contract shape and fail-closed behavior only. They do not execute NCIE-016's independent security testing, create security assurance, demonstrate zero risk, accredit a control or provide acceptance. NCIE-016 Chapter 19 security-test independence and acceptance remain separately Human-controlled.

## 15. Proposed WP-008 implementation boundary

If the Project Owner selects all recommended A options and later issues a separate implementation authorization, WP-008 may include only:

1. immutable provider-neutral contracts for minimized security events, five detection categories, triage/escalation results, symbolic severity, incident lifecycle stages, notification obligations, containment requests and restoration/reinstatement reviews;
2. empty versioned registries for log access, retention/legal hold, assurance assignments, detection rules, escalation routes, severity governance, incident command, notifications/destinations, containment rights, emergency eligibility and restoration/reinstatement authority;
3. unassigned Human/institutional authority interfaces;
4. fail-closed access, retention-policy, detection, triage, incident-declaration, notification, containment and restoration metadata evaluation;
5. an in-memory, non-persistent test collector accepting synthetic metadata only and incapable of becoming an audit/Evidence store;
6. a no-monitor reference boundary with no polling, streaming, product or external source;
7. a no-alert/no-page notification boundary with no destination or send path;
8. a no-incident-command boundary that returns only deny or `HUMAN_DECISION_REQUIRED`;
9. a no-containment/no-recovery boundary with no execution method;
10. synthetic prompt-injection and false-authority tests preserving WP-006/WP-007 untrusted-content semantics;
11. minimized non-authoritative signals;
12. deterministic standard-library unit, contract and negative-path tests;
13. cumulative WP-001 through WP-007 regression; and
14. traceability and local implementation evidence.

## 16. Explicit exclusions

The proposed package excludes:

- any real log, security event, alert, incident, Evidence object, Finding or Human Decision;
- governed production data or production-like protected values;
- a persistent log/audit/Evidence store;
- monitoring, correlation against live sources, alerting, paging or notification delivery;
- incident declaration or operational incident command;
- containment, suspension, revocation, isolation, evidence preservation, recovery, restoration or reinstatement execution;
- populated rules, severity mappings, authority assignments, destinations or notification obligations;
- SIEM, monitoring, logging, paging, incident-management or security product selection;
- provider, account, credential, endpoint, network or external-system capability;
- cross-border transfer;
- dependencies, infrastructure or deployment;
- independent verification, accreditation, acceptance or go-live; and
- WP-009 or later WBS-16 scope.

## 17. Stop conditions

Stop the affected scope and return for Human decision if work requires:

1. a real or production-like log, identity, protected value, governed payload, alert or incident;
2. a concrete institutional authority holder, incident role, team, roster or operational assignment;
3. a severity taxonomy, numeric threshold, response target, retention period, notification deadline or default expiry;
4. a populated access, retention, detection, escalation, command, notification, containment, emergency or restoration registry;
5. a persistent store, Evidence object, Finding, Human Decision or custody chain;
6. a product/provider, connector, SDK, endpoint, credential, external destination or network access;
7. actual monitoring, alert delivery, paging, notification or incident declaration;
8. containment, suspension, revocation, isolation, recovery, restoration or reinstatement;
9. cross-border transfer or a residency exception;
10. weakening current authorization, segregation of duties, minimization, provenance or a WP-001 through WP-007 boundary;
11. a new dependency, infrastructure or deployment;
12. NCIE-016 assurance/acceptance claims; or
13. WP-009 or later implementation.

The fallback remains `DENY / NO CAPABILITY`.

## 18. Proposed WP-008 completion criteria

WP-008 can be declared locally implementation-complete only when all applicable criteria are evidenced:

1. The Project Owner has explicitly selected W16-D24, W16-D25 and W16-D26 options.
2. A separate Project Owner decision has released the exact WP-008 implementation scope.
3. Signal, Security Event, detection/alert, incident, Evidence, Finding, Human Decision and execution authority remain distinct types.
4. Telemetry, security log, audit and provenance remain distinct.
5. The minimized event schema contains no secret, raw prompt, protected value or governed payload.
6. Every access requires current exact four-layer authorization and an applicable access policy.
7. No log access or retention record creates disclosure authority.
8. Retention, legal-hold and disposition periods remain unassigned; no default is invented.
9. The five NCIE-009 detection categories are represented without an invented operational category.
10. Tool/data behavior remains source metadata requiring Human class assignment; no sixth detection category is invented.
11. Detection/alert results cannot create Evidence, Findings, Decisions, incidents or containment authority.
12. Severity is symbolic/unassigned and cannot trigger an operational action.
13. Unknown/stale/expired/revoked rules, decisions and authorities fail closed.
14. Ordinary and emergency incident authority remain separate.
15. Request, approval, execution and independent review remain segregated.
16. The source incident lifecycle order and evidence-preservation boundary are represented.
17. Notification obligations create no delivery capability and contain no actual destination.
18. Emergency containment remains temporary, explicitly expiring/revocable and subject to independent review.
19. The acting Emergency Authority/executor cannot be the sole reinstating authority.
20. Recovery does not recreate prior authorization; restoration and reinstatement require new current decisions.
21. No real incident, Evidence, Finding, notification, containment or recovery action exists.
22. All controlled registries are empty and all authority interfaces unassigned.
23. Agent/model/Tool/VPF and retrieved/external content remain untrusted and non-authoritative.
24. No persistent store, monitoring product, SIEM, paging system, provider, network or external destination exists.
25. African data residency remains deny-by-default for any unknown or cross-border destination.
26. Comprehensive synthetic negative tests cover false authority, payload leakage, stale authority, self-approval, severity escalation, notification and containment bypass.
27. Cumulative WP-001 through WP-007 regression passes.
28. Strict typing, lint, formatting, compilation, reproducibility and template-verification gates pass without a new dependency.
29. Traceability maps HR9-20-1 through HR9-22-1 to decisions, contracts, tests, evidence and deferred Human authorities.
30. Evidence states that local tests are not monitoring activation, an incident, Evidence, a Finding, independent verification, accreditation, acceptance or go-live.

## 19. Recorded Project Owner decision

- `W16-D24: A` — provider-neutral security-log access, retention and independent-assurance contracts with empty policies, unassigned authorities and zero persistent logging.
- `W16-D25: A` — five source-defined detection categories, symbolic severity, empty monitoring/escalation registries and zero monitoring or alerting activation.
- `W16-D26: A` — governed incident lifecycle, notification, containment, recovery and reinstatement contracts with empty operational registries, unassigned authorities and zero incident-response execution capability.
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`.
- Decision date: `2026-09-24`.
- Conditions: `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`, the mandatory semantic separations in Section 2, all fourteen non-waivable protections in Section 13, and every zero-capability condition recorded in the evidence.
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-24-029`.
- Evidence type: `Self-Authorized Project Owner Decision`.

This decision defines architecture only. A separate explicit Project Owner authorization remains required before any WP-008 implementation.

## 20. Source traceability and VPF boundary

Primary controlled sources:

- NCIE-009 Chapters 20–22 and `HR9-20-1` through `HR9-22-1`;
- NCIE-008 Chapters 4, 5, 6, 18, 22–24;
- NCIE-003 Chapters 25 and 27, including Audit Event semantics and `TELEMETRY ≠ AUDIT`;
- NCIE-004 observability and resilience boundaries;
- NCIE-007 Chapter 31 telemetry/privacy/audit separation;
- NCIE-016 Chapter 19 security verification and independence boundary;
- NCIE-017 Chapters 16, 20 and 23 workstream boundaries; and
- W16-D1 through W16-D23 and the controlled WP-001 through WP-007 handovers.

VPF is applied behaviorally to Human-primary authority, identity dignity, least privilege, explainability, provenance, minimization, sovereignty and African data-residency/cross-border boundaries. The VPF configuration is not modified or redistributed by this pack. No VPF runtime, validator, checksum, signature, certificate, ledger, PADCA/Omnis exchange, quarantine action, monitoring service or residency-enforcement service is claimed to have executed.
