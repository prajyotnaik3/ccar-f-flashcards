"""Official Exam Guide Section 9 sample question rationale excerpts (condensed)."""

SAMPLE_Q_RATIONALES: dict[int, str] = {
    1: (
        "Programmatic enforcement gives deterministic guarantees for required tool sequences; "
        "prompt and few-shot options rely on probabilistic LLM compliance—insufficient when "
        "misidentification causes financial harm. Routing classifiers change tool availability, "
        "not ordering, so they do not fix skipped verification."
    ),
    2: (
        "Tool descriptions are the primary LLM selection signal; minimal descriptions cause "
        "confusion between similar tools. Few-shot adds tokens without fixing descriptions; "
        "routing layers are over-engineered for a first step; consolidation is valid but "
        "higher effort than expanding descriptions."
    ),
    3: (
        "Explicit escalation criteria with few-shot examples fix unclear decision boundaries—the "
        "proportionate first fix. LLM self-reported confidence is poorly calibrated on hard cases; "
        "a separate classifier is over-engineered before prompt tuning; sentiment does not "
        "measure case complexity."
    ),
    4: (
        "Project slash commands live in .claude/commands/ and are version-controlled for the team. "
        "~/.claude/commands/ is personal; CLAUDE.md holds instructions not command definitions; "
        ".claude/config.json is not the Claude Code command mechanism."
    ),
    5: (
        "Plan mode fits large architectural work with exploration before edits. Direct execution "
        "risks rework when dependencies are unknown; upfront rigid instructions skip necessary "
        "discovery; switching only if complexity emerges ignores stated large-scale scope."
    ),
    6: (
        ".claude/rules/ with glob patterns apply conventions by file path—including tests spread "
        "across directories. Root CLAUDE.md relies on inference; skills need invocation; "
        "per-directory CLAUDE.md cannot cover scattered test files."
    ),
    7: (
        "Coordinator logs show decomposition into only visual-arts subtasks—subagents succeeded "
        "within narrow assignments. Downstream agents are not the root cause; synthesis, search, "
        "and analysis worked within assigned scope."
    ),
    8: (
        "Structured error context enables coordinator recovery (retry, alternate query, partial "
        "results). Generic retry status hides context; marking failure as success blocks recovery; "
        "terminating the whole workflow is unnecessary when partial progress exists."
    ),
    9: (
        "Scoped verify_fact on synthesis covers the common simple fact-check case while complex "
        "work stays with search via coordinator—least privilege. End-of-pass batching creates "
        "blocking dependencies; giving synthesis all search tools over-provisions; speculative "
        "caching cannot predict verification needs."
    ),
    10: (
        "-p (--print) is the documented non-interactive CI mode: process, output, exit. "
        "CLAUDE_HEADLESS, --batch, and stdin tricks are not the correct Claude Code approach."
    ),
    11: (
        "Message Batches save cost but lack latency SLA—fine for overnight reports, unsuitable "
        "for blocking pre-merge checks. Polling batches for merge gates is unacceptable; "
        "custom_id correlates batch results; timeout fallback adds complexity vs matching API "
        "to workflow latency needs."
    ),
    12: (
        "Split reviews into per-file passes plus a cross-file integration pass—fixes attention "
        "dilution across many files. Splitting PRs burdens developers; larger context does not "
        "fix attention quality; consensus across passes would suppress intermittently caught bugs."
    ),
}
