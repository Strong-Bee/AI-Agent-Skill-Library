#!/usr/bin/env python3
"""
Markdown Validation Script
Validates markdown files using markdownlint (via markdownlint-cli2 or similar).
"""

import sys
import subprocess
from pathlib import Path
from typing import List, Tuple


def run_markdownlint(skill_dir: Path) -> Tuple[bool, List[str], List[str]]:
    """Run markdownlint on all .md files in skill directory."""
    md_files = list(skill_dir.rglob("*.md"))

    if not md_files:
        return True, [], ["No markdown files found"]

    # Try markdownlint-cli2 first, then markdownlint
    commands = [
        ["npx", "markdownlint-cli2", "--config", ".markdownlint.json"] + [str(f) for f in md_files],
        ["markdownlint", "--config", ".markdownlint.json"] + [str(f) for f in md_files],
    ]

    for cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                return True, [], []
            else:
                # Parse output for errors vs warnings
                errors = []
                warnings = []
                for line in result.stdout.splitlines():
                    if ": error:" in line or "error:" in line.lower():
                        errors.append(line.strip())
                    else:
                        warnings.append(line.strip())
                return len(errors) == 0, errors, warnings
        except FileNotFoundError:
            continue
        except subprocess.TimeoutExpired:
            return False, ["markdownlint timed out"], []

    return False, ["markdownlint not installed (install with: npm install -g markdownlint-cli2)"], []


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_markdown.py <skill-directory>")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])

    if not skill_dir.exists():
        print(f"Directory not found: {skill_dir}")
        sys.exit(1)

    success, errors, warnings = run_markdownlint(skill_dir)

    if success:
        print(f"✅ Markdown validation PASSED for {skill_dir.name}")
    else:
        print(f"❌ Markdown validation FAILED for {skill_dir.name}:")

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