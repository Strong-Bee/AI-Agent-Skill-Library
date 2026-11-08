# OpenCode Adapter

Version: 1.0.0
Status: Planned
Last Updated: 2026-11-08

---

## Overview

This adapter enables skills to run on **OpenCode** (open-source AI coding agent).

---

## Discovery & Installation

### Skill Discovery

OpenCode discovers skills via `opencode.json` configuration:

```json
{
  "skills": {
    "paths": [
      "./skills",
      "~/.opencode/skills",
      "/path/to/ai-agent-skill-library/categories"
    ]
  }
}
```

Skills identified by directories containing `skill.yaml` manifest (generated from SKILL.md).

### Installation

```bash
# Generate skill manifest from SKILL.md
opencode skill generate /path/to/skill

# Add to opencode.json
# Or symlink to configured skills directory
ln -s /path/to/ai-agent-skill-library/categories/* ~/.opencode/skills/
```

### Verification

```bash
opencode skill list
```

---

## Execution Model

### Invocation

```bash
opencode run skill-name --input "task description"
```

### Parameter Passing

JSON input via stdin or `--input` flag.

### Tool Bridge

OpenCode tool definitions map to skill tools.

### Permission Model

OpenCode tool permissions system.

---

## Configuration Mapping

### Skill Manifest (`skill.yaml`)

Generated from SKILL.md frontmatter:

```yaml
name: skill-name
version: "1.0.0"
description: "Skill description"
category: "ai-automation"
tools:
  - shell
  - read
  - write
config:
  # Merged from skill config/
```

### Environment Variables

`OPENCODE_SKILL_{SKILL}_{VAR}`

---

## Limitations

| Limitation | Status |
|------------|--------|
| No MCP support | Planned |
| Limited streaming | Partial |
| Manifest generation required | Tool needed |

---

## Development

### Manifest Generator

Tool to convert SKILL.md → skill.yaml (to be built in `tools/generators/`).

---

*See COMPATIBILITY_STANDARD.md for full compatibility matrix.*