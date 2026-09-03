"""NCIE-003 content batch: Chapters 23-30 (platform-layer data models)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 23 — Workflow, Automation, RPA & Tasking Data Model
# ---------------------------------------------------------------------------
BLOCKS[23] = [
    ("h2", "23.1 Purpose"),
    ("p", "Defines persistent workflows, approvals, tasks, waiting dependencies and automated "
         "execution state, implementing NCIE-002 Ch.21's Orchestrator, Scheduler and Workflow Engine."),
    ("h2", "23.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "Requested ≠ Approved ≠ Executed ≠ Verified — four distinct states on the same Workflow Instance, never collapsed into a single 'done' flag.",
        "Unknown external outcome requires reconciliation rather than blind retry — if an automated action's outcome cannot be confirmed, the system records Unknown and schedules reconciliation, never silently re-executing an action that may have already succeeded.",
    ]),
    ("h2", "23.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Workflow Instance", "canonical ID, workflow definition reference, originator (human/room/schedule, Ch.21 of this document), current state."],
        ["Workflow State", "governed enumeration: Requested / Approved / Executed / Verified / Failed / Reconciling."],
        ["Task", "workflow instance reference, description, assignee, status — includes Human Tasks (NCIE-002 Ch.21)."],
        ["Approval", "workflow instance reference, approving actor, decision, timestamp — separate from the requesting actor (Ch.26 separation of duties)."],
        ["Waiting Dependency", "workflow instance reference, named wait state (e.g. WAITING_FOR_PM, WAITING_FOR_TRAFFIC), entered/resolved timestamps."],
        ["Automation/RPA Run", "workflow instance reference, provider reference (Ch.6-style provider abstraction), bot identity (Ch.26 machine identity), idempotency key, output artifact reference."],
        ["External Reference", "run reference, external system's own reference/ticket ID for correlation."],
        ["Outcome", "run reference, result (success/failure/unknown), evidence reference if applicable (Ch.17)."],
        ["Reconciliation State", "run reference, reconciliation status, reconciled-by actor/process, timestamp."],
    ],
     "Workflow, Automation, RPA & Tasking principal entities."),
    ("h2", "23.4 State Machine"),
    ("flow",
     [
        "Workflow Instance Requested (human, room-suggested per Ch.21, or scheduled)",
        "Approval recorded by a distinct authorizing actor where required",
        "Automation/RPA Run executed with idempotency key",
        "Outcome recorded (success/failure/unknown)",
        "If Unknown, Reconciliation State entered rather than automatic retry",
        "Workflow Instance reaches Verified only once Outcome is confirmed",
     ],
     "Workflow state machine from request to verified outcome."),
    ("h2", "23.5 Room-Originated Workflows"),
    ("p",
     "A Workflow Instance originated by a Collaborative Room (Ch.21 of this document) retains its "
     "originating Room/Thread reference for provenance, and its Waiting Dependency may be observed "
     "by that Room in Evidence-Watch Participation Mode without granting the Room any execution "
     "authority — the AI-suggested-is-not-execution-authority principle is enforced by requiring a "
     "distinct Approval actor, never by the room-suggestion alone (NCIE-002 Ch.20 §20.11, Ch.21 §21.4)."),
    ("h2", "23.6 Idempotency and Correlation"),
    ("p",
     "Every Automation/RPA Run carries an idempotency key so a duplicated trigger (e.g. a re-delivered "
     "event, Ch.28) cannot cause the same external action to execute twice. External Reference "
     "correlates NCIE's Run with the external system's own ticket/reference for reconciliation."),
    ("h2", "23.7 Failure / Exception Semantics"),
    ("p",
     "A provider outage mid-Run leaves the Workflow Instance in a persisted Waiting Dependency or "
     "Reconciling state that survives a platform restart (NCIE-002 Ch.28) — it is never lost or "
     "silently marked Failed without an attempted reconciliation first."),
    ("trace002", "Directly implements NCIE-002 Ch.21 in full, and depends on Ch.21 of this document (Room-to-Workflow linkage) and Ch.26 (approval separation of duties)."),
    ("review", [
        ("INSTITUTIONAL", "Confirm which workflows are high-consequence and require mandatory Approval before Automation/RPA Run execution."),
        ("INSTITUTIONAL", "Confirm approval matrices per workflow category."),
        ("SOURCE_DISCOVERY", "Confirm which external systems require RPA versus API integration today."),
    ]),
    ("h2", "23.8 Acceptance Criteria"),
    ("bullets", [
        "A Workflow Instance is demonstrably blocked from reaching Executed without a recorded Approval where one is required.",
        "A simulated duplicate trigger is demonstrably prevented from producing a duplicate Automation/RPA Run via the idempotency key.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 24 — Rules, Configuration & Calculation Data Model
# ---------------------------------------------------------------------------
BLOCKS[24] = [
    ("h2", "24.1 Purpose"),
    ("p", "Defines governed rules and configurable parameters used by deterministic NCIE calculations "
         "and thresholds, implementing NCIE-002 Ch.22. This chapter is the single authoritative "
         "definition referenced — not redefined — by Chapters 7, 12, 14 and 18."),
    ("h2", "24.2 Semantic Definition — Mandatory Principle"),
    ("p",
     "Rates and limits belong in versioned Rules, never in UI constants or application code. This "
     "applies without exception to the international incoming traffic surcharge (currently USD 0.19), "
     "the Ghana Card registration limit (currently 10) and the foreign-passport registration limit "
     "(currently 3): each is a Parameter value inside a governed Rule Version, not a literal anywhere "
     "else in the system."),
    ("h2", "24.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Rule", "canonical ID, rule key (e.g. international-surcharge, sim-limit-ghana-card, sim-limit-passport, kpi-threshold-*, rews-alert-rule-*), domain."],
        ["Rule Version", "rule reference, value/Parameter set, effective-from/effective-to (Ch.5), approval state."],
        ["Parameter", "rule version reference, name, value, unit/currency."],
        ["Effective Period", "rule version reference, start date, end date (nullable for open-ended)."],
        ["Approval State", "rule version reference, approving actor, timestamp."],
        ["Calculation Formula Reference", "links a Rule (e.g. KPI or Revenue formula) to the calculation logic version it governs (Ch.33 schema versioning applies to the formula's own contract)."],
        ["Scenario Rule", "a what-if overlay Rule Version, explicitly isolated from production Rule Version history (§24.5)."],
        ["Rule Conflict State", "rule reference, conflicting rule versions detected, resolution status — blocks authoritative output while unresolved."],
    ],
     "Rules, Configuration & Calculation principal entities."),
    ("h2", "24.4 Effective Dating and Historical Binding"),
    ("p",
     "A calculation (Revenue, Ch.12; KPI evaluation, Ch.7; Registration Exception detection, Ch.14; "
     "Alert Rule evaluation, Ch.18) always binds to the Rule Version effective at its own reference "
     "date, and stores that Rule Version reference permanently — a later rule change never "
     "retroactively alters a historical calculation's stored result."),
    ("h2", "24.5 Scenario Isolation"),
    ("p",
     "A Scenario Rule exists only within a Scenario Time context (Ch.5 §5.2) and is never written to, "
     "or read as, production Rule Version history. A what-if Revenue projection using a Scenario Rule "
     "is clearly labelled as a Scenario result and cannot be mistaken for an authoritative Revenue "
     "Calculation (Ch.12)."),
    ("h2", "24.6 Conflict Handling"),
    ("p",
     "Two Rule Versions with overlapping Effective Periods for the same rule key are a Rule Conflict "
     "State: authoritative output for the affected calculation is blocked, not silently resolved by "
     "picking one, until an administrator resolves the conflict (NCIE-002 Ch.22 §22.4)."),
    ("h2", "24.7 Relationships and Cardinality"),
    ("bullets", [
        "One Rule has one-to-many Rule Versions over time, at most one of which is effective at any given non-conflicted point in time.",
        "One Rule Version has one-to-many Parameters (e.g. the SIM-limit rule's Parameter set might include both the numeric limit and its identity-type key).",
    ]),
    ("h2", "24.8 Failure / Exception Semantics"),
    ("p",
     "If the Rule Service is unavailable, dependent Calculation Engines use the last successfully "
     "cached Rule Version with a visible staleness indicator — they never fall back to a hardcoded "
     "default value (NCIE-002 Ch.22 §22.8)."),
    ("trace002", "Directly implements NCIE-002 Ch.22 in full, and is depended upon by Ch.7, Ch.12, Ch.14 and Ch.18 of this document."),
    ("review", [
        ("PROPOSED", "The current supplied values (surcharge USD 0.19; Ghana Card limit 10; Passport limit 3) are proposed as the initial Rule Version values at go-live, per NCIE-002's existing baseline."),
        ("INSTITUTIONAL", "Confirm which values users may modify at what administrative level, and the approval/effective-date process for each rule key."),
        ("INSTITUTIONAL", "Confirm rule-conflict and rollback behaviour expectations beyond the block-on-conflict default in §24.6."),
    ]),
    ("h2", "24.9 Acceptance Criteria"),
    ("bullets", [
        "A rate/limit change is demonstrably effective-dated: calculations before the change date use the prior Rule Version, after use the new one, with both retrievable.",
        "An overlapping-effective-date Rule Conflict State is demonstrably blocked from producing authoritative output.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 25 — Provenance, Lineage & Decision-Time Data Model
# ---------------------------------------------------------------------------
BLOCKS[25] = [
    ("h2", "25.1 Purpose"),
    ("p", "Defines end-to-end source lineage and dependency structures needed for defensible "
         "historical reconstruction, implementing NCIE-002 Ch.23's Provenance Graph and Historical "
         "Snapshot Service, and providing the Correction/Lineage mechanism referenced by Chapters "
         "5, 6, 11, 12 and 14."),
    ("h2", "25.2 Semantic Definition"),
    ("p",
     "Lineage supports both backward tracing (\"what did this fact derive from?\") and forward impact "
     "analysis (\"what depends on this fact, and what breaks if it is corrected?\"). Decision-Time "
     "(Ch.5, Ch.16) must exclude later Evidence by construction, not by query-time filtering alone."),
    ("h2", "25.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Lineage Record", "canonical ID, from-object reference, to-object reference, transformation type, actor (human/AI/bot/service, Ch.20/Ch.26)."],
        ["Transformation Record", "lineage record reference, transformation logic/version reference (Ch.33)."],
        ["Source Reference", "lineage record reference, originating Source Object Reference (Ch.6)."],
        ["Dependency Edge", "object reference, depends-on object reference — supports forward impact analysis."],
        ["Snapshot", "reference date/time, reconstructed state (Ch.5's Historical Snapshot Service data)."],
        ["Decision-Time Context", "decision reference (Ch.16), bounded fact/evidence/rule-version set available at the decision's timestamp."],
        ["Correction Relationship", "corrected object reference, prior version reference, reason, actor, timestamp — the mechanism Chapters 5/11/12/14 each reference."],
        ["Impact-Review State", "dependency edge reference, review status after an upstream correction — flags downstream objects for human review, never silently recalculates them."],
    ],
     "Provenance, Lineage & Decision-Time principal entities."),
    ("h2", "25.4 Forward Impact Analysis on Correction"),
    ("p",
     "When a Correction Relationship is created for an upstream fact (e.g. a Traffic Observation "
     "Revision, Ch.11), the Dependency Edges pointing to it are walked to identify downstream objects "
     "(e.g. a Revenue Calculation, Ch.12) whose Impact-Review State is then set to flagged — those "
     "downstream objects are never silently recalculated without human review, since a silent "
     "recalculation could alter a figure already relied upon in a Decision (Ch.16)."),
    ("h2", "25.5 Decision-Time Construction"),
    ("p",
     "A Decision-Time Context is built at the moment a Decision (Ch.16) is issued, by binding to the "
     "then-current Rule Versions (Ch.24), Evidence (Ch.17) and canonical facts with a knowledge time "
     "at or before the Decision's timestamp — later Evidence is structurally excluded from the bound "
     "set, not merely filtered out at display time, so it cannot leak in through a different query "
     "path."),
    ("h2", "25.6 Agent/VPF Lineage Extension (v0.4 — VPF & Dynamic Agent Synthesis Amendment)"),
    ("p",
     "Authority: approved NCIE-001 v1.3 §12.77-§12.80A; approved NCIE-002 v0.5 Ch.24 §24.4A; approved "
     "NCIE-007 v1.1 Ch.27. Lineage is extended, not replaced, so NCIE can reconstruct the full material "
     "sequence: Human/System Request → ARGUS Interaction → Task Contract → Agent Definition/Registered "
     "Agent → Agent Run → Model Route → Context/Evidence → Tool Invocations → Agent Result → VPF "
     "Validation → ARGUS Presentation → Human Response/Decision (Ch.3 §3.9, Ch.20 §20.7). This "
     "supports both current reconstruction and Decision-Time reconstruction (§25.5) identically — a "
     "Decision-Time query resolves every reference in this chain against the state applicable at the "
     "Decision's cutoff, not today's lifecycle state."),
    ("h2", "25.7 Historical VPF Integrity (v0.4)"),
    ("p",
     "A historical VPF Validation Artifact (Ch.3 §3.9) remains associated with the Profile Version, "
     "Policy Version, Validation Time and Disposition that existed at the time it was produced. Later "
     "revalidation creates a new, related Validation Artifact rather than overwriting the historical "
     "one. REVALIDATION ≠ HISTORICAL REWRITE. Historical Agent Runs, Agent Definitions, Model Routes, "
     "Tool Invocations, VPF Profiles and Engineering Change Candidates may legitimately reference "
     "retired/superseded objects because those objects were active historically — this is never "
     "treated as a data-quality defect (§29, extended); current activation eligibility remains a "
     "separate, current-state question."),
    ("h2", "25.8 Relationships and Cardinality"),
    ("p",
     "One object may have many Lineage Records leading to it (multiple sources/transformations "
     "contributing to one canonical fact) and many Dependency Edges leading from it (many downstream "
     "consumers). A Snapshot references the full set of objects and their state as of its timestamp, "
     "not a partial subset."),
    ("h2", "25.9 Failure / Exception Semantics"),
    ("p",
     "A Lineage Record that cannot be constructed because the originating Source Object Reference was "
     "purged (per an approved retention rule, Ch.31) retains a tombstone reference recording that "
     "purge, rather than leaving a silent gap that looks like a modelling defect. (v0.4) Where "
     "required provenance for a consequential Agent Result or VPF Validation is missing, the deficiency "
     "is represented explicitly rather than fabricated to permit an unqualified PASS."),
    ("trace002", "Directly implements NCIE-002 Ch.23 in full (lineage, decision-time reconstruction, historical snapshots). (v0.4) §25.6-§25.7 additionally implement approved NCIE-001 v1.3 §12.77-§12.80A, approved NCIE-002 v0.5 Ch.24 §24.4A and approved NCIE-007 v1.1 Ch.27."),
    ("review", [
        ("INSTITUTIONAL", "Confirm how much lineage is mandatory by object class (full transformation chain for Revenue and Findings; lighter for high-volume raw telemetry)."),
        ("INSTITUTIONAL", "Confirm archival period for Snapshots, feeding Ch.31/Ch.35."),
        ("INSTITUTIONAL", "Confirm which Decisions require formal Decision-Time Context reconstruction versus a lighter-weight audit trail."),
    ]),
    ("h2", "25.10 Acceptance Criteria"),
    ("bullets", [
        "A correction to an upstream fact demonstrably flags its downstream dependents for review rather than silently recalculating them.",
        "A Decision-Time Context reconstruction demonstrably excludes Evidence with a knowledge time after the Decision's timestamp.",
        "(v0.4) A historical Decision demonstrably reconstructs the AI Artifact, Agent/ARGUS origin, Agent Definition/Run, Model Route, Evidence/Context, VPF Profile Version, VPF Disposition, qualifications and what the human actually saw at Decision Time, without contamination from later revalidation.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 26 — Identity, Authorization & Security Data Model
# ---------------------------------------------------------------------------
BLOCKS[26] = [
    ("h2", "26.1 Purpose"),
    ("p", "Defines workforce/service identities, roles, attributes, permissions, delegated authority "
         "and data classification relationships, implementing NCIE-002 Ch.4 (Identity, Authorization "
         "& Zero-Trust) at the data-model level, and providing the User/Role/Machine Identity "
         "entities referenced throughout this document."),
    ("h2", "26.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "Room membership does not automatically grant Evidence access — a Participant's Room membership (Ch.21) and their domain-level Object-Access Relation to a specific Evidence Object (Ch.17) are separate grants.",
        "Current permission is not historical permission — a permission change is effective-dated (Ch.5), so a past authorization decision remains explicable using the permission state that applied at that time, not today's.",
        "Human, service, workflow and ARGUS actors remain distinguishable in every access/action record — no actor-identity field is ever generic enough to blur these four classes.",
    ]),
    ("h2", "26.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["User", "canonical ID, human identity reference, status."],
        ["Service Identity", "canonical ID, service/workflow/ARGUS machine identity reference, distinct credential lifecycle from Users (NCIE-002 Ch.4 §4.2)."],
        ["Role", "canonical ID, name, bundle of domain/object/field/action grants, versioned."],
        ["Permission", "role reference, domain, object type, field-level scope, action(s) permitted."],
        ["Attribute", "user/service reference, attribute name/value used in contextual authorization (e.g. clearance level)."],
        ["Delegation", "delegating actor, delegate actor, scope, effective period."],
        ["Classification", "See Ch.31 — this chapter references classification tiers rather than redefining them."],
        ["Object-Access Relation", "actor reference, object reference, effective period, granting basis (role/delegation/exception)."],
        ["Authentication / Session Reference", "user/service reference, session token reference, MFA status, issued/expiry time."],
    ],
     "Identity, Authorization & Security principal entities."),
    ("h2", "26.4 Effective-Dated Permissions"),
    ("p",
     "A Permission granted through a Role, and any Delegation, is effective-dated exactly as Chapter "
     "24's Rules are — an audit or Decision-Time reconstruction (Ch.25) queries the Object-Access "
     "Relation as it stood at the relevant historical timestamp, not the current Role definition."),
    ("h2", "26.5 Four Distinguishable Actor Classes"),
    ("table",
     ["Actor Class", "Represented By", "Never Confused With"],
     [
        ["Human", "User entity, authenticated Session Reference.", "Never inherits a Service Identity's credential."],
        ["Service", "Service Identity, scoped machine credential (NCIE-002 Ch.4 §4.2).", "Never assumes a User's session."],
        ["Workflow", "Service Identity scoped to a Workflow Instance (Ch.23).", "Distinguishable from ARGUS even where both act 'on behalf of' the same Workflow."],
        ["ARGUS", "Service Identity per NCIE-002 Ch.19 §19.11's stable internal identity, independent of its display name.", "Never recorded merely as 'system' or merged with generic Service Identity records."],
        ["(v0.4) Agent Runtime Identity", "A distinct runtime identity assigned to each Agent Run (Ch.3 §3.9), referencing the current effective authorization context under which it executes.", "Never inherits the Human Principal's session; never merged with ARGUS's own stable identity even where ARGUS requested the synthesis."],
        ["(v0.4) Tool Actor", "The identity under which a Tool Invocation (Ch.20 §20.3) executes when acting on behalf of an Agent Run.", "Never assumed to be the same as the Agent Runtime Identity that requested it, where the Tool Gateway (NCIE-002 Ch.19 §19.7) assigns its own execution identity."],
    ],
     "The six actor classes every access/action record must distinguish (v0.4 extends the original four)."),
    ("h2", "26.6 Agent Authorization Reference (v0.4)"),
    ("p",
     "An Agent Run (Ch.3 §3.9) may reference the current authorization context under which it "
     "executed. This reference is not itself persisted as though it were a permanent agent authority "
     "— HISTORICAL AUTHORIZATION ≠ CURRENT AUTHORIZATION. Likewise, an Agent Definition's Authorization "
     "Ceiling and a Task Contract's effective-principal reference specify an upper bound and a "
     "run-specific context respectively; neither itself grants authorization (CAPABILITY ENVELOPE ≠ "
     "CURRENT AUTHORIZATION). Authorization references always originate from this chapter's governed "
     "Object-Access Relation/Role/Delegation model, never from Agent Definition or Task Contract text."),
    ("h2", "26.7 Relationships and Cardinality"),
    ("p",
     "A User has one-to-many Roles; a Role has one-to-many Permissions. An Object-Access Relation "
     "references exactly one actor (User or Service Identity) and one object, with its granting basis "
     "recorded so a later audit can tell whether access came from a standing Role or a time-boxed "
     "Delegation."),
    ("h2", "26.8 Failure / Exception Semantics"),
    ("p",
     "A Delegation whose effective period has lapsed is never silently treated as still active; "
     "Object-Access Relation evaluation checks the Delegation's Effective Period at query time "
     "(NCIE-002 Ch.4 §4.4). (v0.4) An Agent Run's current-authorization reference is re-evaluated at "
     "execution time; a revoked or expired authorization is never honoured through cached Agent Run "
     "state."),
    ("trace002", "Directly implements NCIE-002 Ch.4 in full, and is depended upon by every chapter of this document that references role, permission or actor identity. (v0.4) §26.5-§26.6 additionally implement approved NCIE-007 v1.1 Ch.14, Ch.18, Ch.25 §25.3."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm enterprise identity provider (SSO) and existing role model at NCA, to align rather than duplicate."),
        ("INSTITUTIONAL", "Confirm privileged/step-up authentication requirements per role."),
        ("INSTITUTIONAL", "Confirm delegation and emergency-access (break-glass, Ch.36) policies."),
    ]),
    ("h2", "26.9 Acceptance Criteria"),
    ("bullets", [
        "A permission check for a past action demonstrably uses the Role/Delegation state effective at that action's timestamp, not the current state.",
        "Every sampled access/action record across at least three domain chapters demonstrably distinguishes Human, Service, Workflow and ARGUS actor classes.",
        "(v0.4) A sampled Agent Run demonstrably distinguishes its Agent Runtime Identity from the Human Principal, ARGUS and any Tool Actor it invoked, and demonstrably re-evaluates current authorization at execution time rather than relying on a cached or historical grant.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 27 — Audit & Accountability Data Model
# ---------------------------------------------------------------------------
BLOCKS[27] = [
    ("h2", "27.1 Purpose"),
    ("p", "Defines the accountable record of who accessed, changed, approved, executed or revealed "
         "sensitive NCIE information, implementing NCIE-002 Ch.23's Audit Service."),
    ("h2", "27.2 Semantic Definition"),
    ("bullets", [
        "Read, reveal and export actions can be consequential and are audited exactly like writes where they touch protected/sensitive classification (Ch.31).",
        "Unknown outcome is a valid, first-class Audit Event state — an action whose result could not be confirmed is recorded as Unknown, never silently omitted or guessed.",
        "Audit complements but does not replace Provenance (Ch.25) — Audit records who did what and when; Provenance records how a fact was derived.",
    ]),
    ("h2", "27.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Audit Event", "canonical ID, actor reference (Ch.26), target reference, action, timestamp."],
        ["Actor", "reference to User or Service Identity (Ch.26) — always one of the four distinguishable classes."],
        ["Target", "the object acted upon (any canonical entity across this document)."],
        ["Action", "governed enumeration (read/reveal/export/create/modify/approve/execute/delete)."],
        ["Before / After State", "audit event reference, prior value, new value (for modify actions)."],
        ["Reason", "audit event reference, stated justification, required for sensitive-access events (Ch.36 break-glass)."],
        ["Outcome", "audit event reference, result (success/failure/unknown)."],
        ["Correlation ID", "audit event reference, cross-system correlation identifier (Ch.28)."],
        ["Authority Reference", "audit event reference, the Role/Delegation/Approval (Ch.26, Ch.23) under which the action was permitted."],
        ["Sensitive-Access Marker", "audit event reference, flag distinguishing heightened-audit events (protected identity reveal, blocking action, rule change) from routine ones."],
    ],
     "Audit & Accountability principal entities."),
    ("h2", "27.4 Heightened-Audit Events"),
    ("p",
     "Sensitive-Access Marker is set for: Protected Identity Reference reveal (Ch.14), Anti-Fraud "
     "sensitive joins (Ch.15), Blocking Action execution (Ch.15), Rule changes (Ch.24), Decision "
     "issuance (Ch.16), and material collaborative events (participation-mode change, sensitive "
     "evidence introduction, formal promotion, room-originated automation — Ch.21, mirroring NCIE-002 "
     "Ch.23 §23.6's Material Collaboration Audit Events). (v0.4) Also set for material Agent/VPF "
     "lifecycle events (Ch.3 §3.9): Agent Synthesis Requested, Agent Definition Created, Gate A "
     "Completed, Sandbox Evaluated, Ephemeral Agent Activated, Agent Run Completed/Failed, VPF "
     "Validation Completed, Promotion Candidate Created, Agent Registered, Agent Suspended, and "
     "Engineering Change Candidate Created — this list extends the existing Action enumeration (§27.3) "
     "rather than creating a separate Agent-only event architecture."),
    ("h2", "27.4A Telemetry Boundary (v0.4)"),
    ("p",
     "TELEMETRY ≠ AUDIT. Operational telemetry (NCIE-002 Ch.24 §24.9) may reference Agent/VPF objects "
     "for observability purposes; it does not replace the authoritative Audit Event record defined in "
     "this chapter, and it is never mistaken for the audit trail required by §27.4's heightened-audit "
     "events."),
    ("h2", "27.5 Fail-Closed Requirement"),
    ("p",
     "If the Audit Service cannot record an Audit Event for an action requiring one, the action itself "
     "is blocked from completing rather than proceeding unaudited — this is a data-model consequence "
     "of NCIE-002 Ch.23 §23.9's fail-closed principle, requiring the audit write and the action's own "
     "completion to be part of the same transactional boundary where the action is sensitive."),
    ("h2", "27.6 Relationships and Cardinality"),
    ("p",
     "Every Audit Event references exactly one Actor and one Target, and zero-or-one Authority "
     "Reference (some routine reads may not require an explicit authority citation beyond ordinary "
     "role permission)."),
    ("h2", "27.7 Failure / Exception Semantics"),
    ("p",
     "An Audit Event with Outcome Unknown (e.g. the target system's confirmation could not be "
     "retrieved) triggers the same Reconciliation State pattern as Chapter 23's workflow outcomes, "
     "rather than being left permanently ambiguous."),
    ("trace002", "Directly implements NCIE-002 Ch.23 in full (audit service, heightened-audit events, fail-closed principle). (v0.4) §27.4's Agent/VPF event extension and §27.4A additionally implement approved NCIE-007 v1.1 Ch.27, Ch.31 §31.3."),
    ("review", [
        ("LEGAL", "Confirm audit retention period against applicable records/regulatory requirements."),
        ("INSTITUTIONAL", "Confirm which read operations beyond §27.4's list require audit."),
        ("INSTITUTIONAL", "Confirm fail-closed requirements for each high-consequence action category."),
    ]),
    ("h2", "27.8 Acceptance Criteria"),
    ("bullets", [
        "Every action listed in §27.4 demonstrably produces a Sensitive-Access-Marked Audit Event.",
        "A simulated Audit Service failure during a sensitive action demonstrably blocks the action rather than letting it proceed unaudited.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 28 — Notification, Event & Integration Data Model
# ---------------------------------------------------------------------------
BLOCKS[28] = [
    ("h2", "28.1 Purpose"),
    ("p", "Defines internal domain events, event envelopes, subscriptions and notification-delivery "
         "state, implementing NCIE-002 Ch.25's Event Bus."),
    ("h2", "28.2 Semantic Definition"),
    ("bullets", [
        "Sensitive payloads are referenced, not copied, where possible — an event carrying a pointer to a protected Evidence Object (Ch.17) is preferred over one embedding the protected content inline.",
        "Notification delivery is not business acknowledgement — a Notification's Delivery Status reflects whether the message reached its channel, not whether a human acted on it.",
    ]),
    ("h2", "28.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Event Envelope", "canonical ID, event type, schema version (Ch.33), producer reference, correlation ID, published timestamp."],
        ["Event Type", "governed enumeration (source events, PM/KPI events, Alert/Situation events, Workflow events, collaborative events, and — v0.4 — Agent/VPF lifecycle events per Ch.27 §27.4 — per NCIE-002 Ch.25 §25.3)."],
        ["Producer", "service identity reference (Ch.26) that published the event."],
        ["Object Reference", "event envelope reference, referenced canonical object(s), by pointer rather than embedded copy for sensitive objects."],
        ["Correlation ID", "shared identifier linking a chain of related events/requests (Ch.23, Ch.27)."],
        ["Subscription", "subscriber reference, event type filter, delivery channel."],
        ["Notification", "subscription reference, event envelope reference, rendered content."],
        ["Delivery Attempt", "notification reference, attempt number, timestamp, result."],
        ["Delivery Status", "notification reference, current status (pending/delivered/failed) — distinct from business acknowledgement (Ch.18's Acknowledgement entity)."],
    ],
     "Notification, Event & Integration principal entities."),
    ("h2", "28.4 Idempotent Consumption"),
    ("p",
     "Every Event Envelope's Correlation ID and an idempotency key allow a consuming service to detect "
     "and ignore a duplicate delivery, so a re-delivered event never duplicates its downstream effect "
     "(shared mechanism with Ch.23 §23.6)."),
    ("h2", "28.5 Relationships and Cardinality"),
    ("p",
     "One Event Envelope may be delivered to zero-to-many Subscriptions, each producing its own "
     "Notification with its own Delivery Attempts. A failed Delivery Attempt does not lose the "
     "Notification; it is retried per Ch.33's compatibility/retry policy."),
    ("h2", "28.6 Failure / Exception Semantics"),
    ("p",
     "If the Event Bus is degraded, a Producer buffers Event Envelopes locally and retries publication "
     "— no event is silently dropped (NCIE-002 Ch.25 §25.7)."),
    ("trace002", "Directly implements NCIE-002 Ch.25 in full."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm integration/event platform standards already in use, if any, at NCA."),
        ("INSTITUTIONAL", "Confirm external notification channels (email, SMS, dashboard) required at launch."),
        ("LEGAL", "Confirm which event payloads may leave NCIE's boundary (e.g. to an external notification channel) and under what data-handling policy."),
    ]),
    ("h2", "28.7 Acceptance Criteria"),
    ("bullets", [
        "A simulated duplicate event delivery demonstrably does not duplicate downstream effect.",
        "A sensitive Object Reference is demonstrably passed by pointer, not embedded value, in a sampled Event Envelope.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 29 — Data Quality, Validation & Exception Model
# ---------------------------------------------------------------------------
BLOCKS[29] = [
    ("h2", "29.1 Purpose"),
    ("p", "Defines how NCIE represents invalid, incomplete, stale, partial or conflicting data, "
         "consolidating the Chapter 2 vocabulary into a governed, queryable quality-state model."),
    ("h2", "29.2 Semantic Definition"),
    ("bullets", [
        "Missing is not zero or normal — this chapter's entities are the enforcement mechanism for Chapter 2's null/unknown vocabulary across every domain.",
        "Partial coverage remains visible as a first-class state, never rounded up to complete.",
        "Pipeline/source quality (did the data arrive correctly) is separate from substantive sector condition (is the underlying network/traffic/revenue situation actually good or bad) — a Validation Result never silently stands in for a Network Condition (Ch.7) or Condition (Ch.18).",
    ]),
    ("h2", "29.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Validation Result", "See Ch.6 — this chapter extends it with a governed Quality Issue taxonomy."],
        ["Quality Issue", "validation result reference, issue type (schema/completeness/freshness/conflict), severity."],
        ["Completeness State", "scope (source/period/domain), expected-vs-received ratio, status (per NCIE-002 Ch.6 §6.9 Green/Amber/Grey convention)."],
        ["Freshness State", "scope, last-updated time, freshness threshold (Ch.24), status (current/stale)."],
        ["Schema Exception", "source object reference (Ch.6), expected schema version (Ch.33), actual structure, deviation."],
        ["Source Conflict", "two-or-more conflicting Source Object References for the same fact, retained per Ch.5/Ch.17 contradiction-preservation."],
        ["Remediation Task", "quality issue reference, assignee, status."],
        ["Resolution", "remediation task reference, outcome, timestamp."],
    ],
     "Data Quality, Validation & Exception principal entities."),
    ("h2", "29.4 Quality State Does Not Become Substantive State"),
    ("p",
     "A Completeness or Freshness State of Amber/Grey/Stale never itself raises a Network Condition "
     "(Ch.7) or REWS Condition (Ch.18) — those remain governed by substantive domain rules (Ch.24). "
     "The two kinds of state are cross-referenced for operator context (Ch.37) but never merged."),
    ("h2", "29.5 Domain-Specific Freshness Thresholds"),
    ("p",
     "Freshness State's threshold is a Rule Version (Ch.24), scoped per domain — Network PM data may "
     "have a different freshness expectation than Mobile Money aggregates, and each is governed "
     "independently rather than sharing one global staleness constant."),
    ("h2", "29.5A Agent & VPF Data-Quality Rules (v0.4)"),
    ("p", "Extends this chapter's Quality Issue taxonomy to the Agent & VPF entity family (Ch.3 §3.9) with, at minimum:"),
    ("bullets", [
        "An Agent Run must reference a valid Agent Definition or registered capability — a missing reference is a Quality Issue, not a silently accepted gap.",
        "A Task Contract must identify its purpose.",
        "A VPF Validation must reference the exact input artifact it validated.",
        "PASS cannot exist without an applicable VPF Profile/Version reference.",
        "A Promotion Candidate's state cannot equal Registered Agent state (Ch.3 §3.9.2).",
        "An Ephemeral Agent cannot silently become reusable without a recorded Promotion Candidate and governed review.",
        "Historical VPF validation cannot be overwritten by a later revalidation (Ch.25 §25.7).",
        "Invalid lifecycle transitions, missing provenance, or an unresolvable Tool/Model reference on an Agent Run are detectable Quality Issues.",
    ]),
    ("h2", "29.6 Failure / Exception Semantics"),
    ("p",
     "A Schema Exception blocks the affected Source Object Reference from validation (Ch.6) until "
     "resolved; it never silently coerces mismatched data into the expected shape."),
    ("trace002", "Directly implements NCIE-002 Ch.6 §6.9 and Ch.28 (source health, data quality) at the platform-wide data-model level. (v0.4) §29.5A additionally implements approved NCIE-007 v1.1 Ch.32."),
    ("review", [
        ("INSTITUTIONAL", "Confirm domain-specific freshness thresholds per source (Ch.24 Rule Version values)."),
        ("INSTITUTIONAL", "Confirm data-quality ownership (who is accountable for a given source's Remediation Tasks)."),
        ("INSTITUTIONAL", "Confirm which quality failures block downstream processing entirely versus merely flag it."),
    ]),
    ("h2", "29.7 Acceptance Criteria"),
    ("bullets", [
        "A Completeness State of Amber is demonstrably shown alongside, and never in place of, the underlying domain's own substantive status.",
        "A Schema Exception demonstrably blocks validation rather than silently coercing data.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 30 — Metadata Catalogue & Data Dictionary Architecture
# ---------------------------------------------------------------------------
BLOCKS[30] = [
    ("h2", "30.1 Purpose"),
    ("p", "Defines the metadata fields every eventual Data Dictionary entry must contain — the "
         "structural standard that Chapter 39's worked entities populate."),
    ("h2", "30.2 Semantic Definition"),
    ("p",
     "The final Data Dictionary must define both business meaning (what a field means to a regulator "
     "or analyst) and technical representation (its type, constraints and lineage) for every "
     "canonical field. Enumerations require the same governance as Rules (Ch.24) — an enumeration "
     "value cannot be added informally."),
    ("h2", "30.3 Mandatory Dictionary Columns"),
    ("table",
     ["Column", "Definition"],
     [
        ["Business Name", "Human-readable name used in analyst-facing contexts."],
        ["Technical Name", "Canonical field identifier used in schemas/APIs."],
        ["Definition", "Authoritative business meaning, unambiguous enough for regulatory defensibility."],
        ["Entity", "Owning canonical entity (Ch.3 family, specific chapter)."],
        ["Data Type", "Canonical logical data type (not yet a physical column type, Ch.32)."],
        ["Length / Precision", "Where applicable to the logical type."],
        ["Format", "Encoding/format convention (e.g. ISO 8601 for dates)."],
        ["Nullability", "Whether Unknown/absent is permitted, and what it means if so (Ch.2, Ch.29)."],
        ["Default", "Default value if any — must never silently substitute for Unknown (Ch.2)."],
        ["Enumeration", "Governed value set reference, if applicable."],
        ["Owner", "Accountable steward for the field's definition."],
        ["Source", "Canonical NCIE Field vs Source-System Field Mapping distinction (§30.4)."],
        ["Classification", "Tier per Ch.31."],
        ["Validation", "Constraint(s) enforced, referencing Ch.29's Quality Issue taxonomy where relevant."],
        ["Lineage", "Reference into Ch.25's Lineage Record for how the field's value is derived."],
    ],
     "Mandatory Data Dictionary columns (structural standard for Chapter 39)."),
    ("h2", "30.4 Canonical NCIE Field vs Source-System Field Mapping"),
    ("p",
     "These are two distinct dictionary layers. A Canonical NCIE Field is defined by NCIE-001/002/003 "
     "semantics and may be specified before any particular source system's schema is known. A "
     "Source-System Field Mapping records how a specific external system's actual field populates "
     "that canonical field, and is only populated once the source system has actually been inspected "
     "— it is never fabricated to make the dictionary look complete (§30.5)."),
    ("h2", "30.5 Governance of Enumerations"),
    ("p",
     "An enumeration referenced by the Enumeration column is itself a governed reference-data set "
     "(versioned like a Rule, Ch.24); adding, renaming or removing a value requires the same "
     "change-control discipline as Chapter 1's canonical-definition change process. (v0.4) The Agent "
     "& VPF entity family (Ch.3 §3.9) uses these same mandatory columns and enumeration governance; no "
     "separate Agent/VPF dictionary authority is created."),
    ("h2", "30.6 Failure / Exception Semantics"),
    ("p",
     "A dictionary entry lacking a confirmed Source-System Field Mapping is marked SOURCE DISCOVERY "
     "REQUIRED in that column rather than left blank or guessed (implements the mandatory convention "
     "used throughout Chapter 39)."),
    ("trace002", "Provides the metadata structure that operationalises NCIE-002's data-model requirements across every domain chapter of this document."),
    ("review", [
        ("INSTITUTIONAL", "Approve the mandatory dictionary columns in §30.3 as binding for Chapter 39 and any future NCIE-004 implementation-level dictionary."),
        ("INSTITUTIONAL", "Confirm naming/abbreviation conventions for Technical Name beyond Chapter 2's baseline rules."),
        ("INSTITUTIONAL", "Confirm ownership/stewardship metadata conventions (how an Owner is identified and kept current)."),
    ]),
    ("h2", "30.7 Acceptance Criteria"),
    ("bullets", [
        "Every worked entity in Chapter 39 demonstrably populates all §30.3 columns, using SOURCE DISCOVERY REQUIRED where genuinely unknown.",
        "No Chapter 39 entry fabricates a Source-System Field Mapping value.",
    ]),
]
