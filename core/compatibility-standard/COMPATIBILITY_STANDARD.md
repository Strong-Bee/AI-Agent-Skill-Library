# Compatibility Standard

Version: 1.0.0
Status: Draft
Last Updated: 2026-11-08

---

## Overview

This standard defines the platform compatibility requirements, adapter specifications, and integration patterns for the AI Agent Skill Library across supported platforms.

---

## 1. Supported Platforms

| Platform | Status | Adapter Location | Test Status |
|----------|--------|------------------|-------------|
| **Claude Code / Claude Desktop** | Primary | `platform-adapters/claude/` | 🔄 In Progress |
| **OpenCode** | Primary | `platform-adapters/opencode/` | ⏳ Planned |
| **Cursor** | Primary | `platform-adapters/cursor/` | ⏳ Planned |
| **GitHub Copilot** | Secondary | `platform-adapters/github-copilot/` | ⏳ Planned |
| **Generic Markdown** | Universal | `platform-adapters/generic/` | ✅ Baseline |

---

## 2. Compatibility Matrix

### Core Features Support

| Feature | Claude Code | OpenCode | Cursor | GitHub Copilot | Generic |
|---------|-------------|----------|--------|----------------|---------|
| Skill Discovery | ✅ | ✅ | ✅ | ✅ | ✅ (manual) |
| Metadata Parsing | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| Tool Execution | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| MCP Integration | ✅ | ⚠️ | ❌ | ❌ | ❌ |
| File System Access | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| Network Access | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| Long-running Workflows | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Streaming Output | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| Interactive Prompts | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| Configuration | ✅ | ✅ | ✅ | ✅ | ✅ (manual) |

### Skill Structure Compatibility

| Element | Claude Code | OpenCode | Cursor | GitHub Copilot | Generic |
|---------|-------------|----------|--------|----------------|---------|
| SKILL.md (YAML frontmatter) | ✅ | ✅ | ✅ | ✅ | ✅ |
| README.md | ✅ | ✅ | ✅ | ✅ | ✅ |
| Directory structure | ✅ | ✅ | ✅ | ✅ | ✅ |
| config/ | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| knowledge/ | ✅ | ✅ | ✅ | ✅ | ✅ |
| workflows/ | ✅ | ✅ | ✅ | ✅ | ✅ |
| tools/ | ✅ | ✅ | ⚠️ | ❌ | ✅ (docs) |
| templates/ | ✅ | ✅ | ✅ | ✅ | ✅ |
| quality/ | ✅ | ✅ | ✅ | ✅ | ✅ |
| examples/ | ✅ | ✅ | ✅ | ✅ | ✅ |
| tests/ | ✅ | ✅ | ⚠️ | ❌ | ✅ (docs) |

---

## 3. Platform Adapter Specification

Each platform adapter must provide:

### 3.1 Discovery Mechanism

```yaml
discovery:
  method: "filesystem|config|registry|api"
  location: "Where skills are found"
  pattern: "How skills are identified"
  metadata_extraction: "How SKILL.md is parsed"
```

### 3.2 Installation Format

```yaml
installation:
  format: "symlink|copy|package|extension"
  structure: "Expected directory layout"
  configuration: "Platform-specific config files"
  verification: "How to verify installation"
```

### 3.3 Execution Interface

```yaml
execution:
  entry_point: "How skills are invoked"
  parameter_passing: "How inputs are provided"
  output_handling: "How results are returned"
  tool_bridge: "How skill tools map to platform tools"
  permission_model: "How permissions work"
```

### 3.4 Configuration Mapping

```yaml
configuration:
  skill_config: "How skill config/ maps to platform"
  environment_vars: "Standard env var names"
  secrets_handling: "Credential management"
  tool_availability: "How to check tool presence"
```

---

## 4. Adapter Implementation Requirements

### 4.1 Claude Code Adapter (`platform-adapters/claude/`)

```yaml
claude_adapter:
  discovery:
    method: "filesystem"
    location: "~/.claude/skills/ or project/.claude/skills/"
    pattern: "Directories with SKILL.md"
  
  installation:
    format: "symlink"
    structure: "~/.claude/skills/category/skill-name/"
    verification: "claude /skill command lists skill"
  
  execution:
    entry_point: "Skill invoked via slash command or agent"
    parameter_passing: "Natural language + context"
    tool_bridge: "Native Claude Code tools (Bash, Read, Write, etc.)"
    permission_model: "Claude Code permission modes"
  
  mcp_integration:
    supported: true
    configuration: ".mcp.json in skill directory"
    auto_discovery: true
  
  config_mapping:
    skill_config: "Read from config/ directly"
    env_vars: "Standard: SKILL_{CATEGORY}_{SKILL}_VAR"
```

### 4.2 OpenCode Adapter (`platform-adapters/opencode/`)

```yaml
opencode_adapter:
  discovery:
    method: "config"
    location: "opencode.json skills.paths"
    pattern: "Directories with skill.yaml manifest"
  
  installation:
    format: "copy"
    structure: ".opencode/skill/skill-name/"
    config: "skill.yaml manifest (generated from SKILL.md)"
    verification: "opencode skill list"
  
  execution:
    entry_point: "opencode run skill-name"
    parameter_passing: "JSON input via stdin"
    tool_bridge: "OpenCode tool definitions"
    permission_model: "OpenCode tool permissions"
  
  config_mapping:
    skill_config: "Merged into opencode.json"
    env_vars: "OPENCODE_SKILL_{SKILL}_VAR"
```

### 4.3 Cursor Adapter (`platform-adapters/cursor/`)

```yaml
cursor_adapter:
  discovery:
    method: "config"
    location: "Cursor settings: claude.skillsPath"
    pattern: "Directories with SKILL.md"
  
  installation:
    format: "symlink"
    structure: "~/.cursor/skills/category/skill-name/"
    verification: "Cursor skill palette shows skill"
  
  execution:
    entry_point: "Cmd/Ctrl+K → Skill name"
    parameter_passing: "Chat context + explicit params"
    tool_bridge: "Cursor built-in tools"
    permission_model: "Cursor privacy settings"
  
  config_mapping:
    skill_config: "Cursor settings JSON"
    env_vars: "CURSOR_SKILL_{SKILL}_VAR"
```

### 4.4 GitHub Copilot Adapter (`platform-adapters/github-copilot/`)

```yaml
copilot_adapter:
  discovery:
    method: "package"
    location: "VS Code extensions marketplace"
    pattern: "Packaged skill extensions"
  
  installation:
    format: "extension"
    structure: "VS Code extension with skill bundle"
    config: "package.json with skill metadata"
    verification: "Copilot Chat shows skill"
  
  execution:
    entry_point: "@skill-name in Copilot Chat"
    parameter_passing: "Chat context"
    tool_bridge: "VS Code API + Copilot tools"
    permission_model: "Org/repository permissions"
  
  config_mapping:
    skill_config: "VS Code settings.json"
    env_vars: "Not directly supported"
```

### 4.5 Generic Adapter (`platform-adapters/generic/`)

```yaml
generic_adapter:
  discovery:
    method: "manual"
    location: "User-defined directory"
    pattern: "Directories with SKILL.md"
  
  installation:
    format: "copy"
    structure: "Any directory structure"
    config: "Manual SKILL.md reading"
    verification: "Manual"
  
  execution:
    entry_point: "Manual workflow execution"
    parameter_passing: "User provides context"
    tool_bridge: "User's available tools"
    permission_model: "User-controlled"
  
  config_mapping:
    skill_config: "Manual"
    env_vars: "User-defined"
```

---

## 5. Cross-Platform Skill Development

### 5.1 Universal Core (Platform-Independent)

These elements work identically across all platforms:

- `SKILL.md` metadata and specification
- `knowledge/` domain knowledge
- `workflows/` procedural workflows
- `templates/` reusable templates
- `examples/` usage examples
- `quality/` evaluation criteria

### 5.2 Platform-Specific Adaptations

These may vary by platform:

| Element | Adaptation Strategy |
|---------|---------------------|
| `tools/` | Provide platform-specific implementations; document fallbacks |
| `config/` | Use platform config mapping; provide translation layer |
| `tests/` | Platform-specific test harnesses; shared fixtures |
| MCP servers | Only for Claude Code; document as optional enhancement |

### 5.3 Capability Declaration

Skills declare platform compatibility in metadata:

```yaml
identity:
  platforms:
    - "claude"
    - "opencode"
    - "cursor"
    - "github-copilot"
    - "generic"
  
  platform_requirements:
    claude:
      min_version: "1.0.0"
      required_tools: ["Bash", "Read", "Write"]
      mcp_servers: ["optional-server"]
    opencode:
      min_version: "0.5.0"
      required_tools: ["shell", "read", "write"]
    generic:
      required_tools: ["bash", "python3"]
```

---

## 6. Compatibility Testing

### 6.1 Test Matrix

```yaml
test_matrix:
  skills_tested: "Representative sample (min 3 per category)"
  platforms: ["claude-code", "opencode", "cursor", "generic"]
  test_types:
    - "Installation verification"
    - "Metadata parsing"
    - "Basic workflow execution"
    - "Tool integration"
    - "Output validation"
    - "Error handling"
```

### 6.2 Compatibility Report

```json
{
  "skill_id": "skill-id",
  "test_date": "2026-11-08",
  "platforms": {
    "claude-code": { "status": "pass", "issues": [] },
    "opencode": { "status": "pass", "issues": ["tool-x unavailable"] },
    "cursor": { "status": "partial", "issues": ["no MCP support"] },
    "generic": { "status": "pass", "issues": [] }
  },
  "overall": "compatible"
}
```

---

## 7. Versioning & Migration

### 7.1 Adapter Versioning

- Adapters versioned independently from skills
- Semantic versioning for adapters
- Breaking changes = MAJOR version

### 7.2 Skill Migration

```yaml
migration:
  - Provide migration guide for breaking changes
  - Automated migration scripts where possible
  - Deprecation notice: 2 minor versions
  - Compatibility layer during transition
```

---

## 8. Compatibility Checklist for Skill Authors

Before releasing, verify:

- [ ] SKILL.md validates on all target platforms
- [ ] Platform-specific config mappings documented
- [ ] Tool integrations have fallbacks for unavailable tools
- [ ] MCP servers marked as optional (Claude-only)
- [ ] Installation instructions provided per platform
- [ ] Tested on at least 2 platforms (1 primary + generic)
- [ ] Compatibility limitations documented in README.md
- [ ] Platform-specific docs in `docs/PLATFORM.md`

---

## 9. Future Platform Support

### Evaluation Criteria for New Platforms

1. **Market demand** - User requests, adoption metrics
2. **Technical feasibility** - API access, extension model
3. **Security model** - Compatible with our security framework
4. **Maintenance burden** - Ongoing support requirements
5. **Strategic alignment** - Fits library vision

### Adding a New Platform

1. Create adapter in `platform-adapters/new-platform/`
2. Implement discovery, installation, execution interfaces
3. Add to compatibility matrix
4. Create platform-specific documentation template
5. Add to CI/CD test matrix
6. Update skill metadata schema with platform enum

---

*This standard ensures skills work reliably across the diverse AI agent ecosystem.*