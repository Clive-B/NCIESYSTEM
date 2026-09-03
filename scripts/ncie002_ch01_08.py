"""NCIE-002 content batch: Chapters 1-8."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 1 — Architecture Mandate, Scope & Design Principles
# ---------------------------------------------------------------------------
BLOCKS[1] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Product Vision, Mission, Principles & Scope, and Product Scope, Functional Boundaries & NCIE Intelligence Domain Architecture."),
    ("h2", "1.1 Architectural Mandate"),
    ("p",
     "NCIE-002 translates the product commitments fixed in NCIE-001 into a buildable system of record. "
     "It is binding on every downstream specification in the suite (NCIE-003 through NCIE-018): where a "
     "later document proposes a technology, pattern or interface that conflicts with a principle in this "
     "chapter, this chapter governs unless a documented architecture change record supersedes it."),
    ("bullets", [
        "NCIE is a unified national intelligence environment, not a federation of independent tools presented behind one shell.",
        "Authority over decisions, findings and enforcement actions is Human-Primary; AI and automation act in advisory, preparatory or executing-under-authorization capacities only.",
        "Every domain adapter and provider integration is replaceable without redesigning the platform (provider neutrality).",
        "Every piece of intelligence exposed to a user is traceable to its originating source, rule version and transformation history (evidence/provenance-first).",
        "Boundaries between raw source data, validated data, canonical intelligence and AI-generated reasoning are explicit and never silently blurred.",
    ]),
    ("h2", "1.2 Scope Model"),
    ("p",
     "NCIE-002 covers the full technical stack required to deliver the NCIE-001 product scope: the "
     "application shell and Situational Awareness workspace; identity and authorization; the canonical "
     "data platform; domain intelligence adapters for Network, Topology/GIS, QoS Campaigns, Incidents, "
     "Traffic, Revenue, Mobile Money, SIM Registration and Anti-Fraud; regulatory case workflow; "
     "cross-domain fusion; alerting; the Intelligence Assistant and collaborative brainstorming; "
     "automation/RPA orchestration; rules and calculation governance; evidence and audit; the AI platform "
     "(ARGUS, Model Gateway, Tool Gateway, Context/Memory Services, Evaluation/Guardrail Services, and — "
     "per the v0.5 amendment — the Agent Factory, Ephemeral Agent Runtime, VPF and Agent/VPF Profile "
     "Registries, Ch.24); integration contracts; security and sovereignty; observability; resilience and "
     "DR; deployment and DevSecOps; non-functional architecture; testing and acceptance; and operations/"
     "Codex handover."),
    ("p",
     "Out of scope for NCIE-002: subscriber-level Mobile Money data (excluded by NCIE-001 product scope), "
     "any capability not stated or reasonably implied by NCIE-001, and organizational/staffing decisions, "
     "which belong to NCIE-018 handover governance rather than technical architecture."),
    ("h2", "1.3 Design Principles"),
    ("h3", "1.3.1 Human-Primary Authority"),
    ("p",
     "Every architectural component that produces a finding, decision, enforcement action or irreversible "
     "state change routes through an explicit human authorization point. AI and RPA components are designed "
     "so that removing model or bot availability degrades convenience, not institutional authority."),
    ("h3", "1.3.2 Provider Neutrality"),
    ("p",
     "Network management systems, RPA providers, AI model providers, mapping providers and messaging "
     "providers are integrated behind capability-abstracting adapter interfaces (see Chapter 6, Chapter 21, "
     "Chapter 24). No chapter of this specification names a specific commercial provider as architecturally "
     "load-bearing; provider selections are configuration, not design."),
    ("h3", "1.3.3 Evidence and Provenance First"),
    ("p",
     "Every canonical fact carries source, acquisition time, validation status and applicable rule version. "
     "This is a platform-level invariant enforced by the Canonical Data Platform (Chapter 5) and the "
     "Evidence, Provenance, Audit & Decision-Time Reconstruction architecture (Chapter 23), not an "
     "optional per-domain feature."),
    ("h3", "1.3.4 Clear Source-to-Decision Boundaries"),
    ("p",
     "Five distinct states are never merged into one: raw acquired data; validated/canonical data; "
     "AI-generated reasoning or hypotheses; human-adopted working analysis; and formally validated "
     "Findings/Decisions. Promotion from one state to the next is an explicit, audited action, never an "
     "implicit side effect of storage or display."),
    ("h3", "1.3.5 Graceful Degradation"),
    ("p",
     "Loss of the AI platform, an RPA provider, the mapping provider, or any single source system degrades "
     "the affected capability only. Core NCIE — authentication, canonical data access, evidence retrieval, "
     "workflow state — remains available. This principle is detailed per-domain in Chapter 28."),
    ("h3", "1.3.6 AI/Agent Governing Invariants (v0.5 — VPF & Dynamic Agent Synthesis)"),
    ("p",
     "Dynamic Agent Synthesis and the VPF validation architecture (Ch.24 §24.4A) extend the AI platform "
     "recognized in §1.2; they do not replace the Model Gateway, Tool Gateway, current-authorization or "
     "Human-Primary controls already fixed above. The following invariants bind every chapter that "
     "touches AI orchestration (principally Ch.19, Ch.20, Ch.24, Ch.28, Ch.31, Ch.32) and are stated once "
     "here rather than re-derived per chapter:"),
    ("bullets", [
        "AGENT CREATION ≠ AUTHORITY CREATION.",
        "AGENT SYNTHESIS ≠ PERMISSION EXPANSION.",
        "EPHEMERAL AGENT ≠ REGISTERED REUSABLE AGENT.",
        "AGENT SYNTHESIS ≠ SELF-REGISTRATION.",
        "SYNTHESIZED AGENT ≠ AGENT-FACTORY AUTHORITY.",
        "VPF VALIDATION ≠ HUMAN / INSTITUTIONAL APPROVAL.",
        "UNVALIDATED SUBSTANTIVE AI OUTPUT ≠ VALIDATED NCIE AI RESULT.",
    ]),
    ("h2", "1.4 Non-Functional Drivers"),
    ("table",
     ["Driver", "Architectural Consequence"],
     [
         ["Auditability", "Every write to canonical state carries actor identity (human/AI/bot/service), timestamp and source reference (Ch.23)."],
         ["Multi-tenancy of trust", "Aggregate views and individual/protected views are architecturally distinct data paths, not a display-layer filter (Ch.4, Ch.14)."],
         ["National-scale data volume", "Canonical stores and analytical layers are horizontally scalable and partitioned by operator/geography/time (Ch.5, Ch.30)."],
         ["Operational resilience", "No single external dependency (AI, RPA, map, one source) is a hard availability dependency for core NCIE (Ch.28)."],
         ["Regulatory defensibility", "Decision-time reconstruction must be possible without relying on live external services (Ch.23)."],
     ],
     "Non-functional drivers and their binding architectural consequences."),
    ("h2", "1.5 Architecture Overview"),
    ("flow",
     [
        "Source Systems & Providers (NMS, Billing, Traffic, Mobile Money, SIM Registration, Anti-Fraud, Email, Maps, Regulatory)",
        "Acquisition & Ingestion Layer (Source Registry, API/File/RPA adapters, Ingestion Gateway)",
        "Canonical Data Platform (raw / validated / canonical / analytical layers, entity registry, rules)",
        "Domain Intelligence Services (Network, Topology, Traffic, Revenue, Mobile Money, SIM, Anti-Fraud, Regulatory)",
        "Fusion, Evidence & Alerting (Cross-Domain Fusion, Evidence/Provenance, REWS/Situations)",
        "Experience Layer (Situational Awareness Workspace, Intelligence Assistant, Collaborative Rooms)",
        "Human Authority (Analysts, Investigators, Regulators, Executives, Auditors)",
     ],
     "NCIE end-to-end architectural layering, source to human authority."),
    ("h2", "1.6 Security, Privacy, Sovereignty & Resilience Posture"),
    ("p",
     "This chapter states posture only; controls are specified in Chapter 4 (identity/authorization), "
     "Chapter 26 (security/privacy/sovereignty), Chapter 28 (resilience/DR) and Chapter 31 "
     "(testing/acceptance). Architecturally, NCIE is designed as a sovereign, on-premises-capable "
     "national intelligence system: no chapter of this specification requires data to leave Ghanaian "
     "jurisdiction as a precondition of core operation."),
    ("proposed",
     "Default hosting posture is government/NCA-controlled data centre or sovereign cloud within Ghana, "
     "with any external AI processing subject to the data-minimisation and residency controls in Chapter 24 "
     "and Chapter 26. Confirm the specific hosting facility and sovereign-cloud provider (if any) with NCA IT "
     "leadership; this does not change the architecture, only its deployment target (Ch.29)."),
    ("h2", "1.7 Requirements Traceability Approach"),
    ("p",
     "NCIE-001 requirements are identified by chapter.paragraph number (e.g. §18.241), which is the stable "
     "requirement ID used throughout the suite. Each NCIE-002 chapter closes with a Traceability note "
     "mapping its principal components back to the NCIE-001 chapters that mandate them. A consolidated "
     "Requirements Traceability Matrix is produced in Chapter 31."),
    ("trace", "NCIE-001 §Product Vision, Mission, Principles & Scope; §Product Scope, Functional Boundaries & NCIE Intelligence Domain Architecture; NCIE-001 v1.3 §12.77-§12.80A, §18.241A; NCIE-007 v1.1 front matter §0.3."),
]

# ---------------------------------------------------------------------------
# Chapter 2 — System Context, Actors, Trust Boundaries & External Systems
# ---------------------------------------------------------------------------
BLOCKS[2] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Product Scope & Functional Boundaries; Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance."),
    ("h2", "2.1 Actor Catalogue"),
    ("table",
     ["Actor Class", "Representative Roles", "Trust Characteristics"],
     [
        ["Executive", "Director-General, Deputy Directors, Divisional Heads", "Broad read access to aggregate and Situational Awareness views; no direct data-entry authority."],
        ["Analyst", "Network, Revenue, Fraud, Regulatory analysts", "Domain-scoped read/write on working analysis; cannot validate own Findings."],
        ["Engineer", "NMS/topology engineers, platform engineers", "Elevated access to technical/operational data; no regulatory decision authority."],
        ["Regulator / Case Officer", "Regulatory Intelligence, compliance officers", "Case and Finding/Decision workflow authority within assigned domains and separation-of-duties limits."],
        ["Investigator", "Anti-Fraud/SIMBOX investigators", "Access to sensitive joins and protected-identity resolution under heightened audit (Ch.14, Ch.15, Ch.26)."],
        ["Administrator", "Platform, identity, rule administrators", "Configuration and user/rule administration authority; no analytical decision authority by virtue of the admin role alone."],
        ["Auditor", "Internal/external audit, oversight bodies", "Read-only access to evidence, provenance and audit trails; no operational write access."],
        ["Machine Identity", "RPA bots, scheduled jobs, service accounts, the AI Gateway", "Distinct identity class from humans; scoped, time-bounded credentials; never inherits a human's session (Ch.4)."],
     ],
     "NCIE actor classes and their trust characteristics."),
    ("h2", "2.2 External System Catalogue"),
    ("table",
     ["External System", "Direction", "Nature of Exchange"],
     [
        ["Operator NMS/PM platforms", "Inbound", "Performance-monitoring files/exports per operator, per NCIE-001 NMS/PM requirements."],
        ["Billing systems", "Inbound", "Reported Revenue/Billing figures for verification against calculated Revenue."],
        ["Traffic data sources", "Inbound", "International, Off-Net and On-Net traffic volumes by operator/period."],
        ["Mobile Money aggregate feeds", "Inbound", "Daily aggregate sent/received figures by operator; no subscriber-level data."],
        ["SIM Registration sources", "Inbound", "Registration counts and identity-document class distributions."],
        ["Anti-Fraud/SIMBOX detection feeds", "Inbound", "Detection and suspicion signals feeding investigation workflow."],
        ["Operator incident mailboxes", "Inbound", "Outage/fibre-cut/restoration notifications, structured by the Incident Intelligence adapter."],
        ["Mapping/GIS provider", "Bidirectional", "Base map tiles and geocoding context; NCIE remains the authority for topology and cell placement."],
        ["Regulatory Intelligence platform", "Bidirectional", "Existing case/finding workflow reused rather than rebuilt (Ch.16)."],
        ["RPA providers (UiPath, Power Automate, Automation Anywhere, future)", "Bidirectional", "Automated acquisition/execution behind the Capability Registry (Ch.21)."],
        ["AI model providers (internal/external)", "Bidirectional", "Conversational and reasoning support behind the Model Gateway (Ch.24); never a system of record."],
    ],
     "External systems and the nature of their exchange with NCIE."),
    ("h2", "2.3 Trust Boundaries"),
    ("p",
     "Five trust boundaries recur throughout this specification and are referenced by number in later "
     "chapters:"),
    ("bullets", [
        "TB-1 — Public/operator network to NCIE ingestion edge (Source Registry, Ingestion Gateway).",
        "TB-2 — Ingestion edge to raw store (unauthenticated file/API content is never trusted as canonical until validated).",
        "TB-3 — Human/AI/bot identity boundary at the authorization layer (Ch.4); AI and bots never inherit human session privilege.",
        "TB-4 — Aggregate-view boundary vs protected-identity boundary (Ch.4, Ch.14); aggregate access does not imply individual-record access.",
        "TB-5 — NCIE platform boundary to external AI/RPA providers; data crossing this boundary is minimised and governed (Ch.24, Ch.26).",
    ]),
    ("h2", "2.4 System Context Diagram"),
    ("rel",
     [
        ("Operators (NMS/Billing/Traffic/MoMo/SIM/Fraud)", "sends data across TB-1 to", "Source Registry / Ingestion Gateway"),
        ("Operator Incident Mailboxes", "feeds across TB-1 to", "Incident Intelligence Adapter"),
        ("Mapping/GIS Provider", "supplies base layers across TB-5 to", "Topology & Spatial Service"),
        ("RPA Providers", "execute Runs across TB-5 for", "Automation Orchestrator"),
        ("AI Model Providers", "serve requests across TB-5 to", "Model Gateway"),
        ("Human Actors", "authenticate across TB-3 into", "Identity & Authorization Service"),
        ("Regulatory Intelligence Platform", "exchanges cases/findings across TB-5 with", "Regulatory Case Service"),
     ],
     "Primary NCIE system-context relationships and the trust boundaries they cross."),
    ("h2", "2.5 Interfaces"),
    ("p",
     "Inbound interfaces to source systems are governed by the Source Registry (Ch.6). Outbound "
     "interfaces to humans are governed by the Situational Awareness Workspace (Ch.3) and the Intelligence "
     "Assistant (Ch.19). All inter-service interfaces internal to NCIE are governed API/event contracts "
     "(Ch.25)."),
    ("h2", "2.6 Security Controls"),
    ("bullets", [
        "Every external system is registered in the Source Registry or Capability Registry with a named owner before it can write to NCIE.",
        "No external system is granted write access to canonical or analytical stores directly; all writes pass through validation (Ch.5, Ch.6).",
        "Machine identities crossing TB-5 use short-lived, scoped credentials distinct from any human's identity (Ch.4).",
    ]),
    ("h2", "2.7 Failure Modes"),
    ("bullets", [
        "Unreachable or malformed source feed: ingestion marks source health degraded (Ch.6, Ch.27); downstream views show missing rather than zero.",
        "Compromised or decommissioned external system credential: revoked at the Capability Registry/Identity Service without requiring a platform redeploy.",
    ]),
    ("h2", "2.8 Acceptance Criteria"),
    ("bullets", [
        "Every actor class in §2.1 maps to at least one authorization role tested in Chapter 31.",
        "Every external system in §2.2 has a registered owner, expected frequency and health status visible in the Observability platform (Ch.27).",
    ]),
    ("proposed",
     "The specific list of NCA organisational units mapped to each actor class (§2.1) should be confirmed by "
     "NCA HR/organisational leadership; the actor classes themselves are fixed by NCIE-001 and do not change."),
    ("trace", "NCIE-001 §Product Scope, Functional Boundaries & NCIE Intelligence Domain Architecture; §Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 3 — Full-Screen UX & Situational Awareness Workspace
# ---------------------------------------------------------------------------
BLOCKS[3] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 NCIE Command Center; Situational Awareness, Early Warning, Alerting & National Communications Operating Picture."),
    ("h2", "3.1 Experience Principles"),
    ("bullets", [
        "The workspace is full-screen by default; the operator should never need to leave NCIE to check a second system for authoritative state.",
        "Map, ARGUS (the NCIE Intelligence Assistant), alerts, evidence and domain panels share one operator/geography/time context — changing context in one panel updates the others.",
        "Views are role-aware: an Executive's default composition differs from an Analyst's or Investigator's, but the underlying data contract is identical.",
        "Status is always visible in plain language: known, missing, stale, waiting, or contradictory — never a bare blank space.",
    ]),
    ("h2", "3.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Application Shell", "Hosts panel composition, global navigation, session and context state; framework-agnostic contract with domain modules."],
        ["Workspace Manager", "Persists and restores per-user/per-role panel layouts; enforces which panels a role may add."],
        ["Dashboard Composition Service", "Assembles the National Operating Picture from REWS/Situation, domain health and KPI summaries (Ch.18)."],
        ["Map Context Bridge", "Synchronises map viewport/selection with ARGUS's conversational context and open panels (Ch.8, Ch.19)."],
        ["Panel Registry", "Declares available panels (Network, Topology, Traffic, Revenue, MoMo, SIM, Anti-Fraud, Regulatory, Evidence, Alerts) and their required permissions."],
     ],
     "Situational Awareness Workspace principal components."),
    ("h2", "3.3 Context Propagation Flow"),
    ("flow",
     [
        "Operator selects geography/operator/date in any panel",
        "Workspace Manager publishes context change",
        "Map Context Bridge updates map viewport and selection",
        "Assistant Context Resolver updates conversational grounding (Ch.19)",
        "Subscribed domain panels re-query canonical/analytical data for new context",
        "National Operating Picture status badges refresh",
     ],
     "Cross-panel context propagation in the Situational Awareness Workspace."),
    ("h2", "3.4 Data Model"),
    ("bullets", [
        "Workspace Layout — user/role, panel set, positions, saved filters.",
        "Context State — active operator(s), geography, date/time range, selected entity references (transient, not persisted as evidence).",
        "Panel Contract — panel id, required permission, supported context dimensions, data source binding.",
    ]),
    ("h2", "3.5 Security Controls"),
    ("bullets", [
        "Panel visibility is authorization-filtered server-side, not merely hidden client-side (Ch.4).",
        "Context state never carries protected-identity fields (Ch.14) into panels the active user is not authorized to view.",
    ]),
    ("h2", "3.6 Failure Modes"),
    ("bullets", [
        "Map provider unavailable: workspace falls back to a non-map, list/table-based geography selector; all non-map panels remain fully functional (Ch.28).",
        "One domain panel's data source is degraded: only that panel shows a degraded-status badge; other panels are unaffected.",
    ]),
    ("h2", "3.7 Non-Functional Requirements"),
    ("bullets", [
        "Initial workspace load renders the shell and cached last-known status within 2 seconds on the reference network profile (Ch.30 defines the profile).",
        "Context propagation across panels completes within 500ms of a context change under normal load.",
    ]),
    ("h2", "3.8 Acceptance Criteria"),
    ("bullets", [
        "For each role class in Ch.2, a default panel composition exists and is demonstrably restricted to authorized panels only.",
        "Changing operator/geography/date in any one panel is shown to update all subscribed panels within the NFR target.",
    ]),
    ("h2", "3.9 ARGUS Presentation"),
    ("p",
     "ARGUS — the user-facing name for the NCIE Intelligence Assistant (Ch.19 §19.11) — is presented "
     "within the workspace, not as a separate application. Supported presentation states are:"),
    ("bullets", [
        "Docked — a persistent side panel alongside other workspace panels.",
        "Expanded — a larger conversational/collaborative pane while other panels remain visible.",
        "Full-Screen — ARGUS occupies the primary workspace area.",
        "Present inside Collaborative Rooms — participating per its current Participation Mode (Ch.20 §20.7).",
    ]),
    ("h2", "3.10 UX Doctrine"),
    ("flow",
     [
        "See the national situation",
        "Understand what is current, stale, missing or conflicting",
        "Select the operator / geography / object",
        "Drill into evidence",
        "Ask ARGUS",
        "Brainstorm with humans + ARGUS",
        "Identify hypotheses / contradictions / evidence gaps",
        "Launch or monitor governed evidence acquisition",
        "Receive new validated intelligence",
        "Update the map / situation / reasoning",
        "Move into human-governed action where required",
     ],
     "The governing NCIE UX doctrine loop, from national situational awareness to human-governed action."),
    ("p",
     "Colour never substitutes for meaning; frontend state never substitutes for authoritative state; an "
     "ARGUS suggestion never displays as a completed action; and a hypothesis never displays as a Finding."),
    ("proposed",
     "Default panel compositions for Executive, Analyst, Engineer, Regulator/Case Officer, Investigator, "
     "Administrator and Auditor roles are proposed in NCIE-012 (UX/UI & Design System Specification); confirm "
     "final layouts with representative users from each role before production rollout."),
    ("proposed",
     "Default ARGUS presentation state (§3.9) is proposed as Docked for ordinary workspace use, Expanded "
     "when a collaborative room becomes the active panel, and Full-Screen only on explicit user action; "
     "confirm with representative users before production rollout."),
    ("trace", "NCIE-001 §NCIE Command Center; §Situational Awareness, Early Warning, Alerting & National Communications Operating Picture."),
]

# ---------------------------------------------------------------------------
# Chapter 4 — Identity, Authorization & Zero-Trust
# ---------------------------------------------------------------------------
BLOCKS[4] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance."),
    ("h2", "4.1 Principles"),
    ("bullets", [
        "Zero-trust: no request is implicitly trusted by network location; every request is authenticated and authorized at the service boundary.",
        "RBAC is the baseline, extended with contextual domain/object/field/action controls where NCIE-001 requires finer granularity than role alone provides (e.g. protected identity fields).",
        "Aggregate access never implies individual access; a role permitted to see aggregate MoMo volumes is not thereby permitted to see any subscriber-level data (which is out of scope entirely, Ch.13).",
        "Collaborative rooms (Ch.20) never pool participant permissions; a room's shared context is filtered per-viewer by that viewer's own authorization.",
        "Human, AI and machine identities are architecturally distinct identity classes; an AI or bot identity never silently assumes a human's session.",
    ]),
    ("h2", "4.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Identity Service", "Authenticates humans (SSO/MFA-ready) and issues session tokens; manages machine-identity credentials separately."],
        ["Authorization Service", "Evaluates RBAC plus contextual domain/object/field/action policy for every request; single source of authorization truth."],
        ["Session Manager", "Issues, refreshes and revokes sessions; enforces idle/absolute timeout policy."],
        ["Machine Identity Registry", "Issues scoped, time-bounded credentials to RPA bots, scheduled jobs and the AI Gateway; distinct from human accounts."],
        ["Policy Administration Point", "Where administrators define/version roles, field-level rules and separation-of-duties constraints (Ch.32)."],
     ],
     "Identity, Authorization & Zero-Trust principal components."),
    ("h2", "4.3 Authorization Model"),
    ("p",
     "Authorization decisions combine four layers, evaluated in order: (1) role-based domain access, (2) "
     "object-level access (e.g. a specific case or room), (3) field-level access (e.g. protected identifiers "
     "in Ch.14), (4) action-level access (e.g. may-validate-Finding vs may-propose-Finding). A request is "
     "denied if any layer denies it; layers do not override one another upward."),
    ("rel",
     [
        ("Human Actor", "authenticates via", "Identity Service"),
        ("Identity Service", "issues session to", "Session Manager"),
        ("Authorization Service", "evaluates request against", "Policy Administration Point rules"),
        ("Machine Identity Registry", "issues scoped credential to", "RPA Bot / AI Gateway / Scheduled Job"),
     ],
     "Identity and authorization relationships."),
    ("h2", "4.4 Data Model"),
    ("bullets", [
        "Identity — human/machine, credential reference, MFA status, lifecycle status.",
        "Role — named bundle of domain/object/field/action grants, versioned.",
        "Policy Grant — role-to-permission mapping, effective-dated (aligns with Ch.22 temporal governance).",
        "Session — identity reference, issued/expiry time, device/context metadata, revocation status.",
    ]),
    ("h2", "4.5 Security Controls"),
    ("bullets", [
        "SSO/MFA-ready integration; MFA is mandatory for Administrator, Investigator and regulatory validation actions.",
        "Separation of duties: the role that proposes a Finding cannot also validate the same Finding (Ch.16).",
        "Break-glass access (Ch.26) is logged, time-bounded and requires post-hoc justification.",
        "All authorization decisions — permit and deny — are logged for audit (Ch.23).",
        "Authorization and audit for the NCIE Intelligence Assistant bind to its stable internal service identity, independent of its user-facing presentation name (ARGUS); a future institutional rename does not require reissuing authorization policy or audit history (Ch.19 §19.11).",
    ]),
    ("h2", "4.6 Failure Modes"),
    ("bullets", [
        "Identity Service degraded: existing valid sessions continue to function per policy; new sign-ins queue or fail closed, never fail open.",
        "Policy Administration Point unreachable: Authorization Service uses last-known-good cached policy with a visible staleness indicator; it does not default to permissive.",
    ]),
    ("h2", "4.7 Non-Functional Requirements"),
    ("bullets", [
        "Authorization decisions complete within 100ms at p95 under normal load (Ch.30).",
        "Session revocation propagates to all active service boundaries within 30 seconds.",
    ]),
    ("h2", "4.8 Acceptance Criteria"),
    ("bullets", [
        "Attempting an action denied by any one of the four authorization layers is demonstrably blocked, with an audit entry recorded.",
        "A room with mixed-permission participants is shown to filter shared context per-viewer, not per-room (Ch.20).",
    ]),
    ("proposed",
     "Default session timeouts: 30 minutes idle / 12 hours absolute for standard roles; 15 minutes idle / 8 "
     "hours absolute for Investigator and Administrator roles. Confirm against NCA information-security policy "
     "before production."),
    ("proposed",
     "Default MFA method: authenticator-app TOTP as baseline, with SMS fallback disabled by default given SIM-based "
     "fraud relevance to NCIE's own domain. Confirm with NCA IT security."),
    ("trace", "NCIE-001 §Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 5 — Canonical Data Platform, Domain Model & Metadata
# ---------------------------------------------------------------------------
BLOCKS[5] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Data, Intelligence Domain, Canonical Model & Information Governance."),
    ("h2", "5.1 Layered Data Architecture"),
    ("bullets", [
        "Raw layer — unmodified acquired content (files, API payloads, email bodies, screenshots), immutable once stored.",
        "Validated layer — raw content checked against source-registry expectations (operator/date/scope correctness); rejected content is flagged, not silently dropped.",
        "Canonical layer — the single authoritative representation of each entity (operator, geography, cell, SIM, identity, incident, case, evidence), reconciled across sources.",
        "Analytical layer — derived aggregates, KPIs and fusion outputs optimised for query, always traceable back to canonical sources.",
    ]),
    ("h2", "5.2 Canonical Entities"),
    ("table",
     ["Entity", "Description", "Owning Domain Chapter"],
     [
        ["Operator", "Licensed telecom operator; stable identifier used across all domains.", "Ch.6"],
        ["Geography", "National/regional/district/place hierarchy with versioned boundaries.", "Ch.8"],
        ["Cell", "Network cell/site, versioned by topology change.", "Ch.7, Ch.8"],
        ["SIM / Identity", "Protected SIM and identity-document reference (Ch.14); never exposed in aggregate views.", "Ch.14"],
        ["Incident", "Outage/fibre-cut/restoration event with lineage to source email/NMS evidence.", "Ch.10"],
        ["Case", "Regulatory workflow container linking exceptions, findings and decisions.", "Ch.16"],
        ["Evidence", "Any authoritative artifact (file, calculation, screenshot, extraction) with provenance.", "Ch.23"],
     ],
     "Canonical entity registry (summary; full data dictionary in NCIE-004/NCIE-014)."),
    ("h2", "5.3 Metadata & Temporal Model"),
    ("bullets", [
        "Every canonical record distinguishes event time (when the fact occurred), acquisition time (when NCIE received it) and knowledge time (when NCIE considered it known) — late-arriving data preserves its true knowledge time rather than back-dating silently.",
        "Corrections are versioned, never overwritten in place; the prior version remains queryable for decision-time reconstruction (Ch.23).",
        "Missing data is represented as an explicit missing state, distinct from a zero value, across every domain adapter.",
    ]),
    ("h2", "5.4 Data Flow"),
    ("flow",
     [
        "Raw Store (immutable acquired content)",
        "Validation Pipeline (source/scope/date checks)",
        "Canonical Store (reconciled entities, versioned)",
        "Analytical Layer (aggregates, KPIs, fusion inputs)",
        "Domain Services & Situational Awareness Workspace",
     ],
     "Raw-to-analytical data flow through the Canonical Data Platform."),
    ("h2", "5.5 Metadata Catalogue"),
    ("p",
     "A metadata catalogue records, for every canonical field: source(s) of truth, permitted transformations, "
     "classification (public/internal/protected/sensitive), and owning domain chapter. The catalogue is the "
     "input to both the Authorization Service field-level rules (Ch.4) and the Data Protection controls (Ch.26)."),
    ("h2", "5.6 Security Controls"),
    ("bullets", [
        "Protected and sensitive fields (Ch.14, Ch.15) are tagged in the metadata catalogue and enforced at query time, not only at display time.",
        "Raw layer retains original content for chain-of-custody purposes even after canonicalisation (Ch.23).",
    ]),
    ("h2", "5.7 Failure Modes"),
    ("bullets", [
        "Validation pipeline rejects a batch: the batch is quarantined with a reason; canonical state is unaffected until corrected and re-validated.",
        "Conflicting canonical values from two sources: both are retained with provenance; the platform does not silently pick one without a resolution rule (Ch.17, Ch.22).",
    ]),
    ("h2", "5.8 Non-Functional Requirements"),
    ("bullets", [
        "Canonical store scales horizontally by operator/geography/time partition to national data volumes (Ch.30 sets specific targets).",
        "Analytical layer refresh lag from canonical write is bounded and visible per domain (Ch.27).",
    ]),
    ("h2", "5.9 Acceptance Criteria"),
    ("bullets", [
        "For each canonical entity in §5.2, a versioned change is demonstrably retrievable at a prior point in time.",
        "A deliberately malformed source batch is demonstrably quarantined rather than corrupting canonical state.",
    ]),
    ("trace", "NCIE-001 §Data, Intelligence Domain, Canonical Model & Information Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 6 — Source Registry, Acquisition & Ingestion
# ---------------------------------------------------------------------------
BLOCKS[6] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Data Acquisition, Integration, Source Intelligence & Ingestion Governance."),
    ("h2", "6.1 Source vs Provider"),
    ("p",
     "A Source is the institutional origin of data (e.g. \"Operator X monthly PM export\"); a Provider is the "
     "technical channel used to acquire it (API, file drop, email, screenshot, manual entry, RPA-driven portal "
     "access). The Source Registry tracks both independently so a provider can change (e.g. manual to RPA) "
     "without altering the source's identity or history."),
    ("h2", "6.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Source Registry", "Catalogue of every source: owner, expected frequency, format, provider(s), API-vs-RPA access mode."],
        ["Ingestion Gateway", "Single technical entry point for API, file, email and RPA-submitted content."],
        ["Raw Store", "Immutable storage of acquired content pre-validation."],
        ["Validation Pipeline", "Checks operator/date/scope correctness; produces Request/Run/artifact/validation lineage."],
        ["Source Health Monitor", "Tracks freshness, last successful acquisition and error state per source (feeds Ch.27)."],
     ],
     "Source Registry, Acquisition & Ingestion principal components."),
    ("h2", "6.3 Acquisition Lineage"),
    ("p",
     "Every acquisition is modelled as a Request (what was asked for), a Run (an attempt to fulfil it), an "
     "Artifact (what was actually received), and a Validation outcome. This lineage is preserved even when "
     "acquisition fails, so a missing PM file is visible as a failed Run rather than silent absence."),
    ("rel",
     [
        ("Request", "produces", "Run"),
        ("Run", "yields", "Artifact"),
        ("Artifact", "passes through", "Validation Pipeline"),
        ("Validation Pipeline", "writes to", "Canonical Store"),
     ],
     "Request/Run/Artifact/Validation acquisition lineage."),
    ("h2", "6.4 Validation Rules"),
    ("bullets", [
        "Wrong operator, wrong date range or out-of-scope content is rejected at validation, not silently accepted and miscategorised.",
        "Missing data remains missing — validation never substitutes a zero or default value for an absent measurement.",
        "Late-arriving data is accepted and back-referenced to its true event time while preserving true knowledge time (Ch.5).",
    ]),
    ("h2", "6.5 Provider Channels Supported"),
    ("bullets", [
        "API — direct programmatic acquisition, preferred where available.",
        "File — scheduled or manual file drop (e.g. NMS/PM exports).",
        "Email — structured extraction from operator incident mailboxes (Ch.10).",
        "Screenshot — image capture with OCR/manual transcription support and explicit provenance flag.",
        "Manual entry — human-entered data, flagged distinctly from system-acquired data.",
        "RPA — provider-neutral robotic acquisition via the Automation Orchestrator (Ch.21) for portals without an API.",
    ]),
    ("h2", "6.6 Security Controls"),
    ("bullets", [
        "Every source has a named accountable owner in the registry before it is enabled.",
        "Ingestion Gateway authenticates and rate-limits every channel; unregistered sources are rejected.",
    ]),
    ("h2", "6.7 Failure Modes"),
    ("bullets", [
        "Source unreachable: Source Health Monitor marks it degraded; consumers see explicit staleness, not silent gaps (Ch.27).",
        "Malformed artifact: quarantined with a reason, visible to the source owner for correction.",
    ]),
    ("h2", "6.8 Non-Functional Requirements"),
    ("bullets", [
        "Validation pipeline processes standard daily source volumes within the freight window required by downstream KPI/REWS timing (Ch.7, Ch.18).",
    ]),
    ("h2", "6.9 Acceptance Criteria"),
    ("bullets", [
        "Every source in the registry has owner, frequency and provider-channel populated and visible in Observability (Ch.27).",
        "A deliberately wrong-operator file is demonstrably rejected with a clear reason rather than miscategorised.",
    ]),
    ("proposed",
     "Default source health thresholds mirror the NMS/PM convention already fixed in NCIE-001 Chapter 7: "
     "Green 66-100% expected files received, Amber under 66%, Grey no files received, applied uniformly across "
     "all source types unless a domain chapter states otherwise."),
    ("trace", "NCIE-001 §Data Acquisition, Integration, Source Intelligence & Ingestion Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 7 — Network Intelligence, NMS, PM & KPI
# ---------------------------------------------------------------------------
BLOCKS[7] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Product Capability Architecture; Data, Intelligence Domain, Canonical Model & Information Governance."),
    ("h2", "7.1 Scope"),
    ("p",
     "Covers acquisition and analysis of Performance Monitoring (PM) data from national to cell level, KPI "
     "computation, threshold-based health status, and district-to-cell investigation triggered by degradation."),
    ("h2", "7.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["NMS Adapters", "Provider-neutral ingestion of operator PM exports (Ch.6 channels)."],
        ["PM Service", "Normalises PM records to canonical cell/KPI/date structure."],
        ["KPI Engine", "Computes KPIs against explicit definitions and thresholds; versioned KPI definitions."],
        ["Investigation Service", "Escalates district-level degradation into cell-level investigation workflow."],
    ],
     "Network Intelligence principal components."),
    ("h2", "7.3 KPI Health Status Model"),
    ("p",
     "Each geography/cell/date/KPI combination carries an explicit health status derived from expected-vs-received "
     "file coverage: Green (66-100% of expected files received), Amber (under 66%), Grey (no files received). "
     "This status is distinct from the KPI value itself — a cell can have a good KPI value with Amber coverage, "
     "and both are shown."),
    ("h2", "7.4 District-to-Cell Investigation Flow"),
    ("flow",
     [
        "Daily district KPI extraction",
        "Degradation detected against threshold",
        "Topology resolution (district to constituent cells, Ch.8)",
        "Cell-level PM retrieval and KPI recomputation",
        "Investigation Service opens investigation record with evidence links",
        "Analyst review and escalation to Alert/Situation if warranted (Ch.18)",
     ],
     "District-degradation to cell-investigation workflow."),
    ("h2", "7.5 Data Model"),
    ("bullets", [
        "PM Record — cell, date, KPI, value, source, coverage status.",
        "KPI Definition — name, formula, threshold, effective date range (versioned per Ch.22).",
        "Investigation — trigger geography, opened date, linked cells, linked evidence, status, outcome.",
    ]),
    ("h2", "7.6 Security Controls"),
    ("bullets", [
        "KPI definitions are change-controlled through the Rule Service (Ch.22); no adapter may hardcode a threshold.",
    ]),
    ("h2", "7.7 Failure Modes"),
    ("bullets", [
        "NMS export delayed: coverage status shows Grey/Amber rather than a false Green; investigation triggers are suppressed until data arrives or a manual override is recorded.",
        "PM screenshot ingestion (where no export is available) persists partial state and resumes on next delivery without losing prior progress.",
    ]),
    ("h2", "7.8 Non-Functional Requirements"),
    ("bullets", [
        "KPI Engine recomputation for a full day's national PM volume completes within the operational window required for next-morning district review.",
    ]),
    ("h2", "7.9 Acceptance Criteria"),
    ("bullets", [
        "A synthetic district degradation is demonstrably escalated to cell-level investigation with correct topology resolution.",
        "Coverage status (Green/Amber/Grey) is shown to be independent of and alongside the KPI value.",
    ]),
    ("proposed",
     "Confirm the authoritative KPI set (e.g. availability, drop-call rate, congestion) and their formulas/thresholds "
     "with NCA network-engineering leadership; the Rule Service architecture supports any agreed set without "
     "redesign."),
    ("trace", "NCIE-001 §Product Capability Architecture (Network Intelligence); §Data, Intelligence Domain, Canonical Model & Information Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 8 — Topology, GIS, Spatial Intelligence & Mapping
# ---------------------------------------------------------------------------
BLOCKS[8] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Topology, Geography & QoS Campaign Intelligence."),
    ("h2", "8.1 Scope"),
    ("p",
     "Covers versioned network topology, natural-language place-to-cell resolution, historical topology "
     "reconstruction, and governed map layer presentation."),
    ("h2", "8.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Topology Service", "Maintains versioned cell/site topology per operator; historical topology retrievable."],
        ["Spatial Database", "Stores geography, place and cell geometries for spatial queries."],
        ["Geocoder", "Resolves natural-language place names to canonical geography, using minimal external context only."],
        ["Map API", "Serves governed, permission-aware map layers to the workspace (Ch.3)."],
    ],
     "Topology, GIS & Spatial Intelligence principal components."),
    ("h2", "8.3 Place-to-Cell Resolution Flow"),
    ("p",
     "This is the reference \"Madina-style\" flow named in the approved skeleton: a natural-language place "
     "name resolves through canonical geography to topology to cells to PM/NMS data to analysis, and it must "
     "remain intact end to end."),
    ("flow",
     [
        "Natural-language place name (e.g. 'Madina')",
        "Geocoder resolves to canonical Geography entity",
        "Topology Service resolves Geography to constituent Cells (version-aware)",
        "PM/NMS Service retrieves KPI data for resolved cells (Ch.7)",
        "Situational Awareness Workspace / Assistant present grounded analysis",
     ],
     "Natural-language place to cell-level analysis resolution flow."),
    ("h2", "8.4 Data Model"),
    ("bullets", [
        "Geography — hierarchical place entity (national/regional/district/place), versioned boundary.",
        "Cell/Site — network element with location, versioned by topology change history.",
        "Topology Version — snapshot of cell-to-geography and cell-to-site relationships at a point in time.",
    ]),
    ("h2", "8.5 Security Controls"),
    ("bullets", [
        "Map layers are permission-filtered per role before rendering; sensitive layers (e.g. Anti-Fraud locations) are never exposed to unauthorized roles even as a visual overlay.",
    ]),
    ("h2", "8.6 Failure Modes"),
    ("bullets", [
        "External mapping provider unavailable: NCIE falls back to a non-map geography selector (Ch.3, Ch.28); topology and cell data remain fully queryable.",
        "Ambiguous place-name resolution: system presents candidate matches for human disambiguation rather than guessing silently.",
    ]),
    ("h2", "8.7 Non-Functional Requirements"),
    ("bullets", [
        "Place-to-cell resolution completes within 2 seconds at p95 for common place names.",
    ]),
    ("h2", "8.8 Acceptance Criteria"),
    ("bullets", [
        "The Madina-style flow (§8.3) is demonstrably reproducible end to end for a representative set of place names.",
        "A historical topology query correctly reflects the topology as it existed at a specified prior date.",
    ]),
    ("proposed",
     "Confirm the specific external mapping/geocoding provider and licensing model with NCA procurement; "
     "the architecture treats it as a replaceable provider behind the Map API and Geocoder (§8.2)."),
    ("trace", "NCIE-001 §Topology, Geography & QoS Campaign Intelligence."),
]
