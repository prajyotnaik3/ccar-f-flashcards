# CCAR-F Flashcards

Unofficial flashcards for **Claude Certified Architect – Foundations (CCAR-F)**. One YAML source generates:

- **Markdown** — read on GitHub or in VS Code (`dist/markdown/`)
- **Anki** — spaced repetition (`dist/anki/ccar-f.apkg`)
- **Web viewer** — flip cards on GitHub Pages (`web/`)

> **Disclaimer:** Not affiliated with or endorsed by Anthropic. No leaked exam content. Study from the [official Exam Guide](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf) and public Anthropic docs.

## Quick start

```bash
cd ccar-f-flashcards
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/build_all.py
```

- Import **`dist/anki/ccar-f.apkg`** into Anki (File → Import)
- Open **`dist/markdown/all-flashcards.md`** for reading
- Serve web locally: `cd web && python -m http.server 8080` → http://localhost:8080

## 4-week plan

See [docs/study-plan-4-weeks.md](docs/study-plan-4-weeks.md).

| Week | Focus |
|------|--------|
| 1 | D1 Agentic Architecture (27%) |
| 2 | D3 Claude Code + D4 Prompts (40%) |
| 3 | D2 MCP + D5 Context; publish repo |
| 4 | Scenario drills + exam readiness |

## Add flashcards

Edit YAML in `flashcards/domains/`. Each card needs `id`, `domain`, `type`, `front`, `back`, `sources`.

```yaml
- id: d1-007
  domain: D1
  type: decision
  scenarios: [customer_support]
  front: "Your question here"
  back: "Best answer / pattern"
  rationale: "Why this beats alternatives"
  sources:
    - "Official CCAR-F Exam Guide — D1 task X"
  tags: [escalation]
  exam_day: true   # optional: include on cheat sheet
```

Then run `python scripts/build_all.py`.

## Repository layout

```
flashcards/domains/*.yaml   # source of truth
scripts/                    # validate + build
dist/                       # generated markdown, anki, json
web/                        # GitHub Pages flip viewer
docs/                       # study plan, scenarios, sources
```

## Publish on GitHub

1. Create a new repository on GitHub (e.g. `ccar-f-flashcards`)
2. Push this folder:

```bash
git remote add origin https://github.com/YOUR_USER/ccar-f-flashcards.git
git push -u origin main
```

3. **Settings → Pages → Build and deployment:** Source = **GitHub Actions**
4. After CI runs, your viewer is at `https://YOUR_USER.github.io/ccar-f-flashcards/`

## Exam facts (CCAR-F)

| Item | Value |
|------|--------|
| Questions | 60 scenario-based |
| Scenarios | 4 of 6 per exam |
| Time | 120 minutes |
| Pass score | 720 / 1000 (scaled) |
| Fee | $125 USD (partner pricing may vary) |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). No real exam questions.

## License

MIT — see [LICENSE](LICENSE).
