# Workflows

This directory contains detailed workflow definitions for the AI Agent Developer skill.

## Structure

| File | Purpose |
|------|---------|
| `agent-development-lifecycle.md` | Primary 10-step workflow for agent development |
| `framework-selection.md` | Workflow for selecting orchestration framework |
| `prompt-optimization.md` | Workflow for systematic prompt improvement |
| `evaluation-pipeline.md` | Workflow for building and running agent evaluations |
| `deployment.md` | Workflow for production deployment |
| `diagrams/` | Mermaid/PlantUML workflow diagrams |

## Workflow Documentation Standard

Each workflow must document:

1. **Trigger** - What initiates this workflow
2. **Inputs** - Required and optional inputs
3. **Steps** - Sequential steps with decision points
4. **Outputs** - Expected deliverables
5. **Error Handling** - Failure modes and recovery
6. **Variations** - Alternative paths

## Diagram Format

Use Mermaid for diagrams:

```mermaid
flowchart TD
    A[Problem Definition] --> B{Agentic Needed?}
    B -->|Yes| C[Architecture Selection]
    B -->|No| D[Fixed Pipeline]
    C --> E[Framework Selection]
    E --> F[Implementation]
    F --> G[Evaluation]
    G --> H{Passes?}
    H -->|No| F
    H -->|Yes| I[Deployment]
```

## Integration with SKILL.md

The `workflow` section in SKILL.md provides the 10-step framework. This directory provides detailed implementation for each step.

## Testing

Workflows should have acceptance tests in `../tests/acceptance/`.