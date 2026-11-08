# Configuration

This directory contains configuration files for the RAG Engineer skill.

## Files

| File | Purpose | Format |
|------|---------|--------|
| `settings.yaml` | Main skill configuration | YAML |
| `mcp.json` | MCP server registry (Claude Code) | JSON |
| `prompts/` | Prompt templates for generation, citation, verification | Markdown/Text |

## Configuration Options

### `settings.yaml`

```yaml
# Example configuration structure
embedding:
  model: "text-embedding-3-small"
  dimensions: 1536
  batch_size: 100
  provider: "openai"  # openai, cohere, voyage, huggingface
  fallback_provider: "cohere"
  fallback_model: "embed-english-v3.0"

vector_store:
  provider: "pinecone"  # pinecone, weaviate, chroma, qdrant, pgvector
  index_name: "rag-documents"
  metric: "cosine"
  namespace: "default"
  hybrid_search_enabled: true
  bm25_weight: 0.3

chunking:
  strategy: "semantic"  # fixed, semantic, recursive, parent-child
  chunk_size: 512
  chunk_overlap: 50
  min_chunk_size: 100
  parent_chunk_size: 2048

retrieval:
  top_k: 20
  rerank_top_k: 5
  rerank_model: "cohere-rerank-v3"  # cohere, cross-encoder, llm
  hybrid_search: true
  bm25_weight: 0.3
  query_rewriting: true
  max_query_expansions: 3

generation:
  model: "gpt-4-turbo-preview"
  temperature: 0.1
  max_tokens: 2000
  citation_format: "[{doc_id}]"
  require_citations: true
  verification_enabled: true
  abstention_threshold: 0.3

evaluation:
  ragas_enabled: true
  golden_set_path: "evals/golden_set.jsonl"
  metrics:
    - "faithfulness"
    - "answer_relevancy"
    - "context_precision"
    - "context_recall"
  judge_model: "gpt-4"
  sample_size: 100

production:
  caching_enabled: true
  cache_ttl: 3600
  semantic_cache_threshold: 0.95
  cost_tracking_enabled: true
  monthly_budget_usd: 1000
  alert_threshold_pct: 80
```

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | OpenAI API key | Yes | - |
| `COHERE_API_KEY` | Cohere API key | No | - |
| `VOYAGE_API_KEY` | Voyage AI API key | No | - |
| `PINECONE_API_KEY` | Pinecone API key | No | - |
| `PINECONE_ENVIRONMENT` | Pinecone environment | No | - |
| `WEAVIATE_API_KEY` | Weaviate API key | No | - |
| `WEAVIATE_URL` | Weaviate URL | No | - |
| `CHROMA_HOST` | Chroma host | No | `localhost` |
| `CHROMA_PORT` | Chroma port | No | `8000` |
| `QDRANT_URL` | Qdrant URL | No | - |
| `QDRANT_API_KEY` | Qdrant API key | No | - |

## Platform-Specific Config

- **Claude Code**: Reads `settings.yaml` directly; MCP servers from `mcp.json`
- **OpenCode**: Merged into `opencode.json` via manifest generator
- **Cursor**: Via `claude.skills` settings
- **Generic**: Manual setup

## Validation

```bash
yamllint settings.yaml
```