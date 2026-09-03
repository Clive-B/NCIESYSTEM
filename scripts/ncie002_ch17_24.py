"""NCIE-002 content batch: Chapters 17-24 (includes the v0.4 collaborative
brainstorming amendments to Chapters 19, 20, 21, 23 and 24)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 17 — Cross-Domain Fusion & Intelligence Graph
# ---------------------------------------------------------------------------
BLOCKS[17] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Intelligence Fusion, Cross-Domain Correlation & National Intelligence Synthesis Governance."),
    ("h2", "17.1 Scope"),
    ("p",
     "Defines how Network, Traffic, Revenue, Mobile Money, SIM Registration, Anti-Fraud, Incident, Billing and "
     "Regulatory data relate to one another temporally, spatially and by entity — without asserting causation "
     "the evidence does not support."),
    ("h2", "17.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Fusion Service", "Orchestrates cross-domain correlation queries against the canonical platform."],
        ["Graph Store", "Persists entity relationships and their provenance as a queryable graph."],
        ["Entity Resolution", "Determines when records from different domains refer to the same real-world entity."],
        ["Correlation Engine", "Computes temporal/spatial/entity correlations and confidence indicators."],
        ["Provenance Graph", "Links every fused relationship back to its supporting canonical/evidence records (Ch.23)."],
    ],
     "Cross-Domain Fusion & Intelligence Graph principal components."),
    ("h2", "17.3 Correlation Principle"),
    ("p",
     "The Correlation Engine produces correlation, not causation: a temporal or spatial coincidence between, "
     "say, an Incident and a Revenue anomaly is surfaced with its supporting evidence and confidence, and is "
     "explicitly labelled as a candidate relationship for human interpretation, never as an asserted cause."),
    ("rel",
     [
        ("Network / Traffic / Revenue Domains", "supply canonical facts to", "Fusion Service"),
        ("Mobile Money / SIM / Anti-Fraud Domains", "supply canonical facts to", "Fusion Service"),
        ("Fusion Service", "writes correlated relationships to", "Graph Store"),
        ("Graph Store", "is queried by", "Situational Awareness Workspace / Assistant"),
     ],
     "Domain data feeding cross-domain fusion."),
    ("h2", "17.4 Data Model"),
    ("bullets", [
        "Relationship — source entity, target entity, relationship type, confidence, temporal/spatial basis, provenance references.",
        "Contradiction Record — two relationships or facts that conflict, preserved rather than silently resolved (Ch.5, Ch.23).",
    ]),
    ("h2", "17.5 Security Controls"),
    ("bullets", [
        "Fusion queries respect the same field-level authorization as the underlying domains; fusion never bypasses protected-identity controls (Ch.4, Ch.14)."],
    ),
    ("h2", "17.6 Failure Modes"),
    ("bullets", [
        "Conflicting cross-domain signals: both retained as a Contradiction Record rather than one overwriting the other.",
    ]),
    ("h2", "17.7 Non-Functional Requirements"),
    ("bullets", [
        "Interactive fusion queries for a bounded geography/time window return within 3 seconds at p95 (Ch.30)."],
    ),
    ("h2", "17.8 Acceptance Criteria"),
    ("bullets", [
        "A known cross-domain scenario (e.g. Incident correlated with Traffic dip) is demonstrably surfaced as a labelled correlation with supporting evidence, not an asserted cause.",
    ]),
    ("proposed",
     "Confirm the priority list of cross-domain fusion use cases for launch with NCIE domain leads; the Fusion "
     "Service architecture supports incremental addition of correlation types without redesign."),
    ("trace", "NCIE-001 §Intelligence Fusion, Cross-Domain Correlation & National Intelligence Synthesis Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 18 — REWS, Alerts, Situations & National Operating Picture
# ---------------------------------------------------------------------------
BLOCKS[18] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Situational Awareness, Early Warning, Alerting & National Communications Operating Picture."),
    ("h2", "18.1 Scope"),
    ("p",
     "Defines the Regulatory Early Warning System (REWS) engine, Alert lifecycle, multi-domain Situations, and "
     "the National Operating Picture that exposes known/missing/stale/waiting/contradictory state at a glance."),
    ("h2", "18.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["REWS Engine", "Evaluates effective-dated alert rules against canonical/analytical data."],
        ["Alert Store", "Canonical record of raised, acknowledged and closed Alerts."],
        ["Situation Service", "Groups related Alerts/Incidents/evidence into a multi-domain Situation with its own lifecycle."],
        ["Notification Service", "Delivers Alert/Situation notifications to subscribed roles."],
    ],
     "REWS, Alerts, Situations & National Operating Picture principal components."),
    ("h2", "18.3 Entity Distinctions"),
    ("p",
     "Alert, Incident, Situation, Investigation and Case are kept explicitly distinct: an Alert is a rule-driven "
     "signal; an Incident is a domain-specific event (Ch.10); a Situation is a human- or rule-initiated grouping "
     "of related Alerts/Incidents/evidence across domains; an Investigation is scoped analytical work; a Case is "
     "the regulatory workflow container (Ch.16). Promotion between them is explicit, never implicit."),
    ("h2", "18.4 Alert Lifecycle"),
    ("flow",
     [
        "Effective-dated Alert Rule evaluated against canonical/analytical data",
        "Alert raised with severity and supporting evidence references",
        "Notification Service delivers to subscribed roles",
        "Human acknowledges and investigates, or groups into a Situation",
        "Alert closed with recorded closure authority and reason",
     ],
     "Alert lifecycle from rule evaluation to closure."),
    ("h2", "18.5 National Operating Picture States"),
    ("table",
     ["State", "Meaning"],
     [
        ["Known", "Data is current and validated for the relevant geography/domain."],
        ["Missing", "Expected data has not arrived; distinct from a zero or good-status value (Ch.5, Ch.6)."],
        ["Stale", "Data was received but has exceeded its freshness window."],
        ["Waiting", "A workflow or acquisition Run is in progress (e.g. WAITING_FOR_PM, Ch.21)."],
        ["Contradictory", "Two sources disagree and the conflict is preserved rather than resolved silently (Ch.17)."],
    ],
     "National Operating Picture status vocabulary."),
    ("h2", "18.6 Data Model"),
    ("bullets", [
        "Alert Rule — condition, severity, effective date range, owner.",
        "Alert — rule reference, raised time, evidence references, acknowledgement/closure trail.",
        "Situation — grouped Alerts/Incidents/evidence, lifecycle status, assigned owner.",
    ]),
    ("h2", "18.7 Security Controls"),
    ("bullets", [
        "Alert closure and Situation-lifecycle changes are audited with actor identity (Ch.23).",
    ]),
    ("h2", "18.8 Failure Modes"),
    ("bullets", [
        "REWS Engine degraded: last-known Alert state remains visible with a staleness indicator; the engine fails closed on new rule evaluation rather than silently skipping checks (Ch.28)."],
    ),
    ("h2", "18.9 Non-Functional Requirements"),
    ("bullets", [
        "Alert rule evaluation runs on each relevant data refresh cycle with raised-Alert latency bounded per severity tier (Ch.30)."],
    ),
    ("h2", "18.10 Acceptance Criteria"),
    ("bullets", [
        "Every National Operating Picture status in §18.5 is demonstrably distinguishable in the workspace for a representative geography.",
        "A rule-driven Alert is demonstrably traceable to its supporting evidence.",
    ]),
    ("proposed",
     "Confirm severity tiers, escalation timing and closure authority per Alert category with NCA operations "
     "leadership; the REWS rule model accommodates any agreed severity scheme via the Rule Service (Ch.22)."),
    ("trace", "NCIE-001 §Situational Awareness, Early Warning, Alerting & National Communications Operating Picture."),
]

# ---------------------------------------------------------------------------
# Chapter 19 — Intelligence Assistant & Conversational Orchestration
# ---------------------------------------------------------------------------
BLOCKS[19] = [
    ("status", "Full production content, including the v0.4 controlled-update amendment for active AI participation. Traces to NCIE-001 v1.2 NCIE Intelligence Assistant; NCIE Intelligence Assistant, Conversational Intelligence, Collaborative Brainstorming & Governed Memory (amended Ch.14/15/18)."),
    ("h2", "19.1 Scope"),
    ("p",
     "Defines the Assistant as a governed NCIE interface: multi-turn conversational access to authoritative "
     "platform state, plus — following the v0.4 amendment — the ability to participate proactively in "
     "human-to-human discussion under bounded, human-controlled conditions (see also Chapter 20, which holds "
     "the primary architecture for collaborative reasoning)."),
    ("h2", "19.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Conversation Service", "Manages multi-turn dialogue state per user/room."],
        ["Context Resolver", "Resolves operator/geography/date/entity context from conversation and workspace state (Ch.3)."],
        ["Tool Gateway", "Exposes evidence/map/rule/source/workflow tools to the model under authorization filtering."],
        ["Model Abstraction", "Provider-neutral interface to the Model Gateway (Ch.24)."],
        ["Grounding Layer", "Ensures answers are derived from authoritative NCIE state, not model-invented content."],
        ["Proactive Contribution Controller", "(v0.4) Decides whether/when the Assistant contributes without being directly asked."],
        ["Participation Policy Adapter", "(v0.4) Applies the active room's Participation Mode (Ch.20 §20.7) to Assistant behaviour."],
        ["Collaborative Context Adapter", "(v0.4) Feeds the Assistant the current Collaborative Reasoning State (Ch.20) so it follows the live discussion."],
        ["Grounded Contribution Planner", "(v0.4) Plans a proactive contribution (question, evidence, challenge) grounded in authorized tools before it is offered."],
        ["Assistant Naming Configuration", "Externalises the user-facing Assistant name (ARGUS) from internal identifiers, APIs, schemas, workflow definitions, audit events and domain services (§19.11)."],
        ["Agent Capability Discovery Adapter", "(v0.5) Determines whether an eligible Registered Reusable Agent adequately satisfies a task before ARGUS requests Dynamic Agent Synthesis via the Agent Factory (Ch.24 §24.4A; §19.2A)."],
    ],
     "Intelligence Assistant & Conversational Orchestration principal components."),
    ("h2", "19.2A ARGUS Consumption of Registered and Dynamically Synthesized Agents (v0.5)"),
    ("p",
     "ARGUS does not itself construct, validate or register agents; it consumes agent capability through "
     "the governed Agent Factory and Agent Registry defined in Chapter 24 §24.4A. When a task requires "
     "specialized analytical capability, ARGUS:"),
    ("bullets", [
        "discovers eligible existing Registered Reusable Agents through the Agent Capability Discovery Adapter;",
        "determines whether an adequate eligible capability already exists;",
        "where none exists, requests Dynamic Agent Synthesis through the governed Agent Factory;",
        "receives and uses a bounded Ephemeral Agent created from approved NCIE primitives;",
        "continues to operate within the same authorization, context, tool and model controls as any other ARGUS-orchestrated capability (§19.7).",
    ]),
    ("p",
     "ARGUS ≠ AGENT FACTORY: ARGUS requests synthesis; it does not itself perform Agent Definition "
     "construction, VPF Gate A validation, sandboxing or activation, all of which remain Agent Factory "
     "responsibilities (Ch.24 §24.4A.1). SYNTHESIS ≠ REGISTRATION and SYNTHESIS ≠ AUTHORITY CREATION: a "
     "synthesized agent is ephemeral and unregistered by default, and gains no institutional authority "
     "ARGUS itself does not already hold. Where a task requires a capability outside the available "
     "approved primitives, the architecture routes to an ENGINEERING CHANGE CANDIDATE (Ch.24 §24.4A.1) "
     "rather than allowing ARGUS to fabricate infrastructure."),
    ("h2", "19.3 Invoked Interaction Flow"),
    ("flow",
     [
        "User asks a question in the workspace or a room",
        "Context Resolver grounds operator/geography/date/entity context",
        "Tool Gateway invokes authorized evidence/map/rule/source/workflow tools",
        "Grounding Layer composes an answer from authoritative results only",
        "Conversation Service returns the answer with source references",
     ],
     "Standard invoked Assistant interaction."),
    ("h2", "19.4 Proactive Contribution (v0.4 amendment)"),
    ("p",
     "In Participatory Mode (Ch.20 §20.7), the Assistant is architecturally permitted to contribute without a "
     "direct question, subject to the following required behaviours:"),
    ("bullets", [
        "Follows permitted human-to-human discussion and resolves operator, geography, time, cells, hypotheses and the active analytical thread before contributing.",
        "May ask analytically useful questions, introduce authorized evidence, challenge assumptions, compare hypotheses and identify evidence gaps.",
        "Every proactive contribution is grounded in authoritative NCIE services via the Tool Gateway — never in unexamined model reasoning alone.",
        "Observes non-dominance: useful, occasional contribution, not a reply after every human message; humans can sustain uninterrupted human-to-human discussion.",
    ]),
    ("p",
     "Example invoked query: “ARGUS, why is this cell degraded?” Example proactive contribution, always "
     "attributed and never presented as confirmed fact: “ARGUS Hypothesis — Possible Shared Transmission "
     "Dependency,” not “Confirmed Cause — Shared Transmission Dependency.”"),
    ("h2", "19.5 Participation Modes Consumed"),
    ("p",
     "The Assistant does not own participation-mode state; it consumes the mode set at the room level by the "
     "Participation Mode Manager (Ch.20 §20.7) through the Participation Policy Adapter."),
    ("h2", "19.6 Data Model"),
    ("bullets", [
        "Conversation — participant(s), room reference (if any), turn history, resolved context.",
        "Tool Invocation — tool name, parameters, authorization check result, response reference.",
        "Proactive Contribution Candidate — trigger, planned content, grounding references, offered/suppressed decision.",
    ]),
    ("h2", "19.7 Security Controls"),
    ("bullets", [
        "Tool Gateway enforces the same authorization layers as direct API access (Ch.4); the Assistant never has implicit elevated access.",
        "Proactive contributions never introduce evidence the current room participants are not individually authorized to see (Ch.20 §20.9).",
        "(v0.5) Dynamic Agent Synthesis does not grant ARGUS or the synthesized Ephemeral Agent elevated access beyond the requesting task's current authorization; the agent remains subject to the same Model Gateway, Tool Gateway and Context/Memory boundaries as invoked Assistant use (Ch.24 §24.4A.1, §24.4A.8).",
    ]),
    ("h2", "19.8 Failure Modes"),
    ("bullets", [
        "Model Gateway unavailable: Conversation Service degrades to direct tool/query access without conversational framing; core NCIE data remains reachable (Ch.28).",
        "Grounding Layer cannot verify a claim against authoritative state: the Assistant states the limitation rather than presenting an ungrounded answer as fact.",
        "(v0.5) Agent Factory or VPF unavailable: ARGUS continues to operate using eligible Registered Agents and direct governed model use; Dynamic Agent Synthesis and validated release of new substantive AI output degrade explicitly rather than silently (Ch.28 §28.3).",
    ]),
    ("h2", "19.9 Non-Functional Requirements"),
    ("bullets", [
        "Invoked responses grounded in a single tool call return within 3 seconds at p95 (Ch.30).",
        "Proactive contribution evaluation does not add perceptible latency to ordinary human-to-human messages in a room.",
    ]),
    ("h2", "19.10 Acceptance Criteria"),
    ("bullets", [
        "An invoked question is demonstrably answered using only authoritative tool results, with sources shown.",
        "In Participatory Mode, the Assistant demonstrably refrains from responding to every message (non-dominance) while still surfacing at least one genuinely useful unprompted contribution in a scripted test discussion.",
    ]),
    ("h2", "19.11 ARGUS Naming Boundary"),
    ("p",
     "The NCIE Intelligence Assistant is presented to users under the institutional pseudo-name ARGUS — "
     "Adaptive Regulatory Governance & Unified Surveillance. This section fixes the boundary between that "
     "presentation identity and the underlying architecture defined by this chapter and Chapter 20."),
    ("bullets", [
        "ARGUS = User-Facing Assistant Identity, and not ARGUS = Separate Intelligence System — ARGUS is a human-friendly invocation and presentation identity for the one NCIE Intelligence Assistant described throughout this specification, never a second, independently governed system.",
        "Configurable naming — the user-facing name is externalised through the Assistant Naming Configuration component (§19.2) and is not hard-coded into APIs, database schemas, workflow definitions, audit events or domain services, so the institutional name can change without redesigning the Assistant architecture.",
        "Stable identity in audit — regardless of the user-facing name in effect, material Assistant actions retain a stable machine/service identity for audit (Ch.23), provenance, security (Ch.4, Ch.26) and model governance (Ch.24).",
        "Authorization binds to the stable internal identity, not the display name — whether presented as ARGUS or a future alternate institutional name, the Authorization Service (Ch.4) and Model Registry (Ch.24) evaluate the same underlying service identity, so a rename never requires reissuing policy, approvals or evaluation history.",
    ]),
    ("proposed",
     "Confirm which conversational actions require explicit user confirmation before execution (e.g. triggering an "
     "acquisition workflow via Ch.21) versus which are safe to answer directly; default is that any action with a "
     "side effect requires confirmation, and any read-only query does not."),
    ("trace", "NCIE-001 §NCIE Intelligence Assistant; §NCIE Intelligence Assistant, Conversational Intelligence, Collaborative Brainstorming & Governed Memory; NCIE-001 v1.3 §12.77-§12.79; NCIE-007 v1.1 Ch.11 §11.3, §11.9."),
]

# ---------------------------------------------------------------------------
# Chapter 20 — Memory, Collaborative Intelligence & Multi-User Brainstorming
# ---------------------------------------------------------------------------
BLOCKS[20] = [
    ("status", "Full production content — v0.4 in-place rewrite. This is the primary architecture for Human ↔ Human ↔ NCIE collaborative reasoning. Traces to NCIE-001 v1.2 Evidence, Knowledge, Memory & Provenance Governance; NCIE Intelligence Assistant, Conversational Intelligence, Collaborative Brainstorming & Governed Memory (amended Ch.14/15/18)."),
    ("h2", "20.1 Scope"),
    ("p",
     "Defines persistent private/shared/institutional memory, and the architecture that allows NCIE to "
     "participate as a governed, non-dominant collaborator in multi-user brainstorming rather than a "
     "passive, invoked-only chatbot. The interaction model is Human ↔ Human ↔ NCIE: humans retain "
     "intellectual direction and institutional authority at all times."),
    ("h2", "20.2 Memory Tiers"),
    ("table",
     ["Tier", "Description", "Sharing Rule"],
     [
        ["Private User Memory", "Persistent per-user memory of preferences, working context and history.", "Never automatically shared, even into a room the user joins."],
        ["Shared Room Memory", "Memory scoped to a specific collaborative room.", "Visible to current, authorized room participants only."],
        ["Institutional Memory", "Formally promoted knowledge (validated Findings, Decisions, adopted conclusions).", "Governed by the same authorization rules as its source domain."],
    ],
     "NCIE memory tiers and sharing rules."),
    ("h2", "20.3 Active AI Collaborative Participation"),
    ("p",
     "The following capabilities are explicit architectural requirements, not implied side effects of giving a "
     "room shared chatbot access:"),
    ("bullets", [
        "Active AI Brainstorming Participation — NCIE can participate in the intellectual exchange rather than merely wait for direct questions.",
        "AI Questioning — in Participatory Mode, NCIE may proactively ask analytically useful questions exposing assumptions, missing information, unexplored dimensions or reasoning weaknesses.",
        "AI Hypothesis Generation — NCIE may introduce clearly AI-attributed alternative hypotheses for human consideration; these remain working reasoning, not findings.",
        "AI Challenge Function — NCIE may challenge human or AI hypotheses using authorized evidence, inconsistencies, temporal or spatial relationships, source limitations and credible alternative explanations.",
        "Contradiction Seeking — NCIE may actively seek authorized evidence that contradicts the dominant working hypothesis, testing confirmation bias rather than reinforcing consensus.",
        "Competing-Hypothesis Analysis — multiple human and AI hypotheses may coexist, compared against supporting evidence, contradictory evidence, temporal fit, spatial fit, source quality, coverage and unresolved gaps.",
        "Discriminating-Evidence Identification — NCIE may identify which additional evidence would most help distinguish competing explanations.",
        "Evidence-Gap Identification — NCIE may identify missing PM, topology, incident, Traffic, QoS Campaign or other authorized evidence relevant to the discussion.",
    ]),
    ("p",
     "Every AI-originated hypothesis and question is rendered under ARGUS's name with explicit AI attribution "
     "(e.g. “ARGUS Hypothesis — Possible Shared Transmission Dependency”), and is never rendered in a form that "
     "could be mistaken for a confirmed cause or a human-originated Finding (Ch.19 §19.4)."),
    ("h2", "20.3A Realization via Registered or Ephemeral Synthesized Agents (v0.5)"),
    ("p",
     "Where a collaborative analytical role in §20.3 is realized using an AI agent rather than ARGUS's own "
     "direct model use, it may be realized through an approved Registered Reusable Agent or a bounded "
     "Ephemeral Synthesized Agent created under NCIE-007 governance (Ch.24 §24.4A). Such agents remain "
     "subordinate analytical capabilities: they do not gain Room authority, do not inherit pooled "
     "participant permissions (§20.9), do not become institutional decision makers, and do not change "
     "ARGUS's human-facing role or naming (Ch.19 §19.11)."),
    ("h2", "20.4 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Collaborative Reasoning State Service", "Owns the Collaborative Reasoning State: distinct from raw transcript and memory."],
        ["Collaborative Context Manager", "Tracks current focus, active analytical thread and room membership context."],
        ["Multi-Speaker Attribution Service", "Preserves who introduced, challenged, adopted, modified or rejected each idea, including explicit AI origin."],
        ["Analytical Thread Manager", "Keeps multiple concurrent questions/threads from cross-contaminating evidence or hypotheses."],
        ["Participation Mode Manager", "Owns and enforces the room's current Participation Mode."],
        ["Proactive Contribution Controller", "Shared with Ch.19; gates whether a planned AI contribution is actually offered."],
        ["Hypothesis Lifecycle Manager", "Tracks human/AI hypotheses from proposal through comparison to adoption, deferral or rejection."],
        ["Contradiction / Evidence-Gap Service", "Surfaces contradictions and evidence gaps relevant to the active thread."],
        ["Shared Evidence Board", "Organizes references to authoritative Evidence objects, maps, campaigns, calculations, hypotheses, contradictions, notes and tasks without replacing the Evidence Service (Ch.23)."],
        ["Room-to-Workflow Bridge", "Shared with Ch.21; carries room-originated acquisition suggestions to the Automation Orchestrator."],
        ["Room Summary & Shift-Handover Service", "Reconstructs ‘where were we?’ by combining Shared Room Memory, Collaborative Reasoning State and current authoritative NCIE state."],
        ["Memory Promotion Service", "Governs deliberate promotion of collaborative reasoning into Institutional Knowledge, Findings or Decisions."],
    ],
     "Memory, Collaborative Intelligence & Multi-User Brainstorming principal components."),
    ("h2", "20.5 Collaborative Reasoning State"),
    ("p",
     "The Collaborative Reasoning State is a distinct object from the raw conversation transcript and from "
     "memory. It tracks: current focus, analytical threads, human hypotheses, AI hypotheses, evidence, "
     "contradictions, gaps, rejected/deferred ideas, tasks, automation requests and evidence being waited on. "
     "It is what the Room Summary & Shift-Handover Service reconstructs for a returning or newly joined "
     "participant."),
    ("h2", "20.6 Multi-Speaker Attribution & Analytical Threads"),
    ("bullets", [
        "Every contribution — human or AI — retains its originator, and adoption by a human never erases AI origin.",
        "Multiple analytical threads can coexist in one room without evidence or hypotheses being silently mixed between them.",
        "Room membership changes trigger authorization-aware handling of historical context — a newly joined participant does not automatically see history predating authorization checks passing for them.",
    ]),
    ("h2", "20.7 Participation Modes"),
    ("table",
     ["Mode", "Behaviour"],
     [
        ["Participatory", "Assistant may proactively contribute per §20.3, subject to non-dominance."],
        ["Invoked", "Assistant responds only when directly addressed; no proactive contribution."],
        ["Evidence-Watch", "Assistant stays silent on discussion but may surface material new evidence events (Ch.20 §20.10) as queued room events."],
        ["Silent", "Assistant takes no conversational action; room is human-only until mode changes."],
    ],
     "Persistent, human-controlled room Participation Modes."),
    ("p",
     "The active mode is always visible in the workspace under ARGUS's user-facing name, e.g. "
     "“ARGUS — Participatory,” “ARGUS — Invoked,” “ARGUS — Evidence-Watch,” “ARGUS — Silent” (Ch.19 §19.11). "
     "Authorized users may change the mode through structured UI controls and, where permitted, natural-"
     "language commands such as “ARGUS, don't interrupt unless new evidence arrives.”"),
    ("p",
     "Humans may also invoke Specialized Participation Roles — Devil's Advocate, Evidence Challenger, "
     "Historical Comparator, Data-Gap Analyst — which shape how NCIE contributes within Participatory Mode "
     "without granting any additional authority or data access beyond the participant's own permissions. In "
     "this configuration the workspace shows, for example, “ARGUS — Participatory / Evidence Challenger.”"),
    ("h2", "20.8 Non-Dominance and Human Intellectual Control"),
    ("bullets", [
        "Participatory Mode means useful proactive contribution, not a reply after every human message; humans must be able to sustain uninterrupted human-to-human discussion.",
        "Humans may accept, reject, modify, defer, redirect or formally promote any AI contribution, and may increase, constrain or silence AI participation at any time.",
    ]),
    ("h2", "20.9 Permission-Aware Collaboration"),
    ("bullets", [
        "Shared room context never pools participant permissions; each participant sees only what their own authorization permits, even within one room (Ch.4).",
        "Private User Memory is not automatically shareable merely because it would be relevant to the room's discussion — sharing requires a deliberate user action.",
    ]),
    ("h2", "20.10 Cross-Session Continuity and Event Awareness"),
    ("bullets", [
        "‘Where were we?’ reconstruction combines Shared Room Memory, Collaborative Reasoning State and current authoritative NCIE state — never a stale snapshot presented as current.",
        "Validated PM arrival, workflow completion, new incident reports, Traffic arrival or source corrections may return to the room as events in Participatory/Evidence-Watch mode.",
    ]),
    ("h2", "20.11 Room-to-Workflow Integration"),
    ("p",
     "Brainstorming may lead to governed evidence-acquisition requests via the Room-to-Workflow Bridge (shared "
     "with Ch.21). AI suggestion of an acquisition action remains architecturally distinct from execution "
     "authority; validated results return asynchronously to the originating Collaborative Reasoning State."),
    ("h2", "20.12 Formal Promotion Boundary"),
    ("p",
     "Collaborative reasoning remains distinct from formal analysis, Institutional Knowledge, Findings and "
     "Decisions until deliberately promoted through the Memory Promotion Service, which applies the same "
     "governance as the target object type (e.g. a promoted hypothesis becoming a Proposed Finding follows "
     "Ch.16's Finding Workflow)."),
    ("h2", "20.13 Cross-Chapter Architectural Invariants"),
    ("p", "The following invariants, introduced by the v0.4 collaborative-brainstorming amendment, bind Chapters 19, 20, 21, 23 and 24 collectively:"),
    ("bullets", [
        "Active AI participation does not create institutional authority.",
        "Collaborative Reasoning State is distinct from transcript, memory, evidence, formal analysis, finding and decision.",
        "Human adoption of an AI idea does not erase AI origin.",
        "Shared room context never pools participant permissions.",
        "Private memory is not shareable merely because it is relevant.",
        "Participatory Mode means useful proactive contribution, not continuous AI speech.",
        "Evidence-Watch does not create unrestricted monitoring authority.",
        "AI-suggested acquisition is not execution authority.",
        "Validated workflow results may return to the originating room asynchronously.",
        "Previous collaborative state must be reconciled with current authoritative NCIE state.",
        "Multiple analytical threads must remain separable.",
        "AI challenge is advisory; humans retain intellectual direction and institutional authority.",
        "(v0.5) A Registered Reusable Agent or Ephemeral Synthesized Agent realizing a collaborative role gains no Room authority, pooled permissions or institutional decision authority by virtue of participating.",
    ]),
    ("h2", "20.14 Data Model"),
    ("bullets", [
        "Room — participants, permission map, Participation Mode, linked threads.",
        "Analytical Thread — topic, linked hypotheses, linked evidence, status.",
        "Hypothesis — originator (human/AI), content, supporting/contradicting evidence links, status (active/adopted/deferred/rejected).",
        "Collaborative Evidence Board Entry — reference to authoritative Evidence, added-by, thread linkage.",
        "Promotion Record — source collaborative object, target formal object, promoting actor, timestamp.",
    ]),
    ("h2", "20.15 Security Controls"),
    ("bullets", [
        "Room join/leave and permission changes are enforced by the Authorization Service (Ch.4), not by room-local logic.",
        "Every promotion action is audited with full before/after state (Ch.23 §23.9).",
    ]),
    ("h2", "20.16 Failure Modes"),
    ("bullets", [
        "Model Gateway unavailable during a room session: room continues as human-only (Silent-equivalent behaviour) without losing Collaborative Reasoning State (Ch.28).",
        "Conflicting concurrent edits to the Collaborative Reasoning State: resolved with last-writer-wins per field plus a visible edit trail, never silent data loss.",
    ]),
    ("h2", "20.17 Non-Functional Requirements"),
    ("bullets", [
        "Room Summary/Shift-Handover reconstruction for a typical room completes within 5 seconds at p95.",
    ]),
    ("h2", "20.18 Acceptance Criteria"),
    ("bullets", [
        "A scripted two-human, mixed-permission brainstorming session demonstrates permission-aware filtering, non-dominant proactive contribution, and correct multi-speaker attribution.",
        "A promoted hypothesis is demonstrably traceable from its originating Collaborative Reasoning State entry to the resulting Proposed Finding (Ch.16)."],
    ),
    ("proposed",
     "Confirm the default Participation Mode for ordinary rooms (proposed default: Participatory) versus "
     "Anti-Fraud/regulatory rooms (proposed default: Invoked, given sensitivity), and who may change mode "
     "(proposed default: room owner or any participant with Case-officer-equivalent role), with NCIE governance "
     "leadership."),
    ("proposed",
     "Confirm which specialized brainstorming roles (§20.7) are required at launch versus a later phase; proposed "
     "default is Devil's Advocate and Evidence Challenger at launch, with Historical Comparator and Data-Gap "
     "Analyst following in a subsequent release."),
    ("proposed",
     "Confirm room/thread retention period; proposed default aligns with the Evidence retention period in Ch.23 "
     "given rooms may contain material analytical content."),
    ("trace", "NCIE-001 §Evidence, Knowledge, Memory & Provenance Governance; §NCIE Intelligence Assistant, Conversational Intelligence, Collaborative Brainstorming & Governed Memory (Ch.14/15/18 amendments); NCIE-007 v1.1 Ch.15 (Multi-Agent Coordination & Conflict Handling)."),
]

# ---------------------------------------------------------------------------
# Chapter 21 — Automation Orchestrator, RPA, Scheduling & Persistent Workflows
# ---------------------------------------------------------------------------
BLOCKS[21] = [
    ("status", "Full production content, including the v0.4 room-to-workflow amendment. Traces to NCIE-001 v1.2 Automation Orchestration & RPA Data Acquisition; Automation Orchestration, RPA Governance, Scheduling & Autonomous Workflow Execution."),
    ("h2", "21.1 Scope"),
    ("p",
     "Defines provider-neutral automation: the Capability Registry abstraction, Request/Run state machine, "
     "recurring schedules, persistent wait states, and the governed bridge that lets collaborative rooms "
     "(Ch.20) suggest and track acquisition workflows."),
    ("h2", "21.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Capability Registry", "Abstracts UiPath, Power Automate, Automation Anywhere and future providers behind one capability contract."],
        ["Orchestrator", "Dispatches Requests to providers, tracks Runs, applies failover/retry/idempotency."],
        ["Scheduler", "Manages recurring schedules and condition-based triggers."],
        ["Workflow Engine", "Executes persistent multi-step workflows, including long-lived WAITING_FOR_PM-style states."],
        ["Provider Adapters", "Provider-specific execution shims behind the Capability Registry contract."],
        ["Human Tasks", "Represents steps requiring human action within an otherwise automated workflow."],
        ["Room-to-Workflow Bridge", "(v0.4, shared with Ch.20) Carries room-originated Automation Requests with room/thread provenance."],
        ["Workflow-to-Room Event Adapter", "(v0.4) Returns validated workflow results asynchronously into the originating Collaborative Reasoning State."],
        ["Collaborative Request Correlation", "(v0.4) Correlates a room-suggested request with its resulting Request/Run/Result chain."],
    ],
     "Automation Orchestrator, RPA, Scheduling & Persistent Workflows principal components."),
    ("h2", "21.3 Request/Run State Model"),
    ("p",
     "Request, Run, provider, bot and validation states are kept explicitly separate so a failed Run does not "
     "corrupt the Request's history and a provider substitution does not require redefining the Request."),
    ("flow",
     [
        "Automation Request (scheduled, event-triggered, or room-suggested)",
        "Capability Registry selects provider/bot",
        "Orchestrator dispatches Run with idempotency key",
        "Provider executes; Workflow Engine tracks WAITING_FOR_* states as needed",
        "Validation Pipeline checks Run output (Ch.6)",
        "Result delivered to originating consumer (workspace, schedule, or Room via Workflow-to-Room Event Adapter)",
     ],
     "Automation Request lifecycle from trigger to delivered result."),
    ("h2", "21.4 Room-Originated Requests (v0.4)"),
    ("bullets", [
        "Collaborative rooms can suggest and initiate governed evidence-acquisition workflows via the Room-to-Workflow Bridge.",
        "AI suggestion of an acquisition remains architecturally distinct from execution authority — a human authorizes execution (Ch.4 separation of duties).",
        "Room-originated Automation Requests retain room/thread provenance for later reconstruction (Ch.20 §20.5).",
        "Validated results return asynchronously into the originating Collaborative Reasoning State via the Workflow-to-Room Event Adapter.",
        "WAITING_FOR_PM, WAITING_FOR_TRAFFIC and similar persistent states can be watched by a room in Evidence-Watch mode (Ch.20 §20.7) without granting the room broader monitoring authority.",
        "High-risk actions remain behind human authorization/approval even when proposed during brainstorming.",
    ]),
    ("h2", "21.5 Data Model"),
    ("bullets", [
        "Automation Request — trigger type (schedule/event/room), target capability, parameters, authorization state.",
        "Run — provider, bot identity, start/end, status, idempotency key, output artifact reference.",
        "Schedule — recurrence rule, target Request template, owner.",
        "Persistent Wait State — named state (e.g. WAITING_FOR_PM), entered/resolved timestamps, watching rooms.",
    ]),
    ("h2", "21.6 Security Controls"),
    ("bullets", [
        "Provider credentials are held by the Machine Identity Registry (Ch.4), never embedded in workflow definitions.",
        "Room-suggested high-risk Requests require explicit human authorization distinct from the suggesting AI or the requesting room membership alone.",
    ]),
    ("h2", "21.7 Failure Modes"),
    ("bullets", [
        "Provider outage: Orchestrator fails over to an alternate configured provider where available, or queues the Request with visible degraded status; waiting workflows survive a platform restart (Ch.28).",
        "Duplicate trigger (e.g. re-delivered event): idempotency key prevents a duplicate Run from executing twice.",
    ]),
    ("h2", "21.8 Non-Functional Requirements"),
    ("bullets", [
        "Scheduled Requests fire within 1 minute of their scheduled time at p99.",
        "Failover to an alternate provider, where configured, completes within the provider's own timeout plus a bounded retry window (Ch.30)."],
    ),
    ("h2", "21.9 Acceptance Criteria"),
    ("bullets", [
        "A room-suggested acquisition Request is demonstrably blocked from execution without separate human authorization, and its result demonstrably returns to the originating room.",
        "A simulated provider outage demonstrably triggers failover or a visibly queued, non-silent degraded state.",
    ]),
    ("proposed",
     "Confirm auto-escalation-versus-approval policy per automation category, and RPA provider policy (which "
     "providers are approved and for which capability classes), with NCIE automation governance leadership."),
    ("trace", "NCIE-001 §Automation Orchestration & RPA Data Acquisition; §Automation Orchestration, RPA Governance, Scheduling & Autonomous Workflow Execution."),
]

# ---------------------------------------------------------------------------
# Chapter 22 — Rules, Calculation, Configuration & Temporal Governance
# ---------------------------------------------------------------------------
BLOCKS[22] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression; Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
    ("h2", "22.1 Scope"),
    ("p",
     "Centralizes every changeable rule and deterministic calculation used elsewhere in this specification — "
     "the surcharge rate (Ch.12), SIM registration limits (Ch.14), KPI thresholds (Ch.7) and REWS alert rules "
     "(Ch.18) — so that none of it is hardcoded inside AI or bot logic."),
    ("h2", "22.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Rule Service", "Authoritative store of effective-dated rules consumed by all domain calculators."],
        ["Configuration Service", "Non-rule operational configuration (thresholds unrelated to calculation, feature toggles)."],
        ["Calculation Engine", "Executes deterministic calculations against current or historical rule versions."],
        ["Version Store", "Retains every historical and future-scheduled rule version, immutable once superseded."],
    ],
     "Rules, Calculation, Configuration & Temporal Governance principal components."),
    ("h2", "22.3 Temporal Governance Principle"),
    ("p",
     "Rules are effective-dated: a rule has a defined start (and optionally end) date. Both historical and "
     "future-scheduled rules can exist simultaneously. A calculation always uses the rule version effective "
     "at the calculation's reference date, not the rule version current at query time — this is what makes "
     "decision-time reconstruction (Ch.23) correct."),
    ("h2", "22.4 Conflict Handling"),
    ("p",
     "Two rule versions with overlapping effective ranges for the same rule key are a configuration error: the "
     "Rule Service blocks authoritative output for the affected calculation rather than silently picking one, "
     "and surfaces the conflict for administrator resolution."),
    ("h2", "22.5 Scenario Modelling"),
    ("p",
     "“What-if” scenario runs (e.g. modelling a proposed rate change) use a scenario-scoped rule overlay "
     "and never overwrite the authoritative Version Store history."),
    ("h2", "22.6 Data Model"),
    ("bullets", [
        "Rule — key, value, effective start/end date, version, approving actor.",
        "Rule Change Request — proposed value, proposed effective date, approval status.",
        "Scenario — named what-if run, overlay rules, isolated from authoritative history.",
    ]),
    ("h2", "22.7 Security Controls"),
    ("bullets", [
        "Rule changes require an authorized rule administrator and are individually audited (Ch.23).",
        "AI and bot components read rules through the Rule Service API only; no chapter of this specification permits a rule value to be embedded in model prompts or bot scripts as a constant.",
    ]),
    ("h2", "22.8 Failure Modes"),
    ("bullets", [
        "Rule Service unavailable: Calculation Engine uses the last successfully cached rule set with a visible staleness indicator; it does not fall back to a hardcoded default (Ch.28)."],
    ),
    ("h2", "22.9 Non-Functional Requirements"),
    ("bullets", [
        "Rule lookups for calculation complete within 50ms at p95 given caching (Ch.30)."],
    ),
    ("h2", "22.10 Acceptance Criteria"),
    ("bullets", [
        "An overlapping-effective-date rule conflict is demonstrably blocked rather than silently resolved.",
        "A scenario run is demonstrably isolated from and does not alter authoritative rule history.",
    ]),
    ("trace", "NCIE-001 §Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression; §Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
]

# ---------------------------------------------------------------------------
# Chapter 23 — Evidence, Provenance, Audit & Decision-Time Reconstruction
# ---------------------------------------------------------------------------
BLOCKS[23] = [
    ("status", "Full production content, including the v0.4 collaborative-provenance amendment. Traces to NCIE-001 v1.2 Evidence, Knowledge, Memory & Provenance Governance."),
    ("h2", "23.1 Scope"),
    ("p",
     "Defines defensibility from source to decision: end-to-end lineage, attribution, contradiction "
     "preservation, decision-time reconstruction, and — following the v0.4 amendment — provenance for "
     "collaborative human/AI reasoning."),
    ("h2", "23.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Evidence Service", "Authoritative store of Evidence objects with source, acquisition and validation lineage."],
        ["Provenance Graph", "Links every derived fact/finding back through its transformation chain to origin evidence."],
        ["Audit Service", "Records actor (human/AI/bot/service), action, target and timestamp for sensitive reads/actions."],
        ["Historical Snapshot Service", "Reconstructs authoritative state as it existed at a prior point in time."],
        ["Collaborative Provenance Extension", "(v0.4) Extends provenance to human/AI contribution origin within collaborative rooms."],
        ["Promotion Provenance", "(v0.4) Tracks the path: AI/Human contribution → working hypothesis → formal analytical object."],
        ["Material Collaboration Audit Events", "(v0.4) Audits participation-mode changes, sensitive evidence introduction, formal promotion and room-originated automation."],
    ],
     "Evidence, Provenance, Audit & Decision-Time Reconstruction principal components."),
    ("h2", "23.3 End-to-End Lineage"),
    ("p",
     "Every canonical fact, calculation, Finding and Decision carries a chain back to its originating Evidence: "
     "source system, acquisition Run (Ch.6), applicable rule version (Ch.22), and every transformation applied. "
     "Human, AI, bot and service attribution is recorded at each step."),
    ("rel",
     [
        ("Source Evidence", "supports", "Canonical Fact"),
        ("Canonical Fact + Rule Version", "produces", "Calculation / Correlation"),
        ("Calculation / Correlation", "supports", "Proposed Finding"),
        ("Proposed Finding", "becomes (on human validation)", "Validated Finding / Decision"),
     ],
     "End-to-end provenance chain from evidence to decision."),
    ("h2", "23.4 Contradiction Preservation"),
    ("p",
     "Contradictory evidence or facts are preserved side by side with their provenance (Ch.5, Ch.17), never "
     "silently reconciled by discarding one. A Decision made despite a known contradiction records that the "
     "contradiction existed and was considered."),
    ("h2", "23.5 Decision-Time Reconstruction"),
    ("p",
     "The Historical Snapshot Service can reconstruct exactly what evidence, rule versions and analytical "
     "objects were available at a given decision's time, explicitly excluding evidence that arrived later — "
     "this is what makes a Decision defensible against later-discovered information."),
    ("h2", "23.6 Collaborative Provenance (v0.4)"),
    ("bullets", [
        "Human and AI contribution origin remains visible when collaborative reasoning (Ch.20) becomes material to a Finding or Decision.",
        "Promotion Provenance tracks the full path from an AI or human contribution through working hypothesis to formal analytical object.",
        "The Collaborative Evidence Board (Ch.20 §20.4) references authoritative evidence rather than copying authority into the room — the room is never itself a source of truth.",
        "Material collaborative events are audited: participation-mode changes, introduction of sensitive evidence, formal promotion, and room-originated automation (Ch.21 §21.4).",
        "Private model chain-of-thought is not required to be stored or disclosed; provenance covers grounded tool inputs/outputs and stated conclusions, not internal model deliberation.",
        "Decision-time reconstruction can show which collaborative evidence and formal objects were available at the time, alongside the standard evidence chain.",
    ]),
    ("h2", "23.7 Data Model"),
    ("bullets", [
        "Evidence — content reference, source, acquisition metadata, validation status, classification.",
        "Provenance Edge — from-object, to-object, transformation type, actor (human/AI/bot/service), timestamp.",
        "Audit Event — actor, action, target, timestamp, sensitivity tier.",
        "Snapshot Request — reference date/time, resulting reconstructed state reference.",
    ]),
    ("h2", "23.8 Security Controls"),
    ("bullets", [
        "Sensitive reads (protected identities, Anti-Fraud sensitive joins) and sensitive actions (blocking, rule changes) are always audited, never optional (Ch.14, Ch.15, Ch.22).",
        "Audit records are append-only and themselves covered by the platform's backup/DR posture (Ch.28)."],
    ),
    ("h2", "23.9 Failure Modes"),
    ("bullets", [
        "Audit Service degraded: sensitive actions that require audit are blocked from completing rather than proceeding unaudited (fail closed).",
    ]),
    ("h2", "23.10 Non-Functional Requirements"),
    ("bullets", [
        "A decision-time reconstruction for a typical Case completes within 10 seconds at p95 (Ch.30)."],
    ),
    ("h2", "23.11 Acceptance Criteria"),
    ("bullets", [
        "A Finding's full provenance chain from source evidence to Decision is demonstrably reconstructable.",
        "A decision-time reconstruction demonstrably excludes evidence that arrived after the decision's timestamp.",
        "A promoted collaborative hypothesis is demonstrably traceable via Promotion Provenance to its originating room contribution.",
    ]),
    ("proposed",
     "Confirm Evidence and audit retention periods, and the specific list of heightened-audit event types beyond "
     "those already named in this chapter, with NCA audit/compliance leadership."),
    ("trace", "NCIE-001 §Evidence, Knowledge, Memory & Provenance Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 24 — AI Platform, Model Gateway, Guardrails & Evaluation
# ---------------------------------------------------------------------------
BLOCKS[24] = [
    ("status", "Full production content, including the v0.4 collaborative-evaluation amendment. Traces to NCIE-001 v1.2 NCIE Intelligence Assistant; Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance."),
    ("h2", "24.1 Scope"),
    ("p",
     "Defines AI integration without giving any model ownership of NCIE state: provider abstraction, minimal "
     "authorized context, guardrails, and — following the v0.4 amendment — evaluation specific to active "
     "collaborative participation before it is enabled in production."),
    ("h2", "24.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Model Gateway", "Provider-neutral abstraction over internal/external AI models."],
        ["Context Builder", "Assembles authorization-filtered, minimal context for a given request."],
        ["Policy / Guardrails", "Enforces prompt-injection defense, secrets exclusion and output policy."],
        ["Model Registry", "Catalogue of approved models/providers with data-handling classification."],
        ["Evaluation Harness", "Runs NCIE-specific evaluations before a model/provider is approved for production use."],
        ["Collaborative Evaluation Harness", "(v0.4) Evaluates collaborative-specific behaviour before Participatory Mode production use."],
        ["Participation Guardrail Policy", "(v0.4) Prevents permission pooling, private-memory leakage and privilege escalation during proactive participation."],
        ["Context Minimizer", "(v0.4) Reduces room context sent to external models to the minimum necessary."],
        ["Collaborative Quality Monitor", "(v0.4) Monitors over-participation and under-participation as distinct, tracked failure modes."],
        ["Agent Factory", "(v0.5) Governed construction/preparation of bounded Agent Definitions from approved primitives (§24.4A.1)."],
        ["Agent Registry / Capability Registry", "(v0.5) Distinguishes Registered Reusable Agents from Ephemeral Agent Definitions/Instances and Promotion Candidates (§24.4A.2)."],
        ["Ephemeral Agent Runtime", "(v0.5) Bounded execution environment for run-scoped task-specific agents (§24.4A.3)."],
        ["VPF", "(v0.5) Governed validation architecture for substantive AI-generated output, comprising Gate A, Gate B and the VPF Profile Registry (§24.4A.4-§24.4A.7)."],
    ],
     "AI Platform, Model Gateway, Guardrails & Evaluation principal components."),
    ("h2", "24.3 Context and Provider Boundary"),
    ("p",
     "The Context Builder assembles only the authorization-filtered, minimal context a request needs. No "
     "secret, credential or field the requesting identity is not authorized to see crosses the Model Gateway "
     "boundary. External model use is governed by explicit data-residency and retention/training policy per "
     "model in the Model Registry."),
    ("rel",
     [
        ("Requesting Service (Assistant, Room, Workflow)", "requests context from", "Context Builder"),
        ("Context Builder", "applies authorization filter, sends minimal context to", "Model Gateway"),
        ("Model Gateway", "routes to", "Approved Internal/External Model"),
        ("Policy / Guardrails", "inspects request and response of", "Model Gateway"),
     ],
     "AI Platform request path from requesting service to model, under Context Builder and Guardrails control."),
    ("h2", "24.4 Guardrails"),
    ("bullets", [
        "Prompt-injection defense: content originating from ingested sources (email, files, external text) is treated as data, never as instructions to the model.",
        "No secrets in prompts: credentials, API keys and similar are structurally excluded from any context assembled by the Context Builder.",
        "External retention/training use is governed per model in the Model Registry; default is training-use disabled unless explicitly approved.",
        "Participation Guardrail Policy (v0.4) specifically prevents a proactive contribution from pooling room permissions, leaking Private User Memory, or escalating privilege beyond the contributing participant's own access.",
    ]),
    ("h2", "24.4A AI Orchestration Extension — Agent Factory, Ephemeral Agents & VPF (v0.5)"),
    ("p",
     "This section extends, and does not replace, the AI Platform architecture in §24.2-§24.4. ARGUS "
     "continues to operate through the governed Model Gateway and Tool Gateway boundaries with no "
     "implicit elevated access; authorization remains current and externally governed; deterministic "
     "NCIE capabilities continue when AI is unavailable; and AI does not approve institutional Decisions "
     "or production state. Authority: NCIE-001 v1.3 §12.77-§12.80A, §18.241A; NCIE-007 v1.1. This "
     "section names no specific Agent Framework, container runtime, model provider, sandbox product, "
     "workflow engine, VPF software or registry product as architectural truth — NCIE-004 governs "
     "technology selection (§1.3.2)."),
    ("h3", "24.4A.1 Agent Factory"),
    ("p",
     "Responsible for governed construction and preparation of bounded task-specific Agent Definitions "
     "from approved primitives. It may coordinate Definition Construction, Structural Validation, Policy "
     "Compilation, VPF Gate A (§24.4A.5), Sandbox/Evaluation, Activation Preparation and Lifecycle "
     "Integration. The Agent Factory is a logical capability, not a requirement for one physical "
     "microservice (NCIE-004 governs implementation). CODEX / ENGINEERING BUILDS AND MAINTAINS THE AGENT "
     "FACTORY AND INTRODUCES NEW ENGINEERING PRIMITIVES; ARGUS USES THE FACTORY TO SYNTHESIZE BOUNDED "
     "AGENTS FROM APPROVED PRIMITIVES. Codex is therefore not a runtime dependency for each individual "
     "bounded agent; Codex/engineering re-enters only when a task requires a new Tool, Connector, "
     "Runtime Capability, Security Primitive, Persistent Service, Infrastructure or material Production "
     "Engineering Change (§24.4A.1 boundary; Ch.32 §32.4A)."),
    ("h3", "24.4A.2 Agent Registry / Capability Registry"),
    ("p",
     "Recognizes the governed reusable-agent registry, distinguishing Registered Reusable Agents from "
     "Ephemeral Agent Definitions/Instances and from Promotion Candidates. Not every Ephemeral Agent "
     "becomes a permanent Registry entry; promotion is a separate, governed lifecycle action (NCIE-007 "
     "v1.1 Ch.12, Ch.33)."),
    ("h3", "24.4A.3 Ephemeral Agent Runtime"),
    ("p",
     "A logical execution boundary for run-scoped, task-specific agents. The runtime enforces Task Scope, "
     "Current Authorization, Permitted Models, Permitted Tools, Permitted Data/Context, Resource Limits, "
     "Network/Egress, Lifetime and Termination for every Ephemeral Agent it hosts."),
    ("h3", "24.4A.4 VPF"),
    ("p",
     "The governed validation architecture for substantive AI-generated output. ALL SUBSTANTIVE "
     "AI-GENERATED OUTPUT SHALL ENTER THE APPLICABLE VPF GOVERNANCE PATH BEFORE RELEASE AS A VALIDATED "
     "NCIE AI RESULT. Validation rigor may vary by governed profile, risk and output class (§24.4A.7); "
     "purely deterministic, non-AI processing remains outside the AI-output VPF mandate. VPF FAILURE "
     "SHALL NOT FAIL OPEN (Ch.28 §28.3)."),
    ("h3", "24.4A.5 VPF Gate A"),
    ("p",
     "Architecturally placed before novel Ephemeral Agent activation. Gate A validates the synthesized "
     "agent's capability envelope before execution. It does not validate future agent output — that is "
     "Gate B's responsibility (§24.4A.6)."),
    ("h3", "24.4A.6 VPF Gate B"),
    ("p",
     "Architecturally placed after substantive AI generation and before validated release or persistence. "
     "Gate B applies to substantive output from ARGUS direct model use, Registered Agents, Ephemeral "
     "Agents and multi-agent synthesis alike — no orchestration path is exempt by default."),
    ("h3", "24.4A.7 VPF Profile Registry"),
    ("p",
     "Recognizes logical governance for VPF Profile, Profile Version, Applicable Task/Risk/Output Class, "
     "Lifecycle State and Current Eligibility. Detailed profile schema is not defined here; NCIE-007 v1.1 "
     "Ch.26 §26.5 remains authoritative."),
    ("h3", "24.4A.8 Orchestration Control Plane and Agent Execution Plane"),
    ("p",
     "This chapter distinguishes two logical planes. The Orchestration Control Plane is responsible for "
     "Agent Discovery, Synthesis Request, Lifecycle, Registry State, Eligibility, Policy, Risk/Activation "
     "Requirements, VPF Requirements, Suspension and Routing. The Agent Execution Plane executes the "
     "bounded runtime workload only."),
    ("rel",
     [
        ("Orchestration Control Plane", "governs eligibility, policy, VPF requirements and routing for", "Agent Execution Plane"),
        ("Agent Execution Plane", "executes the bounded runtime workload; never administers", "Agent Registry, Model Registry, Tool Registry, VPF Policies or Agent Factory governance"),
     ],
     "Control Plane / Agent Execution Plane boundary — a logical distinction; physical deployment is governed by NCIE-004 where already established."),
    ("h3", "24.4A.9 Architectural Flows"),
    ("flow",
     ["ARGUS", "Agent Capability Discovery", "Eligible Registered Agent", "Model Gateway / Context / Tool Gateway", "AI Result", "VPF Gate B", "ARGUS / Human"],
     "Existing agent path — ARGUS uses an eligible Registered Reusable Agent."),
    ("flow",
     ["ARGUS", "No adequate eligible registered capability", "Agent Factory", "Agent Definition", "VPF Gate A", "Sandbox / Evaluation", "Ephemeral Agent Runtime", "Model Gateway / Context / Tool Gateway", "Agent Result", "VPF Gate B", "ARGUS / Human"],
     "Dynamic synthesis path — ARGUS requests bounded Ephemeral Agent synthesis when no adequate registered capability exists."),
    ("flow",
     ["ARGUS", "Required primitive unavailable", "ENGINEERING CHANGE CANDIDATE", "Human / Engineering / Codex process"],
     "Capability-gap path — a missing primitive routes to engineering, never fabrication."),
    ("h3", "24.4A.10 Gateway, Memory, Authority & Recursion Preservation"),
    ("bullets", [
        "AGENT → MODEL GATEWAY → ELIGIBLE MODEL, never AGENT → ARBITRARY PROVIDER.",
        "AGENT → TOOL GATEWAY → AUTHORIZED TOOL, never AGENT → DIRECT CONSEQUENTIAL SYSTEM ACCESS. Dynamic synthesis creates no bypass path for either gateway.",
        "Agents obtain governed context exclusively through the existing NCIE Memory/Context architecture (Ch.20); no unrestricted agent access to Institutional Memory, independent permanent agent memory, or agent ownership of NCIE Memory is depicted or specified. AGENT RUNTIME STATE ≠ INSTITUTIONAL MEMORY — detailed Memory semantics remain in NCIE-006.",
        "The effective capability of an agent remains bounded by the intersection of Current Human/Task Authorization, Agent Definition, Model Eligibility, Tool Policy, Data Classification, Context Policy and Runtime Policy; no component may expand authority independently.",
        "AGENT SYNTHESIS ≠ SELF-REGISTRATION: the Agent Factory may instantiate an Ephemeral Agent and ARGUS may recommend promotion, but the synthesized agent may not register itself — permanent reusable registration remains a governed lifecycle action defined in detail by NCIE-007 and governance documents.",
        "SYNTHESIZED AGENT ≠ AGENT-FACTORY AUTHORITY: Ephemeral Agents do not recursively create new agents by default. If recursive synthesis is ever approved, it requires a separate governed policy.",
    ]),
    ("h2", "24.5 Model-Specific and Collaborative Evaluation (v0.4)"),
    ("p",
     "Before Participatory Mode (Ch.20 §20.7) is enabled in production for a given model/provider, the "
     "Collaborative Evaluation Harness must evaluate:"),
    ("bullets", [
        "Context tracking accuracy across a multi-turn, multi-speaker discussion.",
        "Multi-speaker attribution correctness (Ch.20 §20.6).",
        "Thread separation under concurrent analytical threads (Ch.20 §20.6).",
        "Contradiction-seeking and evidence-gap-identification quality (Ch.20 §20.3).",
        "Restraint — non-dominance under realistic conversational load.",
        "Human-control preservation — the model does not resist or work around a human narrowing or silencing its participation.",
    ]),
    ("p",
     "The Collaborative Quality Monitor continues to track over-participation and under-participation in "
     "production as two distinct, separately alertable failure modes, since they require opposite corrections."),
    ("h2", "24.6 Model Replacement"),
    ("p",
     "Replacing or upgrading a model requires it to reconnect to the governed Collaborative Reasoning State "
     "(Ch.20) and Evidence Service (Ch.23) through the same Model Gateway contract — a new model is never "
     "permitted to become an independent owner of collaborative or platform state."),
    ("h2", "24.7 Data Model"),
    ("bullets", [
        "Model Entry — provider, capability class, data-residency classification, training-use policy, approval status.",
        "Evaluation Result — model, evaluation suite, scores, pass/fail, approver.",
        "Guardrail Event — blocked or flagged request/response, rule triggered, timestamp.",
    ]),
    ("h2", "24.8 Security Controls"),
    ("bullets", [
        "Every external model call is logged with the minimal context actually sent, for audit (Ch.23).",
        "A model/provider not present in the Model Registry with an approved status cannot be reached via the Model Gateway.",
        "Model Registry entries, evaluation results and approvals key off the Assistant's stable internal service identity, not its user-facing presentation name (ARGUS); renaming the presented Assistant does not invalidate or require reissuing prior approvals (Ch.19 §19.11).",
    ]),
    ("h2", "24.9 Failure Modes"),
    ("bullets", [
        "Approved model/provider outage: Model Gateway fails over to a configured alternate approved model where available, or degrades to non-conversational tool access (Ch.19 §19.8, Ch.28).",
        "(v0.5) Agent Factory unavailable: existing eligible Registered Agents, direct governed ARGUS model use and deterministic NCIE remain available; new Dynamic Agent Synthesis returns an explicit synthesis-unavailable state (Ch.28 §28.3).",
        "(v0.5) VPF unavailable: substantive AI output requiring VPF remains UNVALIDATED or VALIDATION_UNAVAILABLE; VPF failure shall not fail open (§24.4A.4; Ch.28 §28.3).",
        "(v0.5) Model, Agent, Tool or VPF Profile Registry unavailable: eligibility is never assumed absent confirmed current Registry state; the platform fails safely or uses an explicitly approved current signed/cached state only where such a policy is already established (Ch.28 §28.3)."],
    ),
    ("h2", "24.10 Non-Functional Requirements"),
    ("bullets", [
        "Guardrail evaluation adds no more than 150ms at p95 to a standard model request (Ch.30)."],
    ),
    ("h2", "24.11 Acceptance Criteria"),
    ("bullets", [
        "A prompt-injection attempt embedded in ingested content is demonstrably treated as inert data, not as an instruction.",
        "A model/provider without a passing Collaborative Evaluation Harness result is demonstrably blocked from Participatory Mode production use.",
        "(v0.5) Architecture-level Dynamic Agent Synthesis and VPF acceptance scenarios are defined in Ch.31 §31.3A, including the mandatory Human-Primary adversarial scenario.",
    ]),
    ("proposed",
     "Confirm internal-vs-external-vs-hybrid model deployment policy and data-residency constraints with NCA "
     "information-security and legal leadership; proposed default is internal/sovereign-hosted models preferred, "
     "with external models permitted only for non-sensitive rooms under the Context Minimizer and explicit "
     "Model Registry approval."),
    ("trace", "NCIE-001 §NCIE Intelligence Assistant; §Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance; NCIE-001 v1.3 §12.80A, §18.241A; NCIE-007 v1.1 Ch.11, Ch.12, Ch.26."),
]
