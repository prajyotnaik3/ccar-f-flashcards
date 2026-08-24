# D4: Prompt Engineering & Structured Output

## d4-001 · concept · structured_extraction, ci_cd

**Tasks:** 4.3

**Q:** Why should you use structured output (JSON schema) instead of parsing free-text responses?

**A:** Enables validation, automated retries on failure, and downstream automation without fragile regex on prose.

**Tags:** structured_output

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3
- https://docs.anthropic.com/en/docs/build-with-claude/structured-outputs

---

## d4-002 · compare · ci_cd

**Tasks:** 4.1

**Q:** Why are explicit review criteria better than vague instructions like 'be conservative'?

**A:** Specific categorical criteria (flag when comment contradicts code) beat vague confidence filtering for precision.

**Tags:** prompt_criteria, false_positives

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-003 · decision · ci_cd

**Tasks:** 4.1

**Q:** Automated review has high false positives in one category, and developers ignore all findings. What should you do first?

**A:** Temporarily disable the high false-positive category to restore trust while improving prompts for that category.

**Why:** High false positives in one category destroy trust in every category. Disable that category while you tighten its prompt, then turn it back on.

**Tags:** false_positives, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-004 · decision · ci_cd

**Tasks:** 4.1

**Q:** How do you define consistent severity levels in automated code review prompts?

**A:** Explicit severity criteria with concrete code examples for each level—not generic confidence thresholds.

**Why:** not generic confidence thresholds.

**Tags:** severity, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-005 · concept · ci_cd

**Tasks:** 4.1

**Q:** Why do high false-positive rates in one review category hurt the whole system?

**A:** Developers lose trust and dismiss accurate findings in other categories too.

**Tags:** false_positives, trust

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-006 · decision · ci_cd

**Tasks:** 4.1

**Q:** How should a review prompt distinguish bugs and security issues from minor style nits?

**A:** Define explicit categories to report versus skip—don't rely on confidence-based filtering alone.

**Why:** don't rely on confidence-based filtering alone.

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

**Q:** Review output format is inconsistent (location, severity, fix). How should you improve it?

**A:** Few-shot examples demonstrating exact desired format (location, issue, severity, suggested fix).

**Why:** Few-shot examples of the exact format (location, issue, severity, suggested fix) beat more prose instructions when structure is inconsistent.

**Tags:** few_shot, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-009 · decision · ci_cd

**Tasks:** 4.2

**Q:** How do you reduce false positives in review while still catching real bugs?

**A:** Few-shot examples distinguishing acceptable local patterns from genuine issues—shows reasoning for each.

**Why:** shows reasoning for each.

**Tags:** few_shot, false_positives

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-010 · decision · structured_extraction

**Tasks:** 4.2

**Q:** Extraction fails on varied document layouts (inline citations versus bibliographies). How do you fix that?

**A:** Few-shot examples showing correct handling of each document structure variant.

**Why:** Exam judgment aligned to task 4.2: Few-shot examples showing correct handling of each document structure variant.

**Tags:** few_shot, extraction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-011 · decision · structured_extraction

**Tasks:** 4.2

**Q:** The model returns null or empty required fields on varied formats. What few-shot approach should you use?

**A:** Examples demonstrating correct extraction from each format variant—not just schema tightening alone.

**Why:** not just schema tightening alone.

**Tags:** few_shot, extraction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-012 · decision · structured_extraction, ci_cd

**Tasks:** 4.2

**Q:** How many few-shot examples should you use for ambiguous scenarios, and what should they show?

**A:** 2–4 targeted examples with reasoning for why one action was chosen over plausible alternatives.

**Why:** Exam judgment aligned to task 4.2: 2–4 targeted examples with reasoning for why one action was chosen over plausible alternatives.

**Tags:** few_shot

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-013 · concept · structured_extraction

**Tasks:** 4.3

**Q:** What is the most reliable approach for guaranteed schema-compliant JSON output?

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

**Q:** The source document may omit a field. How should you design the schema to prevent fabrication?

**A:** Make fields optional/nullable when information may be absent—don't require fields the source lacks.

**Why:** don't require fields the source lacks.

**Tags:** schema_design, nullable

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-016 · decision · structured_extraction

**Tasks:** 4.3

**Q:** What schema pattern should you use for an extensible category field?

**A:** Enum with "other" plus a detail string field for categories not in the predefined list.

**Why:** Use an enum plus an 'other' value and a detail string so unknown categories are captured instead of forced into a wrong bucket.

**Tags:** schema_design, enum

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-017 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Source data can be ambiguous. How should you design the extraction enum?

**A:** Add enum value like "unclear" for ambiguous cases rather than forcing a wrong category.

**Why:** Exam judgment aligned to task 4.3: Add enum value like "unclear" for ambiguous cases rather than forcing a wrong category.

**Tags:** schema_design, enum

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-018 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Source documents have inconsistent date formats, but the output schema is strict. What should you do?

**A:** Include format normalization rules in the prompt alongside the strict output schema.

**Why:** Keep the output schema strict, and put date-normalization rules in the prompt so inconsistent source formats still map to one output shape.

**Tags:** schema_design, normalization

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-019 · decision · structured_extraction

**Tasks:** 4.3

**Q:** You have multiple extraction schemas and the document type is unknown at request time. How should you set tool_choice?

**A:** tool_choice: "any" to guarantee structured tool output instead of conversational text.

**Why:** tool_choice "any" guarantees a tool call when several extraction schemas exist and the document type is unknown—auto may return chat text instead.

**Tags:** tool_choice, extraction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## d4-020 · decision · structured_extraction

**Tasks:** 4.3

**Q:** Where do you extract structured data from a tool_use extraction call?

**A:** From the tool_use response block—schema defines tool input parameters; model fills structured fields there.

**Why:** schema defines tool input parameters; model fills structured fields there.

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

**Q:** When do validation retries succeed, and when do they fail?

**A:** Succeed on format/structural mismatches. Fail when required info is absent from source (or only in external doc not provided).

**Tags:** validation, retry

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-023 · compare · structured_extraction, ci_cd

**Tasks:** 4.4

**Q:** How do schema syntax errors differ from semantic validation errors?

**A:** Syntax errors eliminated by tool_use strict schemas; semantic errors need cross-field rules (totals, field placement).

**Tags:** validation, semantic_errors

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-024 · decision · ci_cd

**Tasks:** 4.4

**Q:** Developers dismiss many automated findings. How should you design the feedback loop?

**A:** Add detected_pattern field to findings to analyze which constructs trigger false positives when dismissed.

**Why:** Exam judgment aligned to task 4.4: Add detected_pattern field to findings to analyze which constructs trigger false positives when dismissed.

**Tags:** feedback_loop, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-025 · decision · structured_extraction

**Tasks:** 4.4

**Q:** How should extraction self-correct when invoice totals do not add up?

**A:** Extract calculated_total alongside stated_total and flag discrepancies; add conflict_detected for inconsistent source data.

**Why:** Exam judgment aligned to task 4.4: Extract calculated_total alongside stated_total and flag discrepancies; add conflict_detected for inconsistent source data.

**Tags:** validation, self_correction

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## d4-026 · decision · structured_extraction

**Tasks:** 4.3, 4.4

**Q:** Extraction misses nullable fields intermittently. What is the best improvement?

**A:** Tighten required vs optional schema, validation-retry loop, and explicit examples for null/edge cases.

**Why:** Mark truly optional fields nullable, retry with validation errors, and add few-shot null/edge examples. Tightening every field to required causes fabrication.

**Tags:** validation, nullable

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3–4.4; Structured Extraction scenario

---

## d4-027 · concept · ci_cd, structured_extraction

**Tasks:** 4.5

**Q:** What are the cost and latency tradeoffs of the Message Batches API?

**A:** 50% cost savings, up to 24-hour processing window, no guaranteed latency SLA.

**Tags:** batch_api

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5; Appendix

---

## d4-028 · decision · ci_cd

**Tasks:** 4.5

**Q:** Should you use the Batch API for both a pre-merge blocking check and an overnight technical-debt report?

**A:** Batch only for latency-tolerant jobs (overnight reports); keep synchronous API for blocking pre-merge checks.

**Why:** Message Batches save cost but lack latency SLA—fine for overnight reports, unsuitable for blocking pre-merge checks. Polling batches for merge gates is unacceptable; custom_id correlates batch results; timeout fallback adds complexity vs matching API to workflow latency needs.

**Tags:** batch_api, latency

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5; Sample Q11

---

## d4-029 · concept · structured_extraction

**Tasks:** 4.5

**Q:** What is the Message Batches API limitation on tool calling?

**A:** No multi-turn tool calling within a single batch request—cannot execute tools mid-request and return results.

**Tags:** batch_api, tool_use

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-030 · concept · structured_extraction

**Tasks:** 4.5

**Q:** What is the purpose of custom_id in the Message Batches API?

**A:** Correlate batch request/response pairs and identify failed documents for resubmission.

**Tags:** batch_api, custom_id

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-031 · decision · structured_extraction

**Tasks:** 4.5

**Q:** How should you resubmit failed documents from a batch job?

**A:** Resubmit only failed documents by custom_id with modifications (e.g., chunk oversized docs that exceeded context).

**Why:** Resubmit only failed custom_id items, with fixes such as chunking docs that exceeded context. Do not resubmit the whole batch.

**Tags:** batch_api, failures

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-032 · decision · structured_extraction

**Tasks:** 4.5

**Q:** Before batch-processing 10,000 documents, what cost-reduction step should you take first?

**A:** Refine prompts on a sample set first to maximize first-pass success and reduce resubmission costs.

**Why:** Refine prompts on a sample before 10k documents so first-pass success is high and you avoid expensive resubmission loops.

**Tags:** batch_api, prompt_refinement

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-033 · concept · structured_extraction

**Tasks:** 4.6

**Q:** Why is self-review of generated code in the same session limited?

**A:** Model retains generation reasoning context—less likely to question its own decisions than an independent reviewer.

**Tags:** self_review, multi_instance

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## d4-034 · decision · ci_cd

**Tasks:** 4.6

**Q:** What is the best approach to catch subtle issues in AI-generated code?

**A:** Second independent Claude instance reviewing without the generator's reasoning context.

**Why:** A second Claude instance without the generator's reasoning context catches subtle bugs better than same-session self-review or extended thinking alone.

**Tags:** multi_instance, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## d4-035 · decision · ci_cd

**Tasks:** 4.6

**Q:** For a large multi-file PR review, what multi-pass architecture should you use?

**A:** Per-file passes for local issues plus separate integration pass for cross-file data flow.

**Why:** Split reviews into per-file passes plus a cross-file integration pass—fixes attention dilution across many files. Splitting PRs burdens developers; larger context does not fix attention quality; consensus across passes would suppress intermittently caught bugs.

**Tags:** multi_pass, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6; Sample Q12

---

## d4-036 · decision · ci_cd

**Tasks:** 4.6

**Q:** How should you route automated review findings to human triage?

**A:** Run a verification pass where the model reports confidence alongside each finding, then route using calibrated thresholds (high-severity / low-confidence to humans).

**Why:** Task 4.6 uses a verification pass with self-reported confidence for calibrated routing. That is different from using uncalibrated confidence as an escalation trigger in support.

**Tags:** review, confidence

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## d4-037 · compare · ci_cd, structured_extraction

**Tasks:** 4.3

**Q:** When should PR findings be prompt-only versus JSON schema for CI gates?

**A:** Schema for machine consumption (CI gates, dashboards); prompts alone only for human-readable narrative.

**Tags:** structured_output, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3; CI/CD scenario

---

## d4-038 · anti_pattern · structured_extraction

**Tasks:** 4.4

**Q:** Why is it a problem to trust model self-reported confidence without validation?

**A:** Not calibrated by default—use schema checks, cross-field rules, or human review thresholds for high-risk fields.

**Tags:** confidence, validation

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4; D5 crossover

---

## d4-039 · anti_pattern · ci_cd

**Tasks:** 4.6

**Q:** Why is it wrong to run three full PR review passes and only flag issues that appear in two or more?

**A:** Suppresses real bugs caught intermittently—consensus filtering hides attention-dilution problems; split passes instead.

**Tags:** multi_pass, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6; Sample Q12

---

## d4-040 · scenario_hook · structured_extraction

**Tasks:** 4.3, 5.5

**Q:** What are the primary domains for the Structured Data Extraction scenario (Scenario 6)?

**A:** D4 (schemas, validation, batch) and D5 (reliability, human review for low confidence).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d4-041 · scenario_hook · ci_cd

**Tasks:** 4.3, 4.4

**Q:** What extraction-system requirements does the exam guide list for Scenario 6?

**A:** Extract from unstructured docs, validate with JSON schemas, handle edge cases, integrate with downstream systems.

**Tags:** scenarios, extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6

---

## d4-042 · concept · structured_extraction

**Tasks:** 4.2

**Q:** What extraction use cases benefit from few-shot examples to reduce hallucination?

**A:** Informal measurements, varied document structures, and inconsistent field formats in source documents.

**Tags:** few_shot, hallucination

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-043 · anti_pattern · ci_cd

**Tasks:** 4.5

**Q:** Why is switching blocking pre-merge checks to the Batch API with status polling wrong?

**A:** Batch has no latency SLA—unacceptable for workflows where developers wait to merge.

**Tags:** batch_api, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5; Sample Q11

---

## d4-044 · decision · structured_extraction

**Tasks:** 4.5

**Q:** You have a 30-hour SLA and batches can take up to 24 hours. How often should you submit batches?

**A:** Calculate submission windows (e.g., 4-hour intervals) so batches complete within SLA with margin for retries.

**Why:** Batches can take up to 24 hours. For a 30-hour SLA, submit on a shorter cadence (for example every 4 hours) so there is margin for retries.

**Tags:** batch_api, sla

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## d4-045 · concept · ci_cd, structured_extraction

**Tasks:** 4.6

**Q:** Why prefer independent review instances over extended thinking for self-review?

**A:** Independent instances without generator context catch more subtle issues than self-review instructions or extended thinking alone.

**Tags:** multi_instance, self_review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## d4-046 · concept · ci_cd

**Tasks:** 4.1

**Q:** What is an example of explicit review criteria for comments versus code?

**A:** Flag comments only when claimed behavior contradicts actual code—not vague 'check comment accuracy'.

**Tags:** prompt_criteria, review

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## d4-047 · concept · ci_cd, structured_extraction

**Tasks:** 4.2

**Q:** How do few-shot examples generalize beyond the cases you pre-specify?

**A:** Demonstrate judgment and reasoning on ambiguous examples so the model applies similar logic to novel patterns.

**Tags:** few_shot, generalization

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-048 · decision · ci_cd

**Tasks:** 4.2

**Q:** How should few-shot examples teach the model to report branch-level test coverage gaps?

**A:** Show how to identify and report coverage gaps at branch level—ambiguous case requiring demonstrated judgment.

**Why:** ambiguous case requiring demonstrated judgment.

**Tags:** few_shot, testing

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## d4-049 · anti_pattern · ci_cd

**Tasks:** 4.5

**Q:** Why is switching both blocking and overnight jobs to the Batch API with a real-time fallback over-engineered?

**A:** Match API to latency needs—sync for blocking checks, batch for overnight; fallback adds unnecessary complexity.

**Tags:** batch_api, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5; Sample Q11

---

## d4-050 · anti_pattern · ci_cd

**Tasks:** 4.6

**Q:** For a large PR review, why is switching to a higher-tier model with a larger context window insufficient?

**A:** Larger context doesn't fix attention dilution—split into per-file plus integration passes instead.

**Tags:** multi_pass, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6; Sample Q12

