# Content Strategist

> Develop and execute content strategies that drive organic growth, engagement, and conversions across digital channels.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The Content Strategist skill provides comprehensive capabilities for developing and executing content strategies that align with business objectives, serve target audiences, and drive measurable results across digital channels.

This skill embodies the professional role of a **Content Strategist** - a specialist who bridges the gap between business goals and audience needs through strategic content planning, creation, distribution, and optimization.

## Target Audience

- **Primary**: Digital Marketers, Content Marketers, Content Strategists
- **Secondary**: Business Owners, Startups, Enterprises, SEO Specialists

## Prerequisites

- **Required tools**: Analytics (GA4+GSC), SEO Tool (Ahrefs/SEMrush), CMS, PM Tool, Writing Tool
- **Required knowledge**: Content marketing fundamentals, SEO basics, audience research, analytics
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/Content\ Strategist ~/.claude/skills/digital-marketing/Content\ Strategist
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/Content\ Strategist ~/.opencode/skills/digital-marketing/Content\ Strategist
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/digital-marketing/Content\ Strategist /your/agent/skills/
```

## Quick Start

```markdown
# Build a B2B SaaS content strategy
Use the content-strategist skill to:
1. Run content audit with Screaming Frog + analytics
2. Conduct keyword research and topic clustering
3. Build topic clusters with pillar/cluster model
4. Create quarterly editorial calendar in Notion
5. Produce pillar pages with cluster articles
6. Measure and optimize quarterly
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Content Audit & Analysis | Inventory, quality scoring, performance analysis, gap analysis, action matrix |
| Strategy Development | Mission, audiences, personas, messaging pillars, buyer journey mapping |
| Editorial Planning | Topic clusters, pillar/cluster model, editorial calendar, resource allocation |
| Content Creation & Oversight | Briefs, drafting, editing, multimedia, QA, style guide compliance |
| Distribution & Amplification | Owned/earned/paid, repurposing (atomization), email nurture |
| SEO-Content Integration | Topic clusters, keyword clustering, E-E-A-T, internal linking, refresh |
| Performance Measurement | KPIs, dashboards, attribution, ROI, refresh programs, decay detection |

## Workflow Overview

10-step workflow for content strategy:

1. **Request Analysis** - Business goals, audiences, content landscape, resources
2. **Requirement Clarification** - Content goals, audiences, formats, channels, KPIs
3. **Context Gathering** - Content audit, keywords, competitors, audience research
4. **Research** - Topics, formats, distribution, SEO opportunities
5. **Planning** - Strategy doc, editorial calendar, resource plan, workflow
6. **Task Execution** - Briefs, drafting, editing, design, publishing, distribution
7. **Validation** - 30/60/90 day performance, engagement, rankings, conversions
8. **Quality Review** - Scorecard, top/bottom analysis, decay detection, alignment
9. **Error Correction** - Refresh queue, new commissions, distribution adjustments
10. **Final Delivery** - Strategy report, updated roadmap, handoff docs

## Configuration

Key options in `config/settings.yaml`:

```yaml
analytics:
  ga4_property_id: "G-XXXXXXXX"
  gsc_property: "sc-domain:example.com"

seo:
  primary_tool: "ahrefs"
  target_keywords_per_cluster: 10-20
  pillar_word_count: 3000

content:
  cadence: "weekly"
  formats: ["blog", "video", "podcast", "infographic", "case_study", "whitepaper"]

distribution:
  owned: ["blog", "email", "website"]
  earned: ["pr", "partnerships", "guest_posts"]
  paid: ["social_ads", "native_ads"]
  repurposing: true

measurement:
  kpis: ["organic_traffic", "keyword_rankings_top10", "leads_from_content", "revenue_attribution"]
  reporting_cadence: "monthly"
```

## Examples

See `examples/` for:
- `audit/enterprise-content-audit/` - Complete audit with action matrix
- `strategy/b2b-saas-strategy/` - Full strategy with pillars and calendar
- `planning/quarterly-calendar/` - Editorial calendar with briefs
- `production/seo-optimized-guide/` - Pillar page with cluster articles
- `measurement/quarterly-report/` - Performance dashboard with insights

## Limitations

- Content ROI takes time (6-18 months for organic traction)
- Requires cross-functional collaboration (design, dev, SEO, sales)
- Resource-intensive (writers, editors, designers, videographers)
- Difficult to isolate content impact from other marketing activities
- Algorithm changes can impact distribution reach unpredictably

## Related Skills

- [SEO Specialist](../SEO%20Specialist/README.md) - Technical SEO integration
- [SEO Specialist](../SEO%20Specialist/README.md) - Keyword research for content
- [Google Ads Specialist](../Google%20Ads%20Specialist/README.md) - Paid amplification
- [Meta Ads Specialist](../Meta%20Ads%20Specialist/README.md) - Social paid distribution
- [Digital Marketing Strategist](../Digital%20Marketing%20Strategist/README.md) - Holistic strategy

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)