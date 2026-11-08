#!/usr/bin/env python3
"""
Catalog Synchronization Script
Validates that catalog.json matches actual skill directories.
"""

import sys
import json
from pathlib import Path
from typing import List, Tuple, Dict, Any


def load_catalog(catalog_path: Path) -> Dict[str, Any]:
    """Load catalog.json."""
    if not catalog_path.exists():
        return {}
    with open(catalog_path, 'r') as f:
        return json.load(f)


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
        import yaml
        return yaml.safe_load(frontmatter_str) or {}
    except (ValueError, yaml.YAMLError):
        return {}


def scan_skills(skills_root: Path) -> Dict[str, Dict]:
    """Scan all skill directories and extract catalog info."""
    skills = {}
    skill_dirs = [d for d in skills_root.rglob("*") if d.is_dir() and (d / "SKILL.md").exists()]

    for skill_dir in skill_dirs:
        metadata = load_skill_metadata(skill_dir)
        if not metadata:
            continue

        identity = metadata.get('identity', {})
        skill_id = identity.get('id', '')
        if not skill_id:
            continue

        rel_path = skill_dir.relative_to(skills_root)

        skills[skill_id] = {
            "id": skill_id,
            "name": identity.get('name', ''),
            "version": identity.get('version', ''),
            "description": identity.get('description', ''),
            "category": identity.get('category', ''),
            "professional_role": identity.get('professional_role', ''),
            "maturity": identity.get('maturity', ''),
            "platforms": identity.get('platforms', []),
            "tags": identity.get('tags', []),
            "path": str(rel_path)
        }

    return skills


def validate_catalog_sync(skills_root: Path, catalog_path: Path) -> Tuple[bool, List[str], List[str]]:
    """Validate catalog matches actual skills."""
    errors = []
    warnings = []

    # Load catalog
    catalog = load_catalog(catalog_path)
    catalog_skills = {s['id']: s for s in catalog.get('skills', [])}

    # Scan actual skills
    actual_skills = scan_skills(skills_root)

    # Check for skills in catalog but not on disk
    for skill_id, catalog_skill in catalog_skills.items():
        if skill_id not in actual_skills:
            errors.append(f"Skill in catalog but not found on disk: {skill_id} (catalog path: {catalog_skill.get('path', 'unknown')})")
        else:
            # Check version match
            actual_skill = actual_skills[skill_id]
            if catalog_skill.get('version') != actual_skill.get('version'):
                warnings.append(f"Version mismatch for {skill_id}: catalog={catalog_skill.get('version')}, actual={actual_skill.get('version')}")

    # Check for skills on disk but not in catalog
    for skill_id, actual_skill in actual_skills.items():
        if skill_id not in catalog_skills:
            warnings.append(f"Skill on disk but not in catalog: {skill_id} ({actual_skill['path']})")

    return len(errors) == 0, errors, warnings


def main():
    if len(sys.argv) < 3:
        print("Usage: validate_catalog.py <skills-root-directory> <catalog-path>")
        sys.exit(1)

    skills_root = Path(sys.argv[1])
    catalog_path = Path(sys.argv[2])

    if not skills_root.exists():
        print(f"Skills root not found: {skills_root}")
        sys.exit(1)

    print(f"Validating catalog sync...")
    success, errors, warnings = validate_catalog_sync(skills_root, catalog_path)

    if success:
        print(f"✅ Catalog sync validation PASSED")
    else:
        print(f"❌ Catalog sync validation FAILED:")

    for error in errors:
        print(f"  ERROR: {error}")

    for warning in warnings:
        print(f"  WARNING: {warning}")

    if errors:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()