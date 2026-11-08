# Industry Standards Index

Version: 1.0.0
Last Updated: 2026-11-08

---

## Overview

This directory contains curated industry standards referenced by skills. Each standard entry includes:
- Standard identifier and name
- Scope and applicability
- Key requirements relevant to AI agent skills
- Compliance guidance
- Official references

---

## Standards by Domain

### Software Development

| Standard | Domain | Relevance |
|----------|--------|-----------|
| **ISO/IEC 12207** | Software Life Cycle | Process frameworks |
| **ISO/IEC 25010** | Software Quality | Quality model for evaluation |
| **IEEE 829** | Test Documentation | Test plan/report templates |
| **IEEE 1012** | Software Verification | V&V processes |
| **OWASP Top 10** | Web Security | Security skill requirements |
| **OWASP ASVS** | Application Security | Verification standards |
| **CWE Top 25** | Software Weaknesses | Secure coding practices |
| **Semantic Versioning** | Versioning | Skill versioning |
| **Conventional Commits** | Git Commits | Changelog generation |
| **Keep a Changelog** | Changelog Format | CHANGELOG.md standard |

### AI & Machine Learning

| Standard | Domain | Relevance |
|----------|--------|-----------|
| **ISO/IEC 22989** | AI Terminology | Common vocabulary |
| **ISO/IEC 23894** | AI Risk Management | Risk assessment for AI skills |
| **ISO/IEC 42001** | AI Management System | Governance for AI agents |
| **NIST AI RMF** | AI Risk Management | US framework |
| **EU AI Act** | AI Regulation | Compliance for EU deployment |
| **MLOps Standards** | ML Operations | Model deployment skills |

### Data & Analytics

| Standard | Domain | Relevance |
|----------|--------|-----------|
| **ISO/IEC 27001** | Information Security | Data handling skills |
| **ISO/IEC 27701** | Privacy Extension | PII handling |
| **GDPR** | Data Protection | EU compliance |
| **CCPA** | California Privacy | US compliance |
| **SOC 2** | Service Organization | Cloud service skills |
| **SQL Standards (ISO/IEC 9075)** | Database | SQL Specialist skill |

### Cybersecurity

| Standard | Domain | Relevance |
|----------|--------|-----------|
| **NIST CSF** | Cybersecurity Framework | Security Auditor skill |
| **NIST SP 800-53** | Security Controls | Compliance skills |
| **ISO/IEC 27001** | ISMS | Security management |
| **ISO/IEC 27002** | Security Controls | Implementation guidance |
| **MITRE ATT&CK** | Threat Modeling | Threat analysis skills |
| **CIS Controls** | Critical Security | Baseline hardening |

### Project Management

| Standard | Domain | Relevance |
|----------|--------|-----------|
| **PMBOK Guide** | Project Management | PM skill |
| **ISO 21500** | Project Management | International standard |
| **PRINCE2** | Structured PM | PM methodologies |
| **Scrum Guide** | Agile Framework | Agile skills |
| **SAFe** | Scaled Agile | Enterprise agile |

### Business & Finance

| Standard | Domain | Relevance |
|----------|--------|-----------|
| **GAAP / IFRS** | Accounting | Finance skills |
| **Basel III** | Banking Regulation | Financial risk skills |
| **ISO 31000** | Risk Management | Risk analysis skills |
| **COBIT** | IT Governance | IT management skills |
| **ITIL** | Service Management | ITSM skills |

### Quality & Testing

| Standard | Domain | Relevance |
|----------|--------|-----------|
| **ISO 9001** | Quality Management | QA skills |
| **ISTQB** | Software Testing | QA Automation skill |
| **CMMI** | Process Improvement | Process skills |
| **Six Sigma** | Process Quality | Process improvement |

### Accessibility & UX

| Standard | Domain | Relevance |
|----------|--------|-----------|
| **WCAG 2.1/2.2** | Web Accessibility | UI/UX Designer skill |
| **ISO 9241-210** | Human-Centered Design | UX skills |
| **Section 508** | US Federal Accessibility | Government projects |

---

## Usage in Skills

When referencing a standard in a skill's `knowledge_base.industry_standards`:

```yaml
- standard: "OWASP Top 10 2021"
  relevance: "Defines top web application security risks that security auditor skill must detect"
  compliance_notes: "Skill implements checks for A01-A10; maps findings to CWE IDs"
```

---

## Maintenance

- Review annually for updates
- Add new standards as domains expand
- Remove superseded versions
- Verify links annually

---

*This index ensures consistent, authoritative standard references across all skills.*