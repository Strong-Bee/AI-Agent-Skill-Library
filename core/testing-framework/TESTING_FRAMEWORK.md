# Testing Framework

Version: 1.0.0
Status: Draft
Last Updated: 2026-11-08

---

## Overview

This framework defines the testing standards, test types, and validation approaches for skills in the AI Agent Skill Library.

---

## 1. Test Types

### 1.1 Unit Tests (Skill Logic)
Test individual functions, workflows, and components in isolation.

```yaml
unit_tests:
  scope: "Individual functions, competency implementations, workflow steps"
  tools: "Language-appropriate (pytest, jest, cargo test, etc.)"
  location: "skills/.../tests/unit/"
  naming: "test_<function>_<scenario>.py"
  coverage_target: "≥ 80% for executable code"
  examples:
    - "Test competency calculation logic"
    - "Test workflow step validation"
    - "Test tool integration parameter building"
```

### 1.2 Integration Tests (Platform + Skill)
Test skill behavior on target platforms.

```yaml
integration_tests:
  scope: "Skill execution on Claude Code, OpenCode, Cursor, etc."
  tools: "Platform-specific test harnesses"
  location: "skills/.../tests/integration/"
  scenarios:
    - "Skill loads correctly"
    - "Metadata validates"
    - "Tools available and working"
    - "Workflow executes end-to-end"
    - "Output matches specifications"
```

### 1.3 Acceptance Tests (Requirements Validation)
Test that deliverables meet acceptance criteria.

```yaml
acceptance_tests:
  scope: "User requirements → deliverables"
  tools: "Custom validators, schema checkers"
  location: "skills/.../tests/acceptance/"
  criteria_from: "output_standards.acceptance_criteria in SKILL.md"
  examples:
    - "Deliverable format matches schema"
    - "All required sections present"
    - "Quality thresholds met"
```

### 1.4 Regression Tests
Prevent re-introduction of fixed issues.

```yaml
regression_tests:
  scope: "Previously fixed bugs, known edge cases"
  location: "skills/.../tests/regression/"
  trigger: "Added when bug fixed"
  maintenance: "Review quarterly, remove if fixed upstream"
```

### 1.5 Security Tests
Validate security posture.

```yaml
security_tests:
  scope: "Input validation, auth handling, credential protection"
  tools: "Custom + automated scanners"
  location: "skills/.../tests/security/"
  required_for: "risk_level: medium|high|critical"
```

---

## 2. Test Structure

```
skills/category/skill-name/
└── tests/
    ├── unit/
    │   ├── test_workflow_steps.py
    │   ├── test_competencies.py
    │   └── test_tool_integrations.py
    ├── integration/
    │   ├── test_claude_code.py
    │   ├── test_opencode.py
    │   └── test_generic.py
    ├── acceptance/
    │   ├── test_deliverables.py
    │   └── test_quality_thresholds.py
    ├── regression/
    │   └── test_issue_XXX.py
    ├── security/
    │   ├── test_input_validation.py
    │   └── test_credential_handling.py
    ├── fixtures/
    │   ├── sample_inputs/
    │   └── expected_outputs/
    └── conftest.py (or equivalent)
```

---

## 3. Test Execution

### Local Development

```bash
# Run all tests for a skill
cd categories/ai-automation/ai-agent-developer
./run-tests.sh

# Run specific test type
./run-tests.sh --type unit
./run-tests.sh --type integration --platform claude-code

# Run with coverage
./run-tests.sh --coverage
```

### CI/CD Pipeline

```yaml
ci_pipeline:
  stages:
    - name: "Metadata Validation"
      script: "validate-metadata.sh"
      artifacts: "validation-report.json"
    
    - name: "Unit Tests"
      script: "run-unit-tests.sh"
      coverage: true
      artifacts: "coverage.xml"
    
    - name: "Integration Tests"
      script: "run-integration-tests.sh"
      matrix:
        platform: ["claude-code", "opencode", "generic"]
      artifacts: "integration-results.xml"
    
    - name: "Acceptance Tests"
      script: "run-acceptance-tests.sh"
      artifacts: "acceptance-report.json"
    
    - name: "Security Tests"
      script: "run-security-tests.sh"
      condition: "risk_level in [medium, high, critical]"
    
    - name: "Quality Evaluation"
      script: "evaluate-quality.py"
      artifacts: "scorecard.json"
      gate: "score >= 90"
```

---

## 4. Test Data Management

### Fixtures

```yaml
fixtures:
  principles:
    - "Realistic but anonymized"
    - "Cover happy path + edge cases"
    - "Version controlled with tests"
    - "Documented in fixtures/README.md"
  
  types:
    - "Sample user requests"
    - "Expected intermediate outputs"
    - "Final deliverable examples"
    - "Error scenarios"
    - "Platform-specific contexts"
```

### Test Data Generation

```yaml
generation:
  - "Use factories for complex objects"
  - "Property-based testing for validation logic"
  - "Snapshot testing for output formats"
  - "Contract testing for API integrations"
```

---

## 5. Platform Testing

### Claude Code Testing

```yaml
claude_code:
  test_harness: "Custom MCP test server or CLI automation"
  capabilities_tested:
    - "Skill discovery and loading"
    - "Tool permission handling"
    - "MCP server integration"
    - "File system operations"
    - "Long-running workflow handling"
```

### OpenCode Testing

```yaml
opencode:
  test_harness: "OpenCode CLI automation"
  capabilities_tested:
    - "Skill manifest parsing"
    - "Tool execution"
    - "Configuration handling"
```

### Cursor Testing

```yaml
cursor:
  test_harness: "Cursor extension test runner"
  capabilities_tested:
    - "Skill activation"
    - "Context passing"
    - "Output rendering"
```

### Generic/Markdown Testing

```yaml
generic:
  test_harness: "Markdown parser + schema validator"
  capabilities_tested:
    - "SKILL.md parsing"
    - "Metadata extraction"
    - "Workflow step extraction"
    - "Knowledge base querying"
```

---

## 6. Test Automation Tools

### Validation Scripts (to be created)

```
tools/validators/
├── validate-metadata.py      # JSON Schema validation
├── validate-structure.sh     # Directory structure check
├── validate-markdown.sh      # Markdown linting
├── validate-links.py         # Link checking
├── validate-catalog.py       # Catalog sync check
├── check-duplicates.py       # Duplicate detection
└── run-all-validations.sh    # Orchestrator
```

### Evaluation Tools

```
tools/evaluation/
├── evaluate-skill.py         # Quality scoring
├── scorecard-template.md     # Manual review template
├── security-scan.sh          # Security checks
└── generate-report.py        # Consolidated report
```

### Test Runners

```
tools/testing/
├── run-skill-tests.sh        # Main entry point
├── test-harness-claude.py    # Claude Code harness
├── test-harness-generic.py   # Generic harness
└── fixtures/                 # Shared test fixtures
```

---

## 7. Test Coverage Requirements

| Test Type | Minimum Coverage | Required For |
|-----------|------------------|--------------|
| Unit | 80% (executable code) | All skills |
| Integration | 100% workflow steps | All skills |
| Acceptance | 100% criteria | All skills |
| Regression | 100% fixed issues | All skills |
| Security | 100% trust boundaries | Medium+ risk |

---

## 8. Test Reporting

### Test Result Format

```json
{
  "skill_id": "ai-agent-developer",
  "timestamp": "2026-11-08T10:00:00Z",
  "test_run_id": "uuid",
  "results": {
    "unit": { "passed": 45, "failed": 0, "skipped": 2, "coverage": 87.5 },
    "integration": { "passed": 12, "failed": 0, "skipped": 0 },
    "acceptance": { "passed": 8, "failed": 0, "skipped": 0 },
    "regression": { "passed": 3, "failed": 0, "skipped": 0 },
    "security": { "passed": 5, "failed": 0, "skipped": 0 }
  },
  "overall": "pass",
  "duration_seconds": 120
}
```

### Quality Gate Integration

```yaml
quality_gates:
  unit_tests: "pass AND coverage >= 80%"
  integration_tests: "pass"
  acceptance_tests: "pass"
  security_tests: "pass (when required)"
  quality_score: ">= 90"
```

---

## 9. Continuous Testing

### Pre-commit Hooks

```yaml
pre_commit:
  - "Metadata validation"
  - "Markdown linting"
  - "Unit tests (fast subset)"
  - "Structure validation"
```

### Scheduled Runs

```yaml
scheduled:
  daily:
    - "Full test suite on main branch"
    - "Security scans"
  weekly:
    - "Integration tests on all platforms"
    - "Regression test full suite"
  monthly:
    - "Quality score trending"
    - "Test coverage analysis"
    - "Flaky test detection"
```

---

## 10. Test Maintenance

- **Review tests** with every skill update
- **Remove obsolete tests** when features change
- **Update fixtures** when schemas change
- **Document test purpose** in code comments
- **Track flaky tests** and fix or quarantine

---

*This framework ensures skills are thoroughly tested and reliable across all supported platforms.*