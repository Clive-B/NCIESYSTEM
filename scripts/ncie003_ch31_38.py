"""NCIE-003 content batch: Chapters 31-38 (classification, physical, integration,
migration, performance, security, observability and testing data models)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 31 — Classification, Privacy, Retention & Data Lifecycle
# ---------------------------------------------------------------------------
BLOCKS[31] = [
    ("h2", "31.1 Purpose"),
    ("p", "Defines how NCIE data is classified, retained, archived, held and securely disposed of — "
         "the classification tiers and retention rules referenced throughout this document."),
    ("h2", "31.2 Semantic Definition"),
    ("bullets", [
        "Protected identity (Ch.14) and precise tracking/location data (Ch.8, Ch.15) require heightened protection beyond ordinary internal classification.",
        "Retention differs by data class and purpose — a single global retention period is not assumed.",
        "Derived indexes, embeddings and caches (Ch.20's ARGUS tooling, search) must be considered during lawful deletion — deleting a canonical record without also addressing its derived copies is not lawful deletion.",
    ]),
    ("h2", "31.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Classification", "tier (public/internal/protected/sensitive), applies-to entity/field reference."],
        ["Privacy Category", "governed category (e.g. identity document, location, financial), applicable legal basis reference."],
        ["Retention Rule", "data class, retention period, legal basis, effective period (Ch.24 pattern)."],
        ["Hold", "object reference, reason (e.g. litigation/regulatory hold), effective period, overrides normal retention."],
        ["Archive State", "object reference, tier (hot/warm/cold, Ch.35), archived timestamp."],
        ["Disposition Event", "object reference, action (archived/purged), timestamp, authorizing actor (Ch.26)."],
        ["Deletion Propagation", "object reference, derived-copy references (index/embedding/cache) requiring corresponding deletion, status."],
        ["Redaction / Masking State", "object reference, masked fields, applicable viewer scope."],
    ],
     "Classification, Privacy, Retention & Data Lifecycle principal entities."),
    ("h2", "31.4 Deletion Propagation Requirement"),
    ("p",
     "A Disposition Event of type purge for a canonical object is not considered complete until its "
     "Deletion Propagation record shows every known derived copy (search index entries, ARGUS-related "
     "embeddings, Ch.20; caches) either deleted or explicitly exempted with a recorded reason — this "
     "closes the gap NCIE-002 Ch.26 flags around sensitive semantic/vector indexing."),
    ("h2", "31.5 Hold Overrides Retention"),
    ("p",
     "An active Hold on an object suspends its normal Retention Rule outcome; a Disposition Event "
     "cannot purge an object with an active Hold, regardless of how expired its retention period "
     "otherwise is."),
    ("h2", "31.6 Classification Inheritance"),
    ("p",
     "Consistent with Chapter 2 §2.9, an entity's Classification tier is a floor for its fields and "
     "for any derived object referencing it (e.g. an ARGUS Contribution citing sensitive Evidence "
     "inherits at least sensitive classification, Ch.20 §20.7)."),
    ("h2", "31.7 Failure / Exception Semantics"),
    ("p",
     "A Deletion Propagation that cannot confirm a derived copy was actually removed (e.g. an external "
     "cache outside NCIE's direct control) is left in an open, flagged state rather than marked "
     "complete on an assumption."),
    ("trace002", "Directly implements NCIE-002 Ch.26 in full (classification, privacy, sovereignty, sensitive-index policy)."),
    ("review", [
        ("LEGAL", "Confirm classification taxonomy against applicable Ghanaian data-protection law and NCA policy."),
        ("LEGAL", "Confirm retention schedules and legal-hold procedures."),
        ("LEGAL", "Confirm privacy obligations specific to Ghana Card/Passport-derived data (Ch.14)."),
    ]),
    ("h2", "31.8 Acceptance Criteria"),
    ("bullets", [
        "A purge Disposition Event for a sampled object with a search-index derived copy demonstrably includes a corresponding Deletion Propagation entry.",
        "An object under an active Hold is demonstrably blocked from purge regardless of retention-period expiry.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 32 — Physical Data Design & Storage Mapping
# ---------------------------------------------------------------------------
BLOCKS[32] = [
    ("h2", "32.1 Purpose"),
    ("p", "Maps logical entities into storage technologies after the logical model is approved. This "
         "chapter is explicitly downstream of Chapters 1-31; it does not redefine canonical meaning, "
         "only where and how it is physically stored."),
    ("h2", "32.2 Semantic Definition — Three Model Levels"),
    ("table",
     ["Model Level", "Defines", "Chapter(s)"],
     [
        ["Conceptual Model", "Business/regulatory meaning of entities and relationships, technology-agnostic.", "Ch.3, domain chapters 7-22"],
        ["Logical Canonical Model", "Entities, attributes, relationships, cardinality, keys — still technology-agnostic.", "Ch.4-Ch.30, Ch.40"],
        ["Physical Implementation Model", "Actual database technology, table/collection structures, indexes, partitioning, source-specific mappings.", "This chapter, Ch.35"],
    ],
     "The three model levels this document distinguishes throughout; this chapter is the first to address the third."),
    ("h2", "32.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Relational Store", "workload class, technology reference, hosted entity families."],
        ["Analytical / Time-Series Store", "workload class (e.g. PM Observations, Traffic), technology reference."],
        ["Object / Document Store", "workload class (e.g. Evidence Artifacts), technology reference."],
        ["Graph Store", "workload class (Ch.19 Intelligence Graph), technology reference."],
        ["Search Index", "workload class, technology reference, classification-aware segmentation (Ch.31)."],
        ["Vector Index", "workload class (ARGUS retrieval, Ch.20), technology reference, classification-aware segmentation."],
        ["Immutable Snapshot / Archive Store", "workload class (Ch.25 Snapshots, Ch.35 cold tier), technology reference."],
        ["Logical-to-Physical Map", "logical entity reference, physical store reference, mapping notes."],
    ],
     "Physical Data Design & Storage Mapping principal entities."),
    ("h2", "32.4 One Technology Is Not Forced Onto Every Workload"),
    ("p",
     "The Logical Canonical Model (Ch.4-Ch.30) does not mandate a single database technology; this "
     "chapter's Logical-to-Physical Map lets different entity families use the store best suited to "
     "their access pattern (e.g. bitemporal relational storage for Revenue, Ch.12; time-series storage "
     "for PM Observations, Ch.7; graph storage for the Intelligence Graph, Ch.19) without those "
     "choices leaking back into the logical model's meaning."),
    ("h2", "32.5 Derived vs Canonical Stores"),
    ("p",
     "Graph, Search and Vector stores are derived or specialised representations of canonical data "
     "(per Ch.31 §31.4's deletion-propagation requirement); none of them is independently canonical, "
     "and a discrepancy between a derived store and its canonical source is a data-quality issue "
     "(Ch.29), not a competing truth."),
    ("h2", "32.6 Consistency and Transaction Boundaries"),
    ("p",
     "The Logical-to-Physical Map states, for each mapped entity family, its required consistency "
     "model (strong/eventual) and transaction boundary (e.g. a Revenue Calculation and its Traffic "
     "Input References must be read consistently together) — this must be explicit before physical "
     "technology selection, not discovered afterward."),
    ("h2", "32.7 Failure / Exception Semantics"),
    ("p",
     "A derived store found out of sync with its canonical source (Ch.29 Source Conflict pattern "
     "applied to derived stores) triggers a Remediation Task (Ch.29) rather than being silently "
     "trusted until the next scheduled rebuild."),
    ("trace002", "Depends on NCIE-002 Ch.5 (layered canonical/analytical platform) and Ch.30 (implementation-level persistence, to be detailed in NCIE-014)."),
    ("review", [
        ("INSTITUTIONAL", "Confirm approved enterprise platforms/technologies for each store type in §32.3."),
        ("INSTITUTIONAL", "Confirm hosting constraints (on-prem/sovereign cloud, per NCIE-002 Ch.1 §1.6's proposed posture)."),
        ("LEGAL", "Confirm which stores may contain restricted/sensitive data given each candidate technology's own security posture."),
    ]),
    ("h2", "32.8 Acceptance Criteria"),
    ("bullets", [
        "The Logical-to-Physical Map demonstrably covers every entity family in Chapter 3's enterprise model.",
        "A sampled derived store (Search or Vector Index) is demonstrably reconcilable against its canonical source with a defined remediation path.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 33 — Data API, Schema & Event Contract Standards
# ---------------------------------------------------------------------------
BLOCKS[33] = [
    ("h2", "33.1 Purpose"),
    ("p", "Defines how data contracts are serialized, versioned and evolved across services, "
         "implementing NCIE-002 Ch.25's Schema Registry at the data-contract level."),
    ("h2", "33.2 Semantic Definition"),
    ("p",
     "A contract requires a stable ID and version independent of its serialization format. Temporal, "
     "provenance and classification context (Ch.5, Ch.25, Ch.31) must not be stripped when a "
     "canonical fact crosses an integration boundary — a consumer receiving a fact via API or event "
     "must still be able to determine its knowledge time, lineage and classification."),
    ("h2", "33.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["API Schema", "schema ID, version, request/response structure, owning service."],
        ["Event Schema", "schema ID, version, payload structure, owning event type (Ch.28)."],
        ["Schema ID / Version", "stable identifier plus semantic version (major.minor)."],
        ["Compatibility Policy", "schema reference, rule (additive-only for minor, migration-required for major)."],
        ["Idempotency Key", "See Ch.23/Ch.28 — this chapter defines it as a mandatory contract element wherever a call has a side effect."],
        ["Correlation ID", "See Ch.27/Ch.28 — mandatory contract element for tracing."],
        ["Serialization Format", "governed reference (e.g. JSON, Protobuf), per schema."],
        ["Deprecation State", "schema reference, deprecation date, replacement schema reference, sunset date."],
    ],
     "Data API, Schema & Event Contract Standards principal entities."),
    ("h2", "33.4 Compatibility Rule"),
    ("p",
     "A minor version increment may only add optional fields (additive-first, consistent with "
     "NCIE-002 Ch.25 §25.4). Removing or redefining an existing field's meaning requires a major "
     "version increment, a Deprecation State on the prior version, and a migration plan (Ch.34) for "
     "existing consumers."),
    ("h2", "33.5 Mandatory Context Fields"),
    ("p",
     "Every API Schema and Event Schema that carries a canonical fact includes, at minimum: knowledge "
     "time (Ch.5), a lineage reference (Ch.25), and a classification tag (Ch.31) — a schema omitting "
     "any of these for a canonical-fact-bearing field is non-conformant and blocked at schema review."),
    ("h2", "33.6 Relationships"),
    ("p",
     "Every Event Type (Ch.28) references exactly one current Event Schema version; historical "
     "events retain the schema version they were published under, so a consumer replaying old events "
     "can interpret them correctly even after the schema evolves."),
    ("h2", "33.7 Failure / Exception Semantics"),
    ("p",
     "A payload that fails schema validation is treated as a Schema Exception (Ch.29 §29.3), never "
     "coerced into the expected shape."),
    ("trace002", "Directly implements NCIE-002 Ch.25 in full (schema registry, compatibility rules)."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm preferred API/event standards already in use at NCA (e.g. existing REST/gRPC/messaging conventions)."),
        ("INSTITUTIONAL", "Confirm versioning/deprecation policy timelines (how long a deprecated schema remains supported)."),
        ("SOURCE_DISCOVERY", "Confirm external operator contract constraints (e.g. fixed formats operators already use for regulatory submissions)."),
    ]),
    ("h2", "33.8 Acceptance Criteria"),
    ("bullets", [
        "A sampled schema carrying a canonical fact demonstrably includes knowledge time, lineage reference and classification tag.",
        "A breaking change is demonstrably rejected unless published as a new major schema version with a Deprecation State on the prior one.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 34 — Migration, Legacy Data & Master Data Reconciliation
# ---------------------------------------------------------------------------
BLOCKS[34] = [
    ("h2", "34.1 Purpose"),
    ("p", "Defines how existing NCA and operator historical data will be imported and reconciled to "
         "canonical NCIE entities."),
    ("h2", "34.2 Semantic Definition"),
    ("bullets", [
        "Legacy import is not automatically validated truth — imported records pass through the same Validation Result process (Ch.6, Ch.29) as any other source.",
        "Original source IDs and transformations are retained through migration, never discarded once a canonical match is found.",
        "Ambiguous identity matches are never forced during migration, exactly as Chapter 4 §4.4 requires for ongoing identity resolution.",
    ]),
    ("h2", "34.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Legacy Source", "system name, description, data owner, decommission status."],
        ["Legacy Record", "legacy source reference, original identifier, original structure (pre-mapping)."],
        ["Mapping Rule", "legacy source reference, field-to-canonical-field mapping (references Ch.30/Ch.39 Source-System Field Mapping)."],
        ["Transformation", "legacy record reference, transformation applied, resulting canonical candidate."],
        ["Canonical Match", "legacy record reference, candidate canonical entity reference (Ch.4)."],
        ["Match Confidence / State", "canonical match reference, confidence score, state (auto-matched/human-confirmed/ambiguous/rejected)."],
        ["Migration Batch", "scope, source, target, run timestamp, status."],
        ["Validation Result", "See Ch.6/Ch.29 — migration reuses, not duplicates, this entity."],
        ["Exception", "migration batch reference, unresolved record reference, reason."],
    ],
     "Migration, Legacy Data & Master Data Reconciliation principal entities."),
    ("h2", "34.4 Migration Flow"),
    ("flow",
     [
        "Legacy Source inventoried with owner and decommission status",
        "Legacy Record extracted, original identifier retained",
        "Mapping Rule applies field-to-canonical Transformation",
        "Canonical Match attempted via Ch.4's identity-resolution rules",
        "Match Confidence/State recorded — ambiguous matches held for human confirmation, never forced",
        "Migration Batch completes with Exceptions explicitly listed, not silently dropped",
     ],
     "Legacy-to-canonical migration and reconciliation flow."),
    ("h2", "34.5 Provenance Through Migration"),
    ("p",
     "A migrated canonical fact retains a Lineage Record (Ch.25) back to its Legacy Record and "
     "original Legacy Source identifier permanently — migration is a transformation, not a fresh, "
     "unprovenanced canonical fact."),
    ("h2", "34.6 Failure / Exception Semantics"),
    ("p",
     "A Legacy Record that cannot be matched to any canonical entity, and does not meet the bar for "
     "creating a new one, becomes an Exception retained for later manual reconciliation, never "
     "silently excluded from the migrated dataset."),
    ("trace002", "Depends on NCIE-002 Ch.6 (acquisition/validation reuse) and Ch.5 (canonical entity registry); introduces no new NCIE-002 architecture."),
    ("review", [
        ("SOURCE_DISCOVERY", "Inventory legacy systems that require migration and their current data owners."),
        ("INSTITUTIONAL", "Confirm migration priorities and required historical depth (how far back must legacy data be migrated)."),
        ("INSTITUTIONAL", "Confirm acceptable manual-reconciliation procedures for Exceptions."),
    ]),
    ("h2", "34.7 Acceptance Criteria"),
    ("bullets", [
        "A sampled migrated record demonstrably retains its original Legacy Source identifier and full Transformation lineage.",
        "An ambiguous legacy match is demonstrably held for human confirmation rather than auto-merged.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 35 — Data Performance, Partitioning, Archival & Scalability
# ---------------------------------------------------------------------------
BLOCKS[35] = [
    ("h2", "35.1 Purpose"),
    ("p", "Defines how the data layer handles large current and historical volumes without corrupting "
         "semantics, implementing NCIE-002 Ch.30's capacity model at the data-design level."),
    ("h2", "35.2 Semantic Definition"),
    ("bullets", [
        "Hot/Warm/Cold storage tiering changes performance characteristics, never meaning — a Cold-tier canonical fact is exactly as authoritative as the same fact in Hot tier.",
        "Partitioning must preserve cross-period traceability — a query spanning a partition boundary must still return correct, complete results.",
        "Optimisation (materialised views, caches) must never mix current and historical versions of the same bitemporal fact (Ch.5).",
    ]),
    ("h2", "35.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Partition Strategy", "entity family reference, partition key (typically operator/geography/time), rationale."],
        ["Indexing", "entity/field reference, index type, purpose."],
        ["Hot / Warm / Cold Tier", "entity family reference, tier, transition rule (age/access-frequency based)."],
        ["Archive Retrieval", "archived object reference (Ch.31), retrieval SLA, requesting actor."],
        ["Aggregation / Materialization", "source entity reference, aggregation logic reference, refresh policy — never itself canonical (Ch.32 §32.5)."],
        ["Capacity Metadata", "entity family reference, current volume, growth rate, projected capacity need."],
        ["Performance SLO", "entity family/operation reference, target latency/throughput (Ch.30's NCIE-002 targets translated to data-layer terms)."],
    ],
     "Data Performance, Partitioning, Archival & Scalability principal entities."),
    ("h2", "35.4 Tiering Does Not Change Meaning"),
    ("p",
     "A Hot/Warm/Cold Tier transition is purely a storage-location and retrieval-latency decision; it "
     "never triggers a schema change, a classification change, or a semantic reinterpretation of the "
     "underlying canonical fact — those remain governed exclusively by Chapters 2, 5 and 31."),
    ("h2", "35.5 Partition-Spanning Query Correctness"),
    ("p",
     "The Partition Strategy for any entity family bitemporally significant (Ch.5 §5.5) must ensure a "
     "decision-time reconstruction (Ch.25) spanning multiple partitions returns a complete, correctly "
     "ordered result — partitioning is a physical concern that must not silently truncate a logical "
     "query's correctness."),
    ("h2", "35.6 Failure / Exception Semantics"),
    ("p",
     "An Archive Retrieval request that cannot meet its stated SLA is surfaced as a degraded-status "
     "response, never a silent delay presented as normal performance."),
    ("trace002", "Directly implements NCIE-002 Ch.30 in full (capacity model, performance targets) at the data layer."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm expected data volumes and retention horizons per entity family."),
        ("INSTITUTIONAL", "Confirm performance targets (translate NCIE-002 Ch.30 §30.2's proposed baseline into per-entity-family SLOs)."),
        ("INSTITUTIONAL", "Confirm archive-retrieval SLA expectations for Cold-tier data."),
    ]),
    ("h2", "35.7 Acceptance Criteria"),
    ("bullets", [
        "A decision-time reconstruction spanning a partition boundary is demonstrably complete and correctly ordered.",
        "A Hot-to-Cold tier transition is demonstrably invisible to a consumer querying by canonical meaning alone.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 36 — Data Security & Sovereignty Controls
# ---------------------------------------------------------------------------
BLOCKS[36] = [
    ("h2", "36.1 Purpose"),
    ("p", "Defines technical data-layer protections for confidentiality, integrity and jurisdictional "
         "control, implementing NCIE-002 Ch.26 at the data-model level."),
    ("h2", "36.2 Semantic Definition"),
    ("bullets", [
        "Encryption and masking are distinct controls — encryption protects data at rest/in transit; masking/tokenization controls what a given viewer sees regardless of encryption state.",
        "Sensitive semantic/vector indexing (Ch.20's ARGUS retrieval, Ch.32's Vector Index) requires design distinct from ordinary indexing, since embedding sensitive content can make it searchable in ways ordinary access control does not anticipate.",
        "Data residency follows NCA policy — no entity in this document assumes cross-border processing as a default.",
    ]),
    ("h2", "36.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Encryption", "object/store reference, algorithm, key reference."],
        ["Key Reference", "key identifier — actual key material is never stored alongside the data it protects (managed per NCIE-002 Ch.26 §26.7)."],
        ["Masking / Tokenization", "field reference, masking method, applicable viewer scope (Ch.26 of this document)."],
        ["Protected Reveal", "masked field reference, revealing actor, authorization reference (Ch.26), audited (Ch.27)."],
        ["Database Access Policy", "store reference, permitted access pattern, enforcement point."],
        ["Sovereignty / Residency Metadata", "store reference, jurisdiction, hosting constraint."],
        ["DLP Control", "scope, rule (e.g. block export of protected identity in bulk), enforcement point."],
        ["Sensitive-Index Policy", "index reference (Ch.32), classification-aware segmentation rule, exclusion list."],
    ],
     "Data Security & Sovereignty Controls principal entities."),
    ("h2", "36.4 Sensitive-Index Design Requirement"),
    ("p",
     "A Vector Index or Search Index that could include protected/sensitive content must apply "
     "Sensitive-Index Policy segmentation (index-per-classification-tier, security metadata filtering, "
     "or post-retrieval authorization, per NCIE-002 Ch.26 §26.3) — embedding a protected field is "
     "never permitted to make that content globally searchable to any authenticated user."),
    ("h2", "36.5 Protected Reveal as an Audited Action"),
    ("p",
     "Every instance of a masked field being shown unmasked to a viewer is a Protected Reveal record, "
     "which is itself an Audit Event (Ch.27) with a Sensitive-Access Marker — masking is not "
     "considered a security control unless every bypass of it is individually accountable."),
    ("h2", "36.6 Failure / Exception Semantics"),
    ("p",
     "If Key Reference resolution fails (key management unavailable), an operation requiring "
     "decryption of protected/sensitive data fails closed rather than falling back to an unencrypted "
     "path (NCIE-002 Ch.28's parallel resilience principle applied here)."),
    ("trace002", "Directly implements NCIE-002 Ch.26 in full."),
    ("review", [
        ("LEGAL", "Confirm sovereignty/residency requirements with NCA legal/IT security leadership."),
        ("INSTITUTIONAL", "Confirm encryption/key-management standards and rotation policy."),
        ("LEGAL", "Confirm which data classes may use external/cloud processing, if any."),
    ]),
    ("h2", "36.7 Acceptance Criteria"),
    ("bullets", [
        "A protected field embedded in a Vector Index is demonstrably not retrievable by a role unauthorized for that field.",
        "Every sampled Protected Reveal demonstrably produces a corresponding Sensitive-Access-Marked Audit Event.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 37 — Data Observability, Reconciliation & Operational Management
# ---------------------------------------------------------------------------
BLOCKS[37] = [
    ("h2", "37.1 Purpose"),
    ("p", "Defines operational telemetry for freshness, pipeline health, schema drift and "
         "reconciliation, implementing NCIE-002 Ch.27's Observability Platform at the data layer."),
    ("h2", "37.2 Semantic Definition"),
    ("bullets", [
        "Pipeline health (is ingestion working) is not sector health (is the underlying network/revenue/fraud situation good) — this chapter's entities feed, but never substitute for, Ch.7/Ch.18's substantive condition entities.",
        "Source update time and processing time are kept distinct so a lag can be attributed to the source or to NCIE's own pipeline correctly.",
    ]),
    ("h2", "37.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Pipeline Status", "pipeline reference, current state, last-run outcome."],
        ["Freshness Metric", "See Ch.29 — this chapter's operational view over Freshness State."],
        ["Ingestion Lag", "source reference (Ch.6), source update time, NCIE processing time, computed lag."],
        ["Schema Drift Event", "source reference, expected schema version (Ch.33), detected deviation, timestamp."],
        ["Lineage Exception", "See Ch.25 — broken/incomplete lineage surfaced as an operational alert."],
        ["Reconciliation Job", "scope, schedule, last-run result — the operational counterpart to Ch.23/Ch.27's Reconciliation State."],
        ["Operational Alert", "category, severity, triggering condition, escalation reference (Ch.18 §18.4 pattern reused operationally)."],
        ["Data SLA / SLO", "entity family/pipeline reference, target, current attainment."],
    ],
     "Data Observability, Reconciliation & Operational Management principal entities."),
    ("h2", "37.4 Operational vs Substantive Signals"),
    ("p",
     "An Operational Alert for a data-pipeline issue is routed to data engineering/operations owners "
     "(Ch.26), while a substantive Condition/Alert (Ch.18) is routed to domain analysts — the two "
     "alerting paths share infrastructure (Ch.28's Event/Notification model) but are never merged "
     "into one undifferentiated alert stream."),
    ("h2", "37.5 Reconciliation Scheduling"),
    ("p",
     "A Reconciliation Job runs on a defined schedule per entity family (e.g. daily for Revenue "
     "inputs, per Ch.12) and produces a result that feeds both Ch.29's Quality Issue tracking and this "
     "chapter's Data SLA/SLO attainment metric."),
    ("h2", "37.6 Failure / Exception Semantics"),
    ("p",
     "A Schema Drift Event blocks affected Source Object References from validation (shared mechanism "
     "with Ch.29 §29.6) and raises an Operational Alert simultaneously, so the pipeline issue is "
     "visible to operators even before an analyst notices missing domain data."),
    ("trace002", "Directly implements NCIE-002 Ch.27 in full (observability platform, health signal categories)."),
    ("review", [
        ("INSTITUTIONAL", "Confirm operational owners and escalation paths per pipeline."),
        ("INSTITUTIONAL", "Confirm freshness expectations per domain (feeds Ch.24 Rule Version thresholds)."),
        ("INSTITUTIONAL", "Confirm acceptable reconciliation windows per entity family."),
    ]),
    ("h2", "37.7 Acceptance Criteria"),
    ("bullets", [
        "A simulated Schema Drift Event demonstrably raises an Operational Alert distinct from any substantive domain Condition/Alert.",
        "A Reconciliation Job's result is demonstrably reflected in both Ch.29's Quality Issue tracking and this chapter's Data SLA/SLO metric.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 38 — Data Testing, Verification & Acceptance
# ---------------------------------------------------------------------------
BLOCKS[38] = [
    ("h2", "38.1 Purpose"),
    ("p", "Defines how the data architecture and dictionary are verified before implementation "
         "baseline approval, implementing NCIE-002 Ch.31's test-architecture principles at the "
         "data-model level."),
    ("h2", "38.2 Semantic Definition"),
    ("p",
     "Testing here covers semantics, not only database constraints — a passing schema-validation test "
     "does not by itself demonstrate that temporal, lineage, or authorization behaviour is correct. "
     "Temporal/Decision-Time behaviour, security/lineage and migration each require dedicated test "
     "categories, per the authoritative handover instructions."),
    ("h2", "38.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Schema Tests", "verify structural conformance to Ch.33 contracts."],
        ["Constraint Tests", "verify nullability, enumeration, classification-tier rules (Ch.2, Ch.30, Ch.31)."],
        ["Temporal Tests", "verify bitemporal storage, correction/revision behaviour and effective dating (Ch.5, Ch.24)."],
        ["Lineage Tests", "verify Lineage Record completeness and decision-time reconstruction correctness (Ch.25)."],
        ["Authorization / Privacy Tests", "verify field-level, room-level and classification-aware access rules (Ch.26, Ch.21, Ch.31, Ch.36)."],
        ["Migration Tests", "verify legacy-to-canonical mapping, provenance retention and ambiguous-match handling (Ch.34)."],
        ["Reconciliation Tests", "verify Ch.37's reconciliation jobs and Ch.29's quality-issue detection."],
        ["Acceptance Evidence", "test case reference, executed-by, date, result, defect reference — shared structure with NCIE-002 Ch.31."],
    ],
     "Data Testing, Verification & Acceptance principal entities."),
    ("h2", "38.4 Mandatory Test Categories"),
    ("p",
     "Every domain chapter's principal entities (Ch.7-Ch.22) must have at least one Temporal Test "
     "(bitemporal correctness), one Authorization/Privacy Test (field/classification enforcement) and "
     "one Lineage Test (provenance completeness) before that chapter is eligible for Approved status "
     "(front matter §0.3)."),
    ("h2", "38.5 Relationship to NCIE-002 Acceptance"),
    ("p",
     "This chapter's Acceptance Evidence entity shares its structure with NCIE-002 Ch.31's RTM "
     "acceptance record, so a single evidence repository can serve both documents' traceability needs "
     "without duplication."),
    ("h2", "38.6 Failure / Exception Semantics"),
    ("p",
     "A failed mandatory test category for a chapter blocks that chapter's status from advancing "
     "beyond IN DEVELOPMENT — FOR HUMAN REVIEW, mirroring NCIE-001 §18.242's no-pass-without-"
     "corrective-evidence rule."),
    ("trace002", "Directly implements NCIE-002 Ch.31 in full, adapted to data-model-specific test categories."),
    ("review", [
        ("INSTITUTIONAL", "Confirm acceptance authorities for NCIE-003 test results."),
        ("INSTITUTIONAL", "Confirm required test environments and data (masked, per NCIE-002 Ch.29 §29.3 convention)."),
        ("INSTITUTIONAL", "Confirm which domain users must sign off on which chapters' Acceptance Evidence."),
    ]),
    ("h2", "38.7 Acceptance Criteria"),
    ("bullets", [
        "Every domain chapter (Ch.7-Ch.22) demonstrably has at least one Temporal, one Authorization/Privacy and one Lineage Test recorded.",
        "No chapter is shown as Approved without corresponding passing Acceptance Evidence.",
    ]),
]
