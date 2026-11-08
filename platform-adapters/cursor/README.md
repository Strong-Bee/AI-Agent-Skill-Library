# Cursor Adapter

Version: 1.0.0
Status: Planned
Last Updated: 2026-11-08

---

## Overview

This adapter enables skills to run in **Cursor** (AI-powered code editor).

---

## Discovery & Installation

### Skill Discovery

Via Cursor settings:

```json
{
  "claude.skillsPath": [
    "./skills",
    "~/.cursor/skills",
    "/path/to/ai-agent-skill-library/categories"
  ]
}
```

Skills identified by directories containing `SKILL.md`.

### Installation

```bash
# Symlink to configured directory
ln -s /path/to/ai-agent-skill-library/categories/* ~/.cursor/skills/
```

### Verification

Open Cursor → Cmd/Ctrl+K → Type skill name.

---

## Execution Model

### Invocation

- Cmd/Ctrl+K → Type `@skill-name` or select from palette
- Chat: "Use @skill-name to..."

### Parameter Passing

Chat context + explicit parameters.

### Tool Bridge

Cursor built-in tools (file ops, terminal, search, etc.).

### Permission Model

Cursor privacy/organizational settings.

---

## Configuration Mapping

### Cursor Settings

```json
{
  "claude.skills": {
    "skill-name": {
      "config": { /* from skill config/ */ }
    }
  }
}
```

### Environment Variables

`CURSOR_SKILL_{SKILL}_{VAR}`

---

## Limitations

| Limitation | Status |
|------------|--------|
| No MCP support | Not supported |
| Skill activation via chat only | Native |
| Limited background execution | Partial |

---

*See COMPATIBILITY_STANDARD.md for full compatibility matrix.*