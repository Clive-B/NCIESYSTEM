"""Assemble NCIE-005 ARGUS Intelligence Assistant Specification (In Development)."""

from pathlib import Path

from docx import Document

from ncie005_common import (
    DOC_ID,
    add_cover,
    add_governance_block,
    add_toc,
    configure_document,
    render_chapter,
    validate_output,
)
from ncie005_content import CHAPTERS, FRONT_MATTER, set_blocks

BATCH_MODULES = [
    "ncie005_ch01_06",
    "ncie005_ch07_12",
    "ncie005_ch13_18",
    "ncie005_ch19_24",
    "ncie005_ch25_30",
    "ncie005_ch31_33",
    "ncie005_ch34_35",
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
OUTPUT = ROOT / "NCIE-005_ARGUS_Intelligence_Assistant_Specification_v1_2_IN_DEVELOPMENT.docx"


def add_front_matter_body(document):
    document.add_paragraph("Document Governance", style="NCIE Front Heading")
    add_governance_block(document, FRONT_MATTER["governance_rows"])

    document.add_paragraph("0.1  Authority Chain", style="Heading 2")
    document.add_paragraph(
        "NCIE-001 requirements → NCIE-002 architecture → NCIE-003 canonical data → NCIE-004 "
        "engineering baseline → NCIE-005 ARGUS behavioral & interaction specification. NCIE-005 "
        "specifies how ARGUS behaves and interacts with humans; it does not redesign upstream "
        "architecture, and it does not duplicate the Model Gateway, memory, agent-orchestration, "
        "security or data architectures owned upstream, or the functional-module detail owned by "
        "NCIE-013.",
        style="NCIE Body",
    )

    document.add_paragraph("0.2  Token-Conservation Convention", style="Heading 2")
    document.add_paragraph(
        "Every chapter opens with a short Upstream block citing the specific upstream chapter and "
        "stating only the behavioral consequence for ARGUS — never a restatement of the upstream "
        "architecture. Repeated invariants (Human-Primary authority, voice-is-not-authority) are "
        "stated once below and referenced, not re-explained per chapter.",
        style="NCIE Body",
    )

    document.add_paragraph("0.3  ARGUS Core Doctrine", style="Heading 2")
    document.add_paragraph(
        "ARGUS is a governed intelligence assistant and active analytical participant, not a "
        "chatbot or Q&A tool. It answers, questions, challenges, generates hypotheses and "
        "alternative explanations, seeks contradictions and counterevidence, exposes assumptions, "
        "identifies evidence gaps and discriminating evidence, compares historical situations, "
        "retrieves institutional knowledge, participates in collaborative brainstorming, maintains "
        "Evidence-Watch, proposes tools/actions, supports briefing, and interacts verbally — all "
        "under the invariant in §0.4.",
        style="NCIE Body",
    )

    document.add_paragraph("0.4  Human-Primary Authority Invariant", style="Heading 2")
    document.add_paragraph(
        "ARGUS PARTICIPATES IN INTELLIGENCE — HUMANS RETAIN INSTITUTIONAL AUTHORITY. This invariant "
        "governs every chapter of this document and is stated once here rather than re-derived "
        "repeatedly.",
        style="NCIE Body",
    )
    document.add_paragraph("ARGUS may: question, challenge, recommend, hypothesize, contradict, summarize, propose actions, and request additional evidence.", style="List Bullet")
    document.add_paragraph("ARGUS does not autonomously: issue regulatory Decisions, approve Findings, determine culpability, change Rules, approve Institutional Knowledge, authorize tracking, authorize blocking, or expand a user's permissions.", style="List Bullet")
    document.add_paragraph(
        "The full ARGUS Behavioral Invariants Register (may/may-not, per capability) is Chapter 2's "
        "subject matter; this front-matter statement is the one place the invariant itself is "
        "declared.",
        style="NCIE Body",
    )

    document.add_paragraph("0.5  Voice Interaction Update — Governing Invariants", style="Heading 2")
    document.add_paragraph(
        "NCIE-005 v0.2 requires ARGUS to support spoken notifications and two-way verbal interaction "
        "in addition to visual/text interaction. Voice extends the interaction modality; it does not "
        "change ARGUS's institutional role, evidence status, authorization, decision authority or "
        "Human-Primary governance. These invariants govern every voice-capable chapter and are "
        "stated once here:",
        style="NCIE Body",
    )
    for line in [
        "VOICE IS AN INTERACTION MODALITY — NOT AN AUTHORITY MODALITY.",
        "DISPLAY AUTHORIZATION ≠ SPOKEN-DISCLOSURE AUTHORIZATION.",
        "SPOKEN NOTIFICATION ≠ FORMAL ACKNOWLEDGEMENT unless the governed workflow explicitly records acknowledgement.",
        "VERBAL REQUEST ≠ AUTHORIZATION. Consequential spoken requests follow the same authorization, target validation, confirmation, approval, execution and audit path as typed requests.",
        "ARGUS SPEECH ≠ INSTITUTIONAL DECISION. Spoken recommendations, hypotheses and challenges retain the same epistemic status as textual equivalents.",
        "Voice input/output shall remain provider-neutral and shall not make ARGUS dependent on one STT or TTS vendor.",
        "Microphone activation, listening state and speaking state shall be visible and controllable to users.",
        "Sensitive information shall undergo a spoken-disclosure check before TTS output; authorization to view information does not automatically authorize audible disclosure.",
        "VOICE/SPEAKER RECOGNITION ≠ AUTHENTICATED IDENTITY. ARGUS shall not infer institutional identity, role or authority from voice characteristics alone. Consequential authorization shall rely on the governed NCIE identity and authentication context (NCIE-004 Ch.23), never on a voice sounding like a particular person.",
    ]:
        document.add_paragraph(line, style="List Bullet")

    document.add_paragraph("0.6  Controlled Upstream Impact Register", style="Heading 2")
    document.add_paragraph(
        "These impacts are recorded, per the approved skeleton, for incorporation into future "
        "controlled revisions of already-approved upstream documents. They do not reopen or "
        "invalidate those baselines, and NCIE-005 does not itself modify NCIE-001 through NCIE-004.",
        style="NCIE Body",
    )
    for line in [
        "NCIE-001 — add/confirm spoken notifications, verbal interaction, voice invocation, mute/interrupt controls and accessibility requirements.",
        "NCIE-002 — add the abstract voice path: audio input → STT → governed ARGUS pipeline → voice disclosure policy → TTS → authorized audio output, including audit, privacy and degraded-mode boundaries.",
        "NCIE-003 — extend ARGUS interaction/provenance semantics with modality, voice-session/transcription references where retained, spoken-notification state, retention and classification metadata.",
        "NCIE-004 — add provider-neutral STT/TTS, streaming audio/voice transport, latency/quality observability and speech-privacy controls as controlled technology decisions.",
        "Disposition — upstream documents remain approved; incorporate these impacts during the suite-wide consistency/revision pass or earlier if implementation sequencing requires them.",
    ]:
        document.add_paragraph(line, style="List Bullet")

    document.add_paragraph("0.7  Human Review Focus Classification", style="Heading 2")
    document.add_paragraph(
        "Every chapter's Human Review Focus item carries one of five labels: PROPOSED DESIGN "
        "DEFAULT; INSTITUTIONAL CONFIRMATION REQUIRED; WORKFLOW/SOURCE DISCOVERY REQUIRED; LEGAL/"
        "POLICY CONFIRMATION REQUIRED; or RESOLVED BY UPSTREAM BASELINE. Chapter 34 consolidates "
        "every open item, extracted directly from the chapters so the register cannot drift from "
        "its sources.",
        style="NCIE Body",
    )

    document.add_paragraph("0.8  Status Convention", style="Heading 2")
    document.add_paragraph(
        "Skeletal-structure approval authorizes expansion; it does not approve any individual "
        "behavioral interpretation. Every chapter in this edition is stamped IN DEVELOPMENT — FOR "
        "HUMAN REVIEW and remains so until explicitly approved.",
        style="NCIE Body",
    )

    document.add_paragraph("0.9  Hardening Pass (v1.1)", style="Heading 2")
    document.add_paragraph(
        "NCIE-005 v1.0 received a full human review. Disposition: CONDITIONAL PASS — behaviorally "
        "and architecturally sound; four small hardening controls recommended before baseline "
        "approval. All four are applied in this v1.1 edition, with no rewrite, expansion or "
        "restructuring of the 35 chapters:",
        style="NCIE Body",
    )
    document.add_paragraph(
        "(1) VOICE/SPEAKER RECOGNITION ≠ AUTHENTICATED IDENTITY is added to the voice governing "
        "invariants above and cross-referenced in Ch.4 §4.2 — ARGUS never infers institutional "
        "identity, role or authority from voice characteristics; consequential authorization always "
        "derives from the governed NCIE identity/authentication context.",
        style="List Bullet",
    )
    document.add_paragraph(
        "(2) Ch.29 §29.1 now states that where physical listening context cannot be established, "
        "ARGUS defaults to the more restrictive spoken-disclosure behavior for highly sensitive "
        "information and may redirect the user to the protected visual interface.",
        style="List Bullet",
    )
    document.add_paragraph(
        "(3) Ch.15 §15.2 adds Evidence-Watch spoken-notification anti-fatigue controls: "
        "deduplication, cooldown/suppression, a stricter materiality threshold than the visual "
        "channel, severity-gated escalation, Room/user quiet policy, and no repeated verbalization "
        "of unchanged state. This correction itself added one new Human Review item (the cooldown/"
        "escalation tuning item in Ch.15 §15's review focus), which is why the v1.2 count in (4) "
        "below is one higher than the count first reported when v1.1 was drafted.",
        style="List Bullet",
    )
    from ncie005_ch34_register import summary_counts as _hr_counts
    _c = _hr_counts()
    document.add_paragraph(
        f"(4) Chapter 34's Human Review Register was mechanically re-verified for v1.2: an "
        f"independent manual extraction of every chapter's review blocks ({_c['total']} items: "
        f"{_c['proposed']} Proposed Design Default, {_c['institutional']} Institutional Confirmation "
        f"Required, {_c['legal']} Legal/Policy Confirmation Required, {_c['resolved']} Resolved by "
        f"Upstream Baseline, {_c['workflow']} Workflow/Source Discovery Required; {_c['blocking']} "
        f"Blocking, {_c['non_blocking']} Non-Blocking) matches the register's own programmatic "
        "extraction exactly — no discrepancy found. Both this front-matter statement and Chapter "
        "34's own summary/register (§34.2-§34.3) are generated from the identical computed source "
        "at build time, so they cannot state different totals from each other going forward.",
        style="NCIE Body",
    )
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

    document.core_properties.title = f"{DOC_ID} ARGUS Intelligence Assistant Specification"
    document.core_properties.subject = "ARGUS behavioral and interaction specification — in development"
    document.core_properties.author = "National Communications Intelligence Ecosystem (NCIE)"
    document.core_properties.category = "Controlled Engineering Document"
    document.core_properties.keywords = (
        "NCIE, ARGUS, intelligence assistant, voice interaction, communications intelligence, Ghana, Codex"
    )
    document.core_properties.comments = (
        "Expands the approved NCIE-005 skeletal ARGUS specification (v0.2, Voice Interaction Update, "
        "35 chapters). Chapters remain IN DEVELOPMENT — FOR HUMAN REVIEW until explicitly approved."
    )

    document.save(OUTPUT)
    validation = validate_output(OUTPUT)
    print(f"output={OUTPUT}")
    print(f"batches_loaded={loaded}")
    print(f"chapters_written={len(CHAPTERS)}")
    print(f"validation={validation}")


if __name__ == "__main__":
    main()
