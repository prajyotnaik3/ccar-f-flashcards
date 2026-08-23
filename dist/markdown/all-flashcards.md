# CCAR-F Flashcards (All)

## d1-001 · concept · customer_support, multi_agent_research

**Q:** What is an agentic loop in Claude-based systems?

**A:** A cycle where the model plans, invokes tools, observes results, and iterates until the task completes or escalates.

**Tags:** agent_loop

**Sources:**
- Official CCAR-F Exam Guide — D1
- https://docs.anthropic.com/en/docs/agents-and-tools/agent-sdk/overview

---

## d1-002 · decision · customer_support

**Q:** Support agent must verify identity before refund tools run. Best first approach?

**A:** Structural gate: prerequisite step, scoped tool permissions, or hook—before relying on prompt rules.

**Why:** Identity and money require deterministic enforcement.

**Tags:** escalation, identity

**Sources:**
- Official CCAR-F Exam Guide — D1, Customer Support scenario

---

## d1-003 · compare · multi_agent_research

**Q:** Single agent with many tools vs coordinator + specialized subagents for research pipeline?

**A:** Coordinator + subagents when tasks decompose cleanly (search, analyze, synthesize) and need isolated context and failure boundaries.

**Tags:** orchestration, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1, Multi-Agent Research scenario

---

## d1-004 · anti_pattern · multi_agent_research

**Q:** Why is letting a coordinator invent subagent outputs without tool results an anti-pattern?

**A:** Breaks provenance and reliability; coordinator should delegate via tools and pass explicit context, not hallucinate worker results.

**Tags:** provenance, subagents

**Sources:**
- Official CCAR-F Exam Guide — D1

---

## d1-005 · decision · customer_support

**Q:** When should a support agent escalate to a human instead of continuing the loop?

**A:** When policy requires human judgment, identity cannot be verified, tool failures persist, or confidence/validation thresholds are not met.

**Tags:** escalation

**Sources:**
- Official CCAR-F Exam Guide — D1, D5 crossover

---

## d1-006 · scenario_hook · developer_productivity

**Q:** Developer Productivity scenario—primary domains tested?

**A:** D2 (tools/MCP), D3 (Claude Code), D1 (delegation/orchestration).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

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

