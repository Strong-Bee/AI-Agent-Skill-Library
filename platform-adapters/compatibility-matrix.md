# Platform Compatibility Matrix

Version: 1.0.0
Last Updated: 2026-11-08

---

## Overview

Comprehensive compatibility matrix for all skills across supported platforms.

---

## Core Features Support Matrix

| Feature | Claude Code | OpenCode | Cursor | GitHub Copilot | Generic |
|---------|-------------|----------|--------|----------------|---------|
| **Skill Discovery** | ✅ | ✅ | ✅ | ✅ | ✅ (manual) |
| **Metadata Parsing** | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| **Tool Execution** | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **MCP Integration** | ✅ | ⚠️ | ❌ | ❌ | ❌ |
| **File System Access** | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **Network Access** | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **Long-running Workflows** | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| **Streaming Output** | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **Interactive Prompts** | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| **Configuration** | ✅ | ✅ | ✅ | ✅ | ✅ (manual) |
| **Subagents** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Hooks** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Slash Commands** | ✅ | ❌ | ❌ | ❌ | ❌ |

---

## Skill Structure Compatibility

| Element | Claude Code | OpenCode | Cursor | GitHub Copilot | Generic |
|---------|-------------|----------|--------|----------------|---------|
| **SKILL.md (YAML frontmatter)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **README.md** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Directory structure** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **config/** | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| **knowledge/** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **workflows/** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **tools/** | ✅ | ✅ | ⚠️ | ❌ | ✅ (docs) |
| **templates/** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **quality/** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **examples/** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **tests/** | ✅ | ✅ | ⚠️ | ❌ | ✅ (docs) |

---

## Platform-Specific Features

### Claude Code (Primary)
- Full MCP support
- Subagents for specialization
- Hooks for automation
- Slash commands
- Multiple permission modes
- Native tool set (Bash, Read, Write, Edit, Glob, Grep, Task, WebFetch, WebSearch)

### OpenCode (Primary)
- JSON-based skill manifest
- Tool permission system
- CLI-first workflow
- Extensible tool definitions

### Cursor (Primary)
- IDE-integrated
- Chat-based invocation
- Built-in tools (file, terminal, search)
- Privacy settings

### GitHub Copilot (Secondary)
- VS Code extension model
- Marketplace distribution
- Org policy compliance
- Limited local access

### Generic (Universal Baseline)
- Markdown-only
- Manual execution
- No automation
- Maximum portability

---

## Skill Compatibility Status

> This section tracks compatibility per skill. Updated during testing.

| Skill ID | Category | Claude Code | OpenCode | Cursor | Copilot | Generic | Last Tested |
|----------|----------|-------------|----------|--------|---------|---------|-------------|
| *Template skills to be added as developed* | | | | | | | |

---

## Testing Status

| Platform | Test Environment | Test Suite | Last Run | Status |
|----------|------------------|------------|----------|--------|
| Claude Code | Local + CI | Full | - | 🔄 Planned |
| OpenCode | Local + CI | Full | - | ⏳ Planned |
| Cursor | Local | Basic | - | ⏳ Planned |
| GitHub Copilot | VS Code | Basic | - | ⏳ Planned |
| Generic | Any | Manual | - | ✅ Baseline |

---

## Known Issues

| Platform | Issue | Severity | Workaround | Target Fix |
|----------|-------|----------|------------|------------|
| OpenCode | No MCP support | Medium | Document as optional | Adapter v2 |
| Cursor | No background execution | Low | Use for interactive only | - |
| Copilot | Extension packaging required | Medium | Automate packaging | Tools v1 |
| Generic | No automation | High | N/A (by design) | - |

---

## Version Compatibility

| Library Version | Claude Code | OpenCode | Cursor | Copilot | Generic |
|-----------------|-------------|----------|--------|---------|---------|
| 1.0.0 | ≥ 1.0.0 | ≥ 0.5.0 | ≥ 0.40.0 | ≥ 1.100.0 | Any |

---

## Migration Notes

### Breaking Changes

| Version | Change | Migration |
|---------|--------|-----------|
| 1.0.0 | Initial | N/A |

---

*Update this matrix after each compatibility test run.*