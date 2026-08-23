# D3: Claude Code Configuration & Workflows

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

