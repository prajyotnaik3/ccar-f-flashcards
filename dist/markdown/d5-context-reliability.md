# D5: Context Management & Reliability

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

