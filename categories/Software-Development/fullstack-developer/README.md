# Full-Stack Developer

> Design, build, and deploy full-stack web applications with modern technologies and best practices.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The Full-Stack Developer skill provides comprehensive capabilities for designing, building, and deploying complete web applications across frontend, backend, database, and infrastructure layers using modern technologies and best practices.

This skill embodies the professional role of a **Full-Stack Developer** - a specialist who can work across the entire technology stack and make architectural decisions that balance scalability, maintainability, and delivery speed.

## Target Audience

- **Primary**: Full-Stack Developers, Software Engineers
- **Secondary**: Frontend Developers, Backend Developers, DevOps Engineers, Technical Leads, Startup Founders

## Prerequisites

- **Required tools**: Git, VS Code/Cursor, Node.js 20+, Docker, PostgreSQL, React/Vue, Backend Framework, CI/CD Platform, Testing Framework
- **Required knowledge**: TypeScript/JavaScript, HTML/CSS, REST/GraphQL, SQL, Git, Docker basics, Testing concepts
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/software-development/fullstack-developer ~/.claude/skills/software-development/fullstack-developer
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/software-development/fullstack-developer ~/.opencode/skills/software-development/fullstack-developer
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/software-development/fullstack-developer /your/agent/skills/
```

## Quick Start

```markdown
# Build a full-stack todo application
Use the fullstack-developer skill to:
1. Design API contracts (OpenAPI) for todo CRUD operations
2. Set up Next.js frontend with TypeScript and Tailwind
3. Build Fastify backend with Prisma ORM and PostgreSQL
3. Implement JWT authentication with refresh tokens
4. Write unit, integration, and e2e tests
5. Configure GitHub Actions CI/CD pipeline
6. Deploy to Kubernetes with Helm charts
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Frontend Development | React/Next.js, TypeScript, Tailwind, State Management, Testing |
| Backend Development | Fastify/NestJS, Prisma/Drizzle, Zod, JWT/OAuth, API Design |
| Database Engineering | PostgreSQL, Migrations, Indexing, Connection Pooling, Optimization |
| API Design | REST/GraphQL, OpenAPI, Versioning, Rate Limiting, SDK Generation |
| DevOps & Deployment | Docker, Kubernetes, Terraform, GitHub Actions, Monitoring |
| Testing & Quality | Unit/Integration/E2E, Contract Testing, Mutation Testing, Static Analysis |
| Architecture Design | Monolith vs Microservices, ADRs, 12-Factor App, Scalability Patterns |

## Workflow Overview

10-step workflow for full-stack development:

1. **Request Analysis** - Feature requirements, constraints, user stories
2. **Requirement Clarification** - API contracts, data models, assumptions
3. **Context Gathering** - Codebase exploration, infrastructure, team skills
4. **Research** - Technology evaluation, library selection, benchmarks
5. **Planning** - Task breakdown, sprint plan, test strategy, rollback plan
6. **Task Execution** - Frontend, backend, database, infra, tests, docs
7. **Validation** - Test results, performance, accessibility, security
8. **Quality Review** - Code review, architecture compliance, security
9. **Error Correction** - Fix issues, re-test, update docs
10. **Final Delivery** - Production deploy, monitoring, runbook, retrospective

## Configuration

Key options in `config/settings.yaml`:

| Option | Description | Default |
|--------|-------------|---------|
| `frontend.framework` | Frontend framework | `nextjs` |
| `backend.framework` | Backend framework | `fastify` |
| `database.provider` | Database provider | `postgresql` |
| `infrastructure.orchestration` | Container orchestration | `kubernetes` |
| `quality.testing.coverage_threshold` | Code coverage target | `80` |

## Examples

See `examples/` for:
- `basic/todo-app/` - Full-stack todo with auth
- `ecommerce/shop/` - Product catalog, cart, checkout
- `saas/dashboard/` - Multi-tenant dashboard with billing
- `realtime/chat/` - WebSocket chat application
- `microservices/orders/` - Order service with events

## Limitations

- Cannot be expert in every technology; specialization exists
- Trade-offs between depth and breadth across the stack
- Legacy system constraints may limit modern practices
- Team coordination required for large-scale features
- Security expertise requires continuous learning
- Does not cover: native mobile apps, embedded systems, ML/Data engineering

## Related Skills

- [React Developer](../react-developer/README.md) - Deep React expertise
- [Backend Developer](../backend-developer/README.md) - Backend specialization
- [DevOps Engineer](../devops-engineer/README.md) - Infrastructure specialization
- [API Developer](../api-developer/README.md) - API design specialization

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)