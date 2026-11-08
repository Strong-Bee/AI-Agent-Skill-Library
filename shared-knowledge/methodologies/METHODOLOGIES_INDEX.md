# Professional Methodologies Index

Version: 1.0.0
Last Updated: 2026-11-08

---

## Overview

This directory contains curated professional methodologies referenced by skills. Each methodology entry includes:
- Methodology name and origin
- Core principles and phases
- When to apply
- Key artifacts/deliverables
- Tools and techniques
- Limitations

---

## Methodologies by Category

### AI & Automation

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **CRISP-DM** | Data Mining | ML/AI project lifecycle |
| **MLOps Lifecycle** | Industry | ML model deployment |
| **RAGAS** | RAG Evaluation | RAG system evaluation |
| **Agent Evaluation Framework** | Custom | Multi-agent system evaluation |
| **Prompt Engineering Patterns** | Industry | Prompt optimization |

### Software Development

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **Test-Driven Development (TDD)** | Kent Beck | Development workflow |
| **Behavior-Driven Development (BDD)** | Dan North | Requirements → tests |
| **Domain-Driven Design (DDD)** | Eric Evans | Complex domain modeling |
| **Clean Architecture** | Robert Martin | System architecture |
| **Hexagonal Architecture** | Alistair Cockburn | Ports & adapters |
| **Event Storming** | Alberto Brandolini | Domain exploration |
| **C4 Model** | Simon Brown | Architecture documentation |
| **ADR (Architecture Decision Records)** | Michael Nygard | Decision tracking |
| **GitFlow / GitHub Flow** | Vincent Driessen | Branching strategy |
| **Trunk-Based Development** | Paul Hammant | CI/CD branching |

### Agile & Project Management

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **Scrum** | Schwaber/Sutherland | Sprint-based delivery |
| **Kanban** | David Anderson | Flow-based delivery |
| **SAFe** | Scaled Agile | Enterprise scaling |
| **LeSS** | Larman/Vodde | Large-scale Scrum |
| **Shape Up** | Basecamp | Product development |
| **OKRs** | Andy Grove/John Doerr | Goal setting |
| **RACI Matrix** | Project Management | Role clarity |

### Design & Creative

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **Design Thinking** | IDEO/Stanford d.school | Problem solving |
| **Double Diamond** | Design Council | Diverge/converge |
| **Jobs To Be Done (JTBD)** | Clayton Christensen | User needs |
| **Atomic Design** | Brad Frost | Design systems |
| **Design Sprints** | Google Ventures | Rapid prototyping |
| **Usability Testing** | Nielsen Norman Group | Validation |

### Digital Marketing

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **AARRR (Pirate Metrics)** | Dave McClure | Growth funnel |
| **RACE Framework** | Smart Insights | Digital marketing |
| **Content Marketing Funnel** | Industry | Content strategy |
| **SEO Technical Audit** | Industry | Technical SEO |
| **Conversion Rate Optimization** | Industry | CRO process |

### Business Analysis

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **BABOK** | IIBA | Business analysis |
| **SWOT Analysis** | Albert Humphrey | Strategic analysis |
| **PESTLE Analysis** | Francis Aguilar | Environmental scanning |
| **Porter's Five Forces** | Michael Porter | Competitive analysis |
| **Value Proposition Canvas** | Strategyzer | Product-market fit |
| **Business Model Canvas** | Strategyzer | Business modeling |

### Data & Analytics

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **CRISP-DM** | SPSS | Data mining projects |
| **KDD Process** | Fayyad et al. | Knowledge discovery |
| **Data Mesh** | Zhamak Dehghani | Decentralized data |
| **Data Vault** | Dan Linstedt | Data warehouse modeling |

### Quality & Process Improvement

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **DMAIC (Six Sigma)** | Motorola | Process improvement |
| **PDCA/PDSA** | Deming/Shewhart | Continuous improvement |
| **Kaizen** | Toyota | Incremental improvement |
| **Value Stream Mapping** | Lean | Process visualization |
| **Root Cause Analysis (5 Whys, Fishbone)** | Toyota/Sakichi Toyoda | Problem solving |

### Research & Education

| Methodology | Origin | Application |
|-------------|--------|-------------|
| **Systematic Literature Review** | Cochrane | Evidence synthesis |
| **PRISMA** | Moher et al. | Review reporting |
| **Grounded Theory** | Glaser/Strauss | Qualitative research |
| **Action Research** | Kurt Lewin | Practitioner research |
| **ADDIE** | Florida State | Instructional design |
| **SAM (Successive Approximation)** | Allen Interactions | Agile instructional design |

---

## Usage in Skills

When referencing a methodology in a skill's `knowledge_base.professional_methodologies`:

```yaml
- name: "Test-Driven Development (TDD)"
  description: "Red-Green-Refactor cycle for ensuring code correctness"
  steps:
    - "Write failing test"
    - "Write minimal code to pass"
    - "Refactor with confidence"
  when_to_use: "New feature development, bug fixes, refactoring"
  limitations: "Requires testable architecture; slower initial velocity"
```

---

## Methodology Selection Guide

| Situation | Recommended Methodologies |
|-----------|---------------------------|
| New product discovery | Design Thinking, JTBD, Double Diamond |
| Complex domain modeling | DDD, Event Storming |
| Rapid prototyping | Design Sprints, Shape Up |
| Enterprise scaling | SAFe, LeSS |
| Quality-critical systems | TDD, Clean Architecture, DMAIC |
| Data science projects | CRISP-DM, KDD |
| Process improvement | DMAIC, Kaizen, VSM |
| Strategic planning | OKRs, SWOT, PESTLE, Porter's |
| Architecture decisions | ADR, C4 Model |

---

## Maintenance

- Review annually
- Add methodologies as new domains are covered
- Cross-reference with industry standards
- Validate with practitioners

---

*This index ensures consistent methodology references and application guidance across skills.*