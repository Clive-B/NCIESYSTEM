# NCIE WBS-16-WP-005 Human Review Decision Pack

Status: `DECIDED — W16-D15-A / W16-D16-A / W16-D17-A; IMPLEMENTATION RELEASED SEPARATELY UNDER ...-021`

Prepared: `2026-09-23`

Decided: `2026-09-23`

Proposed work package: `WBS-16-WP-005 Secrets, Cryptography and Network Zero-Trust Contracts`

## 1. Purpose and authority boundary

This pack presents the Human decisions required before WP-005 may be considered for a separate implementation release. It covers:

- `HR9-11-1`: secrets/key custodial authority and secret-handling exception policy;
- `HR9-12-1`: cryptographic policy and key-separation tiers where an approved upstream source has not fixed them; and
- `HR9-13-1`: network trust zones, service boundaries, Agent/external egress classes and exception-granting authority.

The Project Owner selections recorded under `NCIE-WBS16-OWNER-DECISION-2026-09-23-020` approve architecture only. Nothing in this pack:

- makes or infers a Human decision;
- assigns a custodian, policy owner, approver, exception authority, network owner or operational holder;
- selects a secret manager, KMS/HSM, cryptographic product, algorithm, certificate system, firewall, service mesh, cloud/network platform or infrastructure;
- creates, imports, stores, rotates or exposes a live secret, key, certificate, token or production credential;
- activates networking, ingress, egress, an external system, a provider or deployment; or
- authorizes implementation, accreditation, acceptance or go-live.

The three required architectural selections are now recorded. A later, separate Project Owner decision must authorize the exact WP-005 implementation scope before any implementation begins.

## 2. WP-004 source-control evidence reconciliation

Read-only verification on `2026-09-23T09:43:51.387Z` returned:

`08e7b8201a623b70007a9e2b5164509f12e7853e  refs/heads/main`

The two previously reported hashes describe successive repository states:

| Hash | Exact meaning |
|---|---|
| `48a25e6751a2c6c51a2e00c124d7c714a9b95499` | WP-004 implementation commit: `Implement WBS-16-WP-004 access control contracts`; independently verified immediately after its push |
| `08e7b8201a623b70007a9e2b5164509f12e7853e` | Later governance-only commit: `Record WBS-16-WP-004 source release evidence`; exact final remote `main` head observed before this WP-005 preparation |

The later commit added release evidence and associated README, traceability and handoff references. It did not alter WP-004 source, tests or access state. The hashes are therefore not competing claims about one verification point. No history was rewritten.

`implementation/wbs-16-wp-004-authorization-delegation-privileged-emergency/evidence/SOURCE_CONTROL_RELEASE_20260923_001.md` has been reconciled locally to state this chronology and exact final observed remote head. No reconciliation commit or push is authorized or performed by this preparation task; consequently, the remote head remains `08e7b8201a623b70007a9e2b5164509f12e7853e`.

## 3. Controlling source findings

The controlled source chain fixes these boundaries:

1. Secrets never appear in prompts, logs, Agent Context or source code. Occurrence on a prohibited surface is a security incident, not an allowed implementation shortcut.
2. Secret issuance, rotation, access and storage are distinct governed events with attributable actors.
3. Key custody is distinct from ordinary application identity. Using a key does not make a workload its custodian.
4. Root, intermediate and data-encryption key hierarchy concepts are recognized, while product/HSM/KMS selection remains open.
5. Custodial and assurance/audit functions are segregated. An exception approver cannot be the requester, and Assurance/Audit remains independent.
6. Encryption protects data but does not authorize access. IAM, classification, purpose, consent and disclosure controls still apply.
7. Protection is required conceptually for data at rest, in transit and in sensitive fields. Sensitive-field protection may include tokenization or masking in addition to transport/at-rest protection.
8. Keys protecting different sensitivity tiers are separated. Crypto agility is required, but NCIE-009 deliberately fixes no algorithm, key length or product.
9. Network placement and reachability never establish trust or application authorization.
10. Network policy is deny-by-default. Segmentation, service identity, mutually authenticated transport concepts and private connectivity bound lateral movement.
11. Agent egress is bounded by sandbox and Task Contract ceilings. An Agent may not reach an arbitrary provider endpoint or obtain unrestricted internet access through natural-language instruction.
12. External/model/tool paths use governed gateway and destination/service allow-list boundaries; absence of a current explicit exception denies.
13. Residency, sovereignty, classification, retention and purpose constraints apply together. Provider or route availability cannot relax them.
14. The approved WP-002 development posture has no appetite for unapproved cross-border transfer, secret exposure, stale authority or security-control bypass.
15. NCIE-004 product references—including HashiCorp Vault, cloud-native secret managers, Vault Transit, dedicated HSM, cert-manager, a CA, envelope encryption, Kubernetes/network policy and the seven-zone deployment—are Proposed Design Defaults or require security/sovereignty confirmation unless separately approved. This pack does not select them.

## 4. Definition is not operational selection or activation

| A later authorized provider-neutral WP-005 may define | This pack does not select, assign or activate |
|---|---|
| Secret/key reference metadata and lifecycle-event contracts | A secret manager, literal secret, key, certificate, credential or live lifecycle operation |
| Abstract custodial, approval, exception and assurance interfaces | An institutional holder, service account, operator or authority assignment |
| Protection classes and conceptual key-separation tiers | An algorithm family, key length, cipher suite, certificate profile, KMS/HSM or CA |
| Logical trust-zone and service-boundary labels | A subnet, address, firewall rule, service mesh, cloud VPC/VNet, cluster or route |
| Egress-decision classes and deny-by-default evaluation | An allow-list entry, destination, external connection, Agent internet access or network activation |
| Residency/sovereignty constraint references | A hosting/provider choice, cross-border permit or claim of technical residency enforcement |

Until a competent Human decision supplies a required operational assignment or policy, the implementation meaning is `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.

## 5. Decision W16-D15 — HR9-11-1 secrets/key custody and exception policy

### 5.1 Exact source-grounded control requirements

NCIE-009 Chapter 11 requires:

- no secrets in prompts, logs, Agent Context or source code;
- governed and attributable issuance, rotation, access and storage events;
- separation of key custody from application identity;
- conceptual root, intermediate and data-encryption key hierarchy;
- segregation of custodial and independent assurance/audit functions; and
- Human confirmation of the secrets/key custodial authority and exception policy.

Its RACI leaves the `Accountable Authority Class` and `Secrets/Key Custodian` as `to be assigned`. NCIE-008 requires every exception to carry scope, duration, compensating controls, expiry, fresh renewal, revocation and an approver who is not the requester.

### 5.2 Human disposition options and implications

#### Option A — Approve provider-neutral custody/exception contracts; leave holders unassigned (recommended)

Approve these abstract authority classes for contract representation only:

- `Secrets/Key Policy Accountable Authority` — decides policy and any permitted exception class;
- `Secrets/Key Custodian` — performs governed custody/lifecycle functions but does not self-approve policy or exceptions;
- `Secret Consumer` — may reference minimum-necessary secret use but never owns custody merely by use;
- `Exception Reviewer` — independently assesses a request; and
- `Assurance/Audit` — independently verifies operation and remains separate from custody.

No institutional holder is assigned. A later WP-005 may define authority interfaces and must ship them unassigned, so no secret/key lifecycle or exception can be approved or executed.

Approve this exception policy boundary:

1. No exception may permit a secret, private key, recovery value, credential value or certificate private-key material in source code, prompts, Agent Context, generated code, logs, telemetry, test fixtures, documentation or an uncontrolled export.
2. No exception may permit plaintext fallback, local cached-key fallback, shared reusable Human credentials, removal of attribution, or conflation of consumer and custodian.
3. Any future exception not prohibited above requires a competent Human authority, exact target/scope, purpose, classification, residency/sovereignty assessment, requester, independent review, compensating controls, effective time, explicit expiry, revocation conditions and audit obligation.
4. Renewal is a fresh decision; there is no automatic rollover. Missing, stale, conflicted, expired, revoked or out-of-scope authority denies.
5. An exception never repeals policy, creates an unavailable technical capability or authorizes cross-border handling.

Implication: provider-neutral reference/lifecycle and exception-decision contracts can be implemented and negatively tested without holding or processing secret material. Every operational path remains unavailable.

#### Option B — Supply operational custodial and exception assignments

The Human authority supplies the institutional functions/current holders, separation-of-duties matrix, secret/key domains, permitted exception classes, prohibited exception classes, maximum durations, revocation authority and assurance obligations.

Implication: the pack must be revised and reviewed before implementation. This option still does not select a product or authorize a live secret/key operation.

#### Option C — Defer secrets/key governance contracts

Keep `HR9-11-1` open and implement no WP-005 secret/key capability.

Implication: WP-005 and downstream work dependent on governed secret/key interfaces remain blocked.

Recommendation: `W16-D15-A`, because it encodes the absolute exposure prohibitions and separation of duties without inventing institutional holders, exceptions or secret infrastructure.

### 5.3 Items that remain institutionally unassigned

- Accountable policy/exception authority and current holder.
- Secrets/Key Custodian, lifecycle operator, independent reviewer and Assurance/Audit holder.
- Secret/key domains, consumer assignments and access policy.
- Permitted exception categories beyond the source-fixed prohibitions.
- Numeric rotation, lifetime, lease, review or renewal intervals.
- Product, vault, KMS/HSM, CA, certificate system, storage and delivery mechanism.

## 6. Decision W16-D16 — HR9-12-1 cryptographic policy and key separation

### 6.1 Exact source-grounded protection and separation concepts

NCIE-009 Chapter 12 fixes conceptual protection for:

| Protection scope | Source requirement |
|---|---|
| Data at rest | Cryptographic protection required where classification applies; still requires current authorization |
| Data in transit | Authenticated protected transport concept; reachability/encryption does not authorize access |
| Sensitive fields | Field protection, tokenization or masking in addition to at-rest/in-transit protection |

It also requires separation among sensitivity tiers, recognizes root/intermediate/data-encryption key concepts, and requires crypto agility. It deliberately does not fix an algorithm, key length or product. `HR9-12-1` is Non-Blocking for these conceptual protections but requires Human approval of algorithm families and separation tiers where not fixed upstream.

### 6.2 Human disposition options and implications

#### Option A — Approve provider-neutral protection/key-separation contracts; defer algorithms and products (recommended)

Approve a logical contract taxonomy containing:

- protection scopes `AT_REST`, `IN_TRANSIT` and `SENSITIVE_FIELD`;
- conceptual hierarchy tiers `ROOT`, `INTERMEDIATE` and `DATA_ENCRYPTION`;
- separation dimensions for sensitivity/classification tier, purpose/domain, environment and custodial boundary;
- policy/version, effective/expiry/revocation and crypto-agility references; and
- fail-closed evaluation when the applicable current policy, protection requirement, separation rule or authoritative reference is absent.

No algorithm family, key length, mode, cipher suite, signature scheme, certificate profile, rotation interval, KMS/HSM, CA or cryptographic implementation is approved. No reference contract may claim that encryption occurred.

Implication: WP-005 can express and validate protection obligations, hierarchy and separation without pretending to implement cryptography. Operational cryptographic use remains blocked until a competent Human decision supplies an approved concrete policy.

#### Option B — Supply technology-neutral algorithm/profile policy now

The Human authority supplies approved algorithm families, minimum strengths, modes/profiles, transport/certificate requirements, key-generation/custody requirements, separation tiers, rotation/revocation rules, legacy/deprecation rules, regulatory basis and effective version.

Implication: WP-005 may encode the supplied policy but must still remain product-neutral unless a separate technology decision is made. The policy requires security/sovereignty and qualified cryptographic review.

#### Option C — Defer cryptographic-policy contracts

Preserve only the existing conceptual source statements and add no WP-005 cryptographic contract.

Implication: HR9-12-1 remains open. Any operation requiring a concrete algorithm/profile or key tier denies, and broader WP-005 completion may be knowingly deferred or blocked by the Project Owner.

Recommendation: `W16-D16-A`, because it preserves mandatory protection, separation and agility while refusing to invent cryptographic standards or select infrastructure.

### 6.3 Items that remain institutionally unassigned

- Cryptography/Data Protection Owner and policy approver.
- Algorithm families, strengths, modes, suites, certificate profiles and deprecation dates.
- Exact classification-to-key-tier mapping and numeric lifetimes/rotation periods.
- KMS/HSM, vault, CA, certificate automation, libraries and provider choices.
- Claim that any data, field, channel or artifact has been encrypted, signed, tokenized or masked.

## 7. Decision W16-D17 — HR9-13-1 trust zones, service boundaries, egress and exceptions

### 7.1 Source-fixed network doctrine and proposed topology

NCIE-009 Chapter 13 fixes:

- deny-by-default ingress and egress;
- explicit verification regardless of placement;
- network reachability is not application authorization;
- segmentation, service identity, mutually authenticated transport concepts and private connectivity;
- scoped and attributable exceptions through NCIE-008 Chapter 21; and
- Agent egress bounded by NCIE-007 sandbox and Task Contract ceilings.

NCIE-004 proposes, but does not independently approve, seven logical zones:

1. Edge/API.
2. Application.
3. Data.
4. AI.
5. Integration.
6. Security/Observability.
7. Management/Governance.

Its source-defined paths include Public/Operator Network → Edge/API → Application; Application → Data through governed contracts; Application → AI through the Model Gateway; no direct AI → Data crossing; Security/Observability monitoring/gating the operating zones; Management/Governance governing zones; and Ephemeral Agent Execution reaching models/tools only through Model/Tool Gateways with no administrative write to Data Zone registries.

### 7.2 Proposed provider-neutral egress-class normalization

The following labels are proposed WP-005 contract normalizations derived from those source paths; they are not claims that NCIE-009 supplied literal class names:

| Proposed contract class | Source-grounded ceiling | Default |
|---|---|---|
| `NO_EGRESS` | No permitted destination/path | Deny |
| `INTERNAL_GOVERNED_SERVICE` | Named registered service through an approved service boundary with current service identity and application authorization | Deny absent current policy |
| `MODEL_GATEWAY_ONLY` | Named eligible model deployment through Model Gateway; never arbitrary provider endpoint | Deny absent current policy |
| `TOOL_GATEWAY_ONLY` | Named eligible Tool/connector and target through Tool Gateway/current actor-action-target authorization | Deny absent current policy |
| `EXPLICIT_EXTERNAL_DESTINATION` | Exact destination/service allow-list entry, purpose, data class, residency/retention and current exception approval | Deny absent current exception |

For Agents, `NO_EGRESS` is the reference default. Any allowed path must be no broader than the intersection of sandbox ceiling, Task Contract, Agent identity, destination eligibility, classification, purpose, residency, retention and current authorization. Generated code inherits the same ceiling.

### 7.3 Human disposition options and implications

#### Option A — Approve logical zones and provider-neutral egress contracts; leave infrastructure and authorities unassigned (recommended)

Approve the seven NCIE-004 zones as logical contract labels only, the source-fixed service paths/forbidden crossings, and the five normalized egress classes above.

Approve these controls:

1. Every boundary decision binds source zone, destination zone/service, acting service/workload/Agent identity, action, purpose, classification, residency, retention, policy version and current time.
2. Reachability, authenticated transport or service identity cannot replace WP-001/WP-004 current application authorization.
3. All ingress/egress is denied unless a current explicit policy permits the exact path. Unknown zone, destination, route, identity, data class, residency or exception state denies.
4. Agent/model/tool/external egress is gateway-bound and destination-specific. No arbitrary endpoint, wildcard internet access, natural-language expansion or fallback to an ineligible provider is allowed.
5. External egress carrying governed data denies unless classification, minimization, purpose, retention, African residency/sovereignty and any cross-border authorization are separately evidenced.
6. A future exception follows NCIE-008 Chapter 21: exact scope/duration, compensating controls, independent review, non-requester approval, explicit expiry, fresh renewal, revocation and audit.
7. The `Accountable Authority Class`, `Network Security Owner` and exception-granting authority remain unassigned; therefore no network/egress exception can be granted by the reference implementation.

Implication: a later WP-005 can implement logical policy contracts and negative tests without creating a network, route, firewall rule or external connection.

#### Option B — Return with a different zone/egress taxonomy

The Human authority supplies the logical zones, permitted service paths, prohibited crossings, Agent/external egress classes, data/residency ceilings, exception authority and decision evidence.

Implication: the pack must be revised before implementation. Product/subnet/firewall/cloud choices remain separate even if logical policy is approved.

#### Option C — Defer network/egress contracts

Keep all modeled ingress/egress at `NO_EGRESS / DENY` and implement no zone or service-boundary policy contracts.

Implication: `HR9-13-1` and WP-005 remain blocked for any networking-dependent downstream work.

Recommendation: `W16-D17-A`, because it adopts the controlled logical architecture without selecting infrastructure and keeps every external/Agent path deny-by-default.

### 7.4 Residency/sovereignty and exception boundary

- Governed identity/security data is not sent to an external destination merely because a route exists.
- An external destination must independently satisfy classification, purpose, minimization, retention, provider eligibility, residency and sovereignty requirements.
- Unapproved cross-border transfer is denied. Absence of verifiable residency or cross-border authority is not treated as a low-risk default.
- A residency/sovereignty exception cannot relax a security control that NCIE-009 does not permit it to relax and cannot serve as provider selection.
- The institutional residency/sovereignty exception authority remains unassigned under the relevant NCIE-008 gate; no exception can be activated.
- VPF contributes a behavioral Africa-residency and deny-by-default cross-border lens, but this pack does not claim technical enforcement or replace an NCIE Human decision.

### 7.5 Items that remain institutionally unassigned

- Network Security Owner, accountable zone-policy authority and exception-granting authority.
- Actual trust zones, networks, addresses, service registrations, workloads and routes.
- Destination/service allow-lists and any external/provider endpoint.
- Agent egress eligibility, Task Contract destinations and connector credentials.
- Residency locations, cross-border permits and sovereignty exceptions.
- Firewall, service mesh, gateway, cloud/network platform, DNS, proxy and monitoring product.

## 8. Consolidated Project Owner decision

The Project Owner selected the recommended Option A for all three decisions:

| Decision | Selected option | Permitted only after a separate implementation release | Remains unavailable/unassigned |
|---|---|---|---|
| W16-D15 / HR9-11-1 | A | Secret/key reference, lifecycle-authority and exception-policy contracts | Holders, exceptions, products and all secret/key material |
| W16-D16 / HR9-12-1 | A | Protection-scope, hierarchy, separation and agility contracts | Algorithms, lengths, profiles, products and cryptographic execution |
| W16-D17 / HR9-13-1 | A | Logical seven-zone/service-boundary and deny-by-default egress contracts | Authorities, destinations, routes, infrastructure and network activation |

These selections preserve WP-001 current authorization, WP-002 fail-closed risk posture, WP-003 identity/session separation and WP-004 zero-grant/non-expansion controls. They define architecture only and do not authorize WP-005 implementation or activate any capability.

## 9. Exact proposed WP-005 implementation boundary

Only after W16-D15 through W16-D17 are explicitly recorded and a separate implementation release is issued, WP-005 may be limited to:

1. Opaque secret/key/certificate reference types that reject literal or protected material.
2. Provider-neutral secret/key lifecycle-event types for request, issuance reference, access reference, rotation reference, expiry and revocation—without executing an event.
3. Abstract custodial, policy, exception-review and assurance interfaces, all operationally unassigned and denying.
4. A prohibited-surface/exception-policy evaluator with no path to waive the absolute exposure or plaintext-fallback prohibitions.
5. Provider-neutral protection-scope, key-hierarchy, sensitivity-separation and crypto-agility policy contracts without algorithms or products.
6. Fail-closed evaluation for absent, stale, expired, revoked, conflicting or out-of-scope cryptographic policy.
7. Logical zone, service-boundary and egress-policy contracts using only the exact Human-approved taxonomy.
8. Agent/external egress evaluation as the intersection of sandbox, Task Contract, identity, destination, classification, purpose, retention, residency and current authorization ceilings.
9. Provider-neutral exception request/decision metadata with unassigned granting authority and deny-by-default behavior.
10. Minimized, non-authoritative security-condition signals without secret material, network addresses, protected data, persistent audit or institutional Evidence claims.
11. Deterministic local unit/contract and negative-path tests for exposure, custody/consumer confusion, separation failure, missing crypto policy, unknown zone, forbidden crossing, Agent arbitrary egress, exception bypass and residency uncertainty.
12. Traceability and local implementation evidence distinguishing contract validation from operational security enforcement.

The controlled reference configuration must contain no secret/key material, no operational custodian/authority, no algorithm/profile, no destination allow-list entry, no network route and no exception grant.

## 10. Explicit exclusions

- Secret manager, vault, KMS, HSM, CA, PKI/certificate system or cryptographic product.
- Algorithm, key length, cipher/mode/suite, signature scheme, certificate profile or numeric rotation/lifetime policy.
- Live secret, key, certificate, token, credential, private material or protected production value.
- Secret/key issuance, generation, import, storage, delivery, access, rotation, renewal, revocation or recovery execution.
- Institutional custodian, owner, approver, reviewer, assurance or exception-authority assignment.
- Firewall, service mesh, proxy, API/model/tool gateway product, DNS, load balancer, cloud/VPC/VNet, subnet, cluster or network platform.
- Live zone, address, service route, allow-list, ingress, egress, external destination, provider or connector.
- Agent internet access, model/provider activation, Tool invocation or external-system call.
- Persistent governance, policy, secret, key, network, audit or Evidence store.
- Governed production data, cross-border transfer, infrastructure, deployment, accreditation, acceptance or go-live.
- WP-006 or any later WBS-16 capability.

## 11. Stop conditions

Preparation and any later authorized implementation must stop for Human direction if:

1. any of W16-D15 through W16-D17 lacks an explicit recorded selection;
2. an institutional custodian, owner, approver, reviewer, exception authority or operational holder would need to be invented;
3. a secret, key, certificate, token, credential or protected value would need to be created, read, copied, stored, logged or transmitted;
4. an algorithm, key length, cipher/profile, numeric duration, rotation interval, lease, threshold or cadence would need to be guessed;
5. a product, provider, CA, vault, KMS/HSM, firewall, service mesh, gateway, cloud/network platform or infrastructure would enter scope;
6. a zone, destination, route, allow-list entry, Agent/model/tool egress path or external connection would be populated or activated;
7. an exception would weaken a prohibited exposure surface, plaintext-fallback rule, current authorization, segregation of duties, non-expansion or Human-primary boundary;
8. classification, purpose, consent, minimization, retention, residency, sovereignty, provider eligibility or current authority is missing, conflicting or unverifiable;
9. governed production data or cross-border transfer would occur;
10. the work would claim encryption, secret custody, network enforcement, institutional Evidence, independent verification, accreditation, acceptance, deployment or go-live;
11. WP-006 or later work would enter scope; or
12. a controlled source or predecessor decision materially changes.

The fallback state is `DENY / NO CAPABILITY`, never a permissive default.

## 12. Proposed completion criteria

WP-005 may be reported locally `WORK COMPLETE` only if all of the following are evidenced after a separate implementation authorization:

1. Exact Human selections for W16-D15 through W16-D17 and a separate implementation release are recorded without expansion.
2. All reference registries for custodians, exception authorities, algorithms/profiles, destinations and network grants are empty.
3. No secret/key/certificate value or credential material exists in source, tests, fixtures, logs, signals or evidence.
4. Opaque reference validation rejects literal/protected material without echoing it.
5. Consumer identity and custodian authority remain distinct.
6. Custody, policy approval, exception review and assurance interfaces are separated and unassigned; all operational actions deny.
7. Absolute prohibited-surface and no-plaintext-fallback rules cannot be waived.
8. Exception contracts require exact scope, purpose, compensating controls, current non-requester authority, expiry, revocation and fresh renewal; unassigned authority denies.
9. At-rest, in-transit and sensitive-field obligations remain distinct from authorization and cannot claim cryptographic execution.
10. Root/intermediate/data-encryption hierarchy and sensitivity/domain/environment separation are represented without algorithms, keys or products.
11. Missing, stale, expired, revoked, conflicting or unknown cryptographic policy fails closed.
12. The selected logical zones and source-defined service boundaries are represented without infrastructure identifiers.
13. Unknown zones, forbidden crossings and direct AI/Agent-to-data or arbitrary endpoint paths deny.
14. Agent/external egress is no broader than the intersection of every approved ceiling and defaults to no egress.
15. Missing classification, purpose, retention, residency/sovereignty, destination eligibility, current authorization or exception authority denies.
16. Signals are minimized, non-authoritative and contain no secret material, protected data or live network identifiers.
17. Negative tests cover secret exposure, custody/consumer confusion, separation failure, exception bypass, plaintext fallback, policy absence, zone crossing, Agent egress expansion and residency uncertainty.
18. Strict typing, lint, formatting, compilation, cumulative regression and reproducibility checks pass in the approved local environment.
19. No excluded technology, provider, credential, persistent store, external service, infrastructure, governed data or deployment is introduced.
20. Evidence clearly separates local contract testing from NCIE-016 verification, operational enforcement, accreditation and acceptance.

The maximum permissible status would be:

`WBS-16-WP-005 — WORK COMPLETE / LOCALLY VERIFIED; ZERO LIVE SECRETS, KEYS, NETWORK GRANTS OR EXCEPTIONS; OPERATIONAL POLICY, INDEPENDENT SECURITY VERIFICATION, ACCREDITATION AND ACCEPTANCE PENDING`

## 13. Project Owner decision record

- W16-D15: `A` — approve provider-neutral secrets/key custody, lifecycle-authority and exception-policy contracts; operational holders, exceptions, products and all secret/key material remain unassigned.
- W16-D16: `A` — approve provider-neutral cryptographic protection, key-hierarchy, separation and crypto-agility contracts; algorithms, key lengths, profiles, products and cryptographic execution remain unassigned.
- W16-D17: `A` — approve the seven logical Zero-Trust zone labels, source-defined service boundaries and provider-neutral, deny-by-default egress contracts; authorities, destinations, routes, infrastructure and network activation remain unassigned.
- Decision authority: `Project Owner / Clive Ebo Barton-Odro`
- Decision date: `2026-09-23`
- Evidence reference: `NCIE-WBS16-OWNER-DECISION-2026-09-23-020`
- Evidence type: `Self-Authorized Project Owner Decision`
- Separate WP-005 implementation authorization: `GRANTED UNDER NCIE-WBS16-OWNER-DECISION-2026-09-23-021`
- WP-005 source-control release authorization: `GRANTED UNDER NCIE-WBS16-OWNER-DECISION-2026-09-23-022`

Conditions:

1. `UNASSIGNED / UNSPECIFIED = DENY / NO CAPABILITY`.
2. No operational secret/key custodian, policy approver, exception authority, network authority or operational holder is assigned.
3. No secret, key, certificate, token, credential or protected production value may be created, stored, processed or exposed.
4. No cryptographic algorithm, key length, cipher/profile, certificate profile, KMS/HSM, CA or cryptographic product is selected.
5. No network route, allow-list entry, destination, external connection, Agent internet access or infrastructure is activated.
6. Governed data must not cross an external or cross-border boundary without separately evidenced classification, purpose, minimization, retention, residency/sovereignty, provider eligibility and Human authorization.
7. This decision defines architecture only and does not authorize WP-005 implementation.

## 14. Source traceability

- NCIE-009 Chapter 11, Table 18 and `HR9-11-1` — secrets/key lifecycle, custody, exception authority and SoD.
- NCIE-009 Chapter 12, Table 19 and `HR9-12-1` — protection scopes, sensitive-field controls, separation and crypto agility.
- NCIE-009 Chapter 13, Table 20 and `HR9-13-1` — Zero Trust network doctrine, Agent/external egress and exception authority.
- NCIE-004 Chapters 3, 18, 20, 23–25 and 34 — proposed product defaults, seven-zone topology, gateway boundaries, secret references and Agent egress.
- NCIE-007 Chapters 7–8 and Agent runtime boundaries — classification/residency eligibility and no arbitrary provider fallback.
- NCIE-008 Chapters 4–7, 20 and 21 — decision rights, RACI/SoD, policy ownership, sovereignty and exception lifecycle.
- NCIE-002 encryption, segmentation and Zero-Trust mandates as cited by NCIE-004/009.
- NCIE-003 classification, protected-field and fail-closed key-management requirements as cited by NCIE-004/009.
- `implementation/decisions/NCIE_WBS16_WP002_HUMAN_REVIEW_DECISION_PACK.md` — approved conservative development risk posture.
- `implementation/decisions/NCIE_WBS16_WP004_HUMAN_REVIEW_DECISION_PACK.md` — zero-grant, non-expansion and unassigned-authority predecessor controls.
- `implementation/WBS16_REMAINING_SCOPE_AND_COMPLETION_CRITERIA.md`.

## 15. VPF boundary and postflight

VPF was applied behaviorally to Human-primary authority, least privilege, explainability, provenance, minimization, African data residency and deny-by-default cross-border transfer. It reinforces the recommendation to leave operational authorities, products, algorithms, destinations and exceptions unassigned and to deny unverifiable external transfer.

No VPF runtime, validator, signature, checksum, certificate, ledger, PADCA/Omnis service, residency enforcement, quarantine action, scheduled audit or production control is claimed to have executed.
