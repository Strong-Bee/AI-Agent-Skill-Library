# Tests

This directory contains validation tests for the Prompt Engineer skill.

## Structure

```
tests/
├── unit/
│   ├── test_prompt_templates.py       # Test prompt rendering
│   ├── test_schema_validation.py      # Test Pydantic/JSON schema validation
│   ├── test_few_shot_formatting.py    # Test few-shot example formatting
│   ├── test_variable_substitution.py  # Test template variable substitution
│   └── test_config_loading.py         # Test configuration parsing
├── integration/
│   ├── test_openai_integration.py     # OpenAI API integration
│   ├── test_anthropic_integration.py  # Anthropic API integration
│   ├── test_google_integration.py     # Google AI API integration
│   ├── test_dspy_integration.py       # DSPy optimization integration
│   ├── test_promptlayer_integration.py # PromptLayer versioning
│   └── test_langsmith_integration.py  # LangSmith evaluation
├── acceptance/
│   ├── test_classification_prompt.py  # Classification prompt end-to-end
│   ├── test_generation_prompt.py      # Generation prompt end-to-end
│   ├── test_reasoning_prompt.py       # Reasoning prompt end-to-end
│   ├── test_extraction_prompt.py      # Extraction prompt end-to-end
│   ├── test_optimization_pipeline.py  # Optimization pipeline
│   └── test_multi_model_portability.py # Cross-model portability
├── regression/
│   └── test_issue_XXX.py              # Tests for fixed issues
├── security/
│   ├── test_prompt_injection.py       # Prompt injection resistance
│   ├── test_pii_handling.py           # PII detection and handling
│   ├── test_output_validation.py      # Output validation enforcement
│   └── test_input_sanitization.py     # Input sanitization
├── evaluation/
│   ├── golden_set.jsonl               # Ground truth test cases
│   ├── test_llm_judge.py              # LLM-as-judge evaluation
│   ├── test_metrics.py                # Quantitative metrics (accuracy, F1, etc.)
│   └── test_statistical_significance.py # Statistical testing
├── fixtures/
│   ├── sample_inputs/                 # Test input data
│   ├── expected_outputs/              # Expected results
│   └── mock_responses/                # Mocked API responses
├── conftest.py                        # Shared test configuration
└── pytest.ini                         # Pytest configuration
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
pytest tests/integration/ -v --platform claude-code
pytest tests/acceptance/ -v

# With coverage
pytest tests/ --cov=prompts --cov-report=html

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
2. Use descriptive names: `test_prompt_achieves_90_percent_accuracy_on_sentiment`
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