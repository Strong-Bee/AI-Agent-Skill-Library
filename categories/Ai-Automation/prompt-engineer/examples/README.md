# Examples

This directory contains usage examples for the Prompt Engineer skill.

## Structure

```
examples/
├── classification/
│   ├── sentiment/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── prompt.yaml
│   │   ├── eval_dataset.jsonl
│   │   └── README.md
│   └── topic-classification/
├── generation/
│   ├── sql/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── prompt.yaml
│   │   ├── schema.json
│   │   └── README.md
│   ├── code/
│   └── email/
├── reasoning/
│   ├── math/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── prompt.yaml
│   │   └── README.md
│   └── logic/
├── extraction/
│   ├── invoice/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── prompt.yaml
│   │   ├── schema.json
│   │   └── README.md
│   └── entity/
├── optimization/
│   ├── dspy-demo/
│   │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── optimize.py
│   │   ├── baseline_prompt.yaml
│   │   ├── optimized_prompt.yaml
│   │   └── README.md
│   └── opro-demo/
└── multi-model/
    ├── cross-model-port/
    │   ├── input.md
│   │   ├── context/
│   │   ├── output/
│   │   ├── prompts/
│   │   └── README.md
    └── model-comparison/
```

## Example Requirements

Each example must include:
- **Input**: Realistic user request
- **Context**: Any required context files
- **Output**: Expected deliverables (or clearly marked as illustrative)
- **Implementation**: Prompt template, evaluation dataset, code
- **README.md**: Description of what the example demonstrates

## Example Categories

| Category | Purpose |
|----------|---------|
| `classification/` | Classification tasks with structured output |
| `generation/` | Content generation (SQL, code, email, etc.) |
| `reasoning/` | Chain-of-Thought for reasoning tasks |
| `extraction/` | Structured extraction with validation |
| `optimization/` | Automated optimization demonstrations |
| `multi-model/` | Cross-model portability examples |

## Runnable vs Illustrative

- **Runnable**: Can be executed end-to-end with model APIs
- **Illustrative**: Shows expected output format/quality but not executable

Mark each example clearly in its README.md.

## Current Examples

| Example | Type | Status | Platform Tested |
|---------|------|--------|-----------------|
| classification/sentiment | Runnable | 📝 Draft | - |
| generation/sql | Runnable | 📝 Draft | - |
| reasoning/math | Runnable | 📝 Draft | - |
| extraction/invoice | Runnable | 📝 Draft | - |
| optimization/dspy-demo | Runnable | 📝 Draft | - |

## Testing Examples

Examples serve as acceptance tests. Validate:
```bash
# Run example through skill
python -m examples.classification.sentiment.run "I love this product!"
# Compare output to expected/
```

## Contributing Examples

1. Follow the structure above
2. Use realistic but anonymized data
3. Document any setup required
4. Verify output matches current skill version