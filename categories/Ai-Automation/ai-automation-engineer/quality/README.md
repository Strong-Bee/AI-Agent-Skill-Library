# Quality Assurance

This directory contains quality evaluation criteria and results for the AI Automation Engineer skill.

## Structure

| File | Purpose |
|------|---------|
| `EVALUATION.md` | Self-evaluation against quality framework |
| `DEBT.md` | Known quality debt and limitations |
| `WAIVERS.md` | Approved waivers (time-limited) |
| `scorecard.json` | Latest evaluation scorecard |

## Evaluation Criteria (from Quality Framework)

| Criteria | Weight | Target |
|----------|--------|--------|
| Accuracy | 20% | ≥ 90 |
| Professional Expertise | 20% | ≥ 90 |
| Workflow Completeness | 15% | ≥ 90 |
| Output Quality | 15% | ≥ 90 |
| Best Practices | 10% | ≥ 80 |
| Security | 10% | ≥ 90 |
| Documentation | 5% | ≥ 80 |
| Efficiency | 5% | ≥ 80 |
| **Overall** | **100%** | **≥ 90** |

## Minimum Release Requirements

- Overall score ≥ 90/100
- No criterion < 70/100
- No unresolved critical defects
- All required documentation complete
- Metadata validates against schema
- Examples executable or clearly illustrative
- Tests pass (when framework available)
- Security review passed
- Compatibility limitations documented

## Self-Evaluation Process

1. Run automated checks (metadata, structure, markdown, links)
2. Complete manual review checklist
3. Score each criterion with evidence
4. Document any debt or waivers
5. Generate scorecard
6. If PASS: ready for release
7. If FAIL: remediate and re-evaluate

## Current Quality Status

| Criteria | Score | Evidence |
|----------|-------|----------|
| Accuracy | TBD | [To be evaluated] |
| Professional Expertise | TBD | [To be evaluated] |
| Workflow Completeness | TBD | [To be evaluated] |
| Output Quality | TBD | [To be evaluated] |
| Best Practices | TBD | [To be evaluated] |
| Security | TBD | [To be evaluated] |
| Documentation | TBD | [To be evaluated] |
| Efficiency | TBD | [To be evaluated] |
| **Overall** | **TBD** | |

## Debt Tracking

Document in `DEBT.md`:
- Item description
- Impact (user-facing, maintainability, security)
- Effort to fix
- Target resolution date
- Owner

## Waivers

Document in `WAIVERS.md`:
- Waiver description
- Justification
- Approver
- Expiration date (max 6 months)
- Risk acceptance