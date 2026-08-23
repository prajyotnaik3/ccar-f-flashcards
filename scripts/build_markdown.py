#!/usr/bin/env python3
"""Export YAML flashcards to Markdown files per domain."""

from __future__ import annotations

from pathlib import Path

from card_loader import DOMAINS_DIR, ROOT, domain_label, load_cards

OUT_DIR = ROOT / "dist" / "markdown"


def card_to_markdown(card: dict) -> str:
    scenarios = ", ".join(card.get("scenarios", []))
    tags = ", ".join(card.get("tags", []))
    tasks = ", ".join(card.get("tasks", []))
    lines = [
        f"## {card['id']} · {card['type']} · {scenarios}",
        "",
        f"**Tasks:** {tasks}",
        "",
        f"**Q:** {card['front']}",
        "",
        f"**A:** {card['back']}",
    ]
    if card.get("rationale"):
        lines.extend(["", f"**Why:** {card['rationale']}"])
    if tags:
        lines.extend(["", f"**Tags:** {tags}"])
    sources = card.get("sources", [])
    if sources:
        lines.extend(["", "**Sources:**"])
        for s in sources:
            lines.append(f"- {s}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    cards = load_cards()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    by_domain: dict[str, list[dict]] = {}
    for card in cards:
        by_domain.setdefault(card["domain"], []).append(card)

    for domain, domain_cards in sorted(by_domain.items()):
        slug = {
            "D1": "d1-agentic-architecture",
            "D2": "d2-tool-design-mcp",
            "D3": "d3-claude-code",
            "D4": "d4-prompt-structured-output",
            "D5": "d5-context-reliability",
            "META": "meta",
        }.get(domain, domain.lower())
        path = OUT_DIR / f"{slug}.md"
        header = f"# {domain}: {domain_label(domain)}\n\n"
        body = "\n---\n\n".join(card_to_markdown(c) for c in domain_cards)
        path.write_text(header + body + "\n", encoding="utf-8")
        print(f"Wrote {path} ({len(domain_cards)} cards)")

    # Combined deck
    all_path = OUT_DIR / "all-flashcards.md"
    all_body = "\n---\n\n".join(card_to_markdown(c) for c in cards)
    all_path.write_text("# CCAR-F Flashcards (All)\n\n" + all_body + "\n", encoding="utf-8")
    print(f"Wrote {all_path} ({len(cards)} cards)")


if __name__ == "__main__":
    main()
