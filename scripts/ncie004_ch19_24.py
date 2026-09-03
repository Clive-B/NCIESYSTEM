"""NCIE-004 content batch: Chapters 19-24 (AI guardrails, agentic orchestration
& tool gateway, collaborative intelligence, memory, IAM, secrets/PKI)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 19 — AI Guardrails, Evaluation & Safety Engineering
# ---------------------------------------------------------------------------
BLOCKS[19] = [
    ("upstream", [
        ("NCIE-002", "Ch.24 §24.4-24.5", "Prompt-injection defense, secrets exclusion and collaborative-participation evaluation are mandatory before Participatory Mode production use."),
    ]),
    ("h2", "19.1 Guardrails and Evaluation Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Grounding controls", "Answers derived from authoritative tool results, not unexamined model output (NCIE-002 Ch.19 §19.3)", "Grounding Layer enforced in the Model Gateway response path (Ch.18)", "—", "MANDATE"],
        ["Injection defenses", "Ingested content (email, files) treated as data, never instructions (NCIE-002 Ch.24 §24.4)", "Input-classification filter tagging untrusted content before it reaches a prompt", "—", "MANDATE"],
        ["Evaluation harness", "Collaborative-specific evaluation before Participatory Mode production use (NCIE-002 Ch.24 §24.5)", "Offline eval suite (context tracking, attribution, thread separation, restraint) run per model/provider", "—", "MANDATE"],
        ["Red-team testing", "Adversarial testing for jailbreak, permission-pooling and privilege-escalation attempts", "Scheduled red-team exercises ahead of each model/provider approval (Ch.33 registry gate)", "—", "PROPOSED"],
        ["Regression gates", "A model/provider change cannot silently regress guardrail behaviour", "CI gate blocking Model Registry promotion on failed evaluation suite (Ch.28-29)", "—", "PROPOSED"],
        ["Abstention", "ARGUS states a limitation rather than fabricating an answer when ungrounded (NCIE-002 Ch.19 §19.8)", "Grounding Layer returns an explicit \"cannot verify\" response class", "—", "MANDATE"],
    ],
     "AI guardrails and evaluation technology decisions.", 4),
    ("h2", "19.2 Engineering Notes"),
    ("bullets", [
        "Over-participation and under-participation are monitored as distinct failure modes (NCIE-002 Ch.24 §24.5), each with its own alert in Ch.26 observability.",
        "No guardrail check may be bypassed for latency reasons; a guardrail-check failure blocks the response rather than degrading silently.",
    ]),
    ("review", [
        "Confirm acceptable red-team testing cadence and who reviews red-team findings before model/provider approval.",
    ]),
    ("trace", "NCIE-002 Ch.19, Ch.24."),
]

# ---------------------------------------------------------------------------
# Chapter 20 — Agentic Orchestration & Tool Gateway Technology
# ---------------------------------------------------------------------------
BLOCKS[20] = [
    ("upstream", [
        ("NCIE-002", "Ch.21", "Room-to-workflow automation requests remain distinct from execution authority; AI suggestion never becomes execution."),
        ("NCIE-003", "Ch.20 §20.5", "Every Tool Invocation must store its authorization-check result at invocation time, not just a success flag."),
    ]),
    ("h2", "20.1 Governed Agentic Orchestration"),
    ("p",
     "Specialized agents may perform bounded analytical/tool tasks. Delegation to an agent never "
     "expands the delegating identity's authorization, data access, tool access or decision "
     "authority — an agent is not described or engineered as an autonomous institutional decision "
     "maker anywhere in this stack."),
    ("h2", "20.2 Tool Gateway"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Tool Registry", "Every tool explicitly registered with typed input/output before ARGUS/agents may call it", "Internal Tool Registry service, versioned (Ch.33)", "—", "MANDATE"],
        ["Tool Gateway enforcement", "Authorization, classification, purpose and target validation on every invocation (NCIE-002 Ch.19 §19.7)", "Gateway middleware enforcing the full checklist in §20.3", "—", "MANDATE"],
        ["Agent orchestrator", "Bounded task delegation without institutional authority expansion", "Workflow-engine-hosted agent tasks (Ch.10), not a separate autonomous runtime", "Dedicated agent-orchestration framework if task complexity later justifies it", "PROPOSED"],
        ["Sandboxing", "Agent-executed code/tools isolated from unrelated production workloads", "Per-invocation isolated execution context (container/process, Ch.4)", "—", "PROPOSED"],
        ["Execution receipts", "Idempotent, auditable record of what a tool actually did", "Receipt written to Ch.27 (Audit) on every tool execution", "—", "MANDATE"],
    ],
     "Agentic orchestration and Tool Gateway technology decisions.", 4),
    ("rel",
     [
        ("ARGUS / Specialized Agent", "requests tool via", "Tool Gateway"),
        ("Tool Gateway", "validates against", "Tool Registry (typed input/output, registered tools only)"),
        ("Tool Gateway", "checks", "Authorization + Classification + Purpose + Target (§20.3 checklist)"),
        ("Tool Gateway", "requires Human Approval for", "side-effecting tool calls (Ch.10)"),
        ("Tool Gateway", "executes within", "Sandboxed context (Ch.4 isolation)"),
        ("Tool Gateway", "writes", "Execution Receipt to Audit (Ch.27)"),
     ],
     "Tool Gateway / Agentic Orchestration topology: every tool call is registered, checked, approved where required, sandboxed and receipted."),
    ("h3", "20.3 Tool Gateway Enforcement Checklist"),
    ("bullets", [
        "Tool registration (no ad hoc/unregistered tool calls).",
        "Typed input and typed output validation.",
        "Authorization check against the invoking identity's effective scope (NCIE-003 Ch.26).",
        "Classification check against the tool's declared data sensitivity.",
        "Purpose validation (is this tool call consistent with the current task/room context).",
        "Target validation (is the referenced object one the identity may act on).",
        "Human approval where the tool has a side effect requiring it (Ch.10).",
        "Idempotency key on every side-effecting call.",
        "Execution receipt and audit event on completion.",
    ]),
    ("review", [
        "Confirm which tool categories require mandatory human approval versus autonomous bounded execution.",
    ]),
    ("trace", "NCIE-002 Ch.19, Ch.21; NCIE-003 Ch.20, Ch.23."),
]

# ---------------------------------------------------------------------------
# Chapter 21 — Collaborative Intelligence & Real-Time Collaboration Stack
# ---------------------------------------------------------------------------
BLOCKS[21] = [
    ("upstream", [
        ("NCIE-002", "Ch.20", "Human ↔ Human ↔ ARGUS collaboration requires persistent structured reasoning state, not merely a shared chat transcript."),
        ("NCIE-003", "Ch.21", "Room, Thread, Hypothesis, Contradiction, Evidence Gap, Task, Human Judgment, Decision Point, ARGUS Intervention, Consensus, Dissent and Room Snapshot are canonical entities the stack must persist."),
    ]),
    ("h2", "21.1 Collaboration Stack — Not Chat Infrastructure"),
    ("p",
     "Real-time messaging transport is only one component. The stack must persist the full "
     "structured-object set above as first-class, queryable records — a message log alone does not "
     "satisfy NCIE-003 Ch.21."),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Realtime transport", "Low-latency bidirectional updates for Room presence/events", "WebSocket gateway (e.g. Socket.IO/native WS) behind the API gateway (Ch.8)", "—", "PROPOSED"],
        ["Presence", "Participant join/leave/typing state per Room (NCIE-003 Ch.21 §21.3)", "Presence service backed by cache (Ch.17)", "—", "PROPOSED"],
        ["Collaborative editing", "Concurrent edits to shared reasoning objects without silent data loss (NCIE-002 Ch.20 §20.16)", "CRDT-based or operational-transform sync for shared documents/boards", "—", "PROPOSED"],
        ["Whiteboard/evidence board", "Shared references to authoritative Evidence, never copied authority (NCIE-002 Ch.20 §20.4)", "Board component referencing Evidence Objects by ID only (Ch.13)", "—", "MANDATE"],
        ["Room events", "Material events (participation-mode change, promotion) individually audited (NCIE-003 Ch.27)", "Room event bus on top of Ch.9's event broker", "—", "MANDATE"],
        ["ARGUS hooks", "Participation-mode-aware proactive contribution (NCIE-002 Ch.19 §19.4)", "Room event subscription feeding the Proactive Contribution Controller (Ch.18/20)", "—", "MANDATE"],
    ],
     "Collaborative Intelligence technology decisions.", 4),
    ("h2", "21.2 Engineering Notes"),
    ("bullets", [
        "Every structured object (Hypothesis, Contradiction, etc.) is stored in the transactional store (Ch.11) with the same provenance/classification discipline as any other canonical entity — not a lighter-weight \"collaboration database.\"",
        "Room Snapshot generation (NCIE-003 Ch.21 §21.9) reuses Ch.12's historical-query capability rather than a bespoke mechanism.",
    ]),
    ("trace", "NCIE-002 Ch.19, Ch.20; NCIE-003 Ch.20-21, Ch.27."),
]

# ---------------------------------------------------------------------------
# Chapter 22 — Memory, Knowledge & Context Engineering Stack
# ---------------------------------------------------------------------------
BLOCKS[22] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.2", "Private/Shared/Institutional memory tiers must never be an LLM conversation-history feature."),
        ("NCIE-003", "Ch.22", "Memory ≠ Current Truth; Institutional Knowledge ≠ Rule; promotion requires recorded human review."),
    ]),
    ("h2", "22.1 Memory Engineering Boundary"),
    ("p",
     "Memory is engineered as persistent, structured, versioned, authorization-aware, temporally "
     "aware, model-independent and reconcilable with current authoritative state — never as a "
     "model-provider conversation-history buffer that disappears on model/provider substitution."),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Memory service", "Model-independence is mandated verbatim (NCIE-003 Ch.22 §22.3 / NCIE-002 Ch.20 §20.2); the storage location is not — this row proposes the transactional store over a provider-side feature", "Service backed by the transactional store (Ch.11), not provider-side memory features", "—", "PROPOSED"],
        ["Knowledge repository", "Institutional Knowledge's required attributes (Applicability Scope, Review State, Knowledge Version) are mandated (NCIE-003 Ch.22); its storage location is an implementation choice", "Same transactional store, dedicated schema (Ch.11)", "—", "PROPOSED"],
        ["Dependency/context graph", "Reconciliation of memory against current authoritative state (NCIE-003 Ch.22 §22.7)", "Reconciliation job reusing Ch.15's graph technology where relational joins are insufficient", "—", "PROPOSED"],
        ["Snapshots", "Room/session Snapshot capturing state for cross-session continuity is mandated (NCIE-003 Ch.21 §21.9); reusing Ch.12's query layer specifically is an implementation choice", "Reuses Ch.12's historical/bitemporal query layer", "—", "PROPOSED"],
        ["Retrieval", "Authorization-filtered retrieval, including any semantic/vector retrieval (Ch.16)", "Retrieval layer enforcing Ch.16's classification-aware filtering", "—", "MANDATE"],
    ],
     "Memory and knowledge engineering technology decisions.", 4),
    ("review", [
        "Confirm memory retention periods by Memory Class with NCA (already an open item at NCIE-003 Ch.22 §22-review)."]),
    ("trace", "NCIE-002 Ch.20 §20.2, §20.12; NCIE-003 Ch.22."),
]

# ---------------------------------------------------------------------------
# Chapter 23 — Identity, Authentication & Access-Control Technology
# ---------------------------------------------------------------------------
BLOCKS[23] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Zero-trust, four-layer authorization (role/object/field/action) and distinct human/service/workflow/ARGUS identity classes are architectural mandates."),
        ("NCIE-003", "Ch.26", "Effective-dated permissions and delegation must be queryable at any past point in time for decision-time reconstruction."),
    ]),
    ("h2", "23.1 Identity and Access-Control Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["IdP/SSO", "SAML/OIDC-capable, MFA-ready, integrates NCA's existing directory if one exists", "Keycloak", "NCA-existing IdP if one is already mandated", "INSTITUTIONAL"],
        ["MFA", "Mandatory for Administrator, Investigator and regulatory validation actions (NCIE-002 Ch.4 §4.5)", "TOTP authenticator app; SMS fallback disabled by default given SIM-fraud relevance", "—", "PROPOSED"],
        ["RBAC/ABAC/PBAC", "Role plus contextual domain/object/field/action policy (NCIE-002 Ch.4 §4.3)", "Policy engine (e.g. OPA) fronting the four-layer authorization model", "—", "PROPOSED"],
        ["Workload identity", "Distinct machine identity for services/workflows/ARGUS (NCIE-002 Ch.4 §4.2)", "SPIFFE/SPIRE-style workload identity or IdP-issued service accounts", "—", "PROPOSED"],
        ["Privileged access management (PAM)", "Break-glass access logged, time-bounded and justified is mandated verbatim (NCIE-002 Ch.26 §26.4); a dedicated PAM module is one way to implement it, not the only one", "PAM module on top of the IdP with mandatory justification capture", "—", "PROPOSED"],
        ["Federation", "Single sign-on across all NCIE services and any existing NCA systems", "IdP-federated SSO across the service mesh (Ch.8)", "—", "PROPOSED"],
    ],
     "Identity, authentication and access-control technology decisions.", 4),
    ("rel",
     [
        ("Human User", "authenticates via", "IdP/SSO (MFA-enforced)"),
        ("Service/Workflow/ARGUS", "authenticates via", "Workload Identity (distinct credential lifecycle)"),
        ("Authorization Service (Ch.8 gateway + service boundary)", "evaluates", "Role → Object → Field → Action policy"),
        ("Trust Zones (Ch.3)", "bound by", "Network segmentation matching identity class"),
    ],
     "Security/trust-zone topology: identity classes and their authorization path across trust zones."),
    ("review", [
        "Confirm NCA's existing enterprise identity provider and role model before selecting/standing up a new IdP.",
        "Confirm step-up/MFA and break-glass policy requirements per role.",
    ]),
    ("trace", "NCIE-002 Ch.4, Ch.26; NCIE-003 Ch.26."),
]

# ---------------------------------------------------------------------------
# Chapter 24 — Secrets, Keys, Certificates & Cryptographic Services
# ---------------------------------------------------------------------------
BLOCKS[24] = [
    ("upstream", [
        ("NCIE-002", "Ch.26 §26.7", "Encryption at rest/in transit is mandatory for protected/sensitive tiers; keys are managed centrally, never embedded in application code."),
        ("NCIE-003", "Ch.36", "Encryption and masking are distinct controls; key management failure must fail closed, never fall back to an unencrypted path."),
    ]),
    ("h2", "24.1 Secrets, Keys and Cryptographic Services"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Secrets vault", "Runtime secret injection by reference; never in source control or CI logs (NCIE-002 Ch.29 §29.6)", "HashiCorp Vault", "Cloud-native secrets manager if hosting model requires it", "PROPOSED"],
        ["KMS/HSM", "Centralised key management for protected/sensitive-tier encryption (NCIE-002 Ch.26 §26.7)", "Vault Transit engine or dedicated HSM where sovereignty/compliance requires hardware-backed keys", "—", "SECURITY"],
        ["PKI / certificate automation", "Automated issuance/rotation for service-to-service TLS", "cert-manager (Kubernetes-native) with an internal or NCA-approved CA", "—", "PROPOSED"],
        ["Rotation", "Scheduled, auditable, non-manual-only rotation is mandated as a capability; automating it via the specific vault/cert-manager tooling named in §24.1 is this document's proposed mechanism, not an upstream mandate", "Automated rotation policies in the vault/cert-manager", "—", "PROPOSED"],
        ["Encryption/signing", "Field-level encryption for protected identifiers is mandated verbatim (NCIE-003 Ch.14 §14.6); envelope encryption via KMS-issued keys is one implementation of it", "Application-layer envelope encryption using KMS-issued data keys", "—", "PROPOSED"],
    ],
     "Secrets, keys, certificates and cryptographic services decisions.", 4),
    ("h2", "24.2 Engineering Notes"),
    ("bullets", [
        "A KMS/HSM outage fails closed for protected-tier decryption operations — no application falls back to an unencrypted or locally-cached-key path (NCIE-003 Ch.36 §36.6).",
        "Secrets are referenced by name/path in configuration, never by literal value, across every chapter's technology stack.",
    ]),
    ("review", [
        "Confirm encryption/key-management standards and whether hardware-backed HSM is required by NCA policy versus a software-based KMS.",
    ]),
    ("trace", "NCIE-002 Ch.26, Ch.29 §29.6; NCIE-003 Ch.14 §14.6, Ch.36."),
]
