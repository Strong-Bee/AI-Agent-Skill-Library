# Tests

This directory contains validation tests for the AI Agent Developer skill.

## Structure

```
tests/
├── unit/
│   ├── test_agent_graph.py          # Test LangGraph agent compilation
│   ├── test_tool_schemas.py         # Test tool input/output schemas
│   ├── test_prompt_templates.py     # Test prompt rendering
│   ├── test_memory_operations.py    # Test memory read/write
│   └── test_config_loading.py       # Test configuration parsing
├── integration/
│   ├── test_claude_code.py          # Claude Code integration tests
│   ├── test_opencode.py             # OpenCode integration tests
│   ├── test_generic.py              # Generic platform tests
│   ├── test_openai_integration.py   # OpenAI API integration
│   ├── test_anthropic_integration.py # Anthropic API integration
│   └── test_vector_store.py         # Vector DB integration
├── acceptance/
│   ├── test_basic_agent.py          # Basic agent end-to-end
│   ├── test_multi_agent.py          # Multi-agent orchestration
│   ├── test_tool_fallbacks.py       # Tool failure recovery
│   ├── test_human_in_loop.py        # HITL workflow
│   └── test_quality_gates.py        # Quality threshold validation
├── regression/
│   └── test_issue_XXX.py            # Tests for fixed issues
├── security/
│   ├── test_input_validation.py     # Input validation tests
│   ├── test_credential_handling.py  # Credential protection tests
│   ├── test_tool_permissions.py     # Tool authorization tests
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
pytest tests/integration/ -v --platform claude-code
pytest tests/acceptance/ -v

# With coverage
pytest tests/ --cov=agents --cov-report=html

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
2. Use descriptive names: `test_agent_terminates_on_max_iterations`
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