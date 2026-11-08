# Google Ads Specialist

> Manage and optimize Google Ads campaigns for maximum ROI across search, display, shopping, and video.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The Google Ads Specialist skill provides comprehensive capabilities for managing and optimizing Google Ads campaigns across Search, Shopping, Display, Video, and Performance Max to drive qualified traffic, leads, and sales at profitable costs.

This skill embodies the professional role of a **Google Ads Specialist** - a specialist who masters campaign types, bidding strategies, audience targeting, and conversion optimization on the Google Ads platform.

## Target Audience

- **Primary**: Digital Marketers, PPC Specialists, Business Owners
- **Secondary**: Startups, E-commerce Managers, Enterprises, Marketing Agencies

## Prerequisites

- **Required tools**: Google Ads, Google Keyword Planner, GA4, GTM
- **Required knowledge**: PPC fundamentals, keyword research, conversion tracking, bidding strategies
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/Google\ Ads\ Specialist ~/.claude/skills/digital-marketing/Google\ Ads\ Specialist
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/Google\ Ads\ Specialist ~/.opencode/skills/digital-marketing/Google\ Ads\ Specialist
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/digital-marketing/Google\ Ads\ Specialist /your/agent/skills/
```

## Quick Start

```markdown
# Build a search campaign for lead generation
Use the google-ads-specialist skill to:
1. Research keywords with Keyword Planner
2. Structure campaigns by theme and match type
3. Write responsive search ads with all extensions
4. Set up conversion tracking with GA4
5. Launch with Maximize Conversions bidding
6. Monitor and optimize after learning phase
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Search Campaign Management | Keywords, match types, ad copy, extensions, Quality Score |
| Shopping Campaign Management | Merchant Center, feed optimization, CSS, custom labels |
| Bid Management & Automation | Smart Bidding (tCPA, tROAS), portfolio bidding, rules, scripts |
| Performance Max | Asset groups, audience signals, automation, incrementality |
| Conversion Tracking | GA4 link, enhanced conversions, offline imports, value rules |
| Display & Video Campaigns | Audiences, responsive ads, YouTube formats, retargeting |
| Account Audit & Optimization | Wasted spend, A/B testing, creative optimization, budget allocation |

## Workflow Overview

10-step workflow for Google Ads:

1. **Request Analysis** - Business goals, audience, budget, competitive landscape
2. **Requirement Clarification** - Conversions, creatives, landing pages, tracking
3. **Context Gathering** - Keywords, competitors, account audit, audiences
4. **Research** - Bid strategies, targeting, creative best practices, policies
5. **Planning** - Campaign structure, budgets, targets, creative, timeline
6. **Task Execution** - Build campaigns, tracking, ads, audiences, bidding
7. **Validation** - Launch monitoring: IS, CTR, CPC, conv rate, QS, pacing
8. **Quality Review** - Performance scorecard, wasted spend, opportunities
9. **Error Correction** - Bid adjustments, negatives, ad tests, audience refinements
10. **Final Delivery** - Monthly report, optimization roadmap, handoff docs

## Configuration

Key options in `config/settings.yaml`:

| Option | Description | Default |
|--------|-------------|---------|
| `bidding.default_strategy` | Default bid strategy | `maximize_conversions` |
| `campaigns.brand_separate` | Separate brand campaigns | `true` |
| `tracking.enhanced_conversions` | Enable enhanced conversions | `true` |
| `budgets.daily_budget_method` | Budget delivery method | `standard` |

## Examples

See `examples/` for:
- `search/lead-gen/` - B2B lead generation campaign
- `shopping/ecommerce/` - Product feed and campaign structure
- `pmax/omnichannel/` - Performance Max with asset groups
- `display/retargeting/` - Dynamic remarketing setup
- `video/youtube-action/` - Video action campaign for leads

## Limitations

- Cannot guarantee specific results; auction dynamics and competition vary
- Policy restrictions limit certain industries and ad content
- Automated bidding requires sufficient conversion data (30+ conversions)
- Quality Score and ad rank depend on factors beyond direct control
- Platform changes frequently; continuous learning required

## Related Skills

- [SEO Specialist](../SEO%20Specialist/README.md) - Organic search integration
- [Meta Ads Specialist](../Meta%20Ads%20Specialist/README.md) - Social paid advertising
- [Google Ads Specialist](../Google%20Ads%20Specialist/README.md) - This skill
- [Digital Marketing Strategist](../Digital%20Marketing%20Strategist/README.md) - Holistic strategy

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)