# D1: Agentic Architecture & Orchestration

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

