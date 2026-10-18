---
name: pr-guidelines
description: Guide the preparation and review of pull requests, including repository conventions, ownership, ticket references, semantic commits, and concise descriptions.
metadata:
  generated-by: gpt-5
  scope: capability
---

# PR Guidelines

Use this skill when creating, preparing, or reviewing a pull request. The goal
is a complete, reviewable PR with enough context to understand the change
without turning the description into an essay.

## Operating boundaries

- Follow the repository's PR template when one exists. Inspect it before
  drafting or editing the PR description.
- Treat repository-specific conventions as authoritative. Do not invent a
  ticket format, reviewer list, label scheme, or GitHub identity.
- If the requested capability or scope is unclear, ask before proceeding.

## Ownership and ticket reference

- Assign the PR to its creator when the creator's GitHub identity is known
  from reliable context.
- Never guess or assume a GitHub username or ID. Ask the user when it is not
  available or when multiple identities are plausible.
- Reference the related PR ticket when one is available.
- If no ticket was provided, prompt for one. If the user confirms that none
  exists, offer to create one before proceeding when that is within scope.

## Commit guidance

- Use semantic commit messages appropriate to the repository's conventions.
- Keep each commit focused on a coherent change and use a capability-oriented
  scope when the repository's semantic-commit format supports scopes.
- If the correct scope is uncertain, ask rather than choosing one silently.

## PR description template

Use the repository's template and preserve any required sections. At minimum,
the description should make these points clear:

### What

What changed, stated concretely and briefly.

### Why

The problem, user need, or intended outcome that motivated the change.

### How

The implementation approach, including relevant design or behavioral details.

Keep the description informative but concise: include the context a reviewer
needs to evaluate the change, and omit implementation narration that does not
help review.

## Pre-flight checklist

Before delivering or submitting the PR, verify:

- [ ] The repository PR template was observed and required sections are
      complete.
- [ ] The PR is assigned to the verified creator, or the user was asked for
      the creator's GitHub identity.
- [ ] A related ticket is referenced, or the user was prompted and offered
      ticket creation where appropriate.
- [ ] Commit messages use semantic conventions with a capability-oriented
      scope, or scope uncertainty was surfaced.
- [ ] The description clearly covers What, Why, and How and remains concise.

If any check cannot be verified, stop and ask for the missing information
rather than guessing.
