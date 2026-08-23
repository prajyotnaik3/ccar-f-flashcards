# CCAR-F Exam-Day Cheat Sheet

Auto-generated from flashcards with `exam_day: true`.

**14 cards** — review the night before the exam.

### d1-002 (D1)

- **Q:** Support agent must verify identity before refund tools run. Best first approach?
- **A:** Structural gate: prerequisite step, scoped tool permissions, or hook—before relying on prompt rules.
- **Why:** Identity and money require deterministic enforcement.

### d1-005 (D1)

- **Q:** When should a support agent escalate to a human instead of continuing the loop?
- **A:** When policy requires human judgment, identity cannot be verified, tool failures persist, or confidence/validation thresholds are not met.

### d1-006 (D1)

- **Q:** Developer Productivity scenario—primary domains tested?
- **A:** D2 (tools/MCP), D3 (Claude Code), D1 (delegation/orchestration).

### d2-002 (D2)

- **Q:** Refund tool should only run after verified identity. MCP/tool design choice?
- **A:** Narrow tool exposure: separate tools with least privilege, or a refund tool that requires verified session token from a prior identity tool.

### d3-002 (D3)

- **Q:** Plan mode vs full Agent mode in Claude Code for a large refactor?
- **A:** Plan mode when you want reviewable steps before edits; Agent mode when executing a well-scoped implementation with approvals.

### d3-005 (D3)

- **Q:** CI/CD with Claude Code scenario—primary domains?
- **A:** D3 (Claude Code config), D4 (structured output for findings), D5 (reliability in automated runs).

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

