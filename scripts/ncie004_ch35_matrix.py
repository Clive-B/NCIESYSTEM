"""NCIE-004 Chapter 35 consolidated Technology Decision Matrix and Human
Review Register — built by extracting every technology-decision table row
already authored in Chapters 1-32 (status_col-tagged tables), so the
consolidation reflects exactly what each chapter states rather than being
retyped. Avoids the NCIE-003 problem of a register drifting from its
source chapters.
"""

import importlib

from ncie004_common import TECH_STATUS

BATCH_MODULES = [
    "ncie004_ch01_06",
    "ncie004_ch07_12",
    "ncie004_ch13_18",
    "ncie004_ch19_24",
    "ncie004_ch25_30",
    "ncie004_ch31_32",
]

# Chapters whose technology rows are consolidated here (Ch.33-36 are governance
# chapters about the matrix/registry itself and are not self-consolidated).
CONSOLIDATE_UP_TO_CHAPTER = 32

BLOCKING_STATUS = {"SECURITY", "INFRASTRUCTURE", "INSTITUTIONAL"}


def _extract():
    matrix = []
    seq_by_chapter = {}
    for name in BATCH_MODULES:
        try:
            module = importlib.import_module(name)
        except ImportError:
            continue
        for chnum, blocks in sorted(module.BLOCKS.items()):
            if chnum > CONSOLIDATE_UP_TO_CHAPTER:
                continue
            for block in blocks:
                if block[0] != "table":
                    continue
                headers = block[1]
                rows = block[2]
                status_col = block[4] if len(block) > 4 else None
                if status_col is None:
                    continue
                try:
                    candidate_col = headers.index("Candidate/Default")
                except ValueError:
                    candidate_col = 2
                alt_col = headers.index("Alternative") if "Alternative" in headers else None
                for row in rows:
                    seq_by_chapter[chnum] = seq_by_chapter.get(chnum, 0) + 1
                    decision_id = f"TD-{chnum}-{seq_by_chapter[chnum]}"
                    status_key = row[status_col].strip().upper()
                    matrix.append({
                        "id": decision_id,
                        "chapter": chnum,
                        "capability": row[0],
                        "candidate": row[candidate_col] if candidate_col < len(row) else "—",
                        "alternative": row[alt_col] if alt_col is not None and alt_col < len(row) else "—",
                        "status": status_key,
                    })
    return matrix


MATRIX = _extract()


def matrix_rows():
    return [
        [m["id"], f"Ch.{m['chapter']}", m["capability"], m["candidate"], TECH_STATUS[m["status"]]]
        for m in MATRIX
    ]


def review_rows():
    reason_label = {
        "PROPOSED": "Proposed Design Default",
        "INSTITUTIONAL": "Institutional",
        "INFRASTRUCTURE": "Infrastructure Discovery",
        "SECURITY": "Security/Sovereignty",
    }
    rows = []
    for m in MATRIX:
        if m["status"] == "MANDATE":
            continue
        blocking = "BLOCKING" if m["status"] in BLOCKING_STATUS else "NON-BLOCKING"
        rows.append([
            m["id"], f"Ch.{m['chapter']}", m["capability"], reason_label[m["status"]], blocking,
        ])
    return rows


def summary_counts():
    from collections import Counter
    status_counts = Counter(m["status"] for m in MATRIX)
    blocking_count = sum(1 for m in MATRIX if m["status"] in BLOCKING_STATUS)
    non_blocking_open = sum(1 for m in MATRIX if m["status"] == "PROPOSED")
    mandate_count = status_counts.get("MANDATE", 0)
    return {
        "total": len(MATRIX),
        "mandate": mandate_count,
        "proposed": status_counts.get("PROPOSED", 0),
        "institutional": status_counts.get("INSTITUTIONAL", 0),
        "infrastructure": status_counts.get("INFRASTRUCTURE", 0),
        "security": status_counts.get("SECURITY", 0),
        "blocking": blocking_count,
        "non_blocking_open": non_blocking_open,
    }
