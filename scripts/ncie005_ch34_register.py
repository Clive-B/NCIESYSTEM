"""NCIE-005 Chapter 34 master Human Review Register — extracted directly
from every chapter's ("review", [...]) blocks in Chapters 1-33, so the
register cannot drift from its sources (same discipline as NCIE-003 Ch.42
and NCIE-004 Ch.35).
"""

import importlib

from ncie005_common import REVIEW_STATUS

BATCH_MODULES = [
    "ncie005_ch01_06",
    "ncie005_ch07_12",
    "ncie005_ch13_18",
    "ncie005_ch19_24",
    "ncie005_ch25_30",
    "ncie005_ch31_33",
]

BLOCKING_STATUS = {"INSTITUTIONAL", "WORKFLOW", "LEGAL"}


def _extract():
    items = []
    seq_by_chapter = {}
    for name in BATCH_MODULES:
        module = importlib.import_module(name)
        for chnum, blocks in sorted(module.BLOCKS.items()):
            for block in blocks:
                if block[0] != "review":
                    continue
                for entry in block[1]:
                    if not isinstance(entry, tuple):
                        continue
                    category, text = entry
                    seq_by_chapter[chnum] = seq_by_chapter.get(chnum, 0) + 1
                    items.append({
                        "id": f"HR-{chnum}-{seq_by_chapter[chnum]}",
                        "chapter": chnum,
                        "category": category,
                        "issue": text,
                    })
    return items


REGISTER = _extract()


def register_rows():
    return [
        [it["id"], f"Ch.{it['chapter']}", it["issue"], REVIEW_STATUS[it["category"]],
         "BLOCKING" if it["category"] in BLOCKING_STATUS else "NON-BLOCKING"]
        for it in REGISTER
    ]


def summary_counts():
    from collections import Counter
    cat_counts = Counter(it["category"] for it in REGISTER)
    blocking = sum(1 for it in REGISTER if it["category"] in BLOCKING_STATUS)
    return {
        "total": len(REGISTER),
        "proposed": cat_counts.get("PROPOSED", 0),
        "institutional": cat_counts.get("INSTITUTIONAL", 0),
        "workflow": cat_counts.get("WORKFLOW", 0),
        "legal": cat_counts.get("LEGAL", 0),
        "resolved": cat_counts.get("RESOLVED", 0),
        "blocking": blocking,
        "non_blocking": len(REGISTER) - blocking,
    }
