"""NCIE-007 content batch: Chapters 7-12 (classification/purpose/task-aware
routing, provider adapters, model selection/versioning, fallback/failover,
specialized agent architecture & Dynamic Agent Synthesis, agent capability
registry & Agent Factory)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 7 — Classification-, Purpose- & Task-Aware Model Routing
# ---------------------------------------------------------------------------
BLOCKS[7] = [
    ("upstream", [
        ("NCIE-003", "Ch.31", "Classification/residency/retention taxonomy is canonical; this chapter applies it to model eligibility."),
    ]),
    ("h2", "7.1 Eligibility Dimensions"),
    ("table",
     ["Dimension", "Evaluated Before Routing"],
     [
        ["Classification", "Model's classification ceiling (Ch.6) must meet or exceed the task's classification."],
        ["Purpose", "Model's approved purpose scope must cover the requested task type."],
        ["Task", "Model's declared capabilities must cover the specific task (e.g., structured output, tool use)."],
        ["Residency", "Model deployment's data-residency scope must satisfy the request's residency requirement."],
        ["Provider Eligibility", "Provider must hold current approved status (Ch.8)."],
        ["Retention", "Provider-side retention behavior must satisfy the request's retention requirement."],
        ["Model Capability", "Declared model capability must be sufficient for the task profile."],
        ["Tool Requirements", "Where the task requires tool-calling, the model must support the governed tool-calling contract (Ch.19)."],
        ["Availability", "Evaluated last — availability alone never substitutes for the preceding eligibility checks."],
    ],
     "Model routing eligibility dimensions, evaluated in order — availability is never allowed to promote an ineligible model."),
    ("h2", "7.2 Routing Result"),
    ("p",
     "A routing request yields an eligible route, or an explicit degraded/no-route state (Ch.10). "
     "MODEL AVAILABILITY ≠ MODEL ELIGIBILITY (front matter §0.3) — an available but ineligible model "
     "is never selected merely because it responds."),
    ("trace", "NCIE-003 Ch.31."),
]

# ---------------------------------------------------------------------------
# Chapter 8 — Provider Adapters & Provider Neutrality
# ---------------------------------------------------------------------------
BLOCKS[8] = [
    ("upstream", [
        ("NCIE-004", "Ch.18", "Provider neutrality is an engineering-governed principle; this chapter specifies the orchestration-facing adapter boundary."),
    ]),
    ("h2", "8.1 Adapter Isolation"),
    ("p",
     "Provider-specific APIs, request/response formats and proprietary tool-calling conventions are "
     "isolated behind replaceable adapters. No provider-specific capability becomes a hidden "
     "architectural dependency that undermines ARGUS continuity, Agent Definition portability, VPF "
     "sovereignty, Memory sovereignty or Tool governance (Ch.36 sovereignty acceptance tests)."),
    ("h2", "8.2 Provider Outage Behavior"),
    ("p",
     "A provider outage never causes classification downgrade, residency bypass, retention-policy "
     "bypass or use of an unapproved provider. Where no eligible route remains, the Gateway returns a "
     "degraded/no-route state (Ch.10) rather than silently relaxing eligibility."),
    ("trace", "NCIE-004 Ch.18."),
]

# ---------------------------------------------------------------------------
# Chapter 9 — Model Selection, Versioning & Reproducibility
# ---------------------------------------------------------------------------
BLOCKS[9] = [
    ("upstream", [
        ("NCIE-003", "Ch.28", "AI provenance/model-route semantics are canonical; this chapter specifies what must be preserved at selection time."),
    ]),
    ("h2", "9.1 Persisted Selection Context"),
    ("p", "For consequential persisted output, the Model Gateway persists sufficient context to identify:"),
    ("bullets", [
        "Model Route and Deployment.",
        "Model Version/Identifier, where required by policy.",
        "Applicable Routing Policy Version.",
        "Invocation Time.",
    ]),
    ("p",
     "Private chain-of-thought is never persisted. A later model-version change is recorded as a new "
     "route on new outputs; historical outputs retain their original route reference (Ch.33 §33.4 "
     "model-change acceptance behavior)."),
    ("trace", "NCIE-003 Ch.28."),
]

# ---------------------------------------------------------------------------
# Chapter 10 — Fallback, Failover & Degraded AI Operation
# ---------------------------------------------------------------------------
BLOCKS[10] = [
    ("upstream", [
        ("NCIE-002", "Ch.24", "AI safety and service-boundary requirements govern degraded operation; this chapter specifies fallback behavior."),
    ]),
    ("h2", "10.1 Degraded-Mode Behavior"),
    ("table",
     ["Condition", "Behavior"],
     [
        ["No eligible model for a request", "Return degraded/no-route state; never substitute an ineligible model"],
        ["Preferred eligible model unavailable", "Fall back only to another currently eligible model; ineligible models are never used as fallback"],
        ["All routes for a classification tier unavailable", "Deterministic NCIE functions continue independently — AI orchestration failure never disables non-AI regulatory functions (Ch.34 §34.3)"],
     ],
     "Fallback/failover behavior — eligibility constraints are never relaxed to preserve availability."),
    ("h2", "10.2 Model Suspension Propagation"),
    ("p",
     "A model/deployment may become temporarily ineligible even if technically available (e.g., "
     "suspected compromise, Ch.33 §33.5). Routing honors current Registry state immediately; a "
     "suspended model is never used through a stale cached eligibility result."),
    ("trace", "NCIE-002 Ch.24."),
]

# ---------------------------------------------------------------------------
# Chapter 11 — Specialized Agent Architecture & Dynamic Agent Synthesis
# ---------------------------------------------------------------------------
BLOCKS[11] = [
    ("upstream", [
        ("NCIE-007-S01", "§3-5", "Agent Definition Package structure and the DRAFT→ACTIVE_REUSABLE lifecycle are the normative supplement baseline this chapter implements in full."),
        ("NCIE-005", "Ch.4", "ARGUS may initiate bounded synthesis; ARGUS never grants an agent new institutional authority."),
    ]),
    ("h2", "11.1 Two Agent Kinds"),
    ("p",
     "Specialized agents are either Registered Reusable Agents (approved for repeated institutional "
     "use, Ch.12) or Ephemeral Synthesized Agents (instantiated from a validated Agent Definition "
     "Package for one bounded task, expiring by policy unless promoted). EPHEMERAL AGENT ≠ REGISTERED "
     "INSTITUTIONAL AGENT (front matter §0.3) — neither kind is an institutional decision maker."),
    ("h2", "11.2 Dynamic Agent Synthesis Flow"),
    ("flow",
     [
        "Task need identified — existing registered/eligible agent suitability check",
        "No adequate existing agent — ARGUS requests synthesis; Agent Definition Package generated from approved primitives only (Ch.3 §3.2)",
        "VPF Gate A — Agent Envelope Validation (§11.5)",
        "Security/policy validation and sandbox evaluation (Ch.34 §34.4)",
        "Ephemeral Approval — agent activates only within its validated envelope and current authorization context",
        "Execution",
        "VPF Gate B — AI Output Validation (Ch.26 §26.4) before ARGUS presents a validated NCIE AI result",
        "Ephemeral agent expires per policy unless it becomes a Promotion Candidate (§11.7)",
     ],
     "Dynamic Agent Synthesis Flow — this capability must be fully implementable from NCIE-007 without returning to Codex for bespoke development of each bounded agent."),
    ("h2", "11.3 Existing-Agent Reuse Before Synthesis"),
    ("p",
     "ARGUS prefers or at least identifies existing registered-agent capability reuse before "
     "synthesizing a duplicate. Where no approved primitive can satisfy the task, ARGUS produces an "
     "ENGINEERING CHANGE CANDIDATE rather than fabricating the missing capability (§11.6)."),
    ("h2", "11.4 Agent Definition Package"),
    ("p", "The canonical logical structure for a synthesized Agent Definition Package, at minimum:"),
    ("bullets", [
        "Agent Definition ID; Purpose; Task Scope.",
        "Input Schema; Output Schema.",
        "Permitted Models; Permitted Tools; Permitted Data Classes.",
        "Context Scope; Authorization Envelope; Delegation Depth.",
        "Resource/Token/Time Budget; Network/Egress Policy; Persistence Policy.",
        "VPF Validation Profile; Evaluation Tests.",
        "Termination/Expiry Conditions; Provenance Requirements.",
    ]),
    ("p",
     "No physical database fields are invented beyond what is logically required; NCIE-014 specifies "
     "physical storage."),
    ("h2", "11.5 VPF Gate A — Agent Envelope Validation"),
    ("p",
     "Before an agent executes, Gate A validates its Purpose, Task Scope, Inputs/Outputs, Models, "
     "Tools, Data Classes, Context Scope, Authorization Envelope, Delegation Depth, Network/Egress, "
     "Persistence, Resource Budget, Termination Conditions and Policy Boundaries. Gate A and Gate B "
     "(Ch.26 §26.4) are never collapsed into one check."),
    ("h2", "11.6 Approved Primitives Only"),
    ("p",
     "Dynamic agents are composed only from approved/eligible Models, Tools, Context Services, "
     "Schemas, Policies, Execution Runtimes and Capability Primitives (Ch.3 §3.2). ARGUS shall not "
     "synthesize new permissions or infrastructure merely because a task requires them. A task "
     "requiring a capability outside approved primitives yields an ENGINEERING CHANGE CANDIDATE, not "
     "a fabricated one."),
    ("h2", "11.7 Ephemeral Agent Lifecycle"),
    ("flow",
     ["DRAFT", "SYNTHESIZED", "SANDBOXED", "VPF_VALIDATED", "EVALUATED", "EPHEMERAL_APPROVED", "ACTIVE_EPHEMERAL", "EXPIRED — with exceptional states REJECTED, SUSPENDED or TERMINATED available at any stage"],
     "Ephemeral Agent Lifecycle — state names may be normalized in implementation but semantics remain explicit."),
    ("h2", "11.8 Reusable-Agent Promotion"),
    ("p",
     "A repeatedly useful ephemeral agent may become a PROMOTION_CANDIDATE → HUMAN/GOVERNANCE REVIEW "
     "→ REGISTERED → ACTIVE_REUSABLE. ARGUS may recommend promotion; ARGUS shall not approve its own "
     "agent for permanent institutional registration (AGENT SYNTHESIS ≠ SELF-REGISTRATION, front "
     "matter §0.3)."),
    ("h2", "11.9 Current Authorization Envelope"),
    ("p",
     "Every synthesized agent executes under a current authorization envelope derived from the "
     "active governed principal/task context. It shall not obtain authority from Historical Memory, "
     "Prior Human Decision, ARGUS Recommendation, Agent Definition Text or another agent's claimed "
     "permission (REMEMBERED AUTHORIZATION ≠ CURRENT AUTHORIZATION; PRIOR HUMAN DECISION ≠ CURRENT "
     "ACTION AUTHORITY)."),
    ("review", [
        ("INSTITUTIONAL", "Approve the ephemeral-agent activation policy by task/risk class — whether ephemeral agents may activate automatically after Gate A plus security/evaluation checks, or require human approval per risk class."),
        ("INSTITUTIONAL", "Approve the promotion authority and criteria for converting an ephemeral agent into a registered reusable institutional agent."),
    ]),
    ("trace", "NCIE-007-S01 §3-5; NCIE-005 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 12 — Agent Capability Registry & Agent Factory
# ---------------------------------------------------------------------------
BLOCKS[12] = [
    ("upstream", [
        ("NCIE-007-S01", "§1, §7", "Codex builds and maintains the Agent Factory; ARGUS uses it. Promotion requires governed review and explicit registration authority."),
    ]),
    ("h2", "12.1 Agent Factory Boundary"),
    ("p",
     "CODEX BUILDS THE AGENT FACTORY; ARGUS USES THE AGENT FACTORY. Codex does not need to hand-code "
     "every future bounded task-specific agent once the Agent Factory exists. ARGUS does not become a "
     "general unrestricted software-development authority. Codex/engineering re-enters when a "
     "required capability exceeds the approved Agent Factory primitives or requires material "
     "production engineering change — a new Tool, Connector, Infrastructure, Security Primitive, "
     "Persistent Service or permanent generated-code integration."),
    ("h2", "12.2 Registry Distinctions"),
    ("table",
     ["Registry", "Governs"],
     [
        ["Agent Registry", "Reusable Agent Definitions, lifecycle state, promotion history — distinct from ephemeral run-scoped definitions."],
        ["Model Registry", "Eligible models/deployments (Ch.6) — distinct governance from Agent Registry."],
        ["Tool Registry", "Eligible tools (Ch.19) — distinct governance from Agent Registry."],
        ["VPF Profile Registry", "Eligible VPF validation profiles (Ch.26 §26.3) — distinct governance from Agent Registry."],
        ["Agent Pattern Registry", "Approved reusable synthesis patterns — distinct governance, and existing historical agent instances retain their original pattern reference when a pattern is later modified."],
     ],
     "Registry distinctions — shared storage implementation never collapses their governance semantics."),
    ("h2", "12.3 Recursive Synthesis Boundary"),
    ("p",
     "A synthesized agent shall not automatically receive Agent Factory access. SYNTHESIZED AGENT ≠ "
     "AGENT-FACTORY AUTHORITY (front matter §0.3). Default delegation depth for agent creation is "
     "ARGUS → Synthesized Agent, never ARGUS → Agent A → Agent B → Agent C. Unless Human Review "
     "explicitly changes it: RECURSIVE AGENT SYNTHESIS REMAINS DISABLED."),
    ("h2", "12.4 Registry Mutation Boundary"),
    ("p",
     "AI components — ARGUS, agents, the Agent Factory itself, VPF — cannot directly mutate governed "
     "Registry state outside authorized lifecycle workflows. Promotion to reusable registration "
     "considers Need, Evaluation, VPF History, Security, Ownership, Maintainability, Scope and Human/"
     "Governance Approval; repeated use or repeated VPF PASS alone never triggers automatic "
     "promotion."),
    ("review", [
        ("SECURITY", "Approve the Agent Factory resource, model, tool, data and network ceilings applied to every synthesized agent."),
        ("PROPOSED", "Recursive Agent Synthesis remains disabled by default pending any future explicit governed policy change, consistent with NCIE-007-S01 §8."),
    ]),
    ("trace", "NCIE-007-S01 §1, §7-8."),
]
