"""Content model for NCIE-006 Memory & Context Architecture Specification.

CHAPTERS populated in batches (1-6, 7-12, 13-18, 19-24, 25-30, 31-34, 35-36).
Block kinds consumed by ncie006_common.render_blocks:
  ("h2", text) / ("h3", text) / ("p", text) / ("bullets", [items])
  ("upstream", [(doc_id, ref, consequence), ...]) / ("voice", text)
  ("proposed", text) / ("trace", text) / ("review", [items])
  ("flow", [nodes], caption) / ("rel", [(s,r,t), ...], caption)
  ("table", headers, rows, caption, status_col_index_or_None)
"""

CHAPTER_TITLES = {
    1: "Memory & Context Mandate, Authority Chain & Specification Boundary",
    2: "Memory Doctrine, Invariants & Epistemic Boundaries",
    3: "Memory Class Taxonomy",
    4: "Context Taxonomy & Context Envelope",
    5: "Conversation Memory",
    6: "User Preference Memory",
    7: "Workspace & Session Continuity Memory",
    8: "Collaborative Room Memory",
    9: "Investigation Memory",
    10: "Situation Memory",
    11: "Decision Memory & Decision-Time Context",
    12: "Historical Memory & Bitemporal Reconstruction",
    13: "Current-State Reconciliation",
    14: "Context Assembly & Minimum-Necessary Retrieval",
    15: "Context Propagation Across Services & Workflows",
    16: "Private, Shared & Institutional Context Boundaries",
    17: "ARGUS Memory Retrieval Interface",
    18: "Institutional Knowledge Candidate Lifecycle",
    19: "Institutional Knowledge Versioning, Applicability & Review",
    20: "Knowledge Challenge, Contradiction & Impact Analysis",
    21: "Knowledge Graph Context & Memory Relationships",
    22: "Dependency Graph & Downstream Impact Tracking",
    23: "Memory Search, Retrieval Modes & Ranking",
    24: "Semantic Memory & Vector Retrieval Boundaries",
    25: "Memory Security, Authorization & Zero-Trust Controls",
    26: "Sensitive Memory, Protected Identity & Voice Context",
    27: "Memory Provenance, Attribution & Audit",
    28: "Retention, Legal Hold, Archival & Secure Disposition",
    29: "Memory Storage Architecture & Canonical/Derived Stores",
    30: "Memory APIs, Events & Service Contracts",
    31: "Scalability, Tiering, Performance & Observability",
    32: "Resilience, Backup, Recovery & Post-Restore Reconciliation",
    33: "Legacy Memory Migration & Historical Identity Resolution",
    34: "Memory & Context Testing, Verification & Acceptance",
    35: "Human Review Register, Open Decisions & Proposed Defaults",
    36: "Requirements Traceability, Acceptance & Handover Gate",
}

CHAPTER_SCOPE = {
    1: "Establish NCIE-006 as the detailed Memory/Context authority without redefining upstream architecture.",
    2: "Lock Memory ≠ Evidence, Memory ≠ Current Truth, Memory ≠ Institutional Knowledge, Knowledge ≠ Rule, and ARGUS ≠ Memory.",
    3: "Define Conversation, Preference, Workspace, Room, Investigation, Situation, Historical, Decision and Institutional Knowledge memory.",
    4: "Define purpose-bounded, authorized, temporal, provenance-aware context passed among users, services, tools and ARGUS.",
    5: "Specify low-authority conversational continuity, retention, summaries and invalidation.",
    6: "Define permitted low-risk preferences without allowing preferences to change authority or truth.",
    7: "Preserve resumable individual work state independently of runtime sessions.",
    8: "Persist structured multi-user reasoning independently of the raw transcript.",
    9: "Preserve investigative evidence relationships, hypotheses, contradictions, gaps, tasks and human judgments.",
    10: "Preserve evolving Situation context, timelines and cross-domain analytical state.",
    11: "Preserve high-integrity snapshots of what was known when consequential human Decisions were made.",
    12: "Implement occurrence/effective time and knowledge/record time for defensible historical reconstruction.",
    13: "Reconcile remembered state against authoritative current domain state before consequential reuse.",
    14: "Assemble only authorized, relevant and purpose-bounded context for humans, ARGUS and tools.",
    15: "Propagate canonical context without propagating permissions or corrupting temporal meaning.",
    16: "Govern movement from private context to Room-shared context and ultimately to reviewed institutional knowledge.",
    17: "Define governed Memory Service interfaces consumed by ARGUS without giving ARGUS unrestricted institutional memory access.",
    18: "Define how lessons and reusable insights become governed Knowledge Candidates.",
    19: "Define scope, effective period, limitations, review, challenge, supersession and retraction.",
    20: "Handle conflicts between current evidence and approved knowledge through explicit review and downstream impact analysis.",
    21: "Use canonical graph relationships for memory/knowledge without converting connectivity into fact, cause or culpability.",
    22: "Track typed dependencies so corrections and invalidations expose affected downstream artifacts.",
    23: "Define Current, Historical and Decision-Time search with authority- and applicability-aware ranking.",
    24: "Use embeddings for discovery without making vector representations Evidence or Institutional Knowledge.",
    25: "Apply object-, purpose-, classification- and temporal-aware authorization to all memory classes.",
    26: "Govern Protected Identity, Anti-Fraud location, voice transcripts/audio and other heightened-sensitivity context.",
    27: "Preserve human, ARGUS, workflow and source origins plus material retrieval and lifecycle audit.",
    28: "Define differentiated retention, hold, archive and deletion behavior including derived artifacts.",
    29: "Define transactional, object, analytical, graph, search/vector and immutable storage roles without creating alternate truth.",
    30: "Define stable retrieval, reconciliation, historical-state and knowledge-lifecycle interfaces and events.",
    31: "Define Hot/Warm/Cold tiering, retrieval SLOs, index health, reconciliation monitoring and governance metrics.",
    32: "Recover Memory/Knowledge without reactivating superseded state or rewriting original knowledge time.",
    33: "Import historical records with source/transformation provenance and explicit ambiguous-identity handling.",
    34: "Test memory classes, bitemporality, reconciliation, authorization, knowledge lifecycle, deletion, recovery and model replacement.",
    35: "Consolidate every unresolved Memory/Context decision with category, owner and blocking status.",
    36: "Crosswalk NCIE-006 to NCIE-002-005 and define controlled acceptance and handover to NCIE-007.",
}

# Chapters that materially discuss voice-derived memory (NCIE-005 inheritance).
VOICE_CHAPTERS = {8, 26}

GOVERNING_INVARIANTS = [
    "ARGUS ≠ INSTITUTIONAL MEMORY.",
    "MEMORY ≠ CURRENT TRUTH.",
    "MEMORY ≠ EVIDENCE.",
    "MEMORY ≠ INSTITUTIONAL KNOWLEDGE.",
    "INSTITUTIONAL KNOWLEDGE ≠ RULE.",
    "CURRENT STATE ≠ HISTORICAL STATE ≠ DECISION-TIME STATE.",
    "SEMANTIC SIMILARITY ≠ AUTHORITY OR PRECEDENT.",
    "MODEL REPLACEMENT ≠ MEMORY RESET.",
    "PRIVATE CONTEXT ≠ SHARED CONTEXT.",
    "CONTEXT PROPAGATION ≠ PERMISSION PROPAGATION.",
    "REMEMBERED AUTHORIZATION ≠ CURRENT AUTHORIZATION.",
    "PRIOR HUMAN DECISION ≠ CURRENT ACTION AUTHORITY.",
]

FRONT_MATTER = {
    "governance_rows": [
        ("Document", "NCIE-006 Memory & Context Architecture Specification"),
        ("Edition", "In development — Version 1.1"),
        ("Baseline authorized", "NCIE-006 Skeletal v0.1 — approved for full expansion; 36-chapter structure locked"),
        ("Requirements authority", "NCIE-001 Master Product Requirements Document, Version 1.2"),
        ("Architecture authority", "NCIE-002 System Architecture & Technical Design, Version 0.4"),
        ("Canonical data authority", "NCIE-003 Data Model & Data Dictionary, Version 0.3 (Canonical Data Architecture Baseline)"),
        ("Engineering baseline", "NCIE-004 Technology Stack & Engineering Blueprint, Version 1.1 (Approved Engineering Baseline)"),
        ("ARGUS behavioral authority", "NCIE-005 ARGUS Intelligence Assistant Specification, Version 1.2"),
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
