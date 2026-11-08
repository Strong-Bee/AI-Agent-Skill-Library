# Tool Integrations

This directory contains tool integration code and documentation for the AI Automation Engineer skill.

## Structure

| File/Directory | Purpose |
|----------------|---------|
| `llm-integration/` | LLM API wrappers with validation, fallback, cost tracking |
| `orchestration/` | Platform-specific clients (n8n, Airflow, Prefect, Zapier) |
| `data-pipeline/` | ETL/ELT utilities, schema validation, quality checks |
| `monitoring/` | Metrics, logging, tracing, alerting utilities |
| `cost-tracking/` | Token counting, cost calculation, budget enforcement |
| `shared/` | Shared utilities across tools |
| `schemas/` | Input/output schemas for tool calls |

## Platform-Specific Implementations

Each tool may have different implementations per platform:

```
llm-integration/
├── claude/          # Claude Code implementation
├── opencode/        # OpenCode tool definition
├── cursor/          # Cursor integration
├── generic/         # Generic/documentation only
└── README.md        # Tool-specific documentation
```

## Supported Tools (from SKILL.md)

### Required Tools
- **LangChain** - LLM chain composition
- **Python** - Custom functions and scripting
- **Docker** - Containerization
- **Git** - Version control

### Optional Tools (with fallbacks)
- **n8n** - Fallback: Prefect or custom orchestration
- **Zapier** - Fallback: n8n or Make
- **Airflow** - Fallback: Prefect
- **Prefect** - Fallback: Airflow or custom
- **Temporal** - Fallback: Custom state machine

## Adding a New Tool

1. Create platform-specific implementations
2. Define input/output schemas in `schemas/`
3. Add to `supported_tools` in SKILL.md
4. Document fallback procedures
5. Add tests in `../tests/integration/`