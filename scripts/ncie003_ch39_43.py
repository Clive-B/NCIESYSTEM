"""NCIE-003 content batch: Chapters 39-43 (Data Dictionary, ER Catalogue,
Traceability Crosswalk, Open Decisions Register, Acceptance & Handover)."""

from ncie003_ch42_register import REGISTER, sorted_register

BLOCKS = {}

SDR = "SOURCE DISCOVERY REQUIRED"

# ---------------------------------------------------------------------------
# Chapter 39 — Canonical Data Dictionary
# ---------------------------------------------------------------------------
BLOCKS[39] = [
    ("h2", "39.1 Purpose"),
    ("p",
     "Holds the authoritative Data Dictionary structure (Chapter 30) and representative, fully "
     "worked canonical entities demonstrating exactly how the complete dictionary must eventually be "
     "populated. Per the authoritative handover instructions, this chapter does not fabricate the "
     "production field-level dictionary before NCA data discovery — it builds the complete "
     "architecture and structure now, and worked examples across every mandated domain, while "
     "marking unknown source-system mappings SOURCE DISCOVERY REQUIRED rather than inventing them."),
    ("h2", "39.2 How to Read a Worked Entity"),
    ("p",
     "Each worked entity below shows: an entity card (business name, technical name, definition, "
     "owning chapter, classification, owner) and an attribute table (Attribute, Definition, Data "
     "Type, Nullable, Classification, Source Mapping). Source Mapping is populated only where "
     "NCIE-001/002/003 already fixes it (e.g. a governed enumeration or an internally computed "
     "field); every attribute whose value would depend on inspecting an actual NCA/operator system "
     "is marked SOURCE DISCOVERY REQUIRED. Canonical NCIE Field and Source-System Field Mapping "
     "(Ch.30 §30.4) are always kept visually distinct."),
    ("h3", "39.3 Shared/Core — Operator"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier (Ch.4).", "Identifier", "No", "Internal", "Internally assigned"],
        ["name", "Operator's registered trading name.", "String", "No", "Internal", SDR],
        ["licence_reference", "Reference to the operator's NCA licence record.", "String", "Yes (Unknown, Ch.2)", "Internal", SDR],
        ["status", "Active / suspended / revoked.", "Enumeration", "No", "Internal", "Governed enumeration (Ch.24)"],
     ],
     "Worked entity: Operator (Shared/Core)."),
    ("h3", "39.4 Network — PM Observation"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["cell_reference", "Canonical Cell (Ch.7) this observation belongs to.", "Reference", "No", "Internal", "Resolved via Topology Service (Ch.8)"],
        ["kpi_reference", "Governed KPI definition (Ch.24).", "Reference", "No", "Internal", "Governed reference data"],
        ["period", "Observation interval.", "Temporal range", "No", "Internal", SDR],
        ["value", "Measured KPI value.", "Decimal", "Yes (Unknown, Ch.2)", "Internal", SDR],
        ["coverage_status", "Green/Amber/Grey per Ch.6 §6.9.", "Enumeration", "No", "Internal", "Computed by NCIE, not source-supplied"],
    ],
     "Worked entity: PM Observation (Network)."),
    ("h3", "39.5 Traffic — Traffic Observation"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["operator_reference", "Canonical Operator.", "Reference", "No", "Internal", "Resolved via Ch.4"],
        ["traffic_type", "International / Off-Net / On-Net.", "Enumeration", "No", "Internal", "Governed enumeration (Ch.24)"],
        ["direction", "Incoming/outgoing where applicable.", "Enumeration", "Yes (Unknown, Ch.2)", "Internal", SDR],
        ["period", "Reporting interval.", "Temporal range", "No", "Internal", SDR],
        ["volume", "Traffic volume.", "Decimal", "Yes (Unknown, Ch.2)", "Internal", SDR],
        ["unit", "Unit of measure.", "Enumeration", "No", "Internal", SDR],
    ],
     "Worked entity: Traffic Observation (Traffic)."),
    ("h3", "39.6 Revenue — Revenue Calculation"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["operator_reference", "Canonical Operator.", "Reference", "No", "Internal", "Resolved via Ch.4"],
        ["period", "Calculation period.", "Temporal range", "No", "Internal", "Derived from Traffic Input References"],
        ["traffic_input_references", "Exact Traffic Observation version(s) used.", "Reference list", "No", "Internal", "Internally computed, immutable pointer (Ch.5 §5.6)"],
        ["surcharge_rule_version", "Effective Rule Version applied (Ch.24).", "Reference", "No", "Internal", "Internally resolved from Rule Service"],
        ["calculated_value", "Deterministically calculated Revenue.", "Decimal (currency)", "No", "Internal", "Internally computed — never source-supplied"],
        ["currency", "Currency of calculated_value.", "Enumeration", "No", "Internal", SDR],
    ],
     "Worked entity: Revenue Calculation (Revenue) — note the surcharge rate itself is never a literal field here; it is looked up via surcharge_rule_version (Ch.24 §24.2)."),
    ("h3", "39.7 Mobile Money — Mobile Money Aggregate"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["operator_service_reference", "Canonical Operator/Service.", "Reference", "No", "Internal", "Resolved via Ch.4"],
        ["reporting_date", "Aggregate date.", "Date", "No", "Internal", SDR],
        ["sent_amount", "Aggregate sent value.", "Decimal (currency)", "Yes (Unknown, Ch.2)", "Internal", SDR],
        ["received_amount", "Aggregate received value.", "Decimal (currency)", "Yes (Unknown, Ch.2)", "Internal", SDR],
        ["currency", "Currency of sent/received amounts.", "Enumeration", "No", "Internal", SDR],
    ],
     "Worked entity: Mobile Money Aggregate — no subscriber-level field exists in this schema by design (Ch.13 §13.4)."),
    ("h3", "39.8 SIM Registration — Registration"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["sim_reference", "Canonical SIM.", "Reference", "No", "Internal", SDR],
        ["protected_identity_reference", "Protected identity (Ch.4/Ch.14) — value itself lives in the field-level-protected entity, never inline here.", "Reference", "No", "Protected", SDR],
        ["identity_type", "Ghana Card / Passport.", "Enumeration", "No", "Internal", "Governed enumeration"],
        ["status", "Registration status.", "Enumeration", "No", "Internal", SDR],
        ["effective_date", "Registration effective date.", "Date", "No", "Internal", SDR],
    ],
     "Worked entity: Registration (SIM Registration)."),
    ("h3", "39.9 Anti-Fraud/SIMBOX — SIMBOX Detection"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["detection_signal_type", "Type of automated signal.", "Enumeration", "No", "Sensitive", SDR],
        ["confidence", "Detection confidence score.", "Decimal", "Yes (Unknown, Ch.2)", "Sensitive", SDR],
        ["detected_time", "When the signal was generated.", "Timestamp", "No", "Sensitive", SDR],
        ["source_reference", "Originating Source (Ch.6).", "Reference", "No", "Sensitive", "Resolved via Ch.6"],
    ],
     "Worked entity: SIMBOX Detection (Anti-Fraud/SIMBOX) — a Detection alone never asserts Confirmed Fraud (Ch.15 §15.2)."),
    ("h3", "39.10 Evidence — Evidence Object"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Varies (inherits content classification)", "Internally assigned"],
        ["source_reference", "Originating Source Object Reference (Ch.6).", "Reference", "Yes (deliberately registered, Ch.17 §17.2)", "Varies", "Resolved via Ch.6"],
        ["status", "Active / invalidated.", "Enumeration", "No", "Varies", "Internally managed"],
        ["hash_value", "Integrity hash of the Evidence Artifact.", "String (hash)", "No", "Varies", "Internally computed"],
        ["classification_tier", "Ch.31 classification tier.", "Enumeration", "No", "Varies", "Assigned per Ch.31 rules"],
    ],
     "Worked entity: Evidence Object (Evidence)."),
    ("h3", "39.11 REWS/Situation — Alert"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["condition_reference", "Triggering Condition (Ch.18).", "Reference", "No", "Internal", "Internally computed"],
        ["alert_rule_reference", "Effective Alert Rule version (Ch.24).", "Reference", "No", "Internal", "Internally resolved"],
        ["severity", "Alert severity.", "Enumeration", "No", "Internal", "Governed enumeration, effective-dated"],
        ["raised_time", "When the Alert was raised.", "Timestamp", "No", "Internal", "Internally computed"],
    ],
     "Worked entity: Alert (REWS/Situation)."),
    ("h3", "39.12 ARGUS — ARGUS Contribution"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Varies (inherits referenced Evidence classification)", "Internally assigned"],
        ["interaction_reference", "Parent ARGUS Interaction.", "Reference", "No", "Varies", "Internally recorded"],
        ["contribution_type", "Question/Challenge/Hypothesis/Contradiction/Evidence Gap.", "Enumeration", "No", "Varies", "Governed enumeration (Ch.20 §20.3)"],
        ["ai_origin_marker", "Always true for this entity — retained even after human modification (Ch.20 §20.4).", "Boolean", "No", "Varies", "Internally set, immutable"],
        ["evidence_references", "Cited Evidence Objects (Ch.17) — citation only, not promotion to Evidence.", "Reference list", "Yes", "Varies", "Internally recorded"],
        ["model_route_version", "Model/provider and version used (Ch.24).", "Reference", "No (where governance requires audit)", "Internal", "Internally recorded from Model Gateway"],
     ],
     "Worked entity: ARGUS Contribution (ARGUS) — no field for private model chain-of-thought exists anywhere in this entity (Ch.20 §20.2)."),
    ("h3", "39.13 Collaborative Intelligence — Hypothesis"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Varies (Room classification, Ch.31)", "Internally assigned"],
        ["thread_reference", "Parent Thread (Ch.21) — prevents cross-thread contamination.", "Reference", "No", "Varies", "Internally recorded"],
        ["originator", "Human user or ARGUS (Ch.20) — permanently retained.", "Reference", "No", "Varies", "Internally recorded, immutable"],
        ["content", "Hypothesis text.", "Text", "No", "Varies", "Internally recorded"],
        ["supporting_evidence_references", "Ch.17 Evidence Objects supporting this hypothesis.", "Reference list", "Yes", "Varies", "Internally recorded"],
        ["status", "Active/adopted/deferred/rejected.", "Enumeration", "No", "Varies", "Internally managed"],
    ],
     "Worked entity: Hypothesis (Collaborative Intelligence) — never itself a Finding (Ch.21 §21.2)."),
    ("h3", "39.14 Memory/Institutional Knowledge — Institutional Knowledge"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Varies (Applicability Scope-derived)", "Internally assigned"],
        ["knowledge_candidate_reference", "Source Knowledge Candidate that was promoted.", "Reference", "No", "Varies", "Internally recorded"],
        ["content", "Institutional Knowledge content.", "Text", "No", "Varies", "Internally recorded"],
        ["applicability_scope", "Domain/geography/time window this applies to.", "Structured", "No", "Varies", "Internally recorded"],
        ["review_state", "Reviewer, decision, timestamp — proves human promotion (Ch.22 §22.4).", "Structured", "No", "Varies", "Internally recorded"],
    ],
     "Worked entity: Institutional Knowledge (Memory/Institutional Knowledge) — never itself a Rule (Ch.22 §22.2)."),
    ("h3", "39.15 Workflow — Workflow Instance"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["workflow_definition_reference", "Which workflow template this instantiates.", "Reference", "No", "Internal", "Internally recorded"],
        ["originator", "Human, Room (Ch.21) or schedule that requested it.", "Reference", "No", "Internal", "Internally recorded"],
        ["state", "Requested/Approved/Executed/Verified/Failed/Reconciling.", "Enumeration", "No", "Internal", "Governed enumeration (Ch.23 §23.2)"],
    ],
     "Worked entity: Workflow Instance (Workflow)."),
    ("h3", "39.16 Rules — Rule Version"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["rule_reference", "Parent Rule (rule key, e.g. international-surcharge).", "Reference", "No", "Internal", "Internally defined"],
        ["parameters", "Named Parameter values (e.g. rate, currency, or limit and identity type).", "Structured", "No", "Internal", "Institutionally confirmed values (Ch.24 §24.9 review)"],
        ["effective_from", "Effective start date.", "Date", "No", "Internal", "Institutionally confirmed"],
        ["effective_to", "Effective end date (nullable for open-ended).", "Date", "Yes", "Internal", "Institutionally confirmed"],
        ["approval_state", "Approving actor and timestamp.", "Structured", "No", "Internal", "Internally recorded (Ch.26 actor)"],
    ],
     "Worked entity: Rule Version (Rules) — this is where the surcharge rate/SIM limits actually live; no other entity in this dictionary stores them."),
    ("h3", "39.17 Audit — Audit Event"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal (append-only)", "Internally assigned"],
        ["actor_reference", "User or Service Identity (Ch.26) — one of four distinguishable classes.", "Reference", "No", "Internal", "Internally recorded"],
        ["target_reference", "Object acted upon.", "Reference", "No", "Internal", "Internally recorded"],
        ["action", "Read/reveal/export/create/modify/approve/execute/delete.", "Enumeration", "No", "Internal", "Governed enumeration"],
        ["sensitive_access_marker", "Whether this is a heightened-audit event (Ch.27 §27.4).", "Boolean", "No", "Internal", "Internally computed from action/target classification"],
    ],
     "Worked entity: Audit Event (Audit)."),
    ("h3", "39.18 Agent & VPF — Agent Definition (v0.4)"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier (Ch.4).", "Identifier", "No", "Internal", "Internally assigned"],
        ["version", "Effective-dated version of this definition (Ch.3 §2.8).", "Integer", "No", "Internal", "Internally managed"],
        ["purpose", "Governed capability purpose.", "Text", "No", "Internal", "Institutionally confirmed"],
        ["capability_scope", "Bounded task scope.", "Structured", "No", "Internal", "Institutionally confirmed"],
        ["authorization_ceiling_reference", "Ceiling reference only (Ch.26 §26.6) — never itself a grant.", "Reference", "No", "Internal", "Resolved via Ch.26"],
        ["vpf_profile_requirement", "Required VPF Profile reference (§39.21).", "Reference", "No", "Internal", "Resolved via Ch.3 §3.9"],
     ],
     "Worked entity: Agent Definition (Agent & VPF) — AGENT DEFINITION ≠ AGENT RUN (Ch.3 §3.9)."),
    ("h3", "39.19 Agent & VPF — Task Contract (v0.4)"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["agent_definition_reference", "The reusable definition this run-specific contract binds to.", "Reference", "No", "Internal", "Internally recorded"],
        ["effective_principal", "Current authorization context reference (Ch.26 §26.6).", "Reference", "No", "Internal", "Resolved via Ch.26"],
        ["requested_outcome", "Expected result.", "Text", "No", "Internal", "Internally recorded"],
        ["resource_limits", "Bounded resource ceiling for this run.", "Structured", "No", "Internal", SDR],
     ],
     "Worked entity: Task Contract (Agent & VPF) — a reusable Agent Definition never eliminates the need for this run-specific contract."),
    ("h3", "39.20 Agent & VPF — Agent Run (v0.4)"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["agent_definition_reference", "Definition executed.", "Reference", "No", "Internal", "Internally recorded"],
        ["task_contract_reference", "Governing Task Contract.", "Reference", "No", "Internal", "Internally recorded"],
        ["runtime_identity_reference", "Distinct runtime identity (Ch.26 §26.5).", "Reference", "No", "Internal", "Internally assigned"],
        ["lifecycle_state", "Governed execution state (Ch.3 §3.9.2).", "Enumeration", "No", "Internal", "Governed enumeration"],
        ["result_package_reference", "Produced Agent Result Package (§39.21) where completed.", "Reference", "Yes", "Internal", "Internally recorded"],
     ],
     "Worked entity: Agent Run (Agent & VPF) — AGENT DEFINITION ≠ AGENT RUN."),
    ("h3", "39.21 Agent & VPF — Agent Result Package (v0.4)"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Varies (inherits referenced Evidence/context classification)", "Internally assigned"],
        ["agent_run_reference", "Producing Agent Run.", "Reference", "No", "Varies", "Internally recorded"],
        ["structured_ai_output", "The pre-VPF structured output.", "Structured", "No", "Varies", "Internally recorded"],
        ["execution_status", "Completed/failed/degraded.", "Enumeration", "No", "Varies", "Internally managed"],
        ["vpf_validation_reference", "Resulting VPF Validation Artifact (§39.22) once validated.", "Reference", "Yes (Unknown until validated)", "Varies", "Internally recorded"],
     ],
     "Worked entity: Agent Result Package (Agent & VPF) — AGENT RESULT PACKAGE ≠ VALIDATED AI RESULT."),
    ("h3", "39.22 Agent & VPF — VPF Profile (v0.4)"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Internal", "Internally assigned"],
        ["version", "Effective-dated profile version.", "Integer", "No", "Internal", "Internally managed"],
        ["applicable_output_class", "Governed output class this profile applies to (NCIE-007 v1.1 Ch.26 §26.5).", "Reference", "No", "Internal", "Resolved via NCIE-007 output-class registry"],
        ["validation_dimensions", "Mandatory validation dimensions for this profile.", "Structured", "No", "Internal", "Institutionally confirmed"],
        ["lifecycle_state", "Draft/active/retired.", "Enumeration", "No", "Internal", "Governed enumeration"],
     ],
     "Worked entity: VPF Profile (Agent & VPF) — no physical validator technology is implied by this entity."),
    ("h3", "39.23 Agent & VPF — VPF Validation Artifact (v0.4)"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Varies (inherits validated-artifact classification)", "Internally assigned"],
        ["input_artifact_reference", "Exact Agent Result Package/AI artifact validated.", "Reference", "No", "Varies", "Internally recorded"],
        ["vpf_profile_version_reference", "Profile version applied.", "Reference", "No", "Varies", "Internally recorded"],
        ["validation_time", "When validation occurred.", "Timestamp", "No", "Varies", "Internally recorded"],
        ["disposition", "PASS/QUALIFIED/REJECT/HUMAN_REVIEW_REQUIRED/VALIDATION_UNAVAILABLE/REVALIDATION_REQUIRED/INVALIDATED (Ch.3 §3.9.1).", "Enumeration", "No", "Varies", "Governed enumeration"],
        ["qualification_reasons", "Reasons where QUALIFIED/REJECT.", "Text", "Yes", "Varies", "Internally recorded"],
     ],
     "Worked entity: VPF Validation Artifact (Agent & VPF) — VPF VALIDATION ARTIFACT ≠ HUMAN APPROVAL; a later revalidation creates a new related artifact (Ch.25 §25.7), never overwriting this one."),
    ("h3", "39.24 Agent & VPF — Promotion Candidate (v0.4)"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Varies (inherits underlying Agent Run/evaluation classification)", "Internally assigned"],
        ["originating_agent_definition_reference", "Ephemeral Agent Definition proposed for promotion.", "Reference", "No", "Varies", "Internally recorded"],
        ["evaluation_history_reference", "Linked evaluation/VPF history.", "Reference list", "No", "Varies", "Internally recorded"],
        ["proposed_scope", "Proposed reusable scope.", "Text", "No", "Varies", "Institutionally confirmed"],
        ["lifecycle_state", "Proposed/under review/approved/rejected.", "Enumeration", "No", "Varies", "Governed enumeration"],
     ],
     "Worked entity: Promotion Candidate (Agent & VPF) — PROMOTION CANDIDATE ≠ REGISTERED AGENT; this record is not itself the human/governance approval."),
    ("h3", "39.25 Agent & VPF — Engineering Change Candidate (v0.4)"),
    ("table",
     ["Attribute", "Definition", "Data Type", "Nullable", "Classification", "Source Mapping"],
     [
        ["canonical_id", "Stable NCIE canonical identifier.", "Identifier", "No", "Varies (may expose capability gaps or security architecture)", "Internally assigned"],
        ["originating_task_reference", "Task/capability gap that produced this candidate.", "Reference", "No", "Varies", "Internally recorded"],
        ["required_capability", "The missing primitive required.", "Text", "No", "Varies", "Internally recorded"],
        ["engineering_disposition", "Open/routed/accepted/deferred.", "Enumeration", "No", "Varies", "Institutionally managed"],
     ],
     "Worked entity: Engineering Change Candidate (Agent & VPF) — ENGINEERING CHANGE CANDIDATE ≠ IMPLEMENTED CAPABILITY; this record does not itself authorize expenditure, procurement, development or deployment."),
    ("trace002", "Consolidates worked examples for entities defined in Ch.3-Ch.30 of this document, which in turn trace individually to their respective NCIE-002 chapters. (v0.4) §39.18-§39.25 additionally trace to approved NCIE-001 v1.3 §12.80A, approved NCIE-002 v0.5 Ch.24 §24.4A and approved NCIE-007 v1.1."),
    ("review", [
        ("SOURCE_DISCOVERY", "Every attribute marked SOURCE DISCOVERY REQUIRED above requires actual NCA/operator system inspection before NCIE-004 implementation begins."),
        ("INSTITUTIONAL", "Confirm which additional entities beyond these 23 representative examples require full worked treatment before NCIE-003 is considered dictionary-complete."),
    ]),
    ("h2", "39.26 Acceptance Criteria"),
    ("bullets", [
        "Every one of the 15 mandated domains has at least one fully worked entity per §39.3-§39.17.",
        "No worked entity above contains a fabricated Source-System Field Mapping value; every unknown mapping reads SOURCE DISCOVERY REQUIRED.",
        "(v0.4) Each of the 8 new Agent & VPF worked entities in §39.18-§39.25 is present, uses SOURCE DISCOVERY REQUIRED where source mapping is genuinely unknown, and fabricates no physical table name, database type, source-system field or retention period.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 40 — Entity Relationship Catalogue & Reference Diagrams
# ---------------------------------------------------------------------------
BLOCKS[40] = [
    ("h2", "40.1 Purpose"),
    ("p",
     "Provides authoritative conceptual and logical ER diagrams and relationship catalogues that "
     "agree with Chapter 39's Data Dictionary. Per the hybrid principle, logical canonical ER models "
     "are produced now, since NCIE-001/002 already establish enough conceptual architecture; physical "
     "table structures, database-specific keys, indexes and partitioning are explicitly out of scope "
     "here and belong to Chapter 32 and NCIE-014."),
    ("h2", "40.2 Model-Level Convention"),
    ("p",
     "Every diagram below is explicitly a Logical Canonical Model (Ch.32 §32.2): it shows entities "
     "and relationships with cardinality intent, independent of storage technology. None of these "
     "diagrams is a Physical Implementation Model — no diagram implies a specific table, key or index "
     "structure."),
    ("h3", "40.3 Enterprise Core ERD"),
    ("rel",
     [
        ("Operator", "is referenced by", "Cell, Traffic Observation, Revenue Calculation, Registration"),
        ("Geography", "is referenced by", "Cell, Incident, Campaign, Condition"),
        ("Canonical ID (Ch.4)", "underlies identity of", "every entity in this catalogue"),
        ("Evidence Object", "is referenced by", "Finding, Hypothesis, ARGUS Contribution, Graph Edge"),
     ],
     "Enterprise Core logical ERD — shared/core entities referenced across domains."),
    ("h3", "40.4 Network ERD"),
    ("rel",
     [
        ("Operator", "has", "Site"),
        ("Site", "has", "Cell"),
        ("Cell", "has many", "PM Observation"),
        ("PM Observation", "is compared to", "Baseline / Threshold"),
        ("Degradation pattern", "raises", "Network Condition"),
     ],
     "Network logical ERD."),
    ("h3", "40.5 Traffic ERD"),
    ("rel",
     [
        ("Operator", "has many", "Traffic Observation"),
        ("Traffic Observation", "may have", "Revision (Correction relationship, Ch.25)"),
        ("Traffic Observation", "is input to", "Revenue Calculation"),
     ],
     "Traffic logical ERD."),
    ("h3", "40.6 Revenue ERD"),
    ("rel",
     [
        ("Traffic Observation", "feeds", "Revenue Calculation"),
        ("Rule Version (surcharge)", "governs", "Revenue Calculation"),
        ("Revenue Calculation", "is compared in", "Reconciliation"),
        ("Billing Verification", "is compared in", "Reconciliation"),
        ("Reconciliation", "may produce", "Reconciliation Difference"),
     ],
     "Revenue logical ERD."),
    ("h3", "40.7 Mobile Money ERD"),
    ("rel",
     [
        ("Operator/Service", "has many", "Mobile Money Aggregate"),
        ("Mobile Money Aggregate", "is correlated by", "Cross-Domain Fusion (Ch.19)"),
     ],
     "Mobile Money logical ERD (deliberately minimal, no subscriber-level entity)."),
    ("h3", "40.8 SIM Registration ERD"),
    ("rel",
     [
        ("Protected Identity Reference", "has many", "Registration"),
        ("Registration", "is evaluated for Countable State against", "Registration Rule (Ch.24)"),
        ("Count over limit", "raises", "Registration Exception"),
        ("Registration Exception", "may become", "Case (Ch.16)"),
     ],
     "SIM Registration logical ERD."),
    ("h3", "40.9 Anti-Fraud / SIMBOX ERD"),
    ("rel",
     [
        ("SIMBOX Detection", "identifies", "Suspected SIM"),
        ("Suspected SIM", "is examined in", "Investigation"),
        ("Investigation", "may gather", "Location Evidence (under Tracking Authorization)"),
        ("Investigation", "may raise", "Blocking Request"),
        ("Blocking Request", "leads to", "Blocking Action / Blocking Verification"),
     ],
     "Anti-Fraud / SIMBOX logical ERD."),
    ("h3", "40.10 Evidence / Investigation ERD"),
    ("rel",
     [
        ("Source Object Reference", "may be registered as", "Evidence Object"),
        ("Evidence Object", "has", "Hash/Integrity Metadata"),
        ("Evidence Object", "supports or contradicts", "Hypothesis / Finding"),
        ("Evidence Object", "may have", "Correction (new version) or Invalidation"),
     ],
     "Evidence / Investigation logical ERD."),
    ("h3", "40.11 REWS / Situation / NOP ERD"),
    ("rel",
     [
        ("Observation/Condition", "raises", "Alert"),
        ("Alert", "has", "Acknowledgement / Escalation"),
        ("related Alerts/Incidents/Evidence", "are grouped into", "Situation"),
        ("current status across domains", "composes", "NOP Projection"),
     ],
     "REWS / Situation / National Operating Picture logical ERD."),
    ("h3", "40.12 ARGUS / Collaborative Intelligence ERD"),
    ("rel",
     [
        ("ARGUS Interaction", "produces", "ARGUS Contribution"),
        ("ARGUS Contribution", "cites", "Evidence Object (never becomes one)"),
        ("Collaborative Room", "has", "Thread"),
        ("Thread", "has", "Hypothesis, Contradiction, Evidence Gap, Task"),
        ("Room", "captures", "Room Snapshot"),
     ],
     "ARGUS / Collaborative Intelligence logical ERD."),
    ("h3", "40.13 Memory / Institutional Knowledge ERD"),
    ("rel",
     [
        ("Memory Object", "may generalise to", "Knowledge Candidate"),
        ("Knowledge Candidate", "requires human Review State to become", "Institutional Knowledge"),
        ("Institutional Knowledge", "may be", "Superseded / Retracted (history retained)"),
     ],
     "Memory / Institutional Knowledge logical ERD."),
    ("h3", "40.14 Workflow / Rules ERD"),
    ("rel",
     [
        ("Workflow Instance", "requires", "Approval (distinct actor)"),
        ("Workflow Instance", "executes via", "Automation/RPA Run"),
        ("Automation/RPA Run", "produces", "Outcome (with Reconciliation if Unknown)"),
        ("Rule", "has many", "Rule Version (effective-dated)"),
     ],
     "Workflow / Rules logical ERD."),
    ("h3", "40.15 Audit / Provenance ERD"),
    ("rel",
     [
        ("Actor (Ch.26)", "performs", "Audit Event"),
        ("Audit Event", "targets", "any canonical object"),
        ("Lineage Record", "links", "derived object to originating Source Object Reference"),
        ("Correction Relationship", "flags", "Dependency Edge for Impact-Review"),
     ],
     "Audit / Provenance logical ERD."),
    ("h3", "40.15A Agent & VPF ERD (v0.4 — VPF & Dynamic Agent Synthesis Amendment)"),
    ("rel",
     [
        ("Agent Pattern", "may produce", "Agent Definition"),
        ("Agent Definition", "is executed as", "Agent Run"),
        ("Task Contract", "governs", "Agent Run"),
        ("Agent Run", "uses", "Model Route"),
        ("Agent Run", "invokes", "Tool Invocation"),
        ("Agent Run", "references", "Context / Evidence"),
        ("Agent Run", "produces", "Agent Result Package"),
        ("Agent Result Package", "is validated by", "VPF Validation Artifact"),
        ("VPF Profile Version", "governs disposition of", "VPF Validation Artifact"),
        ("Validated AI Result", "is the released form of", "VPF Validation Artifact (PASS/QUALIFIED)"),
        ("Ephemeral Agent Definition/Run history", "may produce", "Promotion Candidate"),
        ("Promotion Candidate", "requires governed review to become", "Registered Reusable Agent"),
        ("Task / Capability Gap", "may produce", "Engineering Change Candidate"),
     ],
     "Agent & VPF logical ERD — promotion always passes through Promotion Candidate → governed review, "
     "never Ephemeral Agent → automatically Registered Agent; revalidation always produces a new, "
     "related VPF Validation Artifact rather than overwriting the original."),
    ("h2", "40.16 Diagram-Dictionary Agreement"),
    ("p",
     "No diagram in this chapter introduces an entity absent from Chapter 3's family catalogue or "
     "Chapters 7-30's domain chapters; conversely, every entity family in Chapter 3 appears in at "
     "least one diagram here. This mutual coverage is a checked acceptance criterion (§40.18), not an "
     "assumption. (v0.4) §40.15A's entities all appear in Chapter 3 §3.9 and Chapter 39 §39.18-§39.25."),
    ("trace002", "Consolidates the entity/relationship structures from Ch.3-Ch.30, agreeing with NCIE-002's domain and platform architecture chapters throughout. (v0.4) §40.15A additionally implements approved NCIE-001 v1.3 §12.80A, approved NCIE-002 v0.5 Ch.24 §24.4A and approved NCIE-007 v1.1."),
    ("review", [
        ("INSTITUTIONAL", "Confirm preferred diagram notation for the eventual formal ERD deliverable (this chapter's relationship-catalogue format is a content-complete stand-in, not a specific notation standard such as Crow's Foot or IE)."),
        ("INSTITUTIONAL", "Confirm the level of detail appropriate for architectural review versus what NCIE-004/implementation will need."),
        ("SOURCE_DISCOVERY", "Validate each domain's relationships with the relevant domain users before physical implementation begins."),
    ]),
    ("h2", "40.17 Physical Model Deferral"),
    ("p",
     "Table/collection names, primary/foreign keys, indexes and partitioning are Physical "
     "Implementation Model concerns (Ch.32, Ch.35) and are deliberately not finalized in this "
     "chapter — doing so before technology selection and source discovery would let physical "
     "convenience silently redefine canonical meaning, which Chapter 32 §32.4 prohibits."),
    ("h2", "40.18 Acceptance Criteria"),
    ("bullets", [
        "Every entity family in Chapter 3 §3.3 appears in at least one ERD in this chapter.",
        "No ERD in this chapter references an entity absent from the Chapter 39 dictionary or Chapters 7-30.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 41 — Requirements Traceability & NCIE-002 Crosswalk
# ---------------------------------------------------------------------------
BLOCKS[41] = [
    ("h2", "41.1 Purpose"),
    ("p",
     "Maps every significant NCIE-003 chapter back to the NCIE-002 architecture chapter(s) that "
     "justify it, consolidating the per-chapter 'NCIE-002 Architecture Dependency & Traceability' "
     "sections that appear throughout Chapters 1-40 (per the authoritative instruction that "
     "traceability is mandatory throughout, not postponed to this chapter — this chapter consolidates "
     "rather than originates it)."),
    ("h2", "41.2 Master Crosswalk"),
    ("table",
     ["NCIE-003 Chapter", "Primary NCIE-002 Dependency"],
     [
        ["1 — Governance & Mandate", "Ch.1 §1.3.3 (evidence/provenance-first), Ch.5"],
        ["2 — Principles & Standards", "Ch.1 §1.3, Ch.5, Ch.18 §18.5, Ch.26"],
        ["3 — Enterprise Canonical Model", "Ch.5, Ch.17; (v0.4) §3.9 Agent & VPF family: approved NCIE-001 v1.3 §12.77-§12.80A, approved NCIE-002 v0.5 Ch.24 §24.4A, approved NCIE-007 v1.1 Ch.3, Ch.11, Ch.12, Ch.26"],
        ["4 — Common Entity/Identifier Model", "Ch.5 §5.2, Ch.17, Ch.19 §19.11"],
        ["5 — Temporal & Bitemporal Model", "Ch.5 §5.3, Ch.22 §22.3, Ch.23 §23.5"],
        ["6 — Source/Acquisition Model", "Ch.6 (in full)"],
        ["7 — Network Intelligence Model", "Ch.7 (in full)"],
        ["8 — Topology/GIS/Spatial Model", "Ch.8 (in full)"],
        ["9 — QoS Campaign Model", "Ch.9 (in full)"],
        ["10 — Incident Intelligence Model", "Ch.10 (in full)"],
        ["11 — Traffic Intelligence Model", "Ch.11 (in full)"],
        ["12 — Revenue/Billing Model", "Ch.12 (in full); depends on Ch.24 (this document)"],
        ["13 — Mobile Money Model", "Ch.13 (in full)"],
        ["14 — SIM Registration Model", "Ch.14 (in full); depends on Ch.4, Ch.24 (this document)"],
        ["15 — Anti-Fraud/SIMBOX Model", "Ch.15 (in full)"],
        ["16 — Regulatory Case/Finding/Decision Model", "Ch.16 (in full); depends on Ch.20, Ch.26 (this document)"],
        ["17 — Evidence Model", "Ch.23 (in full)"],
        ["18 — REWS/Alert/Situation/NOP Model", "Ch.18 (in full); depends on Ch.24 (this document)"],
        ["19 — Cross-Domain Fusion/Graph Model", "Ch.17 (in full); depends on Ch.20 (this document)"],
        ["20 — ARGUS Interaction/AI Provenance Model", "Ch.19 (in full, incl. §19.11), Ch.24 (in full); (v0.4) §20.7-§20.10: approved NCIE-002 v0.5 Ch.19 §19.2A, Ch.24 §24.4A; approved NCIE-007 v1.1 Ch.11, Ch.20, Ch.26"],
        ["21 — Collaborative Intelligence Model", "Ch.20 (in full)"],
        ["22 — Memory/Institutional Knowledge Model", "Ch.20 §20.2, §20.12"],
        ["23 — Workflow/Automation/RPA Model", "Ch.21 (in full)"],
        ["24 — Rules/Configuration/Calculation Model", "Ch.22 (in full)"],
        ["25 — Provenance/Lineage/Decision-Time Model", "Ch.23 (in full); (v0.4) §25.6-§25.7: approved NCIE-007 v1.1 Ch.27"],
        ["26 — Identity/Authorization/Security Model", "Ch.4 (in full); (v0.4) §26.5-§26.6: approved NCIE-007 v1.1 Ch.14, Ch.18, Ch.25 §25.3"],
        ["27 — Audit/Accountability Model", "Ch.23 (in full); (v0.4) §27.4 extension, §27.4A: approved NCIE-007 v1.1 Ch.27, Ch.31 §31.3"],
        ["28 — Notification/Event/Integration Model", "Ch.25 (in full)"],
        ["29 — Data Quality/Validation Model", "Ch.6 §6.9, Ch.28; (v0.4) §29.5A: approved NCIE-007 v1.1 Ch.32"],
        ["30 — Metadata Catalogue Architecture", "Operationalises Ch.2/Ch.5 across every domain chapter"],
        ["31 — Classification/Privacy/Retention", "Ch.26 (in full)"],
        ["32 — Physical Data Design", "Ch.5 (canonical/analytical platform), Ch.30 (implementation persistence, → NCIE-014)"],
        ["33 — Data API/Schema/Event Contracts", "Ch.25 (in full)"],
        ["34 — Migration/Legacy Reconciliation", "Ch.6, Ch.5 — no new architecture introduced"],
        ["35 — Performance/Partitioning/Archival", "Ch.30 (in full)"],
        ["36 — Data Security/Sovereignty", "Ch.26 (in full)"],
        ["37 — Data Observability/Reconciliation", "Ch.27 (in full)"],
        ["38 — Data Testing/Verification/Acceptance", "Ch.31 (in full)"],
        ["39 — Canonical Data Dictionary", "Consolidates Ch.3-Ch.30 of this document; (v0.4) §39.18-§39.25: approved NCIE-001 v1.3 §12.80A, approved NCIE-002 v0.5 Ch.24 §24.4A, approved NCIE-007 v1.1"],
        ["40 — ER Catalogue", "Consolidates Ch.3-Ch.30 of this document; (v0.4) §40.15A: approved NCIE-001 v1.3 §12.80A, approved NCIE-002 v0.5 Ch.24 §24.4A, approved NCIE-007 v1.1"],
    ],
     "Master crosswalk: every NCIE-003 chapter to its primary NCIE-002 architecture dependency. Current "
     "authority chain (v0.4): approved NCIE-001 v1.3, approved NCIE-002 v0.5, and detailed orchestration "
     "authority approved NCIE-007 v1.1. Rows without an explicit (v0.4) annotation are unaffected by "
     "this amendment and continue to trace to the baseline NCIE-002 v0.4 architecture that NCIE-002 "
     "v0.5 itself preserves unchanged."),
    ("h2", "41.3 Chapter 39 ↔ Chapter 40 Consistency Check"),
    ("p",
     "Per the v0.3 hardening pass, every entity named in a Chapter 39 worked entity was checked "
     "against Chapter 40's ERDs, and every entity named in a Chapter 40 ERD was checked against "
     "Chapter 39 (or, where not separately worked in Ch.39, against its owning domain chapter's "
     "Principal Entities table in Ch.7-Ch.30). No discrepancy was found."),
    ("table",
     ["Domain", "Ch.39 Worked Entity", "Ch.40 ERD", "Consistent?"],
     [
        ["Shared/Core", "Operator (§39.3)", "Enterprise Core ERD (§40.3)", "Yes"],
        ["Network", "PM Observation (§39.4)", "Network ERD (§40.4)", "Yes"],
        ["Traffic", "Traffic Observation (§39.5)", "Traffic ERD (§40.5)", "Yes"],
        ["Revenue", "Revenue Calculation (§39.6)", "Revenue ERD (§40.6)", "Yes"],
        ["Mobile Money", "Mobile Money Aggregate (§39.7)", "Mobile Money ERD (§40.7)", "Yes"],
        ["SIM Registration", "Registration (§39.8)", "SIM Registration ERD (§40.8)", "Yes"],
        ["Anti-Fraud/SIMBOX", "SIMBOX Detection (§39.9)", "Anti-Fraud/SIMBOX ERD (§40.9)", "Yes"],
        ["Evidence", "Evidence Object (§39.10)", "Evidence/Investigation ERD (§40.10)", "Yes"],
        ["REWS/Situation", "Alert (§39.11)", "REWS/Situation/NOP ERD (§40.11)", "Yes"],
        ["ARGUS", "ARGUS Contribution (§39.12)", "ARGUS/Collaborative Intelligence ERD (§40.12)", "Yes"],
        ["Collaborative Intelligence", "Hypothesis (§39.13)", "ARGUS/Collaborative Intelligence ERD (§40.12)", "Yes"],
        ["Memory/Institutional Knowledge", "Institutional Knowledge (§39.14)", "Memory/Institutional Knowledge ERD (§40.13)", "Yes"],
        ["Workflow", "Workflow Instance (§39.15)", "Workflow/Rules ERD (§40.14)", "Yes"],
        ["Rules", "Rule Version (§39.16)", "Workflow/Rules ERD (§40.14)", "Yes"],
        ["Audit", "Audit Event (§39.17)", "Audit/Provenance ERD (§40.15)", "Yes"],
     ],
     "Chapter 39 ↔ Chapter 40 consistency check across all 15 mandated domains."),
    ("p",
     "This check is re-run whenever either chapter changes; a future revision that renames or adds an "
     "entity in one chapter without a corresponding update in the other fails this check and must be "
     "corrected before that revision is approved."),
    ("h2", "41.4 Orphan Detection"),
    ("p",
     "An orphan field is one present in Chapter 39's dictionary with no traceable justification in "
     "either NCIE-001 or NCIE-002; an unrealised requirement is an NCIE-001/002 requirement with no "
     "corresponding NCIE-003 entity/field. Neither condition exists in the current chapter set at "
     "this baseline — every worked entity in Chapter 39 and every entity family in Chapter 3 "
     "originates from a cited NCIE-002 chapter in §41.2."),
    ("h2", "41.5 Stable Traceability IDs"),
    ("p",
     "This document's own stable requirement-ID scheme mirrors NCIE-001's: a chapter.section "
     "reference (e.g. NCIE-003 §14.4) is the stable ID used by Chapter 38's test cases and any future "
     "NCIE-004/implementation backlog item that needs to cite a specific NCIE-003 decision."),
    ("h2", "41.6 Upstream Impact Log"),
    ("p",
     "No UPSTREAM ARCHITECTURE IMPACT — REVIEW REQUIRED flag has been raised during this expansion; "
     "NCIE-003 has been produced entirely by implementing NCIE-002 semantically, without requiring "
     "any change to NCIE-002's architecture. This log remains open for any future expansion pass that "
     "does identify such an impact. (v0.4) This amendment likewise implements the already-approved "
     "NCIE-001 v1.3, NCIE-002 v0.5 and NCIE-007 v1.1 baselines semantically; it does not itself "
     "constitute or require a further architecture change."),
    ("h2", "41.6A Downstream Handover Register (v0.4)"),
    ("table",
     ["Downstream Document", "NCIE-003 Obligation Deferred to It"],
     [
        ["NCIE-004 (forthcoming surgical amendment)", "Engineering technology support for the Agent Factory, VPF runtime, sandbox/evaluation and Agent/VPF Registry (Ch.3 §3.9); no technology choice is pre-approved here."],
        ["NCIE-005 (forthcoming surgical amendment)", "ARGUS presentation/behavior for Dynamic Agent Synthesis, VPF status, promotion recommendation and failure presentation."],
        ["NCIE-006 (forthcoming surgical amendment)", "Memory/Context obligations for Agent Task Context, Agent Run Context, VPF artifact references, promotion history and context expiry."],
        ["NCIE-009", "Security/IAM implementation for Agent Runtime Identity and Tool Actor (Ch.26 §26.5)."],
        ["NCIE-011", "API contracts for Agent/VPF service interfaces."],
        ["NCIE-014", "Physical storage design for the Agent & VPF entity family (Ch.3 §3.9); logical relationships in Ch.40 §40.15A do not mandate any physical foreign key, join table, graph edge or index."],
        ["NCIE-015", "Deployment/infrastructure for Ephemeral Agent Runtime and sandbox isolation."],
        ["NCIE-016", "Full implementation verification/test-suite realization for the acceptance requirements defined in Ch.43."],
     ],
     "Downstream handover register — no obligation above is left ownerless."),
    ("trace002", "This chapter's entire content IS the consolidated NCIE-002 crosswalk; see §41.2. (v0.4) §41.6A additionally implements approved NCIE-007 v1.1 Ch.36 §36.4."),
    ("review", [
        ("INSTITUTIONAL", "Confirm traceability granularity required (chapter-level, as here, versus field-level for every dictionary entry)."),
        ("RESOLVED", "Authoritative current architecture baseline for this crosswalk: approved NCIE-002 System Architecture & Technical Design, Version 0.5 (VPF & Dynamic Agent Synthesis Architectural Consistency Amendment), together with approved NCIE-001 Master PRD v1.3 and approved NCIE-007 AI, Agent & Model Orchestration Specification v1.1 for Agent Factory-related data semantics — resolved by this edition's front matter §0.1; supersedes the prior resolution citing NCIE-002 v0.4 alone, which is preserved as history in front matter §0.8."),
        ("INSTITUTIONAL", "Approve the process for resolving any future orphan requirement or field, should one be discovered as the dictionary is populated with real source mappings."),
    ]),
    ("h2", "41.7 Acceptance Criteria"),
    ("bullets", [
        "Every row in §41.2 is independently verifiable against the cited NCIE-002 chapter.",
        "No orphan field or unrealised requirement is found on inspection of Chapters 3-40 against NCIE-001/002.",
        "The §41.3 consistency check passes for all 15 domains with no discrepancy.",
        "(v0.4) Every new Agent & VPF canonical object in §3.9 is traceable to an Impact ID in the approved NCIE-007 v1.1 Upstream Impact Register or a direct NCIE-007 v1.1 chapter citation; no orphan Agent/VPF object exists.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 42 — Open Institutional Decisions & Human Review Register
# ---------------------------------------------------------------------------
_sorted = sorted_register()
_open_count = sum(1 for x in REGISTER if x["status"] != "Closed")
_closed_count = sum(1 for x in REGISTER if x["status"] == "Closed")
_blocking_count = sum(1 for x in REGISTER if x["blocking"].startswith("Blocking"))
_by_cat = {}
for _x in REGISTER:
    _by_cat[_x["category"]] = _by_cat.get(_x["category"], 0) + 1

_table1_rows = [
    [x["id"], x["issue"], f"Ch.{x['chapter']}", x["category"], x["impact"], x["blocking"]]
    for x in _sorted
]
_table2_rows = [
    [x["id"], x["proposed"] or "—", x["owner"], x["evidence"], x["status"], x["decision"], x["effective"]]
    for x in _sorted
]

BLOCKS[42] = [
    ("h2", "42.1 Purpose"),
    ("p",
     f"Consolidates every Human Review Focus item from Chapters 1-41 into one complete, authoritative "
     f"register — all {len(REGISTER)} items (mechanically counted from the register at build time, "
     "never hand-typed), not a representative subset — so NCA reviewers can review every unresolved "
     "decision in one place rather than searching the full document. This corrects the v0.2 edition, "
     "whose §42.3 held only 16 representative high-priority entries while its own §42.1 "
     "and §42.6 promised full consolidation; see front matter §0.6 for the review finding that "
     "prompted this correction."),
    ("h2", "42.2 Register Structure"),
    ("table",
     ["Column", "Definition"],
     [
        ["Decision ID", "Stable reference (chapter-sequence, e.g. 14-A)."],
        ["Issue", "The open question, verbatim from its originating chapter's Human Review Focus section."],
        ["Originating Chapter/Section", "The NCIE-003 chapter where this item was raised."],
        ["Category", "RESOLVED / PROPOSED / INSTITUTIONAL / SOURCE_DISCOVERY / LEGAL, per front matter §0.4."],
        ["Impact", "Consequence if the item remains unresolved."],
        ["Blocking / Non-Blocking", "Whether the item blocks production field-level completion, regulatory/legal defensibility, or an acceptance gate, versus a governance refinement that can proceed provisionally."],
        ["Proposed Default (if any)", "The specific default already proposed for this item, where one exists."],
        ["Owner", "Proposed accountable NCA/NCIE function, pending formal assignment."],
        ["Required Evidence", "What would actually close the item — never a verbal confirmation alone."],
        ["Status", "Open / Open — proposed default standing / Closed."],
        ["Decision", "Recorded once closed; “—” while open."],
        ["Effective Date", "Recorded once closed; “—” while open."],
    ],
     "Open Institutional Decisions & Human Review Register — complete column structure."),
    ("h2", "42.3 Register Summary"),
    ("table",
     ["Metric", "Count"],
     [
        ["Total items", str(len(REGISTER))],
        ["Open", str(_open_count)],
        ["Closed (Resolved)", str(_closed_count)],
        ["Blocking", str(_blocking_count)],
        ["Non-blocking", str(len(REGISTER) - _blocking_count)],
        ["RESOLVED BY APPROVED NCIE BASELINE", str(_by_cat.get("RESOLVED", 0))],
        ["PROPOSED DESIGN DEFAULT", str(_by_cat.get("PROPOSED", 0))],
        ["INSTITUTIONAL CONFIRMATION REQUIRED", str(_by_cat.get("INSTITUTIONAL", 0))],
        ["SOURCE/DATA DISCOVERY REQUIRED", str(_by_cat.get("SOURCE_DISCOVERY", 0))],
        ["LEGAL/POLICY CONFIRMATION REQUIRED", str(_by_cat.get("LEGAL", 0))],
    ],
     "Register summary counts."),
    ("h2", "42.4 Complete Master Register — Identification & Assessment"),
    ("p",
     "Sorted Blocking items first, then by category severity (LEGAL, INSTITUTIONAL, SOURCE_DISCOVERY, "
     "PROPOSED, RESOLVED), then by chapter — so the items most likely to gate progress appear first. "
     "This table and §42.5 share the same Decision ID and are two views of one register, split for "
     "page-width readability rather than presented as a single, unreadably wide table."),
    ("table",
     ["ID", "Issue", "Ch.", "Category", "Impact", "Blocking?"],
     _table1_rows,
     f"Master register, part 1 of 2: identification and assessment, for all {len(REGISTER)} items."),
    ("h2", "42.5 Complete Master Register — Ownership & Closure"),
    ("table",
     ["ID", "Proposed Default", "Owner", "Required Evidence", "Status", "Decision", "Eff. Date"],
     _table2_rows,
     f"Master register, part 2 of 2: ownership and closure, for all {len(REGISTER)} items (same Decision IDs and order as §42.4)."),
    ("h2", "42.6 Closure Process"),
    ("p",
     "A Decision ID closes only when its Required Evidence is actually supplied and recorded — an "
     "owner's verbal confirmation without recorded evidence does not close an item, consistent with "
     "this document's prohibition on converting SOURCE_DISCOVERY, INSTITUTIONAL or LEGAL items into "
     "invented facts. Closing a Decision ID updates both this register's Status/Decision/Effective "
     "Date columns and its originating chapter's Human Review Focus entry in the next revision."),
    ("h2", "42.7 Prioritisation Before Field-Level Expansion"),
    ("p",
     f"Blocking items — {_blocking_count} of the {len(REGISTER)} — should be resolved before Chapter "
     "39's field-level population proceeds further, since populating Source-System Field Mapping "
     "columns without them would require exactly the fabrication this document's instructions "
     "prohibit. Item 39-A alone aggregates the largest single cluster of source-discovery "
     "dependencies and is the practical long pole for reaching a Final Production Data Dictionary."),
    ("trace002", "This register consolidates items already individually traced to NCIE-002 within their originating chapters (see Ch.41 §41.2)."),
    ("h2", "42.8 Acceptance Criteria"),
    ("bullets", [
        "Every Human Review Focus item raised in Chapters 1-41 appears in §42.4/§42.5 by its Decision ID — verified by direct extraction from every chapter's review block, not manual transcription.",
        "No Decision ID is marked Closed without a recorded Decision and Effective Date.",
        "§42.3's counts match the sum of individual category counts across Chapters 1-41.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 43 — NCIE-003 Acceptance Checklist & Handover to NCIE-004
# ---------------------------------------------------------------------------
BLOCKS[43] = [
    ("h2", "43.1 Purpose"),
    ("p",
     "Defines the formal gate for accepting NCIE-003 and handing its canonical data contracts to "
     "the next approved NCIE production artifact (currently designated NCIE-004, subject to "
     "Documentation Suite Register reconciliation) and downstream specifications. This document "
     "does not itself decide NCIE-004's substantive scope or identity — only what NCIE-003 hands "
     "forward, per the suite-numbering principle already fixed in §0.2."),
    ("h2", "43.2 Two-Tier Status Distinction"),
    ("p",
     "Per the reviewer disposition recorded in front matter §0.6, acceptance of this baseline is "
     "explicitly two-tiered, and the two tiers are never to be conflated:"),
    ("table",
     ["Status", "Meaning", "Currently True?"],
     [
        ["APPROVED CANONICAL DATA ARCHITECTURE BASELINE, SUBJECT TO CONTROLLED DATA-DISCOVERY COMPLETION", f"The canonical semantic/data architecture in Chapters 1-41 (entity framework, modelling standards, governance model, temporal model, provenance model, security model, ARGUS model, Agent & VPF model and logical relationships) is approved. Chapter 42 is itself approved as the controlled open-decisions register attached to this baseline — approval covers the register as a governance instrument, not the {_open_count} items it holds, which remain open, classified, owned discovery/institutional dependencies pending closure per §42.6. Chapter 42 is part of the approved baseline; it is not excluded from it.", "IN DEVELOPMENT — FOR HUMAN REVIEW OF SURGICAL AMENDMENT (v0.4); v0.3 approval record preserved as history below"],
        ["FINAL PRODUCTION DATA DICTIONARY", "Would imply Chapter 39's field-level population and Source-System Field Mapping are complete for every canonical field.", "Not yet — explicitly not claimed by this edition"],
     ],
     "The two acceptance tiers this baseline distinguishes."),
    ("p",
     "This document may be approved under the first status without that approval being read, by "
     "implication or by omission, as approval under the second."),
    ("status",
     "Historical approval record (preserved, not current): NCIE-003 v0.3 was APPROVED as the "
     "Canonical Data Architecture Baseline (Chapters 1-42, per the scope above), subject to "
     "controlled data-discovery completion, following the reviewer's second review of that edition "
     "(v0.3, following the v0.2 review recorded in front matter §0.6). (v0.4) This edition is a "
     "controlled surgical amendment to that approved baseline (front matter §0.8) and is IN "
     "DEVELOPMENT — FOR HUMAN REVIEW OF SURGICAL AMENDMENT; it is NOT itself marked Approved. The "
     "v0.3 approval remains historically preserved and in force for everything this amendment did "
     "not change. The Final Production Data Dictionary tier remains explicitly not approved pending "
     "closure of Chapter 42's blocking items."),
    ("h2", "43.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Acceptance Checklist", "item, status, evidence reference."],
        ["Open-Issue Status", "reference to Ch.42's register, count by category, blocking vs non-blocking."],
        ["Traceability Completeness", "confirmation that Ch.41 §41.2 covers every chapter."],
        ["Dictionary Completeness", "confirmation that Ch.39's 15 mandated domains are represented and SOURCE DISCOVERY REQUIRED items are tracked, not fabricated."],
        ["ERD Consistency", "confirmation that Ch.40 agrees with Ch.39 (§40.16, §40.18)."],
        ["Approval Record", "approving authority, date, scope of approval."],
        ["Baseline Version", "the specific NCIE-003 version being accepted."],
        ["Handover Package", "contents list, recipient (NCIE-004/Codex), exclusions (e.g. no fabricated source schemas)."],
    ],
     "Acceptance Checklist & Handover principal entities."),
    ("h2", "43.4 Acceptance Checklist"),
    ("bullets", [
        "No material semantic conflict remains unresolved at baseline (verified against Ch.3 §3.7's and Ch.19/20/21's mandatory semantic separations).",
        "Data Dictionary (Ch.39), ERDs (Ch.40) and Traceability (Ch.41) agree with one another, including the explicit §41.3 consistency check across all 15 domains.",
        "Every item in Ch.42's complete master register has an assigned owner, even if not yet closed (§42.4-§42.5).",
        "No chapter fabricates a source-system schema, field name or enumeration claimed to be currently used by NCA (Ch.39 §39.2, throughout).",
        "Every chapter carries its classified Human Review Focus section (Ch.1-Ch.38), consolidated without omission in Ch.42.",
        "The surcharge rate and SIM registration limits are represented exclusively via Ch.24's governed Rule structures, with no literal constant elsewhere (verified against Ch.12 §12.4, Ch.14 §14.4).",
        "ARGUS-related entities preserve AI origin, human modification, and exclude private chain-of-thought (Ch.20 §20.2, verified against Ch.39 §39.12).",
        "Any approval granted for this baseline is explicitly recorded against one of the two tiers in §43.2, never left ambiguous between them.",
    ]),
    ("h2", "43.4A Agent & VPF Acceptance (v0.4 — VPF & Dynamic Agent Synthesis Amendment)"),
    ("p", "Extends acceptance to prove the following semantic separations hold throughout Chapters 3-41:"),
    ("bullets", [
        "Agent Definition ≠ Agent Run.",
        "Agent Pattern ≠ Active Agent.",
        "Ephemeral Agent ≠ Registered Reusable Agent.",
        "Agent Result Package ≠ Validated AI Result.",
        "Gate A ≠ Gate B.",
        "VPF Validation Artifact ≠ Human Approval.",
        "VPF PASS ≠ Decision (and ≠ Finding).",
        "Promotion Candidate ≠ Registered Agent.",
        "Engineering Change Candidate ≠ Implemented Capability.",
        "Agent Runtime Identity ≠ Human Principal.",
        "Historical Authorization ≠ Current Authorization.",
        "Historical VPF state survives later revalidation (REVALIDATION ≠ HISTORICAL REWRITE).",
    ]),
    ("h2", "43.4B Decision-Time and Human-Modification Acceptance (v0.4)"),
    ("p",
     "A Decision-Time test proves that a historical Decision can reconstruct: the AI Artifact, Agent/"
     "ARGUS origin, Agent Definition/Run, Model Route, Evidence/Context, VPF Profile Version, VPF "
     "Disposition, qualifications, and what the human actually saw at Decision Time — without later "
     "VPF revalidation contaminating the historical reconstruction (Ch.25 §25.7, §25.10)."),
    ("p",
     "A human-modification test proves that human modification of AI output preserves the original AI "
     "provenance, the original VPF state, and the human-modification provenance as a separate, "
     "additional record — never rewriting the original AI object as human-originated (Ch.20 §20.4, "
     "extended by §20.7-§20.8)."),
    ("h2", "43.4C Acceptance Does Not Certify Implementation (v0.4)"),
    ("p",
     "NCIE-003 v0.4 APPROVAL ≠ AGENT FACTORY / VPF PRODUCTION ACTIVATION. Acceptance under §43.2's "
     "first tier validates the canonical-data baseline for the Agent & VPF entity family; it does not "
     "certify that Agent Factory/VPF production software has been implemented, that the Agent Registry "
     "is populated, that VPF Profiles have been institutionally approved, or that Dynamic Agent "
     "Synthesis is operational. Where generated-code artifact modelling is referenced (Ch.3 §3.9.3), "
     "acceptance does not imply generated-code Dynamic Agent execution has been institutionally "
     "approved (tracked in NCIE-007 v1.1 Ch.35, not reopened here). Document approval likewise does not "
     "silently resolve the open retention/stewardship/ownership items in Ch.42 (3-C, 20-D, 20-E, 20-F)."),
    ("h2", "43.5 What the Next Artifact Consumes"),
    ("p",
     "The next approved NCIE production artifact (currently designated NCIE-004, subject to "
     "Documentation Suite Register reconciliation per §0.2) receives: the full Logical Canonical "
     "Model (Ch.3-Ch.30), the Data Dictionary structure and worked entities (Ch.39), the logical "
     "ERDs (Ch.40), the NCIE-002 crosswalk (Ch.41), and the complete open decisions register (Ch.42) "
     "as its own starting backlog of discovery work. It does not receive, and must not fabricate in "
     "its own right, any physical schema this document deliberately deferred (Ch.32, Ch.40 §40.17)."),
    ("h2", "43.6 Baseline-Lock and Change Control"),
    ("p",
     "Once accepted, the NCIE-003 baseline is locked under the same change-control process defined in "
     "Chapter 1 §1.4 — a canonical definition change after acceptance follows proposal, impact "
     "assessment (including against Ch.41's crosswalk and §41.3's consistency check), approval, "
     "version increment and a retained change record."),
    ("trace002", "This chapter is the formal closure of the authority chain stated in this edition's front matter §0.1: NCIE-001 requirements → NCIE-002 architecture → NCIE-003 canonical data semantics, ready for NCIE-004. (v0.4) §43.4A-§43.4C additionally close the approved NCIE-001 v1.3 / NCIE-002 v0.5 / NCIE-007 v1.1 amendment authority chain for this document."),
    ("review", [
        ("INSTITUTIONAL", "Confirm NCIE-003 approvers and their scope of authority."),
        ("INSTITUTIONAL", "Confirm precisely what NCIE-004 will consume from NCIE-003 versus re-derive independently."),
        ("INSTITUTIONAL", "Confirm the baseline-lock and change-control procedure to apply after acceptance."),
    ]),
    ("h2", "43.7 Acceptance Criteria"),
    ("bullets", [
        "Every item in §43.4's checklist is demonstrably satisfied or explicitly logged as an open item in Ch.42 before Baseline Version status changes from IN DEVELOPMENT to either tier in §43.2.",
        "The Handover Package is assembled with all §43.5 contents present and no excluded physical/fabricated content included.",
        "(v0.4) Every separation in §43.4A is demonstrably preserved, the Decision-Time and human-modification tests in §43.4B pass, and no statement in this document implies production implementation per §43.4C.",
    ]),
]
