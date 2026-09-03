"""Content model for NCIE-005 ARGUS Intelligence Assistant Specification.

CHAPTERS populated in 6 batches (1-6, 7-12, 13-18, 19-24, 25-30, 31-35).
Block kinds consumed by ncie005_common.render_blocks:
  ("h2", text) / ("h3", text) / ("p", text) / ("bullets", [items])
  ("upstream", [(doc_id, ref, consequence), ...]) / ("voice", text)
  ("proposed", text) / ("trace", text) / ("review", [items])
  ("flow", [nodes], caption) / ("rel", [(s,r,t), ...], caption)
  ("table", headers, rows, caption, status_col_index_or_None)
"""

CHAPTER_TITLES = {
    1: "ARGUS Mandate, Identity & Specification Boundary",
    2: "Human-Primary Intelligence Governance & Authority Limits",
    3: "ARGUS User Roles, Personas & Interaction Contexts",
    4: "Invocation, Presence, Participation Modes & User Control",
    5: "Conversation, Question Answering & Contextual Assistance",
    6: "Analytical Questioning & Socratic Challenge",
    7: "Hypothesis Generation & Alternative Explanation",
    8: "Contradiction Seeking, Counterevidence & Dissent",
    9: "Assumption Identification & Assumption Testing Support",
    10: "Evidence Gap Identification & Discriminating Evidence",
    11: "Evidence-Bounded Reasoning, Citation & Epistemic Labels",
    12: "Uncertainty, Abstention, Conflict & Incomplete Information",
    13: "Collaborative Brainstorming & Multi-User Intelligence Participation",
    14: "Room Facilitation Support, Threads & Structured Reasoning",
    15: "Evidence-Watch & Event-Triggered ARGUS Re-entry",
    16: "Situational Awareness, NOP & Cross-Domain Intelligence Assistance",
    17: "Network, Traffic & Incident Intelligence Assistance",
    18: "Revenue Intelligence & Billing Verification Assistance",
    19: "Mobile Money Intelligence Assistance",
    20: "SIM Registration Intelligence Assistance",
    21: "Anti-Fraud / SIMBOX Investigation Assistance",
    22: "Regulatory Case, Finding & Decision-Support Assistance",
    23: "Memory Retrieval, Historical Context & Decision-Time Assistance",
    24: "Institutional Knowledge Retrieval & Knowledge-Challenge Behavior",
    25: "ARGUS Tool Use, Action Proposals & Human Approval UX",
    26: "ARGUS Output Types, Structured Artifacts & Briefing Support",
    27: "Provenance, AI Attribution & Human Modification",
    28: "Personalization, Preferences & User-Specific Assistance",
    29: "Safety, Prompt Injection, Sensitive Data & Protected Identity Behavior",
    30: "Failure, Degraded Mode, Model Unavailability & Recovery",
    31: "Quality, Evaluation, Behavioral Testing & Reviewer Simulation",
    32: "Performance, Responsiveness, Accessibility & Interaction NFRs",
    33: "ARGUS Configuration, Policy, Naming & Change Governance",
    34: "Human Review Register, Open Decisions & Proposed Defaults",
    35: "Requirements Traceability, Acceptance & Handover Gate",
}

CHAPTER_SCOPE = {
    1: "Define what ARGUS is, what it is not, and the boundary of NCIE-005.",
    2: "Translate Human-Primary governance into explicit ARGUS behavioral limits.",
    3: "Define the human roles and operational contexts ARGUS must serve.",
    4: "Specify how ARGUS is invoked, made visible, muted, redirected and switched among governed participation modes.",
    5: "Specify ordinary conversational assistance while preserving evidence, authorization and context boundaries.",
    6: "Make proactive questioning and challenge a first-class ARGUS capability rather than passive Q&A.",
    7: "Specify generation, persistence and revision of alternative hypotheses without converting them into findings.",
    8: "Require ARGUS to seek contradictions and counterevidence rather than reinforce dominant interpretations.",
    9: "Specify how ARGUS surfaces hidden assumptions and supports their examination.",
    10: "Specify identification of missing evidence and evidence that could discriminate among competing hypotheses.",
    11: "Define how ARGUS grounds material statements in authorized evidence and labels the epistemic status of outputs.",
    12: "Define behavior when evidence is conflicting, incomplete, stale, unavailable or outside ARGUS authority.",
    13: "Specify ARGUS as an active analytical participant in persistent Collaborative Intelligence Rooms.",
    14: "Define structured facilitation support without making ARGUS the default meeting leader or decision authority.",
    15: "Specify scoped Evidence-Watch behavior and governed re-entry when material evidence changes.",
    16: "Define ARGUS assistance across the National Operating Picture and cross-domain situational analysis.",
    17: "Define bounded assistance for network performance, traffic and incident analysis.",
    18: "Define deterministic-data-aware Revenue assistance without allowing ARGUS to invent calculations or regulatory findings.",
    19: "Define assistance over aggregate Mobile Money intelligence without inventing subscriber-level detail.",
    20: "Define assistance over registration rules, exceptions and protected identity data.",
    21: "Define Anti-Fraud assistance while preserving detection/culpability, registration/actor and tracking-authorization boundaries.",
    22: "Define case and decision support while keeping Findings and Decisions human/institutional.",
    23: "Define use of governed memory and historical/Decision-Time context without treating memory as current truth.",
    24: "Define retrieval, applicability challenge and proposal of knowledge candidates without allowing ARGUS to approve institutional knowledge.",
    25: "Define user-facing behavior around tools, proposed actions, confirmations and execution receipts.",
    26: "Define the forms in which ARGUS may present questions, hypotheses, challenges, summaries, briefs and structured analytical artifacts.",
    27: "Preserve AI origin, human adoption/modification and defensible provenance without storing private chain-of-thought.",
    28: "Define permitted personalization while ensuring preferences never alter authorization or institutional truth.",
    29: "Define ARGUS behavior around untrusted content, sensitive data, protected identities and prompt-injection attempts.",
    30: "Define user-visible and system behavior when models/tools/context services are degraded or unavailable.",
    31: "Define behavioral evaluation, adversarial testing, regression and acceptance of ARGUS capabilities.",
    32: "Define interaction-level nonfunctional requirements for responsiveness, accessibility and usable interruption behavior.",
    33: "Define configurable ARGUS naming/presentation, policies, modes and controlled behavioral change.",
    34: "Consolidate unresolved institutional choices and proposed behavioral defaults.",
    35: "Map ARGUS requirements upstream and define the acceptance gate and handover to later NCIE specifications.",
}

# Chapters carrying an explicit skeleton "Voice requirement:" clause.
VOICE_CHAPTERS = {4, 5, 13, 15, 25, 29, 30, 32, 33}

FRONT_MATTER = {
    "governance_rows": [
        ("Document", "NCIE-005 ARGUS Intelligence Assistant Specification"),
        ("Edition", "In development — Version 1.0"),
        ("Baseline authorized", "NCIE-005 Skeletal v0.2 — Voice Interaction Update — approved for full expansion; 35-chapter structure locked"),
        ("Requirements authority", "NCIE-001 Master Product Requirements Document, Version 1.2"),
        ("Architecture authority", "NCIE-002 System Architecture & Technical Design, Version 0.4"),
        ("Canonical data authority", "NCIE-003 Data Model & Data Dictionary, Version 0.3 (Canonical Data Architecture Baseline)"),
        ("Engineering baseline", "NCIE-004 Technology Stack & Engineering Blueprint, Version 1.1 (Approved Engineering Baseline)"),
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
    for n in range(1, 36)
]


def get_chapter(number):
    for chapter in CHAPTERS:
        if chapter["number"] == number:
            return chapter
    raise KeyError(number)


def set_blocks(number, blocks):
    get_chapter(number)["blocks"] = blocks
