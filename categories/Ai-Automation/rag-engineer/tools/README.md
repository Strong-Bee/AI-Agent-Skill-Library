# Tool Integrations

This directory contains tool integration code and documentation for the RAG Engineer skill.

## Structure

| File/Directory | Purpose |
|----------------|---------|
| `document-processing/` | Document loading, parsing, chunking, enrichment |
| `embedding/` | Embedding generation, model management, batching |
| `vector-store/` | Vector DB operations, schema, migrations |
| `retrieval/` | Search, filtering, reranking, query rewriting |
| `generation/` | Prompt templates, citation, verification |
| `evaluation/` | RAGAS, custom metrics, golden set management |
| `monitoring/` | Latency, quality, cost tracking, alerting |
| `shared/` | Shared utilities across tools |
| `schemas/` | Input/output schemas for tool calls |

## Supported Tools (from SKILL.md)

### Required Tools
- **Python** - Primary implementation language
- **LangChain** - RAG chains, retrievers, document loaders
- **Vector Database** - Pinecone, Weaviate, Chroma, Qdrant, PGVector
- **Embedding API** - OpenAI, Cohere, Voyage, HuggingFace
- **RAGAS** - Standard RAG evaluation
- **Docker** - Containerization
- **Git** - Version control

### Optional Tools (with fallbacks)
- **LlamaIndex** - Fallback: LangChain for core RAG
- **LangSmith / Langfuse** - Fallback: Custom logging and evaluation
- **Unstructured.io** - Fallback: Custom document parsing
- **Reranking API** - Fallback: Local cross-encoder

## Adding a New Tool

1. Create platform-specific implementations
2. Define input/output schemas in `schemas/`
3. Add to `supported_tools` in SKILL.md
4. Document fallback procedures
5. Add tests in `../tests/integration/`