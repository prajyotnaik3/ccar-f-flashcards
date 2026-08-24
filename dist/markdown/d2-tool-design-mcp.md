# D2: Tool Design & MCP Integration

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

