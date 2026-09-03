"""NCIE-004 content batch: Chapters 7-12 (design/visualization/GIS, API gateway,
event streaming, workflow engine, transactional DB, analytical platform)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 7 — Design System, Visualization & Geospatial Technology
# ---------------------------------------------------------------------------
BLOCKS[7] = [
    ("upstream", [
        ("NCIE-002", "Ch.3, Ch.8", "The Situational Awareness Workspace's map-centrality and dashboard composition require a consistent visualization/GIS layer."),
        ("NCIE-003", "Ch.8", "Coordinate reference system, spatial precision and sensitive-layer classification are canonical, not a rendering choice."),
    ]),
    ("h2", "7.1 Visualization and Geospatial Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Design system/components", "Consistent, accessible (WCAG 2.1 AA), shared across dashboards/workspaces/rooms", "Internal component library on a headless UI kit (e.g. Radix)", "Existing NCA design system, if any", "PROPOSED"],
        ["Charting", "Time-series, KPI and status visualizations matching NCIE-003 Ch.2 §2.5 quality states", "Recharts/Observable Plot", "—", "PROPOSED"],
        ["GIS/map engine", "Layered, permission-filtered rendering per NCIE-002 Ch.8 §8.6", "MapLibre GL (open, avoids per-seat licensing)", "Commercial GIS SDK if NCA already licenses one", "INSTITUTIONAL"],
        ["Spatial services", "Coordinate transforms, geocoding matching NCIE-003 Ch.8's canonical CRS", "PostGIS extension on the transactional store (Ch.11)", "—", "PROPOSED"],
        ["Dashboard/export rendering", "Reproducible PDF/image export of workspace views for reporting", "Server-side headless rendering", "—", "PROPOSED"],
    ],
     "Design system, visualization and geospatial technology decisions.", 4),
    ("h2", "7.2 Engineering Notes"),
    ("bullets", [
        "Sensitive map layers (Anti-Fraud location, NCIE-003 Ch.15) are permission-filtered server-side before reaching the client, never hidden by client-side CSS alone.",
        "Map engine failure degrades to a non-map geography selector (NCIE-002 Ch.3 §3.6); the frontend must ship that fallback view, not merely assume map availability.",
    ]),
    ("review", [
        "Confirm whether NCA already licenses a commercial GIS/mapping SDK that should be reused instead of an open alternative.",
    ]),
    ("trace", "NCIE-002 Ch.3, Ch.8, Ch.30 §30.4; NCIE-003 Ch.8."),
]

# ---------------------------------------------------------------------------
# Chapter 8 — API Gateway & Service Communication Stack
# ---------------------------------------------------------------------------
BLOCKS[8] = [
    ("upstream", [
        ("NCIE-002", "Ch.25", "Governed APIs, schema versioning and authorization-at-every-boundary are architectural mandates, not implementation options."),
        ("NCIE-003", "Ch.33", "API/event contracts must carry knowledge time, lineage and classification, never strip them."),
    ]),
    ("h2", "8.1 API and Service Communication Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Synchronous API protocol", "OpenAPI-documented, broadly consumable by frontend/partners (NCIE-002 Ch.25 mandates governed, documented APIs; it does not mandate a specific protocol)", "REST/HTTP+JSON", "—", "PROPOSED"],
        ["Internal high-throughput calls", "Low-latency service-to-service where REST overhead matters (e.g. ARGUS tool calls)", "gRPC where justified by measured latency need", "—", "PROPOSED"],
        ["API gateway", "AuthN/AuthZ enforcement, rate limiting, request correlation, per NCIE-002 Ch.4/Ch.25", "Kong / Envoy-based gateway", "Cloud-native API Gateway if hosting model requires it", "PROPOSED"],
        ["Schema tooling", "Contract-first, breaking-change detection (NCIE-003 Ch.33 §33.4)", "OpenAPI + schema-diff CI gate (Ch.28-29)", "—", "PROPOSED"],
        ["Idempotency enforcement", "Idempotency-key on every side-effecting call, mandated verbatim (NCIE-003 Ch.33 §33.5)", "Idempotency-key middleware in every service", "—", "MANDATE"],
        ["Rate limiting", "Prevents a single tenant/workload from starving others (NCIE-002 Ch.30 §30.3); mechanism/placement not itself mandated", "Gateway-level rate limiting", "—", "PROPOSED"],
    ],
     "API gateway and service communication technology decisions.", 4),
    ("h2", "8.2 Engineering Notes"),
    ("bullets", [
        "Every call carries a correlation ID; the gateway rejects a request without one at the edge rather than let it propagate uncorrelated.",
        "Authorization is enforced at each service boundary, not solely at the gateway, per NCIE-002 Ch.4's zero-trust principle.",
        "Gateway outage degrades to direct service health-check-based routing rather than a total outage where the orchestrator (Ch.4) permits.",
    ]),
    ("review", [
        "Confirm whether NCA's existing enterprise integration standards mandate a specific API gateway product.",
    ]),
    ("trace", "NCIE-002 Ch.4, Ch.25; NCIE-003 Ch.33."),
]

# ---------------------------------------------------------------------------
# Chapter 9 — Event Streaming, Messaging & Asynchronous Processing
# ---------------------------------------------------------------------------
BLOCKS[9] = [
    ("upstream", [
        ("NCIE-002", "Ch.25 §25.3-25.4", "Source/PM/Alert/Workflow/Collaborative events must be idempotent, correlated and versioned."),
        ("NCIE-003", "Ch.28", "Event envelopes must carry correlation IDs and reference sensitive payloads rather than embed them."),
    ]),
    ("h2", "9.1 Event Streaming and Messaging Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Event broker", "Durable, partitioned, replayable, supports the event categories in NCIE-002 Ch.25 §25.3", "Apache Kafka (or Redpanda for lighter ops)", "RabbitMQ (if throughput/replay needs are modest)", "PROPOSED"],
        ["Queues", "At-least-once delivery, dead-letter handling for workflow/automation events (NCIE-003 Ch.23)", "Broker-native topics/queues", "—", "PROPOSED"],
        ["Schema registry", "Versioned event schemas per NCIE-003 Ch.33", "Confluent/Karapace-style schema registry", "—", "PROPOSED"],
        ["Dead-letter queue & replay", "Failed events retained and replayable, never silently dropped, mandated verbatim (NCIE-002 Ch.25 §25.7); the DLQ/replay mechanism itself is an implementation choice", "Broker-native DLQ + replay tooling", "—", "PROPOSED"],
        ["Outbox/inbox pattern", "Exactly-once effect despite at-least-once delivery (idempotent consumption, NCIE-003 Ch.23 §23.6)", "Transactional outbox on the publishing service's own database (Ch.11)", "—", "PROPOSED"],
    ],
     "Event streaming and asynchronous processing technology decisions.", 4),
    ("rel",
     [
        ("Domain Service (publisher)", "writes Outbox row + business change in one transaction, then", "Outbox Relay"),
        ("Outbox Relay", "publishes to", "Event Broker (partitioned, schema-versioned)"),
        ("Event Broker", "delivers to", "Consumer Service (idempotent, correlation-ID checked)"),
        ("Consumer Service", "on failure routes to", "Dead-Letter Queue (replayable)"),
        ("Workflow Instance (Ch.10)", "raises/consumes events via", "Event Broker"),
     ],
     "Event/workflow topology: publish-outbox-broker-consume-DLQ pattern feeding the workflow engine."),
    ("review", [
        "Confirm expected event throughput/retention before final broker sizing (feeds Ch.31)."]),
    ("trace", "NCIE-002 Ch.25; NCIE-003 Ch.23, Ch.28."),
]

# ---------------------------------------------------------------------------
# Chapter 10 — Workflow, BPM & Long-Running Process Engine
# ---------------------------------------------------------------------------
BLOCKS[10] = [
    ("upstream", [
        ("NCIE-002", "Ch.21", "Request/Run state machine, WAITING_FOR_PM-style persistent waits and human-task approvals must survive restarts."),
        ("NCIE-003", "Ch.23", "Requested/Approved/Executed/Verified/Reconciling states are canonical entities the engine must expose, not internal engine state alone."),
    ]),
    ("h2", "10.1 Workflow Engine"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Workflow/orchestration engine", "Durable execution surviving process/node restart, human-task support", "Temporal", "Camunda (BPMN-native, if NCA prefers visual process modelling)", "PROPOSED"],
        ["State machine / BPMN", "Explicit states matching NCIE-003 Ch.23 §23.2's four-state separation", "Engine-native workflow definitions mapped 1:1 to canonical Workflow States", "—", "MANDATE"],
        ["Timers & waiting dependencies", "Persistent WAITING_FOR_PM/WAITING_FOR_TRAFFIC-style waits (NCIE-002 Ch.21 §21.4)", "Engine-native durable timers/signals", "—", "PROPOSED"],
        ["Human tasks & approvals", "Distinct approving actor from requester (separation of duties, NCIE-003 Ch.26)", "Engine human-task API integrated with Ch.23 IAM roles", "—", "MANDATE"],
        ["Reconciliation", "Unknown outcome triggers reconciliation, never blind retry (NCIE-003 Ch.23 §23.2)", "Engine-native compensation/reconciliation workflow", "—", "PROPOSED"],
    ],
     "Workflow/BPM engine technology decisions.", 4),
    ("h2", "10.2 Engineering Notes"),
    ("bullets", [
        "Room-originated workflows (NCIE-002 Ch.20 §20.11) retain room/thread provenance as workflow metadata, not a side-channel record.",
        "Engine outage: in-flight workflows resume from persisted state on recovery (Ch.30); no workflow is lost to a process restart.",
    ]),
    ("review", [
        "Confirm which workflows are high-consequence and require mandatory dual approval before automated execution (populates Ch.35 Decision Matrix constraints).",
    ]),
    ("trace", "NCIE-002 Ch.21; NCIE-003 Ch.23."),
]

# ---------------------------------------------------------------------------
# Chapter 11 — Transactional Database Technology
# ---------------------------------------------------------------------------
BLOCKS[11] = [
    ("upstream", [
        ("NCIE-002", "Ch.5", "Canonical/validated layers require ACID transactional storage; optimisation must never redefine canonical meaning."),
        ("NCIE-003", "Ch.5, Ch.24, Ch.32", "Bitemporal storage, effective-dated Rules and the logical-to-physical map bind schema design here."),
    ]),
    ("h2", "11.1 Transactional Database"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Relational DBMS", "ACID, mature bitemporal/window-function support, row-level security", "PostgreSQL", "—", "PROPOSED"],
        ["HA/replication", "Synchronous replica for failover per Ch.30 RTO/RPO targets", "Streaming replication + automated failover (e.g. Patroni)", "Managed HA offering if hosting model (Ch.3) permits", "PROPOSED"],
        ["Migrations", "Versioned, reversible, reviewed schema changes (NCIE-003 Ch.1 §1.4 change control)", "Alembic/Flyway-style migration tooling in CI (Ch.28)", "—", "PROPOSED"],
        ["Backup / PITR", "Point-in-time recovery capability matching Ch.30 RPO is mandated; the specific WAL-based mechanism is PostgreSQL-oriented, not itself an upstream mandate", "Continuous WAL archiving + scheduled base backups", "—", "PROPOSED"],
        ["Row/column security", "Protected-identity field isolation is mandated (NCIE-003 Ch.14 §14.6, Ch.26); RLS + column encryption is one implementation of it, not the only one", "Row-level security policies + column encryption (Ch.24-25)", "—", "PROPOSED"],
    ],
     "Transactional database technology decisions.", 4),
    ("h2", "11.2 Engineering Notes"),
    ("bullets", [
        "Bitemporal entities (NCIE-003 Ch.5 §5.5) use append-only versioned tables; no UPDATE ever destroys a prior version's row.",
        "Rule Versions (NCIE-003 Ch.24) live here as the authoritative store — never duplicated as literals elsewhere in the stack.",
        "Failure: automated failover to replica; application layer retries idempotently against the new primary (Ch.5 §5.2).",
    ]),
    ("review", [
        "Confirm whether NCA mandates a specific relational database platform already in institutional use.",
    ]),
    ("trace", "NCIE-002 Ch.5; NCIE-003 Ch.5, Ch.24, Ch.32."),
]

# ---------------------------------------------------------------------------
# Chapter 12 — Analytical, Time-Series & Historical Data Platform
# ---------------------------------------------------------------------------
BLOCKS[12] = [
    ("upstream", [
        ("NCIE-002", "Ch.30", "National-scale PM/Traffic/Revenue volumes require partitioned, query-efficient analytical storage distinct from transactional storage."),
        ("NCIE-003", "Ch.32 §32.5, Ch.35", "Analytical stores are derived, never independently canonical; discrepancy from canonical source is a data-quality issue, not a competing truth."),
    ]),
    ("h2", "12.1 Analytical and Historical Platform"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["OLAP/time-series engine", "High-volume PM/Traffic observation storage and query (NCIE-003 Ch.7, Ch.11)", "TimescaleDB (PostgreSQL extension, minimises polyglot footprint)", "ClickHouse (if query volume later demands a dedicated columnar engine)", "PROPOSED"],
        ["Warehouse/lakehouse", "Cross-domain historical analytics and reporting", "Deferred until analytical query volume justifies a separate warehouse", "—", "INFRASTRUCTURE"],
        ["Partitioning", "Cross-period traceability across partitions is mandated (NCIE-003 Ch.35 §35.5); the specific partition key/scheme is an engineering choice", "Native partitioning by period + operator", "—", "PROPOSED"],
        ["Materialized views", "Derived views must be rebuildable and never independently canonical, mandated verbatim (Ch.32 §32.5); the refresh mechanism itself is an implementation choice", "Scheduled materialized-view refresh", "—", "PROPOSED"],
        ["Historical query", "Decision-time reconstruction support (NCIE-003 Ch.25)", "Bitemporal query layer over Ch.11's canonical tables plus this analytical layer", "—", "PROPOSED"],
    ],
     "Analytical, time-series and historical data platform decisions.", 4),
    ("h2", "12.2 Engineering Notes"),
    ("bullets", [
        "This layer is always rebuildable from Ch.11's canonical store; it is never the system of record for a fact.",
        "A materialized view found out of sync with canonical source triggers a Remediation Task (NCIE-003 Ch.29), not silent trust until next refresh.",
    ]),
    ("review", [
        "Confirm expected historical data volumes and query patterns before committing to a dedicated warehouse/lakehouse (currently deferred as Infrastructure Discovery Required).",
    ]),
    ("trace", "NCIE-002 Ch.30; NCIE-003 Ch.7, Ch.11, Ch.32, Ch.35."),
]
