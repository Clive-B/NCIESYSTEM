"""NCIE-006 content batch: Chapters 25-30 (memory security/authorization,
sensitive memory/protected identity/voice, provenance/audit,
retention/legal hold/disposition, storage architecture, APIs/events)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 25 — Memory Security, Authorization & Zero-Trust Controls
# ---------------------------------------------------------------------------
BLOCKS[25] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Zero-trust, four-layer authorization (role/object/field/action) applies to every Memory class independently."),
    ]),
    ("h2", "25.1 Memory Authority Matrix"),
    ("table",
     ["Access Granted", "Does NOT Automatically Grant"],
     [
        ["Access to current canonical objects", "Historical access, Private Memory access, Room Memory access, Investigation Memory access, or Decision Memory access"],
        ["Room membership", "Access to every Evidence object referenced within the Room (NCIE-003 Ch.4 §4.69)"],
        ["Access to a Decision record", "Access to every underlying restricted Evidence item cited by it (Ch.11 §11.3)"],
    ],
     "Memory Authority Matrix — object-, purpose-, classification- and temporal-aware; nothing is transitively assumed."),
    ("h2", "25.2 Concurrency and Conflict"),
    ("p",
     "Concurrent human/system activity (two reviewers editing a Knowledge Candidate, a Room Snapshot "
     "during active collaboration, retraction while ARGUS retrieves the same object, permission "
     "revocation mid-session, correction during historical reconstruction) is never resolved by "
     "silent last-write-wins for consequential institutional state. A VERSION CONFLICT state "
     "requires reload, merge or human resolution according to object type."),
    ("h2", "25.3 Remembered Authorization Is Never Current Authorization"),
    ("p",
     "REMEMBERED AUTHORIZATION ≠ CURRENT AUTHORIZATION (front matter §0.3). A Memory object may "
     "record that a person held a role, permission or access grant at some past point — including "
     "within a Decision-Time Snapshot (Ch.11) or a Historical Memory reconstruction (Ch.12). That "
     "recorded fact is never itself treated as authorizing a new consequential action today. Every "
     "consequential action is authorized from the current governed IAM/authorization context (NCIE-004 "
     "Ch.23; NCIE-009), re-checked at the time of the new action, regardless of what Memory shows the "
     "person was permitted to do previously — a revoked, expired or role-changed permission is never "
     "reinstated by historical recollection. Current-State Reconciliation (Ch.13) applies to "
     "remembered authorization exactly as it applies to any other remembered state."),
    ("trace", "NCIE-002 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 26 — Sensitive Memory, Protected Identity & Voice Context
# ---------------------------------------------------------------------------
BLOCKS[26] = [
    ("upstream", [
        ("NCIE-003", "Ch.14 §14.6, Ch.36 §36.3", "Ghana Card/Passport and Anti-Fraud location protections apply to Memory exactly as to canonical data."),
        ("NCIE-005", "Ch.29 §29.1", "The Voice Interaction & Spoken-Disclosure Matrix governs what may be spoken; this chapter governs what is remembered about it."),
    ]),
    ("h2", "26.1 Governed Sensitive Classes"),
    ("bullets", [
        "Protected Identity (Ghana Card, Passport) — masked/tokenized in Memory exactly as in canonical stores (NCIE-003 Ch.14 §14.6); never stored in plaintext in a Memory Object merely because it appeared in a conversation.",
        "Anti-Fraud location — inherits sensitive-tier isolation and heightened authorization wherever it appears in Memory (Ch.9 §9.2).",
        "Restricted Investigation Evidence and sensitive infrastructure data — classification inherited from the referenced canonical object, never downgraded by being remembered.",
    ]),
    ("voice", "Voice/Speaker Recognition ≠ Authenticated Identity — Memory never records an inferred speaker identity as authoritative; identity comes from the governed NCIE authentication context (NCIE-005 Ch.4 §4.2), never from voice characteristics. Display Authorization ≠ Spoken-Disclosure Authorization — remembered authorization to view sensitive information never becomes permission to speak it aloud later; every synthesis still passes through NCIE-005 Ch.29's spoken-disclosure check at the time of speaking. Spoken-notification Memory: the fact that ARGUS spoke a notification is never treated as proof a human heard, understood, acknowledged or acted on it — acknowledgement, where it matters, is a separately stored governed event (Ch.11-style integrity, not inferred from audio)."),
    ("h2", "26.2 Voice Object Distinctness"),
    ("p",
     "Raw Audio, Speech-to-Text Transcript, Structured Room/Investigation Memory and Formal Record "
     "are distinct objects (Ch.8 §8.2 for the Room-specific case). Audio retention and transcript "
     "retention are separate decisions — raw audio storage is never assumed merely because "
     "transcription occurred."),
    ("review", [
        ("LEGAL", "Confirm audio/transcript retention periods and applicable privacy policy — this is the same open question already raised at NCIE-005 Ch.29 §29-review; not duplicated here as a new decision."),
        ("SECURITY", "Confirm cross-border processing boundaries for any voice/transcript content that could leave an approved jurisdiction via cloud STT/TTS processing (NCIE-004 Ch.18's provider eligibility applies)."),
    ]),
    ("trace", "NCIE-003 Ch.14 §14.6, Ch.36; NCIE-005 Ch.29."),
]

# ---------------------------------------------------------------------------
# Chapter 27 — Memory Provenance, Attribution & Audit
# ---------------------------------------------------------------------------
BLOCKS[27] = [
    ("upstream", [
        ("NCIE-005", "Ch.27", "AI origin is preserved permanently; human modification never erases it; no private chain-of-thought is stored."),
    ]),
    ("h2", "27.1 Provenance Requirements"),
    ("p", "Material Memory/Knowledge objects preserve:"),
    ("bullets", [
        "Origin and Actor Type (human, ARGUS, workflow, source — always distinguishable).",
        "Source References; Created Time; Knowledge Time.",
        "Version; Classification; Review State.",
        "Correction/Supersession Relationships.",
    ]),
    ("h2", "27.2 No Chain-of-Thought Requirement"),
    ("p",
     "Memory is never designed to store private model chain-of-thought. Defensibility comes from "
     "persisted structured artifacts — Questions, Hypotheses, Assumptions, Contradictions, Evidence "
     "Gaps, Evidence References, Tool Results, ARGUS Contributions and Human Responses — matching "
     "NCIE-005 Ch.27 §27.2 exactly, restated here as a Memory-architecture constraint rather than an "
     "ARGUS behavioral one."),
    ("h2", "27.3 AI-Generated Summaries"),
    ("p",
     "An ARGUS-generated Memory summary retains ARGUS Origin, Source References, Generation Time, "
     "applicable temporal cutoff, and Validation/Review State where required. Human adoption never "
     "erases AI provenance. A dependent summary whose underlying Memory materially changes supports "
     "STALE/REFRESH_REQUIRED rather than remaining silently presented as current."),
    ("h2", "27.4 Historical Prompt-Injection Boundary"),
    ("p",
     "Stored Conversation, Document, Evidence, Knowledge Candidate or Historical Note content may "
     "contain malicious instructions. Such content remains data — it never becomes executable ARGUS "
     "instruction merely because it is retrieved from Memory (NCIE-002 Ch.24 §24.4's ingestion "
     "principle applies identically to retrieval from Memory)."),
    ("trace", "NCIE-002 Ch.24 §24.4; NCIE-005 Ch.27."),
]

# ---------------------------------------------------------------------------
# Chapter 28 — Retention, Legal Hold, Archival & Secure Disposition
# ---------------------------------------------------------------------------
BLOCKS[28] = [
    ("upstream", [
        ("NCIE-003", "Ch.31", "Classification/privacy/retention taxonomy is canonical; this chapter applies class-specific retention to each of Chapter 3's nine Memory classes."),
    ]),
    ("h2", "28.1 Class-Specific Retention"),
    ("p",
     "No universal Memory retention period exists. Each Memory class (Ch.3 §3.2) has its own "
     "retention policy hook; where the institutional/legal period is unknown, it is classified LEGAL/"
     "POLICY CONFIRMATION REQUIRED, never invented."),
    ("h2", "28.2 Holds Override Disposition"),
    ("p",
     "LEGAL HOLD, REGULATORY HOLD, INVESTIGATION HOLD and RECORDS HOLD override ordinary disposition "
     "for any Memory object they apply to, exactly as NCIE-003 Ch.31 §31.5 requires for canonical "
     "data generally."),
    ("h2", "28.3 Derived Deletion"),
    ("p",
     "Where an object is lawfully destroyed, its Search Index entry, Vector Embedding, Cache entry, "
     "Graph Materialization and Snippet are addressed explicitly — primary data is never deleted "
     "while retrievable derived copies remain unintentionally (NCIE-003 Ch.31 §31.4's Deletion "
     "Propagation mechanism applies to every derived Memory representation)."),
    ("h2", "28.4 Personal Memory Deletion Boundary"),
    ("p",
     "Deletion of eligible personal Conversation or Preference Memory never silently destroys "
     "independent Formal Records, Decision Evidence, Room Records, Investigation Records or Audit "
     "Records that have a separate lawful institutional basis."),
    ("review", [
        ("LEGAL", "Confirm retention periods per Memory class (Ch.3 §3.2) with NCA Legal/Records Management; none is assumed."),
        ("LEGAL", "Confirm how personal deletion rights interact with institutional records obligations where they may conflict — no universal precedence is assumed."),
    ]),
    ("trace", "NCIE-003 Ch.31."),
]

# ---------------------------------------------------------------------------
# Chapter 29 — Memory Storage Architecture & Canonical/Derived Stores
# ---------------------------------------------------------------------------
BLOCKS[29] = [
    ("upstream", [
        ("NCIE-004", "Ch.11-17", "Transactional/analytical/object/search/graph/vector/cache store roles are engineering-governed; this chapter assigns Memory's logical role to each without naming a product."),
    ]),
    ("h2", "29.1 Logical Memory Storage Architecture"),
    ("rel",
     [
        ("Transactional Memory Metadata", "canonical for", "Memory Object identity, state, provenance"),
        ("Object/Document Store", "canonical for", "Room transcripts, briefing artifacts, large content bodies"),
        ("Historical/Analytical Store", "derived, rebuildable, canonical for", "bitemporal historical query (Ch.12)"),
        ("Knowledge Graph", "derived, canonical for", "typed Memory/Knowledge relationships (Ch.21)"),
        ("Search Index / Vector Index", "derived, rebuildable, never independently canonical", "discovery and semantic retrieval (Ch.23-24)"),
        ("Snapshot/Immutable Archive", "canonical, append-only for", "Decision-Time Snapshots and Room Snapshots (Ch.11, Ch.8)"),
        ("Cache", "derived, ephemeral accelerator over", "all of the above"),
     ],
     "Logical Memory Storage Architecture — canonical vs derived roles; no alternate truth exists in a derived store."),
    ("h2", "29.2 Technology Neutrality"),
    ("p",
     "This chapter specifies logical roles only. Physical technology selection remains governed by "
     "NCIE-004's Technology Decision Matrix; a technology named there retains its existing approval "
     "status when referenced here — this document never promotes a Proposed Design Default to "
     "Approved merely by using it in an example (NCIE-004 Ch.33 §33.1A's invariant applies "
     "identically)."),
    ("trace", "NCIE-004 Ch.11-17, Ch.33."),
]

# ---------------------------------------------------------------------------
# Chapter 30 — Memory APIs, Events & Service Contracts
# ---------------------------------------------------------------------------
BLOCKS[30] = [
    ("upstream", [
        ("NCIE-004", "Ch.8-9", "API/event contract engineering is governed upstream; this chapter defines the logical capability set those contracts must expose."),
    ]),
    ("h2", "30.1 Service Capabilities"),
    ("bullets", [
        "GetCurrentContext, GetHistoricalContext, GetDecisionTimeContext — the three retrieval modes (Ch.23) as distinct calls, never one undifferentiated \"get memory\" endpoint.",
        "SearchMemory — authorization- and mode-aware (Ch.23).",
        "ReconcileMemory — invokes Ch.13's reconciliation flow explicitly.",
        "CreateKnowledgeCandidate, ReviewKnowledgeCandidate, ChallengeKnowledge, SupersedeKnowledge, RetractKnowledge — one call per lifecycle transition (Ch.18, Ch.20), never one generic \"update knowledge\" call.",
    ]),
    ("p", "Names may be normalized during downstream implementation (NCIE-011); the capability "
         "boundaries above are what must not be collapsed."),
    ("h2", "30.2 Material Events"),
    ("bullets", [
        "MemoryCreated, MemoryCorrected, MemoryInvalidated.",
        "KnowledgeCandidateCreated, KnowledgeApproved, KnowledgeChallenged, KnowledgeSuperseded, KnowledgeRetracted.",
        "DecisionSnapshotCreated.",
        "ReconciliationRequired.",
    ]),
    ("p",
     "Event payloads reference sensitive objects rather than copying them unnecessarily (NCIE-003 "
     "Ch.28 §28.2's data-minimization pattern applies identically to Memory events)."),
    ("trace", "NCIE-004 Ch.8-9; NCIE-003 Ch.28."),
]
