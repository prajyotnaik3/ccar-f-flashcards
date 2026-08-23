# CCAR-F Flashcards (All)

## d1-001 · concept · customer_support, multi_agent_research, developer_productivity

**Tasks:** 1.1

**Q:** What is the agentic loop lifecycle in Claude-based systems?

**A:** Send request → inspect stop_reason → if tool_use, execute tools and append results to history → repeat until stop_reason is end_turn.

**Tags:** agent_loop, stop_reason

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1
- https://docs.anthropic.com/en/docs/agents-and-tools/agent-sdk/overview

---

## d1-002 · decision · customer_support

**Tasks:** 1.4

**Q:** 12% of support cases skip get_customer and call lookup_order by name only, causing wrong refunds. Most effective fix?

**A:** Programmatic prerequisite: block lookup_order and process_refund until get_customer returns a verified customer ID.

**Why:** Financial identity steps need deterministic enforcement; prompts and few-shot alone are probabilistic.

**Tags:** prerequisites, hooks, customer_support

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4; Sample Q1

---

## d1-003 · compare · multi_agent_research

**Tasks:** 1.2

**Q:** Single agent with many tools vs coordinator + specialized subagents for a research pipeline?

**A:** Coordinator + subagents when work decomposes (search, analyze, synthesize), needs isolated context, and clear failure boundaries.

**Tags:** orchestration, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-004 · anti_pattern · multi_agent_research

**Tasks:** 1.2, 1.3

**Q:** Why must a coordinator not invent subagent outputs without tool results?

**A:** Breaks provenance and reliability; delegate via Task tool and pass explicit context—never hallucinate worker findings.

**Tags:** provenance, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2–1.3

---

## d1-005 · concept · customer_support, multi_agent_research

**Tasks:** 1.1

**Q:** When should an agentic loop continue vs terminate?

**A:** Continue when stop_reason is tool_use; terminate when stop_reason is end_turn.

**Tags:** agent_loop, stop_reason

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-006 · anti_pattern · customer_support, developer_productivity

**Tasks:** 1.1

**Q:** Agentic loop anti-patterns for termination (name three).

**A:** Parsing natural language for completion; arbitrary iteration caps as primary stop; treating assistant text as completion signal.

**Tags:** agent_loop, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-007 · concept · customer_support, multi_agent_research

**Tasks:** 1.1

**Q:** Model-driven tool selection vs pre-configured decision trees?

**A:** Model-driven: Claude picks tools from context each turn. Decision trees/forced sequences bypass model reasoning—use only when deterministic ordering is required.

**Tags:** agent_loop, tool_selection

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-008 · concept · customer_support, multi_agent_research

**Tasks:** 1.1

**Q:** Why append tool results to conversation history between loop iterations?

**A:** So the model can reason about new information and choose the next action based on actual tool output.

**Tags:** agent_loop, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-009 · concept · multi_agent_research

**Tasks:** 1.2

**Q:** What is hub-and-spoke multi-agent architecture?

**A:** Coordinator manages all inter-subagent communication, error handling, and information routing; subagents do not talk directly.

**Tags:** orchestration, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-010 · concept · multi_agent_research

**Tasks:** 1.2, 1.3

**Q:** Do subagents automatically inherit the coordinator's conversation history?

**A:** No—subagents operate with isolated context; parent history is not inherited automatically.

**Tags:** subagents, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2–1.3

---

## d1-011 · decision · multi_agent_research

**Tasks:** 1.2

**Q:** Research on 'AI in creative industries' covers only visual arts—logs show coordinator assigned digital art, graphic design, photography only. Root cause?

**A:** Coordinator task decomposition too narrow—subagents executed correctly but were assigned incomplete scope.

**Tags:** decomposition, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2; Sample Q7

---

## d1-012 · decision · multi_agent_research

**Tasks:** 1.2

**Q:** How should a coordinator select which subagents to invoke?

**A:** Analyze query requirements and dynamically select needed subagents—not always route through the full pipeline.

**Tags:** coordinator, orchestration

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-013 · decision · multi_agent_research

**Tasks:** 1.2

**Q:** How partition research scope across subagents to reduce duplication?

**A:** Assign distinct subtopics or source types per agent (e.g., web vs documents vs synthesis)—not overlapping queries.

**Tags:** decomposition, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-014 · concept · multi_agent_research

**Tasks:** 1.2

**Q:** What is an iterative refinement loop in multi-agent research?

**A:** Coordinator evaluates synthesis for gaps, re-delegates to search/analysis with targeted queries, re-invokes synthesis until coverage is sufficient.

**Tags:** orchestration, refinement

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-015 · decision · multi_agent_research

**Tasks:** 1.2

**Q:** Why route all subagent communication through the coordinator?

**A:** Observability, consistent error handling, and controlled information flow.

**Tags:** coordinator, observability

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-016 · concept · multi_agent_research, developer_productivity

**Tasks:** 1.3

**Q:** What tool spawns subagents in the Agent SDK, and what must allowedTools include?

**A:** The Task tool; allowedTools must include "Task" for a coordinator to invoke subagents.

**Tags:** Task_tool, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-017 · decision · multi_agent_research

**Tasks:** 1.3

**Q:** How pass prior agent findings to a synthesis subagent?

**A:** Include complete findings directly in the subagent prompt (search results, document analysis)—not rely on automatic inheritance.

**Tags:** context_passing, synthesis

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-018 · decision · multi_agent_research

**Tasks:** 1.3

**Q:** Best practice when passing context between agents for attribution?

**A:** Use structured formats separating content from metadata (URLs, document names, page numbers).

**Tags:** provenance, context_passing

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-019 · decision · multi_agent_research

**Tasks:** 1.3

**Q:** How spawn parallel subagents for lower latency?

**A:** Emit multiple Task tool calls in a single coordinator response—not separate turns per subagent.

**Tags:** parallel, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-020 · decision · multi_agent_research

**Tasks:** 1.3

**Q:** Coordinator prompts: step-by-step procedures vs research goals?

**A:** Specify research goals and quality criteria—enables subagent adaptability vs rigid procedural scripts.

**Tags:** prompting, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-021 · concept · multi_agent_research, developer_productivity

**Tasks:** 1.3

**Q:** What does AgentDefinition configure for each subagent type?

**A:** Description, system prompt, and tool restrictions per subagent role.

**Tags:** AgentDefinition, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-022 · concept · multi_agent_research, developer_productivity

**Tasks:** 1.3

**Q:** What is fork-based session management in multi-agent workflows?

**A:** Create independent branches from a shared analysis baseline to explore divergent approaches (e.g., two testing strategies).

**Tags:** fork_session, session

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3, 1.7

---

## d1-023 · compare · customer_support

**Tasks:** 1.4

**Q:** Programmatic enforcement (hooks, gates) vs prompt-based workflow ordering?

**A:** Prompts have non-zero failure rate; programmatic gates give deterministic compliance when identity verification or financial ops require it.

**Tags:** prerequisites, hooks

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-024 · decision · customer_support

**Tasks:** 1.4

**Q:** Customer message has multiple concerns (billing + return). How should the agent investigate?

**A:** Decompose into distinct items, investigate each in parallel using shared context, then synthesize a unified resolution.

**Tags:** decomposition, customer_support

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-025 · concept · customer_support

**Tasks:** 1.4

**Q:** What must a structured human handoff include when escalating mid-process?

**A:** Customer details, root cause analysis, recommended actions—humans may lack full conversation transcript.

**Tags:** escalation, handoff

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-026 · decision · customer_support

**Tasks:** 1.4

**Q:** Example structured handoff fields for a refund escalation?

**A:** Customer ID, root cause, refund amount, recommended action.

**Tags:** handoff, escalation

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-027 · concept · customer_support, multi_agent_research

**Tasks:** 1.5

**Q:** PostToolUse hook—what does it do?

**A:** Intercepts tool results after execution to transform/normalize data before the model processes them.

**Tags:** hooks, PostToolUse

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-028 · decision · customer_support

**Tasks:** 1.5

**Q:** MCP tools return mixed timestamp formats (Unix, ISO 8601). Best approach before agent reasoning?

**A:** PostToolUse hook to normalize heterogeneous formats into a consistent representation.

**Tags:** hooks, normalization

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-029 · decision · customer_support

**Tasks:** 1.5

**Q:** Business rule: block refunds over $500 and escalate. Hooks vs prompt instructions?

**A:** Tool call interception hook—hooks guarantee compliance; prompts are probabilistic.

**Tags:** hooks, compliance

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-030 · concept · customer_support

**Tasks:** 1.5

**Q:** Tool call interception hooks—purpose?

**A:** Block policy-violating outgoing tool calls (e.g., large refunds) and redirect to alternative workflows (human escalation).

**Tags:** hooks, interception

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-031 · compare · ci_cd, multi_agent_research

**Tasks:** 1.6

**Q:** Fixed sequential pipeline (prompt chaining) vs dynamic adaptive decomposition?

**A:** Sequential pipelines for predictable multi-step reviews; dynamic decomposition for open-ended investigation that adapts to intermediate findings.

**Tags:** decomposition, prompt_chaining

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-032 · decision · ci_cd

**Tasks:** 1.6

**Q:** 14-file PR review misses bugs and gives contradictory feedback. Restructure approach?

**A:** Per-file local analysis passes, then a separate cross-file integration pass—avoids attention dilution.

**Tags:** decomposition, review

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6; Sample Q12

---

## d1-033 · decision · developer_productivity, ci_cd

**Tasks:** 1.6

**Q:** Task: add comprehensive tests to a legacy codebase. Decomposition strategy?

**A:** Map structure → identify high-impact areas → prioritized plan that adapts as dependencies are discovered.

**Tags:** decomposition, testing

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-034 · concept · ci_cd, multi_agent_research

**Tasks:** 1.6

**Q:** What is prompt chaining for task decomposition?

**A:** Break work into sequential focused steps (e.g., analyze each file, then cross-file integration pass).

**Tags:** prompt_chaining

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-035 · concept · developer_productivity

**Tasks:** 1.7

**Q:** Named session resumption in Claude Code—how?

**A:** Use --resume with a session name to continue a specific prior conversation.

**Tags:** session, resume

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-036 · concept · developer_productivity

**Tasks:** 1.7

**Q:** What is fork_session used for?

**A:** Create parallel exploration branches from a shared baseline (e.g., compare two refactoring or testing strategies).

**Tags:** fork_session, session

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-037 · decision · developer_productivity

**Tasks:** 1.7

**Q:** Resume session after code changed vs start fresh?

**A:** Resume when prior context is mostly valid; start fresh with injected summary when prior tool results are stale—more reliable than stale resumes.

**Tags:** session, resume

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-038 · decision · developer_productivity

**Tasks:** 1.7

**Q:** Resuming a session after specific files changed—what to tell the agent?

**A:** Inform about specific file changes for targeted re-analysis—not require full re-exploration of the codebase.

**Tags:** session, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-039 · decision · multi_agent_research

**Tasks:** 1.2, 1.3

**Q:** Synthesis needs simple fact-checks (85%) but complex search (15%). Reduce latency without over-provisioning?

**A:** Give synthesis a scoped verify_fact tool for simple lookups; complex verifications still delegate through coordinator to search agent.

**Tags:** subagents, tool_scoping

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2–1.3; Sample Q9

---

## d1-040 · scenario_hook · customer_support, multi_agent_research

**Tasks:** 1.2

**Q:** Customer Support and Multi-Agent Research scenarios—shared primary domain?

**A:** D1 (Agentic Architecture & Orchestration)—plus D2 tools/MCP and D5 context/reliability for both.

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d1-041 · concept · multi_agent_research

**Tasks:** 1.2

**Q:** Four coordinator responsibilities in hub-and-spoke orchestration?

**A:** Task decomposition, delegation to subagents, result aggregation, and dynamic selection of which subagents to invoke.

**Tags:** coordinator, orchestration

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-042 · concept · multi_agent_research, developer_productivity

**Tasks:** 1.3

**Q:** Do subagents share memory across separate Task invocations?

**A:** No—each invocation is isolated; context must be explicitly provided in the prompt every time.

**Tags:** subagents, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-043 · concept · ci_cd, multi_agent_research

**Tasks:** 1.6

**Q:** What is attention dilution in multi-step agent workflows?

**A:** Processing too many items in one pass (many files, broad topics) reduces depth and consistency—some areas get superficial treatment while others are detailed.

**Tags:** decomposition, attention

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-044 · concept · multi_agent_research, developer_productivity

**Tasks:** 1.6

**Q:** What is an adaptive investigation plan for task decomposition?

**A:** Generate subtasks based on what is discovered at each step—not a fixed pipeline decided upfront.

**Tags:** decomposition, adaptive

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-045 · decision · customer_support

**Tasks:** 1.5

**Q:** PostToolUse hook: what heterogeneous MCP fields should you normalize before the model sees them?

**A:** Timestamps (Unix vs ISO 8601), numeric status codes, and other inconsistent formats from different backend tools.

**Tags:** hooks, normalization

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-046 · decision · multi_agent_research

**Tasks:** 1.2

**Q:** Web search subagent times out. Best error propagation to the coordinator?

**A:** Structured error context: failure type, attempted query, partial results, and potential alternative approaches.

**Tags:** error_propagation, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2; Sample Q8

---

## d1-047 · anti_pattern · customer_support

**Tasks:** 1.4

**Q:** Agent skips identity verification before refunds. Why is a routing classifier the wrong first fix?

**A:** Problem is tool ordering, not tool availability—a classifier limits which tools exist but does not enforce get_customer before lookup_order/refund.

**Tags:** prerequisites, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4; Sample Q1

---

## d1-048 · decision · customer_support

**Tasks:** 5.2

**Q:** When should a support agent escalate to a human instead of continuing the agentic loop?

**A:** Policy requires human judgment, identity cannot be verified, tool failures persist, or validation/confidence thresholds are not met.

**Tags:** escalation, agent_loop

**Sources:**
- Official CCAR-F Exam Guide — D1; Customer Support scenario

---

## d1-049 · scenario_hook · developer_productivity

**Tasks:** 2.3

**Q:** Developer Productivity scenario—primary domains and D1 focus?

**A:** D2 (tools/MCP), D3 (Claude Code), D1 (delegation/orchestration with built-in tools + MCP servers).

**Tags:** scenarios, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d1-050 · concept · multi_agent_research

**Tasks:** 1.2

**Q:** Typical subagent roles in a multi-agent research pipeline (Exam Scenario 3)?

**A:** Web search, document analysis, synthesis of findings, and report generation—coordinator delegates each role.

**Tags:** subagents, research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3; D1, Task 1.2

---

## d1-051 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** Subagent catches timeout and returns empty results marked successful. Why wrong?

**A:** Suppresses failure—coordinator cannot recover, retry, or annotate coverage gaps; risks incomplete research output.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-052 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** Subagent timeout propagates and terminates the entire research workflow. Why wrong?

**A:** Single failures often recoverable with partial results, alternate queries, or gap annotation—unnecessary full termination.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-053 · compare · customer_support, multi_agent_research

**Tasks:** 1.4, 1.5

**Q:** When is prompt-based workflow guidance enough vs requiring programmatic gates or hooks?

**A:** Prompts suffice for soft ordering and preferences; programmatic enforcement when business rules need deterministic compliance (identity before money, refund caps).

**Tags:** hooks, prerequisites

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4–1.5

---

## d1-054 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** Subagent retries timeout internally then returns generic 'search unavailable' to coordinator. Gap?

**A:** Hides failure type, attempted query, and partial results—coordinator cannot make informed recovery decisions.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-055 · concept · customer_support, multi_agent_research

**Tasks:** 1.1

**Q:** Two stop_reason values that drive agentic loop control?

**A:** tool_use (continue loop—execute tools and append results) and end_turn (terminate and present response).

**Tags:** stop_reason, agent_loop

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1; Appendix

---

## d1-056 · decision · multi_agent_research

**Tasks:** 2.3

**Q:** Give synthesis agent all web search tools to eliminate coordinator round-trips. Why avoid?

**A:** Over-provisions synthesis—violates separation of concerns and role-specific tool scoping; use scoped tools for common cases only.

**Tags:** tool_scoping, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q9

---

## d1-057 · concept · customer_support

**Tasks:** 1.4

**Q:** What is a programmatic prerequisite gate in a multi-step agent workflow?

**A:** Code or hook that blocks downstream tool calls until a prerequisite step completes (e.g., no refund until verified customer ID).

**Tags:** prerequisites, gates

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d2-001 · concept · customer_support, developer_productivity

**Tasks:** 2.4

**Q:** What does MCP (Model Context Protocol) provide to Claude agents?

**A:** A standard way for AI clients to discover and invoke tools, resources, and prompts from external servers.

**Tags:** mcp_basics

**Sources:**
- Official CCAR-F Exam Guide — D2
- https://modelcontextprotocol.io/introduction

---

## d2-002 · concept · customer_support, developer_productivity

**Tasks:** 2.1

**Q:** Primary mechanism LLMs use to select among similar tools?

**A:** Tool descriptions—minimal descriptions lead to unreliable selection when tools overlap.

**Tags:** tool_descriptions

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-003 · decision · customer_support

**Tasks:** 2.1

**Q:** Agent calls get_customer for order queries (#12345) instead of lookup_order. Both have minimal descriptions. Best first fix?

**A:** Expand each tool description: input formats, example queries, edge cases, and when to use vs similar tools.

**Why:** Descriptions are the primary selection mechanism; few-shot and routing layers don't fix inadequate descriptions first.

**Tags:** tool_descriptions, customer_support

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-004 · concept · customer_support, developer_productivity

**Tasks:** 2.1

**Q:** What should effective tool descriptions include beyond a one-line summary?

**A:** Expected inputs, outputs, example queries, edge cases, and boundaries explaining when to use vs similar alternatives.

**Tags:** tool_descriptions

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-005 · anti_pattern · developer_productivity, multi_agent_research

**Tasks:** 2.1

**Q:** analyze_content and analyze_document have near-identical descriptions. Likely result?

**A:** Tool misrouting—the model cannot reliably distinguish overlapping tools with ambiguous descriptions.

**Tags:** tool_descriptions, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-006 · decision · multi_agent_research

**Tasks:** 2.1

**Q:** Generic analyze_content overlaps with analyze_document. Rename/fix strategy?

**A:** Rename to purpose-specific names (e.g., extract_web_results) with web-specific descriptions that eliminate overlap.

**Tags:** tool_descriptions, naming

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-007 · decision · multi_agent_research, structured_extraction

**Tasks:** 2.1

**Q:** One generic analyze_document tool does too much. How split it?

**A:** Purpose-specific tools with clear contracts: extract_data_points, summarize_content, verify_claim_against_source.

**Tags:** tool_design, splitting

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-008 · concept · customer_support, developer_productivity

**Tasks:** 2.1

**Q:** How can system prompt wording undermine well-written tool descriptions?

**A:** Keyword-sensitive instructions can create unintended tool associations that override description clarity.

**Tags:** tool_descriptions, system_prompt

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-009 · decision · customer_support

**Tasks:** 2.1

**Q:** Tool selection still wrong after improving descriptions. Next check?

**A:** Review system prompt for keyword-sensitive instructions that might override tool descriptions.

**Tags:** system_prompt, tool_descriptions

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-010 · anti_pattern · developer_productivity

**Tasks:** 2.1

**Q:** Why expose one mega-tool that 'does anything on GitHub' to the agent?

**A:** Harder correct selection, weak error semantics, and excessive blast radius if mis-invoked.

**Tags:** tool_design, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-011 · anti_pattern · customer_support

**Tasks:** 2.1

**Q:** Similar tools misroute. Why is consolidating into lookup_entity not the best first step?

**A:** Valid architecture but higher effort; immediate problem is inadequate descriptions—expand those first (Sample Q2).

**Tags:** tool_descriptions, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-012 · concept · customer_support

**Tasks:** 2.2

**Q:** MCP pattern for communicating tool failures back to the agent?

**A:** The isError flag on tool results, plus structured error metadata—not raw stack traces or generic messages.

**Tags:** errors, mcp, isError

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-013 · concept · customer_support, multi_agent_research

**Tasks:** 2.2

**Q:** Four MCP error categories the exam distinguishes?

**A:** Transient (timeouts, unavailability), validation (invalid input), business (policy violations), permission (access denied).

**Tags:** errors, error_category

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-014 · anti_pattern · customer_support

**Tasks:** 2.2

**Q:** Why return generic 'Operation failed' for all tool errors?

**A:** Prevents the agent from choosing appropriate recovery—retry, explain to user, escalate, or accept empty results.

**Tags:** errors, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-015 · decision · customer_support

**Tasks:** 2.2

**Q:** Structured error metadata fields for MCP tools (name three)?

**A:** errorCategory (transient/validation/permission/business), isRetryable boolean, and human-readable description.

**Tags:** errors, structured_errors

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-016 · decision · customer_support

**Tasks:** 2.2

**Q:** Business rule violation (e.g., refund over policy limit). Error response design?

**A:** isRetryable: false, customer-friendly explanation so the agent can communicate appropriately—not retry endlessly.

**Tags:** errors, business_errors

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-017 · compare · customer_support, multi_agent_research

**Tasks:** 2.2

**Q:** Access failure (timeout) vs valid empty result (no matches)—how should tools report differently?

**A:** Access failure: structured error with retry guidance. Valid empty: successful response indicating no matches—not an error.

**Tags:** errors, empty_results

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-018 · decision · multi_agent_research

**Tasks:** 2.2

**Q:** Transient failure in a subagent. Handle locally vs propagate to coordinator?

**A:** Retry locally when possible; propagate only unresolved errors with partial results and what was attempted.

**Tags:** errors, subagents

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-019 · decision · customer_support

**Tasks:** 2.2

**Q:** Tool returns ambiguous error from external API. Best tool-layer behavior?

**A:** Structured error payload (category, message, retryable flag)—not raw stack traces or silent failure.

**Tags:** errors, reliability

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-020 · concept · multi_agent_research, developer_productivity

**Tasks:** 2.3

**Q:** Why giving an agent 18 tools instead of 4–5 hurts reliability?

**A:** Increases decision complexity and degrades tool selection accuracy.

**Tags:** tool_scoping, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-021 · anti_pattern · multi_agent_research

**Tasks:** 2.3

**Q:** Synthesis agent attempts web searches. Likely tool design issue?

**A:** Agent has tools outside its specialization—scoped access should limit synthesis to synthesis-appropriate tools.

**Tags:** tool_scoping, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-022 · concept · multi_agent_research, developer_productivity

**Tasks:** 2.3

**Q:** What is scoped tool access for subagents?

**A:** Each agent gets only tools for its role, plus limited cross-role tools for specific high-frequency needs.

**Tags:** tool_scoping, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-023 · concept · customer_support, structured_extraction

**Tasks:** 2.3

**Q:** Three tool_choice configuration options on the Claude API?

**A:** "auto" (model may return text), "any" (must call a tool), and forced selection {"type": "tool", "name": "..."}.

**Tags:** tool_choice

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; Appendix

---

## d2-024 · decision · structured_extraction

**Tasks:** 2.3

**Q:** When use tool_choice: "any"?

**A:** When you need guaranteed tool invocation instead of conversational text—e.g., unknown document type among multiple extraction schemas.

**Tags:** tool_choice

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-025 · decision · structured_extraction

**Tasks:** 2.3

**Q:** Must run extract_metadata before enrichment tools. tool_choice approach?

**A:** Force specific tool first with {"type": "tool", "name": "extract_metadata"}, then process enrichment in follow-up turns.

**Tags:** tool_choice, forced_tool

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-026 · decision · multi_agent_research

**Tasks:** 2.3

**Q:** Replace generic fetch_url with what kind of constrained tool?

**A:** Purpose-specific tool like load_document that validates document URLs and rejects non-document URLs.

**Tags:** tool_design, constraints

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-027 · decision · multi_agent_research

**Tasks:** 2.3

**Q:** Synthesis needs simple fact-checks often. Scoped cross-role tool pattern?

**A:** Provide verify_fact for high-frequency simple lookups; route complex verification through coordinator to search agent.

**Tags:** tool_scoping, verify_fact

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; D1 Sample Q9

---

## d2-028 · decision · customer_support

**Tasks:** 2.3

**Q:** Refund tool should only run after verified identity. Tool design choice?

**A:** Least privilege: narrow tool exposure or refund tool requiring verified session token from prior identity tool.

**Tags:** tool_boundaries, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; Customer Support scenario

---

## d2-029 · compare · developer_productivity

**Tasks:** 2.4

**Q:** Project-level vs user-level MCP server configuration?

**A:** Project .mcp.json for shared team tooling (version controlled); user ~/.claude.json for personal/experimental servers.

**Tags:** mcp_config, scoping

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-030 · decision · developer_productivity

**Tasks:** 2.4

**Q:** Store GitHub token for team MCP server without committing secrets?

**A:** Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) with secrets in env—not in the repo.

**Tags:** mcp_config, credentials

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-031 · concept · developer_productivity

**Tasks:** 2.4

**Q:** When are MCP tools from multiple servers available to the agent?

**A:** All configured servers are discovered at connection time—tools from all servers are available simultaneously.

**Tags:** mcp_config, discovery

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-032 · concept · developer_productivity, multi_agent_research

**Tasks:** 2.4

**Q:** MCP resources vs MCP tools—when use resources?

**A:** Resources expose content catalogs (issue summaries, doc hierarchies, DB schemas) to reduce exploratory tool calls.

**Tags:** mcp_resources

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-033 · decision · developer_productivity

**Tasks:** 2.4

**Q:** Agent prefers Grep over a more capable MCP search tool. Fix?

**A:** Enhance MCP tool descriptions to explain capabilities and outputs in detail so the model understands when MCP beats built-ins.

**Tags:** tool_descriptions, mcp

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-034 · decision · developer_productivity

**Tasks:** 2.4

**Q:** Jira integration needed. Community MCP server vs custom?

**A:** Prefer existing community MCP for standard integrations (Jira); custom servers for team-specific workflows.

**Tags:** mcp_config, community

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-035 · compare · developer_productivity

**Tasks:** 2.4, 2.5

**Q:** Built-in Claude Code tools vs custom MCP—when prefer MCP?

**A:** MCP for external systems (GitHub, DB, SaaS) or sharing tools across clients; built-ins for local repo operations.

**Tags:** mcp, claude_code

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4–2.5

---

## d2-036 · concept · developer_productivity

**Tasks:** 2.5

**Q:** Built-in Grep vs Glob—primary use case for each?

**A:** Grep: search file contents for patterns (function names, errors, imports). Glob: match file paths by name/extension patterns.

**Tags:** builtin_tools, Grep, Glob

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-037 · decision · developer_productivity

**Tasks:** 2.5

**Q:** Find all test files named *.test.tsx anywhere in the repo. Which built-in tool?

**A:** Glob with pattern like **/*.test.tsx.

**Tags:** builtin_tools, Glob

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-038 · decision · developer_productivity

**Tasks:** 2.5

**Q:** Find all callers of a function across the codebase. Which built-in tool?

**A:** Grep to search file contents for the function name/reference patterns.

**Tags:** builtin_tools, Grep

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-039 · compare · developer_productivity

**Tasks:** 2.5

**Q:** Read/Write/Edit—when use Edit vs Read + Write?

**A:** Edit for targeted changes with unique anchor text; Read + Write when Edit fails due to non-unique matches.

**Tags:** builtin_tools, Edit, Read, Write

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-040 · decision · developer_productivity

**Tasks:** 2.5

**Q:** Best incremental codebase exploration pattern?

**A:** Grep for entry points → Read to follow imports and trace flows—not read all files upfront.

**Tags:** builtin_tools, exploration

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-041 · decision · developer_productivity

**Tasks:** 2.5

**Q:** Trace usage across wrapper modules exporting many names?

**A:** Identify all exported names first, then Grep for each name across the codebase.

**Tags:** builtin_tools, Grep, exploration

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-042 · scenario_hook · customer_support, multi_agent_research, developer_productivity

**Tasks:** 2.1

**Q:** Which three exam scenarios list D2 as a primary domain?

**A:** Customer Support, Multi-Agent Research, and Developer Productivity.

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d2-043 · concept · customer_support

**Tasks:** 2.1, 2.4

**Q:** Customer Support scenario MCP tools (Exam Scenario 1)—examples?

**A:** get_customer, lookup_order, process_refund, escalate_to_human—backend integration via custom MCP tools.

**Tags:** scenarios, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1

---

## d2-044 · concept · developer_productivity

**Tasks:** 2.5

**Q:** Developer Productivity scenario built-in tools (Exam Scenario 4)?

**A:** Read, Write, Bash, Grep, Glob—plus MCP server integrations for external systems.

**Tags:** scenarios, builtin_tools

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4

---

## d2-045 · anti_pattern · customer_support

**Tasks:** 2.1

**Q:** Improve tool selection with keyword routing layer parsing user input each turn. Why often wrong?

**A:** Over-engineered—bypasses LLM NLU; fix descriptions first; routing doesn't solve ordering or description gaps.

**Tags:** anti_pattern, routing

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-046 · compare · developer_productivity

**Tasks:** 2.4

**Q:** MCP tools vs MCP resources—division of responsibility?

**A:** Tools perform actions (fetch, update, search); resources expose catalogs and static context (schemas, doc trees) to cut exploratory calls.

**Tags:** mcp_tools, mcp_resources

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4; Appendix in-scope

---

## d2-047 · concept · developer_productivity

**Tasks:** 2.2

**Q:** Why return structured isRetryable metadata on errors?

**A:** Lets the agent retry transient failures and avoid wasted retries on non-retryable business or validation errors.

**Tags:** errors, isRetryable

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-048 · concept · developer_productivity

**Tasks:** 2.5

**Q:** Built-in Bash tool—when use vs Grep?

**A:** Bash for shell commands and scripted operations; Grep for searching file contents for patterns across the codebase.

**Tags:** builtin_tools, Bash

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5; Scenario 4; Appendix

---

## d2-049 · concept · customer_support, structured_extraction

**Tasks:** 2.3, 4.3

**Q:** tool_choice: "auto"—what can the model return?

**A:** The model may respond with conversational text instead of calling a tool—no guaranteed tool invocation.

**Tags:** tool_choice, auto

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; D4 Task 4.3

---

## d2-050 · anti_pattern · customer_support

**Tasks:** 2.1

**Q:** Similar tools misroute. Add 5–8 few-shot tool-selection examples first?

**A:** Adds token overhead without fixing root cause—inadequate tool descriptions are the primary selection mechanism.

**Tags:** tool_descriptions, few_shot, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-051 · concept · developer_productivity

**Tasks:** 2.5

**Q:** Edit built-in tool—how does it modify files?

**A:** Targeted modifications using unique text matching as anchor—fails when anchor text is not unique.

**Tags:** builtin_tools, Edit

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-052 · decision · customer_support

**Tasks:** 2.2

**Q:** errorCategory for policy violation refund blocked?

**A:** Business error with isRetryable: false and customer-friendly explanation—not transient or permission.

**Tags:** errors, business_errors

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d3-001 · concept · code_generation, developer_productivity

**Tasks:** 3.1

**Q:** What is CLAUDE.md in Claude Code workflows?

**A:** Project instructions and context Claude Code loads to align behavior, conventions, and constraints.

**Tags:** claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1
- https://docs.anthropic.com/en/docs/claude-code/overview

---

## d3-002 · concept · code_generation, developer_productivity

**Tasks:** 3.1

**Q:** CLAUDE.md configuration hierarchy (three levels)?

**A:** User (~/.claude/CLAUDE.md), project (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files).

**Tags:** claude_md, hierarchy

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-003 · decision · code_generation

**Tasks:** 3.1

**Q:** New teammate doesn't receive team coding standards in Claude Code. Likely cause?

**A:** Instructions are in user-level ~/.claude/CLAUDE.md—not shared via version control; move to project-level config.

**Tags:** claude_md, hierarchy

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-004 · concept · code_generation

**Tasks:** 3.1

**Q:** What is @import syntax in CLAUDE.md?

**A:** References external files to keep CLAUDE.md modular—import standards files relevant to each package.

**Tags:** claude_md, import

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-005 · decision · code_generation

**Tasks:** 3.1

**Q:** Monolithic CLAUDE.md is hard to maintain. Alternative organization?

**A:** Split into focused files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md).

**Tags:** claude_md, rules

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-006 · decision · code_generation

**Tasks:** 3.1

**Q:** Inconsistent Claude Code behavior across sessions—how diagnose loaded config?

**A:** Use /memory to verify which memory files are loaded and what context is active.

**Tags:** claude_md, memory

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-007 · anti_pattern · code_generation

**Tasks:** 3.1

**Q:** Why skip shared project CLAUDE.md when multiple developers use Claude Code?

**A:** Inconsistent conventions, duplicated prompt context, and drift in how the agent edits code across teammates.

**Tags:** claude_md, team

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-008 · decision · code_generation, ci_cd

**Tasks:** 3.2

**Q:** Team /review slash command for every developer on clone. Where create it?

**A:** .claude/commands/ in the project repository—version-controlled and shared on clone/pull.

**Tags:** slash_commands

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2; Sample Q4

---

## d3-009 · compare · code_generation

**Tasks:** 3.2

**Q:** Project-scoped vs user-scoped slash commands?

**A:** .claude/commands/ in repo (shared via git) vs ~/.claude/commands/ (personal, not version controlled).

**Tags:** slash_commands, scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-010 · concept · code_generation, developer_productivity

**Tasks:** 3.2

**Q:** Skill frontmatter options in .claude/skills/SKILL.md (name three)?

**A:** context: fork, allowed-tools, and argument-hint.

**Tags:** skills, frontmatter

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-011 · decision · code_generation

**Tasks:** 3.2

**Q:** Skill produces verbose codebase analysis output. Frontmatter to isolate it?

**A:** context: fork—runs skill in isolated sub-agent context so output doesn't pollute main conversation.

**Tags:** skills, context_fork

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-012 · decision · code_generation

**Tasks:** 3.2

**Q:** Skill should only write files, not run destructive shell commands. Frontmatter?

**A:** allowed-tools restricting tool access during skill execution (e.g., file write operations only).

**Tags:** skills, allowed_tools

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-013 · decision · code_generation

**Tasks:** 3.2

**Q:** Developer invokes skill without required arguments. Frontmatter help?

**A:** argument-hint prompts for required parameters when the skill is invoked without them.

**Tags:** skills, argument_hint

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-014 · compare · code_generation

**Tasks:** 3.2

**Q:** Skills vs CLAUDE.md—when use each?

**A:** Skills: on-demand task-specific workflows. CLAUDE.md: always-loaded universal standards for the project.

**Tags:** skills, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-015 · decision · code_generation

**Tasks:** 3.2

**Q:** Personal skill customization without affecting teammates?

**A:** Create personal variants in ~/.claude/skills/ with different names—not in shared project skills.

**Tags:** skills, scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-016 · concept · code_generation

**Tasks:** 3.3

**Q:** How do .claude/rules/ path-specific rules activate?

**A:** YAML frontmatter paths field with glob patterns—rules load only when editing matching files.

**Tags:** rules, path_scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-017 · decision · code_generation

**Tasks:** 3.3

**Q:** Test files spread as Button.test.tsx next to Button.tsx. Apply test conventions automatically?

**A:** .claude/rules/ with glob paths like **/*.test.tsx—applies by file type across all directories.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-018 · decision · code_generation

**Tasks:** 3.3

**Q:** React, API, and DB areas need different conventions; tests scattered everywhere. Best maintainable approach?

**A:** .claude/rules/ with YAML frontmatter glob patterns (e.g., paths: ["**/*.test.tsx"], ["src/api/**/*"])—not inference from one monolithic CLAUDE.md.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-019 · compare · code_generation

**Tasks:** 3.3

**Q:** Path-specific rules vs subdirectory CLAUDE.md for scattered test files?

**A:** Path-specific glob rules apply by file pattern anywhere in the tree; subdirectory CLAUDE.md is directory-bound.

**Tags:** rules, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-020 · concept · code_generation

**Tasks:** 3.3

**Q:** Benefit of path-scoped rules loading only on matching files?

**A:** Reduces irrelevant context and token usage—conventions apply only when relevant.

**Tags:** rules, context

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-021 · decision · code_generation

**Tasks:** 3.4

**Q:** Restructure monolith into microservices—dozens of files, architectural decisions. Approach?

**A:** Plan mode: explore codebase, understand dependencies, design approach before making changes.

**Tags:** plan_mode

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-022 · compare · code_generation

**Tasks:** 3.4

**Q:** Plan mode vs direct execution—when use each?

**A:** Plan mode: large-scale, multi-file, architectural, multiple valid approaches. Direct execution: simple, well-scoped single changes.

**Tags:** plan_mode, direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-023 · decision · code_generation

**Tasks:** 3.4

**Q:** Single-file bug fix with clear stack trace. Plan mode or direct execution?

**A:** Direct execution—well-understood change with clear scope.

**Tags:** direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-024 · concept · code_generation

**Tasks:** 3.4

**Q:** What is the Explore subagent used for in Claude Code?

**A:** Isolates verbose discovery output and returns summaries—preserves main conversation context during exploration.

**Tags:** Explore_subagent, context

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-025 · decision · code_generation

**Tasks:** 3.4

**Q:** Library migration affecting 45+ files—workflow pattern?

**A:** Plan mode for investigation and design, then direct execution to implement the planned approach.

**Tags:** plan_mode, direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-026 · anti_pattern · code_generation

**Tasks:** 3.4

**Q:** Start monolith-to-microservices in direct execution, switch to plan if complexity emerges. Why wrong?

**A:** Complexity is already stated—plan first prevents costly rework from late-discovered dependencies.

**Tags:** plan_mode, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-027 · decision · code_generation

**Tasks:** 3.5

**Q:** Natural language transformation spec produces inconsistent code. Best fix?

**A:** Provide 2–3 concrete input/output examples showing expected transformations.

**Tags:** iterative_refinement, examples

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-028 · concept · code_generation

**Tasks:** 3.5

**Q:** Test-driven iteration pattern with Claude Code?

**A:** Write tests first (behavior, edge cases, performance), then iterate by sharing test failures to guide fixes.

**Tags:** iterative_refinement, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-029 · concept · code_generation

**Tasks:** 3.5

**Q:** What is the interview pattern in Claude Code workflows?

**A:** Have Claude ask clarifying questions to surface design considerations before implementing in unfamiliar domains.

**Tags:** iterative_refinement, interview

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-030 · compare · code_generation

**Tasks:** 3.5

**Q:** Fix multiple issues in one message vs sequentially?

**A:** Single message when fixes interact; sequential iteration when issues are independent.

**Tags:** iterative_refinement

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-031 · decision · code_generation

**Tasks:** 3.5

**Q:** Migration script mishandles null edge cases. Iteration approach?

**A:** Provide specific test cases with example input and expected output for the failing edge case.

**Tags:** iterative_refinement, edge_cases

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-032 · decision · ci_cd

**Tasks:** 3.6

**Q:** CI job hangs—Claude Code waiting for interactive input. Fix?

**A:** Use -p (or --print) flag for non-interactive mode: process prompt, output result, exit.

**Tags:** ci_cd, non_interactive

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6; Sample Q10

---

## d3-033 · decision · ci_cd

**Tasks:** 3.6

**Q:** Post structured PR review findings as inline comments from CI. CLI flags?

**A:** --output-format json with --json-schema for machine-parseable structured findings.

**Tags:** ci_cd, structured_output

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-034 · concept · ci_cd

**Tasks:** 3.6

**Q:** How provide project context to CI-invoked Claude Code?

**A:** CLAUDE.md with testing standards, fixture conventions, and review criteria loaded automatically.

**Tags:** ci_cd, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-035 · concept · ci_cd

**Tasks:** 3.6

**Q:** Why use an independent Claude instance to review code it generated in the same session?

**A:** Session context isolation—generator retains reasoning context and is less likely to question its own decisions.

**Tags:** ci_cd, self_review

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-036 · decision · ci_cd

**Tasks:** 3.6

**Q:** Re-run PR review after new commits—avoid duplicate inline comments?

**A:** Include prior review findings in context; instruct Claude to report only new or still-unaddressed issues.

**Tags:** ci_cd, review

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-037 · decision · ci_cd

**Tasks:** 3.6

**Q:** CI test generation suggests scenarios already in the suite. Context fix?

**A:** Provide existing test files in context so generation avoids duplicate coverage.

**Tags:** ci_cd, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-038 · decision · ci_cd, code_generation

**Tasks:** 3.6

**Q:** Reduce low-value generated tests in Claude Code?

**A:** Document testing standards, valuable test criteria, and available fixtures in CLAUDE.md.

**Tags:** claude_md, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-039 · decision · ci_cd

**Tasks:** 3.6

**Q:** Running Claude Code in CI for PR review. Critical configuration concerns?

**A:** Non-interactive (-p), explicit permissions, structured/deterministic outputs, independent review instance—not open-ended agent runs.

**Tags:** ci_cd, automation

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-040 · anti_pattern · ci_cd

**Tasks:** 3.6

**Q:** CI non-interactive flags that do NOT exist (name two)?

**A:** CLAUDE_HEADLESS env var and --batch flag—use -p/--print instead.

**Tags:** ci_cd, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6; Sample Q10

---

## d3-041 · scenario_hook · code_generation

**Tasks:** 3.4, 5.1

**Q:** Code Generation scenario (Scenario 2)—primary domains?

**A:** D3 (Claude Code config/workflows) and D5 (context management/reliability).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d3-042 · scenario_hook · ci_cd

**Tasks:** 3.6, 4.1

**Q:** CI/CD with Claude Code scenario (Scenario 5)—primary domains?

**A:** D3 (Claude Code) and D4 (prompt engineering/structured output for review findings).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d3-043 · scenario_hook · developer_productivity, code_generation

**Tasks:** 3.2, 3.4

**Q:** Scenario 2 tools: slash commands, CLAUDE.md, plan mode—what is being tested?

**A:** Integrating Claude Code into dev workflow: team config, custom commands, and when to plan vs execute directly.

**Tags:** scenarios, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2

---

## d3-044 · concept · code_generation

**Tasks:** 3.3

**Q:** Example path-scoped rule for Terraform files only?

**A:** .claude/rules/ file with frontmatter paths: ["terraform/**/*"] loading only when editing matching files.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-045 · anti_pattern · code_generation

**Tasks:** 3.3

**Q:** Put all area conventions in root CLAUDE.md headers—rely on Claude to infer which applies. Why unreliable?

**A:** Relies on inference vs explicit path matching—rules with glob patterns give deterministic automatic application.

**Tags:** rules, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-046 · anti_pattern · code_generation

**Tasks:** 3.4

**Q:** Monolith-to-microservices: direct execution with comprehensive upfront structure instructions. Why wrong?

**A:** Assumes structure without codebase exploration—dependencies discovered late cause costly rework; plan first.

**Tags:** plan_mode, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-047 · anti_pattern · code_generation

**Tasks:** 3.3

**Q:** Auto-apply conventions via skills in .claude/skills/ instead of path rules. Why insufficient?

**A:** Skills require manual invocation or model choice—not deterministic path-based automatic application.

**Tags:** skills, rules, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-048 · decision · code_generation

**Tasks:** 3.5

**Q:** Test-driven iteration before implementation—what should tests cover?

**A:** Expected behavior, edge cases, and performance requirements—iterate by sharing failures with Claude.

**Tags:** iterative_refinement, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-049 · decision · code_generation

**Tasks:** 3.2

**Q:** context: fork for skills—another use case besides verbose codebase analysis?

**A:** Exploratory brainstorming of alternatives—isolates speculative output from the main session.

**Tags:** skills, context_fork

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-050 · scenario_hook · developer_productivity

**Tasks:** 1.2, 2.5, 3.2

**Q:** Developer Productivity scenario (Scenario 4)—primary domains?

**A:** D2 (built-in tools + MCP), D3 (Claude Code workflows), D1 (delegation/orchestration).

**Tags:** scenarios, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

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

---

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

**Q:** Risk of progressive summarization in long support sessions?

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

**Q:** Preserve order amounts and dates across a long support conversation?

**A:** Extract transactional facts into a persistent case facts block in each prompt—outside summarized history.

**Tags:** case_facts, context

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-005 · decision · customer_support

**Tasks:** 5.1

**Q:** Order lookup returns 40+ fields but only 5 matter for returns. Context fix?

**A:** Trim verbose tool outputs to relevant fields before they accumulate in conversation context.

**Tags:** trimming, tool_results

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-006 · decision · multi_agent_research

**Tasks:** 5.1

**Q:** Mitigate lost-in-the-middle when aggregating subagent results?

**A:** Place key findings summary at the beginning; organize detailed results with explicit section headers.

**Tags:** lost_in_middle, aggregation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-007 · decision · multi_agent_research

**Tasks:** 5.1

**Q:** Downstream synthesis agent has limited context budget. Upstream agent output design?

**A:** Return structured key facts, citations, and relevance scores—not verbose reasoning chains.

**Tags:** structured_output, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-008 · concept · customer_support, multi_agent_research

**Tasks:** 5.1

**Q:** Why pass complete conversation history in subsequent API requests?

**A:** Maintains conversational coherence—the model needs prior turns to reason about the ongoing case.

**Tags:** conversation_history

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-009 · decision · customer_support

**Tasks:** 5.1

**Q:** Multi-issue support session (billing + return). Context layer approach?

**A:** Persist structured issue data (order IDs, amounts, statuses) in a separate context layer for each concern.

**Tags:** case_facts, multi_issue

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-010 · concept · customer_support

**Tasks:** 5.2

**Q:** Three appropriate escalation triggers (beyond 'complex case')?

**A:** Customer explicitly requests human, policy exception/gap, and inability to make meaningful progress.

**Tags:** escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-011 · decision · customer_support

**Tasks:** 5.2

**Q:** 55% FCR—escalates easy cases, handles hard policy exceptions alone. Best calibration fix?

**A:** Add explicit escalation criteria with few-shot examples showing escalate vs resolve autonomously.

**Tags:** escalation, few_shot

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-012 · anti_pattern · customer_support

**Tasks:** 5.2

**Q:** Route to human when self-reported confidence score is below threshold. Why unreliable?

**A:** LLM confidence is poorly calibrated—agent may be wrongly confident on hard cases and uncertain on easy ones.

**Tags:** escalation, confidence, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-013 · anti_pattern · customer_support

**Tasks:** 5.2

**Q:** Escalate on negative sentiment threshold. Why wrong for calibration?

**A:** Sentiment doesn't correlate with case complexity—the actual issue is unclear escalation boundaries.

**Tags:** escalation, sentiment, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-014 · decision · customer_support

**Tasks:** 5.2

**Q:** Customer explicitly demands a human agent. Response?

**A:** Honor immediately—do not attempt investigation first when they explicitly request a human.

**Tags:** escalation, customer_request

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-015 · decision · customer_support

**Tasks:** 5.2

**Q:** Frustrated customer, issue is within agent capability. Approach?

**A:** Acknowledge frustration and offer resolution; escalate only if customer reiterates preference for human.

**Tags:** escalation, de_escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-016 · decision · customer_support

**Tasks:** 5.2

**Q:** Policy silent on competitor price matching (only covers own-site adjustments). Action?

**A:** Escalate—policy gap/exception case, not autonomous resolution.

**Tags:** escalation, policy_gap

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-017 · decision · customer_support

**Tasks:** 5.2

**Q:** get_customer returns multiple matches. What should the agent do?

**A:** Ask for additional identifiers—never pick a match heuristically.

**Tags:** ambiguity, identity

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2

---

## d5-018 · decision · multi_agent_research

**Tasks:** 5.1

**Q:** Subagents need prior search results. Best context passing?

**A:** Explicit structured handoffs (IDs, snippets, citations) via coordinator—not implicit shared memory.

**Tags:** context_passing, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1; Multi-Agent Research scenario

---

## d5-019 · decision · multi_agent_research

**Tasks:** 5.3

**Q:** Web search subagent timeout—best error propagation to coordinator?

**A:** Structured context: failure type, attempted query, partial results, and alternative approaches.

**Tags:** error_propagation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3; Sample Q8

---

## d5-020 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** Subagent returns empty results marked successful after timeout. Why anti-pattern?

**A:** Silently suppresses errors—coordinator cannot recover or annotate coverage gaps.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3; Sample Q8

---

## d5-021 · decision · multi_agent_research

**Tasks:** 5.3

**Q:** Synthesis output after partial subagent failures—what include?

**A:** Coverage annotations: which findings are well-supported vs which topic areas have gaps from unavailable sources.

**Tags:** synthesis, coverage

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## d5-022 · decision · customer_support, multi_agent_research

**Tasks:** 5.3

**Q:** Agent loop fails twice on same tool error. Next step?

**A:** Escalate or change strategy (alternate tool, human handoff)—not infinite identical retries.

**Tags:** errors, escalation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## d5-023 · concept · code_generation, developer_productivity

**Tasks:** 5.4

**Q:** Scratchpad files in long Claude Code exploration sessions—purpose?

**A:** Persist key findings across context boundaries; reference for later questions to counteract degradation.

**Tags:** scratchpad, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-024 · decision · code_generation, developer_productivity

**Tasks:** 5.4

**Q:** Verbose codebase exploration fills context. Claude Code command to reduce usage?

**A:** /compact to condense verbose discovery output during extended sessions.

**Tags:** compact, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4; Appendix

---

## d5-025 · decision · developer_productivity

**Tasks:** 5.4

**Q:** Multi-phase codebase exploration—context pattern between phases?

**A:** Summarize key findings from one phase, inject summary into context before spawning subagents for the next.

**Tags:** exploration, summarization

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-026 · concept · multi_agent_research, developer_productivity

**Tasks:** 5.4

**Q:** Crash recovery pattern for multi-agent workflows?

**A:** Each agent exports state to a known location; coordinator loads manifest on resume and injects into prompts.

**Tags:** crash_recovery, manifests

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-027 · anti_pattern · code_generation, developer_productivity

**Tasks:** 2.5, 5.4

**Q:** Why dump entire repo into context for every Claude Code task?

**A:** Wastes tokens and adds noise—use Grep/Glob and scoped reads incrementally.

**Tags:** context, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4; D2 Task 2.5

---

## d5-028 · concept · structured_extraction

**Tasks:** 5.5

**Q:** 97% overall extraction accuracy—why not automate all human review?

**A:** Aggregate metrics may mask poor performance on specific document types or individual fields.

**Tags:** human_review, metrics

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-029 · decision · structured_extraction

**Tasks:** 5.5

**Q:** Ongoing quality monitoring for high-confidence extractions?

**A:** Stratified random sampling to measure error rates and detect novel error patterns.

**Tags:** human_review, sampling

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-030 · decision · structured_extraction

**Tasks:** 5.5

**Q:** Calibrate human review routing for extractions?

**A:** Model outputs field-level confidence; calibrate thresholds using labeled validation sets.

**Tags:** confidence, human_review

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-031 · decision · structured_extraction

**Tasks:** 5.5

**Q:** Before reducing human review on high-confidence extractions—verify what?

**A:** Accuracy by document type and field segment—consistent performance across all segments.

**Tags:** human_review, segmentation

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.5

---

## d5-032 · decision · structured_extraction

**Tasks:** 5.5

**Q:** Limited reviewer capacity—prioritize which extractions for human review?

**A:** Low model confidence, ambiguous source documents, or contradictory source data.

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

**Q:** Subagent output for downstream synthesis—provenance requirement?

**A:** Structured claim-source mappings (URLs, document names, excerpts) preserved through synthesis.

**Tags:** provenance, claim_source

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-035 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** Two credible sources report different statistics. Synthesis handling?

**A:** Annotate conflict with source attribution—do not arbitrarily pick one value.

**Tags:** provenance, conflicts

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-036 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** Why require publication/collection dates in structured subagent outputs?

**A:** Enables correct temporal interpretation—prevents time differences being misread as contradictions.

**Tags:** temporal, provenance

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-037 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** Research report structure for contested vs established findings?

**A:** Explicit sections distinguishing well-established findings from contested ones with methodological context.

**Tags:** synthesis, provenance

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-038 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** Synthesis output formatting for mixed content types?

**A:** Render appropriately—financial data as tables, news as prose, technical findings as structured lists.

**Tags:** synthesis, formatting

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-039 · scenario_hook · customer_support, multi_agent_research, structured_extraction

**Tasks:** 5.1, 5.2, 5.3

**Q:** Which three scenarios list D5 as a primary domain?

**A:** Customer Support, Multi-Agent Research, and Structured Data Extraction.

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d5-040 · scenario_hook · code_generation

**Tasks:** 3.4, 5.1

**Q:** Code Generation scenario (Scenario 2)—D5 focus areas?

**A:** Context preservation across edits, plan vs execute context management, and session reliability.

**Tags:** scenarios, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2

---

## d5-041 · decision · multi_agent_research

**Tasks:** 5.1

**Q:** Subagent structured outputs for downstream synthesis—required metadata?

**A:** Dates, source locations, and methodological context—not just claims without provenance context.

**Tags:** metadata, subagents

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.1

---

## d5-042 · anti_pattern · customer_support

**Tasks:** 5.2

**Q:** Deploy classifier model to predict escalation before agent runs. Why over-engineered first step?

**A:** Requires labeled data and ML infra when prompt criteria with few-shot hasn't been tried yet.

**Tags:** escalation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.2; Sample Q3

---

## d5-043 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** Subagent retries then returns generic 'search unavailable' to coordinator. Problem?

**A:** Hides failure type, attempted query, and partial results—coordinator cannot make informed recovery.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3; Sample Q8

---

## d5-044 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** Single subagent failure terminates entire multi-agent workflow. Why wrong?

**A:** Often recoverable with partial results, alternate queries, or gap annotations—unnecessary full termination.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.3

---

## d5-045 · decision · developer_productivity, code_generation

**Tasks:** 5.4

**Q:** Long codebase exploration—delegate specific questions while preserving coordination?

**A:** Spawn subagents for focused tasks (find test files, trace refund flow) while main agent keeps high-level coordination.

**Tags:** subagents, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## d5-046 · decision · multi_agent_research

**Tasks:** 5.6

**Q:** Document analysis finds conflicting values from sources. Before synthesis?

**A:** Complete analysis with conflicts included and explicitly annotated—let coordinator reconcile before passing to synthesis.

**Tags:** provenance, conflicts

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## d5-047 · decision · developer_productivity

**Tasks:** 5.4

**Q:** Scratchpad file during exploration—how use for follow-up questions?

**A:** Record key findings in scratchpad; reference it for subsequent questions to counteract context degradation.

**Tags:** scratchpad, exploration

**Sources:**
- Official CCAR-F Exam Guide — D5, Task 5.4

---

## meta-001 · meta · all

**Tasks:** exam-format

**Q:** What is the official exam code for Claude Certified Architect, Foundations?

**A:** CCAR-F (also written CCA-F or CCAF in older materials).

**Why:** Pearson lists CCAR-F as the current code.

**Tags:** exam_basics

**Sources:**
- Official CCAR-F Exam Guide
- https://docs.anthropic.com/en/docs/about-claude/models

---

## meta-002 · meta · all

**Tasks:** exam-format

**Q:** CCAR-F format: how many questions, time limit, and passing score?

**A:** 60 scenario-based items, 120 minutes, pass at scaled 720 on a 100–1000 scale.

**Tags:** exam_basics

**Sources:**
- Official CCAR-F Exam Guide

---

## meta-003 · meta · all

**Tasks:** scenarios

**Q:** How many scenarios appear on the exam, and from what pool?

**A:** 4 scenarios per exam, drawn randomly from a published bank of 6.

**Tags:** exam_basics, scenarios

**Sources:**
- Official CCAR-F Exam Guide

---

## meta-004 · decision · all

**Tasks:** cross-domain

**Q:** Core heuristic when a scenario needs deterministic guarantees (money, identity, schema compliance)?

**A:** Prefer structural/programmatic fixes (hooks, prerequisites, scoped tools, tool_use schemas) over prompt-only instructions.

**Why:** Exam tests judgment: prompts are insufficient for hard guarantees.

**Tags:** heuristic, exam_day

**Sources:**
- Community study guides aligned to Exam Guide patterns
- Official CCAR-F Exam Guide — sample rationales

---

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

**Q:** [Customer Support · 2/5] Production data: 12% of cases skip get_customer and call lookup_order by name only, causing wrong refunds. Best fix?

**A:** Programmatic prerequisite blocking lookup_order and process_refund until get_customer returns verified customer ID.

**Why:** Money and identity need deterministic enforcement—not prompts alone.

**Tags:** scenario_chain, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1; Sample Q1
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## sc-003 · scenario_chain · customer_support

**Tasks:** 2.1

**Q:** [Customer Support · 3/5] Logs show get_customer called for order queries (#12345) instead of lookup_order. Both tools have minimal descriptions. First fix?

**A:** Expand tool descriptions with inputs, example queries, edge cases, and when to use each vs similar tools.

**Tags:** scenario_chain, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1; Sample Q2
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## sc-004 · scenario_chain · customer_support

**Tasks:** 5.2

**Q:** [Customer Support · 4/5] 55% first-contact resolution—agent escalates easy cases and handles hard policy exceptions alone. Best calibration fix?

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

**Q:** [Code Generation · 3/5] Assignment: split monolith into microservices—dozens of files, unclear boundaries. What mode first?

**A:** Plan mode—explore dependencies and design before editing; direct execution risks costly rework.

**Tags:** scenario_chain, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2; Sample Q5
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## sc-009 · scenario_chain · code_generation

**Tasks:** 3.3

**Q:** [Code Generation · 4/5] Tests live as *.test.tsx next to components across the repo. How auto-apply test conventions when generating code?

**A:** .claude/rules/ with glob paths like **/*.test.tsx—not directory-bound CLAUDE.md or inference from headers.

**Tags:** scenario_chain, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2; Sample Q6
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## sc-010 · scenario_chain · code_generation

**Tasks:** 5.4

**Q:** [Code Generation · 5/5] Long refactor session—model starts citing generic patterns instead of files it read earlier. Mitigation?

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

**Q:** [Multi-Agent Research · 2/5] Topic 'AI in creative industries'—final report covers only visual arts; coordinator assigned digital art, graphic design, photography only. Root cause?

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

**Q:** [Multi-Agent Research · 4/5] Synthesis needs many simple fact-checks (85%) but some deep searches (15%). Reduce latency without over-provisioning synthesis?

**A:** Scoped verify_fact tool on synthesis for simple lookups; complex cases still route through coordinator to search agent.

**Tags:** scenario_chain, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3; Sample Q9
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## sc-015 · scenario_chain · multi_agent_research

**Tasks:** 5.6

**Q:** [Multi-Agent Research · 5/5] Final report must preserve citations through synthesis. What require from subagents?

**A:** Structured claim–source mappings (URLs, excerpts, dates) preserved through synthesis—not compressed summaries without attribution.

**Tags:** scenario_chain, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3
- Official CCAR-F Exam Guide — D5, Task 5.6

---

## sc-016 · scenario_chain · developer_productivity

**Tasks:** 2.4, 2.5

**Q:** [Developer Productivity · 1/5] Agent helps engineers explore legacy codebases using built-in tools and MCP. When prefer MCP over Grep/Glob?

**A:** External systems (GitHub, DB, SaaS) or shared team integrations—not local file search.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.4–2.5

---

## sc-017 · scenario_chain · developer_productivity

**Tasks:** 2.5

**Q:** [Developer Productivity · 2/5] Find all callers of a function across the monorepo. Which built-in tool first?

**A:** Grep for content patterns across files—not Glob (paths) or reading every file upfront.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## sc-018 · scenario_chain · developer_productivity

**Tasks:** 2.4

**Q:** [Developer Productivity · 3/5] Agent prefers Grep over your team's richer MCP code-search tool. Fix?

**A:** Enhance MCP tool descriptions so the model understands when MCP beats built-in search.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## sc-019 · scenario_chain · developer_productivity

**Tasks:** 2.5, 5.4

**Q:** [Developer Productivity · 4/5] Large codebase exploration without reading every file. Pattern?

**A:** Grep entry points → Read to follow imports → scratchpad key findings for later questions.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.5; D5, Task 5.4

---

## sc-020 · scenario_chain · developer_productivity

**Tasks:** 2.4

**Q:** [Developer Productivity · 5/5] Share GitHub MCP with the team; keep experimental personal server. Config locations?

**A:** Team server in project .mcp.json with ${TOKEN}; personal server in ~/.claude.json.

**Tags:** scenario_chain, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## sc-021 · scenario_chain · ci_cd

**Tasks:** 3.6

**Q:** [CI/CD · 1/5] Pipeline runs claude 'Review this PR' but hangs waiting for input. Fix?

**A:** Use -p (--print) for non-interactive mode—process prompt, output, exit.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5; Sample Q10
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## sc-022 · scenario_chain · ci_cd

**Tasks:** 3.6, 4.3

**Q:** [CI/CD · 2/5] Post structured findings as inline PR comments from CI. CLI approach?

**A:** --output-format json with --json-schema for machine-parseable review output.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5
- Official CCAR-F Exam Guide — D3, Task 3.6; D4, Task 4.3

---

## sc-023 · scenario_chain · ci_cd

**Tasks:** 3.6, 4.6

**Q:** [CI/CD · 3/5] Same Claude session generated code and reviews it—misses subtle bugs. Better approach?

**A:** Independent Claude Code instance for review without the generator's reasoning context.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5
- Official CCAR-F Exam Guide — D3, Task 3.6; D4, Task 4.6

---

## sc-024 · scenario_chain · ci_cd

**Tasks:** 4.6

**Q:** [CI/CD · 4/5] 14-file PR review—inconsistent depth, missed bugs, contradictory feedback. Restructure?

**A:** Per-file local analysis passes, then separate cross-file integration pass.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5; Sample Q12
- Official CCAR-F Exam Guide — D4, Task 4.6

---

## sc-025 · scenario_chain · ci_cd

**Tasks:** 3.6

**Q:** [CI/CD · 5/5] Re-run review after new commits—duplicate inline comments. Context fix?

**A:** Include prior findings; instruct Claude to report only new or still-unaddressed issues.

**Tags:** scenario_chain, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Scenario 5
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## sc-026 · scenario_chain · structured_extraction

**Tasks:** 4.3

**Q:** [Structured Extraction · 1/5] Pipeline extracts from unstructured docs, validates with JSON schema, integrates downstream. Most reliable structured output approach?

**A:** tool_use with JSON schemas—eliminates syntax errors; add semantic validation separately.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## sc-027 · scenario_chain · structured_extraction

**Tasks:** 4.3

**Q:** [Structured Extraction · 2/5] Source docs often omit optional fields—model fabricates values. Schema fix?

**A:** Make fields optional/nullable when information may be absent—don't require missing data.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## sc-028 · scenario_chain · structured_extraction

**Tasks:** 4.4

**Q:** [Structured Extraction · 3/5] Validation fails on date format mismatch—info exists in document. Next step?

**A:** Retry with original doc, failed extraction, and specific validation errors in the follow-up prompt.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## sc-029 · scenario_chain · structured_extraction

**Tasks:** 4.5

**Q:** [Structured Extraction · 4/5] Manager wants batch API for pre-merge blocking checks and overnight reports. Correct split?

**A:** Synchronous API for blocking pre-merge; batch API only for latency-tolerant overnight jobs.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6; Sample Q11
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## sc-030 · scenario_chain · structured_extraction

**Tasks:** 5.5

**Q:** [Structured Extraction · 5/5] 97% overall accuracy—can you remove all human review?

**A:** No—verify accuracy by document type and field segment; route low-confidence and ambiguous docs to humans.

**Tags:** scenario_chain, structured_extraction

**Sources:**
- Official CCAR-F Exam Guide — Scenario 6
- Official CCAR-F Exam Guide — D5, Task 5.5

