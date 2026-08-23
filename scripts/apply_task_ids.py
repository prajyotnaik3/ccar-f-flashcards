#!/usr/bin/env python3
"""Infer and apply Exam Guide task IDs to all flashcard YAML files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

from card_loader import DOMAINS_DIR

TASK_RE = re.compile(r"Task ([1-5])\.([1-9])")
RANGE_RE = re.compile(r"Task ([1-5])\.([1-9])[–-]([1-5])\.([1-9])")

# Cards without explicit Task N.M in sources (scenario hooks, samples, cross-links)
MANUAL_TASKS: dict[str, list[str]] = {
    "d1-040": ["1.2"],
    "d1-048": ["5.2"],
    "d1-049": ["2.3"],
    "d1-051": ["5.3"],
    "d1-052": ["5.3"],
    "d1-054": ["5.3"],
    "d1-056": ["2.3"],
    "d2-001": ["2.4"],
    "d2-042": ["2.1"],
    "d2-043": ["2.1", "2.4"],
    "d2-044": ["2.5"],
    "d3-041": ["3.4", "5.1"],
    "d3-042": ["3.6", "4.1"],
    "d3-043": ["3.2", "3.4"],
    "d3-050": ["1.2", "2.5", "3.2"],
    "d4-040": ["4.3", "5.5"],
    "d4-041": ["4.3", "4.4"],
    "d5-039": ["5.1", "5.2", "5.3"],
    "d5-040": ["5.1", "3.4"],
    "meta-001": ["exam-format"],
    "meta-002": ["exam-format"],
    "meta-003": ["scenarios"],
    "meta-004": ["cross-domain"],
}


def infer_tasks_from_sources(sources: list[str] | None) -> list[str]:
    tasks: set[str] = set()
    for src in sources or []:
        for m in RANGE_RE.finditer(src):
            d1, t1, d2, t2 = map(int, (m.group(1), m.group(2), m.group(3), m.group(4)))
            if d1 == d2:
                for t in range(t1, t2 + 1):
                    tasks.add(f"{d1}.{t}")
        for m in TASK_RE.finditer(src):
            tasks.add(f"{m.group(1)}.{m.group(2)}")
    return sorted(tasks, key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1])))


def sort_tasks(tasks: list[str]) -> list[str]:
    def key(t: str) -> tuple:
        if "." in t:
            a, b = t.split(".", 1)
            return (0, int(a), int(b))
        return (1, 0, t)

    return sorted(tasks, key=key)


def apply_tasks_to_card(card: dict) -> list[str]:
    cid = card["id"]
    if cid in MANUAL_TASKS:
        manual = MANUAL_TASKS[cid]
        inferred = infer_tasks_from_sources(card.get("sources"))
        merged = sort_tasks(list(set(manual + inferred)))
        return merged if merged else manual
    inferred = infer_tasks_from_sources(card.get("sources"))
    if inferred:
        return inferred
    domain = card.get("domain", "")
    if domain and domain.startswith("D") and domain[1:].isdigit():
        raise ValueError(f"{cid}: no tasks inferred and no manual mapping")
    return MANUAL_TASKS.get(cid, ["exam-format"])


def extract_header(text: str) -> str:
    lines = text.splitlines(keepends=True)
    header_lines: list[str] = []
    for line in lines:
        if line.startswith("#"):
            header_lines.append(line)
        elif header_lines and line.strip() == "":
            header_lines.append(line)
        elif header_lines:
            break
    return "".join(header_lines)


def main() -> int:
    errors: list[str] = []
    for path in sorted(DOMAINS_DIR.glob("*.yaml")):
        original = path.read_text(encoding="utf-8")
        header = extract_header(original)
        cards = yaml.safe_load(original)
        if not isinstance(cards, list):
            errors.append(f"{path}: expected list")
            continue
        for card in cards:
            try:
                card["tasks"] = apply_tasks_to_card(card)
            except ValueError as e:
                errors.append(str(e))
        dumped = yaml.dump(
            cards,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        )
        path.write_text(header + dumped, encoding="utf-8")
        print(f"Updated {path.name} ({len(cards)} cards)")

    if errors:
        print("Errors:")
        for e in errors:
            print(f"  - {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
