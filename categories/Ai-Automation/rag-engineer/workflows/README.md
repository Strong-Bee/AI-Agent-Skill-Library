# Workflows

This directory contains detailed workflow definitions for the RAG Engineer skill.

## Structure

| File | Purpose |
|------|---------|
| `rag-development-lifecycle.md` | Primary 10-step workflow for RAG engineering |
| `embedding-selection.md` | Workflow for embedding model selection |
| `retrieval-optimization.md` | Workflow for retrieval pipeline optimization |
| `evaluation-process.md` | Workflow for RAG evaluation with RAGAS |
| `deployment.md` | Workflow for production deployment |
| `incident-response.md` | Workflow for quality drift and incidents |
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
    A[Requirements] --> B[Data Analysis]
    B --> C[Embedding Selection]
    C --> D[Vector Store Setup]
    D --> E[Retrieval Pipeline]
    E --> F[Generation Pipeline]
    F --> G[Evaluation]
    G --> H{Passes?}
    H -->|No| E
    H -->|Yes| I[Deployment]
```

## Integration with SKILL.md

The `workflow` section in SKILL.md provides the 10-step framework. This directory provides detailed implementation for each step.

## Testing

Workflows should have acceptance tests in `../tests/acceptance/`.