#!/usr/bin/env python3
"""Generate docs/task-coverage.md — flashcard counts per Exam Guide task."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from card_loader import ROOT, load_cards

OUT = ROOT / "docs" / "task-coverage.md"

TASK_LABELS = {
    "1.1": "Agentic loops and stop_reason",
    "1.2": "Coordinator–subagent orchestration",
    "1.3": "Subagent invocation and context passing",
    "1.4": "Workflow enforcement and handoffs",
    "1.5": "Agent SDK hooks",
    "1.6": "Task decomposition strategies",
    "1.7": "Session state, resume, fork",
    "2.1": "Tool descriptions and boundaries",
    "2.2": "Structured MCP error responses",
    "2.3": "Tool distribution and tool_choice",
    "2.4": "MCP server integration",
    "2.5": "Built-in tools (Grep, Glob, Read, etc.)",
    "3.1": "CLAUDE.md hierarchy and rules",
    "3.2": "Slash commands and skills",
    "3.3": "Path-specific rules",
    "3.4": "Plan mode vs direct execution",
    "3.5": "Iterative refinement",
    "3.6": "Claude Code in CI/CD",
    "4.1": "Explicit criteria, false positives",
    "4.2": "Few-shot prompting",
    "4.3": "tool_use and JSON schemas",
    "4.4": "Validation-retry loops",
    "4.5": "Message Batches API",
    "4.6": "Multi-instance and multi-pass review",
    "5.1": "Conversation context preservation",
    "5.2": "Escalation and ambiguity",
    "5.3": "Error propagation",
    "5.4": "Large codebase exploration",
    "5.5": "Human review workflows",
    "5.6": "Provenance and synthesis",
}


def main() -> None:
    cards = load_cards()
    counts: Counter[str] = Counter()
    for card in cards:
        for task in card.get("tasks", []):
            counts[task] += 1

    lines = [
        "# Task coverage",
        "",
        "Flashcard count per **Exam Guide** task statement. Filter in the "
        "[web viewer](https://prajyotnaik3.github.io/ccar-f-flashcards/?task=1.1) "
        "with the Task dropdown or `?task=1.4`.",
        "",
        "| Task | Topic | Cards | Viewer |",
        "|------|--------|-------|--------|",
    ]

    for d in range(1, 6):
        for t in range(1, 8):
            tid = f"{d}.{t}"
            if tid not in TASK_LABELS:
                continue
            n = counts.get(tid, 0)
            label = TASK_LABELS[tid]
            link = f"[filter](https://prajyotnaik3.github.io/ccar-f-flashcards/?task={tid})"
            lines.append(f"| **{tid}** | {label} | {n} | {link} |")

    lines.extend(
        [
            "",
            "## Meta keys",
            "",
            "| Key | Cards |",
            "|-----|-------|",
        ]
    )
    for key in ["exam-format", "scenarios", "cross-domain"]:
        lines.append(f"| {key} | {counts.get(key, 0)} |")

    lines.append("")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
