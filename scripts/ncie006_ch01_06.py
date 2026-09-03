"""NCIE-006 content batch: Chapters 1-6 (mandate/boundary, doctrine, memory
class taxonomy, context envelope, conversation memory, preference memory)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 1 — Memory & Context Mandate, Authority Chain & Specification Boundary
# ---------------------------------------------------------------------------
BLOCKS[1] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.2, §20.12", "Memory tiers and the formal promotion boundary are architecturally fixed; NCIE-006 details their implementation."),
        ("NCIE-003", "Ch.22", "Memory Object, Knowledge Candidate, Institutional Knowledge entities are canonical; NCIE-006 specifies the services and lifecycle around them."),
    ]),
    ("h2", "1.1 Mandate"),
    ("p",
     "NCIE-006 consolidates persistent Memory and Context architecture into an implementable "
     "specification. It preserves model independence, Human-Primary governance, temporal integrity, "
     "provenance and authorization, and does not redesign the upstream architecture that already "
     "fixes these requirements."),
    ("h2", "1.2 Specification Boundary — What NCIE-006 Does Not Own"),
    ("table",
     ["Concern", "Owned By"],
     [
        ["AI/agent/model orchestration engineering", "NCIE-007; NCIE-006 specifies only what Memory/Context must expose to it"],
        ["Identity, authorization enforcement engineering", "NCIE-004 Ch.23; NCIE-009; NCIE-006 specifies authorization requirements, not IAM implementation"],
        ["Evidence object lifecycle, chain-of-custody engineering", "NCIE-003 Ch.17; NCIE-010; NCIE-006 references Evidence, never redefines it"],
        ["API/event transport engineering", "NCIE-004 Ch.8-9; NCIE-011; NCIE-006 specifies service contracts, not wire protocols"],
        ["Physical database/search/graph/vector technology selection", "NCIE-004 (Technology Decision Matrix); NCIE-014; NCIE-006 specifies logical storage roles only"],
        ["Comprehensive test-suite implementation", "NCIE-016; NCIE-006 Ch.34 specifies required test categories, not the full verification programme"],
        ["ARGUS conversational/analytical behavior", "NCIE-005; NCIE-006 specifies what Memory ARGUS may retrieve, not how ARGUS behaves"],
    ],
     "NCIE-006 specification boundary."),
    ("h2", "1.3 Structural Change Control"),
    ("p",
     "The 36-chapter structure is locked. A material contradiction or omission discovered during "
     "expansion is flagged STRUCTURAL CHANGE REQUIRED — HUMAN REVIEW rather than silently resolved. "
     "None has been raised in this edition."),
    ("review", [
        ("INSTITUTIONAL", "Confirm the acceptance authority for NCIE-006 as a whole and for individual chapter sign-off."),
    ]),
    ("trace", "NCIE-002 Ch.20; NCIE-003 Ch.22."),
]

# ---------------------------------------------------------------------------
# Chapter 2 — Memory Doctrine, Invariants & Epistemic Boundaries
# ---------------------------------------------------------------------------
BLOCKS[2] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.2", "ARGUS is not institutional memory; Memory ≠ Current Truth is architecturally fixed."),
        ("NCIE-003", "Ch.22 §22.2", "Institutional Knowledge ≠ Rule; promotion requires recorded human review."),
    ]),
    ("h2", "2.1 Authoritative Definitions"),
    ("table",
     ["Term", "Definition"],
     [
        ["Memory", "A persistent record of something previously observed, decided, discussed or concluded. It is retrospective by nature — it records what was, not what currently is."],
        ["Institutional Knowledge", "A Memory-derived generalisation that has been deliberately reviewed and approved through the lifecycle in Ch.18-19, and is applicable within a defined scope (Ch.19 §19)."],
        ["Evidence", "An authoritative artifact with source, acquisition and validation lineage (NCIE-003 Ch.17) — governed entirely outside NCIE-006; Memory may reference Evidence, never substitute for it."],
        ["Rule", "A governed, effective-dated parameter or threshold (NCIE-003 Ch.24) — governed entirely outside NCIE-006; Institutional Knowledge may motivate a Rule Change Candidate but never directly modifies a Rule."],
    ],
     "Core term definitions, stated once and referenced throughout this document."),
    ("h2", "2.2 Epistemic Boundaries"),
    ("bullets", [
        "ARGUS ≠ Institutional Memory — ARGUS has no memory store of its own; every recollection is retrieved from governed NCIE-006 services (front matter §0.3).",
        "Memory ≠ Current Truth — a Memory Object is never presented as live authoritative state without reconciliation (Ch.13).",
        "Memory ≠ Evidence — a Memory Object may reference Evidence; it never becomes Evidence by being remembered.",
        "Memory ≠ Institutional Knowledge — a raw Memory Object requires deliberate promotion (Ch.18) before it carries institutional authority.",
        "Institutional Knowledge ≠ Rule — approved Knowledge informs human judgment and may motivate a Rule Change Candidate; it never directly alters a governed Rule (NCIE-003 Ch.24).",
    ]),
    ("h2", "2.3 Model Independence"),
    ("p",
     "Model Replacement ≠ Memory Reset. Replacing the ARGUS model or provider (NCIE-004 Ch.18) never "
     "erases or resets Memory or Institutional Knowledge, since both live in governed NCIE-006 "
     "services entirely outside the model/provider boundary. Chapter 34's acceptance tests "
     "demonstrate this directly."),
    ("review", [
        ("RESOLVED", "All five epistemic boundaries in §2.2 are fixed by NCIE-002 Ch.20 and NCIE-003 Ch.22; no institutional decision is required to adopt them."),
    ]),
    ("trace", "NCIE-002 Ch.20 §20.2, §20.12; NCIE-003 Ch.22."),
]

# ---------------------------------------------------------------------------
# Chapter 3 — Memory Class Taxonomy
# ---------------------------------------------------------------------------
BLOCKS[3] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.2", "Private/Shared/Institutional tiers are the architectural basis this taxonomy details into nine operational classes."),
    ]),
    ("h2", "3.1 Memory Class Architecture"),
    ("rel",
     [
        ("Conversation Memory / User Preference Memory", "carry no institutional authority into", "Workspace, Room, Investigation, Situation Memory"),
        ("Workspace, Room, Investigation, Situation Memory", "may be finalized (never auto-converted) into", "Decision Memory"),
        ("Decision Memory / Historical Memory", "may be generalised through deliberate promotion (Ch.18) into", "Institutional Knowledge"),
        ("Institutional Knowledge", "never demotes back to, nor is derived automatically from,", "Conversation or Preference Memory"),
     ],
     "Memory Class Architecture — authority flows only through deliberate promotion (Ch.18); no Memory class silently escalates its own authority."),
    ("h2", "3.2 Memory Class Matrix"),
    ("p", "Nine Memory classes are distinguished throughout this document and never collapsed into "
         "one generic store or lifecycle:"),
    ("table",
     ["Memory Class", "Purpose", "Authority", "Owner Chapter", "Reconciliation Required?"],
     [
        ["Conversation Memory", "Low-authority conversational continuity", "None — never overrides current state, Evidence, Rules, Findings, Decisions or authorization", "Ch.5", "No"],
        ["User Preference Memory", "Low-risk personalization", "None — never alters permissions, Evidence meaning, Rules, analytical truth or Decision authority", "Ch.6", "No"],
        ["Workspace/Session Continuity Memory", "Resumable individual work state", "Low — reflects a user's own prior working state", "Ch.7", "Yes, on resume"],
        ["Collaborative Room Memory", "Structured multi-user analytical reasoning", "Working analysis — Hypothesis/Consensus, never Finding/Decision", "Ch.8", "Yes, on re-entry"],
        ["Investigation Memory", "Investigative evidence relationships, hypotheses, tasks", "Working analysis", "Ch.9", "Yes, on resume"],
        ["Situation Memory", "Evolving cross-domain analytical state", "Working analysis", "Ch.10", "Yes, on resume"],
        ["Decision Memory", "High-integrity Decision-Time snapshots", "High — protected historical record of institutional action", "Ch.11", "N/A — immutable once finalized"],
        ["Historical Memory", "Bitemporal record of past canonical state", "Reflects what was known/true at a point in time", "Ch.12", "Yes, before consequential reuse"],
        ["Institutional Knowledge", "Reviewed, approved, applicability-scoped generalisation", "Institutional — requires human approval (Ch.18-19)", "Ch.18-19", "Yes, via challenge/review (Ch.20)"],
    ],
     "Memory Class Matrix — nine distinguished classes, each independently governed."),
    ("h2", "3.3 Class-Specific Attributes"),
    ("p",
     "Each class in §3.2 additionally has its own Scope, Retention, Authorization and Retrieval "
     "behavior, detailed in its owning chapter — this matrix is the index, not the full "
     "specification for any one class."),
    ("review", [
        ("INSTITUTIONAL", "Confirm retention, access or ownership rules that differ by Memory class beyond what each owning chapter proposes."),
    ]),
    ("trace", "NCIE-002 Ch.20 §20.2."),
]

# ---------------------------------------------------------------------------
# Chapter 4 — Context Taxonomy & Context Envelope
# ---------------------------------------------------------------------------
BLOCKS[4] = [
    ("upstream", [
        ("NCIE-002", "Ch.19 §19.6", "Conversation/Tool Invocation/Proactive Contribution objects carry resolved context; NCIE-006 formalizes the envelope structure."),
    ]),
    ("h2", "4.1 Context Envelope Specification"),
    ("p", "The Context Envelope is the single implementable structure passed among users, services, "
         "tools and ARGUS. Fields are included only where they carry real weight — not merely "
         "because they are convenient:"),
    ("table",
     ["Field", "Purpose"],
     [
        ["Context ID", "Stable reference for this specific context instance (correlation/audit)."],
        ["User", "The human identity the context is resolved for (never a machine-inferred identity, NCIE-005 Ch.4 §4.2)."],
        ["Session / Workspace / Room / Investigation / Situation / Task", "Which of these scopes the context is bound to — mutually clarifying, not all populated simultaneously."],
        ["Operator / Domain / Geography", "The NCIE-003 canonical scope the context concerns."],
        ["Time Mode", "Current / Historical / Decision-Time (Ch.12-13) — never left implicit."],
        ["Time Range / Decision-Time Cutoff", "The specific bound applicable when Time Mode is not Current."],
        ["Purpose", "Why this context is being assembled (feeds Ch.14's minimum-necessary retrieval)."],
        ["Classification", "The governing classification tier (NCIE-003 Ch.31) of the context's most sensitive component."],
        ["Authorization Context", "The effective authorization the context was assembled under (Ch.25) — never expanded after assembly."],
        ["Provenance", "Where each component of the context originated (Ch.27)."],
        ["Correlation ID", "Cross-service tracing reference (NCIE-004 Ch.9)."],
    ],
     "Context Envelope field specification."),
    ("h2", "4.2 Context Taxonomy"),
    ("bullets", [
        "Private Context — visible only to the originating user (Ch.16).",
        "Shared Context — visible to authorized participants of a specific Room/Investigation/Situation (Ch.16).",
        "Institutional Context — promoted, broadly applicable Institutional Knowledge (Ch.16, Ch.18-19).",
    ]),
    ("review", [
        ("PROPOSED", "The Context Envelope field set in §4.1 is proposed as complete for launch; additional fields may be added additively without a breaking change (NCIE-003 Ch.2 §2.8 pattern)."),
    ]),
    ("trace", "NCIE-002 Ch.19 §19.6."),
]

# ---------------------------------------------------------------------------
# Chapter 5 — Conversation Memory
# ---------------------------------------------------------------------------
BLOCKS[5] = [
    ("upstream", [
        ("NCIE-005", "Ch.5", "Conversational assistance grounds answers in authoritative tool results; Conversation Memory supplies continuity only, never authority."),
    ]),
    ("h2", "5.1 Conversation Memory Boundary"),
    ("p",
     "Conversation Memory preserves continuity across turns and sessions. It never overrides "
     "Current Authoritative Domain State, Evidence, Rules, Findings, Decisions or authorization. A "
     "user previously saying something does not make it current institutional truth — Conversation "
     "Memory is retrieved and labelled per NCIE-005 Ch.11's epistemic-type matrix (\"Historical "
     "Memory\"), never presented as a live fact."),
    ("h2", "5.2 Lifecycle"),
    ("table",
     ["State", "Trigger", "Resulting State"],
     [
        ["Active", "Turn recorded during a live session", "Retrievable as recent continuity"],
        ["Aged", "Retention policy threshold reached (Ch.28)", "Retrievable as Historical Memory only, not default continuity"],
        ["Invalidated", "User/administrator requests removal, or content found materially inaccurate", "Retained per Ch.28 §28 rules (INVALIDATED ≠ DELETED), excluded from active retrieval"],
    ],
     "Conversation Memory lifecycle."),
    ("review", [
        ("LEGAL", "Confirm Conversation Memory retention period — no universal period is assumed; classified per Ch.28's class-specific retention requirement."),
    ]),
    ("trace", "NCIE-005 Ch.5, Ch.11."),
]

# ---------------------------------------------------------------------------
# Chapter 6 — User Preference Memory
# ---------------------------------------------------------------------------
BLOCKS[6] = [
    ("upstream", [
        ("NCIE-005", "Ch.28", "Personalization is permitted for presentation/notification/voice/verbosity/workspace; preferences never alter authorization or institutional truth."),
    ]),
    ("h2", "6.1 Preference Memory Boundary"),
    ("table",
     ["Preference May Influence", "Preference Shall Never Alter"],
     [
        ["Presentation, language, voice, notification preferences, accessibility settings", "Permissions"],
        ["Low-risk personalization generally", "Evidence meaning"],
        ["—", "Regulatory Rules"],
        ["—", "Analytical truth"],
        ["—", "Decision authority"],
    ],
     "User Preference Memory boundary (mirrors NCIE-005 Ch.28 §28.2, restated here as the canonical Memory-side rule)."),
    ("trace", "NCIE-005 Ch.28."),
]
