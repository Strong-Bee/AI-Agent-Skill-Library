#!/usr/bin/env python3
"""
Duplicate Detection Script
Checks for duplicate skill IDs, competency IDs, and similar content.
"""

import sys
import json
from pathlib import Path
from typing import List, Dict, Set, Tuple
from collections import defaultdict
import hashlib


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


def get_content_hash(skill_dir: Path) -> str:
    """Get hash of skill content for similarity detection."""
    content_parts = []
    for md_file in skill_dir.rglob("*.md"):
        if md_file.name == "CHANGELOG.md":
            continue
        content_parts.append(md_file.read_text(encoding='utf-8'))
    combined = "".join(content_parts)
    return hashlib.md5(combined.encode()).hexdigest()[:16]


def check_duplicates(skills_root: Path) -> Tuple[List[str], List[str], List[str]]:
    """Check for duplicates across all skills."""
    skill_ids = {}
    competency_ids = {}
    content_hashes = {}
    errors = []
    warnings = []
    info = []

    skill_dirs = [d for d in skills_root.rglob("*") if d.is_dir() and (d / "SKILL.md").exists()]

    for skill_dir in skill_dirs:
        metadata = load_skill_metadata(skill_dir)
        if not metadata:
            continue

        skill_id = metadata.get('identity', {}).get('id', '')
        rel_path = skill_dir.relative_to(skills_root)

        # Check duplicate skill IDs
        if skill_id:
            if skill_id in skill_ids:
                errors.append(f"Duplicate skill ID '{skill_id}': {skill_ids[skill_id]} and {rel_path}")
            else:
                skill_ids[skill_id] = str(rel_path)

        # Check duplicate competency IDs within skill
        competencies = metadata.get('core_competencies', [])
        for comp in competencies:
            comp_id = comp.get('id', '')
            if comp_id:
                key = f"{skill_id}:{comp_id}"
                if comp_id in competency_ids:
                    warnings.append(f"Duplicate competency ID '{comp_id}' in {skill_id} (also in {competency_ids[comp_id]})")
                else:
                    competency_ids[comp_id] = skill_id

        # Check content similarity
        content_hash = get_content_hash(skill_dir)
        if content_hash in content_hashes:
            warnings.append(f"Similar content hash ({content_hash}): {content_hashes[content_hash]} and {rel_path}")
        else:
            content_hashes[content_hash] = str(rel_path)

    # Report unique skills found
    info.append(f"Total skills scanned: {len(skill_dirs)}")
    info.append(f"Unique skill IDs: {len(skill_ids)}")
    info.append(f"Unique competency IDs: {len(competency_ids)}")

    return errors, warnings, info


def main():
    if len(sys.argv) < 2:
        print("Usage: check_duplicates.py <skills-root-directory>")
        sys.exit(1)

    skills_root = Path(sys.argv[1])

    if not skills_root.exists():
        print(f"Directory not found: {skills_root}")
        sys.exit(1)

    print(f"Checking for duplicates in {skills_root}...")
    errors, warnings, info = check_duplicates(skills_root)

    for msg in info:
        print(f"  INFO: {msg}")

    if warnings:
        print(f"⚠️  {len(warnings)} warnings:")
        for warn in warnings:
            print(f"  - {warn}")

    if errors:
        print(f"❌ {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"✅ No duplicate errors found")
        sys.exit(0)


if __name__ == "__main__":
    main()