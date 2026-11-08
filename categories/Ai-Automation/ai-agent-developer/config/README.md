# Configuration

This directory contains configuration files for the AI Agent Developer skill.

## Files

| File | Purpose | Format |
|------|---------|--------|
| `settings.yaml` | Main skill configuration | YAML |
| `mcp.json` | MCP server registry (Claude Code) | JSON |
| `prompts/` | Prompt templates for different agent types | Markdown/Text |

## Configuration Options

### `settings.yaml`

```yaml
# Example configuration structure
llm:
  primary_provider: "openai"  # openai, anthropic, local
  model: "gpt-4-turbo-preview"
  temperature: 0.1
  max_tokens: 4000
  fallback_provider: "anthropic"
  fallback_model: "claude-3-opus-20240229"

agent:
  max_iterations: 10
  timeout_seconds: 300
  enable_human_in_loop: true
  recursion_limit: 25

tools:
  enabled:
    - "web_search"
    - "file_operations"
    - "code_execution"
    - "python_repl"
  rate_limits:
    web_search: 10/minute
    code_execution: 5/minute
  timeouts:
    web_search: 30
    code_execution: 120

memory:
  short_term_window: 20
  long_term_enabled: true
  vector_store: "chroma"  # chroma, pinecone, weaviate, faiss
  embedding_model: "text-embedding-3-small"
  collection_name: "agent_memory"

evaluation:
  enabled: true
  dataset: "evals/golden_set.jsonl"
  judge_model: "gpt-4"
  metrics:
    - "success_rate"
    - "latency_p95"
    - "token_usage"
    - "cost_per_task"

observability:
  enabled: true
  provider: "langsmith"  # langsmith, langfuse, custom
  project_name: "ai-agent-developer"
  trace_level: "debug"  # debug, info, warn, error

deployment:
  container_registry: "ghcr.io"
  image_name: "ai-agent-developer"
  health_check_path: "/health"
  port: 8000
```

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | OpenAI API key | Yes (if using OpenAI) | - |
| `ANTHROPIC_API_KEY` | Anthropic API key | Yes (if using Anthropic) | - |
| `LANGCHAIN_API_KEY` | LangSmith API key | No | - |
| `LANGCHAIN_PROJECT` | LangSmith project name | No | `ai-agent-developer` |
| `PINECONE_API_KEY` | Pinecone API key | No (if using Pinecone) | - |
| `PINECONE_ENVIRONMENT` | Pinecone environment | No | - |
| `CHROMA_HOST` | Chroma host | No (if using Chroma) | `localhost` |
| `CHROMA_PORT` | Chroma port | No | `8000` |

## Platform-Specific Config

- **Claude Code**: Reads `settings.yaml` directly; MCP servers from `mcp.json`
- **OpenCode**: Merged into `opencode.json` via manifest generator
- **Cursor**: Via `claude.skills` settings
- **Generic**: Manual setup

## Validation

Run validation:
```bash
# Validate YAML syntax
yamllint settings.yaml

# Validate against schema (when available)
python -m jsonschema -i settings.yaml ../../../../core/metadata-schema/config.schema.json
```