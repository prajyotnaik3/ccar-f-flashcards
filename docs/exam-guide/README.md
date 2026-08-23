# Official CCAR-F Exam Guide (local copy)

The **authoritative** exam guide is published by Anthropic. This repo does **not** commit the PDF to git (keeps the repo lightweight and points you to the latest revision from Academy).

## Download (canonical)

1. [Anthropic Partner Academy — Foundations certification](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification)
2. Click **Download the exam guide**

Direct PDF (may be updated by Anthropic):

[Official CCAR-F Exam Guide (PDF)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf)

Always prefer the file linked from Academy so your copy matches the current exam version.

## Optional local copy in this project

Place the PDF here for side-by-side study with flashcards (file is **gitignored**):

```text
docs/exam-guide/CCAR-F-Exam-Guide.pdf
```

Or run:

```bash
./scripts/setup_exam_guide.sh
```

That script copies from `~/Downloads/` if the guide PDF is there.

## Better way to consume the guide with this repo

| Step | What to use |
|------|-------------|
| 1. Orient | [exam-guide-index.md](../exam-guide-index.md) — section map + task → flashcard links |
| 2. Read | Official PDF sections 4–6 (scenarios + task statements) |
| 3. Recall | [Web viewer](https://prajyotnaik3.github.io/ccar-f-flashcards/) or Anki — filter by domain/scenario |
| 4. Practice | PDF Section 8 exercises + Section 9 sample question **rationales** |
| 5. Exam day | `docs/cheat-sheet.md` (built from `exam_day` cards) |

**Web study hub:** [study.html](https://prajyotnaik3.github.io/ccar-f-flashcards/study.html) — links to PDF, task index, and filtered card decks.

## License note

The Exam Guide is Anthropic’s material. This project links to it and maps study cards to its public blueprint; it does not replace reading the full guide.
