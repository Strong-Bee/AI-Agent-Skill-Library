# Examples

This directory contains usage examples for this skill.

## Structure

```
examples/
├── basic/
│   ├── input.md          # Example user request
│   ├── context/          # Context files (if any)
│   ├── output/           # Expected deliverables
│   └── README.md         # Example description
├── advanced/
│   ├── input.md
│   ├── context/
│   ├── output/
│   └── README.md
└── edge-cases/
    ├── input.md
    ├── context/
    ├── output/
    └── README.md
```

## Example Requirements

Each example must include:
- **Input**: Realistic user request
- **Context**: Any required context files
- **Output**: Expected deliverables (or clearly marked as illustrative)
- **README.md**: Description of what the example demonstrates

## Example Categories

| Category | Purpose |
|----------|---------|
| `basic/` | Minimal viable usage |
| `advanced/` | Full feature demonstration |
| `edge-cases/` | Error handling, limits, unusual inputs |
| `integration/` | Multi-skill or platform-specific |

## Runnable vs Illustrative

- **Runnable**: Can be executed end-to-end on target platform
- **Illustrative**: Shows expected output format/quality but not executable

Mark each example clearly in its README.md.

## Testing Examples

Examples serve as acceptance tests. Validate:
```bash
# Run example through skill
# Compare output to expected/
```

## Contributing Examples

1. Follow the structure above
2. Use realistic but anonymized data
3. Document any setup required
4. Verify output matches current skill version