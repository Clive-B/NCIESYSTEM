"""NCIE-007 content batch: Chapters 31-34 (observability/telemetry,
evaluation/regression/adversarial testing, model & agent lifecycle
governance, security/isolation/supply-chain boundaries)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 31 — Observability, Telemetry & AI Operations
# ---------------------------------------------------------------------------
BLOCKS[31] = [
    ("upstream", [
        ("NCIE-006", "Ch.31 §31.3", "Technical-vs-governance observability separation is canonical; this chapter applies it to orchestration."),
    ]),
    ("h2", "31.1 Separate Operational Visibility"),
    ("p",
     "Separate operational visibility exists for the Model Gateway, Agent Factory, Agent Runtime, "
     "Tool Gateway, VPF, the Registries (Ch.6, Ch.12 §12.2) and ARGUS. Route/agent/tool metrics, "
     "latency, token/cost, policy denials, error taxonomy and distributed trace are captured per "
     "component, not collapsed into one undifferentiated stream."),
    ("h2", "31.2 Telemetry Privacy"),
    ("p",
     "Telemetry does not unnecessarily expose Prompts, Evidence, Protected Identity, Secrets, Precise "
     "Location or Sensitive Tool Results."),
    ("h2", "31.3 Telemetry Is Not Audit"),
    ("p",
     "TELEMETRY ≠ AUDIT. Operational telemetry (§31.1) is never mistaken for the authoritative "
     "provenance/audit architecture (Ch.27); the two serve different purposes and different retention "
     "rules."),
    ("trace", "NCIE-006 Ch.31 §31.3."),
]

# ---------------------------------------------------------------------------
# Chapter 32 — Evaluation, Regression & Adversarial Testing
# ---------------------------------------------------------------------------
BLOCKS[32] = [
    ("upstream", [
        ("NCIE-003", "Ch.38", "Dedicated temporal/lineage/authorization test categories are canonical; this chapter is their orchestration, VPF and Dynamic Agent application."),
    ]),
    ("h2", "32.1 Evaluation Programme Coverage"),
    ("p", "The evaluation programme includes at minimum:"),
    ("bullets", [
        "Positive Capability Tests; Negative Tests; Adversarial Tests; Regression.",
        "Model Replacement; Provider Replacement.",
        "Agent Factory; VPF; Dynamic Agents.",
        "Human-Primary Authority.",
    ]),
    ("h2", "32.2 Mandatory Acceptance Test Matrix"),
    ("p",
     "Every named test below is mandatory before NCIE-007 v1.0 delivery. Categories are condensed "
     "here per the token-conservation convention (front matter §0.2); the full test set traces "
     "one-to-one to the handover instruction's acceptance-test enumeration."),
    ("table",
     ["Category", "Representative Tests", "Must Demonstrate"],
     [
        ["VPF temporal/current-state", "Decision-Time contamination test; current-state reconciliation test", "Later Evidence/Knowledge/Rules never contaminate historical reconstruction; historical Memory used for a current claim without reconciliation yields QUALIFIED/HUMAN_REVIEW_REQUIRED, never PASS"],
        ["VPF authorization/disclosure", "Restricted-information leakage test; spoken-disclosure test", "VPF never reveals restricted information, never treats validation as disclosure authorization; VPF PASS ≠ spoken-disclosure authorization"],
        ["VPF non-authority", "Human-approval test; Knowledge/Finding/Decision promotion tests", "A VPF-PASS recommendation for a consequential action remains PROPOSED/AWAITING AUTHORIZATION; VPF-PASS artifacts cannot auto-promote to Institutional Knowledge, Finding or Decision"],
        ["Dynamic-agent scope/authorization", "Envelope-expansion test; cross-user reuse test; cross-context retrieval test", "Every unauthorized expansion beyond the validated envelope is denied; historical/cached authority is never inherited across users or contexts"],
        ["Dynamic-agent governance boundary", "Self-registration test; recursive-synthesis test; Gate B/Tool Gateway/Model Gateway/Registry bypass tests; VPF tampering test", "Self-registration denied; recursive synthesis denied by default; no bypass path exists for any gate or registry; VPF cannot be disabled, weakened or forged"],
        ["Dynamic-agent resource/lifecycle", "Resource-ceiling test; expiry test; reactivation test; promotion/promotion-rejection tests; duplicate-capability test; capability-gap test", "Enforced termination at budget limits; expired agents do not silently reactivate with stale authorization; only governed human/institutional authority approves registration; missing capability yields ENGINEERING CHANGE CANDIDATE, never fabrication"],
        ["Generated-code boundary", "Positive sandboxed-execution test; negative escape/exfiltration test", "If unapproved for initial release, no path silently activates it; if approved, sandbox/network/secret/dependency controls hold under adversarial attempt"],
        ["Compromise/suspension response", "Agent Factory, VPF validator, model and tool compromise tests; authorization-revocation test; Room-membership-change test", "New activity stops; dependents are identified; historical outputs remain traceable rather than deleted; revoked authorization is not honored through cached state"],
        ["Change management", "Evidence-correction, Knowledge-retraction, Rule-change, model-change, VPF-profile-change, Agent-Definition-change, Agent-Pattern-change, Tool-schema-change, Context-schema-change tests", "Dependent artifacts are identified and revalidated/flagged; historical artifacts retain their original reference; nothing is silently presented as current"],
        ["Fail-closed", "VPF/Gate A/Model Registry/Tool Registry/human-approval/audit/provenance unavailability tests", "A PASS or an executed consequential action never occurs solely because a mandatory control did not run"],
        ["Sovereignty", "Dynamic Agent, VPF, Institutional Memory, Agent Registry, Tool, human-authority sovereignty tests", "Each capability/doctrine survives replacement of the underlying model, provider, runtime or framework"],
        ["Human-Primary final scenario", "Full-chain adversarial scenario (Gate A/B pass, sandbox pass, agents agree, Knowledge supports the recommendation, tool available)", "None of those facts alone creates institutional execution authority absent required current human/institutional authorization — mandatory before delivery"],
     ],
     "Mandatory Acceptance Test Matrix — condensed per category; every listed capability/boundary must fail safely under its adversarial test."),
    ("h2", "32.3 Adversarial Envelope Tests"),
    ("p",
     "Agent-envelope tests specifically probe authority expansion, unsafe tool/data access, recursive "
     "synthesis and excessive resource scope. Output tests specifically verify that unvalidated or "
     "rejected results cannot be released as validated NCIE AI output."),
    ("review", [
        ("INSTITUTIONAL", "Confirm required test environments and masked/synthetic test data provisioning for the acceptance test matrix, consistent with NCIE-003 Ch.29 §29.3's convention."),
    ]),
    ("trace", "NCIE-003 Ch.38."),
]

# ---------------------------------------------------------------------------
# Chapter 33 — Model & Agent Lifecycle Governance
# ---------------------------------------------------------------------------
BLOCKS[33] = [
    ("upstream", [
        ("NCIE-007-S01", "§5", "The DRAFT→ACTIVE_REUSABLE lifecycle is the normative supplement baseline; this chapter integrates it with Model lifecycle governance."),
    ]),
    ("h2", "33.1 Unified Lifecycle Distinctions"),
    ("p", "State machines remain distinct across:"),
    ("bullets", [
        "Model; Agent Definition; Ephemeral Agent; Registered Agent.",
        "Agent Run; Task; Promotion Candidate.",
        "Tool Invocation; VPF Profile; VPF Validation; Human Approval.",
    ]),
    ("p", "Shared storage implementation never collapses these distinct governance semantics (Ch.12 §12.2)."),
    ("h2", "33.2 Model Lifecycle"),
    ("table",
     ["State", "Meaning"],
     [
        ["Candidate", "Proposed for evaluation; not yet eligible for routing."],
        ["Evaluated", "Evaluation complete; approval pending."],
        ["Approved / Active", "Eligible for routing per Ch.6-7."],
        ["Restricted", "Eligible only for a narrowed scope."],
        ["Suspended", "Temporarily ineligible even if technically available (Ch.10 §10.2)."],
        ["Deprecated / Retired", "No longer eligible for new routing; historical outputs remain traceable."],
     ],
     "Model lifecycle states."),
    ("h2", "33.3 Change-Management Discipline"),
    ("p",
     "A model, VPF profile, Agent Definition or Agent Pattern change produces a new version; existing "
     "historical instances retain their original version/profile/pattern reference while new "
     "instances use the current eligible version. A material Agent Definition modification triggers "
     "new-version creation plus applicable Evaluation, Gate A revalidation and Approval."),
    ("review", [
        ("INSTITUTIONAL", "Confirm model-approval authority and emergency model/agent suspension authority."),
    ]),
    ("trace", "NCIE-007-S01 §5."),
]

# ---------------------------------------------------------------------------
# Chapter 34 — Security, Isolation & Supply-Chain Boundaries
# ---------------------------------------------------------------------------
BLOCKS[34] = [
    ("upstream", [
        ("NCIE-007-S01", "§6", "Runtime and sandbox boundary requirements are the normative supplement baseline; this chapter details sandbox evaluation without duplicating NCIE-009."),
    ]),
    ("h2", "34.1 Runtime & Sandbox Boundary"),
    ("p",
     "Synthesized agents execute in bounded runtime isolation with explicit tool, data, model, "
     "network, context and resource ceilings. They cannot grant themselves new capabilities or bypass "
     "the Tool Gateway, Model Gateway, Memory/Context services, VPF or current authorization."),
    ("h2", "34.2 Sandbox Evaluation Requirements"),
    ("p", "Before ephemeral activation, evaluate the synthesized agent in isolation appropriate to its risk, testing:"),
    ("bullets", [
        "Schema Compliance; Tool Restrictions; Data-Class Restrictions.",
        "Network/Egress; Resource Limits; Termination.",
        "Prompt Injection; Authority Expansion; VPF Integration.",
    ]),
    ("p",
     "Sandbox success does not imply Registration, Institutional Approval, Output Validity or Action "
     "Authorization. SANDBOX PASS ≠ ACTIVATION / REGISTRATION / OUTPUT APPROVAL."),
    ("h2", "34.3 Deterministic Continuity"),
    ("p",
     "AI orchestration failure does not unnecessarily disable deterministic NCIE functions — a core "
     "resilience requirement (Ch.10 §10.1)."),
    ("h2", "34.4 Generated-Code Boundary"),
    ("p",
     "If generated executable code remains outside the approved initial-release scope, this is marked "
     "GENERATED-CODE AGENT ACTIVATION — NOT YET APPROVED / SECURITY & ENGINEERING CONFIRMATION "
     "REQUIRED. The broader Dynamic Agent Synthesis approval never silently activates generated-code "
     "capability. If later approved, the specification requires Static Analysis, Dependency Control, "
     "Sandbox, Network Restrictions, Secrets Protection, Runtime Limits, Artifact Integrity, "
     "Evaluation and an Engineering Promotion Boundary."),
    ("review", [
        ("SECURITY", "Determine the initial disposition of generated executable code: out of initial scope, proposed with restrictions, or approved for a defined risk class. Blocking only for generated-code agent activation, not for configuration-only Dynamic Agent Synthesis."),
    ]),
    ("trace", "NCIE-007-S01 §6."),
]
