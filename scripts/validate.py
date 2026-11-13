#!/usr/bin/env python3
"""Check package paths and file invariants, not scientific accuracy."""
import csv
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote
from xml.etree import ElementTree as E
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    root = Path(root)
    errors = []
    skill = root / 'skills/research-boost'
    body = (skill / 'SKILL.md').read_text()
    if not body.startswith('---\nname: research-boost\n') or 'description:' not in body.split('---')[1]:
        errors.append('Invalid skill frontmatter')
    for p in root.rglob('*.md'):
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text()):
            if re.match(r'^[a-zA-Z][\w+.-]*:', target) or target.startswith('#'):
                continue
            path = unquote(target.split('#', 1)[0].split('?', 1)[0]).strip('<>')
            if path and not (p.parent / path).exists():
                errors.append(f'Broken local link in {p.relative_to(root)}: {path}')
    config = json.loads((skill / 'artifact-template.json').read_text())
    for key in ('reference', 'preview'):
        target = (skill / config[key]).resolve()
        if not target.is_relative_to(skill.resolve()) or not target.is_file():
            errors.append('Missing or nonportable template asset: ' + key)
    manifest = json.loads((root / 'PROVENANCE.json').read_text())
    ref = skill / config['reference']
    if hashlib.sha256(ref.read_bytes()).hexdigest() != manifest['template_sha256']:
        errors.append('Template hash does not match provenance')
    ns = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
    for name, expected in [('skills/research-boost/assets/reference.pptx',46),
                           ('examples/robotics-coordination/demo.pptx',46),
                           ('slides/research-boost-intro/ResearchBoost-Introduction.pptx',12)]:
        p = root / name
        if not p.is_file():
            errors.append('Missing deck: ' + name)
            continue
        with ZipFile(p) as z:
            if z.testzip(): errors.append('Corrupt PPTX: ' + name)
            slides = [n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', n)]
            if len(slides) != expected: errors.append('Unexpected slide count: ' + name)
            text = ' '.join(t.text or '' for n in slides for t in E.fromstring(z.read(n)).findall('.//a:t',ns))
            if 'PRESENTER PERSPECTIVE' in text.upper():
                errors.append('Inherited Presenter Perspective remains in ' + name)
    for p in root.rglob('*'):
        if p.is_file() and p.suffix in {'.md','.py','.json','.yaml','.yml','.csv','.mjs'}:
            content = p.read_text(encoding='utf-8-sig')
            if '/' + 'Users/' in content or 'file' + '://' in content:
                errors.append('Machine-specific path in ' + str(p.relative_to(root)))
        if p.is_file() and p.stat().st_size >= 100_000_000:
            errors.append('File exceeds ordinary GitHub file limit: ' + str(p.relative_to(root)))
    with (root / 'examples/robotics-coordination/data/evaluation-corpus.csv').open(encoding='utf-8-sig') as f:
        if len(list(csv.DictReader(f))) != 205: errors.append('Evaluation corpus row count changed')
    return errors

if __name__ == '__main__':
    issues = validate()
    for issue in issues: print('ERROR:', issue)
    if issues: raise SystemExit(1)
    print('Package checks passed: local links, portable assets, provenance, deck counts and data shape.')
    print('Scientific claims, live URLs and application-specific rendering require separate review.')
