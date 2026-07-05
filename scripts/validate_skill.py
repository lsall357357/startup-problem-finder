#!/usr/bin/env python3
"""Validate the cross-agent startup-problem-finder package."""

from __future__ import annotations

import re
import sys
from pathlib import Path
import json


SKILL_NAME = "startup-problem-finder"

REQUIRED_FILES = {
    "SKILL.md",
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "agents/openai.yaml",
    "examples/test-prompts.md",
    "references/bp-screening-rubric.md",
    "references/file-input-guide.md",
    "references/follow-up-routing.md",
    "references/funding-path-map.md",
    "references/fundraising-meeting-playbook.md",
    "references/investor-question-bank.md",
    "references/narrative-recipes.md",
    "references/output-recipes.md",
    "references/restricted-finance-questions.md",
    "references/safety-rules.md",
    "references/safety.md",
    "scripts/package_skill.py",
    "scripts/validate_skill.py",
}

FORBIDDEN_PATH_NAMES = {
    ".DS_Store",
    "listing-" + "copy.md",
}

FORBIDDEN_TEXT = {
    "early-stage-startup-" + "problem-finder",
    "Red" + "Hub",
    "listing-" + "copy.md",
    "Documents/Codex/" + "media",
    "/Users/" + "lusai",
}

REQUIRED_TEXT = {
    "name: startup-problem-finder",
    "material-grounded intake",
    "value anchor",
    "business model",
    "fundraising story",
    "Do not preview",
    "references/output-recipes.md",
    "references/safety-rules.md",
}

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".txt", ".json"}
SKIP_DIRS = {".git", ".cache", "__pycache__", "dist", "tmp"}
CJK_RE = re.compile(
    "["
    "\u3400-\u4dbf"
    "\u4e00-\u9fff"
    "\uf900-\ufaff"
    "]"
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_source_files(root: Path):
    for path in root.rglob("*"):
        rel_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        if path.is_file():
            yield path


def validate_frontmatter(skill_md: Path, errors: list[str]) -> None:
    text = read_text(skill_md)
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter.")
        return
    try:
        _, frontmatter, _ = text.split("---", 2)
    except ValueError:
        errors.append("SKILL.md frontmatter is not closed.")
        return

    if f"name: {SKILL_NAME}" not in frontmatter:
        errors.append("SKILL.md frontmatter name is missing or incorrect.")
    if "description:" not in frontmatter:
        errors.append("SKILL.md frontmatter description is missing.")
    if "[TODO" in text:
        errors.append("SKILL.md contains unfinished TODO text.")


def validate_references(root: Path, errors: list[str]) -> None:
    skill_text = read_text(root / "SKILL.md")
    refs = sorted(set(re.findall(r"`(references/[^`]+\.md)`", skill_text)))
    for ref in refs:
        if not (root / ref).exists():
            errors.append(f"Missing referenced file: {ref}")

    for path in sorted((root / "references").glob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel not in skill_text:
            errors.append(f"Reference is not mapped directly from SKILL.md: {rel}")


def validate_files(root: Path, errors: list[str]) -> None:
    existing = {
        path.relative_to(root).as_posix()
        for path in iter_source_files(root)
    }
    for rel in sorted(REQUIRED_FILES - existing):
        errors.append(f"Missing required file: {rel}")

    for path in iter_source_files(root):
        rel = path.relative_to(root)
        if path.name in FORBIDDEN_PATH_NAMES:
            errors.append(f"Forbidden file present: {rel}")
        if path.suffix in {".zip", ".skill"}:
            errors.append(f"Generated archive must not be committed: {rel}")


def validate_content(root: Path, errors: list[str]) -> None:
    combined_parts: list[str] = []

    for path in iter_source_files(root):
        if path.suffix not in TEXT_SUFFIXES and path.name != "LICENSE":
            continue
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            errors.append(f"Non-UTF-8 file: {path.relative_to(root)}")
            continue

        if CJK_RE.search(text):
            errors.append(f"CJK text found: {path.relative_to(root)}")
        combined_parts.append(text)

    combined = "\n".join(combined_parts)
    for needle in sorted(FORBIDDEN_TEXT):
        if needle in combined:
            errors.append(f"Forbidden text found: {needle}")
    for needle in sorted(REQUIRED_TEXT):
        if needle not in combined:
            errors.append(f"Required text missing: {needle}")


def validate_evals(root: Path, errors: list[str]) -> None:
    evals_path = root / "evals" / "evals.json"
    if not evals_path.exists():
        return

    try:
        data = json.loads(read_text(evals_path))
    except json.JSONDecodeError as exc:
        errors.append(f"evals/evals.json is invalid JSON: {exc}")
        return

    if data.get("skill_name") != SKILL_NAME:
        errors.append("evals/evals.json skill_name is missing or incorrect.")

    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        errors.append("evals/evals.json must contain a non-empty evals list.")
        return

    seen_ids: set[str] = set()
    for index, item in enumerate(evals, start=1):
        if not isinstance(item, dict):
            errors.append(f"evals/evals.json eval #{index} must be an object.")
            continue
        eval_id = item.get("id")
        if not isinstance(eval_id, str) or not eval_id:
            errors.append(f"evals/evals.json eval #{index} is missing id.")
        elif eval_id in seen_ids:
            errors.append(f"evals/evals.json duplicate id: {eval_id}")
        else:
            seen_ids.add(eval_id)
        if not isinstance(item.get("prompt"), str) or not item["prompt"].strip():
            errors.append(f"evals/evals.json eval #{index} is missing prompt.")
        assertions = item.get("assertions")
        if not isinstance(assertions, list) or not assertions:
            errors.append(f"evals/evals.json eval #{index} must have assertions.")
        elif not all(isinstance(value, str) and value.strip() for value in assertions):
            errors.append(f"evals/evals.json eval #{index} has invalid assertions.")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors: list[str] = []

    validate_files(root, errors)
    if (root / "SKILL.md").exists():
        validate_frontmatter(root / "SKILL.md", errors)
        validate_references(root, errors)
    validate_content(root, errors)
    validate_evals(root, errors)

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Skill package validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
