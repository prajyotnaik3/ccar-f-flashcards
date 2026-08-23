# Contributing

Thank you for helping improve CCAR-F study materials.

## The one hard rule

**No real or leaked exam content, ever.**

Do not add:

- Questions from the live Pearson VUE exam
- Content from exam takers describing specific exam items
- Screenshots or transcripts of proctored sessions

Do add:

- Concepts from the **official CCAR-F Exam Guide** task statements
- Decision patterns and rationales in your own words
- Facts from public Anthropic documentation with links

## Card quality checklist

Each flashcard in `flashcards/domains/*.yaml` must have:

- Unique `id` (e.g. `d1-001`)
- `domain` (D1–D5), `type`, `front`, `back`
- At least one `sources` entry
- Valid `scenarios` tags when applicable

Run validation before submitting:

```bash
python scripts/validate.py
```

## Pull requests

1. Fork and branch from `main`
2. Add or edit YAML cards only (do not hand-edit `dist/` outputs)
3. Run `python scripts/build_all.py`
4. Describe what domain/scenario you expanded
