# Templates

This directory contains reusable templates for the RAG Engineer skill.

## Structure

| File | Purpose |
|------|---------|
| `ingestion-pipeline.j2` | Document ingestion pipeline template |
| `embedding-pipeline.j2` | Embedding generation pipeline template |
| `retrieval-pipeline.j2` | Retrieval pipeline with search/rerank template |
| `generation-prompt.j2` | Grounded generation prompt with citations |
| `verification-prompt.j2` | Answer verification prompt template |
| `evaluation-case.j2` | RAG evaluation test case template |
| `dockerfile.j2` | Dockerfile template for deployment |
| `docker-compose.j2` | Docker Compose template |
| `monitoring-dashboard.j2` | Grafana/Prometheus dashboard template |
| `variables.yaml` | Template variable definitions and defaults |

## Template Standards

- Use consistent variable naming: `{{ variable_name }}`
- Document all variables in `variables.yaml`
- Provide example rendered output
- Test with edge cases

## Variable Documentation

```yaml
# variables.yaml
corpus_path:
  description: "Path to document corpus"
  type: "string"
  required: true
  example: "./data/documents"

embedding_model:
  description: "Embedding model to use"
  type: "string"
  required: true
  default: "text-embedding-3-small"
  example: "text-embedding-3-large"

vector_store:
  description: "Vector database provider"
  type: "string"
  required: true
  default: "pinecone"
  example: "weaviate"

chunk_size:
  description: "Chunk size in tokens"
  type: "integer"
  required: true
  default: 512
  example: 1024

top_k:
  description: "Number of documents to retrieve"
  type: "integer"
  required: true
  default: 20
  example: 10

rerank_model:
  description: "Reranking model"
  type: "string"
  required: true
  default: "cohere-rerank-v3"
  example: "cross-encoder/ms-marco-MiniLM-L-6-v2"
```

## Usage

Templates are referenced in SKILL.md `output_standards.expected_deliverables` and used in workflow step 6 (execution) and step 10 (delivery).

## Testing

```bash
pip install jinja2 pyyaml
python -c "
from jinja2 import Environment, FileSystemLoader
import yaml
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('retrieval-pipeline.j2')
with open('variables.yaml') as f:
    vars = yaml.safe_load(f)
print(template.render(**vars))
"
```