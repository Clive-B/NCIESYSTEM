from pathlib import Path
import re
import zipfile
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "NCIE-001_Master_PRD_v1_2_EXPANDED_BASELINE.docx"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ARROWS = "→←↔↓↑"


def paragraph_text(paragraph):
    parts = []
    for node in paragraph.iter():
        if node.tag == W + "t" and node.text:
            parts.append(node.text)
        elif node.tag in {W + "br", W + "cr"}:
            parts.append("\n")
        elif node.tag == W + "tab":
            parts.append("\t")
    return "".join(parts).strip()


def arrow_count(text):
    return sum(text.count(char) for char in ARROWS)


def arrow_only(text):
    compact = re.sub(r"\s+", "", text)
    return bool(compact) and all(char in ARROWS for char in compact)


def diagramish_line(text):
    text = text.strip()
    if not text:
        return False
    if arrow_only(text) or arrow_count(text):
        return True
    if len(text) > 180 or "\n" in text:
        return False
    if text.endswith((".", "?", "!", ";")):
        return False
    return len(text.split()) <= 20


def bridgeable_gap(texts, left_end, right_start):
    """Join diagram fragments separated only by short labels and small blank gaps."""
    gap = texts[left_end + 1:right_start]
    if len(gap) > 4:
        return False
    nonempty = [value.strip() for value in gap if value.strip()]
    return all(len(value) <= 220 and len(value.split()) <= 30 for value in nonempty)


def merge_ranges(texts, ranges):
    merged = []
    for start, end in sorted(ranges):
        if not merged:
            merged.append([start, end])
            continue
        previous_start, previous_end = merged[-1]
        direct_overlap = start <= previous_end + 1
        close_arrow_fragments = (
            start <= previous_end + 5
            and bridgeable_gap(texts, previous_end, start)
            and any(arrow_only(texts[i]) for i in range(previous_start, previous_end + 1))
            and any(arrow_only(texts[i]) for i in range(start, end + 1))
        )
        if direct_overlap or close_arrow_fragments:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return [tuple(item) for item in merged]


def detect(texts):
    ranges = []
    for index, text in enumerate(texts):
        if not arrow_only(text):
            continue
        start = index
        while start > 0 and diagramish_line(texts[start - 1]):
            start -= 1
        end = index
        while end + 1 < len(texts) and diagramish_line(texts[end + 1]):
            end += 1
        ranges.append((start, end))

    index = 0
    while index < len(texts):
        if not arrow_count(texts[index]):
            index += 1
            continue
        end = index
        while end + 1 < len(texts) and arrow_count(texts[end + 1]):
            end += 1
        if end > index:
            ranges.append((index, end))
        index = end + 1

    for index, text in enumerate(texts):
        if arrow_count(text) >= 2 or text.count("|") >= 2 or "↓" in text:
            ranges.append((index, index))

    merged = merge_ranges(texts, ranges)
    return [item for item in merged if any(texts[i].strip() for i in range(item[0], item[1] + 1))]


def main():
    with zipfile.ZipFile(SOURCE) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    body = root.find(W + "body")
    paragraphs = [child for child in body if child.tag == W + "p"]
    texts = [paragraph_text(paragraph) for paragraph in paragraphs]
    ranges = detect(texts)
    print(f"body_paragraphs={len(texts)}")
    print(f"diagram_blocks={len(ranges)}")
    print(f"diagram_paragraphs={sum(end - start + 1 for start, end in ranges)}")
    for number, (start, end) in enumerate(ranges, start=1):
        values = [texts[index].replace("\n", " / ") for index in range(start, end + 1) if texts[index]]
        sample = " || ".join(values)
        print(f"{number:03d} [{start}:{end}] {sample[:900]}")


if __name__ == "__main__":
    main()
