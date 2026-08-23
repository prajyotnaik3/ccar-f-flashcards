#!/usr/bin/env python3
"""Validate all flashcard YAML files against JSON Schema."""

from __future__ import annotations

import sys

from jsonschema import Draft202012Validator

from card_loader import load_cards, load_schema


def main() -> int:
    schema = load_schema()
    validator = Draft202012Validator(schema)
    cards = load_cards()
    ids: set[str] = set()
    errors: list[str] = []

    for i, card in enumerate(cards):
        for err in validator.iter_errors(card):
            errors.append(f"Card index {i} ({card.get('id', '?')}): {err.message}")
        cid = card.get("id")
        if cid in ids:
            errors.append(f"Duplicate id: {cid}")
        ids.add(cid)

    if errors:
        print("Validation failed:\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {len(cards)} cards validated, {len(ids)} unique ids")
    return 0


if __name__ == "__main__":
    sys.exit(main())
