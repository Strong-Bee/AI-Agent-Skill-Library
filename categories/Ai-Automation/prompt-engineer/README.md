# Prompt Engineer

> Design, optimize, and evaluate prompts for reliable LLM behavior across tasks and models.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The Prompt Engineer skill provides comprehensive capabilities for designing, optimizing, and systematically evaluating prompts to elicit reliable, accurate, and cost-effective behavior from Large Language Models. It treats prompts as programmable interfaces that require versioning, testing, and optimization.

This skill embodies the professional role of a **Prompt Engineer** - a specialist who applies scientific methods to prompt design, combining prompt patterns, structured outputs, automated optimization, and rigorous evaluation frameworks.

## Target Audience

- **Primary**: Prompt Engineers, AI Agent Developers, AI Automation Engineers
- **Secondary**: Developers, Researchers, Content Creators, ML Engineers, Technical Leads

## Prerequisites

- **Required tools**: Python 3.10+, LangChain, Model APIs (OpenAI/Anthropic/Google), Git, pytest
- **Required knowledge**: Python proficiency, LLM fundamentals, basic prompting concepts, evaluation methodologies
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/prompt-engineer ~/.claude/skills/ai-automation/prompt-engineer
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/prompt-engineer ~/.opencode/skills/ai-automation/prompt-engineer
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/ai-automation/prompt-engineer /your/agent/skills/
```

## Quick Start

```markdown
# Optimize a classification prompt
Use the prompt-engineer skill to:
1. Design a few-shot prompt for sentiment classification
2. Build evaluation dataset with 100 labeled examples
3. Run evaluation pipeline measuring accuracy, F1, format validity
4. Optimize using DSPy for 20% accuracy improvement
5. Deploy with CI/CD and monitoring
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Prompt Design Patterns | Master Zero-shot, Few-shot, CoT, ToT, ReAct, Self-Consistency |
| Structured Output Engineering | JSON Schema, Pydantic, Function Calling for reliable parsing |
| Prompt Optimization | Manual iteration, DSPy, OPRO, APE for systematic improvement |
| Evaluation Methodologies | Ground truth, LLM-as-judge, statistical significance testing |
| Model-Specific Tuning | Adapt prompts for GPT-4, Claude, Gemini, Llama, etc. |
| Prompt Versioning & CI/CD | Git-based versioning, automated testing, canary deployment |
| Context Window Management | RAG integration, dynamic context selection, token optimization |

## Workflow Overview

10-step workflow for prompt engineering:

1. **Request Analysis** - Define task, constraints, success criteria
2. **Requirement Clarification** - Resolve ambiguities, edge cases
3. **Context Gathering** - Inventory prompts, data, model access
4. **Research** - Compare techniques, model behaviors, prior art
5. **Planning** - Template design, evaluation strategy, optimization plan
6. **Task Execution** - Develop prompts, build eval dataset, pipeline
7. **Validation** - Run evaluation, measure metrics, statistical testing
8. **Quality Review** - Best practices, security, portability review
9. **Error Correction** - Optimize, fix failures, re-evaluate
10. **Final Delivery** - Prompt library, eval report, deployment config

## Configuration

Key options in `config/settings.yaml`:

| Option | Description | Default |
|--------|-------------|---------|
| `models.primary` | Primary model for prompts | `gpt-4-turbo-preview` |
| `evaluation.dataset_path` | Path to golden set | `evals/golden_set.jsonl` |
| `evaluation.metrics` | Metrics to track | `accuracy, f1, format_validity, latency, cost` |
| `optimization.method` | Optimization approach | `dspy` |
| `prompt_defaults.temperature` | Default temperature | `0.1` |

## Examples

See `examples/` for:
- `classification/sentiment/` - Few-shot classification with structured output
- `generation/sql/` - Text-to-SQL with schema-guided generation
- `reasoning/math/` - Chain-of-Thought for mathematical reasoning
- `extraction/invoice/` - Structured extraction with validation
- `optimization/dspy-demo/` - Automated optimization with DSPy

## Limitations

- Prompt effectiveness varies significantly across model versions
- No universal 'best' prompt; requires empirical validation
- Optimization can be computationally expensive
- Prompt injection vulnerabilities require careful handling
- Context window limits constrain prompt complexity
- Does not cover: training foundation models, model architecture research

## Related Skills

- [AI Agent Developer](../ai-agent-developer/README.md) - Prompts for agent behavior
- [AI Automation Engineer](../ai-automation-engineer/README.md) - Prompts for automation pipelines
- [RAG Engineer](../rag-engineer/README.md) - Retrieval-augmented prompting
- [MCP Developer](../mcp-developer/README.md) - Tool descriptions for function calling

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)