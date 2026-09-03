"""Content model for NCIE-003 Data Model & Data Dictionary.

CHAPTERS is populated in production batches (1-6, 7-14, 15-22, 23-30,
31-38, 39-43). Block kinds consumed by ncie003_common.render_blocks:
  ("h2", text) / ("h3", text) / ("p", text) / ("bullets", [items])
  ("proposed", text) / ("upstream", text) / ("trace", text) / ("trace002", text)
  ("review", [(category, text), ...])  -- category in REVIEW_CATEGORIES
  ("flow", [nodes], caption) / ("rel", [(s,r,t), ...], caption)
  ("table", headers, rows, caption) / ("pagebreak",)
"""

CHAPTER_TITLES = {
    1: "Document Governance, Purpose & Data-Modelling Mandate",
    2: "Data Architecture Principles & Modelling Standards",
    3: "Enterprise Canonical Data Model",
    4: "Common Entity, Identifier & Reference Model",
    5: "Temporal & Bitemporal Data Model",
    6: "Source, Provider, Acquisition & Ingestion Data Model",
    7: "Network Intelligence Data Model",
    8: "Topology, GIS & Spatial Data Model",
    9: "QoS Campaign & Drive-Test Data Model",
    10: "Incident Intelligence Data Model",
    11: "Traffic Intelligence Data Model",
    12: "Revenue Intelligence & Billing Verification Data Model",
    13: "Mobile Money Intelligence Data Model",
    14: "SIM Registration Intelligence Data Model",
    15: "Anti-Fraud / SIMBOX Intelligence Data Model",
    16: "Regulatory Case, Finding & Decision Data Model",
    17: "Evidence & Evidence Relationship Model",
    18: "REWS Alert, Situation & National Operating Picture Data Model",
    19: "Cross-Domain Fusion & Intelligence Graph Model",
    20: "ARGUS Interaction & AI Provenance Data Model",
    21: "Collaborative Intelligence & Multi-User Brainstorming Data Model",
    22: "Memory & Institutional Knowledge Data Model",
    23: "Workflow, Automation, RPA & Tasking Data Model",
    24: "Rules, Configuration & Calculation Data Model",
    25: "Provenance, Lineage & Decision-Time Data Model",
    26: "Identity, Authorization & Security Data Model",
    27: "Audit & Accountability Data Model",
    28: "Notification, Event & Integration Data Model",
    29: "Data Quality, Validation & Exception Model",
    30: "Metadata Catalogue & Data Dictionary Architecture",
    31: "Classification, Privacy, Retention & Data Lifecycle",
    32: "Physical Data Design & Storage Mapping",
    33: "Data API, Schema & Event Contract Standards",
    34: "Migration, Legacy Data & Master Data Reconciliation",
    35: "Data Performance, Partitioning, Archival & Scalability",
    36: "Data Security & Sovereignty Controls",
    37: "Data Observability, Reconciliation & Operational Management",
    38: "Data Testing, Verification & Acceptance",
    39: "Canonical Data Dictionary",
    40: "Entity Relationship Catalogue & Reference Diagrams",
    41: "Requirements Traceability & NCIE-002 Crosswalk",
    42: "Open Institutional Decisions & Human Review Register",
    43: "NCIE-003 Acceptance Checklist & Handover to NCIE-004",
}

CHAPTER_SCOPE = {
    1: "Defines why NCIE-003 exists, what it governs, and how its data definitions become authoritative across implementation.",
    2: "Sets the modelling rules every NCIE domain must follow so that data remains consistent, temporal, traceable and secure.",
    3: "Provides the top-level view of the major objects and relationships across the whole NCIE ecosystem.",
    4: "Defines how NCIE identifies the same real-world or system object consistently across domains and source systems.",
    5: "Defines all time semantics needed to reconstruct what happened, when NCIE learned it, and which rules applied.",
    6: "Models where data comes from, how it enters NCIE, and how source lineage is retained.",
    7: "Defines the canonical data objects for network performance monitoring and QoS intelligence.",
    8: "Defines the geographic and network-topology objects used for mapping and spatial analysis.",
    9: "Defines field-testing campaigns, routes, devices, test points and measurements.",
    10: "Defines reported and observed incidents, affected scope, restoration and incident timelines.",
    11: "Defines international, off-net and on-net traffic observations and their reporting semantics.",
    12: "Defines revenue calculation inputs/results, international incoming traffic surcharge rules, billing verification and reconciliation.",
    13: "Defines daily aggregate Mobile Money transfer amounts sent and received on each network.",
    14: "Defines SIM registrations, identity type, countable registrations, configurable limits and registration exceptions.",
    15: "Defines the data required to detect, investigate, locate and block SIMs associated with suspected SIMBOX activity.",
    16: "Defines the formal regulatory objects through which intelligence becomes an institutional case, finding or decision.",
    17: "Defines evidence objects, integrity, annotations, corrections, invalidation and relationships to reasoning.",
    18: "Defines Conditions, Alerts, Situations and the data required to compose the national situational picture.",
    19: "Defines how objects from different domains may be connected for cross-domain analysis without losing their native meaning.",
    20: "Defines data needed to govern ARGUS participation, tools, model routing and AI-originated analytical objects.",
    21: "Defines persistent collaborative Rooms in which humans and ARGUS can brainstorm, challenge, hypothesize and preserve structured reasoning.",
    22: "Defines long-term memory classes and how reviewed experience becomes reusable Institutional Knowledge.",
    23: "Defines persistent workflows, approvals, tasks, waiting dependencies and automated execution state.",
    24: "Defines governed rules and configurable parameters used by deterministic NCIE calculations and thresholds.",
    25: "Defines end-to-end source lineage and dependency structures needed for defensible historical reconstruction.",
    26: "Defines workforce/service identities, roles, attributes, permissions, delegated authority and data classification relationships.",
    27: "Defines the accountable record of who accessed, changed, approved, executed or revealed sensitive NCIE information.",
    28: "Defines internal domain events, event envelopes, subscriptions and notification-delivery state.",
    29: "Defines how NCIE represents invalid, incomplete, stale, partial or conflicting data.",
    30: "Defines the metadata fields that every eventual data-dictionary entry must contain.",
    31: "Defines how NCIE data is classified, retained, archived, held and securely disposed of.",
    32: "Maps logical entities into storage technologies after the logical model is approved.",
    33: "Defines how data contracts are serialized, versioned and evolved across services.",
    34: "Defines how existing NCA and operator historical data will be imported and reconciled to canonical NCIE entities.",
    35: "Defines how the data layer will handle large current and historical volumes without corrupting semantics.",
    36: "Defines technical data-layer protections for confidentiality, integrity and jurisdictional control.",
    37: "Defines operational telemetry for freshness, pipeline health, schema drift and reconciliation.",
    38: "Defines how the data architecture and dictionary will be verified before implementation baseline approval.",
    39: "Holds the authoritative Data Dictionary structure and representative fully worked canonical entities.",
    40: "Provides authoritative conceptual and logical ER diagrams and relationship catalogues that agree with the Data Dictionary.",
    41: "Maps every significant data object and field back to the requirements and architecture that justify it.",
    42: "Captures data decisions that architecture cannot legitimately settle without NCA confirmation.",
    43: "Defines the formal gate for accepting NCIE-003 and handing its canonical data contracts to the next NCIE artifact.",
}

FRONT_MATTER = {
    "governance_rows": [
        ("Document", "NCIE-003 Data Model & Data Dictionary"),
        ("Edition", "In development — Version 0.4 (VPF & Dynamic Agent Synthesis Canonical-Data Consistency Amendment)"),
        ("Baseline authorized", "NCIE-003 Skeletal v0.2 — approved for full expansion (superseding its “FOR REVIEW” stamp)"),
        ("Prior baseline", "NCIE-003 v0.3 Full Data Model & Data Dictionary (APPROVED Canonical Data Architecture Baseline, subject to controlled data-discovery completion) — historically preserved; see §0.8"),
        ("Requirements authority", "NCIE-001 Master Product Requirements Document, Version 1.3 (VPF & Dynamic Agent Synthesis Consistency Amendment) — APPROVED"),
        ("Architecture authority", "NCIE-002 System Architecture & Technical Design, Version 0.5 (VPF & Dynamic Agent Synthesis Architectural Consistency Amendment) — APPROVED"),
        ("Orchestration authority", "NCIE-007 AI, Agent & Model Orchestration Specification, Version 1.1 — APPROVED"),
        ("Chapter count", "43 (locked structural baseline; unchanged by this amendment; the Suite register's “Technology Stack & Engineering Blueprint” entry for NCIE-003 is superseded and reconciled separately, not by this document)"),
        ("Owner", "National Communications Intelligence Ecosystem (NCIE) Architecture Function"),
        ("Reviewer", "David King Boison (PhD) — Academic Intelligence Center"),
        ("Status", "IN DEVELOPMENT — FOR HUMAN REVIEW OF SURGICAL AMENDMENT. Not Approved. The v0.3 approval remains historically preserved until v0.4 is reviewed and approved."),
    ],
}

CHAPTERS = [
    {
        "number": n,
        "title": CHAPTER_TITLES[n],
        "scope": CHAPTER_SCOPE[n],
        "blocks": [],
    }
    for n in range(1, 44)
]


def get_chapter(number):
    for chapter in CHAPTERS:
        if chapter["number"] == number:
            return chapter
    raise KeyError(number)


def set_blocks(number, blocks):
    get_chapter(number)["blocks"] = blocks
