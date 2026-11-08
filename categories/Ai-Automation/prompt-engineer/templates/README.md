# Templates

This directory contains reusable templates for the Prompt Engineer skill.

## Structure

| File | Purpose |
|------|---------|
| `prompt-template.j2` | Base prompt template with variables |
| `few-shot-template.j2` | Few-shot example template |
| `cot-template.j2` | Chain-of-Thought template |
| `structured-output.j2` | JSON Schema / Pydantic output template |
| `evaluation-case.j2` | Evaluation test case template |
| `optimization-log.j2` | Optimization iteration log template |
| `deployment-config.j2` | CI/CD deployment configuration template |
| `variables.yaml` | Template variable definitions and defaults |

## Template Standards

- Use consistent variable naming: `{{ variable_name }}`
- Document all variables in `variables.yaml`
- Provide example rendered output
- Test with edge cases

## Variable Documentation

```yaml
# variables.yaml
task_type:
  description: "Type of task (classification, generation, reasoning, extraction)"
  type: "string"
  required: true
  example: "classification"

model:
  description: "Target model"
  type: "string"
  required: true
  default: "gpt-4-turbo-preview"
  example: "gpt-4o"

examples:
  description: "Few-shot examples"
  type: "array"
  required: true
  default: []
  example: [{"input": "text", "output": "label"}]

output_schema:
  description: "JSON Schema for structured output"
  type: "object"
  required: false
  example: {"type": "object", "properties": {"label": {"type": "string"}}}
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
template = env.get_template('prompt-template.j2')
with open('variables.yaml') as f:
    vars = yaml.safe_load(f)
print(template.render(**vars))
"
```