"""NCIE-004 content batch: Chapters 25-30 (data protection/DLP, observability,
SecOps/SIEM, DevSecOps/CI-CD, testing, resilience/DR)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 25 — Data Protection, DLP, Masking & Protected Reveal
# ---------------------------------------------------------------------------
BLOCKS[25] = [
    ("upstream", [
        ("NCIE-003", "Ch.36 §36.3-36.4", "Ghana Card/Passport identifiers and precise Anti-Fraud location require masking/tokenization, never plaintext exposure in logs, search, vector indexes or uncontrolled exports."),
    ]),
    ("h2", "25.1 Data Protection Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Tokenization", "Reversible-only-under-authorization substitution for Ghana Card/Passport values is mandated (NCIE-003 Ch.14 §14.6); which tokenization service implements it is not", "Vault Transit tokenization (Ch.24) or a dedicated tokenization service", "—", "PROPOSED"],
        ["Masking", "Default-masked display for protected fields outside authorized Protected Reveal, enforced non-bypassably (server-side, never client-side only)", "Server-side masking applied before response serialization, never client-side only", "—", "MANDATE"],
        ["Field encryption", "Encryption for protected columns is mandated (Ch.11, Ch.24); the specific envelope-encryption/KMS-key mechanism is an implementation choice", "Application-layer field encryption using KMS-issued keys", "—", "PROPOSED"],
        ["DLP", "Blocks bulk export of protected identity information (NCIE-003 Ch.36 §36.3)", "DLP policy on export/API-response paths flagging bulk protected-field extraction", "—", "SECURITY"],
        ["Protected reveal", "Every unmask is an audited action (NCIE-003 Ch.36 §36.5)", "Protected-reveal endpoint requiring explicit authorization check + audit event (Ch.27)", "—", "MANDATE"],
        ["Export controls", "Anti-Fraud location/evidence exports individually authorized and logged", "Export gateway enforcing classification + Ch.27 audit on every export", "—", "MANDATE"],
    ],
     "Data protection, DLP and masking technology decisions.", 4),
    ("h2", "25.2 Prohibited Exposure Surfaces"),
    ("bullets", [
        "Raw Ghana Card/Passport values never appear in application logs, general search indexes, general vector indexes, ARGUS prompts (beyond the minimum authorized reference), telemetry, or uncontrolled exports — enforced by the masking/tokenization layer sitting ahead of every one of those surfaces, not by developer discipline alone.",
        "Anti-Fraud location data is never treated as ordinary GIS data (Ch.7); it inherits sensitive-tier isolation, authorization and ARGUS context-minimization (Ch.18 §18.3) automatically via its classification tag.",
    ]),
    ("review", [
        "Confirm field-level protection scope (which roles may invoke Protected Reveal) with NCA Legal/Data Protection (already open at NCIE-003 Ch.14 §14-review, Ch.31-review).",
    ]),
    ("trace", "NCIE-002 Ch.26; NCIE-003 Ch.14, Ch.31, Ch.36."),
]

# ---------------------------------------------------------------------------
# Chapter 26 — Observability, Telemetry & Operational Monitoring Stack
# ---------------------------------------------------------------------------
BLOCKS[26] = [
    ("upstream", [
        ("NCIE-002", "Ch.27", "Platform, automation, source and sector health must remain distinct, individually visible signals."),
        ("NCIE-003", "Ch.37", "Pipeline health is not sector health; source update time and processing time must remain distinct."),
    ]),
    ("h2", "26.1 Observability Semantics"),
    ("p", "Five signal categories are kept separate throughout this stack and never collapsed into one "
         "dashboard colour: Platform Health, Data Pipeline Health, Sector/Network Condition, ARGUS "
         "Quality, and Security Condition. A green infrastructure dashboard must never imply that "
         "Ghana's telecommunications environment is itself healthy."),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Logs", "Structured, correlation-ID-tagged, classification-aware logging (no protected values in plaintext) is mandated; JSON format and log-store choice are not", "Structured JSON logging shipped to a central log store", "—", "PROPOSED"],
        ["Metrics", "Per-service and per-signal-category metrics (§26.1's five categories)", "Prometheus-compatible metrics", "—", "PROPOSED"],
        ["Traces", "Correlated distributed tracing across service/event boundaries (Ch.8-9)", "OpenTelemetry instrumentation", "—", "PROPOSED"],
        ["APM/dashboards", "Distinct dashboards per signal category (§26.1), never one merged view", "Grafana dashboards, one board family per category", "—", "PROPOSED"],
        ["Alerting", "Routes to the correct owner per signal category (platform vs sector vs security)", "Alertmanager routing rules keyed to signal category and severity", "—", "PROPOSED"],
        ["SLOs", "Per NCIE-002 Ch.30's proposed performance targets", "SLO burn-rate alerting on the reference targets", "—", "PROPOSED"],
    ],
     "Observability and telemetry technology decisions.", 4),
    ("rel",
     [
        ("Services/Workloads (Ch.4-24)", "emit logs/metrics/traces to", "OpenTelemetry Collector"),
        ("Collector", "routes to", "Metrics Store / Log Store / Trace Store"),
        ("Metrics/Log/Trace Stores", "feed", "Dashboards (one family per signal category)"),
        ("Dashboards", "trigger", "Alerting (routed by signal category to the correct owner)"),
     ],
     "Observability topology: five signal categories routed to distinct dashboards and owners."),
    ("review", [
        "Confirm operational owners and escalation paths per signal category (already open at NCIE-003 Ch.37 §37-review).",
    ]),
    ("trace", "NCIE-002 Ch.27; NCIE-003 Ch.29, Ch.37."),
]

# ---------------------------------------------------------------------------
# Chapter 27 — Security Operations, SIEM & Threat Detection Integration
# ---------------------------------------------------------------------------
BLOCKS[27] = [
    ("upstream", [
        ("NCIE-003", "Ch.27", "Every read/reveal/export/approve/execute action on sensitive data is an Audit Event; unknown outcome is a valid, first-class audit state."),
    ]),
    ("h2", "27.1 Security Operations Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["SIEM", "Ingests audit events (Ch.11), guardrail events (Ch.19) and infrastructure logs (Ch.26)", "Wazuh (open) or NCA-existing SIEM", "Commercial SIEM if NCA already operates one", "INSTITUTIONAL"],
        ["SOAR", "Automated response playbooks for common security events", "SIEM-integrated SOAR module where the chosen SIEM supports it", "—", "PROPOSED"],
        ["WAF/IDS/IPS", "Perimeter protection at trust-zone boundaries (Ch.3, Ch.23)", "WAF at the API gateway (Ch.8); network IDS/IPS at zone boundaries", "—", "PROPOSED"],
        ["EDR integration", "Endpoint detection on hosts/nodes underlying the orchestrator (Ch.4)", "EDR agent feeding SIEM", "—", "INFRASTRUCTURE"],
        ["Security-event pipeline", "Fail-closed on high-consequence action audit failure is mandated verbatim (NCIE-003 Ch.27 §27.5); routing security events via Ch.9's broker specifically is this document's proposed mechanism", "Same event broker (Ch.9) carrying a dedicated security-event topic into the SIEM", "—", "PROPOSED"],
    ],
     "Security operations and SIEM integration decisions.", 4),
    ("review", [
        "Confirm whether NCA operates an existing SOC/SIEM this platform must integrate with rather than stand up independently.",
    ]),
    ("trace", "NCIE-002 Ch.26; NCIE-003 Ch.27."),
]

# ---------------------------------------------------------------------------
# Chapter 28 — DevSecOps, Source Control & CI/CD Engineering Toolchain
# ---------------------------------------------------------------------------
BLOCKS[28] = [
    ("upstream", [
        ("NCIE-002", "Ch.29", "Environment separation, versioned deployments, and secrets excluded from code/CI logs are architectural mandates."),
    ]),
    ("h2", "28.1 DevSecOps Toolchain"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Source control", "Branch/review policy enforced, no direct pushes to protected branches", "Git (GitLab/GitHub, self-hosted or NCA-approved)", "—", "INSTITUTIONAL"],
        ["CI/CD", "Automated build/test/deploy with mandatory gate checks (NCIE-002 Ch.29 §29.4)", "GitLab CI or GitHub Actions, self-hosted runners in the sovereign environment (Ch.3)", "—", "PROPOSED"],
        ["Artifact/container registry", "Immutable, versioned build artifacts (NCIE-002 Ch.29 §29.2)", "Self-hosted registry (e.g. Harbor) inside the sovereign environment", "—", "PROPOSED"],
        ["SAST/SCA/secret scanning", "Blocking a release with a critical vulnerability or leaked secret is the mandated gate; the named scanning tools are candidate products, not upstream mandates", "Integrated scanners in the CI pipeline (e.g. Semgrep, Trivy, gitleaks)", "—", "PROPOSED"],
        ["IaC", "Reproducible, reviewed infrastructure definitions", "Terraform / Kubernetes manifests under source control", "—", "PROPOSED"],
        ["Policy-as-code", "Enforces this document's mandates (e.g. no unencrypted protected-tier store) at deploy time", "OPA/Conftest policy gates in CI", "—", "PROPOSED"],
        ["SBOM", "Software bill of materials for supply-chain accountability where appropriate", "Generated per release build (e.g. Syft)", "—", "PROPOSED"],
    ],
     "DevSecOps and CI/CD engineering toolchain decisions.", 4),
    ("h2", "28.2 Engineering Notes"),
    ("bullets", [
        "A failed mandatory gate (SAST/SCA/secret-scan/policy) blocks promotion; no manual override without a recorded exception (NCIE-002 Ch.29 §29.7).",
        "Rollback to the immediately prior artifact version is a tested, supported operation, not emergency improvisation (NCIE-002 Ch.29 §29.4).",
    ]),
    ("review", [
        "Confirm whether NCA mandates a specific source-control/CI platform already in institutional use.",
    ]),
    ("trace", "NCIE-002 Ch.29."),
]

# ---------------------------------------------------------------------------
# Chapter 29 — Testing, Quality Engineering & Test Automation Stack
# ---------------------------------------------------------------------------
BLOCKS[29] = [
    ("upstream", [
        ("NCIE-002", "Ch.31", "Test layers span functional, integration, security, AI/collaborative evaluation, automation, resilience and cross-domain/multi-user scenarios."),
        ("NCIE-003", "Ch.38", "Data testing requires dedicated temporal, lineage and authorization/privacy test categories, not schema tests alone."),
    ]),
    ("h2", "29.1 Test Automation Stack"),
    ("p",
     "This chapter defines the engineering toolchain and technical test capability only; the "
     "comprehensive verification programme (acceptance authorities, sign-off matrices, full RTM) is "
     "NCIE-016's scope, not reproduced here."),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Unit/integration", "Fast, deterministic, run on every commit", "Language-native test frameworks (pytest/Jest) in CI (Ch.28)", "—", "PROPOSED"],
        ["Contract testing", "API/event schema compatibility (Ch.8-9) verified pre-merge", "Consumer-driven contract tests (e.g. Pact) or schema-diff gate", "—", "PROPOSED"],
        ["End-to-end/UI automation", "Critical workspace/collaborative-room flows (Ch.6, Ch.21)", "Playwright", "—", "PROPOSED"],
        ["Performance testing", "Load/capacity validation against Ch.31 targets", "k6 or similar load-testing tool in a staging environment", "—", "PROPOSED"],
        ["Security testing", "SAST/SCA (Ch.28) plus scheduled DAST/pen-testing", "DAST tool integrated pre-release; periodic external pen-test", "—", "PROPOSED"],
        ["Data testing", "Temporal/lineage/authorization test categories (NCIE-003 Ch.38 §38.4)", "Test harness asserting bitemporal correctness and field-level authorization per entity family", "—", "MANDATE"],
        ["Workflow/resilience testing", "Durable-workflow recovery (Ch.10) and failover drills (Ch.30)", "Chaos/failure-injection testing in staging", "—", "PROPOSED"],
        ["AI evaluation", "Model/provider evaluation before production use (Ch.18-19)", "Offline evaluation harness gating Model Registry promotion (Ch.33)", "—", "MANDATE"],
    ],
     "Testing and quality-engineering technology decisions.", 4),
    ("review", [
        "Confirm required test environments and masked test data provisioning (already open at NCIE-003 Ch.38 §38-review).",
    ]),
    ("trace", "NCIE-002 Ch.31; NCIE-003 Ch.38."),
]

# ---------------------------------------------------------------------------
# Chapter 30 — Resilience, Backup, Disaster Recovery & Business Continuity Technology
# ---------------------------------------------------------------------------
BLOCKS[30] = [
    ("upstream", [
        ("NCIE-002", "Ch.28", "Loss of any single external dependency (AI, RPA, map, source) must degrade only the affected capability, never core NCIE."),
        ("NCIE-003", "Ch.5, Ch.25", "Backup/DR must preserve bitemporal history and provenance, not merely current-state snapshots."),
    ]),
    ("h2", "30.1 Resilience and DR Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["HA/replication", "Per-tier HA matching Ch.11's database replication and Ch.4's orchestrator rescheduling", "Multi-replica deployment per service tier", "—", "PROPOSED"],
        ["Backup", "Canonical data, rules, audit, memory, schedules and workflows all covered (NCIE-002 Ch.28 §28.4)", "Automated scheduled backups per store (Ch.11-17)", "—", "MANDATE"],
        ["PITR", "Point-in-time recovery capability matching RPO targets is mandated; WAL archiving is a PostgreSQL-specific mechanism, not itself an upstream mandate", "Continuous WAL archiving (Ch.11) + object-store versioning (Ch.13)", "—", "PROPOSED"],
        ["Cross-site DR", "Secondary site/capability for platform-level failure", "Warm-standby DR site within Ghanaian jurisdiction (Ch.3 sovereignty posture)", "—", "INFRASTRUCTURE"],
        ["Failover", "Automated or documented manual failover per critical service tier", "Orchestrator-driven failover (Ch.4) + database failover (Ch.11)", "—", "PROPOSED"],
        ["Restore testing", "Recovery is rehearsed, not assumed (NCIE-002 Ch.29 §29.9)", "Scheduled DR/restore drills with recorded results", "—", "MANDATE"],
    ],
     "Resilience, backup and disaster-recovery technology decisions.", 4),
    ("h2", "30.2 RTO/RPO by Tier"),
    ("p",
     "Inherits NCIE-002 Ch.28 §28.9's proposed defaults: Tier 1 (identity, canonical data, evidence/"
     "audit) RTO 4h/RPO 15min; Tier 2 (domain services, automation) RTO 8h/RPO 1h; Tier 3 (AI/"
     "collaborative features) RTO 24h/RPO 4h — pending NCA business-continuity confirmation."),
    ("review", [
        "Confirm DR site location and RTO/RPO targets against NCA business-continuity requirements (already open at NCIE-002 Ch.28 §28-review).",
    ]),
    ("trace", "NCIE-002 Ch.28, Ch.29 §29.9; NCIE-003 Ch.5, Ch.25."),
]
