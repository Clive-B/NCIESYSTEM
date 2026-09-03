"""NCIE-004 content batch: Chapters 13-18 (object/evidence storage, search,
graph, vector retrieval, cache, ARGUS/Model Gateway)."""

BLOCKS = {}

# ---------------------------------------------------------------------------
# Chapter 13 — Object, Document & Evidence Storage
# ---------------------------------------------------------------------------
BLOCKS[13] = [
    ("upstream", [
        ("NCIE-003", "Ch.17", "Evidence Objects require hash/integrity metadata, WORM-capable retention and chain-of-custody re-verification."),
    ]),
    ("h2", "13.1 Object/Document Storage"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Object/document storage", "S3-compatible, versioned, encrypted at rest (Ch.24)", "MinIO (self-hosted, sovereignty-friendly) or S3-compatible NCA-approved object store", "Managed cloud object storage if hosting model permits", "SECURITY"],
        ["Versioning", "New-version-not-overwrite on correction is mandated (NCIE-003 Ch.17 §17.5); the storage mechanism is not", "Object-store native versioning", "—", "PROPOSED"],
        ["WORM / immutability", "Evidence cannot be silently altered post-registration (NCIE-003 Ch.17; capability named in the approved Ch.13 skeleton); the specific retention mechanism is a product feature, not itself mandated", "Object-lock / compliance-mode retention on evidence buckets", "—", "PROPOSED"],
        ["Hashing", "Chain-of-custody verification on registration and retrieval is mandated (NCIE-003 Ch.17 §17.6); the hash algorithm is not specified upstream", "SHA-256 computed at registration and re-verified on formal retrieval", "—", "PROPOSED"],
        ["Malware scanning", "Ingested artifacts (screenshots, uploaded files) scanned before acceptance", "Scan-on-ingest pipeline ahead of validation (NCIE-003 Ch.6)", "—", "PROPOSED"],
    ],
     "Object, document and evidence storage decisions.", 4),
    ("h2", "13.2 Engineering Notes"),
    ("bullets", [
        "A hash mismatch on retrieval halts release of the artifact and raises a chain-of-custody exception (NCIE-003 Ch.17 §17.7), never a silent pass-through.",
        "Lifecycle (hot/warm/cold tiering) follows NCIE-003 Ch.35 without changing meaning or classification.",
    ]),
    ("review", [
        "Confirm retention/WORM period requirements per NCA legal guidance (NCIE-003 Ch.17 §17-review already flags this upstream)."]),
    ("trace", "NCIE-003 Ch.6, Ch.17, Ch.31, Ch.35."),
]

# ---------------------------------------------------------------------------
# Chapter 14 — Search, Indexing & Retrieval Stack
# ---------------------------------------------------------------------------
BLOCKS[14] = [
    ("upstream", [
        ("NCIE-003", "Ch.36 §36.4", "Search indexes must apply classification-aware segmentation; embedding/indexing a protected field must never make it globally searchable."),
    ]),
    ("h2", "14.1 Search and Retrieval Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Search engine", "Full-text + faceted search over canonical entities, authorization-aware", "OpenSearch (avoids Elastic licensing constraints)", "Elasticsearch if NCA already licenses it", "PROPOSED"],
        ["Facets", "Domain/classification/operator/date faceting matching NCIE-003 Ch.3 families", "Engine-native aggregations", "—", "PROPOSED"],
        ["Authorization filters", "Classification-aware filtering is mandated (NCIE-003 Ch.36 §36.4), which itself offers index segmentation, security metadata filtering or post-retrieval authorization as alternative mechanisms — this row selects one", "Index-per-classification-tier + post-retrieval authorization check", "—", "PROPOSED"],
        ["Snippets", "Result highlighting without leaking unauthorized field content", "Engine-native highlighting restricted to authorized fields only", "—", "PROPOSED"],
        ["Reindexing", "Rebuildable-from-canonical is mandated (Ch.32 §32.5); the specific pipeline mechanism is not", "Scheduled/triggered reindex pipeline, never a manual one-off script", "—", "PROPOSED"],
    ],
     "Search, indexing and retrieval technology decisions.", 4),
    ("review", [
        "Confirm autocomplete/search must never reveal restricted case names, SIM identifiers or locations (NCIE-003 Ch.4 §4.90) — verify engine config enforces this at index build time."]),
    ("trace", "NCIE-003 Ch.4 §4.89-4.93, Ch.36."),
]

# ---------------------------------------------------------------------------
# Chapter 15 — Graph Technology & Relationship Analytics
# ---------------------------------------------------------------------------
BLOCKS[15] = [
    ("upstream", [
        ("NCIE-003", "Ch.19", "Typed edges require Edge Origin (observed/deterministic/human-inferred/ARGUS-proposed) and Validation State as first-class properties, not graph metadata bolted on."),
    ]),
    ("h2", "15.1 Graph Technology"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Graph engine", "Property graph with temporal-edge support (NCIE-003 Ch.19 §19.3)", "Neo4j", "Apache AGE (PostgreSQL extension, minimises polyglot footprint)", "PROPOSED"],
        ["Query language", "Expressive multi-hop traversal with authorization-aware filtering", "Cypher (Neo4j) / openCypher (AGE)", "—", "PROPOSED"],
        ["Temporal edges", "Effective-period validity per NCIE-003 Ch.5, Ch.19 §19.3", "Edge properties carrying effective-from/to, queried via Ch.5's bitemporal pattern", "—", "MANDATE"],
        ["Access filtering", "Sensitive traversal rules crossing protected-identity/Anti-Fraud boundaries (NCIE-003 Ch.19 §19.7)", "Query-time authorization filter preventing traversal into unauthorized-classification nodes", "—", "SECURITY"],
        ["Graph analytics", "Correlation pattern detection feeding Cross-Domain Fusion", "Engine-native graph algorithms (community detection, shortest-path) as analyst-invoked queries, never autonomous", "—", "PROPOSED"],
    ],
     "Graph technology and relationship analytics decisions.", 4),
    ("review", [
        "Confirm sensitive graph-traversal rules with NCA IT Security/Anti-Fraud before enabling multi-hop queries in production (NCIE-003 Ch.19 §19-review)."]),
    ("trace", "NCIE-003 Ch.5, Ch.19."),
]

# ---------------------------------------------------------------------------
# Chapter 16 — Vector Retrieval & Semantic Search Technology
# ---------------------------------------------------------------------------
BLOCKS[16] = [
    ("upstream", [
        ("NCIE-002", "Ch.26 §26.3", "Sensitive semantic/vector indexing requires index segmentation, security metadata filtering or post-retrieval authorization."),
        ("NCIE-003", "Ch.36 §36.4", "Embedding a protected field must never make it globally searchable."),
    ]),
    ("h2", "16.1 Vector Retrieval Stack"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Embedding service", "Classification-aware, routes through the Model Gateway (Ch.18), never a direct provider call", "Embedding models registered in the Approved Model Registry (Ch.18)", "—", "MANDATE"],
        ["Vector store", "Metadata-filterable, index-isolated by classification tier", "pgvector (PostgreSQL extension) for launch scale", "Dedicated vector database (e.g. Qdrant/Milvus) if scale later demands it", "PROPOSED"],
        ["Metadata filters", "Classification/domain/room-scope filtering applied before similarity search returns results", "Filtered ANN search restricted to the querying identity's authorized scope", "—", "MANDATE"],
        ["Index isolation", "Protected/sensitive content never in a general-purpose shared index (NCIE-003 Ch.36 §36.4)", "Separate vector index per classification tier", "—", "SECURITY"],
        ["Re-embedding", "Model upgrade must reconnect to governed state, not silently re-embed sensitive content without review", "Scheduled, audited re-embedding pipeline", "—", "PROPOSED"],
        ["Evaluation", "Retrieval quality assessed before production use (Ch.19)", "Retrieval-quality evaluation harness integrated with Ch.19's AI evaluation suite", "—", "PROPOSED"],
    ],
     "Vector retrieval and semantic search technology decisions.", 4),
    ("review", [
        "Confirm which data classes may ever be embedded at all, versus excluded from vector retrieval entirely (feeds Ch.25 DLP policy)."]),
    ("trace", "NCIE-002 Ch.26 §26.3; NCIE-003 Ch.36 §36.4."),
]

# ---------------------------------------------------------------------------
# Chapter 17 — Cache & Distributed State Technology
# ---------------------------------------------------------------------------
BLOCKS[17] = [
    ("upstream", [
        ("NCIE-002", "Ch.30 §30.5", "Caching may never bypass authorization filtering or evidence/provenance recording; cache invalidation must preserve control correctness, not only data freshness."),
    ]),
    ("h2", "17.1 Cache and Distributed State"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Distributed cache", "Sub-100ms authorization-decision and rule-lookup caching (NCIE-002 Ch.4 §4.7, NCIE-003 Ch.24 §24.9)", "Redis", "—", "PROPOSED"],
        ["Session/ephemeral state", "Session tokens, presence (Ch.21), rate-limit counters", "Redis-backed session store", "—", "PROPOSED"],
        ["Cache invalidation", "No stale authorization decision past revocation is mandated verbatim (NCIE-002 Ch.4 §4.6); event-driven invalidation is one mechanism among alternatives (e.g. short TTL)", "Event-driven invalidation on permission/rule change (Ch.9 event broker)", "—", "PROPOSED"],
    ],
     "Cache and distributed-state technology decisions.", 4),
    ("h2", "17.2 Engineering Notes"),
    ("bullets", [
        "Cache is never classification-isolated; a protected value is never cached without the same access control as its canonical source (NCIE-003 Ch.36).",
        "Cache-node failure degrades to direct database reads with higher latency, never to serving unauthenticated/unauthorized results.",
    ]),
    ("trace", "NCIE-002 Ch.4, Ch.30 §30.5."),
]

# ---------------------------------------------------------------------------
# Chapter 18 — ARGUS AI Platform & Model Gateway Technology
# ---------------------------------------------------------------------------
BLOCKS[18] = [
    ("upstream", [
        ("NCIE-002", "Ch.19 §19.11, Ch.24", "ARGUS is a presentation identity for the NCIE Intelligence Assistant; the underlying architecture is provider-neutral via the Model Gateway."),
        ("NCIE-003", "Ch.20", "ARGUS Interaction/Contribution/AI Provenance entities must be populated by whatever engineering implements the gateway, without persisting private chain-of-thought."),
    ]),
    ("h2", "18.1 ARGUS Engineering Relationship"),
    ("p",
     "ARGUS is not a specific LLM. The engineering relationship is fixed and does not change with "
     "model/provider substitution:"),
    ("flow",
     [
        "ARGUS (user-facing NCIE Intelligence Assistant identity)",
        "Model Gateway (provider-neutral entry point)",
        "Routing Policy (classification, task type, purpose, residency, retention)",
        "Approved Model Registry (NCIE-003 Ch.20 §20.3 Model Route/Version)",
        "Provider Adapter (per-provider integration shim)",
        "Eligible Model / Deployment (internal or approved external)",
     ],
     "ARGUS engineering relationship: ARGUS is never architected directly around one provider SDK."),
    ("h2", "18.2 Model Gateway Technology"),
    ("table",
     ["Capability", "Engineering Characteristics Required", "Candidate/Default", "Alternative", "Status"],
     [
        ["Model Gateway", "Provider-neutral abstraction is mandated by name (NCIE-002 Ch.24 §24.2); this row states only that an internal gateway service must exist, not a specific implementation technology", "Internal gateway service, provider-neutral by construction", "—", "MANDATE"],
        ["Provider adapters", "One adapter per eligible provider is the mandated pattern itself (NCIE-002 Ch.24 §24.2) — this is the mandate, not an implementation choice on top of it", "Adapter-per-provider pattern behind a common interface", "—", "MANDATE"],
        ["Approved Model Registry", "That a registry tracking model/provider/classification eligibility exists is mandated by name (NCIE-003 Ch.20 §20.3); where/how it is stored is an implementation choice", "Registry table in the transactional store (Ch.11), administered via Ch.33", "—", "PROPOSED"],
        ["Routing policy engine", "Classification-aware eligibility per §18.3 below", "Policy evaluated per-request before model selection", "—", "MANDATE"],
        ["Context assembly", "Minimal, authorization-filtered context per request (NCIE-002 Ch.24 §24.3)", "Context Builder service filtering by requester's effective authorization", "—", "MANDATE"],
        ["Fallback", "Failover to an alternate approved model; never an unapproved model as fallback (NCIE-002 Ch.24 §24.9)", "Routing policy defines an approved fallback chain per task type", "—", "PROPOSED"],
    ],
     "ARGUS Model Gateway technology decisions.", 4),
    ("h2", "18.3 Classification-Aware Model Eligibility"),
    ("p",
     "Routing considers data classification, task type, purpose, model capability, provider "
     "eligibility, residency, retention policy, tool requirements and availability together. An "
     "external model is never an automatic fallback for restricted information merely because the "
     "preferred (internal/sovereign) model is unavailable — unavailability degrades ARGUS "
     "conversational capability (Ch.19 §19.4 covers the outage boundary), it does not relax "
     "classification eligibility."),
    ("review", [
        "Confirm internal-vs-external-vs-hybrid model deployment policy and data-residency constraints with NCA information-security and legal leadership (NCIE-002 Ch.24 §24-review already raised this)."]),
    ("trace", "NCIE-002 Ch.19 §19.11, Ch.24; NCIE-003 Ch.20."),
]
