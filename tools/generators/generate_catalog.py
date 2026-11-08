#!/usr/bin/env python3
"""
Catalog Generator
Generates catalog.json from skill directories.
"""

import sys
import json
import yaml
from pathlib import Path
from typing import Dict, Any, List


def load_skill_metadata(skill_dir: Path) -> Dict:
    """Load skill metadata from SKILL.md."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return {}

    content = skill_md.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return {}

    try:
        end_idx = content.index('---', 3)
        frontmatter_str = content[3:end_idx].strip()
        return yaml.safe_load(frontmatter_str) or {}
    except (ValueError, yaml.YAMLError):
        return {}


def scan_skills(skills_root: Path) -> List[Dict]:
    """Scan all skill directories and extract catalog info."""
    skills = []
    skill_dirs = sorted([d for d in skills_root.rglob("*") if d.is_dir() and (d / "SKILL.md").exists()])

    for skill_dir in skill_dirs:
        metadata = load_skill_metadata(skill_dir)
        if not metadata:
            continue

        identity = metadata.get('identity', {})
        skill_id = identity.get('id', '')
        if not skill_id:
            continue

        rel_path = skill_dir.relative_to(skills_root)

        # Get core competencies summary
        competencies = metadata.get('core_competencies', [])
        competency_names = [c.get('name', '') for c in competencies if c.get('name')]

        # Get required tools
        tools = metadata.get('tools_integrations', {})
        required_tools = tools.get('required_tools', [])

        skills.append({
            "id": skill_id,
            "name": identity.get('name', ''),
            "version": identity.get('version', ''),
            "description": identity.get('description', ''),
            "category": identity.get('category', ''),
            "professional_role": identity.get('professional_role', ''),
            "target_users": identity.get('target_users', []),
            "required_capabilities": identity.get('required_capabilities', []),
            "core_competencies": competency_names,
            "required_tools": required_tools,
            "maturity": identity.get('maturity', ''),
            "license": identity.get('license', ''),
            "platforms": identity.get('platforms', []),
            "tags": identity.get('tags', []),
            "path": str(rel_path)
        })

    return skills


def generate_catalog(skills_root: Path, output_path: Path = None) -> Dict[str, Any]:
    """Generate catalog from skills."""
    skills = scan_skills(skills_root)

    catalog = {
        "version": "1.0.0",
        "generated_at": __import__('datetime').datetime.utcnow().isoformat() + "Z",
        "total_skills": len(skills),
        "categories": {},
        "skills": skills
    }

    # Group by category
    for skill in skills:
        cat = skill.get('category', 'uncategorized')
        if cat not in catalog["categories"]:
            catalog["categories"][cat] = []
        catalog["categories"][cat].append(skill["id"])

    # Sort categories
    catalog["categories"] = dict(sorted(catalog["categories"].items()))

    if output_path:
        with open(output_path, 'w') as f:
            json.dump(catalog, f, indent=2)
        print(f"Catalog written to {output_path}")

    return catalog


def main():
    if len(sys.argv) < 2:
        print("Usage: generate_catalog.py <skills-root-directory> [output-path]")
        sys.exit(1)

    skills_root = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else skills_root.parent / "catalog.json"

    if not skills_root.exists():
        print(f"Skills root not found: {skills_root}")
        sys.exit(1)

    print(f"Generating catalog from {skills_root}...")
    catalog = generate_catalog(skills_root, output_path)
    print(f"Generated catalog with {catalog['total_skills']} skills across {len(catalog['categories'])} categories")


if __name__ == "__main__":
    main()