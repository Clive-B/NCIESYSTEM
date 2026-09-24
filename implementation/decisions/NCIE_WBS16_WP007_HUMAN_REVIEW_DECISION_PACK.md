# NCIE WBS-16-WP-007 Human Review Decision Pack

Status: `DECIDED — W16-D22-A / W16-D23-A; IMPLEMENTATION RELEASED UNDER NCIE-WBS16-OWNER-DECISION-2026-09-24-027`

Prepared: `2026-09-24`

Proposed work package: `WBS-16-WP-007 DLP, Disclosure and Protected-Identity Controls`

Decision identifiers proposed for Project Owner review:

- `W16-D22` — `HR9-18-1`, DLP policy classes, disclosure authorities, disclosure decisions and exception boundaries; and
- `W16-D23` — `HR9-19-1`, protected-identity access classes, privacy controls and privacy-escalation authority.

## 1. Purpose and authority boundary

This pack presents the source-grounded choices and records the Project Owner's W16-D22-A and W16-D23-A selections in Section 17. Those selections grant no implementation or operational authority.

Preparation of this pack does not:

- implement WP-007;
- classify, create, retrieve, reveal or process a real protected identity;
- authorize or execute a disclosure;
- approve an exception, output channel, destination or cross-border transfer;
- select a DLP, privacy, identity, masking, tokenization or disclosure product/provider;
- assign an institutional authority, actor, role, identity class, threshold or destination;
- add a dependency, infrastructure or deployment; or
- authorize WP-008 or any later WBS-16 scope.

The governing fallback remains:

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

## 2. Exact source baseline

### 2.1 HR9-18-1 and the five NCIE-009 data paths

NCIE-009 Chapter 18 makes `HR9-18-1` blocking and requires Human confirmation of DLP policy classes, disclosure authorities and exceptions. Its Table 25 defines five exact enforcement paths:

| Source-defined data path | Required check point | Source-defined DLP behavior |
|---|---|---|
| Tool invocation input/output | Before Tool-call assembly | Field-level masking or blocking per classification |
| Export: file, report or API response | Before export generation | Classification-aware export policy |
| Model input: prompt/Context assembly | Before Context/prompt assembly | Minimization and field masking |
| Voice/spoken output | Before speech synthesis | Protected-identity and voice-disclosure controls |
| Agent-to-Agent handoff | Before Context handoff | The same classification checks as the original path |

NCIE-009 further requires classification to travel with data. Generated and inferred values may be sensitive even when they were not directly sourced. A VPF PASS is a content-quality/policy disposition and is explicitly not security authorization or disclosure authority.

### 2.2 HR9-19-1 and protected identity

NCIE-009 Chapter 19 makes `HR9-19-1` blocking and requires Human confirmation of protected-identity access classes and privacy-escalation authority. It requires:

- minimum-necessary access for the current authorized purpose;
- no exposure merely because a value is technically retrievable;
- vault/tokenization-interface, masking and purpose-limitation boundaries;
- inferred protected-identity-equivalent or otherwise sensitive output to receive the same classification and control standard as directly sourced data; and
- privacy access to be audited at the same standard as direct access.

NCIE-003 Chapter 14 separates a Protected Identity Reference from the Registration entity so most queries do not touch the protected value. Ghana Card and Passport are source-defined distinct identity types. Aggregate reporting exposes counts, not underlying identity values. Every unmasked view is a separately accountable Protected Reveal with heightened audit.

This pack uses those source concepts only as symbolic metadata. It creates or processes no identity value.

### 2.3 Classification floor and disclosure independence

NCIE-003 Chapter 2 defines four canonical classification tiers:

1. `PUBLIC`;
2. `INTERNAL`;
3. `PROTECTED`; and
4. `SENSITIVE`.

An entity declares a default tier. An attribute may raise but never lower that floor. Derived objects inherit at least the governing source classification. Unknown raw content defaults to the most protective applicable tier until validated.

NCIE-003 separately leaves legal/policy confirmation of the taxonomy open. Using the four structural tiers in a future WP-007 contract would not declare that their mapping to Ghanaian data-protection law or NCA policy has been legally approved.

The following remain separate decisions:

| Concept | Meaning | What it does not do |
|---|---|---|
| Classification | Describes the protection floor attached to data or a field | Does not authorize an actor, recipient, purpose, channel or destination |
| Current authorization | Evaluates the current actor against exact object, field, action and purpose | Does not waive DLP, privacy, consent, channel, residency or disclosure requirements |
| Disclosure authority | A current accountable Human/institutional decision for the exact recipient, content, purpose, channel and destination when required | Does not lower classification, repeal policy or create a missing technical capability |
| DLP evaluation | Applies path-specific minimization, masking, redaction, suppression, blocking and review rules | Does not itself become a permission or Human approval |
| Consent/legal basis | Governs lawful and dignified use where applicable | Does not replace current authorization or security enforcement |

`CLASSIFIED ≠ AUTHORIZED ≠ DISCLOSURE-APPROVED ≠ RELEASED`.

### 2.4 Voice, Memory, Agent and Tool boundaries

NCIE-005 Chapter 29 establishes that display authorization does not imply spoken-disclosure authorization. Full Ghana Card or Passport identifiers are not spoken merely because a viewer may see a masked/protected-revealed value. Credentials and secrets are never disclosed through ARGUS. When the physical listening context cannot be established, the more restrictive voice behavior applies.

NCIE-006 Chapters 25–26 establish that remembered authorization is never current authorization; protected identity remains masked/tokenized in Memory; Room membership does not pool permissions; voice/speaker recognition is not authenticated identity; and remembered display authority never becomes later spoken-disclosure authority.

NCIE-007 Chapters 19–21 establish that Tool possession does not create action authority, read-only disclosure may still be high risk, and a proposal or validated AI result is not authorization, approval, execution or verification.

WP-006 already establishes that Agent/model/Tool output, Evidence, Documents, Memory, web/API content and other-Agent output are untrusted data. WP-007 must preserve that rule.

### 2.5 Governance and exception boundaries

NCIE-008 Chapters 20–21 separate institutional decision ownership from technical enforcement. Privacy-disclosure and residency/sovereignty exception authorities decide; NCIE-009 security controls enforce. Every exception requires exact scope, duration, compensating controls, a non-requester accountable approver, expiry, fresh assessment for renewal, prospective revocation and audit. An exception:

- does not repeal the underlying policy;
- cannot fabricate a technical capability;
- cannot be self-approved; and
- cannot relax a security control that NCIE-009 has not approved as relaxable.

The exact prohibited-exception classes and institutional holders remain unresolved under `HR8-20-1` and `HR8-21-1`; this pack must not invent them.

## 3. Mandatory invariants for either decision

Any selectable option must preserve all of the following:

1. Human-primary authority and segregation of requester, approver and independent reviewer.
2. Least privilege, minimum necessary, purpose limitation and field-level control.
3. Current four-layer actor/object-field/action/purpose authorization from WP-001.
4. WP-004 non-expanding delegation and unassigned privilege/emergency boundaries.
5. WP-005 protected-material and egress controls, including deny-by-default cross-border handling.
6. WP-006 zero Agent/model/Tool/Context capability and untrusted-content boundary.
7. Classification propagation and no downgrading through derivation, formatting, aggregation, translation, summarization, masking failure or channel change.
8. Separate disclosure evaluation for each recipient, channel and destination; no permission pooling.
9. Provenance retention without logging or returning protected values.
10. Consent, identity dignity and privacy escalation where required.
11. African data residency and deny-by-default cross-border transfer.
12. Missing, expired, revoked, conflicting, stale, unknown or indeterminate input returns deny/no capability.

## 4. Decision W16-D22 — HR9-18-1 DLP/disclosure policy

### Option A — Approve the five source-defined DLP path classes with empty registries and zero disclosure capability (recommended)

Approve these five policy classes exactly as the NCIE-009 Table 25 path boundaries:

1. `TOOL_INVOCATION_INPUT_OUTPUT`;
2. `EXPORT_FILE_REPORT_API_RESPONSE`;
3. `MODEL_INPUT_CONTEXT_ASSEMBLY`;
4. `VOICE_SPOKEN_OUTPUT`; and
5. `AGENT_TO_AGENT_HANDOFF`.

Approve the following provider-neutral DLP dispositions:

- `DENY`;
- `INDETERMINATE`;
- `MASK_REQUIRED`;
- `REDACTION_REQUIRED`;
- `SUPPRESSION_REQUIRED`;
- `MINIMIZATION_REQUIRED`;
- `HUMAN_REVIEW_REQUIRED`;
- `EXCEPTION_REQUIRED`; and
- `POLICY_CHECK_SATISFIED`.

These are control dispositions, not disclosure authority. `POLICY_CHECK_SATISFIED` means only that the applicable DLP rule did not independently block the candidate. Actual release would still require current authorization, exact recipient/channel/destination eligibility and every required Human/institutional decision.

Approve a separate disclosure-decision effect of `PERMIT`, `DENY` or `INDETERMINATE`, with `PERMIT` impossible in the controlled WP-007 reference state because all disclosure authorities, policy entries, channels and destinations remain empty or unassigned.

Approve immutable metadata contracts for:

- request, correlation, policy and provenance references;
- current actor/principal and non-expanding delegation reference;
- exact object and fields;
- field-level and aggregate classification floor;
- action, purpose, task and Context;
- recipient or recipient class;
- the exact output channel and destination;
- residency, cross-border and retention/reuse metadata;
- legal basis and consent references where applicable;
- the applicable DLP path class and versioned rule reference;
- a minimum-necessary field set;
- masking, redaction and suppression plan references;
- current four-layer authorization decision;
- current disclosure-authority decision when required;
- exception reference when required;
- effective time, explicit expiry and revocation state;
- audit/provenance and downstream handling obligations; and
- the final DLP disposition and disclosure effect.

Approve empty versioned registries for DLP rules, output channels/destinations, disclosure-authority assignments and disclosure/cross-border exceptions. Therefore all release attempts deny.

Implication: a later authorized implementation can validate synthetic disclosure candidates and prove fail-closed handling without outputting data, activating a channel, choosing a destination or granting a disclosure.

### Option B — Approve concrete DLP rules, channels, destinations and authority assignments

Provide, for every one of the five source paths:

- exact rule inventory and versions;
- field/classification mappings;
- recipient classes and current authorization matrix;
- channel and destination inventory;
- minimization, masking, redaction, suppression and block rules;
- legal/consent basis;
- African residency and cross-border dispositions;
- accountable disclosure, exception and review authorities;
- effective/expiry/revocation rules;
- operational thresholds and bulk/pattern limits; and
- product/provider and enforcement-point decisions if any are intended.

Implication: this creates operational policy and requires privacy, legal, security, sovereignty, data-owner and independent-review decisions plus a revised implementation package. Selecting Option B does not itself authorize disclosure or deployment.

### Option C — Defer DLP/disclosure policy

Do not implement the WP-007 DLP/disclosure contract family. All disclosure remains outside implemented capability and denied.

Implication: WP-007 cannot become work-complete, and no later scope may treat DLP/disclosure prerequisites as satisfied.

### Recommendation

Recommend `W16-D22-A`. It represents every source-defined data path, keeps classification separate from authorization and disclosure authority, preserves the conservative WP-002 risk posture, and allows deterministic deny/no-output tests without inventing an authority, rule, recipient, channel, destination, exception or product.

## 5. Output-channel and destination controls under W16-D22-A

The architecture would define these source-grounded output-channel classes without activating any instance:

| Channel class | Required boundary |
|---|---|
| Protected visual/display | Exact viewer, field, purpose and protected-reveal rules; display does not imply voice/export authority |
| File export | Classification-aware export policy before generation |
| Report export | Classification-aware export policy before generation |
| API response | Classification-aware response filtering before serialization |
| Tool input/output | Field masking/blocking before Tool-call assembly and before returning Tool output |
| Model prompt/Context input | Minimum authorized subset, minimization and masking before assembly |
| Voice/spoken output | Separate spoken-disclosure policy before synthesis; unknown physical context selects the restrictive result |
| Agent-to-Agent handoff | Original classification floor and a new current recipient/handoff authorization check |

Every channel/destination contract must bind channel class, destination reference, residency/jurisdiction, approved purpose, classification ceiling, recipient scope, policy version and current lifecycle state. An empty registry, missing destination, unknown residency or absent current authority returns deny. Channel substitution and fallback cannot bypass a denial: a voice denial does not silently become API/export, and a provider or channel outage does not permit an unapproved alternative.

## 6. Minimum-necessary, masking, redaction and suppression boundary

The recommended architecture would enforce the following order on synthetic metadata only:

1. Determine current actor, exact recipients, purpose, object/fields and source provenance.
2. Resolve field classifications and calculate the highest applicable aggregate floor.
3. Reject unknown classification, recipient, purpose, channel, destination, residency or policy state.
4. Reduce the candidate to the minimum fields necessary for the authorized purpose.
5. Apply source-required masking/tokenization to protected fields.
6. Redact fields not permitted for the exact recipient/channel/destination.
7. Suppress fragments whose inclusion would reveal protected information through context, linkage or inference.
8. Reclassify the resulting candidate, including inference sensitivity.
9. Re-run current authorization and path-specific DLP evaluation on the transformed candidate.
10. Require current disclosure/exception authority where policy says it is required.
11. Produce deny/no-output unless every independent condition is current and exact.

Masking, redaction or aggregation is not automatically declassification. A masked value may remain `PROTECTED` or `SENSITIVE`; linkage, small-group counts, surrounding text and inference may still disclose identity. No numeric k-anonymity, bulk-export, risk-score or suppression threshold is supplied and none may be invented.

## 7. Mixed-classification and mixed-authority output handling

Approve these fail-closed rules under Option A:

1. The output classification floor is the most protective applicable field/source/derived classification; a lower-class envelope cannot downgrade a protected component.
2. Field-level segmentation is permitted only when provenance is retained and the resulting fragments can be independently evaluated.
3. If protected and non-protected content cannot be reliably separated, suppress the whole candidate.
4. In a mixed-authority audience, compute disclosure independently per recipient. Never union or pool permissions.
5. A shared output contains only the intersection of content independently releasable to every current recipient for the exact purpose and channel.
6. If recipient membership, authorization or classification changes, the candidate is invalidated and re-evaluated.
7. A mixed current/stale decision is stale; a mixed permit/deny decision is deny; any indeterminate component makes the affected disclosure indeterminate/denied.
8. Generated summaries, translations, visualizations, counts and inferred statements inherit relevant source classifications and are re-evaluated before use.
9. A model/Agent/Tool statement that content is safe, public, consented or authorized is untrusted data, never the classification or disclosure decision.

## 8. Decision W16-D23 — HR9-19-1 protected identity and privacy escalation

### Option A — Approve source-grounded protected-identity handling classes with zero real identities, zero reveal and unassigned privacy authorities (recommended)

Approve these security/privacy handling classes:

1. `OPAQUE_PROTECTED_REFERENCE_ONLY` — an opaque canonical reference; no protected value;
2. `AGGREGATE_OR_COUNT_ONLY` — a derived count or aggregate that excludes the underlying identity value and remains subject to inference review;
3. `MASKED_OR_TOKENIZED` — a protected field represented through an approved masking/tokenization contract;
4. `PROTECTED_REVEAL` — an individually accountable, field-specific unmasked-view request requiring current authorization, disclosure/privacy authority and heightened audit; and
5. `INFERRED_PROTECTED_IDENTITY_EQUIVALENT` — output inferred from other fields that must be controlled as if directly sourced protected data.

These are handling classes, not actor roles or access grants. No class permits processing a real identity in WP-007. The source-defined Ghana Card and Passport types remain semantic references only; no number, document, person, account, biometric, contact detail or other identity attribute is created or processed.

Approve an unassigned privacy-escalation interface. Escalation is required when a synthetic request represents any of the following:

- a Protected Reveal or an unmasked value;
- inferred protected-identity-equivalent content;
- mixed classification or mixed recipient authority;
- voice/spoken disclosure of protected identity;
- export, API, external destination or Agent/Tool/model propagation;
- missing/unclear legal basis, consent, purpose or accountable Human owner;
- unknown or cross-border residency;
- bulk, pattern, linkage or re-identification risk whose threshold is unspecified;
- conflicting classification/privacy decisions;
- expired, revoked, stale or indeterminate authority; or
- inability to produce the required provenance/audit reference.

Escalation creates no authority. It returns `HUMAN_DECISION_REQUIRED` and denies disclosure until a separately assigned, current authority records a valid decision. Independent review remains a distinct unassigned boundary and cannot be performed by the requester, the Agent/model/Tool, or the same authority whose decision is under review.

Implication: a later authorized implementation can represent protected-identity security states and negative paths using opaque synthetic references, but it cannot create, retrieve, reveal, infer or disclose a real identity.

### Option B — Approve a concrete protected-identity access and privacy-escalation matrix

Provide:

- the authoritative inventory of protected identity types and fields;
- exact actor/role/purpose access classes;
- legal basis and consent requirements;
- masked, tokenized, aggregate and reveal rules;
- display, voice, export, API, Tool, model and Agent channel rules;
- inference/re-identification rules and thresholds;
- accountable privacy, disclosure, escalation and independent-review authorities;
- residency and cross-border rules;
- expiry, revocation, retention, deletion and audit obligations; and
- any product/provider or vault/tokenization implementation decisions.

Implication: this creates operational privacy/security policy requiring legal, data-protection, identity-owner, sovereignty and independent security review. Selecting Option B does not itself authorize real data processing, reveal, product selection or deployment.

### Option C — Defer protected-identity/privacy policy

Do not implement protected-identity handling or privacy-escalation contracts. All protected-identity access and disclosure remains denied and WP-007 remains incomplete.

Implication: later work cannot treat protected-identity privacy controls as implemented.

### Recommendation

Recommend `W16-D23-A`. It directly models NCIE-003/005/006/009 minimum-necessary, masking, Protected Reveal and inference rules while keeping all real identities, actors, authorities and operations absent. It aligns with Human-primary authority, dignity, consent, fail-closed access and the existing empty-registry architecture.

## 9. Disclosure, privacy and cross-border exception contract

Under the selected Option A architecture, a separately authorized WP-007 implementation may define—but not populate—an exact exception contract requiring:

- exception reference, type and policy version;
- requesting actor, accountable Human owner and non-requester approver;
- exact objects, fields, classification and protected-identity handling class;
- exact recipients, purpose, task and Context;
- legal basis and consent references where applicable;
- exact output channel, destination, jurisdiction and residency disposition;
- current object/field/action/purpose authorization;
- current DLP disposition and disclosure decision;
- minimum-necessary justification and transform plan;
- security/privacy assessment and compensating controls;
- source data-owner, disclosure, privacy and residency/cross-border decisions;
- independent privacy/security review;
- effective time, explicit expiry and revocation state;
- provenance, audit and downstream dependency references;
- retention, deletion, recall and reconciliation obligations; and
- a statement that the exception creates no capability and does not repeal policy.

The exception registry remains empty. Renewal is never automatic. No recipient, destination, context pair, legal basis, consent, jurisdiction, duration, threshold or authority holder is approved.

### Proposed non-waivable protections for Project Owner decision

Under recommended Options A, approve the following as non-waivable within WP-007 contracts:

1. Human-primary authority; an Agent/model/Tool/VPF result cannot approve disclosure or an exception.
2. Current four-layer authorization for the exact actor/object-field/action/purpose.
3. No classification downgrade by derivation, channel change, masking claim or exception.
4. No disclosure with unknown actor, recipient, purpose, classification, channel, destination, residency or authority.
5. No self-approval, missing expiry, automatic renewal or exception-created technical capability.
6. No credentials, secrets or protected material in Agent/model/voice/export output.
7. No cross-border transfer without a separately approved exact destination and current privacy/security/sovereignty authority.
8. No direct Memory/store/index/cache access or permission pooling.
9. No unlogged Protected Reveal or privacy-sensitive access; if the required audit boundary is unavailable, deny.
10. No real protected identity or governed production data in the WP-007 local reference implementation or tests.

These approved bounded WP-007 non-waivable protections do not assign the broader institutional prohibited-exception classes left open by `HR8-21-1`. Anything outside this bounded list remains unresolved and must return for Human decision; the fallback is deny/no capability.

## 10. Agent/model/Tool and untrusted-content boundary

Every disclosure candidate from an Agent, model or Tool remains a proposal. Before any future release, the independent DLP/disclosure boundary must re-evaluate current actor, recipients, object/fields, purpose, classification, protected-identity status, channel, destination, residency and current authority.

The following origins are always untrusted data:

- Agent or other-Agent output;
- model output;
- Tool output or execution receipt;
- Evidence and Documents;
- Memory, Knowledge Candidates and retrieved Context;
- web/API/external content;
- voice transcript or uploaded content; and
- VPF validation output.

Instructions or labels inside those values cannot alter classification, declare consent, approve a recipient, widen purpose/target, choose a channel/destination, grant an exception, relax residency or suppress required review. A VPF PASS remains non-authoritative for security disclosure.

## 11. Institutional authorities remaining UNASSIGNED

The architecture may name interfaces for these authority classes, but no holder, person, team, role or organization may be assigned:

- Classification Authority / NCIE-003 Classification Owner;
- DLP Policy Authority;
- DLP/Disclosure Security Owner;
- Disclosure Authority;
- Protected Visual/Display Disclosure Authority;
- Voice/Spoken-Disclosure Authority;
- Export/API Disclosure Authority;
- Output Channel/Destination Approval Authority;
- Data/Domain Owner;
- Protected-Identity Access Authority;
- Protected Reveal Authority;
- Privacy Security Owner;
- Privacy/Consent/Legal-Basis Authority;
- Privacy Escalation Authority;
- DLP/Disclosure Exception Authority;
- Residency/Sovereignty and African Cross-Border Authority;
- Exception Renewal/Revocation Authority;
- Independent Privacy/Security Reviewer; and
- Assurance/Audit Authority.

Any missing assignment returns deny/no capability.

## 12. Other values that remain UNASSIGNED / UNSPECIFIED

### Thresholds and policy values

- bulk-export, record-count, field-count, frequency, rate or volume thresholds;
- re-identification, inference, linkage, aggregation or small-group thresholds;
- masking/tokenization/redaction methods and sufficiency criteria;
- privacy, disclosure, sensitivity or risk scores;
- approval/review quorum, duration, expiry default or renewal interval;
- retention, recall, deletion or reconciliation periods;
- consent form, legal basis, privacy notice or jurisdiction-specific determination; and
- independent-review triggers beyond the fail-closed conditions proposed here.

### Operational inventories

- real people, protected identities, identity documents, biometrics or identity attributes;
- any additional operational protected-identity type/class, attribute inventory or identity-to-access mapping beyond the source-defined symbolic Ghana Card/Passport references;
- operational actor/role/recipient classes and access grants;
- DLP rules or exception entries;
- output channels, accounts, endpoints, queues, fileshares, email/SMS/voice systems or API consumers;
- external destinations, countries, regions, providers, processors or sub-processors;
- cross-border routes or exemptions;
- DLP, CASB, privacy, tokenization, vault, masking or identity products/providers;
- data stores, logs, audit systems, infrastructure and deployments; and
- governed production data, prompts, Evidence, Documents, Memory or external content.

## 13. Exact WP-007 implementation scope after both decisions and a separate release

The Project Owner has recorded W16-D22-A and W16-D23-A. Only after a later separate implementation decision explicitly names and releases `WBS-16-WP-007 DLP, Disclosure and Protected-Identity Controls` may the work package include:

1. Provider-neutral enums and immutable metadata contracts for the approved DLP paths, DLP dispositions, disclosure decisions, output channels and protected-identity handling classes.
2. Empty versioned registries for DLP rules, channels/destinations, disclosure authorities, protected-identity access rules, privacy authorities and disclosure/cross-border exceptions.
3. Fail-closed classification-floor, minimum-necessary, mixed-authority, mixed-classification and disclosure evaluators.
4. Unassigned protocols/interfaces for every Human/institutional authority named in this pack.
5. A no-output DLP reference boundary that evaluates synthetic metadata but cannot emit, serialize, speak, export or transmit content.
6. A no-reveal protected-identity reference boundary that accepts opaque synthetic references only and cannot retrieve or unmask a value.
7. A privacy-escalation reference boundary that can return `HUMAN_DECISION_REQUIRED` but cannot create a decision or assignment.
8. Exact exception metadata and expiry/revocation validation with an empty registry and no exception capability.
9. Synthetic prompt-injection and false-authorization tests reusing WP-006 untrusted-content semantics.
10. Minimized, non-authoritative provenance/security signals containing no prompt, identity, protected value, document, Memory or private chain-of-thought.
11. Standard-library local unit, contract and negative-path tests using synthetic/non-governed references only.
12. Cumulative WP-001 through WP-006 regression, traceability and local implementation evidence.

## 14. Explicit exclusions

WP-007 preparation and any later Option-A contract implementation exclude:

- real identity creation, ingestion, retrieval, matching, inference, reveal or disclosure;
- governed production data or production-like identity values;
- an actual disclosure, output payload, export, spoken value, API response or Agent handoff;
- a populated DLP, channel, destination, identity-access, authority or exception registry;
- any current disclosure permission, consent/legal determination or cross-border approval;
- product/provider selection, SDK, connector, endpoint, credential or account;
- network/internet access, external system, storage, queue, audit product, infrastructure or deployment;
- operational monitoring, privacy accreditation, independent verification, acceptance or go-live;
- changing WP-001 through WP-006 decisions or creating a bypass around them; and
- WP-008 or later WBS-16 implementation.

## 15. Stop conditions

Stop the affected scope and return for Human decision if any requested implementation requires:

1. a concrete DLP/privacy product, provider, adapter, connector, endpoint or account;
2. a real person, identity, protected value, biometric, document or governed dataset;
3. a concrete actor, recipient, role, permission, authority holder or operational assignment;
4. a numeric threshold, scoring model, retention period or default expiry;
5. a real output channel, destination, jurisdiction, external transfer or cross-border route;
6. a disclosure, Protected Reveal, consent/legal determination, exception or policy waiver;
7. a non-source-grounded classification, identity or DLP taxonomy;
8. weakening a non-waivable protection, current authorization, no-pooling rule or African residency boundary;
9. allowing Agent/model/Tool/VPF or untrusted content to create authority;
10. logging or returning a prompt, protected value, identity, secret, credential or private chain-of-thought;
11. a new dependency, persistent store, infrastructure, external system or deployment;
12. a change to an approved WP-001 through WP-006 boundary;
13. implementation before both decisions and the separate WP-007 release; or
14. WP-008 or later scope.

The fallback state is `DENY / NO CAPABILITY`.

## 16. Proposed completion criteria

WP-007 can be declared locally implementation-complete only when all applicable criteria are evidenced:

1. The Project Owner has recorded explicit W16-D22 and W16-D23 selections.
2. A separate Project Owner decision has released the exact WP-007 implementation scope.
3. Classification, current authorization, disclosure authority, DLP evaluation and consent/legal basis remain distinct contracts.
4. The exact five NCIE-009 Table 25 paths are represented without an invented operational path.
5. Every controlled DLP, channel/destination, authority, protected-identity-access and exception registry is empty.
6. All institutional authority interfaces are unassigned and fail closed.
7. The four NCIE-003 classification tiers and attribute-can-raise-never-lower rule are preserved.
8. Minimum-necessary, masking, redaction, suppression and reclassification order is deterministic and fail closed.
9. Masking or aggregation never automatically declassifies data.
10. Mixed-classification output uses the most protective applicable floor; inseparable content suppresses as a whole.
11. Mixed-authority output is evaluated per recipient and never pools permissions.
12. Every channel and destination requires exact current eligibility; fallback cannot bypass denial.
13. Voice disclosure remains separate from display authority and unknown listening context chooses the restrictive result.
14. Agent/model/Tool/VPF output and all retrieved/external content remain untrusted data with no disclosure authority.
15. Protected-identity handling classes are metadata-only and no real identity is created or processed.
16. Protected Reveal, inference-equivalent and privacy-escalation paths deny without current Human/institutional authority.
17. The exception registry is empty; expiry, renewal, revocation, non-self-approval and no-policy-repeal semantics are enforced.
18. The approved non-waivable protections cannot be overridden by an exception contract.
19. Unknown or cross-border destination denies; no African residency or sovereignty exception is created.
20. No output, serialization, speech synthesis, export, provider call, Tool call, Agent handoff, network access or external transfer path exists.
21. Signals/errors contain no prompt, identity, protected value, secret, credential, document, Memory or private chain-of-thought.
22. Positive contract-construction and comprehensive negative-path tests use only synthetic/non-governed references.
23. WP-001 through WP-006 and WBS-15 regression tests continue to pass in the approved locked environment.
24. Strict typing, lint, formatting, compilation, reproducibility and template-verification gates pass without a new dependency.
25. Traceability maps HR9-18-1 and HR9-19-1 to decisions, contracts, tests, evidence and deferred Human authorities.
26. Evidence states that local tests are not disclosure authorization, privacy approval, a protected-identity reveal, a cross-border exception, independent verification, accreditation, acceptance or go-live.

## 17. Recorded Project Owner decision

- `W16-D22: A` — five source-defined DLP paths, provider-neutral DLP/disclosure contracts, empty controlled registries, unassigned disclosure authorities and zero disclosure capability.
- `W16-D23: A` — metadata-only protected-identity handling classes, privacy-escalation contracts, zero real identity processing/reveal and unassigned privacy authorities.
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`.
- Decision date: `2026-09-24`.
- Conditions: `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`, all ten bounded non-waivable protections in Section 9, and every zero-capability condition in the evidence record.
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-24-026`.
- Evidence type: `Self-Authorized Project Owner Decision`.

The architecture decision itself did not authorize implementation. The later Project Owner decision `NCIE-WBS16-OWNER-DECISION-2026-09-24-027` released the exact controlled WP-007 implementation scope while preserving every zero-capability and non-waivable restriction in this pack.

## 18. Source traceability and VPF boundary

Primary controlled sources:

- NCIE-009 Chapters 18–20 and `HR9-18-1` / `HR9-19-1`;
- NCIE-003 Chapters 2, 4, 14, 27, 31 and 36;
- NCIE-005 Chapters 19–21 and 29;
- NCIE-006 Chapters 25–27;
- NCIE-007 Chapters 19–21 and 31;
- NCIE-008 Chapters 6, 17 and 20–23;
- W16-D1 through W16-D21 and the controlled WP-001 through WP-006 handovers.

VPF is applied behaviorally to Human-primary authority, identity dignity, consent-sensitive use, explainability, provenance, minimization, sovereignty and African data-residency/cross-border boundaries. The VPF configuration is not modified or redistributed by this pack. No VPF runtime, validator, checksum, signature, certificate, ledger, PADCA/Omnis exchange, quarantine action or residency-enforcement service is claimed to have executed.
