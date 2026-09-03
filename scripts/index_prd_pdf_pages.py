import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".tmp_pypdf"))
from pypdf import PdfReader  # noqa: E402


PDF = ROOT / "NCIE-001_Master_PRD_v1_2_PAGINATION_STAGE.pdf"
OUTPUT = ROOT / "prd-page-index.json"

TITLES = {
    "Document Governance": None,
    "Executive Summary": None,
    "Product Vision, Mission, Principles & Scope": 1,
    "Product Scope, Functional Boundaries & NCIE Intelligence Domain Architecture": 2,
    "Product Capability Architecture": 3,
    "NCIE Command Center": 4,
    "Regulatory Early Warning System (REWS)": 5,
    "Data, Intelligence Domain, Canonical Model & Information Governance": 6,
    "Topology, Geography & QoS Campaign Intelligence": 7,
    "Intelligence Fusion, Cross-Domain Correlation & National Intelligence Synthesis Governance": 8,
    "Regulatory Intelligence, Compliance, Revenue Assurance & Governed Case Progression": 9,
    "Situational Awareness, Early Warning, Alerting & National Communications Operating Picture": 10,
    "Automation Orchestration & RPA Data Acquisition": 11,
    "NCIE Intelligence Assistant": 12,
    "Evidence, Knowledge, Memory & Provenance Governance": 13,
    "Security, Privacy, Identity, Authorization & Intelligence Sovereignty Governance": 14,
    "NCIE Intelligence Assistant, Conversational Intelligence, Collaborative Brainstorming & Governed Memory": 15,
    "Data Acquisition, Integration, Source Intelligence & Ingestion Governance": 16,
    "Automation Orchestration, RPA Governance, Scheduling & Autonomous Workflow Execution": 17,
    "Governance, Auditability, Explainability, Human Oversight, Operational Resilience & Product Acceptance": 18,
}


def main():
    reader = PdfReader(str(PDF))
    found = {}
    for page_number, page in enumerate(reader.pages, start=1):
        text = " ".join((page.extract_text() or "").split())
        for title, chapter in TITLES.items():
            if title in found or title not in text:
                continue
            if chapter is not None and f"Chapter {chapter} Expansion" not in text:
                continue
            found[title] = page_number
        if page_number % 100 == 0:
            print(f"scanned={page_number} found={len(found)}", flush=True)
    result = {
        "pdf_pages": len(reader.pages),
        "entries": found,
        "missing": [title for title in TITLES if title not in found],
    }
    OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
