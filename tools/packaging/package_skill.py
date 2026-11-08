#!/usr/bin/env python3
"""
Skill Packaging Script
Packages a skill for distribution.
"""

import sys
import json
import yaml
import shutil
import zipfile
import tarfile
from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime


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


def validate_skill_for_packaging(skill_dir: Path) -> Tuple[bool, List[str]]:
    """Validate skill is ready for packaging."""
    errors = []

    # Check required files
    for req_file in ["SKILL.md", "README.md", "CHANGELOG.md"]:
        if not (skill_dir / req_file).exists():
            errors.append(f"Missing required file: {req_file}")

    # Check required directories
    for req_dir in ["config", "knowledge", "workflows", "tools", "templates", "quality", "examples", "tests"]:
        if not (skill_dir / req_dir).exists():
            errors.append(f"Missing required directory: {req_dir}/")

    # Check metadata
    metadata = load_skill_metadata(skill_dir)
    identity = metadata.get('identity', {})

    required_fields = ['name', 'id', 'version', 'description', 'professional_role', 'category', 'target_users', 'platforms', 'maturity', 'license']
    for field in required_fields:
        if not identity.get(field):
            errors.append(f"Missing required metadata field: identity.{field}")

    # Check version format
    version = identity.get('version', '')
    if version and not __import__('re').match(r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?$', version):
        errors.append(f"Invalid version format: {version} (must be semantic version)")

    return len(errors) == 0, errors


def create_package(skill_dir: Path, output_dir: Path, formats: List[str] = None):
    """Create distribution packages for a skill."""
    if formats is None:
        formats = ["zip", "tar.gz"]

    identity = load_skill_metadata(skill_dir).get('identity', {})
    skill_id = identity.get('id', skill_dir.name)
    version = identity.get('version', '1.0.0')

    output_dir.mkdir(parents=True, exist_ok=True)

    # Files to include
    include_patterns = [
        "SKILL.md",
        "README.md",
        "CHANGELOG.md",
        "config/**",
        "knowledge/**",
        "workflows/**",
        "tools/**",
        "templates/**",
        "quality/**",
        "examples/**",
        "tests/**",
    ]

    exclude_patterns = [
        "**/__pycache__/**",
        "**/.git/**",
        "**/*.pyc",
        "**/.DS_Store",
        "**/generated/**",
        "**/node_modules/**",
    ]

    def should_include(path: Path) -> bool:
        rel = path.relative_to(skill_dir)
        rel_str = str(rel)

        # Check exclude patterns
        for pattern in exclude_patterns:
            if Path(rel_str).match(pattern):
                return False

        # Check include patterns
        for pattern in include_patterns:
            if Path(rel_str).match(pattern):
                return True

        return False

    files_to_package = [f for f in skill_dir.rglob("*") if f.is_file() and should_include(f)]

    if not files_to_package:
        print("No files to package!")
        return

    print(f"Packaging {skill_id} v{version} ({len(files_to_package)} files)")

    # Create ZIP
    if "zip" in formats:
        zip_path = output_dir / f"{skill_id}-{version}.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for file_path in files_to_package:
                arcname = file_path.relative_to(skill_dir)
                zf.write(file_path, arcname)
        print(f"Created: {zip_path}")

    # Create tar.gz
    if "tar.gz" in formats:
        tar_path = output_dir / f"{skill_id}-{version}.tar.gz"
        with tarfile.open(tar_path, 'w:gz') as tf:
            for file_path in files_to_package:
                arcname = file_path.relative_to(skill_dir)
                tf.add(file_path, arcname=str(arcname))
        print(f"Created: {tar_path}")

    # Create manifest
    manifest = {
        "skill_id": skill_id,
        "version": version,
        "packaged_at": datetime.utcnow().isoformat() + "Z",
        "files": [str(f.relative_to(skill_dir)) for f in files_to_package],
        "formats": formats
    }
    manifest_path = output_dir / f"{skill_id}-{version}-manifest.json"
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"Created: {manifest_path}")

    print(f"\nPackaging complete. Output in {output_dir}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Package a skill for distribution")
    parser.add_argument("skill_dir", help="Path to skill directory")
    parser.add_argument("-o", "--output", help="Output directory (default: ./dist)")
    parser.add_argument("-f", "--formats", nargs="+", choices=["zip", "tar.gz"], default=["zip", "tar.gz"], help="Package formats")
    parser.add_argument("--skip-validation", action="store_true", help="Skip pre-packaging validation")

    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    output_dir = Path(args.output) if args.output else Path("dist")

    if not skill_dir.exists():
        print(f"Skill directory not found: {skill_dir}")
        sys.exit(1)

    if not args.skip_validation:
        print("Validating skill...")
        valid, errors = validate_skill_for_packaging(skill_dir)
        if not valid:
            print("Validation failed:")
            for error in errors:
                print(f"  - {error}")
            sys.exit(1)
        print("Validation passed")

    create_package(skill_dir, output_dir, args.formats)


if __name__ == "__main__":
    main()