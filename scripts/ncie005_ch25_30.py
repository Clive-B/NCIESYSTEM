"""NCIE-005 content batch: Chapters 25-30 (tool use/action proposals, output
types/briefing, provenance/AI attribution, personalization, safety/prompt
injection/protected identity, failure/degraded mode)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 25 — ARGUS Tool Use, Action Proposals & Human Approval UX
# ---------------------------------------------------------------------------
BLOCKS[25] = [
    ("upstream", [
        ("NCIE-004", "Ch.20 §20.2-20.3", "The Tool Gateway enforces registration, typed I/O, authorization, classification, purpose, target validation, approval and audit; NCIE-005 specifies only the human-facing presentation of that enforcement."),
    ]),
    ("voice", "Verbal requests for consequential actions never bypass confirmation or approval. Where required, ARGUS restates the exact target/action before proceeding, and governed authorization is captured independently of speech recognition alone."),
    ("h2", "25.1 Tool/Action Authority Matrix"),
    ("p", "Every proposed action passes through the same state chain regardless of input modality "
         "(typed or spoken):"),
    ("flow",
     [
        "PROPOSED (ARGUS suggests an action)",
        "REQUESTED (user confirms intent)",
        "AUTHORIZED (Authorization Service checks effective permissions, NCIE-004 Ch.23)",
        "APPROVED (human approval where required, distinct actor from requester)",
        "SUBMITTED (Tool Gateway dispatches to the target system)",
        "EXECUTED (target system reports completion)",
        "VERIFIED (independent confirmation the effect actually occurred)",
     ],
     "Proposed-action state chain — an UNKNOWN outcome at any stage triggers reconciliation, never a silent 'success' claim."),
    ("h2", "25.2 What ARGUS Must Communicate"),
    ("bullets", [
        "What it proposes to do, and why (grounded in the discussion/evidence that motivated it).",
        "The exact target of the action (e.g. which SIM, which Rule).",
        "What authority/role is required to approve it.",
        "Whether approval is required at all, or the action is read-only.",
        "Current execution state (PROPOSED through VERIFIED, §25.1) — never skipped or glossed.",
        "Verified outcome, explicitly, once known — including if it is UNKNOWN pending reconciliation (NCIE-003 Ch.23 §23.2).",
    ]),
    ("h2", "25.3 Voice Authority Boundary"),
    ("p",
     "A spoken request such as \"ARGUS, block this SIM\" passes through the identical chain in "
     "§25.1: Target Identification → Authorization → Required Confirmation → Human/Institutional "
     "Approval → Tool Gateway → Execution → Verification → Audit. Speech recognition alone never "
     "constitutes authorization for a consequential action — VERBAL REQUEST ≠ AUTHORIZATION."),
    ("h2", "25.4 Speech-Recognition Uncertainty"),
    ("p",
     "Material transcription ambiguity triggers clarification, never a best-guess execution. "
     "Uncertain speech recognition shall not be converted into a Blocking, Tracking, Rule Change, "
     "Approval, Protected Reveal or any other consequential action."),
    ("trace", "NCIE-004 Ch.20; NCIE-003 Ch.23 §23.2."),
]

# ---------------------------------------------------------------------------
# Chapter 26 — ARGUS Output Types, Structured Artifacts & Briefing Support
# ---------------------------------------------------------------------------
BLOCKS[26] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.5", "Multi-Speaker Attribution preserves who introduced, challenged, adopted, modified or rejected each idea."),
    ]),
    ("h2", "26.1 Output Forms"),
    ("table",
     ["Output Form", "Purpose", "Boundary"],
     [
        ["Conversational answer", "Direct response to a question (Ch.5)", "Epistemically labelled per Ch.11's matrix"],
        ("Question / Challenge", "Analytical questioning (Ch.6)", "Attributed to ARGUS, never presented as a human's own"),
        ["Hypothesis", "Working alternative interpretation (Ch.7)", "Always \"ARGUS Hypothesis\", never \"Confirmed\""],
        ["Summary", "Condensed restatement of discussion/evidence/state", "Preserves dissent (Ch.8 §8.2); never smooths over disagreement"],
        ["Brief/Report", "Structured, exportable artifact for executive/regulatory use", "Every material claim retains its citation and epistemic type"],
        ["Action Proposal", "A proposed tool/action (Ch.25)", "Never presented as already executed"],
    ],
     "ARGUS output forms and their boundaries."),
    ("h2", "26.2 Briefing Support"),
    ("p",
     "A generated brief inherits the full citation discipline of Ch.11 — a briefing document is not "
     "exempt from epistemic labelling merely because it is formatted for executive presentation."),
    ("trace", "NCIE-002 Ch.20 §20.5, §20.6."),
]

# ---------------------------------------------------------------------------
# Chapter 27 — Provenance, AI Attribution & Human Modification
# ---------------------------------------------------------------------------
BLOCKS[27] = [
    ("upstream", [
        ("NCIE-003", "Ch.20 §20.4, §20.6", "Human Modification of AI Contribution retains the original, unmodified AI-originated version; AI origin never erased by adoption."),
    ]),
    ("h2", "27.1 Provenance Behavior"),
    ("bullets", [
        "Every ARGUS Contribution retains AI Origin permanently, even after a human edits or extends it.",
        "A Human Modification of AI Contribution is recorded alongside — not instead of — the original.",
        "Provenance covers: Evidence References, Tool Results, structured Hypotheses/Assumptions/Contradictions/Evidence Gaps, Model/Deployment Reference where governance requires it, and Human Response — never private model chain-of-thought (NCIE-003 Ch.20 §20.2).",
    ]),
    ("h2", "27.2 No Hidden Reasoning Requirement"),
    ("p",
     "Defensibility comes from the structured artifacts in §27.1, not from persisting or exposing "
     "the model's internal deliberation. NCIE-005 does not require, and NCIE-004/006 do not build, "
     "any chain-of-thought storage or disclosure mechanism."),
    ("trace", "NCIE-003 Ch.20 §20.2, §20.4, §20.6."),
]

# ---------------------------------------------------------------------------
# Chapter 28 — Personalization, Preferences & User-Specific Assistance
# ---------------------------------------------------------------------------
BLOCKS[28] = [
    ("upstream", [
        ("NCIE-003", "Ch.22 §22.2", "Private User Memory is a distinct, non-automatically-shared memory tier."),
    ]),
    ("h2", "28.1 Permitted Personalization"),
    ("table",
     ["Preference Class", "Governed?", "May Alter"],
     [
        ["Presentation (Docked/Expanded/Full-Screen, NCIE-002 Ch.3 §3.9)", "User-set, persisted in Private User Memory", "Display only"],
        ["Notification classes eligible for speech", "User-set, subject to Ch.33 policy limits", "Which events ARGUS speaks vs. displays silently"],
        ["Voice (provider/language/accent where offered)", "User-set within Ch.33's approved voice policy", "Voice presentation only"],
        ["Verbosity", "User-set", "Response length/detail, not content accuracy"],
        ["Workspace layout", "User-set (NCIE-002 Ch.3)", "Layout only"],
    ],
     "Permitted personalization classes."),
    ("h2", "28.2 What Preferences Never Alter"),
    ("bullets", [
        "Authorization — a preference never grants access a role does not already have.",
        "Evidence — a preference never changes what evidence exists or its classification.",
        "Rules — a preference never changes a governed Rule Version.",
        "Institutional Knowledge — a preference never promotes or retracts Knowledge.",
        "Decision Authority — a preference never grants decision-making capability.",
    ]),
    ("trace", "NCIE-002 Ch.3 §3.9; NCIE-003 Ch.22 §22.2."),
]

# ---------------------------------------------------------------------------
# Chapter 29 — Safety, Prompt Injection, Sensitive Data & Protected Identity Behavior
# ---------------------------------------------------------------------------
BLOCKS[29] = [
    ("upstream", [
        ("NCIE-002", "Ch.24 §24.4", "Ingested content (email, files) is treated as data, never as instructions to the model."),
        ("NCIE-003", "Ch.14 §14.6, Ch.36 §36.3", "Ghana Card/Passport identifiers and precise Anti-Fraud location require masking/tokenization and heightened protection."),
    ]),
    ("voice", "Before synthesizing sensitive content, ARGUS applies a spoken-disclosure check. Raw Ghana Card numbers, passport numbers, precise Anti-Fraud tracking locations, credentials and other highly restricted information are not spoken merely because the user can view them. Voice input, transcripts and retained audio — if any — inherit applicable classification and retention controls."),
    ("h2", "29.1 Voice Interaction & Spoken-Disclosure Matrix"),
    ("table",
     ["Information Class", "Display Authorization", "Spoken-Disclosure Authorization", "ARGUS Behavior"],
     [
        ["Ghana Card / Passport identifiers", "Authorized viewer may see masked/protected-revealed value", "Never spoken in full, even to an authorized viewer, absent a specific approved exception", "States that the value exists and is available on-screen; does not vocalize it"],
        ["Precise SIMBOX tracking locations", "Authorized Investigator may see on map/record", "Not spoken with precision; may reference general status verbally", "Directs the user to the visual/authorized channel for precise detail"],
        ["Restricted Investigation Evidence", "Authorized Investigator/Case Officer", "Case-by-case per Ch.33 policy; defaults to not spoken", "States existence without content where policy requires"],
        ["Credentials / secrets", "Never displayed to any user via ARGUS", "Never spoken under any circumstance", "Refuses; states credentials are never handled via ARGUS"],
        ["Sensitive Revenue information", "Authorized Revenue Assurance role", "May be spoken in a private, single-user context; not in a shared Room with mixed authorization", "Applies per-viewer authorization check before speaking in a Room"],
        ["Protected network/security information", "Authorized IT Security role", "Not spoken in a shared Room; may be spoken 1:1 to an authorized user", "Defers to display channel in mixed-authorization contexts"],
    ],
     "Voice Interaction & Spoken-Disclosure Matrix — display authorization does not imply spoken-disclosure authorization."),
    ("p",
     "ARGUS ordinarily cannot establish with certainty who else is physically present near an "
     "authorized user. Where physical listening context cannot be established, ARGUS shall default "
     "to the more restrictive spoken-disclosure behavior for highly sensitive information (§29.1's "
     "Ghana Card/Passport, precise tracking, credentials and protected network/security rows) and "
     "may direct the authorized user to the protected visual interface instead of speaking the "
     "content. This default applies regardless of Room type or Participation Mode."),
    ("h2", "29.2 Prompt Injection Defense"),
    ("p",
     "Content from ingested sources (operator email, uploaded files, transcribed speech from an "
     "unauthenticated channel) is treated as data ARGUS may reason about, never as an instruction "
     "that changes ARGUS's own behavior, authorization or disclosure policy."),
    ("h2", "29.3 Voice Privacy Controls"),
    ("bullets", [
        "Visible microphone state, listening indicator and speaking indicator at all times voice is active.",
        "Mute, stop-listening, stop-speaking and interrupt/barge-in always available.",
        "Voice enabled/disabled is a persistent, user-visible setting; text fallback is always available.",
        "Persistent listening is never silently activated — an explicit invocation or opt-in starts a listening session.",
        "Transcript visibility and audio/transcript retention are explicitly governed (Ch.33 policy), never assumed.",
    ]),
    ("review", [
        ("LEGAL", "Confirm audio/transcript retention periods and applicable privacy policy with NCA Legal/Data Protection."),
        ("INSTITUTIONAL", "Confirm the exact spoken-disclosure policy per information class in §29.1's matrix with the relevant domain owners."),
    ]),
    ("trace", "NCIE-002 Ch.24 §24.4; NCIE-003 Ch.14 §14.6, Ch.36."),
]

# ---------------------------------------------------------------------------
# Chapter 30 — Failure, Degraded Mode, Model Unavailability & Recovery
# ---------------------------------------------------------------------------
BLOCKS[30] = [
    ("upstream", [
        ("NCIE-002", "Ch.19 §19.8, Ch.28", "Deterministic NCIE functions remain operational independently of ARGUS; loss of a dependency degrades only the affected capability."),
    ]),
    ("voice", "STT/TTS failure degrades to authorized text interaction where available, without changing ARGUS authority. Uncertain transcription never silently becomes a consequential action; material ambiguity triggers clarification."),
    ("h2", "30.1 Degraded-Mode Behavior"),
    ("table",
     ["Dependency Lost", "ARGUS Behavior"],
     [
        ["LLM / Model Gateway unavailable", "States the limitation; falls back to direct tool/query access without conversational framing (NCIE-002 Ch.19 §19.8)"],
        ["Tool unavailable", "States which action could not be attempted; does not claim success"],
        ["Evidence unavailable", "States Unknown/Unavailable per NCIE-003 Ch.2 §2.5 vocabulary; never substitutes a guess"],
        ["Memory unavailable", "Proceeds without historical context, states that it is doing so"],
        ["STT unavailable", "Falls back to text input; states voice is temporarily unavailable"],
        ["TTS unavailable", "Falls back to text output (Voice → Text, never Voice Failure → NCIE Failure)"],
        ["Network degraded", "Slows/queues rather than fabricating a response from stale cached state without labelling it stale"],
        ["Context incomplete", "Asks a clarifying question rather than proceeding on an incomplete assumption"],
    ],
     "ARGUS degraded-mode behavior by dependency."),
    ("h2", "30.2 Deterministic NCIE Independence"),
    ("p",
     "Every deterministic NCIE function — ingestion, validation, Traffic monitoring, Revenue "
     "calculation, SIM Registration rule evaluation, Anti-Fraud workflow, REWS deterministic rules, "
     "Evidence access, workflow processing, human collaboration and audit — remains fully "
     "operational when ARGUS itself is entirely unavailable (NCIE-002 Ch.28)."),
    ("trace", "NCIE-002 Ch.19 §19.8, Ch.28."),
]
