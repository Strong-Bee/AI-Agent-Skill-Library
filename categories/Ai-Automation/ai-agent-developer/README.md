# AI Agent Developer

> Build, deploy, and manage autonomous AI agents using modern frameworks and best practices.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The AI Agent Developer skill provides comprehensive capabilities for designing, building, and deploying production-ready autonomous AI agents. It covers the complete lifecycle from architecture selection through deployment and monitoring, using industry-standard frameworks like LangGraph, AutoGen, and CrewAI.

This skill embodies the professional role of an **AI Agent Developer** - a specialist who combines LLM reasoning with tools, memory, and orchestration to create agents that can autonomously perceive, reason, and act to accomplish complex tasks.

## Target Audience

- **Primary**: AI Agent Developers, AI Automation Engineers
- **Secondary**: Full-Stack Developers, ML Engineers, Technical Leads, Startup Founders

## Prerequisites

- **Required tools**: Python 3.10+, Docker, Git, LangChain
- **Required knowledge**: Python proficiency, async/await patterns, REST APIs, basic LLM concepts
- **Platform requirements**: 
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
# User-level (available everywhere)
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/ai-agent-developer ~/.claude/skills/ai-automation/ai-agent-developer

# Project-level
mkdir -p .claude/skills
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/ai-agent-developer .claude/skills/ai-automation/ai-agent-developer
```

### OpenCode
```bash
# Add to opencode.json skills.paths
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/ai-agent-developer ~/.opencode/skills/ai-automation/ai-agent-developer
```

### Generic (Any Markdown-compatible Agent)
```bash
cp -r /path/to/ai-agent-skill-library/categories/ai-automation/ai-agent-developer /your/agent/skills/
```

## Quick Start

```markdown
# Basic agent invocation
Use the ai-agent-developer skill to build a research agent that:
1. Searches for latest AI agent frameworks
2. Compares LangGraph, AutoGen, and CrewAI
3. Outputs a comparison report with recommendations
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Agent Architecture Design | Design single-agent, multi-agent, and hierarchical architectures |
| Framework Implementation | Build agents with LangGraph, AutoGen, CrewAI, Semantic Kernel |
| Tool Integration | Connect agents to APIs, databases, file systems, and custom functions |
| Agentic Prompt Engineering | Craft reliable prompts using ReAct, CoT, structured output patterns |
| Memory Management | Implement short-term, long-term, and semantic memory systems |
| Agent Evaluation | Build evaluation pipelines with LLM-as-judge and quantitative metrics |
| Production Deployment | Containerize, monitor, and scale agents in production |

## Workflow Overview

This skill follows the standard 10-step workflow adapted for agent development:

1. **Request Analysis** - Determine if agentic approach is appropriate
2. **Requirement Clarification** - Define agent capabilities, constraints, integrations
3. **Context Gathering** - Inventory APIs, data sources, team skills
4. **Research** - Compare frameworks, find reference implementations
5. **Planning** - Architecture diagram, task breakdown, evaluation criteria
6. **Task Execution** - Implement agent graph, tools, prompts, memory
7. **Validation** - Run evaluation suite; measure success rate, latency, cost
8. **Quality Review** - Security audit, best practices, code review
9. **Error Correction** - Fix failures; optimize prompts; re-evaluate
10. **Final Delivery** - Docker image, docs, runbook, handoff

## Configuration

Key configuration options (see `config/settings.yaml` for full list):

| Option | Description | Default |
|--------|-------------|---------|
| `llm.primary_provider` | LLM provider (openai, anthropic, local) | `openai` |
| `llm.model` | Model name | `gpt-4-turbo-preview` |
| `agent.max_iterations` | Maximum agent loop iterations | `10` |
| `agent.enable_human_in_loop` | Require confirmation for critical actions | `true` |
| `tools.enabled` | Enabled tool integrations | `["web_search", "file_operations"]` |
| `memory.long_term_enabled` | Enable persistent memory | `true` |

## Examples

See `examples/` directory for complete working examples:
- `examples/basic/research-agent/` - Single-agent research assistant
- `examples/multi-agent/code-review-team/` - Multi-agent code review (reviewer, tester, security)
- `examples/production/customer-support/` - Customer support agent with HITL

## Limitations

- Cannot guarantee 100% reliability of LLM-based agents
- Agent behavior may vary across model versions
- Requires human oversight for high-stakes decisions
- Token costs can be significant for complex agents
- Evaluation of open-ended agent behavior remains challenging
- Does not cover: training foundation models, hardware infrastructure, non-agentic LLM apps

## Related Skills

- [AI Automation Engineer](../ai-automation-engineer/README.md) - Build automation pipelines with agents
- [Prompt Engineer](../prompt-engineer/README.md) - Advanced prompt optimization techniques
- [RAG Engineer](../rag-engineer/README.md) - Retrieval-augmented generation for agent knowledge
- [MCP Developer](../mcp-developer/README.md) - Build Model Context Protocol servers for agents
- [Multi-Agent Architect](../multi-agent-architect/README.md) - Advanced multi-agent system design

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)