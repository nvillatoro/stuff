---
name: skill-provenance
description: Require model provenance metadata when creating or materially revising Codex skills or their supporting prompt files. Use whenever writing, generating, updating, or reviewing a skill.
metadata:
  generated-by: gpt-5.6-luna
---

# Skill Provenance

When creating or materially revising a skill or supporting prompt file, record
the exact model identifier that produced the change in the file's YAML metadata:

```yaml
metadata:
  generated-by: gpt-5.6-luna
```

Use the exact active model identifier from the session context. Do not infer,
normalize, or replace it with a family name. Preserve existing markers. If
multiple models contributed, record all known identifiers without guessing
section-level attribution.

## Personal skill storage

For personal skills, create the skill in the tracked repository first:

```text
/Users/NVILLATO/Dev/git/stuff/.codex/skills/<skill-name>
```

Keep `.system` out of the repository. After creating a skill, expose it to
Codex with a per-skill symlink:

```bash
ln -s \
  /Users/NVILLATO/Dev/git/stuff/.codex/skills/<skill-name> \
  /Users/NVILLATO/.codex/skills/<skill-name>
```

Do not replace the entire `~/.codex/skills` directory; leave `.system`
managed by Codex.
