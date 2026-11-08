# MCP Developer

> Build Model Context Protocol servers and clients to extend AI agent capabilities with custom tools and resources.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The MCP Developer skill provides comprehensive capabilities for building Model Context Protocol (MCP) servers and clients that extend AI agents with custom tools, resources, and prompts. MCP is an open protocol for connecting AI agents to external systems.

This skill embodies the professional role of an **MCP Developer** - a specialist who implements the MCP specification to create secure, scalable integrations between AI agents and external systems.

## Target Audience

- **Primary**: Developers, AI Agent Developers, AI Automation Engineers
- **Secondary**: Platform Engineers, Integration Specialists, Backend Developers

## Prerequisites

- **Required tools**: TypeScript/Node.js, MCP TypeScript SDK, Zod, Vitest, MCP Inspector
- **Required knowledge**: JSON-RPC 2.0, TypeScript, async programming, API design
- **Platform requirements**:
  - Claude Code ≥ 1.0.0 (best MCP support)
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/mcp-developer ~/.claude/skills/ai-automation/mcp-developer
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/mcp-developer ~/.opencode/skills/ai-automation/mcp-developer
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/ai-automation/mcp-developer /your/agent/skills/
```

## Quick Start

```markdown
# Build a filesystem MCP server
Use the mcp-developer skill to:
1. Set up TypeScript project with MCP SDK
2. Implement initialize, tools/list, tools/call
3. Add file read/write/list tools with Zod schemas
4. Test with MCP Inspector
5. Deploy to Claude Code via stdio transport
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| MCP Server Development | Build compliant servers with tools, resources, prompts |
| Tool Design & Schema Engineering | Design LLM-optimized tool interfaces with validation |
| Resource & Template Management | Dynamic resources, URI templates, prompt templates |
| MCP Security Hardening | OAuth 2.1, RBAC, validation, rate limiting, audit logging |
| Transport Implementation | stdio, HTTP/SSE, WebSocket, custom transports |
| MCP Testing & Compliance | Protocol compliance tests, multi-client testing |

## Workflow Overview

10-step workflow for MCP development:

1. **Request Analysis** - Use case, target client, capabilities, security
2. **Requirement Clarification** - Tool/resource/prompt interfaces, schemas
3. **Context Gathering** - SDK selection, dependencies, deployment target
4. **Research** - Spec updates, SDK features, security patterns
5. **Planning** - Module structure, test strategy, milestones
6. **Task Execution** - Core protocol, tools, resources, prompts, transport, security
7. **Validation** - Compliance, security, performance, multi-client
8. **Quality Review** - Spec compliance, security, maintainability, docs
9. **Error Correction** - Fix issues, re-validate, update docs
10. **Final Delivery** - Package, docs, examples, monitoring, handoff

## Configuration

Key options in `config/settings.yaml`:

```yaml
server:
  name: "my-mcp-server"
  version: "1.0.0"
  transport: "stdio"
  capabilities:
    tools: true
    resources: true
    prompts: true
    logging: true

security:
  auth_enabled: false
  rate_limit: 100
  validation: "strict"

tools:
  namespace: "myapp"
  timeout_ms: 30000
  max_retries: 3
```

## Examples

See `examples/` for:
- `basic/filesystem/` - File read/write/list tools
- `api/github/` - GitHub API integration with tools
- `database/postgres/` - SQL query and schema tools
- `custom/weather/` - Weather API with caching
- `advanced/agent-tools/` - Tools for AI agent orchestration

## Limitations

- MCP specification is evolving; backward compatibility not guaranteed
- Transport implementations vary across clients
- Security model requires careful implementation
- Limited debugging tools compared to REST APIs
- Client support varies (Claude Code best, others limited)

## Related Skills

- [AI Agent Developer](../ai-agent-developer/README.md) - Uses MCP servers
- [AI Automation Engineer](../ai-automation-engineer/README.md) - Integrates MCP in workflows
- [Prompt Engineer](../prompt-engineer/README.md) - Designs prompts for MCP

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)