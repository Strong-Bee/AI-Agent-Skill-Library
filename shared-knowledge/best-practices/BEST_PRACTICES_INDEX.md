# Best Practices Index

Version: 1.0.0
Last Updated: 2026-11-08

---

## Overview

This directory contains curated best practices organized by domain. Each practice includes:
- Practice statement
- Rationale
- Implementation guidance
- Anti-patterns to avoid
- References

---

## Best Practices by Domain

### Universal (Apply to All Skills)

| Practice | Description |
|----------|-------------|
| **Single Responsibility** | Each skill does one thing well |
| **Explicit over Implicit** | Clear inputs, outputs, assumptions |
| **Fail Fast** | Validate early, error clearly |
| **Document Decisions** | ADRs for significant choices |
| **Version Everything** | Semantic versioning for all artifacts |
| **Test Automation** | Automated validation for all capabilities |
| **Security by Default** | Least privilege, input validation |
| **Observability** | Logs, metrics, traces for debugging |

### AI & Automation

| Practice | Description |
|----------|-------------|
| **Prompt Versioning** | Track prompt versions with skill versions |
| **Evaluation-Driven Development** | Define evals before building |
| **Human-in-the-Loop** | Critical decisions require human review |
| **Context Window Management** | Optimize token usage, summarize |
| **Tool Result Caching** | Avoid redundant tool calls |
| **Graceful Degradation** | Fallback when tools unavailable |
| **Prompt Injection Prevention** | Sanitize external content |
| **Deterministic Outputs** | Structured outputs, schemas |

### Software Development

| Practice | Description |
|----------|-------------|
| **TDD/BDD** | Tests drive implementation |
| **Code Reviews** | All changes reviewed |
| **CI/CD** | Automated build, test, deploy |
| **Dependency Management** | Pin versions, scan vulnerabilities |
| **Static Analysis** | Lint, type-check, security scan |
| **Documentation as Code** | Docs in repo, versioned |
| **Feature Flags** | Safe rollouts |
| **Error Handling** | Explicit, recoverable, logged |
| **Performance Budgets** | Measure and enforce |

### Digital Marketing

| Practice | Description |
|----------|-------------|
| **Data-Driven Decisions** | Metrics over intuition |
| **A/B Testing** | Experiment with statistical rigor |
| **Audience Segmentation** | Targeted messaging |
| **Consent Management** | GDPR/CCPA compliant |
| **Attribution Modeling** | Multi-touch attribution |
| **Content Repurposing** | Maximize asset value |
| **Brand Consistency** | Guidelines enforced |
| **Mobile-First** | Mobile experience priority |

### Design & Creative

| Practice | Description |
|----------|-------------|
| **Accessibility First** | WCAG 2.1 AA minimum |
| **Design Systems** | Reusable components, tokens |
| **User Testing** | Validate with real users |
| **Responsive Design** | Mobile to desktop |
| **Performance Budgets** | Load time, interaction |
| **Design Tokens** | Single source of truth |
| **Version Control for Design** | Figma branches, commits |
| **Handoff Documentation** | Specs for developers |

### Business & Management

| Practice | Description |
|----------|-------------|
| **OKR Alignment** | Objectives cascade |
| **Regular Retrospectives** | Continuous improvement |
| **Stakeholder Communication** | Regular, structured updates |
| **Risk Register** | Track and mitigate |
| **Decision Logs** | Document rationale |
| **Capacity Planning** | Sustainable pace |
| **Knowledge Sharing** | Documentation, sessions |

### Data & Analytics

| Practice | Description |
|----------|-------------|
| **Data Quality Checks** | Automated validation |
| **Reproducible Pipelines** | Versioned, parameterized |
| **Data Lineage** | Track transformations |
| **Privacy by Design** | Minimize, anonymize |
| **Statistical Rigor** | Power analysis, p-values |
| **Visualization Standards** | Consistent, accessible |
| **Model Monitoring** | Drift detection |

### Cybersecurity

| Practice | Description |
|----------|-------------|
| **Defense in Depth** | Multiple layers |
| **Zero Trust** | Verify everything |
| **Least Privilege** | Minimum necessary access |
| **Incident Response Plan** | Tested, updated |
| **Threat Modeling** | Proactive identification |
| **Regular Patching** | Vulnerability management |
| **Security Training** | Continuous awareness |

### Finance & Accounting

| Practice | Description |
|----------|-------------|
| **Double-Entry Bookkeeping** | Accuracy guarantee |
| **Audit Trails** | Immutable logs |
| **Reconciliation** | Regular verification |
| **Regulatory Compliance** | GAAP/IFRS adherence |
| **Forecast Accuracy** | Track variance |
| **Internal Controls** | Separation of duties |

### Writing & Communication

| Practice | Description |
|----------|-------------|
| **Audience Analysis** | Tailor to reader |
| **Plain Language** | Clear, concise, accessible |
| **Style Guide Consistency** | AP, Chicago, or house |
| **Review Cycles** | Peer review, legal review |
| **Version Control** | Track changes |
| **Localization Ready** | Structure for translation |

---

## Anti-Patterns (What to Avoid)

| Anti-Pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| **God Skill** | Does everything poorly | Focused, composable skills |
| **Hardcoded Secrets** | Security risk | Environment variables |
| **No Error Handling** | Silent failures | Explicit validation |
| **Undocumented Assumptions** | Misuse, bugs | Explicit preconditions |
| **Ignoring Platform Limits** | Failures in production | Test on target platforms |
| **Copy-Paste Configuration** | Drift, errors | Template generation |
| **Skipping Tests** | Regression risk | Automated gates |
| **Over-Engineering** | Complexity, maintenance | YAGNI, simplest solution |

---

## Usage in Skills

When referencing a best practice in a skill's `knowledge_base.best_practices`:

```yaml
- practice: "Evaluation-Driven Development"
  description: "Define evaluation criteria and test cases before implementing skill capabilities"
  rationale: "Ensures measurable quality; prevents scope creep; enables regression detection"
  anti_pattern: "Building features without defined success criteria"
```

---

## Maintenance

- Review quarterly
- Add practices as domains expand
- Validate with practitioners
- Cross-reference with methodologies and standards

---

*This index ensures consistent best practice application across all skills.*