# D4: Prompt Engineering & Structured Output

## d4-001 · concept · structured_extraction, ci_cd

**Q:** Why use structured output (JSON schema) with Claude instead of free-text parsing?

**A:** Enables validation, retries on schema failure, and downstream automation without fragile regex on prose.

**Tags:** structured_output

**Sources:**
- Official CCAR-F Exam Guide — D4
- https://docs.anthropic.com/en/docs/build-with-claude/structured-outputs

---

## d4-002 · decision · structured_extraction

**Q:** Extraction misses nullable fields intermittently. Best improvement?

**A:** Tighten schema (required vs optional), add validation-retry loop, and explicit examples for edge/null cases—not longer vague prompts alone.

**Tags:** validation, retry

**Sources:**
- Official CCAR-F Exam Guide — D4, Structured Extraction scenario

---

## d4-003 · anti_pattern · structured_extraction

**Q:** Why trust model self-reported 'confidence' without validation?

**A:** Confidence is not calibrated by default; use schema checks, cross-field rules, or human review thresholds for high-risk fields.

**Tags:** confidence, validation

**Sources:**
- Official CCAR-F Exam Guide — D4

---

## d4-004 · compare · ci_cd

**Q:** Prompt-only PR review checklist vs schema for review findings?

**A:** Schema for machine consumption (CI gates, dashboards); prompts alone are fine for human-readable narrative only.

**Tags:** ci_cd, structured_output

**Sources:**
- Official CCAR-F Exam Guide — D4, CI/CD scenario

---

## d4-005 · scenario_hook · structured_extraction

**Q:** Structured Data Extraction scenario—primary domains?

**A:** D4 (schemas, validation), D5 (reliability, human review for low confidence).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

