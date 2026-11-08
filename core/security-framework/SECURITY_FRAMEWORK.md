# Security Framework

Version: 1.0.0
Status: Draft
Last Updated: 2026-11-08

---

## Overview

This framework defines the universal security requirements for all skills in the AI Agent Skill Library. It ensures safe, responsible operation across all platforms and use cases.

---

## 1. Core Security Principles

### Principle 1: Treat External Content as Untrusted

```yaml
external_content_handling:
  - All external documents, APIs, user inputs are untrusted by default
  - Validate and sanitize before processing
  - Implement prompt injection prevention for document processing
  - Use allowlists for acceptable content types/formats
  - Size limits on all inputs
```

### Principle 2: Credential Protection

```yaml
credential_protection:
  - NEVER expose API keys, passwords, tokens in logs, commits, outputs
  - Use environment variables or secure vaults only
  - Skills must document authentication requirements clearly
  - No credential storage in skill directories
  - Rotation policies documented for each service
```

### Principle 3: Authorization for Consequential Actions

```yaml
authorization:
  - Destructive operations require explicit user confirmation
  - External API calls with side effects need approval
  - Skills declare authorization requirements in metadata
  - Audit trail for consequential actions
```

### Principle 4: Privacy & Data Protection

```yaml
privacy:
  - Respect user permissions and data privacy
  - No telemetry without explicit consent
  - Local processing preferred over external APIs
  - Data minimization - collect only what's needed
  - Clear data retention policies
```

### Principle 5: Input Validation

```yaml
input_validation:
  - Validate all files and scripts before execution
  - Schema validation for structured inputs
  - Size and type limits for uploads
  - Path traversal prevention
  - Command injection prevention
```

---

## 2. Domain-Specific Security Requirements

### Cybersecurity Skills

```yaml
cybersecurity:
  focus: "Authorized defensive operations only"
  allowed:
    - Security auditing and assessment
    - Incident response and forensics
    - Vulnerability scanning (authorized scope)
    - Security education and training
    - Compliance checking
  prohibited:
    - Exploit development without explicit authorized context
    - Offensive tooling without clear authorization
    - Credential harvesting
    - Unauthorized access attempts
  requirements:
    - Explicit scope documentation
    - Authorization verification steps
    - Chain of custody for evidence
```

### Finance, Health, Legal Skills

```yaml
regulated_domains:
  finance:
    - Professional limitations documented
    - Verification requirements for calculations
    - No investment advice without disclaimers
    - Regulatory compliance notes (SEC, FINRA, etc.)
  
  health:
    - HIPAA compliance considerations
    - No medical advice without disclaimers
    - PHI handling procedures
    - Clinical validation requirements
  
  legal:
    - No legal advice without disclaimers
    - Jurisdiction specificity
    - Attorney-client privilege considerations
    - Regulatory compliance notes
```

### Code Execution Skills

```yaml
code_execution:
  - Sandboxed execution environments only
  - No arbitrary code execution from untrusted input
  - Resource limits (CPU, memory, time, network)
  - Language-specific safety controls
  - Output sanitization
```

### Data Access Skills

```yaml
data_access:
  - Read-only by default
  - Write operations require explicit configuration
  - Connection string validation
  - Query parameterization (SQL injection prevention)
  - Access logging
```

---

## 3. Skill Security Metadata

Every skill must declare its security posture in `SKILL.md`:

```yaml
security_metadata:
  risk_level: "low|medium|high|critical"
  external_integrations:
    - service: "Service name"
      risk: "low|medium|high"
      data_shared: "What data leaves local environment"
      authentication: "How auth is handled"
  
  file_operations:
    read: ["patterns"]
    write: ["patterns"]
    execute: ["patterns"]
  
  network_access:
    required: true|false
    destinations: ["allowed domains/IPs"]
    protocols: ["https", "wss"]
  
  credentials_required:
    - name: "ENV_VAR_NAME"
      description: "What it's for"
      rotation: "policy"
  
  user_confirmation_required:
    - "Destructive operations"
    - "External API calls with side effects"
    - "Cost-incurring operations"
  
  data_handling:
    pii_processed: true|false
    pii_types: ["email", "name", "etc"]
    retention: "policy"
    encryption: "at-rest|in-transit|both"
  
  security_testing:
    - "Static analysis passed"
    - "Dependency scan passed"
    - "Penetration test (for high/critical)"
```

---

## 4. Secure Development Practices

### For Skill Authors

```yaml
author_practices:
  - Never hardcode credentials or secrets
  - Use environment variable references: ${API_KEY}
  - Validate all user inputs at trust boundaries
  - Document all external integrations and security implications
  - Specify required permissions and justification
  - Include fallback procedures for unavailable tools
  - Use parameterized queries for databases
  - Implement rate limiting for external APIs
  - Log security-relevant events (no secrets)
  - Regular dependency updates
```

### For Platform Integrations

```yaml
platform_security:
  claude_code:
    - Respect permission modes
    - Use approved tools only
    - No bypass of sandbox
  
  opencode:
    - Follow opencode security model
    - Respect tool permissions
  
  cursor:
    - Follow Cursor privacy settings
    - No unauthorized data access
  
  github_copilot:
    - Respect organizational policies
    - No unauthorized repository access
  
  generic:
    - Document platform-specific security requirements
    - Provide secure defaults
```

---

## 5. Security Review Process

### Automated Security Scanning

```yaml
automated_scans:
  secret_detection:
    tool: "gitleaks, trufflehog, or similar"
    scope: "All skill directories"
    fail_on: "Any detected secret"
  
  dependency_scanning:
    tool: "npm audit, pip-audit, cargo audit, etc."
    scope: "All package dependencies in tools/"
    fail_on: "Critical/High vulnerabilities"
  
  static_analysis:
    tool: "semgrep, codeql, or language-specific"
    scope: "All executable code in skills"
    rules: "OWASP Top 10, CWE Top 25"
```

### Manual Security Review

```yaml
manual_review:
  required_for:
    - risk_level: "high|critical"
    - external_integrations: true
    - file_operations_write: true
    - code_execution: true
  
  review_items:
    - Threat model review
    - Attack surface analysis
    - Authentication/authorization verification
    - Data flow analysis
    - Fallback procedure testing
```

### Penetration Testing

```yaml
pentest:
  required_for: "risk_level: critical"
  scope: "Skill + platform integration"
  frequency: "Annual or after major changes"
  reporting: "Findings tracked in security tracker"
```

---

## 6. Incident Response

### Vulnerability Disclosure

```yaml
disclosure:
  - Report via: security@ai-agent-skill-library.example.com
  - Or: GitHub Security Advisories (private)
  - Acknowledgment: Within 48 hours
  - Assessment: Within 7 days
  - Fix timeline: Critical 7 days, High 30 days, Medium 90 days
  - Disclosure: Coordinated, 90 days default
```

### Security Updates

```yaml
updates:
  - Patch releases for security fixes
  - Advisory published for each fix
  - Affected skills listed
  - Upgrade instructions provided
  - No breaking changes in patch versions
```

---

## 7. Security Checklist for Skill Release

Before releasing any skill:

- [ ] Security metadata complete in SKILL.md
- [ ] No hardcoded secrets anywhere
- [ ] All external integrations documented with risks
- [ ] Input validation implemented at all trust boundaries
- [ ] User confirmation required for consequential actions
- [ ] Credentials handled via environment variables only
- [ ] Automated security scans pass
- [ ] Manual security review passed (if required)
- [ ] Fallback procedures documented and tested
- [ ] Data handling compliant with privacy requirements
- [ ] Dependencies scanned, no critical vulnerabilities
- [ ] Security testing documented

---

## 8. Platform-Specific Security

| Platform | Security Model | Skill Requirements |
|----------|---------------|-------------------|
| Claude Code | Permission modes, sandbox | Respect permissions, no sandbox escape |
| OpenCode | Tool permissions | Declare required tools |
| Cursor | Privacy settings, org policies | No unauthorized access |
| GitHub Copilot | Org policies, repo permissions | Respect boundaries |
| Generic | User-defined | Document requirements |

---

*This framework is mandatory for all skills. Non-compliant skills cannot be released.*