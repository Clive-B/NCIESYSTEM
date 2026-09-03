"""NCIE-006 content batch: Chapters 19-24 (knowledge versioning/applicability,
knowledge challenge/impact, knowledge graph context, dependency graph, memory
search/ranking, semantic/vector retrieval boundaries)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 19 — Institutional Knowledge Versioning, Applicability & Review
# ---------------------------------------------------------------------------
BLOCKS[19] = [
    ("upstream", [
        ("NCIE-003", "Ch.22 §22.3", "Applicability Scope and Knowledge Version are canonical Institutional Knowledge attributes."),
    ]),
    ("h2", "19.1 Applicability Scope"),
    ("p",
     "Approved Institutional Knowledge identifies its applicable Domain, Operator, Geography, "
     "Technology, Time, Methodology, Situation Type, Regulatory Context or other relevant boundary. "
     "Contextual lessons are never silently universalized — if retrieved Knowledge appears used "
     "outside its approved scope, ARGUS may warn KNOWLEDGE APPLICABILITY REVIEW REQUIRED (NCIE-005 "
     "Ch.24 restates this as ARGUS behavior); it never silently extends the scope itself."),
    ("h2", "19.2 Review-Due Behavior"),
    ("table",
     ["Situation", "Behavior"],
     [
        ["Review date reached", "Knowledge class/policy determines whether it remains ACTIVE — REVIEW DUE or moves to SUSPENDED PENDING REVIEW; where policy is unknown, classified INSTITUTIONAL CONFIRMATION REQUIRED, never assumed universally"],
        ["Ownership changes (staff departure, reorganization, role/department change)", "Original Authorship, Review, Approval and Contribution Provenance are preserved; changing the owner never rewrites history"],
        ["No accountable current owner", "Enters GOVERNANCE REVIEW REQUIRED rather than remaining indefinitely ownerless"],
    ],
     "Institutional Knowledge review and ownership-transfer behavior."),
    ("h2", "19.3 Versioning"),
    ("p",
     "Each Knowledge Version retains its own effective period and content; retrieval of current "
     "guidance always resolves to the active version, while historical reconstruction (Ch.12) can "
     "recover which version was in force at a prior knowledge time."),
    ("review", [
        ("INSTITUTIONAL", "Confirm review-due default behavior (ACTIVE-REVIEW-DUE vs SUSPENDED) per Knowledge class where NCA policy is not otherwise specified."),
    ]),
    ("trace", "NCIE-003 Ch.22 §22.3."),
]

# ---------------------------------------------------------------------------
# Chapter 20 — Knowledge Challenge, Contradiction & Impact Analysis
# ---------------------------------------------------------------------------
BLOCKS[20] = [
    ("upstream", [
        ("NCIE-005", "Ch.24", "ARGUS may identify a contradiction between current Evidence and approved Knowledge; humans govern the Knowledge response."),
    ]),
    ("h2", "20.1 Knowledge Challenge, Supersession & Retraction Lifecycle"),
    ("flow",
     [
        "Material conflict identified between current Evidence and Approved Knowledge (human or ARGUS)",
        "KNOWLEDGE REVIEW REQUIRED state generated — never silently resolved by picking one side",
        "Human review of the conflict",
        "Outcome: Knowledge reaffirmed, superseded by a new version, or retracted",
        "SUPERSEDED/RETRACTED recorded — historical traceability retained (SUPERSEDED ≠ DELETED; RETRACTED ≠ NEVER EXISTED)",
        "Current retrieval stops presenting superseded/retracted Knowledge as active guidance",
     ],
     "Knowledge Challenge / Supersession / Retraction lifecycle."),
    ("h2", "20.2 Retraction Impact Analysis"),
    ("p",
     "If Knowledge is retracted, active Rooms, Investigations, Situations, Briefings, Reports or "
     "Decision-Support Packages that materially relied upon it are flagged for review — historical "
     "artifacts are never silently rewritten as a result (Ch.22 formalizes the dependency-tracking "
     "mechanism this relies on)."),
    ("h2", "20.3 Re-Review Triggers"),
    ("p",
     "Review date reached, material contradiction, underlying Rule change, definition change, "
     "methodology change, major incident, repeated challenge, or scope-expansion request may each "
     "trigger review — none of them automatically retracts Knowledge; they trigger the human review "
     "process in Ch.18 §18.2."),
    ("trace", "NCIE-005 Ch.24; NCIE-003 Ch.22."),
]

# ---------------------------------------------------------------------------
# Chapter 21 — Knowledge Graph Context & Memory Relationships
# ---------------------------------------------------------------------------
BLOCKS[21] = [
    ("upstream", [
        ("NCIE-003", "Ch.19 §19.2", "Graph Relationship ≠ Causality is the platform-wide invariant; this chapter applies it to Memory/Knowledge relationships specifically."),
    ]),
    ("h2", "21.1 Memory Authority Hierarchy"),
    ("rel",
     [
        ("Evidence (NCIE-003 Ch.17)", "may be cited by", "Memory Object"),
        ("Memory Object", "may be generalised into", "Knowledge Candidate (Ch.18)"),
        ("Knowledge Candidate", "requires human Review State to become", "Approved Institutional Knowledge"),
        ("Approved Institutional Knowledge", "may motivate (never directly modify)", "Rule Change Candidate (NCIE-003 Ch.24)"),
        ("Memory / Knowledge Graph edges", "are correlations, never", "Causality or Culpability claims (NCIE-003 Ch.19 §19.2)"),
     ],
     "Memory Authority Hierarchy — the chain of deliberate promotion from Evidence to Institutional Knowledge."),
    ("h2", "21.2 Graph Authorization"),
    ("p",
     "Graph traversal authorizes Node, Edge, Connected Object and, where relevant, Topology "
     "Disclosure. A hidden node must not be inferable merely through degree count, neighbor count, "
     "path existence or graph visualization — the same authorization discipline NCIE-003 Ch.19 §19.7 "
     "requires for the Intelligence Graph applies identically to the Memory/Knowledge Graph."),
    ("trace", "NCIE-003 Ch.19 §19.2, §19.7."),
]

# ---------------------------------------------------------------------------
# Chapter 22 — Dependency Graph & Downstream Impact Tracking
# ---------------------------------------------------------------------------
BLOCKS[22] = [
    ("upstream", [
        ("NCIE-003", "Ch.25 §25.4", "Correction Relationships trigger forward impact analysis via Dependency Edges; this chapter applies that mechanism to Memory/Knowledge."),
    ]),
    ("h2", "22.1 Knowledge Graph / Dependency Relationship Architecture"),
    ("rel",
     [
        ("Source", "supports", "Evidence"),
        ("Evidence", "supports", "Memory / Hypothesis"),
        ("Hypothesis", "may inform (never automatically becomes)", "Finding"),
        ("Finding", "supports", "Decision"),
        ("Decision / Memory", "may generalise to", "Institutional Knowledge"),
        ("Institutional Knowledge / Decision", "may be cited by", "Report / Briefing"),
     ],
     "Knowledge Graph / Dependency Relationship Architecture — typed dependencies used for impact tracking, not causal assertion (Ch.21 §21.1 restates the authority-hierarchy view of this same graph)."),
    ("h2", "22.2 Typed Dependencies and Impact Analysis"),
    ("p",
     "If upstream Evidence changes, dependent objects identified via §22.1's typed edges are flagged "
     "for review — this never automatically reverses a human Decision (NCIE-003 Ch.25 §25.4's "
     "Impact-Review State pattern applies identically here)."),
    ("h2", "22.3 Pending-Output Invalidation"),
    ("p",
     "If ARGUS has generated a draft briefing or analytical artifact from information subsequently "
     "invalidated before human approval, the artifact is flagged SOURCE STATE CHANGED — REVIEW "
     "REQUIRED rather than silently remaining apparently current."),
    ("trace", "NCIE-003 Ch.25 §25.4."),
]

# ---------------------------------------------------------------------------
# Chapter 23 — Memory Search, Retrieval Modes & Ranking
# ---------------------------------------------------------------------------
BLOCKS[23] = [
    ("upstream", [
        ("NCIE-003", "Ch.4 §4.89-4.93", "Search enforces authorization before returning results, including facets, snippets, autocomplete and semantic matches."),
    ]),
    ("h2", "23.1 Search & Retrieval Architecture"),
    ("flow",
     ["Search Request (Current / Historical / Decision-Time mode)", "Authorization Filter", "Mode-Specific Query (canonical store / bitemporal store / decision-time-bound store)", "Ranking (Ch.23 §23.2)", "Labelled, Authorized Results (Ch.17 §17.2 result labels)"],
     "Memory Search & Retrieval Architecture — mode-differentiated, authorization-filtered throughout."),
    ("h2", "23.2 Ranking Factors"),
    ("p",
     "Ranking considers Authority, Applicability, Temporal Validity, Governance State, Relevance and "
     "Source Quality — never solely Recency or Semantic Similarity, which are inputs to relevance "
     "but never the entire ranking basis."),
    ("h2", "23.3 Retrieval Explainability"),
    ("p",
     "For material retrieval, authorized users can determine why an object was returned, along the "
     "dimensions in §23.2 plus Source and Retrieval Mode — without exposing implementation-sensitive "
     "scoring internals unnecessarily."),
    ("h2", "23.4 Search-Result Leakage Prevention"),
    ("p",
     "Authorization applies before disclosure through titles, snippets, counts, graph neighbors, "
     "semantic matches, autocomplete or facets — none of these surfaces is exempt from the same "
     "authorization check applied to the underlying object (NCIE-003 Ch.4 §4.89-4.93)."),
    ("trace", "NCIE-003 Ch.4 §4.89-4.93."),
]

# ---------------------------------------------------------------------------
# Chapter 24 — Semantic Memory & Vector Retrieval Boundaries
# ---------------------------------------------------------------------------
BLOCKS[24] = [
    ("upstream", [
        ("NCIE-002", "Ch.26 §26.3", "Sensitive semantic/vector indexing requires isolation; NCIE-004 Ch.16 defines the classification-aware vector retrieval stack this chapter governs the Memory-side rules for."),
    ]),
    ("h2", "24.1 Embeddings Are Derived, Not Authoritative"),
    ("p",
     "Embeddings are derived retrieval artifacts. They are not Evidence, Institutional Knowledge or "
     "canonical truth. Changing the embedding model never changes the substantive meaning or status "
     "of the underlying object — a re-embedding event (NCIE-004 Ch.16) is a retrieval-technology "
     "change, not a Memory/Knowledge change."),
    ("h2", "24.2 Sensitive Semantic Indexing"),
    ("p",
     "Highly sensitive information — Protected Identity, raw Ghana Card/Passport values, precise "
     "Anti-Fraud location, restricted Investigation Evidence, sensitive infrastructure data — is "
     "never placed into general-purpose vector infrastructure merely because semantic retrieval is "
     "useful. Where semantic retrieval over such content is required, it uses isolated, "
     "authorization-aware infrastructure per NCIE-004 Ch.16's index-isolation-by-classification-tier "
     "requirement."),
    ("trace", "NCIE-002 Ch.26 §26.3; NCIE-004 Ch.16."),
]
