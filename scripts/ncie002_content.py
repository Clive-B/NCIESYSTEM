"""Content model for NCIE-002 System Architecture & Technical Design.

CHAPTERS is populated in production batches (front matter, 1-8, 9-16,
17-24, 25-32). Each chapter dict has: number, title, scope, blocks.
Block tuple kinds consumed by ncie002_common.render_blocks:
  ("h2", text) / ("h3", text) / ("p", text) / ("bullets", [items])
  ("status", text) / ("proposed", text) / ("trace", text)
  ("flow", [nodes], caption) / ("rel", [(s,r,t), ...], caption)
  ("table", headers, rows, caption) / ("pagebreak",)
"""

CHAPTER_TITLES = {
    1: "Architecture Mandate, Scope & Design Principles",
    2: "System Context, Actors, Trust Boundaries & External Systems",
    3: "Full-Screen UX & Situational Awareness Workspace",
    4: "Identity, Authorization & Zero-Trust",
    5: "Canonical Data Platform, Domain Model & Metadata",
    6: "Source Registry, Acquisition & Ingestion",
    7: "Network Intelligence, NMS, PM & KPI",
    8: "Topology, GIS, Spatial Intelligence & Mapping",
    9: "QoS Campaign / Drive-Test Intelligence",
    10: "Incident Intelligence & Operator Email",
    11: "Traffic Intelligence",
    12: "Revenue Intelligence & Billing Verification",
    13: "Mobile Money Intelligence",
    14: "SIM Registration Intelligence",
    15: "Anti-Fraud / SIMBOX Intelligence",
    16: "Regulatory Intelligence, Cases, Findings & Decisions",
    17: "Cross-Domain Fusion & Intelligence Graph",
    18: "REWS, Alerts, Situations & National Operating Picture",
    19: "Intelligence Assistant & Conversational Orchestration",
    20: "Memory, Collaborative Intelligence & Multi-User Brainstorming",
    21: "Automation Orchestrator, RPA, Scheduling & Persistent Workflows",
    22: "Rules, Calculation, Configuration & Temporal Governance",
    23: "Evidence, Provenance, Audit & Decision-Time Reconstruction",
    24: "AI Platform, Model Gateway, Guardrails & Evaluation",
    25: "API, Event Bus & Integration Contracts",
    26: "Security, Privacy, Sovereignty & Sensitive Data",
    27: "Observability, Health, Operations & Support",
    28: "Resilience, High Availability, Backup & Disaster Recovery",
    29: "Deployment, Environments, DevSecOps & Configuration",
    30: "Performance, Scalability, Accessibility & Non-Functional Architecture",
    31: "Testing, Verification, Traceability & Acceptance Architecture",
    32: "Operations, Administration, Documentation & Codex Handover",
}

CHAPTER_SCOPE = {
    1: "Defines the architectural mandate and non-negotiable principles translating NCIE-001 v1.2 into buildable systems.",
    2: "Maps every user, external system, provider and trust boundary around NCIE.",
    3: "Defines the main operating experience.",
    4: "Defines authentication and permission enforcement.",
    5: "Defines the shared data foundation.",
    6: "Defines how sources enter NCIE.",
    7: "Defines national-to-cell network intelligence.",
    8: "Defines place-to-cell resolution and mapping.",
    9: "Defines driven-test evidence reuse.",
    10: "Converts daily outage/fibre-cut/restoration email into governed incidents.",
    11: "Defines International, Off-Net and On-Net Traffic.",
    12: "Defines deterministic Revenue calculation and reconciliation.",
    13: "Defines approved aggregate Mobile Money intelligence.",
    14: "Defines protected identity/SIM intelligence and exception classification.",
    15: "Defines the broader Anti-Fraud domain.",
    16: "Defines regulatory workflow and reuse of the existing Regulatory Intelligence platform.",
    17: "Defines relationships across domains without false causation.",
    18: "Defines alerting and multi-domain Situations.",
    19: "Defines the Assistant as a governed NCIE interface.",
    20: "Defines persistent memory, permission-aware multi-user brainstorming, and the architecture that allows the NCIE Intelligence Assistant to participate as a governed, non-dominant collaborator.",
    21: "Defines provider-neutral automation.",
    22: "Centralizes changeable rules and deterministic calculations.",
    23: "Defines defensibility from source to decision.",
    24: "Defines AI integration without giving the model ownership of NCIE state.",
    25: "Defines reliable inter-service communication.",
    26: "Defines technical protection of sensitive intelligence.",
    27: "Defines how NCIE itself is monitored.",
    28: "Defines failure behavior and recovery.",
    29: "Defines controlled build and deployment.",
    30: "Defines measurable quality attributes.",
    31: "Defines how every requirement will be proven.",
    32: "Defines sustainable production ownership and the package handed to Codex/implementation teams.",
}

FRONT_MATTER = {
    "governance_rows": [
        ("Document", "NCIE-002 System & Solution Architecture Specification"),
        ("Edition", "In development — Version 0.5 (VPF & Dynamic Agent Synthesis Architectural Consistency Amendment)"),
        ("Supersedes", "NCIE-002 v0.4 Production Ready (17 August 2026), which itself superseded the Skeletal Architecture Review Edition v0.4 (chapter structure preserved throughout)"),
        ("Prior baseline", "NCIE-002 v0.4 Production Ready (17 August 2026) — historically preserved; see §1.8"),
        ("Authoritative source", "NCIE-001 Master Product Requirements Document, Version 1.3 (VPF & Dynamic Agent Synthesis Consistency Amendment)"),
        ("Amendment authority", "NCIE-007 AI, Agent & Model Orchestration Specification, Version 1.1"),
        ("Chapter count", "32 (revised up from the 20 recorded in the NCIE Production Documentation Suite register; see §1.4). Chapter structure unchanged by this amendment."),
        ("Owner", "National Communications Intelligence Ecosystem (NCIE) Architecture Function"),
        ("Assistant identity", "Presented to users as ARGUS — Adaptive Regulatory Governance & Unified Surveillance (Ch.19 §19.11)"),
        ("Reviewer", "David King Boison (PhD) — Academic Intelligence Center"),
        ("Status", "IN DEVELOPMENT — FOR HUMAN REVIEW OF SURGICAL AMENDMENT. Not Approved. The v0.4 approval remains historically preserved until v0.5 is reviewed and approved."),
    ],
}

CHAPTERS = [
    {
        "number": n,
        "title": CHAPTER_TITLES[n],
        "scope": CHAPTER_SCOPE[n],
        "blocks": [],
    }
    for n in range(1, 33)
]


def get_chapter(number):
    for chapter in CHAPTERS:
        if chapter["number"] == number:
            return chapter
    raise KeyError(number)


def set_blocks(number, blocks):
    get_chapter(number)["blocks"] = blocks
