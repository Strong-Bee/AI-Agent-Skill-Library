#!/usr/bin/env python3
"""
Link Validation Script
Checks internal and external links in markdown files.
"""

import sys
import re
import requests
from pathlib import Path
from typing import List, Tuple, Set
from urllib.parse import urljoin, urlparse
import time


INTERNAL_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
EXTERNAL_URL_PATTERN = re.compile(r'^https?://')


def find_links(skill_dir: Path) -> List[Tuple[Path, str, str, int]]:
    """Find all markdown links in skill directory."""
    links = []
    md_files = list(skill_dir.rglob("*.md"))

    for md_file in md_files:
        content = md_file.read_text(encoding='utf-8')
        for match in INTERNAL_LINK_PATTERN.finditer(content):
            link_text = match.group(1)
            link_url = match.group(2)
            line_num = content[:match.start()].count('\n') + 1
            links.append((md_file, link_text, link_url, line_num))

    return links


def check_internal_link(skill_dir: Path, md_file: Path, link_url: str) -> Tuple[bool, str]:
    """Check if internal link target exists."""
    # Remove anchor
    url_part = link_url.split('#')[0]

    if not url_part:
        # Anchor-only link, check in same file
        return True, ""

    # Resolve relative to markdown file's directory
    target_path = (md_file.parent / url_part).resolve()

    # Check if within skill directory
    try:
        target_path.relative_to(skill_dir.resolve())
    except ValueError:
        return False, f"Link escapes skill directory: {link_url}"

    if target_path.exists():
        return True, ""
    else:
        return False, f"Target not found: {target_path}"


def check_external_link(url: str, timeout: int = 10) -> Tuple[bool, str]:
    """Check external link with HEAD request."""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        if response.status_code < 400:
            return True, ""
        else:
            return False, f"HTTP {response.status_code}"
    except requests.exceptions.Timeout:
        return False, "Timeout"
    except requests.exceptions.ConnectionError:
        return False, "Connection error"
    except requests.exceptions.RequestException as e:
        return False, str(e)


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_links.py <skill-directory> [--skip-external]")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    skip_external = '--skip-external' in sys.argv

    if not skill_dir.exists():
        print(f"Directory not found: {skill_dir}")
        sys.exit(1)

    links = find_links(skill_dir)

    if not links:
        print(f"✅ No links found in {skill_dir.name}")
        sys.exit(0)

    internal_errors = []
    external_errors = []
    external_warnings = []
    checked_external: Set[str] = set()

    print(f"Checking {len(links)} links in {skill_dir.name}...")

    for md_file, link_text, link_url, line_num in links:
        rel_file = md_file.relative_to(skill_dir)

        if EXTERNAL_URL_PATTERN.match(link_url):
            if skip_external:
                continue

            if link_url in checked_external:
                continue
            checked_external.add(link_url)

            success, error = check_external_link(link_url)
            if not success:
                external_warnings.append(f"{rel_file}:{line_num} - {link_url}: {error}")
        else:
            success, error = check_internal_link(skill_dir, md_file, link_url)
            if not success:
                internal_errors.append(f"{rel_file}:{line_num} - {link_url}: {error}")

    # Report results
    has_errors = False

    if internal_errors:
        print(f"❌ {len(internal_errors)} broken INTERNAL links:")
        for err in internal_errors:
            print(f"  - {err}")
        has_errors = True
    else:
        print(f"✅ All internal links OK")

    if not skip_external:
        if external_errors:
            print(f"❌ {len(external_errors)} broken EXTERNAL links:")
            for err in external_errors:
                print(f"  - {err}")
            has_errors = True

        if external_warnings:
            print(f"⚠️  {len(external_warnings)} external link warnings:")
            for warn in external_warnings:
                print(f"  - {warn}")
    else:
        print(f"⏭️  External link checking skipped")

    if has_errors:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()