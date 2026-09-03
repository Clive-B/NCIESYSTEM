"""NCIE-006 content batch: Chapters 13-18 (current-state reconciliation,
context assembly, context propagation, private/shared/institutional
boundaries, ARGUS memory retrieval interface, knowledge candidate lifecycle)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 13 — Current-State Reconciliation
# ---------------------------------------------------------------------------
BLOCKS[13] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.10", "Previous collaborative state must be reconciled with current authoritative NCIE state — the architectural mandate this chapter operationalizes for all Memory classes."),
    ]),
    ("h2", "13.1 Reconciliation States"),
    ("table",
     ["State", "Meaning"],
     [
        ["UNCHANGED", "Current authoritative state matches remembered state exactly."],
        ["CHANGED", "Current state differs from remembered state in a way that does not invalidate the memory's historical accuracy."],
        ["STALE", "Remembered state has exceeded its freshness expectation and has not been re-verified."],
        ["SUPERSEDED", "A newer canonical version exists; the remembered version is no longer current."],
        ["INVALIDATED", "The remembered fact has been formally invalidated at its source."],
        ["CURRENT STATE UNAVAILABLE", "The authoritative source cannot be reached to verify (Ch.30 §30 failure behavior)."],
        ["RECONCILIATION REQUIRED", "A material discrepancy exists that requires explicit resolution before consequential reuse."],
    ],
     "Current-State Reconciliation states — historical Memory is never silently updated; history and current state are always separately exposed."),
    ("h2", "13.2 Current-State Reconciliation Flow"),
    ("flow",
     [
        "Consequential reuse of historical Memory requested",
        "Memory Service resolves the canonical entity the Memory references",
        "Authoritative domain service queried for current state",
        "Comparison against remembered state",
        "Reconciliation state assigned (UNCHANGED/CHANGED/STALE/SUPERSEDED/INVALIDATED/UNAVAILABLE/REQUIRED)",
        "Both remembered and current state exposed distinctly to the consumer",
     ],
     "Current-State Reconciliation flow."),
    ("h2", "13.3 Priority Rule"),
    ("p",
     "When a user requests current operational state, authoritative domain services take precedence "
     "over remembered historical state. Memory may provide context; it never replaces authoritative "
     "current-state retrieval (NCIE-005 Ch.23 restates this at the ARGUS behavior layer; this chapter "
     "is its Memory-service-level enforcement point)."),
    ("trace", "NCIE-002 Ch.20 §20.10; NCIE-005 Ch.23."),
]

# ---------------------------------------------------------------------------
# Chapter 14 — Context Assembly & Minimum-Necessary Retrieval
# ---------------------------------------------------------------------------
BLOCKS[14] = [
    ("upstream", [
        ("NCIE-002", "Ch.24 §24.3", "Context Builder assembles only authorization-filtered, minimal context per request — this chapter is its Memory-side implementation."),
    ]),
    ("h2", "14.1 Context Assembly Flow"),
    ("flow",
     [
        "Requesting service/ARGUS states Purpose and Context Envelope (Ch.4)",
        "Authorization filter applied (Ch.25) — never expanded beyond requester's effective scope",
        "Classification filter applied — sensitive-tier content requires explicit eligibility",
        "Temporal Mode applied (Current/Historical/Decision-Time, Ch.11-13)",
        "Relevance and Applicability filters applied (Ch.19 §19 scope matching for Institutional Knowledge)",
        "Context Budget enforced — excess content trimmed by materiality, not truncated arbitrarily",
        "Assembled Context Envelope returned",
     ],
     "Context Assembly Flow — minimum-necessary retrieval, never a full institutional context dump."),
    ("h2", "14.2 Assembly Considerations"),
    ("bullets", [
        "Purpose — what the context is for shapes what is retrieved.",
        "Authorization and Classification — never assembled beyond the requester's effective scope.",
        "Temporal Mode — Current/Historical/Decision-Time are never mixed silently.",
        "Relevance and Applicability — Institutional Knowledge outside its applicable scope (Ch.19) is excluded, not force-included.",
        "Data Minimization and Context Budget — prioritised by authorization, purpose, authority, temporal applicability, materiality, evidence/contradiction relevance; never by semantic similarity alone.",
    ]),
    ("h2", "14.3 ARGUS Does Not Access Raw Memory Stores"),
    ("flow",
     ["ARGUS", "Context/Memory Retrieval Service", "Authorization + Purpose + Temporal Filters", "Memory/Knowledge Sources"],
     "ARGUS's memory access path — no AI-only unrestricted retrieval path exists."),
    ("trace", "NCIE-002 Ch.24 §24.3."),
]

# ---------------------------------------------------------------------------
# Chapter 15 — Context Propagation Across Services & Workflows
# ---------------------------------------------------------------------------
BLOCKS[15] = [
    ("upstream", [
        ("NCIE-002", "Ch.4 §4.4", "Zero-trust authorization is re-evaluated at every service boundary; context propagation never substitutes for it."),
    ]),
    ("h2", "15.1 Context Propagation ≠ Authorization Propagation"),
    ("p",
     "A user navigating Dashboard → Situation → Investigation → Evidence → ARGUS may retain "
     "relevant context (operator, geography, active thread). Navigation never expands access — "
     "every destination independently applies its own authorization check (Ch.25), regardless of "
     "what context was carried forward."),
    ("h2", "15.2 Permission-Change Propagation"),
    ("bullets", [
        "If a user's authorization changes during an active session, Room or Investigation, subsequently assembled context reflects the new authorization immediately — authorization is never assumed valid for the lifetime of a session.",
        "Revocation after sensitive context has already been retrieved is handled via: future retrieval block; UI redaction/removal where technically feasible; cache invalidation; ARGUS context removal; search/graph access restriction; and audit. Already-perceived human information cannot be technically \"unseen\" — this is an acknowledged limit, not a false guarantee.",
    ]),
    ("trace", "NCIE-002 Ch.4 §4.4."),
]

# ---------------------------------------------------------------------------
# Chapter 16 — Private, Shared & Institutional Context Boundaries
# ---------------------------------------------------------------------------
BLOCKS[16] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.9", "Shared room context never pools participant permissions; Private User Memory is not automatically shareable."),
    ]),
    ("h2", "16.1 Private → Shared → Institutional Context Transition"),
    ("flow",
     [
        "Private Context (single user, e.g. Preference/Conversation Memory, Ch.5-6)",
        "Deliberate sharing action into a Room/Investigation/Situation (Ch.8-10)",
        "Shared Context — visible only to that Room/Investigation/Situation's authorized participants",
        "Knowledge Candidate proposed from Shared Context pattern (Ch.18)",
        "Human review and approval (Ch.18-19)",
        "Institutional Context — Approved Institutional Knowledge, broadly applicable within its scope",
     ],
     "Private → Shared → Institutional context transition — each step is a deliberate, human-governed action, never automatic."),
    ("h2", "16.2 Shared Room Disclosure"),
    ("p",
     "A Collaborative Room's shared disclosure is calculated per-participant from governed "
     "authorization, never as a permission union: one participant's ability to access an object "
     "never means ARGUS may expose it to every Room participant (NCIE-002 Ch.20 §20.9). ARGUS's "
     "effective Room context is restricted to information appropriately shareable in that context — "
     "private context from one participant never silently becomes ARGUS-shared Room context."),
    ("trace", "NCIE-002 Ch.20 §20.9; NCIE-003 Ch.4 §4.72-4.79."),
]

# ---------------------------------------------------------------------------
# Chapter 17 — ARGUS Memory Retrieval Interface
# ---------------------------------------------------------------------------
BLOCKS[17] = [
    ("upstream", [
        ("NCIE-005", "Ch.23", "ARGUS retrieves memory via governed services and reconciles it against current state; NCIE-006 specifies the interface those retrievals actually use."),
    ]),
    ("h2", "17.1 Governed Retrieval Interface"),
    ("p",
     "ARGUS consumes Memory exclusively through the Memory/Context Retrieval Service (Ch.14's "
     "assembly flow), never a direct store connection. Every retrieval carries the requesting "
     "identity's effective authorization, purpose, and temporal mode; none of these may be widened "
     "by the fact that the requester is ARGUS rather than a human."),
    ("h2", "17.2 Retrieval Result Labels"),
    ("p",
     "Returned Memory/Knowledge visibly distinguishes its category — never collapsed into one "
     "generic \"memory result\":"),
    ("bullets", [
        "CURRENT AUTHORITATIVE CONTEXT",
        "HISTORICAL MEMORY",
        "DECISION-TIME CONTEXT",
        "APPROVED INSTITUTIONAL KNOWLEDGE",
        "PRIOR HUMAN JUDGMENT",
        "ARGUS-GENERATED HISTORICAL ANALYSIS",
        "UNVALIDATED KNOWLEDGE CANDIDATE",
    ]),
    ("p",
     "These labels are the Memory-service-side source of NCIE-005 Ch.11's ARGUS Output/Epistemic-"
     "Type Matrix — that chapter specifies how ARGUS presents them; this chapter specifies that the "
     "Memory Service produces them accurately in the first place."),
    ("trace", "NCIE-005 Ch.11, Ch.23."),
]

# ---------------------------------------------------------------------------
# Chapter 18 — Institutional Knowledge Candidate Lifecycle
# ---------------------------------------------------------------------------
BLOCKS[18] = [
    ("upstream", [
        ("NCIE-003", "Ch.22 §22.4", "Promotion to Institutional Knowledge requires a recorded human Review State; a Knowledge Candidate never self-promotes."),
    ]),
    ("h2", "18.1 Knowledge Candidate Definition"),
    ("p",
     "A Knowledge Candidate is a proposed generalisation derived from Memory, awaiting human review "
     "before it may carry institutional authority (Ch.2 §2.1's authoritative definition applies)."),
    ("h2", "18.2 Institutional Knowledge Promotion Lifecycle"),
    ("flow",
     ["CANDIDATE (proposed, origin traceable)", "REVIEW (human evaluation, separation of duties where policy requires)", "APPROVED (applicability scope defined, Ch.19)", "ACTIVE (in force within scope)"],
     "Institutional Knowledge Promotion Lifecycle — the main forward path; §18.3's table below covers the full state machine including challenge/supersession/retraction branches."),
    ("h2", "18.3 Full Lifecycle State Machine"),
    ("table",
     ["State", "Trigger", "Permitted Actor", "Resulting State"],
     [
        ["CANDIDATE", "Proposed from Human Analyst, Collaborative Room, Investigation, Situation, Post-Incident Review, Expert Contribution or ARGUS Proposal", "Any of the above; origin remains traceable after promotion", "REVIEW"],
        ["REVIEW", "Submitted for human evaluation", "Authorized reviewer, distinct from proposer where policy requires (Ch.20 §20.5)", "APPROVED or REJECTED"],
        ["APPROVED", "Reviewer approves with defined applicability scope (Ch.19)", "Authorized approver", "ACTIVE"],
        ["ACTIVE", "In force within its applicability scope", "N/A (state, not action)", "CHALLENGED, REVIEW_DUE, SUPERSEDED, RETRACTED or EXPIRED"],
        ["CHALLENGED", "Material conflict identified (Ch.20)", "Any authorized user/ARGUS may flag; only a human resolves", "ACTIVE (challenge resolved) or REVIEW (re-review triggered)"],
        ["REVIEW_DUE / SUPERSEDED / RETRACTED / EXPIRED", "Review date reached / newer version approved / formally withdrawn / applicability period lapsed", "Per Ch.19 policy", "Terminal or REVIEW, per Ch.19 §19"],
    ],
     "Institutional Knowledge Candidate lifecycle state machine."),
    ("h2", "18.4 ARGUS Role"),
    ("p",
     "ARGUS may propose a Knowledge Candidate, organize supporting evidence, surface contradictions, "
     "and prepare review material. ARGUS does not approve — this remains true even where the "
     "candidate originated from ARGUS itself (NCIE-005 Ch.24 §24.1 restates this at the behavioral "
     "layer)."),
    ("review", [
        ("INSTITUTIONAL", "Confirm whether separation of duties between Candidate Contributor, Reviewer and Approver is institutionally required, or whether one authorized role may perform more than one step."),
    ]),
    ("trace", "NCIE-003 Ch.22 §22.4; NCIE-005 Ch.24."),
]
