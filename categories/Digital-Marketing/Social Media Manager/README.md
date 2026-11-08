# Social Media Manager

> Manage and grow brand presence across social media platforms through strategic content, community engagement, and data-driven optimization.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The Social Media Manager skill provides comprehensive capabilities for managing and growing brand presence across social media platforms (Instagram, LinkedIn, Twitter/X, TikTok, Facebook, YouTube, Threads) through strategic content, community engagement, influencer partnerships, and data-driven optimization.

This skill embodies the professional role of a **Social Media Manager** - a specialist who serves as the brand's voice online, fostering relationships with audiences while driving measurable business results through organic social media.

## Target Audience

- **Primary**: Social Media Managers, Digital Marketers, Community Managers
- **Secondary**: Business Owners, Startups, Enterprises, Marketing Agencies

## Prerequisites

- **Required tools**: Scheduling Tool (Buffer/Later/Hootsuite), Native Analytics, Design Tool (Canva/Figma)
- **Required knowledge**: Social media fundamentals, platform algorithms, content creation, community management
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/Social\ Media\ Manager ~/.claude/skills/digital-marketing/Social\ Media\ Manager
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/Social\ Media\ Manager ~/.opencode/skills/digital-marketing/Social\ Media\ Manager
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/digital-marketing/Social\ Media\ Manager /your/agent/skills/
```

## Quick Start

```markdown
# Build a brand's social media presence
Use the social-media-manager skill to:
1. Audit current social profiles and competitors
2. Define content pillars and platform strategies
3. Set up scheduling tool and content calendar
4. Create content batches and schedule posts
4. Set up community management workflows
5. Launch influencer outreach program
6. Monitor and report monthly
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Platform Strategy & Optimization | Platform selection, profile optimization, algorithm understanding, platform-native content |
| Content Creation & Curation | Content pillars, batching, formats (Reels, Carousel, Stories, Articles, Threads), UGC |
| Community Management & Engagement | Engagement protocols, response SLAs, advocacy programs, crisis management |
| Social Analytics & Reporting | KPI tracking, competitive benchmarking, attribution, executive reporting |
| Influencer Marketing & Partnerships | Discovery, vetting, contracts, campaign management, ROI measurement |
| Crisis Management | Monitoring, playbooks, response templates, escalation, post-mortem |
| Paid Social Integration | Organic/paid synergy, boosting, retargeting, audience insights |

## Workflow Overview

10-step workflow for social media management:

1. **Request Analysis** - Business goals, audience, current presence, resources
2. **Requirement Clarification** - Platform goals, content needs, KPIs, governance
3. **Context Gathering** - Social audit, audience insights, competitor analysis
4. **Research** - Platform trends, competitor strategies, audience behaviors
5. **Planning** - Strategy, content pillars, calendar, workflows, budgets
6. **Task Execution** - Content creation, scheduling, engagement, monitoring
7. **Validation** - Weekly/monthly/quarterly performance measurement
8. **Quality Review** - Strategy alignment, content quality, community health
9. **Error Correction** - Content pivots, audience adjustments, budget shifts
10. **Final Delivery** - Reports, updated strategy, handoff docs

## Configuration

Key options in `config/settings.yaml`:

```yaml
platforms:
  primary: ["instagram", "linkedin"]
  secondary: ["twitter", "tiktok"]
  posting_cadence:
    instagram: "daily"
    linkedin: "3x/week"
    twitter: "daily"
    tiktok: "3x/week"

content:
  pillars: ["education", "behind_scenes", "customer_stories", "industry_insights", "product_updates"]
  formats:
    instagram: ["reels", "carousel", "story", "single_image"]
    linkedin: ["article", "single_image", "document", "video"]

engagement:
  response_sla_hours: 1
  templates_enabled: true

analytics:
  utm_template: "utm_source={{platform}}&utm_medium=social&utm_campaign={{campaign}}&utm_content={{content_id}}"
  kpis: ["follower_growth_rate", "engagement_rate", "reach", "profile_visits", "website_clicks", "conversions"]
```

## Examples

See `examples/` for:
- `strategy/brand-launch/` - Complete launch strategy with pillars and calendar
- `calendar/monthly-content-calendar/` - Monthly calendar with briefs and assets
- `campaign/ugc-campaign/` - UGC campaign with brief, assets, results
- `crisis/negative-sentiment/` - Crisis response with timeline and templates
- `influencer/micro-influencer-program/` - Micro-influencer program with tracking

## Limitations

- Organic reach continues to decline across platforms; paid support often needed
- Algorithm changes can dramatically impact reach overnight
- Resource-intensive (content creation, community management, monitoring)
- Difficult to attribute revenue directly to organic social
- Platform-specific expertise required; hard to master all platforms equally

## Related Skills

- [Content Strategist](../Content%20Strategist/README.md) - Content strategy for social
- [Meta Ads Specialist](../Meta%20Ads%20Specialist/README.md) - Paid social integration
- [Content Strategist](../Content%20Strategist/README.md) - Content strategy for social
- [Digital Marketing Strategist](../Digital%20Marketing%20Strategist/README.md) - Holistic strategy

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)