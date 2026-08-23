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
        if card.get("type") == "scenario_chain" and not card.get("chain"):
            errors.append(f"{cid}: scenario_chain requires chain metadata")
        chain = card.get("chain")
        if chain and chain.get("step", 0) > chain.get("steps", 0):
            errors.append(f"{cid}: chain.step exceeds chain.steps")

    if errors:
        print("Validation failed:\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    _print_task_coverage(cards)
    print(f"OK: {len(cards)} cards validated, {len(ids)} unique ids")
    return 0


def _print_task_coverage(cards: list[dict]) -> None:
    """Report flashcard count per Exam Guide task statement."""
    from collections import Counter

    counts: Counter[str] = Counter()
    for card in cards:
        for task in card.get("tasks", []):
            counts[task] += 1

    expected = (
        [f"1.{t}" for t in range(1, 8)]
        + [f"2.{t}" for t in range(1, 6)]
        + [f"3.{t}" for t in range(1, 7)]
        + [f"4.{t}" for t in range(1, 7)]
        + [f"5.{t}" for t in range(1, 7)]
    )
    thin = [t for t in expected if counts.get(t, 0) < 2]
    if thin:
        print(f"Note: tasks with fewer than 2 cards: {', '.join(thin)}")


if __name__ == "__main__":
    sys.exit(main())
