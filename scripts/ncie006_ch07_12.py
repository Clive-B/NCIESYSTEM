"""NCIE-006 content batch: Chapters 7-12 (workspace/session continuity, room
memory, investigation memory, situation memory, decision memory, historical/
bitemporal reconstruction)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 7 — Workspace & Session Continuity Memory
# ---------------------------------------------------------------------------
BLOCKS[7] = [
    ("upstream", [
        ("NCIE-002", "Ch.3 §3.1", "Workspace layout/context state must survive across sessions independently of runtime session objects."),
    ]),
    ("h2", "7.1 Workspace Continuity"),
    ("p",
     "Workspace Memory preserves an individual's resumable work state — layout, active filters, "
     "open panels, last context — independently of any specific runtime session, browser tab or "
     "ARGUS conversation instance. A session ending does not destroy the workspace state a user "
     "would expect to resume."),
    ("h2", "7.2 Reconciliation on Resume"),
    ("p",
     "On resume, Workspace Memory is reconciled against current authoritative state (Ch.13) before "
     "being presented — a saved filter referencing a since-closed Investigation, for example, "
     "surfaces as CHANGED or SUPERSEDED rather than silently reopening stale context."),
    ("trace", "NCIE-002 Ch.3 §3.1."),
]

# ---------------------------------------------------------------------------
# Chapter 8 — Collaborative Room Memory
# ---------------------------------------------------------------------------
BLOCKS[8] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.5", "Room Memory persists structured reasoning objects, distinct from the raw transcript, per the Collaborative Reasoning State architecture."),
        ("NCIE-003", "Ch.21 §21.3", "Room, Thread, Question, Hypothesis, Assumption, Contradiction, Evidence Gap, Task, Human Judgment, Decision Point, ARGUS Intervention, Consensus, Dissent and Room Snapshot are canonical persistent objects."),
    ]),
    ("h2", "8.1 Room Memory Is Not a Transcript"),
    ("p",
     "Room Memory persists the structured analytical objects named above as first-class records — "
     "the raw message transcript may supplement this structure but never substitutes for it. A "
     "'summarize this room' request is answered from the structured objects, not by re-reading the "
     "transcript from scratch."),
    ("h2", "8.2 Voice-Derived Room Memory"),
    ("voice", "Where verbal Collaborative Intelligence is used, Raw Audio, Speech-to-Text Transcript, Structured Room Memory and Formal Record are distinct objects, never automatically the same thing. A transcript error never silently alters a persisted Hypothesis, Human Judgment, Decision Point or authorization. Where a material spoken contribution is mistranscribed, correction preserves the original transcript state where required, the corrected transcript, correcting actor, correction time, and the affected structured objects."),
    ("h2", "8.3 Room Snapshot and Cross-Session Continuity"),
    ("p",
     "A Room Snapshot captures the Collaborative Reasoning State at a point in time, enabling "
     "'where were we?' reconstruction by combining the snapshot with current authoritative state "
     "(never presenting a stale snapshot as current without reconciliation, Ch.13)."),
    ("review", [
        ("WORKFLOW", "Confirm audio retention policy specifics with NCA (inherits NCIE-005's open item on audio/transcript retention as a separate decision, per §0.2's no-duplication rule — see NCIE-005 Ch.29 §29 review)."),
    ]),
    ("trace", "NCIE-002 Ch.20 §20.5, §20.10; NCIE-003 Ch.21."),
]

# ---------------------------------------------------------------------------
# Chapter 9 — Investigation Memory
# ---------------------------------------------------------------------------
BLOCKS[9] = [
    ("upstream", [
        ("NCIE-003", "Ch.15 §15.3", "Investigation stage progression (Detection→Suspicion→Investigation→Validation→Blocking→Outcome) is canonical; Investigation Memory persists its working analytical state."),
    ]),
    ("h2", "9.1 Investigation Memory Behavior"),
    ("p",
     "Investigation Memory preserves evidence relationships, hypotheses, contradictions, evidence "
     "gaps, tasks and human judgments accumulated during an investigation, supporting pause/resume "
     "across sessions, shifts, users, ARGUS model changes and system restarts — resumption never "
     "depends on the original chat/session being available."),
    ("h2", "9.2 Sensitivity Inheritance"),
    ("p",
     "Investigation Memory tied to Anti-Fraud/SIMBOX work inherits sensitive-tier classification "
     "(NCIE-003 Ch.15, Ch.31) automatically; it is never treated as ordinary working-analysis memory "
     "merely because it uses the same underlying structure as Ch.8's Room Memory."),
    ("trace", "NCIE-003 Ch.15."),
]

# ---------------------------------------------------------------------------
# Chapter 10 — Situation Memory
# ---------------------------------------------------------------------------
BLOCKS[10] = [
    ("upstream", [
        ("NCIE-003", "Ch.18", "Situation is a canonical entity distinct from Condition/Alert/Investigation/Case; Situation Memory persists its evolving cross-domain analytical state."),
    ]),
    ("h2", "10.1 Situation Memory Behavior"),
    ("p",
     "Situation Memory preserves timelines and cross-domain analytical state across the Situation's "
     "lifecycle (NCIE-003 Ch.18), supporting the same pause/resume guarantees as Investigation "
     "Memory (Ch.9) — across sessions, shifts, users, model changes and restarts."),
    ("trace", "NCIE-003 Ch.18."),
]

# ---------------------------------------------------------------------------
# Chapter 11 — Decision Memory & Decision-Time Context
# ---------------------------------------------------------------------------
BLOCKS[11] = [
    ("upstream", [
        ("NCIE-003", "Ch.16 §16.3, Ch.25 §25.5", "Decision-Time Snapshot and Decision-Time Context are canonical; Decision Memory is their high-integrity persisted form."),
    ]),
    ("h2", "11.1 Decision Memory Contents"),
    ("p", "Decision Memory preserves, where applicable:"),
    ("bullets", [
        "Decision ID, Decision Authority, Decision Time.",
        "Decision-Time Snapshot (the bounded fact/evidence/rule-version set available at that timestamp).",
        "Evidence Available at Decision Time; Applicable Rule Versions.",
        "Known Hypotheses, Known Contradictions, Known Evidence Gaps at that time.",
        "Human Rationale; ARGUS Contribution (distinctly attributed, NCIE-005 Ch.27).",
        "Subsequent Review Relationship (appeal/reversal, linked forward, never rewriting the original).",
    ]),
    ("h2", "11.2 Decision-Time Definition"),
    ("p",
     "Decision-Time is formally defined here and referenced, not redefined, elsewhere in this "
     "document: the specific timestamp as of which a Decision's supporting context is bound. "
     "Reconstruction implements AS KNOWN AT T, never WHAT WE KNOW NOW ABOUT T — the system supports "
     "both views but never confuses them (Ch.12 covers the general bitemporal mechanism this relies "
     "on)."),
    ("h2", "11.3 Integrity Protection"),
    ("table",
     ["Requirement", "Behavior"],
     [
        ["Immutability", "A finalized Decision-Time Snapshot is protected against ordinary modification once created"],
        ["Subsequent events as new objects", "Correction/review/appeal/outcome are linked as subsequent objects/events, never rewrites of the original snapshot"],
        ["Sensitive-content access", "Access to a Decision record does not automatically grant access to every underlying restricted Evidence item (Ch.25); redacted/limited reconstruction is supported"],
        ["Outcome ≠ quality/causation", "A later-known outcome informs learning; it never automatically rewrites the historical assessment of whether the Decision was reasonable given what was known then"],
    ],
     "Decision Memory integrity requirements."),
    ("h2", "11.4 Prior Decision Is Never Automatic Current Authority"),
    ("p",
     "PRIOR HUMAN DECISION ≠ CURRENT ACTION AUTHORITY (front matter §0.3). A finalized Decision "
     "recorded in Decision Memory may inform current human reasoning — as precedent, context or "
     "pattern — but it is never automatically replayed as authorization for a new blocking, tracking, "
     "regulatory or other consequential action. A new consequential action requires its own current "
     "human Decision Authority and current Decision-Time context (§11.1-§11.2); ARGUS may surface a "
     "prior Decision as relevant context (NCIE-005 Ch.24) but never initiates or authorizes a new "
     "action on the strength of the prior Decision alone."),
    ("trace", "NCIE-003 Ch.16, Ch.25, Ch.26."),
]

# ---------------------------------------------------------------------------
# Chapter 12 — Historical Memory & Bitemporal Reconstruction
# ---------------------------------------------------------------------------
BLOCKS[12] = [
    ("upstream", [
        ("NCIE-003", "Ch.5", "Occurrence/effective time and knowledge/record time are the canonical bitemporal axes; this chapter is their Memory-service realisation."),
    ]),
    ("h2", "12.1 Bitemporal Definitions"),
    ("table",
     ["Time Axis", "Definition"],
     [
        ["Occurrence / Valid Time", "When the remembered fact actually happened or was true."],
        ["Knowledge / Record Time", "When NCIE came to know/record the fact — never substituted with ingestion time where they genuinely differ."],
    ],
     "Bitemporal time axes (formally defined here; NCIE-003 Ch.5 establishes the platform-wide principle this chapter applies to Memory specifically)."),
    ("h2", "12.2 Historical Reconstruction Flow"),
    ("flow",
     [
        "Reconstruction request: 'what was known as of knowledge-time T?'",
        "Bind to canonical facts with knowledge time ≤ T (NCIE-003 Ch.25 pattern)",
        "Bind to Rule Versions effective at T (NCIE-003 Ch.24)",
        "Bind to Evidence registered with knowledge time ≤ T",
        "Exclude any fact/rule/evidence with knowledge time > T",
        "Return AS KNOWN AT T, with later developments available separately as SUBSEQUENTLY LEARNED",
     ],
     "Decision-Time / historical reconstruction flow — later evidence never contaminates the reconstructed view."),
    ("h2", "12.3 Correction Without Overwrite"),
    ("p",
     "Historical knowledge state is never overwritten merely because current understanding changes. "
     "A correction to historical Memory uses an explicit CORRECTION, AMENDMENT, NEW VERSION, "
     "INVALIDATION or SUPERSESSION relationship (Ch.20 detail for Knowledge specifically) — the "
     "institution's prior understanding remains reconstructable even after it is known to have been "
     "wrong."),
    ("review", [
        ("PROPOSED", "UTC as the canonical knowledge-time storage basis is proposed, consistent with NCIE-003 Ch.5 §5.8's platform-wide default."),
    ]),
    ("trace", "NCIE-003 Ch.5, Ch.25."),
]
