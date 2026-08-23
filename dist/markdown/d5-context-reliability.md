# D5: Context Management & Reliability

## d5-001 · concept · customer_support, multi_agent_research, code_generation

**Q:** What is context degradation in long agent sessions?

**A:** Reasoning quality drops as irrelevant history accumulates—inconsistent answers and vague 'typical pattern' references instead of specifics.

**Tags:** context_degradation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-002 · concept · customer_support, structured_extraction

**Q:** Risk of progressive summarization in long support sessions?

**A:** Condenses amounts, dates, percentages, and customer-stated expectations into vague summaries—loses critical transactional facts.

**Tags:** summarization, case_facts

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-003 · concept · multi_agent_research, structured_extraction

**Q:** What is the 'lost in the middle' effect?

**A:** Models reliably use info at the start and end of long inputs but may omit findings buried in middle sections.

**Tags:** lost_in_middle, position

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-004 · decision · customer_support

**Q:** Preserve order amounts and dates across a long support conversation?

**A:** Extract transactional facts into a persistent case facts block in each prompt—outside summarized history.

**Tags:** case_facts, context

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-005 · decision · customer_support

**Q:** Order lookup returns 40+ fields but only 5 matter for returns. Context fix?

**A:** Trim verbose tool outputs to relevant fields before they accumulate in conversation context.

**Tags:** trimming, tool_results

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-006 · decision · multi_agent_research

**Q:** Mitigate lost-in-the-middle when aggregating subagent results?

**A:** Place key findings summary at the beginning; organize detailed results with explicit section headers.

**Tags:** lost_in_middle, aggregation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-007 · decision · multi_agent_research

**Q:** Downstream synthesis agent has limited context budget. Upstream agent output design?

**A:** Return structured key facts, citations, and relevance scores—not verbose reasoning chains.

**Tags:** structured_output, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-008 · concept · customer_support, multi_agent_research

**Q:** Why pass complete conversation history in subsequent API requests?

**A:** Maintains conversational coherence—the model needs prior turns to reason about the ongoing case.

**Tags:** conversation_history

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-009 · decision · customer_support

**Q:** Multi-issue support session (billing + return). Context layer approach?

**A:** Persist structured issue data (order IDs, amounts, statuses) in a separate context layer for each concern.

**Tags:** case_facts, multi_issue

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-010 · concept · customer_support

**Q:** Three appropriate escalation triggers (beyond 'complex case')?

**A:** Customer explicitly requests human, policy exception/gap, and inability to make meaningful progress.

**Tags:** escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-011 · decision · customer_support

**Q:** 55% FCR—escalates easy cases, handles hard policy exceptions alone. Best calibration fix?

**A:** Add explicit escalation criteria with few-shot examples showing escalate vs resolve autonomously.

**Tags:** escalation, few_shot

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-012 · anti_pattern · customer_support

**Q:** Route to human when self-reported confidence score is below threshold. Why unreliable?

**A:** LLM confidence is poorly calibrated—agent may be wrongly confident on hard cases and uncertain on easy ones.

**Tags:** escalation, confidence, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-013 · anti_pattern · customer_support

**Q:** Escalate on negative sentiment threshold. Why wrong for calibration?

**A:** Sentiment doesn't correlate with case complexity—the actual issue is unclear escalation boundaries.

**Tags:** escalation, sentiment, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-014 · decision · customer_support

**Q:** Customer explicitly demands a human agent. Response?

**A:** Honor immediately—do not attempt investigation first when they explicitly request a human.

**Tags:** escalation, customer_request

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-015 · decision · customer_support

**Q:** Frustrated customer, issue is within agent capability. Approach?

**A:** Acknowledge frustration and offer resolution; escalate only if customer reiterates preference for human.

**Tags:** escalation, de_escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-016 · decision · customer_support

**Q:** Policy silent on competitor price matching (only covers own-site adjustments). Action?

**A:** Escalate—policy gap/exception case, not autonomous resolution.

**Tags:** escalation, policy_gap

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-017 · decision · customer_support

**Q:** get_customer returns multiple matches. What should the agent do?

**A:** Ask for additional identifiers—never pick a match heuristically.

**Tags:** ambiguity, identity

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-018 · decision · multi_agent_research

**Q:** Subagents need prior search results. Best context passing?

**A:** Explicit structured handoffs (IDs, snippets, citations) via coordinator—not implicit shared memory.

**Tags:** context_passing, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1; Multi-Agent Research scenario

---

## d5-019 · decision · multi_agent_research

**Q:** Web search subagent timeout—best error propagation to coordinator?

**A:** Structured context: failure type, attempted query, partial results, and alternative approaches.

**Tags:** error_propagation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3; Sample Q8

---

## d5-020 · anti_pattern · multi_agent_research

**Q:** Subagent returns empty results marked successful after timeout. Why anti-pattern?

**A:** Silently suppresses errors—coordinator cannot recover or annotate coverage gaps.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3; Sample Q8

---

## d5-021 · decision · multi_agent_research

**Q:** Synthesis output after partial subagent failures—what include?

**A:** Coverage annotations: which findings are well-supported vs which topic areas have gaps from unavailable sources.

**Tags:** synthesis, coverage

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## d5-022 · decision · customer_support, multi_agent_research

**Q:** Agent loop fails twice on same tool error. Next step?

**A:** Escalate or change strategy (alternate tool, human handoff)—not infinite identical retries.

**Tags:** errors, escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## d5-023 · concept · code_generation, developer_productivity

**Q:** Scratchpad files in long Claude Code exploration sessions—purpose?

**A:** Persist key findings across context boundaries; reference for later questions to counteract degradation.

**Tags:** scratchpad, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-024 · decision · code_generation, developer_productivity

**Q:** Verbose codebase exploration fills context. Claude Code command to reduce usage?

**A:** /compact to condense verbose discovery output during extended sessions.

**Tags:** compact, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4; Appendix

---

## d5-025 · decision · developer_productivity

**Q:** Multi-phase codebase exploration—context pattern between phases?

**A:** Summarize key findings from one phase, inject summary into context before spawning subagents for the next.

**Tags:** exploration, summarization

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-026 · concept · multi_agent_research, developer_productivity

**Q:** Crash recovery pattern for multi-agent workflows?

**A:** Each agent exports state to a known location; coordinator loads manifest on resume and injects into prompts.

**Tags:** crash_recovery, manifests

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-027 · anti_pattern · code_generation, developer_productivity

**Q:** Why dump entire repo into context for every Claude Code task?

**A:** Wastes tokens and adds noise—use Grep/Glob and scoped reads incrementally.

**Tags:** context, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4; D2 Task 2.5

---

## d5-028 · concept · structured_extraction

**Q:** 97% overall extraction accuracy—why not automate all human review?

**A:** Aggregate metrics may mask poor performance on specific document types or individual fields.

**Tags:** human_review, metrics

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-029 · decision · structured_extraction

**Q:** Ongoing quality monitoring for high-confidence extractions?

**A:** Stratified random sampling to measure error rates and detect novel error patterns.

**Tags:** human_review, sampling

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-030 · decision · structured_extraction

**Q:** Calibrate human review routing for extractions?

**A:** Model outputs field-level confidence; calibrate thresholds using labeled validation sets.

**Tags:** confidence, human_review

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-031 · decision · structured_extraction

**Q:** Before reducing human review on high-confidence extractions—verify what?

**A:** Accuracy by document type and field segment—consistent performance across all segments.

**Tags:** human_review, segmentation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-032 · decision · structured_extraction

**Q:** Limited reviewer capacity—prioritize which extractions for human review?

**A:** Low model confidence, ambiguous source documents, or contradictory source data.

**Tags:** human_review, routing

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-033 · concept · multi_agent_research

**Q:** How is source attribution lost in multi-agent research pipelines?

**A:** Summarization compresses findings without preserving claim-to-source mappings.

**Tags:** provenance, synthesis

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-034 · decision · multi_agent_research

**Q:** Subagent output for downstream synthesis—provenance requirement?

**A:** Structured claim-source mappings (URLs, document names, excerpts) preserved through synthesis.

**Tags:** provenance, claim_source

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-035 · decision · multi_agent_research

**Q:** Two credible sources report different statistics. Synthesis handling?

**A:** Annotate conflict with source attribution—do not arbitrarily pick one value.

**Tags:** provenance, conflicts

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-036 · decision · multi_agent_research

**Q:** Why require publication/collection dates in structured subagent outputs?

**A:** Enables correct temporal interpretation—prevents time differences being misread as contradictions.

**Tags:** temporal, provenance

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-037 · decision · multi_agent_research

**Q:** Research report structure for contested vs established findings?

**A:** Explicit sections distinguishing well-established findings from contested ones with methodological context.

**Tags:** synthesis, provenance

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-038 · decision · multi_agent_research

**Q:** Synthesis output formatting for mixed content types?

**A:** Render appropriately—financial data as tables, news as prose, technical findings as structured lists.

**Tags:** synthesis, formatting

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-039 · scenario_hook · customer_support, multi_agent_research, structured_extraction

**Q:** Which three scenarios list D5 as a primary domain?

**A:** Customer Support, Multi-Agent Research, and Structured Data Extraction.

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d5-040 · scenario_hook · code_generation

**Q:** Code Generation scenario (Scenario 2)—D5 focus areas?

**A:** Context preservation across edits, plan vs execute context management, and session reliability.

**Tags:** scenarios, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2

