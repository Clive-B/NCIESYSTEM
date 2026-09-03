"""NCIE-002 content batch: Chapters 25-32."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 25 — API, Event Bus & Integration Contracts
# ---------------------------------------------------------------------------
BLOCKS[25] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Data Acquisition, Integration, Source Intelligence & Ingestion Governance."),
    ("h2", "25.1 Scope"),
    ("p",
     "Defines reliable inter-service communication: governed APIs, the platform event bus, schema/contract "
     "versioning, and authorization enforcement across every service call — internal or external."),
    ("h2", "25.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["API Gateway", "Single authenticated entry point for synchronous service and external-partner APIs."],
        ["Event Bus", "Publishes PM/source/alert/workflow events for asynchronous consumption."],
        ["Schema Registry", "Versions request/response and event schemas; enforces compatibility rules."],
        ["Service Contracts", "Documented, versioned interface definitions between NCIE services."],
    ],
     "API, Event Bus & Integration Contracts principal components."),
    ("h2", "25.3 Event Categories"),
    ("bullets", [
        "Source events — new artifact validated, source health change (Ch.6).",
        "PM/KPI events — degradation detected, investigation opened (Ch.7).",
        "Alert/Situation events — Alert raised/closed, Situation opened (Ch.18).",
        "Workflow events — Run completed, WAITING_FOR_* entered/resolved (Ch.21).",
        "Collaborative events — material collaboration audit events (Ch.20, Ch.23)."],
    ),
    ("h2", "25.4 Reliability Patterns"),
    ("bullets", [
        "Every API call and event carries a correlation ID for end-to-end tracing.",
        "Event delivery is idempotent-consumer safe: duplicate delivery does not duplicate effect (Ch.21).",
        "Schema changes follow additive-first compatibility; breaking changes require a new major contract version, never an in-place redefinition.",
    ]),
    ("h2", "25.5 Data Model"),
    ("bullets", [
        "Service Contract — name, version, request/response schema reference, owning service.",
        "Event — type, schema version, payload, correlation ID, published timestamp.",
    ]),
    ("h2", "25.6 Security Controls"),
    ("bullets", [
        "The API Gateway enforces the same authorization layers as any other NCIE entry point (Ch.4); no internal service is reachable by bypassing it.",
        "External-partner API access uses scoped machine identities with the narrowest capability set required (Ch.4).",
    ]),
    ("h2", "25.7 Failure Modes"),
    ("bullets", [
        "Event Bus degraded: publishing services buffer locally and retry; no event is silently dropped (Ch.28)."],
    ),
    ("h2", "25.8 Non-Functional Requirements"),
    ("bullets", [
        "Internal API calls complete within 200ms at p95 under normal load; event delivery latency is bounded per event category (Ch.30)."],
    ),
    ("h2", "25.9 Acceptance Criteria"),
    ("bullets", [
        "A schema-breaking change is demonstrably rejected unless published as a new contract version.",
        "A simulated duplicate event delivery demonstrably does not duplicate downstream effect.",
    ]),
    ("proposed",
     "Confirm whether NCA has existing enterprise middleware/ESB standards that NCIE must integrate with rather "
     "than operate independently; the API Gateway/Event Bus architecture can front an existing middleware layer "
     "without redesign if required."),
    ("trace", "NCIE-001 §Data Acquisition, Integration, Source Intelligence & Ingestion Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 26 — Security, Privacy, Sovereignty & Sensitive Data
# ---------------------------------------------------------------------------
BLOCKS[26] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance."),
    ("h2", "26.1 Scope"),
    ("p",
     "Defines the technical protection of sensitive intelligence beyond identity/authorization (Ch.4): "
     "encryption, secrets management, segmentation, protected-field handling, search/cache isolation, "
     "external-processing governance, and break-glass/export/redaction controls."),
    ("h2", "26.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Security Services", "Platform-wide encryption, network segmentation and hardening baseline."],
        ["Secrets & Key Management", "Centralized credential/key storage; no secret is ever embedded in code, config files or documents."],
        ["Data Protection Layer", "Applies classification-aware handling (public/internal/protected/sensitive) across storage, search and cache."],
        ["Monitoring", "Security event detection feeding Observability (Ch.27)."],
    ],
     "Security, Privacy, Sovereignty & Sensitive Data principal components."),
    ("h2", "26.3 Classification and Protected Data"),
    ("bullets", [
        "Ghana Card and foreign-passport-derived identifiers (Ch.14), SIM identifiers, and precise location data are classified protected or sensitive and are field-level access-controlled (Ch.4).",
        "Search indexes, vector stores and caches are isolated per classification tier — a protected field is never indexed into a general-purpose search or embedding store without the same access control applied to the index itself.",
        "External AI/RPA processing of protected or sensitive data is governed by explicit policy in the Model Registry (Ch.24) and Capability Registry (Ch.21); default is minimisation and, where feasible, exclusion.",
    ]),
    ("h2", "26.4 Break-Glass, Export and Redaction"),
    ("bullets", [
        "Break-glass access to normally restricted data is time-bounded, individually logged, and requires post-hoc justification review (Ch.4 §4.5).",
        "Data export is a controlled action requiring authorization and is itself an audited event (Ch.23).",
        "Redaction of protected fields for lower-clearance views is applied server-side, never left to client-side masking alone.",
        "Chain-of-custody for exported or redacted material is preserved via the Evidence/Provenance architecture (Ch.23)."],
    ),
    ("h2", "26.5 Sovereignty Posture"),
    ("p",
     "Consistent with Chapter 1's posture statement, NCIE's default architecture keeps canonical and protected "
     "data within Ghanaian jurisdiction; any external processing is minimised, logged and policy-governed rather "
     "than assumed."),
    ("h2", "26.6 Data Model"),
    ("bullets", [
        "Classification Tag — field/record reference, tier (public/internal/protected/sensitive), applicable controls.",
        "Break-Glass Event — actor, accessed data, justification, review status.",
        "Export Record — requester, authorization reference, exported content reference, timestamp.",
    ]),
    ("h2", "26.7 Security Controls"),
    ("bullets", [
        "Encryption at rest and in transit is mandatory for protected and sensitive tiers; keys are managed by the Secrets & Key Management component, never application code.",
        "Network segmentation isolates ingestion, canonical/analytical storage and external-facing services into distinct zones.",
    ]),
    ("h2", "26.8 Failure Modes"),
    ("bullets", [
        "Key Management unavailable: services relying on protected-tier decryption fail closed rather than falling back to an unencrypted path (Ch.28)."],
    ),
    ("h2", "26.9 Non-Functional Requirements"),
    ("bullets", [
        "Classification-tier lookups add no more than 20ms at p95 to a protected-field query (Ch.30)."],
    ),
    ("h2", "26.10 Acceptance Criteria"),
    ("bullets", [
        "A protected field is demonstrably absent from any general-purpose search/embedding index accessible to unauthorized roles.",
        "A break-glass access is demonstrably logged with justification captured before or immediately after use.",
    ]),
    ("proposed",
     "Confirm final data classification tiers, residency, retention and third-party processing policy with NCA "
     "data-protection/legal leadership; the architecture in this chapter is designed to be conservative pending "
     "that confirmation and does not require redesign once policy is finalised."),
    ("trace", "NCIE-001 §Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance."),
]

# ---------------------------------------------------------------------------
# Chapter 27 — Observability, Health, Operations & Support
# ---------------------------------------------------------------------------
BLOCKS[27] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
    ("h2", "27.1 Scope"),
    ("p",
     "Defines how NCIE monitors itself: platform health, automation health, source health and sector "
     "(domain) health kept as distinct, individually visible signals, plus runbooks and escalation."),
    ("h2", "27.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Observability Platform", "Collects metrics, logs and traces across all NCIE services."],
        ["Health Service", "Aggregates platform-level health for the National Operating Picture (Ch.18)."],
        ["Source Monitor", "Tracks per-source freshness and coverage status (Ch.6)."],
        ["Automation Monitor", "Tracks Orchestrator/RPA provider health and Run success rates (Ch.21)."],
    ],
     "Observability, Health, Operations & Support principal components."),
    ("h2", "27.3 Health Signal Categories"),
    ("bullets", [
        "Platform health — service availability, latency, error rates.",
        "Automation health — provider availability, Run success/failure rates, queue depth.",
        "Source health — per-source freshness, coverage status (Green/Amber/Grey per Ch.6 §6.9), last successful acquisition.",
        "Sector/domain health — per-domain (Network, Traffic, Revenue, MoMo, SIM, Anti-Fraud, Regulatory) data currency and quality summary.",
    ]),
    ("h2", "27.4 Explainable Operational State"),
    ("p",
     "Every health signal shown to a human is paired with the freshness/last-validated-output metadata that "
     "explains it, and the Assistant (Ch.19) can explain authoritative operational state in natural language "
     "grounded in these same signals — it does not have a separate, potentially inconsistent view of health."),
    ("h2", "27.5 Data Model"),
    ("bullets", [
        "Health Signal — category, scope (service/source/domain), status, last-updated, contributing metrics.",
        "Runbook — trigger condition, procedure reference, owning team.",
        "Escalation Policy — severity, notification chain, timeout-to-escalate.",
    ]),
    ("h2", "27.6 Security Controls"),
    ("bullets", [
        "Observability data itself is classification-aware; logs/traces do not capture protected-tier field values in plaintext (Ch.26)."],
    ),
    ("h2", "27.7 Failure Modes"),
    ("bullets", [
        "Observability Platform degraded: services continue operating; only visibility into their health is reduced, with that reduction itself surfaced as a meta-level health signal (Ch.28)."],
    ),
    ("h2", "27.8 Non-Functional Requirements"),
    ("bullets", [
        "Health signal propagation from source event to visible status update completes within 60 seconds at p95 (Ch.30)."],
    ),
    ("h2", "27.9 Acceptance Criteria"),
    ("bullets", [
        "Platform, automation, source and sector health are demonstrably shown as distinct signals for the same underlying incident, not collapsed into one status.",
    ]),
    ("proposed",
     "Confirm the on-call/support model (in-house NCA team, vendor-supported, or hybrid) and required operational "
     "dashboards with NCA operations leadership; runbook content is produced during Ch.32 handover regardless of "
     "model chosen."),
    ("trace", "NCIE-001 §Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
]

# ---------------------------------------------------------------------------
# Chapter 28 — Resilience, High Availability, Backup & Disaster Recovery
# ---------------------------------------------------------------------------
BLOCKS[28] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
    ("h2", "28.1 Scope"),
    ("p",
     "Defines failure behaviour and recovery so that loss of any single external dependency degrades only the "
     "affected capability, never core NCIE, consistent with the graceful-degradation principle in Chapter 1."),
    ("h2", "28.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["HA Design", "Redundancy and failover design per service tier."],
        ["Backup", "Scheduled, verified backups of canonical data, rules, audit, memory, schedules and workflows."],
        ["Disaster Recovery (DR)", "Recovery procedures and secondary site/capability for platform-level failure."],
        ["Recovery Coordinator", "Orchestrates ordered service restoration and state reconciliation after an outage."],
        ["State Reconciliation", "Resolves state drift between primary and recovered/failed-over components."],
    ],
     "Resilience, High Availability, Backup & Disaster Recovery principal components."),
    ("h2", "28.3 Dependency Degradation Matrix"),
    ("table",
     ["Dependency Lost", "Preserved Capability", "Degraded Capability"],
     [
        ["AI / Model Gateway", "Core NCIE, all canonical data, workflows, non-conversational tool access", "Conversational Assistant, proactive room participation (Ch.19, Ch.20, Ch.24)"],
        ["RPA provider", "Manually triggered/API-based acquisition, all canonical data", "Automated acquisition/execution via that provider; failover to alternate provider where configured (Ch.21)"],
        ["Mapping provider", "Full non-map workspace, all domain data and topology data", "Map visualisation only; non-map geography selector remains available (Ch.3, Ch.8)"],
        ["Single source system", "All other sources, all prior canonical data", "New data from that source; existing status visibly degraded, not silently missing (Ch.6)"],
        ["(v0.5) Agent Factory", "Existing eligible Registered Agents; direct governed ARGUS model use; deterministic NCIE", "New Dynamic Agent Synthesis; an explicit synthesis-unavailable state is returned (Ch.24 §24.4A.1)"],
        ["(v0.5) Ephemeral Agent Runtime", "Existing unaffected services; Registered Agent execution", "Dynamic Agent execution; an explicit runtime-unavailable state is returned, never a silent retry (Ch.24 §24.4A.3)"],
        ["(v0.5) VPF", "Deterministic NCIE functions; existing already-validated results", "New substantive AI output remains UNVALIDATED or VALIDATION_UNAVAILABLE — VPF failure shall not fail open (Ch.24 §24.4A.4)"],
        ["(v0.5) Model / Agent / Tool / VPF Profile Registry", "Last-known eligible state only where an explicitly approved current signed/cached policy already exists", "New eligibility determinations; no eligibility is assumed absent confirmed current Registry state (Ch.24 §24.9)"],
    ],
     "What is preserved versus degraded when a given external dependency is lost."),
    ("h2", "28.4 Backup Scope"),
    ("bullets", [
        "Canonical and analytical data (Ch.5).",
        "Evidence and provenance graph (Ch.23).",
        "Rules and their version history (Ch.22).",
        "Audit trail (Ch.23).",
        "Memory — private, shared room, and institutional (Ch.20).",
        "Schedules and in-flight/waiting workflow state (Ch.21) — a waiting workflow must survive a platform restart or failover without losing its wait state.",
    ]),
    ("h2", "28.5 Recovery Flow"),
    ("flow",
     [
        "Failure or DR event detected (Observability, Ch.27)",
        "Recovery Coordinator initiates ordered restoration per service tier",
        "Backup/replica promoted where required",
        "State Reconciliation resolves drift against last-known-good canonical state",
        "Waiting workflows resume from persisted wait state (Ch.21)",
        "Health Service confirms restored status to National Operating Picture (Ch.18)",
     ],
     "Disaster recovery and state-reconciliation flow."),
    ("h2", "28.6 Security Controls"),
    ("bullets", [
        "Backups are encrypted and classification-aware, subject to the same protected-tier controls as live data (Ch.26).",
    ]),
    ("h2", "28.7 Failure Modes"),
    ("bullets", [
        "Partial failover leaving two components with divergent state: State Reconciliation flags the divergence for review rather than auto-resolving silently.",
    ]),
    ("h2", "28.8 Non-Functional Requirements"),
    ("bullets", [
        "Recovery Time Objective (RTO) and Recovery Point Objective (RPO) are defined per critical service tier (see proposed defaults below) and validated by DR test per Ch.31.",
    ]),
    ("h2", "28.9 Acceptance Criteria"),
    ("bullets", [
        "A simulated loss of each dependency in §28.3 demonstrably preserves the stated capability and only degrades the stated one.",
        "A simulated platform restart during an active WAITING_FOR_PM workflow demonstrably resumes correctly rather than losing the wait state.",
        "(v0.5) A simulated VPF outage demonstrably leaves new substantive AI output UNVALIDATED or VALIDATION_UNAVAILABLE rather than PASS, while deterministic NCIE functions remain available (§28.3).",
    ]),
    ("proposed",
     "Proposed default RTO/RPO: Tier 1 (identity, canonical data, evidence/audit) RTO 4 hours / RPO 15 minutes; "
     "Tier 2 (domain services, automation) RTO 8 hours / RPO 1 hour; Tier 3 (AI/collaborative features) RTO 24 "
     "hours / RPO 4 hours. Confirm against NCA business-continuity requirements and the DR site location."),
    ("trace", "NCIE-001 §Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance; NCIE-007 v1.1 Ch.32 (Model & Agent Lifecycle Governance)."),
]

# ---------------------------------------------------------------------------
# Chapter 29 — Deployment, Environments, DevSecOps & Configuration
# ---------------------------------------------------------------------------
BLOCKS[29] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
    ("h2", "29.1 Scope"),
    ("p",
     "Defines controlled build and deployment: environment separation, versioned releases, secrets handling, "
     "rollback and the protection of sensitive production data from non-production environments."),
    ("h2", "29.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["CI/CD", "Automated build, test and deployment pipeline with mandatory gate checks (Ch.31)."],
        ["Artifact Registry", "Versioned, immutable build artifacts."],
        ["Environment Configuration", "Per-environment configuration, separated from code and from production secrets."],
        ["Secrets Integration", "Runtime secret injection from the Secrets & Key Management component (Ch.26); never committed to code or docs."],
    ],
     "Deployment, Environments, DevSecOps & Configuration principal components."),
    ("h2", "29.3 Environment Model"),
    ("bullets", [
        "Development — active engineering work; synthetic or heavily masked data only.",
        "Test — automated and manual test execution (Ch.31); synthetic or masked data only.",
        "Staging — production-representative rehearsal environment; masked production-shaped data only.",
        "Production — live NCIE; the only environment permitted to hold real protected/sensitive data.",
    ]),
    ("h2", "29.4 Release Discipline"),
    ("bullets", [
        "Every deployment is versioned and traceable to a specific artifact and commit.",
        "Rollback to the immediately prior artifact version is a supported, tested operation, not an emergency improvisation.",
        "Every deployment is itself an audited change event (Ch.23), recording who approved and executed it.",
    ]),
    ("h2", "29.5 Data Model"),
    ("bullets", [
        "Release — artifact version, environment, deployed-by, timestamp, rollback target.",
        "Environment Config — environment, key, value reference (secrets stored by reference, not value).",
    ]),
    ("h2", "29.6 Security Controls"),
    ("bullets", [
        "Secrets are never present in source control, CI/CD logs or any document in this suite; they are injected at runtime by reference only.",
        "Production data does not flow to non-production environments unmasked; masking is enforced by the pipeline, not left to manual discipline.",
    ]),
    ("h2", "29.7 Failure Modes"),
    ("bullets", [
        "Failed deployment gate check: deployment is blocked from promotion; the pipeline does not allow manual override of a failed mandatory gate without a recorded exception (Ch.31)."],
    ),
    ("h2", "29.8 Non-Functional Requirements"),
    ("bullets", [
        "Rollback to the prior artifact version completes within the RTO defined for the affected service tier (Ch.28)."],
    ),
    ("h2", "29.9 Acceptance Criteria"),
    ("bullets", [
        "A deployment with a failing mandatory gate is demonstrably blocked from reaching production.",
        "A rollback is demonstrably exercised successfully in a rehearsal environment before go-live.",
    ]),
    ("proposed",
     "Confirm the hosting model (on-premises NCA data centre, sovereign cloud, or hybrid — consistent with the "
     "posture proposed in Ch.1 §1.6) and release authority (who may approve a production deployment) with NCA "
     "IT leadership."),
    ("trace", "NCIE-001 §Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
]

# ---------------------------------------------------------------------------
# Chapter 30 — Performance, Scalability, Accessibility & Non-Functional Architecture
# ---------------------------------------------------------------------------
BLOCKS[30] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Product Capability Architecture; Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
    ("h2", "30.1 Scope"),
    ("p",
     "Defines the measurable quality attributes referenced by number throughout this specification (e.g. "
     "\"p95 latency\", \"national data volumes\") as one consolidated, consistent set."),
    ("h2", "30.2 Reference Non-Functional Targets"),
    ("table",
     ["Attribute", "Target", "Applies To"],
     [
        ["Interactive query latency (p95)", "≤ 3 seconds", "Workspace panels, Assistant invoked responses, Fusion queries (Ch.3, Ch.17, Ch.19)"],
        ["Authorization decision latency (p95)", "≤ 100 ms", "Authorization Service (Ch.4)"],
        ["Internal API latency (p95)", "≤ 200 ms", "API Gateway (Ch.25)"],
        ["Scheduled Request punctuality (p99)", "≤ 1 minute drift", "Scheduler (Ch.21)"],
        ["Health signal propagation (p95)", "≤ 60 seconds", "Observability (Ch.27)"],
        ["Concurrent users (initial production target)", "≥ 500 concurrent, ≥ 3,000 registered", "Platform-wide"],
        ["National cell/topology scale", "≥ current national cell count, versioned", "Ch.7, Ch.8"],
        ["Accessibility conformance", "WCAG 2.1 AA", "Situational Awareness Workspace (Ch.3)"],
    ],
     "Reference non-functional targets consumed by other chapters (proposed baseline; confirm at scale)."),
    ("h2", "30.3 Capacity Model"),
    ("p",
     "Canonical and analytical stores scale horizontally by operator/geography/time partition (Ch.5); "
     "concurrency controls at the Authorization and API layers (Ch.4, Ch.25) prevent a single tenant or "
     "workload from starving others. Capacity planning is revisited at each major release using Observability "
     "trend data (Ch.27)."),
    ("h2", "30.4 Accessibility Beyond Colour"),
    ("bullets", [
        "Every status distinction that uses colour (e.g. Green/Amber/Grey coverage, Ch.6 §6.9) also carries a text label and, where applicable, an icon shape — colour is never the only signal.",
        "Keyboard navigation and screen-reader labelling are required for all primary Situational Awareness Workspace panels (Ch.3).",
    ]),
    ("h2", "30.5 Performance Cannot Bypass Governance"),
    ("p",
     "No performance optimisation (caching, precomputation, denormalisation) is permitted to bypass "
     "authorization filtering, evidence/provenance recording, or audit logging. Where caching is used for "
     "latency (e.g. Ch.4 authorization decisions, Ch.22 rule lookups), cache invalidation is itself designed to "
     "preserve correctness of these controls, not just data freshness."),
    ("h2", "30.6 Security Controls"),
    ("bullets", [
        "Load-testing and capacity-testing environments use masked data only, consistent with Ch.29 §29.3.",
    ]),
    ("h2", "30.7 Failure Modes"),
    ("bullets", [
        "Load exceeding capacity targets: services degrade gracefully with request shedding/backpressure and visible status, rather than uncontrolled failure (Ch.28)."],
    ),
    ("h2", "30.8 Acceptance Criteria"),
    ("bullets", [
        "Each target in §30.2 is demonstrably measured under a representative load test and recorded as part of production acceptance (Ch.31).",
        "A representative workspace panel passes an automated WCAG 2.1 AA accessibility check.",
    ]),
    ("proposed",
     "The specific figures in §30.2 (concurrent users, national cell count, latency targets) are proposed "
     "baselines derived from NCIE-001's stated scale ambitions; confirm exact production-scale targets with NCA "
     "capacity-planning stakeholders before final acceptance sign-off."),
    ("trace", "NCIE-001 §Product Capability Architecture; §Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
]

# ---------------------------------------------------------------------------
# Chapter 31 — Testing, Verification, Traceability & Acceptance Architecture
# ---------------------------------------------------------------------------
BLOCKS[31] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
    ("h2", "31.1 Scope"),
    ("p",
     "Defines how every requirement in NCIE-001 and every architectural commitment in NCIE-002 will be "
     "proven, through a Requirements Traceability Matrix (RTM), layered test suites, and governed "
     "acceptance evidence."),
    ("h2", "31.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Test Architecture", "Defines test layers, environments and required coverage per chapter."],
        ["Requirements Traceability Matrix (RTM)", "Maps every NCIE-001 requirement ID (chapter.paragraph) to its NCIE-002 architectural component(s) and test case(s)."],
        ["Evaluation Suites", "AI- and automation-specific evaluation suites, including the Collaborative Evaluation Harness (Ch.24 §24.5)."],
        ["Acceptance Evidence Repository", "Stores test results, sign-offs and defect references as durable acceptance evidence."],
    ],
     "Testing, Verification, Traceability & Acceptance Architecture principal components."),
    ("h2", "31.3 Test Layers"),
    ("bullets", [
        "Functional — per-chapter feature correctness (Ch.6-Ch.22 domain behaviours).",
        "Integration — cross-service and cross-domain flows (Ch.17, Ch.25).",
        "Security — authorization, protected-data and guardrail verification (Ch.4, Ch.26, Ch.24).",
        "AI/Collaborative evaluation — Model Gateway and collaborative-participation quality (Ch.20, Ch.24).",
        "Automation — RPA/orchestration reliability, idempotency and failover (Ch.21).",
        "Resilience — dependency-loss and DR rehearsal (Ch.28).",
        "Cross-domain and multi-user — scenarios spanning multiple domains and multiple concurrent, differently-permissioned users (Ch.17, Ch.20).",
    ]),
    ("h2", "31.3A Dynamic Agent Synthesis & VPF Acceptance Architecture (v0.5)"),
    ("p",
     "Architecture-level acceptance scenarios for the Ch.24 §24.4A extension. These are testable "
     "architectural acceptance criteria, not the full NCIE-007 acceptance catalogue (NCIE-007 v1.1 Ch.32 "
     "remains authoritative for the detailed test suite):"),
    ("bullets", [
        "ARGUS can use an eligible Registered Agent.",
        "ARGUS can synthesize a bounded Ephemeral Agent when no adequate registered agent exists.",
        "Individual bounded synthesis does not require Codex hand-coding.",
        "A synthesized agent cannot create new permissions.",
        "A synthesized agent cannot self-register.",
        "Recursive synthesis is disabled by default.",
        "A synthesized agent cannot bypass the Model Gateway.",
        "A synthesized agent cannot bypass the Tool Gateway.",
        "Substantive AI output cannot bypass VPF.",
        "VPF PASS ≠ Human / Institutional Approval.",
        "VPF unavailable ≠ PASS.",
        "Agent Factory unavailable does not disable deterministic NCIE.",
        "A missing primitive produces an Engineering Change Candidate.",
        "Current authorization remains authoritative at execution.",
    ]),
    ("h2", "31.3B Human-Primary Acceptance Scenario (Mandatory)"),
    ("p",
     "One mandatory adversarial acceptance scenario, which must pass before production acceptance: ARGUS "
     "receives a high-consequence task; ARGUS synthesizes an agent; VPF Gate A passes; the sandbox "
     "passes; the agent uses eligible models and tools; VPF Gate B returns PASS; several agents agree. "
     "Verify that the consequential institutional action still requires the applicable current human/"
     "institutional authorization — none of the preceding facts independently creates institutional "
     "execution authority (Ch.24 §24.4A.10)."),
    ("h2", "31.4 Requirements Traceability Matrix"),
    ("p",
     "The RTM uses NCIE-001's stable chapter.paragraph requirement ID (e.g. §18.241, per NCIE-001 §18.241 "
     "\"Requirement ID\") as the anchor, and maps each to the NCIE-002 chapter/component that implements it and "
     "the test case(s) that verify it. This chapter defines the RTM's structure; the populated RTM is a "
     "companion artifact maintained alongside this document and delivered as part of Chapter 32 handover."),
    ("table",
     ["RTM Column", "Content"],
     [
        ["Requirement ID", "NCIE-001 chapter.paragraph reference (e.g. §18.241)."],
        ["Requirement Summary", "Short restatement of the requirement."],
        ["NCIE-002 Component", "Owning architectural component (e.g. Rule Service, Ch.22)."],
        ["Test Case ID", "Reference to the verifying test case."],
        ["Status", "Not started / In progress / Passed / Failed / Waived."],
        ["Evidence Reference", "Link into the Acceptance Evidence Repository."],
    ],
     "Requirements Traceability Matrix structure."),
    ("h2", "31.5 Acceptance Gates"),
    ("bullets", [
        "A critical defect (data corruption, authorization bypass, evidence/provenance loss, human-authority bypass) blocks ordinary production acceptance — no severity-based waiver is permitted for these categories.",
        "AI shall not approve NCIE for production (per NCIE-001 §18.244); final acceptance authority is always a named human/institutional authority.",
        "Conditional acceptance, where permitted for non-critical gaps, records Known Limitation, Risk, Mitigation, Owner and Target Resolution (per NCIE-001 §18.243).",
    ]),
    ("h2", "31.6 Data Model"),
    ("bullets", [
        "RTM Entry — as per §31.4 table.",
        "Test Case — id, layer, preconditions, steps, expected result, linked requirement ID(s).",
        "Acceptance Record — test case, executed-by, date, result, defect reference if applicable.",
    ]),
    ("h2", "31.7 Security Controls"),
    ("bullets", [
        "Test environments never contain unmasked production protected/sensitive data (Ch.29 §29.3).",
    ]),
    ("h2", "31.8 Failure Modes"),
    ("bullets", [
        "A failed mandatory acceptance criterion is not marked passed without corrective evidence attached (per NCIE-001 §18.242)."],
    ),
    ("h2", "31.9 Acceptance Criteria for This Chapter"),
    ("bullets", [
        "The RTM structure in §31.4 is demonstrably populated for at least one representative requirement per NCIE-002 chapter as a proof of traceability before full production acceptance.",
        "Five-domain acceptance (Traffic, Revenue, Mobile Money, SIM Registration, Anti-Fraud, per NCIE-001 §18.245) is explicitly represented in the RTM.",
    ]),
    ("proposed",
     "Confirm acceptance authorities per domain (who signs off Five-Domain Acceptance, who signs off overall "
     "production acceptance) with NCA leadership; NCIE-001 already fixes that AI may not hold this authority."),
    ("trace", "NCIE-001 §Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance; NCIE-007 v1.1 Ch.32 (Model & Agent Lifecycle Governance) §32.7-§32.10."),
]

# ---------------------------------------------------------------------------
# Chapter 32 — Operations, Administration, Documentation & Codex Handover
# ---------------------------------------------------------------------------
BLOCKS[32] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance."),
    ("h2", "32.1 Scope"),
    ("p",
     "Defines sustainable production ownership and the package handed to Codex/implementation teams: "
     "administration surfaces, runbooks, the full documentation set, and an implementation backlog mapped to "
     "requirements."),
    ("h2", "32.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Administration Plane", "Admin surfaces for users/roles, rules, sources, automation providers and AI models."],
        ["Documentation Set", "Architecture (this document), API, data and security specifications (NCIE-003 through NCIE-016)."],
        ["Runbooks", "Operational procedures per Ch.27/Ch.28, with named owners."],
        ["Handover Package", "Consolidated deliverable to Codex: architecture, RTM, deployment/recovery docs, backlog — no credentials included."],
        ["Implementation Work Breakdown", "NCIE-002 components mapped to build sequence (detailed in NCIE-017)."],
    ],
     "Operations, Administration, Documentation & Codex Handover principal components."),
    ("h2", "32.3 Administration Surfaces"),
    ("bullets", [
        "User and role administration (Ch.4).",
        "Rule administration (Ch.22): surcharge rate, SIM limits, KPI thresholds, REWS rules.",
        "Source administration (Ch.6): registry entries, owners, health thresholds.",
        "Automation administration (Ch.21): Capability Registry entries, provider policy.",
        "Model administration (Ch.24): Model Registry entries, evaluation status, participation-mode approval per model.",
    ]),
    ("h2", "32.4 Handover Contents"),
    ("bullets", [
        "This document (NCIE-002) as the authoritative architecture reference.",
        "The populated Requirements Traceability Matrix (Ch.31).",
        "Deployment and recovery documentation (Ch.28, Ch.29).",
        "Runbooks with named operational owners (Ch.27).",
        "Implementation backlog mapped to NCIE-001 requirement IDs and NCIE-002 components.",
        "No credentials, secrets or keys are included in any handover artifact — these are provisioned separately through the Secrets & Key Management component (Ch.26)."],
    ),
    ("h2", "32.4A Dynamic Agent Synthesis & VPF Engineering Handover (v0.5)"),
    ("p", "Extends the implementation handover to explicitly require engineering delivery of:"),
    ("bullets", [
        "Agent Factory (Ch.24 §24.4A.1).",
        "Agent Definition logical implementation.",
        "Ephemeral Agent Runtime (Ch.24 §24.4A.3).",
        "Agent Registry integration (Ch.24 §24.4A.2).",
        "VPF runtime (Ch.24 §24.4A.4).",
        "VPF Profile Registry integration (Ch.24 §24.4A.7).",
        "VPF Gate A (Ch.24 §24.4A.5).",
        "VPF Gate B (Ch.24 §24.4A.6).",
        "Sandbox/Evaluation capability.",
        "Runtime-policy enforcement.",
        "Agent expiry.",
        "Kill/Suspend controls.",
        "Provenance.",
        "Observability.",
    ]),
    ("p",
     "Final vendor choices are not prescribed here beyond what is already approved elsewhere (NCIE-004). "
     "Once these capabilities are implemented and operationally approved, ARGUS can create bounded "
     "task-specific agents without requiring bespoke Codex development for every individual agent. Where "
     "the required capability exceeds the approved Agent Factory primitives, engineering/Codex "
     "intervention is required (Ch.24 §24.4A.1)."),
    ("h2", "32.5 Handover Flow"),
    ("flow",
     [
        "Architecture and RTM finalised and reviewed (Ch.1-31)",
        "Administration Plane configured for initial production users/rules/sources",
        "Runbooks assigned to named operational owners",
        "Implementation Work Breakdown sequenced (NCIE-017)",
        "Handover Package assembled, credentials excluded",
        "Codex/implementation teams receive package and begin build",
     ],
     "Architecture-to-Codex handover flow."),
    ("h2", "32.6 Data Model"),
    ("bullets", [
        "Admin Action — actor, target (user/rule/source/provider/model), change, timestamp (audited per Ch.23).",
        "Runbook Entry — trigger, procedure, owner, last-reviewed date.",
        "Handover Artifact — type, version, inclusion/exclusion status (e.g. credentials explicitly excluded).",
    ]),
    ("h2", "32.7 Security Controls"),
    ("bullets", [
        "Administration Plane actions are themselves authorized and audited exactly like any other sensitive action (Ch.4, Ch.23) — administrator status is not a bypass of governance.",
        "Handover Package assembly is checked against a no-credentials checklist before release.",
    ]),
    ("h2", "32.8 Failure Modes"),
    ("bullets", [
        "Runbook without a named current owner: flagged by the Administration Plane as an operational gap rather than silently left unassigned.",
    ]),
    ("h2", "32.9 Non-Functional Requirements"),
    ("bullets", [
        "Administration Plane actions apply and take effect within the same latency targets as their underlying component (Ch.30)."],
    ),
    ("h2", "32.10 Acceptance Criteria"),
    ("bullets", [
        "The Handover Package is demonstrably assembled with all items in §32.4 present and the no-credentials check passed.",
        "Every runbook has a named current owner at the time of handover.",
        "(v0.5) The §32.4A engineering deliverable list is demonstrably present in the Handover Package before Dynamic Agent Synthesis is activated in production.",
    ]),
    ("proposed",
     "Confirm required handover artifacts beyond the baseline in §32.4, and the operational owners for each "
     "runbook category, with NCA operations and the Codex/implementation team lead."),
    ("trace", "NCIE-001 §Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance; NCIE-001 v1.3 §18.241A; NCIE-007 v1.1 Ch.36 §36.7-§36.8."),
]
