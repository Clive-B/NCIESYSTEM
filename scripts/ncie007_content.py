"""Content model for NCIE-007 AI, Agent & Model Orchestration Specification.

CHAPTERS populated in batches (1-6, 7-12, 13-18, 19-24, 25-30, 31-36).
Block kinds consumed by ncie007_common.render_blocks:
  ("h2", text) / ("h3", text) / ("p", text) / ("bullets", [items])
  ("upstream", [(doc_id, ref, consequence), ...]) / ("vpf", text)
  ("proposed", text) / ("trace", text) / ("review", [items])
  ("flow", [nodes], caption) / ("rel", [(s,r,t), ...], caption)
  ("table", headers, rows, caption, status_col_index_or_None)
"""

CHAPTER_TITLES = {
    1: "Mandate, Authority Chain & Specification Boundary",
    2: "Orchestration Doctrine & Governing Invariants",
    3: "AI Runtime Actor & Capability Taxonomy",
    4: "ARGUS Orchestrator Boundary",
    5: "Model Gateway Contract",
    6: "Approved Model Registry",
    7: "Classification-, Purpose- & Task-Aware Model Routing",
    8: "Provider Adapters & Provider Neutrality",
    9: "Model Selection, Versioning & Reproducibility",
    10: "Fallback, Failover & Degraded AI Operation",
    11: "Specialized Agent Architecture & Dynamic Agent Synthesis",
    12: "Agent Capability Registry & Agent Factory",
    13: "Task Decomposition & Delegation",
    14: "Delegated Authorization & Identity Propagation",
    15: "Multi-Agent Coordination & Conflict Handling",
    16: "Agent State, Checkpointing & Resumption",
    17: "Context Acquisition & Memory-Service Integration",
    18: "Evidence & Grounding Integration",
    19: "Tool Gateway Integration",
    20: "Read-Only vs State-Changing Tool Classes",
    21: "Human Approval, Confirmation & Execution Boundary",
    22: "Agent-to-Agent Tool Delegation",
    23: "Planning, Reflection & Iterative Analytical Loops",
    24: "Prompt, Instruction & Policy Assembly",
    25: "Prompt Injection & Untrusted-Content Containment",
    26: "Output Schemas, Validation & the VPF Validation Framework",
    27: "AI Provenance, Attribution & Execution Receipts",
    28: "Safety Guardrails & Policy Enforcement",
    29: "Resource Budgets, Cost, Rate Limits & Quotas",
    30: "Concurrency, Idempotency & Duplicate Suppression",
    31: "Observability, Telemetry & AI Operations",
    32: "Evaluation, Regression & Adversarial Testing",
    33: "Model & Agent Lifecycle Governance",
    34: "Security, Isolation & Supply-Chain Boundaries",
    35: "Human Review Register, Open Decisions & Proposed Defaults",
    36: "Requirements Traceability, Acceptance & Handover Gate",
}

CHAPTER_SCOPE = {
    1: "Establish NCIE-007 as the orchestration authority beneath ARGUS without redefining upstream architecture.",
    2: "Lock the invariants governing models, agents, delegation, tools, VPF and Dynamic Agent Synthesis.",
    3: "Define runtime actor types (Human, ARGUS, Registered Agent, Ephemeral Agent, Model, Tool, Service) and machine-readable capability classes.",
    4: "Define how ARGUS coordinates AI capabilities without becoming the Model Gateway, Memory Service or Tool Gateway.",
    5: "Define the single governed entry boundary between ARGUS/agents and eligible model deployments.",
    6: "Define governed metadata and lifecycle for models/deployments eligible for NCIE use.",
    7: "Define deterministic eligibility and routing based on classification, purpose, task and policy.",
    8: "Isolate provider-specific APIs behind replaceable adapters.",
    9: "Preserve exact model/deployment context for consequential persisted outputs.",
    10: "Define safe fallback and degraded operation without weakening eligibility controls.",
    11: "Define bounded specialized agents — Registered Reusable and Ephemeral Synthesized — and the Dynamic Agent Synthesis capability that creates the latter.",
    12: "Define the governed registry of agent capabilities and the Agent Factory that synthesizes bounded agents from approved primitives.",
    13: "Define decomposition of complex work into bounded delegated subtasks, including subtasks satisfied by Dynamic Agent Synthesis.",
    14: "Propagate current authorization without allowing delegation or synthesis to expand authority.",
    15: "Coordinate multiple agents — registered and ephemeral — while preserving conflicts, attribution and human control.",
    16: "Persist operational run/checkpoint state without turning agent state into Institutional Memory.",
    17: "Acquire minimum-necessary governed context through NCIE-006 Memory/Context services.",
    18: "Ground model/agent work in authorized Evidence while preserving epistemic boundaries.",
    19: "Require all consequential tool access through the governed Tool Gateway.",
    20: "Classify tool risk and distinguish sensitive read/reveal from state-changing actions.",
    21: "Define mandatory human/current-authority boundaries before consequential execution.",
    22: "Govern indirect agent-to-agent tool delegation without transitive privilege escalation or Agent Factory access.",
    23: "Bound planning/revision loops while persisting defensible artifacts rather than private chain-of-thought.",
    24: "Define the trusted instruction hierarchy and prompt/policy assembly order.",
    25: "Contain prompt injection and malicious instructions embedded in retrieved content.",
    26: "Define the mandatory VPF Validation Framework — dimensions, profiles and dispositions — that all substantive AI-generated output must enter before validated release, with profile rigor (not exemption) varying by risk.",
    27: "Preserve end-to-end model, agent, tool, VPF and human attribution, including for Dynamic Agent Synthesis runs.",
    28: "Enforce technical safety policy beyond prompt instructions.",
    29: "Bound token, time, concurrency, cost and tool-call consumption for every model/agent invocation.",
    30: "Prevent duplicate actions and stale-result overwrites under retries/concurrency.",
    31: "Provide operational visibility into routing, agents, tools, VPF, Agent Factory and failures.",
    32: "Define release evaluation, regression and adversarial testing for orchestration, VPF and Dynamic Agent Synthesis.",
    33: "Govern model/agent onboarding, approval scope, suspension, deprecation, retirement and promotion.",
    34: "Define orchestration-specific isolation and supply-chain boundaries without duplicating NCIE-009.",
    35: "Consolidate every unresolved orchestration, VPF and Dynamic Agent Synthesis decision with category and blocking state.",
    36: "Provide the complete upstream crosswalk, Upstream Impact Register, Downstream Handover Register, acceptance scenarios and controlled handover to NCIE-008.",
}

GOVERNING_INVARIANTS = [
    "ARGUS ≠ MODEL.",
    "ARGUS ≠ SPECIALIZED AGENT.",
    "MODEL ≠ INSTITUTIONAL AUTHORITY.",
    "AGENT ≠ INSTITUTIONAL DECISION MAKER.",
    "DELEGATION ≠ AUTHORITY EXPANSION.",
    "TOOL ACCESS ≠ ACTION AUTHORITY.",
    "MODEL AVAILABILITY ≠ MODEL ELIGIBILITY.",
    "AGENT CONSENSUS ≠ INSTITUTIONAL TRUTH.",
    "MODEL/AGENT OUTPUT ≠ EVIDENCE, FINDING OR DECISION.",
    "RETRIEVED CONTENT ≠ TRUSTED INSTRUCTION.",
    "ARGUS/AGENTS ≠ INSTITUTIONAL MEMORY.",
    "REMEMBERED AUTHORIZATION ≠ CURRENT AUTHORIZATION.",
    "AGENT CREATION ≠ AUTHORITY CREATION.",
    "AGENT SYNTHESIS ≠ PERMISSION EXPANSION.",
    "EPHEMERAL AGENT ≠ REGISTERED INSTITUTIONAL AGENT.",
    "SYNTHESIZED AGENT ≠ AGENT-FACTORY AUTHORITY.",
    "AGENT SYNTHESIS ≠ SELF-REGISTRATION.",
    "VPF VALIDATION ≠ HUMAN / INSTITUTIONAL APPROVAL.",
    "UNVALIDATED AI OUTPUT ≠ VALIDATED NCIE AI RESULT.",
    "SUBSTANTIVE AI OUTPUT ≠ VPF-EXEMPT BY DEFAULT.",
]

# Chapters carrying substantive VPF architecture content (mandatory per item 1780).
VPF_CHAPTERS = {26}
# Chapters that must fully incorporate Dynamic Agent Synthesis / VPF consequences (item 1780).
DYNAMIC_AGENT_CHAPTERS = {11, 12, 13, 14, 15, 16, 22, 26, 27, 31, 32, 33, 34, 35, 36}

FRONT_MATTER = {
    "governance_rows": [
        ("Document", "NCIE-007 AI, Agent & Model Orchestration Specification"),
        ("Edition", "In development — Version 1.1"),
        ("Baseline authorized", "NCIE-007 Skeletal v0.2 (VPF & Dynamic Agent Update) + NCIE-007-S01 v0.1 (Dynamic Agent Synthesis & Runtime Registration Supplement) — approved for full expansion; 36-chapter structure locked"),
        ("Requirements authority", "NCIE-001 Master Product Requirements Document, Version 1.2"),
        ("Architecture authority", "NCIE-002 System Architecture & Technical Design, Version 0.4"),
        ("Canonical data authority", "NCIE-003 Data Model & Data Dictionary, Version 0.3 (Canonical Data Architecture Baseline)"),
        ("Engineering baseline", "NCIE-004 Technology Stack & Engineering Blueprint, Version 1.1 (Approved Engineering Baseline)"),
        ("ARGUS behavioral authority", "NCIE-005 ARGUS Intelligence Assistant Specification, Version 1.2"),
        ("Memory & Context authority", "NCIE-006 Memory & Context Architecture Specification, Version 1.1"),
        ("Owner", "National Communications Intelligence Ecosystem (NCIE) Architecture Function"),
        ("Reviewer", "David King Boison (PhD) — Academic Intelligence Center"),
        ("Status", "IN DEVELOPMENT — FOR HUMAN REVIEW until explicitly approved"),
    ],
}

CHAPTERS = [
    {
        "number": n,
        "title": CHAPTER_TITLES[n],
        "scope": CHAPTER_SCOPE[n],
        "blocks": [],
    }
    for n in range(1, 37)
]


def get_chapter(number):
    for chapter in CHAPTERS:
        if chapter["number"] == number:
            return chapter
    raise KeyError(number)


def set_blocks(number, blocks):
    get_chapter(number)["blocks"] = blocks
