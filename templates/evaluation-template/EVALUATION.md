# Skill Evaluation Template

Version: 1.0.0
Use this template for evaluating skill quality per QUALITY_FRAMEWORK.md.

---

# Evaluation: [skill-id]

## Metadata
- **Skill**: [skill-id]
- **Version**: [skill version]
- **Evaluator**: [name]
- **Date**: YYYY-MM-DD
- **Time Spent**: [hours]

## Automated Checks

| Check | Status | Details |
|-------|--------|---------|
| Metadata Validation | PASS/FAIL | [errors if any] |
| Structure Validation | PASS/FAIL | [missing items] |
| Markdown Linting | PASS/FAIL | [error count, warning count] |
| Link Checking | PASS/FAIL | [broken internal, broken external] |
| Duplicate Detection | PASS/FAIL | [duplicates found] |
| Catalog Sync | PASS/FAIL | [sync status] |

## Manual Review Scores

| Criteria | Weight | Score (0-100) | Weighted | Evidence/Notes |
|----------|--------|---------------|----------|----------------|
| Accuracy | 20% | | | [specific examples checked] |
| Professional Expertise | 20% | | | [depth assessment] |
| Workflow Completeness | 15% | | | [all 10 steps present?] |
| Output Quality | 15% | | | [deliverable quality] |
| Best Practices | 10% | | | [standards alignment] |
| Security | 10% | | | [security posture] |
| Documentation | 5% | | | [clarity, completeness] |
| Efficiency | 5% | | | [practical approach] |
| **TOTAL** | **100%** | | **/100** | |

## Verdict

- [ ] **PASS** (Overall ≥ 90, no criterion < 70, no critical defects)
- [ ] **FAIL**

## Critical Defects

| Defect | Severity | Description | Remediation |
|--------|----------|-------------|-------------|
| | Critical/High | | |

## Recommendations

### Must Fix (Before Release)
1. [Specific actionable item]

### Should Fix (Next Version)
1. [Specific actionable item]

### Nice to Have
1. [Specific actionable item]

## Quality Debt Identified

| Item | Impact | Effort | Target Date |
|------|--------|--------|-------------|
| | | | |

## Waivers Requested

| Waiver | Justification | Expiration |
|--------|---------------|------------|
| | | |

## Sign-off

- **Evaluator**: [name] - [date]
- **Approver**: [name] - [date] (if required)

---

*Per QUALITY_FRAMEWORK.md - Minimum release: Overall ≥ 90, no criterion < 70, no critical defects.*