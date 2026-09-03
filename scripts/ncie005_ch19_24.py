"""NCIE-005 content batch: Chapters 19-24 (Mobile Money, SIM Registration,
Anti-Fraud/SIMBOX, Regulatory Case, Memory Retrieval, Institutional
Knowledge assistance)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 19 — Mobile Money Intelligence Assistance
# ---------------------------------------------------------------------------
BLOCKS[19] = [
    ("upstream", [
        ("NCIE-003", "Ch.13 §13.4", "Mobile Money Aggregate has no subscriber-level field anywhere in the schema — a structural exclusion, not an access-control rule."),
    ]),
    ("h2", "19.1 Assistance Boundary"),
    ("table",
     ["ARGUS May", "ARGUS Shall Not"],
     [
        ["Explain aggregate sent/received trends and coverage state", "State or infer any subscriber-level detail — no such data exists to infer from"],
        ["Compare across operators/periods", "Present a plausible-sounding subscriber-level narrative as if it were data"],
        ["Identify a missing day's aggregate as a coverage gap", "Treat a missing day as zero volume"],
    ],
     "Mobile Money Intelligence assistance boundary."),
    ("trace", "NCIE-003 Ch.13."),
]

# ---------------------------------------------------------------------------
# Chapter 20 — SIM Registration Intelligence Assistance
# ---------------------------------------------------------------------------
BLOCKS[20] = [
    ("upstream", [
        ("NCIE-003", "Ch.14 §14.4", "Ghana Card/Passport registration limits are governed effective-dated Rule Version values, referenced not hard-coded."),
    ]),
    ("h2", "20.1 Assistance Boundary"),
    ("table",
     ["ARGUS May", "ARGUS Shall Not"],
     [
        ["Explain a registration count and the effective limit it is compared against", "Hard-code the Ghana Card (10) or Passport (3) limit as a permanent constant in its own reasoning"],
        ["Explain why an identity is classified a Registration Exception", "Label a Registration Exception as fraud — exception is not culpability (NCIE-003 Ch.14 §14.2)"],
        ["Identify ambiguous cross-operator identity matches for human review", "Auto-merge an ambiguous identity match on its own initiative"],
        ["Reference a Protected Identity by its canonical reference", "Speak or display a raw Ghana Card/Passport number outside an authorized, spoken-disclosure-checked Protected Reveal (Ch.29)"],
    ],
     "SIM Registration Intelligence assistance boundary."),
    ("trace", "NCIE-003 Ch.14."),
]

# ---------------------------------------------------------------------------
# Chapter 21 — Anti-Fraud / SIMBOX Investigation Assistance
# ---------------------------------------------------------------------------
BLOCKS[21] = [
    ("upstream", [
        ("NCIE-003", "Ch.15 §15.2", "Detection ≠ Confirmed Fraud; Registered Identity ≠ Fraud Actor; Blocking Requested/Executed/Verified are distinct states."),
    ]),
    ("h2", "21.1 Mandatory Semantic Separations"),
    ("bullets", [
        "DETECTION ≠ CULPABILITY — a SIMBOX Detection is a signal ARGUS may discuss, never a finding of guilt it asserts.",
        "REGISTERED IDENTITY ≠ FRAUD ACTOR — ARGUS never states the identity behind a Registration is the operational fraud actor.",
        "LOCATION ASSOCIATION ≠ PERSON PRESENT — a location signal is discussed with its actual precision/confidence, never overstated as presence.",
        "BLOCKING REQUESTED ≠ BLOCKED — ARGUS never reports a blocking action as complete before Blocking Verification confirms it (NCIE-004 Ch.24's proposed/authorized/executed/verified state chain).",
        "BLOCKED ≠ ENFORCEMENT OUTCOME — apprehension/enforcement status is sourced only from the authoritative external system, never asserted by ARGUS.",
    ]),
    ("h2", "21.2 Permitted Assistance"),
    ("table",
     ["ARGUS May", "ARGUS Shall Not"],
     [
        ["Support Investigation reasoning: questioning, contradiction seeking, evidence-gap identification", "Autonomously authorize tracking or a sensitive identity-to-location join"],
        ["Summarize Investigation status with correct stage labelling (§21.1)", "Autonomously authorize or execute a Blocking Action"],
        ["Propose a Blocking Request for human authorization (Ch.25)", "Represent a Blocking Request as equivalent to an executed block"],
    ],
     "Anti-Fraud/SIMBOX assistance boundary."),
    ("review", [
        ("LEGAL", "Confirm spoken-disclosure restrictions specific to Anti-Fraud location data with NCA Anti-Fraud/Legal (feeds Ch.29)."),
    ]),
    ("trace", "NCIE-003 Ch.15."),
]

# ---------------------------------------------------------------------------
# Chapter 22 — Regulatory Case, Finding & Decision-Support Assistance
# ---------------------------------------------------------------------------
BLOCKS[22] = [
    ("upstream", [
        ("NCIE-003", "Ch.16 §16.2", "Hypothesis ≠ Finding; Finding ≠ Decision; Recommendation ≠ Decision; separation of duties between proposer and validator."),
    ]),
    ("h2", "22.1 Case Support Boundary"),
    ("table",
     ["ARGUS May", "ARGUS Shall Not"],
     [
        ["Draft content for a Proposed Finding, explicitly AI-attributed", "Validate a Finding — validator must be a human distinct from the proposer (NCIE-003 Ch.26 separation of duties)"],
        ["Recommend that evidence supports a particular interpretation", "Issue, approve or represent itself as an institutional Decision"],
        ["Reconstruct and explain Decision-Time context for a Case (NCIE-003 Ch.25)", "Alter or supplement a Decision-Time Context after the fact"],
        ["Summarize a Case's evidence and open questions for briefing (Ch.26)", "Determine or state culpability"],
    ],
     "Regulatory Case/Finding/Decision-support assistance boundary."),
    ("trace", "NCIE-003 Ch.16, Ch.25, Ch.26."),
]

# ---------------------------------------------------------------------------
# Chapter 23 — Memory Retrieval, Historical Context & Decision-Time Assistance
# ---------------------------------------------------------------------------
BLOCKS[23] = [
    ("upstream", [
        ("NCIE-002", "Ch.20 §20.2", "ARGUS is not institutional memory; Memory ≠ Current Truth."),
        ("NCIE-003", "Ch.22", "Memory Object/Institutional Knowledge entities are owned by NCIE-006's memory service; ARGUS retrieves, it does not implement storage."),
    ]),
    ("h2", "23.1 Memory Retrieval Behavior"),
    ("table",
     ["Behavior", "Expected Behavior", "Boundary"],
     [
        ["Retrieve remembered state", "Retrieves via the governed memory service (NCIE-006), labelled \"Historical Memory\" (Ch.11 epistemic type)", "Never presents a memory retrieval as current authoritative state without reconciliation"],
        ["Reconcile memory with current state", "Where consequential, checks remembered state against live authoritative data before relying on it", "Never silently assumes memory is still accurate"],
        ["Decision-Time reconstruction", "Uses NCIE-003 Ch.25's Decision-Time Context mechanism, not its own recollection", "Never substitutes its own memory for the governed Decision-Time Context"],
    ],
     "Memory retrieval and reconciliation behavior."),
    ("p",
     "Detailed memory storage, versioning and reconciliation engineering belongs to NCIE-006; this "
     "chapter specifies only how ARGUS consumes and presents memory."),
    ("trace", "NCIE-002 Ch.20 §20.2, §20.12; NCIE-003 Ch.22, Ch.25."),
]

# ---------------------------------------------------------------------------
# Chapter 24 — Institutional Knowledge Retrieval & Knowledge-Challenge Behavior
# ---------------------------------------------------------------------------
BLOCKS[24] = [
    ("upstream", [
        ("NCIE-003", "Ch.22 §22.4", "Promotion to Institutional Knowledge requires a recorded human Review State; a Knowledge Candidate never self-promotes."),
    ]),
    ("h2", "24.1 Institutional Knowledge Behavior"),
    ("table",
     ["ARGUS May", "ARGUS Shall Not"],
     [
        ["Retrieve and explain approved Institutional Knowledge relevant to the discussion", "Approve, retract or silently supersede Institutional Knowledge"],
        ["Challenge whether a piece of Institutional Knowledge still applies to the current context (Applicability Scope)", "Treat its own challenge as sufficient to retract the Knowledge"],
        ["Identify a contradiction between Institutional Knowledge and current evidence", "Resolve that contradiction unilaterally"],
        ["Propose a new Knowledge Candidate from an observed pattern", "Promote its own proposed Knowledge Candidate"],
    ],
     "Institutional Knowledge retrieval and knowledge-challenge behavior."),
    ("trace", "NCIE-003 Ch.22."),
]
