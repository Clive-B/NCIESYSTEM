"""NCIE-004 content batch: Chapters 33-36 (Technology Registry, Reference
Deployment Topology, Technology Decision Matrix & Human Review Register,
Acceptance/Traceability/Handover Gate)."""

from ncie004_ch35_matrix import matrix_rows, review_rows, summary_counts

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 33 — Engineering Governance, Technology Registry & Lifecycle Management
# ---------------------------------------------------------------------------
BLOCKS[33] = [
    ("upstream", [
        ("NCIE-002", "Ch.29", "Approved technologies require governed version/license/lifecycle tracking, distinct from the choosing record (Ch.35)."),
    ]),
    ("h2", "33.1 Technology Registry vs Technology Decision Matrix"),
    ("p",
     "The Technology Registry (this chapter) governs what has been institutionally approved: "
     "version, owner, license, support/security/lifecycle state. The Technology Decision Matrix "
     "(Chapter 35) records the choosing process: candidate, rationale, alternative, status. These "
     "are independent axes — a Ch.35 status of APPROVED UPSTREAM MANDATE describes where a "
     "requirement originated (already dictated by NCIE-001/002/003); it is not the same thing as a "
     "Registry Lifecycle State of Approved, which records that NCA has institutionally confirmed the "
     "specific technology. A capability can be an Approved Upstream Mandate while its chosen "
     "implementation technology is still Proposed — pending approval, exactly as most rows in "
     "Chapter 35 now show after the mandate/implementation audit in §33.1A below."),
    ("h3", "33.1A Mandate/Implementation Separation (Audit Finding)"),
    ("p",
     "A prior edition over-classified several implementation mechanisms as APPROVED UPSTREAM "
     "MANDATE merely because the capability they served was mandated (e.g. WAL archiving for a "
     "mandated PITR capability, Vault Transit for mandated tokenization, a named event-broker topic "
     "for a mandated fail-closed audit behaviour). This edition corrects every such row: the status "
     "now reflects whether the exact technology/pattern shown — not merely the underlying capability "
     "— was itself dictated by NCIE-001/002/003. Where it was not, the row is reclassified PROPOSED "
     "DESIGN DEFAULT, and its Engineering Characteristics column states the mandate separately from "
     "the implementation. Chapter 35 reflects this corrected classification, extracted directly from "
     "the chapter tables so the two never drift apart."),
    ("h2", "33.2 NCIE Technology Registry (Seeded)"),
    ("table",
     ["Technology", "Purpose", "Category", "Version Policy", "Deployment Scope", "Owner", "License", "Lifecycle State"],
     [
        ["PostgreSQL", "Transactional canonical store", "Database", "Latest stable major, security-patched", "Ch.11 (+ PostGIS/pgvector/TimescaleDB extensions, Ch.7/12/16)", "NCIE Architecture Function", "PostgreSQL (open)", "Proposed — pending approval"],
        ["Kubernetes", "Container orchestration", "Runtime", "N-1 minor version support window", "All containerized services (Ch.4)", "NCIE Architecture Function / NCA IT Infrastructure", "Apache 2.0 (open)", "Proposed — pending approval"],
        ["Apache Kafka", "Event streaming/messaging", "Integration", "LTS releases only", "Event broker (Ch.9)", "NCIE Architecture Function", "Apache 2.0 (open)", "Proposed — pending approval"],
        ["Redis", "Cache and distributed state", "Data", "Latest stable, security-patched", "Ch.17", "NCIE Architecture Function", "BSD/RSALv2 (verify license terms at approval)", "Proposed — pending approval"],
        ["OpenSearch", "Search and retrieval", "Data", "Latest stable major", "Ch.14", "NCIE Architecture Function", "Apache 2.0 (open)", "Proposed — pending approval"],
        ["Neo4j", "Graph technology", "Data", "Latest stable, community or enterprise per licensing decision", "Ch.15", "NCIE Architecture Function", "GPL (community) / commercial (enterprise) — confirm at approval", "Proposed — pending approval"],
        ["pgvector", "Vector retrieval (launch scale)", "Data / AI", "Tracks PostgreSQL major version", "Ch.16", "NCIE Architecture Function", "PostgreSQL (open)", "Proposed — pending approval"],
        ["MapLibre GL", "GIS/map rendering", "Visualization", "Latest stable", "Ch.7", "NCIE Architecture Function", "BSD (open)", "Proposed — pending approval"],
        ["Keycloak", "Identity provider / SSO", "Security", "Latest stable, security-patched", "Ch.23", "NCA IT Security", "Apache 2.0 (open)", "Proposed — pending approval"],
        ["HashiCorp Vault", "Secrets/KMS", "Security", "Latest stable, security-patched", "Ch.24-25", "NCA IT Security", "BUSL (verify license terms at approval)", "Proposed — pending approval"],
        ["Temporal", "Durable workflow engine", "Integration", "Latest stable", "Ch.10", "NCIE Architecture Function", "MIT (open)", "Proposed — pending approval"],
        ["Prometheus / Grafana", "Metrics and dashboards", "Observability", "Latest stable", "Ch.26", "NCIE Architecture Function", "Apache 2.0 (open)", "Proposed — pending approval"],
        ["OpenTelemetry", "Tracing/instrumentation", "Observability", "Latest stable SDK per language", "Ch.26", "NCIE Architecture Function", "Apache 2.0 (open)", "Proposed — pending approval"],
        ["MinIO", "Object/evidence storage", "Data", "Latest stable, security-patched", "Ch.13", "NCIE Architecture Function", "AGPLv3 (verify license terms at approval)", "Proposed — pending approval"],
        ["React / TypeScript", "Frontend framework/type system", "Application", "Latest stable LTS-equivalent", "Ch.6", "NCIE Architecture Function", "MIT (open)", "Proposed — pending approval"],
        ["RPA Provider (unnamed)", "Legacy/portal automation", "Integration", "Per vendor support policy", "Ch.32, behind Capability Registry", "NCA Automation Governance", "Commercial — depends on NCA's existing licence", "Institutional confirmation required"],
    ],
     "Seeded NCIE Technology Registry — representative approved-candidate entries, none yet institutionally approved."),
    ("h3", "33.2A Version Policy, Not Pinned Versions"),
    ("p",
     "Every entry above states an approved version policy or supported-release window (e.g. \"N-1 "
     "minor version support window\", \"LTS releases only\") rather than a pinned exact version "
     "number. Fixing a specific major version before hosting/deployment discovery (Ch.3) is complete "
     "would create needless rework; the policy is what this Registry governs, and the exact "
     "in-service version is tracked operationally against that policy once deployed."),
    ("h2", "33.3 Lifecycle, Promotion and Deprecation"),
    ("proposed",
     "Registry promotion invariant: a Technology Registry entry shall not transition to Approved "
     "merely because its associated Proposed Design Default has been used in downstream design, "
     "prototyping or specification work (see Ch.35 §35.5). Approval requires an explicit "
     "institutional decision recorded against the applicable Technology Decision ID, with approving "
     "actor and date — the same discipline NCIE-003 Ch.24 requires before a Rule Version is treated "
     "as effective. A capability's Ch.35 status of APPROVED UPSTREAM MANDATE never by itself promotes "
     "the chosen implementation technology's Registry Lifecycle State.",
    ),
    ("bullets", [
        "Vulnerability status is tracked per entry via Ch.28's SCA scanning; a critical unpatched vulnerability moves Security Status to At Risk and blocks new deployments matching that version policy.",
        "Deprecation/replacement follows the same change-control discipline as NCIE-003 Ch.1 §1.4 — a superseding entry is added, the prior entry is marked Deprecated with a sunset date, never silently removed.",
    ]),
    ("review", [
        "Confirm license terms (BUSL/AGPL/RSALv2-class technologies above) against NCA procurement/legal policy before approval.",
    ]),
    ("trace", "NCIE-002 Ch.29."),
]

# ---------------------------------------------------------------------------
# Chapter 34 — Reference Deployment Topology & Environment Blueprint
# ---------------------------------------------------------------------------
BLOCKS[34] = [
    ("upstream", [
        ("NCIE-002", "Ch.26 §26.7, Ch.29", "Trust-zone segmentation and environment separation must be visible as a concrete deployment topology, not only a principle."),
    ]),
    ("h2", "34.1 Technology Stack Layer Model"),
    ("flow",
     [
        "Edge / API layer (Ch.8: gateway, TLS, rate limiting)",
        "Application layer (Ch.5-7, Ch.20-22: backend services, frontend, ARGUS/collaboration)",
        "Data layer (Ch.11-17: transactional, analytical, object, search, graph, vector, cache)",
        "AI layer (Ch.18-19: Model Gateway, guardrails, evaluation)",
        "Integration layer (Ch.9-10, Ch.32: events, workflow, adapters/RPA)",
        "Security & observability layer (Ch.23-27: IAM, secrets, DLP, telemetry, SecOps)",
        "Management/governance layer (Ch.28, Ch.33: CI/CD, Technology Registry)",
     ],
     "Technology Stack Layer Model — how Chapters 4-33 compose into one platform."),
    ("h2", "34.2 Logical Deployment Topology"),
    ("rel",
     [
        ("Public/Operator Network", "reaches via TLS/API gateway", "Edge/API Zone"),
        ("Edge/API Zone", "routes authenticated calls to", "Application Zone"),
        ("Application Zone", "reads/writes via governed contracts to", "Data Zone"),
        ("Application Zone", "invokes ARGUS via Model Gateway in", "AI Zone"),
        ("AI Zone", "never crosses directly into", "Data Zone (goes via Application Zone's authorization boundary)"),
        ("Security/Observability Zone", "monitors and gates", "Edge, Application, Data, AI and Integration Zones"),
        ("Management/Governance Zone", "deploys and governs", "all zones via CI/CD (Ch.28) and the Technology Registry (Ch.33)"),
     ],
     "Logical deployment topology across NCIE-002 Ch.26's trust zones."),
    ("h2", "34.3 Data Technology Topology"),
    ("rel",
     [
        ("Transactional Store (Ch.11, PostgreSQL default)", "is the canonical source for", "Analytical/Time-Series Store (Ch.12)"),
        ("Transactional Store", "is the canonical source for", "Search Index (Ch.14) and Vector Index (Ch.16)"),
        ("Transactional Store", "is the canonical source for", "Graph Store (Ch.15)"),
        ("Object/Evidence Store (Ch.13)", "is referenced by pointer from", "Transactional Store (never embedded copies)"),
        ("Cache (Ch.17)", "is a derived, rebuildable accelerator over", "Transactional Store and Rule/Session state"),
        ("All derived stores", "are rebuildable from and never independently canonical relative to", "Transactional Store"),
     ],
     "Data technology topology: canonical-vs-derived store relationships (NCIE-003 Ch.32 §32.5)."),
    ("review", [
        "Confirm the final zone-to-network-segment mapping with NCA IT Infrastructure once hosting facility (Ch.3) is confirmed.",
    ]),
    ("trace", "NCIE-002 Ch.26, Ch.29; NCIE-003 Ch.32."),
]

# ---------------------------------------------------------------------------
# Chapter 35 — Technology Decision Matrix, Proposed Defaults & Human Review Register
# ---------------------------------------------------------------------------
_counts = summary_counts()

BLOCKS[35] = [
    ("upstream", [
        ("NCIE-002", "—", "Consolidates every technology decision from Chapters 2-32 into one authoritative matrix, per the mandatory-consolidation directive."),
    ]),
    ("h2", "35.1 Purpose"),
    ("p",
     "Consolidates every technology decision raised in Chapters 2-32 into one Technology Decision "
     "Matrix, and every non-mandate decision into one Human Review Register, classified Blocking or "
     "Non-Blocking and by reason. Individual chapters are not repeated here beyond a Decision ID and "
     "one-line capability/status — the rationale, alternative and engineering characteristics remain "
     "in the owning chapter."),
    ("h2", "35.2 Summary"),
    ("table",
     ["Metric", "Count"],
     [
        ["Total technology decisions (Ch.2-32)", str(_counts["total"])],
        ["Approved Upstream Mandate", str(_counts["mandate"])],
        ["Proposed Design Default", str(_counts["proposed"])],
        ["Institutional Confirmation Required", str(_counts["institutional"])],
        ["Infrastructure Discovery Required", str(_counts["infrastructure"])],
        ["Security/Sovereignty Confirmation Required", str(_counts["security"])],
        ["Blocking (Institutional + Infrastructure + Security)", str(_counts["blocking"])],
        ["Non-Blocking open (Proposed Design Default)", str(_counts["non_blocking_open"])],
    ],
     "Technology Decision Matrix summary counts."),
    ("h2", "35.3 Technology Decision Matrix"),
    ("p", "Every technology decision from Chapters 2-32, in chapter order. Full rationale, "
         "alternative and engineering characteristics remain in the cited chapter."),
    ("table",
     ["Decision ID", "Ch.", "Capability", "Proposed/Default", "Status"],
     matrix_rows(),
     "Complete Technology Decision Matrix (Chapters 2-32)."),
    ("h2", "35.4 Human Review Register"),
    ("p",
     "Every decision not yet an Approved Upstream Mandate, classified Blocking (requires resolution "
     "before that technology can be treated as settled) or Non-Blocking (a defensible default that "
     "may proceed provisionally) and by reason."),
    ("table",
     ["Decision ID", "Ch.", "Capability", "Reason", "Blocking?"],
     review_rows(),
     "Human Review Register: all non-mandate technology decisions."),
    ("h2", "35.5 Prioritisation and the Limits of a Non-Blocking Default"),
    ("p",
     f"The {_counts['blocking']} Blocking items (Institutional/Infrastructure/Security) should be "
     "resolved before their affected chapters' technology can move to Approved status."),
    ("proposed",
     f"Non-Blocking Proposed Design Defaults ({_counts['non_blocking_open']} items) may be used "
     "provisionally for downstream design continuation, prototyping, proof-of-concept work, "
     "technical elaboration and specification development in NCIE-005 through NCIE-016. They shall "
     "not be interpreted as procurement approval, production authorization or institutional "
     "technology approval. Moving a Non-Blocking item from Proposed to Registry Lifecycle State "
     "Approved (Ch.33 §33.3) still requires an explicit institutional decision against its Decision "
     "ID — non-blocking status affects what may proceed provisionally, not what has been approved.",
    ),
    ("trace", "Consolidates Chapters 2-32; individual chapters trace to NCIE-002/003 as cited therein."),
]

# ---------------------------------------------------------------------------
# Chapter 36 — NCIE-004 Acceptance, Traceability & Handover Gate
# ---------------------------------------------------------------------------
BLOCKS[36] = [
    ("upstream", [
        ("NCIE-002", "—", "Formal closure of the authority chain: NCIE-001 requirements → NCIE-002 architecture → NCIE-003 canonical data → NCIE-004 technology."),
    ]),
    ("h2", "36.1 Traceability Matrix"),
    ("table",
     ["Ch.", "Title", "Primary Upstream Dependency"],
     [
        ["1", "Engineering Mandate & Selection Doctrine", "NCIE-002 Ch.1"],
        ["2", "Engineering Principles & Standards", "NCIE-003 Ch.2, Ch.30"],
        ["3", "Target Runtime, Hosting & Environment", "NCIE-002 Ch.1 §1.6, Ch.26, Ch.28, Ch.30; NCIE-003 Ch.32, Ch.35-36"],
        ["4", "Containerization & Orchestration", "NCIE-002 Ch.4 §4.2, Ch.29, Ch.30"],
        ["5", "Backend Application Stack", "NCIE-002 Ch.4, Ch.5, Ch.25"],
        ["6", "Frontend Web Application Stack", "NCIE-002 Ch.3, Ch.30 §30.4"],
        ["7", "Design System, Visualization & GIS", "NCIE-002 Ch.3, Ch.8, Ch.30 §30.4; NCIE-003 Ch.8"],
        ["8", "API Gateway & Service Communication", "NCIE-002 Ch.4, Ch.25; NCIE-003 Ch.33"],
        ["9", "Event Streaming & Messaging", "NCIE-002 Ch.25; NCIE-003 Ch.23, Ch.28"],
        ["10", "Workflow, BPM & Process Engine", "NCIE-002 Ch.21; NCIE-003 Ch.23"],
        ["11", "Transactional Database", "NCIE-002 Ch.5; NCIE-003 Ch.5, Ch.24, Ch.32"],
        ["12", "Analytical/Time-Series Platform", "NCIE-002 Ch.30; NCIE-003 Ch.7, Ch.11, Ch.32, Ch.35"],
        ["13", "Object/Document/Evidence Storage", "NCIE-003 Ch.6, Ch.17, Ch.31, Ch.35"],
        ["14", "Search, Indexing & Retrieval", "NCIE-003 Ch.4 §4.89-4.93, Ch.36"],
        ["15", "Graph Technology", "NCIE-003 Ch.5, Ch.19"],
        ["16", "Vector Retrieval & Semantic Search", "NCIE-002 Ch.26 §26.3; NCIE-003 Ch.36 §36.4"],
        ["17", "Cache & Distributed State", "NCIE-002 Ch.4, Ch.30 §30.5"],
        ["18", "ARGUS AI Platform & Model Gateway", "NCIE-002 Ch.19 §19.11, Ch.24; NCIE-003 Ch.20"],
        ["19", "AI Guardrails, Evaluation & Safety", "NCIE-002 Ch.19, Ch.24"],
        ["20", "Agentic Orchestration & Tool Gateway", "NCIE-002 Ch.19, Ch.21; NCIE-003 Ch.20, Ch.23"],
        ["21", "Collaborative Intelligence Stack", "NCIE-002 Ch.19, Ch.20; NCIE-003 Ch.20-21, Ch.27"],
        ["22", "Memory, Knowledge & Context Stack", "NCIE-002 Ch.20 §20.2, §20.12; NCIE-003 Ch.22"],
        ["23", "Identity, Authentication & Access", "NCIE-002 Ch.4, Ch.26; NCIE-003 Ch.26"],
        ["24", "Secrets, Keys, Certificates & Crypto", "NCIE-002 Ch.26, Ch.29 §29.6; NCIE-003 Ch.14 §14.6, Ch.36"],
        ["25", "Data Protection, DLP & Masking", "NCIE-002 Ch.26; NCIE-003 Ch.14, Ch.31, Ch.36"],
        ["26", "Observability & Telemetry", "NCIE-002 Ch.27; NCIE-003 Ch.29, Ch.37"],
        ["27", "Security Operations & SIEM", "NCIE-002 Ch.26; NCIE-003 Ch.27"],
        ["28", "DevSecOps & CI/CD Toolchain", "NCIE-002 Ch.29"],
        ["29", "Testing & Quality Engineering", "NCIE-002 Ch.31; NCIE-003 Ch.38"],
        ["30", "Resilience, Backup & DR", "NCIE-002 Ch.28, Ch.29 §29.9; NCIE-003 Ch.5, Ch.25"],
        ["31", "Performance & Capacity Engineering", "NCIE-002 Ch.30"],
        ["32", "Integration Adapters, RPA & Legacy", "NCIE-002 Ch.21; NCIE-003 Ch.6, Ch.23, Ch.34"],
        ["33", "Technology Registry & Lifecycle", "NCIE-002 Ch.29"],
        ["34", "Reference Deployment Topology", "NCIE-002 Ch.26 §26.7, Ch.29; NCIE-003 Ch.32"],
        ["35", "Technology Decision Matrix & Review Register", "Consolidates Ch.2-32"],
        ["36", "Acceptance, Traceability & Handover", "Closes NCIE-001→002→003→004 authority chain"],
    ],
     "NCIE-004 chapter-to-upstream traceability matrix."),
    ("h2", "36.2 Acceptance Checklist"),
    ("bullets", [
        "No material contradiction with NCIE-002/003 remains unresolved (none flagged STRUCTURAL CHANGE REQUIRED in this edition, per Ch.1 §1.2).",
        "Every technology decision in Ch.35's matrix carries one of the five statuses in front matter §0.3 — none is asserted as settled fact beyond its actual status.",
        "The Technology Registry (Ch.33) and Decision Matrix (Ch.35) agree — every Registry entry traces to a Ch.35 Decision ID.",
        "No named product anywhere in this document is asserted as \"NCIE uses X\" beyond Approved Upstream Mandate status.",
        "Provider neutrality is preserved for AI models, cloud, databases, search, vector stores, graph technology, workflow engines, message brokers and external integration providers (Ch.9-10, Ch.14-18, Ch.32).",
        "ARGUS engineering (Ch.18) never architects directly around one provider SDK.",
        "The AI outage boundary (Ch.18 §18.3, Ch.19) is preserved: deterministic NCIE operation continues without ARGUS.",
        "Ghana Card/Passport and Anti-Fraud location protections (Ch.25) apply consistently across every chapter that touches them.",
        "The surcharge rate and SIM registration limits remain governed Rule/Parameter values (NCIE-003 Ch.24), never hard-coded anywhere in this stack.",
    ]),
    ("h2", "36.3 Technology Registry Snapshot"),
    ("p",
     "This gate references Chapter 33's Registry as of this edition: 16 seeded technologies, all at "
     "Lifecycle State \"Proposed — pending approval\" or \"Institutional confirmation required\" — "
     "none yet Approved. No entry advances without an institutional decision recorded against its "
     "Chapter 35 Decision ID."),
    ("h2", "36.4 Handover"),
    ("p",
     "On acceptance, this technology baseline hands forward to NCIE-005 (ARGUS), NCIE-006 (Memory), "
     "NCIE-007 (AI/Agent Orchestration), NCIE-009 (Security Architecture), NCIE-011 (API/Integration), "
     "NCIE-012 (UX/UI), NCIE-014 (Database & Storage Engineering), NCIE-015 (DevSecOps/Infrastructure) "
     "and NCIE-016 (Testing) — each of which implements this document's technology families in detail "
     "without re-deciding them, per Ch.1 §1.3's boundary."),
    ("review", [
        "Confirm NCIE-004 approvers and their scope of authority.",
        "Confirm which of Ch.35's Blocking items must close before NCIE-005/006/007/009/011/012/014/015/016 may begin detailed implementation versus which may proceed against the Proposed Design Default provisionally.",
    ]),
    ("trace", "Closes the NCIE-001 → NCIE-002 → NCIE-003 → NCIE-004 authority chain (front matter §0.1)."),
]
