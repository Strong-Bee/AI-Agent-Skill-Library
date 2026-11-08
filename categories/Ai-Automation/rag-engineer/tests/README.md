# Tests

This directory contains validation tests for the RAG Engineer skill.

## Structure

```
tests/
├── unit/
│   ├── test_chunking_strategies.py      # Test chunking implementations
│   ├── test_embedding_generation.py     # Test embedding pipeline
│   ├── test_vector_operations.py        # Test vector DB operations
│   ├── test_retrieval_pipeline.py       # Test search, filter, rerank
│   ├── test_citation_formatting.py      # Test citation generation
│   └── test_config_loading.py           # Test configuration parsing
├── integration/
│   ├── test_pinecone_integration.py     # Pinecone integration
│   ├── test_weaviate_integration.py     # Weaviate integration
│   ├── test_chroma_integration.py       # Chroma integration
│   ├── test_openai_embeddings.py        # OpenAI embeddings integration
│   ├── test_cohere_embeddings.py        # Cohere embeddings integration
│   ├── test_voyage_embeddings.py        # Voyage embeddings integration
│   ├── test_cohere_rerank.py            # Cohere rerank integration
│   └── test_llama_index_integration.py  # LlamaIndex integration
├── acceptance/
│   ├── test_basic_rag.py                # Basic RAG end-to-end
│   ├── test_multi_hop_rag.py            # Multi-hop retrieval
│   ├── test_hybrid_search.py            # Hybrid search (dense+BM25)
│   ├── test_reranking.py                # Reranking effectiveness
│   ├── test_citation_accuracy.py        # Citation accuracy validation
│   ├── test_hallucination_reduction.py  # Hallucination metrics
│   └── test_ragas_metrics.py            # RAGAS metric validation
├── regression/
│   └── test_issue_XXX.py                # Tests for fixed issues
├── security/
│   ├── test_pii_in_retrieval.py         # PII in retrieved context
│   ├── test_prompt_injection.py         # Prompt injection resistance
│   ├── test_data_leakage.py             # Data leakage prevention
│   └── test_access_control.py           # Access control on retrieval
├── evaluation/
│   ├── golden_set.jsonl                 # Ground truth test cases
│   ├── test_ragas_faithfulness.py       # Faithfulness metric
│   ├── test_ragas_answer_relevancy.py   # Answer relevancy metric
│   ├── test_ragas_context_precision.py  # Context precision metric
│   ├── test_ragas_context_recall.py     # Context recall metric
│   ├── test_custom_metrics.py           # Custom metrics (latency, cost)
│   └── test_statistical_significance.py # Statistical testing
├── fixtures/
│   ├── sample_documents/                # Test documents
│   ├── sample_queries/                  # Test queries
│   ├── expected_retrievals/             # Expected retrieval results
│   ├── expected_answers/                # Expected generated answers
│   └── mock_embeddings/                 # Mocked embedding responses
├── conftest.py                          # Shared test configuration
└── pytest.ini                           # Pytest configuration
```

## Test Types & Requirements

| Type | Coverage Target | Required For |
|------|-----------------|--------------|
| Unit | ≥ 80% (executable code) | All skills |
| Integration | 100% workflow steps | All skills |
| Acceptance | 100% criteria | All skills |
| Regression | 100% fixed issues | All skills |
| Security | 100% trust boundaries | Medium+ risk |

## Running Tests

```bash
# All tests
pytest tests/ -v

# Specific type
pytest tests/unit/ -v
pytest tests/integration/ -v --platform pinecone
pytest tests/acceptance/ -v

# With coverage
pytest tests/ --cov=rag --cov-report=html

# Security tests
pytest tests/security/ -v

# Evaluation tests
pytest tests/evaluation/ -v
```

## Test Data Management

- **Fixtures**: Realistic but anonymized, version-controlled
- **Factories**: For complex object generation (use `factory_boy`)
- **Snapshots**: For output format validation (use `pytest-snapshot`)
- **Contracts**: For API integration testing (use `schemathesis`)

## CI/CD Integration

Tests run automatically on:
- Pre-commit (fast subset: unit tests only)
- Pull request (full suite: unit + integration + acceptance)
- Merge to main (full + security + evaluation)
- Scheduled (regression, compatibility)

## Platform Test Harnesses

- **Claude Code**: Custom MCP test server or CLI automation
- **OpenCode**: CLI automation with JSON I/O
- **Generic**: Markdown parser + schema validator

## Writing Tests

1. Test one thing per test case
2. Use descriptive names: `test_ragas_faithfulness_above_09_on_golden_set`
3. Arrange-Act-Assert structure
4. Mock external dependencies (APIs, databases)
5. Document test purpose in docstring

## Test Configuration

```ini
# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --strict-markers --tb=short
markers =
    unit: Unit tests
    integration: Integration tests
    acceptance: Acceptance tests
    security: Security tests
    evaluation: Evaluation tests
    slow: Slow tests (>10s)
filterwarnings =
    ignore::DeprecationWarning
```