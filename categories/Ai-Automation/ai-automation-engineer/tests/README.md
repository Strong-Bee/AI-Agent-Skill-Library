# Tests

This directory contains validation tests for the AI Automation Engineer skill.

## Structure

```
tests/
├── unit/
│   ├── test_llm_chains.py           # Test LCEL chain compilation
│   ├── test_prompt_templates.py     # Test prompt rendering
│   ├── test_schema_validation.py    # Test Pydantic/JSON schema validation
│   ├── test_cost_calculations.py    # Test token counting and cost
│   └── test_config_loading.py       # Test configuration parsing
├── integration/
│   ├── test_n8n_integration.py      # n8n workflow execution
│   ├── test_airflow_integration.py  # Airflow DAG execution
│   ├── test_prefect_integration.py  # Prefect flow execution
│   ├── test_openai_integration.py   # OpenAI API integration
│   ├── test_anthropic_integration.py # Anthropic API integration
│   └── test_vector_store.py         # Vector DB integration
├── acceptance/
│   ├── test_basic_workflow.py       # Basic workflow end-to-end
│   ├── test_multi_step_workflow.py  # Multi-step with HITL
│   ├── test_event_driven.py         # Event-triggered workflow
│   ├── test_batch_workflow.py       # Scheduled workflow
│   ├── test_error_handling.py       # Retries, compensation, alerting
│   └── test_cost_budget.py          # Token budget enforcement
├── regression/
│   └── test_issue_XXX.py            # Tests for fixed issues
├── security/
│   ├── test_input_validation.py     # Input validation tests
│   ├── test_credential_handling.py  # Credential protection tests
│   ├── test_webhook_security.py     # Webhook signature verification
│   └── test_prompt_injection.py     # Prompt injection resistance
├── evaluation/
│   ├── golden_set.jsonl             # Ground truth test cases
│   ├── test_llm_judge.py            # LLM-as-judge evaluation
│   └── test_metrics.py              # Quantitative metrics
├── fixtures/
│   ├── sample_inputs/               # Test input data
│   ├── expected_outputs/            # Expected results
│   └── mock_responses/              # Mocked API responses
├── conftest.py                      # Shared test configuration
└── pytest.ini                       # Pytest configuration
```

## Test Types & Requirements

| Type | Coverage Target | Required For |
|------|-----------------|--------------|
| Unit | ≥ 80% (executable code) | All skills |
| Integration | 100% workflow steps | All skills |
| Acceptance | 100% criteria | All skills |
| Regression | 100% fixed issues | All skills |
| Security | 100% trust boundaries | Medium+ risk |

## Running Tests

```bash
# All tests
pytest tests/ -v

# Specific type
pytest tests/unit/ -v
pytest tests/integration/ -v --platform prefect
pytest tests/acceptance/ -v

# With coverage
pytest tests/ --cov=workflows --cov-report=html

# Security tests
pytest tests/security/ -v

# Evaluation tests
pytest tests/evaluation/ -v
```

## Test Data Management

- **Fixtures**: Realistic but anonymized, version-controlled
- **Factories**: For complex object generation (use `factory_boy`)
- **Snapshots**: For output format validation (use `pytest-snapshot`)
- **Contracts**: For API integration testing (use `schemathesis`)

## CI/CD Integration

Tests run automatically on:
- Pre-commit (fast subset: unit tests only)
- Pull request (full suite: unit + integration + acceptance)
- Merge to main (full + security + evaluation)
- Scheduled (regression, compatibility)

## Platform Test Harnesses

- **Claude Code**: Custom MCP test server or CLI automation
- **OpenCode**: CLI automation with JSON I/O
- **Generic**: Markdown parser + schema validator

## Writing Tests

1. Test one thing per test case
2. Use descriptive names: `test_workflow_compensates_on_downstream_failure`
3. Arrange-Act-Assert structure
4. Mock external dependencies (APIs, databases)
5. Document test purpose in docstring

## Test Configuration

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers --tb=short
markers =
    unit: Unit tests
    integration: Integration tests
    acceptance: Acceptance tests
    security: Security tests
    evaluation: Evaluation tests
    slow: Slow tests (>10s)
filterwarnings =
    ignore::DeprecationWarning
```