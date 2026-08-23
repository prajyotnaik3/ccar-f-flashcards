#!/usr/bin/env python3
"""Export flashcards to JSON for the web viewer."""

from __future__ import annotations

import json
from pathlib import Path

from card_loader import ROOT, load_cards

OUT_WEB = ROOT / "web" / "cards.json"
OUT_DIST = ROOT / "dist" / "cards.json"


def main() -> None:
    cards = load_cards()
    payload = {"count": len(cards), "cards": cards}
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    OUT_WEB.write_text(text, encoding="utf-8")
    OUT_DIST.parent.mkdir(parents=True, exist_ok=True)
    OUT_DIST.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT_WEB} and {OUT_DIST} ({len(cards)} cards)")


if __name__ == "__main__":
    main()
