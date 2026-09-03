"""Assemble NCIE-003 Data Model & Data Dictionary (In Development)."""

from pathlib import Path

from docx import Document

from ncie003_common import (
    DOC_ID,
    add_cover,
    add_governance_block,
    add_status,
    add_toc,
    configure_document,
    render_chapter,
    validate_output,
)
from ncie003_content import CHAPTERS, FRONT_MATTER, set_blocks

BATCH_MODULES = [
    "ncie003_ch01_06",
    "ncie003_ch07_14",
    "ncie003_ch15_22",
    "ncie003_ch23_30",
    "ncie003_ch31_38",
    "ncie003_ch39_43",
]


def load_batches():
    import importlib

    loaded = []
    for name in BATCH_MODULES:
        try:
            module = importlib.import_module(name)
        except ImportError:
            continue
        for number, blocks in module.BLOCKS.items():
            set_blocks(number, blocks)
        loaded.append(name)
    return loaded


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "NCIE-003_Data_Model_Data_Dictionary_v0_4_IN_DEVELOPMENT.docx"


def add_front_matter_body(document):
    document.add_paragraph("Document Governance", style="NCIE Front Heading")
    add_governance_block(document, FRONT_MATTER["governance_rows"])

    document.add_paragraph("0.1  Authority Chain", style="Heading 2")
    document.add_paragraph(
        "NCIE-001 establishes what NCIE requires. NCIE-002 establishes how the system is "
        "architecturally structured. NCIE-003 establishes how the information required by that "
        "architecture is represented, related, governed and persisted. NCIE-003 implements "
        "NCIE-002 semantically; it does not reinterpret it. Where this document appears to require "
        "an architectural change to NCIE-002, the affected chapter flags it as UPSTREAM ARCHITECTURE "
        "IMPACT — REVIEW REQUIRED rather than silently modifying the architecture through the data "
        "model.",
        style="NCIE Body",
    )

    document.add_paragraph("0.2  Baseline and Numbering Status", style="Heading 2")
    document.add_paragraph(
        "The NCIE-003 Skeletal v0.2 43-chapter structure is the approved structural baseline for "
        "this expansion; its original “FOR REVIEW — NOT YET APPROVED FOR FULL EXPANSION” stamp is "
        "superseded by that approval. The structure is locked unless a genuine architectural "
        "contradiction or material omission is discovered during expansion, in which case it is "
        "flagged rather than silently corrected. Separately, the NCIE Production Documentation Suite "
        "register identifies NCIE-003 as “Technology Stack & Engineering Blueprint”; that entry is "
        "stale relative to this approved artifact and is not overridden or renumbered by this "
        "document — reconciling the register, and deciding what becomes of the displaced document, "
        "is a documentation-governance decision outside this expansion's scope.",
        style="NCIE Body",
    )

    document.add_paragraph("0.3  Chapter Status Convention", style="Heading 2")
    document.add_paragraph(
        "Every chapter in this edition is stamped IN DEVELOPMENT — FOR HUMAN REVIEW. Approval of the "
        "skeletal baseline authorizes expansion; it does not automatically approve every expanded "
        "interpretation. Chapters move to Approved only on explicit confirmation.",
        style="NCIE Body",
    )

    document.add_paragraph("0.4  Human Review Focus Classification", style="Heading 2")
    document.add_paragraph(
        "Every chapter closes with a classified Human Review Focus register. Each item carries one "
        "of five labels:",
        style="NCIE Body",
    )
    document.add_paragraph(
        "RESOLVED BY APPROVED NCIE BASELINE — already established by NCIE-001/002 or an approved "
        "NCIE-003 decision.",
        style="List Bullet",
    )
    document.add_paragraph(
        "PROPOSED DESIGN DEFAULT — technically recommended for the implementation baseline but "
        "subject to NCA confirmation.",
        style="List Bullet",
    )
    document.add_paragraph(
        "INSTITUTIONAL CONFIRMATION REQUIRED — cannot legitimately be settled from architecture "
        "alone.",
        style="List Bullet",
    )
    document.add_paragraph(
        "SOURCE/DATA DISCOVERY REQUIRED — depends on actual NCA/operator systems, schemas, fields, "
        "workflows or data characteristics not yet inspected.",
        style="List Bullet",
    )
    document.add_paragraph(
        "LEGAL/POLICY CONFIRMATION REQUIRED — depends on applicable NCA policy, records requirements, "
        "privacy, legal authority, sovereignty or regulatory interpretation.",
        style="List Bullet",
    )
    document.add_paragraph(
        "The last three categories are never converted into invented facts to make the document "
        "appear complete. Chapter 42 consolidates every still-open item across all chapters into the "
        "authoritative Open Institutional Decisions & Human Review Register.",
        style="NCIE Body",
    )

    document.add_paragraph("0.5  Depth Standard", style="Heading 2")
    document.add_paragraph(
        "Architecture already established in NCIE-002 is referenced, not rewritten. Each substantive "
        "data-model capability addresses, where relevant: purpose, semantic definition, principal "
        "entities, attributes/attribute classes, relationships and cardinality, identifiers, "
        "lifecycle/states, temporal semantics, provenance, validation/constraints, "
        "classification/security, ownership, failure/exception semantics, ARGUS implications where "
        "relevant, NCIE-002 traceability, human review requirements and acceptance criteria. Atomic "
        "definitions or invariants remain short where additional prose would add no technical value.",
        style="NCIE Body",
    )

    document.add_paragraph("0.6  Reviewer Disposition (v0.2 Review) and v0.3 Hardening Pass", style="Heading 2")
    document.add_paragraph(
        "NCIE-003 v0.2 (109 pages, 43 chapters) received its first full human review. The reviewer's "
        "disposition was CONDITIONAL PASS: the 43-chapter architecture, NCIE-001/002 alignment, "
        "canonical semantic separations, ARGUS/human provenance model, temporal/decision-time model, "
        "security/classification model, domain coverage, no-fabrication discipline and logical data "
        "modelling all passed review. Two items were identified as not yet complete by design — the "
        "final production field-level Data Dictionary (Chapter 39 remains representative, pending "
        "source discovery) and source-system mappings generally — and one item was identified for "
        "correction: Chapter 42 held only representative high-priority open decisions rather than the "
        "complete register its own stated purpose promised.",
        style="NCIE Body",
    )
    document.add_paragraph(
        "The reviewer's recommended disposition for this baseline, once the corrections below are "
        "made, is:",
        style="NCIE Body",
    )
    from ncie003_common import add_proposed
    add_proposed(
        document,
        "NCIE-003 v0.3 — APPROVED CANONICAL DATA ARCHITECTURE BASELINE, SUBJECT TO CONTROLLED "
        "DATA-DISCOVERY COMPLETION. This means the architecture, semantics, entity framework, "
        "modelling standards, governance model, temporal model, provenance model, security model, "
        "ARGUS model and logical relationships in Chapters 1-41 are approved, and Chapter 42 is "
        "approved as the controlled open-decisions register attached to this baseline — the register "
        "itself is part of the approved baseline; the 121 open items it holds are not thereby "
        "resolved, and remain governed discovery/institutional dependencies. This is explicitly "
        "distinct from — and must never be read as — FINAL PRODUCTION DATA DICTIONARY, which would "
        "imply Chapter 39's field-level population and source mappings are complete; they are not.",
    )
    document.add_paragraph(
        "This is the reviewer's recorded recommendation, not a self-declared approval — formal "
        "sign-off remains a human/institutional act per §0.3. This v0.3 edition makes the following "
        "corrections requested by that review: (1) Chapter 42 now holds the complete master register "
        "of all 123 open-decision items, not a representative subset; (2) Chapter 41 adds an explicit "
        "Chapter 39↔40 consistency check; (3) the two-tier status distinction above is now recorded "
        "in this front matter and echoed in Chapter 43's acceptance checklist; (4) this document is "
        "versioned 0.3 to make the hardening pass traceable as a distinct, reviewed revision.",
        style="NCIE Body",
    )

    document.add_paragraph("0.7  Second Review (v0.3) and Formal Approval", style="Heading 2")
    document.add_paragraph(
        "NCIE-003 v0.3 received a second full human review, checking the four corrections above. "
        "The reviewer's disposition: all four corrections were confirmed effective, including "
        "verifying Chapter 42's complete 123-item register (121 open, 2 resolved, 85 blocking, 38 "
        "non-blocking) and Chapter 41's Chapter 39↔40 consistency check. Two further wording "
        "corrections were requested and are applied in this edition: (1) Chapter 43's tier-one scope "
        "was clarified so Chapter 42 reads as part of the approved baseline (an approved register), "
        "not as content excluded from it; (2) every place in this document that characterised the "
        "next NCIE artifact's substantive identity as “NCIE-004 (implementation-level data "
        "engineering)” was reworded to “the next approved NCIE production artifact (currently "
        "designated NCIE-004, subject to Documentation Suite Register reconciliation),” so this "
        "document does not make a suite-numbering decision it is not authorised to make (§0.2).",
        style="NCIE Body",
    )
    add_status(
        document,
        "Historical formal disposition (preserved, not current): following the second review, "
        "NCIE-003 v0.3 (Chapters 1-42, as scoped in Chapter 43 §43.2) was APPROVED as the Canonical "
        "Data Architecture Baseline, subject to controlled data-discovery completion. The Final "
        "Production Data Dictionary tier remained explicitly not approved.",
    )

    document.add_paragraph("0.8  Document Amendment History (v0.3 → v0.4)", style="Heading 2")
    for text in [
        "Version: v0.3",
        "Change: Complete master Human Review Register (123 items); Chapter 41 Ch.39↔40 consistency "
        "check; two-tier acceptance-status distinction; suite-numbering wording correction.",
        "Status: APPROVED as the Canonical Data Architecture Baseline, subject to controlled "
        "data-discovery completion (historical baseline preserved unchanged above).",
        "Version: v0.4",
        "Change: VPF & Dynamic Agent Synthesis Canonical-Data Consistency Amendment (Chapters 1-3, "
        "20, 21, 25, 26-30, 39-43). Recognizes the canonical Agent & VPF object family (Agent "
        "Definition, Agent Pattern, Agent Run, Task Contract, Agent Risk Classification, Agent Result "
        "Package, VPF Profile/Version, VPF Validation Artifact, VPF Disposition, Validated AI Result, "
        "Promotion Candidate, Engineering Change Candidate).",
        "Authority: Approved NCIE-001 Master PRD v1.3, approved NCIE-002 System Architecture & "
        "Technical Design v0.5, and approved NCIE-007 AI, Agent & Model Orchestration Specification "
        "v1.1.",
        "Scope: Controlled surgical amendment — not a rewrite, regeneration, restructuring or general "
        "data-model improvement of NCIE-003. The 43-chapter structure is unchanged.",
        "Human Review Register: 123 → 127 items (4 new: 3-C, 20-D, 20-E, 20-F, all Institutional, "
        "Non-Blocking); 121 → 125 Open, 2 Closed (unchanged); 85 Blocking (unchanged), 38 → 42 "
        "Non-Blocking. Reconciles as 123 + 4 added − 0 removed/merged = 127.",
        "Non-Impact: No change to canonical entities, domain models, temporal semantics, identifier "
        "rules, Evidence semantics, Decision-Time semantics, Human-Primary authority, ARGUS "
        "provenance model, Memory boundaries, authorization semantics, audit semantics or Data "
        "Dictionary governance beyond the specific extensions listed above.",
        "Status: v0.4 IN DEVELOPMENT — FOR HUMAN REVIEW OF SURGICAL AMENDMENT. The v0.3 approval "
        "remains historically preserved until v0.4 is reviewed and approved.",
    ]:
        document.add_paragraph(text, style="NCIE Body")

    document.add_page_break()


def main():
    loaded = load_batches()

    document = Document()
    configure_document(document)
    add_cover(document)
    add_front_matter_body(document)
    add_toc(document)

    for chapter in CHAPTERS:
        render_chapter(document, chapter)

    document.core_properties.title = f"{DOC_ID} Data Model & Data Dictionary"
    document.core_properties.subject = "NCIE canonical data model — in development"
    document.core_properties.author = "National Communications Intelligence Ecosystem (NCIE)"
    document.core_properties.category = "Controlled Engineering Document"
    document.core_properties.keywords = (
        "NCIE, data model, data dictionary, communications intelligence, Ghana, Codex"
    )
    document.core_properties.comments = (
        "v0.4: VPF & Dynamic Agent Synthesis Canonical-Data Consistency Amendment (Ch.1-3,20,21,25,"
        "26-30,39-43), authority NCIE-001 v1.3/NCIE-002 v0.5/NCIE-007 v1.1. IN DEVELOPMENT — FOR "
        "HUMAN REVIEW."
    )

    document.save(OUTPUT)
    validation = validate_output(OUTPUT)
    print(f"output={OUTPUT}")
    print(f"batches_loaded={loaded}")
    print(f"chapters_written={len(CHAPTERS)}")
    print(f"validation={validation}")


if __name__ == "__main__":
    main()
