# SEO Specialist

> Optimize websites for search engines to increase organic visibility, traffic, and conversions.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The SEO Specialist skill provides comprehensive capabilities for optimizing websites to rank higher in search engine results pages (SERPs) for relevant queries, driving qualified organic traffic that converts. It covers technical SEO, content strategy, link building, local/international SEO, and analytics.

This skill embodies the professional role of an **SEO Specialist** - a specialist who combines technical expertise, content strategy, and analytical skills to improve visibility across search engines.

## Target Audience

- **Primary**: Digital Marketers, SEO Specialists, Business Owners
- **Secondary**: Startups, Freelancers, Enterprises, Content Creators

## Prerequisites

- **Required tools**: Ahrefs/SEMrush, Google Search Console, GA4, Screaming Frog
- **Required knowledge**: Search engine fundamentals, HTML basics, keyword research concepts, analytics
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/SEO\ Specialist ~/.claude/skills/digital-marketing/SEO\ Specialist
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/SEO\ Specialist ~/.opencode/skills/digital-marketing/SEO\ Specialist
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/digital-marketing/SEO\ Specialist /your/agent/skills/
```

## Quick Start

```markdown
# Conduct a technical SEO audit
Use the seo-specialist skill to:
1. Crawl the website with Screaming Frog
2. Analyze Google Search Console coverage report
3. Check Core Web Vitals in PageSpeed Insights
4. Review indexation, canonicalization, and schema
5. Deliver prioritized technical fix list
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Technical SEO Auditing | Crawl, indexation, Core Web Vitals, site architecture, schema |
| Keyword Research & Strategy | Keyword universe, intent classification, gap analysis, mapping |
| On-Page Optimization | Titles, headings, content, schema, internal linking, images |
| Link Building & Digital PR | Outreach, linkable assets, journalist relationships, toxic links |
| SEO Content Strategy | Topic clusters, content gaps, featured snippets, content briefs |
| Local SEO | GBP optimization, citations, reviews, local links, local schema |
| Analytics & Reporting | GA4, GSC, rank tracking, conversion attribution, forecasting |

## Workflow Overview

10-step workflow for SEO:

1. **Request Analysis** - Business goals, audience, current performance, constraints
2. **Requirement Clarification** - Scope, KPIs, priorities, assumptions
3. **Context Gathering** - Site audit, rankings, backlinks, competitors
4. **Research** - Keywords, content gaps, link prospects, algorithm updates
5. **Planning** - Technical fixes, content calendar, link campaigns, timeline
6. **Task Execution** - Technical fixes, content optimization, link building
7. **Validation** - Rankings, traffic, conversions, Core Web Vitals, ROI
8. **Quality Review** - Completeness, compliance, sustainability, scalability
9. **Error Correction** - Optimize underperformers; iterate strategy
10. **Final Delivery** - Executive report, ongoing roadmap, handoff docs

## Configuration

Key options in `config/settings.yaml`:

| Option | Description | Default |
|--------|-------------|---------|
| `tools.primary_seo_tool` | Primary SEO platform | `ahrefs` |
| `audit.frequency` | Audit frequency | `quarterly` |
| `content.min_word_count` | Minimum content length | `1500` |
| `link_building.target_dr_min` | Minimum Domain Rating | `40` |

## Examples

See `examples/` for:
- `audit/technical-seo-audit/` - Complete technical audit with fixes
- `keywords/ecommerce-research/` - Keyword universe for online store
- `content/blog-optimization/` - Content briefs and optimized articles
- `technical/schema-implementation/` - Schema markup for rich results
- `local/gbp-optimization/` - Google Business Profile optimization

## Limitations

- Cannot guarantee specific rankings; search algorithms are proprietary
- Results take time (3-12 months for competitive terms)
- Algorithm updates can impact rankings unpredictably
- Requires cross-functional collaboration for implementation
- Competitive landscapes vary significantly by industry

## Related Skills

- [Technical SEO Specialist](../technical-seo-specialist/README.md) - Deep technical SEO
- [Content Strategist](../Content\ Strategist/README.md) - Content strategy for SEO
- [Google Ads Specialist](../Google\ Ads\ Specialist/README.md) - Paid search integration
- [Digital Marketing Strategist](../Digital\ Marketing\ Strategist/README.md) - Holistic digital strategy

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)