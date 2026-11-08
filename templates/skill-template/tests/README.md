# Tests

This directory contains validation tests for this skill.

## Structure

```
tests/
├── unit/
│   ├── test_workflow_steps.py      # Test individual workflow steps
│   ├── test_competencies.py        # Test competency implementations
│   └── test_tool_integrations.py   # Test tool parameter building
├── integration/
│   ├── test_claude_code.py         # Claude Code integration tests
│   ├── test_opencode.py            # OpenCode integration tests
│   └── test_generic.py             # Generic platform tests
├── acceptance/
│   ├── test_deliverables.py        # Validate output format/quality
│   └── test_quality_thresholds.py  # Verify quality gates
├── regression/
│   └── test_issue_XXX.py           # Tests for fixed issues
├── security/
│   ├── test_input_validation.py    # Input validation tests
│   └── test_credential_handling.py # Credential protection tests
├── fixtures/
│   ├── sample_inputs/              # Test input data
│   └── expected_outputs/           # Expected results
└── conftest.py                     # Shared test configuration
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
./run-tests.sh

# Specific type
./run-tests.sh --type unit
./run-tests.sh --type integration --platform claude-code

# With coverage
./run-tests.sh --coverage
```

## Test Data Management

- **Fixtures**: Realistic but anonymized, version-controlled
- **Factories**: For complex object generation
- **Snapshots**: For output format validation
- **Contracts**: For API integration testing

## CI/CD Integration

Tests run automatically on:
- Pre-commit (fast subset)
- Pull request (full suite)
- Merge to main (full + security)
- Scheduled (regression, compatibility)

## Platform Test Harnesses

- **Claude Code**: Custom MCP test server or CLI automation
- **OpenCode**: CLI automation with JSON I/O
- **Generic**: Markdown parser + schema validator

## Writing Tests

1. Test one thing per test case
2. Use descriptive names: `test_workflow_step_3_gathers_context_from_files`
3. Arrange-Act-Assert structure
4. Mock external dependencies
5. Document test purpose in docstring