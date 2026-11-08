# GitHub Copilot Adapter

Version: 1.0.0
Status: Planned
Last Updated: 2026-11-08

---

## Overview

This adapter enables skills to run in **GitHub Copilot** (VS Code extension / GitHub.com).

---

## Discovery & Installation

### Skill Discovery

Via VS Code extension marketplace or manual installation.

Skills packaged as VS Code extensions with skill bundle.

### Installation

```bash
# Package skill as VS Code extension
vsce package skill-name/

# Install
code --install-extension skill-name.vsix
```

Or install from marketplace.

### Verification

Copilot Chat: `@skill-name` appears in suggestions.

---

## Execution Model

### Invocation

Copilot Chat: `@skill-name your request`

### Parameter Passing

Chat context.

### Tool Bridge

VS Code API + Copilot tools.

### Permission Model

Organization/repository permissions.

---

## Configuration Mapping

### package.json

```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "contributes": {
    "copilotSkills": [{
      "id": "skill-name",
      "name": "Skill Name",
      "description": "Skill description"
    }]
  }
}
```

### VS Code Settings

```json
{
  "copilot.skills": {
    "skill-name": { "config": {} }
  }
}
```

---

## Limitations

| Limitation | Status |
|------------|--------|
| Extension packaging required | Extra step |
| No local file system access | VS Code workspace only |
| Org policy restrictions | May block |

---

*See COMPATIBILITY_STANDARD.md for full compatibility matrix.*