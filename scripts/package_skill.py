#!/usr/bin/env python3
"""Create an installable release archive with one top-level skill directory."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path


SKILL_NAME = "startup-problem-finder"

INCLUDED_ROOT_FILES = {
    "LICENSE",
    "README.md",
    "SECURITY.md",
    "SKILL.md",
}

INCLUDED_DIRS = {
    "agents",
    "references",
}


def should_include(path: Path, root: Path) -> bool:
    if not path.is_file():
        return False
    rel = path.relative_to(root)
    if len(rel.parts) == 1:
        return rel.name in INCLUDED_ROOT_FILES
    return rel.parts[0] in INCLUDED_DIRS


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        print("SKILL.md not found. Run from the repository root or pass its path.")
        return 1

    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    output = dist / f"{SKILL_NAME}.zip"

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            if should_include(path, root):
                rel = path.relative_to(root)
                archive.write(path, Path(SKILL_NAME) / rel)

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
