# NCIE WBS-16-WP-006 Human Review Decision Pack

Status: `DECIDED — W16-D18-A / W16-D19-A / W16-D20-A / W16-D21-A; IMPLEMENTATION RELEASED UNDER NCIE-WBS16-OWNER-DECISION-2026-09-24-024`

Prepared: `2026-09-24`

Proposed work package: `WBS-16-WP-006 Agent, Model, Tool and Context Isolation Security`

Recorded decision identifiers:

- `W16-D18` — `HR9-14-1`, Agent Factory ceilings and generated-code review;
- `W16-D19` — `HR9-15-1`, model/provider security acceptance and restricted-data/provider combinations;
- `W16-D20` — `HR9-16-1`, high-risk Tool classes and approval requirements; and
- `W16-D21` — `HR9-17-1`, Context/Memory isolation and cross-context exceptions.

## 1. Purpose and authority boundary

This pack records the Project Owner's architecture selections needed before a separate implementation release for WP-006 may be considered. It defines provider-neutral security boundaries only.

This pack does **not**:

- infer any selection, authority or capability beyond W16-D18-A through W16-D21-A and their recorded conditions;
- authorize implementation;
- create, synthesize, register, promote, activate or run an Agent;
- approve or execute generated code;
- select or activate a model, deployment, provider or provider adapter;
- register, invoke or authorize a Tool;
- enable internet, network or external-system access;
- create a Context/Memory exception or move data between contexts;
- process governed production data;
- assign an institutional authority or operational holder;
- add a dependency, infrastructure, external system or deployment; or
- establish independent security verification, accreditation, acceptance or go-live.

The governing rule throughout is:

`UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

Definition of an Agent, model, provider, Tool, context or security class is taxonomy only. It does not make an instance eligible, approved, active, authorized or available.

## 2. Controlling source findings

### 2.1 NCIE-009 security decisions

The WBS-16 plan identifies the following unresolved NCIE-009 Human decisions for WP-006:

| Requirement | Decision required |
|---|---|
| `HR9-14-1` | Agent Factory resource, model, Tool, data and network ceilings, including generated-code security/review requirements |
| `HR9-15-1` | Model/provider security acceptance and permitted restricted-data/provider combinations |
| `HR9-16-1` | High-risk Tool classes, current authorization and Human approval requirements |
| `HR9-17-1` | Context/Memory isolation and cross-context exception approval requirements |

These decisions must preserve the already approved WBS-16 governance/risk posture: no appetite for loss of Human authority, unauthorized privilege, protected-data exposure, cross-context disclosure, unapproved cross-border transfer, stale authority or security-control bypass.

### 2.2 NCIE-007 Agent/model/Tool architecture

NCIE-007 establishes that:

1. ARGUS coordinates governed services; it does not become the Model Gateway, Tool Gateway, Agent Factory, Memory service, VPF or institutional authority.
2. The Agent Factory composes only approved primitives. A missing capability produces an `ENGINEERING CHANGE CANDIDATE`, never a fabricated permission, Tool, model, connector, runtime or infrastructure capability.
3. Every Agent Definition Package binds purpose, task scope, input/output schema, permitted models, permitted Tools, permitted data classes, context scope, authorization envelope, delegation depth, resource budget, network/egress policy, persistence policy, VPF profile, tests, termination/expiry and provenance.
4. Gate A validates the Agent envelope before execution. Gate B validates substantive output. Neither gate creates current authorization or Human approval.
5. Recursive Agent synthesis is disabled by default. A synthesized Agent receives no Agent Factory authority, cannot self-register, cannot mutate governed registries and cannot promote itself.
6. Agent runtime isolation must enforce explicit Tool, data, model, network, context and resource ceilings and prevent bypass of the Model Gateway, Tool Gateway, Memory/Context services, VPF and current authorization.
7. Generated executable code is a separately governed capability. Dynamic Agent Synthesis does not silently approve generated-code execution. If later approved, static analysis, dependency control, sandboxing, network restrictions, secrets protection, runtime limits, artifact integrity, evaluation and an engineering promotion boundary are mandatory.
8. Every model route is eligibility-first. Classification, purpose, task, residency, provider eligibility, retention, model capability, Tool requirements and current lifecycle state are checked before availability, cost or latency.
9. Provider outage never permits classification downgrade, residency bypass, retention bypass or an unapproved fallback. No eligible route means an explicit degraded/no-route result.
10. All Agent Tool access passes through the Tool Gateway. Tool possession or binding is not action authority.
11. Current actor authorization, exact action/target validation, idempotency where applicable and execution receipts are Tool Gateway concerns. Consequential execution requires current Human/institutional approval.
12. Retrieved Evidence, Documents, Memory, Institutional Knowledge Candidates, web/API content, Tool output and other-Agent output are untrusted data, never higher-authority instructions.
13. Every run is bounded by runtime, tokens, model calls, Tool calls, concurrency, Memory/Context volume and compute, with safe termination for runaway loops.

### 2.3 NCIE-006 Context/Memory architecture

NCIE-006 establishes that:

1. Context assembly is purpose-bound, authorization-filtered, classification-filtered, temporally explicit and minimum necessary.
2. ARGUS and Agents have no direct raw Memory-store access; they use the governed Context/Memory Retrieval Service.
3. Context propagation never propagates authorization. Authorization is independently re-evaluated at every service boundary and reflects current permission changes immediately.
4. Private, shared Room/Investigation/Situation and institutional contexts are distinct. Private context never silently becomes shared context.
5. Shared disclosure is calculated per participant; Room membership never pools permissions or exposes an object merely because another participant may access it.
6. Remembered or historical authorization is never current authorization.
7. Sensitive semantic/vector content requires classification isolation and authorization-aware retrieval; usefulness never justifies placement in general-purpose infrastructure.

### 2.4 Existing controlled WBS-16 baseline

- WP-001 supplies seven principal classes, four-layer current authorization and a zero-grant reference policy.
- WP-002 supplies conservative risk/threat contracts and no production risk-acceptance path.
- WP-003 supplies proofing/lifecycle/assurance/session contracts with no live identity or issuer.
- WP-004 supplies empty authorization mappings and unassigned delegation, privileged and emergency authorities.
- WP-005 supplies opaque protected-material references, empty cryptographic/egress registries and deny-by-default logical network boundaries.

WP-006 must consume those boundaries. It may not replace them with Agent inference, model output, Tool availability, historical context, VPF disposition or cached state.

## 3. Cross-cutting invariants for all four decisions

Whichever options are selected, the following controlled architecture remains binding:

1. Human-primary authority: an Agent/model/Tool may propose or prepare; it cannot approve its own creation, promotion, access or consequential action.
2. Least privilege: every envelope is an explicit intersection of current actor, task, purpose, data, context, model, Tool, resource and egress ceilings.
3. Zero Trust: no placement, registration, prior success, provider reputation, model capability or prior decision creates current trust.
4. Current authorization: every protected retrieval, route and Tool invocation re-evaluates current actor/action/target/purpose and relevant classification.
5. Fail closed: missing, stale, ambiguous, unavailable or conflicting policy, registry, authority, assurance, route or context state denies capability.
6. Provenance: definitions, versions, decisions, evaluations, routes, context references, Tool requests and outcomes remain attributable without storing private chain-of-thought.
7. Minimization: only the minimum authorized context is exposed; prompts, telemetry and evidence do not contain secrets or unnecessary protected values.
8. Sovereignty: provider/runtime replacement must not change doctrine; no provider-specific SDK becomes an architectural escape path.
9. African data residency: no governed data leaves approved African residency without a separately approved exact destination, data class, purpose, authority and cross-border disposition.
10. Separation of definition and activation: taxonomy or contract eligibility never activates an instance or operation.

## 4. Decision W16-D18 — HR9-14-1 Agent Factory ceilings and generated-code review

### Option A — Approve provider-neutral ceilings with zero activation and generated-code execution prohibited (recommended)

Approve a contract-only Agent Factory security envelope. Every future Agent Definition must contain explicit references for:

- Human/governed requesting actor and accountable owner;
- purpose, bounded task and expiry/termination conditions;
- input/output schema and permitted data classifications;
- permitted model classes and exact eligible model-route references;
- permitted Tool classes and exact eligible Tool references;
- Context/Memory source scope and maximum context subset;
- current authorization envelope and delegation depth;
- runtime, token, model-call, Tool-call, concurrency, Memory/Context-volume, compute and storage ceilings;
- network/egress and persistence policy references;
- Gate A, sandbox/evaluation and VPF profile references;
- provenance and integrity references; and
- suspension, cancellation and kill conditions.

Approve these invariant generation/runtime ceilings for the WP-006 reference behavior:

1. Only already approved primitives may be referenced.
2. Agent definitions cannot create permissions, roles, delegations, credentials, secrets, Tools, model routes, contexts, destinations, infrastructure or governance authority.
3. Recursive Agent synthesis, self-registration, registry mutation and automatic promotion remain prohibited.
4. Delegation depth is zero unless a later exact policy explicitly authorizes a class; WP-004 remains the source of delegation eligibility.
5. Direct Database, Operating System, network, external-system, Memory-store, Model-provider or Tool access is prohibited; governed gateways remain mandatory.
6. Internet/network/egress capability is empty. An absent exact route and destination means no egress.
7. Persistence is none unless an exact approved persistence policy exists; temporary runtime state cannot become Institutional Memory or Evidence by implication.
8. Secrets and credential material are never placed in Agent definitions, prompts, Context, logs, telemetry or generated artifacts.
9. All resource dimensions are mandatory contract fields. Numeric values and operational policies remain `UNSPECIFIED`; therefore no Agent may execute.
10. Agent expiry, suspension, revocation, policy change or current-authorization change prevents new work and invalidates stale eligibility.

Approve a configuration-only boundary for initial WP-006 contracts: an Agent Definition may be represented and validated synthetically, but no Agent is instantiated or activated.

Generated executable code remains outside the approved capability set. A generated-code artifact may be represented only as quarantined metadata with `NOT_APPROVED_FOR_EXECUTION`. It cannot be compiled, loaded, imported, executed, promoted, deployed or used as a Tool.

Any later generated-code proposal must receive a new Human decision and, at minimum, demonstrate:

- immutable source/provenance and generator/model/Agent attribution;
- independent Human engineering review and independent Human security review;
- static analysis and dependency/supply-chain review;
- secret/protected-value and prohibited-surface scanning;
- license and provenance review;
- isolated sandbox evaluation with no default network access;
- escape, exfiltration, prompt-injection, authority-expansion and Tool-misuse tests;
- explicit runtime/resource/egress ceilings;
- artifact integrity/versioning;
- a separate engineering promotion decision; and
- no self-review by the generating Agent/model or implementing actor where independence is required.

The following authority classes are defined but operational holders remain `UNASSIGNED`:

- Agent Factory Security Ceiling Authority;
- Ephemeral Agent Activation Authority;
- Agent Registration/Promotion Authority;
- Agent Suspension/Kill Authority;
- Generated-Code Engineering Reviewer;
- Generated-Code Security Reviewer; and
- Generated-Code Promotion Authority.

Implication: a future implementation can validate envelopes and negative paths without creating an Agent, executing code or inventing numeric ceilings. Because operational holders and numeric ceilings are unassigned, the reference behavior has zero Agent execution capability.

### Option B — Approve concrete Agent activation and generated-code classes now

Supply the permitted Agent task/risk classes, numeric resource budgets, model/Tool/data/context ceilings, network destinations, persistence rules, activation policy, promotion policy, operational authority holders, reviewer-independence rules and generated-code risk classes.

Implication: this could support operational activation later, but only after a revised work package, provider/runtime/tool decisions, security testing and separate implementation authority. Selecting B does not itself create or run an Agent.

### Option C — Defer Agent Factory ceiling policy

Do not implement Agent Factory or generated-code security contracts. WP-006 remains blocked for this control domain.

Implication: no Agent definition, synthesis, sandbox or generated-code capability may be represented as security-approved.

Recommendation: `W16-D18-A`, because it captures every mandatory envelope and Human gate while preserving zero activation, zero generated-code execution and the existing empty-registry/deny-by-default architecture.

## 5. Decision W16-D19 — HR9-15-1 model/provider security acceptance and restricted-data combinations

### Option A — Approve an empty provider-neutral eligibility registry and exact-combination contract (recommended)

Approve a provider/model security record containing, at minimum:

- provider, model, version and deployment references;
- lifecycle state: Candidate, Evaluated, Approved/Active, Restricted, Suspended, Deprecated or Retired;
- approved purpose/task capability;
- classification ceiling;
- approved residency scope and exact processing/storage destinations;
- prompt/input/output/log/telemetry/abuse-monitoring retention behavior;
- training/fine-tuning reuse prohibition or approved terms;
- Tool-calling and output-schema capability;
- isolation, encryption, incident, deletion and subcontractor assurance references;
- security/evaluation/red-team results and review dates;
- current approval, restriction, suspension and expiry references; and
- model route, policy version and provenance requirements.

Approve eligibility-first evaluation in this order: current provider status, model/deployment lifecycle, task/purpose, classification, residency, retention/reuse, security assurance, Tool/output capability and only then availability/performance/cost/latency.

Approve an exact restricted-data/provider combination registry keyed by:

- canonical data-classification reference;
- data element/category reference;
- purpose/task reference;
- model/deployment/provider reference;
- processing and storage destination references;
- retention/reuse policy reference;
- required assurance/evaluation reference;
- effective/expiry/revocation state; and
- approving authority/decision reference.

The registry is empty for WP-006. No provider, model, deployment, destination or governed-data combination is approved. Consequently:

- no external or internal model route exists;
- no governed production data may be sent to a model/provider;
- restricted or protected data has `NO ROUTE`;
- no provider is used as fallback;
- provider/model unavailability produces an explicit degraded/no-route result; and
- local contract tests use synthetic references and no provider call.

The following authority classes are defined but holders remain `UNASSIGNED`:

- Model Approval Authority;
- Provider Security Acceptance Authority;
- Restricted-Data/Provider Combination Authority;
- African Data Residency/Cross-Border Authority;
- Privacy/Legal Review Authority;
- Model/Provider Emergency Suspension Authority; and
- Independent Model Security/Evaluation Reviewer.

All numeric thresholds, review cadence, evaluation pass criteria, red-team cadence, retention duration and assurance standards remain `UNSPECIFIED`. Missing criteria prevent approval.

Implication: model/provider eligibility can be implemented as a fail-closed contract without selecting a provider or permitting a single model call. Provider and model sovereignty are preserved because doctrine is independent of any vendor.

### Option B — Approve named providers, models and restricted-data combinations now

Supply exact providers, models/versions/deployments, African processing/storage destinations, data classifications/elements, purposes, retention/reuse terms, security evidence, evaluation thresholds, approving authorities, expiry/review cadence and permitted fallback chains.

Implication: this becomes a concrete technology, privacy, legal, residency and operational-security decision requiring a revised package and explicit implementation/integration authority. Selecting B alone does not activate a provider.

### Option C — Defer model/provider security policy

Do not implement provider/model eligibility contracts. WP-006 remains blocked for model access.

Implication: no model or provider may be represented as eligible, and no governed data may be routed to AI processing.

Recommendation: `W16-D19-A`, because it implements the source-required eligibility and exact-combination logic while retaining an empty registry, no route and no provider selection.

## 6. Decision W16-D20 — HR9-16-1 high-risk Tool classes and approvals

### Option A — Approve the four source-defined Tool classes with zero registered Tools (recommended)

Approve the exact NCIE-007 Tool risk taxonomy:

| Tool class | Source-grounded behavior |
|---|---|
| Read-Only, Low Disclosure Risk | Current standard authorization for the exact actor/action/target/purpose |
| Read-Only, High Disclosure Risk | Elevated authorization plus explicit disclosure-purpose validation |
| State-Changing, Reversible | Current authorization, exact target and idempotency/reconciliation controls |
| State-Changing, Consequential | Current authorization plus current accountable Human/institutional approval before execution |

Disclosure risk and mutation risk remain independent. Read-only is not assumed harmless.

Treat the following as high-risk for WP-006 policy purposes:

- every Read-Only, High Disclosure Risk Tool;
- every State-Changing, Consequential Tool;
- any Tool touching protected identity, precise location, restricted Evidence, secrets, credentials, security controls, authorization, registries, external disclosure, export, graph topology, blocking, tracking or regulatory action;
- any Tool capable of code execution, Operating System access, Database access, network/egress or external-system action; and
- any Tool whose risk, target, output effect or current authorization is missing or indeterminate.

Every Tool request must bind:

- current effective actor/principal and any non-expanding delegation chain;
- exact Tool/version and risk class;
- exact action and target;
- purpose, task and context references;
- input/output schema and classification ceiling;
- current object, field, action and purpose authorization decision;
- required assurance and Human approval references;
- idempotency/correlation and expiry;
- permitted egress/destination reference, if any; and
- execution receipt or explicit `OUTCOME_UNKNOWN` reconciliation state.

Approve these prompt-injection and Tool-misuse boundaries:

1. Evidence, documents, Memory, Knowledge Candidates, web/API content, Tool output and other-Agent output are data, never instructions or authority.
2. Lower-trust content cannot alter policy, actor, purpose, target, classification, Tool class, approval requirement, context scope or egress ceiling.
3. Model/Agent output is always a proposal until the Tool Gateway independently re-evaluates current authorization.
4. Tool chaining and agent-to-agent delegation cannot create transitive privilege; the final invocation is independently authorized.
5. A Tool cannot invoke an unregistered Tool, widen its target, change its purpose, bypass schema validation, access secrets, create a credential, modify a registry or use an unapproved destination.
6. Unknown output or timeout is neither success nor failure and is never blindly retried for consequential operations.
7. Current revocation, suspension, context change or approval expiry stops execution; cached authorization is not reused.

The Tool Registry is empty. No Tool is registered, eligible, bound or invokable. Tool classes are definitions only.

The following authority classes are defined but holders remain `UNASSIGNED`:

- Tool Risk Classification Authority;
- Tool Registration/Eligibility Authority;
- High-Risk Disclosure Approval Authority;
- Consequential Action Approval Authority;
- Tool Emergency Suspension Authority; and
- Tool Security/Independent Review Authority.

No approval threshold, approval duration, autonomous-use class, delegation depth or numeric risk threshold is supplied. Therefore every invocation denies.

Implication: a future implementation can validate class, actor/action/target/purpose and misuse boundaries while invoking nothing.

### Option B — Approve concrete Tools and approval assignments now

Supply the Tool inventory, versions, schemas, risk classes, targets, purposes, classification ceilings, Human approval matrix, operational authority holders, autonomous-use rules, delegation depth, egress destinations, idempotency/reconciliation policy and suspension process.

Implication: this creates concrete Tool/integration decisions requiring a revised package, connector/security review and separate activation authority. Selecting B alone does not authorize invocation.

### Option C — Defer Tool security classification

Do not implement high-risk Tool contracts. WP-006 remains blocked for all Tool capability.

Implication: the Tool Registry remains empty and every Tool request is denied.

Recommendation: `W16-D20-A`, because it adopts the exact four-class source taxonomy and complete current-authorization boundary without inventing a Tool, approval holder or executable path.

## 7. Decision W16-D21 — HR9-17-1 Context/Memory isolation and cross-context exceptions

### Option A — Approve strict context isolation with an empty exception registry (recommended)

Approve these distinct context security classes:

- Private User Context;
- Session/Workspace Context;
- Collaborative Room Context;
- Investigation Context;
- Situation/Task Context;
- Agent Run Context;
- Decision-Time/Historical Context; and
- Institutional Context/Approved Knowledge.

Classification does not authorize movement between classes. Shared storage must not collapse their governance meaning.

Approve these isolation rules:

1. Context is bound to one current actor/task/purpose/temporal mode and exact source scope.
2. Every retrieval applies current actor authorization, purpose, classification, temporal mode, relevance and minimum-necessary filtering before disclosure.
3. Agents/models use the governed Context/Memory Retrieval Service only; direct Memory-store, index, cache or conversation-history access is prohibited.
4. Context propagation does not propagate permission. Every service, model route and Tool invocation independently re-authorizes.
5. Private context cannot silently enter shared, Room, Investigation, Situation, Agent or institutional context.
6. Room/shared context is computed per participant; permissions are never pooled or unioned.
7. Historical/remembered authorization cannot support a current action.
8. Agent Run Context expires with the run and cannot become persistent Memory, Institutional Knowledge, Evidence or a new Agent definition without its separate governed lifecycle.
9. Prompt/model/provider Context is the minimum authorized subset and excludes credentials, secrets, unnecessary protected values and unauthorized cross-context references.
10. Suspension, revocation, membership change or source invalidation blocks future retrieval and invalidates represented cached/Agent context.

Approve a cross-context exception contract requiring all of the following:

- exception reference and version;
- source and destination context classes/instances;
- current requesting actor and accountable Human owner;
- exact purpose, data elements/fields and classification;
- legal/consent/authority references where applicable;
- current source-object and destination-purpose authorization;
- minimum-necessary justification;
- approved processing/storage/residency destinations;
- effective time, explicit expiry and revocation state;
- source-context owner and destination-context owner decisions;
- independent privacy/security review where required;
- provenance, audit and downstream-dependency references; and
- deletion/reconciliation obligations after expiry or revocation.

The exception registry is empty. No context pair, data element, purpose, authority, holder, consent rule, threshold, duration, destination or exception is approved. Missing any required element denies transfer/retrieval.

The following authority classes are defined but holders remain `UNASSIGNED`:

- Cross-Context Exception Authority;
- Source Context Owner;
- Destination Context Owner;
- Privacy/Consent Review Authority;
- Classification/Disclosure Authority;
- African Data Residency/Cross-Border Authority; and
- Independent Context Security Reviewer.

Implication: WP-006 can model isolation and prove that unauthorized cross-context access fails, but it cannot create an exception or move governed data.

### Option B — Approve specific cross-context exception classes now

Supply exact permitted source/destination pairs, data fields, purposes, classifications, actor classes, consent/legal bases, operational authority holders, review requirements, expiry/retention rules, African destinations and cross-border dispositions.

Implication: this creates real disclosure/data-movement policy requiring privacy, legal, residency and security approval plus a revised implementation package. Selecting B does not itself create an exception.

### Option C — Defer cross-context exception policy

Implement isolation only, with no exception-contract capability beyond unconditional denial.

Implication: all cross-context access and transfer remains prohibited. Later exception support requires a new decision and implementation release.

Recommendation: `W16-D21-A`, because an empty, exact exception registry allows enforceable isolation tests without fabricating an authority, permitted context pair or disclosure path.

## 8. Consolidated recommendation

Recorded selection, matching the recommendation: `W16-D18-A / W16-D19-A / W16-D20-A / W16-D21-A`.

| Decision | Recommended definition-only result | Remains unassigned / denied |
|---|---|---|
| W16-D18 / HR9-14-1 | Agent envelope, runtime ceilings and generated-code quarantine/review contracts | Agents, activation, numeric budgets, runtime, network, generated-code execution, reviewers and promotion |
| W16-D19 / HR9-15-1 | Provider/model eligibility and exact restricted-data-combination contracts | Providers, models, deployments, destinations, combinations, thresholds and routes |
| W16-D20 / HR9-16-1 | Four Tool classes, high-risk predicate and current invocation checks | Tools, bindings, approvals, holders, invocations, destinations and autonomous-use rules |
| W16-D21 / HR9-17-1 | Context classes, isolation rules and exact exception contract | Exceptions, context pairs, data fields, purposes, authorities, durations and transfers |

These recommendations preserve the existing controlled architecture because all registries begin empty, all operational authority interfaces are unassigned and all missing policy returns deny/no capability.

## 9. Explicit UNASSIGNED / UNSPECIFIED register

The following must not be invented during WP-006 preparation or implementation:

### Institutional authorities and holders

- Every Agent Factory, activation, registration, promotion, suspension and generated-code authority listed under W16-D18.
- Every provider/model acceptance, data-combination, legal/privacy, residency and suspension authority listed under W16-D19.
- Every Tool classification, registration, disclosure, consequential-action, suspension and security-review authority listed under W16-D20.
- Every cross-context, source/destination-owner, privacy/consent, classification and residency authority listed under W16-D21.

### Thresholds and policies

- Numeric runtime, token, model-call, Tool-call, concurrency, compute, storage or Context limits.
- Agent activation/risk thresholds, promotion thresholds, expiry defaults or delegation depth.
- Generated-code risk thresholds, scan pass criteria, reviewer quorum or promotion criteria.
- Model evaluation thresholds, assurance levels, review/red-team cadence, retention durations or fallback policy.
- Tool risk scores, approval duration, autonomous-use threshold or retry limit.
- Cross-context duration, volume, field, consent, review or retention thresholds.

### Technologies and operational assignments

- Agent frameworks, factories, runtimes, sandboxes, orchestrators or registries.
- Providers, models, deployments, adapters, endpoints or provider accounts.
- Tools, connectors, schemas, target systems, execution identities or credentials.
- Networks, internet access, routes, domains, IP ranges, proxies or egress destinations.
- Context/Memory stores, indexes, caches, destinations or allowed context pairs.
- Infrastructure, regions, environments, products or deployment topology.

For every item above: `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

## 10. Proposed WP-006 implementation scope

Only after the Project Owner records explicit W16-D18 through W16-D21 selections and issues a separate decision naming and releasing `WBS-16-WP-006 Agent, Model, Tool and Context Isolation Security`, the package may include:

1. Provider-neutral enums and immutable metadata contracts for Agent ceilings, model/provider eligibility, Tool risk and Context classes.
2. Empty versioned registries for approved Agent primitives, provider/model/data combinations, eligible Tools and cross-context exceptions.
3. Fail-closed evaluators for Agent definitions, generated-code state, model routes, Tool requests and context access.
4. Unassigned protocols/interfaces for every Human/institutional authority named in this pack.
5. A zero-capability Agent Factory reference boundary that validates synthetic definitions but cannot instantiate or activate an Agent.
6. A no-route Model Gateway reference boundary that cannot contact a provider.
7. A no-invocation Tool Gateway reference boundary that cannot execute a Tool.
8. A deny-all cross-context boundary that cannot retrieve or transfer governed data.
9. Prompt-injection and Tool-misuse contract checks using synthetic instruction-shaped strings only.
10. Generated-code metadata/quarantine contracts with no source-code generation, compilation, import or execution.
11. Provenance and minimized non-authoritative security signals with no prompt, secret, protected value or private chain-of-thought content.
12. Standard-library local tests, cumulative regression, traceability and implementation evidence.

## 11. Explicit exclusions

WP-006 implementation must exclude:

- Agent creation, synthesis, instantiation, activation, registration, promotion or execution;
- generated source/executable code creation, analysis using external services, compilation or execution;
- named Agent frameworks/runtimes/sandboxes or infrastructure;
- model/provider selection, provider adapters, APIs, credentials, accounts, calls or telemetry;
- real prompts, governed production data, protected identities, Evidence, secrets or credentials;
- Tool registration, Tool binding, Tool invocation, connector activation or action execution;
- internet/network access, DNS, external destinations, routes or cross-border transfer;
- Context/Memory retrieval, persistence, index access, data transfer or exception creation;
- role, permission, delegation, privilege, emergency or approval activation;
- institutional Evidence creation, production audit, notification or monitoring;
- new dependencies, infrastructure, external systems or deployment;
- WP-007 or any later WBS-16 control domain; and
- independent security verification, accreditation, controlled acceptance or go-live.

## 12. Stop conditions

Stop and request a new Human decision if any work would require:

1. an Agent instance, Agent run, Agent activation or registry entry;
2. recursive synthesis, delegation depth above the selected ceiling or self-registration;
3. generated code, compilation, loading, import, execution or promotion;
4. a numeric resource, evaluation, risk, review, retention or expiry threshold;
5. a named provider, model, version, deployment, adapter, account, endpoint or destination;
6. a restricted-data/provider combination or any governed-data model route;
7. a Tool, connector, schema, binding, invocation, approval or external action;
8. Operating System, Database, network, internet, external-system or secret access;
9. a context pair, data element, consent/legal basis, cross-context exception or data movement;
10. an institutional authority holder, reviewer, approver, eligible actor or operational assignment;
11. a product, dependency, persistent store, infrastructure or deployment;
12. a broader WBS-16 control domain or change to a prior decision; or
13. any claim of operational AI security, independent verification, accreditation, acceptance or go-live.

## 13. Proposed local completion criteria

WP-006 may be reported locally work-complete only if all of the following hold:

1. Explicit Project Owner selections for W16-D18 through W16-D21 and a separate implementation release are recorded without expansion.
2. Security-class definition remains distinct from instance eligibility, activation, authorization and execution.
3. Every operational authority interface is unassigned and fails closed.
4. Every controlled registry starts empty and has no hidden default entry.
5. Agent-envelope validation covers purpose, task, model, Tool, data, context, authorization, delegation, resource, egress, persistence, expiry and provenance.
6. Missing or unspecified resource ceilings prevent Agent execution; no Agent runtime exists in the reference implementation.
7. Recursive synthesis, self-registration, registry mutation, automatic promotion and capability fabrication deny.
8. Generated-code artifacts remain non-executable/quarantined metadata; no generation or execution path exists.
9. Model/provider eligibility is current, exact, classification/purpose/residency/retention aware and availability never overrides eligibility.
10. The provider/model/data-combination registry is empty and every route returns no route.
11. No provider-specific SDK, provider call, credential, endpoint or governed data enters source/tests/evidence.
12. The four source-defined Tool classes and disclosure/mutation distinction are represented exactly.
13. Every Tool request requires current actor/action/target/purpose authorization; consequential requests additionally require current Human/institutional approval.
14. The Tool Registry is empty and no Tool invocation path exists.
15. Prompt injection from every source-defined untrusted surface cannot alter policy, authorization, Tool target, context or egress ceilings.
16. Context classes remain isolated; permission pooling, direct Memory access, remembered authorization and implicit private-to-shared promotion deny.
17. The cross-context exception registry is empty and every cross-context request denies.
18. Revocation, suspension, expiry, membership change and current-state change invalidate stale eligibility/context.
19. Signals and errors are minimized and contain no prompt, protected value, secret, credential or private chain-of-thought.
20. Positive contract-construction and comprehensive negative-path tests use synthetic/non-governed values only.
21. WP-001 through WP-005 and WBS-15 regression tests continue to pass in the approved locked environment.
22. Strict typing, lint, formatting, compilation, reproducibility and template-verification gates pass without a new dependency.
23. Traceability maps HR9-14-1 through HR9-17-1 to decisions, contracts, tests, evidence and deferred operational owners.
24. Evidence states that local tests are not Agent activation, model/provider acceptance, Tool authorization, cross-context approval, independent verification, accreditation, acceptance or go-live.

## 14. Recorded Project Owner decision

- W16-D18 selection: `A — provider-neutral Agent Factory/runtime ceilings; zero Agent activation; generated executable code prohibited and quarantined as NOT_APPROVED_FOR_EXECUTION`
- W16-D19 selection: `A — provider-neutral model/provider and restricted-data/provider combination contracts; empty eligibility registry and zero routes`
- W16-D20 selection: `A — four source-defined Tool classes and current actor/action/target/purpose boundaries; zero Tools`
- W16-D21 selection: `A — strict Context/Memory isolation and exact exception contracts; empty exception registry and zero transfer capability`
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`
- Decision date: `2026-09-24`
- Conditions: `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`, plus every zero-capability and no-activation restriction recorded in the evidence record.
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-24-023`
- Evidence type: `Self-Authorized Project Owner Decision`

The decision is recorded in `implementation/decisions/NCIE_WBS16_OWNER_DECISION_2026-09-24-023.md`.

The architecture decision itself did not authorize implementation. The later Project Owner decision `NCIE-WBS16-OWNER-DECISION-2026-09-24-024` released the exact controlled WP-006 implementation scope while preserving every zero-capability restriction in this pack.

## 15. Source traceability and VPF boundary

Primary sources:

- NCIE-009 Chapters 14-17 and `HR9-14-1` through `HR9-17-1`;
- NCIE-007 Chapters 3-12, 14, 19-22, 24-30 and 32-34;
- NCIE-006 Chapters 4, 13-17, 24-25 and 34;
- NCIE-005 Chapters 4, 23, 25, 27 and 29;
- NCIE-004 Chapters 18-20 and 33;
- NCIE-008 Human-primary authority and segregation-of-duties requirements;
- NCIE-003 classification, authorization, provenance and protected-identity semantics;
- W16-D1 through W16-D17 and the WP-001 through WP-005 controlled handovers.

VPF is applied behaviorally to Human-primary authority, identity dignity, consent-sensitive use, least privilege, explainability, provenance, minimization, sovereignty and African data-residency/cross-border boundaries. The VPF configuration is not modified or redistributed by this pack. No VPF runtime, Gate service, validator, checksum, signature, ledger, PADCA/Omnis exchange, quarantine action or residency-enforcement service is claimed to have executed.
