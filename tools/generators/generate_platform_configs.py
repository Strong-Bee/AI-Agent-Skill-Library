#!/usr/bin/env python3
"""
Platform Config Generator
Generates platform-specific configuration files from skill metadata.
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


def generate_opencode_manifest(skill_dir: Path, metadata: Dict) -> Dict:
    """Generate OpenCode skill.yaml manifest."""
    identity = metadata.get('identity', {})
    tools = metadata.get('tools_integrations', {})

    manifest = {
        "name": identity.get('id', ''),
        "version": identity.get('version', ''),
        "description": identity.get('description', ''),
        "category": identity.get('category', ''),
        "tools": tools.get('required_tools', []),
        "config": {}
    }

    # Add optional tools as optional
    optional_tools = tools.get('optional_tools', [])
    if optional_tools:
        manifest["optional_tools"] = [t.get('tool', '') for t in optional_tools]

    return manifest


def generate_cursor_config(skill_dir: Path, metadata: Dict) -> Dict:
    """Generate Cursor settings snippet."""
    identity = metadata.get('identity', {})

    return {
        "claude.skills": {
            identity.get('id', ''): {
                "enabled": True,
                "config": {}
            }
        }
    }


def generate_vscode_extension(skill_dir: Path, metadata: Dict) -> Dict:
    """Generate VS Code extension package.json for GitHub Copilot."""
    identity = metadata.get('identity', {})

    return {
        "name": f"skill-{identity.get('id', '')}",
        "displayName": identity.get('name', ''),
        "description": identity.get('description', ''),
        "version": identity.get('version', ''),
        "publisher": "ai-agent-skill-library",
        "categories": ["AI"],
        "contributes": {
            "copilotSkills": [{
                "id": identity.get('id', ''),
                "name": identity.get('name', ''),
                "description": identity.get('description', '')
            }]
        },
        "scripts": {
            "vscode:prepublish": "npm run compile"
        },
        "devDependencies": {
            "@vscode/vsce": "^2.15.0"
        }
    }


def generate_mcp_config(skill_dir: Path, metadata: Dict) -> Dict:
    """Generate MCP server configuration for Claude Code."""
    tools = metadata.get('tools_integrations', {})
    mcp_integrations = tools.get('mcp_integrations', [])

    if not mcp_integrations:
        return {}

    mcp_servers = {}
    for mcp in mcp_integrations:
        server_name = mcp.get('server', '').lower().replace(' ', '-')
        mcp_servers[server_name] = {
            "command": "node",
            "args": [f"config/mcp/{server_name}/index.js"],
            "env": {}
        }

    return {"mcpServers": mcp_servers}


def generate_platform_configs(skill_dir: Path, output_dir: Path = None):
    """Generate all platform configs for a skill."""
    metadata = load_skill_metadata(skill_dir)
    if not metadata:
        print(f"No metadata found in {skill_dir}")
        return

    identity = metadata.get('identity', {})
    skill_id = identity.get('id', '')

    if output_dir is None:
        output_dir = skill_dir / "generated"
    output_dir.mkdir(parents=True, exist_ok=True)

    # OpenCode manifest
    opencode_manifest = generate_opencode_manifest(skill_dir, metadata)
    (output_dir / "skill.yaml").write_text(yaml.dump(opencode_manifest, sort_keys=False))
    print(f"Generated: {output_dir / 'skill.yaml'}")

    # Cursor config
    cursor_config = generate_cursor_config(skill_dir, metadata)
    (output_dir / "cursor-settings.json").write_text(json.dumps(cursor_config, indent=2))
    print(f"Generated: {output_dir / 'cursor-settings.json'}")

    # VS Code extension package.json
    vscode_ext = generate_vscode_extension(skill_dir, metadata)
    (output_dir / "package.json").write_text(json.dumps(vscode_ext, indent=2))
    print(f"Generated: {output_dir / 'package.json'}")

    # MCP config
    mcp_config = generate_mcp_config(skill_dir, metadata)
    if mcp_config:
        (output_dir / "mcp.json").write_text(json.dumps(mcp_config, indent=2))
        print(f"Generated: {output_dir / 'mcp.json'}")

    print(f"\nAll platform configs generated in {output_dir}")


def main():
    if len(sys.argv) < 2:
        print("Usage: generate_platform_configs.py <skill-directory> [output-directory]")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not skill_dir.exists():
        print(f"Skill directory not found: {skill_dir}")
        sys.exit(1)

    generate_platform_configs(skill_dir, output_dir)


if __name__ == "__main__":
    main()