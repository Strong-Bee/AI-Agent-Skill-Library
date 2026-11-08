#!/usr/bin/env python3
"""
Structure Validation Script
Validates that skill directories have all required files and directories.
"""

import sys
from pathlib import Path
from typing import List, Tuple


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md"
]

REQUIRED_DIRS = [
    "config",
    "knowledge",
    "workflows",
    "tools",
    "templates",
    "quality",
    "examples",
    "tests"
]

OPTIONAL_DIRS = [
    "docs"
]


def validate_skill_structure(skill_dir: Path) -> Tuple[bool, List[str], List[str]]:
    """Validate a single skill's directory structure."""
    errors = []
    warnings = []

    # Check required files
    for req_file in REQUIRED_FILES:
        file_path = skill_dir / req_file
        if not file_path.exists():
            errors.append(f"Missing required file: {req_file}")
        elif file_path.stat().st_size == 0:
            warnings.append(f"Required file is empty: {req_file}")

    # Check required directories
    for req_dir in REQUIRED_DIRS:
        dir_path = skill_dir / req_dir
        if not dir_path.exists():
            errors.append(f"Missing required directory: {req_dir}/")
        elif not dir_path.is_dir():
            errors.append(f"Path exists but is not a directory: {req_dir}/")
        elif not any(dir_path.iterdir()):
            warnings.append(f"Required directory is empty: {req_dir}/ (add README.md at minimum)")

    # Check for README.md in each required directory
    for req_dir in REQUIRED_DIRS:
        readme_path = skill_dir / req_dir / "README.md"
        if not readme_path.exists():
            warnings.append(f"Missing README.md in {req_dir}/")

    return len(errors) == 0, errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_structure.py <skill-directory>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])

    if not skill_dir.exists():
        print(f"Directory not found: {skill_dir}")
        sys.exit(1)

    if not skill_dir.is_dir():
        print(f"Path is not a directory: {skill_dir}")
        sys.exit(1)

    success, errors, warnings = validate_skill_structure(skill_dir)

    if success:
        print(f"✅ Structure validation PASSED for {skill_dir.name}")
    else:
        print(f"❌ Structure validation FAILED for {skill_dir.name}:")

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