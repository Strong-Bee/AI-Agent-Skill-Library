# Claude Code Adapter

Version: 1.0.0
Status: Draft
Last Updated: 2026-11-08

---

## Overview

This adapter enables skills to run on **Claude Code** (CLI) and **Claude Desktop**.

---

## Discovery & Installation

### Skill Discovery

Claude Code discovers skills in:
- `~/.claude/skills/` (user-level)
- `.claude/skills/` (project-level)
- Any directory added via `/skill` command

Skills are identified by directories containing `SKILL.md`.

### Installation

```bash
# User-level (available everywhere)
ln -s /path/to/ai-agent-skill-library/categories/* ~/.claude/skills/

# Project-level (specific to project)
mkdir -p .claude/skills
ln -s /path/to/ai-agent-skill-library/categories/* .claude/skills/

# Or copy
cp -r /path/to/ai-agent-skill-library/categories/* ~/.claude/skills/
```

### Verification

```bash
# List installed skills
claude /skill list

# Or in chat
> /skill list
```

---

## Execution Model

### Invocation Methods

1. **Slash Command** - `/skill-name` (if skill registers command)
2. **Agent Delegation** - Main agent delegates to skill agent
3. **Direct Reference** - "Use the ai-agent-developer skill to..."

### Parameter Passing

Skills receive context through:
- Conversation history
- Explicit parameters in request
- File references (`@filepath`)
- MCP server resources

### Tool Bridge

Skills use native Claude Code tools:
- `Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`
- `Task` (subagents)
- `WebFetch`, `WebSearch`
- MCP tools (when servers configured)

### Permission Model

Respects Claude Code permission modes:
- `default` - Ask for each tool
- `acceptEdits` - Auto-accept edits
- `plan` - Plan mode
- `auto` - Auto-approve safe tools
- `bypassPermissions` - No prompts

---

## MCP Integration

### Skill MCP Servers

Skills can include MCP servers in `config/mcp/`:

```
skill-name/
├── config/
│   └── mcp/
│       ├── server-name/
│       │   ├── package.json
│       │   └── index.js
│       └── mcp.json (server registry)
```

### Registration

MCP servers auto-discovered from `.mcp.json` in skill directory or user config.

---

## Configuration Mapping

### Skill Config Files

Located in `skill-name/config/` - read directly by skill.

### Environment Variables

Standard naming: `SKILL_{CATEGORY}_{SKILL}_{VAR}`

Example: `SKILL_AI_AUTOMATION_AI_AGENT_DEVELOPER_API_KEY`

### User Settings

Claude Code settings in `~/.claude/settings.json` or project `.claude/settings.json`.

---

## Platform-Specific Features

### Subagents

Skills can define specialized subagents in `.claude/agents/`.

### Hooks

Event-triggered automation in `.claude/hooks/`.

### Slash Commands

Custom commands in `.claude/commands/`.

---

## Limitations

| Limitation | Workaround |
|------------|------------|
| No native skill marketplace | Manual installation |
| Permission prompts per tool | Use `acceptEdits` or `auto` mode |
| No built-in skill versioning | Use git submodules or manual updates |
| MCP servers require restart | Document in skill README |

---

## Testing

```bash
# Test skill loads
claude /skill list | grep skill-name

# Test basic invocation
claude -p "Use the skill-name skill to do X"
```

---

## Configuration Files

### `.mcp.json` (Skill MCP Registry)

```json
{
  "mcpServers": {
    "skill-server": {
      "command": "node",
      "args": ["config/mcp/skill-server/index.js"],
      "env": {}
    }
  }
}
```

### `skill-manifest.json` (Optional)

```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "commands": ["skill-command"],
  "agents": ["subagent-name"],
  "mcpServers": ["skill-server"]
}
```

---

## Development

### Local Development

```bash
# Link for development
ln -s /path/to/skill ~/.claude/skills/category/skill-name

# Test changes immediately
claude -p "Test skill"
```

### Publishing

Package as git repository or release archive.

---

*See COMPATIBILITY_STANDARD.md for full compatibility matrix.*