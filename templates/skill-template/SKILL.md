---
# Universal Skill Specification Template
# Copy this file to your skill directory and fill in ALL fields
# Validate against: ../../core/metadata-schema/skill-metadata.schema.json
# Remove all comments (lines starting with #) before release

identity:
  name: "Skill Display Name"                    # REQUIRED: Human-readable name
  id: "kebab-case-skill-id"                     # REQUIRED: Unique ID, lowercase, hyphens only
  version: "1.0.0"                              # REQUIRED: Semantic version (MAJOR.MINOR.PATCH)
  description: "One-sentence description of what this skill does"  # REQUIRED: 10-500 chars
  professional_role: "Professional Role Title"  # REQUIRED: e.g., "AI Agent Developer"
  category: "category-name"                     # REQUIRED: One of 12 categories (see below)
  target_users:                                 # REQUIRED: At least one
    - "freelancers"
    - "developers"
  required_capabilities:                        # REQUIRED: At least one
    - "capability-1"
    - "capability-2"
  tags:                                         # OPTIONAL: Searchable tags
    - "tag1"
    - "tag2"
  platforms:                                    # REQUIRED: At least one
    - "claude"
    - "opencode"
    - "cursor"
    - "github-copilot"
    - "generic"
  maturity: "alpha"                             # REQUIRED: alpha, beta, stable, deprecated
  license: "MIT"                                # REQUIRED: MIT, Apache-2.0, BSD-3-Clause, CC-BY-4.0
  dependencies:                                 # OPTIONAL: Other skill IDs this depends on
    - "dependency-skill-id"

# VALID CATEGORIES (must match exactly):
# ai-automation, software-development, digital-marketing, design-creative,
# business-management, data-analytics, administration, cybersecurity-it,
# finance-accounting, ecommerce-sales, writing-communication, education-research

role_definition:
  professional_identity: "Detailed professional identity and description of the role this skill embodies"  # REQUIRED: 10+ chars
  expertise_areas:                              # REQUIRED: At least one
    - "Expertise Area 1"
    - "Expertise Area 2"
  responsibilities:                             # REQUIRED: At least one
    - "Primary responsibility 1"
    - "Primary responsibility 2"
  scope_of_work: "Clear description of what this skill covers and explicitly does NOT cover"  # REQUIRED: 20+ chars
  limitations:                                  # REQUIRED: At least one
    - "Limitation 1 (e.g., no legal advice without disclaimer)"
    - "Limitation 2 (e.g., requires human review for production deployment)"
  expected_behavior:
    tone: "professional"                        # REQUIRED: professional, collaborative, authoritative, educational
    communication_style: "step-by-step"         # REQUIRED: concise, detailed, step-by-step
    decision_making: "evidence-based"           # REQUIRED: evidence-based, best-practice, creative

core_competencies:                              # REQUIRED: At least one
  - id: "competency-id"                         # REQUIRED: kebab-case unique ID
    name: "Competency Name"                     # REQUIRED
    description: "What this competency enables the agent to do"  # REQUIRED: 10+ chars
    proficiency_level: "expert"                 # REQUIRED: expert, advanced, intermediate, basic
    measurable_outcomes:                        # REQUIRED: At least one
      - "Measurable outcome 1"
      - "Measurable outcome 2"
    prerequisites:                              # OPTIONAL
      - "Prerequisite knowledge or skill"

knowledge_base:
  fundamental_concepts:                         # REQUIRED: Array (can be empty with note)
    - concept: "Concept Name"
      description: "Clear, accurate explanation"
      references:
        - "Authoritative source 1 (URL or citation)"
        - "Authoritative source 2"
  industry_terminology:
    - term: "Term"
      definition: "Precise definition"
      context: "When/how this term is used in practice"
  professional_methodologies:
    - name: "Methodology Name"
      description: "How the methodology works"
      steps:
        - "Step 1"
        - "Step 2"
      when_to_use: "Conditions for applying this methodology"
      limitations: "Known limitations or when NOT to use"
  industry_standards:
    - standard: "Standard Name (e.g., ISO 27001, WCAG 2.1)"
      relevance: "How this standard applies to the skill's work"
      compliance_notes: "Key compliance points for practitioners"
  best_practices:
    - practice: "Practice Name"
      description: "What to do"
      rationale: "Why this practice matters"
      anti_pattern: "What to avoid (common mistake)"
  common_mistakes:
    - mistake: "Description of common mistake"
      consequence: "What goes wrong when this mistake is made"
      prevention: "How to avoid this mistake"
  practical_references:
    - title: "Reference Title"
      type: "documentation"                     # documentation, tool, template, case-study, regulation
      url: "https://authoritative-source.com"
      description: "Why this reference is valuable for this skill"

workflow:
  step_1_request_analysis:
    description: "Analyze the user's request for intent, scope, and constraints"
    inputs:
      - "User request"
      - "Available context"
    outputs:
      - "Structured requirements"
      - "Identified gaps and ambiguities"
    validation: "Checklist: intent clear? scope bounded? constraints noted?"
  
  step_2_requirement_clarification:
    description: "Clarify ambiguous requirements with targeted questions"
    inputs:
      - "Structured requirements from step 1"
      - "Identified gaps"
    outputs:
      - "Clarified requirements"
      - "Documented assumptions"
    validation: "All critical ambiguities resolved; assumptions explicit"
  
  step_3_context_gathering:
    description: "Gather relevant context from files, documentation, environment"
    inputs:
      - "Clarified requirements"
    outputs:
      - "Context package (files, docs, env info)"
      - "Missing context identified"
    validation: "Sufficient context to proceed with planning"
  
  step_4_research:
    description: "Research best practices, standards, alternatives, prior art"
    inputs:
      - "Context package"
      - "Requirements"
    outputs:
      - "Research findings with sources"
      - "Options analysis with trade-offs"
    validation: "Evidence-based recommendations; sources cited"
  
  step_5_planning:
    description: "Create detailed execution plan with steps, resources, risks"
    inputs:
      - "Research findings"
      - "Requirements"
    outputs:
      - "Execution plan (step-by-step)"
      - "Resource requirements (tools, time, access)"
      - "Risk assessment with mitigations"
    validation: "Plan complete, feasible, traceable to requirements"
  
  step_6_task_execution:
    description: "Execute the plan with quality checkpoints"
    inputs:
      - "Execution plan"
    outputs:
      - "Work products (deliverables)"
      - "Execution log (decisions, issues, deviations)"
    validation: "Checkpoints passed; deviations documented"
  
  step_7_validation:
    description: "Validate outputs against requirements and acceptance criteria"
    inputs:
      - "Work products"
      - "Requirements"
      - "Acceptance criteria"
    outputs:
      - "Validation report"
      - "Defects found (if any)"
    validation: "All acceptance criteria met; no critical defects"
  
  step_8_quality_review:
    description: "Review for professional standards, best practices, completeness"
    inputs:
      - "Work products"
      - "Validation report"
    outputs:
      - "Quality assessment (score per criterion)"
      - "Improvement suggestions"
    validation: "Meets quality threshold (≥90/100 overall, no criterion <70)"
  
  step_9_error_correction:
    description: "Fix identified issues and re-validate"
    inputs:
      - "Defects from validation"
      - "Improvement suggestions from quality review"
    outputs:
      - "Corrected work products"
      - "Re-validation report"
    validation: "No critical defects remain; quality threshold met"
  
  step_10_final_delivery:
    description: "Package and deliver final outputs with documentation"
    inputs:
      - "Corrected work products"
    outputs:
      - "Final deliverables"
      - "Delivery documentation (what was done, how to use, limitations)"
    validation: "Complete, documented, ready for intended use"

tools_integrations:
  supported_tools:                              # REQUIRED: Tools this skill works with
    - tool: "tool-name"
      type: "cli"                               # cli, api, mcp, builtin
      purpose: "What this tool is used for in this skill"
      required: true                            # true if skill cannot work without it
      version: "minimum version if applicable"
  
  required_tools:                               # REQUIRED: Array of tool names that MUST be available
    - "tool-that-must-be-available"
  
  optional_tools:                               # OPTIONAL: Nice-to-have tools with fallbacks
    - tool: "nice-to-have-tool"
      fallback: "Alternative approach if unavailable"
  
  api_integrations:                             # OPTIONAL: External APIs used
    - api: "API Name"
      auth_type: "apikey"                       # oauth, apikey, bearer, none
      scopes: ["required", "scopes"]
      rate_limits: "Documented limits (e.g., 100 req/min)"
      fallback: "Offline/degraded mode description"
  
  mcp_integrations:                             # OPTIONAL: MCP servers used (Claude Code only)
    - server: "MCP Server Name"
      capabilities: ["capability1", "capability2"]
      required: false
  
  tool_prerequisites:                           # OPTIONAL: Setup needed for tools
    - tool: "tool-name"
      setup: "Setup instructions"
      verification: "How to verify it works"
  
  authentication_requirements:                  # OPTIONAL: Credentials needed
    - service: "Service name"
      credentials_needed: ["ENV_VAR_NAME"]
      storage: "env-var"                        # env-var, vault, config-file
      rotation: "Rotation policy (e.g., 90 days)"
  
  fallback_procedures:                          # REQUIRED: At least one
    - scenario: "Tool unavailable / API down / Auth failed"
      procedure: "Step-by-step fallback procedure"
      degraded_capability: "What functionality still works"

output_standards:
  expected_deliverables:                        # REQUIRED: At least one
    - name: "Deliverable Name"
      format: "markdown"                        # markdown, json, yaml, code, document, spreadsheet
      structure: "Defined structure or reference to template"
      required: true
  
  output_structure:                             # OPTIONAL: Example structure
    report:
      sections:
        - "Executive Summary"
        - "Methodology"
        - "Findings"
        - "Recommendations"
        - "Appendices"
  
  documentation_requirements:                   # REQUIRED: At least one
    - "Inline documentation for all public interfaces"
    - "Usage examples for each major feature"
    - "Architecture decision records for significant choices"
    - "Troubleshooting guide for common issues"
  
  quality_expectations:                         # REQUIRED
    accuracy: "Factual correctness verified against authoritative sources"
    completeness: "All requirements addressed; no gaps"
    consistency: "Terminology, formatting, style consistent throughout"
    usability: "Clear, actionable, appropriate detail level for target audience"
  
  acceptance_criteria:                          # REQUIRED: At least one
    - criterion: "Specific, measurable criterion (e.g., 'All code compiles without errors')"
      verification_method: "How to verify (e.g., 'Run build command')"
      priority: "critical"                      # critical, high, medium, low

self_review:
  protocol: "ANALYZE → EXECUTE → REVIEW → DETECT → FIX → RETEST → DELIVER"
  no_fake_completion: "TODO placeholders, skipped tests, stubs = incomplete"
  bounded_retries: "Max 3 correction cycles, then escalate/report blocker"

# --- HUMAN-READABLE SECTIONS BELOW (optional but recommended) ---

# ## Overview
# Brief description of what this skill does and its value proposition.

# ## Quick Start
# Minimal example to get running immediately.

# ## Configuration
# Configuration options with examples.

# ## Workflow Details
# How the 10-step workflow applies specifically to this skill.

# ## Knowledge Base Highlights
# Key concepts, methodologies, and references for quick reference.

# ## Tools & Integrations
# Tools used, setup required, and fallback procedures.

# ## Output Examples
# Sample deliverables showing expected format and quality.

# ## Troubleshooting
# Common issues and solutions.

# ## Contributing
# Skill-specific contribution guidelines.