# CCAR-F Exam Guide — study index

Use this page to navigate the **official Exam Guide** alongside flashcards in this repo. Read the PDF for full detail; use filters here for recall.

**Official PDF:** [Download from Partner Academy](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification) · [Direct link](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542750%2FClaude+Certified+Architect+%E2%80%93+Foundations+Exam+Guide.pdf)

**Local PDF (optional):** `docs/exam-guide/CCAR-F-Exam-Guide.pdf` — see [exam-guide/README.md](exam-guide/README.md)

**Live flashcards:** [Web viewer](https://prajyotnaik3.github.io/ccar-f-flashcards/) · [Study hub](https://prajyotnaik3.github.io/ccar-f-flashcards/study.html)

---

## Recommended workflow

1. **Skim** PDF Sections 1–3 (audience, format, blueprint weights).
2. **Read** Section 5 — all **6 scenarios** ([scenarios.md](scenarios.md)).
3. **Study one domain:** read task statements in PDF Section 6 → review matching YAML → drill cards filtered by domain.
4. **Read rationales** in PDF Section 9 (sample questions) — explains why distractors fail.
5. **Build** at least two exercises from PDF Section 8.

---

## PDF section map

| Section | Topic | Repo companion |
|---------|--------|----------------|
| 1–3 | Certification overview, audience, exam format | [meta.yaml](../flashcards/domains/meta.yaml) |
| 4 | Blueprint weights | Study plan [week 1–3](study-plan-4-weeks.md) |
| 5 | Six scenarios | [scenarios.md](scenarios.md) |
| 6 | Task statements D1–D5 | Domain YAML below |
| 7 | How to prepare | [sources.md](sources.md) |
| 8 | Hands-on exercises | Do in your own project |
| 9 | Sample questions + rationales | **Read every rationale** · [Sample Q cards](https://prajyotnaik3.github.io/ccar-f-flashcards/?domain=META) (`meta-005`–`meta-016`) |
| 10–16 | Scoring, registration, policies | Expand meta cards (future) |
| 17 | Appendix: in/out of scope tech | [sources.md](sources.md) |

---

## Domain 1 — Agentic Architecture & Orchestration (27%)

Flashcards: [`d1-agentic-architecture.yaml`](../flashcards/domains/d1-agentic-architecture.yaml) · [Filter D1 in viewer](https://prajyotnaik3.github.io/ccar-f-flashcards/?domain=D1) · [D1 task notes](https://prajyotnaik3.github.io/ccar-f-flashcards/?kind=notes&domain=D1)

| Task | Topic |
|------|--------|
| 1.1 | Agentic loops, `stop_reason`, tool results in history |
| 1.2 | Coordinator–subagent, hub-and-spoke, refinement loops |
| 1.3 | Task tool, context passing, parallel spawn, AgentDefinition |
| 1.4 | Prerequisite gates, multi-concern decomposition, human handoffs |
| 1.5 | Hooks: PostToolUse, tool interception, compliance |
| 1.6 | Task decomposition: prompt chaining vs adaptive plans |
| 1.7 | Session resume, `fork_session`, stale context |

**Scenarios:** Customer Support, Multi-Agent Research, Developer Productivity (partial)

---

## Domain 2 — Tool Design & MCP Integration (18%)

Flashcards: [`d2-tool-design-mcp.yaml`](../flashcards/domains/d2-tool-design-mcp.yaml) · [Filter D2](https://prajyotnaik3.github.io/ccar-f-flashcards/?domain=D2) · [D2 task notes](https://prajyotnaik3.github.io/ccar-f-flashcards/?kind=notes&domain=D2)

| Task | Topic |
|------|--------|
| 2.1 | Tool descriptions, boundaries, splitting overlapping tools |
| 2.2 | MCP `isError`, structured errors, retryable vs business errors |
| 2.3 | Tool scoping per agent, `tool_choice` (auto/any/forced) |
| 2.4 | `.mcp.json` vs `~/.claude.json`, resources, env vars |
| 2.5 | Built-in tools: Grep, Glob, Read, Write, Edit, Bash |

**Scenarios:** Customer Support, Multi-Agent Research, Developer Productivity

---

## Domain 3 — Claude Code Configuration & Workflows (20%)

Flashcards: [`d3-claude-code.yaml`](../flashcards/domains/d3-claude-code.yaml) · [Filter D3](https://prajyotnaik3.github.io/ccar-f-flashcards/?domain=D3) · [D3 task notes](https://prajyotnaik3.github.io/ccar-f-flashcards/?kind=notes&domain=D3)

| Task | Topic |
|------|--------|
| 3.1 | CLAUDE.md hierarchy, `@import`, `.claude/rules/`, `/memory` |
| 3.2 | Slash commands, skills, `context: fork`, `allowed-tools` |
| 3.3 | Path-scoped rules with glob patterns |
| 3.4 | Plan mode vs direct execution, Explore subagent |
| 3.5 | I/O examples, test-driven iteration, interview pattern |
| 3.6 | CI: `-p`, `--json-schema`, independent review instance |

**Scenarios:** Code Generation, CI/CD, Developer Productivity (partial)

---

## Domain 4 — Prompt Engineering & Structured Output (20%)

Flashcards: [`d4-prompt-structured-output.yaml`](../flashcards/domains/d4-prompt-structured-output.yaml) · [Filter D4](https://prajyotnaik3.github.io/ccar-f-flashcards/?domain=D4) · [D4 task notes](https://prajyotnaik3.github.io/ccar-f-flashcards/?kind=notes&domain=D4)

| Task | Topic |
|------|--------|
| 4.1 | Explicit review criteria, false-positive management |
| 4.2 | Few-shot prompting for format and ambiguous cases |
| 4.3 | `tool_use` + JSON schema, nullable fields, enums |
| 4.4 | Validation-retry, semantic vs syntax errors |
| 4.5 | Message Batches API, latency vs cost |
| 4.6 | Multi-instance review, multi-pass PR analysis |

**Scenarios:** Structured Extraction, CI/CD

---

## Domain 5 — Context Management & Reliability (15%)

Flashcards: [`d5-context-reliability.yaml`](../flashcards/domains/d5-context-reliability.yaml) · [Filter D5](https://prajyotnaik3.github.io/ccar-f-flashcards/?domain=D5) · [D5 task notes](https://prajyotnaik3.github.io/ccar-f-flashcards/?kind=notes&domain=D5)

| Task | Topic |
|------|--------|
| 5.1 | Case facts, trimming tool output, lost-in-the-middle |
| 5.2 | Escalation triggers, policy gaps, ambiguity resolution |
| 5.3 | Error propagation, coverage annotations |
| 5.4 | Scratchpad files, `/compact`, crash recovery manifests |
| 5.5 | Human review routing, stratified sampling, calibration |
| 5.6 | Provenance, claim–source mappings, temporal data |

**Scenarios:** Customer Support, Multi-Agent Research, Structured Extraction, Code Generation (partial)

---

## Scenario → domain quick links

| Scenario | Filter in viewer |
|----------|------------------|
| Customer Support | [customer_support](https://prajyotnaik3.github.io/ccar-f-flashcards/?scenario=customer_support) |
| Code Generation | [code_generation](https://prajyotnaik3.github.io/ccar-f-flashcards/?scenario=code_generation) |
| Multi-Agent Research | [multi_agent_research](https://prajyotnaik3.github.io/ccar-f-flashcards/?scenario=multi_agent_research) |
| Developer Productivity | [developer_productivity](https://prajyotnaik3.github.io/ccar-f-flashcards/?scenario=developer_productivity) |
| CI/CD | [ci_cd](https://prajyotnaik3.github.io/ccar-f-flashcards/?scenario=ci_cd) |
| Structured Extraction | [structured_extraction](https://prajyotnaik3.github.io/ccar-f-flashcards/?scenario=structured_extraction) |

---

## Section 8 exercises (do these hands-on)

| Exercise | Domains reinforced |
|----------|-------------------|
| Multi-tool agent with escalation | D1, D2, D5 |
| Claude Code team workflow | D3, D2 |
| Structured extraction pipeline | D4, D5 |
| Multi-agent research pipeline | D1, D2, D5 |
