#!/usr/bin/env python3
"""
Main Skill Validation Runner
Orchestrates all validation checks for a skill.
"""

import sys
import subprocess
import json
from pathlib import Path
from typing import List, Dict, Any
import argparse


VALIDATORS = [
    ("Metadata", "validate_metadata.py"),
    ("Structure", "validate_structure.py"),
    ("Markdown", "validate_markdown.py"),
    ("Links", "validate_links.py"),
]


def run_validator(validator_script: str, skill_dir: Path, extra_args: List[str] = None) -> Dict[str, Any]:
    """Run a single validator script."""
    script_path = Path(__file__).parent / validator_script

    if not script_path.exists():
        return {
            "name": validator_script,
            "status": "error",
            "message": f"Validator script not found: {script_path}"
        }

    cmd = [sys.executable, str(script_path), str(skill_dir)]
    if extra_args:
        cmd.extend(extra_args)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return {
            "name": validator_script.replace(".py", "").replace("_", " ").title(),
            "status": "pass" if result.returncode == 0 else "fail",
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    except subprocess.TimeoutExpired:
        return {
            "name": validator_script.replace(".py", "").replace("_", " ").title(),
            "status": "error",
            "message": "Validator timed out (120s)"
        }
    except Exception as e:
        return {
            "name": validator_script.replace(".py", "").replace("_", " ").title(),
            "status": "error",
            "message": str(e)
        }


def run_duplicate_check(skills_root: Path) -> Dict[str, Any]:
    """Run duplicate check across all skills."""
    script_path = Path(__file__).parent / "check_duplicates.py"
    if not script_path.exists():
        return {"name": "Duplicate Check", "status": "skipped", "message": "Script not found"}

    cmd = [sys.executable, str(script_path), str(skills_root)]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return {
            "name": "Duplicate Check",
            "status": "pass" if result.returncode == 0 else "fail",
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    except Exception as e:
        return {"name": "Duplicate Check", "status": "error", "message": str(e)}


def run_catalog_sync(skills_root: Path, catalog_path: Path) -> Dict[str, Any]:
    """Run catalog sync validation."""
    script_path = Path(__file__).parent / "validate_catalog.py"
    if not script_path.exists():
        return {"name": "Catalog Sync", "status": "skipped", "message": "Script not found"}

    cmd = [sys.executable, str(script_path), str(skills_root), str(catalog_path)]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return {
            "name": "Catalog Sync",
            "status": "pass" if result.returncode == 0 else "fail",
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    except Exception as e:
        return {"name": "Catalog Sync", "status": "error", "message": str(e)}


def validate_single_skill(skill_dir: Path, skip_external_links: bool = False) -> Dict[str, Any]:
    """Run all validations for a single skill."""
    print(f"\n{'='*60}")
    print(f"Validating skill: {skill_dir.name}")
    print(f"{'='*60}")

    results = {
        "skill": skill_dir.name,
        "path": str(skill_dir),
        "validators": [],
        "overall": "pass"
    }

    # Run standard validators
    for name, script in VALIDATORS:
        extra_args = ["--skip-external"] if name == "Links" and skip_external_links else None
        result = run_validator(script, skill_dir, extra_args)
        results["validators"].append(result)

        status_icon = "✅" if result["status"] == "pass" else "❌" if result["status"] == "fail" else "⚠️"
        print(f"  {status_icon} {result['name']}: {result['status'].upper()}")
        if result["status"] != "pass" and result.get("stdout"):
            for line in result["stdout"].splitlines():
                print(f"    {line}")

        if result["status"] in ("fail", "error"):
            results["overall"] = "fail"

    return results


def validate_all_skills(skills_root: Path, catalog_path: Path = None, skip_external_links: bool = False) -> Dict[str, Any]:
    """Run validations for all skills."""
    skill_dirs = sorted([d for d in skills_root.rglob("*") if d.is_dir() and (d / "SKILL.md").exists()])

    if not skill_dirs:
        return {"error": "No skills found"}

    print(f"Found {len(skill_dirs)} skills to validate")

    all_results = {
        "skills": [],
        "duplicate_check": None,
        "catalog_sync": None,
        "summary": {"total": 0, "passed": 0, "failed": 0}
    }

    # Validate each skill
    for skill_dir in skill_dirs:
        result = validate_single_skill(skill_dir, skip_external_links)
        all_results["skills"].append(result)
        all_results["summary"]["total"] += 1
        if result["overall"] == "pass":
            all_results["summary"]["passed"] += 1
        else:
            all_results["summary"]["failed"] += 1

    # Run duplicate check
    print(f"\n{'='*60}")
    print("Running duplicate check across all skills...")
    print(f"{'='*60}")
    all_results["duplicate_check"] = run_duplicate_check(skills_root)

    # Run catalog sync if catalog provided
    if catalog_path and catalog_path.exists():
        print(f"\n{'='*60}")
        print("Running catalog synchronization check...")
        print(f"{'='*60}")
        all_results["catalog_sync"] = run_catalog_sync(skills_root, catalog_path)

    return all_results


def main():
    parser = argparse.ArgumentParser(description="Validate skill(s) in the AI Agent Skill Library")
    parser.add_argument("path", help="Skill directory or skills root directory")
    parser.add_argument("--all", action="store_true", help="Validate all skills in directory tree")
    parser.add_argument("--catalog", help="Path to catalog.json for sync validation")
    parser.add_argument("--skip-external-links", action="store_true", help="Skip external link checking")
    parser.add_argument("--output", help="Output results to JSON file")
    parser.add_argument("--quiet", action="store_true", help="Suppress detailed output")

    args = parser.parse_args()

    path = Path(args.path)

    if not path.exists():
        print(f"Path not found: {path}")
        sys.exit(1)

    if args.all or path.name == "categories":
        # Validate all skills
        skills_root = path if path.name == "categories" else path
        catalog_path = Path(args.catalog) if args.catalog else skills_root.parent / "catalog.json"

        results = validate_all_skills(skills_root, catalog_path, args.skip_external_links)

        if "error" in results:
            print(results["error"])
            sys.exit(1)

        # Print summary
        print(f"\n{'='*60}")
        print("VALIDATION SUMMARY")
        print(f"{'='*60}")
        print(f"Total skills: {results['summary']['total']}")
        print(f"Passed: {results['summary']['passed']}")
        print(f"Failed: {results['summary']['failed']}")

        if results["duplicate_check"]:
            status = "✅" if results["duplicate_check"]["status"] == "pass" else "❌"
            print(f"{status} Duplicate Check: {results['duplicate_check']['status'].upper()}")

        if results["catalog_sync"]:
            status = "✅" if results["catalog_sync"]["status"] == "pass" else "❌"
            print(f"{status} Catalog Sync: {results['catalog_sync']['status'].upper()}")

        overall = "pass" if results["summary"]["failed"] == 0 else "fail"
        if results["duplicate_check"] and results["duplicate_check"]["status"] != "pass":
            overall = "fail"
        if results["catalog_sync"] and results["catalog_sync"]["status"] != "pass":
            overall = "fail"

        print(f"\nOverall: {overall.upper()}")

        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"\nResults written to {args.output}")

        sys.exit(0 if overall == "pass" else 1)

    else:
        # Validate single skill
        result = validate_single_skill(path, args.skip_external_links)

        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"\nResults written to {args.output}")

        sys.exit(0 if result["overall"] == "pass" else 1)


if __name__ == "__main__":
    main()