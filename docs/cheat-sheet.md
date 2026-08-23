# CCAR-F Exam-Day Cheat Sheet

Auto-generated from flashcards with `exam_day: true`.

**39 cards** — review the night before the exam.

### d1-002 (D1)

- **Q:** 12% of support cases skip get_customer and call lookup_order by name only, causing wrong refunds. Most effective fix?
- **A:** Programmatic prerequisite: block lookup_order and process_refund until get_customer returns a verified customer ID.
- **Why:** Financial identity steps need deterministic enforcement; prompts and few-shot alone are probabilistic.

### d1-005 (D1)

- **Q:** When should an agentic loop continue vs terminate?
- **A:** Continue when stop_reason is tool_use; terminate when stop_reason is end_turn.

### d1-009 (D1)

- **Q:** What is hub-and-spoke multi-agent architecture?
- **A:** Coordinator manages all inter-subagent communication, error handling, and information routing; subagents do not talk directly.

### d1-010 (D1)

- **Q:** Do subagents automatically inherit the coordinator's conversation history?
- **A:** No—subagents operate with isolated context; parent history is not inherited automatically.

### d1-016 (D1)

- **Q:** What tool spawns subagents in the Agent SDK, and what must allowedTools include?
- **A:** The Task tool; allowedTools must include "Task" for a coordinator to invoke subagents.

### d1-023 (D1)

- **Q:** Programmatic enforcement (hooks, gates) vs prompt-based workflow ordering?
- **A:** Prompts have non-zero failure rate; programmatic gates give deterministic compliance when identity verification or financial ops require it.

### d1-025 (D1)

- **Q:** What must a structured human handoff include when escalating mid-process?
- **A:** Customer details, root cause analysis, recommended actions—humans may lack full conversation transcript.

### d1-029 (D1)

- **Q:** Business rule: block refunds over $500 and escalate. Hooks vs prompt instructions?
- **A:** Tool call interception hook—hooks guarantee compliance; prompts are probabilistic.

### d1-040 (D1)

- **Q:** Customer Support and Multi-Agent Research scenarios—shared primary domain?
- **A:** D1 (Agentic Architecture & Orchestration)—plus D2 tools/MCP and D5 context/reliability for both.

### d1-042 (D1)

- **Q:** Do subagents share memory across separate Task invocations?
- **A:** No—each invocation is isolated; context must be explicitly provided in the prompt every time.

### d1-048 (D1)

- **Q:** When should a support agent escalate to a human instead of continuing the agentic loop?
- **A:** Policy requires human judgment, identity cannot be verified, tool failures persist, or validation/confidence thresholds are not met.

### d1-055 (D1)

- **Q:** Two stop_reason values that drive agentic loop control?
- **A:** tool_use (continue loop—execute tools and append results) and end_turn (terminate and present response).

### d1-057 (D1)

- **Q:** What is a programmatic prerequisite gate in a multi-step agent workflow?
- **A:** Code or hook that blocks downstream tool calls until a prerequisite step completes (e.g., no refund until verified customer ID).

### d2-002 (D2)

- **Q:** Primary mechanism LLMs use to select among similar tools?
- **A:** Tool descriptions—minimal descriptions lead to unreliable selection when tools overlap.

### d2-003 (D2)

- **Q:** Agent calls get_customer for order queries (#12345) instead of lookup_order. Both have minimal descriptions. Best first fix?
- **A:** Expand each tool description: input formats, example queries, edge cases, and when to use vs similar tools.
- **Why:** Descriptions are the primary selection mechanism; few-shot and routing layers don't fix inadequate descriptions first.

### d2-012 (D2)

- **Q:** MCP pattern for communicating tool failures back to the agent?
- **A:** The isError flag on tool results, plus structured error metadata—not raw stack traces or generic messages.

### d2-015 (D2)

- **Q:** Structured error metadata fields for MCP tools (name three)?
- **A:** errorCategory (transient/validation/permission/business), isRetryable boolean, and human-readable description.

### d2-020 (D2)

- **Q:** Why giving an agent 18 tools instead of 4–5 hurts reliability?
- **A:** Increases decision complexity and degrades tool selection accuracy.

### d2-023 (D2)

- **Q:** Three tool_choice configuration options on the Claude API?
- **A:** "auto" (model may return text), "any" (must call a tool), and forced selection {"type": "tool", "name": "..."}.

### d2-028 (D2)

- **Q:** Refund tool should only run after verified identity. Tool design choice?
- **A:** Least privilege: narrow tool exposure or refund tool requiring verified session token from prior identity tool.

### d2-029 (D2)

- **Q:** Project-level vs user-level MCP server configuration?
- **A:** Project .mcp.json for shared team tooling (version controlled); user ~/.claude.json for personal/experimental servers.

### d2-036 (D2)

- **Q:** Built-in Grep vs Glob—primary use case for each?
- **A:** Grep: search file contents for patterns (function names, errors, imports). Glob: match file paths by name/extension patterns.

### d2-042 (D2)

- **Q:** Which three exam scenarios list D2 as a primary domain?
- **A:** Customer Support, Multi-Agent Research, and Developer Productivity.

### d3-002 (D3)

- **Q:** CLAUDE.md configuration hierarchy (three levels)?
- **A:** User (~/.claude/CLAUDE.md), project (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files).

### d3-008 (D3)

- **Q:** Team /review slash command for every developer on clone. Where create it?
- **A:** .claude/commands/ in the project repository—version-controlled and shared on clone/pull.

### d3-010 (D3)

- **Q:** Skill frontmatter options in .claude/skills/SKILL.md (name three)?
- **A:** context: fork, allowed-tools, and argument-hint.

### d3-016 (D3)

- **Q:** How do .claude/rules/ path-specific rules activate?
- **A:** YAML frontmatter paths field with glob patterns—rules load only when editing matching files.

### d3-021 (D3)

- **Q:** Restructure monolith into microservices—dozens of files, architectural decisions. Approach?
- **A:** Plan mode: explore codebase, understand dependencies, design approach before making changes.

### d3-022 (D3)

- **Q:** Plan mode vs direct execution—when use each?
- **A:** Plan mode: large-scale, multi-file, architectural, multiple valid approaches. Direct execution: simple, well-scoped single changes.

### d3-032 (D3)

- **Q:** CI job hangs—Claude Code waiting for interactive input. Fix?
- **A:** Use -p (or --print) flag for non-interactive mode: process prompt, output result, exit.

### d3-042 (D3)

- **Q:** CI/CD with Claude Code scenario (Scenario 5)—primary domains?
- **A:** D3 (Claude Code) and D4 (prompt engineering/structured output for review findings).

### d4-002 (D4)

- **Q:** Extraction misses nullable fields intermittently. Best improvement?
- **A:** Tighten schema (required vs optional), add validation-retry loop, and explicit examples for edge/null cases—not longer vague prompts alone.

### d4-005 (D4)

- **Q:** Structured Data Extraction scenario—primary domains?
- **A:** D4 (schemas, validation), D5 (reliability, human review for low confidence).

### d5-002 (D5)

- **Q:** Subagents need prior search results. Best context passing approach?
- **A:** Explicit structured handoffs (IDs, snippets, citations) via coordinator—not assuming shared implicit memory.

### d5-005 (D5)

- **Q:** Customer Support scenario—domains beyond D1?
- **A:** D2 (tool boundaries for refunds/account), D5 (escalation, handoffs, failure handling).

### meta-001 (META)

- **Q:** What is the official exam code for Claude Certified Architect, Foundations?
- **A:** CCAR-F (also written CCA-F or CCAF in older materials).
- **Why:** Pearson lists CCAR-F as the current code.

### meta-002 (META)

- **Q:** CCAR-F format: how many questions, time limit, and passing score?
- **A:** 60 scenario-based items, 120 minutes, pass at scaled 720 on a 100–1000 scale.

### meta-003 (META)

- **Q:** How many scenarios appear on the exam, and from what pool?
- **A:** 4 scenarios per exam, drawn randomly from a published bank of 6.

### meta-004 (META)

- **Q:** Core heuristic when a scenario needs deterministic guarantees (money, identity, schema compliance)?
- **A:** Prefer structural/programmatic fixes (hooks, prerequisites, scoped tools, tool_use schemas) over prompt-only instructions.
- **Why:** Exam tests judgment: prompts are insufficient for hard guarantees.

