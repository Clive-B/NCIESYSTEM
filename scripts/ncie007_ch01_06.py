"""NCIE-007 content batch: Chapters 1-6 (mandate/boundary, orchestration
doctrine, runtime actor taxonomy, ARGUS orchestrator boundary, Model Gateway
contract, approved model registry)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 1 — Mandate, Authority Chain & Specification Boundary
# ---------------------------------------------------------------------------
BLOCKS[1] = [
    ("upstream", [
        ("NCIE-002", "Ch.4, Ch.24", "Human-Primary authority, Model Gateway, Tool Gateway and AI safety boundaries are architecturally fixed; NCIE-007 specifies their implementation."),
        ("NCIE-005", "Ch.5-30", "ARGUS behavioral limits are canonical; NCIE-007 specifies what ARGUS orchestrates through, not how it behaves."),
        ("NCIE-006", "Ch.1-36", "Memory/Context services are canonical; NCIE-007 specifies how agents consume them, never redefines them."),
    ]),
    ("h2", "1.1 Mandate"),
    ("p",
     "NCIE-007 specifies the orchestration layer beneath ARGUS: model routing, specialized agents, "
     "Dynamic Agent Synthesis, delegation, tools, the VPF Validation Framework, provenance and "
     "failure containment. It implements upstream authority; it does not redesign Human-Primary "
     "governance, ARGUS's behavioral doctrine, canonical data semantics or Memory/Context "
     "architecture."),
    ("h2", "1.2 Specification Boundary — What NCIE-007 Does Not Own"),
    ("table",
     ["Concern", "Owned By"],
     [
        ["Institutional governance/human authority structures", "NCIE-008; NCIE-007 specifies what orchestration must expose to it, not the authority structure itself"],
        ["Identity, authorization enforcement engineering, sandbox/network security implementation", "NCIE-009; NCIE-007 specifies authorization/isolation requirements, not IAM/security implementation"],
        ["Evidence object lifecycle, chain-of-custody engineering", "NCIE-003 Ch.17; NCIE-010; NCIE-007 references Evidence, never redefines it"],
        ["API/event transport engineering", "NCIE-011; NCIE-007 specifies gateway/service contracts, not wire protocols"],
        ["Physical compute/storage/model-hosting technology selection", "NCIE-004 (Technology Decision Matrix); NCIE-014; NCIE-007 specifies logical roles only"],
        ["User experience of agent/VPF status to end users", "NCIE-012; NCIE-007 specifies the states to be shown, not the UI"],
        ["Comprehensive test-suite implementation", "NCIE-016; NCIE-007 Ch.32 specifies required test categories, not the full verification programme"],
        ["ARGUS conversational/analytical/voice behavior", "NCIE-005; NCIE-007 specifies what ARGUS may orchestrate, not how ARGUS behaves"],
        ["Memory/Context persistence and Institutional Knowledge lifecycle", "NCIE-006; NCIE-007 specifies how agents consume governed Memory/Context, never redefines it"],
    ],
     "NCIE-007 specification boundary."),
    ("h2", "1.3 Structural Change Control"),
    ("p",
     "The 36-chapter structure is locked. A material contradiction or omission discovered during "
     "expansion is flagged STRUCTURAL CHANGE REQUIRED — HUMAN REVIEW rather than silently resolved. "
     "None has been raised in this edition."),
    ("review", [
        ("INSTITUTIONAL", "Confirm the acceptance authority for NCIE-007 as a whole and for individual chapter sign-off."),
    ]),
    ("trace", "NCIE-002 Ch.4, Ch.24; NCIE-005; NCIE-006."),
]

# ---------------------------------------------------------------------------
# Chapter 2 — Orchestration Doctrine & Governing Invariants
# ---------------------------------------------------------------------------
BLOCKS[2] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "ARGUS ≠ institutional authority is architecturally fixed; this chapter locks the orchestration-specific corollaries."),
        ("NCIE-006", "front matter §0.3", "REMEMBERED AUTHORIZATION ≠ CURRENT AUTHORIZATION and PRIOR HUMAN DECISION ≠ CURRENT ACTION AUTHORITY apply identically to every model/agent invocation."),
    ]),
    ("h2", "2.1 Authoritative Definitions"),
    ("table",
     ["Term", "Definition"],
     [
        ["Model", "A hosted AI model/deployment invoked only through the Model Gateway (Ch.5); a replaceable implementation component with no institutional standing of its own."],
        ["Agent", "A bounded runtime actor — Registered Reusable or Ephemeral Synthesized (Ch.11) — that performs a declared task using approved models/tools/context; never an institutional decision maker."],
        ["Tool", "A governed capability invoked only through the Tool Gateway (Ch.19); read-only tools are potentially consequential (Ch.20 §20.2)."],
        ["Delegation", "The act of a human, ARGUS or an agent assigning a bounded subtask to another actor; never a mechanism for expanding authority (Ch.14)."],
        ["VPF Disposition", "The explicit validation outcome (PASS/QUALIFIED/REJECT/HUMAN_REVIEW_REQUIRED, Ch.26) an AI-generated output receives before validated release; a disposition, not an approval."],
        ["Agent Definition Package", "The canonical logical structure describing a synthesized agent's purpose, scope, permitted primitives and constraints (Ch.11 §11.4)."],
    ],
     "Core term definitions, stated once and referenced throughout this document."),
    ("h2", "2.2 Governing Invariants"),
    ("p",
     "The 19 invariants in front matter §0.3 bind every chapter without exception, including the "
     "controlled additions for VPF and Dynamic Agent Synthesis. None is re-derived per chapter; each "
     "chapter applies the subset relevant to its scope."),
    ("h2", "2.3 Model Independence"),
    ("p",
     "Replacing the ARGUS model/provider, any routed model, an agent runtime or an agent framework "
     "never transfers institutional authority to that replacement and never resets Institutional "
     "Memory (NCIE-006 §2.3). Orchestration doctrine belongs to NCIE, not to any model vendor's "
     "proprietary agent, tool-calling or validation feature (Ch.36 sovereignty acceptance tests)."),
    ("review", [
        ("RESOLVED", "All 19 governing invariants are fixed by NCIE-002 Ch.4 and the approved NCIE-007 Skeletal v0.2; no institutional decision is required to adopt them."),
    ]),
    ("trace", "NCIE-002 Ch.4; NCIE-006 front matter §0.3."),
]

# ---------------------------------------------------------------------------
# Chapter 3 — AI Runtime Actor & Capability Taxonomy
# ---------------------------------------------------------------------------
BLOCKS[3] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Zero-trust, distinct-identity requirements apply to every orchestration actor without exception."),
    ]),
    ("h2", "3.1 Runtime Actor Taxonomy"),
    ("rel",
     [
        ("Human Principal", "is never assumed to be", "ARGUS"),
        ("ARGUS", "coordinates but is never identical to", "Specialized Agent (Registered or Ephemeral)"),
        ("Specialized Agent", "invokes but is never identical to", "Model"),
        ("Model / Agent", "invokes but is never identical to", "Tool"),
        ("Any Runtime Actor", "is never identical to", "Workflow or Service Identity"),
     ],
     "AI Runtime Actor Taxonomy — every instantiated actor requires a distinct runtime identity (§0.3; audit must identify which actor performed each operation, Ch.27)."),
    ("h2", "3.2 Capability Primitive Classes"),
    ("p", "Every orchestration capability is composed only from approved or eligible primitives:"),
    ("bullets", [
        "Models — eligible hosted deployments invoked via the Model Gateway (Ch.5-6).",
        "Tools — governed capabilities invoked via the Tool Gateway (Ch.19).",
        "Context Services — governed NCIE-006 Memory/Context interfaces (Ch.17).",
        "Schemas — governed output/input contracts (Ch.24, Ch.26).",
        "Policies — governed routing, risk, VPF and resource policy (Ch.7, Ch.20, Ch.26, Ch.29).",
        "Execution Runtimes — sandboxed environments bounding agent execution (Ch.34).",
    ]),
    ("p",
     "ARGUS and the Agent Factory (Ch.12) compose capabilities only from these approved primitives; "
     "neither synthesizes new permissions or infrastructure merely because a task requires them."),
    ("trace", "NCIE-002 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 4 — ARGUS Orchestrator Boundary
# ---------------------------------------------------------------------------
BLOCKS[4] = [
    ("upstream", [
        ("NCIE-005", "Ch.4", "ARGUS is a Human-Primary conversational/analytical assistant, not a model, agent or institutional authority; this chapter specifies its orchestration boundary."),
    ]),
    ("h2", "4.1 What ARGUS Coordinates, Not Owns"),
    ("table",
     ["ARGUS Coordinates", "ARGUS Does Not Become"],
     [
        ["Model selection request", "The Model Gateway (Ch.5) — routing/eligibility decisions are made there, not by ARGUS directly"],
        ["Agent task assignment, including Dynamic Agent Synthesis requests", "The Agent Factory (Ch.12) — synthesis, sandboxing and Gate A occur there"],
        ["Tool invocation request", "The Tool Gateway (Ch.19) — authorization and execution occur there"],
        ["Context retrieval request", "The NCIE-006 Memory/Context Service — ARGUS never owns Institutional Memory directly"],
        ["AI output presentation", "The VPF Validation Framework (Ch.26) — ARGUS never self-certifies its own or an agent's output as validated"],
    ],
     "ARGUS Orchestrator Boundary — ARGUS requests and coordinates; the governed services decide and execute."),
    ("h2", "4.2 Orchestration Request Lifecycle"),
    ("flow",
     ["Human or governed workflow request", "ARGUS interprets task/purpose", "Existing-capability suitability check (registered agent, direct model, or governed tool)", "Route to Model Gateway / Tool Gateway / Agent Factory as applicable", "Result returned to ARGUS", "VPF Gate B validation where applicable (Ch.26)", "ARGUS presents result with disposition to the human"],
     "ARGUS Orchestration Request Lifecycle — every path terminates in a governed service, never an ARGUS-internal shortcut."),
    ("trace", "NCIE-005 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 5 — Model Gateway Contract
# ---------------------------------------------------------------------------
BLOCKS[5] = [
    ("upstream", [
        ("NCIE-002", "Ch.24", "The Model Gateway is the single governed entry boundary to eligible model deployments; this chapter specifies its contract."),
    ]),
    ("h2", "5.1 Model Gateway Mandate"),
    ("p",
     "All model access remains through the Model Gateway. Dynamic agents and registered agents alike "
     "shall not embed direct provider SDK dependencies as an escape path. This applies to every "
     "runtime actor defined in Ch.3, without exception for ephemeral or synthesized agents."),
    ("h2", "5.2 Routing Priority"),
    ("p",
     "Model selection is Eligibility First, then Capability / Performance / Cost / Latency "
     "optimization (Ch.7 defines eligibility criteria in full). An ineligible model is never used as "
     "fallback merely because an eligible model is temporarily unavailable (Ch.10 §10.2)."),
    ("h2", "5.3 Gateway Contract"),
    ("table",
     ["Element", "Purpose"],
     [
        ["Request", "Task profile, purpose, classification, residency, requesting actor identity (Ch.3)."],
        ["Eligibility Result", "Pass/fail against Ch.7's criteria before routing proceeds."],
        ["Route", "The selected eligible model/deployment, or a degraded/no-route state (Ch.10)."],
        ["Response", "Model output plus route/version metadata required for provenance (Ch.9, Ch.27)."],
        ["Telemetry", "Latency, token/cost and error taxonomy (Ch.31) — operational, never authoritative audit (Ch.31 §31.4)."],
    ],
     "Model Gateway request/response contract."),
    ("trace", "NCIE-002 Ch.24."),
]

# ---------------------------------------------------------------------------
# Chapter 6 — Approved Model Registry
# ---------------------------------------------------------------------------
BLOCKS[6] = [
    ("upstream", [
        ("NCIE-004", "Ch.18", "Model/provider approval and lifecycle are engineering-governed; this chapter specifies the orchestration-facing registry contract."),
    ]),
    ("h2", "6.1 Registry Fields"),
    ("table",
     ["Field", "Purpose"],
     [
        ["Model ID / Deployment", "Stable reference distinguishing model version from hosting deployment."],
        ["Provider", "The eligible provider hosting this deployment (Ch.8 governs adapter isolation)."],
        ["Capabilities", "Declared task/tool/output capabilities of this deployment."],
        ["Classification Ceiling", "The maximum data classification this deployment may process."],
        ["Residency", "Approved data-residency scope for this deployment."],
        ["Retention", "Provider-side retention behavior applicable to requests/outputs."],
        ["Lifecycle State", "Candidate / Evaluated / Approved / Active / Restricted / Suspended / Deprecated / Retired (Ch.33)."],
    ],
     "Approved Model Registry fields — evaluated per Ch.7's eligibility dimensions before routing."),
    ("h2", "6.2 Registry Mutation Boundary"),
    ("p",
     "AI components cannot directly mutate Registry state outside authorized lifecycle workflows "
     "(Ch.33). Routing honors current Registry state immediately upon a lifecycle change — a "
     "suspended model is never used merely because a cached eligibility result has not expired."),
    ("review", [
        ("INSTITUTIONAL", "Confirm the model-approval authority and cadence for Registry review."),
    ]),
    ("trace", "NCIE-004 Ch.18."),
]
