"""NCIE-007 content batch: Chapters 25-30 (prompt injection containment,
Output Schemas/Validation/VPF Validation Framework, AI provenance/attribution,
safety guardrails, resource budgets, concurrency/idempotency)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 25 — Prompt Injection & Untrusted-Content Containment
# ---------------------------------------------------------------------------
BLOCKS[25] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Retrieved content ≠ trusted instruction is architecturally fixed; this chapter specifies containment testing."),
    ]),
    ("h2", "25.1 Malicious-Instruction Surfaces"),
    ("p",
     "Malicious instructions may originate from Evidence, Documents, Memory, Institutional Knowledge "
     "Candidates, Web/API Content, Tool Results or another Agent. Every such surface is explicitly "
     "tested; none is assumed safe merely because it passed prior validation for a different purpose. "
     "None may override the higher-authority policy levels in Ch.24 §24.1."),
    ("h2", "25.2 Containment Discipline"),
    ("p",
     "Content from any of §25.1's surfaces is treated as data throughout assembly (Ch.24), execution "
     "(Ch.19-21) and validation (Ch.26). An instruction-shaped string appearing inside retrieved "
     "content never gains the authority of a Task/Agent Policy or Current Authorized User Intent "
     "element."),
    ("trace", "NCIE-002 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 26 — Output Schemas, Validation & the VPF Validation Framework
# ---------------------------------------------------------------------------
BLOCKS[26] = [
    ("upstream", [
        ("NCIE-007", "Skeletal v0.2", "VPF is a mandatory controlled addition approved for inclusion before full expansion; this chapter is its substantive architecture."),
    ]),
    ("vpf",
     "ALL SUBSTANTIVE AI-GENERATED OUTPUT SHALL ENTER THE VPF GOVERNANCE PATH BEFORE RELEASE AS A "
     "VALIDATED NCIE AI RESULT OR PERSISTENCE AS A GOVERNED AI-GENERATED ANALYTICAL ARTIFACT. The "
     "governed VPF profile may vary by output class and risk — including a lightweight deterministic "
     "profile for low-risk, mechanical AI output — but no substantive AI output is exempt from VPF by "
     "default (§26.5). Purely deterministic, non-AI processing that involves no model/agent inference "
     "remains outside this AI-output VPF mandate. No agent type — registered, ephemeral, or ARGUS's "
     "own direct model use — receives an implicit exemption."),
    ("h2", "26.1 Normal Path"),
    ("flow",
     ["Model / Agent generates output", "Schema Validation", "VPF", "Disposition", "ARGUS / Persistence / Downstream Use"],
     "VPF Normal Path — every substantive AI output traverses schema validation and VPF before validated release."),
    ("h2", "26.2 VPF Dispositions"),
    ("table",
     ["Disposition", "Meaning"],
     [
        ["PASS", "The AI result satisfied the applicable validation framework — not that NCA has institutionally approved the conclusion."],
        ["QUALIFIED", "The result is releasable with an explicit qualification (Evidence Incomplete, Material Contradiction, Historical Context Only, Current-State Verification Unavailable, Methodological Limitation). Never rendered visually or verbally as equivalent to PASS."],
        ["REJECT", "The result shall not be presented as a validated NCIE AI result. Provenance/audit of the rejected run is retained where policy requires; the system does not silently regenerate until something passes without preserving the failed attempts where consequential."],
        ["HUMAN_REVIEW_REQUIRED", "ARGUS may present the output only in the explicitly governed review context appropriate to that state — never as validated institutional guidance."],
        ["VALIDATION_UNAVAILABLE", "A mandatory validator did not run, timed out, failed technically, or was ineligible. A PASS never occurs on this basis."],
     ],
     "VPF disposition semantics — consistent across every chapter; no chapter redefines them independently."),
    ("h2", "26.3 VPF Validation Dimensions"),
    ("p", "Applicable VPF validation dimensions include, where relevant:"),
    ("bullets", [
        "Evidence grounding; Source/provenance integrity.",
        "Epistemic classification; Contradiction handling; Assumption exposure.",
        "Methodological validity; Claim-boundary compliance.",
        "Temporal validity; Authorization; Classification; Policy compliance.",
        "Human-Primary boundary; Output-schema integrity.",
    ]),
    ("p",
     "No single universal numerical VPF score is manufactured across these dimensions — a PASS/"
     "QUALIFIED/REJECT/HUMAN_REVIEW_REQUIRED disposition is explainable along the specific dimensions "
     "that produced it."),
    ("h2", "26.4 Two Gates"),
    ("p",
     "VPF GATE A validates the dynamically synthesized Agent Envelope before execution (Ch.11 §11.5). "
     "VPF GATE B validates substantive AI output after execution and before validated release. "
     "Neither gate substitutes for current human/institutional authorization where required (Ch.21). "
     "The two gates are never collapsed."),
    ("h2", "26.5 Validation Profiles"),
    ("p",
     "Different AI tasks require different validation profiles — for example Question Answer, "
     "Hypothesis, Contradiction, Evidence-Gap Analysis, Cross-Domain Analysis, Briefing, "
     "Recommendation, Tool Proposal and Dynamic-Agent Output. Every profile has a defined Purpose, "
     "Applicable Scope, Version and Lifecycle State, identifies its mandatory validation dimensions, "
     "and cannot silently weaken global mandatory controls — a weaker profile never bypasses "
     "mandatory authority/security controls."),
    ("p",
     "SUBSTANTIVE AI OUTPUT ≠ VPF-EXEMPT BY DEFAULT (front matter §0.3). A low-risk, mechanical AI "
     "output (for example a routine reformatting or extraction task with negligible epistemic or "
     "authority consequence) may be governed by a lightweight, largely deterministic VPF profile with "
     "correspondingly narrow mandatory dimensions — it is never routed around VPF altogether merely "
     "for latency or usability. Purely deterministic, non-AI processing that involves no model/agent "
     "inference is outside the AI-output VPF mandate entirely, since it is not AI-generated output "
     "(§26 vpf callout)."),
    ("h2", "26.6 Validator Kinds"),
    ("p",
     "The architecture distinguishes Deterministic Validators from AI-Assisted Validators. AI is not "
     "used for controls that are authoritatively determinable through structured policy/state where "
     "deterministic validation is sufficient."),
    ("h2", "26.7 VPF Does Not Become Institutional Authority"),
    ("p",
     "VPF validates AI output. VPF does not approve regulatory Decisions, create Findings, authorize "
     "blocking, authorize tracking, approve Institutional Knowledge, or replace human judgment. VPF "
     "VALIDATION ≠ HUMAN / INSTITUTIONAL APPROVAL — this is a foundational NCIE-007 principle "
     "restated, never contradicted, in any chapter."),
    ("h2", "26.8 Human Modification After Validation"),
    ("p",
     "If a human materially modifies an AI result after VPF validation, the modified artifact does "
     "not automatically inherit the original VPF status. Policy determines whether the modification "
     "requires Revalidation or a Human-Origin/Human-Modified designation; both AI and human "
     "provenance are preserved regardless."),
    ("h2", "26.9 VPF Provenance"),
    ("p", "Persist for every consequential VPF validation:"),
    ("bullets", [
        "VPF Validation ID; Validation Profile; Input Artifact Reference.",
        "Applicable Framework/Policy Version; Validation Time.",
        "Disposition; Qualification/Failure Reasons.",
        "Human Review Outcome, where applicable.",
    ]),
    ("review", [
        ("INSTITUTIONAL", "Approve the VPF validation dispositions, mandatory dimensions and release behavior for PASS, QUALIFIED, REJECT and HUMAN_REVIEW_REQUIRED."),
        ("PROPOSED", "The disposition set in §26.2 (PASS/QUALIFIED/REJECT/HUMAN_REVIEW_REQUIRED/VALIDATION_UNAVAILABLE) is proposed as complete for launch."),
    ]),
    ("trace", "NCIE-007 Skeletal v0.2 — MANDATORY VPF ADDITION, Chapter 26."),
]

# ---------------------------------------------------------------------------
# Chapter 27 — AI Provenance, Attribution & Execution Receipts
# ---------------------------------------------------------------------------
BLOCKS[27] = [
    ("upstream", [
        ("NCIE-005", "Ch.27", "Human/ARGUS/workflow attribution is canonical; this chapter extends it to models, agents and VPF."),
    ]),
    ("h2", "27.1 End-to-End Attribution"),
    ("p",
     "Every consequential output/action preserves attribution across Run ID, Actor (Ch.3), Model "
     "Route, Agent, Context References, Tool Calls, Output, Human Response and Timestamps. Audit "
     "identifies exactly which actor performed each operation (Ch.3 §3.1)."),
    ("h2", "27.2 Dynamic-Agent Provenance"),
    ("p", "For every synthesized agent run, preserve at least:"),
    ("bullets", [
        "Agent Definition ID/version; Synthesis Origin; ARGUS Request.",
        "VPF Gate A Result; Sandbox/Evaluation Result.",
        "Runtime Identity; Model Route; Context References; Tool Calls.",
        "VPF Gate B Result; Output.",
        "Expiry State; Promotion State.",
    ]),
    ("h2", "27.3 Artifact Integrity"),
    ("p",
     "Agent Definition Packages support integrity controls such as Hash, Signature, Version and "
     "Immutable Run Reference where appropriate. An agent definition does not change silently between "
     "validation and execution."),
    ("trace", "NCIE-005 Ch.27."),
]

# ---------------------------------------------------------------------------
# Chapter 28 — Safety Guardrails & Policy Enforcement
# ---------------------------------------------------------------------------
BLOCKS[28] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "AI safety and service-boundary requirements are architecturally fixed; this chapter specifies technical enforcement beyond prompt instructions."),
    ]),
    ("h2", "28.1 Enforcement Beyond Prompt Instructions"),
    ("p",
     "Safety policy is enforced technically — through the Model Gateway, Tool Gateway, VPF and Agent "
     "Factory controls — never relying solely on prompt-level instruction to models or agents, which "
     "retrieved content can attempt to override (Ch.25)."),
    ("trace", "NCIE-002 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 29 — Resource Budgets, Cost, Rate Limits & Quotas
# ---------------------------------------------------------------------------
BLOCKS[29] = [
    ("upstream", [
        ("NCIE-004", "Ch.31", "Performance/tiering targets are engineering-governed; this chapter specifies orchestration-level resource bounding."),
    ]),
    ("h2", "29.1 Bounded Resources"),
    ("p", "Every model/agent invocation, including every synthesized agent, requires bounded:"),
    ("bullets", [
        "Runtime; Tokens; Model Calls; Tool Calls.",
        "Concurrency; Memory/Context Volume.",
        "Compute/GPU, where relevant.",
    ]),
    ("p", "Runaway agent loops terminate safely rather than running unbounded."),
    ("h2", "29.2 Cancellation"),
    ("p",
     "Humans and governed orchestration can cancel active agent runs where appropriate. Cancellation "
     "does not leave consequential tool operations in an ambiguous state; reconciliation (Ch.30 §30.2) "
     "applies when an external outcome is unknown."),
    ("trace", "NCIE-004 Ch.31."),
]

# ---------------------------------------------------------------------------
# Chapter 30 — Concurrency, Idempotency & Duplicate Suppression
# ---------------------------------------------------------------------------
BLOCKS[30] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Zero-trust concurrency handling is architecturally fixed; this chapter specifies idempotency and unknown-outcome handling."),
    ]),
    ("h2", "30.1 Duplicate Suppression"),
    ("p",
     "Idempotency and correlation apply to Agent Runs, Tool Calls, Action Requests and VPF Validation "
     "Requests wherever retries are possible."),
    ("h2", "30.2 Unknown Execution Outcome"),
    ("p",
     "UNKNOWN OUTCOME ≠ FAILURE and UNKNOWN OUTCOME ≠ SUCCESS (front matter §0.3). A consequential "
     "operation with an unknown external outcome is never blindly retried; it triggers reconciliation "
     "instead. TIMEOUT ≠ FAILURE and TIMEOUT ≠ SUCCESS follow the same rule."),
    ("h2", "30.3 Stale Agent Results"),
    ("p",
     "If authoritative context changes materially while an agent executes, its result may require "
     "STALE_CONTEXT, REVALIDATION_REQUIRED or HUMAN_REVIEW_REQUIRED. Newer authoritative state is "
     "never overwritten by stale agent output."),
    ("trace", "NCIE-002 Ch.4."),
]
