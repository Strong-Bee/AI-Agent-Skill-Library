# Contributing to AI Agent Skill Library

Thank you for your interest in contributing! This library aims to provide high-quality, professional AI agent skills. Please follow these guidelines to ensure consistency and quality.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Adding a New Skill](#adding-a-new-skill)
- [Improving Existing Skills](#improving-existing-skills)
- [Skill Quality Standards](#skill-quality-standards)
- [Review Process](#review-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/skill-name`
3. Make your changes
4. Run validation: `./scripts/validate.sh` (when available)
5. Submit a pull request

## Adding a New Skill

### 1. Choose the Right Category

Select from the 12 professional categories:
- `ai-automation/`
- `software-development/`
- `digital-marketing/`
- `design-creative/`
- `business-management/`
- `data-analytics/`
- `administration/`
- `cybersecurity-it/`
- `finance-accounting/`
- `ecommerce-sales/`
- `writing-communication/`
- `education-research/`

### 2. Use the Skill Template

Copy the template structure from `templates/skill-template/`:

```bash
cp -r templates/skill-template categories/your-category/your-skill-name
```

### 3. Fill in All Required Components

Every skill **must** include:

#### Required Files
- `SKILL.md` - Main specification (see [Skill Specification](#skill-specification))
- `README.md` - Human-readable overview
- `CHANGELOG.md` - Version history

#### Required Directories (create even if empty initially)
- `config/` - Configuration files
- `knowledge/` - Domain knowledge base
- `workflows/` - Workflow definitions
- `tools/` - Tool integrations & scripts
- `templates/` - Reusable templates
- `quality/` - Quality assurance & evaluation
- `examples/` - Usage examples
- `tests/` - Validation tests

### 4. Skill Specification (SKILL.md)

Follow the [Universal Skill Specification](core/skill-standard/UNIVERSAL_SKILL_SPEC.md) with these sections:

1. **Identity** - Name, ID, version, description, role, category, target users, capabilities
2. **Role Definition** - Professional identity, expertise, responsibilities, scope, limitations, behavior
3. **Core Competencies** - Specific professional capabilities
4. **Knowledge Base** - Concepts, terminology, methodologies, standards, best practices, mistakes, references
5. **Workflow** - Request analysis → Clarification → Context gathering → Research → Planning → Execution → Validation → Quality review → Error correction → Delivery
6. **Tools & Integrations** - Supported/required/optional tools, APIs, MCP, prerequisites, auth, fallbacks
7. **Output Standards** - Deliverables, structure, documentation, quality, acceptance criteria

### 5. Validate Your Skill

Before submitting:
- [ ] All required files exist
- [ ] SKILL.md follows the specification
- [ ] Metadata is valid (run metadata validator when available)
- [ ] Examples are executable or clearly illustrative
- [ ] Tests pass (when implemented)
- [ ] No placeholder content remains
- [ ] Documentation is clear and accurate

## Improving Existing Skills

### Types of Improvements
- **Bug fixes** - Correct errors in workflows, knowledge, or tools
- **Enhancements** - Add capabilities, improve workflows, expand knowledge
- **Documentation** - Improve clarity, add examples, fix typos
- **Platform compatibility** - Add adapters, fix integration issues
- **Quality** - Add tests, improve evaluation criteria

### Process
1. Check existing issues or create a new one
2. Discuss significant changes in an issue first
3. Make focused, atomic changes
4. Update CHANGELOG.md
5. Run validation

## Skill Quality Standards

### Minimum Release Requirements
- **Quality Score**: ≥ 90/100
- **No critical defects** unresolved
- **Required documentation** complete
- **Valid metadata** per schema
- **Complete workflow** (all 10 steps)
- **Executable examples** or clear illustrations
- **Passing tests** (when framework available)
- **Security review** passed
- **Compatibility limitations** documented

### Evaluation Criteria (Weighted)

| Criteria | Weight | Description |
|----------|--------|-------------|
| Accuracy | 20% | Correct information, valid references |
| Professional Expertise | 20% | Depth and relevance to profession |
| Workflow Completeness | 15% | All 10 steps implemented |
| Output Quality | 15% | Deliverables meet professional standards |
| Best Practices | 10% | Follows industry standards |
| Security | 10% | Safe, no credential exposure, validated inputs |
| Documentation | 5% | Clear, complete, well-structured |
| Efficiency | 5% | Practical, not over-engineered |

## Review Process

1. **Automated Checks** - Metadata validation, structure validation, link checking
2. **Peer Review** - At least one maintainer reviews
3. **Quality Evaluation** - Scored against criteria
4. **Security Review** - For skills with external integrations
5. **Merge** - Approved changes merged to main

## Style Guidelines

### Writing Style
- Professional, clear, concise
- Active voice preferred
- Define acronyms on first use
- Use consistent terminology (see `shared-knowledge/terminology/`)

### Markdown Standards
- ATX headings (`#`, `##`, `###`)
- Fenced code blocks with language tags
- Relative links for internal references
- Tables for structured data

### File Naming
- Directories: kebab-case (`skill-name/`)
- Files: PascalCase for specs (`SKILL.md`), kebab-case for others
- No spaces in file/directory names

### Metadata
- Use the defined JSON schema
- Version: Semantic Versioning (MAJOR.MINOR.PATCH)
- Dates: ISO 8601 (YYYY-MM-DD)

## Questions?

Open an issue for:
- Clarification on guidelines
- Category placement questions
- Architecture discussions
- Platform integration questions

---

**Remember**: Quality over quantity. A few excellent skills are better than many mediocre ones.