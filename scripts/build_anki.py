#!/usr/bin/env python3
"""Export YAML flashcards to Anki .apkg via genanki."""

from __future__ import annotations

import genanki

from card_loader import ROOT, domain_label, load_cards

OUT_DIR = ROOT / "dist" / "anki"
DECK_ID_BASE = 1607392319


def make_deck_id(suffix: int) -> int:
    return DECK_ID_BASE + suffix


def card_fields(card: dict) -> tuple[str, str]:
    scenarios = ", ".join(card.get("scenarios", []))
    tags_line = ", ".join(card.get("tags", []))
    tasks_line = ", ".join(card.get("tasks", []))
    sources = "\n".join(f"• {s}" for s in card.get("sources", []))
    front = card["front"]
    back_parts = [card["back"]]
    if card.get("rationale"):
        back_parts.append(f"\n\nWhy: {card['rationale']}")
    if tasks_line:
        back_parts.append(f"\n\nTasks: {tasks_line}")
    if tags_line:
        back_parts.append(f"\n\nTags: {tags_line}")
    if scenarios:
        back_parts.append(f"\n\nScenarios: {scenarios}")
    if sources:
        back_parts.append(f"\n\nSources:\n{sources}")
    return front, "\n".join(back_parts)


def anki_tags(card: dict) -> list[str]:
    tags = list(card.get("tags", [])) + [card["domain"], card["type"]]
    for task in card.get("tasks", []):
        tags.append(f"task_{task.replace('.', '_')}")
    return tags


def main() -> None:
    cards = load_cards()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    model = genanki.Model(
        make_deck_id(0),
        "CCAR-F Flashcard",
        fields=[
            {"name": "Front"},
            {"name": "Back"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": "{{Front}}",
                "afmt": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}",
            }
        ],
    )

    by_domain: dict[str, list[dict]] = {}
    for card in cards:
        by_domain.setdefault(card["domain"], []).append(card)

    decks: list[genanki.Deck] = []
    suffix = 1
    for domain, domain_cards in sorted(by_domain.items()):
        deck_name = f"CCAR-F::{domain} {domain_label(domain)}"
        deck = genanki.Deck(make_deck_id(suffix), deck_name)
        suffix += 1
        for card in domain_cards:
            front, back = card_fields(card)
            note = genanki.Note(
                model=model,
                fields=[front, back],
                tags=anki_tags(card),
            )
            deck.add_note(note)
        decks.append(deck)
        print(f"Deck {deck_name}: {len(domain_cards)} notes")

    mixed = genanki.Deck(make_deck_id(99), "CCAR-F::Mixed (All)")
    for card in cards:
        front, back = card_fields(card)
        note = genanki.Note(
            model=model,
            fields=[front, back],
            tags=anki_tags(card),
        )
        mixed.add_note(note)
    decks.append(mixed)

    out_path = OUT_DIR / "ccar-f.apkg"
    package = genanki.Package(decks)
    package.write_to_file(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
