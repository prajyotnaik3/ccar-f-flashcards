# D1: Agentic Architecture & Orchestration

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

