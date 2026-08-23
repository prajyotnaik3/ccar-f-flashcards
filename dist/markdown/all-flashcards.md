# CCAR-F Flashcards (All)

## d1-001 · concept · customer_support, multi_agent_research, developer_productivity

**Q:** What is the agentic loop lifecycle in Claude-based systems?

**A:** Send request → inspect stop_reason → if tool_use, execute tools and append results to history → repeat until stop_reason is end_turn.

**Tags:** agent_loop, stop_reason

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1
- https://docs.anthropic.com/en/docs/agents-and-tools/agent-sdk/overview

---

## d1-002 · decision · customer_support

**Q:** 12% of support cases skip get_customer and call lookup_order by name only, causing wrong refunds. Most effective fix?

**A:** Programmatic prerequisite: block lookup_order and process_refund until get_customer returns a verified customer ID.

**Why:** Financial identity steps need deterministic enforcement; prompts and few-shot alone are probabilistic.

**Tags:** prerequisites, hooks, customer_support

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4; Sample Q1

---

## d1-003 · compare · multi_agent_research

**Q:** Single agent with many tools vs coordinator + specialized subagents for a research pipeline?

**A:** Coordinator + subagents when work decomposes (search, analyze, synthesize), needs isolated context, and clear failure boundaries.

**Tags:** orchestration, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-004 · anti_pattern · multi_agent_research

**Q:** Why must a coordinator not invent subagent outputs without tool results?

**A:** Breaks provenance and reliability; delegate via Task tool and pass explicit context—never hallucinate worker findings.

**Tags:** provenance, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2–1.3

---

## d1-005 · concept · customer_support, multi_agent_research

**Q:** When should an agentic loop continue vs terminate?

**A:** Continue when stop_reason is tool_use; terminate when stop_reason is end_turn.

**Tags:** agent_loop, stop_reason

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-006 · anti_pattern · customer_support, developer_productivity

**Q:** Agentic loop anti-patterns for termination (name three).

**A:** Parsing natural language for completion; arbitrary iteration caps as primary stop; treating assistant text as completion signal.

**Tags:** agent_loop, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-007 · concept · customer_support, multi_agent_research

**Q:** Model-driven tool selection vs pre-configured decision trees?

**A:** Model-driven: Claude picks tools from context each turn. Decision trees/forced sequences bypass model reasoning—use only when deterministic ordering is required.

**Tags:** agent_loop, tool_selection

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-008 · concept · customer_support, multi_agent_research

**Q:** Why append tool results to conversation history between loop iterations?

**A:** So the model can reason about new information and choose the next action based on actual tool output.

**Tags:** agent_loop, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-009 · concept · multi_agent_research

**Q:** What is hub-and-spoke multi-agent architecture?

**A:** Coordinator manages all inter-subagent communication, error handling, and information routing; subagents do not talk directly.

**Tags:** orchestration, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-010 · concept · multi_agent_research

**Q:** Do subagents automatically inherit the coordinator's conversation history?

**A:** No—subagents operate with isolated context; parent history is not inherited automatically.

**Tags:** subagents, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2–1.3

---

## d1-011 · decision · multi_agent_research

**Q:** Research on 'AI in creative industries' covers only visual arts—logs show coordinator assigned digital art, graphic design, photography only. Root cause?

**A:** Coordinator task decomposition too narrow—subagents executed correctly but were assigned incomplete scope.

**Tags:** decomposition, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2; Sample Q7

---

## d1-012 · decision · multi_agent_research

**Q:** How should a coordinator select which subagents to invoke?

**A:** Analyze query requirements and dynamically select needed subagents—not always route through the full pipeline.

**Tags:** coordinator, orchestration

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-013 · decision · multi_agent_research

**Q:** How partition research scope across subagents to reduce duplication?

**A:** Assign distinct subtopics or source types per agent (e.g., web vs documents vs synthesis)—not overlapping queries.

**Tags:** decomposition, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-014 · concept · multi_agent_research

**Q:** What is an iterative refinement loop in multi-agent research?

**A:** Coordinator evaluates synthesis for gaps, re-delegates to search/analysis with targeted queries, re-invokes synthesis until coverage is sufficient.

**Tags:** orchestration, refinement

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-015 · decision · multi_agent_research

**Q:** Why route all subagent communication through the coordinator?

**A:** Observability, consistent error handling, and controlled information flow.

**Tags:** coordinator, observability

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-016 · concept · multi_agent_research, developer_productivity

**Q:** What tool spawns subagents in the Agent SDK, and what must allowedTools include?

**A:** The Task tool; allowedTools must include "Task" for a coordinator to invoke subagents.

**Tags:** Task_tool, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-017 · decision · multi_agent_research

**Q:** How pass prior agent findings to a synthesis subagent?

**A:** Include complete findings directly in the subagent prompt (search results, document analysis)—not rely on automatic inheritance.

**Tags:** context_passing, synthesis

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-018 · decision · multi_agent_research

**Q:** Best practice when passing context between agents for attribution?

**A:** Use structured formats separating content from metadata (URLs, document names, page numbers).

**Tags:** provenance, context_passing

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-019 · decision · multi_agent_research

**Q:** How spawn parallel subagents for lower latency?

**A:** Emit multiple Task tool calls in a single coordinator response—not separate turns per subagent.

**Tags:** parallel, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-020 · decision · multi_agent_research

**Q:** Coordinator prompts: step-by-step procedures vs research goals?

**A:** Specify research goals and quality criteria—enables subagent adaptability vs rigid procedural scripts.

**Tags:** prompting, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-021 · concept · multi_agent_research, developer_productivity

**Q:** What does AgentDefinition configure for each subagent type?

**A:** Description, system prompt, and tool restrictions per subagent role.

**Tags:** AgentDefinition, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-022 · concept · multi_agent_research, developer_productivity

**Q:** What is fork-based session management in multi-agent workflows?

**A:** Create independent branches from a shared analysis baseline to explore divergent approaches (e.g., two testing strategies).

**Tags:** fork_session, session

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3, 1.7

---

## d1-023 · compare · customer_support

**Q:** Programmatic enforcement (hooks, gates) vs prompt-based workflow ordering?

**A:** Prompts have non-zero failure rate; programmatic gates give deterministic compliance when identity verification or financial ops require it.

**Tags:** prerequisites, hooks

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-024 · decision · customer_support

**Q:** Customer message has multiple concerns (billing + return). How should the agent investigate?

**A:** Decompose into distinct items, investigate each in parallel using shared context, then synthesize a unified resolution.

**Tags:** decomposition, customer_support

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-025 · concept · customer_support

**Q:** What must a structured human handoff include when escalating mid-process?

**A:** Customer details, root cause analysis, recommended actions—humans may lack full conversation transcript.

**Tags:** escalation, handoff

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-026 · decision · customer_support

**Q:** Example structured handoff fields for a refund escalation?

**A:** Customer ID, root cause, refund amount, recommended action.

**Tags:** handoff, escalation

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-027 · concept · customer_support, multi_agent_research

**Q:** PostToolUse hook—what does it do?

**A:** Intercepts tool results after execution to transform/normalize data before the model processes them.

**Tags:** hooks, PostToolUse

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-028 · decision · customer_support

**Q:** MCP tools return mixed timestamp formats (Unix, ISO 8601). Best approach before agent reasoning?

**A:** PostToolUse hook to normalize heterogeneous formats into a consistent representation.

**Tags:** hooks, normalization

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-029 · decision · customer_support

**Q:** Business rule: block refunds over $500 and escalate. Hooks vs prompt instructions?

**A:** Tool call interception hook—hooks guarantee compliance; prompts are probabilistic.

**Tags:** hooks, compliance

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-030 · concept · customer_support

**Q:** Tool call interception hooks—purpose?

**A:** Block policy-violating outgoing tool calls (e.g., large refunds) and redirect to alternative workflows (human escalation).

**Tags:** hooks, interception

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-031 · compare · ci_cd, multi_agent_research

**Q:** Fixed sequential pipeline (prompt chaining) vs dynamic adaptive decomposition?

**A:** Sequential pipelines for predictable multi-step reviews; dynamic decomposition for open-ended investigation that adapts to intermediate findings.

**Tags:** decomposition, prompt_chaining

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-032 · decision · ci_cd

**Q:** 14-file PR review misses bugs and gives contradictory feedback. Restructure approach?

**A:** Per-file local analysis passes, then a separate cross-file integration pass—avoids attention dilution.

**Tags:** decomposition, review

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6; Sample Q12

---

## d1-033 · decision · developer_productivity, ci_cd

**Q:** Task: add comprehensive tests to a legacy codebase. Decomposition strategy?

**A:** Map structure → identify high-impact areas → prioritized plan that adapts as dependencies are discovered.

**Tags:** decomposition, testing

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-034 · concept · ci_cd, multi_agent_research

**Q:** What is prompt chaining for task decomposition?

**A:** Break work into sequential focused steps (e.g., analyze each file, then cross-file integration pass).

**Tags:** prompt_chaining

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-035 · concept · developer_productivity

**Q:** Named session resumption in Claude Code—how?

**A:** Use --resume with a session name to continue a specific prior conversation.

**Tags:** session, resume

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-036 · concept · developer_productivity

**Q:** What is fork_session used for?

**A:** Create parallel exploration branches from a shared baseline (e.g., compare two refactoring or testing strategies).

**Tags:** fork_session, session

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-037 · decision · developer_productivity

**Q:** Resume session after code changed vs start fresh?

**A:** Resume when prior context is mostly valid; start fresh with injected summary when prior tool results are stale—more reliable than stale resumes.

**Tags:** session, resume

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-038 · decision · developer_productivity

**Q:** Resuming a session after specific files changed—what to tell the agent?

**A:** Inform about specific file changes for targeted re-analysis—not require full re-exploration of the codebase.

**Tags:** session, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-039 · decision · multi_agent_research

**Q:** Synthesis needs simple fact-checks (85%) but complex search (15%). Reduce latency without over-provisioning?

**A:** Give synthesis a scoped verify_fact tool for simple lookups; complex verifications still delegate through coordinator to search agent.

**Tags:** subagents, tool_scoping

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2–1.3; Sample Q9

---

## d1-040 · scenario_hook · customer_support, multi_agent_research

**Q:** Customer Support and Multi-Agent Research scenarios—shared primary domain?

**A:** D1 (Agentic Architecture & Orchestration)—plus D2 tools/MCP and D5 context/reliability for both.

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d1-041 · concept · multi_agent_research

**Q:** Four coordinator responsibilities in hub-and-spoke orchestration?

**A:** Task decomposition, delegation to subagents, result aggregation, and dynamic selection of which subagents to invoke.

**Tags:** coordinator, orchestration

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-042 · concept · multi_agent_research, developer_productivity

**Q:** Do subagents share memory across separate Task invocations?

**A:** No—each invocation is isolated; context must be explicitly provided in the prompt every time.

**Tags:** subagents, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-043 · concept · ci_cd, multi_agent_research

**Q:** What is attention dilution in multi-step agent workflows?

**A:** Processing too many items in one pass (many files, broad topics) reduces depth and consistency—some areas get superficial treatment while others are detailed.

**Tags:** decomposition, attention

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-044 · concept · multi_agent_research, developer_productivity

**Q:** What is an adaptive investigation plan for task decomposition?

**A:** Generate subtasks based on what is discovered at each step—not a fixed pipeline decided upfront.

**Tags:** decomposition, adaptive

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-045 · decision · customer_support

**Q:** PostToolUse hook: what heterogeneous MCP fields should you normalize before the model sees them?

**A:** Timestamps (Unix vs ISO 8601), numeric status codes, and other inconsistent formats from different backend tools.

**Tags:** hooks, normalization

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-046 · decision · multi_agent_research

**Q:** Web search subagent times out. Best error propagation to the coordinator?

**A:** Structured error context: failure type, attempted query, partial results, and potential alternative approaches.

**Tags:** error_propagation, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2; Sample Q8

---

## d1-047 · anti_pattern · customer_support

**Q:** Agent skips identity verification before refunds. Why is a routing classifier the wrong first fix?

**A:** Problem is tool ordering, not tool availability—a classifier limits which tools exist but does not enforce get_customer before lookup_order/refund.

**Tags:** prerequisites, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4; Sample Q1

---

## d1-048 · decision · customer_support

**Q:** When should a support agent escalate to a human instead of continuing the agentic loop?

**A:** Policy requires human judgment, identity cannot be verified, tool failures persist, or validation/confidence thresholds are not met.

**Tags:** escalation, agent_loop

**Sources:**
- Official CCAR-F Exam Guide — D1; Customer Support scenario

---

## d1-049 · scenario_hook · developer_productivity

**Q:** Developer Productivity scenario—primary domains and D1 focus?

**A:** D2 (tools/MCP), D3 (Claude Code), D1 (delegation/orchestration with built-in tools + MCP servers).

**Tags:** scenarios, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d1-050 · concept · multi_agent_research

**Q:** Typical subagent roles in a multi-agent research pipeline (Exam Scenario 3)?

**A:** Web search, document analysis, synthesis of findings, and report generation—coordinator delegates each role.

**Tags:** subagents, research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3; D1, Task 1.2

---

## d1-051 · anti_pattern · multi_agent_research

**Q:** Subagent catches timeout and returns empty results marked successful. Why wrong?

**A:** Suppresses failure—coordinator cannot recover, retry, or annotate coverage gaps; risks incomplete research output.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-052 · anti_pattern · multi_agent_research

**Q:** Subagent timeout propagates and terminates the entire research workflow. Why wrong?

**A:** Single failures often recoverable with partial results, alternate queries, or gap annotation—unnecessary full termination.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-053 · compare · customer_support, multi_agent_research

**Q:** When is prompt-based workflow guidance enough vs requiring programmatic gates or hooks?

**A:** Prompts suffice for soft ordering and preferences; programmatic enforcement when business rules need deterministic compliance (identity before money, refund caps).

**Tags:** hooks, prerequisites

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4–1.5

---

## d1-054 · anti_pattern · multi_agent_research

**Q:** Subagent retries timeout internally then returns generic 'search unavailable' to coordinator. Gap?

**A:** Hides failure type, attempted query, and partial results—coordinator cannot make informed recovery decisions.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-055 · concept · customer_support, multi_agent_research

**Q:** Two stop_reason values that drive agentic loop control?

**A:** tool_use (continue loop—execute tools and append results) and end_turn (terminate and present response).

**Tags:** stop_reason, agent_loop

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1; Appendix

---

## d1-056 · decision · multi_agent_research

**Q:** Give synthesis agent all web search tools to eliminate coordinator round-trips. Why avoid?

**A:** Over-provisions synthesis—violates separation of concerns and role-specific tool scoping; use scoped tools for common cases only.

**Tags:** tool_scoping, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q9

---

## d1-057 · concept · customer_support

**Q:** What is a programmatic prerequisite gate in a multi-step agent workflow?

**A:** Code or hook that blocks downstream tool calls until a prerequisite step completes (e.g., no refund until verified customer ID).

**Tags:** prerequisites, gates

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d2-001 · concept · customer_support, developer_productivity

**Q:** What does MCP (Model Context Protocol) provide to Claude agents?

**A:** A standard way for AI clients to discover and invoke tools, resources, and prompts from external servers.

**Tags:** mcp_basics

**Sources:**
- Official CCAR-F Exam Guide — D2
- https://modelcontextprotocol.io/introduction

---

## d2-002 · decision · customer_support

**Q:** Refund tool should only run after verified identity. MCP/tool design choice?

**A:** Narrow tool exposure: separate tools with least privilege, or a refund tool that requires verified session token from a prior identity tool.

**Tags:** tool_boundaries, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Customer Support scenario

---

## d2-003 · anti_pattern · developer_productivity

**Q:** Why expose one mega-tool that 'does anything on GitHub' to the agent?

**A:** Harder for the model to select correctly, weak error semantics, and excessive blast radius if mis-invoked.

**Tags:** tool_design

**Sources:**
- Official CCAR-F Exam Guide — D2

---

## d2-004 · compare · developer_productivity

**Q:** Built-in Claude Code tools (Read, Grep, Bash) vs custom MCP tools—when prefer MCP?

**A:** MCP when integrating external systems (GitHub, DB, SaaS) or sharing tools across clients; built-ins for local repo operations.

**Tags:** mcp, claude_code

**Sources:**
- Official CCAR-F Exam Guide — D2, D3

---

## d2-005 · decision · customer_support

**Q:** Tool returns ambiguous error from external API. Best tool-layer behavior?

**A:** Structured error payload to the model (code, message, retryable flag) rather than raw stack traces or silent failure.

**Tags:** errors, reliability

**Sources:**
- Official CCAR-F Exam Guide — D2

---

## d3-001 · concept · code_generation, ci_cd

**Q:** What is CLAUDE.md in Claude Code workflows?

**A:** Project-level instructions and context file that Claude Code reads to align behavior, conventions, and constraints.

**Tags:** claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3
- https://docs.anthropic.com/en/docs/claude-code/overview

---

## d3-002 · compare · code_generation

**Q:** Plan mode vs full Agent mode in Claude Code for a large refactor?

**A:** Plan mode when you want reviewable steps before edits; Agent mode when executing a well-scoped implementation with approvals.

**Tags:** plan_mode, agent_mode

**Sources:**
- Official CCAR-F Exam Guide — D3, Code Generation scenario

---

## d3-003 · decision · ci_cd

**Q:** Running Claude Code in CI for PR review. Critical configuration concern?

**A:** Non-interactive execution, explicit permissions, deterministic outputs (structured findings), and independent verification—not open-ended agent runs.

**Tags:** ci_cd, automation

**Sources:**
- Official CCAR-F Exam Guide — D3, CI/CD scenario

---

## d3-004 · anti_pattern · code_generation

**Q:** Why skip shared CLAUDE.md when multiple developers use Claude Code on one repo?

**A:** Inconsistent conventions, duplicated context in prompts, and drift in how the agent edits code across team members.

**Tags:** claude_md, team

**Sources:**
- Official CCAR-F Exam Guide — D3

---

## d3-005 · scenario_hook · ci_cd

**Q:** CI/CD with Claude Code scenario—primary domains?

**A:** D3 (Claude Code config), D4 (structured output for findings), D5 (reliability in automated runs).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

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

---

## d5-001 · concept · customer_support, multi_agent_research

**Q:** What is context rot in long agent sessions?

**A:** Degraded reasoning as irrelevant history accumulates; mitigated by summarization, scoped context, and tool-first retrieval.

**Tags:** context

**Sources:**
- Official CCAR-F Exam Guide — D5

---

## d5-002 · decision · multi_agent_research

**Q:** Subagents need prior search results. Best context passing approach?

**A:** Explicit structured handoffs (IDs, snippets, citations) via coordinator—not assuming shared implicit memory.

**Tags:** context_passing, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Multi-Agent Research scenario

---

## d5-003 · decision · customer_support

**Q:** Agent loop fails twice on same tool error. Next step?

**A:** Escalate or change strategy (alternate tool, human handoff, degraded path)—not infinite identical retries.

**Tags:** errors, escalation

**Sources:**
- Official CCAR-F Exam Guide — D5

---

## d5-004 · anti_pattern · code_generation

**Q:** Why dump entire repo into context for every Claude Code task?

**A:** Wastes tokens, increases noise, and hides relevant files—use grep/glob tools and scoped reads.

**Tags:** context, claude_code

**Sources:**
- Official CCAR-F Exam Guide — D5, D3

---

## d5-005 · scenario_hook · customer_support

**Q:** Customer Support scenario—domains beyond D1?

**A:** D2 (tool boundaries for refunds/account), D5 (escalation, handoffs, failure handling).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## meta-001 · meta · all

**Q:** What is the official exam code for Claude Certified Architect, Foundations?

**A:** CCAR-F (also written CCA-F or CCAF in older materials).

**Why:** Pearson lists CCAR-F as the current code.

**Tags:** exam_basics

**Sources:**
- Official CCAR-F Exam Guide
- https://docs.anthropic.com/en/docs/about-claude/models

---

## meta-002 · meta · all

**Q:** CCAR-F format: how many questions, time limit, and passing score?

**A:** 60 scenario-based items, 120 minutes, pass at scaled 720 on a 100–1000 scale.

**Tags:** exam_basics

**Sources:**
- Official CCAR-F Exam Guide

---

## meta-003 · meta · all

**Q:** How many scenarios appear on the exam, and from what pool?

**A:** 4 scenarios per exam, drawn randomly from a published bank of 6.

**Tags:** exam_basics, scenarios

**Sources:**
- Official CCAR-F Exam Guide

---

## meta-004 · decision · all

**Q:** Core heuristic when a scenario needs deterministic guarantees (money, identity, schema compliance)?

**A:** Prefer structural/programmatic fixes (hooks, prerequisites, scoped tools, tool_use schemas) over prompt-only instructions.

**Why:** Exam tests judgment: prompts are insufficient for hard guarantees.

**Tags:** heuristic, exam_day

**Sources:**
- Community study guides aligned to Exam Guide patterns
- Official CCAR-F Exam Guide — sample rationales

