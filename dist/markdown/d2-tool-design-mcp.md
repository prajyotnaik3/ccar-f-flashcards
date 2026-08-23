# D2: Tool Design & MCP Integration

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

