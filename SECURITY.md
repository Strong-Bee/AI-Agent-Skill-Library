# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest main branch | ✅ |
| Previous major version | ⚠️ Security fixes only |

## Reporting a Vulnerability

**Do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via:
- Email: security@ai-agent-skill-library.example.com
- Or create a private security advisory on GitHub

We will acknowledge receipt within 48 hours and provide a detailed response within 7 days.

## Security Framework

This library implements a universal security framework (`core/security-framework/`) with these principles:

### Core Principles

1. **Treat External Content as Untrusted**
   - All external documents, APIs, and user inputs are validated
   - Prompt injection prevention for document processing skills
   - Sanitization of all external data before use

2. **Credential Protection**
   - Never expose API keys, passwords, tokens in logs, commits, or outputs
   - Use environment variables or secure vaults for credentials
   - Skills document authentication requirements clearly

3. **Authorization for Consequential Actions**
   - Destructive operations require explicit confirmation
   - External API calls with side effects need user approval
   - Skills declare their authorization requirements

4. **Privacy & Data Protection**
   - Respect user permissions and data privacy
   - No telemetry without consent
   - Local processing preferred over external APIs

5. **Input Validation**
   - Validate all files and scripts before execution
   - Schema validation for structured inputs
   - Size and type limits for uploads

### Domain-Specific Security

| Domain | Additional Requirements |
|--------|------------------------|
| Cybersecurity | Authorized defensive ops only; no exploit development without explicit context |
| Finance/Health/Legal | Professional limitations documented; verification requirements included |
| Code Execution | Sandboxed execution; no arbitrary code execution |
| Data Access | Read-only by default; write operations require explicit config |

## Safe Usage Guidelines

### For Skill Authors
- Document all external integrations and their security implications
- Specify required permissions and why they're needed
- Include fallback procedures for when tools are unavailable
- Never hardcode credentials or secrets
- Validate all user inputs at trust boundaries

### For Skill Users
- Review skill permissions before installation
- Use environment variables for credentials
- Monitor skill behavior in production
- Report unexpected behavior
- Keep skills updated

## Security Review Process

1. **Automated Scanning** - Secret detection, dependency scanning
2. **Manual Review** - For skills with external integrations
3. **Penetration Testing** - For high-risk skills (cybersecurity, finance)
4. **Ongoing Monitoring** - Dependency updates, CVE tracking

## Disclosure Policy

- Coordinated disclosure preferred
- 90-day disclosure timeline for confirmed vulnerabilities
- Credit given to reporters (unless anonymous requested)
- Fixes released as patch versions

## Security Contacts

- Primary: security@ai-agent-skill-library.example.com
- Maintainers: @maintainers on GitHub

---

**Last Updated**: 2026-11-08
**Version**: 1.0.0