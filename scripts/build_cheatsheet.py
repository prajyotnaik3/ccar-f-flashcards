#!/usr/bin/env python3
"""Build exam-day cheat sheet from cards tagged exam_day."""

from __future__ import annotations

from card_loader import ROOT, load_cards

OUT = ROOT / "docs" / "cheat-sheet.md"


def main() -> None:
    cards = [c for c in load_cards() if c.get("exam_day")]
    lines = [
        "# CCAR-F Exam-Day Cheat Sheet",
        "",
        "Auto-generated from flashcards with `exam_day: true`.",
        "",
        f"**{len(cards)} cards** — review the night before the exam.",
        "",
    ]
    for card in cards:
        lines.append(f"### {card['id']} ({card['domain']})")
        lines.append("")
        lines.append(f"- **Q:** {card['front']}")
        lines.append(f"- **A:** {card['back']}")
        if card.get("rationale"):
            lines.append(f"- **Why:** {card['rationale']}")
        lines.append("")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(cards)} cards)")


if __name__ == "__main__":
    main()
