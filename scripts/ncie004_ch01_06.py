"""NCIE-004 content batch: Chapters 1-6 (mandate, standards, runtime/hosting,
containerization, backend stack, frontend stack)."""

BLOCKS = {}
M = "MANDATE"
P = "PROPOSED"
I = "INSTITUTIONAL"
IN = "INFRASTRUCTURE"
S = "SECURITY"

# ---------------------------------------------------------------------------
# Chapter 1 — Engineering Mandate, Authority Chain & Technology Selection Doctrine
# ---------------------------------------------------------------------------
BLOCKS[1] = [
    ("upstream", [
        ("NCIE-002", "Ch.1 §1.3", "Human-Primary authority, provider neutrality, evidence/provenance-first bind every technology choice below."),
        ("NCIE-003", "Ch.1-2", "Canonical semantics, temporal integrity and classification are engineering constraints, not optional features."),
    ]),
    ("h2", "1.1 Selection Doctrine"),
    ("bullets", [
        "A technology is selected to implement an upstream requirement, never to justify one retroactively.",
        "Vendor/product selection is justified by security, sovereignty, resilience, maintainability and lifecycle — convenience alone is never sufficient.",
        "Every technology decision carries one of the five statuses in front matter §0.3; none is asserted as settled fact unless it is an Approved Upstream Mandate.",
        "This document distinguishes capability (what is needed) from candidate product (a proposed way to meet it) throughout — see Chapter 35 for the consolidated record.",
    ]),
    ("h2", "1.2 Structural Change Control"),
    ("p",
     "The 36-chapter structure is locked. A material contradiction or omission discovered during "
     "expansion is flagged inline as STRUCTURAL CHANGE REQUIRED — HUMAN REVIEW rather than silently "
     "resolved by adding, merging or renumbering a chapter. No such flag has been raised in this "
     "edition."),
    ("h2", "1.3 Boundary with NCIE-005 Through NCIE-016"),
    ("p",
     "NCIE-004 establishes the technology baseline and engineering constraints for ARGUS (→ NCIE-005), "
     "memory (→ NCIE-006), AI/agent orchestration (→ NCIE-007), security architecture (→ NCIE-009), "
     "API/integration (→ NCIE-011), UX/UI (→ NCIE-012), database/storage engineering (→ NCIE-014), "
     "DevSecOps/infrastructure (→ NCIE-015) and testing (→ NCIE-016). It does not write those "
     "documents' implementation detail; it fixes the technology families and patterns they must build "
     "within."),
    ("review", [
        "Confirm the acceptance authority for NCIE-004 as a whole and for individual chapter/technology sign-off.",
    ]),
    ("trace", "NCIE-002 Ch.1; NCIE-003 Ch.1-2."),
]

# ---------------------------------------------------------------------------
# Chapter 2 — Engineering Principles, Standards & Reference Conventions
# ---------------------------------------------------------------------------
BLOCKS[2] = [
    ("upstream", [
        ("NCIE-003", "Ch.2", "Naming, null/unknown semantics, temporal and classification rules bind every service's code and schema, not only the data model."),
    ]),
    ("h2", "2.1 Engineering Conventions"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Status"],
     [
        ["Code style & linting", "Deterministic, automatically enforced, language-appropriate", "Per-language formatter/linter (e.g. Black/Ruff for Python, ESLint/Prettier for TypeScript), enforced in CI (Ch.28)", "PROPOSED"],
        ["API/error conventions", "Consistent error shape, idempotency keys and correlation IDs on every call, per NCIE-003 Ch.33", "Problem-details-style JSON error envelope; mandatory correlation ID header", "PROPOSED"],
        ["Null/unknown representation", "Must distinguish Unknown/Partial/Stale/Unavailable, never collapse to a default (NCIE-003 Ch.2 §2.5 mandates the vocabulary; the code-level mechanism does not)", "Typed nullable/optional fields plus an explicit status enum", "PROPOSED"],
        ["Versioning", "Additive-first; breaking change requires major version + deprecation window", "Semantic versioning across services and schemas", "PROPOSED"],
     ],
     "Engineering conventions applied across all NCIE-004 technology families.", 3),
    ("h2", "2.2 Documentation and Traceability Convention"),
    ("p",
     "Every service/component references the Decision ID (Ch.35) that selected its technology and "
     "the NCIE-002/003 chapter it implements, in its own README/architecture-decision-record — this "
     "keeps traceability alive in code, not only in this document."),
    ("review", [
        "Confirm whether NCA already mandates a specific coding-standard/linting toolchain to adopt instead of §2.1's proposed defaults.",
    ]),
    ("trace", "NCIE-003 Ch.2, Ch.30 (dictionary/metadata conventions)."),
]

# ---------------------------------------------------------------------------
# Chapter 3 — Target Runtime, Hosting & Environment Strategy
# ---------------------------------------------------------------------------
BLOCKS[3] = [
    ("upstream", [
        ("NCIE-002", "Ch.1 §1.6", "Sovereign, on-premises-capable hosting is the proposed default posture; no core operation requires data to leave Ghanaian jurisdiction."),
        ("NCIE-003", "Ch.32, Ch.36", "Hosting constraints gate storage-technology selection and sovereignty controls."),
    ]),
    ("h2", "3.1 Hosting and Environment Model"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Status"],
     [
        ["Hosting model", "Sovereign, NCA-controlled, capable of on-premises or approved sovereign-cloud operation", "NCA data centre or approved sovereign cloud within Ghana", "SECURITY"],
        ["Environment tiers", "Development / Test / Staging / Production, isolated, masked non-production data (NCIE-003 Ch.29 §29.3)", "Four-tier environment model, one per NCIE-002 Ch.29", "MANDATE"],
        ["Trust zones", "Network segmentation across ingestion/application/data/AI/integration boundaries is mandated (NCIE-002 Ch.26 §26.7); the specific zone taxonomy is an NCIE-004 engineering choice", "The 7-zone model in §34.2 (edge/API, application, data, AI, integration, security-observability, management)", "PROPOSED"],
        ["Capacity baseline", "Sized to NCIE-002 Ch.30's proposed targets (500+ concurrent users, national cell/topology scale)", "Sized once real infrastructure and volumes are confirmed", "INFRASTRUCTURE"],
    ],
     "Hosting, environment and trust-zone decisions.", 3),
    ("h2", "3.2 Failure and Recovery"),
    ("p",
     "Loss of a single environment tier or trust zone must not corrupt another (NCIE-002 Ch.28). "
     "Recovery targets are inherited from NCIE-002 Ch.28 §28.9's proposed RTO/RPO tiers pending NCA "
     "confirmation (Ch.30 of this document details the resilience engineering)."),
    ("review", [
        "Confirm the specific hosting facility/sovereign-cloud provider and whether NCA already operates environment tiers this platform must integrate with.",
        "Confirm capacity/volume assumptions before infrastructure sizing (feeds Ch.31).",
    ]),
    ("trace", "NCIE-002 Ch.1 §1.6, Ch.26, Ch.28, Ch.30; NCIE-003 Ch.32, Ch.35-36."),
]

# ---------------------------------------------------------------------------
# Chapter 4 — Containerization, Orchestration & Workload Scheduling
# ---------------------------------------------------------------------------
BLOCKS[4] = [
    ("upstream", [
        ("NCIE-002", "Ch.29 §29.3", "Performance/scalability targets require horizontal, autoscaling service deployment rather than fixed monoliths."),
    ]),
    ("h2", "4.1 Containerization and Orchestration"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Container runtime", "OCI-compliant, widely supported", "containerd (via Docker build tooling)", "CRI-O", "PROPOSED"],
        ["Orchestrator", "Declarative scheduling, autoscaling, rolling deploys, secrets integration (Ch.24)", "Kubernetes", "OpenShift (if NCA already standardises on it)", "PROPOSED"],
        ["Ingress/networking", "TLS termination, trust-zone-aware routing (Ch.3), rate limiting", "NGINX/Envoy-based ingress controller", "—", "PROPOSED"],
        ["Autoscaling", "Horizontal pod/service autoscaling on load and queue depth (Ch.9)", "Kubernetes HPA + custom metrics", "—", "PROPOSED"],
        ["Stateful/GPU scheduling", "Isolated scheduling for databases and AI model workloads (Ch.11-18)", "Dedicated node pools with taints/tolerations; GPU device plugin where ARGUS requires local inference", "—", "INFRASTRUCTURE"],
    ],
     "Containerization and orchestration technology decisions.", 4),
    ("h2", "4.2 Security and Failure"),
    ("bullets", [
        "Workload identity per NCIE-002 Ch.4 §4.2 machine-identity model; no shared cluster-admin credentials for application workloads.",
        "Node/cluster failure: orchestrator reschedules; stateful workloads rely on Ch.30's HA/replication, not container restart alone.",
        "Monitored via Ch.26 observability stack (cluster and workload-level metrics).",
    ]),
    ("review", [
        "Confirm whether NCA already operates a container platform (Kubernetes distribution, OpenShift or other) that must be reused rather than newly stood up.",
        "Confirm GPU availability/capacity for any locally hosted ARGUS model (Ch.18).",
    ]),
    ("trace", "NCIE-002 Ch.4 §4.2, Ch.29, Ch.30."),
]

# ---------------------------------------------------------------------------
# Chapter 5 — Backend Application & Service Engineering Stack
# ---------------------------------------------------------------------------
BLOCKS[5] = [
    ("upstream", [
        ("NCIE-002", "Ch.5-Ch.25", "Every domain and platform service (Network, Revenue, Rules, Evidence, etc.) needs one consistent backend runtime family."),
    ]),
    ("h2", "5.1 Backend Runtime and Service Framework"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Primary backend runtime", "Strong typing, mature async I/O, long-term support, maintainable by a growing NCA team", "Python (type-checked) for domain/AI-adjacent services", "TypeScript/Node.js (if frontend-adjacent team unification is preferred)", "INSTITUTIONAL"],
        ["API framework", "OpenAPI-first, dependency injection, async request handling", "FastAPI (Python)", "NestJS (TypeScript)", "PROPOSED"],
        ["Background workers", "Reliable queue consumption, retries, idempotency (NCIE-003 Ch.23)", "Framework-native worker process consuming the Ch.9 event broker", "—", "PROPOSED"],
        ["Dependency/build tooling", "Reproducible builds, lockfiles, SBOM-capable (Ch.28)", "Poetry/pip-tools (Python) or pnpm (Node.js)", "—", "PROPOSED"],
        ["Service template", "Standard scaffold with logging, health checks, auth middleware pre-wired", "Internal service template repository", "—", "PROPOSED"],
    ],
     "Backend application and service engineering decisions.", 4),
    ("h2", "5.2 Engineering Notes"),
    ("bullets", [
        "Every service exposes a health/readiness endpoint feeding Ch.26 observability.",
        "Service-to-service calls carry correlation IDs and enforce authorization per NCIE-002 Ch.4 at the boundary, not only at the API gateway (Ch.8).",
        "A service failing its readiness check is removed from the load-balancing pool by the orchestrator (Ch.4), never left serving degraded traffic silently.",
    ]),
    ("review", [
        "Confirm primary engineering language/runtime based on NCA's actual institutional engineering capability and long-term support commitments.",
    ]),
    ("trace", "NCIE-002 Ch.4, Ch.5, Ch.25."),
]

# ---------------------------------------------------------------------------
# Chapter 6 — Frontend Web Application Stack
# ---------------------------------------------------------------------------
BLOCKS[6] = [
    ("upstream", [
        ("NCIE-002", "Ch.3", "The Situational Awareness Workspace, ARGUS presentation and Collaborative Rooms all render in one consistent web stack."),
    ]),
    ("h2", "6.1 Frontend Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Web framework", "Component-based, large ecosystem, SSR/CSR flexibility for dashboards and workspaces", "React", "Vue", "PROPOSED"],
        ["Type system", "Compile-time safety across a large, multi-team codebase", "TypeScript", "—", "PROPOSED"],
        ["State/data layer", "Server-state caching, optimistic updates for collaborative rooms (Ch.21)", "React Query / equivalent data-fetching layer", "Redux Toolkit (for complex local state)", "PROPOSED"],
        ["Routing", "Role-aware, deep-linkable views matching NCIE-002 Ch.3 panel model", "Framework-native router", "—", "PROPOSED"],
        ["Build/accessibility tooling", "WCAG 2.1 AA per NCIE-002 Ch.30 §30.4", "Vite build; automated accessibility linting/testing in CI (Ch.28-29)", "—", "PROPOSED"],
    ],
     "Frontend web application stack decisions.", 4),
    ("h2", "6.2 Engineering Notes"),
    ("bullets", [
        "Panel/workspace composition (NCIE-002 Ch.3) is implemented as independently loadable modules so a degraded panel never blocks the rest of the shell from rendering.",
        "Colour is never the only status signal, per NCIE-002 Ch.30 §30.4 — enforced via an accessibility lint rule, not convention alone.",
        "ARGUS presentation states (Docked/Expanded/Full-Screen/in-Room, NCIE-002 Ch.3 §3.9) are layout variants of one component, not separate applications.",
    ]),
    ("review", [
        "Confirm whether NCA has an existing design-system/frontend standard (e.g. from the NMS Dashboard) that should be reused rather than introducing a new one.",
    ]),
    ("trace", "NCIE-002 Ch.3, Ch.30 §30.4."),
]
