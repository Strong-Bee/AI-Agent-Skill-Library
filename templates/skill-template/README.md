# Skill Name

> One-sentence tagline describing the skill's value.

[![Maturity](https://img.shields.io/badge/Maturity-Alpha-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

2-3 paragraphs explaining:
- The professional role this skill embodies
- Key capabilities it provides
- Typical use cases and scenarios

## Target Audience

- **Primary**: [e.g., AI Agent Developers]
- **Secondary**: [e.g., Automation Engineers, Technical Leads]

## Prerequisites

- Required tools/accounts: [e.g., Python 3.10+, Git, API keys]
- Required knowledge: [e.g., Basic Python, REST APIs]
- Platform requirements: [e.g., Claude Code ≥ 1.0.0]

## Installation

### Claude Code / Claude Desktop
```bash
# User-level (available everywhere)
ln -s /path/to/skill ~/.claude/skills/category/skill-name

# Project-level
mkdir -p .claude/skills
ln -s /path/to/skill .claude/skills/category/skill-name
```

### OpenCode
```bash
# Add to opencode.json skills.paths
# Or symlink to ~/.opencode/skills/
ln -s /path/to/skill ~/.opencode/skills/category/skill-name
```

### Generic (Any Markdown-compatible Agent)
```bash
# Copy to your agent's skill/knowledge directory
cp -r /path/to/skill /your/agent/skills/
```

## Quick Start

```markdown
# Minimal working example
# Replace with actual skill invocation
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Capability 1 | What it does and when to use it |
| Capability 2 | What it does and when to use it |
| Capability 3 | What it does and when to use it |

## Workflow Overview

This skill follows the standard 10-step workflow:

1. **Request Analysis** - Understand intent and scope
2. **Requirement Clarification** - Resolve ambiguities
3. **Context Gathering** - Collect relevant information
4. **Research** - Find best practices and alternatives
5. **Planning** - Create detailed execution plan
6. **Task Execution** - Implement with checkpoints
7. **Validation** - Verify against requirements
8. **Quality Review** - Check professional standards
9. **Error Correction** - Fix issues and re-validate
10. **Final Delivery** - Package and document outputs

## Configuration

Key configuration options (see `config/` for details):

| Option | Description | Default |
|--------|-------------|---------|
| `option1` | Description | `value` |
| `option2` | Description | `value` |

## Examples

See `examples/` directory for complete working examples:
- `examples/basic/` - Minimal example
- `examples/advanced/` - Full-featured example

## Limitations

- What this skill does NOT do
- Known constraints
- Platform-specific limitations

## Related Skills

- [Complementary Skill](../complementary-skill/README.md) - How it complements
- [Alternative Skill](../alternative-skill/README.md) - When to use instead

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)