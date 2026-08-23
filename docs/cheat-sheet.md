# CCAR-F Exam-Day Cheat Sheet

Auto-generated from flashcards with `exam_day: true`.

**63 cards** — review the night before the exam.

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
- **Why:** hooks guarantee compliance; prompts are probabilistic.

### d1-040 (D1)

- **Q:** Customer Support and Multi-Agent Research scenarios—shared primary domain?
- **A:** D1 (Agentic Architecture & Orchestration)—plus D2 tools/MCP and D5 context/reliability for both.

### d1-042 (D1)

- **Q:** Do subagents share memory across separate Task invocations?
- **A:** No—each invocation is isolated; context must be explicitly provided in the prompt every time.

### d1-048 (D1)

- **Q:** When should a support agent escalate to a human instead of continuing the agentic loop?
- **A:** Policy requires human judgment, identity cannot be verified, tool failures persist, or validation/confidence thresholds are not met.
- **Why:** Correct choice avoids the wrong pattern: not met..

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
- **Why:** Tool choice follows capability fit: built-in tools for repo search, MCP for external systems—descriptions and scoping drive correct selection.

### d2-020 (D2)

- **Q:** Why giving an agent 18 tools instead of 4–5 hurts reliability?
- **A:** Increases decision complexity and degrades tool selection accuracy.

### d2-023 (D2)

- **Q:** Three tool_choice configuration options on the Claude API?
- **A:** "auto" (model may return text), "any" (must call a tool), and forced selection {"type": "tool", "name": "..."}.

### d2-028 (D2)

- **Q:** Refund tool should only run after verified identity. Tool design choice?
- **A:** Least privilege: narrow tool exposure or refund tool requiring verified session token from prior identity tool.
- **Why:** Exam tests structural or configuration fixes over prompt-only approaches when reliability, security, or compliance matter.

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
- **Why:** Project slash commands live in .claude/commands/ and are version-controlled for the team. ~/.claude/commands/ is personal; CLAUDE.md holds instructions not command definitions; .claude/config.json is not the Claude Code command mechanism.

### d3-010 (D3)

- **Q:** Skill frontmatter options in .claude/skills/SKILL.md (name three)?
- **A:** context: fork, allowed-tools, and argument-hint.

### d3-016 (D3)

- **Q:** How do .claude/rules/ path-specific rules activate?
- **A:** YAML frontmatter paths field with glob patterns—rules load only when editing matching files.

### d3-021 (D3)

- **Q:** Restructure monolith into microservices—dozens of files, architectural decisions. Approach?
- **A:** Plan mode: explore codebase, understand dependencies, design approach before making changes.
- **Why:** Plan mode fits large architectural work with exploration before edits. Direct execution risks rework when dependencies are unknown; upfront rigid instructions skip necessary discovery; switching only if complexity emerges ignores stated large-scale scope.

### d3-022 (D3)

- **Q:** Plan mode vs direct execution—when use each?
- **A:** Plan mode: large-scale, multi-file, architectural, multiple valid approaches. Direct execution: simple, well-scoped single changes.

### d3-032 (D3)

- **Q:** CI job hangs—Claude Code waiting for interactive input. Fix?
- **A:** Use -p (or --print) flag for non-interactive mode: process prompt, output result, exit.
- **Why:** -p (--print) is the documented non-interactive CI mode: process, output, exit. CLAUDE_HEADLESS, --batch, and stdin tricks are not the correct Claude Code approach.

### d3-042 (D3)

- **Q:** CI/CD with Claude Code scenario (Scenario 5)—primary domains?
- **A:** D3 (Claude Code) and D4 (prompt engineering/structured output for review findings).

### d4-002 (D4)

- **Q:** Explicit review criteria vs vague instructions like 'be conservative'?
- **A:** Specific categorical criteria (flag when comment contradicts code) beat vague confidence filtering for precision.

### d4-013 (D4)

- **Q:** Most reliable approach for guaranteed schema-compliant JSON output?
- **A:** tool_use with JSON schemas—eliminates JSON syntax errors vs free-text JSON generation.

### d4-015 (D4)

- **Q:** Source document may omit a field. Schema design to prevent fabrication?
- **A:** Make fields optional/nullable when information may be absent—don't require fields the source lacks.
- **Why:** don't require fields the source lacks.

### d4-021 (D4)

- **Q:** What is retry-with-error-feedback for extraction?
- **A:** On validation failure, send follow-up with original document, failed extraction, and specific validation errors for self-correction.

### d4-026 (D4)

- **Q:** Extraction misses nullable fields intermittently. Best improvement?
- **A:** Tighten required vs optional schema, validation-retry loop, and explicit examples for null/edge cases.
- **Why:** Structured output plus validation-retry separates syntax from semantics; schemas must reflect absent data, not force fabrication.

### d4-027 (D4)

- **Q:** Message Batches API tradeoffs (cost, latency)?
- **A:** 50% cost savings, up to 24-hour processing window, no guaranteed latency SLA.

### d4-040 (D4)

- **Q:** Structured Data Extraction scenario (Scenario 6)—primary domains?
- **A:** D4 (schemas, validation, batch) and D5 (reliability, human review for low confidence).

### d5-002 (D5)

- **Q:** Risk of progressive summarization in long support sessions?
- **A:** Condenses amounts, dates, percentages, and customer-stated expectations into vague summaries—loses critical transactional facts.

### d5-004 (D5)

- **Q:** Preserve order amounts and dates across a long support conversation?
- **A:** Extract transactional facts into a persistent case facts block in each prompt—outside summarized history.
- **Why:** outside summarized history.

### d5-010 (D5)

- **Q:** Three appropriate escalation triggers (beyond 'complex case')?
- **A:** Customer explicitly requests human, policy exception/gap, and inability to make meaningful progress.

### d5-018 (D5)

- **Q:** Subagents need prior search results. Best context passing?
- **A:** Explicit structured handoffs (IDs, snippets, citations) via coordinator—not implicit shared memory.
- **Why:** not implicit shared memory.

### d5-030 (D5)

- **Q:** Calibrate human review routing for extractions?
- **A:** Model outputs field-level confidence; calibrate thresholds using labeled validation sets.
- **Why:** Multi-pass or independent review reduces attention dilution and self-review bias in large change sets.

### d5-034 (D5)

- **Q:** Subagent output for downstream synthesis—provenance requirement?
- **A:** Structured claim-source mappings (URLs, document names, excerpts) preserved through synthesis.
- **Why:** Exam judgment aligned to task 5.6: Structured claim-source mappings (URLs, document names, excerpts) preserved through synthesis.

### d5-039 (D5)

- **Q:** Which three scenarios list D5 as a primary domain?
- **A:** Customer Support, Multi-Agent Research, and Structured Data Extraction.

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

### meta-005 (META)

- **Q:** Sample Q1 (Customer Support): Why programmatic prerequisite (A) beats prompt, few-shot, or routing for skipped get_customer?
- **A:** Blocks lookup_order and process_refund until get_customer returns verified ID—deterministic enforcement for identity before refunds.
- **Why:** Programmatic enforcement gives deterministic guarantees for required tool sequences; prompt and few-shot rely on probabilistic LLM compliance—insufficient when misidentification causes financial harm. Routing classifiers change tool availability, not ordering.

### meta-006 (META)

- **Q:** Sample Q2 (Customer Support): Why expand tool descriptions (B) before few-shot, routing, or tool consolidation?
- **A:** Descriptions are the primary LLM tool-selection signal—add inputs, examples, edge cases, and boundaries vs similar tools.
- **Why:** Tool descriptions are the primary selection mechanism; minimal descriptions cause confusion between similar tools. Few-shot adds tokens without fixing descriptions; routing is over-engineered for a first step; consolidation is valid but higher effort.

### meta-008 (META)

- **Q:** Sample Q4 (Code Generation): Where should a team-shared /review slash command live?
- **A:** .claude/commands/ in the project repository—version-controlled for everyone who clones the repo.
- **Why:** Project slash commands live in .claude/commands/ and are version-controlled. ~/.claude/commands/ is personal; CLAUDE.md holds instructions not command definitions; .claude/config.json is not the Claude Code command mechanism.

### meta-009 (META)

- **Q:** Sample Q5 (Code Generation): Monolith-to-microservices across dozens of files—why plan mode first (A)?
- **A:** Explore dependencies and design service boundaries before editing—large architectural scope is already stated.
- **Why:** Plan mode fits large architectural work with exploration before edits. Direct execution risks rework when dependencies are unknown; rigid upfront instructions skip discovery; waiting for emergent complexity ignores stated large-scale scope.

### meta-011 (META)

- **Q:** Sample Q7 (Multi-Agent Research): Report covers only visual arts—why coordinator decomposition (B)?
- **A:** Logs show narrow subtasks (digital art, graphic design, photography)—subagents succeeded within assigned scope.
- **Why:** Coordinator logs show decomposition into only visual-arts subtasks—subagents succeeded within narrow assignments. Downstream agents are not the root cause; synthesis, search, and analysis worked within assigned scope.

### meta-013 (META)

- **Q:** Sample Q9 (Multi-Agent Research): 85% simple fact-checks—why scoped verify_fact on synthesis (A)?
- **A:** Least privilege for common lookups; complex verification still routes through coordinator to search agent.
- **Why:** Scoped verify_fact on synthesis covers simple fact-checks while complex work stays with search via coordinator—least privilege. End-of-pass batching creates blocking dependencies; giving synthesis all search tools over-provisions; speculative caching cannot predict verification needs.

### meta-014 (META)

- **Q:** Sample Q10 (CI/CD): Pipeline hangs waiting for input—why -p flag (A)?
- **A:** claude -p runs non-interactive: process prompt, output to stdout, exit—required for CI/CD.
- **Why:** -p (--print) is the documented non-interactive CI mode. CLAUDE_HEADLESS, --batch, and stdin tricks are not the correct Claude Code approach.

### meta-015 (META)

- **Q:** Sample Q11: Batch API for pre-merge checks and overnight reports—why batch only overnight jobs (A)?
- **A:** Batches save ~50% cost but lack latency SLA—unsuitable for blocking merge gates.
- **Why:** Message Batches save cost but lack latency SLA—fine for overnight reports, unsuitable for blocking pre-merge checks. Polling batches for merge gates is unacceptable; custom_id correlates batch results; timeout fallback adds complexity vs matching API to workflow latency needs.

### meta-016 (META)

- **Q:** Sample Q12 (CI/CD): 14-file PR review inconsistent—why split per-file and integration passes (A)?
- **A:** Per-file local analysis then cross-file integration pass—fixes attention dilution across many files.
- **Why:** Split reviews into per-file passes plus a cross-file integration pass—fixes attention dilution. Splitting PRs burdens developers; larger context does not fix attention quality; consensus across passes would suppress intermittently caught bugs.

### sc-002 (CHAIN)

- **Q:** [Customer Support · 2/5] Production data: 12% of cases skip get_customer and call lookup_order by name only, causing wrong refunds. Best fix?
- **A:** Programmatic prerequisite blocking lookup_order and process_refund until get_customer returns verified customer ID.
- **Why:** Money and identity need deterministic enforcement—not prompts alone.

### sc-008 (CHAIN)

- **Q:** [Code Generation · 3/5] Assignment: split monolith into microservices—dozens of files, unclear boundaries. What mode first?
- **A:** Plan mode—explore dependencies and design before editing; direct execution risks costly rework.

### sc-015 (CHAIN)

- **Q:** [Multi-Agent Research · 5/5] Final report must preserve citations through synthesis. What require from subagents?
- **A:** Structured claim–source mappings (URLs, excerpts, dates) preserved through synthesis—not compressed summaries without attribution.

### sc-021 (CHAIN)

- **Q:** [CI/CD · 1/5] Pipeline runs claude 'Review this PR' but hangs waiting for input. Fix?
- **A:** Use -p (--print) for non-interactive mode—process prompt, output, exit.

### sc-027 (CHAIN)

- **Q:** [Structured Extraction · 2/5] Source docs often omit optional fields—model fabricates values. Schema fix?
- **A:** Make fields optional/nullable when information may be absent—don't require missing data.

