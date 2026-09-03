"""NCIE-007 content batch: Chapters 35-36 (Human Review Register, Requirements
Traceability, Upstream Impact Register, Downstream Handover Register,
Acceptance & Handover Gate)."""

from ncie007_ch35_register import register_rows, summary_counts

BLOCKS = {}

_counts = summary_counts()

# ---------------------------------------------------------------------------
# Chapter 35 — Human Review Register, Open Decisions & Proposed Defaults
# ---------------------------------------------------------------------------
BLOCKS[35] = [
    ("upstream", [
        ("NCIE-007", "—", "Consolidates every Human Review Focus item from Chapters 1-34 into one authoritative register."),
    ]),
    ("h2", "35.1 Purpose"),
    ("p",
     "Consolidates every Human Review Focus item raised in Chapters 1-34, extracted directly from "
     "the chapter review blocks so this register cannot drift from its sources. Each item states "
     "precisely what it blocks; no unresolved optional capability is allowed to imply that the whole "
     "NCIE-007 architecture is unusable (handover items 1312/1370/1385)."),
    ("h2", "35.2 Summary"),
    ("table",
     ["Metric", "Count"],
     [
        ["Total items", str(_counts["total"])],
        ["Resolved by Upstream Baseline", str(_counts["resolved"])],
        ["Proposed Design Default", str(_counts["proposed"])],
        ["Institutional Confirmation Required", str(_counts["institutional"])],
        ["Security/Sovereignty Confirmation Required", str(_counts["security"])],
        ["Legal/Policy Confirmation Required", str(_counts["legal"])],
        ["Engineering/Infrastructure Discovery Required", str(_counts["infrastructure"])],
        ["Source/Workflow Discovery Required", str(_counts["workflow"])],
        ["Blocking", str(_counts["blocking"])],
        ["Non-Blocking", str(_counts["non_blocking"])],
    ],
     "Human Review Register summary counts."),
    ("h2", "35.3 Complete Register"),
    ("table",
     ["ID", "Ch.", "Issue", "Category", "Blocking?"],
     register_rows(),
     "Complete Human Review Register (Chapters 1-34)."),
    ("h2", "35.4 Mechanical Verification"),
    ("p",
     f"Per handover items 1311/1369, this register's totals are verified programmatically, not by "
     "inspection: the production build independently re-extracts every ('review', ...) block across "
     "Chapters 1-34 and asserts the result matches this chapter's own extraction (§35.2-§35.3) "
     "exactly, by category and by blocking status; a mismatch fails the build rather than reaching "
     f"this document. The current build confirms an exact match — {_counts['total']} items "
     f"({_counts['resolved']} Resolved / {_counts['proposed']} Proposed / "
     f"{_counts['institutional']} Institutional / {_counts['security']} Security / "
     f"{_counts['legal']} Legal / {_counts['infrastructure']} Infrastructure / "
     f"{_counts['workflow']} Workflow), {_counts['blocking']} Blocking / "
     f"{_counts['non_blocking']} Non-Blocking. This figure and §35.2's summary table are generated "
     "from the same computed extraction at build time, so they cannot diverge from one another."),
    ("h2", "35.5 Blocking Scope Discipline"),
    ("p",
     "Where a Blocking item remains open, it blocks only the specific capability it names — for "
     "example, generated-code Dynamic Agent activation (Ch.34 §34.4) remains blocked pending Security/"
     "Engineering confirmation while configuration-only Dynamic Agent Synthesis (Ch.11) remains fully "
     "specified and reviewable. No Blocking item is read as blocking the entire NCIE-007 "
     "architecture."),
    ("trace", "Consolidates Chapters 1-34; individual chapters trace to NCIE-002/003/004/005/006/007-S01 as cited therein."),
]

# ---------------------------------------------------------------------------
# Chapter 36 — Requirements Traceability, Acceptance & Handover Gate
# ---------------------------------------------------------------------------
BLOCKS[36] = [
    ("upstream", [
        ("NCIE-007", "—", "Closes the authority chain: NCIE-001 requirements → ... → NCIE-006 Memory & Context → NCIE-007 AI/Agent/Model Orchestration."),
    ]),
    ("h2", "36.1 Traceability Matrix"),
    ("table",
     ["Ch.", "Title", "Primary Upstream Dependency"],
     [
        ["1", "Mandate, Authority Chain & Specification Boundary", "NCIE-002 Ch.4, Ch.24; NCIE-005; NCIE-006"],
        ["2", "Orchestration Doctrine & Governing Invariants", "NCIE-002 Ch.4; NCIE-006 front matter §0.3"],
        ["3", "AI Runtime Actor & Capability Taxonomy", "NCIE-002 Ch.4"],
        ["4", "ARGUS Orchestrator Boundary", "NCIE-005 Ch.4"],
        ["5", "Model Gateway Contract", "NCIE-002 Ch.24"],
        ["6", "Approved Model Registry", "NCIE-004 Ch.18"],
        ["7", "Classification-, Purpose- & Task-Aware Model Routing", "NCIE-003 Ch.31"],
        ["8", "Provider Adapters & Provider Neutrality", "NCIE-004 Ch.18"],
        ["9", "Model Selection, Versioning & Reproducibility", "NCIE-003 Ch.28"],
        ["10", "Fallback, Failover & Degraded AI Operation", "NCIE-002 Ch.24"],
        ["11", "Specialized Agent Architecture & Dynamic Agent Synthesis", "NCIE-007-S01 §3-5; NCIE-005 Ch.4"],
        ["12", "Agent Capability Registry & Agent Factory", "NCIE-007-S01 §1, §7-8"],
        ["13", "Task Decomposition & Delegation", "NCIE-002 Ch.4"],
        ["14", "Delegated Authorization & Identity Propagation", "NCIE-006 Ch.25 §25.3"],
        ["15", "Multi-Agent Coordination & Conflict Handling", "NCIE-002 Ch.4"],
        ["16", "Agent State, Checkpointing & Resumption", "NCIE-006 Ch.20"],
        ["17", "Context Acquisition & Memory-Service Integration", "NCIE-006 Ch.14, Ch.17"],
        ["18", "Evidence & Grounding Integration", "NCIE-003 Ch.17"],
        ["19", "Tool Gateway Integration", "NCIE-002 Ch.4"],
        ["20", "Read-Only vs State-Changing Tool Classes", "NCIE-003 Ch.4"],
        ["21", "Human Approval, Confirmation & Execution Boundary", "NCIE-002 Ch.4"],
        ["22", "Agent-to-Agent Tool Delegation", "NCIE-007-S01 §8"],
        ["23", "Planning, Reflection & Iterative Analytical Loops", "NCIE-006 Ch.11 §11.2"],
        ["24", "Prompt, Instruction & Policy Assembly", "NCIE-002 Ch.4"],
        ["25", "Prompt Injection & Untrusted-Content Containment", "NCIE-002 Ch.4"],
        ["26", "Output Schemas, Validation & the VPF Validation Framework", "NCIE-007 Skeletal v0.2 — MANDATORY VPF ADDITION"],
        ["27", "AI Provenance, Attribution & Execution Receipts", "NCIE-005 Ch.27"],
        ["28", "Safety Guardrails & Policy Enforcement", "NCIE-002 Ch.4"],
        ["29", "Resource Budgets, Cost, Rate Limits & Quotas", "NCIE-004 Ch.31"],
        ["30", "Concurrency, Idempotency & Duplicate Suppression", "NCIE-002 Ch.4"],
        ["31", "Observability, Telemetry & AI Operations", "NCIE-006 Ch.31 §31.3"],
        ["32", "Evaluation, Regression & Adversarial Testing", "NCIE-003 Ch.38"],
        ["33", "Model & Agent Lifecycle Governance", "NCIE-007-S01 §5"],
        ["34", "Security, Isolation & Supply-Chain Boundaries", "NCIE-007-S01 §6"],
        ["35", "Human Review Register & Open Decisions", "Consolidates Ch.1-34"],
        ["36", "Traceability, Acceptance & Handover", "Closes NCIE-001→...→NCIE-006→NCIE-007 authority chain"],
    ],
     "NCIE-007 chapter-to-upstream traceability matrix."),
    ("h2", "36.2 Traceability Mechanical Verification"),
    ("p",
     "Per handover items 1307/1371, every one of the 36 chapters above carries at least one upstream "
     "citation, verified programmatically at build time (not merely by inspection of §36.1) against "
     "every chapter's own ('upstream', ...) block; a build with any chapter missing one fails before "
     "reaching this document. No ORPHAN NCIE-007 REQUIREMENT was found in this edition."),
    ("h2", "36.3 Upstream Impact Register"),
    ("p",
     "NCIE-001–006 remain approved and are not amended during this production cycle (front matter "
     "§0.1). The following impacts are recorded for the surgical amendment pass that NCIE-007 "
     "approval shall initiate:"),
    ("table",
     ["Impact ID", "Affected Document", "Required Surgical Amendment", "Severity", "Blocking Scope", "Amendment Status"],
     [
        ["UIR-001", "NCIE-001", "Recognize bounded Dynamic Agent Synthesis and VPF-validated AI output as explicit NCIE capabilities.", "Material", "Does not block NCIE-007 approval", "DEFERRED UNTIL NCIE-007 APPROVAL"],
        ["UIR-002", "NCIE-002", "Add Dynamic Agent Factory/synthesis boundary, ephemeral-vs-registered lifecycle, and VPF validation gates without changing Human-Primary authority.", "Material", "Does not block NCIE-007 approval", "DEFERRED UNTIL NCIE-007 APPROVAL"],
        ["UIR-003", "NCIE-003", "Add/extend Agent Definition, Agent Instance, VPF Validation Result, Promotion Candidate and agent lifecycle/provenance data semantics.", "Material", "Does not block NCIE-007 approval", "DEFERRED UNTIL NCIE-007 APPROVAL"],
        ["UIR-004", "NCIE-004", "Add sandboxed Agent Factory/runtime, agent-definition artifact controls, evaluation pipeline, signing/integrity and VPF integration as governed technology capabilities.", "Material", "Does not block NCIE-007 approval", "DEFERRED UNTIL NCIE-007 APPROVAL"],
        ["UIR-005", "NCIE-005", "Allow ARGUS to initiate bounded agent synthesis when needed; confirm ARGUS still cannot grant authority, self-register an agent, or bypass human approval.", "Material", "Does not block NCIE-007 approval", "DEFERRED UNTIL NCIE-007 APPROVAL"],
        ["UIR-006", "NCIE-006", "Confirm synthesized agents consume governed minimum-necessary Context/Memory and receive no unrestricted Memory or inherited ARGUS-wide context.", "Material", "Does not block NCIE-007 approval", "DEFERRED UNTIL NCIE-007 APPROVAL"],
    ],
     "VPF & Dynamic Agent Upstream Impact Register — controlled for post-NCIE-007 surgical incorporation; this is a documentation-governance action, not an amendment performed now."),
    ("h2", "36.4 Downstream Handover Register"),
    ("table",
     ["Downstream Document", "NCIE-007 Obligation to Implement"],
     [
        ["NCIE-008 (Governance & Human Authority)", "Institutional acceptance authority for NCIE-007 chapters and for VPF/Dynamic Agent governance decisions (Ch.1 §1.3, Ch.35)."],
        ["NCIE-009 (Security/IAM)", "Sandbox isolation, current-authorization enforcement, and Agent Factory/Model/Tool Gateway security implementation (Ch.34 references, never duplicates, this obligation)."],
        ["NCIE-010 (Evidence, Provenance & Audit)", "Physical audit/provenance store implementing the logical fields specified in Ch.27, Ch.26 §26.9."],
        ["NCIE-011 (API/Integration)", "Wire-protocol implementation of the Model Gateway, Tool Gateway and VPF service contracts specified logically in Ch.5, Ch.19, Ch.26."],
        ["NCIE-012 (UX)", "User-facing presentation of VPF dispositions, agent status and human approval checkpoints specified logically in Ch.21, Ch.26 §26.2."],
        ["NCIE-014 (Database & Storage Engineering)", "Physical storage for the Model/Agent/Tool/VPF Profile/Agent Pattern Registries and VPF artifact persistence specified logically in Ch.6, Ch.12 §12.2, Ch.26 §26.9."],
        ["NCIE-015 (Deployment/Infrastructure)", "Physical sandbox/runtime infrastructure and network/egress enforcement specified logically in Ch.34."],
        ["NCIE-016 (Testing)", "Full implementation of the Mandatory Acceptance Test Matrix specified in Ch.32 §32.2."],
    ],
     "Downstream Handover Register — NCIE-007 specifies logical requirements; it does not pre-design these downstream implementations (front matter §0.2)."),
    ("h2", "36.5 Acceptance Checklist"),
    ("bullets", [
        "All 19 Governing Invariants (front matter §0.3) are preserved without exception across all 36 chapters.",
        "VPF is fully integrated: every substantive AI-generated output enters the VPF governance path (Gate B) before validated release, with profile rigor — never exemption — varying by risk/output class; no chapter implies Model Output can be directly validated by ARGUS, or that registered/ephemeral agents are exempt from VPF by default.",
        "Dynamic Agent Synthesis is fully integrated: ARGUS can create bounded task-specific agents from approved primitives without Codex hand-coding each one, while agent synthesis cannot create new institutional authority, infrastructure or unapproved capability.",
        "NCIE-007-S01 is fully crosswalked: every normative S01 requirement is incorporated, retained or explicitly superseded with rationale (§36.6).",
        "The Human Review Register (Ch.35) is mechanically reconciled (§35.4); the Upstream Impact Register (§36.3) and Downstream Handover Register (§36.4) are complete.",
        "Required diagrams, matrices, state models and logical contracts are present (Dynamic Agent Synthesis Flow Ch.11 §11.2, Ephemeral Agent Lifecycle Ch.11 §11.7, ARGUS Orchestration Request Lifecycle Ch.4 §4.2, VPF Normal Path Ch.26 §26.1, AI Runtime Actor Taxonomy Ch.3 §3.1, Prompt/Instruction Trust Hierarchy Ch.24 §24.1).",
        "Acceptance-test coverage (Ch.32 §32.2) addresses VPF, Dynamic Agent Synthesis, sovereignty, fail-closed, change-management and the mandatory Human-Primary final scenario.",
        "No chapter fully specifies NCIE-008/009/010/011/012/014/015/016; each cross-references the downstream owner (§36.4).",
        "No technology named from NCIE-004 is asserted as more approved here than its NCIE-004 Technology Registry status.",
    ]),
    ("h2", "36.6 S01 Disposition"),
    ("p",
     "Every normative NCIE-007-S01 requirement is incorporated into this document (Ch.11-12, Ch.22, "
     "Ch.27 §27.2, Ch.33-34) with no silent loss. Proposed disposition: NCIE-007-S01 — FULLY "
     "INCORPORATED; CANDIDATE FOR SUPERSESSION UPON HUMAN APPROVAL OF NCIE-007. Final supersession is "
     "not decided here; it requires human approval."),
    ("h2", "36.7 Readiness Statements"),
    ("table",
     ["Capability", "Status"],
     [
        ["VPF", "ARCHITECTURALLY SPECIFIED — IMPLEMENTATION-READY SUBJECT TO OPEN DECISIONS (Ch.35). Not yet operational merely because the specification exists."],
        ["Dynamic Agent Synthesis", "ARCHITECTURE SPECIFIED. Agent Factory implementation and Dynamic Agent production activation are separate, later milestones."],
        ["Codex/engineering pre-conditions", "Agent Factory, Agent Definition Schema, Runtime Policy Enforcement, Sandbox/Evaluation, Agent Registry Integration, Model Gateway Integration, Tool Gateway Integration, VPF Gate A/B, Provenance, Observability, Expiry and Kill/Suspend Controls must be implemented and operationally approved before ARGUS exercises Dynamic Agent Synthesis operationally."],
     ],
     "Readiness statements — architecture completeness is distinct from operational activation."),
    ("h2", "36.8 Capability and Limitation Statement"),
    ("p",
     "Once the Ch.36 §36.7 pre-conditions are implemented and approved: ARGUS MAY SYNTHESIZE AND USE "
     "BOUNDED TASK-SPECIFIC AI AGENTS FROM APPROVED NCIE PRIMITIVES WITHOUT REQUIRING CODEX TO "
     "HAND-CODE EACH INDIVIDUAL AGENT. Simultaneously: ARGUS MAY NOT USE DYNAMIC AGENT SYNTHESIS TO "
     "CREATE NEW INSTITUTIONAL AUTHORITY, BYPASS GOVERNED CONTROLS, SELF-REGISTER AGENTS, MODIFY VPF, "
     "OR CREATE INFRASTRUCTURE CAPABILITIES THAT DO NOT EXIST WITHIN THE APPROVED SYNTHESIS ENVELOPE. "
     "CODEX / ENGINEERING RE-ENTERS WHEN THE REQUIRED CAPABILITY EXCEEDS THE APPROVED AGENT FACTORY "
     "PRIMITIVES OR REQUIRES MATERIAL PRODUCTION ENGINEERING CHANGE. Both the capability and the "
     "limitation are true simultaneously (Ch.12 §12.1)."),
    ("h2", "36.9 Final Disposition"),
    ("p",
     "NCIE-007 v1.0 is architecturally complete across all 36 chapters. This is distinct from all "
     "implementation decisions being resolved: Chapter 35 records genuine open decisions, none of "
     "which is presented as already resolved. Claude does not recommend approval merely because the "
     "document is complete; this document presents sufficient evidence for human review, and formal "
     "approval remains with the authorized human governance process (NCIE-008)."),
    ("review", [
        ("INSTITUTIONAL", "Confirm the boundary with NCIE-008 (Governance & Human Authority) and NCIE-009 (Security/IAM) for the specific acceptance items in §36.5."),
    ]),
    ("trace", "Closes the NCIE-001 → NCIE-002 → NCIE-003 → NCIE-004 → NCIE-005 → NCIE-006 → NCIE-007 authority chain (front matter §0.1)."),
]
