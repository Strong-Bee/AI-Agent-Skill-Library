# Examples

This directory contains usage examples for the RAG Engineer skill.

## Structure

```
examples/
├── basic/
│   ├── qa-system/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── ingestion_pipeline.py
│   │   ├── retrieval_pipeline.py
│   │   ├── generation_pipeline.py
│   │   └── README.md
│   └── faq-bot/
├── multi-hop/
│   ├── research/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── multi_hop_retriever.py
│   │   ├── query_decomposer.py
│   │   └── README.md
│   └── comparison/
├── code/
│   ├── technical-docs/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── hierarchical_chunker.py
│   │   ├── code_embedder.py
│   │   └── README.md
│   └── api-docs/
├── legal/
│   ├── contract-analysis/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── legal_chunker.py
│   │   ├── citation_formatter.py
│   │   └── README.md
│   └── compliance-check/
└── production/
    ├── customer-support/
    │   ├── input.md
    │   ├── context/
    │   ├── output/
    │   ├── semantic_cache.py
    │   ├── monitoring_dashboard.json
    │   ├── deployment/
    │   └── README.md
    └── internal-knowledge/
```

## Example Requirements

Each example must include:
- **Input**: Realistic user request
- **Context**: Any required context files
- **Output**: Expected deliverables (or clearly marked as illustrative)
- **Implementation**: Working pipeline code
- **README.md**: Description of what the example demonstrates

## Example Categories

| Category | Purpose |
|----------|---------|
| `basic/` | Minimal viable RAG systems (Q&A, FAQ) |
| `multi-hop/` | Complex reasoning with multi-step retrieval |
| `code/` | Code and technical documentation RAG |
| `legal/` | Legal document analysis with citations |
| `production/` | Production-ready with caching, monitoring, deployment |

## Runnable vs Illustrative

- **Runnable**: Can be executed end-to-end with model APIs
- **Illustrative**: Shows expected output format/quality but not executable

Mark each example clearly in its README.md.

## Current Examples

| Example | Type | Status | Platform Tested |
|---------|------|--------|-----------------|
| basic/qa-system | Runnable | 📝 Draft | - |
| multi-hop/research | Runnable | 📝 Draft | - |
| code/technical-docs | Runnable | 📝 Draft | - |
| legal/contract-analysis | Runnable | 📝 Draft | - |
| production/customer-support | Runnable | 📝 Draft | - |

## Testing Examples

Examples serve as acceptance tests. Validate:
```bash
# Run example through skill
python -m examples.basic.qa-system.run "What is the refund policy?"
# Compare output to expected/
```

## Contributing Examples

1. Follow the structure above
2. Use realistic but anonymized data
3. Document any setup required
4. Verify output matches current skill version