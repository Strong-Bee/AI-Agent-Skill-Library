# Examples

This directory contains usage examples for the AI Automation Engineer skill.

## Structure

```
examples/
├── basic/
│   ├── document-processing/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── workflow.json (n8n) / dag.py (Airflow) / flow.py (Prefect)
│   │   └── README.md
│   └── data-extraction/
├── multi-step/
│   ├── customer-onboarding/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── workflows/
│   │   ├── hitl_handlers/
│   │   └── README.md
│   └── order-processing/
├── event-driven/
│   ├── support-triage/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── trigger_config/
│   │   └── README.md
│   └── webhook-handler/
├── batch/
│   ├── report-generation/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── schedule_config/
│   │   └── README.md
│   └── data-sync/
└── edge-cases/
    ├── rate-limit-handling/
    ├── partial-failure-recovery/
    └── schema-evolution/
```

## Example Requirements

Each example must include:
- **Input**: Realistic user request / trigger payload
- **Context**: Any required context files
- **Output**: Expected deliverables (or clearly marked as illustrative)
- **Implementation**: Working workflow definition
- **README.md**: Description of what the example demonstrates

## Example Categories

| Category | Purpose |
|----------|---------|
| `basic/` | Minimal viable single-workflow examples |
| `multi-step/` | Complex multi-system workflows with HITL |
| `event-driven/` | Event-triggered automations |
| `batch/` | Scheduled/recurring workflows |
| `edge-cases/` | Error handling, limits, unusual inputs |

## Runnable vs Illustrative

- **Runnable**: Can be executed end-to-end on target platform
- **Illustrative**: Shows expected output format/quality but not executable

Mark each example clearly in its README.md.

## Current Examples

| Example | Type | Status | Platform Tested |
|---------|------|--------|-----------------|
| basic/document-processing | Runnable | 📝 Draft | - |
| multi-step/customer-onboarding | Runnable | 📝 Draft | - |
| event-driven/support-triage | Runnable | 📝 Draft | - |
| batch/report-generation | Runnable | 📝 Draft | - |

## Testing Examples

Examples serve as acceptance tests. Validate:
```bash
# Deploy and test workflow
# n8n: Import workflow.json, execute
# Prefect: prefect deploy flow.py
# Airflow: airflow dags test dag_id
```

## Contributing Examples

1. Follow the structure above
2. Use realistic but anonymized data
3. Document any setup required
4. Verify output matches current skill version