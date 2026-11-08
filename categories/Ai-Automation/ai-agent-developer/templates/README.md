# Templates

This directory contains reusable templates for the AI Agent Developer skill.

## Structure

| File | Purpose |
|------|---------|
| `agent-graph.j2` | Jinja2 template for LangGraph agent definition |
| `tool-definition.j2` | Tool schema template with descriptions |
| `prompt-template.j2` | Base prompt template with variables |
| `evaluation-case.j2` | Evaluation test case template |
| `dockerfile.j2` | Dockerfile template for deployment |
| `docker-compose.j2` | Docker Compose template |
| `variables.yaml` | Template variable definitions and defaults |

## Template Standards

- Use consistent variable naming: `{{ variable_name }}`
- Document all variables in `variables.yaml`
- Provide example rendered output
- Test with edge cases

## Variable Documentation

```yaml
# variables.yaml
agent_name:
  description: "Name of the agent"
  type: "string"
  required: true
  example: "research_assistant"

llm_model:
  description: "LLM model to use"
  type: "string"
  required: true
  default: "gpt-4-turbo-preview"
  example: "gpt-4o"

tools_list:
  description: "List of enabled tools"
  type: "array"
  required: true
  default: ["web_search", "file_operations"]
  example: ["web_search", "file_operations", "code_execution"]

max_iterations:
  description: "Maximum agent loop iterations"
  type: "integer"
  required: true
  default: 10
  example: 15
```

## Usage

Templates are referenced in SKILL.md `output_standards.expected_deliverables` and used in workflow step 6 (execution) and step 10 (delivery).

## Testing

Test templates render correctly:
```bash
# Example with Jinja2
pip install jinja2
python -c "
from jinja2 import Environment, FileSystemLoader
import yaml
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('agent-graph.j2')
with open('variables.yaml') as f:
    vars = yaml.safe_load(f)
print(template.render(**vars))
"
```