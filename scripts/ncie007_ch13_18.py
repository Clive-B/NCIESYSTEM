"""NCIE-007 content batch: Chapters 13-18 (task decomposition/delegation,
delegated authorization/identity propagation, multi-agent coordination,
agent state/checkpointing, context acquisition, evidence/grounding)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 13 — Task Decomposition & Delegation
# ---------------------------------------------------------------------------
BLOCKS[13] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Delegation ≠ authority expansion is architecturally fixed; this chapter specifies bounded subtask decomposition."),
    ]),
    ("h2", "13.1 Decomposition Boundary"),
    ("p",
     "A complex task decomposes into bounded delegated subtasks. Where no eligible existing agent "
     "satisfies a bounded subtask, ARGUS may request Dynamic Agent Synthesis (Ch.11). The synthesized "
     "agent receives only the task-specific subset of context, tools, data classes and authority "
     "required for that subtask — never the parent task's full scope by default."),
    ("h2", "13.2 Subtask Record"),
    ("table",
     ["Field", "Purpose"],
     [
        ["Parent Task", "The originating task this subtask decomposes from."],
        ["Subtask", "The bounded unit of work assigned."],
        ["Delegator", "The human, ARGUS or agent that issued the delegation."],
        ["Purpose", "Why this subtask exists (feeds minimum-necessary context, Ch.17)."],
        ["Context Subset", "The bounded context the subtask actually receives."],
        ["Constraints", "Resource, tool, data-class and temporal constraints (Ch.14, Ch.29)."],
        ["Completion State", "Pending / Completed / Failed / Escalated."],
     ],
     "Subtask decomposition record."),
    ("trace", "NCIE-002 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 14 — Delegated Authorization & Identity Propagation
# ---------------------------------------------------------------------------
BLOCKS[14] = [
    ("upstream", [
        ("NCIE-006", "Ch.25 §25.3", "Remembered Authorization ≠ Current Authorization applies identically to every delegated/synthesized agent invocation."),
    ]),
    ("h2", "14.1 Current Authorization Propagation"),
    ("p",
     "Delegated and synthesized agents propagate current authorization; they never expand it. A "
     "synthesized agent has its own runtime identity (Ch.3 §3.1) and effective authorization envelope "
     "— it cannot inherit broader ARGUS privileges, another user's private context, or create new "
     "permissions through its generated definition."),
    ("h2", "14.2 Authorization Recheck"),
    ("table",
     ["Element", "Behavior"],
     [
        ["Human Principal", "The accountable current human whose authorization anchors the delegation."],
        ["Agent/Service Identity", "The distinct runtime identity executing the delegated work (never conflated with the Human Principal or ARGUS)."],
        ["Current Authorization Context", "Rechecked at time of use, not assumed from delegation time."],
        ["Purpose", "The declared reason authorization was granted; expiring when the purpose completes."],
        ["Expiry / Recheck / Denial", "A delegated authorization that has expired or been revoked is denied, never silently honored from cached state."],
     ],
     "Delegated authorization propagation model."),
    ("h2", "14.3 Recursive Delegation Boundary"),
    ("p",
     "Delegation cannot create transitive privilege expansion. If agent-to-agent delegation is "
     "permitted (Ch.22), every hop preserves Parent Task, Purpose, Effective Principal, "
     "Classification, Context Subset, Tool Ceiling, Resource Ceiling and Provenance — no hop widens "
     "them."),
    ("review", [
        ("SECURITY", "Confirm the authorization-revocation propagation latency acceptable for an active agent run — historical authorization shall not remain effective through cached agent state."),
    ]),
    ("trace", "NCIE-006 Ch.25 §25.3."),
]

# ---------------------------------------------------------------------------
# Chapter 15 — Multi-Agent Coordination & Conflict Handling
# ---------------------------------------------------------------------------
BLOCKS[15] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Agent consensus ≠ institutional truth is architecturally fixed; this chapter specifies multi-agent disagreement handling."),
    ]),
    ("h2", "15.1 Disagreement Is Not Resolved by Voting"),
    ("p",
     "Multi-agent disagreement — among registered agents, ephemeral synthesized agents, or a mix — "
     "is never resolved through simple majority voting. AGENT CONSENSUS ≠ INSTITUTIONAL TRUTH (front "
     "matter §0.3)."),
    ("h2", "15.2 Preserved Disagreement Record"),
    ("bullets", [
        "Agent A Result; Agent B Result (and further agents where applicable).",
        "Evidence Basis for each result.",
        "Contradictions between results.",
        "Uncertainty in each result.",
        "VPF Disposition for each result (Ch.26).",
    ]),
    ("p",
     "ARGUS may synthesize the disagreement for humans — presenting the record above — but never "
     "collapses it into a single asserted truth on the agents' behalf."),
    ("trace", "NCIE-002 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 16 — Agent State, Checkpointing & Resumption
# ---------------------------------------------------------------------------
BLOCKS[16] = [
    ("upstream", [
        ("NCIE-006", "Ch.20", "Agent state is not Institutional Memory; material reasoning artifacts requiring institutional persistence flow through governed NCIE-006 services."),
    ]),
    ("h2", "16.1 Run-Scoped State"),
    ("p",
     "Synthesized-agent state is run-scoped by default. Checkpoints preserve the Agent Definition "
     "version and VPF Gate A result in force at checkpoint time. Expired ephemeral agents shall not "
     "silently reactivate as reusable capabilities — reactivation always re-evaluates current "
     "authorization and eligibility (Ch.11 §11.9)."),
    ("h2", "16.2 Memory Independence"),
    ("p",
     "Agent checkpoints may preserve operational run state; they are not Institutional Memory. "
     "Material reasoning artifacts that require institutional persistence — Findings, Decisions, "
     "Knowledge Candidates — are stored through the governed NCIE-006 Memory/Context architecture, "
     "never left only in agent checkpoint storage. Agent expiry shall not erase properly persisted "
     "institutional artifacts."),
    ("h2", "16.3 Checkpoint Fields"),
    ("table",
     ["Field", "Purpose"],
     [
        ["Run ID", "Stable reference for this specific agent execution."],
        ["Checkpoint", "Point-in-time operational state snapshot."],
        ["Task State", "Progress against the declared task/subtask."],
        ["Context Reference", "Pointer to the governed context the run consumed, not a private copy."],
        ["Retry / Resume", "Whether this run may be retried or resumed and under what current-authorization conditions."],
        ["Expiry", "The governed expiry condition applicable to this run."],
        ["Terminal State", "Completed / Failed / Expired / Terminated."],
     ],
     "Agent run/checkpoint record."),
    ("review", [
        ("INFRASTRUCTURE", "Confirm checkpoint retention duration and storage tier separate from institutional Memory retention (NCIE-006 Ch.28)."),
    ]),
    ("trace", "NCIE-006 Ch.20."),
]

# ---------------------------------------------------------------------------
# Chapter 17 — Context Acquisition & Memory-Service Integration
# ---------------------------------------------------------------------------
BLOCKS[17] = [
    ("upstream", [
        ("NCIE-006", "Ch.14, Ch.17", "Minimum-necessary retrieval and the governed ARGUS Memory Retrieval Interface are canonical; this chapter is their orchestration-side consumption contract."),
    ]),
    ("h2", "17.1 Minimum-Necessary Context Acquisition"),
    ("p",
     "Synthesized and registered agents receive only the context required for their declared task. "
     "They consume governed context exclusively through NCIE-006 services and shall not inherit "
     "ARGUS's entire context, another user's private context, unrestricted Institutional Memory, or "
     "all Room information merely because ARGUS created or coordinates them."),
    ("h2", "17.2 Context Request Contract"),
    ("table",
     ["Field", "Purpose"],
     [
        ["Context Request", "Declares the requesting actor identity (Ch.3), purpose and task scope."],
        ["Context Envelope", "The NCIE-006 Context Envelope (NCIE-006 Ch.4) returned, bounded to the declared purpose."],
        ["Temporal Mode", "Current / Historical / Decision-Time — never left implicit (NCIE-006 Ch.12-13)."],
        ["Classification", "The governing classification of the returned context."],
        ["Authorization", "The effective authorization the context was assembled under."],
        ["Reconciliation State", "Whether the returned context is Current, Stale or requires Reconciliation (NCIE-006 Ch.13)."],
     ],
     "Context acquisition contract — mirrors NCIE-006's Context Envelope exactly, never a parallel structure."),
    ("trace", "NCIE-006 Ch.14, Ch.17."),
]

# ---------------------------------------------------------------------------
# Chapter 18 — Evidence & Grounding Integration
# ---------------------------------------------------------------------------
BLOCKS[18] = [
    ("upstream", [
        ("NCIE-003", "Ch.17", "Evidence lifecycle and chain-of-custody are canonical; this chapter governs how models/agents ground work in it."),
    ]),
    ("h2", "18.1 Grounding Boundary"),
    ("p",
     "Model/agent work is grounded in authorized Evidence references, never in ungrounded assertion "
     "presented as fact. AI OUTPUT ≠ EVIDENCE (Ch.36 §36.8 final audit) unless an independent governed "
     "process establishes an appropriate Evidence object from an actual source/acquisition event. AI "
     "transformation of Evidence remains traceable to the original Evidence."),
    ("h2", "18.2 Grounding Package"),
    ("bullets", [
        "Evidence References — the specific authorized Evidence objects consulted.",
        "Source Authority — provenance of each reference (NCIE-003 Ch.17).",
        "Contradiction Set — known contradictions among referenced Evidence.",
        "Citation Metadata — sufficient for a human reviewer to verify the grounding.",
    ]),
    ("p",
     "Evidence/tool access is governed independently at use time; an AI proposal or verbal request "
     "never becomes execution authority (Ch.21)."),
    ("trace", "NCIE-003 Ch.17."),
]
