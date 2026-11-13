#!/usr/bin/env python3
"""Install a complete local skill without replacing an existing destination."""
import argparse
from pathlib import Path
import shutil
import sys

REPO = Path(__file__).resolve().parents[1]

def install(source, destination):
    source, destination = Path(source).resolve(), Path(destination).expanduser()
    if not (source / 'SKILL.md').is_file():
        raise ValueError('Source is not a skill directory')
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('Destination already exists: ' + str(destination))
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return destination

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument('--project', type=Path, help='Research project to receive .agents/skills/research-boost')
    scope.add_argument('--user', action='store_true', help='Install into ~/.agents/skills/research-boost')
    args = parser.parse_args()
    destination = ((args.project.expanduser().resolve() / '.agents/skills/research-boost')
                   if args.project else Path.home() / '.agents/skills/research-boost')
    try:
        result = install(REPO / 'skills/research-boost', destination)
    except (ValueError, OSError) as error:
        print('Installation stopped: ' + str(error), file=sys.stderr)
        return 1
    print('Installed ResearchBoost into ' + str(result))
    print('Open the research project in Codex and invoke $research-boost. Restart if absent.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
