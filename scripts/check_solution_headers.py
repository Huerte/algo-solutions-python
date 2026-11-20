#!/usr/bin/env python3
"""Validate the required metadata header in changed solution files."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Problem and Source are always required individually.
# The third field is satisfied by EITHER Note OR Topic — whichever is present.
REQUIRED_FIELDS = ("Problem", "Source")
THIRD_FIELD_ALTERNATIVES = ("Note", "Topic")

HEADER_PATTERN = r"^\s*(?:#|//|--|/\*+|\*)\s*{field}s?:\s*(\S.*?)\s*(?:\*/)?$"
SOLUTION_FILENAME = re.compile(r"practice\d+\.[A-Za-z0-9]+$")


def run_diff_cmd(args: list[str]) -> list[Path]:
    """Execute git diff safely and return matching solution paths."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
        )
        paths = (
            item.decode("utf-8", errors="surrogateescape")
            for item in result.stdout.split(b"\0")
            if item
        )
        return [REPO_ROOT / path for path in paths if path.startswith("solutions/")]
    except subprocess.CalledProcessError:
        return []


def changed_solution_files(base: str, head: str) -> list[Path]:
    """Return added, copied, modified, and renamed solution paths in a diff with fallbacks."""
    # 1. Direct base..head diff
    if base and head:
        paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", base, head, "--", "solutions/"])
        if paths:
            return paths

    # 2. Triple-dot merge-base diff
    if base and head:
        paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", f"{base}...{head}", "--", "solutions/"])
        if paths:
            return paths

    # 3. Fallback: HEAD~1..HEAD
    paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", "HEAD~1", "HEAD", "--", "solutions/"])
    if paths:
        return paths

    return []


def validate_file(path: Path) -> list[str]:
    """Return validation errors for a single solution file."""
    # Guard: deleted or non-existent files must be ignored
    if not path.is_file():
        return []

    errors: list[str] = []

    if not SOLUTION_FILENAME.fullmatch(path.name):
        errors.append("filename must match practice<n>.<ext>")

    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as solution:
            top_lines = [solution.readline().rstrip("\r\n") for _ in range(30)]
    except (OSError, UnicodeError) as error:
        return [f"could not read file: {error}"]

    # Check Problem and Source individually
    for field in REQUIRED_FIELDS:
        pattern = re.compile(HEADER_PATTERN.format(field=re.escape(field)), re.IGNORECASE)
        found = any(
            (m := pattern.match(line)) and m.group(1).strip()
            for line in top_lines
        )
        if not found:
            errors.append(
                f"missing or empty required header field '{field}:' "
                "(supported comment prefixes: #, //, --, or block comment *)"
            )

    # Check that at least one of Note or Topic is present and non-empty
    third_found = False
    for field in THIRD_FIELD_ALTERNATIVES:
        pattern = re.compile(HEADER_PATTERN.format(field=re.escape(field)), re.IGNORECASE)
        if any(
            (m := pattern.match(line)) and m.group(1).strip()
            for line in top_lines
        ):
            third_found = True
            break

    if not third_found:
        errors.append(
            "missing or empty 'Note:' or 'Topic:' header field — include at least one "
            "(supported comment prefixes: #, //, --, or block comment *)"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check metadata headers in solution files changed by a pull request."
    )
    parser.add_argument("--base", default="", help="Base commit SHA")
    parser.add_argument("--head", default="", help="Head commit SHA")
    args = parser.parse_args()

    files = changed_solution_files(args.base, args.head)
    # Filter to only existing files
    existing_files = [f for f in files if f.is_file()]

    if not existing_files:
        print("No solution files changed; header validation skipped.")
        return 0

    failures: dict[Path, list[str]] = {}
    for path in existing_files:
        errors = validate_file(path)
        if errors:
            failures[path] = errors

    if failures:
        print("Solution header validation failed:")
        for path, errors in sorted(failures.items(), key=lambda item: str(item[0])):
            try:
                rel = path.relative_to(REPO_ROOT)
            except ValueError:
                rel = path
            print(f"  {rel}")
            for error in errors:
                print(f"    - {error}")
        print(
            "\nEach solution must begin with these comment lines: "
            "Problem, Source, and either Note or Topic (at least one of the two).\n"
            "Example:\n"
            "  # Problem: Two Sum\n"
            "  # Source: https://leetcode.com/problems/two-sum\n"
            "  # Topic: Hash Table, Arrays"
        )
        return 1

    print(f"Validated required headers in {len(existing_files)} changed solution file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
