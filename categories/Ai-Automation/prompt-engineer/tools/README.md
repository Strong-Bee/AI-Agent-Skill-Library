# Tool Integrations

This directory contains tool integration code and documentation for the Prompt Engineer skill.

## Structure

| File/Directory | Purpose |
|----------------|---------|
| `prompt-templates/` | Jinja2/Python prompt template rendering |
| `evaluation/` | Evaluation pipeline components (metrics, judges) |
| `optimization/` | DSPy, OPRO, manual optimization utilities |
| `versioning/` | Prompt versioning, diffing, migration tools |
| `security/` | Prompt injection detection, PII scanning |
| `shared/` | Shared utilities across tools |
| `schemas/` | Input/output schemas for tool calls |

## Supported Tools (from SKILL.md)

### Required Tools
- **Python** - Prompt development, evaluation, optimization
- **LangChain** - Prompt templates, chains, evaluation
- **Model APIs** - OpenAI, Anthropic, Google for testing
- **Git** - Prompt version control
- **pytest** - Prompt testing and evaluation

### Optional Tools (with fallbacks)
- **DSPy** - Fallback: Manual optimization with structured process
- **PromptLayer** - Fallback: LangSmith, Langfuse, or Git-based versioning
- **LangSmith** - Fallback: Langfuse or custom evaluation pipeline
- **Langfuse** - Fallback: Custom logging and evaluation

## Adding a New Tool

1. Create platform-specific implementations
2. Define input/output schemas in `schemas/`
3. Add to `supported_tools` in SKILL.md
4. Document fallback procedures
5. Add tests in `../tests/integration/`