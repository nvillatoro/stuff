---
name: prompt-import-analysis
description: Use when analyzing, reviewing, linting, rewriting, or importing AI prompt files, especially Markdown prompt files that include other local prompt files through Markdown links. Resolves the prompt import graph first, then checks contradictions, ambiguity, persona consistency, cognitive load, semantic coverage, and cross-file composition conflicts while keeping outputs token-efficient.
---

# Prompt Import Analysis

Use this skill for AI prompt files stored as local files, especially `.md` prompts that compose other prompts with Markdown links.

## Goals

Check for:
- contradiction detection
- semantic ambiguity
- persona consistency
- cognitive load
- semantic coverage gaps
- composition conflicts across imported prompt files

Generated artifacts must be token-efficient:
- do not restate full prompt files unless asked
- quote only the minimum needed to support a finding
- prefer short rewrites over verbose rewrites
- keep final reports compact and directly actionable

## Workflow

1. Identify the entry prompt file and whether the task is:
- analysis only
- rewrite only
- analysis plus rewrite
- import/composition investigation

2. Resolve local Markdown-link imports before deep analysis.
- Run `scripts/resolve_prompt_imports.py <entry-file>`.
- Treat local relative Markdown links as imports.
- Ignore external URLs and same-file anchor links.
- If an imported file is missing, report it as a coverage/composition blocker.

3. Read only the files needed for the active prompt graph.
- Start with the entry file.
- Then load directly imported files.
- Expand deeper only when imports exist.
- Avoid unrelated files to preserve context budget.

4. Analyze in this order:
- contradictions within a file
- contradictions introduced by imported files
- ambiguous wording and underspecified behavior
- persona and tone drift across files
- excessive nesting, branching, or exception handling that raises cognitive load
- missing intent handling, missing edge cases, and missing failure behavior

5. If rewrites are requested or clearly useful, produce the smallest rewrite that fixes the issue.
- Preserve user intent.
- Remove redundant instructions.
- Collapse overlapping rules.
- Prefer one explicit rule over several loosely overlapping rules.

## Heuristics

### Contradiction detection

Look for:
- mutually exclusive requirements
- conflicting output-format rules
- instructions that both require and forbid the same behavior
- priority inversions between base and imported prompts

### Semantic ambiguity

Look for:
- vague qualifiers like `appropriate`, `reasonable`, `careful`, `brief`, `high quality`
- undefined scope terms like `latest`, `safe`, `sensitive`, `complex`
- unclear escalation thresholds

When useful, rewrite by:
- replacing vague adjectives with observable criteria
- naming explicit decision boundaries
- converting soft preferences into ordered rules

### Persona consistency

Look for:
- conflicting tone instructions
- incompatible role expectations
- drift between “be concise” and “be exhaustive” style layers
- imports that silently override the stated persona

### Cognitive load

Warn when prompts have:
- too many nested conditions
- long priority chains
- repeated exceptions to exceptions
- duplicated policy text across imports

Prefer:
- ordered rules
- tighter scope
- merged duplicate instructions

### Semantic coverage

Look for missing handling for:
- unsupported requests
- missing inputs
- ambiguous user goals
- external dependency failures
- import resolution failures

### Composition conflict analysis

Compare the entry prompt with imported files for:
- contradictory behavior
- redundant constraints
- mismatched response formats
- persona or tone overrides
- duplicate instructions that inflate tokens without adding control

## Output shape

Default to a compact report with:
- `Findings`: short bullets ordered by severity
- `Rewrite suggestions`: only for real issues
- `Import graph`: only when imports matter

Use this severity model:
- `high`: likely to cause incorrect or unstable behavior
- `medium`: likely to cause drift, ambiguity, or excess tokens
- `low`: cleanup or compression opportunity

If no material issues are found, say so explicitly and note any residual uncertainty from missing imports or vague requirements.

## Bundled resources

- `AGENTS.md`: more specific operating guidance for this skill
- `scripts/resolve_prompt_imports.py`: deterministic import-graph resolver for local Markdown prompt files

Read `AGENTS.md` in this folder when you need the detailed analysis checklist or response template.
