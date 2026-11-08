# Configuration

This directory contains configuration files for the skill.

## Files

| File | Purpose | Format |
|------|---------|--------|
| `settings.yaml` | Main skill configuration | YAML |
| `mcp.json` | MCP server registry (Claude Code) | JSON |
| `prompts/` | Prompt templates | Markdown/Text |

## Configuration Options

Document each configuration option:

### `settings.yaml`

```yaml
# Example configuration
option1: "description and default"
option2: "description and default"
```

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `SKILL_CATEGORY_SKILL_OPTION` | Description | No | `default` |

## Platform-Specific Config

- **Claude Code**: Reads `settings.yaml` directly; MCP servers from `mcp.json`
- **OpenCode**: Merged into `opencode.json` via manifest generator
- **Cursor**: Via `claude.skills` settings
- **Generic**: Manual setup

## Validation

Run validation:
```bash
# Validate YAML syntax
yamllint settings.yaml

# Validate against schema (when available)
python -m jsonschema -i settings.yaml ../../core/metadata-schema/config.schema.json
```