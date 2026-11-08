# Workflows

This directory contains detailed workflow definitions for the AI Automation Engineer skill.

## Structure

| File | Purpose |
|------|---------|
| `ai-automation-lifecycle.md` | Primary 10-step workflow for AI automation |
| `platform-selection.md` | Workflow for selecting orchestration platform |
| `cost-optimization.md` | Workflow for systematic cost reduction |
| `deployment.md` | Workflow for production deployment |
| `incident-response.md` | Workflow for handling automation failures |
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
    A[Process Discovery] --> B{AI Suitable?}
    B -->|Yes| C[Platform Selection]
    B -->|No| D[Traditional Automation]
    C --> E[Workflow Design]
    E --> F[Implementation]
    F --> G[Testing]
    G --> H{Passes?}
    H -->|No| F
    H -->|Yes| I[Deployment]
```

## Integration with SKILL.md

The `workflow` section in SKILL.md provides the 10-step framework. This directory provides detailed implementation for each step.

## Testing

Workflows should have acceptance tests in `../tests/acceptance/`.