"""Shared utilities for loading and validating CCAR-F flashcards."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "flashcards" / "domains"
SCHEMA_PATH = ROOT / "flashcards" / "schema.json"


def load_schema() -> dict:
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_cards() -> list[dict]:
    cards: list[dict] = []
    for path in sorted(DOMAINS_DIR.glob("*.yaml")):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not data:
            continue
        if not isinstance(data, list):
            raise ValueError(f"{path}: expected a list of cards")
        cards.extend(data)
    return cards


def domain_label(domain: str) -> str:
    labels = {
        "D1": "Agentic Architecture & Orchestration",
        "D2": "Tool Design & MCP Integration",
        "D3": "Claude Code Configuration & Workflows",
        "D4": "Prompt Engineering & Structured Output",
        "D5": "Context Management & Reliability",
        "META": "Exam Meta",
        "CHAIN": "Scenario Chains",
    }
    return labels.get(domain, domain)
