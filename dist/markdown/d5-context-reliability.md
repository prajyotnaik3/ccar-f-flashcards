# D5: Context Management & Reliability

## d5-001 · concept · customer_support, multi_agent_research, code_generation

**Tasks:** 5.4

**Q:** What is context degradation in long agent sessions?

**A:** Reasoning quality drops as irrelevant history accumulates—inconsistent answers and vague 'typical pattern' references instead of specifics.

**Tags:** context_degradation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-002 · concept · customer_support, structured_extraction

**Tasks:** 5.1

**Q:** What is the risk of progressive summarization in long support sessions?

**A:** Condenses amounts, dates, percentages, and customer-stated expectations into vague summaries—loses critical transactional facts.

**Tags:** summarization, case_facts

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-003 · concept · multi_agent_research, structured_extraction

**Tasks:** 5.1

**Q:** What is the 'lost in the middle' effect?

**A:** Models reliably use info at the start and end of long inputs but may omit findings buried in middle sections.

**Tags:** lost_in_middle, position

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-004 · decision · customer_support

**Tasks:** 5.1

**Q:** How do you preserve order amounts and dates across a long support conversation?

**A:** Extract transactional facts into a persistent case facts block in each prompt—outside summarized history.

**Why:** Keep amounts, dates, and order IDs in a persistent case-facts block outside summarized history so progressive summarization cannot wash them out.

**Tags:** case_facts, context

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-005 · decision · customer_support

**Tasks:** 5.1

**Q:** Order lookup returns 40+ fields but only 5 matter for returns. How should you fix the context?

**A:** Trim verbose tool outputs to relevant fields before they accumulate in conversation context.

**Why:** Trim 40-field order payloads to the few return-relevant fields before they accumulate. Verbose tool results crowd out the facts that matter.

**Tags:** trimming, tool_results

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-006 · decision · multi_agent_research

**Tasks:** 5.1

**Q:** How do you mitigate lost-in-the-middle when aggregating subagent results?

**A:** Place key findings summary at the beginning; organize detailed results with explicit section headers.

**Why:** Exam judgment aligned to task 5.1: Place key findings summary at the beginning; organize detailed results with explicit section headers.

**Tags:** lost_in_middle, aggregation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-007 · decision · multi_agent_research

**Tasks:** 5.1

**Q:** The downstream synthesis agent has a limited context budget. How should upstream agents shape their output?

**A:** Return structured key facts, citations, and relevance scores—not verbose reasoning chains.

**Why:** When downstream context is tight, upstream agents should return key facts, citations, and relevance scores—not long reasoning chains.

**Tags:** structured_output, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-008 · concept · customer_support, multi_agent_research

**Tasks:** 5.1

**Q:** Why should you pass complete conversation history in subsequent API requests?

**A:** Maintains conversational coherence—the model needs prior turns to reason about the ongoing case.

**Tags:** conversation_history

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-009 · decision · customer_support

**Tasks:** 5.1

**Q:** A support session covers multiple issues (billing and a return). How should you structure the context layer?

**A:** Persist structured issue data (order IDs, amounts, statuses) in a separate context layer for each concern.

**Why:** For billing plus a return, persist structured issue data (IDs, amounts, statuses) in a separate layer per concern so one summary does not merge them.

**Tags:** case_facts, multi_issue

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-010 · concept · customer_support

**Tasks:** 5.2

**Q:** Name three appropriate escalation triggers besides calling the case 'complex'.

**A:** Customer explicitly requests human, policy exception/gap, and inability to make meaningful progress.

**Tags:** escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-011 · decision · customer_support

**Tasks:** 5.2

**Q:** First-contact resolution is 55%: the agent escalates easy cases and handles hard policy exceptions alone. What is the best calibration fix?

**A:** Add explicit escalation criteria with few-shot examples showing escalate vs resolve autonomously.

**Why:** Explicit escalation criteria with few-shot examples fix unclear decision boundaries—the proportionate first fix. LLM self-reported confidence is poorly calibrated on hard cases; a separate classifier is over-engineered before prompt tuning; sentiment does not measure case complexity.

**Tags:** escalation, few_shot

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-012 · anti_pattern · customer_support

**Tasks:** 5.2

**Q:** Why is routing to a human when self-reported confidence is below a threshold unreliable?

**A:** LLM confidence is poorly calibrated—agent may be wrongly confident on hard cases and uncertain on easy ones.

**Tags:** escalation, confidence, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-013 · anti_pattern · customer_support

**Tasks:** 5.2

**Q:** Why is escalating on a negative-sentiment threshold the wrong calibration fix?

**A:** Sentiment doesn't correlate with case complexity—the actual issue is unclear escalation boundaries.

**Tags:** escalation, sentiment, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-014 · decision · customer_support

**Tasks:** 5.2

**Q:** The customer explicitly demands a human agent. What should the agent do?

**A:** Honor immediately—do not attempt investigation first when they explicitly request a human.

**Why:** do not attempt investigation first when they explicitly request a human.

**Tags:** escalation, customer_request

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-015 · decision · customer_support

**Tasks:** 5.2

**Q:** The customer is frustrated, but the issue is within the agent's capability. What should the agent do?

**A:** Acknowledge frustration and offer resolution; escalate only if customer reiterates preference for human.

**Why:** Frustration alone is not an escalation trigger if the issue is in scope. Acknowledge, offer to resolve, and escalate only if they still want a human.

**Tags:** escalation, de_escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-016 · decision · customer_support

**Tasks:** 5.2

**Q:** Policy is silent on competitor price matching (it only covers own-site adjustments). What should the agent do?

**A:** Escalate—policy gap/exception case, not autonomous resolution.

**Why:** policy gap/exception case, not autonomous resolution.

**Tags:** escalation, policy_gap

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-017 · decision · customer_support

**Tasks:** 5.2

**Q:** get_customer returns multiple matches. What should the agent do?

**A:** Ask for additional identifiers—never pick a match heuristically.

**Why:** never pick a match heuristically.

**Tags:** ambiguity, identity

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-018 · decision · multi_agent_research

**Tasks:** 5.1

**Q:** Subagents need prior search results. What is the best way to pass that context?

**A:** Explicit structured handoffs (IDs, snippets, citations) via coordinator—not implicit shared memory.

**Why:** not implicit shared memory.

**Tags:** context_passing, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1; Multi-Agent Research scenario

---

## d5-019 · decision · multi_agent_research

**Tasks:** 5.3

**Q:** The web search subagent times out. What error context should you propagate to the coordinator?

**A:** Structured context: failure type, attempted query, partial results, and alternative approaches.

**Why:** Structured error context enables coordinator recovery (retry, alternate query, partial results). Generic retry status hides context; marking failure as success blocks recovery; terminating the whole workflow is unnecessary when partial progress exists.

**Tags:** error_propagation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3; Sample Q8

---

## d5-020 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** Why is it an anti-pattern for a subagent to return empty results marked successful after a timeout?

**A:** Silently suppresses errors—coordinator cannot recover or annotate coverage gaps.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3; Sample Q8

---

## d5-021 · decision · multi_agent_research

**Tasks:** 5.3

**Q:** After partial subagent failures, what should synthesis output include?

**A:** Coverage annotations: which findings are well-supported vs which topic areas have gaps from unavailable sources.

**Why:** Exam judgment aligned to task 5.3: Coverage annotations: which findings are well-supported vs which topic areas have gaps from unavailable sources.

**Tags:** synthesis, coverage

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## d5-022 · decision · customer_support, multi_agent_research

**Tasks:** 5.3

**Q:** The agent loop fails twice on the same tool error. What should you do next?

**A:** Escalate or change strategy (alternate tool, human handoff)—not infinite identical retries.

**Why:** not infinite identical retries.

**Tags:** errors, escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## d5-023 · concept · code_generation, developer_productivity

**Tasks:** 5.4

**Q:** What is the purpose of scratchpad files in long Claude Code exploration sessions?

**A:** Persist key findings across context boundaries; reference for later questions to counteract degradation.

**Tags:** scratchpad, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-024 · decision · code_generation, developer_productivity

**Tasks:** 5.4

**Q:** Verbose codebase exploration fills the context. Which Claude Code command reduces usage?

**A:** /compact to condense verbose discovery output during extended sessions.

**Why:** /compact condenses verbose discovery output in long Claude Code sessions. It is the documented command for context pressure during exploration.

**Tags:** compact, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4; Appendix

---

## d5-025 · decision · developer_productivity

**Tasks:** 5.4

**Q:** In multi-phase codebase exploration, how should you manage context between phases?

**A:** Summarize key findings from one phase, inject summary into context before spawning subagents for the next.

**Why:** Summarize each exploration phase and inject that summary before the next subagents spawn so later phases do not inherit a huge raw trace.

**Tags:** exploration, summarization

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-026 · concept · multi_agent_research, developer_productivity

**Tasks:** 5.4

**Q:** What crash-recovery pattern should multi-agent workflows use?

**A:** Each agent exports state to a known location; coordinator loads manifest on resume and injects into prompts.

**Tags:** crash_recovery, manifests

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-027 · anti_pattern · code_generation, developer_productivity

**Tasks:** 2.5, 5.4

**Q:** Why is dumping the entire repo into context for every Claude Code task a problem?

**A:** Wastes tokens and adds noise—use Grep/Glob and scoped reads incrementally.

**Tags:** context, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4; D2 Task 2.5

---

## d5-028 · concept · structured_extraction

**Tasks:** 5.5

**Q:** Overall extraction accuracy is 97%. Why should you not automate away all human review?

**A:** Aggregate metrics may mask poor performance on specific document types or individual fields.

**Tags:** human_review, metrics

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-029 · decision · structured_extraction

**Tasks:** 5.5

**Q:** How should you monitor quality for high-confidence extractions over time?

**A:** Stratified random sampling to measure error rates and detect novel error patterns.

**Why:** Exam judgment aligned to task 5.5: Stratified random sampling to measure error rates and detect novel error patterns.

**Tags:** human_review, sampling

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-030 · decision · structured_extraction

**Tasks:** 5.5

**Q:** How do you calibrate human-review routing for extractions?

**A:** Model outputs field-level confidence; calibrate thresholds using labeled validation sets.

**Why:** Have the model emit field-level confidence, then set review thresholds on a labeled validation set. Uncalibrated scores are not production routing rules.

**Tags:** confidence, human_review

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-031 · decision · structured_extraction

**Tasks:** 5.5

**Q:** Before reducing human review on high-confidence extractions, what should you verify?

**A:** Accuracy by document type and field segment—consistent performance across all segments.

**Why:** consistent performance across all segments.

**Tags:** human_review, segmentation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-032 · decision · structured_extraction

**Tasks:** 5.5

**Q:** Reviewer capacity is limited. Which extractions should you prioritize for human review?

**A:** Low model confidence, ambiguous source documents, or contradictory source data.

**Why:** With limited reviewers, send low-confidence extractions and ambiguous or contradictory source documents to humans first.

**Tags:** human_review, routing

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-033 · concept · multi_agent_research

**Tasks:** 5.6

**Q:** How is source attribution lost in multi-agent research pipelines?

**A:** Summarization compresses findings without preserving claim-to-source mappings.

**Tags:** provenance, synthesis

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-034 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** What provenance must subagent output include for downstream synthesis?

**A:** Structured claim-source mappings (URLs, document names, excerpts) preserved through synthesis.

**Why:** Exam judgment aligned to task 5.6: Structured claim-source mappings (URLs, document names, excerpts) preserved through synthesis.

**Tags:** provenance, claim_source

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-035 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** Two credible sources report different statistics. How should synthesis handle that?

**A:** Annotate conflict with source attribution—do not arbitrarily pick one value.

**Why:** do not arbitrarily pick one value.

**Tags:** provenance, conflicts

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-036 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** Why should structured subagent outputs include publication or collection dates?

**A:** Enables correct temporal interpretation—prevents time differences being misread as contradictions.

**Why:** prevents time differences being misread as contradictions.

**Tags:** temporal, provenance

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-037 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** How should a research report structure contested findings versus established ones?

**A:** Explicit sections distinguishing well-established findings from contested ones with methodological context.

**Why:** Structure the report with explicit well-established vs contested sections and keep methodological context. Do not flatten everything into one confident narrative.

**Tags:** synthesis, provenance

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-038 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** How should synthesis format mixed content types?

**A:** Render appropriately—financial data as tables, news as prose, technical findings as structured lists.

**Why:** financial data as tables, news as prose, technical findings as structured lists.

**Tags:** synthesis, formatting

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-039 · scenario_hook · customer_support, code_generation, multi_agent_research, structured_extraction

**Tasks:** 5.1, 5.2, 5.3

**Q:** Which exam scenarios list D5 as a primary domain?

**A:** Four: Customer Support, Code Generation, Multi-Agent Research, and Structured Data Extraction. Developer Productivity and CI/CD do not list D5 as primary.

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d5-040 · scenario_hook · code_generation

**Tasks:** 3.4, 5.1

**Q:** What D5 focus areas does the Code Generation scenario (Scenario 2) emphasize?

**A:** Context preservation across edits, plan vs execute context management, and session reliability.

**Tags:** scenarios, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2

---

## d5-041 · decision · multi_agent_research

**Tasks:** 5.1

**Q:** What metadata must structured subagent outputs include for downstream synthesis?

**A:** Dates, source locations, and methodological context—not just claims without provenance context.

**Why:** not just claims without provenance context.

**Tags:** metadata, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-042 · anti_pattern · customer_support

**Tasks:** 5.2

**Q:** Why is deploying a classifier to predict escalation before the agent runs an over-engineered first step?

**A:** Requires labeled data and ML infra when prompt criteria with few-shot hasn't been tried yet.

**Tags:** escalation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-043 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** A subagent retries, then returns generic 'search unavailable' to the coordinator. What is the problem?

**A:** Hides failure type, attempted query, and partial results—coordinator cannot make informed recovery.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3; Sample Q8

---

## d5-044 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** A single subagent failure terminates the entire multi-agent workflow. Why is that wrong?

**A:** Often recoverable with partial results, alternate queries, or gap annotations—unnecessary full termination.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## d5-045 · decision · developer_productivity, code_generation

**Tasks:** 5.4

**Q:** During long codebase exploration, how do you delegate specific questions while preserving coordination?

**A:** Spawn subagents for focused tasks (find test files, trace refund flow) while main agent keeps high-level coordination.

**Why:** Exam judgment aligned to task 5.4: Spawn subagents for focused tasks (find test files, trace refund flow) while main agent keeps high-level coordination.

**Tags:** subagents, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-046 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** Document analysis finds conflicting values from sources. What should happen before synthesis?

**A:** Complete analysis with conflicts included and explicitly annotated—let coordinator reconcile before passing to synthesis.

**Why:** let coordinator reconcile before passing to synthesis.

**Tags:** provenance, conflicts

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-047 · decision · developer_productivity

**Tasks:** 5.4

**Q:** How should you use a scratchpad file during exploration for follow-up questions?

**A:** Record key findings in scratchpad; reference it for subsequent questions to counteract context degradation.

**Why:** Write key findings to a scratchpad and reread it on follow-up questions so later turns do not fall back on vague 'typical patterns'.

**Tags:** scratchpad, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## tn-5-1 · task_notes · all

**Tasks:** 5.1

**Q:** Task 5.1 — Manage conversation context to preserve critical information

**A:** Copy facts forward verbatim. Do not ask the model to 'summarize the chat'.

**Notes:**
- Progressive summary eats amounts, dates, %, names, and customer expectations.
- Keep a persistent case-facts block copied forward exactly, outside the summary.
- Lost-in-the-middle: lead with a findings summary; section-header the rest.
- Trim 40-field order payloads to the 5 return-relevant fields before they pile up.
- Always send complete conversation history on later API calls.
- Multi-issue: structured layer per concern. Upstream should emit facts/citations/scores, not novels.

**Tags:** task_notes, context

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## tn-5-2 · task_notes · all

**Tasks:** 5.2

**Q:** Task 5.2 — Design escalation and ambiguity resolution patterns

**A:** Human-on-request, policy gaps, stuck. Not confidence or sentiment.

**Notes:**
- Escalate: explicit human request, policy gap/exception, cannot make progress.
- Honor 'I want a human' immediately—do not investigate first.
- Frustrated but in-scope: empathize and offer to finish; escalate if they insist.
- Policy silent on competitor match (only own-site) → gap → escalate. Policy forbids → refuse with the rule.
- Multiple customer matches: ask for more IDs, never pick a heuristic winner.
- Self-reported confidence and sentiment are distractors (Sample Q3). Fix with criteria + few-shot.

**Tags:** task_notes, escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## tn-5-3 · task_notes · all

**Tasks:** 5.3

**Q:** Task 5.3 — Implement error propagation across multi-agent systems

**A:** Structured errors with partials. Never fake success or kill the whole job.

**Notes:**
- Return failure type, attempted query, partial results, alternatives tried, suggested next step.
- Generic 'search unavailable' after internal retries hides recovery options.
- Empty result marked success after timeout blocks recovery. One timeout should not abort the workflow.
- Synthesis should annotate coverage: solid vs gapped topics.
- Same tool error twice: change strategy or escalate—do not infinite-retry.

**Tags:** task_notes, error_propagation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## tn-5-4 · task_notes · all

**Tasks:** 5.4

**Q:** Task 5.4 — Manage context in large codebase exploration

**A:** Scratchpads survive context reset. Conversation history does not.

**Notes:**
- Long sessions drift to 'typical patterns' instead of files already read.
- Write findings to a scratchpad file; reread it after compact/reset. Disk outlives the window.
- /compact when discovery spam fills the window. Between phases: summarize, then spawn next subagents.
- Main agent coordinates; subagents take 'find tests' / 'trace refund flow'.
- Crash recovery: each agent writes state; coordinator reloads a manifest into prompts.
- Never dump the whole repo into context.

**Tags:** task_notes, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## tn-5-5 · task_notes · all

**Tasks:** 5.5

**Q:** Task 5.5 — Design human review workflows and confidence calibration

**A:** 97% overall can hide a bad slice. Stratify. Calibrate on labels.

**Notes:**
- High overall accuracy + user complaints → per-type/field accuracy, not a bigger aggregate.
- Before dropping review on high-confidence rows, slice by document type and field.
- Field-level scores + thresholds belong on a labeled validation set.
- Stratified random sample of the 'easy' pile to catch new error modes.
- Finite reviewers: low confidence, messy docs, contradictory sources first.

**Tags:** task_notes, human_review

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## tn-5-6 · task_notes · all

**Tasks:** 5.6

**Q:** Task 5.6 — Preserve provenance and handle uncertainty in multi-source synthesis

**A:** Structured claim–source maps. Annotate conflicts. Do not pick a winner.

**Notes:**
- Inline markdown links die in summarization. Structured {claim, source, url, date} survives.
- Subagents emit mappings; synthesis must keep them.
- Two credible stats: keep both with dates. Do not average or silently pick the newer one.
- Dates often explain 'contradictions' that are just different collection times.
- Report shape: established vs contested. Analyst annotates; coordinator reconciles before synthesis.
- Render by type: tables for finance, prose for news, lists for technical findings.

**Tags:** task_notes, provenance

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

