# Meta Ads Specialist

> Manage and optimize Meta (Facebook/Instagram) advertising campaigns for maximum ROI across feed, stories, reels, and messenger placements.

[![Maturity](https://img.shields.io/badge/Maturity-Beta-yellow)]()
[![Platform](https://img.shields.io/badge/Platform-Claude%20Code%20%7C%20OpenCode%20%7C%20Cursor%20%7C%20GitHub%20Copilot%20%7C%20Generic-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

## What This Skill Does

The Meta Ads Specialist skill provides comprehensive capabilities for managing and optimizing advertising campaigns across Meta's platforms (Facebook, Instagram, Messenger, Audience Network) to drive qualified traffic, leads, and sales at profitable costs.

This skill embodies the professional role of a **Meta Ads Specialist** - a specialist who masters campaign objectives, audience targeting, creative formats, and conversion optimization within Meta's advertising ecosystem.

## Target Audience

- **Primary**: Digital Marketers, PPC Specialists, Business Owners
- **Secondary**: Startups, E-commerce Managers, Enterprises, Marketing Agencies

## Prerequisites

- **Required tools**: Meta Ads Manager, Ads Editor, Events Manager, Meta Pixel/CAPI
- **Required knowledge**: PPC fundamentals, audience targeting, creative strategy, conversion tracking
- **Platform requirements**:
  - Claude Code ≥ 1.0.0
  - OpenCode ≥ 0.5.0
  - Cursor ≥ 0.40.0
  - Generic: Any Markdown-compatible agent

## Installation

### Claude Code / Claude Desktop
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/Meta\ Ads\ Specialist ~/.claude/skills/digital-marketing/Meta\ Ads\ Specialist
```

### OpenCode
```bash
ln -s /path/to/ai-agent-skill-library/categories/digital-marketing/Meta\ Ads\ Specialist ~/.opencode/skills/digital-marketing/Meta\ Ads\ Specialist
```

### Generic
```bash
cp -r /path/to/ai-agent-skill-library/categories/digital-marketing/Meta\ Ads\ Specialist /your/agent/skills/
```

## Quick Start

```markdown
# Build a conversion campaign for e-commerce
Use the meta-ads-specialist skill to:
1. Set up Meta Pixel and Conversions API
2. Create product catalog and dynamic ads
3. Build lookalike audiences from purchasers
4. Launch Advantage+ Shopping Campaign
5. Set up creative testing framework
6. Monitor and optimize for ROAS
```

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Campaign Structure & Strategy | CBO/ABO, funnel separation, naming conventions, budget optimization |
| Audience Targeting Mastery | Core, Custom, Lookalike, Advantage+ audiences with exclusion strategies |
| Creative Strategy & Optimization | Static, Video, Carousel, Collection, Reels, DCO, systematic testing |
| Pixel & Conversions API | Pixel, CAPI, custom events, AEM, deduplication, Event Match Quality |
| Conversion Optimization & Bidding | Smart Bidding (Cost Cap, ROAS Goal), value optimization, learning phase |
| Product Catalog & Dynamic Ads | Merchant Center, feeds, Advantage+ catalog ads, collection ads |
| Advantage+ Automation Suite | ASC, Advantage+ Creative, Advantage+ Audience, automated rules |

## Workflow Overview

10-step workflow for Meta Ads:

1. **Request Analysis** - Business goals, audience, budget, competitive landscape
2. **Requirement Clarification** - Conversions, creatives, landing pages, tracking
3. **Context Gathering** - Audience insights, competitor analysis, pixel data
4. **Research** - Audience targeting, creative trends, bidding strategies, policies
5. **Planning** - Campaign architecture, budgets, targets, creative, timeline
6. **Task Execution** - Build campaigns, audiences, creatives, bidding, tracking
7. **Validation** - Launch monitoring: delivery, CTR, CPC, CPA, ROAS, frequency
8. **Quality Review** - Performance scorecard, wasted spend, optimization ops
9. **Error Correction** - Budget shifts, audience refresh, creative rotation, bids
10. **Final Delivery** - Monthly report, optimization roadmap, handoff docs

## Configuration

Key options in `config/settings.yaml`:

```yaml
account:
  business_manager_id: "BM_ID"
  ad_account_id: "ACT_ID"
  timezone: "UTC"
  currency: "USD"

tracking:
  pixel_installed: true
  capi_enabled: true
  capi_deduplication: true
  aem_configured: true
  custom_events: ["ViewContent", "AddToCart", "InitiateCheckout", "Purchase"]

audiences:
  lookalike_sources: ["purchasers_180d", "high_value_customers", "email_subscribers"]
  lookalike_percentages: [1, 3, 5]
  advantage_plus_enabled: true

creative:
  formats: ["single_image", "video", "carousel", "collection", "reels"]
  aspect_ratios: ["1:1", "4:5", "9:16", "16:9"]
  max_frequency: 3

bidding:
  default_strategy: "lowest_cost"
  attribution_window: "7d_click_1d_view"
  conversion_window: "7d_click_1d_view"
```

## Examples

See `examples/` for:
- `prospecting/conversion/` - Cold audience conversion campaign
- `retargeting/dynamic/` - Dynamic product retargeting
- `advantage-plus/shopping/` - ASC with product catalog
- `lead-gen/instant-form/` - Lead generation with Instant Forms
- `brand/awareness/` - Brand awareness with video

## Limitations

- Cannot guarantee specific results; auction dynamics and competition vary
- iOS 14.5+ privacy changes limit tracking and attribution accuracy
- Policy restrictions limit certain industries and ad content
- Automated features (Advantage+) require sufficient conversion data
- Creative fatigue requires continuous production; platform changes frequently

## Related Skills

- [SEO Specialist](../SEO%20Specialist/README.md) - Organic search integration
- [Google Ads Specialist](../Google%20Ads%20Specialist/README.md) - Paid search integration
- [Digital Marketing Strategist](../Digital%20Marketing%20Strategist/README.md) - Holistic strategy
- [Content Strategist](../Content%20Strategist/README.md) - Creative content strategy

## License

MIT - see [LICENSE](../../../../LICENSE) file.

## Support

- Issues: [GitHub Issues](https://github.com/your-org/ai-agent-skill-library/issues)
- Discussions: [GitHub Discussions](https://github.com/your-org/ai-agent-skill-library/discussions)