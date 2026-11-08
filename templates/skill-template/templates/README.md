# Templates

This directory contains reusable templates for this skill.

## Structure

| File | Purpose |
|------|---------|
| `template-name.j2` | Jinja2 template (or other templating engine) |
| `template-name.md` | Markdown template |
| `template-name.yaml` | YAML template |
| `variables.yaml` | Template variable definitions and defaults |

## Template Standards

- Use consistent variable naming: `{{ variable_name }}`
- Document all variables in `variables.yaml`
- Provide example rendered output
- Test with edge cases

## Variable Documentation

```yaml
# variables.yaml
variable_name:
  description: "What this variable represents"
  type: "string|number|boolean|array|object"
  required: true|false
  default: "default value"
  example: "example value"
```

## Usage

Templates are referenced in SKILL.md `output_standards.expected_deliverables` and used in workflow step 6 (execution) and step 10 (delivery).

## Testing

Test templates render correctly:
```bash
# Example with Jinja2
jinja2 template.j2 variables.yaml --format=json
```