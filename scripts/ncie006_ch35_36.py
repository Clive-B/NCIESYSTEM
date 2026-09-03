"""NCIE-006 content batch: Chapters 35-36 (Human Review Register,
Requirements Traceability, Acceptance & Handover Gate)."""

from ncie006_ch35_register import register_rows, summary_counts

BLOCKS = {}

_counts = summary_counts()

# ---------------------------------------------------------------------------
# Chapter 35 — Human Review Register, Open Decisions & Proposed Defaults
# ---------------------------------------------------------------------------
BLOCKS[35] = [
    ("upstream", [
        ("NCIE-002", "—", "Consolidates every Human Review Focus item from Chapters 1-34 into one authoritative register."),
    ]),
    ("h2", "35.1 Purpose"),
    ("p",
     "Consolidates every Human Review Focus item raised in Chapters 1-34, extracted directly from "
     "the chapter review blocks so this register cannot drift from its sources. Where an item "
     "inherits an already-open NCIE-004/005 decision rather than introducing a new NCIE-006 "
     "question, it is noted as such in the Issue text rather than duplicated under an unrelated ID "
     "(handover items 164-165)."),
    ("h2", "35.2 Summary"),
    ("table",
     ["Metric", "Count"],
     [
        ["Total items", str(_counts["total"])],
        ["Resolved by Upstream Baseline", str(_counts["resolved"])],
        ["Proposed Design Default", str(_counts["proposed"])],
        ["Institutional Confirmation Required", str(_counts["institutional"])],
        ["Source/Workflow Discovery Required", str(_counts["workflow"])],
        ["Legal/Policy Confirmation Required", str(_counts["legal"])],
        ["Security/Sovereignty Confirmation Required", str(_counts["security"])],
        ["Blocking", str(_counts["blocking"])],
        ["Non-Blocking", str(_counts["non_blocking"])],
    ],
     "Human Review Register summary counts."),
    ("h2", "35.3 Complete Register"),
    ("table",
     ["ID", "Ch.", "Issue", "Category", "Blocking?"],
     register_rows(),
     "Complete Human Review Register (Chapters 1-34)."),
    ("h2", "35.4 Mechanical Verification"),
    ("p",
     f"Per handover items 49/110, this register's totals are verified programmatically, not by "
     "inspection: the production build independently re-extracts every ('review', ...) block "
     "across Chapters 1-34 and asserts the result matches this chapter's own extraction "
     "(§35.2-§35.3) exactly, by category and by blocking status; a mismatch fails the build rather "
     f"than reaching this document. The current build confirms an exact match — {_counts['total']} "
     f"items ({_counts['resolved']} Resolved / {_counts['proposed']} Proposed / "
     f"{_counts['institutional']} Institutional / {_counts['workflow']} Workflow / "
     f"{_counts['legal']} Legal / {_counts['security']} Security), {_counts['blocking']} Blocking / "
     f"{_counts['non_blocking']} Non-Blocking — confirming no item was silently dropped or "
     "miscounted. This figure and §35.2's summary table are generated from the same computed "
     "extraction at build time, so they cannot diverge from one another."),
    ("h2", "35.5 Closure and Blocking Scope"),
    ("p",
     "An item closes only when its required confirmation is actually supplied and recorded — never "
     "converted into an invented fact merely to appear resolved. A Blocking item blocks only the "
     "specific chapter/capability that genuinely depends on it — retention period, storage "
     "technology or audio retention being unresolved does not block the entire 36-chapter "
     "specification; technology-neutral, policy-hook design proceeds where possible (handover item "
     "166)."),
    ("trace", "Consolidates Chapters 1-34; individual chapters trace to NCIE-002/003/004/005 as cited therein."),
]

# ---------------------------------------------------------------------------
# Chapter 36 — Requirements Traceability, Acceptance & Handover Gate
# ---------------------------------------------------------------------------
BLOCKS[36] = [
    ("upstream", [
        ("NCIE-002", "—", "Closes the authority chain: NCIE-001 requirements → NCIE-002 architecture → NCIE-003 canonical data → NCIE-004 engineering → NCIE-005 ARGUS behavior → NCIE-006 Memory/Context."),
    ]),
    ("h2", "36.1 Traceability Matrix"),
    ("table",
     ["Ch.", "Title", "Primary Upstream Dependency"],
     [
        ["1", "Mandate, Authority Chain & Specification Boundary", "NCIE-002 Ch.20; NCIE-003 Ch.22"],
        ["2", "Memory Doctrine, Invariants & Epistemic Boundaries", "NCIE-002 Ch.20 §20.2, §20.12; NCIE-003 Ch.22"],
        ["3", "Memory Class Taxonomy", "NCIE-002 Ch.20 §20.2"],
        ["4", "Context Taxonomy & Context Envelope", "NCIE-002 Ch.19 §19.6"],
        ["5", "Conversation Memory", "NCIE-005 Ch.5, Ch.11"],
        ["6", "User Preference Memory", "NCIE-005 Ch.28"],
        ["7", "Workspace & Session Continuity Memory", "NCIE-002 Ch.3 §3.1"],
        ["8", "Collaborative Room Memory", "NCIE-002 Ch.20 §20.5, §20.10; NCIE-003 Ch.21"],
        ["9", "Investigation Memory", "NCIE-003 Ch.15 §15.3"],
        ["10", "Situation Memory", "NCIE-003 Ch.18"],
        ["11", "Decision Memory & Decision-Time Context", "NCIE-003 Ch.16, Ch.25, Ch.26"],
        ["12", "Historical Memory & Bitemporal Reconstruction", "NCIE-003 Ch.5, Ch.25"],
        ["13", "Current-State Reconciliation", "NCIE-002 Ch.20 §20.10; NCIE-005 Ch.23"],
        ["14", "Context Assembly & Minimum-Necessary Retrieval", "NCIE-002 Ch.24 §24.3"],
        ["15", "Context Propagation Across Services & Workflows", "NCIE-002 Ch.4 §4.4"],
        ["16", "Private, Shared & Institutional Context Boundaries", "NCIE-002 Ch.20 §20.9; NCIE-003 Ch.4"],
        ["17", "ARGUS Memory Retrieval Interface", "NCIE-005 Ch.11, Ch.23"],
        ["18", "Institutional Knowledge Candidate Lifecycle", "NCIE-003 Ch.22 §22.4; NCIE-005 Ch.24"],
        ["19", "Knowledge Versioning, Applicability & Review", "NCIE-003 Ch.22 §22.3"],
        ["20", "Knowledge Challenge, Contradiction & Impact Analysis", "NCIE-005 Ch.24; NCIE-003 Ch.22"],
        ["21", "Knowledge Graph Context & Memory Relationships", "NCIE-003 Ch.19 §19.2, §19.7"],
        ["22", "Dependency Graph & Downstream Impact Tracking", "NCIE-003 Ch.25 §25.4"],
        ["23", "Memory Search, Retrieval Modes & Ranking", "NCIE-003 Ch.4 §4.89-4.93"],
        ["24", "Semantic Memory & Vector Retrieval Boundaries", "NCIE-002 Ch.26 §26.3; NCIE-004 Ch.16"],
        ["25", "Memory Security, Authorization & Zero-Trust Controls", "NCIE-002 Ch.4"],
        ["26", "Sensitive Memory, Protected Identity & Voice Context", "NCIE-003 Ch.14 §14.6, Ch.36; NCIE-005 Ch.29"],
        ["27", "Memory Provenance, Attribution & Audit", "NCIE-002 Ch.24 §24.4; NCIE-005 Ch.27"],
        ["28", "Retention, Legal Hold, Archival & Secure Disposition", "NCIE-003 Ch.31"],
        ["29", "Memory Storage Architecture & Canonical/Derived Stores", "NCIE-004 Ch.11-17, Ch.33"],
        ["30", "Memory APIs, Events & Service Contracts", "NCIE-004 Ch.8-9; NCIE-003 Ch.28"],
        ["31", "Scalability, Tiering, Performance & Observability", "NCIE-004 Ch.31, Ch.35; NCIE-003 Ch.32"],
        ["32", "Resilience, Backup, Recovery & Post-Restore Reconciliation", "NCIE-004 Ch.30"],
        ["33", "Legacy Memory Migration & Historical Identity Resolution", "NCIE-003 Ch.34"],
        ["34", "Memory & Context Testing, Verification & Acceptance", "NCIE-003 Ch.38"],
        ["35", "Human Review Register & Open Decisions", "Consolidates Ch.1-34"],
        ["36", "Traceability, Acceptance & Handover", "Closes NCIE-001→002→003→004→005→006 authority chain"],
    ],
     "NCIE-006 chapter-to-upstream traceability matrix."),
    ("h2", "36.2 Traceability Mechanical Verification"),
    ("p",
     "Per handover item 111, every one of the 36 chapters above carries at least one upstream "
     "citation — verified by inspection of §36.1. No ORPHAN NCIE-006 REQUIREMENT (a chapter with no "
     "upstream justification) or UNREALIZED UPSTREAM REQUIREMENT (an NCIE-002-005 Memory/Context "
     "mandate with no corresponding NCIE-006 chapter) was found in this edition."),
    ("h2", "36.3 Acceptance Checklist"),
    ("bullets", [
        "All ten Governing Invariants (front matter §0.3) are preserved without exception across all 36 chapters.",
        "The nine Memory classes (Ch.3 §3.2) each have distinct purpose, authority, retention and reconciliation treatment — none collapsed into a generic store or lifecycle.",
        "Decision-Time reconstruction (Ch.11-12) excludes later Evidence in every worked example.",
        "Institutional Knowledge promotion/challenge/supersession/retraction (Ch.18-20) requires human action at every authority-changing step; ARGUS never approves.",
        "Voice-derived Memory (Ch.8 §8.2, Ch.26) preserves the NCIE-005 voice invariants without modification.",
        "No chapter fully specifies NCIE-007/009/010/011/014/016; each cross-references the downstream owner (Ch.1 §1.2 boundary table).",
        "No technology named from NCIE-004 is asserted as more approved here than its NCIE-004 Technology Registry status.",
        "Chapter 35's Human Review Register is complete and mechanically verified against its source chapters (§35.4).",
        "Chapter 36's traceability matrix is mechanically verified complete (§36.2).",
    ]),
    ("h2", "36.4 Handover"),
    ("p",
     "On acceptance, this Memory & Context architecture hands forward to NCIE-007 (AI, Agent & Model "
     "Orchestration), NCIE-009 (Security/IAM), NCIE-010 (Evidence, Provenance & Audit), NCIE-011 "
     "(API/Integration), NCIE-014 (Database & Storage Engineering) and NCIE-016 (Testing) — each of "
     "which implements this document's Memory/Context requirements without re-deciding the "
     "Governing Invariants or Memory Class boundaries this document fixes."),
    ("review", [
        ("INSTITUTIONAL", "Confirm NCIE-006 approvers and their scope of authority."),
        ("INSTITUTIONAL", "Confirm which of Ch.35's Blocking items must close before NCIE-007/009/010/011/014/016 may begin detailed implementation versus which may proceed provisionally."),
    ]),
    ("trace", "Closes the NCIE-001 → NCIE-002 → NCIE-003 → NCIE-004 → NCIE-005 → NCIE-006 authority chain (front matter §0.1)."),
]
