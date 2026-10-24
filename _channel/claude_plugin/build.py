#!/usr/bin/env python3
"""Build true-crime-channel.plugin from src/.

Copies src/shared/*.md into every skill's references/, validates the package
and writes a zip archive next to this script.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
OUT = HERE / "true-crime-channel.plugin"


def fail(msg):
    sys.exit(f"build failed: {msg}")


def main():
    manifest = json.loads((SRC / ".claude-plugin" / "plugin.json").read_text())
    for key in ("name", "version", "description"):
        if not manifest.get(key):
            fail(f"plugin.json missing {key}")

    shared = {p.name: p.read_bytes() for p in sorted((SRC / "shared").glob("*.md"))}
    skills = sorted(p for p in (SRC / "skills").iterdir() if (p / "SKILL.md").is_file())
    if not skills:
        fail("no skills found")

    files = {
        ".claude-plugin/plugin.json": (SRC / ".claude-plugin" / "plugin.json").read_bytes(),
        "README.md": (SRC / "README.md").read_bytes(),
    }
    for skill in skills:
        text = (skill / "SKILL.md").read_text()
        m = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n", text)
        if not m:
            fail(f"{skill.name}: bad frontmatter")
        if m.group(1).strip() != skill.name:
            fail(f"{skill.name}: frontmatter name is {m.group(1)!r}")
        for ref in re.findall(r"`references/([^`]+)`", text):
            if ref not in shared:
                fail(f"{skill.name}: references/{ref} not in src/shared")
        for sibling in re.findall(r"\.\./([a-z-]+)/SKILL\.md", text):
            if not (SRC / "skills" / sibling / "SKILL.md").is_file():
                fail(f"{skill.name}: routes to missing skill {sibling}")
        files[f"skills/{skill.name}/SKILL.md"] = text.encode()
        for name, data in shared.items():
            files[f"skills/{skill.name}/references/{name}"] = data

    tmp = OUT.with_suffix(".plugin.tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, data in sorted(files.items()):
            z.writestr(arc, data)
    with zipfile.ZipFile(tmp) as z:
        if z.testzip() is not None or set(z.namelist()) != set(files):
            fail("archive verification")
    tmp.replace(OUT)
    print(f"{OUT.name} v{manifest['version']}: {len(skills)} skills, "
          f"{len(shared)} shared references, {len(files)} files")


if __name__ == "__main__":
    main()
