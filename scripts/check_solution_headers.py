#!/usr/bin/env python3
"""Validate the required metadata header in changed solution files."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

HEADER_FIELDS = ("Problem", "Source", "Note")
HEADER_LINE = r"^\s*(?:#|//)\s*{field}:\s*\S.*$"
SOLUTION_FILENAME = re.compile(r"practice\d+\.[A-Za-z0-9]+$")


def changed_solution_files(base: str, head: str) -> list[Path]:
    """Return added, copied, modified, and renamed solution paths in a diff."""
    result = subprocess.run(
        [
            "git",
            "diff",
            "--name-only",
            "-z",
            "--diff-filter=ACMR",
            base,
            head,
            "--",
            "solutions/",
        ],
        check=True,
        capture_output=True,
    )
    paths = (
        item.decode("utf-8", errors="surrogateescape")
        for item in result.stdout.split(b"\0")
        if item
    )
    return [Path(path) for path in paths if path.startswith("solutions/")]


def validate_file(path: Path) -> list[str]:
    """Return validation errors for a single solution file."""
    errors: list[str] = []

    if not SOLUTION_FILENAME.fullmatch(path.name):
        errors.append("filename must match practice<n>.<ext>")

    try:
        with path.open("r", encoding="utf-8-sig") as solution:
            header = [solution.readline().rstrip("\r\n") for _ in HEADER_FIELDS]
    except (OSError, UnicodeError) as error:
        return [f"could not read file: {error}"]

    for line_number, field in enumerate(HEADER_FIELDS, start=1):
        pattern = re.compile(HEADER_LINE.format(field=re.escape(field)))
        if not pattern.fullmatch(header[line_number - 1]):
            errors.append(
                f"line {line_number} must be a non-empty {field}: comment "
                "using # or //"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check metadata headers in solution files changed by a pull request."
    )
    parser.add_argument("--base", required=True, help="Base commit SHA")
    parser.add_argument("--head", required=True, help="Head commit SHA")
    args = parser.parse_args()

    try:
        files = changed_solution_files(args.base, args.head)
    except subprocess.CalledProcessError as error:
        print(f"Unable to determine changed solution files: {error}", file=sys.stderr)
        if error.stderr:
            print(error.stderr.decode(errors="replace"), file=sys.stderr)
        return 2

    if not files:
        print("No solution files changed; header validation skipped.")
        return 0

    failures: dict[Path, list[str]] = {}
    for path in files:
        errors = validate_file(path)
        if errors:
            failures[path] = errors

    if failures:
        print("Solution header validation failed:")
        for path, errors in sorted(failures.items(), key=lambda item: str(item[0])):
            print(f"  {path}")
            for error in errors:
                print(f"    - {error}")
        print(
            "\nEach solution must begin with three comment lines in this order: "
            "Problem, Source, and Note."
        )
        return 1

    print(f"Validated required headers in {len(files)} changed solution file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
