# Quality Assurance Framework

Version: 1.0.0
Status: Draft
Last Updated: 2026-11-08

---

## Overview

This framework defines the quality assurance standards, evaluation methodology, and automated validation for all skills in the AI Agent Skill Library.

---

## 1. Quality Scoring System

### Weighted Criteria (Total: 100%)

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Accuracy** | 20% | Factual correctness, valid references, no fabrication |
| **Professional Expertise** | 20% | Depth and relevance to the profession |
| **Workflow Completeness** | 15% | All 10 steps implemented with inputs/outputs/validation |
| **Output Quality** | 15% | Deliverables meet professional standards |
| **Best Practices** | 10% | Follows industry standards and conventions |
| **Security** | 10% | Safe execution, no credential exposure, input validation |
| **Documentation** | 5% | Clear, complete, well-structured |
| **Efficiency** | 5% | Practical, not over-engineered |

### Scoring Scale (per criterion)

| Score | Level | Description |
|-------|-------|-------------|
| 0-20 | Critical | Fundamental failures, unusable |
| 21-40 | Poor | Major gaps, significant issues |
| 41-60 | Fair | Basic functionality, notable gaps |
| 61-80 | Good | Solid implementation, minor issues |
| 81-100 | Excellent | Professional grade, production-ready |

### Minimum Release Threshold

- **Overall Score**: ≥ 90/100
- **No criterion below**: 70/100
- **No critical defects** unresolved

---

## 2. Evaluation Process

### Automated Checks (Pre-review)

```yaml
automated_checks:
  metadata_validation:
    tool: "jsonschema validator"
    schema: "core/metadata-schema/skill-metadata.schema.json"
    fail_on: "any validation error"
  
  structure_validation:
    tool: "custom script"
    checks:
      - "All required directories exist"
      - "Required files present (SKILL.md, README.md, CHANGELOG.md)"
      - "No empty required directories without justification"
  
  markdown_validation:
    tool: "markdownlint"
    config: ".markdownlint.json"
    fail_on: "errors (warnings allowed)"
  
  link_checking:
    tool: "lychee or similar"
    scope: "internal and external links in SKILL.md, README.md"
    fail_on: "broken internal links; external warnings allowed"
  
  duplicate_detection:
    tool: "custom script"
    checks:
      - "Duplicate skill IDs across library"
      - "Duplicate competency IDs within skill"
      - "Substantially similar content"
  
  catalog_sync:
    tool: "custom script"
    check: "catalog.json matches actual skill directories"
```

### Manual Review (Peer Review)

```yaml
manual_review:
  reviewers_required: 1  # minimum
  review_criteria:
    - "Accuracy of knowledge base (spot-check references)"
    - "Professional expertise depth"
    - "Workflow practicality and completeness"
    - "Output quality matches professional standards"
    - "Best practices alignment"
    - "Security posture"
    - "Documentation clarity"
    - "Efficiency of approach"
  evidence_required: "Reviewer must cite specific examples for scores < 80"
```

### Security Review (For Skills with External Integrations)

```yaml
security_review:
  required_for:
    - "API integrations"
    - "MCP integrations"
    - "File system write operations"
    - "Code execution capabilities"
    - "Credential handling"
  checks:
    - "No hardcoded secrets"
    - "Input validation at trust boundaries"
    - "Least privilege principle"
    - "Fallback procedures documented"
    - "Authorization requirements clear"
```

---

## 3. Quality Gates

### Gate 1: Structure Gate (Automated)
- All required files/directories exist
- Metadata validates against schema
- No critical markdown errors
- **Result**: PASS/FAIL

### Gate 2: Content Gate (Automated + Manual)
- Knowledge base accuracy spot-check
- Workflow all 10 steps defined
- Tools integrations reflect reality
- Output standards concrete
- **Result**: PASS/FAIL with score

### Gate 3: Quality Gate (Manual)
- Full scoring against 8 criteria
- Overall ≥ 90, no criterion < 70
- No critical defects
- **Result**: SCORE + PASS/FAIL

### Gate 4: Security Gate (Conditional)
- Required for skills with external integrations
- All security checks pass
- **Result**: PASS/FAIL

### Gate 5: Compatibility Gate (Automated)
- Platform adapters work (when tested)
- Installation instructions verified
- **Result**: PASS/FAIL (per platform)

---

## 4. Continuous Quality

### Regression Testing
- Run automated checks on every change
- Track quality scores over time
- Alert on score degradation > 5 points

### Skill Health Metrics
```yaml
health_metrics:
  - "Quality score trend"
  - "Test pass rate"
  - "Issue resolution time"
  - "Documentation freshness (days since update)"
  - "Compatibility status per platform"
  - "Usage/adoption metrics (when available)"
```

### Quality Debt Tracking
- Document known limitations in `quality/DEBT.md`
- Prioritize by impact and effort
- Review quarterly

---

## 5. Evaluation Templates

### Skill Evaluation Scorecard

```markdown
# Skill Evaluation: [skill-id]

## Scores
| Criteria | Weight | Score | Weighted | Notes |
|----------|--------|-------|----------|-------|
| Accuracy | 20% | /100 | /20 | |
| Professional Expertise | 20% | /100 | /20 | |
| Workflow Completeness | 15% | /100 | /15 | |
| Output Quality | 15% | /100 | /15 | |
| Best Practices | 10% | /100 | /10 | |
| Security | 10% | /100 | /10 | |
| Documentation | 5% | /100 | /5 | |
| Efficiency | 5% | /100 | /5 | |
| **TOTAL** | **100%** | | **/100** | |

## Verdict
- [ ] PASS (≥ 90, no criterion < 70)
- [ ] FAIL

## Critical Defects
- None / List defects

## Recommendations
- List improvement items

## Reviewer
- Name:
- Date:
- Time spent:
```

### Automated Validation Report

```json
{
  "skill_id": "skill-id",
  "timestamp": "2026-11-08T10:00:00Z",
  "checks": {
    "metadata_validation": { "status": "pass", "errors": [] },
    "structure_validation": { "status": "pass", "missing": [] },
    "markdown_validation": { "status": "pass", "errors": 0, "warnings": 3 },
    "link_checking": { "status": "pass", "broken_internal": 0, "broken_external": 2 },
    "duplicate_detection": { "status": "pass", "duplicates": [] },
    "catalog_sync": { "status": "pass" }
  },
  "overall": "pass"
}
```

---

## 6. Quality Tools

### Validation Script (to be created at `tools/validators/validate-skill.sh`)

```bash
#!/bin/bash
# Usage: ./validate-skill.sh <skill-directory>

SKILL_DIR="$1"
# 1. Validate metadata
# 2. Check structure
# 3. Lint markdown
# 4. Check links
# 5. Check duplicates
# 6. Verify catalog sync
# 7. Output report
```

### Evaluation Script (to be created at `tools/validators/evaluate-skill.py`)

```python
#!/usr/bin/env python3
# Usage: ./evaluate-skill.py <skill-directory> [--reviewer name]

# Load skill metadata
# Run automated checks
# Present manual review checklist
# Calculate weighted score
# Generate scorecard
```

---

## 7. Remediation Process

When a skill fails a quality gate:

1. **Document failures** - Specific, actionable findings
2. **Assign owner** - Skill author or maintainer
3. **Set deadline** - Based on severity (critical: 1 week, major: 2 weeks, minor: 1 month)
4. **Track progress** - In issue tracker
5. **Re-evaluate** - Full re-review after fixes
6. **Update scorecard** - Record improvement

---

## 8. Exceptions & Waivers

- **Waivers require**: Architecture review approval
- **Documented in**: `quality/WAIVERS.md` per skill
- **Time-limited**: Max 6 months, then re-evaluate
- **Transparent**: Listed in release notes

---

*This framework ensures consistent, measurable quality across the entire skill library.*