# Documentation Specialist

> Create, maintain, and optimize technical and user documentation with clarity, accuracy, and usability.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The Documentation Specialist skill provides comprehensive capabilities for creating, maintaining, and optimizing technical and user documentation with clarity, accuracy, and usability.

This skill embodies the professional role of a **Documentation Specialist** - a specialist who creates, maintains, and optimizes technical and user documentation that enables users to understand, use, and troubleshoot products effectively.

## Target Audience

- **Primary**: Technical Writers, Documentation Specialists, Developer Experience Engineers
- **Secondary**: Engineering Teams, Product Managers, Support Teams, Developer Relations

## Prerequisites

- **Required tools**: Static Site Generator (Docusaurus/MkDocs/VitePress), Git, CI/CD, API Doc Tool (Redoc/Scalar), Linting (Vale/Markdownlint)
- **Required knowledge**: Technical writing fundamentals, Markdown/AsciiDoc, Git, CI/CD, API concepts (REST/GraphQL)
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/Administration-Virtual-Assistant/Documentation-Specialist ~/.claude/skills/administration/documentation-specialist
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/Administration-Virtual-Assistant/Documentation-Specialist ~/.opencode/skills/administration/documentation-specialist
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/Administration-Virtual-Assistant/Documentation-Specialist /your/agent/skills/
```

## Quick Start

```markdown
# Build a documentation site
Use the documentation-specialist skill to:
1. Set up Docusaurus with TypeScript
2. Configure OpenAPI spec for API reference
3. Create content structure (concept, how-to, reference, tutorial)
4. Configure Vale for style checking
6. Set up GitHub Actions for CI/CD
7. Deploy to Netlify/Vercel/GitHub Pages
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Technical Writing Excellence | Clear, accurate, user-focused content across formats |
| API Documentation | OpenAPI/Swagger, endpoint reference, tutorials, SDK docs |
| Information Architecture | Content organization, navigation, search, findability |
| Documentation Tools & Automation | Static site generators, CI/CD, linting, automated checks |
| Content Strategy & Governance | Style guides, editorial workflows, content modeling |
| Developer Experience Optimization | Code samples, interactive examples, search, feedback |

## Workflow Overview

10-step workflow for documentation:

1. **Request Analysis** - Audience, goals, scope, format, timeline, constraints
2. **Requirement Clarification** - Scope, content types, depth, format, review process
3. **Context Gathering** - Specs, code, designs, existing docs, SME interviews
4. **Research** - Best practices, competitor docs, user needs, tooling options
5. **Planning** - Structure, timeline, resources, review process, metrics
6. **Task Execution** - Write, review, publish with standards and CI/CD
7. **Validation** - Technical accuracy, usability, accessibility, completeness
8. **Quality Review** - Quality, consistency, strategy alignment, maintenance
9. **Error Correction** - Fix issues, improve content, update processes
10. **Final Delivery** - Package, handoff, monitoring, knowledge transfer

## Configuration

Key options in `config/settings.yaml`:

```yaml
site:
  name: "Product Documentation"
  url: "https://docs.example.com"
  base_url: "/"
  organization: "Your Company"
  repo: "github.com/your-org/docs"

build:
  generator: "docusaurus"  # docusaurus, mkdocs, vitepress, nextra
  versioning: true
  last_update: true
  edit_url: "https://github.com/your-org/docs/edit/main/"

content:
  languages: ["en"]  # add more for i18n
  versioning: "current"  # current, all, specific
  sidebar: "auto"  # auto, manual
  search: "algolia"  # algolia, local, none

quality:
  linting: "vale"  # vale, markdownlint, both
  link_check: "lychee"
  spell_check: "cspell"
  accessibility: "axe-core"
  broken_links: "fail"

api:
  openapi_spec: "./api/openapi.yaml"
  generator: "redoc"  # redoc, scalar, swagger-ui
  grouping: "tags"
  examples: true

analytics:
  provider: "plausible"  # plausible, ga4, matomo, none
  search: "algolia"  # algolia, local, none
  feedback: true
```

## Examples

See `examples/` for:
- `getting-started/` - Quickstart guide with interactive examples
- `api-reference/` - Auto-generated API reference from OpenAPI
- `tutorial/first-app/` - Step-by-step tutorial with code
- `architecture/system-design/` - System design documentation
- `runbooks/incident-response/` - Operational runbooks

## Limitations

- Cannot write accurate docs without engineer/PM input and review
- Cannot maintain docs for rapidly changing features without process integration
- Cannot measure ROI of documentation directly without instrumentation
- Cannot fix poor product UX with documentation alone
- Localization and translation require specialized workflows and budget

## Related Skills

- [Technical Writer](../Technical-Writer/README.md) - Deep technical writing focus
- [Customer Support Specialist](../Customer-Support-Specialist/README.md) - Knowledge base for support
- [API Developer](../API-Developer/README.md) - API design for documentation
- [Content Strategist](../Content-Strategist/README.md) - Content strategy for docs

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)