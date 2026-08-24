# CHAIN: Scenario Chains

## sc-001 · scenario_chain · customer_support

**Tasks:** 1.1, 1.4

**Q:** [Customer Support · 1/5] You deploy a support agent with MCP tools (get_customer, lookup_order, process_refund, escalate_to_human). Target is 80%+ first-contact resolution. What architectural foundation comes first?

**A:** Design agentic loop with stop_reason control, scoped tools, and escalation paths—before tuning prompts.

**Tags:** scenario_chain, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## sc-002 · scenario_chain · customer_support

**Tasks:** 1.4

**Q:** [Customer Support · 2/5] Production data: 12% of cases skip get_customer and call lookup_order by name only, causing wrong refunds. What is the best fix?

**A:** Programmatic prerequisite blocking lookup_order and process_refund until get_customer returns verified customer ID.

**Why:** Money and identity need deterministic enforcement—not prompts alone.

**Tags:** scenario_chain, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1; Sample Q1
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## sc-003 · scenario_chain · customer_support

**Tasks:** 2.1

**Q:** [Customer Support · 3/5] Logs show get_customer called for order queries (#12345) instead of lookup_order. Both tools have minimal descriptions. What should you fix first?

**A:** Expand tool descriptions with inputs, example queries, edge cases, and when to use each vs similar tools.

**Tags:** scenario_chain, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1; Sample Q2
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## sc-004 · scenario_chain · customer_support

**Tasks:** 5.2

**Q:** [Customer Support · 4/5] First-contact resolution is 55%: the agent escalates easy cases and handles hard policy exceptions alone. What is the best calibration fix?

**A:** Add explicit escalation criteria with few-shot examples for escalate vs resolve autonomously.

**Tags:** scenario_chain, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1; Sample Q3
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## sc-005 · scenario_chain · customer_support

**Tasks:** 5.2

**Q:** [Customer Support · 5/5] get_customer returns multiple matches for one name. What must the agent do?

**A:** Ask for additional identifiers—never select a match heuristically.

**Tags:** scenario_chain, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## sc-006 · scenario_chain · code_generation

**Tasks:** 3.1, 3.2

**Q:** [Code Generation · 1/5] Your team uses Claude Code for generation, refactoring, and docs—with slash commands, CLAUDE.md, and plan mode. What should be shared via git for consistent team behavior?

**A:** Project-level CLAUDE.md, .claude/commands/, .claude/rules/, and .mcp.json—not user-only ~/.claude config.

**Tags:** scenario_chain, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## sc-007 · scenario_chain · code_generation

**Tasks:** 3.2

**Q:** [Code Generation · 2/5] You need a /review slash command available to everyone who clones the repo. Where do you put it?

**A:** .claude/commands/ in the project repository (version controlled).

**Tags:** scenario_chain, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2; Sample Q4
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## sc-008 · scenario_chain · code_generation

**Tasks:** 3.4

**Q:** [Code Generation · 3/5] Assignment: split a monolith into microservices across dozens of files with unclear boundaries. Which mode should you use first?

**A:** Plan mode—explore dependencies and design before editing; direct execution risks costly rework.

**Tags:** scenario_chain, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2; Sample Q5
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## sc-009 · scenario_chain · code_generation

**Tasks:** 3.3

**Q:** [Code Generation · 4/5] Tests live as *.test.tsx next to components across the repo. How do you auto-apply test conventions when generating code?

**A:** .claude/rules/ with glob paths like **/*.test.tsx—not directory-bound CLAUDE.md or inference from headers.

**Tags:** scenario_chain, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2; Sample Q6
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## sc-010 · scenario_chain · code_generation

**Tasks:** 5.4

**Q:** [Code Generation · 5/5] In a long refactor session, the model starts citing generic patterns instead of files it read earlier. How do you mitigate that?

**A:** Scratchpad file for key findings, /compact for verbose output, or summarize before the next exploration phase.

**Tags:** scenario_chain, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## sc-011 · scenario_chain · multi_agent_research

**Tasks:** 1.3

**Q:** [Multi-Agent Research · 1/5] Coordinator delegates search, document analysis, synthesis, and report agents. What must allowedTools include on the coordinator?

**A:** Task tool—required for spawning subagents.

**Tags:** scenario_chain, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## sc-012 · scenario_chain · multi_agent_research

**Tasks:** 1.2

**Q:** [Multi-Agent Research · 2/5] Topic is 'AI in creative industries', but the final report covers only visual arts because the coordinator assigned digital art, graphic design, and photography only. What is the root cause?

**A:** Coordinator task decomposition too narrow—subagents executed correctly but incomplete scope.

**Tags:** scenario_chain, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3; Sample Q7
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## sc-013 · scenario_chain · multi_agent_research

**Tasks:** 5.3

**Q:** [Multi-Agent Research · 3/5] Web search subagent times out. What should the coordinator receive?

**A:** Structured error context—failure type, attempted query, partial results, alternative approaches.

**Tags:** scenario_chain, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3; Sample Q8
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## sc-014 · scenario_chain · multi_agent_research

**Tasks:** 2.3

**Q:** [Multi-Agent Research · 4/5] Synthesis needs many simple fact-checks (85%) but some deep searches (15%). How do you reduce latency without over-provisioning synthesis?

**A:** Scoped verify_fact tool on synthesis for simple lookups; complex cases still route through coordinator to search agent.

**Tags:** scenario_chain, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3; Sample Q9
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## sc-015 · scenario_chain · multi_agent_research

**Tasks:** 5.6

**Q:** [Multi-Agent Research · 5/5] The final report must preserve citations through synthesis. What should you require from subagents?

**A:** Structured claim–source mappings (URLs, excerpts, dates) preserved through synthesis—not compressed summaries without attribution.

**Tags:** scenario_chain, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## sc-016 · scenario_chain · developer_productivity

**Tasks:** 2.4, 2.5

**Q:** [Developer Productivity · 1/5] An agent helps engineers explore legacy codebases using built-in tools and MCP. When should you prefer MCP over Grep or Glob?

**A:** External systems (GitHub, DB, SaaS) or shared team integrations—not local file search.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.4–2.5

---

## sc-017 · scenario_chain · developer_productivity

**Tasks:** 2.5

**Q:** [Developer Productivity · 2/5] You need all callers of a function across the monorepo. Which built-in tool should you use first?

**A:** Grep for content patterns across files—not Glob (paths) or reading every file upfront.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## sc-018 · scenario_chain · developer_productivity

**Tasks:** 2.4

**Q:** [Developer Productivity · 3/5] The agent prefers Grep over your team's richer MCP code-search tool. How do you fix that?

**A:** Enhance MCP tool descriptions so the model understands when MCP beats built-in search.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## sc-019 · scenario_chain · developer_productivity

**Tasks:** 2.5, 5.4

**Q:** [Developer Productivity · 4/5] How should you explore a large codebase without reading every file?

**A:** Grep entry points → Read to follow imports → scratchpad key findings for later questions.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.5; D5, Task 5.4

---

## sc-020 · scenario_chain · developer_productivity

**Tasks:** 2.4

**Q:** [Developer Productivity · 5/5] You want to share GitHub MCP with the team but keep an experimental personal server. Where does each config live?

**A:** Team server in project .mcp.json with ${TOKEN}; personal server in ~/.claude.json.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## sc-021 · scenario_chain · ci_cd

**Tasks:** 3.6

**Q:** [CI/CD · 1/5] The pipeline runs claude 'Review this PR' but hangs waiting for input. How do you fix that?

**A:** Use -p (--print) for non-interactive mode—process prompt, output, exit.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5; Sample Q10
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## sc-022 · scenario_chain · ci_cd

**Tasks:** 3.6, 4.3

**Q:** [CI/CD · 2/5] How do you post structured findings as inline PR comments from CI?

**A:** --output-format json with --json-schema for machine-parseable review output.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5
- Official CCAR-F Exam Guide — D3, Task 3.6; D4, Task 4.3

---

## sc-023 · scenario_chain · ci_cd

**Tasks:** 3.6, 4.6

**Q:** [CI/CD · 3/5] The same Claude session generated the code and then reviews it, missing subtle bugs. What is a better approach?

**A:** Independent Claude Code instance for review without the generator's reasoning context.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5
- Official CCAR-F Exam Guide — D3, Task 3.6; D4, Task 4.6

---

## sc-024 · scenario_chain · ci_cd

**Tasks:** 4.6

**Q:** [CI/CD · 4/5] A 14-file PR review has inconsistent depth, missed bugs, and contradictory feedback. How should you restructure it?

**A:** Per-file local analysis passes, then separate cross-file integration pass.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5; Sample Q12
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## sc-025 · scenario_chain · ci_cd

**Tasks:** 3.6

**Q:** [CI/CD · 5/5] Re-running the review after new commits duplicates inline comments. What context should you add?

**A:** Include prior findings; instruct Claude to report only new or still-unaddressed issues.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## sc-026 · scenario_chain · structured_extraction

**Tasks:** 4.3

**Q:** [Structured Extraction · 1/5] A pipeline extracts from unstructured docs, validates with JSON schema, and integrates downstream. What is the most reliable structured-output approach?

**A:** tool_use with JSON schemas—eliminates syntax errors; add semantic validation separately.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## sc-027 · scenario_chain · structured_extraction

**Tasks:** 4.3

**Q:** [Structured Extraction · 2/5] Source docs often omit optional fields, and the model fabricates values. How should you fix the schema?

**A:** Make fields optional/nullable when information may be absent—don't require missing data.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## sc-028 · scenario_chain · structured_extraction

**Tasks:** 4.4

**Q:** [Structured Extraction · 3/5] Validation fails on a date format mismatch, but the information exists in the document. What is the next step?

**A:** Retry with original doc, failed extraction, and specific validation errors in the follow-up prompt.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## sc-029 · scenario_chain · structured_extraction

**Tasks:** 4.5

**Q:** [Structured Extraction · 4/5] A manager wants the Batch API for pre-merge blocking checks and overnight reports. How should you split those jobs?

**A:** Synchronous API for blocking pre-merge; batch API only for latency-tolerant overnight jobs.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6; Sample Q11
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## sc-030 · scenario_chain · structured_extraction

**Tasks:** 5.5

**Q:** [Structured Extraction · 5/5] Overall accuracy is 97%. Can you remove all human review?

**A:** No—verify accuracy by document type and field segment; route low-confidence and ambiguous docs to humans.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6
- Official CCAR-F Exam Guide — D5, Task 5.5

