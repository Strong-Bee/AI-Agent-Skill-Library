# React Developer

> Build performant, accessible, and scalable user interfaces with React and its ecosystem.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The React Developer skill provides comprehensive capabilities for building performant, accessible, and scalable user interfaces with React and its ecosystem. It covers component architecture, state management, performance optimization, testing, TypeScript, and server-side rendering.

This skill embodies the professional role of a **React Developer** - a specialist who creates reusable component architectures, manages complex state, optimizes performance, and ensures accessibility and maintainability across large-scale applications.

## Target Audience

- **Primary**: React Developers, Frontend Developers
- **Secondary**: Full-Stack Developers, UI Engineers, Technical Leads, Startup Founders

## Prerequisites

- **Required tools**: VS Code/Cursor, Vite/Next.js, TypeScript, Vitest/Jest, React Testing Library, ESLint/Prettier, Styling Solution
- **Required knowledge**: React fundamentals, TypeScript, HTML/CSS, JavaScript, Testing concepts
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/software-development/react-developer ~/.claude/skills/software-development/react-developer
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/software-development/react-developer ~/.opencode/skills/software-development/react-developer
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/software-development/react-developer /your/agent/skills/
```

## Quick Start

```markdown
# Build a reusable component library
Use the react-developer skill to:
1. Design component APIs with TypeScript
2. Implement with React Testing Library tests
3. Document in Storybook with controls
4. Add visual regression testing
5. Ensure WCAG 2.1 AA accessibility
6. Optimize bundle size and performance
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Component Architecture | Atomic design, compound components, render props, HOCs, Server Components |
| State Management | useState, useReducer, Context, Zustand, Redux, React Query, optimistic updates |
| Performance Optimization | Memoization, code splitting, virtualization, bundle analysis, streaming SSR |
| TypeScript | Generics, utility types, strict mode, component prop types |
| Testing | RTL, Vitest, Playwright, MSW, visual regression, axe-core |
| SSR/SSG | Next.js App Router, ISR, streaming, edge runtime, middleware |
| Accessibility | Semantic HTML, ARIA, focus management, screen readers, WCAG 2.1 AA |

## Workflow Overview

10-step workflow for React development:

1. **Request Analysis** - Designs, user flows, responsive, accessibility, performance
2. **Requirement Clarification** - Component APIs, state ownership, data contracts
3. **Context Gathering** - Codebase, design system, conventions, tooling
4. **Research** - Patterns, libraries, performance, accessibility
5. **Planning** - Component order, dependencies, testing, milestones
6. **Task Execution** - Components, hooks, tests, stories, docs
7. **Validation** - Visual regression, a11y, performance, cross-browser
8. **Quality Review** - Code review, bundle size, types, tests, ADRs
9. **Error Correction** - Fix feedback, optimize, fix a11y, update tests
10. **Final Delivery** - Deploy, Storybook, docs, monitoring, handoff

## Configuration

Key options in `config/settings.yaml`:

| Option | Description | Default |
|--------|-------------|---------|
| `framework.build_tool` | Build tool | `vite` |
| `framework.styling` | Styling solution | `tailwind` |
| `testing.coverage_threshold` | Code coverage target | `80` |
| `performance.bundle_budget_kb` | Bundle size budget | `50` |

## Examples

See `examples/` for:
- `components/button/` - Polymorphic button with variants, loading, a11y
- `forms/login/` - Form with validation, error handling, submission states
- `data-table/` - Virtualized table with sorting, filtering, pagination
- `hooks/use-debounce/` - Custom hook with tests and documentation
- `nextjs/app-router/` - SSR/SSG/ISR with App Router patterns

## Limitations

- React ecosystem evolves rapidly; patterns change frequently
- Performance optimization requires deep understanding of React internals
- State management choices have significant architectural impact
- Testing complex interactions can be challenging
- Accessibility requires continuous attention and testing
- Does not cover: backend API development, database design, DevOps infrastructure

## Related Skills

- [Full-Stack Developer](../fullstack-developer/README.md) - End-to-end development
- [Frontend Developer](../frontend-developer/README.md) - General frontend
- [TypeScript Developer](../typescript-developer/README.md) - TypeScript expertise
- [UI/UX Designer](../UI%20UX%20Designer/README.md) - Design collaboration

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)