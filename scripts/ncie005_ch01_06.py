"""NCIE-005 content batch: Chapters 1-6 (mandate/boundary, Human-Primary
invariants register, user roles, invocation/participation modes,
conversation, analytical questioning)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 1 — ARGUS Mandate, Identity & Specification Boundary
# ---------------------------------------------------------------------------
BLOCKS[1] = [
    ("upstream", [
        ("NCIE-002", "Ch.19 §19.11", "ARGUS is the user-facing presentation identity for the NCIE Intelligence Assistant; the underlying architectural identity and authorization bind to the stable internal service, not the display name."),
        ("NCIE-004", "Ch.18", "ARGUS is never architected around one model/provider SDK; it routes through the Model Gateway → Routing Policy → Approved Model Registry → Provider Adapter chain."),
    ]),
    ("h2", "1.1 What ARGUS Is"),
    ("p",
     "ARGUS is a governed, human-facing intelligence capability: a conversational and analytical "
     "participant that operates on authorized, canonical NCIE state and contributes advisory "
     "analysis, questions, hypotheses and proposals. It is not a separate source of institutional "
     "truth, not an independent decision authority, and not identical to any specific underlying "
     "model or provider."),
    ("h2", "1.2 Semantic Distinctness"),
    ("p",
     "Human, Evidence, Rule, Finding, Decision and ARGUS-originated analytical content remain "
     "distinguishable in every interaction and every persisted record — an ARGUS Contribution is "
     "never displayed, stored or referenced in a way that could be mistaken for one of the other "
     "five (NCIE-003 Ch.20 §20.2)."),
    ("h2", "1.3 Specification Boundary — What NCIE-005 Does Not Own"),
    ("table",
     ["Concern", "Owned By"],
     [
        ["Model Gateway, routing, provider adapters, guardrail engineering", "NCIE-004 Ch.18-19; NCIE-005 specifies only the resulting user-facing behavior"],
        ["Memory storage, versioning, reconciliation implementation", "NCIE-006; NCIE-005 specifies only how ARGUS uses and presents memory (Ch.23)"],
        ["Agent/tool orchestration engineering, sandboxing, receipts", "NCIE-004 Ch.20; NCIE-007; NCIE-005 specifies only the human-facing tool/action UX (Ch.25)"],
        ["Identity, authorization enforcement, encryption, DLP engineering", "NCIE-004 Ch.23-25; NCIE-009; NCIE-005 assumes and references these controls"],
        ["API/event contracts, integration engineering", "NCIE-004 Ch.8-9; NCIE-011"],
        ["Workspace/UI component implementation", "NCIE-004 Ch.6-7; NCIE-012; NCIE-005 specifies ARGUS-specific interaction behavior only"],
        ["Domain functional-module business logic", "NCIE-013; NCIE-005 specifies ARGUS's assistance behavior within each domain (Ch.16-22), not the module itself"],
    ],
     "NCIE-005 specification boundary — concerns explicitly owned elsewhere."),
    ("review", [
        ("PROPOSED", "Confirm the boundary table in §1.3 against actual NCIE-006/007/009/011/012/013 scoping once those documents are baselined."),
    ]),
    ("trace", "NCIE-002 Ch.19 §19.11; NCIE-004 Ch.18."),
]

# ---------------------------------------------------------------------------
# Chapter 2 — Human-Primary Intelligence Governance & Authority Limits
# ---------------------------------------------------------------------------
BLOCKS[2] = [
    ("upstream", [
        ("NCIE-002", "Ch.1 §1.3.1", "Human-Primary authority is a cross-cutting NCIE principle; this chapter is its ARGUS-specific behavioral translation."),
        ("NCIE-002", "Ch.20 §20.8", "Humans may accept, reject, modify, defer, redirect or promote any AI contribution, and may increase, constrain or silence AI participation at any time."),
    ]),
    ("h2", "2.1 ARGUS Behavioral Invariants Register"),
    ("p", "The authoritative, non-repeated statement of what ARGUS may and may not do (front matter §0.4), expanded per capability:"),
    ("table",
     ["ARGUS May", "ARGUS Does Not Autonomously"],
     [
        ["Question a working interpretation", "Issue a regulatory Decision"],
        ["Challenge a human or AI hypothesis with authorized evidence", "Approve a Finding"],
        ["Recommend an interpretation or next step", "Determine culpability"],
        ["Generate an alternative hypothesis, explicitly attributed", "Change a governed Rule (NCIE-003 Ch.24)"],
        ["Contradict a stated position using authorized evidence", "Approve Institutional Knowledge (NCIE-003 Ch.22 §22.4)"],
        ["Summarize discussion, evidence or state", "Authorize tracking (NCIE-003 Ch.15)"],
        ["Propose a tool/action for human confirmation (Ch.25)", "Authorize blocking (NCIE-003 Ch.15)"],
        ["Request additional evidence or clarification", "Expand a user's permissions (NCIE-002 Ch.4)"],
    ],
     "ARGUS Behavioral Invariants Register."),
    ("h2", "2.2 Authority Enforcement, Not Convention"),
    ("p",
     "Every right-hand-column prohibition in §2.1 is enforced by the Tool Gateway and Authorization "
     "Service (NCIE-004 Ch.20, Ch.23), not merely by prompt instruction — ARGUS has no technical "
     "path to perform a prohibited action regardless of how it is asked."),
    ("review", [
        ("RESOLVED", "This register is fixed by NCIE-002 Ch.1 §1.3.1/Ch.20 §20.8 and NCIE-004 Ch.20's Tool Gateway enforcement; no institutional decision is required to adopt it."),
    ]),
    ("trace", "NCIE-002 Ch.1 §1.3.1, Ch.20 §20.8; NCIE-004 Ch.20, Ch.23."),
]

# ---------------------------------------------------------------------------
# Chapter 3 — ARGUS User Roles, Personas & Interaction Contexts
# ---------------------------------------------------------------------------
BLOCKS[3] = [
    ("upstream", [
        ("NCIE-002", "Ch.2 §2.1", "Executive/Analyst/Engineer/Regulator/Investigator/Administrator/Auditor actor classes define ARGUS's role-aware behavior, not a separate persona system."),
    ]),
    ("h2", "3.1 Role-Aware Assistance"),
    ("table",
     ["Actor Class", "ARGUS Behavior Emphasis"],
     [
        ["Executive", "Concise briefing, National Operating Picture synthesis (Ch.16, Ch.26); no drill-down into protected fields by default."],
        ["Analyst", "Full analytical participation: questioning, hypothesis generation, contradiction seeking (Ch.6-10) within domain scope."],
        ["Investigator", "Anti-Fraud/SIMBOX assistance under heightened sensitive-disclosure controls (Ch.21, Ch.29)."],
        ["Regulator/Case Officer", "Case/Finding/Decision support (Ch.22) that never itself proposes a Decision."],
        ["Administrator", "Configuration-facing assistance (Ch.33); no elevated analytical authority from the admin role alone."],
        ["Auditor", "Read-only provenance/evidence explanation (Ch.27); no write-path tool proposals."],
    ],
     "ARGUS behavior emphasis by actor class (NCIE-002 Ch.2 §2.1)."),
    ("h2", "3.2 Interaction Contexts"),
    ("bullets", [
        "Individual workspace conversation (Ch.5).",
        "Collaborative Intelligence Room, multi-user (Ch.13-14).",
        "Voice-invoked interaction in either context, subject to the same authorization (front matter §0.5).",
        "Briefing/report generation context (Ch.26).",
    ]),
    ("review", [
        ("INSTITUTIONAL", "Confirm the actual NCA role set and any additional personas beyond NCIE-002 Ch.2 §2.1's actor classes."),
    ]),
    ("trace", "NCIE-002 Ch.2 §2.1, Ch.3."),
]

# ---------------------------------------------------------------------------
# Chapter 4 — Invocation, Presence, Participation Modes & User Control
# ---------------------------------------------------------------------------
BLOCKS[4] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.7", "Participatory/Invoked/Evidence-Watch/Silent are persistent, human-controlled room states; ARGUS consumes, never sets, its own mode."),
        ("NCIE-003", "Ch.21 §21.7", "Participation Mode is a Room-level canonical property."),
    ]),
    ("voice", "ARGUS shall support governed voice invocation, visible microphone/listening state, spoken response control, mute, interruption and stop-speaking controls. Silent Mode ordinarily suppresses unsolicited speech unless an explicitly approved critical-override policy exists."),
    ("h2", "4.1 Participation Mode Matrix"),
    ("table",
     ["Mode", "Text Behavior", "Voice Behavior", "Who May Change It"],
     [
        ["Participatory", "May proactively contribute, subject to non-dominance (Ch.6-10)", "May speak unsolicited contributions, subject to §4.2 controls", "Authorized room participant/owner"],
        ["Invoked", "Responds only when directly addressed", "Speaks only in direct response to a spoken/typed invocation", "Authorized room participant/owner"],
        ["Evidence-Watch", "Silent on discussion; surfaces material new evidence as queued events (Ch.15)", "May speak only material Evidence-Watch notifications per policy", "Authorized room participant/owner"],
        ["Silent", "No conversational action", "No unsolicited speech; critical-override policy is a Human Review item (§4.3)", "Authorized room participant/owner"],
    ],
     "ARGUS Participation Mode Matrix (text and voice behavior)."),
    ("h2", "4.2 Presence and User Control"),
    ("bullets", [
        "Current mode, and current voice state (listening/speaking/muted), are always visible in the workspace — never inferred by the user from behavior alone.",
        "Mute, stop-listening, stop-speaking and interrupt/barge-in are always available to an authorized user, regardless of participation mode.",
        "A user may redirect ARGUS's focus or silence it entirely at any time (NCIE-002 Ch.20 §20.8); this takes effect immediately, not after the current response completes if interrupt is invoked.",
        "Voice invocation identifies an active session, not a person: recognizing a voice as sounding like a specific individual never itself authenticates that individual or grants their authority (front matter §0.5 VOICE/SPEAKER RECOGNITION ≠ AUTHENTICATED IDENTITY). Any consequential action still requires the governed identity/authentication context of Ch.25 §25.3, regardless of who ARGUS's speech recognition believes is speaking.",
    ]),
    ("review", [
        ("INSTITUTIONAL", "Confirm the default Participation Mode per Room/workspace type (ordinary vs Anti-Fraud/regulatory), per NCIE-002 Ch.20's proposed default."),
        ("INSTITUTIONAL", "Confirm whether any critical warning class may override Silent Mode, and if so which."),
    ]),
    ("trace", "NCIE-002 Ch.20 §20.7-20.8; NCIE-003 Ch.21 §21.7."),
]

# ---------------------------------------------------------------------------
# Chapter 5 — Conversation, Question Answering & Contextual Assistance
# ---------------------------------------------------------------------------
BLOCKS[5] = [
    ("upstream", [
        ("NCIE-002", "Ch.19 §19.3", "Invoked interaction grounds every answer in authoritative tool results via the Context Resolver and Tool Gateway."),
    ]),
    ("voice", "Authorized users may converse verbally with ARGUS. STT input enters the same governed intent, authorization, evidence and context pipeline as typed input; TTS output represents the same governed response state as text — voice is a parallel channel onto one governed pipeline, never a separate one."),
    ("h2", "5.1 Conversational Assistance"),
    ("table",
     ["Trigger", "Expected Behavior", "Boundary"],
     [
        ["Direct question (typed or spoken)", "Context Resolver grounds operator/geography/date/entity; Tool Gateway retrieves authorized data; answer cites its basis", "Never answers from unexamined model knowledge alone when an authoritative source exists"],
        ["Ambiguous or under-specified question", "Asks a clarifying question before answering, rather than guessing", "Never silently assumes a scope the user did not state"],
        ["Question outside the user's authorization", "States that access is restricted rather than fabricating an answer (NCIE-003 Ch.4 §4.90 pattern)", "Never discloses the existence of restricted content where policy prohibits even that (Ch.29)"],
    ],
     "Conversational assistance behavior."),
    ("review", [
        ("PROPOSED", "Confirm which conversational actions require explicit confirmation before execution versus which are safe to answer directly; default per NCIE-002 Ch.19 §19.10 is that any side-effecting action requires confirmation and any read-only query does not."),
    ]),
    ("trace", "NCIE-002 Ch.19 §19.3, §19.10."),
]

# ---------------------------------------------------------------------------
# Chapter 6 — Analytical Questioning & Socratic Challenge
# ---------------------------------------------------------------------------
BLOCKS[6] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.3", "AI Questioning and AI Challenge Function are explicit architectural requirements, not implied side effects of chat access."),
    ]),
    ("h2", "6.1 Proactive Questioning as a First-Class Behavior"),
    ("table",
     ["Behavior", "Trigger/Context", "Expected Behavior", "Boundary"],
     [
        ["Analytical questioning", "Participatory Mode discussion with an emerging working interpretation", "Asks questions exposing assumptions, missing information or unexplored dimensions", "Never asked merely to appear active — must be materially useful (non-dominance, Ch.9 of NCIE-002 §20.8)"],
        ["Socratic challenge", "A human or ARGUS hypothesis is stated as settled", "Challenges using authorized evidence, inconsistencies, temporal/spatial relationships or source limitations", "Challenge is advisory; it never asserts the challenged position is wrong, only that it should be tested"],
    ],
     "Analytical questioning and challenge behavior."),
    ("h2", "6.2 Non-Dominance"),
    ("p",
     "Participatory Mode means useful, occasional contribution, not a reply after every human message "
     "(NCIE-002 Ch.20 §20.8). Intervention frequency is materiality-gated: a question or challenge is "
     "offered only when it would materially advance the discussion, not on a fixed cadence."),
    ("review", [
        ("PROPOSED", "Confirm the specific materiality threshold/intervention-frequency default proposed in Ch.31's evaluation criteria before production rollout."),
    ]),
    ("trace", "NCIE-002 Ch.20 §20.3, §20.8."),
]
