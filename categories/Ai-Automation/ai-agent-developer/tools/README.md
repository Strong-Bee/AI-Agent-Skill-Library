# Tool Integrations

This directory contains tool integration code and documentation for the AI Agent Developer skill.

## Structure

| File/Directory | Purpose |
|----------------|---------|
| `web-search/` | Web search tool (Tavily, SerpAPI, DuckDuckGo) |
| `file-operations/` | File read/write/list operations |
| `code-execution/` | Python/JavaScript code execution sandbox |
| `python-repl/` | Interactive Python REPL tool |
| `vector-store/` | Vector database operations (Chroma, Pinecone, FAISS) |
| `shared/` | Shared utilities across tools |
| `schemas/` | Input/output schemas for tool calls |

## Platform-Specific Implementations

Each tool may have different implementations per platform:

```
web-search/
├── claude/          # Claude Code implementation (Bash, WebSearch tool)
├── opencode/        # OpenCode tool definition
├── cursor/          # Cursor integration
├── generic/         # Generic/documentation only
└── README.md        # Tool-specific documentation
```

## Tool Documentation

Each tool integration must document:
- Setup requirements
- Configuration options
- Usage examples
- Error handling
- Fallback procedures
- Rate limits

## Supported Tools (from SKILL.md)

### Required Tools
- **Python** - Primary implementation language
- **LangChain** - LLM application components
- **Docker** - Containerization for deployment
- **Git** - Version control

### Optional Tools (with fallbacks)
- **LangGraph** - Fallback: LangChain Runnable with custom state
- **AutoGen** - Fallback: Custom orchestration or LangGraph
- **CrewAI** - Fallback: LangGraph for role-based agents
- **LangSmith** - Fallback: Langfuse or custom logging
- **Langfuse** - Fallback: Custom evaluation implementation

## Adding a New Tool

1. Create platform-specific implementations in `tool-name/{claude,opencode,cursor,generic}/`
2. Define input/output schemas in `schemas/tool-name.json`
3. Add to `supported_tools` in SKILL.md
4. Document fallback procedures
5. Add tests in `../tests/integration/`