# Examples

This directory contains usage examples for the AI Agent Developer skill.

## Structure

```
examples/
├── basic/
│   ├── research-agent/
│   │   ├── input.md          # Example user request
│   │   ├── context/          # Context files (if any)
│   │   ├── output/           # Expected deliverables
│   │   ├── agent.py          # Agent implementation
│   │   └── README.md         # Example description
│   └── simple-chatbot/
├── multi-agent/
│   ├── code-review-team/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── agents/
│   │   │   ├── reviewer.py
│   │   │   ├── tester.py
│   │   │   └── security.py
│   │   ├── orchestrator.py
│   │   └── README.md
│   └── research-team/
├── production/
│   ├── customer-support/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── agent.py
│   │   ├── hitl_handler.py
│   │   ├── deployment/
│   │   │   ├── Dockerfile
│   │   │   ├── docker-compose.yml
│   │   │   └── k8s/
│   │   └── README.md
│   └── data-analysis/
└── edge-cases/
    ├── tool-failure-recovery/
    ├── long-context-handling/
    └── adversarial-inputs/
```

## Example Requirements

Each example must include:
- **Input**: Realistic user request
- **Context**: Any required context files
- **Output**: Expected deliverables (or clearly marked as illustrative)
- **Implementation**: Working agent code
- **README.md**: Description of what the example demonstrates

## Example Categories

| Category | Purpose |
|----------|---------|
| `basic/` | Minimal viable single-agent examples |
| `multi-agent/` | Multi-agent system demonstrations |
| `production/` | Production-ready with deployment configs |
| `edge-cases/` | Error handling, limits, unusual inputs |

## Runnable vs Illustrative

- **Runnable**: Can be executed end-to-end on target platform
- **Illustrative**: Shows expected output format/quality but not executable

Mark each example clearly in its README.md.

## Current Examples

| Example | Type | Status | Platform Tested |
|---------|------|--------|-----------------|
| basic/research-agent | Runnable | 📝 Draft | - |
| multi-agent/code-review-team | Runnable | 📝 Draft | - |
| production/customer-support | Runnable | 📝 Draft | - |

## Testing Examples

Examples serve as acceptance tests. Validate:
```bash
# Run example through skill
python -m examples.basic.research-agent.agent "Research topic"
# Compare output to expected/
```

## Contributing Examples

1. Follow the structure above
2. Use realistic but anonymized data
3. Document any setup required
4. Verify output matches current skill version