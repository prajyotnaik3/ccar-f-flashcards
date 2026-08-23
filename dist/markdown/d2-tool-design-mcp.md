# D2: Tool Design & MCP Integration

## d2-001 · concept · customer_support, developer_productivity

**Q:** What does MCP (Model Context Protocol) provide to Claude agents?

**A:** A standard way for AI clients to discover and invoke tools, resources, and prompts from external servers.

**Tags:** mcp_basics

**Sources:**
- Official CCAR-F Exam Guide — D2
- https://modelcontextprotocol.io/introduction

---

## d2-002 · concept · customer_support, developer_productivity

**Q:** Primary mechanism LLMs use to select among similar tools?

**A:** Tool descriptions—minimal descriptions lead to unreliable selection when tools overlap.

**Tags:** tool_descriptions

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-003 · decision · customer_support

**Q:** Agent calls get_customer for order queries (#12345) instead of lookup_order. Both have minimal descriptions. Best first fix?

**A:** Expand each tool description: input formats, example queries, edge cases, and when to use vs similar tools.

**Why:** Descriptions are the primary selection mechanism; few-shot and routing layers don't fix inadequate descriptions first.

**Tags:** tool_descriptions, customer_support

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-004 · concept · customer_support, developer_productivity

**Q:** What should effective tool descriptions include beyond a one-line summary?

**A:** Expected inputs, outputs, example queries, edge cases, and boundaries explaining when to use vs similar alternatives.

**Tags:** tool_descriptions

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-005 · anti_pattern · developer_productivity, multi_agent_research

**Q:** analyze_content and analyze_document have near-identical descriptions. Likely result?

**A:** Tool misrouting—the model cannot reliably distinguish overlapping tools with ambiguous descriptions.

**Tags:** tool_descriptions, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-006 · decision · multi_agent_research

**Q:** Generic analyze_content overlaps with analyze_document. Rename/fix strategy?

**A:** Rename to purpose-specific names (e.g., extract_web_results) with web-specific descriptions that eliminate overlap.

**Tags:** tool_descriptions, naming

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-007 · decision · multi_agent_research, structured_extraction

**Q:** One generic analyze_document tool does too much. How split it?

**A:** Purpose-specific tools with clear contracts: extract_data_points, summarize_content, verify_claim_against_source.

**Tags:** tool_design, splitting

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-008 · concept · customer_support, developer_productivity

**Q:** How can system prompt wording undermine well-written tool descriptions?

**A:** Keyword-sensitive instructions can create unintended tool associations that override description clarity.

**Tags:** tool_descriptions, system_prompt

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-009 · decision · customer_support

**Q:** Tool selection still wrong after improving descriptions. Next check?

**A:** Review system prompt for keyword-sensitive instructions that might override tool descriptions.

**Tags:** system_prompt, tool_descriptions

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-010 · anti_pattern · developer_productivity

**Q:** Why expose one mega-tool that 'does anything on GitHub' to the agent?

**A:** Harder correct selection, weak error semantics, and excessive blast radius if mis-invoked.

**Tags:** tool_design, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1

---

## d2-011 · anti_pattern · customer_support

**Q:** Similar tools misroute. Why is consolidating into lookup_entity not the best first step?

**A:** Valid architecture but higher effort; immediate problem is inadequate descriptions—expand those first (Sample Q2).

**Tags:** tool_descriptions, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-012 · concept · customer_support

**Q:** MCP pattern for communicating tool failures back to the agent?

**A:** The isError flag on tool results, plus structured error metadata—not raw stack traces or generic messages.

**Tags:** errors, mcp, isError

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-013 · concept · customer_support, multi_agent_research

**Q:** Four MCP error categories the exam distinguishes?

**A:** Transient (timeouts, unavailability), validation (invalid input), business (policy violations), permission (access denied).

**Tags:** errors, error_category

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-014 · anti_pattern · customer_support

**Q:** Why return generic 'Operation failed' for all tool errors?

**A:** Prevents the agent from choosing appropriate recovery—retry, explain to user, escalate, or accept empty results.

**Tags:** errors, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-015 · decision · customer_support

**Q:** Structured error metadata fields for MCP tools (name three)?

**A:** errorCategory (transient/validation/permission/business), isRetryable boolean, and human-readable description.

**Tags:** errors, structured_errors

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-016 · decision · customer_support

**Q:** Business rule violation (e.g., refund over policy limit). Error response design?

**A:** isRetryable: false, customer-friendly explanation so the agent can communicate appropriately—not retry endlessly.

**Tags:** errors, business_errors

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-017 · compare · customer_support, multi_agent_research

**Q:** Access failure (timeout) vs valid empty result (no matches)—how should tools report differently?

**A:** Access failure: structured error with retry guidance. Valid empty: successful response indicating no matches—not an error.

**Tags:** errors, empty_results

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-018 · decision · multi_agent_research

**Q:** Transient failure in a subagent. Handle locally vs propagate to coordinator?

**A:** Retry locally when possible; propagate only unresolved errors with partial results and what was attempted.

**Tags:** errors, subagents

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-019 · decision · customer_support

**Q:** Tool returns ambiguous error from external API. Best tool-layer behavior?

**A:** Structured error payload (category, message, retryable flag)—not raw stack traces or silent failure.

**Tags:** errors, reliability

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-020 · concept · multi_agent_research, developer_productivity

**Q:** Why giving an agent 18 tools instead of 4–5 hurts reliability?

**A:** Increases decision complexity and degrades tool selection accuracy.

**Tags:** tool_scoping, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-021 · anti_pattern · multi_agent_research

**Q:** Synthesis agent attempts web searches. Likely tool design issue?

**A:** Agent has tools outside its specialization—scoped access should limit synthesis to synthesis-appropriate tools.

**Tags:** tool_scoping, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-022 · concept · multi_agent_research, developer_productivity

**Q:** What is scoped tool access for subagents?

**A:** Each agent gets only tools for its role, plus limited cross-role tools for specific high-frequency needs.

**Tags:** tool_scoping, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-023 · concept · customer_support, structured_extraction

**Q:** Three tool_choice configuration options on the Claude API?

**A:** "auto" (model may return text), "any" (must call a tool), and forced selection {"type": "tool", "name": "..."}.

**Tags:** tool_choice

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; Appendix

---

## d2-024 · decision · structured_extraction

**Q:** When use tool_choice: "any"?

**A:** When you need guaranteed tool invocation instead of conversational text—e.g., unknown document type among multiple extraction schemas.

**Tags:** tool_choice

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-025 · decision · structured_extraction

**Q:** Must run extract_metadata before enrichment tools. tool_choice approach?

**A:** Force specific tool first with {"type": "tool", "name": "extract_metadata"}, then process enrichment in follow-up turns.

**Tags:** tool_choice, forced_tool

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-026 · decision · multi_agent_research

**Q:** Replace generic fetch_url with what kind of constrained tool?

**A:** Purpose-specific tool like load_document that validates document URLs and rejects non-document URLs.

**Tags:** tool_design, constraints

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3

---

## d2-027 · decision · multi_agent_research

**Q:** Synthesis needs simple fact-checks often. Scoped cross-role tool pattern?

**A:** Provide verify_fact for high-frequency simple lookups; route complex verification through coordinator to search agent.

**Tags:** tool_scoping, verify_fact

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; D1 Sample Q9

---

## d2-028 · decision · customer_support

**Q:** Refund tool should only run after verified identity. Tool design choice?

**A:** Least privilege: narrow tool exposure or refund tool requiring verified session token from prior identity tool.

**Tags:** tool_boundaries, least_privilege

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; Customer Support scenario

---

## d2-029 · compare · developer_productivity

**Q:** Project-level vs user-level MCP server configuration?

**A:** Project .mcp.json for shared team tooling (version controlled); user ~/.claude.json for personal/experimental servers.

**Tags:** mcp_config, scoping

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-030 · decision · developer_productivity

**Q:** Store GitHub token for team MCP server without committing secrets?

**A:** Environment variable expansion in .mcp.json (e.g., ${GITHUB_TOKEN}) with secrets in env—not in the repo.

**Tags:** mcp_config, credentials

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-031 · concept · developer_productivity

**Q:** When are MCP tools from multiple servers available to the agent?

**A:** All configured servers are discovered at connection time—tools from all servers are available simultaneously.

**Tags:** mcp_config, discovery

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-032 · concept · developer_productivity, multi_agent_research

**Q:** MCP resources vs MCP tools—when use resources?

**A:** Resources expose content catalogs (issue summaries, doc hierarchies, DB schemas) to reduce exploratory tool calls.

**Tags:** mcp_resources

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-033 · decision · developer_productivity

**Q:** Agent prefers Grep over a more capable MCP search tool. Fix?

**A:** Enhance MCP tool descriptions to explain capabilities and outputs in detail so the model understands when MCP beats built-ins.

**Tags:** tool_descriptions, mcp

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-034 · decision · developer_productivity

**Q:** Jira integration needed. Community MCP server vs custom?

**A:** Prefer existing community MCP for standard integrations (Jira); custom servers for team-specific workflows.

**Tags:** mcp_config, community

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4

---

## d2-035 · compare · developer_productivity

**Q:** Built-in Claude Code tools vs custom MCP—when prefer MCP?

**A:** MCP for external systems (GitHub, DB, SaaS) or sharing tools across clients; built-ins for local repo operations.

**Tags:** mcp, claude_code

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4–2.5

---

## d2-036 · concept · developer_productivity

**Q:** Built-in Grep vs Glob—primary use case for each?

**A:** Grep: search file contents for patterns (function names, errors, imports). Glob: match file paths by name/extension patterns.

**Tags:** builtin_tools, Grep, Glob

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-037 · decision · developer_productivity

**Q:** Find all test files named *.test.tsx anywhere in the repo. Which built-in tool?

**A:** Glob with pattern like **/*.test.tsx.

**Tags:** builtin_tools, Glob

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-038 · decision · developer_productivity

**Q:** Find all callers of a function across the codebase. Which built-in tool?

**A:** Grep to search file contents for the function name/reference patterns.

**Tags:** builtin_tools, Grep

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-039 · compare · developer_productivity

**Q:** Read/Write/Edit—when use Edit vs Read + Write?

**A:** Edit for targeted changes with unique anchor text; Read + Write when Edit fails due to non-unique matches.

**Tags:** builtin_tools, Edit, Read, Write

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-040 · decision · developer_productivity

**Q:** Best incremental codebase exploration pattern?

**A:** Grep for entry points → Read to follow imports and trace flows—not read all files upfront.

**Tags:** builtin_tools, exploration

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-041 · decision · developer_productivity

**Q:** Trace usage across wrapper modules exporting many names?

**A:** Identify all exported names first, then Grep for each name across the codebase.

**Tags:** builtin_tools, Grep, exploration

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-042 · scenario_hook · customer_support, multi_agent_research, developer_productivity

**Q:** Which three exam scenarios list D2 as a primary domain?

**A:** Customer Support, Multi-Agent Research, and Developer Productivity.

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d2-043 · concept · customer_support

**Q:** Customer Support scenario MCP tools (Exam Scenario 1)—examples?

**A:** get_customer, lookup_order, process_refund, escalate_to_human—backend integration via custom MCP tools.

**Tags:** scenarios, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Scenario 1

---

## d2-044 · concept · developer_productivity

**Q:** Developer Productivity scenario built-in tools (Exam Scenario 4)?

**A:** Read, Write, Bash, Grep, Glob—plus MCP server integrations for external systems.

**Tags:** scenarios, builtin_tools

**Sources:**
- Official CCAR-F Exam Guide — Scenario 4

---

## d2-045 · anti_pattern · customer_support

**Q:** Improve tool selection with keyword routing layer parsing user input each turn. Why often wrong?

**A:** Over-engineered—bypasses LLM NLU; fix descriptions first; routing doesn't solve ordering or description gaps.

**Tags:** anti_pattern, routing

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-046 · compare · developer_productivity

**Q:** MCP tools vs MCP resources—division of responsibility?

**A:** Tools perform actions (fetch, update, search); resources expose catalogs and static context (schemas, doc trees) to cut exploratory calls.

**Tags:** mcp_tools, mcp_resources

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.4; Appendix in-scope

---

## d2-047 · concept · developer_productivity

**Q:** Why return structured isRetryable metadata on errors?

**A:** Lets the agent retry transient failures and avoid wasted retries on non-retryable business or validation errors.

**Tags:** errors, isRetryable

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

---

## d2-048 · concept · developer_productivity

**Q:** Built-in Bash tool—when use vs Grep?

**A:** Bash for shell commands and scripted operations; Grep for searching file contents for patterns across the codebase.

**Tags:** builtin_tools, Bash

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5; Scenario 4; Appendix

---

## d2-049 · concept · customer_support, structured_extraction

**Q:** tool_choice: "auto"—what can the model return?

**A:** The model may respond with conversational text instead of calling a tool—no guaranteed tool invocation.

**Tags:** tool_choice, auto

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.3; D4 Task 4.3

---

## d2-050 · anti_pattern · customer_support

**Q:** Similar tools misroute. Add 5–8 few-shot tool-selection examples first?

**A:** Adds token overhead without fixing root cause—inadequate tool descriptions are the primary selection mechanism.

**Tags:** tool_descriptions, few_shot, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.1; Sample Q2

---

## d2-051 · concept · developer_productivity

**Q:** Edit built-in tool—how does it modify files?

**A:** Targeted modifications using unique text matching as anchor—fails when anchor text is not unique.

**Tags:** builtin_tools, Edit

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.5

---

## d2-052 · decision · customer_support

**Q:** errorCategory for policy violation refund blocked?

**A:** Business error with isRetryable: false and customer-friendly explanation—not transient or permission.

**Tags:** errors, business_errors

**Sources:**
- Official CCAR-F Exam Guide — D2, Task 2.2

