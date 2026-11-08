# Configuration

This directory contains configuration files for the Prompt Engineer skill.

## Files

| File | Purpose | Format |
|------|---------|--------|
| `settings.yaml` | Main skill configuration | YAML |
| `mcp.json` | MCP server registry (Claude Code) | JSON |
| `prompts/` | Base prompt templates | Markdown/Text |

## Configuration Options

### `settings.yaml`

```yaml
# Example configuration structure
models:
  primary: "gpt-4-turbo-preview"
  fallback:
    - "claude-3-opus-20240229"
    - "gemini-1.5-pro"
  evaluation_judge: "gpt-4"
  local_models: []  # e.g., "llama-3-70b" via Ollama

evaluation:
  dataset_path: "evals/golden_set.jsonl"
  metrics:
    - "accuracy"
    - "f1"
    - "format_validity"
    - "latency"
    - "cost"
  judge_model: "gpt-4"
  sample_size: 100
  confidence_level: 0.95

optimization:
  enabled: true
  method: "dspy"  # dspy, opro, manual
  budget: 1000  # API calls
  metric: "accuracy"
  max_iterations: 10

prompt_defaults:
  temperature: 0.1
  max_tokens: 2000
  top_p: 0.95
  frequency_penalty: 0.0
  presence_penalty: 0.0

security:
  prompt_injection_detection: true
  pii_detection: true
  output_validation: true

deployment:
  versioning: "semantic"  # semantic, date-based
  ci_cd_enabled: true
  canary_percentage: 10
  rollback_on_regression: true
```

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | OpenAI API key | Yes | - |
| `ANTHROPIC_API_KEY` | Anthropic API key | Yes | - |
| `GOOGLE_API_KEY` | Google AI API key | No | - |
| `PROMPTLAYER_API_KEY` | PromptLayer API key | No | - |
| `LANGCHAIN_API_KEY` | LangSmith API key | No | - |
| `LANGFUSE_API_KEY` | Langfuse API key | No | - |

## Platform-Specific Config

- **Claude Code**: Reads `settings.yaml` directly; MCP servers from `mcp.json`
- **OpenCode**: Merged into `opencode.json` via manifest generator
- **Cursor**: Via `claude.skills` settings
- **Generic**: Manual setup

## Validation

```bash
yamllint settings.yaml
```