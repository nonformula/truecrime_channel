#!/usr/bin/env python3
"""Validate and build the Codex plugin folder and distributable marketplace ZIP."""
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'src'
DEST = ROOT / 'true-crime-channel'
OUT = ROOT / 'true-crime-channel-codex.zip'


def main():
    manifest = json.loads((SRC / 'plugin.json').read_text())
    overlay = json.loads((SRC / '.codex-plugin/plugin.json').read_text())
    for key in ('name', 'version', 'description', 'author'):
        assert manifest[key] == overlay[key], f'manifest mismatch: {key}'
    assert overlay['skills'] == './skills/'
    shared = {p.name: p.read_bytes() for p in (SRC / 'shared').glob('*.md')}
    skills = sorted((SRC / 'skills').glob('*/SKILL.md'))
    assert len(skills) == 11, 'expected all 11 source workflow skills'
    files = {name: (SRC / name).read_bytes() for name in
             ('plugin.json', '.codex-plugin/plugin.json')}
    for skill in skills:
        text = skill.read_text()
        front = re.match(r'---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n', text)
        assert front and front[1] == skill.parent.name, f'invalid frontmatter: {skill}'
        for ref in re.findall(r'`references/([^`]+)`', text):
            assert ref in shared, f'missing reference: {ref}'
        for sibling in re.findall(r'\.\./([a-z-]+)/SKILL\.md', text):
            assert (SRC / 'skills' / sibling / 'SKILL.md').is_file(), sibling
        files[f'skills/{skill.parent.name}/SKILL.md'] = text.encode()
        for name, data in shared.items():
            files[f'skills/{skill.parent.name}/references/{name}'] = data
    marketplace_path = ROOT / '.agents/plugins/marketplace.json'
    marketplace = json.loads(marketplace_path.read_text())
    entry = marketplace['plugins'][0]
    assert entry['name'] == manifest['name']
    assert (ROOT / entry['source']['path']).resolve() == DEST.resolve()
    # Avoid silently retaining removed or unrelated files in the generated plugin.
    if DEST.exists():
        existing = {p.relative_to(DEST).as_posix() for p in DEST.rglob('*') if p.is_file()}
        assert not existing - files.keys(), 'unexpected files in generated folder; review before rebuilding'
    for name, data in files.items():
        path = DEST / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    package = {f'true-crime-channel/{name}': data for name, data in files.items()}
    package['.agents/plugins/marketplace.json'] = marketplace_path.read_bytes()
    package['README.md'] = (ROOT / 'README.md').read_bytes()
    tmp = OUT.with_suffix('.zip.tmp')
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(package.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 23, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(tmp) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(package)
        for name, data in package.items():
            assert archive.read(name) == data
    tmp.replace(OUT)
    print(f'Validated v{manifest["version"]}: {len(skills)} skills, {len(shared)} references per skill')
    print(f'Plugin: {DEST}\nDistribution: {OUT}')


if __name__ == '__main__':
    main()
