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

**Q:** When should an agentic loop continue versus terminate?

**A:** Continue when stop_reason is tool_use; terminate when stop_reason is end_turn.

**Tags:** agent_loop, stop_reason

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-006 · anti_pattern · customer_support, developer_productivity

**Tasks:** 1.1

**Q:** Name three anti-patterns for deciding when an agentic loop should terminate.

**A:** Parsing natural language for completion; arbitrary iteration caps as primary stop; treating assistant text as completion signal.

**Tags:** agent_loop, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-007 · concept · customer_support, multi_agent_research

**Tasks:** 1.1

**Q:** When should you use model-driven tool selection versus pre-configured decision trees?

**A:** Model-driven: Claude picks tools from context each turn. Decision trees/forced sequences bypass model reasoning—use only when deterministic ordering is required.

**Tags:** agent_loop, tool_selection

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## d1-008 · concept · customer_support, multi_agent_research

**Tasks:** 1.1

**Q:** Why should you append tool results to conversation history between loop iterations?

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

**Q:** A report on 'AI in creative industries' covers only visual arts. Logs show the coordinator assigned digital art, graphic design, and photography only. What is the root cause?

**A:** Coordinator task decomposition too narrow—subagents executed correctly but were assigned incomplete scope.

**Why:** Coordinator logs show decomposition into only visual-arts subtasks—subagents succeeded within narrow assignments. Downstream agents are not the root cause; synthesis, search, and analysis worked within assigned scope.

**Tags:** decomposition, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2; Sample Q7

---

## d1-012 · decision · multi_agent_research

**Tasks:** 1.2

**Q:** How should a coordinator select which subagents to invoke?

**A:** Analyze query requirements and dynamically select needed subagents—not always route through the full pipeline.

**Why:** The coordinator should analyze the query and invoke only needed subagents. Always running the full pipeline wastes latency and context.

**Tags:** coordinator, orchestration

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## d1-013 · decision · multi_agent_research

**Tasks:** 1.2

**Q:** How should you partition research scope across subagents to reduce duplication?

**A:** Assign distinct subtopics or source types per agent (e.g., web vs documents vs synthesis)—not overlapping queries.

**Why:** Assign distinct subtopics or source types (for example web vs documents vs synthesis) so subagents do not duplicate overlapping queries.

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

**Why:** Hub-and-spoke routing through the coordinator gives observability, consistent error handling, and controlled information flow; subagents should not talk directly.

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

**Q:** How should you pass prior agent findings to a synthesis subagent?

**A:** Include complete findings directly in the subagent prompt (search results, document analysis)—not rely on automatic inheritance.

**Why:** Subagents do not inherit parent history. Put complete prior findings in the prompt or they will invent or omit evidence.

**Tags:** context_passing, synthesis

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-018 · decision · multi_agent_research

**Tasks:** 1.3

**Q:** When passing context between agents, what practice preserves attribution?

**A:** Use structured formats separating content from metadata (URLs, document names, page numbers).

**Why:** Separate claims from metadata (URLs, document names, page numbers) so attribution survives synthesis instead of collapsing into an uncited summary.

**Tags:** provenance, context_passing

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-019 · decision · multi_agent_research

**Tasks:** 1.3

**Q:** How should you spawn parallel subagents to lower latency?

**A:** Emit multiple Task tool calls in a single coordinator response—not separate turns per subagent.

**Why:** Multiple Task calls in one coordinator response run in parallel. Sequential turns add a full round-trip of latency per subagent.

**Tags:** parallel, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## d1-020 · decision · multi_agent_research

**Tasks:** 1.3

**Q:** Should coordinator prompts specify step-by-step procedures or research goals?

**A:** Specify research goals and quality criteria—enables subagent adaptability vs rigid procedural scripts.

**Why:** Goal-and-quality-criteria prompts let subagents adapt. Step-by-step scripts break when the evidence does not match the assumed procedure.

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

**Q:** When should you use programmatic enforcement (hooks, gates) instead of prompt-based workflow ordering?

**A:** Prompts have non-zero failure rate; programmatic gates give deterministic compliance when identity verification or financial ops require it.

**Tags:** prerequisites, hooks

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-024 · decision · customer_support

**Tasks:** 1.4

**Q:** Customer message has multiple concerns (billing + return). How should the agent investigate?

**A:** Decompose into distinct items, investigate each in parallel using shared context, then synthesize a unified resolution.

**Why:** Task 1.4: split multi-concern messages, investigate items in parallel with shared context, then synthesize one resolution—do not treat mixed issues as a single thread.

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

**Q:** What fields should a structured handoff include for a refund escalation?

**A:** Customer ID, root cause, refund amount, recommended action.

**Why:** Humans often lack the transcript. Hand off customer ID, root cause, refund amount, and a recommended action so they can act immediately.

**Tags:** handoff, escalation

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## d1-027 · concept · customer_support, multi_agent_research

**Tasks:** 1.5

**Q:** What does a PostToolUse hook do?

**A:** Intercepts tool results after execution to transform/normalize data before the model processes them.

**Tags:** hooks, PostToolUse

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-028 · decision · customer_support

**Tasks:** 1.5

**Q:** MCP tools return mixed timestamp formats (Unix, ISO 8601). Best approach before agent reasoning?

**A:** PostToolUse hook to normalize heterogeneous formats into a consistent representation.

**Why:** PostToolUse normalizes timestamps and status codes before the model reasons. Prompting the model to 'handle mixed formats' is probabilistic.

**Tags:** hooks, normalization

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-029 · decision · customer_support

**Tasks:** 1.5

**Q:** A business rule blocks refunds over $500 and requires escalation. Should you use hooks or prompt instructions?

**A:** Tool call interception hook—hooks guarantee compliance; prompts are probabilistic.

**Why:** hooks guarantee compliance; prompts are probabilistic.

**Tags:** hooks, compliance

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-030 · concept · customer_support

**Tasks:** 1.5

**Q:** What is the purpose of tool-call interception hooks?

**A:** Block policy-violating outgoing tool calls (e.g., large refunds) and redirect to alternative workflows (human escalation).

**Tags:** hooks, interception

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-031 · compare · ci_cd, multi_agent_research

**Tasks:** 1.6

**Q:** When should you use a fixed sequential pipeline versus dynamic adaptive decomposition?

**A:** Sequential pipelines for predictable multi-step reviews; dynamic decomposition for open-ended investigation that adapts to intermediate findings.

**Tags:** decomposition, prompt_chaining

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## d1-032 · decision · ci_cd

**Tasks:** 1.6

**Q:** A 14-file PR review misses bugs and gives contradictory feedback. How should you restructure the review?

**A:** Per-file local analysis passes, then a separate cross-file integration pass—avoids attention dilution.

**Why:** Split reviews into per-file passes plus a cross-file integration pass—fixes attention dilution across many files. Splitting PRs burdens developers; larger context does not fix attention quality; consensus across passes would suppress intermittently caught bugs.

**Tags:** decomposition, review

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6; Sample Q12

---

## d1-033 · decision · developer_productivity, ci_cd

**Tasks:** 1.6

**Q:** You need to add comprehensive tests to a legacy codebase. What decomposition strategy should you use?

**A:** Map structure → identify high-impact areas → prioritized plan that adapts as dependencies are discovered.

**Why:** Exam judgment aligned to task 1.6: Map structure → identify high-impact areas → prioritized plan that adapts as dependencies are discovered.

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

**Q:** How do you resume a named session in Claude Code?

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

**Q:** After the code has changed, when should you resume a session versus start fresh?

**A:** Resume when prior context is mostly valid; start fresh with injected summary when prior tool results are stale—more reliable than stale resumes.

**Why:** Resume when prior context is still valid. If tool results are stale after code changes, start fresh with an injected summary rather than a stale session.

**Tags:** session, resume

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-038 · decision · developer_productivity

**Tasks:** 1.7

**Q:** When resuming a session after specific files changed, what should you tell the agent?

**A:** Inform about specific file changes for targeted re-analysis—not require full re-exploration of the codebase.

**Why:** Tell the resumed session which files changed so it re-analyzes those paths instead of re-exploring the whole codebase.

**Tags:** session, context

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## d1-039 · decision · multi_agent_research

**Tasks:** 1.2, 1.3

**Q:** Synthesis needs simple fact-checks 85% of the time and complex search 15% of the time. How do you reduce latency without over-provisioning?

**A:** Give synthesis a scoped verify_fact tool for simple lookups; complex verifications still delegate through coordinator to search agent.

**Why:** Scoped verify_fact on synthesis covers the common simple fact-check case while complex work stays with search via coordinator—least privilege. End-of-pass batching creates blocking dependencies; giving synthesis all search tools over-provisions; speculative caching cannot predict verification needs.

**Tags:** subagents, tool_scoping

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2–1.3; Sample Q9

---

## d1-040 · scenario_hook · customer_support, multi_agent_research

**Tasks:** 1.2

**Q:** Which primary domains do the Customer Support and Multi-Agent Research scenarios share?

**A:** Both list D1 (Agentic Architecture), D2 (Tool Design & MCP), and D5 (Context Management & Reliability).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d1-041 · concept · multi_agent_research

**Tasks:** 1.2

**Q:** What are the four coordinator responsibilities in hub-and-spoke orchestration?

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

**Q:** In a PostToolUse hook, which heterogeneous MCP fields should you normalize before the model sees them?

**A:** Timestamps (Unix vs ISO 8601), numeric status codes, and other inconsistent formats from different backend tools.

**Why:** Task 1.5: normalize Unix vs ISO timestamps, numeric status codes, and other inconsistent MCP fields in PostToolUse before they enter model context.

**Tags:** hooks, normalization

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## d1-046 · decision · multi_agent_research

**Tasks:** 1.2

**Q:** The web search subagent times out. What error context should you send to the coordinator?

**A:** Structured error context: failure type, attempted query, partial results, and potential alternative approaches.

**Why:** Structured error context enables coordinator recovery (retry, alternate query, partial results). Generic retry status hides context; marking failure as success blocks recovery; terminating the whole workflow is unnecessary when partial progress exists.

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

**A:** Customer explicitly requests a human, policy is silent or requires an exception, or the agent cannot make meaningful progress—not self-reported confidence scores.

**Why:** Exam Guide task 5.2 names those three triggers. Sample Q3 rejects confidence thresholds and sentiment as proxies for complexity; identity ambiguity is resolved by asking for more identifiers, not by treating a confidence score as a stop signal.

**Tags:** escalation, agent_loop

**Sources:**
- Official CCAR-F Exam Guide — D1; Customer Support scenario

---

## d1-049 · scenario_hook · developer_productivity

**Tasks:** 2.3

**Q:** For the Developer Productivity scenario, which domains are primary, and what is the D1 focus?

**A:** D2 (tools/MCP), D3 (Claude Code), D1 (delegation/orchestration with built-in tools + MCP servers).

**Tags:** scenarios, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d1-050 · concept · multi_agent_research

**Tasks:** 1.2

**Q:** What typical subagent roles appear in a multi-agent research pipeline (Exam Scenario 3)?

**A:** Web search, document analysis, synthesis of findings, and report generation—coordinator delegates each role.

**Tags:** subagents, research

**Sources:**
- Official CCAR-F Exam Guide — Scenario 3; D1, Task 1.2

---

## d1-051 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** A subagent catches a timeout and returns empty results marked successful. Why is that wrong?

**A:** Suppresses failure—coordinator cannot recover, retry, or annotate coverage gaps; risks incomplete research output.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-052 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** A subagent timeout terminates the entire research workflow. Why is that wrong?

**A:** Single failures often recoverable with partial results, alternate queries, or gap annotation—unnecessary full termination.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-053 · compare · customer_support, multi_agent_research

**Tasks:** 1.4, 1.5

**Q:** When is prompt-based workflow guidance enough, and when do you need programmatic gates or hooks?

**A:** Prompts suffice for soft ordering and preferences; programmatic enforcement when business rules need deterministic compliance (identity before money, refund caps).

**Tags:** hooks, prerequisites

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4–1.5

---

## d1-054 · anti_pattern · multi_agent_research

**Tasks:** 5.3

**Q:** A subagent retries a timeout internally, then returns generic 'search unavailable' to the coordinator. What information is missing?

**A:** Hides failure type, attempted query, and partial results—coordinator cannot make informed recovery decisions.

**Tags:** error_propagation, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D1; Sample Q8

---

## d1-055 · concept · customer_support, multi_agent_research

**Tasks:** 1.1

**Q:** Which two stop_reason values drive agentic loop control?

**A:** tool_use (continue loop—execute tools and append results) and end_turn (terminate and present response).

**Tags:** stop_reason, agent_loop

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1; Appendix

---

## d1-056 · decision · multi_agent_research

**Tasks:** 2.3

**Q:** Why should you not give the synthesis agent all web search tools just to eliminate coordinator round-trips?

**A:** Over-provisions synthesis—violates separation of concerns and role-specific tool scoping; use scoped tools for common cases only.

**Why:** Scoped verify_fact on synthesis covers the common simple fact-check case while complex work stays with search via coordinator—least privilege. End-of-pass batching creates blocking dependencies; giving synthesis all search tools over-provisions; speculative caching cannot predict verification needs.

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

**Q:** What is the primary mechanism LLMs use to select among similar tools?

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

**Q:** Generic analyze_content overlaps with analyze_document. How should you rename or fix the tools?

**A:** Rename to purpose-specific names (e.g., extract_web_results) with web-specific descriptions that eliminate overlap.

**Why:** Rename overlapping tools to purpose-specific names (for example extract_web_results) and write web-specific descriptions so selection is unambiguous.

**Tags:** tool_descriptions, naming

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-007 · decision · multi_agent_research, structured_extraction

**Tasks:** 2.1

**Q:** One generic analyze_document tool does too much. How should you split it?

**A:** Purpose-specific tools with clear contracts: extract_data_points, summarize_content, verify_claim_against_source.

**Why:** Exam judgment aligned to task 2.1: Purpose-specific tools with clear contracts: extract_data_points, summarize_content, verify_claim_against_source.

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

**Q:** Tool selection is still wrong after improving descriptions. What should you check next?

**A:** Review system prompt for keyword-sensitive instructions that might override tool descriptions.

**Why:** After descriptions are fixed, check the system prompt. Keyword-sensitive instructions can create unintended tool associations that override good descriptions.

**Tags:** system_prompt, tool_descriptions

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-010 · anti_pattern · developer_productivity

**Tasks:** 2.1

**Q:** Why is exposing one mega-tool that 'does anything on GitHub' a problem?

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

**Q:** How should MCP tools communicate failures back to the agent?

**A:** The isError flag on tool results, plus structured error metadata—not raw stack traces or generic messages.

**Tags:** errors, mcp, isError

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-013 · concept · customer_support, multi_agent_research

**Tasks:** 2.2

**Q:** Which four MCP error categories does the exam distinguish?

**A:** Transient (timeouts, unavailability), validation (invalid input), business (policy violations), permission (access denied).

**Tags:** errors, error_category

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-014 · anti_pattern · customer_support

**Tasks:** 2.2

**Q:** Why is returning generic 'Operation failed' for all tool errors a problem?

**A:** Prevents the agent from choosing appropriate recovery—retry, explain to user, escalate, or accept empty results.

**Tags:** errors, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-015 · decision · customer_support

**Tasks:** 2.2

**Q:** Name three structured error metadata fields for MCP tools.

**A:** errorCategory (transient/validation/permission/business), isRetryable boolean, and human-readable description.

**Why:** Task 2.2 wants structured metadata: errorCategory, isRetryable, and a human-readable description so the agent can retry, explain, or stop.

**Tags:** errors, structured_errors

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-016 · decision · customer_support

**Tasks:** 2.2

**Q:** How should you design the error response for a business-rule violation (for example, a refund over the policy limit)?

**A:** isRetryable: false, customer-friendly explanation so the agent can communicate appropriately—not retry endlessly.

**Why:** Exam judgment aligned to task 2.2: isRetryable: false, customer-friendly explanation so the agent can communicate appropriately—not retry endlessly.

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

**Q:** When a subagent hits a transient failure, when should it retry locally versus propagate to the coordinator?

**A:** Retry locally when possible; propagate only unresolved errors with partial results and what was attempted.

**Why:** Exam judgment aligned to task 2.2: Retry locally when possible; propagate only unresolved errors with partial results and what was attempted.

**Tags:** errors, subagents

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-019 · decision · customer_support

**Tasks:** 2.2

**Q:** A tool returns an ambiguous error from an external API. How should the tool layer behave?

**A:** Structured error payload (category, message, retryable flag)—not raw stack traces or silent failure.

**Why:** Translate ambiguous API failures into category, message, and retryable flag. Raw stack traces and silent failures both block recovery.

**Tags:** errors, reliability

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-020 · concept · multi_agent_research, developer_productivity

**Tasks:** 2.3

**Q:** Why does giving an agent 18 tools instead of 4–5 hurt reliability?

**A:** Increases decision complexity and degrades tool selection accuracy.

**Tags:** tool_scoping, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-021 · anti_pattern · multi_agent_research

**Tasks:** 2.3

**Q:** The synthesis agent attempts web searches. What tool-design issue is likely?

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

**Q:** What are the three tool_choice configuration options on the Claude API?

**A:** "auto" (model may return text), "any" (must call a tool), and forced selection {"type": "tool", "name": "..."}.

**Tags:** tool_choice

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; Appendix

---

## d2-024 · decision · structured_extraction

**Tasks:** 2.3

**Q:** When should you set tool_choice to "any"?

**A:** When you need guaranteed tool invocation instead of conversational text—e.g., unknown document type among multiple extraction schemas.

**Why:** tool_choice "any" forces a tool call (the model may choose which). Use it when you need structured extraction and the document type is unknown.

**Tags:** tool_choice

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-025 · decision · structured_extraction

**Tasks:** 2.3

**Q:** You must run extract_metadata before enrichment tools. How should you set tool_choice?

**A:** Force specific tool first with {"type": "tool", "name": "extract_metadata"}, then process enrichment in follow-up turns.

**Why:** Exam judgment aligned to task 2.3: Force specific tool first with {"type": "tool", "name": "extract_metadata"}, then process enrichment in follow-up turns.

**Tags:** tool_choice, forced_tool

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-026 · decision · multi_agent_research

**Tasks:** 2.3

**Q:** Replace generic fetch_url with what kind of constrained tool?

**A:** Purpose-specific tool like load_document that validates document URLs and rejects non-document URLs.

**Why:** Exam judgment aligned to task 2.3: Purpose-specific tool like load_document that validates document URLs and rejects non-document URLs.

**Tags:** tool_design, constraints

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-027 · decision · multi_agent_research

**Tasks:** 2.3

**Q:** Synthesis often needs simple fact-checks. What scoped cross-role tool pattern should you use?

**A:** Provide verify_fact for high-frequency simple lookups; route complex verification through coordinator to search agent.

**Why:** Scoped verify_fact on synthesis covers the common simple fact-check case while complex work stays with search via coordinator—least privilege. End-of-pass batching creates blocking dependencies; giving synthesis all search tools over-provisions; speculative caching cannot predict verification needs.

**Tags:** tool_scoping, verify_fact

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; D1 Sample Q9

---

## d2-028 · decision · customer_support

**Tasks:** 2.3

**Q:** A refund tool should run only after verified identity. What tool-design choice enforces that?

**A:** Least privilege: narrow tool exposure or refund tool requiring verified session token from prior identity tool.

**Why:** Least privilege: do not expose refund until identity is verified, or require a verified session token from get_customer. Prompts cannot guarantee ordering.

**Tags:** tool_boundaries, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; Customer Support scenario

---

## d2-029 · compare · developer_productivity

**Tasks:** 2.4

**Q:** How do project-level and user-level MCP server configurations differ?

**A:** Project .mcp.json for shared team tooling (version controlled); user ~/.claude.json for personal/experimental servers.

**Tags:** mcp_config, scoping

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-030 · decision · developer_productivity

**Tasks:** 2.4

**Q:** How do you store a GitHub token for a team MCP server without committing secrets?

**A:** Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) with secrets in env—not in the repo.

**Why:** Put ${GITHUB_TOKEN} (or similar) in project .mcp.json and keep the secret in the environment so the repo never contains credentials.

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

**Q:** When should you use MCP resources instead of MCP tools?

**A:** Resources expose content catalogs (issue summaries, doc hierarchies, DB schemas) to reduce exploratory tool calls.

**Tags:** mcp_resources

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-033 · decision · developer_productivity

**Tasks:** 2.4

**Q:** The agent prefers Grep over a more capable MCP search tool. How do you fix that?

**A:** Enhance MCP tool descriptions to explain capabilities and outputs in detail so the model understands when MCP beats built-ins.

**Why:** If Grep wins over a richer MCP search tool, the MCP description is too weak. Spell out capabilities and outputs so the model knows when MCP is better.

**Tags:** tool_descriptions, mcp

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-034 · decision · developer_productivity

**Tasks:** 2.4

**Q:** You need Jira integration. Should you use a community MCP server or a custom one?

**A:** Prefer existing community MCP for standard integrations (Jira); custom servers for team-specific workflows.

**Why:** Use a community MCP for standard SaaS (Jira). Reserve custom servers for team-specific workflows the community server cannot cover.

**Tags:** mcp_config, community

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-035 · compare · developer_productivity

**Tasks:** 2.4, 2.5

**Q:** When should you prefer custom MCP over built-in Claude Code tools?

**A:** MCP for external systems (GitHub, DB, SaaS) or sharing tools across clients; built-ins for local repo operations.

**Tags:** mcp, claude_code

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4–2.5

---

## d2-036 · concept · developer_productivity

**Tasks:** 2.5

**Q:** What is the primary use case for built-in Grep versus Glob?

**A:** Grep: search file contents for patterns (function names, errors, imports). Glob: match file paths by name/extension patterns.

**Tags:** builtin_tools, Grep, Glob

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-037 · decision · developer_productivity

**Tasks:** 2.5

**Q:** Which built-in tool finds all test files named *.test.tsx anywhere in the repo?

**A:** Glob with pattern like **/*.test.tsx.

**Why:** Glob matches file paths. **/*.test.tsx finds tests by name anywhere; Grep searches file contents, not filenames.

**Tags:** builtin_tools, Glob

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-038 · decision · developer_productivity

**Tasks:** 2.5

**Q:** Which built-in tool finds all callers of a function across the codebase?

**A:** Grep to search file contents for the function name/reference patterns.

**Why:** Callers are content matches. Grep for the function name; Glob would only find files whose names happen to match.

**Tags:** builtin_tools, Grep

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-039 · compare · developer_productivity

**Tasks:** 2.5

**Q:** When should you use Edit versus Read plus Write?

**A:** Edit for targeted changes with unique anchor text; Read + Write when Edit fails due to non-unique matches.

**Tags:** builtin_tools, Edit, Read, Write

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-040 · decision · developer_productivity

**Tasks:** 2.5

**Q:** What is the best incremental pattern for exploring a codebase?

**A:** Grep for entry points → Read to follow imports and trace flows—not read all files upfront.

**Why:** Start with Grep for entry points, then Read along imports. Loading every file upfront wastes context and dilutes attention.

**Tags:** builtin_tools, exploration

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-041 · decision · developer_productivity

**Tasks:** 2.5

**Q:** How do you trace usage across wrapper modules that export many names?

**A:** Identify all exported names first, then Grep for each name across the codebase.

**Why:** Wrapper modules re-export many names. List exports first, then Grep each name so you do not miss aliased callers.

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

**Q:** What MCP tools appear in the Customer Support scenario (Exam Scenario 1)?

**A:** get_customer, lookup_order, process_refund, escalate_to_human—backend integration via custom MCP tools.

**Tags:** scenarios, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1

---

## d2-044 · concept · developer_productivity

**Tasks:** 2.5

**Q:** What built-in tools appear in the Developer Productivity scenario (Exam Scenario 4)?

**A:** Read, Write, Bash, Grep, Glob—plus MCP server integrations for external systems.

**Tags:** scenarios, builtin_tools

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4

---

## d2-045 · anti_pattern · customer_support

**Tasks:** 2.1

**Q:** Why is adding a keyword-routing layer that parses user input each turn often the wrong way to improve tool selection?

**A:** Over-engineered—bypasses LLM NLU; fix descriptions first; routing doesn't solve ordering or description gaps.

**Tags:** anti_pattern, routing

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-046 · compare · developer_productivity

**Tasks:** 2.4

**Q:** How do MCP tools and MCP resources divide responsibility?

**A:** Tools perform actions (fetch, update, search); resources expose catalogs and static context (schemas, doc trees) to cut exploratory calls.

**Tags:** mcp_tools, mcp_resources

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4; Appendix in-scope

---

## d2-047 · concept · developer_productivity

**Tasks:** 2.2

**Q:** Why should error results include structured isRetryable metadata?

**A:** Lets the agent retry transient failures and avoid wasted retries on non-retryable business or validation errors.

**Tags:** errors, isRetryable

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-048 · concept · developer_productivity

**Tasks:** 2.5

**Q:** When should you use the built-in Bash tool versus Grep?

**A:** Bash for shell commands and scripted operations; Grep for searching file contents for patterns across the codebase.

**Tags:** builtin_tools, Bash

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5; Scenario 4; Appendix

---

## d2-049 · concept · customer_support, structured_extraction

**Tasks:** 2.3, 4.3

**Q:** What can the model return when tool_choice is "auto"?

**A:** The model may respond with conversational text instead of calling a tool—no guaranteed tool invocation.

**Tags:** tool_choice, auto

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; D4 Task 4.3

---

## d2-050 · anti_pattern · customer_support

**Tasks:** 2.1

**Q:** Similar tools misroute. Why is adding 5–8 few-shot tool-selection examples the wrong first step?

**A:** Adds token overhead without fixing root cause—inadequate tool descriptions are the primary selection mechanism.

**Tags:** tool_descriptions, few_shot, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-051 · concept · developer_productivity

**Tasks:** 2.5

**Q:** How does the built-in Edit tool modify files?

**A:** Targeted modifications using unique text matching as anchor—fails when anchor text is not unique.

**Tags:** builtin_tools, Edit

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-052 · decision · customer_support

**Tasks:** 2.2

**Q:** Which errorCategory should you use when a policy violation blocks a refund?

**A:** Business error with isRetryable: false and customer-friendly explanation—not transient or permission.

**Why:** Policy violations are business errors: isRetryable false plus a customer-friendly explanation. They are not transient timeouts or permission denials.

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

**Q:** What are the three levels of the CLAUDE.md configuration hierarchy?

**A:** User (~/.claude/CLAUDE.md), project (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files).

**Tags:** claude_md, hierarchy

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-003 · decision · code_generation

**Tasks:** 3.1

**Q:** A new teammate does not receive team coding standards in Claude Code. What is the likely cause?

**A:** Instructions are in user-level ~/.claude/CLAUDE.md—not shared via version control; move to project-level config.

**Why:** User-level ~/.claude/CLAUDE.md is not in git. Team standards belong in project CLAUDE.md so clones pick them up.

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

**Q:** A monolithic CLAUDE.md is hard to maintain. How should you reorganize it?

**A:** Split into focused files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md).

**Why:** Split a monolithic CLAUDE.md into focused files under .claude/rules/ (testing.md, api-conventions.md, deployment.md) instead of one huge always-loaded file.

**Tags:** claude_md, rules

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-006 · decision · code_generation

**Tasks:** 3.1

**Q:** Claude Code behaves inconsistently across sessions. How do you diagnose which config is loaded?

**A:** Use /memory to verify which memory files are loaded and what context is active.

**Why:** /memory shows which memory files are loaded. Use it when behavior drifts across sessions because the wrong CLAUDE.md layer is active.

**Tags:** claude_md, memory

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-007 · anti_pattern · code_generation

**Tasks:** 3.1

**Q:** Why is it a problem to skip a shared project CLAUDE.md when multiple developers use Claude Code?

**A:** Inconsistent conventions, duplicated prompt context, and drift in how the agent edits code across teammates.

**Tags:** claude_md, team

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-008 · decision · code_generation, ci_cd

**Tasks:** 3.2

**Q:** Where should you create a team /review slash command so every developer gets it on clone?

**A:** .claude/commands/ in the project repository—version-controlled and shared on clone/pull.

**Why:** Project slash commands live in .claude/commands/ and are version-controlled for the team. ~/.claude/commands/ is personal; CLAUDE.md holds instructions not command definitions; .claude/config.json is not the Claude Code command mechanism.

**Tags:** slash_commands

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2; Sample Q4

---

## d3-009 · compare · code_generation

**Tasks:** 3.2

**Q:** How do project-scoped and user-scoped slash commands differ?

**A:** .claude/commands/ in repo (shared via git) vs ~/.claude/commands/ (personal, not version controlled).

**Tags:** slash_commands, scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-010 · concept · code_generation, developer_productivity

**Tasks:** 3.2

**Q:** Name three Skill frontmatter options in .claude/skills/SKILL.md.

**A:** context: fork, allowed-tools, and argument-hint.

**Tags:** skills, frontmatter

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-011 · decision · code_generation

**Tasks:** 3.2

**Q:** A skill produces verbose codebase analysis. Which frontmatter option isolates that output?

**A:** context: fork—runs skill in isolated sub-agent context so output doesn't pollute main conversation.

**Why:** runs skill in isolated sub-agent context so output doesn't pollute main conversation.

**Tags:** skills, context_fork

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-012 · decision · code_generation

**Tasks:** 3.2

**Q:** A skill should only write files, not run destructive shell commands. Which frontmatter option enforces that?

**A:** allowed-tools restricting tool access during skill execution (e.g., file write operations only).

**Why:** allowed-tools in skill frontmatter limits what the skill can invoke—for example file writes only, so it cannot run destructive shell commands.

**Tags:** skills, allowed_tools

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-013 · decision · code_generation

**Tasks:** 3.2

**Q:** A developer invokes a skill without required arguments. Which frontmatter option helps?

**A:** argument-hint prompts for required parameters when the skill is invoked without them.

**Why:** Exam judgment aligned to task 3.2: argument-hint prompts for required parameters when the skill is invoked without them.

**Tags:** skills, argument_hint

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-014 · compare · code_generation

**Tasks:** 3.2

**Q:** When should you use Skills versus CLAUDE.md?

**A:** Skills: on-demand task-specific workflows. CLAUDE.md: always-loaded universal standards for the project.

**Tags:** skills, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-015 · decision · code_generation

**Tasks:** 3.2

**Q:** How do you customize a skill for yourself without affecting teammates?

**A:** Create personal variants in ~/.claude/skills/ with different names—not in shared project skills.

**Why:** not in shared project skills.

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

**Q:** Test files sit as Button.test.tsx next to Button.tsx. How do you apply test conventions automatically?

**A:** .claude/rules/ with glob paths like **/*.test.tsx—applies by file type across all directories.

**Why:** .claude/rules/ with glob patterns apply conventions by file path—including tests spread across directories. Root CLAUDE.md relies on inference; skills need invocation; per-directory CLAUDE.md cannot cover scattered test files.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-018 · decision · code_generation

**Tasks:** 3.3

**Q:** React, API, and DB areas need different conventions; tests scattered everywhere. Best maintainable approach?

**A:** .claude/rules/ with YAML frontmatter glob patterns (e.g., paths: ["**/*.test.tsx"], ["src/api/**/*"])—not inference from one monolithic CLAUDE.md.

**Why:** .claude/rules/ with glob patterns apply conventions by file path—including tests spread across directories. Root CLAUDE.md relies on inference; skills need invocation; per-directory CLAUDE.md cannot cover scattered test files.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-019 · compare · code_generation

**Tasks:** 3.3

**Q:** For scattered test files, when should you use path-specific rules versus subdirectory CLAUDE.md?

**A:** Path-specific glob rules apply by file pattern anywhere in the tree; subdirectory CLAUDE.md is directory-bound.

**Tags:** rules, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-020 · concept · code_generation

**Tasks:** 3.3

**Q:** What is the benefit of path-scoped rules loading only for matching files?

**A:** Reduces irrelevant context and token usage—conventions apply only when relevant.

**Tags:** rules, context

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-021 · decision · code_generation

**Tasks:** 3.4

**Q:** You need to restructure a monolith into microservices across dozens of files. Which approach should you take first?

**A:** Plan mode: explore codebase, understand dependencies, design approach before making changes.

**Why:** Plan mode fits large architectural work with exploration before edits. Direct execution risks rework when dependencies are unknown; upfront rigid instructions skip necessary discovery; switching only if complexity emerges ignores stated large-scale scope.

**Tags:** plan_mode

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-022 · compare · code_generation

**Tasks:** 3.4

**Q:** When should you use plan mode versus direct execution?

**A:** Plan mode: large-scale, multi-file, architectural, multiple valid approaches. Direct execution: simple, well-scoped single changes.

**Tags:** plan_mode, direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-023 · decision · code_generation

**Tasks:** 3.4

**Q:** For a single-file bug fix with a clear stack trace, should you use plan mode or direct execution?

**A:** Direct execution—well-understood change with clear scope.

**Why:** well-understood change with clear scope.

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

**Q:** A library migration affects 45+ files. What workflow pattern should you use?

**A:** Plan mode for investigation and design, then direct execution to implement the planned approach.

**Why:** Plan mode for investigation and design on a 45+ file migration, then direct execution to implement the agreed plan.

**Tags:** plan_mode, direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-026 · anti_pattern · code_generation

**Tasks:** 3.4

**Q:** Why is it wrong to start a monolith-to-microservices split in direct execution and switch to plan only if complexity emerges?

**A:** Complexity is already stated—plan first prevents costly rework from late-discovered dependencies.

**Tags:** plan_mode, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-027 · decision · code_generation

**Tasks:** 3.5

**Q:** A natural-language transformation spec produces inconsistent code. What is the best fix?

**A:** Provide 2–3 concrete input/output examples showing expected transformations.

**Why:** Exam judgment aligned to task 3.5: Provide 2–3 concrete input/output examples showing expected transformations.

**Tags:** iterative_refinement, examples

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-028 · concept · code_generation

**Tasks:** 3.5

**Q:** What is the test-driven iteration pattern with Claude Code?

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

**Q:** When should you fix multiple issues in one message versus sequentially?

**A:** Single message when fixes interact; sequential iteration when issues are independent.

**Tags:** iterative_refinement

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-031 · decision · code_generation

**Tasks:** 3.5

**Q:** A migration script mishandles null edge cases. How should you iterate with Claude?

**A:** Provide specific test cases with example input and expected output for the failing edge case.

**Why:** Exam judgment aligned to task 3.5: Provide specific test cases with example input and expected output for the failing edge case.

**Tags:** iterative_refinement, edge_cases

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-032 · decision · ci_cd

**Tasks:** 3.6

**Q:** A CI job hangs because Claude Code is waiting for interactive input. How do you fix that?

**A:** Use -p (or --print) flag for non-interactive mode: process prompt, output result, exit.

**Why:** -p (--print) is the documented non-interactive CI mode: process, output, exit. CLAUDE_HEADLESS, --batch, and stdin tricks are not the correct Claude Code approach.

**Tags:** ci_cd, non_interactive

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6; Sample Q10

---

## d3-033 · decision · ci_cd

**Tasks:** 3.6

**Q:** Which CLI flags post structured PR review findings as inline comments from CI?

**A:** --output-format json with --json-schema for machine-parseable structured findings.

**Why:** --output-format json with --json-schema produces machine-parseable findings so CI can post inline PR comments. This is not a review-architecture question.

**Tags:** ci_cd, structured_output

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-034 · concept · ci_cd

**Tasks:** 3.6

**Q:** How do you provide project context to Claude Code invoked from CI?

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

**Q:** When re-running a PR review after new commits, how do you avoid duplicate inline comments?

**A:** Include prior review findings in context; instruct Claude to report only new or still-unaddressed issues.

**Why:** Pass prior findings back in and instruct Claude to report only new or still-open issues so re-runs do not spam duplicate comments.

**Tags:** ci_cd, review

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-037 · decision · ci_cd

**Tasks:** 3.6

**Q:** CI test generation suggests scenarios already in the suite. What context should you add?

**A:** Provide existing test files in context so generation avoids duplicate coverage.

**Why:** Put existing test files in context so generation does not propose coverage the suite already has.

**Tags:** ci_cd, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-038 · decision · ci_cd, code_generation

**Tasks:** 3.6

**Q:** How do you reduce low-value generated tests in Claude Code?

**A:** Document testing standards, valuable test criteria, and available fixtures in CLAUDE.md.

**Why:** Document testing standards, what a valuable test looks like, and available fixtures in CLAUDE.md so CI generation produces fewer low-value tests.

**Tags:** claude_md, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-039 · decision · ci_cd

**Tasks:** 3.6

**Q:** When running Claude Code in CI for PR review, what configuration concerns matter most?

**A:** Non-interactive (-p), explicit permissions, structured/deterministic outputs, independent review instance—not open-ended agent runs.

**Why:** CI needs -p (non-interactive), tight permissions, structured output, and an independent review instance—not an open-ended interactive agent.

**Tags:** ci_cd, automation

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-040 · anti_pattern · ci_cd

**Tasks:** 3.6

**Q:** Name two CI non-interactive flags that do not exist for Claude Code.

**A:** CLAUDE_HEADLESS env var and --batch flag—use -p/--print instead.

**Tags:** ci_cd, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6; Sample Q10

---

## d3-041 · scenario_hook · code_generation

**Tasks:** 3.4, 5.1

**Q:** What are the primary domains for the Code Generation scenario (Scenario 2)?

**A:** D3 (Claude Code config/workflows) and D5 (context management/reliability).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d3-042 · scenario_hook · ci_cd

**Tasks:** 3.6, 4.1

**Q:** What are the primary domains for the CI/CD with Claude Code scenario (Scenario 5)?

**A:** D3 (Claude Code) and D4 (prompt engineering/structured output for review findings).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d3-043 · scenario_hook · developer_productivity, code_generation

**Tasks:** 3.2, 3.4

**Q:** Scenario 2 involves slash commands, CLAUDE.md, and plan mode. What skill is the exam testing?

**A:** Integrating Claude Code into dev workflow: team config, custom commands, and when to plan vs execute directly.

**Tags:** scenarios, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2

---

## d3-044 · concept · code_generation

**Tasks:** 3.3

**Q:** What is an example path-scoped rule that applies only to Terraform files?

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

**Q:** For a monolith-to-microservices split, why is direct execution with comprehensive upfront structure instructions wrong?

**A:** Assumes structure without codebase exploration—dependencies discovered late cause costly rework; plan first.

**Tags:** plan_mode, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-047 · anti_pattern · code_generation

**Tasks:** 3.3

**Q:** Why is auto-applying conventions via skills in .claude/skills/ insufficient compared with path rules?

**A:** Skills require manual invocation or model choice—not deterministic path-based automatic application.

**Tags:** skills, rules, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-048 · decision · code_generation

**Tasks:** 3.5

**Q:** In test-driven iteration before implementation, what should the tests cover?

**A:** Expected behavior, edge cases, and performance requirements—iterate by sharing failures with Claude.

**Why:** iterate by sharing failures with Claude.

**Tags:** iterative_refinement, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-049 · decision · code_generation

**Tasks:** 3.2

**Q:** Besides verbose codebase analysis, what is another use case for context: fork on skills?

**A:** Exploratory brainstorming of alternatives—isolates speculative output from the main session.

**Why:** isolates speculative output from the main session.

**Tags:** skills, context_fork

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-050 · scenario_hook · developer_productivity

**Tasks:** 1.2, 2.5, 3.2

**Q:** What are the primary domains for the Developer Productivity scenario (Scenario 4)?

**A:** D2 (built-in tools + MCP), D3 (Claude Code workflows), D1 (delegation/orchestration).

**Tags:** scenarios, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

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

**Q:** How many questions, how much time, and what passing score does CCAR-F use?

**A:** 60 items in 120 minutes; pass at scaled 720 on a 100–1000 scale. Items are multiple-choice or multiple-response (each item says how many to select).

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

**Q:** When a scenario needs deterministic guarantees (money, identity, or schema compliance), what should you prefer?

**A:** Prefer structural/programmatic fixes (hooks, prerequisites, scoped tools, tool_use schemas) over prompt-only instructions.

**Why:** Exam tests judgment: prompts are insufficient for hard guarantees.

**Tags:** heuristic, exam_day

**Sources:**
- Community study guides aligned to Exam Guide patterns
- Official CCAR-F Exam Guide — sample rationales

---

## meta-005 · sample_rationale · customer_support

**Tasks:** cross-domain

**Q:** Sample Q1 (Customer Support): Why does a programmatic prerequisite beat a prompt, few-shot examples, or routing when get_customer is skipped?

**A:** Blocks lookup_order and process_refund until get_customer returns verified ID—deterministic enforcement for identity before refunds.

**Why:** Programmatic enforcement gives deterministic guarantees for required tool sequences; prompt and few-shot rely on probabilistic LLM compliance—insufficient when misidentification causes financial harm. Routing classifiers change tool availability, not ordering.

**Tags:** sample_rationale, sample_q1, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q1

---

## meta-006 · sample_rationale · customer_support

**Tasks:** cross-domain

**Q:** Sample Q2 (Customer Support): Why should you expand tool descriptions before adding few-shot examples, routing, or consolidating tools?

**A:** Descriptions are the primary LLM tool-selection signal—add inputs, examples, edge cases, and boundaries vs similar tools.

**Why:** Tool descriptions are the primary selection mechanism; minimal descriptions cause confusion between similar tools. Few-shot adds tokens without fixing descriptions; routing is over-engineered for a first step; consolidation is valid but higher effort.

**Tags:** sample_rationale, sample_q2, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q2

---

## meta-007 · sample_rationale · customer_support

**Tasks:** cross-domain

**Q:** Sample Q3 (Customer Support): Why do explicit escalation criteria with few-shot examples beat confidence scores, classifiers, or sentiment?

**A:** Fix unclear escalate-vs-resolve boundaries—the proportionate first response before adding infrastructure.

**Why:** Explicit escalation criteria with few-shot examples fix unclear decision boundaries. LLM self-reported confidence is poorly calibrated on hard cases; a separate classifier is over-engineered before prompt tuning; sentiment does not measure case complexity.

**Tags:** sample_rationale, sample_q3, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q3

---

## meta-008 · sample_rationale · code_generation, developer_productivity

**Tasks:** cross-domain

**Q:** Sample Q4 (Code Generation): Where should a team-shared /review slash command live?

**A:** .claude/commands/ in the project repository—version-controlled for everyone who clones the repo.

**Why:** Project slash commands live in .claude/commands/ and are version-controlled. ~/.claude/commands/ is personal; CLAUDE.md holds instructions not command definitions; .claude/config.json is not the Claude Code command mechanism.

**Tags:** sample_rationale, sample_q4, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q4

---

## meta-009 · sample_rationale · code_generation

**Tasks:** cross-domain

**Q:** Sample Q5 (Code Generation): For a monolith-to-microservices split across dozens of files, why start in plan mode?

**A:** Explore dependencies and design service boundaries before editing—large architectural scope is already stated.

**Why:** Plan mode fits large architectural work with exploration before edits. Direct execution risks rework when dependencies are unknown; rigid upfront instructions skip discovery; waiting for emergent complexity ignores stated large-scale scope.

**Tags:** sample_rationale, sample_q5, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q5

---

## meta-010 · sample_rationale · code_generation

**Tasks:** cross-domain

**Q:** Sample Q6 (Code Generation): Tests are spread as *.test.tsx. Why use .claude/rules/ with globs?

**A:** Glob patterns (e.g. **/*.test.tsx) auto-apply conventions by path regardless of directory.

**Why:** .claude/rules/ with glob patterns apply conventions by file path—including tests spread across directories. Root CLAUDE.md relies on inference; skills need invocation; per-directory CLAUDE.md cannot cover scattered test files.

**Tags:** sample_rationale, sample_q6, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q6

---

## meta-011 · sample_rationale · multi_agent_research

**Tasks:** cross-domain

**Q:** Sample Q7 (Multi-Agent Research): The report covers only visual arts. Why is coordinator decomposition the root cause?

**A:** Logs show narrow subtasks (digital art, graphic design, photography)—subagents succeeded within assigned scope.

**Why:** Coordinator logs show decomposition into only visual-arts subtasks—subagents succeeded within narrow assignments. Downstream agents are not the root cause; synthesis, search, and analysis worked within assigned scope.

**Tags:** sample_rationale, sample_q7, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q7

---

## meta-012 · sample_rationale · multi_agent_research

**Tasks:** cross-domain

**Q:** Sample Q8 (Multi-Agent Research): The search subagent times out. Why return structured error context to the coordinator?

**A:** Return failure type, attempted query, partial results, and alternatives so coordinator can recover intelligently.

**Why:** Structured error context enables coordinator recovery (retry, alternate query, partial results). Generic retry status hides context; marking failure as success blocks recovery; terminating the whole workflow is unnecessary when partial progress exists.

**Tags:** sample_rationale, sample_q8, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q8

---

## meta-013 · sample_rationale · multi_agent_research

**Tasks:** cross-domain

**Q:** Sample Q9 (Multi-Agent Research): 85% of checks are simple facts. Why give synthesis a scoped verify_fact tool?

**A:** Least privilege for common lookups; complex verification still routes through coordinator to search agent.

**Why:** Scoped verify_fact on synthesis covers simple fact-checks while complex work stays with search via coordinator—least privilege. End-of-pass batching creates blocking dependencies; giving synthesis all search tools over-provisions; speculative caching cannot predict verification needs.

**Tags:** sample_rationale, sample_q9, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q9

---

## meta-014 · sample_rationale · ci_cd

**Tasks:** cross-domain

**Q:** Sample Q10 (CI/CD): The pipeline hangs waiting for input. Why use the -p flag?

**A:** claude -p runs non-interactive: process prompt, output to stdout, exit—required for CI/CD.

**Why:** -p (--print) is the documented non-interactive CI mode. CLAUDE_HEADLESS, --batch, and stdin tricks are not the correct Claude Code approach.

**Tags:** sample_rationale, sample_q10, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q10

---

## meta-015 · sample_rationale · structured_extraction, ci_cd

**Tasks:** cross-domain

**Q:** Sample Q11: Why use the Batch API only for overnight jobs, not for pre-merge checks?

**A:** Batches save ~50% cost but lack latency SLA—unsuitable for blocking merge gates.

**Why:** Message Batches save cost but lack latency SLA—fine for overnight reports, unsuitable for blocking pre-merge checks. Polling batches for merge gates is unacceptable; custom_id correlates batch results; timeout fallback adds complexity vs matching API to workflow latency needs.

**Tags:** sample_rationale, sample_q11, structured_extraction, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q11

---

## meta-016 · sample_rationale · ci_cd

**Tasks:** cross-domain

**Q:** Sample Q12 (CI/CD): A 14-file PR review is inconsistent. Why split into per-file and integration passes?

**A:** Per-file local analysis then cross-file integration pass—fixes attention dilution across many files.

**Why:** Split reviews into per-file passes plus a cross-file integration pass—fixes attention dilution. Splitting PRs burdens developers; larger context does not fix attention quality; consensus across passes would suppress intermittently caught bugs.

**Tags:** sample_rationale, sample_q12, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q12

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

---

## tn-1-1 · task_notes · all

**Tasks:** 1.1

**Q:** Task 1.1 — Design and implement agentic loops for autonomous task execution

**A:** Loop on stop_reason. Caps are a safety net, not the stop rule.

**Notes:**
- Code loop: send Messages request → read stop_reason → tool_use: run tools, append results, repeat; end_turn: stop.
- Append tool results to history. Skip that and the model never sees what the tool returned.
- stop_reason is the only primary stop signal. Do not parse 'I'm done' or check content[0].type == text (text can sit next to tool_use).
- Iteration caps belong as a runaway safety net, not the fix for premature exit.
- Trap: tool_choice any to 'stop leftover text' forces tools forever. Let the model end via end_turn.
- Default: model picks tools from context. Hard-code sequences only when compliance must be deterministic (see 1.4).

**Tags:** task_notes, agent_loop

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.1

---

## tn-1-2 · task_notes · all

**Tasks:** 1.2

**Q:** Task 1.2 — Orchestrate multi-agent systems with coordinator–subagent patterns

**A:** Hub-and-spoke only. Coverage gaps are coordinator decomposition bugs.

**Notes:**
- Coordinator owns split, who to call, routing, errors, and merge. Subagents never talk peer-to-peer.
- Subagents do not inherit coordinator history. Isolation is a feature, not a bug.
- Pick subagents from the query. A simple fact-check should not run search+analyze+synthesize.
- Partition by subtopic or source type so workers do not duplicate work.
- Trap: report misses music/film because coordinator assigned only visual-arts subtasks—workers did their jobs.
- Refinement: judge synthesis for gaps → targeted re-search → synthesize again until coverage is enough.

**Tags:** task_notes, coordinator

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.2

---

## tn-1-3 · task_notes · all

**Tasks:** 1.3

**Q:** Task 1.3 — Configure subagent invocation, context passing, and spawning

**A:** allowedTools must include Task. Context is copied in, never inherited.

**Notes:**
- Spawn with the Task tool (Claude Code may label it Agent; exam still says Task). Coordinator allowedTools must include it.
- Each Task call is a blank slate—paste prior findings into the prompt every time.
- AgentDefinition: description, system prompt, tool list. Aim for ~4–5 tools per specialist.
- Keep claim text separate from URL/title/page so synthesis can still cite.
- Independent work: multiple Task calls in one coordinator turn (parallel). That is not fork_session.
- Coordinator prompts: goals and quality bars, not rigid step lists.

**Tags:** task_notes, Task_tool

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.3

---

## tn-1-4 · task_notes · all

**Tasks:** 1.4

**Q:** Task 1.4 — Implement multi-step workflows with enforcement and handoff patterns

**A:** If the stem says guaranteed/must always, the answer is a gate or hook, not a prompt.

**Notes:**
- Prompts are probabilistic. Identity-before-money needs a programmatic prerequisite/hook.
- Block lookup_order / process_refund until get_customer returns a verified ID.
- Multi-concern tickets: split, investigate in parallel, then one synthesized reply.
- Handoff packet the exam expects: customer ID, factual summary, root cause, recommended action.
- Never fail silent. If the agent cannot finish, emit that structured handoff—not a vague error.

**Tags:** task_notes, prerequisites

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.4

---

## tn-1-5 · task_notes · all

**Tasks:** 1.5

**Q:** Task 1.5 — Apply Agent SDK hooks for tool-call interception and data normalization

**A:** PreToolUse blocks; PostToolUse normalizes. Prompts cannot match that guarantee.

**Notes:**
- PreToolUse / intercept: runs before the tool. Block refunds over $500; validate args.
- PostToolUse: runs after. Normalize Unix vs ISO timestamps and status codes before the model sees them.
- Hooks are code. Prompt injection cannot skip them. Soft style rules stay in the system prompt.
- Stem words guaranteed / must always / compliance / audit → hooks, not few-shot.

**Tags:** task_notes, hooks

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.5

---

## tn-1-6 · task_notes · all

**Tasks:** 1.6

**Q:** Task 1.6 — Design task decomposition strategies for complex workflows

**A:** Known steps → chain. Unknown scope → adaptive. Many files → per-item then integration.

**Notes:**
- Prompt chaining: fixed A→B→C when each step needs the last output (predictable reviews).
- Adaptive: next subtask comes from what you just found (open-ended 'add tests to this repo').
- Attention dilution: one pass over 14 files → uneven depth and contradictions.
- Fix: per-file local pass, then a separate cross-file integration pass.
- Traps: bigger context window, split the PR, or keep findings only if 2 of 3 full passes agree.

**Tags:** task_notes, decomposition

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.6

---

## tn-1-7 · task_notes · all

**Tasks:** 1.7

**Q:** Task 1.7 — Manage session state, resumption, and forking

**A:** Resume if still valid. Stale tools → new session + summary. Fork to compare approaches.

**Notes:**
- --resume continues a named session. Tell it which files changed so it re-reads those, not the whole tree.
- Stale signals: repeats, contradicts itself, ignores recent tool output. Fix is a fresh session plus a curated summary—not 'more context'.
- fork_session: branch from a shared baseline to try two designs without polluting the main thread.
- fork_session ≠ firing several Task tools in one turn (that is parallel spawn).

**Tags:** task_notes, session

**Sources:**
- Official CCAR-F Exam Guide — D1, Task 1.7

---

## tn-2-1 · task_notes · all

**Tasks:** 2.1

**Q:** Task 2.1 — Design effective tool interfaces with clear descriptions and boundaries

**A:** Descriptions select tools. Improve text first; do not merge tools as step one.

**Notes:**
- Description > name. Include what it does, inputs, outputs, what it does not do, and example queries.
- Misroutes between similar tools: expand descriptions before few-shot, routers, or a mega-tool.
- Rename to purpose (extract_web_results) and split fat tools (extract vs summarize vs verify).
- System-prompt keywords can override good descriptions—audit the prompt next.
- Trap: 'just reduce the tool count' is the wrong first move.

**Tags:** task_notes, tool_descriptions

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## tn-2-2 · task_notes · all

**Tasks:** 2.2

**Q:** Task 2.2 — Implement structured error responses for MCP tools

**A:** isError + category + isRetryable. Zero hits is success, not failure.

**Notes:**
- Return isError plus category (transient / validation / business / permission), isRetryable, and a clear description.
- Transient: retry. Validation: fix input. Business/permission: do not retry; explain or escalate.
- Timeout/401 = access failure. Search with 0 rows = successful empty result. Do not mix those.
- Subagents retry transients locally; bubble up only unresolved errors with partial results and what was tried.
- Trap: generic 'Operation failed' or treating empty search as an error.

**Tags:** task_notes, errors

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## tn-2-3 · task_notes · all

**Tasks:** 2.3

**Q:** Task 2.3 — Distribute tools across agents and configure tool_choice

**A:** 4–5 tools per role. auto / any / forced-name are three different guarantees.

**Notes:**
- 18 tools tank selection. Scope specialists; synthesis with search tools will search.
- Allowed exception: one tiny cross-role tool for a high-frequency need (verify_fact), not the whole search suite.
- auto: model may chat (default agent loop). any: must call some tool. Forced name: that tool, that schema.
- Unknown doc type among several extractors → any. Known schema every time → force that tool.
- Replace fetch_url with load_document that rejects non-document URLs.

**Tags:** task_notes, tool_choice

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## tn-2-4 · task_notes · all

**Tasks:** 2.4

**Q:** Task 2.4 — Integrate MCP servers into Claude Code and agent workflows

**A:** Team config in the repo; secrets in env. Prefer community servers. Resources ≠ tools.

**Notes:**
- Project .mcp.json is shared. ~/.claude.json is personal. Do not commit tokens—use ${GITHUB_TOKEN}.
- Host/client talks to servers. Servers do not peer with each other.
- All connected servers' tools appear together at connect time.
- Resources = catalogs (schemas, doc trees). Tools = actions.
- If Grep beats a better MCP search, the MCP description is too weak.
- Use community Jira/GitHub first; custom servers only for team-specific flows.

**Tags:** task_notes, mcp_config

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## tn-2-5 · task_notes · all

**Tasks:** 2.5

**Q:** Task 2.5 — Select and apply built-in tools (Read, Write, Edit, Bash, Grep, Glob)

**A:** Most specific tool wins. Grep contents, Glob paths, Edit unique anchors.

**Notes:**
- Grep: callers, errors, imports. Glob: **/*.test.tsx. Read: you already know the path.
- Edit needs unique old_string. If not unique → Read + Write.
- Bash for build/test/git—not as a lazy Grep.
- Explore: Grep entry points → Read along imports. Do not dump the repo.
- Wrappers: list exports, then Grep each name.

**Tags:** task_notes, builtin_tools

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## tn-3-1 · task_notes · all

**Tasks:** 3.1

**Q:** Task 3.1 — Configure CLAUDE.md hierarchy, scoping, and modular organization

**A:** User vs project vs directory. Files stack; they do not silently override.

**Notes:**
- User ~/.claude/CLAUDE.md is personal. Project CLAUDE.md / .claude/CLAUDE.md is git-shared.
- Directory CLAUDE.md applies under that folder. @import keeps package standards modular.
- Split a monolith into .claude/rules/ topic files.
- New hire missing standards → they lived in user-level, not project-level.
- /memory shows which memory files are loaded when behavior drifts.
- Trap: 'user CLAUDE.md always wins' — layers concatenate; fix real contradictions in source.

**Tags:** task_notes, CLAUDE.md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## tn-3-2 · task_notes · all

**Tasks:** 3.2

**Q:** Task 3.2 — Create and configure custom slash commands and skills

**A:** Team commands in .claude/commands/. Skills: context: fork, allowed-tools, argument-hint.

**Notes:**
- Shared slash commands: .claude/commands/. Personal: ~/.claude/commands/. CLAUDE.md is not a command file.
- Skills = on-demand workflows (directory + SKILL.md). CLAUDE.md = always-on standards.
- context: fork isolates verbose analysis/brainstorming from the main thread.
- allowed-tools can lock a skill to writes only. argument-hint prompts for missing args.
- Personal variants: ~/.claude/skills/ under new names so teammates are unaffected.

**Tags:** task_notes, skills

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## tn-3-3 · task_notes · all

**Tasks:** 3.3

**Q:** Task 3.3 — Apply path-specific rules for conditional convention loading

**A:** Glob paths in .claude/rules/ frontmatter—automatic, path-based, not skills.

**Notes:**
- YAML paths globs (terraform/**/*, **/*.test.tsx) load only while editing matches.
- Saves tokens vs stuffing every convention in root CLAUDE.md.
- Scattered tests: globs beat per-directory CLAUDE.md (directory-bound).
- Root headers that hope Claude infers the section are unreliable.
- Skills are opt-in. They are not automatic path application.

**Tags:** task_notes, rules

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## tn-3-4 · task_notes · all

**Tasks:** 3.4

**Q:** Task 3.4 — Determine when to use plan mode vs direct execution

**A:** Plan when design is unknown or costly to reverse. Direct when the fix is obvious.

**Notes:**
- Plan: many files, architecture, several valid designs, unknown dependencies.
- Direct: one well-scoped change (stack trace in a single file).
- Monolith → services: plan first. The complexity is already in the prompt.
- Pattern: plan to design, then direct to implement (e.g. 45-file migration).
- Explore subagent: noisy discovery there; summary back to main context.
- Trap: -p is CI headless mode, not plan mode.

**Tags:** task_notes, plan_mode

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## tn-3-5 · task_notes · all

**Tasks:** 3.5

**Q:** Task 3.5 — Apply iterative refinement techniques for progressive improvement

**A:** Show I/O examples. Tests first. Interview before unfamiliar designs. Independent review session.

**Notes:**
- Wobbly NL specs → 2–3 concrete input/output pairs, not more adjectives.
- TDD: write behavior/edge/perf tests, paste failures back.
- Interview pattern: Claude asks design questions before coding a new domain.
- Interacting bugs → one message. Independent bugs → sequential.
- Do not review generated code in the same session that wrote it—start a fresh reviewer.

**Tags:** task_notes, iteration

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## tn-3-6 · task_notes · all

**Tasks:** 3.6

**Q:** Task 3.6 — Integrate Claude Code into CI/CD pipelines

**A:** -p for headless. JSON schema for comments. Independent reviewer. CLAUDE.md for CI context.

**Notes:**
- -p/--print is non-interactive. CLAUDE_HEADLESS and --batch are not the documented flags.
- --output-format json plus --json-schema for parseable PR comments.
- CI loads project CLAUDE.md (standards, fixtures, review criteria).
- Generator session is a weak reviewer—use an independent instance.
- Re-review: pass prior findings; ask only for new or still-open issues.
- Include existing tests so generation does not duplicate coverage.

**Tags:** task_notes, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## tn-4-1 · task_notes · all

**Tasks:** 4.1

**Q:** Task 4.1 — Design prompts with explicit criteria to improve precision

**A:** Name what to flag vs skip. Kill a noisy category. Calibrate severity with examples.

**Notes:**
- Vague 'be conservative' loses to categorical rules (flag comments only when they contradict code).
- Say report bugs/security, skip style nits—do not rely on confidence filtering alone.
- One high-FP category makes people ignore every category. Disable it while you fix the prompt.
- Severity needs concrete code examples, not a 1–10 vibe.
- Show before/after snippets; they beat paragraphs of style advice.

**Tags:** task_notes, precision

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.1

---

## tn-4-2 · task_notes · all

**Tasks:** 4.2

**Q:** Task 4.2 — Apply few-shot prompting for consistency and ambiguous cases

**A:** 2–4 targeted examples with why. More than ~4 rarely helps.

**Notes:**
- Use few-shot when instructions still yield messy format or shaky edges.
- 2–4 examples that show why A beat a plausible B (sweet spot; 10 examples waste context).
- Show the finding shape: location, issue, severity, fix.
- Contrast local style vs a real bug to cut FPs while still catching novel bugs.
- Extraction: one shot per layout (inline cites vs bibliography).

**Tags:** task_notes, few_shot

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.2

---

## tn-4-3 · task_notes · all

**Tasks:** 4.3

**Q:** Task 4.3 — Enforce structured output with tool use and JSON schemas

**A:** Forced tool_use is the production JSON path. Required fields cause fabrication.

**Notes:**
- Most reliable JSON: a dedicated extract tool + forced tool_choice (or any if type is unknown).
- Prompt-only JSON is for prototypes. Schema on the tool is enforced by the API.
- Strict schema ≠ correct semantics (totals, wrong field).
- If a value may be missing, make it optional/nullable—required fields get invented.
- Extensible category: enum + other + detail. Ambiguous: unclear, do not force a bucket.
- Put date-normalization rules in the prompt next to the schema.

**Tags:** task_notes, json_schema

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.3

---

## tn-4-4 · task_notes · all

**Tasks:** 4.4

**Q:** Task 4.4 — Implement validation, retry, and feedback loops

**A:** Retry original + failed output + specific error. Never just 'try again'.

**Notes:**
- Retry payload: original doc, failed extract, exact validation errors.
- Retries fix format/structure. They cannot invent facts that are not in the document.
- Escalate after repeated failures or a fundamentally wrong interpretation.
- detected_pattern on findings lets you mine which constructs cause FPs.
- Invoices: calculated_total vs stated_total; conflict_detected for inconsistent source.

**Tags:** task_notes, validation

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.4

---

## tn-4-5 · task_notes · all

**Tasks:** 4.5

**Q:** Task 4.5 — Design efficient batch processing strategies

**A:** ~50% cheaper, up to 24h, no latency SLA. Batch is cost, not speed.

**Notes:**
- Message Batches: cheaper, no SLA, window up to 24 hours. Not for real-time/user-facing waits.
- Overnight reports = batch. Blocking pre-merge = synchronous. Do not poll batches as a merge gate.
- No multi-turn tool calling inside one batch request.
- custom_id correlates request/response and failed docs. Resubmit only failures (chunk oversized).
- Tune prompts on a sample before 10k docs. 30h SLA with 24h max → submit often enough for retries.

**Tags:** task_notes, batch_api

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.5

---

## tn-4-6 · task_notes · all

**Tasks:** 4.6

**Q:** Task 4.6 — Design multi-instance and multi-pass review architectures

**A:** New instance, no generator history. Per-file + integration. Not 2-of-3 voting.

**Notes:**
- Same-session self-review keeps generation bias. Second instance without that context catches more.
- Extended thinking is not a substitute for an independent reviewer.
- Large PR: local per-file pass + cross-file integration pass. Bigger windows do not fix attention.
- Consensus of 3 full passes hides intermittent real bugs.
- Optional verification pass: confidence next to each finding for human routing (not a support escalate rule).

**Tags:** task_notes, multi_pass

**Sources:**
- Official CCAR-F Exam Guide — D4, Task 4.6

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

