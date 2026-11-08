# Universal Skill Specification

Version: 1.0.0
Status: Draft
Last Updated: 2026-11-08

---

## Overview

This document defines the universal specification that every skill in the AI Agent Skill Library must follow. It ensures consistency, quality, and interoperability across all skills and platforms.

---

## 1. Identity

Every skill must have a unique identity block at the top of `SKILL.md`:

```yaml
identity:
  name: "Human-readable skill name"
  id: "kebab-case-unique-id"
  version: "1.0.0"                    # Semantic versioning
  description: "One-sentence description"
  professional_role: "Professional Role Title"
  category: "category-name"            # From the 12 categories
  target_users:                        # Array of target user types
    - "freelancers"
    - "developers"
    - "enterprises"
  required_capabilities:               # Capabilities this skill provides
    - "capability-1"
    - "capability-2"
  tags:                                # Searchable tags
    - "tag1"
    - "tag2"
  platforms:                           # Supported platforms
    - "claude"
    - "opencode"
    - "cursor"
    - "github-copilot"
    - "generic"
  maturity: "alpha"                    # alpha, beta, stable, deprecated
  license: "MIT"
  dependencies:                        # Other skills this depends on
    - "dependency-skill-id"
```

---

## 2. Role Definition

Defines the professional persona the agent adopts:

```yaml
role_definition:
  professional_identity: "Title and professional description"
  expertise_areas:
    - "Area 1"
    - "Area 2"
  responsibilities:
    - "Primary responsibility 1"
    - "Primary responsibility 2"
  scope_of_work: "What this skill covers and does not cover"
  limitations:
    - "Limitation 1 (e.g., no legal advice)"
    - "Limitation 2 (e.g., requires human review for X)"
  expected_behavior:
    tone: "professional|collaborative|authoritative|educational"
    communication_style: "concise|detailed|step-by-step"
    decision_making: "evidence-based|best-practice|creative"
```

---

## 3. Core Competencies

Specific professional capabilities this skill provides. Each competency must be measurable.

```yaml
core_competencies:
  - id: "competency-id"
    name: "Competency Name"
    description: "What this competency enables"
    proficiency_level: "expert|advanced|intermediate|basic"
    measurable_outcomes:
      - "Outcome 1"
      - "Outcome 2"
    prerequisites:
      - "Prerequisite knowledge or skill"
```

---

## 4. Knowledge Base

Structured domain knowledge. Must be accurate, sourced, and relevant.

```yaml
knowledge_base:
  fundamental_concepts:
    - concept: "Concept Name"
      description: "Clear explanation"
      references:
        - "Authoritative source 1"
        - "Authoritative source 2"
  
  industry_terminology:
    - term: "Term"
      definition: "Precise definition"
      context: "When/how it's used"
  
  professional_methodologies:
    - name: "Methodology Name"
      description: "How it works"
      steps:
        - "Step 1"
        - "Step 2"
      when_to_use: "Conditions for application"
      limitations: "Known limitations"
  
  industry_standards:
    - standard: "Standard Name (e.g., ISO 27001, GDPR, WCAG 2.1)"
      relevance: "How it applies to this skill"
      compliance_notes: "Key compliance points"
  
  best_practices:
    - practice: "Practice Name"
      description: "What to do"
      rationale: "Why it matters"
      anti_pattern: "What to avoid"
  
  common_mistakes:
    - mistake: "Mistake description"
      consequence: "What goes wrong"
      prevention: "How to avoid"
  
  practical_references:
    - title: "Reference Title"
      type: "documentation|tool|template|case-study|regulation"
      url: "https://..."
      description: "Why this reference is valuable"
```

**Critical**: Never fabricate standards, citations, API behavior, or technical documentation. All references must be verifiable.

---

## 5. Workflow

The complete working procedure. All 10 steps are mandatory.

```yaml
workflow:
  step_1_request_analysis:
    description: "Analyze the user's request for intent, scope, and constraints"
    inputs: ["User request", "Context"]
    outputs: ["Structured requirements", "Identified gaps"]
    validation: "Checklist for complete analysis"
  
  step_2_requirement_clarification:
    description: "Clarify ambiguous requirements with targeted questions"
    inputs: ["Structured requirements", "Identified gaps"]
    outputs: ["Clarified requirements", "Assumptions documented"]
    validation: "All critical ambiguities resolved"
  
  step_3_context_gathering:
    description: "Gather relevant context from files, docs, environment"
    inputs: ["Clarified requirements"]
    outputs: ["Context package", "Missing context identified"]
    validation: "Sufficient context for planning"
  
  step_4_research:
    description: "Research best practices, standards, alternatives"
    inputs: ["Context package", "Requirements"]
    outputs: ["Research findings", "Options analysis"]
    validation: "Evidence-based recommendations"
  
  step_5_planning:
    description: "Create detailed execution plan"
    inputs: ["Research findings", "Requirements"]
    outputs: ["Execution plan", "Resource requirements", "Risk assessment"]
    validation: "Plan is complete, feasible, and traceable to requirements"
  
  step_6_task_execution:
    description: "Execute the plan with quality checkpoints"
    inputs: ["Execution plan"]
    outputs: ["Work products", "Execution log"]
    validation: "Checkpoints passed"
  
  step_7_validation:
    description: "Validate outputs against requirements"
    inputs: ["Work products", "Requirements"]
    outputs: ["Validation report", "Defects found"]
    validation: "All acceptance criteria met"
  
  step_8_quality_review:
    description: "Review for professional standards, best practices"
    inputs: ["Work products", "Validation report"]
    outputs: ["Quality assessment", "Improvement suggestions"]
    validation: "Meets quality threshold (≥90/100)"
  
  step_9_error_correction:
    description: "Fix identified issues and re-validate"
    inputs: ["Defects", "Improvement suggestions"]
    outputs: ["Corrected work products", "Re-validation report"]
    validation: "No critical defects remain"
  
  step_10_final_delivery:
    description: "Package and deliver final outputs"
    inputs: ["Corrected work products"]
    outputs: ["Final deliverables", "Delivery documentation"]
    validation: "Complete, documented, ready for use"
```

### Workflow Execution Rules

1. **Sequential by default** - Steps 1-5 must complete before step 6
2. **Iterative loops allowed** - Steps 7-9 can loop back to 6
3. **No skipping** - All steps must have documented output
4. **Evidence required** - Each step produces verifiable artifacts

---

## 6. Tools & Integrations

```yaml
tools_integrations:
  supported_tools:
    - tool: "tool-name"
      type: "cli|api|mcp|builtin"
      purpose: "What it's used for"
      required: true|false
      version: "minimum version"
  
  required_tools:
    - "tool-that-must-be-available"
  
  optional_tools:
    - tool: "nice-to-have-tool"
      fallback: "Alternative approach if unavailable"
  
  api_integrations:
    - api: "API Name"
      auth_type: "oauth|apikey|bearer|none"
      scopes: ["required", "scopes"]
      rate_limits: "Documented limits"
      fallback: "Offline/degraded mode"
  
  mcp_integrations:
    - server: "MCP Server Name"
      capabilities: ["capability1", "capability2"]
      required: true|false
  
  tool_prerequisites:
    - tool: "tool-name"
      setup: "Setup instructions"
      verification: "How to verify it works"
  
  authentication_requirements:
    - service: "Service name"
      credentials_needed: ["API_KEY", "SECRET"]
      storage: "env-var|vault|config-file"
      rotation: "Rotation policy"
  
  fallback_procedures:
    - scenario: "Tool unavailable / API down / Auth failed"
      procedure: "Step-by-step fallback"
      degraded_capability: "What still works"
```

**Critical**: Never claim a tool is available unless actually available in the execution environment.

---

## 7. Output Standards

```yaml
output_standards:
  expected_deliverables:
    - name: "Deliverable Name"
      format: "markdown|json|yaml|code|document|spreadsheet"
      structure: "Defined structure or schema reference"
      required: true|false
  
  output_structure:
    # Example for a report deliverable
    report:
      sections:
        - "Executive Summary"
        - "Methodology"
        - "Findings"
        - "Recommendations"
        - "Appendices"
      formatting: "Consistent heading levels, tables, code blocks"
  
  documentation_requirements:
    - "Inline documentation for all public interfaces"
    - "Usage examples for each major feature"
    - "Architecture decision records for significant choices"
    - "Troubleshooting guide for common issues"
  
  quality_expectations:
    accuracy: "Factual correctness verified against sources"
    completeness: "All requirements addressed"
    consistency: "Terminology, formatting, style consistent"
    usability: "Clear, actionable, appropriate detail level"
  
  acceptance_criteria:
    - criterion: "Specific, measurable criterion"
      verification_method: "How to verify"
      priority: "critical|high|medium|low"
```

---

## 8. Self-Review Protocol

Every skill execution must complete this review:

```yaml
self_review:
  steps:
    - step: "Review original user requirements"
      check: "All explicit requirements addressed?"
    
    - step: "Compare deliverables against requirements"
      check: "Gap analysis - nothing missing?"
    
    - step: "Identify missing requirements"
      check: "Implicit needs considered?"
    
    - step: "Inspect technical and logical errors"
      check: "Code/logic correctness verified?"
    
    - step: "Verify accuracy"
      check: "Facts, citations, calculations correct?"
    
    - step: "Validate output format"
      check: "Matches specified structure?"
    
    - step: "Check security constraints"
      check: "No credentials exposed, inputs validated?"
    
    - step: "Correct issues where possible"
      action: "Fix and re-verify"
    
    - step: "Execute validation again"
      check: "All checks pass?"
    
    - step: "Report final verification status"
      output: "PASS|FAIL with evidence"
  
  principle: "ANALYZE → EXECUTE → REVIEW → DETECT → FIX → RETEST → DELIVER"
  no_fake_completion: "TODO placeholders, skipped tests, stubs = incomplete"
  bounded_retries: "Max 3 correction cycles, then escalate/report blocker"
```

---

## 9. Metadata Schema Reference

See `core/metadata-schema/skill-metadata.schema.json` for the complete JSON Schema.

### Required Fields
- `identity` (all sub-fields)
- `role_definition` (all sub-fields)
- `core_competencies` (at least 1)
- `knowledge_base` (all sections, can be empty arrays with note)
- `workflow` (all 10 steps)
- `tools_integrations` (all sub-sections)
- `output_standards` (all sub-sections)
- `self_review` (protocol reference)

### Optional Fields
- `examples` - Reference to examples/ directory
- `tests` - Reference to tests/ directory
- `quality` - Reference to quality/ directory
- `changelog` - Reference to CHANGELOG.md

---

## 10. Versioning & Compatibility

- **Skill Version**: Semantic Versioning (MAJOR.MINOR.PATCH)
- **Spec Version**: This document version
- **Breaking Changes**: MAJOR version increment
- **Backward Compatibility**: Maintained within MAJOR version
- **Deprecation**: 2 minor versions notice before removal

---

## Compliance Checklist

Before releasing a skill, verify:

- [ ] Identity block complete and unique
- [ ] Role definition matches professional standards
- [ ] Core competencies are specific and measurable
- [ ] Knowledge base is accurate and sourced (no fabrication)
- [ ] All 10 workflow steps defined with inputs/outputs/validation
- [ ] Tools integrations reflect actual availability
- [ ] Output standards are concrete and verifiable
- [ ] Self-review protocol implemented
- [ ] Metadata validates against schema
- [ ] Examples are executable or clearly illustrative
- [ ] Tests exist and pass (when framework available)
- [ ] Security review passed
- [ ] Documentation complete
- [ ] Quality score ≥ 90/100

---

*This specification is the contract for all skills in the library. Deviations require architecture review approval.*