# D4: Prompt Engineering & Structured Output

## d4-001 · concept · structured_extraction, ci_cd

**Tasks:** 4.3

**Q:** Why use structured output (JSON schema) instead of parsing free-text responses?

**A:** Enables validation, automated retries on failure, and downstream automation without fragile regex on prose.

**Tags:** structured_output

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3
- https://docs.anthropic.com/en/docs/build-with-claude/structured-outputs

---

## d4-002 · compare · ci_cd

**Tasks:** 4.1

**Q:** Explicit review criteria vs vague instructions like 'be conservative'?

**A:** Specific categorical criteria (flag when comment contradicts code) beat vague confidence filtering for precision.

**Tags:** prompt_criteria, false_positives

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-003 · decision · ci_cd

**Tasks:** 4.1

**Q:** Automated review has high false positives in one category—developers ignore all findings. First response?

**A:** Temporarily disable the high false-positive category to restore trust while improving prompts for that category.

**Tags:** false_positives, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-004 · decision · ci_cd

**Tasks:** 4.1

**Q:** How define consistent severity levels in automated code review prompts?

**A:** Explicit severity criteria with concrete code examples for each level—not generic confidence thresholds.

**Tags:** severity, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-005 · concept · ci_cd

**Tasks:** 4.1

**Q:** Why high false-positive rates in one review category hurt the whole system?

**A:** Developers lose trust and dismiss accurate findings in other categories too.

**Tags:** false_positives, trust

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-006 · decision · ci_cd

**Tasks:** 4.1

**Q:** Review prompt design: report bugs/security vs skip minor style?

**A:** Define explicit categories to report versus skip—don't rely on confidence-based filtering alone.

**Tags:** review, prompt_criteria

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-007 · concept · structured_extraction, ci_cd

**Tasks:** 4.2

**Q:** When are few-shot examples most effective?

**A:** When detailed instructions alone produce inconsistent format or ambiguous-case handling—enables generalization to novel patterns.

**Tags:** few_shot

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-008 · decision · ci_cd

**Tasks:** 4.2

**Q:** Review output format inconsistent (location, severity, fix). Improvement?

**A:** Few-shot examples demonstrating exact desired format (location, issue, severity, suggested fix).

**Tags:** few_shot, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-009 · decision · ci_cd

**Tasks:** 4.2

**Q:** Reduce false positives while still catching real bugs in review?

**A:** Few-shot examples distinguishing acceptable local patterns from genuine issues—shows reasoning for each.

**Tags:** few_shot, false_positives

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-010 · decision · structured_extraction

**Tasks:** 4.2

**Q:** Extraction fails on varied document layouts (inline citations vs bibliographies). Fix?

**A:** Few-shot examples showing correct handling of each document structure variant.

**Tags:** few_shot, extraction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-011 · decision · structured_extraction

**Tasks:** 4.2

**Q:** Model returns null/empty for required fields on varied formats. Few-shot approach?

**A:** Examples demonstrating correct extraction from each format variant—not just schema tightening alone.

**Tags:** few_shot, extraction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-012 · decision · structured_extraction, ci_cd

**Tasks:** 4.2

**Q:** How many few-shot examples for ambiguous scenarios, and what show?

**A:** 2–4 targeted examples with reasoning for why one action was chosen over plausible alternatives.

**Tags:** few_shot

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-013 · concept · structured_extraction

**Tasks:** 4.3

**Q:** Most reliable approach for guaranteed schema-compliant JSON output?

**A:** tool_use with JSON schemas—eliminates JSON syntax errors vs free-text JSON generation.

**Tags:** tool_use, json_schema

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-014 · concept · structured_extraction

**Tasks:** 4.3, 4.4

**Q:** Strict JSON schemas via tool_use eliminate syntax errors—but what errors remain?

**A:** Semantic errors: wrong field values, line items not summing to total, values in incorrect fields.

**Tags:** validation, semantic_errors

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3–4.4

---

## d4-015 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Source document may omit a field. Schema design to prevent fabrication?

**A:** Make fields optional/nullable when information may be absent—don't require fields the source lacks.

**Tags:** schema_design, nullable

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-016 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Extensible category field in extraction schema—pattern?

**A:** Enum with "other" plus a detail string field for categories not in the predefined list.

**Tags:** schema_design, enum

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-017 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Ambiguous source data in extraction—enum design?

**A:** Add enum value like "unclear" for ambiguous cases rather than forcing a wrong category.

**Tags:** schema_design, enum

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-018 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Inconsistent date formats in source documents alongside strict schema?

**A:** Include format normalization rules in the prompt alongside the strict output schema.

**Tags:** schema_design, normalization

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-019 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Multiple extraction schemas; document type unknown at request time. tool_choice?

**A:** tool_choice: "any" to guarantee structured tool output instead of conversational text.

**Tags:** tool_choice, extraction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-020 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Where extract structured data from a tool_use extraction call?

**A:** From the tool_use response block—schema defines tool input parameters; model fills structured fields there.

**Tags:** tool_use, extraction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-021 · concept · structured_extraction

**Tasks:** 4.4

**Q:** What is retry-with-error-feedback for extraction?

**A:** On validation failure, send follow-up with original document, failed extraction, and specific validation errors for self-correction.

**Tags:** validation, retry

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-022 · compare · structured_extraction

**Tasks:** 4.4

**Q:** When will validation retries succeed vs fail?

**A:** Succeed on format/structural mismatches. Fail when required info is absent from source (or only in external doc not provided).

**Tags:** validation, retry

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-023 · compare · structured_extraction, ci_cd

**Tasks:** 4.4

**Q:** Schema syntax errors vs semantic validation errors?

**A:** Syntax errors eliminated by tool_use strict schemas; semantic errors need cross-field rules (totals, field placement).

**Tags:** validation, semantic_errors

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-024 · decision · ci_cd

**Tasks:** 4.4

**Q:** Developers dismiss many automated findings. Feedback loop design?

**A:** Add detected_pattern field to findings to analyze which constructs trigger false positives when dismissed.

**Tags:** feedback_loop, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-025 · decision · structured_extraction

**Tasks:** 4.4

**Q:** Self-correction for invoice totals that don't add up?

**A:** Extract calculated_total alongside stated_total and flag discrepancies; add conflict_detected for inconsistent source data.

**Tags:** validation, self_correction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-026 · decision · structured_extraction

**Tasks:** 4.3, 4.4

**Q:** Extraction misses nullable fields intermittently. Best improvement?

**A:** Tighten required vs optional schema, validation-retry loop, and explicit examples for null/edge cases.

**Tags:** validation, nullable

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3–4.4; Structured Extraction scenario

---

## d4-027 · concept · ci_cd, structured_extraction

**Tasks:** 4.5

**Q:** Message Batches API tradeoffs (cost, latency)?

**A:** 50% cost savings, up to 24-hour processing window, no guaranteed latency SLA.

**Tags:** batch_api

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5; Appendix

---

## d4-028 · decision · ci_cd

**Tasks:** 4.5

**Q:** Pre-merge blocking check vs overnight technical debt report—batch API for both?

**A:** Batch only for latency-tolerant jobs (overnight reports); keep synchronous API for blocking pre-merge checks.

**Tags:** batch_api, latency

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5; Sample Q11

---

## d4-029 · concept · structured_extraction

**Tasks:** 4.5

**Q:** Message Batches API limitation on tool calling?

**A:** No multi-turn tool calling within a single batch request—cannot execute tools mid-request and return results.

**Tags:** batch_api, tool_use

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-030 · concept · structured_extraction

**Tasks:** 4.5

**Q:** custom_id in Message Batches API—purpose?

**A:** Correlate batch request/response pairs and identify failed documents for resubmission.

**Tags:** batch_api, custom_id

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-031 · decision · structured_extraction

**Tasks:** 4.5

**Q:** Batch job failures—resubmission strategy?

**A:** Resubmit only failed documents by custom_id with modifications (e.g., chunk oversized docs that exceeded context).

**Tags:** batch_api, failures

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-032 · decision · structured_extraction

**Tasks:** 4.5

**Q:** Before batch-processing 10,000 documents—cost reduction step?

**A:** Refine prompts on a sample set first to maximize first-pass success and reduce resubmission costs.

**Tags:** batch_api, prompt_refinement

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-033 · concept · structured_extraction

**Tasks:** 4.6

**Q:** Why self-review of generated code in the same session is limited?

**A:** Model retains generation reasoning context—less likely to question its own decisions than an independent reviewer.

**Tags:** self_review, multi_instance

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## d4-034 · decision · ci_cd

**Tasks:** 4.6

**Q:** Best approach to catch subtle issues in AI-generated code?

**A:** Second independent Claude instance reviewing without the generator's reasoning context.

**Tags:** multi_instance, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## d4-035 · decision · ci_cd

**Tasks:** 4.6

**Q:** Large multi-file PR review—multi-pass architecture?

**A:** Per-file passes for local issues plus separate integration pass for cross-file data flow.

**Tags:** multi_pass, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6; Sample Q12

---

## d4-036 · decision · ci_cd

**Tasks:** 4.6

**Q:** Route review findings to human triage by severity—schema approach?

**A:** Verification pass where model reports confidence alongside each finding for calibrated routing.

**Tags:** review, confidence

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## d4-037 · compare · ci_cd, structured_extraction

**Tasks:** 4.3

**Q:** Prompt-only PR findings vs JSON schema for CI gates?

**A:** Schema for machine consumption (CI gates, dashboards); prompts alone only for human-readable narrative.

**Tags:** structured_output, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3; CI/CD scenario

---

## d4-038 · anti_pattern · structured_extraction

**Tasks:** 4.4

**Q:** Why trust model self-reported confidence without validation?

**A:** Not calibrated by default—use schema checks, cross-field rules, or human review thresholds for high-risk fields.

**Tags:** confidence, validation

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4; D5 crossover

---

## d4-039 · anti_pattern · ci_cd

**Tasks:** 4.6

**Q:** Run three full PR review passes and only flag issues in 2+ passes. Why wrong?

**A:** Suppresses real bugs caught intermittently—consensus filtering hides attention-dilution problems; split passes instead.

**Tags:** multi_pass, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6; Sample Q12

---

## d4-040 · scenario_hook · structured_extraction

**Tasks:** 4.3, 5.5

**Q:** Structured Data Extraction scenario (Scenario 6)—primary domains?

**A:** D4 (schemas, validation, batch) and D5 (reliability, human review for low confidence).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d4-041 · scenario_hook · ci_cd

**Tasks:** 4.3, 4.4

**Q:** Scenario 6 extraction system requirements from the exam guide?

**A:** Extract from unstructured docs, validate with JSON schemas, handle edge cases, integrate with downstream systems.

**Tags:** scenarios, extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6

---

## d4-042 · concept · structured_extraction

**Tasks:** 4.2

**Q:** Few-shot examples reduce hallucination in extraction—example use cases?

**A:** Informal measurements, varied document structures, and inconsistent field formats in source documents.

**Tags:** few_shot, hallucination

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-043 · anti_pattern · ci_cd

**Tasks:** 4.5

**Q:** Switch blocking pre-merge checks to batch API with status polling. Why wrong?

**A:** Batch has no latency SLA—unacceptable for workflows where developers wait to merge.

**Tags:** batch_api, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5; Sample Q11

---

## d4-044 · decision · structured_extraction

**Tasks:** 4.5

**Q:** 30-hour SLA with 24-hour max batch processing—submission frequency?

**A:** Calculate submission windows (e.g., 4-hour intervals) so batches complete within SLA with margin for retries.

**Tags:** batch_api, sla

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-045 · concept · ci_cd, structured_extraction

**Tasks:** 4.6

**Q:** Independent review instances vs extended thinking for self-review?

**A:** Independent instances without generator context catch more subtle issues than self-review instructions or extended thinking alone.

**Tags:** multi_instance, self_review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## d4-046 · concept · ci_cd

**Tasks:** 4.1

**Q:** Explicit review criteria example—comments vs code?

**A:** Flag comments only when claimed behavior contradicts actual code—not vague 'check comment accuracy'.

**Tags:** prompt_criteria, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-047 · concept · ci_cd, structured_extraction

**Tasks:** 4.2

**Q:** How few-shot examples generalize beyond pre-specified cases?

**A:** Demonstrate judgment and reasoning on ambiguous examples so the model applies similar logic to novel patterns.

**Tags:** few_shot, generalization

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-048 · decision · ci_cd

**Tasks:** 4.2

**Q:** Few-shot use case: branch-level test coverage gaps?

**A:** Show how to identify and report coverage gaps at branch level—ambiguous case requiring demonstrated judgment.

**Tags:** few_shot, testing

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-049 · anti_pattern · ci_cd

**Tasks:** 4.5

**Q:** Switch both blocking and overnight jobs to batch API with real-time fallback. Why over-engineered?

**A:** Match API to latency needs—sync for blocking checks, batch for overnight; fallback adds unnecessary complexity.

**Tags:** batch_api, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5; Sample Q11

---

## d4-050 · anti_pattern · ci_cd

**Tasks:** 4.6

**Q:** Large PR review: switch to higher-tier model with larger context window. Why insufficient?

**A:** Larger context doesn't fix attention dilution—split into per-file plus integration passes instead.

**Tags:** multi_pass, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6; Sample Q12

