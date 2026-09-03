"""NCIE-007 content batch: Chapters 19-24 (Tool Gateway integration, tool risk
classes, human approval/execution boundary, agent-to-agent tool delegation,
planning/iterative loops, prompt/instruction/policy assembly)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 19 — Tool Gateway Integration
# ---------------------------------------------------------------------------
BLOCKS[19] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "The Tool Gateway is the single governed entry boundary for consequential tool access; this chapter specifies its contract."),
    ]),
    ("h2", "19.1 Tool Gateway Mandate"),
    ("p",
     "All agent tool use goes through the governed Tool Gateway. No synthesized or registered agent "
     "receives direct unrestricted Database, Operating System, Network, Blocking Interface, Tracking "
     "Interface or External System access. TOOL ACCESS ≠ ACTION AUTHORITY (front matter §0.3) — "
     "possessing a tool binding never itself authorizes a consequential action (Ch.21)."),
    ("h2", "19.2 Gateway Contract"),
    ("table",
     ["Element", "Purpose"],
     [
        ["Tool Registry", "Eligible tools and their declared risk class (Ch.20)."],
        ["Authorization Check", "Current authorization of the requesting actor (Ch.14) for this specific tool/target."],
        ["Target Validation", "Confirms the exact target/action matches what was authorized — never a broader match."],
        ["Idempotency", "Correlation key preventing duplicate execution under retry (Ch.30)."],
        ["Execution Receipt", "Verifiable confirmation of outcome, or an explicit OUTCOME UNKNOWN state (Ch.30 §30.2)."],
     ],
     "Tool Gateway request/response contract."),
    ("trace", "NCIE-002 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 20 — Read-Only vs State-Changing Tool Classes
# ---------------------------------------------------------------------------
BLOCKS[20] = [
    ("upstream", [
        ("NCIE-003", "Ch.4", "Disclosure-risk classification is canonical; this chapter applies it to tool risk classification."),
    ]),
    ("h2", "20.1 Read-Only Does Not Mean Harmless"),
    ("p",
     "Search, Reveal, Export, Graph Traversal, Protected Identity Retrieval and Precise Location "
     "Retrieval are treated as potentially consequential even though they do not mutate state. Tool "
     "risk classification reflects disclosure risk, not only mutation risk."),
    ("h2", "20.2 Tool Risk Classes"),
    ("table",
     ["Class", "Examples", "Governs"],
     [
        ["Read-Only, Low Disclosure Risk", "Non-sensitive metadata lookup", "Standard authorization check"],
        ["Read-Only, High Disclosure Risk", "Protected Identity Retrieval, Precise Location, Restricted Graph Traversal, Reveal/Export", "Elevated authorization + disclosure-purpose check (NCIE-006 Ch.25 §25.3 pattern)"],
        ["State-Changing, Reversible", "Draft creation, non-consequential updates", "Standard authorization + idempotency (Ch.30)"],
        ["State-Changing, Consequential", "Blocking Interface, Tracking Interface, external regulatory action", "Current human/institutional approval required before execution (Ch.21)"],
     ],
     "Tool risk classification — disclosure risk and mutation risk are assessed independently."),
    ("trace", "NCIE-003 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 21 — Human Approval, Confirmation & Execution Boundary
# ---------------------------------------------------------------------------
BLOCKS[21] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Human-Primary governance over consequential execution is architecturally fixed; this chapter specifies the approval sequence."),
    ]),
    ("h2", "21.1 Consequential-Action Sequence"),
    ("p",
     "PROPOSED ≠ AUTHORIZED ≠ APPROVED ≠ EXECUTED ≠ VERIFIED (front matter §0.3). An agent may "
     "prepare or recommend an action. Current institutional authority — never Model Eligibility, "
     "Agent Registration, VPF Gate A/B PASS, Agent Consensus, Tool Availability, Prior Decision, "
     "Institutional Knowledge or Human Presence alone — determines whether execution may proceed "
     "(Ch.36 §36.7 final audit)."),
    ("h2", "21.2 Execution Boundary Table"),
    ("table",
     ["Stage", "Meaning"],
     [
        ["Proposed", "An agent/model has generated a candidate action; no authority attaches."],
        ["Authorized", "Current governed authorization exists for this specific action/target."],
        ["Approved", "The accountable current human/institutional process has approved execution."],
        ["Executed", "The Tool Gateway has performed the action and returned a receipt."],
        ["Verified", "The outcome has been reconciled against the intended result (Ch.30 §30.2)."],
     ],
     "Consequential-action stage sequence — no stage is skipped for a consequential action."),
    ("trace", "NCIE-002 Ch.4."),
]

# ---------------------------------------------------------------------------
# Chapter 22 — Agent-to-Agent Tool Delegation
# ---------------------------------------------------------------------------
BLOCKS[22] = [
    ("upstream", [
        ("NCIE-007-S01", "§8", "Recursive synthesis is disabled by default; this chapter applies the same non-escalation discipline to agent-to-agent tool delegation."),
    ]),
    ("h2", "22.1 Delegation Without Escalation"),
    ("p",
     "Synthesized agents do not possess Agent Factory authority by default and do not recursively "
     "synthesize agents (Ch.12 §12.3). Where agent-to-agent tool delegation is permitted at all, it "
     "remains independently authorized at the final Tool Gateway invocation — an intermediate agent's "
     "claimed permission is never trusted in place of that final check."),
    ("h2", "22.2 Delegation Record"),
    ("p", "If permitted, every agent-to-agent delegation preserves:"),
    ("bullets", [
        "Parent Task; Purpose; Effective Principal.",
        "Classification; Context Subset.",
        "Tool Ceiling; Resource Ceiling.",
        "Provenance.",
    ]),
    ("p", "Delegation cannot create transitive privilege expansion (Ch.14 §14.3)."),
    ("review", [
        ("INSTITUTIONAL", "Confirm whether agent-to-agent tool delegation is permitted in the initial release, and if so its maximum delegation depth."),
    ]),
    ("trace", "NCIE-007-S01 §8."),
]

# ---------------------------------------------------------------------------
# Chapter 23 — Planning, Reflection & Iterative Analytical Loops
# ---------------------------------------------------------------------------
BLOCKS[23] = [
    ("upstream", [
        ("NCIE-006", "Ch.11 §11.2", "Decision-Time / private chain-of-thought boundaries are canonical; this chapter bounds planning loops accordingly."),
    ]),
    ("h2", "23.1 Bounded Planning"),
    ("p",
     "Bounded planning/revision loops are permitted where useful, governed by an Iteration Budget, "
     "Time Budget, Token Budget, Tool Budget, Termination Conditions and Escalation Conditions (Ch.29 "
     "budgets apply identically here)."),
    ("h2", "23.2 Persisted vs Private Artifacts"),
    ("p", "Private chain-of-thought is never persisted. Defensible artifacts persisted instead include:"),
    ("bullets", [
        "Plan State; Questions; Hypotheses.",
        "Contradictions; Evidence Gaps.",
        "Tool Results; Final Output.",
    ]),
    ("trace", "NCIE-006 Ch.11 §11.2."),
]

# ---------------------------------------------------------------------------
# Chapter 24 — Prompt, Instruction & Policy Assembly
# ---------------------------------------------------------------------------
BLOCKS[24] = [
    ("upstream", [
        ("NCIE-002", "Ch.4", "Retrieved content ≠ trusted instruction is architecturally fixed; this chapter specifies the assembly hierarchy that enforces it."),
    ]),
    ("h2", "24.1 Trust Hierarchy"),
    ("flow",
     ["Governed NCIE Policy", "Task/Agent Policy", "Current Authorized User Intent", "Governed Context", "Retrieved Evidence/Data", "Tool Output"],
     "Prompt/Instruction Trust Hierarchy — retrieved content is data; it never gains instruction authority by appearing in a prompt."),
    ("h2", "24.2 Assembly Discipline"),
    ("p",
     "Prompt/policy assembly follows the hierarchy in §24.1 strictly. A lower-trust element (Retrieved "
     "Evidence/Data, Tool Output) is never assembled in a way that lets it override a higher-trust "
     "element (Governed NCIE Policy, Task/Agent Policy, Current Authorized User Intent)."),
    ("trace", "NCIE-002 Ch.4."),
]
