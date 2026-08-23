# D3: Claude Code Configuration & Workflows

## d3-001 · concept · code_generation, developer_productivity

**Q:** What is CLAUDE.md in Claude Code workflows?

**A:** Project instructions and context Claude Code loads to align behavior, conventions, and constraints.

**Tags:** claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1
- https://docs.anthropic.com/en/docs/claude-code/overview

---

## d3-002 · concept · code_generation, developer_productivity

**Q:** CLAUDE.md configuration hierarchy (three levels)?

**A:** User (~/.claude/CLAUDE.md), project (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files).

**Tags:** claude_md, hierarchy

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-003 · decision · code_generation

**Q:** New teammate doesn't receive team coding standards in Claude Code. Likely cause?

**A:** Instructions are in user-level ~/.claude/CLAUDE.md—not shared via version control; move to project-level config.

**Tags:** claude_md, hierarchy

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-004 · concept · code_generation

**Q:** What is @import syntax in CLAUDE.md?

**A:** References external files to keep CLAUDE.md modular—import standards files relevant to each package.

**Tags:** claude_md, import

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-005 · decision · code_generation

**Q:** Monolithic CLAUDE.md is hard to maintain. Alternative organization?

**A:** Split into focused files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md).

**Tags:** claude_md, rules

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-006 · decision · code_generation

**Q:** Inconsistent Claude Code behavior across sessions—how diagnose loaded config?

**A:** Use /memory to verify which memory files are loaded and what context is active.

**Tags:** claude_md, memory

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-007 · anti_pattern · code_generation

**Q:** Why skip shared project CLAUDE.md when multiple developers use Claude Code?

**A:** Inconsistent conventions, duplicated prompt context, and drift in how the agent edits code across teammates.

**Tags:** claude_md, team

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-008 · decision · code_generation, ci_cd

**Q:** Team /review slash command for every developer on clone. Where create it?

**A:** .claude/commands/ in the project repository—version-controlled and shared on clone/pull.

**Tags:** slash_commands

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2; Sample Q4

---

## d3-009 · compare · code_generation

**Q:** Project-scoped vs user-scoped slash commands?

**A:** .claude/commands/ in repo (shared via git) vs ~/.claude/commands/ (personal, not version controlled).

**Tags:** slash_commands, scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-010 · concept · code_generation, developer_productivity

**Q:** Skill frontmatter options in .claude/skills/SKILL.md (name three)?

**A:** context: fork, allowed-tools, and argument-hint.

**Tags:** skills, frontmatter

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-011 · decision · code_generation

**Q:** Skill produces verbose codebase analysis output. Frontmatter to isolate it?

**A:** context: fork—runs skill in isolated sub-agent context so output doesn't pollute main conversation.

**Tags:** skills, context_fork

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-012 · decision · code_generation

**Q:** Skill should only write files, not run destructive shell commands. Frontmatter?

**A:** allowed-tools restricting tool access during skill execution (e.g., file write operations only).

**Tags:** skills, allowed_tools

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-013 · decision · code_generation

**Q:** Developer invokes skill without required arguments. Frontmatter help?

**A:** argument-hint prompts for required parameters when the skill is invoked without them.

**Tags:** skills, argument_hint

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-014 · compare · code_generation

**Q:** Skills vs CLAUDE.md—when use each?

**A:** Skills: on-demand task-specific workflows. CLAUDE.md: always-loaded universal standards for the project.

**Tags:** skills, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-015 · decision · code_generation

**Q:** Personal skill customization without affecting teammates?

**A:** Create personal variants in ~/.claude/skills/ with different names—not in shared project skills.

**Tags:** skills, scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-016 · concept · code_generation

**Q:** How do .claude/rules/ path-specific rules activate?

**A:** YAML frontmatter paths field with glob patterns—rules load only when editing matching files.

**Tags:** rules, path_scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-017 · decision · code_generation

**Q:** Test files spread as Button.test.tsx next to Button.tsx. Apply test conventions automatically?

**A:** .claude/rules/ with glob paths like **/*.test.tsx—applies by file type across all directories.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-018 · decision · code_generation

**Q:** React, API, and DB areas need different conventions; tests scattered everywhere. Best maintainable approach?

**A:** .claude/rules/ with YAML frontmatter glob patterns (e.g., paths: ["**/*.test.tsx"], ["src/api/**/*"])—not inference from one monolithic CLAUDE.md.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-019 · compare · code_generation

**Q:** Path-specific rules vs subdirectory CLAUDE.md for scattered test files?

**A:** Path-specific glob rules apply by file pattern anywhere in the tree; subdirectory CLAUDE.md is directory-bound.

**Tags:** rules, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-020 · concept · code_generation

**Q:** Benefit of path-scoped rules loading only on matching files?

**A:** Reduces irrelevant context and token usage—conventions apply only when relevant.

**Tags:** rules, context

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-021 · decision · code_generation

**Q:** Restructure monolith into microservices—dozens of files, architectural decisions. Approach?

**A:** Plan mode: explore codebase, understand dependencies, design approach before making changes.

**Tags:** plan_mode

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-022 · compare · code_generation

**Q:** Plan mode vs direct execution—when use each?

**A:** Plan mode: large-scale, multi-file, architectural, multiple valid approaches. Direct execution: simple, well-scoped single changes.

**Tags:** plan_mode, direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-023 · decision · code_generation

**Q:** Single-file bug fix with clear stack trace. Plan mode or direct execution?

**A:** Direct execution—well-understood change with clear scope.

**Tags:** direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-024 · concept · code_generation

**Q:** What is the Explore subagent used for in Claude Code?

**A:** Isolates verbose discovery output and returns summaries—preserves main conversation context during exploration.

**Tags:** Explore_subagent, context

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-025 · decision · code_generation

**Q:** Library migration affecting 45+ files—workflow pattern?

**A:** Plan mode for investigation and design, then direct execution to implement the planned approach.

**Tags:** plan_mode, direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-026 · anti_pattern · code_generation

**Q:** Start monolith-to-microservices in direct execution, switch to plan if complexity emerges. Why wrong?

**A:** Complexity is already stated—plan first prevents costly rework from late-discovered dependencies.

**Tags:** plan_mode, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-027 · decision · code_generation

**Q:** Natural language transformation spec produces inconsistent code. Best fix?

**A:** Provide 2–3 concrete input/output examples showing expected transformations.

**Tags:** iterative_refinement, examples

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-028 · concept · code_generation

**Q:** Test-driven iteration pattern with Claude Code?

**A:** Write tests first (behavior, edge cases, performance), then iterate by sharing test failures to guide fixes.

**Tags:** iterative_refinement, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-029 · concept · code_generation

**Q:** What is the interview pattern in Claude Code workflows?

**A:** Have Claude ask clarifying questions to surface design considerations before implementing in unfamiliar domains.

**Tags:** iterative_refinement, interview

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-030 · compare · code_generation

**Q:** Fix multiple issues in one message vs sequentially?

**A:** Single message when fixes interact; sequential iteration when issues are independent.

**Tags:** iterative_refinement

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-031 · decision · code_generation

**Q:** Migration script mishandles null edge cases. Iteration approach?

**A:** Provide specific test cases with example input and expected output for the failing edge case.

**Tags:** iterative_refinement, edge_cases

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-032 · decision · ci_cd

**Q:** CI job hangs—Claude Code waiting for interactive input. Fix?

**A:** Use -p (or --print) flag for non-interactive mode: process prompt, output result, exit.

**Tags:** ci_cd, non_interactive

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6; Sample Q10

---

## d3-033 · decision · ci_cd

**Q:** Post structured PR review findings as inline comments from CI. CLI flags?

**A:** --output-format json with --json-schema for machine-parseable structured findings.

**Tags:** ci_cd, structured_output

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-034 · concept · ci_cd

**Q:** How provide project context to CI-invoked Claude Code?

**A:** CLAUDE.md with testing standards, fixture conventions, and review criteria loaded automatically.

**Tags:** ci_cd, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-035 · concept · ci_cd

**Q:** Why use an independent Claude instance to review code it generated in the same session?

**A:** Session context isolation—generator retains reasoning context and is less likely to question its own decisions.

**Tags:** ci_cd, self_review

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-036 · decision · ci_cd

**Q:** Re-run PR review after new commits—avoid duplicate inline comments?

**A:** Include prior review findings in context; instruct Claude to report only new or still-unaddressed issues.

**Tags:** ci_cd, review

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-037 · decision · ci_cd

**Q:** CI test generation suggests scenarios already in the suite. Context fix?

**A:** Provide existing test files in context so generation avoids duplicate coverage.

**Tags:** ci_cd, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-038 · decision · ci_cd, code_generation

**Q:** Reduce low-value generated tests in Claude Code?

**A:** Document testing standards, valuable test criteria, and available fixtures in CLAUDE.md.

**Tags:** claude_md, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-039 · decision · ci_cd

**Q:** Running Claude Code in CI for PR review. Critical configuration concerns?

**A:** Non-interactive (-p), explicit permissions, structured/deterministic outputs, independent review instance—not open-ended agent runs.

**Tags:** ci_cd, automation

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-040 · anti_pattern · ci_cd

**Q:** CI non-interactive flags that do NOT exist (name two)?

**A:** CLAUDE_HEADLESS env var and --batch flag—use -p/--print instead.

**Tags:** ci_cd, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6; Sample Q10

---

## d3-041 · scenario_hook · code_generation

**Q:** Code Generation scenario (Scenario 2)—primary domains?

**A:** D3 (Claude Code config/workflows) and D5 (context management/reliability).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d3-042 · scenario_hook · ci_cd

**Q:** CI/CD with Claude Code scenario (Scenario 5)—primary domains?

**A:** D3 (Claude Code) and D4 (prompt engineering/structured output for review findings).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d3-043 · scenario_hook · developer_productivity, code_generation

**Q:** Scenario 2 tools: slash commands, CLAUDE.md, plan mode—what is being tested?

**A:** Integrating Claude Code into dev workflow: team config, custom commands, and when to plan vs execute directly.

**Tags:** scenarios, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2

---

## d3-044 · concept · code_generation

**Q:** Example path-scoped rule for Terraform files only?

**A:** .claude/rules/ file with frontmatter paths: ["terraform/**/*"] loading only when editing matching files.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-045 · anti_pattern · code_generation

**Q:** Put all area conventions in root CLAUDE.md headers—rely on Claude to infer which applies. Why unreliable?

**A:** Relies on inference vs explicit path matching—rules with glob patterns give deterministic automatic application.

**Tags:** rules, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

