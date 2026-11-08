# Configuration

This directory contains configuration files for the AI Automation Engineer skill.

## Files

| File | Purpose | Format |
|------|---------|--------|
| `settings.yaml` | Main skill configuration | YAML |
| `mcp.json` | MCP server registry (Claude Code) | JSON |
| `prompts/` | Prompt templates for different automation patterns | Markdown/Text |

## Configuration Options

### `settings.yaml`

```yaml
# Example configuration structure
orchestration:
  platform: "prefect"  # n8n, airflow, prefect, zapier
  environment: "development"  # development, staging, production

llm:
  primary_provider: "openai"  # openai, anthropic, local
  model: "gpt-4-turbo-preview"
  temperature: 0.1
  max_tokens: 2000
  token_budget_per_run: 50000
  fallback_provider: "anthropic"
  fallback_model: "claude-3-opus-20240229"

workflow:
  default_timeout: 300
  max_retries: 3
  retry_delay: 5
  enable_compensation: true
  idempotency_keys: true

monitoring:
  enabled: true
  metrics_port: 9090
  log_level: "info"  # debug, info, warn, error
  alert_webhook: ""
  trace_sampling: 0.1

cost_control:
  enabled: true
  monthly_budget_usd: 1000
  alert_threshold_pct: 80
  track_per_workflow: true

deployment:
  container_registry: "ghcr.io"
  image_name: "ai-automation-engineer"
  health_check_path: "/health"
  port: 8000
```

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | OpenAI API key | Yes (if using OpenAI) | - |
| `ANTHROPIC_API_KEY` | Anthropic API key | Yes (if using Anthropic) | - |
| `PREFECT_API_KEY` | Prefect Cloud API key | No | - |
| `N8N_API_KEY` | n8n API key | No | - |
| `AIRFLOW_CONN_*` | Airflow connections | No | - |
| `PINECONE_API_KEY` | Pinecone API key | No | - |
| `CHROMA_HOST` | Chroma host | No | `localhost` |

## Platform-Specific Config

- **Claude Code**: Reads `settings.yaml` directly; MCP servers from `mcp.json`
- **OpenCode**: Merged into `opencode.json` via manifest generator
- **Cursor**: Via `claude.skills` settings
- **Generic**: Manual setup

## Validation

```bash
yamllint settings.yaml
```