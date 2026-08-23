# META: Exam Meta

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

## meta-005 · sample_rationale · customer_support

**Tasks:** cross-domain

**Q:** Sample Q1 (Customer Support): Why programmatic prerequisite (A) beats prompt, few-shot, or routing for skipped get_customer?

**A:** Blocks lookup_order and process_refund until get_customer returns verified ID—deterministic enforcement for identity before refunds.

**Why:** Programmatic enforcement gives deterministic guarantees for required tool sequences; prompt and few-shot rely on probabilistic LLM compliance—insufficient when misidentification causes financial harm. Routing classifiers change tool availability, not ordering.

**Tags:** sample_rationale, sample_q1, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q1

---

## meta-006 · sample_rationale · customer_support

**Tasks:** cross-domain

**Q:** Sample Q2 (Customer Support): Why expand tool descriptions (B) before few-shot, routing, or tool consolidation?

**A:** Descriptions are the primary LLM tool-selection signal—add inputs, examples, edge cases, and boundaries vs similar tools.

**Why:** Tool descriptions are the primary selection mechanism; minimal descriptions cause confusion between similar tools. Few-shot adds tokens without fixing descriptions; routing is over-engineered for a first step; consolidation is valid but higher effort.

**Tags:** sample_rationale, sample_q2, customer_support

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q2

---

## meta-007 · sample_rationale · customer_support

**Tasks:** cross-domain

**Q:** Sample Q3 (Customer Support): Why explicit escalation criteria with few-shot (A) beats confidence scores, classifiers, or sentiment?

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

**Q:** Sample Q5 (Code Generation): Monolith-to-microservices across dozens of files—why plan mode first (A)?

**A:** Explore dependencies and design service boundaries before editing—large architectural scope is already stated.

**Why:** Plan mode fits large architectural work with exploration before edits. Direct execution risks rework when dependencies are unknown; rigid upfront instructions skip discovery; waiting for emergent complexity ignores stated large-scale scope.

**Tags:** sample_rationale, sample_q5, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q5

---

## meta-010 · sample_rationale · code_generation

**Tasks:** cross-domain

**Q:** Sample Q6 (Code Generation): Tests spread as *.test.tsx—why .claude/rules/ with globs (A)?

**A:** Glob patterns (e.g. **/*.test.tsx) auto-apply conventions by path regardless of directory.

**Why:** .claude/rules/ with glob patterns apply conventions by file path—including tests spread across directories. Root CLAUDE.md relies on inference; skills need invocation; per-directory CLAUDE.md cannot cover scattered test files.

**Tags:** sample_rationale, sample_q6, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q6

---

## meta-011 · sample_rationale · multi_agent_research

**Tasks:** cross-domain

**Q:** Sample Q7 (Multi-Agent Research): Report covers only visual arts—why coordinator decomposition (B)?

**A:** Logs show narrow subtasks (digital art, graphic design, photography)—subagents succeeded within assigned scope.

**Why:** Coordinator logs show decomposition into only visual-arts subtasks—subagents succeeded within narrow assignments. Downstream agents are not the root cause; synthesis, search, and analysis worked within assigned scope.

**Tags:** sample_rationale, sample_q7, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q7

---

## meta-012 · sample_rationale · multi_agent_research

**Tasks:** cross-domain

**Q:** Sample Q8 (Multi-Agent Research): Search subagent times out—why structured error context to coordinator (A)?

**A:** Return failure type, attempted query, partial results, and alternatives so coordinator can recover intelligently.

**Why:** Structured error context enables coordinator recovery (retry, alternate query, partial results). Generic retry status hides context; marking failure as success blocks recovery; terminating the whole workflow is unnecessary when partial progress exists.

**Tags:** sample_rationale, sample_q8, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q8

---

## meta-013 · sample_rationale · multi_agent_research

**Tasks:** cross-domain

**Q:** Sample Q9 (Multi-Agent Research): 85% simple fact-checks—why scoped verify_fact on synthesis (A)?

**A:** Least privilege for common lookups; complex verification still routes through coordinator to search agent.

**Why:** Scoped verify_fact on synthesis covers simple fact-checks while complex work stays with search via coordinator—least privilege. End-of-pass batching creates blocking dependencies; giving synthesis all search tools over-provisions; speculative caching cannot predict verification needs.

**Tags:** sample_rationale, sample_q9, multi_agent_research

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q9

---

## meta-014 · sample_rationale · ci_cd

**Tasks:** cross-domain

**Q:** Sample Q10 (CI/CD): Pipeline hangs waiting for input—why -p flag (A)?

**A:** claude -p runs non-interactive: process prompt, output to stdout, exit—required for CI/CD.

**Why:** -p (--print) is the documented non-interactive CI mode. CLAUDE_HEADLESS, --batch, and stdin tricks are not the correct Claude Code approach.

**Tags:** sample_rationale, sample_q10, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q10

---

## meta-015 · sample_rationale · structured_extraction, ci_cd

**Tasks:** cross-domain

**Q:** Sample Q11: Batch API for pre-merge checks and overnight reports—why batch only overnight jobs (A)?

**A:** Batches save ~50% cost but lack latency SLA—unsuitable for blocking merge gates.

**Why:** Message Batches save cost but lack latency SLA—fine for overnight reports, unsuitable for blocking pre-merge checks. Polling batches for merge gates is unacceptable; custom_id correlates batch results; timeout fallback adds complexity vs matching API to workflow latency needs.

**Tags:** sample_rationale, sample_q11, structured_extraction, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q11

---

## meta-016 · sample_rationale · ci_cd

**Tasks:** cross-domain

**Q:** Sample Q12 (CI/CD): 14-file PR review inconsistent—why split per-file and integration passes (A)?

**A:** Per-file local analysis then cross-file integration pass—fixes attention dilution across many files.

**Why:** Split reviews into per-file passes plus a cross-file integration pass—fixes attention dilution. Splitting PRs burdens developers; larger context does not fix attention quality; consensus across passes would suppress intermittently caught bugs.

**Tags:** sample_rationale, sample_q12, ci_cd

**Sources:**
- Official CCAR-F Exam Guide — Section 9, Sample Q12

