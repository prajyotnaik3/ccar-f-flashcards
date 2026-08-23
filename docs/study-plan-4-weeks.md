# CCAR-F 4-Week Study Plan

Study for **Claude Certified Architect – Foundations (CCAR-F)** using this repo’s flashcards. Expand cards from your **official Exam Guide** task statements (~5–10 new cards per day).

## Exam weights (allocate time accordingly)

| Domain | Weight | Starter cards in repo |
|--------|--------|------------------------|
| D1 Agentic Architecture & Orchestration | 27% | 6 |
| D3 Claude Code Configuration & Workflows | 20% | 5 |
| D4 Prompt Engineering & Structured Output | 20% | 5 |
| D2 Tool Design & MCP Integration | 18% | 5 |
| D5 Context Management & Reliability | 15% | 5 |
| Meta (exam format) | — | 4 |

**Target by exam day:** ~180–220 cards total.

## Daily rhythm (45–90 minutes)

1. **15 min** — Anki review (`dist/anki/ccar-f.apkg`)
2. **30–45 min** — Add 5–10 cards from one Exam Guide task statement
3. **15–30 min** — Hands-on build from Anthropic Academy / Exam Guide exercises

Run after adding cards:

```bash
pip install -r requirements.txt
python scripts/build_all.py
```

## Week 1 — D1 + foundations

| Day | Create cards | Review | Hands-on |
|-----|--------------|--------|----------|
| Mon | Read Exam Guide intro + all 6 scenarios | Meta cards | Skim scenario map |
| Tue–Thu | D1 task statements → ~15 cards | Anki daily | Small agent loop |
| Fri | D1 → ~15 more cards | Full D1 deck | Escalation path in support agent |
| Sat | Refine rationales | Scenario drill: support + multi-agent | — |
| Sun | Catch-up / weak cards | Web viewer shuffle | — |

## Week 2 — D3 + D4

| Day | Focus | Target |
|-----|-------|--------|
| Mon–Wed | D3 Claude Code | ~35 cards |
| Thu–Sat | D4 Structured output | ~35 cards |
| Sun | Scenarios: Code Generation + CI/CD | Timed 20-card drill |

**Hands-on:** `CLAUDE.md`, slash commands, JSON schema + validation-retry.

## Week 3 — D2 + D5 + publish

| Day | Focus | Target |
|-----|-------|--------|
| Mon–Wed | D2 MCP & tools | ~30 cards |
| Thu–Fri | D5 Context & reliability | ~25 cards |
| Sat | Push repo to GitHub, enable Pages | v0.1 public |
| Sun | Scenarios: Support, Multi-agent, Dev productivity | — |

**Hands-on:** MCP server with 2–3 scoped tools + structured errors.

## Week 4 — Integration + exam readiness

| Day | Activity |
|-----|----------|
| Mon–Tue | Mixed review all domains; tag `exam_day: true` on critical cards |
| Wed | Simulate 4-of-6 scenarios (pick 4, answer decision cards) |
| Thu | `docs/cheat-sheet.md` + weak-domain Anki cram |
| Fri | Timed mock (community resource, 60 Q / 120 min) |
| Sat | Light review only; no new cards |
| Sun | Exam day prep: meta cards + cheat sheet |

## Weekly checklist

- [ ] `python scripts/validate.py` passes
- [ ] `python scripts/build_all.py` run
- [ ] Anki import updated `.apkg`
- [ ] Git commit + push
- [ ] One scenario simulation completed
