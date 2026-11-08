# Templates

This directory contains reusable templates for the AI Automation Engineer skill.

## Structure

| File | Purpose |
|------|---------|
| `workflow-n8n.j2` | n8n workflow JSON template |
| `workflow-airflow.j2` | Airflow DAG template |
| `workflow-prefect.j2` | Prefect flow template |
| `prompt-template.j2` | Base prompt template with variables |
| `llm-chain.j2` | LCEL chain template |
| `dockerfile.j2` | Dockerfile template for deployment |
| `docker-compose.j2` | Docker Compose template |
| `monitoring-dashboard.j2` | Grafana/Prometheus dashboard template |
| `variables.yaml` | Template variable definitions and defaults |

## Template Standards

- Use consistent variable naming: `{{ variable_name }}`
- Document all variables in `variables.yaml`
- Provide example rendered output
- Test with edge cases

## Variable Documentation

```yaml
# variables.yaml
workflow_name:
  description: "Name of the workflow"
  type: "string"
  required: true
  example: "invoice_processing"

orchestration_platform:
  description: "Target platform"
  type: "string"
  required: true
  default: "prefect"
  example: "n8n"

llm_model:
  description: "LLM model to use"
  type: "string"
  required: true
  default: "gpt-4-turbo-preview"
  example: "gpt-4o"

trigger_type:
  description: "Workflow trigger type"
  type: "string"
  required: true
  default: "webhook"
  example: "schedule"

token_budget:
  description: "Max tokens per execution"
  type: "integer"
  required: true
  default: 50000
  example: 100000
```

## Usage

Templates are referenced in SKILL.md `output_standards.expected_deliverables` and used in workflow step 6 (execution) and step 10 (delivery).

## Testing

```bash
pip install jinja2 pyyaml
python -c "
from jinja2 import Environment, FileSystemLoader
import yaml
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('workflow-prefect.j2')
with open('variables.yaml') as f:
    vars = yaml.safe_load(f)
print(template.render(**vars))
"
```