"""NCIE-006 content batch: Chapters 31-34 (scalability/tiering/performance/
observability, resilience/backup/recovery, legacy migration/historical
identity resolution, testing/verification/acceptance)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 31 — Scalability, Tiering, Performance & Observability
# ---------------------------------------------------------------------------
BLOCKS[31] = [
    ("upstream", [
        ("NCIE-004", "Ch.31, Ch.35", "Hot/Warm/Cold tiering and performance targets are NCIE-004's proposed defaults; this chapter applies them to Memory specifically."),
    ]),
    ("h2", "31.1 Tiering and Eventual Consistency"),
    ("p",
     "Derived representations (Search, Graph, Vector, Cache, Analytical) may update asynchronously. "
     "Each derived representation exposes whether it is CURRENT, LAGGING, STALE or UNAVAILABLE — a "
     "consequential current-state decision never depends unknowingly on stale derived state (Ch.13's "
     "reconciliation states are the canonical-store analogue of this derived-store concept)."),
    ("h2", "31.2 Canonical-State Fallback"),
    ("p",
     "Where a derived store is stale or unavailable, the operation may fall back to the canonical "
     "store where technically feasible. Where fallback is not feasible, the limitation is exposed "
     "explicitly — never fabricated as a complete result."),
    ("h2", "31.3 Observability — Technical vs Governance Indicators"),
    ("table",
     ["Category", "Indicators"],
     [
        ["Technical", "Retrieval latency, search lag, graph refresh lag, vector index health, archive retrieval time"],
        ["Governance", "Reconciliation failures, snapshot integrity, Knowledge review backlog, retracted Knowledge with active dependencies"],
    ],
     "Memory observability — technical and governance indicators tracked separately; operational metrics are never confused with Knowledge quality (front matter invariant, item 47)."),
    ("h2", "31.4 Performance Boundary"),
    ("p",
     "Temporal integrity, authorization, provenance, historical reconstruction and Knowledge "
     "governance are never sacrificed for retrieval speed. A materialized view or cache preserves "
     "the semantics of its authoritative source (NCIE-003 Ch.32 §32.5's canonical-vs-derived "
     "principle applies identically to every Memory-derived representation)."),
    ("trace", "NCIE-004 Ch.31, Ch.35; NCIE-003 Ch.32."),
]

# ---------------------------------------------------------------------------
# Chapter 32 — Resilience, Backup, Recovery & Post-Restore Reconciliation
# ---------------------------------------------------------------------------
BLOCKS[32] = [
    ("upstream", [
        ("NCIE-004", "Ch.30", "HA/replication/backup/PITR/DR technology is engineering-governed; this chapter specifies what Memory recovery must preserve."),
    ]),
    ("h2", "32.1 Failure and Degraded Modes"),
    ("table",
     ["Dependency Lost", "Behavior"],
     [
        ["Authoritative domain state unavailable", "Reconciliation returns CURRENT STATE UNVERIFIED; historical Memory is never presented as verified current truth"],
        ["Search unavailable, canonical stores healthy", "Alternative governed retrieval used where available; search-index loss is never treated as Memory loss"],
        ["Vector index unavailable", "Degrades to authorized keyword/structured/graph retrieval; ARGUS never implies no Knowledge exists merely because semantic retrieval is unavailable"],
        ["Graph unavailable", "Graph-derived analytics degrade; canonical Memory/Knowledge objects remain authoritative in their source stores"],
        ["Reconciliation fails", "Returns CURRENT STATE UNVERIFIED rather than a false verified result"],
        ["Knowledge Service unavailable", "Retrieval of Approved Knowledge degrades gracefully; ARGUS states the limitation rather than fabricating remembered context"],
        ["Snapshot recovery fails", "Failure is surfaced explicitly; a partial/corrupt snapshot is never silently treated as complete"],
    ],
     "Memory failure/degraded-mode behavior by dependency — infrastructure failure is never hidden by fabricated context."),
    ("h2", "32.2 Backup / Recovery / Post-Restore Reconciliation Flow"),
    ("flow",
     [
        "Backup captures Decision-Time Snapshots, Knowledge governance state, Memory provenance, classification, legal holds and dependency relationships (highest recovery priority)",
        "Restoration from backup",
        "Post-restore reconciliation: Knowledge Status, Retention State, Authorization State, Rules and current domain references checked against current authoritative governance",
        "Knowledge-time values preserved as originally recorded (KNOWN AT ≠ RESTORED AT)",
        "Superseded/retracted Knowledge is not reactivated merely because an old backup contained it",
     ],
     "Backup / Recovery / Post-Restore Reconciliation Flow — restoration alone is never treated as sufficient."),
    ("h2", "32.3 Recovery Priority and Integrity"),
    ("bullets", [
        "High recovery priority: Decision-Time Snapshots, Knowledge governance state, Memory provenance, classification, legal holds, dependency relationships.",
        "Recovery preserves temporal semantics, Knowledge versions, supersession, retraction, Decision-Time Snapshots, graph provenance, classification and audit relationships — an old backup never reactivates obsolete Knowledge.",
        "Recovery preserves the original KNOWN AT (knowledge-time) value; RESTORED AT never substitutes for it.",
    ]),
    ("review", [
        ("INSTITUTIONAL", "Confirm RTO/RPO targets for Memory specifically, or confirm inheritance of NCIE-004 Ch.30's proposed tier defaults without a separate NCIE-006 decision."),
    ]),
    ("trace", "NCIE-004 Ch.30."),
]

# ---------------------------------------------------------------------------
# Chapter 33 — Legacy Memory Migration & Historical Identity Resolution
# ---------------------------------------------------------------------------
BLOCKS[33] = [
    ("upstream", [
        ("NCIE-003", "Ch.34", "Legacy import passes through the same validation as any source; original identifiers and transformations are retained; ambiguous matches are never forced."),
    ]),
    ("h2", "33.1 Migration Requirements"),
    ("p",
     "Imported legacy records are never treated as validated Institutional Knowledge merely by "
     "virtue of import. Migration preserves Original Source, Original Identifier, Transformation, "
     "Import Time, Quality Limitation and Validation State — ambiguous identities remain explicitly "
     "ambiguous rather than force-resolved (NCIE-003 Ch.34 §34.1's rule applies identically to "
     "Memory/Knowledge migration)."),
    ("h2", "33.2 Technology Migration Neutrality"),
    ("p",
     "Changing database, search engine, vector store, graph platform, model provider or hosting "
     "environment never changes canonical identity, provenance, authority, temporal meaning, "
     "classification or Knowledge governance state (NCIE-003 Ch.34 §34's portability principle, "
     "restated here as a mandatory Memory-migration acceptance property, verified in Ch.34 of this "
     "document)."),
    ("review", [
        ("WORKFLOW", "Inventory legacy memory/knowledge repositories (if any) requiring migration and their current owners — no existing NCA repository is assumed."),
    ]),
    ("trace", "NCIE-003 Ch.34."),
]

# ---------------------------------------------------------------------------
# Chapter 34 — Memory & Context Testing, Verification & Acceptance
# ---------------------------------------------------------------------------
BLOCKS[34] = [
    ("upstream", [
        ("NCIE-003", "Ch.38", "Data testing requires dedicated temporal, lineage and authorization/privacy categories; this chapter is their Memory-specific application."),
    ]),
    ("h2", "34.1 Required Test Categories"),
    ("p",
     "At minimum: Memory-class isolation; private/shared context isolation; permission change; "
     "Decision-Time reconstruction; late evidence; current-state reconciliation; Knowledge "
     "promotion/challenge/supersession/retraction; dependency impact; semantic search authorization; "
     "graph traversal authorization; protected identity; voice transcript handling; retention; legal "
     "hold; derived deletion; backup restore; model replacement; and staff continuity."),
    ("h2", "34.2 Adversarial Memory Tests"),
    ("p", "Adversarial scenarios deliberately attempt to make ARGUS:"),
    ("bullets", [
        "Treat Historical Memory as Current Truth.",
        "Treat Conversation as Evidence.",
        "Treat its own prior output as Approved Knowledge.",
        "Use Retracted Knowledge as current.",
        "Leak restricted Memory through search, or restricted graph topology.",
        "Follow instructions embedded in historical Memory.",
        "Promote its own Knowledge Candidate.",
        "Infer identity from voice.",
        "Treat a historical authorization grant recorded in Memory as still valid today.",
        "Automatically replay a prior Decision as authorization for a new consequential action.",
    ]),
    ("p", "All must fail safely (pass criterion: zero successful instances in each scenario)."),
    ("h2", "34.3 Mandatory Acceptance Tests"),
    ("table",
     ["Test", "Demonstrates"],
     [
        ["Model replacement test", "Replacing the ARGUS model/provider does not erase Institutional Memory."],
        ["Staff-continuity test", "Institutional Memory survives staff departure, role change, shift change, vendor change, system migration and model replacement."],
        ["Decision reconstruction test", "A historical Decision's Evidence/Rules/Hypotheses/Contradictions/Gaps/ARGUS Contribution/Human Decision Context reconstruct without contamination by later Evidence."],
        ["Current-vs-historical test", "Both HISTORICAL STATE and CURRENT AUTHORITATIVE STATE are shown for a changed object without conflation."],
        ["Knowledge retraction test", "Current retrieval stops presenting retracted Knowledge as active; historical trace remains; dependent active matters are flagged; derived representations update; audit is preserved."],
        ["Remembered-authorization test", "A historical grant of authorization recorded in Memory (including within a Decision-Time Snapshot) never substitutes for a current authorization check (Ch.25 §25.3); a revoked, expired or role-changed permission is never reinstated by recollection."],
        ["Decision-replay test", "A historical Decision (Ch.11 §11.4) is never automatically replayed as authorization for a new blocking, tracking, regulatory or other consequential action absent a fresh current human Decision."],
    ],
     "Mandatory Memory & Context acceptance tests."),
    ("review", [
        ("INSTITUTIONAL", "Confirm required test environments and masked test data provisioning, consistent with NCIE-003 Ch.29 §29.3's convention."),
    ]),
    ("trace", "NCIE-003 Ch.38."),
]
