# Generic Markdown Adapter

Version: 1.0.0
Status: Baseline
Last Updated: 2026-11-08

---

## Overview

This adapter enables skills to run on **any Markdown-compatible AI agent system** that can read and follow written instructions.

---

## Discovery & Installation

### Skill Discovery

Manual - user copies skill directory to their agent's knowledge/skill directory.

### Installation

```bash
# Copy to your agent's skill directory
cp -r /path/to/ai-agent-skill-library/categories/ai-automation/ai-agent-developer /your/agent/skills/
```

### Verification

Manual - check that skill directory exists and contains SKILL.md.

---

## Execution Model

### Invocation

User manually follows the workflow in SKILL.md:

1. Read SKILL.md for role, competencies, workflow
2. Provide context to agent
3. Agent executes workflow steps
4. User validates outputs

### Parameter Passing

User provides context in conversation.

### Tool Bridge

User's available tools (shell, editor, browser, etc.).

### Permission Model

User-controlled.

---

## Configuration Mapping

### Manual Configuration

User reads `config/` files and sets up manually.

### Environment Variables

User sets in their environment.

---

## Universal Compatibility

This adapter works with:
- Any LLM chat interface (ChatGPT, Claude.ai, Gemini, etc.)
- Local LLM runners (Ollama, LM Studio, etc.)
- Custom agent frameworks
- Documentation-only reference

---

## Limitations

| Limitation | Impact |
|------------|--------|
| No automation | Manual workflow execution |
| No tool integration | User must operate tools |
| No validation | User verifies outputs |
| No version management | Manual updates |

---

## Usage Guide

### For Users

1. Copy skill to your knowledge base
2. Read SKILL.md to understand capabilities
3. Follow the 10-step workflow manually
4. Use knowledge/ templates/ examples/ as reference

### For Agent Developers

1. Parse SKILL.md frontmatter for metadata
2. Extract workflow steps for automation
3. Map tools to your platform's capabilities
4. Implement platform-specific adapter

---

## Minimum Viable Skill (for Generic)

A skill works generically if it has:
- ✅ SKILL.md with complete specification
- ✅ README.md with usage guide
- ✅ knowledge/ with domain knowledge
- ✅ workflows/ with step-by-step procedures
- ✅ templates/ with reusable artifacts
- ✅ examples/ with input/output samples

---

*See COMPATIBILITY_STANDARD.md for full compatibility matrix.*