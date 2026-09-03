"""NCIE-004 content batch: Chapters 31-32 (performance/capacity engineering,
integration adapters/RPA/legacy engineering)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 31 — Performance, Capacity, Scalability & Load Engineering
# ---------------------------------------------------------------------------
BLOCKS[31] = [
    ("upstream", [
        ("NCIE-002", "Ch.30", "Reference NFR targets (latency, concurrent users, national cell scale) are proposed baselines this stack must be capacity-planned against."),
    ]),
    ("h2", "31.1 Performance and Capacity Engineering"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Status"],
     [
        ["Capacity planning", "Sized against NCIE-002 Ch.30 §30.2's reference targets (≥500 concurrent users, national cell scale)", "Load-test-driven sizing per service tier, revisited each major release", "PROPOSED"],
        ["Horizontal scaling", "That stateless services scale out is mandated (Ch.4, NCIE-002 Ch.30); the specific autoscaling metric (request rate/queue depth) is an engineering choice", "Orchestrator autoscaling policies keyed to request rate/queue depth", "PROPOSED"],
        ["Concurrency controls", "Prevents a single tenant/workload from starving others (NCIE-002 Ch.30 §30.3)", "Per-tenant rate limiting at the API gateway (Ch.8)", "PROPOSED"],
        ["Backpressure/request shedding", "Graceful degradation under load rather than uncontrolled failure (NCIE-002 Ch.30 §30.7)", "Gateway-level shedding with visible degraded-status signal (Ch.26)", "MANDATE"],
    ],
     "Performance, capacity and load-engineering technology decisions.", 3),
    ("review", [
        "Confirm production-scale targets (concurrent users, national cell count, data volumes) with NCA capacity-planning stakeholders (already open at NCIE-002 Ch.30 §30-review).",
    ]),
    ("trace", "NCIE-002 Ch.30."),
]

# ---------------------------------------------------------------------------
# Chapter 32 — Integration Adapters, RPA & Legacy-System Engineering
# ---------------------------------------------------------------------------
BLOCKS[32] = [
    ("upstream", [
        ("NCIE-002", "Ch.21", "Capability Registry abstracts UiPath/Power Automate/Automation Anywhere and future providers behind one contract; provider neutrality is mandatory."),
        ("NCIE-003", "Ch.34", "Legacy import passes through the same validation as any source; original identifiers and transformations are retained, never discarded."),
    ]),
    ("h2", "32.1 Integration and Legacy Engineering"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Connector framework", "Provider-neutral adapter contract (NCIE-002 Ch.21 §21.2 Capability Registry)", "Internal adapter interface with one implementation per provider", "—", "MANDATE"],
        ["File/SFTP ingestion", "Scheduled/triggered acquisition for sources without an API (NCIE-003 Ch.6)", "SFTP poller feeding the Ch.6 ingestion gateway", "—", "PROPOSED"],
        ["RPA", "Provider-neutral, behind the Capability Registry; no ARGUS/workflow code depends on one RPA vendor's SDK", "UiPath, Power Automate or Automation Anywhere per NCA's existing licensing — selected as a Provider Adapter, not a platform dependency", "—", "INSTITUTIONAL"],
        ["Anti-corruption layer", "Legacy/external system quirks isolated from canonical semantics (NCIE-003 Ch.34)", "Adapter-local translation layer; canonical services never see legacy field shapes directly", "—", "MANDATE"],
        ["Retries", "Idempotent retry with backoff on transient failure (NCIE-003 Ch.6 §6.6 deduplication)", "Adapter-level retry policy with idempotency key", "—", "PROPOSED"],
        ["Reconciliation", "Unknown external outcome reconciled, not blindly retried (NCIE-003 Ch.23 §23.2)", "Shared reconciliation mechanism with Ch.10's workflow engine", "—", "MANDATE"],
    ],
     "Integration adapters, RPA and legacy-system engineering decisions.", 4),
    ("review", [
        "Confirm which RPA provider(s) NCA already licenses before approving one as the primary Provider Adapter.",
        "Confirm which external systems require RPA versus direct API integration (already open at NCIE-003 Ch.23 §23-review).",
    ]),
    ("trace", "NCIE-002 Ch.21; NCIE-003 Ch.6, Ch.23, Ch.34."),
]
