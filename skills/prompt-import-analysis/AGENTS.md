# prompt-import-analysis

Purpose: analyze AI prompt files and prompt compositions with minimal context waste and minimal output tokens.

## Scope

Use this skill when the target is one or more local prompt files, usually Markdown, and especially when one prompt imports others through Markdown links.

This skill covers:
- contradiction detection
- ambiguity analysis
- persona consistency
- cognitive load assessment
- semantic coverage gaps
- composition conflict analysis across imports

## Import rules

Treat these as imports:
- relative Markdown links such as `[policy](./policy.md)`
- parent-directory Markdown links such as `[shared](../shared/base.md)`

Do not treat these as imports:
- `http://` or `https://` links
- same-file anchors like `#section`
- image links

If a link target cannot be resolved locally, report:
- the importing file
- the unresolved link text or target
- the impact on analysis confidence

## Analysis checklist

1. Resolve the import graph first.
2. Identify the effective instruction stack:
- entry prompt rules
- imported rules
- repeated rules
- silent overrides
3. Look for direct conflicts:
- required vs forbidden behavior
- concise vs exhaustive response requirements
- strict format vs flexible format instructions
4. Look for behavioral drift:
- persona changes
- tone shifts
- escalation mismatches
- inconsistent refusal or safety behavior
5. Measure complexity:
- nested conditions
- long exception chains
- repeated caveats
- duplicate imports or repeated policy blocks
6. Check coverage:
- unsupported or out-of-scope requests
- missing input cases
- failure paths
- missing precedence rules

## Response template

Prefer this compact structure:

`Findings`
- `[severity] file-or-composition: issue`

`Rewrite suggestions`
- only include when the rewrite is shorter and clearer than the original behavior

`Import graph`
- include only when it clarifies cross-file findings

## Token discipline

Keep artifacts usable but small:
- summarize instead of paraphrasing entire prompts
- quote only a few words when evidence is needed
- do not emit merged prompt files unless the user asks
- prefer one rewrite block per issue cluster instead of many micro-rewrites
