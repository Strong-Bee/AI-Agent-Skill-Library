# Tool Integrations

This directory contains tool integration code and documentation.

## Structure

| File/Directory | Purpose |
|----------------|---------|
| `tool-name/` | Platform-specific implementation for each tool |
| `shared/` | Shared utilities across platforms |
| `schemas/` | Input/output schemas for tool calls |

## Platform-Specific Implementations

Each tool may have different implementations per platform:

```
tool-name/
├── claude/          # Claude Code implementation (Bash, MCP, etc.)
├── opencode/        # OpenCode tool definition
├── cursor/          # Cursor integration
├── generic/         # Generic/documentation only
└── README.md        # Tool-specific documentation
```

## Tool Documentation

Each tool integration must document:
- Setup requirements
- Configuration options
- Usage examples
- Error handling
- Fallback procedures
- Rate limits

## Adding a New Tool

1. Create platform-specific implementations
2. Define input/output schemas
3. Add to `supported_tools` in SKILL.md
4. Document fallback procedures
5. Add tests in `../tests/integration/`