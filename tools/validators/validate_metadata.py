#!/usr/bin/env python3
"""
Metadata Validation Script
Validates SKILL.md frontmatter against the JSON schema.
"""

import sys
import json
import yaml
import jsonschema
from pathlib import Path
from typing import Dict, Any, Tuple


def load_schema(schema_path: Path) -> Dict[str, Any]:
    """Load JSON schema from file."""
    with open(schema_path, 'r') as f:
        return json.load(f)


def extract_frontmatter(skill_md_path: Path) -> Tuple[Dict[str, Any], str]:
    """Extract YAML frontmatter from SKILL.md."""
    content = skill_md_path.read_text(encoding='utf-8')

    if not content.startswith('---'):
        return {}, "No YAML frontmatter found (file must start with '---')"

    try:
        # Find the closing ---
        end_idx = content.index('---', 3)
        frontmatter_str = content[3:end_idx].strip()
        frontmatter = yaml.safe_load(frontmatter_str)
        return frontmatter, ""
    except ValueError:
        return {}, "No closing '---' found for frontmatter"
    except yaml.YAMLError as e:
        return {}, f"YAML parsing error: {e}"


def validate_skill_metadata(skill_dir: Path, schema: Dict[str, Any]) -> Tuple[bool, list]:
    """Validate a single skill's metadata."""
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return False, [f"SKILL.md not found in {skill_dir}"]

    frontmatter, error = extract_frontmatter(skill_md)
    if error:
        return False, [error]

    if not frontmatter:
        return False, ["Empty or invalid frontmatter"]

    # Validate against schema
    validator = jsonschema.Draft7Validator(schema)
    errors = list(validator.iter_errors(frontmatter))

    if errors:
        error_messages = []
        for error in errors:
            path = " -> ".join(str(p) for p in error.absolute_path)
            error_messages.append(f"{path}: {error.message}")
        return False, error_messages

    return True, []


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_metadata.py <skill-directory> [--schema <schema-path>]")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    schema_path = Path(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[2] == '--schema' else Path(__file__).parent.parent.parent / "core" / "metadata-schema" / "skill-metadata.schema.json"

    if not schema_path.exists():
        print(f"Schema not found: {schema_path}")
        sys.exit(1)

    schema = load_schema(schema_path)

    if skill_dir.is_file():
        # Single skill file
        skill_dir = skill_dir.parent

    success, errors = validate_skill_metadata(skill_dir, schema)

    if success:
        print(f"✅ Metadata validation PASSED for {skill_dir.name}")
        sys.exit(0)
    else:
        print(f"❌ Metadata validation FAILED for {skill_dir.name}:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()