"""NCIE-003 content batch: Chapters 1-6 (foundational modelling chapters)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 1 — Document Governance, Purpose & Data-Modelling Mandate
# ---------------------------------------------------------------------------
BLOCKS[1] = [
    ("h2", "1.1 Purpose"),
    ("p",
     "NCIE-003 is the semantic authority for NCIE's data: it defines what every canonical object "
     "means, how it is identified, how it relates to other objects, how it changes over time, where "
     "it came from, who owns it, how it is protected, and how downstream systems may consume it "
     "without changing its meaning. It governs after NCIE-001 (requirements) and NCIE-002 "
     "(architecture), and before the next approved NCIE production artifact (currently designated "
     "NCIE-004, subject to Documentation Suite Register reconciliation) and any physical database "
     "design. (v0.4) Following approved NCIE-001 v1.3, approved NCIE-002 v0.5 and approved NCIE-007 "
     "v1.1, this scope now explicitly includes the canonical Agent & VPF object family required to "
     "represent governed Dynamic Agent Synthesis and VPF validation (Ch.3 §3.9, Ch.20) — this is a "
     "consistency amendment to the existing scope, not a redesign of it."),
    ("h2", "1.2 Semantic Definition: Canonical, Authoritative, Source of Truth"),
    ("p",
     "Three terms recur throughout this document and are fixed here so later chapters do not "
     "redefine them locally:"),
    ("bullets", [
        "Canonical — the one NCIE-native representation of an entity or fact, independent of any single source system's format.",
        "Authoritative — the specific service or store that NCIE treats as correct for a given canonical object, per NCIE-002's domain-service ownership (e.g. the Rule Service is authoritative for rule values, per NCIE-002 Ch.22).",
        "Source of truth — the originating system or record from which a canonical fact was derived; distinct from authoritative, since NCIE can be authoritative for the canonical representation while the source system remains the source of truth for the original observation.",
    ]),
    ("h2", "1.3 Principal Entities"),
    ("table",
     ["Entity", "Description"],
     [
        ["Document Metadata", "Version, edition, status, prepared/approved dates, custodian."],
        ["Scope Statement", "What NCIE-003 governs and explicitly excludes."],
        ["Normative Term", "A defined term whose meaning is binding across all chapters (e.g. canonical, authoritative)."],
        ["Change Record", "A controlled, versioned change to a canonical definition."],
        ["Baseline Status", "Per-chapter approval state (IN DEVELOPMENT — FOR HUMAN REVIEW / APPROVED)."],
        ["Cross-Document Reference", "A pointer to the specific NCIE-001/002 requirement or architecture element a definition traces to."],
    ],
     "Chapter 1 governance entities."),
    ("h2", "1.4 Change Control"),
    ("p",
     "A canonical definition change follows: proposal → impact assessment against dependent chapters "
     "and NCIE-002 traceability → approval by the confirmed authority (§1's Human Review Focus) → "
     "version increment → change record retained permanently. No canonical definition is edited in "
     "place without a retained record of its prior form, consistent with NCIE-002's evidence/"
     "provenance-first principle (NCIE-002 Ch.1 §1.3.3)."),
    ("h2", "1.5 Ownership"),
    ("p",
     "NCIE-003 as a whole is owned by the NCIE Architecture Function. Individual chapters may name a "
     "domain steward (e.g. the Revenue Intelligence data model is stewarded jointly with Revenue "
     "Assurance) without transferring change-control authority away from the Architecture Function."),
    ("trace002",
     "NCIE-003 exists because NCIE-002 Ch.1 §1.3.3 (evidence/provenance-first) and Ch.5 (Canonical "
     "Data Platform) require canonical data whose meaning is fixed independently of any one domain "
     "service's implementation. This chapter is the governance root for that requirement."),
    ("review", [
        ("INSTITUTIONAL", "Confirm the approval authority for NCIE-003 as a whole and for individual chapter sign-off."),
        ("SOURCE_DISCOVERY", "Confirm whether any existing NCA enterprise data-governance standard already exists and must be adopted rather than superseded by this chapter's change-control model."),
        ("RESOLVED", "When a skeletal definition becomes an authoritative baseline: resolved by §0.2/§0.3 of this edition's front matter — skeletal-structure approval authorizes expansion; each chapter separately requires explicit approval before its content is binding."),
    ]),
    ("h2", "1.6 Acceptance Criteria"),
    ("bullets", [
        "Every subsequent NCIE-003 chapter states its approval status using the convention fixed in §0.3.",
        "Every canonical definition change is demonstrably traceable to a Change Record with prior version retained.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 2 — Data Architecture Principles & Modelling Standards
# ---------------------------------------------------------------------------
BLOCKS[2] = [
    ("h2", "2.1 Purpose"),
    ("p",
     "Fixes the modelling rules every domain chapter in this document must follow, so canonical data "
     "remains consistent, temporal, traceable and secure across 43 chapters authored at different "
     "times by different contributors."),
    ("h2", "2.2 Semantic Definition"),
    ("p",
     "A modelling standard in this chapter is binding: a domain chapter that deviates from it must "
     "say so explicitly and justify the deviation, rather than silently using a different convention."),
    ("h2", "2.3 Canonical Modelling Rules"),
    ("bullets", [
        "Unknown, Partial, Stale and Unavailable are modelled as explicit, distinguishable states on every canonical fact — never collapsed into a null that could also mean zero or false (directly implements NCIE-002 Ch.5 §5.3's missing-is-not-zero principle and Ch.18 §18.5's National Operating Picture state vocabulary).",
        "Canonical identity never depends on a display name, human-friendly label, or user-facing product name (this is the data-model counterpart of NCIE-002 Ch.19 §19.11's ARGUS naming boundary, generalised to every entity, not only the Assistant).",
        "Provenance, time and classification are first-class properties on every canonical entity, not optional metadata bolted on later.",
        "(v0.4) The Agent & VPF entity family (Ch.3 §3.9) follows these same modelling rules without exception — no Agent-specific temporal, identifier or classification mechanism is created (§2.5-§2.9 apply identically).",
    ]),
    ("h2", "2.4 Naming Conventions"),
    ("bullets", [
        "Canonical entity names are singular, domain-neutral nouns (e.g. Incident, not Incidents or NetworkIncident).",
        "A field name never encodes a specific source system (e.g. operator_export_col_14 is prohibited as a canonical field name; it belongs only in a Source-System Field Mapping, §30, §39).",
        "Abbreviations are only used where already fixed by NCIE-001/002 (e.g. PM, KPI, SIM, MoMo, REWS, NOP, ARGUS).",
    ]),
    ("h2", "2.5 Null / Unknown Semantics"),
    ("table",
     ["State", "Meaning", "Prohibited Substitute"],
     [
        ["Unknown", "No observation exists yet for this fact.", "Never represented as 0, empty string, or false."],
        ["Partial", "An observation exists but does not cover the full expected scope (e.g. some cells missing from a district PM file).", "Never silently treated as complete."],
        ["Stale", "An observation exists but has exceeded its freshness window (NCIE-002 Ch.18 §18.5).", "Never silently treated as current."],
        ["Unavailable", "The source or pipeline that would produce this fact is currently degraded (NCIE-002 Ch.6, Ch.27).", "Never conflated with Unknown, which is about the fact, not the pipeline."],
     ],
     "Explicit data-quality state vocabulary, binding across all domain chapters."),
    ("h2", "2.6 Temporal Modelling Rules"),
    ("p",
     "Every canonical fact capable of changing over time carries, at minimum, occurrence time and "
     "knowledge time as distinct properties (full bitemporal model in Chapter 5). Rules and "
     "relationships that can change under governance carry effective-from/effective-to dates "
     "(Chapter 24)."),
    ("h2", "2.7 Provenance Requirements"),
    ("p",
     "Every canonical fact references: the Source that supplied it (Chapter 6), the Ingestion Run "
     "that acquired it, and — where derived — the transformation chain that produced it (Chapter 25). "
     "No canonical fact may exist without at least one of these unless it is itself a foundational "
     "reference-data seed explicitly marked as such."),
    ("h2", "2.8 Extensibility and Versioning"),
    ("bullets", [
        "New attributes may be added to a canonical entity without a breaking version change, provided existing consumers are unaffected (additive-first, consistent with NCIE-002 Ch.25 §25.4).",
        "Removing or redefining the meaning of an existing attribute requires a new major schema version and a migration/deprecation plan (Chapter 33, Chapter 34).",
    ]),
    ("h2", "2.9 Classification and Security"),
    ("p",
     "Every canonical entity declares a default classification tier (public/internal/protected/"
     "sensitive) at the entity level, which individual attributes may raise but never lower, "
     "consistent with NCIE-002 Ch.26 §26.3."),
    ("h2", "2.10 Failure / Exception Semantics"),
    ("p",
     "A domain chapter that cannot populate a required modelling property (e.g. no clear knowledge "
     "time available from a source) must model that gap explicitly as Unknown/Unavailable rather than "
     "omit the property, so downstream consumers can detect the gap programmatically."),
    ("trace002",
     "Directly implements NCIE-002 Ch.1 §1.3 (design principles), Ch.5 (Canonical Data Platform, "
     "layered architecture and temporal model), Ch.18 §18.5 (National Operating Picture state "
     "vocabulary) and Ch.26 (classification tiers)."),
    ("review", [
        ("INSTITUTIONAL", "Approve the enterprise naming conventions in §2.4 as binding across all NCIE domains, including any existing NCA-wide systems this may eventually touch."),
        ("PROPOSED", "The null/unknown state vocabulary in §2.5 is proposed as the binding standard for all 43 chapters; it is technically defensible from NCIE-002 alone and does not depend on undiscovered NCA data."),
        ("SOURCE_DISCOVERY", "Confirm whether NCA already operates an enterprise data-modelling standard (naming, null-handling or otherwise) that NCIE-003 must adopt rather than establish independently."),
    ]),
    ("h2", "2.11 Acceptance Criteria"),
    ("bullets", [
        "Every domain chapter (Ch.7 onward) is checked against §2.3-§2.9 before being marked ready for review.",
        "A sampled canonical entity from at least three different domains demonstrably carries provenance, temporal and classification properties per this chapter's rules.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 3 — Enterprise Canonical Data Model
# ---------------------------------------------------------------------------
BLOCKS[3] = [
    ("h2", "3.1 Purpose"),
    ("p",
     "Provides the top-level, whole-of-NCIE view of major object families and how they relate, before "
     "any single domain chapter goes deep. This is the map that Chapters 7 onward each occupy one "
     "region of."),
    ("h2", "3.2 Semantic Definition"),
    ("p",
     "An enterprise entity is shared or referenced across more than one domain (e.g. Operator, "
     "Evidence); a domain entity belongs to exactly one domain chapter's ownership (e.g. PM "
     "Observation belongs to Chapter 7)."),
    ("h2", "3.3 Principal Entity Families"),
    ("table",
     ["Family", "Representative Entities", "Owning Chapter(s)"],
     [
        ["Shared / Core", "Operator, Geography, Cell, Identity Reference, Source, Evidence", "Ch.3, Ch.4, Ch.6, Ch.8, Ch.17"],
        ["Domain — Network & Field", "PM Observation, Topology Relation, Campaign, Measurement", "Ch.7, Ch.8, Ch.9"],
        ["Domain — Commercial", "Traffic Observation, Revenue Calculation, Mobile Money Aggregate", "Ch.11, Ch.12, Ch.13"],
        ["Domain — Identity & Fraud", "Registration, SIMBOX Detection, Blocking Action", "Ch.14, Ch.15"],
        ["Regulatory", "Case, Finding, Decision", "Ch.16"],
        ["Analytical", "Condition, Alert, Situation, Graph Edge", "Ch.18, Ch.19"],
        ["Collaborative", "Room, Hypothesis, ARGUS Interaction, Memory Object", "Ch.20, Ch.21, Ch.22"],
        ["Platform", "Workflow Instance, Rule, Audit Event, Event Envelope", "Ch.23, Ch.24, Ch.27, Ch.28"],
        ["Agent & VPF (v0.4)", "Agent Definition, Agent Pattern, Agent Run, Task Contract, Agent Result Package, VPF Profile, VPF Validation Artifact, Promotion Candidate, Engineering Change Candidate", "Ch.3 §3.9, Ch.20"],
    ],
     "Enterprise entity families and their owning domain chapters."),
    ("h2", "3.4 Cross-Domain Relationship Principle"),
    ("p",
     "A domain entity references a shared entity by canonical reference (Chapter 4), never by copying "
     "the shared entity's attributes inline. A Traffic Observation references Operator by ID; it does "
     "not carry its own duplicate operator-name field that could drift out of sync."),
    ("h2", "3.5 Enterprise Relationship Diagram"),
    ("rel",
     [
        ("Shared/Core entities", "are referenced by", "Domain entities (Network, Commercial, Identity & Fraud)"),
        ("Domain entities", "are correlated by", "Cross-Domain Fusion & Intelligence Graph (Ch.19)"),
        ("Domain entities + Fusion", "become candidates for", "Regulatory Case, Finding & Decision (Ch.16)"),
        ("All entities", "carry references into", "Evidence & Provenance (Ch.17, Ch.25)"),
        ("Humans + ARGUS", "reason over entities within", "Collaborative Intelligence (Ch.20, Ch.21)"),
     ],
     "Enterprise-level relationships between entity families."),
    ("h2", "3.6 Ownership Boundaries"),
    ("p",
     "Each entity has exactly one owning chapter for its canonical definition. Other chapters may "
     "extend it with domain-specific attributes only through an explicit extension relationship, "
     "never by redefining the shared entity's core meaning."),
    ("h2", "3.7 Semantic Separations (Enterprise Level)"),
    ("p",
     "This chapter is where the enterprise-wide semantic separations mandated for NCIE-003 are first "
     "declared as entity-family boundaries, not merely explanatory prose:"),
    ("bullets", [
        "Source Data ≠ Evidence (Ch.6 vs Ch.17).",
        "Observation ≠ Condition ≠ Alert ≠ Situation (Ch.7/Ch.11 vs Ch.18).",
        "Hypothesis ≠ Finding ≠ Decision (Ch.20/Ch.21 vs Ch.16).",
        "Detection ≠ Confirmed Fraud, and Registered Identity ≠ Fraud Actor (Ch.15).",
        "Requested ≠ Approved ≠ Executed ≠ Verified (Ch.23).",
        "Memory ≠ Current Truth, and Institutional Knowledge ≠ Rule (Ch.22 vs Ch.24).",
        "ARGUS Contribution ≠ Evidence, and Graph Relationship ≠ Causality (Ch.20, Ch.19).",
        "(v0.4) Agent Definition ≠ Agent Instance/Run; Agent Pattern ≠ Active Agent; Ephemeral Agent ≠ Registered Reusable Agent; Agent Result Package ≠ Validated AI Result; VPF Validation Artifact ≠ Human Approval; VPF PASS ≠ Finding; VPF PASS ≠ Decision; Promotion Candidate ≠ Registered Agent; Engineering Change Candidate ≠ Implemented Capability; Agent Runtime State ≠ Institutional Memory; AI Output ≠ Evidence (§3.9).",
    ]),
    ("trace002",
     "Directly implements NCIE-002 Ch.5 (Canonical Data Platform, canonical entity registry) and "
     "Ch.17 (Cross-Domain Fusion correlation-not-causation principle). §3.9 (v0.4) additionally "
     "implements approved NCIE-001 v1.3 §12.77-§12.80A, approved NCIE-002 v0.5 Ch.24 §24.4A and "
     "approved NCIE-007 v1.1 Ch.3, Ch.11, Ch.12, Ch.26."),
    ("review", [
        ("INSTITUTIONAL", "Confirm the principal enterprise entities in §3.3 against NCA's actual organisational view of its own data assets."),
        ("SOURCE_DISCOVERY", "Identify any NCA-wide master entity not yet represented (e.g. an existing enterprise operator master list) that should be adopted as the canonical source rather than re-created."),
    ]),
    ("h2", "3.9 Agent & VPF Canonical Object Family (v0.4 — VPF & Dynamic Agent Synthesis Amendment)"),
    ("p",
     "Authority: approved NCIE-001 v1.3 §12.77-§12.80A, §18.241A; approved NCIE-002 v0.5 Ch.24 §24.4A; "
     "approved NCIE-007 v1.1. This section recognizes the canonical object family required by the "
     "approved Dynamic Agent Synthesis and VPF architecture. It extends the enterprise model; it does "
     "not redesign it, and it does not reproduce NCIE-007's orchestration behaviour, gate execution "
     "logic or Agent Factory internal design (those remain authoritative in NCIE-007). Each object "
     "below follows this document's existing rules for identifiers (Ch.4), versioning (§2.8), temporal "
     "semantics (Ch.5), provenance (Ch.25), classification (Ch.31 — referenced, not redefined) and "
     "authorization references (Ch.26 — referenced, not redefined)."),
    ("table",
     ["Entity", "Canonical Definition", "Key Attributes / Attribute Classes", "Preserves"],
     [
        ["Agent Pattern", "A governed reusable template from which bounded task-specific Agent "
         "Definitions/instances may be produced. Carries no current authorization, context or "
         "execution authority of its own.",
         "canonical ID, version, purpose template, permitted-primitive constraints, lifecycle state.",
         "AGENT PATTERN ≠ ACTIVE AGENT"],
        ["Agent Definition", "The governed definition of an agent capability — purpose, scope and "
         "constraints — independent of any specific execution.",
         "Agent Definition ID, version, purpose, capability scope, permitted model classes/references, "
         "permitted tool classes/references, permitted data classes, context scope, authorization "
         "ceiling/reference, delegation constraint, resource constraint, network/egress policy "
         "reference, persistence policy reference, VPF Profile requirement, evaluation requirement, "
         "termination/expiry policy, provenance.",
         "AGENT DEFINITION ≠ AGENT RUN"],
        ["Task Contract", "The run-specific governed statement of what a particular Agent Run is "
         "authorized and expected to do. A reusable Agent Definition does not eliminate the need for "
         "a run-specific Task Contract.",
         "purpose, effective principal, requested outcome, scope, temporal scope, context scope, "
         "permitted data, permitted tools, resource limits, expected output, VPF requirement, "
         "termination conditions.",
         "TASK CONTRACT ≠ AUTHORIZATION RECORD"],
        ["Agent Run (Agent Instance)", "The runtime/execution object recording one bounded execution "
         "of an Agent Definition under a specific Task Contract.",
         "Run ID, Agent Definition reference, Task Contract reference, runtime identity (Ch.26 §26.5), "
         "lifecycle/execution state, start/end time, model route references (Ch.24), context "
         "references, evidence references (Ch.17), tool invocation references (Ch.20 §20.3), resource "
         "use, Gate A reference where applicable, Result Package reference, expiry/termination state.",
         "AGENT DEFINITION ≠ AGENT RUN"],
        ["Agent Risk Classification", "The governed reference/object representing the risk "
         "classification of an agent/run, considered across multiple factors rather than one score.",
         "data sensitivity, tool risk, state-changing capability, external egress, generated code, "
         "novelty, consequentiality, intended use — no single universal numerical score.",
         "RISK CLASSIFICATION ≠ NUMERICAL SCORE"],
        ["Agent Result Package", "The pre-VPF package produced by an Agent Run — structured output "
         "plus its supporting references, prior to validation.",
         "Task Contract reference, Agent Definition/Run reference, model route, context references, "
         "evidence references, tool receipts/invocations, structured AI output, execution status, "
         "known limitations, provenance.",
         "AGENT RESULT PACKAGE ≠ VALIDATED AI RESULT"],
        ["VPF Profile", "The governed validation-requirement definition applicable to a class of "
         "substantive AI-generated output.",
         "Profile ID, version, purpose/applicable output class, domain/risk applicability, validation "
         "dimensions, lifecycle state, effective period, owner/governance reference where known, "
         "provenance.",
         "VPF PROFILE ≠ POLICY AUTHORITY"],
        ["VPF Profile Version", "A specific, effective-dated version of a VPF Profile.",
         "version number, effective period, applicable output class/risk/domain, superseding/superseded "
         "reference.",
         "PROFILE VERSION CHANGE ≠ HISTORICAL REWRITE"],
        ["VPF Validation Artifact", "The first-class governed record of one VPF validation event.",
         "Validation ID, input artifact reference, VPF Profile reference, profile version, validation "
         "time, applicable policy/framework version, validation dimensions applied, disposition, "
         "qualification/failure reasons, validator references where applicable, human review reference "
         "where applicable, provenance.",
         "VPF VALIDATION ARTIFACT ≠ HUMAN APPROVAL"],
        ["Validated AI Result", "An AI-generated artifact whose applicable VPF validation permits "
         "release for its declared purpose/context.",
         "AI artifact reference, VPF Validation Artifact reference, disposition, qualifications, "
         "purpose, temporal context, provenance.",
         "VALIDATED AI RESULT ≠ INSTITUTIONAL DECISION"],
        ["Promotion Candidate", "The governed proposal to consider an Ephemeral Agent capability for "
         "reusable registration or pattern promotion.",
         "originating Agent Definition reference, Agent Run references, evaluation history, VPF "
         "history, failure/security history where applicable, proposed scope, human/governance review "
         "reference, lifecycle state.",
         "PROMOTION CANDIDATE ≠ REGISTERED AGENT"],
        ["Engineering Change Candidate", "The canonical object/reference required when a requested "
         "agent capability exceeds available approved primitives.",
         "originating task/capability gap, required capability, reason existing primitives are "
         "insufficient, affected domain/task, potential security/data impact, urgency where "
         "applicable, engineering disposition, provenance.",
         "ENGINEERING CHANGE CANDIDATE ≠ IMPLEMENTED CAPABILITY"],
     ],
     "Agent & VPF Canonical Object Family — new entities recognized by the v0.4 amendment (Ephemeral "
     "Agent and Registered Reusable Agent are the two Agent Run/lifecycle states this family governs; "
     "no separate canonical entity is created for either beyond the Agent Definition/Run/Registry "
     "structure above)."),
    ("h2", "3.9.1 VPF Dispositions"),
    ("table",
     ["Disposition", "Meaning"],
     [
        ["PASS", "Applicable validation satisfied — not institutional approval (VPF PASS ≠ FINDING; VPF PASS ≠ DECISION)."],
        ["QUALIFIED", "Releasable with an explicit qualification; never treated as equivalent to PASS."],
        ["REJECT", "Not releasable as a Validated AI Result; provenance of the rejected run is retained where policy requires."],
        ["HUMAN_REVIEW_REQUIRED", "Presentable only in the governed review context appropriate to that state."],
        ["VALIDATION_UNAVAILABLE", "A mandatory validator did not run, timed out, failed technically, or was ineligible — never treated as PASS."],
        ["REVALIDATION_REQUIRED", "Where NCIE-007 requires it — a later Validation Artifact is created; the original is never overwritten."],
        ["INVALIDATED", "Where NCIE-007 requires it — the original historical validation state survives (REVALIDATION ≠ HISTORICAL REWRITE)."],
     ],
     "VPF Disposition vocabulary — not reduced to one numeric score."),
    ("h2", "3.9.2 Registry vs Ephemeral Boundary"),
    ("p",
     "The Agent Registry (referenced here, canonically detailed alongside Ch.20 and NCIE-007 v1.1 "
     "Ch.12) distinguishes Registered Reusable Agents from Ephemeral Agent Definitions/instances and "
     "from Promotion Candidates. Not every Agent Definition is automatically a Registered Reusable "
     "Agent; an Ephemeral Agent's Definition/Run history is never retroactively relabelled as "
     "registered merely because it was later promoted (EPHEMERAL AGENT ≠ REGISTERED REUSABLE AGENT)."),
    ("h2", "3.9.3 Scope Boundaries"),
    ("bullets", [
        "NCIE-003 specifies meaning, identity, relationships, lifecycle semantics, temporal semantics, provenance, dictionary definition and logical ER structure for these objects. It does not specify runtime orchestration algorithms, physical database implementation, infrastructure topology, model-provider selection or Agent Factory source code (NCIE-007, NCIE-004, NCIE-014 remain authoritative for those).",
        "CANONICAL MODEL DEFINED ≠ PRODUCTION SYSTEM IMPLEMENTED, and APPROVED CANONICAL ENTITY ≠ OPERATIONAL DATA POPULATED — this section defines the architecture required to support Agent Factory/VPF capability; it does not assert that capability is deployed, populated or institutionally approved.",
        "Existing Tool Invocation (Ch.20 §20.3), Model Route/Version (Ch.20 §20.3, Ch.24) and Evidence (Ch.17) semantics are reused for Agent Runs; no Agent-specific duplicate Tool, Model or Evidence entity is created.",
        "Generated-code artifact data treatment (where an Agent Result Package includes generated executable code) is already tracked as an open institutional/security decision in approved NCIE-007 v1.1 Ch.35; it is referenced here, not reopened as a separate NCIE-003 decision.",
    ]),
    ("review", [
        ("INSTITUTIONAL", "Confirm canonical stewardship/ownership for the new Agent & VPF entity family (§3.9), consistent with the existing per-family ownership model in §3.6."),
    ]),
    ("h2", "3.10 Acceptance Criteria"),
    ("bullets", [
        "Every entity introduced in Chapters 7-28 is traceable to exactly one family in §3.3 and one owning chapter.",
        "None of the semantic separations in §3.7 is violated by a foreign-key structure that would allow two distinct states to merge (verified per-domain in each owning chapter and consolidated in Ch.40).",
        "(v0.4) Every Agent & VPF entity in §3.9 is traceable to exactly one family row in §3.3 and preserves its stated invariant; no diagram or relationship in Ch.20/Ch.40 implies Agent Definition = Agent Run, Agent Pattern = Active Agent, Ephemeral Agent = Registered Reusable Agent, Agent Result Package = Validated AI Result, VPF PASS = Human Approval/Finding/Decision, Promotion Candidate = Registered Agent, or Engineering Change Candidate = Implemented Capability.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 4 — Common Entity, Identifier & Reference Model
# ---------------------------------------------------------------------------
BLOCKS[4] = [
    ("h2", "4.1 Purpose"),
    ("p",
     "Defines how NCIE identifies the same real-world or system object consistently across domains "
     "and source systems, so that a cell, operator or identity referenced in five different chapters "
     "is provably the same object each time."),
    ("h2", "4.2 Semantic Definition"),
    ("bullets", [
        "Canonical ID — the stable NCIE-native identifier for an entity, assigned once and never reused, surviving renames.",
        "External/Source ID — the identifier a specific source system uses for the same real-world object; retained for lineage, never used as the canonical key.",
        "Alias — a human-facing alternative label (including a configurable presentation name such as ARGUS for the Assistant service identity) that never substitutes for canonical identity.",
    ]),
    ("h2", "4.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Canonical ID", "entity type, id value, created date, status (active/merged/retired)."],
        ["External/Source ID", "canonical ID reference, source reference (Ch.6), source-native id value, first/last observed."],
        ["Alias", "canonical ID reference, alias value, alias type (display name, legacy name, presentation identity), effective period."],
        ["Identity-Resolution State", "candidate match set, confidence, resolution status (resolved/ambiguous/rejected)."],
        ["Merge/Split Lineage", "prior canonical ID(s), resulting canonical ID(s), reason, actor, timestamp."],
    ],
     "Common Entity, Identifier & Reference Model principal entities."),
    ("h2", "4.4 Identity Resolution Rules"),
    ("bullets", [
        "An ambiguous match (more than one plausible canonical entity) is stored as an Identity-Resolution State with status ambiguous and is never force-resolved automatically to the highest-confidence candidate without a rule or human decision permitting it (directly implements NCIE-002 Ch.14 §14.6, Ch.34 §34.1's ambiguous-match handling generalised platform-wide).",
        "A canonical ID is never reused after retirement, even if the original entity is later found to be identical to a new one — reconciliation produces a Merge/Split Lineage record instead.",
    ]),
    ("h2", "4.5 Lifecycle / States"),
    ("flow",
     [
        "New object observed with no confident canonical match",
        "Identity-Resolution State created (candidate set, confidence)",
        "Resolved automatically (high confidence per governed threshold) or by human decision",
        "Canonical ID assigned or merged into existing canonical ID",
        "External/Source ID and Alias linked to the resolved Canonical ID",
     ],
     "Identity resolution lifecycle from first observation to canonical assignment."),
    ("h2", "4.6 Relationships and Cardinality"),
    ("bullets", [
        "One Canonical ID has zero-to-many External/Source IDs (one per source system that has independently referenced it).",
        "One Canonical ID has zero-to-many Aliases, at most one active per alias type at a time (effective-dated, Chapter 24 pattern).",
        "A Merge/Split Lineage record has one-to-many prior canonical IDs and one-to-many resulting canonical IDs, supporting both merges and splits.",
    ]),
    ("h2", "4.7 Provenance and Classification"),
    ("p",
     "Every External/Source ID retains which Source (Chapter 6) supplied it and when, for lineage. "
     "Identifier records themselves inherit the classification of the entity they identify — a "
     "protected-identity canonical ID (Chapter 14) is itself protected metadata, not merely the "
     "attributes attached to it."),
    ("h2", "4.8 Failure / Exception Semantics"),
    ("p",
     "A source supplying an identifier that cannot be resolved to any canonical entity, and does not "
     "meet the bar for creating a new one, is retained as an unresolved External/Source ID with a "
     "flagged exception state rather than silently discarded — this preserves the option to resolve "
     "it later without re-ingesting the original source data."),
    ("trace002",
     "Directly implements NCIE-002 Ch.5 §5.2 (canonical entity registry), Ch.17 (entity resolution "
     "for fusion) and Ch.19 §19.11 (ARGUS as a presentation alias over a stable internal identity)."),
    ("review", [
        ("INSTITUTIONAL", "Confirm identifier formats where institutionally constrained (e.g. any existing NCA-mandated operator or facility identifier scheme)."),
        ("SOURCE_DISCOVERY", "Confirm authoritative master-data sources for core entities (Operator, Geography) — is there an existing NCA master list, or does NCIE-003 establish the first canonical one?"),
        ("PROPOSED", "The ambiguous-match handling in §4.4 (never force-resolve automatically) is proposed as the binding default for all identity resolution across NCIE-003, extending the pattern already fixed for SIM/identity matching in NCIE-002 Ch.14."),
    ]),
    ("h2", "4.9 Acceptance Criteria"),
    ("bullets", [
        "A simulated rename of a real-world entity (e.g. a cell relocated and renamed) is demonstrably resolved without losing its Canonical ID or historical External/Source ID linkage.",
        "An ambiguous identity match is demonstrably retained as ambiguous rather than silently merged.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 5 — Temporal & Bitemporal Data Model
# ---------------------------------------------------------------------------
BLOCKS[5] = [
    ("h2", "5.1 Purpose"),
    ("p",
     "Defines every time semantic needed to reconstruct what happened, when NCIE learned it, and "
     "which rules applied — the data-model foundation for NCIE-002's decision-time reconstruction "
     "requirement (NCIE-002 Ch.23 §23.5)."),
    ("h2", "5.2 Semantic Definition"),
    ("table",
     ["Time Type", "Definition"],
     [
        ["Occurrence/Observation Time", "When the real-world fact actually happened or was measured."],
        ["Acquisition Time", "When NCIE's ingestion pipeline received the artifact containing the fact (Ch.6)."],
        ["Knowledge Time", "When NCIE considered the fact known/validated — may lag acquisition time and must never be back-dated to occurrence time for late-arriving data."],
        ["Effective-From / Effective-To", "The period during which a rule, relationship or configuration value is in force (Ch.24)."],
        ["Decision Time", "The point in time as of which a Decision (Ch.16) is evaluated, excluding any evidence that arrived later (NCIE-002 Ch.23 §23.5)."],
        ["Revision Time", "When a correction to a previously recorded fact was made (distinct from the fact's own occurrence time)."],
        ["Scenario Time", "A hypothetical reference time used by a what-if Scenario (Ch.24 §24 pattern); never written to production history."],
    ],
     "NCIE-003 time-type vocabulary, binding across all chapters."),
    ("h2", "5.3 Bitemporal Storage Principle"),
    ("p",
     "An entity requiring historical defensibility stores both occurrence/effective time and "
     "knowledge/revision time as independent axes: querying \"as it was known on date X\" and "
     "querying \"as it occurred/applied on date Y\" must be answerable independently and in "
     "combination, without one overwriting the other."),
    ("h2", "5.4 Principal Entities"),
    ("bullets", [
        "Temporal Fact Envelope — the reusable structure (occurrence time, acquisition time, knowledge time, revision time, superseded-by reference) that domain entities requiring bitemporal storage embed.",
        "Historical Snapshot — a reconstructed view of canonical state as of a specified knowledge time (implements NCIE-002 Ch.23's Historical Snapshot Service data requirements).",
        "Decision-Time Context — the bounded set of facts, rule versions and evidence available at a Decision's timestamp, explicitly excluding later arrivals.",
    ]),
    ("h2", "5.5 Which Entities Require Bitemporal Storage"),
    ("p",
     "Full bitemporal storage (both axes independently queryable) is required for: canonical facts "
     "feeding Revenue calculation (Ch.12), Rules (Ch.24), Registration limits (Ch.14), Evidence "
     "(Ch.17), and Findings/Decisions (Ch.16). Simpler single-axis (knowledge-time-only) storage is "
     "acceptable for high-volume, low-materiality telemetry such as raw PM samples (Ch.7), provided "
     "the coarser Ingestion Run (Ch.6) retains acquisition time."),
    ("h2", "5.6 Correction Semantics"),
    ("p",
     "A correction to a previously recorded fact never overwrites the prior value in place. It "
     "creates a new version with its own revision time, linked to the prior version via a Correction "
     "relationship (Ch.25), so a query as of a knowledge time before the correction still returns the "
     "pre-correction value."),
    ("h2", "5.7 Failure / Exception Semantics"),
    ("p",
     "A source that cannot supply a clear occurrence time (only a delivery time) has that gap recorded "
     "explicitly — occurrence time is marked Unknown (Chapter 2's vocabulary) rather than defaulted to "
     "acquisition time, which would silently misrepresent when the fact actually happened."),
    ("h2", "5.8 Official Time Zone and Reference Clock"),
    ("p",
     "All canonical timestamps are stored in a single reference time zone (UTC recommended) with "
     "local Ghana time (GMT, no DST) derived for display, so cross-source comparison is never subject "
     "to ambiguous local-time arithmetic."),
    ("trace002",
     "Directly implements NCIE-002 Ch.5 §5.3 (temporal/metadata model), Ch.22 §22.3 (rule effective "
     "dating) and Ch.23 §23.5 (decision-time reconstruction)."),
    ("review", [
        ("PROPOSED", "UTC as the canonical storage time zone with Ghana local time derived for display is proposed as the binding default (§5.8); technically defensible and does not depend on undiscovered facts."),
        ("INSTITUTIONAL", "Confirm which entities beyond the §5.5 list require full bitemporal storage versus knowledge-time-only, weighing storage cost against legal/operational reconstruction needs."),
        ("LEGAL", "Confirm legal/operational expectations for how far back historical reconstruction must be defensible (informs retention in Ch.31 and archival tiering in Ch.35)."),
    ]),
    ("h2", "5.9 Acceptance Criteria"),
    ("bullets", [
        "A correction to a Revenue-relevant Traffic fact is demonstrably retrievable both in its pre- and post-correction form, keyed by knowledge time.",
        "A Decision-Time Context reconstruction for a sampled Case demonstrably excludes evidence with a knowledge time after the Decision's timestamp.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 6 — Source, Provider, Acquisition & Ingestion Data Model
# ---------------------------------------------------------------------------
BLOCKS[6] = [
    ("h2", "6.1 Purpose"),
    ("p",
     "Models where data comes from, how it enters NCIE, and how source lineage is retained — the "
     "data-model realisation of NCIE-002's Source Registry and Ingestion Gateway (NCIE-002 Ch.6)."),
    ("h2", "6.2 Semantic Definition"),
    ("bullets", [
        "Source — the institutional origin of data (e.g. \"MTN monthly PM export\"), distinct from the technical channel used to acquire it.",
        "Provider — the technical acquisition channel (API, file, email, screenshot, manual, RPA) currently used for a Source; a Source may change Provider without changing identity.",
        "Multiple technical copies of the same underlying observation (e.g. the same file received via two channels) do not create independent corroboration — they are deduplicated to one Source Object Reference before being treated as evidence of anything.",
    ]),
    ("h2", "6.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Source", "name, owner, domain, expected frequency, trust tier, status."],
        ["Provider", "type (API/file/email/screenshot/manual/RPA), source reference, configuration reference (credentials by reference only, per NCIE-002 Ch.26)."],
        ["Acquisition Channel", "provider reference, endpoint/mailbox/portal reference, authentication reference."],
        ["Ingestion Run", "source reference, provider reference, start/end time, status, artifact reference(s)."],
        ["Source Object Reference", "ingestion run reference, raw artifact pointer, hash/integrity metadata, deduplication key."],
        ["Validation Result", "source object reference, checks performed, pass/fail, rejection reason."],
        ["Transformation Reference", "source object reference, transformation applied, resulting canonical fact reference(s) (Ch.25)."],
        ["Acquisition Status", "source reference, current health (Green/Amber/Grey per NCIE-002 Ch.6 §6.9), last successful run."],
    ],
     "Source, Provider, Acquisition & Ingestion principal entities."),
    ("h2", "6.4 Lifecycle / States"),
    ("flow",
     [
        "Source registered with owner, frequency and provider",
        "Acquisition Channel configured (credentials by reference only)",
        "Ingestion Run attempted",
        "Source Object Reference created from received artifact",
        "Validation Result recorded (pass/fail/reason)",
        "Transformation Reference links validated content to canonical facts",
        "Acquisition Status updated (Green/Amber/Grey)",
     ],
     "Source-to-canonical acquisition lifecycle."),
    ("h2", "6.5 Relationships and Cardinality"),
    ("bullets", [
        "One Source has one current Provider but may retain historical Provider records (e.g. manual-to-RPA transition) without losing Source identity.",
        "One Ingestion Run produces zero-to-many Source Object References (e.g. a single file yielding multiple records).",
        "One Source Object Reference has zero-or-one Validation Result and, if passed, one-to-many Transformation References.",
    ]),
    ("h2", "6.6 Deduplication Rule"),
    ("p",
     "Two Source Object References with the same deduplication key (content hash plus source plus "
     "occurrence-time bucket) are treated as one substantive observation for corroboration purposes, "
     "even if acquired through different Providers or Ingestion Runs — this directly implements the "
     "multiple-technical-copies-are-not-independent-corroboration principle."),
    ("h2", "6.7 Failure / Exception Semantics"),
    ("bullets", [
        "A failed Validation Result quarantines the Source Object Reference; it never silently becomes canonical, and it never silently disappears — it remains queryable as a rejected artifact with its reason (NCIE-002 Ch.6 §6.4).",
        "A Source with no successful Ingestion Run within its expected frequency window shows Acquisition Status Grey, not a false Green.",
    ]),
    ("h2", "6.8 Classification and Ownership"),
    ("p",
     "Every Source has a named accountable owner before being enabled (NCIE-002 Ch.6 §6.6). Source "
     "Object References inherit the classification of the content they carry once known; until "
     "validated, raw content defaults to the most protective applicable classification tier."),
    ("trace002",
     "Directly implements NCIE-002 Ch.6 in full (Source Registry, Ingestion Gateway, Request/Run/"
     "Artifact/Validation lineage, health thresholds)."),
    ("review", [
        ("SOURCE_DISCOVERY", "Inventory actual NCA/operator source systems, their current owners and provider channels — this chapter's entities are structurally ready but not yet populated with real sources."),
        ("INSTITUTIONAL", "Confirm source ownership and trust hierarchy where more than one plausible owner exists (e.g. a source jointly relevant to Network and Regulatory domains)."),
        ("SOURCE_DISCOVERY", "Confirm which sources arrive via API, file, stream, RPA or manual upload today, to correctly populate initial Provider records."),
    ]),
    ("h2", "6.9 Acceptance Criteria"),
    ("bullets", [
        "A deliberately duplicated source artifact (same content, two channels) is demonstrably deduplicated to one Source Object Reference before downstream use.",
        "A rejected Validation Result is demonstrably retrievable with its rejection reason, distinct from data that never arrived at all.",
    ]),
]
