#!/usr/bin/env python3
"""Add rationale to decision cards missing the field."""

from __future__ import annotations

import re
from pathlib import Path

from ruamel.yaml import YAML

from card_loader import DOMAINS_DIR
from sample_q_rationales import SAMPLE_Q_RATIONALES

CARD_OVERRIDES: dict[str, str] = {
    "d1-002": (
        "Financial identity steps need deterministic enforcement; prompts and few-shot alone "
        "are probabilistic."
    ),
    "d2-003": (
        "Descriptions are the primary selection mechanism; few-shot and routing layers do not "
        "fix inadequate descriptions first."
    ),
}

STRUCTURAL_KEYWORDS = (
    "programmatic",
    "prerequisite",
    "hook",
    "deterministic",
    "PostToolUse",
    "interception",
    "tool_use",
    "JSON schema",
    "scoped",
    "least privilege",
    "-p ",
    "--print",
    "plan mode",
    ".claude/rules",
)


def sample_q_from_card(card: dict) -> int | None:
    for src in card.get("sources", []):
        m = re.search(r"Sample Q(\d+)", src)
        if m:
            return int(m.group(1))
    return None


def derive_rationale(card: dict) -> str:
    cid = card.get("id", "")
    if cid in CARD_OVERRIDES:
        return CARD_OVERRIDES[cid]

    sq = sample_q_from_card(card)
    if sq and sq in SAMPLE_Q_RATIONALES:
        return SAMPLE_Q_RATIONALES[sq]

    back = card.get("back", "").strip()
    front = card.get("front", "").lower()

    if "—" in back:
        tail = back.split("—", 1)[1].strip()
        if len(tail) >= 25:
            return tail

    if " not " in back.lower():
        idx = back.lower().index(" not ")
        snippet = back[idx:].strip()
        if len(snippet) <= 200:
            return f"Correct choice avoids the wrong pattern: {snippet}."

    combined = f"{front} {back.lower()}"
    if any(k.lower() in combined for k in STRUCTURAL_KEYWORDS):
        return (
            "Exam tests structural or configuration fixes over prompt-only approaches when "
            "reliability, security, or compliance matter."
        )

    if "escalat" in combined:
        return (
            "Escalation calibration needs explicit criteria—ambiguous boundaries cause wrong "
            "routing between autonomous resolution and human handoff."
        )

    if "mcp" in combined or "grep" in combined or "glob" in combined:
        return (
            "Tool choice follows capability fit: built-in tools for repo search, MCP for "
            "external systems—descriptions and scoping drive correct selection."
        )

    if "context" in combined or "compact" in combined or "scratchpad" in combined:
        return (
            "Context management trades completeness against window limits—preserve facts "
            "externally or summarize before long exploration phases."
        )

    if "batch" in combined or "latency" in combined:
        return (
            "Match API latency and cost to workflow: blocking paths need synchronous calls; "
            "overnight jobs can use batch savings."
        )

    if "review" in combined or "pass" in combined:
        return (
            "Multi-pass or independent review reduces attention dilution and self-review bias "
            "in large change sets."
        )

    if "schema" in combined or "nullable" in combined or "validation" in combined:
        return (
            "Structured output plus validation-retry separates syntax from semantics; schemas "
            "must reflect absent data, not force fabrication."
        )

    first_sentence = back.split(".")[0].strip()
    if len(first_sentence) >= 20:
        return f"Exam judgment aligned to task {card.get('tasks', ['?'])[0]}: {first_sentence}."

    return f"Best practice per Exam Guide task {card.get('tasks', ['?'])[0]}: {back[:160]}."


def main() -> int:
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.default_flow_style = False
    yaml.width = 1000

    updated = 0
    for path in sorted(DOMAINS_DIR.glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            cards = yaml.load(f)
        if not cards:
            continue

        file_updated = 0
        for card in cards:
            if card.get("type") != "decision":
                continue
            if card.get("rationale"):
                continue
            card["rationale"] = derive_rationale(card)
            file_updated += 1

        if file_updated:
            with open(path, "w", encoding="utf-8") as f:
                yaml.dump(cards, f)
            print(f"{path.name}: added {file_updated} rationales")
            updated += file_updated

    print(f"Total rationales added: {updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
