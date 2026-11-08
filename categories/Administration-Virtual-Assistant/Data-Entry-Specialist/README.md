# Data Entry Specialist

> Accurately input, validate, and manage data across systems with high speed and precision.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The Data Entry Specialist skill provides comprehensive capabilities for accurately inputting, validating, and managing data across systems with high speed, precision, and attention to detail.

This skill embodies the professional role of a **Data Entry Specialist** - a specialist who ensures data integrity, maintains confidentiality, and optimizes data entry workflows for efficiency and accuracy.

## Target Audience

- **Primary**: Data Entry Managers, Data Entry Specialists, Operations Managers
- **Secondary**: Business Owners, Healthcare Administrators, Finance Teams, Data Managers

## Prerequisites

- **Required tools**: Spreadsheet Application (Excel/Sheets), Database/CRM System, Validation Tools
- **Required knowledge**: Touch typing (80+ WPM), 10-key numeric, basic database concepts, data validation principles
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/Administration-Virtual-Assistant/Data-Entry-Specialist ~/.claude/skills/administration/data-entry-specialist
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/Administration-Virtual-Assistant/Data-Entry-Specialist ~/.opencode/skills/administration/data-entry-specialist
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/Administration-Virtual-Assistant/Data-Entry-Specialist /your/agent/skills/
```

## Quick Start

```markdown
# Process 1000 invoices with validation
Use the data-entry-specialist skill to:
1. Set up Excel with data validation rules
2. Configure database connections and table structures
3. Create templates and macros for repetitive patterns
4. Process batches of 100 with hourly quality checkpoints
3. Generate quality report with accuracy metrics
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| High-Speed Data Entry | Touch typing 80+ WPM, 10-key 10,000+ KPH, 500+ records/hour |
| Data Validation & Quality Control | Real-time validation, double-entry, automated rules, audit trails |
| Batch Processing & Automation | ETL tools, macros, scripts, OCR, 10,000+ records/day |
| Data Confidentiality & Compliance | HIPAA, GDPR, PCI-DSS, encryption, audit trails |
| Error Detection & Correction | Fuzzy matching, deduplication, anomaly detection, root cause analysis |
| Multi-System Navigation | ERP, CRM, database, spreadsheet, 5+ systems simultaneously |

## Workflow Overview

10-step workflow for data entry:

1. **Request Analysis** - Source documents, specs, volume, quality requirements
2. **Requirement Clarification** - Fields, formats, validation, exceptions
3. **Context Gathering** - Documents, access, templates, validation config
4. **Research** - Entry methods, automation, best practices, ergonomics
5. **Planning** - Batches, resources, quality checkpoints, contingencies
6. **Task Execution** - Entry, validation checkpoints, exception handling
7. **Validation** - Accuracy verification, double-entry, audit
8. **Quality Review** - Metrics, trends, root cause, improvements
9. **Error Correction** - Corrections, preventive controls, retraining
10. **Final Delivery** - Dataset, quality report, exception log, handoff

## Configuration

Key options in `config/settings.yaml`:

```yaml
entry:
  target_systems: ["excel", "database", "crm"]
  validation_mode: "real-time"
  double_entry: false
  batch_size: 100

quality:
  accuracy_target: 99.9
  checkpoint_frequency: "hourly"
  audit_sample_rate: 0.05
  double_entry_critical: true

performance:
  target_kph: 10000
  target_wpm: 80
  batch_size: 100
  hourly_target: 500

compliance:
  regulations: ["GDPR", "HIPAA"]
  encryption: "at-rest-and-transit"
  access_logging: true
  retention_days: 2555
```

## Examples

See `examples/` for:
- `invoice-processing/` - High-volume invoice data entry with validation
- `medical-records/` - HIPAA-compliant patient data entry
- `survey-data/` - Large-scale survey response entry with validation
- `inventory-update/` - Batch inventory updates with verification
- `migration-legacy/` - Legacy system migration with validation

## Limitations

- Cannot interpret or analyze data beyond validation rules
- Cannot modify source documents or make judgment calls on ambiguous data
- Speed-accuracy tradeoff requires balance; 100% accuracy may reduce throughput
- Cannot access systems without proper authorization
- Repetitive nature requires ergonomic considerations and breaks

## Related Skills

- [Customer Support Specialist](../Customer-Support-Specialist/README.md) - Data entry for support tickets
- [Virtual Assistant](../Virtual-Assistant/README.md) - General administrative data tasks
- [Documentation Specialist](../Documentation-Specialist/README.md) - Document processing

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)