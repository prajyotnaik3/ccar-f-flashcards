# D3: Claude Code Configuration & Workflows

## d3-001 · concept · code_generation, developer_productivity

**Tasks:** 3.1

**Q:** What is CLAUDE.md in Claude Code workflows?

**A:** Project instructions and context Claude Code loads to align behavior, conventions, and constraints.

**Tags:** claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1
- https://docs.anthropic.com/en/docs/claude-code/overview

---

## d3-002 · concept · code_generation, developer_productivity

**Tasks:** 3.1

**Q:** What are the three levels of the CLAUDE.md configuration hierarchy?

**A:** User (~/.claude/CLAUDE.md), project (.claude/CLAUDE.md or root CLAUDE.md), and directory-level (subdirectory CLAUDE.md files).

**Tags:** claude_md, hierarchy

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-003 · decision · code_generation

**Tasks:** 3.1

**Q:** A new teammate does not receive team coding standards in Claude Code. What is the likely cause?

**A:** Instructions are in user-level ~/.claude/CLAUDE.md—not shared via version control; move to project-level config.

**Why:** User-level ~/.claude/CLAUDE.md is not in git. Team standards belong in project CLAUDE.md so clones pick them up.

**Tags:** claude_md, hierarchy

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-004 · concept · code_generation

**Tasks:** 3.1

**Q:** What is @import syntax in CLAUDE.md?

**A:** References external files to keep CLAUDE.md modular—import standards files relevant to each package.

**Tags:** claude_md, import

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-005 · decision · code_generation

**Tasks:** 3.1

**Q:** A monolithic CLAUDE.md is hard to maintain. How should you reorganize it?

**A:** Split into focused files in .claude/rules/ (e.g., testing.md, api-conventions.md, deployment.md).

**Why:** Split a monolithic CLAUDE.md into focused files under .claude/rules/ (testing.md, api-conventions.md, deployment.md) instead of one huge always-loaded file.

**Tags:** claude_md, rules

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-006 · decision · code_generation

**Tasks:** 3.1

**Q:** Claude Code behaves inconsistently across sessions. How do you diagnose which config is loaded?

**A:** Use /memory to verify which memory files are loaded and what context is active.

**Why:** /memory shows which memory files are loaded. Use it when behavior drifts across sessions because the wrong CLAUDE.md layer is active.

**Tags:** claude_md, memory

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-007 · anti_pattern · code_generation

**Tasks:** 3.1

**Q:** Why is it a problem to skip a shared project CLAUDE.md when multiple developers use Claude Code?

**A:** Inconsistent conventions, duplicated prompt context, and drift in how the agent edits code across teammates.

**Tags:** claude_md, team

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.1

---

## d3-008 · decision · code_generation, ci_cd

**Tasks:** 3.2

**Q:** Where should you create a team /review slash command so every developer gets it on clone?

**A:** .claude/commands/ in the project repository—version-controlled and shared on clone/pull.

**Why:** Project slash commands live in .claude/commands/ and are version-controlled for the team. ~/.claude/commands/ is personal; CLAUDE.md holds instructions not command definitions; .claude/config.json is not the Claude Code command mechanism.

**Tags:** slash_commands

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2; Sample Q4

---

## d3-009 · compare · code_generation

**Tasks:** 3.2

**Q:** How do project-scoped and user-scoped slash commands differ?

**A:** .claude/commands/ in repo (shared via git) vs ~/.claude/commands/ (personal, not version controlled).

**Tags:** slash_commands, scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-010 · concept · code_generation, developer_productivity

**Tasks:** 3.2

**Q:** Name three Skill frontmatter options in .claude/skills/SKILL.md.

**A:** context: fork, allowed-tools, and argument-hint.

**Tags:** skills, frontmatter

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-011 · decision · code_generation

**Tasks:** 3.2

**Q:** A skill produces verbose codebase analysis. Which frontmatter option isolates that output?

**A:** context: fork—runs skill in isolated sub-agent context so output doesn't pollute main conversation.

**Why:** runs skill in isolated sub-agent context so output doesn't pollute main conversation.

**Tags:** skills, context_fork

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-012 · decision · code_generation

**Tasks:** 3.2

**Q:** A skill should only write files, not run destructive shell commands. Which frontmatter option enforces that?

**A:** allowed-tools restricting tool access during skill execution (e.g., file write operations only).

**Why:** allowed-tools in skill frontmatter limits what the skill can invoke—for example file writes only, so it cannot run destructive shell commands.

**Tags:** skills, allowed_tools

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-013 · decision · code_generation

**Tasks:** 3.2

**Q:** A developer invokes a skill without required arguments. Which frontmatter option helps?

**A:** argument-hint prompts for required parameters when the skill is invoked without them.

**Why:** Exam judgment aligned to task 3.2: argument-hint prompts for required parameters when the skill is invoked without them.

**Tags:** skills, argument_hint

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-014 · compare · code_generation

**Tasks:** 3.2

**Q:** When should you use Skills versus CLAUDE.md?

**A:** Skills: on-demand task-specific workflows. CLAUDE.md: always-loaded universal standards for the project.

**Tags:** skills, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-015 · decision · code_generation

**Tasks:** 3.2

**Q:** How do you customize a skill for yourself without affecting teammates?

**A:** Create personal variants in ~/.claude/skills/ with different names—not in shared project skills.

**Why:** not in shared project skills.

**Tags:** skills, scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-016 · concept · code_generation

**Tasks:** 3.3

**Q:** How do .claude/rules/ path-specific rules activate?

**A:** YAML frontmatter paths field with glob patterns—rules load only when editing matching files.

**Tags:** rules, path_scoping

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-017 · decision · code_generation

**Tasks:** 3.3

**Q:** Test files sit as Button.test.tsx next to Button.tsx. How do you apply test conventions automatically?

**A:** .claude/rules/ with glob paths like **/*.test.tsx—applies by file type across all directories.

**Why:** .claude/rules/ with glob patterns apply conventions by file path—including tests spread across directories. Root CLAUDE.md relies on inference; skills need invocation; per-directory CLAUDE.md cannot cover scattered test files.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-018 · decision · code_generation

**Tasks:** 3.3

**Q:** React, API, and DB areas need different conventions; tests scattered everywhere. Best maintainable approach?

**A:** .claude/rules/ with YAML frontmatter glob patterns (e.g., paths: ["**/*.test.tsx"], ["src/api/**/*"])—not inference from one monolithic CLAUDE.md.

**Why:** .claude/rules/ with glob patterns apply conventions by file path—including tests spread across directories. Root CLAUDE.md relies on inference; skills need invocation; per-directory CLAUDE.md cannot cover scattered test files.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-019 · compare · code_generation

**Tasks:** 3.3

**Q:** For scattered test files, when should you use path-specific rules versus subdirectory CLAUDE.md?

**A:** Path-specific glob rules apply by file pattern anywhere in the tree; subdirectory CLAUDE.md is directory-bound.

**Tags:** rules, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-020 · concept · code_generation

**Tasks:** 3.3

**Q:** What is the benefit of path-scoped rules loading only for matching files?

**A:** Reduces irrelevant context and token usage—conventions apply only when relevant.

**Tags:** rules, context

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-021 · decision · code_generation

**Tasks:** 3.4

**Q:** You need to restructure a monolith into microservices across dozens of files. Which approach should you take first?

**A:** Plan mode: explore codebase, understand dependencies, design approach before making changes.

**Why:** Plan mode fits large architectural work with exploration before edits. Direct execution risks rework when dependencies are unknown; upfront rigid instructions skip necessary discovery; switching only if complexity emerges ignores stated large-scale scope.

**Tags:** plan_mode

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-022 · compare · code_generation

**Tasks:** 3.4

**Q:** When should you use plan mode versus direct execution?

**A:** Plan mode: large-scale, multi-file, architectural, multiple valid approaches. Direct execution: simple, well-scoped single changes.

**Tags:** plan_mode, direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-023 · decision · code_generation

**Tasks:** 3.4

**Q:** For a single-file bug fix with a clear stack trace, should you use plan mode or direct execution?

**A:** Direct execution—well-understood change with clear scope.

**Why:** well-understood change with clear scope.

**Tags:** direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-024 · concept · code_generation

**Tasks:** 3.4

**Q:** What is the Explore subagent used for in Claude Code?

**A:** Isolates verbose discovery output and returns summaries—preserves main conversation context during exploration.

**Tags:** Explore_subagent, context

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-025 · decision · code_generation

**Tasks:** 3.4

**Q:** A library migration affects 45+ files. What workflow pattern should you use?

**A:** Plan mode for investigation and design, then direct execution to implement the planned approach.

**Why:** Plan mode for investigation and design on a 45+ file migration, then direct execution to implement the agreed plan.

**Tags:** plan_mode, direct_execution

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4

---

## d3-026 · anti_pattern · code_generation

**Tasks:** 3.4

**Q:** Why is it wrong to start a monolith-to-microservices split in direct execution and switch to plan only if complexity emerges?

**A:** Complexity is already stated—plan first prevents costly rework from late-discovered dependencies.

**Tags:** plan_mode, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-027 · decision · code_generation

**Tasks:** 3.5

**Q:** A natural-language transformation spec produces inconsistent code. What is the best fix?

**A:** Provide 2–3 concrete input/output examples showing expected transformations.

**Why:** Exam judgment aligned to task 3.5: Provide 2–3 concrete input/output examples showing expected transformations.

**Tags:** iterative_refinement, examples

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-028 · concept · code_generation

**Tasks:** 3.5

**Q:** What is the test-driven iteration pattern with Claude Code?

**A:** Write tests first (behavior, edge cases, performance), then iterate by sharing test failures to guide fixes.

**Tags:** iterative_refinement, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-029 · concept · code_generation

**Tasks:** 3.5

**Q:** What is the interview pattern in Claude Code workflows?

**A:** Have Claude ask clarifying questions to surface design considerations before implementing in unfamiliar domains.

**Tags:** iterative_refinement, interview

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-030 · compare · code_generation

**Tasks:** 3.5

**Q:** When should you fix multiple issues in one message versus sequentially?

**A:** Single message when fixes interact; sequential iteration when issues are independent.

**Tags:** iterative_refinement

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-031 · decision · code_generation

**Tasks:** 3.5

**Q:** A migration script mishandles null edge cases. How should you iterate with Claude?

**A:** Provide specific test cases with example input and expected output for the failing edge case.

**Why:** Exam judgment aligned to task 3.5: Provide specific test cases with example input and expected output for the failing edge case.

**Tags:** iterative_refinement, edge_cases

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-032 · decision · ci_cd

**Tasks:** 3.6

**Q:** A CI job hangs because Claude Code is waiting for interactive input. How do you fix that?

**A:** Use -p (or --print) flag for non-interactive mode: process prompt, output result, exit.

**Why:** -p (--print) is the documented non-interactive CI mode: process, output, exit. CLAUDE_HEADLESS, --batch, and stdin tricks are not the correct Claude Code approach.

**Tags:** ci_cd, non_interactive

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6; Sample Q10

---

## d3-033 · decision · ci_cd

**Tasks:** 3.6

**Q:** Which CLI flags post structured PR review findings as inline comments from CI?

**A:** --output-format json with --json-schema for machine-parseable structured findings.

**Why:** --output-format json with --json-schema produces machine-parseable findings so CI can post inline PR comments. This is not a review-architecture question.

**Tags:** ci_cd, structured_output

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-034 · concept · ci_cd

**Tasks:** 3.6

**Q:** How do you provide project context to Claude Code invoked from CI?

**A:** CLAUDE.md with testing standards, fixture conventions, and review criteria loaded automatically.

**Tags:** ci_cd, claude_md

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-035 · concept · ci_cd

**Tasks:** 3.6

**Q:** Why use an independent Claude instance to review code it generated in the same session?

**A:** Session context isolation—generator retains reasoning context and is less likely to question its own decisions.

**Tags:** ci_cd, self_review

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-036 · decision · ci_cd

**Tasks:** 3.6

**Q:** When re-running a PR review after new commits, how do you avoid duplicate inline comments?

**A:** Include prior review findings in context; instruct Claude to report only new or still-unaddressed issues.

**Why:** Pass prior findings back in and instruct Claude to report only new or still-open issues so re-runs do not spam duplicate comments.

**Tags:** ci_cd, review

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-037 · decision · ci_cd

**Tasks:** 3.6

**Q:** CI test generation suggests scenarios already in the suite. What context should you add?

**A:** Provide existing test files in context so generation avoids duplicate coverage.

**Why:** Put existing test files in context so generation does not propose coverage the suite already has.

**Tags:** ci_cd, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-038 · decision · ci_cd, code_generation

**Tasks:** 3.6

**Q:** How do you reduce low-value generated tests in Claude Code?

**A:** Document testing standards, valuable test criteria, and available fixtures in CLAUDE.md.

**Why:** Document testing standards, what a valuable test looks like, and available fixtures in CLAUDE.md so CI generation produces fewer low-value tests.

**Tags:** claude_md, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-039 · decision · ci_cd

**Tasks:** 3.6

**Q:** When running Claude Code in CI for PR review, what configuration concerns matter most?

**A:** Non-interactive (-p), explicit permissions, structured/deterministic outputs, independent review instance—not open-ended agent runs.

**Why:** CI needs -p (non-interactive), tight permissions, structured output, and an independent review instance—not an open-ended interactive agent.

**Tags:** ci_cd, automation

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6

---

## d3-040 · anti_pattern · ci_cd

**Tasks:** 3.6

**Q:** Name two CI non-interactive flags that do not exist for Claude Code.

**A:** CLAUDE_HEADLESS env var and --batch flag—use -p/--print instead.

**Tags:** ci_cd, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.6; Sample Q10

---

## d3-041 · scenario_hook · code_generation

**Tasks:** 3.4, 5.1

**Q:** What are the primary domains for the Code Generation scenario (Scenario 2)?

**A:** D3 (Claude Code config/workflows) and D5 (context management/reliability).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d3-042 · scenario_hook · ci_cd

**Tasks:** 3.6, 4.1

**Q:** What are the primary domains for the CI/CD with Claude Code scenario (Scenario 5)?

**A:** D3 (Claude Code) and D4 (prompt engineering/structured output for review findings).

**Tags:** scenarios

**Sources:**
- Official CCAR-F Exam Guide — scenario map

---

## d3-043 · scenario_hook · developer_productivity, code_generation

**Tasks:** 3.2, 3.4

**Q:** Scenario 2 involves slash commands, CLAUDE.md, and plan mode. What skill is the exam testing?

**A:** Integrating Claude Code into dev workflow: team config, custom commands, and when to plan vs execute directly.

**Tags:** scenarios, code_generation

**Sources:**
- Official CCAR-F Exam Guide — Scenario 2

---

## d3-044 · concept · code_generation

**Tasks:** 3.3

**Q:** What is an example path-scoped rule that applies only to Terraform files?

**A:** .claude/rules/ file with frontmatter paths: ["terraform/**/*"] loading only when editing matching files.

**Tags:** rules, glob

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3

---

## d3-045 · anti_pattern · code_generation

**Tasks:** 3.3

**Q:** Put all area conventions in root CLAUDE.md headers—rely on Claude to infer which applies. Why unreliable?

**A:** Relies on inference vs explicit path matching—rules with glob patterns give deterministic automatic application.

**Tags:** rules, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-046 · anti_pattern · code_generation

**Tasks:** 3.4

**Q:** For a monolith-to-microservices split, why is direct execution with comprehensive upfront structure instructions wrong?

**A:** Assumes structure without codebase exploration—dependencies discovered late cause costly rework; plan first.

**Tags:** plan_mode, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.4; Sample Q5

---

## d3-047 · anti_pattern · code_generation

**Tasks:** 3.3

**Q:** Why is auto-applying conventions via skills in .claude/skills/ insufficient compared with path rules?

**A:** Skills require manual invocation or model choice—not deterministic path-based automatic application.

**Tags:** skills, rules, anti_pattern

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.3; Sample Q6

---

## d3-048 · decision · code_generation

**Tasks:** 3.5

**Q:** In test-driven iteration before implementation, what should the tests cover?

**A:** Expected behavior, edge cases, and performance requirements—iterate by sharing failures with Claude.

**Why:** iterate by sharing failures with Claude.

**Tags:** iterative_refinement, testing

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.5

---

## d3-049 · decision · code_generation

**Tasks:** 3.2

**Q:** Besides verbose codebase analysis, what is another use case for context: fork on skills?

**A:** Exploratory brainstorming of alternatives—isolates speculative output from the main session.

**Why:** isolates speculative output from the main session.

**Tags:** skills, context_fork

**Sources:**
- Official CCAR-F Exam Guide — D3, Task 3.2

---

## d3-050 · scenario_hook · developer_productivity

**Tasks:** 1.2, 2.5, 3.2

**Q:** What are the primary domains for the Developer Productivity scenario (Scenario 4)?

**A:** D2 (built-in tools + MCP), D3 (Claude Code workflows), D1 (delegation/orchestration).

**Tags:** scenarios, developer_productivity

**Sources:**
- Official CCAR-F Exam Guide — scenario map

