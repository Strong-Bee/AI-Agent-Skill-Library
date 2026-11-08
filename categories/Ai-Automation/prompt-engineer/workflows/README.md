# Workflows

This directory contains detailed workflow definitions for the Prompt Engineer skill.

## Structure

| File | Purpose |
|------|---------|
| `prompt-development-lifecycle.md` | Primary 10-step workflow for prompt engineering |
| `optimization-process.md` | Workflow for systematic prompt optimization |
| `evaluation-process.md` | Workflow for building and running evaluations |
| `ab-testing.md` | Workflow for A/B testing prompt variants |
| `deployment.md` | Workflow for production prompt deployment |
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
    A[Task Analysis] --> B[Pattern Selection]
    B --> C[Initial Draft]
    C --> D[Evaluation]
    D --> E{Meets Criteria?}
    E -->|No| F[Error Analysis]
    F --> C
    E -->|Yes| G[Validation]
    G --> H[Deployment]
```

## Integration with SKILL.md

The `workflow` section in SKILL.md provides the 10-step framework. This directory provides detailed implementation for each step.

## Testing

Workflows should have acceptance tests in `../tests/acceptance/`.