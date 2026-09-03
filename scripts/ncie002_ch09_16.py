"""NCIE-002 content batch: Chapters 9-16."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 9 — QoS Campaign / Drive-Test Intelligence
# ---------------------------------------------------------------------------
BLOCKS[9] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Topology, Geography & QoS Campaign Intelligence."),
    ("h2", "9.1 Scope"),
    ("p",
     "Covers reuse of drive-test/QoS campaign data: campaign ingestion, geometry matching to topology, and "
     "presentation of the latest applicable campaign per geography alongside full historical access."),
    ("h2", "9.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Campaign Repository", "Stores QoS/drive-test campaigns with date, operator, route, technology and measurements."],
        ["Geometry Store", "Holds route/measurement geometries for spatial matching."],
        ["Matcher", "Associates campaign geometry with topology/geography for geography-specific latest-applicable resolution."],
        ["Analytics Service", "Computes campaign-derived KPIs and trend comparisons across campaigns."],
    ],
     "QoS Campaign Intelligence principal components."),
    ("h2", "9.3 Latest-Applicable Resolution"),
    ("p",
     "For any given geography, \"latest applicable\" campaign data is geography-specific: a newer campaign in "
     "one district does not make an older campaign in a different, unsampled district stale by association. "
     "Age and coverage are always shown alongside the data so a user can judge relevance."),
    ("flow",
     [
        "Campaign file/API ingestion (Ch.6)",
        "Geometry Store receives route/measurement geometry",
        "Matcher associates geometry to topology/geography",
        "Campaign Repository indexes by operator/date/geography",
        "Analytics Service surfaces latest-applicable + full history on request",
     ],
     "QoS Campaign ingestion-to-analysis flow."),
    ("h2", "9.4 Data Model"),
    ("bullets", [
        "Campaign — operator, date, route, technology, measurement set, source.",
        "Measurement Point — geolocated sample with KPI values.",
        "Geography Coverage Index — which geographies a given campaign actually sampled.",
    ]),
    ("h2", "9.5 Security Controls"),
    ("bullets", [
        "Campaign data is attributed to source operator/vendor and cannot be edited post-ingestion except through a versioned correction (Ch.5).",
    ]),
    ("h2", "9.6 Failure Modes"),
    ("bullets", [
        "Campaign geometry fails to match any known geography: retained and flagged unmatched rather than discarded, pending manual topology reconciliation.",
    ]),
    ("h2", "9.7 Non-Functional Requirements"),
    ("bullets", [
        "Latest-applicable lookup for a given geography returns within 2 seconds at p95.",
    ]),
    ("h2", "9.8 Acceptance Criteria"),
    ("bullets", [
        "For a geography sampled by multiple campaigns over time, the system correctly identifies the latest-applicable campaign and still allows retrieval of all prior campaigns.",
        "Age and coverage indicators are shown alongside every campaign-derived value in the workspace.",
    ]),
    ("proposed",
     "Confirm required campaign formats, KPI set and retention period with NCA network-engineering leadership; "
     "the Campaign Repository schema is format-agnostic at the storage layer."),
    ("trace", "NCIE-001 §Topology, Geography & QoS Campaign Intelligence."),
]

# ---------------------------------------------------------------------------
# Chapter 10 — Incident Intelligence & Operator Email
# ---------------------------------------------------------------------------
BLOCKS[10] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Product Capability Architecture; Automation Orchestration & RPA Data Acquisition."),
    ("h2", "10.1 Scope"),
    ("p",
     "Converts daily operator outage/fibre-cut/restoration email into governed, structured incident records, "
     "fused with NMS evidence for restoration verification."),
    ("h2", "10.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Mailbox Connector", "Reads designated operator incident mailboxes; original email is retained as evidence, never modified."],
        ["Extractor", "Structures operator-reported incident data (type, location, start time, cause) from email content."],
        ["Threading Service", "Deduplicates and threads related messages (initial report, updates, restoration) into one Incident."],
        ["Incident Workflow", "Tracks incident status; checks operator-reported restoration against NMS evidence before closure."],
    ],
     "Incident Intelligence & Operator Email principal components."),
    ("h2", "10.3 Email-to-Incident Flow"),
    ("flow",
     [
        "Operator incident email arrives in designated mailbox",
        "Mailbox Connector retains original as evidence",
        "Extractor structures incident fields",
        "Threading Service links to existing Incident or opens a new one",
        "Incident Workflow cross-checks restoration claim against NMS data (Ch.7)",
        "Incident closed or escalated to REWS/Situation (Ch.18)",
     ],
     "Operator incident email to governed Incident record."),
    ("h2", "10.4 Data Model"),
    ("bullets", [
        "Incident — category, affected geography/cells, start/restoration time (reported and verified), status, linked evidence.",
        "Email Evidence — original message, sender, timestamp, thread linkage; immutable.",
    ]),
    ("h2", "10.5 Security Controls"),
    ("bullets", [
        "Email content cannot issue commands to NCIE; the Extractor only produces proposed structured fields for the Incident Workflow, never direct system actions.",
        "Original email is retained unmodified as evidence for the life of the incident record (Ch.23).",
    ]),
    ("h2", "10.6 Failure Modes"),
    ("bullets", [
        "Restoration claimed by email but not corroborated by NMS: incident remains open pending verification rather than auto-closing.",
        "Mailbox unreachable: Source Health Monitor (Ch.6) flags degraded status; no incidents are silently missed without visibility.",
    ]),
    ("h2", "10.7 Non-Functional Requirements"),
    ("bullets", [
        "New incident emails are structured and threaded within 5 minutes of arrival under normal load.",
    ]),
    ("h2", "10.8 Acceptance Criteria"),
    ("bullets", [
        "A multi-message incident thread (report, update, restoration) is demonstrably consolidated into one Incident with full lineage to each source email.",
        "A restoration claim unsupported by NMS evidence is demonstrably kept open rather than auto-closed.",
    ]),
    ("proposed",
     "Confirm designated incident mailboxes, incident category taxonomy and closure rules with NCA network "
     "operations; the extraction/threading architecture is taxonomy-agnostic."),
    ("trace", "NCIE-001 §Product Capability Architecture; §Automation Orchestration & RPA Data Acquisition."),
]

# ---------------------------------------------------------------------------
# Chapter 11 — Traffic Intelligence
# ---------------------------------------------------------------------------
BLOCKS[11] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Product Capability Architecture; Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
    ("h2", "11.1 Scope"),
    ("p",
     "Covers International, Off-Net and On-Net traffic intelligence: explicit operator/period/type/volume/unit/"
     "source/coverage attribution, versioned corrections, and the feed into Revenue calculation (Ch.12) and "
     "cross-domain fusion (Ch.17)."),
    ("h2", "11.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Traffic Adapter", "Ingests traffic volumes per operator/period/type via Ch.6 channels."],
        ["Traffic Store", "Canonical, versioned traffic records."],
        ["Analytics Service", "Trend, comparison and anomaly views over traffic volumes."],
        ["Quality Service", "Flags missing periods and out-of-pattern values for review, without auto-correcting them."],
    ],
     "Traffic Intelligence principal components."),
    ("h2", "11.3 Data Model"),
    ("bullets", [
        "Traffic Record — operator, period, traffic type (International/Off-Net/On-Net), volume, unit, source, coverage status.",
        "Correction — versioned adjustment to a prior Traffic Record, with reason and actor.",
    ]),
    ("h2", "11.4 Traffic-to-Revenue Flow"),
    ("flow",
     [
        "Traffic Adapter ingests operator traffic volumes",
        "Quality Service flags missing/anomalous periods",
        "Traffic Store holds canonical, versioned traffic",
        "Revenue Calculator consumes Traffic for calculated Revenue (Ch.12)",
        "Cross-Domain Fusion consumes Traffic for correlation (Ch.17)",
     ],
     "Traffic Intelligence feeding Revenue and Fusion."),
    ("h2", "11.5 Security Controls"),
    ("bullets", [
        "Traffic classifications (International/Off-Net/On-Net) are fixed reference data, changeable only through the Rule Service change process (Ch.22)."],
    ),
    ("h2", "11.6 Failure Modes"),
    ("bullets", [
        "Missing period: remains explicitly missing in Revenue calculation inputs rather than treated as zero traffic (Ch.12).",
    ]),
    ("h2", "11.7 Non-Functional Requirements"),
    ("bullets", [
        "Monthly national traffic ingestion for all operators completes within the operational window required for Revenue Verification reporting (Ch.12).",
    ]),
    ("h2", "11.8 Acceptance Criteria"),
    ("bullets", [
        "A traffic correction is demonstrably versioned, with the prior value still retrievable for decision-time reconstruction.",
    ]),
    ("trace", "NCIE-001 §Product Capability Architecture; §Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
]

# ---------------------------------------------------------------------------
# Chapter 12 — Revenue Intelligence & Billing Verification
# ---------------------------------------------------------------------------
BLOCKS[12] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
    ("h2", "12.1 Scope"),
    ("p",
     "Covers deterministic calculated Revenue derivation from Traffic and the effective-dated surcharge rate, "
     "and its reconciliation against operator-reported Billing figures."),
    ("h2", "12.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Revenue Calculator", "Computes calculated Revenue deterministically from Traffic and the effective-dated surcharge Rule."],
        ["Billing Adapter", "Ingests operator-reported Billing figures."],
        ["Reconciliation Engine", "Compares calculated vs reported Revenue and surfaces differences with explicit basis/unit."],
        ["Rule Dependency", "Reads the current and historical surcharge rate from the Rule Service (Ch.22)."],
    ],
     "Revenue Intelligence & Billing Verification principal components."),
    ("h2", "12.3 Calculation Principle"),
    ("p",
     "Calculated Revenue and reported Revenue are always kept distinct and separately labelled. The surcharge "
     "rate is an effective-dated Rule Service value (currently supplied as USD 0.19) rather than a constant "
     "embedded in code, so historical calculations remain correct even after the rate changes."),
    ("rel",
     [
        ("Traffic Store", "supplies volumes to", "Revenue Calculator"),
        ("Rule Service (surcharge rate)", "supplies effective-dated rate to", "Revenue Calculator"),
        ("Revenue Calculator", "produces calculated Revenue for", "Reconciliation Engine"),
        ("Billing Adapter", "supplies reported Revenue to", "Reconciliation Engine"),
     ],
     "Revenue calculation and reconciliation relationships."),
    ("h2", "12.4 Reconciliation Semantics"),
    ("p",
     "A difference between calculated and reported Revenue is surfaced as a difference, not automatically "
     "labelled underpayment — it becomes a candidate for the Regulatory Intelligence workflow (Ch.16), where "
     "a human determines cause and any enforcement action."),
    ("h2", "12.5 Data Model"),
    ("bullets", [
        "Calculated Revenue Record — operator, period, traffic basis, applied rate/version, calculated value, unit/currency.",
        "Reported Revenue Record — operator, period, reported value, source.",
        "Reconciliation Result — difference, basis, status, linked Case if escalated.",
    ]),
    ("h2", "12.6 Security Controls"),
    ("bullets", [
        "Only authorized rate administrators may change the surcharge rate, through the Rule Service change process with effective dating (Ch.22).",
        "Historical rates are immutable once superseded, preserving past calculations exactly as they were computed.",
    ]),
    ("h2", "12.7 Failure Modes"),
    ("bullets", [
        "Rate change pending approval: calculations continue using the last approved effective rate until the new rate's effective date is confirmed.",
        "Missing Traffic for a period: Revenue for that period is marked not-calculable rather than computed from a zero/default assumption.",
    ]),
    ("h2", "12.8 Non-Functional Requirements"),
    ("bullets", [
        "Monthly Revenue calculation and reconciliation for all operators completes within the reporting window required by Regulatory Intelligence.",
    ]),
    ("h2", "12.9 Acceptance Criteria"),
    ("bullets", [
        "A surcharge rate change is demonstrably effective-dated: calculations before the change date use the old rate, after use the new rate.",
        "A reconciliation difference is demonstrably surfaced with basis/unit and does not auto-label as underpayment.",
    ]),
    ("proposed",
     "Confirm legal basis, currency/rounding convention and rate-change approval authority with NCA Revenue "
     "Assurance and Legal; the current supplied surcharge value of USD 0.19 is treated as the initial Rule Service "
     "value pending that confirmation."),
    ("trace", "NCIE-001 §Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
]

# ---------------------------------------------------------------------------
# Chapter 13 — Mobile Money Intelligence
# ---------------------------------------------------------------------------
BLOCKS[13] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Product Capability Architecture."),
    ("h2", "13.1 Scope"),
    ("p",
     "Covers approved aggregate Mobile Money monitoring only — daily sent/received volumes by operator. "
     "Subscriber-level Mobile Money data is explicitly out of scope for NCIE-002, matching the NCIE-001 "
     "product boundary."),
    ("h2", "13.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Mobile Money Adapter", "Ingests daily aggregate sent/received figures by operator (Ch.6 channels)."],
        ["Aggregate Store", "Canonical, versioned aggregate records; no subscriber-level fields exist in the schema."],
        ["Quality Service", "Flags missing days and anomalous swings without auto-correcting."],
        ["Analytics Service", "Trend and comparison views over aggregate volumes."],
    ],
     "Mobile Money Intelligence principal components."),
    ("h2", "13.3 Data Model"),
    ("bullets", [
        "Aggregate Record — operator, date, currency, sent volume, received volume, source, coverage status.",
    ]),
    ("h2", "13.4 Security Controls"),
    ("bullets", [
        "The Aggregate Store schema structurally excludes any subscriber-identifying field; this is enforced at the schema level, not merely by access policy, so no future adapter can accidentally introduce subscriber-level data without a deliberate architecture change.",
    ]),
    ("h2", "13.5 Failure Modes"),
    ("bullets", [
        "Missing day's figures: remains explicitly missing, never assumed zero, consistent with the platform-wide missing-data principle (Ch.5).",
    ]),
    ("h2", "13.6 Non-Functional Requirements"),
    ("bullets", [
        "Daily aggregate ingestion for all operators completes before the start of next-business-day review.",
    ]),
    ("h2", "13.7 Acceptance Criteria"),
    ("bullets", [
        "A schema inspection confirms no subscriber-identifying field exists anywhere in the Mobile Money data path.",
    ]),
    ("proposed",
     "Confirm source system, currency and daily cut-off time with NCA Mobile Money oversight; confirm whether "
     "any additional approved aggregate measures (e.g. transaction counts) should be added — architecture "
     "accommodates additional aggregate fields without redesign, subject to the same subscriber-level exclusion."),
    ("trace", "NCIE-001 §Product Capability Architecture."),
]

# ---------------------------------------------------------------------------
# Chapter 14 — SIM Registration Intelligence
# ---------------------------------------------------------------------------
BLOCKS[14] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance (amended); Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
    ("h2", "14.1 Scope"),
    ("p",
     "Covers protected identity/SIM registration intelligence, exception classification against configurable "
     "registration limits, and governed cross-operator identity resolution."),
    ("h2", "14.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Protected Identity Service", "Holds Ghana Card and foreign-passport-based identity references under field-level protection (Ch.4)."],
        ["Registration Store", "Canonical SIM registration counts and status per identity/operator."],
        ["Identity Resolution Service", "Performs governed cross-operator identity matching under heightened audit (Ch.23, Ch.26)."],
        ["Rule Engine", "Applies effective-dated registration-limit rules (current supplied limits: 10 for Ghana Card, 3 for foreign passport)."],
    ],
     "SIM Registration Intelligence principal components."),
    ("h2", "14.3 Exception Semantics"),
    ("p",
     "An identity exceeding the effective registration limit is classified as an exception, not automatically as "
     "fraud. Exceptions become candidates for the Regulatory Intelligence workflow (Ch.16), where investigation "
     "determines cause (e.g. legitimate multi-line business use) before any enforcement consideration."),
    ("h2", "14.4 Data Model"),
    ("bullets", [
        "Protected Identity — document class (Ghana Card / foreign passport), protected reference, never displayed in plaintext outside authorized protected-identity views.",
        "Registration Record — identity reference, operator, SIM count, status.",
        "Registration Limit Rule — document class, limit value, effective date range (Ch.22).",
    ]),
    ("h2", "14.5 Security Controls"),
    ("bullets", [
        "Protected identifiers are field-level access-controlled (Ch.4) and never appear in aggregate or Situational Awareness views by default.",
        "Cross-operator identity resolution actions are individually audited (Ch.23), given their sensitivity.",
        "Access to protected identity fields requires MFA and is logged with heightened detail (Ch.26).",
    ]),
    ("h2", "14.6 Failure Modes"),
    ("bullets", [
        "Ambiguous identity match across operators: presented for human confirmation rather than auto-merged.",
    ]),
    ("h2", "14.7 Non-Functional Requirements"),
    ("bullets", [
        "Registration-limit exception detection runs on each registration-data refresh cycle without manual triggering.",
    ]),
    ("h2", "14.8 Acceptance Criteria"),
    ("bullets", [
        "An identity exceeding the effective limit is demonstrably classified as an exception, and not labelled fraud, pending investigation.",
        "A registration-limit rule change is demonstrably effective-dated, consistent with §12.3's approach to the surcharge rate.",
    ]),
    ("proposed",
     "The current supplied limits of 10 (Ghana Card) and 3 (foreign passport) are treated as the initial Rule "
     "Service values; confirm final limits and rule-change authority with NCA registration-policy leadership."),
    ("proposed",
     "Confirm exact field-level protection scope (which roles may view protected identifiers unmasked) with NCA "
     "data-protection/legal leadership before production."),
    ("trace", "NCIE-001 §Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance; §Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
]

# ---------------------------------------------------------------------------
# Chapter 15 — Anti-Fraud / SIMBOX Intelligence
# ---------------------------------------------------------------------------
BLOCKS[15] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression (amended)."),
    ("h2", "15.1 Scope"),
    ("p",
     "Covers the broader Anti-Fraud domain: detection, suspicion, investigation, validation, blocking, "
     "location, referral and outcome, kept as explicitly distinct stages."),
    ("h2", "15.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Anti-Fraud Service", "Ingests and correlates detection signals into suspicion candidates."],
        ["Investigation Workflow", "Governs progression from suspicion through investigation to validated finding."],
        ["Location Service", "Resolves suspected SIMBOX activity to physical/network location under sensitive-join controls."],
        ["Blocking Workflow", "Executes approved blocking actions only after validation and authorization."],
        ["Evidence Links", "Binds every stage to authoritative Evidence objects (Ch.23)."],
    ],
     "Anti-Fraud / SIMBOX Intelligence principal components."),
    ("h2", "15.3 Stage Model"),
    ("flow",
     [
        "Detection (automated signal)",
        "Suspicion (analyst-reviewed candidate)",
        "Investigation (evidence gathering, sensitive joins under audit)",
        "Validation (human-confirmed finding)",
        "Blocking (approved, verified action)",
        "Location & Referral (where applicable)",
        "Outcome (apprehension status — authoritative source only)",
     ],
     "Anti-Fraud / SIMBOX stage progression, each stage explicit and auditable."),
    ("h2", "15.4 Data Model"),
    ("bullets", [
        "Suspicion Candidate — detection signals, confidence indicators, linked identities/cells.",
        "Investigation — assigned investigator, evidence links, sensitive-join log.",
        "Blocking Action — target, authorization reference, execution status, verification result.",
        "Outcome Record — apprehension status sourced only from the authoritative law-enforcement/regulatory system of record, never inferred by NCIE.",
    ]),
    ("h2", "15.5 Security Controls"),
    ("bullets", [
        "Sensitive joins (e.g. identity-to-location) are individually authorized and logged, not a standing capability of the investigator role.",
        "Blocking actions require both validation and separate authorization approval before execution (separation of duties, Ch.4).",
        "Blocking is never treated as an admission of guilt; outcome/apprehension status is sourced only from the authoritative system, never asserted by NCIE.",
    ]),
    ("h2", "15.6 Failure Modes"),
    ("bullets", [
        "Blocking execution fails at the provider: Blocking Workflow retries under idempotency control and surfaces failure rather than silently reporting success.",
    ]),
    ("h2", "15.7 Non-Functional Requirements"),
    ("bullets", [
        "Detection-to-suspicion candidate generation completes within the near-real-time window required for SIMBOX response effectiveness (target confirmed with NCA Anti-Fraud, Ch.30).",
    ]),
    ("h2", "15.8 Acceptance Criteria"),
    ("bullets", [
        "Each of the six stages in §15.3 is demonstrably distinct and independently auditable for a representative case.",
        "A blocking action is demonstrably blocked from execution without both validation and authorization present.",
    ]),
    ("proposed",
     "Confirm which Anti-Fraud modules and blocking interfaces are required at launch, and the investigation-stage "
     "approval matrix, with NCA Anti-Fraud/SIMBOX leadership."),
    ("trace", "NCIE-001 §Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
]

# ---------------------------------------------------------------------------
# Chapter 16 — Regulatory Intelligence, Cases, Findings & Decisions
# ---------------------------------------------------------------------------
BLOCKS[16] = [
    ("status", "Full production content. Traces to NCIE-001 v1.2 Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
    ("h2", "16.1 Scope"),
    ("p",
     "Defines regulatory case workflow and governs reuse of NCA's existing Regulatory Intelligence platform "
     "rather than rebuilding case management from scratch."),
    ("h2", "16.2 Principal Components"),
    ("table",
     ["Component", "Responsibility"],
     [
        ["Case Service", "Opens and tracks Cases from Exceptions/Candidates across all domains (Traffic, Revenue, MoMo, SIM, Anti-Fraud, Network)."],
        ["Finding Workflow", "Manages Proposed Finding to Validated Finding progression, with AI preparing but never validating."],
        ["Decision Service", "Records human/institutional Decisions against Validated Findings, including appeal/reversal history."],
        ["Evidence Binder", "Aggregates all Evidence objects (Ch.23) supporting a Case into a defensible package."],
        ["Existing Platform Adapter", "Integration boundary with NCA's existing Regulatory Intelligence platform (Ch.25)."],
    ],
     "Regulatory Intelligence, Cases, Findings & Decisions principal components."),
    ("h2", "16.3 Case Lifecycle"),
    ("flow",
     [
        "Exception / Candidate (from any domain)",
        "Case opened, linked to Evidence Binder",
        "Proposed Finding (AI may assist, never validates)",
        "Validated Finding (human-confirmed)",
        "Decision (institutional authority)",
        "Appeal / Reversal (preserves full history, never overwrites)",
     ],
     "Regulatory Case lifecycle from exception to decision."),
    ("h2", "16.4 Data Model"),
    ("bullets", [
        "Case — originating domain/exception, status, linked evidence, assigned officer(s).",
        "Proposed Finding — drafted content, AI-attribution flag where applicable, supporting evidence references.",
        "Validated Finding — human validator identity, validation date, immutable content.",
        "Decision — decision content, authority, date, appeal/reversal linkage preserving prior state.",
    ]),
    ("h2", "16.5 Security Controls"),
    ("bullets", [
        "The role proposing a Finding is distinct from the role validating it (separation of duties, Ch.4).",
        "AI-assisted content in a Proposed Finding is explicitly attributed and never silently merged into human-authored text (Ch.23, Ch.24).",
        "An appeal or reversal preserves the original Decision and Finding history rather than deleting or overwriting it.",
    ]),
    ("h2", "16.6 Failure Modes"),
    ("bullets", [
        "Existing Regulatory Intelligence platform unreachable: new Case creation queues locally with Evidence intact; no evidence is lost pending reconnection (Ch.28)."],
    ),
    ("h2", "16.7 Non-Functional Requirements"),
    ("bullets", [
        "Case and Evidence Binder assembly for a typical case completes within seconds, independent of the number of linked evidence items up to the platform's stated capacity target (Ch.30)."],
    ),
    ("h2", "16.8 Acceptance Criteria"),
    ("bullets", [
        "A Case is demonstrably blocked from reaching Validated Finding status without a distinct validator from the proposer.",
        "An appealed Decision is demonstrably shown with full prior history intact.",
    ]),
    ("proposed",
     "Confirm the precise integration contract (API vs data-sync) with NCA's existing Regulatory Intelligence "
     "platform, and confirm case-lifecycle stage names/approval roles, with the Regulatory Intelligence platform "
     "owner."),
    ("trace", "NCIE-001 §Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression."),
]
