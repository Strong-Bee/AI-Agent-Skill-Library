# Documentation Standard

Version: 1.0.0
Status: Draft
Last Updated: 2026-11-08

---

## Overview

This standard defines the documentation requirements, structure, and style for all skills in the AI Agent Skill Library.

---

## 1. Required Documentation Files

Every skill **must** include these files:

| File | Purpose | Required |
|------|---------|----------|
| `SKILL.md` | Machine-readable specification (primary) | ✅ Yes |
| `README.md` | Human-readable overview and usage | ✅ Yes |
| `CHANGELOG.md` | Version history | ✅ Yes |

### Optional but Recommended

| File | Purpose |
|------|---------|
| `docs/ARCHITECTURE.md` | Architecture decisions |
| `docs/USAGE.md` | Detailed usage guide |
| `docs/TROUBLESHOOTING.md` | Common issues and solutions |
| `docs/EXAMPLES.md` | Extended examples |
| `docs/API.md` | API reference (if applicable) |

---

## 2. SKILL.md Structure

The `SKILL.md` is the **single source of truth**. It must contain all specification sections in YAML frontmatter + Markdown format.

### Format

```markdown
---
# YAML frontmatter with all metadata per schema
identity:
  name: "..."
  id: "..."
  # ... all required fields
---

# Human-readable sections (optional but recommended)

## Overview
Brief description of what this skill does.

## Quick Start
Minimal example to get running.

## Configuration
Configuration options and examples.

## Workflow
How the 10-step workflow applies to this skill.

## Knowledge Base
Key concepts, methodologies, references.

## Tools & Integrations
Tools used, setup required.

## Output Examples
Sample deliverables.

## Troubleshooting
Common issues.

## Contributing
Skill-specific contribution notes.
```

### Frontmatter Requirements

- **Must validate** against `core/metadata-schema/skill-metadata.schema.json`
- **All required fields** present
- **No placeholder values** (e.g., "TODO", "TBD", "example.com")
- **Version** follows Semantic Versioning
- **Category** matches directory structure

---

## 3. README.md Structure

Human-friendly overview for skill users.

### Template

```markdown
# Skill Name

> One-sentence tagline describing the skill's value.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

2-3 paragraphs explaining:
- The professional role this skill embodies
- Key capabilities it provides
- Typical use cases

## Target Audience

- **Primary**: [e.g., AI Agent Developers]
- **Secondary**: [e.g., Automation Engineers]

## Prerequisites

- Required tools/accounts
- Required knowledge
- Platform requirements

## Installation

```bash
# Platform-specific installation
```

## Quick Start

```markdown
# Minimal working example
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Capability 1 | What it does |
| Capability 2 | What it does |

## Workflow Overview

Brief description of the 10-step workflow as applied.

## Configuration

Key configuration options.

## Examples

Links to `examples/` directory.

## Limitations

What this skill does NOT do.

## Related Skills

Links to complementary skills.

## License

MIT - see LICENSE file.
```

---

## 4. CHANGELOG.md Structure

Follows [Keep a Changelog](https://keepachangelog.com/).

### Template

```markdown
# Changelog

All notable changes to this skill.

## [Unreleased]

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security improvements

---

## [1.0.0] - 2026-11-08

### Added
- Initial release
- Core competencies: X, Y, Z
- Workflow implementation
- Knowledge base
- Examples
```

### Version Format

- **MAJOR**: Breaking changes to workflow, outputs, or metadata schema
- **MINOR**: New capabilities, backward-compatible additions
- **PATCH**: Bug fixes, documentation updates, minor improvements

---

## 5. Writing Style Guide

### Language

- **English** (primary), other languages as translations
- **Professional, clear, concise**
- **Active voice** preferred
- **Present tense** for descriptions
- **Second person** ("you") for instructions

### Formatting

| Element | Standard |
|---------|----------|
| Headings | ATX style (`#`, `##`, `###`) |
| Code blocks | Fenced with language tag |
| Inline code | Backticks |
| Lists | Dashes for unordered, numbers for ordered |
| Tables | GitHub-flavored markdown |
| Links | Relative for internal, absolute for external |
| Images | Relative paths, alt text required |

### Terminology

- Use terms from `shared-knowledge/terminology/`
- Define acronyms on first use: "Large Language Model (LLM)"
- Consistent naming for concepts across skills
- Avoid jargon without definition

### Structure Principles

1. **Progressive disclosure** - Summary first, details later
2. **Scannable** - Headings, bullets, tables
3. **Actionable** - Examples, commands, steps
4. **Complete** - No "TODO" or "coming soon" in released docs

---

## 6. Documentation in Skill Directories

### config/

```markdown
# config/README.md
Documents each configuration file:
- Purpose
- Format/schema
- Example
- Environment variable mapping
```

### knowledge/

```markdown
# knowledge/README.md
Index of knowledge documents:
- concepts.md - Fundamental concepts
- methodologies.md - Professional methodologies
- standards.md - Industry standards
- references.md - Curated reference list
```

### workflows/

```markdown
# workflows/README.md
Documents each workflow:
- workflow-name.md - Steps, inputs, outputs, decision points
- diagrams/ - Mermaid/PlantUML diagrams
```

### tools/

```markdown
# tools/README.md
Documents each tool integration:
- tool-name.md - Setup, usage, fallback, troubleshooting
```

### templates/

```markdown
# templates/README.md
Documents each template:
- template-name.md - Purpose, variables, example output
```

### quality/

```markdown
# quality/README.md
- EVALUATION.md - Self-evaluation results
- DEBT.md - Known quality debt
- WAIVERS.md - Approved waivers
```

### examples/

```markdown
# examples/README.md
Index of examples:
- example-name/ - Self-contained example with input/expected output
```

### tests/

```markdown
# tests/README.md
- Test strategy
- How to run tests
- Coverage targets
- Fixture descriptions
```

---

## 7. Platform-Specific Documentation

### Claude Code

```markdown
# docs/CLAUDE_CODE.md
- Installation via symlink/copy
- Permission requirements
- MCP server configuration
- Usage examples
- Known limitations
```

### OpenCode

```markdown
# docs/OPENCODE.md
- opencode.json configuration
- Skill manifest format
- Tool permissions
- Usage examples
```

### Cursor

```markdown
# docs/CURSOR.md
- Settings configuration
- Skill activation
- Context handling
- Usage examples
```

### GitHub Copilot

```markdown
# docs/GITHUB_COPILOT.md
- Extension setup
- Skill packaging
- Workspace integration
- Usage examples
```

### Generic

```markdown
# docs/GENERIC.md
- Markdown-based usage
- Manual workflow execution
- Tool requirements
- Integration patterns
```

---

## 8. Documentation Quality Checklist

Before release, verify:

- [ ] SKILL.md frontmatter validates against schema
- [ ] README.md follows template
- [ ] CHANGELOG.md follows format
- [ ] All directory READMEs exist
- [ ] No placeholder content (TODO, TBD, example.com)
- [ ] All links work (internal and external)
- [ ] Code examples are syntactically correct
- [ ] Screenshots/diagrams are current
- [ ] Version numbers consistent across files
- [ ] Terminology consistent with shared glossary
- [ ] Platform-specific docs complete for supported platforms
- [ ] Examples are runnable or clearly illustrative
- [ ] Troubleshooting covers top 5 issues
- [ ] License headers present

---

## 9. Documentation Tools

### Validation

```bash
# Validate SKILL.md metadata
python -m jsonschema -i SKILL.md core/metadata-schema/skill-metadata.schema.json

# Lint markdown
markdownlint **/*.md

# Check links
lychee **/*.md

# Spell check
cspell **/*.md
```

### Generation

```bash
# Generate catalog entry from SKILL.md
python tools/generators/generate-catalog.py

# Generate platform-specific configs
python tools/generators/generate-platform-configs.py
```

---

## 10. Documentation Maintenance

- **Update with every skill change**
- **Review quarterly** for accuracy
- **Version lock** external references
- **Archive** superseded documentation
- **Translate** for priority languages

---

*Consistent documentation enables discovery, adoption, and trust.*