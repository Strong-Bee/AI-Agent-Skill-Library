# RAG Engineer

> Design, build, and optimize Retrieval-Augmented Generation systems for accurate, grounded LLM responses.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The RAG Engineer skill provides comprehensive capabilities for designing, building, and optimizing Retrieval-Augmented Generation (RAG) systems that combine information retrieval with LLM generation to produce accurate, grounded, and verifiable responses.

This skill embodies the professional role of a **RAG Engineer** - a specialist who designs end-to-end pipelines from document ingestion through retrieval to generation, optimizing for relevance, latency, and cost.

## Target Audience

- **Primary**: RAG Engineers, AI Agent Developers, AI Automation Engineers
- **Secondary**: ML Engineers, Data Engineers, Developers, Researchers, Technical Leads

## Prerequisites

- **Required tools**: Python 3.10+, LangChain, Vector Database, Embedding API, RAGAS, Docker, Git
- **Required knowledge**: Python proficiency, LLM fundamentals, vector search basics, information retrieval concepts
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/rag-engineer ~/.claude/skills/ai-automation/rag-engineer
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/ai-automation/rag-engineer ~/.opencode/skills/ai-automation/rag-engineer
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/ai-automation/rag-engineer /your/agent/skills/
```

## Quick Start

```markdown
# Build a document Q&A system
Use the rag-engineer skill to:
1. Ingest and chunk technical documentation
2. Generate embeddings with text-embedding-3-small
3. Index in Pinecone with cosine similarity
4. Implement hybrid search with BM25 + dense vectors
5. Add Cohere reranking for top-5 results
6. Generate answers with citations using GPT-4
7. Evaluate with RAGAS (faithfulness, answer_relevancy, context_precision, context_recall)
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| RAG Architecture Design | Design naive, modular, agentic, graph-based RAG architectures |
| Vector Store Engineering | Select, configure, optimize Pinecone, Weaviate, Chroma, Qdrant, PGVector |
| Embedding Optimization | Benchmark, select, fine-tune embeddings (OpenAI, Cohere, Voyage, BGE, E5) |
| Advanced Retrieval Strategies | Hybrid search, reranking, multi-hop, query rewriting, GraphRAG |
| Grounded Generation | Citation generation, verification loops, confidence scoring, structured output |
| RAG Evaluation | RAGAS metrics, ARES automation, golden datasets, production monitoring |
| Production Optimization | Semantic caching, quantization, cost tracking, horizontal scaling |

## Workflow Overview

10-step workflow for RAG engineering:

1. **Request Analysis** - Corpus analysis, query types, quality targets, constraints
2. **Requirement Clarification** - Functional/non-functional requirements, SLAs
3. **Context Gathering** - Corpus samples, infrastructure, team skills
4. **Research** - Embedding benchmarks, vector store comparison, retrieval strategies
5. **Planning** - Architecture, data pipeline, retrieval/generation design, evaluation plan
6. **Task Execution** - Ingestion, embedding, indexing, retrieval, generation pipelines
7. **Validation** - RAGAS metrics, failure analysis, latency/cost benchmarks
8. **Quality Review** - Retrieval quality, grounding, security, performance
9. **Error Correction** - Optimize chunking, retrieval, generation; re-evaluate
10. **Final Delivery** - Production deployment, monitoring, runbook, handoff

## Configuration

Key options in `config/settings.yaml`:

| Option | Description | Default |
|--------|-------------|---------|
| `embedding.model` | Embedding model | `text-embedding-3-small` |
| `vector_store.provider` | Vector DB provider | `pinecone` |
| `chunking.strategy` | Chunking strategy | `semantic` |
| `retrieval.top_k` | Initial retrieval count | `20` |
| `retrieval.rerank_model` | Reranking model | `cohere-rerank-v3` |
| `generation.citation_format` | Citation format | `[{doc_id}]` |
| `evaluation.metrics` | RAGAS metrics | `faithfulness, answer_relevancy, context_precision, context_recall` |

## Examples

See `examples/` for:
- `basic/qa-system/` - Document Q&A with citations
- `multi-hop/research/` - Multi-step retrieval for complex questions
- `code/technical-docs/` - Code documentation RAG with hierarchy
- `legal/contract-analysis/` - Legal document analysis with citations
- `production/customer-support/` - Production RAG with caching and monitoring

## Limitations

- Retrieval quality fundamentally limits generation quality
- Vector search is approximate; exact matches not guaranteed
- Context window limits constrain retrieved context
- Embedding model quality varies by domain/language
- Evaluation of open-ended RAG remains challenging
- Cost scales with document corpus size and query volume
- Does not cover: training embedding models from scratch, building custom vector databases

## Related Skills

- [AI Agent Developer](../ai-agent-developer/README.md) - RAG for agent knowledge
- [AI Automation Engineer](../ai-automation-engineer/README.md) - RAG in automation pipelines
- [Prompt Engineer](../prompt-engineer/README.md) - Prompts for grounded generation
- [MCP Developer](../mcp-developer/README.md) - Custom retrieval tools

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)