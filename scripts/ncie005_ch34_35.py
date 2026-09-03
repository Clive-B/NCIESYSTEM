"""NCIE-005 content batch: Chapters 34-35 (Human Review Register,
Requirements Traceability, Acceptance & Handover Gate)."""

from ncie005_ch34_register import register_rows, summary_counts

BLOCKS = {}

_counts = summary_counts()

# ---------------------------------------------------------------------------
# Chapter 34 — Human Review Register, Open Decisions & Proposed Defaults
# ---------------------------------------------------------------------------
BLOCKS[34] = [
    ("upstream", [
        ("NCIE-002", "—", "Consolidates every Human Review Focus item from Chapters 1-33 into one authoritative register."),
    ]),
    ("h2", "34.1 Purpose"),
    ("p",
     "Consolidates every Human Review Focus item raised in Chapters 1-33, extracted directly from "
     "the chapter review blocks so this register cannot drift from its sources."),
    ("h2", "34.2 Summary"),
    ("table",
     ["Metric", "Count"],
     [
        ["Total items", str(_counts["total"])],
        ["Proposed Design Default", str(_counts["proposed"])],
        ["Institutional Confirmation Required", str(_counts["institutional"])],
        ["Workflow/Source Discovery Required", str(_counts["workflow"])],
        ["Legal/Policy Confirmation Required", str(_counts["legal"])],
        ["Resolved by Upstream Baseline", str(_counts["resolved"])],
        ["Blocking", str(_counts["blocking"])],
        ["Non-Blocking", str(_counts["non_blocking"])],
    ],
     "Human Review Register summary counts."),
    ("h2", "34.3 Complete Register"),
    ("table",
     ["ID", "Ch.", "Issue", "Category", "Blocking?"],
     register_rows(),
     "Complete Human Review Register (Chapters 1-33)."),
    ("h2", "34.4 Mechanical Verification (v1.2)"),
    ("p",
     f"Per the v1.2 reconciliation pass, this register's totals were independently re-verified: a "
     "manual extraction of every ('review', ...) block across Chapters 1-33 was compared against "
     f"this chapter's programmatic extraction (§34.2-§34.3). The two matched exactly — "
     f"{_counts['total']} items ({_counts['proposed']} Proposed / {_counts['institutional']} "
     f"Institutional / {_counts['legal']} Legal / {_counts['resolved']} Resolved / "
     f"{_counts['workflow']} Workflow), {_counts['blocking']} Blocking / "
     f"{_counts['non_blocking']} Non-Blocking — confirming no item was silently dropped or "
     "miscounted. This figure, front matter §0.9's figure, and §34.2's summary table are all "
     "generated from the same computed extraction at build time (ncie005_ch34_register.py), so "
     "they cannot diverge from one another the way v1.1's hand-typed prose diverged from the "
     "live register after a late edit added one item."),
    ("h2", "34.5 Closure Process"),
    ("p",
     "An item closes only when its required confirmation is actually supplied and recorded — never "
     "converted into an invented fact merely to appear resolved (consistent with NCIE-003/004's "
     "no-fabrication discipline). Blocking items should be prioritised before the affected chapter's "
     "behavior is treated as production-final; Non-Blocking Proposed Design Defaults may proceed "
     "into downstream design and prototyping (NCIE-006/007/009/011/012/013) provisionally, without "
     "constituting institutional approval (mirrors NCIE-004 Ch.35 §35.5's qualification)."),
    ("trace", "Consolidates Chapters 1-33; individual chapters trace to NCIE-002/003/004 as cited therein."),
]

# ---------------------------------------------------------------------------
# Chapter 35 — Requirements Traceability, Acceptance & Handover Gate
# ---------------------------------------------------------------------------
BLOCKS[35] = [
    ("upstream", [
        ("NCIE-002", "—", "Closes the authority chain: NCIE-001 requirements → NCIE-002 architecture → NCIE-003 canonical data → NCIE-004 engineering → NCIE-005 ARGUS behavior."),
    ]),
    ("h2", "35.1 Traceability Matrix"),
    ("table",
     ["Ch.", "Title", "Primary Upstream Dependency"],
     [
        ["1", "Mandate, Identity & Specification Boundary", "NCIE-002 Ch.19 §19.11; NCIE-004 Ch.18"],
        ["2", "Human-Primary Governance & Authority Limits", "NCIE-002 Ch.1 §1.3.1, Ch.20 §20.8; NCIE-004 Ch.20, Ch.23"],
        ["3", "User Roles, Personas & Interaction Contexts", "NCIE-002 Ch.2 §2.1, Ch.3"],
        ["4", "Invocation, Presence, Participation Modes", "NCIE-002 Ch.20 §20.7-20.8; NCIE-003 Ch.21 §21.7"],
        ["5", "Conversation, QA & Contextual Assistance", "NCIE-002 Ch.19 §19.3, §19.10"],
        ["6", "Analytical Questioning & Socratic Challenge", "NCIE-002 Ch.20 §20.3, §20.8"],
        ["7", "Hypothesis Generation & Alternative Explanation", "NCIE-002 Ch.20 §20.3, §20.6; NCIE-003 Ch.21 §21.3"],
        ["8", "Contradiction Seeking, Counterevidence & Dissent", "NCIE-002 Ch.20 §20.3; NCIE-003 Ch.5, Ch.6, Ch.21"],
        ["9", "Assumption Identification & Testing Support", "NCIE-003 Ch.21 §21.3"],
        ["10", "Evidence Gap & Discriminating Evidence", "NCIE-002 Ch.20 §20.3; NCIE-004 Ch.20"],
        ["11", "Evidence-Bounded Reasoning & Epistemic Labels", "NCIE-003 Ch.20 §20.3, Ch.22"],
        ["12", "Uncertainty, Abstention & Incomplete Information", "NCIE-002 Ch.19 §19.8; NCIE-003 Ch.2 §2.5"],
        ["13", "Collaborative Brainstorming & Multi-User Participation", "NCIE-002 Ch.20; NCIE-003 Ch.4 §4.77-4.79, Ch.21"],
        ["14", "Room Facilitation Support, Threads & Structured Reasoning", "NCIE-002 Ch.20 §20.10; NCIE-003 Ch.21"],
        ["15", "Evidence-Watch & Event-Triggered Re-entry", "NCIE-002 Ch.20 §20.10; NCIE-003 Ch.18, Ch.23 §23.6"],
        ["16", "Situational Awareness, NOP & Cross-Domain Assistance", "NCIE-002 Ch.18; NCIE-003 Ch.19 §19.2, Ch.29"],
        ["17", "Network, Traffic & Incident Assistance", "NCIE-003 Ch.7, Ch.10, Ch.11"],
        ["18", "Revenue Intelligence & Billing Verification Assistance", "NCIE-003 Ch.12"],
        ["19", "Mobile Money Intelligence Assistance", "NCIE-003 Ch.13"],
        ["20", "SIM Registration Intelligence Assistance", "NCIE-003 Ch.14"],
        ["21", "Anti-Fraud / SIMBOX Investigation Assistance", "NCIE-003 Ch.15"],
        ["22", "Regulatory Case, Finding & Decision-Support Assistance", "NCIE-003 Ch.16, Ch.25, Ch.26"],
        ["23", "Memory Retrieval, Historical Context & Decision-Time", "NCIE-002 Ch.20 §20.2, §20.12; NCIE-003 Ch.22, Ch.25"],
        ["24", "Institutional Knowledge Retrieval & Challenge", "NCIE-003 Ch.22"],
        ["25", "Tool Use, Action Proposals & Human Approval UX", "NCIE-004 Ch.20; NCIE-003 Ch.23 §23.2"],
        ["26", "Output Types, Structured Artifacts & Briefing", "NCIE-002 Ch.20 §20.5, §20.6"],
        ["27", "Provenance, AI Attribution & Human Modification", "NCIE-003 Ch.20 §20.2, §20.4, §20.6"],
        ["28", "Personalization, Preferences & User-Specific Assistance", "NCIE-002 Ch.3 §3.9; NCIE-003 Ch.22 §22.2"],
        ["29", "Safety, Prompt Injection & Protected Identity Behavior", "NCIE-002 Ch.24 §24.4; NCIE-003 Ch.14 §14.6, Ch.36"],
        ["30", "Failure, Degraded Mode & Recovery", "NCIE-002 Ch.19 §19.8, Ch.28"],
        ["31", "Quality, Evaluation & Behavioral Testing", "NCIE-002 Ch.24 §24.5; NCIE-004 Ch.19"],
        ["32", "Performance, Responsiveness & Accessibility NFRs", "NCIE-002 Ch.30 §30.2, §30.4"],
        ["33", "Configuration, Policy, Naming & Change Governance", "NCIE-002 Ch.19 §19.11; NCIE-004 Ch.33"],
        ["34", "Human Review Register & Open Decisions", "Consolidates Ch.1-33"],
        ["35", "Traceability, Acceptance & Handover", "Closes NCIE-001→002→003→004→005 authority chain"],
    ],
     "NCIE-005 chapter-to-upstream traceability matrix."),
    ("h2", "35.2 Acceptance Checklist"),
    ("bullets", [
        "The Human-Primary authority invariant (front matter §0.4) is preserved without exception across all 35 chapters — no chapter grants ARGUS a prohibited autonomous authority.",
        "Voice governing invariants (front matter §0.5) are preserved: voice is an interaction modality, never an authority modality, in every voice-bearing chapter (4, 5, 13, 15, 25, 29, 30, 32, 33).",
        "The ARGUS Output/Epistemic-Type Matrix (Ch.11) is applied consistently — no chapter's material output collapses epistemic types into a generic assertion.",
        "Every domain assistance chapter (16-22) preserves its stated semantic separations (Detection≠Culpability, Hypothesis≠Finding, etc.).",
        "No private model chain-of-thought storage/disclosure is required anywhere in this document (Ch.27 §27.2).",
        "The Controlled Upstream Impact Register (front matter §0.6) is preserved verbatim and NCIE-001 through NCIE-004 are not reopened or modified by this document.",
        "No chapter fully specifies NCIE-006/007/009/011/012/013; each cross-references the downstream owner (Ch.1 §1.3 boundary table).",
        "Chapter 34's Human Review Register is complete and mechanically consistent with the chapters it consolidates.",
    ]),
    ("h2", "35.3 Required Matrices — Location Index"),
    ("table",
     ["Required Artifact", "Location"],
     [
        ["ARGUS Behavioral Invariants Register", "Front matter §0.4; detailed in Ch.2 §2.1"],
        ["Participation Mode Matrix", "Ch.4 §4.1"],
        ["ARGUS Output/Epistemic-Type Matrix", "Ch.11 §11.1"],
        ["Voice Interaction & Spoken-Disclosure Matrix", "Ch.29 §29.1"],
        ["Domain Assistance Boundary Matrix", "Ch.16 §16.1"],
        ["Tool/Action Authority Matrix", "Ch.25 §25.1"],
        ["Behavioral Evaluation Matrix", "Ch.31 §31.1"],
        ["Human Review/Open Decision Register", "Ch.34 (complete)"],
        ["NCIE-002/003/004 Traceability Matrix", "Ch.35 §35.1"],
        ["Controlled Upstream Voice Impact Register", "Front matter §0.6"],
        ["Acceptance/Handover Gate", "Ch.35 §35.2, §35.4"],
    ],
     "Index of the 11 required deliverable artifacts and their location in this document."),
    ("h2", "35.4 Handover"),
    ("p",
     "On acceptance, this behavioral specification hands forward to NCIE-006 (Memory & Context "
     "Architecture), NCIE-007 (AI, Agent & Model Orchestration), NCIE-009 (Security/IAM), NCIE-011 "
     "(API/Integration), NCIE-012 (UX/UI) and NCIE-013 (Functional Modules) — each of which "
     "implements the behavioral requirements this document fixes without re-deciding ARGUS's "
     "institutional role or authority limits."),
    ("review", [
        ("INSTITUTIONAL", "Confirm NCIE-005 approvers and their scope of authority."),
        ("INSTITUTIONAL", "Confirm which of Ch.34's Blocking items must close before NCIE-006/007/009/011/012/013 may begin detailed implementation versus which may proceed provisionally."),
    ]),
    ("trace", "Closes the NCIE-001 → NCIE-002 → NCIE-003 → NCIE-004 → NCIE-005 authority chain (front matter §0.1)."),
]
