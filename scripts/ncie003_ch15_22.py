"""NCIE-003 content batch: Chapters 15-22 (regulatory, evidence, situational,
ARGUS/collaborative and memory data models)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 15 — Anti-Fraud / SIMBOX Intelligence Data Model
# ---------------------------------------------------------------------------
BLOCKS[15] = [
    ("h2", "15.1 Purpose"),
    ("p", "Defines the data required to detect, investigate, locate and block SIMs associated with "
         "suspected SIMBOX activity, implementing NCIE-002 Ch.15's staged Anti-Fraud model."),
    ("h2", "15.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "Detection ≠ Confirmed Fraud — a SIMBOX Detection is a signal, never itself a fraud finding.",
        "Registered Identity ≠ Fraud Actor — the identity behind a Registration (Ch.14) is not asserted to be the operational fraud actor merely by association with a Suspected SIM.",
        "Blocking Requested ≠ Blocking Executed ≠ Blocking Verified — three distinct states, never collapsed into one 'blocked' flag.",
    ]),
    ("h2", "15.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["SIMBOX Detection", "canonical ID, detection signal type, confidence, detected time, source reference (Ch.6)."],
        ["Suspected SIM", "SIM reference (Ch.14), linked detections, status."],
        ["Detection Evidence", "evidence reference (Ch.17), linkage to SIMBOX Detection."],
        ["Investigation", "canonical ID, assigned investigator (Ch.26), suspected SIM reference(s), status, sensitive-join log."],
        ["Tracking Authorization", "investigation reference, authorizing actor, scope, effective period."],
        ["Location Evidence", "investigation reference, geometry (Ch.8, heightened classification), source reference."],
        ["Blocking Request", "investigation reference, target SIM, requested-by actor, status."],
        ["Blocking Action", "blocking request reference, provider reference (Ch.23), execution status, timestamp."],
        ["Blocking Verification", "blocking action reference, verification method, verified status."],
        ["Enforcement Outcome", "investigation reference, outcome sourced only from the authoritative law-enforcement/regulatory system of record — never inferred by NCIE."],
    ],
     "Anti-Fraud / SIMBOX Intelligence principal entities."),
    ("h2", "15.4 Stage Lifecycle"),
    ("flow",
     [
        "SIMBOX Detection (automated signal)",
        "Suspected SIM (analyst-reviewed candidate)",
        "Investigation opened (sensitive joins individually authorized and logged)",
        "Location Evidence gathered under Tracking Authorization",
        "Blocking Request raised, requiring separate validation and authorization",
        "Blocking Action executed and Blocking Verification confirmed",
        "Enforcement Outcome recorded only from the authoritative external system",
     ],
     "Anti-Fraud stage progression, each stage an explicit, auditable entity."),
    ("h2", "15.5 Relationships and Cardinality"),
    ("bullets", [
        "One SIMBOX Detection may link to zero-or-more Suspected SIMs (a single signal can implicate multiple SIMs, e.g. a shared device).",
        "One Investigation has zero-or-more Blocking Requests, each with at most one Blocking Action and at most one Blocking Verification.",
        "Enforcement Outcome references the Investigation but is never derived by NCIE computation — only ingested from the authoritative external source.",
    ]),
    ("h2", "15.6 Classification and Security"),
    ("p",
     "Location Evidence and Detection Evidence tied to Anti-Fraud investigations are sensitive-tier "
     "by default (NCIE-002 Ch.26). Sensitive joins (identity-to-location) require an explicit "
     "Tracking Authorization record before they may be performed, not merely a standing role grant."),
    ("h2", "15.7 Failure / Exception Semantics"),
    ("p",
     "A Blocking Action that fails at the provider is retried under idempotency control (Ch.28) and "
     "surfaces failure explicitly; it is never recorded as Verified without a genuine Blocking "
     "Verification."),
    ("trace002", "Directly implements NCIE-002 Ch.15 in full."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm actual Anti-Fraud workflow, tools and detection sources currently used at NCA."),
        ("SOURCE_DISCOVERY", "Confirm what location data is received and at what precision."),
        ("INSTITUTIONAL", "Confirm blocking interfaces, approval matrix and verification process with operators."),
    ]),
    ("h2", "15.8 Acceptance Criteria"),
    ("bullets", [
        "Each stage in §15.4 is demonstrably a distinct, independently queryable entity for a representative case.",
        "A Blocking Action cannot reach Verified status without both Blocking Request validation and a genuine Blocking Verification record.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 16 — Regulatory Case, Finding & Decision Data Model
# ---------------------------------------------------------------------------
BLOCKS[16] = [
    ("h2", "16.1 Purpose"),
    ("p", "Defines the formal regulatory objects through which intelligence becomes an institutional "
         "case, finding or decision, implementing NCIE-002 Ch.16."),
    ("h2", "16.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "Investigation/Situation ≠ Finding — an open Investigation (Ch.15) or Situation (Ch.18) does not automatically become a Finding merely by existing.",
        "Hypothesis ≠ Finding — a Hypothesis (Ch.20/Ch.21), including an ARGUS-attributed one, is working reasoning, never a Finding.",
        "Recommendation ≠ Decision — an ARGUS or analyst recommendation is advisory input to a Decision, never the Decision itself.",
        "Finding ≠ Decision — a Validated Finding states what is established; a Decision states the institutional action taken in response.",
    ]),
    ("h2", "16.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Case", "canonical ID, originating domain/exception reference, status, assigned officer(s) (Ch.26)."],
        ["Referral", "case reference, referring entity, reason, timestamp."],
        ["Finding", "case reference, state (proposed/validated), content, contributor origin (human/AI, Ch.20), validator (distinct from proposer, Ch.26 separation of duties)."],
        ["Decision", "case reference, finding reference(s), decision authority, content, status."],
        ["Decision Authority", "role/actor reference (Ch.26), scope of authority."],
        ["Rationale", "decision reference, reasoning content, evidence references (Ch.17)."],
        ["Decision Status", "governed enumeration (draft/issued/appealed/reversed)."],
        ["Decision-Time Snapshot", "decision reference, reconstructed state as of decision timestamp (Ch.5, Ch.25)."],
        ["Review / Appeal", "decision reference, prior decision reference (never overwritten), new decision reference, reason."],
    ],
     "Regulatory Case, Finding & Decision principal entities."),
    ("h2", "16.4 Case Lifecycle"),
    ("flow",
     [
        "Exception / Investigation / Situation (from any domain)",
        "Case opened, Referral recorded if applicable",
        "Proposed Finding drafted (AI contribution distinctly attributed per Ch.20)",
        "Validated Finding (human validator distinct from proposer)",
        "Decision issued by named Decision Authority, with Rationale and Decision-Time Snapshot",
        "Appeal / Reversal preserves prior Decision and Finding, never overwrites",
     ],
     "Regulatory Case lifecycle from exception to decision."),
    ("h2", "16.5 Relationships and Cardinality"),
    ("bullets", [
        "One Case has one-to-many Findings and zero-to-many Decisions over its lifecycle.",
        "A Review/Appeal always references its prior Decision; the prior Decision record is retained, never deleted, with the new Decision linked as superseding it.",
    ]),
    ("h2", "16.6 Provenance and Security"),
    ("p",
     "A Finding's contributor origin is preserved permanently — an AI-attributed contribution that a "
     "human adopts into a Validated Finding retains its AI-origin marker (NCIE-002 Ch.20 §20.6, "
     "Ch.23 §23.6). Decision Authority is checked against Ch.26's role model at issuance time, not "
     "merely assumed from the acting user's general role."),
    ("h2", "16.7 Failure / Exception Semantics"),
    ("p",
     "A Case with an existing Regulatory Intelligence platform outage (NCIE-002 Ch.16 §16.6) queues "
     "locally with Evidence intact rather than losing the Case; reconciliation on reconnection is "
     "recorded, not silently merged."),
    ("trace002", "Directly implements NCIE-002 Ch.16 in full, and depends on Ch.20 (AI-origin attribution) and Ch.26 (separation of duties)."),
    ("review", [
        ("SOURCE_DISCOVERY", "Confirm NCA case/finding terminology and existing Regulatory Intelligence platform's own object model, to align field naming rather than duplicate it under different names."),
        ("INSTITUTIONAL", "Confirm decision authorities and approval levels per case category."),
        ("LEGAL", "Confirm which decisions require preserved Rationale and Decision-Time Snapshot as a matter of regulatory defensibility."),
    ]),
    ("h2", "16.8 Acceptance Criteria"),
    ("bullets", [
        "A Case is demonstrably blocked from reaching Validated Finding status without a distinct validator from the proposer.",
        "An appealed Decision demonstrably retains its full prior history intact.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 17 — Evidence & Evidence Relationship Model
# ---------------------------------------------------------------------------
BLOCKS[17] = [
    ("h2", "17.1 Purpose"),
    ("p", "Defines evidence objects, integrity, annotations, corrections, invalidation and "
         "relationships to reasoning, implementing NCIE-002 Ch.23's Evidence Service."),
    ("h2", "17.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "Source Data ≠ Evidence — a raw Source Object Reference (Ch.6) becomes Evidence only when deliberately registered as such, not automatically upon ingestion.",
        "Annotation ≠ Evidence — a human or ARGUS annotation on an Evidence object is commentary, never itself independently authoritative Evidence.",
        "Invalidated Evidence is not necessarily deleted — invalidation is a state change, preserving the historical record of what was once relied upon.",
    ]),
    ("h2", "17.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Evidence Object", "canonical ID, source reference (Ch.6), classification (Ch.31), status (active/invalidated)."],
        ["Evidence Artifact", "evidence object reference, content pointer, format."],
        ["Hash / Integrity Metadata", "evidence artifact reference, hash algorithm, hash value, computed timestamp."],
        ["Annotation", "evidence object reference, author (human/ARGUS, Ch.20), content, timestamp — explicitly not Evidence."],
        ["Evidence Relationship", "source evidence reference, target reasoning-object reference (Hypothesis/Finding, Ch.16/Ch.20/Ch.21), relationship type (supports/contradicts)."],
        ["Correction", "evidence object reference, prior version reference, reason, actor, timestamp (Ch.5, Ch.25)."],
        ["Invalidation", "evidence object reference, reason, actor, timestamp — evidence object retained, status changed."],
        ["Classification", "evidence object reference, tier (Ch.31)."],
    ],
     "Evidence & Evidence Relationship principal entities."),
    ("h2", "17.4 Supporting and Contradictory Relationships"),
    ("p",
     "An Evidence Relationship of type contradicts must preserve both the supporting and "
     "contradicting Evidence's original sources — it never resolves the contradiction by discarding "
     "one side, consistent with NCIE-002 Ch.17's contradiction-preservation principle applied at the "
     "Evidence layer."),
    ("h2", "17.5 Lifecycle"),
    ("flow",
     [
        "Source Object Reference deliberately registered as Evidence Object",
        "Hash/Integrity Metadata computed at registration",
        "Evidence Relationship links formed to Hypotheses/Findings as reasoning develops",
        "Annotation added by human or ARGUS without altering the Evidence itself",
        "Correction creates a new version if the Evidence Object requires amendment",
        "Invalidation changes status without deleting the historical record",
     ],
     "Evidence lifecycle from registration to potential invalidation."),
    ("h2", "17.6 Provenance and Chain of Custody"),
    ("p",
     "Hash/Integrity Metadata is computed at registration and re-verified whenever the Evidence "
     "Artifact is retrieved for a formal proceeding, giving a verifiable chain of custody independent "
     "of the underlying storage technology (Ch.32)."),
    ("h2", "17.7 Failure / Exception Semantics"),
    ("p",
     "A hash mismatch on retrieval is treated as a chain-of-custody failure requiring investigation, "
     "never silently ignored or auto-repaired."),
    ("trace002", "Directly implements NCIE-002 Ch.23 in full."),
    ("review", [
        ("LEGAL", "Confirm what NCA recognizes as formal Evidence for regulatory/legal purposes, to align the Evidence Object's classification and integrity requirements."),
        ("LEGAL", "Confirm chain-of-custody requirements in detail (algorithm, re-verification frequency)."),
        ("INSTITUTIONAL", "Confirm retention and correction rules for Evidence, feeding Ch.31."),
    ]),
    ("h2", "17.8 Acceptance Criteria"),
    ("bullets", [
        "An Annotation is demonstrably distinguishable from Evidence in every query and export.",
        "An Invalidation demonstrably preserves the original Evidence Object rather than deleting it.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 18 — REWS Alert, Situation & National Operating Picture Data Model
# ---------------------------------------------------------------------------
BLOCKS[18] = [
    ("h2", "18.1 Purpose"),
    ("p", "Defines Conditions, Alerts, Situations and the data required to compose the National "
         "Operating Picture, implementing NCIE-002 Ch.18."),
    ("h2", "18.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "Condition ≠ Alert ≠ Situation ≠ Investigation ≠ Case — five distinct entities, each with its own lifecycle (Ch.15, Ch.16 hold Investigation and Case; this chapter holds Condition, Alert and Situation).",
        "Acknowledgement is not resolution — acknowledging an Alert changes its acknowledgement state only, never its resolution status.",
        "National Operating Picture must preserve completeness, freshness and uncertainty as first-class properties, never implied by absence of data.",
    ]),
    ("h2", "18.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Condition", "canonical ID, domain reference, detected state, supporting evidence/observation references."],
        ["Alert", "canonical ID, condition reference, alert rule reference (Ch.24), severity, raised time."],
        ["Severity", "governed enumeration, effective-dated (Ch.24)."],
        ["Acknowledgement", "alert reference, actor, timestamp — distinct from resolution."],
        ["Escalation", "alert reference, escalated-to actor/role, timestamp, reason."],
        ["Situation", "canonical ID, grouped Alert/Incident/Evidence references, lifecycle status, owner."],
        ["Situation Association", "situation reference, associated object reference (Alert/Incident/Evidence), relationship type."],
        ["NOP Projection", "current composed view: per-domain known/missing/stale/waiting/contradictory status (Ch.2 vocabulary)."],
        ["NOP Snapshot", "NOP projection captured at a point in time, for historical reconstruction (Ch.5, Ch.25)."],
    ],
     "REWS Alert, Situation & National Operating Picture principal entities."),
    ("h2", "18.4 Lifecycle"),
    ("flow",
     [
        "Observation/PM data evaluated against effective Alert Rule (Ch.24)",
        "Condition detected",
        "Alert raised with severity and evidence references",
        "Acknowledgement recorded (distinct from resolution)",
        "Escalation if unresolved within governed timing",
        "Human groups related Alerts/Incidents/Evidence into a Situation",
        "NOP Projection recomputed and periodically captured as an NOP Snapshot",
     ],
     "Condition-to-Situation lifecycle feeding the National Operating Picture."),
    ("h2", "18.5 Relationships and Cardinality"),
    ("bullets", [
        "One Condition may produce zero-or-one Alert per effective Alert Rule (avoiding duplicate alerts for the same underlying condition).",
        "One Situation has one-to-many Situation Associations, spanning Alerts, Incidents (Ch.10) and Evidence (Ch.17) across multiple domains.",
    ]),
    ("h2", "18.6 Provenance and Temporal Semantics"),
    ("p",
     "Every Alert retains its triggering Alert Rule version (Ch.24) so historical Alerts remain "
     "explicable even after rules change. NOP Snapshots allow reconstruction of \"what the national "
     "picture looked like\" at a prior time, supporting Ch.25's decision-time reconstruction needs at "
     "the situational-awareness level."),
    ("h2", "18.7 Failure / Exception Semantics"),
    ("p",
     "Loss of the REWS evaluation pipeline is reflected as a stale/waiting NOP Projection state, never "
     "as a silently frozen 'all clear' picture (NCIE-002 Ch.18 §18.8)."),
    ("trace002", "Directly implements NCIE-002 Ch.18 in full, and depends on Ch.24 for governed Alert Rules."),
    ("review", [
        ("INSTITUTIONAL", "Confirm REWS severity taxonomy and escalation timing per category."),
        ("INSTITUTIONAL", "Confirm Alert acknowledgement/escalation workflow and closure authority."),
        ("INSTITUTIONAL", "Confirm which domains are mandatory for a complete National Operating Picture at launch."),
    ]),
    ("h2", "18.8 Acceptance Criteria"),
    ("bullets", [
        "An Alert is demonstrably traceable to the Condition and evidence that triggered it.",
        "An NOP Snapshot is demonstrably reconstructable for a prior point in time, including its uncertainty state at that time.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 19 — Cross-Domain Fusion & Intelligence Graph Model
# ---------------------------------------------------------------------------
BLOCKS[19] = [
    ("h2", "19.1 Purpose"),
    ("p", "Defines how objects from different domains may be connected for cross-domain analysis "
         "without losing their native meaning, implementing NCIE-002 Ch.17."),
    ("h2", "19.2 Semantic Definition — Mandatory Separation"),
    ("p",
     "Graph Relationship ≠ Causality. Every edge in the intelligence graph states a correlation type "
     "and its supporting basis; none is rendered or queryable in a way that implies a causal claim "
     "the evidence does not support."),
    ("h2", "19.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Graph Node Reference", "pointer to a canonical entity in its owning domain chapter — the graph never copies the entity's substantive attributes."],
        ["Typed Edge", "source node reference, target node reference, relationship type."],
        ["Edge Origin", "governed enumeration: observed / deterministic / human-inferred / ARGUS-proposed — each requiring a different validation state per §19.4."],
        ["Validation State", "edge reference, state (unvalidated/human-confirmed/rejected)."],
        ["Temporal Validity", "edge reference, effective period during which the relationship held (Ch.5)."],
        ["Evidence Support", "edge reference, evidence object reference(s) (Ch.17)."],
        ["Cross-Domain Correlation", "a computed set of edges meeting a correlation pattern, with confidence."],
        ["Graph Projection", "a bounded, queryable view of the graph for a given scope/time window."],
    ],
     "Cross-Domain Fusion & Intelligence Graph principal entities."),
    ("h2", "19.4 Edge Origin and Validation"),
    ("table",
     ["Edge Origin", "Required Validation State Before Use in a Finding"],
     [
        ["Observed", "Directly evidenced; usable as supporting Evidence Support without further validation."],
        ["Deterministic", "Computed by a governed, deterministic rule (Ch.24); usable once the rule itself is approved."],
        ["Human-Inferred", "Requires the inferring human's attribution retained; usable as working analysis, requires promotion (Ch.16) to support a Finding."],
        ["ARGUS-Proposed", "Requires explicit AI-origin attribution (Ch.20) and human validation before any use beyond working analysis; never auto-promoted."],
    ],
     "Required validation state by edge origin before an edge may support a Finding."),
    ("h2", "19.5 Relationships and Cardinality"),
    ("p",
     "A Typed Edge references exactly two Graph Node References (source, target) and zero-to-many "
     "Evidence Support records. Multiple edges of different types may exist between the same two "
     "nodes without merging into one relationship."),
    ("h2", "19.6 Provenance"),
    ("p",
     "Every edge retains its Edge Origin permanently, even after human validation — validating an "
     "ARGUS-Proposed edge does not silently reclassify it as Observed or Deterministic (mirrors the "
     "AI-origin-preservation principle of Ch.16 §16.6 and Ch.20)."),
    ("h2", "19.7 Failure / Exception Semantics"),
    ("p",
     "Two edges that conflict (e.g. contradictory correlation claims about the same two nodes) are "
     "both retained with their respective Evidence Support, never auto-resolved."),
    ("trace002", "Directly implements NCIE-002 Ch.17 in full, and depends on Ch.20 for ARGUS-Proposed edge attribution."),
    ("review", [
        ("INSTITUTIONAL", "Confirm which relationship types are operationally useful for launch (§19.3 Typed Edge)."),
        ("INSTITUTIONAL", "Confirm which inferred edges require mandatory human validation before appearing in any shared view."),
        ("INSTITUTIONAL", "Confirm sensitive graph traversal rules where a path would cross a protected-identity or Anti-Fraud boundary (Ch.14, Ch.15)."),
    ]),
    ("h2", "19.8 Acceptance Criteria"),
    ("bullets", [
        "An ARGUS-Proposed edge is demonstrably blocked from supporting a Finding until explicitly human-validated.",
        "A sampled Graph Projection demonstrably never displays a causal claim unsupported by its Edge Origin and Evidence Support.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 20 — ARGUS Interaction & AI Provenance Data Model
# ---------------------------------------------------------------------------
BLOCKS[20] = [
    ("h2", "20.1 Purpose"),
    ("p", "Defines data needed to govern ARGUS participation, tools, model routing and AI-originated "
         "analytical objects, implementing NCIE-002 Ch.19 (Intelligence Assistant), Ch.19 §19.11 "
         "(ARGUS Naming Boundary) and Ch.24 (AI Platform)."),
    ("h2", "20.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "ARGUS output is not automatically Evidence (Ch.17) — an ARGUS Contribution becomes Evidence only if it is itself registered as such through deliberate promotion, which is rare and distinct from ordinary use.",
        "AI origin must remain after human adoption or modification — a Human Modification of an AI Contribution retains the original AI Contribution's identity and content, never overwriting it.",
        "Private model chain-of-thought is not persisted. This chapter's entities capture defensible reasoning artifacts and provenance — sources, tools, outputs and governance metadata — never the model's internal, unexaminable deliberation (NCIE-002 Ch.23 §23.6, Ch.24 §24.4).",
    ]),
    ("h2", "20.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["ARGUS Interaction", "canonical ID, conversation/room reference, participant (human or ARGUS), timestamp."],
        ["ARGUS Contribution", "interaction reference, contribution type, content, AI Origin marker."],
        ["Contribution Type", "governed enumeration: Question / Challenge / Hypothesis / Contradiction / Evidence Gap / other analytical contribution types fixed by NCIE-002 Ch.20 §20.3."],
        ["Tool Invocation", "contribution reference, tool name, parameters, authorization check result (Ch.26), response reference."],
        ["Model Route / Version", "interaction reference, model/provider reference (Ch.24 Model Registry), version, retained where governance requires audit."],
        ["Evidence Reference", "contribution reference, evidence object reference(s) (Ch.17) — a contribution cites Evidence; it does not become Evidence."],
        ["Human Response", "contribution reference, responding human, action (accept/reject/modify/defer/promote)."],
        ["Human Modification of AI Contribution", "original contribution reference (retained, unmodified), modifying human, modified content, timestamp."],
        ["Participation Mode", "room/interaction reference, mode (Participatory/Invoked/Evidence-Watch/Silent, Ch.21 §21.7), effective period."],
        ["AI Provenance", "contribution reference, full derivation chain: sources cited, tools invoked, model route, human responses — never internal model reasoning."],
    ],
     "ARGUS Interaction & AI Provenance principal entities (all mandated classes from the handover instructions are represented)."),
    ("h2", "20.4 Human Modification Never Erases AI Origin"),
    ("p",
     "When a human edits or extends an ARGUS Contribution, the system creates a Human Modification "
     "of AI Contribution record that references, and does not replace, the original ARGUS "
     "Contribution. Any later display of the modified content shows both the current text and its "
     "AI-originated ancestry, directly implementing NCIE-002 Ch.20 §20.6 and Ch.23 §23.6."),
    ("h2", "20.5 Tool Authorization at the Data Layer"),
    ("p",
     "Every Tool Invocation stores its authorization check result at the time of invocation, not only "
     "a boolean success flag — this gives Ch.27's audit model a queryable record of exactly which "
     "authorization layer (Ch.26) permitted or denied each ARGUS tool use, implementing NCIE-002 "
     "Ch.19 §19.7 and Ch.24 §24.4's guardrail requirements."),
    ("h2", "20.6 Lifecycle"),
    ("flow",
     [
        "ARGUS Interaction opened (invoked or proactive per Participation Mode)",
        "Tool Invocation(s) executed under authorization filtering",
        "ARGUS Contribution produced with explicit Contribution Type and Evidence References",
        "AI Provenance recorded (sources, tools, model route — not internal reasoning)",
        "Human Response recorded (accept/reject/modify/defer/promote)",
        "If modified, Human Modification of AI Contribution created alongside the retained original",
     ],
     "ARGUS interaction-to-provenance lifecycle."),
    ("h2", "20.7 Orchestration Relationship Path (v0.4 — VPF & Dynamic Agent Synthesis Amendment)"),
    ("p",
     "Authority: approved NCIE-001 v1.3 §12.77-§12.80A; approved NCIE-002 v0.5 Ch.19 §19.2A, Ch.24 "
     "§24.4A; approved NCIE-007 v1.1 Ch.20. This section extends, and does not replace, the existing "
     "ARGUS Interaction, ARGUS Contribution, Tool Invocation, Model Route/Version, Evidence Reference, "
     "Human Response, Human Modification, Participation Mode and AI Provenance entities in §20.3."),
    ("flow",
     [
        "ARGUS Interaction / Task Need (§20.3)",
        "Task Contract (Ch.3 §3.9)",
        "Registered Agent Reference OR Agent Definition (Ch.3 §3.9)",
        "Agent Run (Ch.3 §3.9)",
        "Model Route / Context / Evidence / Tool Invocations (§20.3, Ch.17, Ch.24, Ch.26)",
        "Agent Result Package (Ch.3 §3.9)",
        "VPF Validation Artifact (Ch.3 §3.9, §3.9.1)",
        "Validated AI Result / other VPF Disposition (Ch.3 §3.9)",
        "ARGUS Contribution (§20.3)",
        "Human Response (§20.3)",
     ],
     "Orchestration relationship path — from ARGUS interaction/task need to human response, via the "
     "governed Agent/VPF object family."),
    ("h2", "20.8 Dynamically Synthesized Agent Provenance (v0.4)"),
    ("p",
     "For an Agent Run whose Agent Definition was dynamically synthesized, provenance additionally "
     "preserves references to:"),
    ("bullets", [
        "Synthesis Origin (the originating ARGUS request/task need).",
        "Gate A Validation (§20.9) — the envelope validation that occurred before activation.",
        "Sandbox / Evaluation reference.",
        "Agent Definition Version actually executed.",
        "Runtime Identity (Ch.26 §26.5) — distinct from the Human Principal and from ARGUS's own identity.",
        "Expiry state.",
        "Promotion state, where a Promotion Candidate (Ch.3 §3.9) was later created from this Run.",
    ]),
    ("p", "Private model chain-of-thought is not persisted for synthesized agents, exactly as for direct ARGUS use (§20.2)."),
    ("h2", "20.9 VPF Gate A Data Semantics (v0.4)"),
    ("p",
     "Gate A is represented as a validation artifact/reference associated with the Agent "
     "Definition/envelope before activation. GATE A VALIDATES AGENT ENVELOPE — NOT FUTURE OUTPUT. Gate "
     "A and Gate B (§20.10) are not collapsed into one record; the canonical model distinguishes their "
     "validation type explicitly."),
    ("h2", "20.10 VPF Gate B Data Semantics (v0.4)"),
    ("p",
     "Gate B is represented as the VPF validation of substantive AI-generated output (the VPF "
     "Validation Artifact, Ch.3 §3.9) and must link to the exact Agent Result Package/AI artifact it "
     "validated. GATE B VALIDATION ≠ HUMAN APPROVAL. This applies uniformly to substantive output from "
     "ARGUS direct model use, Registered Reusable Agents, Ephemeral Agents and multi-agent synthesis "
     "(no agent type is represented as exempt, per approved NCIE-007 v1.1 Ch.26)."),
    ("h2", "20.11 Classification and Security"),
    ("p",
     "An ARGUS Contribution inherits the classification of the Evidence and context it references; "
     "it is never rendered at a lower classification than its most sensitive input, consistent with "
     "NCIE-002 Ch.19 §19.7's authorization-filtering requirement. (v0.4) The same rule applies to an "
     "Agent Result Package and its resulting Validated AI Result."),
    ("h2", "20.12 Failure / Exception Semantics"),
    ("p",
     "If the Model Gateway is unavailable mid-interaction, the ARGUS Interaction record closes with "
     "an explicit degraded-completion status rather than a silently truncated or fabricated "
     "continuation (NCIE-002 Ch.19 §19.8). (v0.4) If VPF is unavailable, the affected VPF Validation "
     "Artifact records VALIDATION_UNAVAILABLE rather than PASS (Ch.3 §3.9.1); VPF unavailability never "
     "prevents the Agent Result Package itself from being recorded with its Execution Status."),
    ("trace002", "Directly implements NCIE-002 Ch.19 (Assistant), Ch.19 §19.11 (naming boundary), Ch.20 (collaborative reasoning) and Ch.24 (AI Platform, Model Gateway, Guardrails). (v0.4) §20.7-§20.10 additionally implement approved NCIE-001 v1.3 §12.77-§12.80A, approved NCIE-002 v0.5 Ch.19 §19.2A/Ch.24 §24.4A and approved NCIE-007 v1.1 Ch.11, Ch.20, Ch.26."),
    ("review", [
        ("INSTITUTIONAL", "Confirm retention period for ARGUS Interactions and Contributions."),
        ("INSTITUTIONAL", "Confirm which model/tool metadata (§20.3 Model Route/Version) NCA requires retained for audit versus what can be summarised."),
        ("LEGAL", "Confirm treatment of private versus shared ARGUS interactions under applicable records/privacy policy."),
        ("INSTITUTIONAL", "(v0.4) Confirm retention period for Agent Definitions, Agent Runs and VPF Validation Artifacts (Ch.3 §3.9)."),
        ("INSTITUTIONAL", "(v0.4) Confirm canonical stewardship for VPF Profiles distinct from the entity-family ownership already raised in Ch.3 §3.9."),
        ("INSTITUTIONAL", "(v0.4) Confirm retention period for Promotion Candidates and ownership for Engineering Change Candidates (Ch.3 §3.9)."),
    ]),
    ("h2", "20.13 Acceptance Criteria"),
    ("bullets", [
        "A sampled ARGUS Contribution demonstrably carries Contribution Type, AI Origin marker and Evidence References, with no persisted private chain-of-thought field anywhere in the schema.",
        "A human-modified ARGUS Contribution demonstrably retains its original, unmodified AI-originated version alongside the modification.",
        "(v0.4) A sampled Agent Run demonstrably traces to its Task Contract, Agent Definition Version, Runtime Identity, current authorization reference, Model Route, Context/Evidence references, Tool Invocations, Gate A reference where applicable, Agent Result Package and Gate B (VPF) validation.",
        "(v0.4) A dynamically synthesized Agent Run demonstrably preserves Synthesis Origin, Gate A Validation, Sandbox/Evaluation reference, Agent Definition Version, Runtime Identity, Expiry and Promotion state.",
        "(v0.4) A historical VPF Validation Artifact demonstrably remains associated with the Profile Version, Policy Version, Validation Time and Disposition that existed at validation time, even after a later revalidation creates a new related artifact.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 21 — Collaborative Intelligence & Multi-User Brainstorming Data Model
# ---------------------------------------------------------------------------
BLOCKS[21] = [
    ("h2", "21.1 Purpose"),
    ("p", "Defines persistent collaborative Rooms in which humans and ARGUS can brainstorm, challenge, "
         "hypothesize and preserve structured reasoning, implementing NCIE-002 Ch.20 in full. This "
         "chapter is deliberately not reducible to chat messages: it defines first-class persistent "
         "objects so collaborative intelligence can stop, resume and evolve without depending "
         "entirely on transcript history."),
    ("h2", "21.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "Room is more than chat — a Room's Collaborative Reasoning State (§21.4) is a structured object distinct from its raw message transcript.",
        "Shared disclosure must not become permission union — a Room's shared context is filtered per-participant by that participant's own authorization (Ch.26), never the union of all participants' permissions.",
        "Consensus ≠ Finding — participants agreeing within a Room produces a Consensus record, which remains working analysis until deliberately promoted through Ch.16's Finding Workflow.",
        "(v0.4) An agent's participation is not institutional authority — where a Registered Reusable Agent or Ephemeral Synthesized Agent (Ch.3 §3.9) contributes to a Room, it gains no Room Membership Authority, no pooled permissions, and no institutional decision authority by virtue of participating; Consensus ≠ Finding and Dissent/Contradiction preservation (§21.6) apply identically to agent- and human-originated contributions.",
    ]),
    ("h2", "21.3 Principal Entities (Mandatory Persistent Object Classes)"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Collaborative Room", "canonical ID, room type, classification (Ch.31), current Participation Mode (Ch.20 §20.5, Ch.21 §21.7)."],
        ["Participant", "room reference, user reference (Ch.26), individual permission scope, join/leave timestamps."],
        ["Thread", "room reference, topic, status — supports multiple concurrent analytical threads without cross-contamination."],
        ["Question", "thread reference, originator (human or ARGUS via Ch.20), content."],
        ["Hypothesis", "thread reference, originator, content, supporting/contradicting Evidence References (Ch.17), status (active/adopted/deferred/rejected)."],
        ["Assumption", "thread reference, originator, content, whether tested."],
        ["Contradiction", "thread reference, conflicting Hypothesis or Evidence references, status."],
        ["Evidence Gap", "thread reference, description of missing evidence, originator."],
        ["Evidence Relationship", "thread reference, evidence object reference (Ch.17), relationship to Hypothesis/Assumption (supports/contradicts) — shares its type vocabulary with Ch.17 §17.3."],
        ["Task", "thread reference, description, assignee, status."],
        ["Waiting Dependency", "thread reference, description (e.g. WAITING_FOR_PM), linked Workflow reference (Ch.23), status."],
        ["Human Judgment", "thread reference, judging human, content — a human's own analytical position, distinct from a Hypothesis attributed to ARGUS."],
        ["Decision Point", "thread reference, description of a choice the room must make, linked options."],
        ["ARGUS Intervention", "thread reference, ARGUS Contribution reference (Ch.20), triggering condition, Participation Mode in effect at the time. (v0.4) Machine contribution origin, where material, identifies ARGUS Direct, Registered Reusable Agent, or Ephemeral Synthesized Agent (Ch.3 §3.9)."],
        ["Consensus", "thread reference, participants agreeing, content — explicitly not a Finding (§21.2)."],
        ["Dissent", "thread reference, dissenting participant, content — preserved even where a Consensus exists."],
        ["Room Snapshot", "room reference, timestamp, captured Collaborative Reasoning State — supports 'where were we?' reconstruction (Ch.5, Ch.25)."],
    ],
     "Collaborative Intelligence & Multi-User Brainstorming principal entities — every class listed in the authoritative handover instructions is represented as a first-class persistent object."),
    ("h2", "21.4 Collaborative Reasoning State"),
    ("p",
     "A Room's Collaborative Reasoning State is the composed, queryable aggregation of its current "
     "Threads, Questions, Hypotheses, Assumptions, Contradictions, Evidence Gaps, Tasks, Waiting "
     "Dependencies, Human Judgments, Decision Points, ARGUS Interventions, Consensus and Dissent "
     "records. It is distinct from — and reconstructable independently of — the raw message "
     "transcript, directly implementing NCIE-002 Ch.20 §20.5."),
    ("h2", "21.5 Multi-Speaker Attribution"),
    ("p",
     "Every object in §21.3 that has an originator field preserves that originator permanently, "
     "including explicit AI origin where the originator is ARGUS (via Ch.20's AI Origin marker). "
     "Adoption, challenge or modification by another participant does not overwrite the original "
     "originator field (NCIE-002 Ch.20 §20.6). (v0.4) Where the originator is a machine contribution, "
     "the record additionally distinguishes ARGUS Direct, Registered Reusable Agent, or Ephemeral "
     "Synthesized Agent origin (Ch.3 §3.9, Ch.20 §20.7) without creating a separate Agent-only version "
     "of the same object class."),
    ("h2", "21.6 Analytical Thread Isolation"),
    ("p",
     "Every object in §21.3 references exactly one Thread. Evidence, Hypotheses and Contradictions "
     "belonging to different Threads within the same Room are never implicitly combined in a query "
     "unless the query explicitly spans threads, preventing cross-thread contamination (NCIE-002 "
     "Ch.20 §20.6)."),
    ("h2", "21.7 Participation Modes and Room-to-Workflow Linkage"),
    ("p",
     "Participation Mode (Participatory/Invoked/Evidence-Watch/Silent) is stored per Room and "
     "changeable by an authorized participant, per NCIE-002 Ch.20 §20.7. A Waiting Dependency links "
     "to its originating Workflow (Ch.23) via the Room-to-Workflow Bridge pattern, so a validated "
     "result can return asynchronously to the correct Thread without re-establishing context "
     "(NCIE-002 Ch.21 §21.4)."),
    ("h2", "21.8 Permission-Aware Shared Context"),
    ("p",
     "The Room's effective shared disclosure context is computed per-participant at query time from "
     "each Participant's own permission scope (Ch.26) — it is never stored as a single pooled "
     "permission set for the Room, implementing NCIE-002 Ch.20 §20.9 at the data-model level."),
    ("h2", "21.9 Room Snapshot and Cross-Session Continuity"),
    ("p",
     "A Room Snapshot captures the Collaborative Reasoning State at a point in time (e.g. end of "
     "shift), enabling 'where were we?' reconstruction by combining the snapshot with current "
     "authoritative NCIE state, per NCIE-002 Ch.20 §20.10 — never presenting a stale snapshot as "
     "current without reconciliation."),
    ("h2", "21.10 Failure / Exception Semantics"),
    ("p",
     "Concurrent edits to the same Thread's Collaborative Reasoning State are resolved with a visible "
     "edit trail (last-writer-wins per field plus history), never silent data loss, matching NCIE-002 "
     "Ch.20 §20.16."),
    ("trace002", "Directly implements NCIE-002 Ch.20 in full, and depends on Ch.20 of this document (ARGUS Interaction) for AI-originated object attribution."),
    ("review", [
        ("INSTITUTIONAL", "Confirm Room types and membership rules (who may create a Room, invite participants)."),
        ("INSTITUTIONAL", "Confirm default Participation Mode per Room type (ordinary vs Anti-Fraud/regulatory rooms, per NCIE-002 Ch.20's proposed default)."),
        ("INSTITUTIONAL", "Confirm how Consensus, Dissent and private-to-room sharing should work in edge cases (e.g. a participant leaving mid-discussion)."),
    ]),
    ("h2", "21.11 Acceptance Criteria"),
    ("bullets", [
        "A scripted two-human, mixed-permission Room session demonstrates permission-aware filtering (§21.8), correct multi-speaker attribution (§21.5) and thread isolation (§21.6).",
        "A Room Snapshot is demonstrably sufficient, combined with current authoritative state, to answer 'where were we?' without relying on the raw transcript.",
    ]),
]

# ---------------------------------------------------------------------------
# Chapter 22 — Memory & Institutional Knowledge Data Model
# ---------------------------------------------------------------------------
BLOCKS[22] = [
    ("h2", "22.1 Purpose"),
    ("p", "Defines long-term memory classes and how reviewed experience becomes reusable Institutional "
         "Knowledge, implementing NCIE-002 Ch.20 §20.2 (memory tiers) and Ch.20 §20.12 (formal "
         "promotion boundary)."),
    ("h2", "22.2 Semantic Definition — Mandatory Separations"),
    ("bullets", [
        "Memory is not current truth — a Memory Object records what was previously observed, decided or discussed; it is never queried as if it were live authoritative state.",
        "ARGUS is not institutional memory — ARGUS has no persistent memory store of its own separate from the governed Memory Object entities defined here; anything ARGUS 'recalls' is retrieved from these entities under normal authorization.",
        "Institutional Knowledge ≠ Rule — a piece of Institutional Knowledge (e.g. \"district X historically degrades during rainy season\") informs human and ARGUS reasoning but is never itself a governed Rule (Ch.24) unless deliberately encoded as one.",
    ]),
    ("h2", "22.3 Principal Entities"),
    ("table",
     ["Entity", "Attributes / Attribute Classes"],
     [
        ["Memory Object", "canonical ID, memory class, owner (user/room/institutional), content reference, recorded time."],
        ["Memory Class", "governed enumeration: Private User Memory / Shared Room Memory / Institutional Memory (NCIE-002 Ch.20 §20.2)."],
        ["Knowledge Candidate", "memory object reference, proposed generalisation, proposing actor — requires human promotion (§22.4)."],
        ["Institutional Knowledge", "knowledge candidate reference (once promoted), content, applicability scope, review state."],
        ["Knowledge Version", "institutional knowledge reference, version, change reason (Ch.5, Ch.25 pattern)."],
        ["Applicability Scope", "institutional knowledge reference, domain(s)/geography/time window the knowledge applies to."],
        ["Review State", "institutional knowledge reference, reviewer, decision, timestamp."],
        ["Supersession / Retraction", "institutional knowledge reference, prior version reference, reason — history remains traceable."],
    ],
     "Memory & Institutional Knowledge principal entities."),
    ("h2", "22.4 Promotion Requires Human Action"),
    ("p",
     "A Knowledge Candidate — whether proposed by a human or by ARGUS (Ch.20) — never becomes "
     "Institutional Knowledge automatically. Promotion is a deliberate, audited human action recorded "
     "as a Review State entry, implementing NCIE-002 Ch.20 §20.12's formal promotion boundary."),
    ("h2", "22.5 Lifecycle"),
    ("flow",
     [
        "Memory Object recorded (private/shared/institutional per its Memory Class)",
        "Knowledge Candidate proposed from a pattern noticed in memory or collaborative reasoning (Ch.21)",
        "Human review (Review State)",
        "Promotion to Institutional Knowledge, or rejection/deferral",
        "Superseded/retracted Institutional Knowledge remains historically traceable via Knowledge Version",
     ],
     "Memory-to-Institutional-Knowledge promotion lifecycle."),
    ("h2", "22.6 Sharing and Classification"),
    ("p",
     "Private User Memory is never automatically shared into a Room merely because it would be "
     "relevant, matching Ch.21 §21.8's permission-aware sharing rule. Institutional Knowledge is "
     "classified and access-controlled exactly as its Applicability Scope's domain requires (Ch.26, "
     "Ch.31) — e.g. Institutional Knowledge derived from Anti-Fraud experience remains sensitive-tier."),
    ("h2", "22.7 Failure / Exception Semantics"),
    ("p",
     "Superseded or retracted Institutional Knowledge is never deleted; it is marked superseded/"
     "retracted with a reason and remains queryable for historical reconstruction of what was "
     "believed true at a past point in time (Ch.5, Ch.25)."),
    ("trace002", "Directly implements NCIE-002 Ch.20 §20.2 and §20.12 in full."),
    ("review", [
        ("INSTITUTIONAL", "Confirm memory retention period by Memory Class."),
        ("INSTITUTIONAL", "Confirm Institutional Knowledge owners, reviewers and approvers."),
        ("INSTITUTIONAL", "Confirm what may become organisation-wide Institutional Knowledge versus remaining room- or user-scoped."),
    ]),
    ("h2", "22.8 Acceptance Criteria"),
    ("bullets", [
        "A Knowledge Candidate is demonstrably blocked from becoming Institutional Knowledge without a recorded human Review State.",
        "A superseded piece of Institutional Knowledge is demonstrably retrievable in its pre-supersession form.",
    ]),
]
