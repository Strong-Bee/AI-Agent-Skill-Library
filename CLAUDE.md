# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**AI Agent Skill Library** - A professional, multi-platform AI Agent Skill Library for transforming general-purpose AI agents into specialized professional assistants. Contains 12 categories targeting 100-300+ skills with standardized architecture, validation, packaging, and platform adapters.

**Current Phase**: Phase 4 - Initial Skill Development (30 skills) - Core architecture, templates, and validation tools are COMPLETE.

---

## Common Development Commands

### Validation (run before committing)
```bash
# Full validation suite (all skills under categories/)
./scripts/validate-all.sh

# Validate single skill
python tools/validators/validate_skill.py categories/ai-automation/ai-agent-developer

# Validate all skills with output
python tools/validators/validate_skill.py categories --all --output validation-report.json

# Skip external link checking (faster)
./scripts/validate-all.sh --skip-external
```

### Catalog Generation
```bash
# Generate catalog.json from all skills
python tools/generators/generate_catalog.py categories catalog.json

# Catalog is used for platform config generation and sync validation
```

### Platform Config Generation
```bash
# Generate platform-specific configs (Claude, OpenCode, Cursor, Copilot)
python tools/generators/generate_platform_configs.py categories catalog.json
```

### Skill Packaging
```bash
# Package a skill for distribution (zip + tar.gz + manifest)
python tools/packaging/package_skill.py categories/ai-automation/ai-agent-developer -o dist

# Skip validation (not recommended)
python tools/packaging/package_skill.py categories/ai-automation/ai-agent-developer --skip-validation
```

### Individual Validators
```bash
# Metadata validation (YAML frontmatter against JSON schema)
python tools/validators/validate_metadata.py categories/ai-automation/ai-agent-developer

# Structure validation (required dirs/files)
python tools/validators/validate_structure.py categories/ai-automation/ai-agent-developer

# Markdown linting
python tools/validators/validate_markdown.py categories/ai-automation/ai-agent-developer

# Link checking (internal + external)
python tools/validators/validate_links.py categories/ai-automation/ai-agent-developer
python tools/validators/validate_links.py categories/ai-automation/ai-agent-developer --skip-external

# Duplicate detection across skills
python tools/validators/check_duplicates.py categories

# Catalog synchronization check
python tools/validators/validate_catalog.py categories catalog.json
```

---

## High-Level Architecture

### Repository Structure
```
ai-agent-skill-library/
├── README.md, LICENSE, CHANGELOG.md, CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md
├── PROJECT_STATUS.md              # Development phase tracking
├── CLAUDE.md                       # This file
├── core/                           # Core frameworks & standards
│   ├── skill-standard/UNIVERSAL_SKILL_SPEC.md    # Skill specification (source of truth)
│   ├── metadata-schema/skill-metadata.schema.json # JSON Schema for frontmatter validation
│   ├── quality-framework/QUALITY_FRAMEWORK.md    # Quality criteria & scoring (90+/100 target)
│   ├── security-framework/SECURITY_FRAMEWORK.md  # Security requirements & safe execution
│   ├── testing-framework/TESTING_FRAMEWORK.md    # Test standards & validation
│   ├── documentation-standard/DOCUMENTATION_STANDARD.md
│   └── compatibility-standard/COMPATIBILITY_STANDARD.md
├── categories/                     # 12 professional categories (skill directories)
│   ├── ai-automation/              # AI & Automation (9 skills)
│   ├── software-development/       # (empty, ready for skills)
│   ├── digital-marketing/          # (empty, ready for skills)
│   ├── design-creative/            # (empty, ready for skills)
│   ├── business-management/        # (empty, ready for skills)
│   ├── data-analytics/             # (empty, ready for skills)
│   ├── administration/             # (empty, ready for skills)
│   ├── cybersecurity-it/           # (empty, ready for skills)
│   ├── finance-accounting/         # (empty, ready for skills)
│   ├── ecommerce-sales/            # (empty, ready for skills)
│   ├── writing-communication/      # (empty, ready for skills)
│   └── education-research/         # (empty, ready for skills)
├── shared-knowledge/               # Cross-cutting reference materials
│   ├── industry-standards/STANDARDS_INDEX.md
│   ├── methodologies/METHODOLOGIES_INDEX.md
│   ├── best-practices/BEST_PRACTICES_INDEX.md
│   └── terminology/TERMINOLOGY.md
├── platform-adapters/              # Platform-specific integration guides
│   ├── claude/README.md            # Claude Code / Claude Desktop
│   ├── opencode/README.md          # OpenCode
│   ├── cursor/README.md            # Cursor
│   ├── github-copilot/README.md    # GitHub Copilot
│   ├── generic/README.md           # Generic Markdown-based
│   └── compatibility-matrix.md     # Feature support matrix
├── templates/                      # Starter templates for new skills
│   ├── skill-template/             # Complete skill directory structure
│   │   ├── SKILL.md                # Template with all required fields
│   │   ├── README.md, CHANGELOG.md
│   │   ├── config/, knowledge/, workflows/, tools/, templates/, quality/, examples/, tests/
│   ├── workflow-template/WORKFLOW.md
│   ├── documentation-template/DOCUMENTATION.md
│   └── evaluation-template/EVALUATION.md
├── tools/                          # Development tooling
│   ├── validators/                 # 6 validators + main runner (validate_skill.py)
│   ├── generators/                 # Catalog & platform config generators
│   └── packaging/                  # Skill packaging (zip, tar.gz, manifest)
└── scripts/validate-all.sh         # Master validation script
```

**Note**: There are also empty category directories at the repository root (AI & Automation, AI-Automation, Business-Management, etc.) that appear to be legacy/duplicate structures. The canonical location for skills is `categories/<category>/<skill-name>/`.

### Core Standards (Must Follow)

1. **Universal Skill Specification** (`core/skill-standard/UNIVERSAL_SKILL_SPEC.md`) - Every skill MUST conform to this 10-section specification:
   - Identity (YAML frontmatter with unique ID, version, category)
   - Role Definition (professional persona)
   - Core Competencies (measurable, with proficiency levels)
   - Knowledge Base (sourced, no fabrication)
   - Workflow (10 mandatory steps: Analyze → Clarify → Gather → Research → Plan → Execute → Validate → Quality Review → Fix → Deliver)
   - Tools & Integrations (with fallbacks)
   - Output Standards (deliverables, acceptance criteria)
   - Self-Review Protocol (ANALYZE → EXECUTE → REVIEW → DETECT → FIX → RETEST → DELIVER)
   - Metadata Schema Reference
   - Versioning & Compatibility

2. **Metadata Schema** (`core/metadata-schema/skill-metadata.schema.json`) - JSON Schema for validating the YAML frontmatter in SKILL.md

3. **Quality Framework** - Target score ≥90/100, no criterion <70

4. **Security Framework** - No credential exposure, input validation, safe execution

5. **Testing Framework** - Unit, integration, and evaluation tests

### Skill Directory Structure (Standardized)
```
categories/category-name/skill-name/
├── SKILL.md              # Main specification (REQUIRED, validates against schema)
├── README.md             # Human-readable overview
├── CHANGELOG.md          # Version history (semantic versioning)
├── config/               # Configuration files (settings.yaml, mcp/)
├── knowledge/            # Domain knowledge base (markdown files)
├── workflows/            # Workflow definitions
├── tools/                # Tool integrations & scripts
├── templates/            # Reusable templates
├── quality/              # Quality assurance & evaluation configs
├── examples/             # Usage examples (executable)
└── tests/                # Validation tests
```

### Development Workflow for New Skills

1. **Copy Template**: `cp -r templates/skill-template categories/<category>/<skill-name>`
2. **Fill SKILL.md**: Complete all YAML frontmatter fields + human-readable sections
3. **Populate Directories**: Add content to config/, knowledge/, workflows/, tools/, templates/, quality/, examples/, tests/
4. **Validate**: `python tools/validators/validate_skill.py categories/<category>/<skill-name>`
5. **Fix Issues**: Iterate until all validators pass
6. **Generate Catalog**: `python tools/generators/generate_catalog.py categories catalog.json`
7. **Package**: `python tools/packaging/package_skill.py categories/<category>/<skill-name> -o dist`

### Key Files to Reference

| Purpose | File |
|---------|------|
| Skill specification (source of truth) | `core/skill-standard/UNIVERSAL_SKILL_SPEC.md` |
| Metadata validation schema | `core/metadata-schema/skill-metadata.schema.json` |
| Skill template (copy this) | `templates/skill-template/SKILL.md` |
| Example complete skill | `categories/ai-automation/ai-agent-developer/SKILL.md` |
| Validation runner | `tools/validators/validate_skill.py` |
| Catalog generator | `tools/generators/generate_catalog.py` |
| Package creator | `tools/packaging/package_skill.py` |
| Platform adapter (Claude) | `platform-adapters/claude/README.md` |

---

## Important Conventions

### Skill Identity (YAML Frontmatter)
- `id`: kebab-case, unique across library (e.g., `ai-agent-developer`)
- `category`: Must match one of 12 exact category names
- `version`: Semantic versioning (MAJOR.MINOR.PATCH)
- `maturity`: alpha, beta, stable, deprecated
- `platforms`: At least one of: claude, opencode, cursor, github-copilot, generic

### Category Names (Exact Match Required)
```
ai-automation, software-development, digital-marketing, design-creative,
business-management, data-analytics, administration, cybersecurity-it,
finance-accounting, ecommerce-sales, writing-communication, education-research
```

### Validation Requirements
- All skills MUST pass `validate_skill.py` before release
- No TODO placeholders, skipped tests, or stub functionality in released skills
- Quality score ≥90/100 with no criterion <70
- Security review passed (no exposed credentials, validated inputs)

### Platform Integration
- **Claude Code**: Symlink categories to `~/.claude/skills/` or `.claude/skills/`
- **OpenCode**: Configure `opencode.json` with skills paths
- **Cursor**: Set `claude.skillsPath` in settings
- **Generic**: Copy categories directory to agent's knowledge directory

---

## Current Development Priorities

1. **Develop 30 initial high-value skills** across priority categories (see PROJECT_STATUS.md)
2. **Complete platform adapter implementation** (scripts, manifests)
3. **Create comprehensive documentation** (getting started, installation, development guides)
4. **Run validation suite** on all skills
5. **Prepare release packages**

---

## Testing & Verification

```bash
# Quick validation of single skill (run during development)
python tools/validators/validate_skill.py categories/ai-automation/ai-agent-developer

# Full suite before commits
./scripts/validate-all.sh

# Check catalog sync after adding/modifying skills
python tools/generators/generate_catalog.py categories catalog.json
python tools/validators/validate_catalog.py categories catalog.json
```

---

## Notes for Future Instances

- **This is a skill library, not an application** - there's no "build" or "run" in the traditional sense
- **Validation is the primary CI gate** - all changes must pass validators
- **Templates are in `templates/skill-template/`** - use these as starting point for new skills
- **The example skill `ai-agent-developer`** is the reference implementation - follow its patterns
- **Platform adapters are documentation only** - they describe how skills integrate with each platform
- **No external dependencies** - tools are pure Python, shell scripts; run with `python3` and `bash`
- **Root-level category directories** (AI & Automation, Business-Management, etc.) are empty/legacy - ignore them; canonical skills are under `categories/`