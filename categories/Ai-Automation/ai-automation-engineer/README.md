# AI Automation Engineer

> Design and implement AI-powered automation pipelines for business processes and workflows.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The AI Automation Engineer skill provides comprehensive capabilities for designing and implementing automated workflows that integrate AI capabilities (LLMs, vision, audio) with orchestration platforms to streamline business processes. It bridges the gap between AI model capabilities and production automation systems.

This skill embodies the professional role of an **AI Automation Engineer** - a specialist who combines traditional workflow automation with AI model invocations to create intelligent, reliable, and cost-effective automation pipelines.

## Target Audience

- **Primary**: AI Automation Engineers, AI Agent Developers
- **Secondary**: Full-Stack Developers, DevOps Engineers, Business Analysts, Technical Leads, Startup Founders

## Prerequisites

- **Required tools**: Python 3.10+, Docker, Git, LangChain
- **Required knowledge**: Python proficiency, workflow orchestration concepts, REST APIs, basic LLM concepts
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/ai-automation-engineer ~/.claude/skills/ai-automation/ai-automation-engineer
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/ai-automation-engineer ~/.opencode/skills/ai-automation/ai-automation-engineer
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/ai-automation/ai-automation-engineer /your/agent/skills/
```

## Quick Start

```markdown
# Build an invoice processing automation
Use the ai-automation-engineer skill to create a pipeline that:
1. Monitors email for incoming invoices
2. Extracts structured data using LLM
3. Validates against business rules
4. Routes for human approval if needed
5. Posts to accounting system
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Automation Architecture Design | Design scalable architectures integrating AI and traditional automation |
| LLM Workflow Integration | Integrate LLMs with validation, fallback, and cost control |
| Orchestration Platforms | Build on n8n, Airflow, Prefect, Zapier with custom extensions |
| Data Pipeline Engineering | Build ETL/ELT pipelines with quality checks for AI workflows |
| Observability & Monitoring | Implement metrics, alerting, debugging for AI pipelines |
| Cost Optimization | Reduce token usage through caching, model selection, batching |
| Governance & Compliance | Access controls, audit trails, data privacy compliance |

## Workflow Overview

10-step workflow adapted for AI automation:

1. **Request Analysis** - Map process, identify AI opportunities, estimate ROI
2. **Requirement Clarification** - Define triggers, actions, decisions, SLAs
3. **Context Gathering** - Inventory systems, APIs, data schemas, team skills
4. **Research** - Compare platforms (n8n, Airflow, Prefect); find patterns
5. **Planning** - Workflow design, task breakdown, monitoring design
6. **Task Execution** - Build workflows, custom nodes, prompts, configs
7. **Validation** - Test scenarios, measure success rate, latency, cost
8. **Quality Review** - Reliability, security, maintainability, cost review
9. **Error Correction** - Fix failures, optimize, re-validate
10. **Final Delivery** - Production workflows, CI/CD, runbook, dashboards

## Configuration

Key options in `config/settings.yaml`:

| Option | Description | Default |
|--------|-------------|---------|
| `orchestration.platform` | Platform (n8n, airflow, prefect, zapier) | `prefect` |
| `llm.primary_provider` | LLM provider | `openai` |
| `llm.token_budget_per_run` | Max tokens per execution | `50000` |
| `workflow.enable_compensation` | Enable saga pattern | `true` |
| `cost_control.monthly_budget_usd` | Monthly cost limit | `1000` |

## Examples

See `examples/` for:
- `basic/document-processing/` - Invoice extraction with validation
- `multi-step/customer-onboarding/` - Multi-system onboarding with HITL
- `event-driven/support-triage/` - Email classification and routing
- `batch/report-generation/` - Scheduled AI report generation

## Limitations

- AI model outputs are probabilistic; require validation layers
- Token costs can scale unexpectedly with usage
- Rate limits on external APIs constrain throughput
- Debugging non-deterministic failures is challenging
- Governance requirements vary by industry/region
- Does not cover: training custom models, infrastructure provisioning, non-AI automation

## Related Skills

- [AI Agent Developer](../ai-agent-developer/README.md) - Build autonomous agents
- [RAG Engineer](../rag-engineer/README.md) - Knowledge retrieval for automations
- [MCP Developer](../mcp-developer/README.md) - Custom tool servers for workflows
- [Prompt Engineer](../prompt-engineer/README.md) - Optimize prompts for automation

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)