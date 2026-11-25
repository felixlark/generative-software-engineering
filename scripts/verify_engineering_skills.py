#!/usr/bin/env python3
"""Verify both GSE skills against their manifests and installed skill roots."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import re
import subprocess
from typing import Any
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
GSE = SKILLS / "generative-software-engineering"
BASELINE = SKILLS / "professional-engineering-baseline"
GSE_MANIFEST = GSE / "install-manifest.json"
BASELINE_MANIFEST = BASELINE / "install-manifest.json"
GSE_MARKERS = (
    "professional-engineering-baseline",
    "blocked(baseline-missing)",
    "../professional-engineering-baseline/SKILL.md",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def skill_files(skill_dir: Path, manifest: Path) -> dict[str, str]:
    files = {}
    for path in sorted(skill_dir.rglob("*")):
        if (
            path.is_file()
            and path != manifest
            and "__pycache__" not in path.parts
            and path.name != ".DS_Store"
        ):
            files[str(path.relative_to(skill_dir))] = digest(path)
    return files


def write_manifest(skill_dir: Path, manifest: Path, skill: str) -> dict[str, Any]:
    value = {
        "schema": "gse.skill-install-manifest/v1",
        "skill": skill,
        "version": "2026-11-25",
        "files": skill_files(skill_dir, manifest),
    }
    encoded = (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()
    manifest.write_bytes(encoded)
    return value


def read_manifest(path: Path, skill: str) -> dict[str, Any]:
    value = json.loads(path.read_text())
    if value.get("schema") != "gse.skill-install-manifest/v1":
        raise RuntimeError(f"{path}: manifest schema mismatch")
    if value.get("skill") != skill:
        raise RuntimeError(f"{path}: manifest skill mismatch")
    files = value.get("files")
    if not isinstance(files, dict):
        raise RuntimeError(f"{path}: manifest files are missing")
    return value


def check_manifest_source(skill_dir: Path, manifest_path: Path, manifest: dict[str, Any]) -> list[str]:
    errors = []
    expected = dict(manifest["files"])
    observed = skill_files(skill_dir, manifest_path)
    for relative in sorted(set(expected) | set(observed)):
        if relative not in observed:
            errors.append(f"missing source file: {skill_dir / relative}")
        elif relative not in expected:
            errors.append(f"source file is absent from manifest: {skill_dir / relative}")
        elif observed[relative] != expected[relative]:
            errors.append(f"source file hash differs from manifest: {skill_dir / relative}")
    return errors


def markdown_link_errors(skill_dir: Path, manifest: dict[str, Any]) -> list[str]:
    errors = []
    for relative in manifest["files"]:
        if not relative.endswith(".md"):
            continue
        path = skill_dir / relative
        text = path.read_text()
        text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", text, flags=re.M | re.S)
        for match in re.finditer(r"\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)", text):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            destination = Path(unquote(parsed.path))
            if not destination.is_absolute():
                destination = path.parent / destination
            if not destination.exists():
                errors.append(f"{path}: missing linked file {target}")
    return errors


def check_target(
    root: Path,
    skill: str,
    source_manifest_path: Path,
    manifest: dict[str, Any],
) -> list[str]:
    skill_dir = root / skill
    errors = []
    if not skill_dir.is_dir():
        return [f"missing installed skill: {skill_dir}"]
    target_manifest = skill_dir / "install-manifest.json"
    if not target_manifest.is_file():
        errors.append(f"missing installed manifest: {target_manifest}")
    elif digest(target_manifest) != digest(source_manifest_path):
        errors.append(f"installed manifest mismatch: {target_manifest}")
    for relative, expected in manifest["files"].items():
        target = skill_dir / relative
        if not target.is_file():
            errors.append(f"missing installed file: {target}")
        elif digest(target) != expected:
            errors.append(f"installed file hash mismatch: {target}")
    expected_paths = set(manifest["files"]) | {"install-manifest.json"}
    actual_paths = {
        str(path.relative_to(skill_dir))
        for path in skill_dir.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.name != ".DS_Store"
    }
    for extra in sorted(actual_paths - expected_paths):
        errors.append(f"unexpected installed file: {skill_dir / extra}")
    return errors


def check_gse_contract(root: Path) -> list[str]:
    skill = root / "generative-software-engineering/SKILL.md"
    route = root / "generative-software-engineering/references/skill-routing.md"
    prompt = root / "generative-software-engineering/agents/openai.yaml"
    errors = []
    if not skill.is_file():
        return [f"missing GSE skill: {skill}"]
    text = skill.read_text()
    for marker in GSE_MARKERS:
        if marker not in text:
            errors.append(f"{skill}: missing marker {marker}")
    if not (skill.parent / "../professional-engineering-baseline/SKILL.md").is_file():
        errors.append(f"{skill}: baseline link does not resolve")
    if not route.is_file():
        errors.append(f"missing GSE routing: {route}")
    else:
        route_text = route.read_text()
        for marker in ("professional-engineering-baseline", "blocked(baseline-missing)"):
            if marker not in route_text:
                errors.append(f"{route}: missing marker {marker}")
    if not prompt.is_file():
        errors.append(f"missing GSE default prompt: {prompt}")
    elif "professional-engineering-baseline" not in prompt.read_text():
        errors.append(f"{prompt}: default prompt does not reference the baseline")
    return errors


def source_state() -> tuple[str | None, list[str], bool]:
    result = subprocess.run(
        [
            "git",
            "-C",
            str(ROOT),
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "--",
            "skills",
            "scripts/verify_engineering_skills.py",
        ],
        capture_output=True,
        text=True,
    )
    dirty = [line for line in result.stdout.splitlines() if line]
    commit = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
    )
    ok = result.returncode == 0 and commit.returncode == 0
    return (commit.stdout.strip() if ok and not dirty else None, dirty, ok)


def target_status(
    target_root: Path,
    gse_manifest: dict[str, Any],
    baseline_manifest: dict[str, Any],
) -> dict[str, Any]:
    errors = []
    errors += check_target(
        target_root,
        "generative-software-engineering",
        GSE_MANIFEST,
        gse_manifest,
    )
    errors += check_target(
        target_root,
        "professional-engineering-baseline",
        BASELINE_MANIFEST,
        baseline_manifest,
    )
    errors += check_gse_contract(target_root)
    return {
        "target_root": str(target_root),
        "status": "pass" if not errors else "fail",
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-root", type=Path, action="append", default=[])
    parser.add_argument("--write-manifest", action="store_true")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    if not args.target_root and (args.receipt or not args.write_manifest):
        parser.error("at least one --target-root is required to verify installation")

    if args.write_manifest:
        gse_manifest = write_manifest(GSE, GSE_MANIFEST, "generative-software-engineering")
        baseline_manifest = write_manifest(
            BASELINE,
            BASELINE_MANIFEST,
            "professional-engineering-baseline",
        )
    else:
        gse_manifest = read_manifest(GSE_MANIFEST, "generative-software-engineering")
        baseline_manifest = read_manifest(
            BASELINE_MANIFEST,
            "professional-engineering-baseline",
        )

    errors = []
    errors += check_manifest_source(GSE, GSE_MANIFEST, gse_manifest)
    errors += check_manifest_source(BASELINE, BASELINE_MANIFEST, baseline_manifest)
    errors += check_gse_contract(SKILLS)
    errors += markdown_link_errors(GSE, gse_manifest)
    errors += markdown_link_errors(BASELINE, baseline_manifest)
    targets = [
        target_status(path.expanduser(), gse_manifest, baseline_manifest)
        for path in args.target_root
    ]
    for target in targets:
        errors.extend(target["errors"])
    commit, dirty_paths, git_ok = source_state()
    if not git_ok:
        errors.append("source is not a readable Git worktree")
    if dirty_paths:
        errors.append("source worktree is not clean")
    receipt = {
        "schema": "gse.engineering-skills-verification/v1",
        "verified_at": datetime.now(timezone.utc).isoformat(),
        "source_commit": commit,
        "source_dirty_paths": dirty_paths,
        "gse_manifest_sha256": digest(GSE_MANIFEST),
        "baseline_manifest_sha256": digest(BASELINE_MANIFEST),
        "gse_files": gse_manifest["files"],
        "baseline_files": baseline_manifest["files"],
        "targets": targets,
        "status": "pass" if not errors else "fail",
        "errors": errors,
    }
    if args.receipt:
        args.receipt.expanduser().parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(
            args.receipt.expanduser(),
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o600,
        )
        with os.fdopen(fd, "w") as stream:
            json.dump(receipt, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
    print(json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError) as error:
        print(f"verify-engineering-skills: {error}")
        raise SystemExit(1)
