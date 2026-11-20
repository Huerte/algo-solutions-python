#!/usr/bin/env python3
"""Automatically create a GitHub issue when a solution with Status: IN PROGRESS is merged or pushed."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOLUTIONS_DIR = REPO_ROOT / "solutions"

IN_PROGRESS_PATTERN = re.compile(
    r"""
    ^\s*(?:#|//|--|/\*+|\*)\s*               # Comment indicator
    (?:[^\w\s]\s*)?                          # Optional leading emoji (e.g. 🔄, 🚧, ⏳)
    (?:status\s*[:\-—–]?\s*.*?)?             # Optional 'status:' prefix
    \b(in[-_\s]?progress|wip|work[-_\s]in[-_\s]progress|needs[-_\s]work|incomplete|unfinished|unsolved|todo)\b
    """,
    re.IGNORECASE | re.VERBOSE,
)

SOLVED_PATTERN = re.compile(
    r"\b(solved|done|complete|completed|passed|fixed)\b",
    re.IGNORECASE,
)


def run_git(*args: str) -> list[str]:
    """Execute git command safely and return stripped output lines."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Git command failed ('git {' '.join(args)}'): {e}", file=sys.stderr)
        return []


def is_valid_commit(sha: str | None) -> bool:
    """Check if a commit SHA exists locally and is not a zero-hash."""
    if not sha or sha == "0" * 40:
        return False
    try:
        subprocess.run(
            ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
            cwd=REPO_ROOT,
            capture_output=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def get_changed_solution_files() -> list[Path]:
    """
    Get added or modified solution files reliably across push ranges,
    merge commits, multi-commit pushes, or manual workflow dispatches.
    """
    event_name = os.environ.get("EVENT_NAME", "").lower()
    before_sha = os.environ.get("BEFORE_SHA", "")
    after_sha = os.environ.get("AFTER_SHA", "HEAD")

    # If triggered manually via workflow_dispatch, scan all solution files
    if event_name == "workflow_dispatch":
        print("Manual workflow_dispatch detected. Scanning all solution files for in-progress status.")
        return sorted(SOLUTIONS_DIR.rglob("practice*.*"))

    changed_names: set[str] = set()

    # 1. Try push range diff if before_sha is valid
    if is_valid_commit(before_sha) and is_valid_commit(after_sha):
        print(f"Inspecting commit range: {before_sha[:8]}..{after_sha[:8]}")
        names = run_git("diff", "--name-only", "--diff-filter=AM", f"{before_sha}..{after_sha}", "--", "solutions/")
        changed_names.update(names)

    # 2. Check if HEAD is a merge commit
    parents = run_git("rev-list", "--parents", "-n", "1", "HEAD")
    is_merge = len(parents[0].split()) > 2 if parents else False

    if is_merge:
        print("HEAD is a merge commit. Checking diff against both merge parents.")
        names_p1 = run_git("diff", "--name-only", "--diff-filter=AM", "HEAD^1", "HEAD", "--", "solutions/")
        changed_names.update(names_p1)

        names_p2 = run_git("diff", "--name-only", "--diff-filter=AM", "HEAD^2", "HEAD", "--", "solutions/")
        changed_names.update(names_p2)

    # 3. Fallback: standard HEAD~1 diff if nothing found yet
    if not changed_names:
        print("Falling back to HEAD~1..HEAD diff.")
        names_head1 = run_git("diff", "--name-only", "--diff-filter=AM", "HEAD~1", "HEAD", "--", "solutions/")
        changed_names.update(names_head1)

    # 4. Final safety fallback: inspect changed files in HEAD commit metadata
    if not changed_names:
        names_log = run_git("show", "--name-only", "--diff-filter=AM", "--format=", "HEAD", "--", "solutions/")
        changed_names.update(names_log)

    files = [REPO_ROOT / p for p in changed_names]
    valid_files = [f for f in files if f.is_file() and not f.name.startswith(".")]
    return sorted(valid_files)


def is_in_progress(path: Path) -> bool:
    """
    Check if the solution file contains an IN PROGRESS status indicator.
    Case-insensitive, allows emojis, hyphens, underscores, or alternate phrasings.
    """
    try:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return False

    for line in content.splitlines()[:30]:
        # If line explicitly says solved/done/complete, skip it
        if SOLVED_PATTERN.search(line):
            continue
        if IN_PROGRESS_PATTERN.search(line):
            return True
    return False


def extract_problem_name(path: Path) -> str:
    """Extract problem title from header or fallback to filename (case-insensitive)."""
    try:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return path.name

    for line in content.splitlines()[:25]:
        match = re.match(
            r"^\s*(?:#|//|--|/\*+|\*)\s*(?:[^\w\s]\s*)?problem(?:\s*[:\-—–]+\s*|\s+)(.*?)\s*(?:\*/)?$",
            line,
            re.IGNORECASE,
        )
        if match:
            cleaned = match.group(1).strip()
            cleaned = re.sub(r"[\r\n\t]+", " ", cleaned).strip()
            cleaned = re.sub(r"\s*(?:\*/|-->)\s*$", "", cleaned).strip()
            if cleaned:
                return cleaned
    return path.name


def issue_already_exists(repo: str, filename: str) -> bool:
    """Check if an open issue already references this filename (case-insensitive)."""
    try:
        result = subprocess.run(
            ["gh", "issue", "list", "--repo", repo, "--state", "open", "--search", filename, "--json", "title,body"],
            capture_output=True,
            text=True,
            check=True,
        )
        issues = json.loads(result.stdout)
        target = filename.lower()
        for issue in issues:
            title = issue.get("title", "").lower()
            body = issue.get("body", "").lower()
            if target in title or target in body:
                return True
        return False
    except Exception as e:
        print(f"Warning: Issue existence check failed for {filename}: {e}", file=sys.stderr)
        return False


def create_issue(path: Path, repo: str) -> bool:
    filename = path.name
    rel_path = path.relative_to(REPO_ROOT).as_posix()
    lang = path.parent.name
    problem = extract_problem_name(path)

    # Sanitize title to prevent formatting or shell breakage
    problem_clean = re.sub(r'["`]', "'", problem).strip()
    title = f"Fix and complete the {problem_clean} solution ({filename})"

    if issue_already_exists(repo, filename):
        print(f"Issue already exists for {filename}. Skipping.")
        return False

    body = f"""## Fix and complete the `{problem_clean}` solution

The file `{rel_path}` was merged with `# Status: 🔄 IN PROGRESS`, which means the implementation is unfinished or has known issues.

**File:** [`{filename}`](https://github.com/{repo}/blob/main/{rel_path})
**Language:** {lang}

### Task

- [ ] Open `{rel_path}`
- [ ] Review the existing code and comments for what is incomplete or broken
- [ ] Fix or complete the implementation
- [ ] Remove the `# Status: 🔄 IN PROGRESS` comment and replace it with `# Status: ✅ Done`
- [ ] Open a Pull Request

No new file needed. Fix the existing file in place.

---

## Open for everyone

This issue is open for everyone: beginners, experienced developers, students, and people who don't code at all. Any language, any level, no experience required. If you want to help, you are welcome here.

## How to contribute

1. Fork this repo
2. Clone your fork and create a new branch
3. Make your change
4. Commit, push, and open a Pull Request

New to open source? Start here before anything else:

**[First Contributions - github.com/firstcontributions/first-contributions](https://github.com/firstcontributions/first-contributions)**

Prefer video? Watch this: [How to contribute on GitHub (YouTube)](https://youtu.be/WldXhauP024?si=9u5wErqvnz9ZZRAv)

<!-- star-note -->
If this repo helps you or you like where it is going, a [star](https://github.com/{repo}) is a nice way to say thanks and helps other people find it. Entirely optional, and you do not need it to contribute.
"""

    labels = "bug,help wanted,good first issue,beginner-friendly,30-minutes"
    cmd = [
        "gh", "issue", "create",
        "--repo", repo,
        "--title", title,
        "--body", body,
        "--label", labels,
    ]
    print(f"Creating issue: {title}")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating issue for {filename}: {e}", file=sys.stderr)
        return False


def main() -> int:
    repo = os.environ.get("GITHUB_REPOSITORY", "Huerte/algo-solutions-python")
    changed_files = get_changed_solution_files()

    flagged = [f for f in changed_files if is_in_progress(f)]
    if not flagged:
        print("No in-progress solution files detected.")
        return 0

    print(f"Found {len(flagged)} in-progress file(s): {[f.name for f in flagged]}")
    success_count = 0
    for file_path in flagged:
        if create_issue(file_path, repo):
            success_count += 1

    print(f"Completed processing in-progress solutions. Created {success_count} issue(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
