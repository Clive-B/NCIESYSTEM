"""Content model for NCIE-004 Technology Stack & Engineering Blueprint.

CHAPTERS populated in 6 batches (1-6, 7-12, 13-18, 19-24, 25-30, 31-36) per
the approved production method. Block kinds consumed by
ncie004_common.render_blocks:
  ("h2", text) / ("h3", text) / ("p", text) / ("bullets", [items])
  ("upstream", [(doc_id, ref, consequence), ...])
  ("proposed", text) / ("trace", text) / ("review", [items])
  ("flow", [nodes], caption) / ("rel", [(s,r,t), ...], caption)
  ("table", headers, rows, caption, status_col_index_or_None)
"""

CHAPTER_TITLES = {
    1: "Engineering Mandate, Authority Chain & Technology Selection Doctrine",
    2: "Engineering Principles, Standards & Reference Conventions",
    3: "Target Runtime, Hosting & Environment Strategy",
    4: "Containerization, Orchestration & Workload Scheduling",
    5: "Backend Application & Service Engineering Stack",
    6: "Frontend Web Application Stack",
    7: "Design System, Visualization & Geospatial Technology",
    8: "API Gateway & Service Communication Stack",
    9: "Event Streaming, Messaging & Asynchronous Processing",
    10: "Workflow, BPM & Long-Running Process Engine",
    11: "Transactional Database Technology",
    12: "Analytical, Time-Series & Historical Data Platform",
    13: "Object, Document & Evidence Storage",
    14: "Search, Indexing & Retrieval Stack",
    15: "Graph Technology & Relationship Analytics",
    16: "Vector Retrieval & Semantic Search Technology",
    17: "Cache & Distributed State Technology",
    18: "ARGUS AI Platform & Model Gateway Technology",
    19: "AI Guardrails, Evaluation & Safety Engineering",
    20: "Agentic Orchestration & Tool Gateway Technology",
    21: "Collaborative Intelligence & Real-Time Collaboration Stack",
    22: "Memory, Knowledge & Context Engineering Stack",
    23: "Identity, Authentication & Access-Control Technology",
    24: "Secrets, Keys, Certificates & Cryptographic Services",
    25: "Data Protection, DLP, Masking & Protected Reveal",
    26: "Observability, Telemetry & Operational Monitoring Stack",
    27: "Security Operations, SIEM & Threat Detection Integration",
    28: "DevSecOps, Source Control & CI/CD Engineering Toolchain",
    29: "Testing, Quality Engineering & Test Automation Stack",
    30: "Resilience, Backup, Disaster Recovery & Business Continuity Technology",
    31: "Performance, Capacity, Scalability & Load Engineering",
    32: "Integration Adapters, RPA & Legacy-System Engineering",
    33: "Engineering Governance, Technology Registry & Lifecycle Management",
    34: "Reference Deployment Topology & Environment Blueprint",
    35: "Technology Decision Matrix, Proposed Defaults & Human Review Register",
    36: "NCIE-004 Acceptance, Traceability & Handover Gate",
}

CHAPTER_SCOPE = {
    1: "Governs technology selection under the approved NCIE authority chain.",
    2: "Sets enforceable engineering conventions across all implementation teams.",
    3: "Defines sovereign hosting, environment tiers and runtime placement.",
    4: "Defines service packaging, orchestration, scaling and workload isolation.",
    5: "Selects maintainable backend runtimes and service-engineering patterns.",
    6: "Selects the web stack for dashboards, workspaces and collaborative interfaces.",
    7: "Standardizes UI components, charts, maps and spatial visualization.",
    8: "Standardizes synchronous APIs, gateways and service-to-service communication.",
    9: "Standardizes durable events, queues and asynchronous processing.",
    10: "Selects durable workflow technology for approvals and long-running processes.",
    11: "Selects ACID storage for canonical transactional state.",
    12: "Selects high-volume analytical and historical query platforms.",
    13: "Selects governed storage for documents, evidence artifacts and snapshots.",
    14: "Selects authorization-aware full-text and faceted retrieval technology.",
    15: "Selects technology for governed cross-domain graph relationships.",
    16: "Selects classification-aware semantic/vector retrieval infrastructure.",
    17: "Defines cache and ephemeral distributed-state technology.",
    18: "Implements ARGUS through a provider-neutral, policy-aware Model Gateway.",
    19: "Engineers ARGUS guardrails, evaluation, regression and safe failure modes.",
    20: "Implements governed agent/tool orchestration without expanding authority.",
    21: "Implements persistent multi-user Rooms and human-ARGUS collaboration.",
    22: "Implements persistent memory, institutional knowledge and context reconciliation.",
    23: "Implements IAM for humans, services, workloads and ARGUS.",
    24: "Implements secrets, keys, certificates and cryptographic lifecycle controls.",
    25: "Implements masking, DLP, tokenization and governed protected reveal.",
    26: "Standardizes logs, metrics, traces, SLOs and operational observability.",
    27: "Integrates NCIE security telemetry with SOC/SIEM/threat-detection controls.",
    28: "Defines secure source control, CI/CD, artifact and software-supply-chain tooling.",
    29: "Defines automated functional, data, security, performance and AI testing.",
    30: "Defines HA, backup, DR, recovery testing and business-continuity technology.",
    31: "Defines load, capacity, scalability and performance-engineering practices.",
    32: "Implements replaceable adapters, RPA and legacy-system integration patterns.",
    33: "Governs approved technologies, versions, licensing and deprecation.",
    34: "Integrates the selected stack into a logical deployment topology.",
    35: "Consolidates proposed defaults, unresolved decisions, rationale and ownership.",
    36: "Defines traceability, acceptance and controlled handover of NCIE-004.",
}

FRONT_MATTER = {
    "governance_rows": [
        ("Document", "NCIE-004 Technology Stack & Engineering Blueprint"),
        ("Edition", "In development — Version 1.0"),
        ("Baseline authorized", "NCIE-004 Skeletal v0.1 — approved for full expansion; 36-chapter structure locked"),
        ("Requirements authority", "NCIE-001 Master Product Requirements Document, Version 1.2"),
        ("Architecture authority", "NCIE-002 System Architecture & Technical Design, Version 0.4"),
        ("Canonical data authority", "NCIE-003 Data Model & Data Dictionary, Version 0.3 (Canonical Data Architecture Baseline)"),
        ("Owner", "National Communications Intelligence Ecosystem (NCIE) Architecture Function"),
        ("Reviewer", "David King Boison (PhD) — Academic Intelligence Center"),
        ("Status", "IN DEVELOPMENT — FOR HUMAN REVIEW until explicitly approved; named vendors/products are proposed defaults only"),
    ],
}

CHAPTERS = [
    {
        "number": n,
        "title": CHAPTER_TITLES[n],
        "scope": CHAPTER_SCOPE[n],
        "blocks": [],
    }
    for n in range(1, 37)
]


def get_chapter(number):
    for chapter in CHAPTERS:
        if chapter["number"] == number:
            return chapter
    raise KeyError(number)


def set_blocks(number, blocks):
    get_chapter(number)["blocks"] = blocks
