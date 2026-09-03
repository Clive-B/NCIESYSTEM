"""NCIE-003 content batch: Chapters 7-14 (network, field-test and commercial domain data models)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 7 — Network Intelligence Data Model
# ---------------------------------------------------------------------------
BLOCKS[7] = [
    ("h2", "7.1 Purpose"),
    ("p",
     "Defines the canonical data objects for network performance monitoring (PM) and QoS "
     "intelligence, implementing NCIE-002 Ch.7's KPI Engine and Investigation Service."),
    ("h2", "7.2 Semantic Definition"),
    ("bullets", [
        "PM availability (whether expected files/records arrived, Green/Amber/Grey) is a distinct property from QoS interpretation (whether the KPI value itself is good or bad) — the two are never merged into one status.",
        "District-level degradation evidence never becomes cell-level evidence merely by geographic containment; a cell is only shown as degraded when cell-level PM data supports it (NCIE-002 Ch.7 §7.4).",
    ]),
    ("h2", "7.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Operator", "canonical ID (Ch.4), name, licence reference, status."],
        ["Site", "canonical ID, operator reference, location reference (Ch.8)."],
        ["Cell", "canonical ID, site reference, technology, topology version (Ch.8), status."],
        ["Technology", "enumeration (2G/3G/4G/5G and successors), governed reference data."],
        ["KPI", "name, formula reference (Ch.24), unit, effective definition version."],
        ["PM Observation", "cell reference, KPI reference, date/period, value, source reference (Ch.6), coverage status."],
        ["Baseline", "KPI reference, scope (cell/site/district), reference value, effective period."],
        ["Threshold", "KPI reference, threshold value, severity, effective period (Ch.24)."],
        ["Network Condition", "scope, KPI(s) involved, detected state, evidence references — the Ch.18 Condition object as realised for the Network domain."],
    ],
     "Network Intelligence principal entities."),
    ("h2", "7.4 Lifecycle and Relationships"),
    ("flow",
     [
        "PM Observation ingested per cell/KPI/period (Ch.6)",
        "Coverage status computed (Green/Amber/Grey)",
        "KPI value compared to Threshold/Baseline",
        "District-level degradation detected",
        "Topology resolution to constituent Cells (Ch.8)",
        "Cell-level PM Observation confirms or refutes degradation",
        "Network Condition raised only on cell-level evidence",
     ],
     "District-to-cell network investigation data flow."),
    ("h2", "7.5 Temporal Semantics"),
    ("p", "PM Observation carries occurrence period (the measured interval), acquisition time and "
         "knowledge time (Ch.5). Baseline and Threshold are effective-dated (Ch.24) so a KPI's "
         "definition of \"good\" can change over time without corrupting historical evaluations."),
    ("h2", "7.6 Validation and Classification"),
    ("bullets", [
        "A PM Observation failing source/date/scope validation (Ch.6) is quarantined, never silently included in KPI aggregation.",
        "Network Condition and PM Observation are internal/operational classification by default; no protected-identity data is modelled in this chapter.",
    ]),
    ("h2", "7.7 Failure / Exception Semantics"),
    ("p",
     "A cell with no PM Observation for the period is modelled as coverage status Grey with KPI value "
     "Unknown (Ch.2 vocabulary) — never defaulted to a passing or failing KPI value."),
    ("trace002", "Directly implements NCIE-002 Ch.7 in full (NMS Adapters, PM Service, KPI Engine, Investigation Service, coverage-status model)."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm available network source fields per operator NMS/PM export format."),
        ("INSTITUTIONAL", "Confirm the authoritative KPI set, formulas and units (Ch.24 Rule Service will hold the governed values once confirmed)."),
        ("SOURCE_DISCOVERY", "Confirm cell/site master-data authority and update process — is there an existing NCA or operator-supplied cell master list?"),
    ]),
    ("h2", "7.8 Acceptance Criteria"),
    ("bullets", [
        "A synthetic district degradation with no cell-level PM data does not produce a Network Condition; the same scenario with confirming cell-level PM Observations does.",
        "A cell missing PM data for a period shows Grey/Unknown, never a false passing KPI.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 8 — Topology, GIS & Spatial Data Model
# ---------------------------------------------------------------------------
BLOCKS[8] = [
    ("h2", "8.1 Purpose"),
    ("p", "Defines the geographic and network-topology objects used for mapping, spatial analysis and "
         "the Madina-style place-to-cell resolution flow (NCIE-002 Ch.8 §8.3)."),
    ("h2", "8.2 Semantic Definition"),
    ("bullets", [
        "Spatial precision is an explicit attribute of every location fact, not an assumed property of the coordinate value's apparent decimal length.",
        "National/operator-only aggregate data must never be placed on a map at a precision it does not actually possess.",
        "Anti-Fraud location evidence (Ch.15) is a distinct, more strongly controlled data class than ordinary network/topology location.",
    ]),
    ("h2", "8.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Region / District", "canonical ID (Ch.4), name, parent geography reference, boundary version."],
        ["Site Geometry", "site reference (Ch.7), coordinates, coordinate reference system, precision."],
        ["Cell Location", "cell reference (Ch.7), geometry, sector/azimuth where applicable, precision."],
        ["Coverage Area", "cell/site reference, derived polygon, method, effective period."],
        ["Coordinate Reference System", "governed reference data; the single system canonical geometry is stored in."],
        ["Spatial Precision", "enumeration (exact/approximate/aggregate-only), applies to any location fact."],
        ["Topology Relation", "cell-to-geography and cell-to-site relationships, versioned (Ch.5)."],
    ],
     "Topology, GIS & Spatial principal entities."),
    ("h2", "8.4 Temporal Semantics"),
    ("p", "Topology Relation and Coverage Area are versioned by effective period so historical topology "
         "(\"what cells covered this district as of date X\") is reconstructable, per NCIE-002 Ch.8's "
         "historical-topology requirement."),
    ("h2", "8.5 Place-to-Cell Resolution Data Flow"),
    ("rel",
     [
        ("Natural-language place name", "resolves to", "Region/District (canonical geography)"),
        ("Region/District", "resolves via Topology Relation to", "constituent Cells"),
        ("Cells", "supply", "PM Observation (Ch.7)"),
    ],
     "Place-to-cell resolution supported by the topology data model."),
    ("h2", "8.6 Classification and Security"),
    ("p",
     "Cell Location and Coverage Area default to internal classification. Any location fact "
     "associated with Anti-Fraud investigation (Ch.15) is reclassified sensitive and is never joined "
     "into a general-purpose map layer query without passing through Ch.15's sensitive-join controls."),
    ("h2", "8.7 Failure / Exception Semantics"),
    ("p",
     "An ambiguous place-name resolution (matching more than one Region/District candidate) is "
     "returned as a candidate set for human disambiguation, never silently resolved to the first "
     "match (NCIE-002 Ch.8 §8.6)."),
    ("trace002", "Directly implements NCIE-002 Ch.8 in full (Topology Service, Spatial Database, Geocoder, Map API, historical topology, sensitive-layer permission filtering)."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm authoritative GIS datasets (region/district boundaries, site coordinates) currently available at NCA/operators."),
        ("INSTITUTIONAL", "Confirm coordinate system and precision standards to be used as the canonical storage CRS."),
        ("INSTITUTIONAL", "Confirm which users/roles may see sensitive location layers (cross-references NCIE-002 Ch.4 role model)."),
    ]),
    ("h2", "8.8 Acceptance Criteria"),
    ("bullets", [
        "A historical Topology Relation query returns the topology as it existed at a specified prior date.",
        "A location fact lacking real precision is never displayed at a finer precision than it actually has.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 9 — QoS Campaign & Drive-Test Data Model
# ---------------------------------------------------------------------------
BLOCKS[9] = [
    ("h2", "9.1 Purpose"),
    ("p", "Defines field-testing campaigns, routes, devices, test points and measurements, implementing "
         "NCIE-002 Ch.9's Campaign Repository and Matcher."),
    ("h2", "9.2 Semantic Definition"),
    ("bullets", [
        "Campaign metadata (operator, date, route, technology, method) is modelled separately from its Measurements, since metadata governs how measurements should be interpreted.",
        "Device, method and software/firmware version are preserved per campaign so measurement comparability can be judged rather than assumed.",
    ]),
    ("h2", "9.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Campaign", "canonical ID, operator reference, date range, route reference, technology, methodology reference, status."],
        ["Route", "geometry, associated Region/District references (Ch.8)."],
        ["Test Device", "make/model, firmware/software version."],
        ["Test Point", "campaign reference, geolocation (Ch.8 spatial precision), timestamp."],
        ["Measurement", "test point reference, metric reference, value, unit."],
        ["Metric", "governed reference data (e.g. RSRP, throughput, call-setup success)."],
        ["Methodology", "description, version, applicable metrics."],
        ["Campaign Status", "coverage/completeness, evidential status."],
    ],
     "QoS Campaign & Drive-Test principal entities."),
    ("h2", "9.4 Relationships and Geography Linkage"),
    ("p",
     "Measurements link to canonical Cell (Ch.7) and Region/District (Ch.8) references via the "
     "Matcher process (NCIE-002 Ch.9 §9.3), never via free-text location strings. Latest-applicable "
     "campaign resolution is geography-specific, per NCIE-002 Ch.9 §9.3 — a newer campaign in one "
     "district does not make an older, unrelated district's campaign stale by association."),
    ("h2", "9.5 Temporal and Provenance Semantics"),
    ("p",
     "Every Measurement retains campaign date, device and methodology, so age and comparability are "
     "always derivable, not assumed. Campaigns are never edited in place after ingestion; a correction "
     "is a new Campaign version with lineage to the original (Ch.25)."),
    ("h2", "9.6 Classification"),
    ("p", "Campaign and Measurement data default to internal classification unless a specific campaign "
         "is flagged sensitive by its owning source agreement."),
    ("h2", "9.7 Failure / Exception Semantics"),
    ("p",
     "Route geometry that fails to match any known geography is retained as unmatched rather than "
     "discarded, pending manual topology reconciliation (mirrors NCIE-002 Ch.9 §9.6)."),
    ("trace002", "Directly implements NCIE-002 Ch.9 in full (Campaign Repository, Geometry Store, Matcher, Analytics Service)."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm existing drive-test systems, vendors and export formats."),
        ("INSTITUTIONAL", "Confirm mandatory campaign metadata for a campaign to be treated as evidential."),
        ("LEGAL", "Confirm retention and evidential status of drive-test outputs for regulatory purposes."),
    ]),
    ("h2", "9.8 Acceptance Criteria"),
    ("bullets", [
        "For a geography sampled by multiple campaigns over time, the latest-applicable campaign is correctly identified while all historical campaigns remain retrievable.",
        "Unmatched route geometry is demonstrably retained and flagged rather than dropped.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 10 — Incident Intelligence Data Model
# ---------------------------------------------------------------------------
BLOCKS[10] = [
    ("h2", "10.1 Purpose"),
    ("p", "Defines reported and observed incidents, affected scope, restoration and incident timelines, "
         "implementing NCIE-002 Ch.10's Mailbox Connector, Extractor, Threading Service and Incident Workflow."),
    ("h2", "10.2 Semantic Definition"),
    ("bullets", [
        "Operator-reported incident state and independently observed (NMS-corroborated) state are distinct properties on the same Incident, never merged into one status.",
        "Occurrence time (when the outage actually began) and reporting time (when the operator's email arrived) are both preserved.",
        "Restoration Reported (operator claims restored) is distinct from Restoration Verified (NMS evidence corroborates it); an Incident does not close on the former alone.",
    ]),
    ("h2", "10.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Incident", "canonical ID, category, occurrence time, reporting time, status, reported vs verified restoration."],
        ["Incident Report", "incident reference, source email reference (Ch.6, Ch.17 evidence), extracted fields, thread reference."],
        ["Affected Operator", "incident reference, operator reference (Ch.7)."],
        ["Affected Network Object", "incident reference, cell/site reference (Ch.7)."],
        ["Affected Geography", "incident reference, region/district reference (Ch.8)."],
        ["Restoration Event", "incident reference, reported time, verification method, verified time (nullable/Unknown)."],
        ["Incident Update", "incident reference, source report reference, update content, timestamp."],
        ["Incident Status", "governed enumeration (open/monitoring/restoration-claimed/restoration-verified/closed)."],
    ],
     "Incident Intelligence principal entities."),
    ("h2", "10.4 Lifecycle"),
    ("flow",
     [
        "Incident Report received (original email retained as Evidence, Ch.17)",
        "Extractor produces structured fields",
        "Threading Service links to existing Incident or opens new one",
        "Restoration Reported recorded from operator update",
        "Restoration Verified checked against Network Condition/PM Observation (Ch.7)",
        "Incident closes only once verified, or remains open pending verification",
     ],
     "Incident lifecycle from report to verified closure."),
    ("h2", "10.5 Provenance"),
    ("p",
     "Every Incident Update retains its source Incident Report and, transitively, the original email "
     "evidence — the email itself is never modified, consistent with NCIE-002 Ch.10 §10.5."),
    ("h2", "10.6 Failure / Exception Semantics"),
    ("p",
     "A restoration claim unsupported by NMS evidence keeps the Incident in restoration-claimed "
     "status, not closed — closure requires either verification or an explicit, audited manual "
     "override with recorded justification."),
    ("trace002", "Directly implements NCIE-002 Ch.10 in full."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm incident reporting workflow and mailbox structure currently used by operators."),
        ("SOURCE_DISCOVERY", "Confirm operator incident email fields available for extraction."),
        ("INSTITUTIONAL", "Confirm what constitutes validated restoration for closure purposes (i.e. which NMS evidence is sufficient)."),
    ]),
    ("h2", "10.7 Acceptance Criteria"),
    ("bullets", [
        "A multi-message incident thread is demonstrably consolidated into one Incident with full lineage to each source email.",
        "A restoration claim unsupported by NMS evidence is demonstrably kept open.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 11 — Traffic Intelligence Data Model
# ---------------------------------------------------------------------------
BLOCKS[11] = [
    ("h2", "11.1 Purpose"),
    ("p", "Defines International, Off-Net and On-Net traffic observations and their reporting semantics, "
         "feeding Revenue calculation (Ch.12) and cross-domain fusion (Ch.19)."),
    ("h2", "11.2 Semantic Definition"),
    ("p",
     "Traffic type, direction, unit and reporting period are never implicit — every Traffic "
     "Observation states all four explicitly, since Revenue calculation correctness depends on them "
     "(NCIE-002 Ch.11 §11.2)."),
    ("h2", "11.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Traffic Observation", "canonical ID, operator reference (Ch.7), traffic type, direction, period, volume, unit, source reference (Ch.6), coverage status."],
        ["Traffic Type", "governed enumeration (International/Off-Net/On-Net)."],
        ["Direction", "governed enumeration (incoming/outgoing, where applicable)."],
        ["Unit", "governed reference data (minutes, MB, etc.)."],
        ["Period", "reporting interval, effective time semantics (Ch.5)."],
        ["Revision", "traffic observation reference, prior value, reason, actor, timestamp (Ch.25 Correction relationship)."],
        ["Coverage State", "expected-vs-received completeness per operator/period."],
    ],
     "Traffic Intelligence principal entities."),
    ("h2", "11.4 Relationships"),
    ("rel",
     [
        ("Traffic Observation", "is an input to", "Revenue Calculation (Ch.12)"),
        ("Traffic Observation", "is correlated by", "Cross-Domain Fusion (Ch.19)"),
        ("Revision", "supersedes (with lineage)", "prior Traffic Observation"),
     ],
     "Traffic Intelligence relationships to Revenue and Fusion."),
    ("h2", "11.5 Temporal and Provenance Semantics"),
    ("p",
     "A Revision never overwrites the original Traffic Observation; it creates a new version with a "
     "Correction relationship (Ch.25) so a Revenue calculation performed before the revision remains "
     "reproducible against the value it actually used, per Ch.5's bitemporal principle applied to a "
     "Revenue-relevant fact."),
    ("h2", "11.6 Failure / Exception Semantics"),
    ("p",
     "A missing period for an operator is modelled as Unknown coverage, never as zero traffic — this "
     "is load-bearing for Chapter 12's Revenue calculation, which must not silently compute a low "
     "Revenue figure from an absent Traffic Observation."),
    ("trace002", "Directly implements NCIE-002 Ch.11 in full."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm source granularity and frequency of traffic reporting per operator."),
        ("INSTITUTIONAL", "Confirm units and direction conventions to standardise across operators."),
        ("PROPOSED", "Revisions are proposed to always be modelled as new versions with a Correction relationship (§11.5), never in-place overwrites; this is technically defensible from Ch.5/Ch.25 alone."),
    ]),
    ("h2", "11.7 Acceptance Criteria"),
    ("bullets", [
        "A revised Traffic Observation is demonstrably retrievable in both its pre- and post-revision form.",
        "A missing period is demonstrably distinguishable from a zero-volume period in every consuming query.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 12 — Revenue Intelligence & Billing Verification Data Model
# ---------------------------------------------------------------------------
BLOCKS[12] = [
    ("h2", "12.1 Purpose"),
    ("p", "Defines revenue calculation inputs/results, the international incoming traffic surcharge "
         "rule, billing verification and reconciliation, implementing NCIE-002 Ch.12."),
    ("h2", "12.2 Semantic Definition"),
    ("p",
     "Calculated Revenue (derived deterministically by NCIE from Traffic and the effective-dated "
     "surcharge Rule) and Reported Revenue (supplied by the operator's Billing system) are distinct "
     "entities. A Reconciliation Difference between them is a labelled difference, never an automatic "
     "assertion of underpayment (NCIE-002 Ch.12 §12.4)."),
    ("h2", "12.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Revenue Calculation", "canonical ID, operator reference, period, traffic input reference(s) (Ch.11), surcharge Rule Version reference (Ch.24), calculated value, currency, calculation version."],
        ["Traffic Input Reference", "revenue calculation reference, exact Traffic Observation version used (immutable pointer, per Ch.5 §5.6)."],
        ["Surcharge Rule", "See Ch.24 — this chapter references, and does not redefine, the Rule/Rule Version/Parameter entities."],
        ["Billing Verification", "operator reference, period, reported value, currency, source reference."],
        ["Reconciliation", "revenue calculation reference, billing verification reference, comparison basis."],
        ["Reconciliation Difference", "reconciliation reference, difference value, status (candidate/explained/escalated), linked Case reference (Ch.16) if escalated."],
    ],
     "Revenue Intelligence & Billing Verification principal entities."),
    ("h2", "12.4 The Surcharge Rate Is Not a Constant"),
    ("p",
     "The international incoming traffic surcharge — currently USD 0.19 (19 US cents) — is "
     "represented exclusively through the governed, effective-dated Rule / Rule Version / Parameter "
     "structure defined in Chapter 24. It is never stored as a literal constant in this chapter's "
     "entities, in application code, or in any UI configuration outside that governed structure. A "
     "Revenue Calculation references the specific Rule Version that was effective at its calculation "
     "period, so historical calculations remain correct and reproducible after the rate changes."),
    ("h2", "12.5 Relationships and Cardinality"),
    ("bullets", [
        "One Revenue Calculation references exactly one effective Surcharge Rule Version and one-to-many Traffic Input References.",
        "One Reconciliation compares exactly one Revenue Calculation with one Billing Verification for the same operator/period.",
        "A Reconciliation Difference may reference zero-or-one Case (Ch.16) if and when it is escalated to regulatory workflow.",
    ]),
    ("h2", "12.6 Provenance and Temporal Semantics"),
    ("p",
     "Every Revenue Calculation is fully reproducible from its stored Traffic Input References and "
     "Rule Version reference alone (Ch.5, Ch.25) — recalculating with the same inputs must always "
     "yield the same result, which is the data-model precondition for NCIE-002 Ch.12's deterministic "
     "calculation requirement."),
    ("h2", "12.7 Failure / Exception Semantics"),
    ("p",
     "A Revenue Calculation cannot be produced for a period with Unknown Traffic coverage (Ch.11); it "
     "is marked not-calculable rather than computed from an implicit zero."),
    ("trace002", "Directly implements NCIE-002 Ch.12 in full, and depends on Ch.24's Rule/Rule Version/Parameter model for the surcharge rate."),
    ("review", [
        ("LEGAL", "Confirm the exact surcharge formula, legal basis and charging basis (per-minute, per-call, or other) with NCA Legal/Revenue Assurance."),
        ("INSTITUTIONAL", "Confirm who may change the surcharge rate and who approves a rate change, to populate Ch.24's Rule approval workflow."),
        ("SOURCE_DISCOVERY", "Confirm billing-verification source system and the reconciliation workflow currently used, if any."),
    ]),
    ("h2", "12.8 Acceptance Criteria"),
    ("bullets", [
        "A surcharge rate change is demonstrably effective-dated: Revenue Calculations before the change date reference the old Rule Version, after use the new one.",
        "A Reconciliation Difference is demonstrably surfaced with basis/unit and does not auto-populate a Case without explicit escalation.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 13 — Mobile Money Intelligence Data Model
# ---------------------------------------------------------------------------
BLOCKS[13] = [
    ("h2", "13.1 Purpose"),
    ("p", "Defines daily aggregate Mobile Money transfer amounts sent and received on each network, "
         "implementing NCIE-002 Ch.13. Subscriber-level data is out of scope, matching NCIE-001/002."),
    ("h2", "13.2 Semantic Definition"),
    ("p",
     "Sent and Received are modelled as separate measures on the same daily aggregate, never combined "
     "into a single net figure that would obscure their individual coverage/quality state."),
    ("h2", "13.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Mobile Money Aggregate", "canonical ID, operator/service reference, reporting date, sent amount, received amount, currency, source reference (Ch.6), coverage/revision state."],
        ["Operator/Service", "reference to Operator (Ch.7) plus service identifier if the operator offers more than one Mobile Money service."],
    ],
     "Mobile Money Intelligence principal entities (deliberately minimal — no subscriber-level entity exists in this schema)."),
    ("h2", "13.4 Schema-Level Exclusion of Subscriber Data"),
    ("p",
     "The Mobile Money Aggregate entity has no subscriber-identifying attribute, and no relationship "
     "path in this chapter connects it to any Protected Identity entity (Ch.14). This is a structural "
     "exclusion, not merely an access-control rule, so a future adapter cannot introduce "
     "subscriber-level data without a deliberate schema change to this chapter (implements NCIE-002 "
     "Ch.13 §13.4 at the data-model level)."),
    ("h2", "13.5 Temporal Semantics"),
    ("p", "Mobile Money Aggregate carries reporting date, acquisition time and knowledge time (Ch.5); "
         "a missing day is Unknown coverage, never zero."),
    ("h2", "13.6 Failure / Exception Semantics"),
    ("p", "A revised aggregate for a prior date follows the same Correction relationship pattern as "
         "Chapter 11's Traffic Revision — the prior value remains retrievable."),
    ("trace002", "Directly implements NCIE-002 Ch.13 in full, including its schema-level subscriber-data exclusion principle."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm source system, currency and daily cut-off time for Mobile Money aggregate reporting."),
        ("INSTITUTIONAL", "Confirm whether any additional approved aggregate measures (e.g. transaction counts) should be added to §13.3."),
    ]),
    ("h2", "13.7 Acceptance Criteria"),
    ("bullets", [
        "A schema inspection confirms no subscriber-identifying attribute or relationship path exists anywhere in this chapter's entities.",
        "A missing day's aggregate is demonstrably distinguishable from a zero-volume day.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 14 — SIM Registration Intelligence Data Model
# ---------------------------------------------------------------------------
BLOCKS[14] = [
    ("h2", "14.1 Purpose"),
    ("p", "Defines SIM registrations, identity type, countable registrations, configurable limits and "
         "registration exceptions, implementing NCIE-002 Ch.14."),
    ("h2", "14.2 Semantic Definition"),
    ("bullets", [
        "Ghana Card and Passport are distinct Identity Type values, never merged into one generic identity-document field, since their governed limits differ (§14.4).",
        "Raw identity values are Protected Identity References, structurally separate from the Registration count entity that uses them, so most queries never need to touch the protected reference at all.",
        "An identity exceeding its registration limit is a Registration Exception, not a fraud finding — culpability is never asserted by this entity's existence.",
    ]),
    ("h2", "14.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Registration", "canonical ID, SIM reference, protected identity reference, operator reference (Ch.7), status, effective date."],
        ["SIM", "canonical ID, operator reference, status."],
        ["Identity Type", "governed enumeration (Ghana Card / Passport)."],
        ["Protected Identity Reference", "canonical ID (Ch.4), identity type, protected value (field-level access-controlled per NCIE-002 Ch.4/Ch.26)."],
        ["Registration Status", "governed enumeration (active/inactive/ported/deregistered)."],
        ["Countable State", "registration reference, whether this registration counts toward the identity's limit at a given date (some statuses may be excluded by governed rule)."],
        ["Registration Rule", "See Ch.24 — limit value, identity type, effective period; this chapter references, not redefines, it."],
        ["Registration Exception", "protected identity reference, count at time of detection, applicable Registration Rule version, status (open/investigated/explained)."],
    ],
     "SIM Registration Intelligence principal entities."),
    ("h2", "14.4 Limits Are Governed Rules, Not Constants"),
    ("p",
     "The Ghana Card maximum (currently 10) and foreign-passport maximum (currently 3) are "
     "represented exclusively through Chapter 24's Rule / Rule Version / Parameter structure, keyed "
     "by Identity Type, exactly as Chapter 12 requires for the surcharge rate. A Registration "
     "Exception references the specific Registration Rule version effective at its detection date, "
     "so a later rule change does not retroactively reclassify historical exceptions."),
    ("h2", "14.5 Lifecycle"),
    ("flow",
     [
        "Registration recorded against Protected Identity Reference and SIM",
        "Countable State evaluated against current Registration Rule version",
        "Aggregate count per identity computed from Countable registrations",
        "Count compared to effective Registration Rule limit",
        "Registration Exception raised if count exceeds limit",
        "Exception routed to Regulatory Intelligence (Ch.16) for investigation, not automatic action",
     ],
     "Registration-to-exception detection lifecycle."),
    ("h2", "14.6 Classification and Security"),
    ("p",
     "Protected Identity Reference is field-level access-controlled and never appears in aggregate "
     "reporting views; only the Registration count (not the underlying identity value) is exposed "
     "there, per NCIE-002 Ch.4 §4.3 and Ch.14 §14.5."),
    ("h2", "14.7 Failure / Exception Semantics"),
    ("p",
     "An ambiguous cross-operator identity match (Ch.4 §4.4 generalised) is never auto-merged before "
     "computing the aggregate count; it is retained as an unresolved candidate pending human "
     "confirmation, since a false merge could wrongly trigger or suppress a Registration Exception."),
    ("trace002", "Directly implements NCIE-002 Ch.14 in full, and depends on Ch.4 (identity resolution) and Ch.24 (governed limits)."),
    ("review", [
        ("PROPOSED", "The current supplied limits of 10 (Ghana Card) and 3 (Passport) are proposed as the initial Ch.24 Rule Service values; this is technically consistent with NCIE-001/002 and does not require new discovery to state as an initial default."),
        ("INSTITUTIONAL", "Confirm the exact lifecycle states counted toward the limit (§14.3 Countable State) — e.g. does a ported-out SIM still count?"),
        ("LEGAL", "Confirm field-level protection scope for Protected Identity Reference — which roles may view unmasked values, and under what legal authority."),
    ]),
    ("h2", "14.8 Acceptance Criteria"),
    ("bullets", [
        "An identity exceeding the effective Registration Rule limit is demonstrably classified as a Registration Exception, not a fraud finding.",
        "A Registration Rule change is demonstrably effective-dated: exceptions detected before the change reference the prior rule version.",
    ]),
]
