#!/usr/bin/env python3
"""Automatically create a GitHub issue when a solution with Status: IN PROGRESS is merged."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def get_changed_solution_files() -> list[Path]:
    """Get added or modified solution files from the latest commit."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=AM", "HEAD~1", "HEAD", "--", "solutions/"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        files = [REPO_ROOT / line.strip() for line in result.stdout.splitlines() if line.strip()]
        return [f for f in files if f.is_file()]
    except subprocess.CalledProcessError as e:
        print(f"Git diff failed: {e}", file=sys.stderr)
        return []


def is_in_progress(path: Path) -> bool:
    """Check if the solution file contains an IN PROGRESS status indicator."""
    try:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return False

    for line in content.splitlines()[:20]:
        if re.search(r"^\s*(?:#|//|--|/\*+|\*)\s*Status:\s*.*in.?progress", line, re.IGNORECASE):
            return True
    return False


def extract_problem_name(path: Path) -> str:
    """Extract problem title from header or fallback to filename."""
    try:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return path.name

    for line in content.splitlines()[:15]:
        match = re.match(r"^\s*(?:#|//|--|/\*+|\*)\s*(?:📜\s*)?Problem(?:\s*[:\-—–]+\s*|\s+)(.*?)\s*(?:\*/)?$", line, re.IGNORECASE)
        if match:
            cleaned = match.group(1).strip()
            if cleaned:
                return cleaned
    return path.name


def issue_already_exists(repo: str, filename: str) -> bool:
    """Check if an open issue already references this filename."""
    try:
        result = subprocess.run(
            ["gh", "issue", "list", "--repo", repo, "--state", "open", "--search", filename, "--json", "number"],
            capture_output=True,
            text=True,
            check=True,
        )
        import json
        issues = json.loads(result.stdout)
        return len(issues) > 0
    except Exception as e:
        print(f"Check existing issues failed: {e}", file=sys.stderr)
        return False


def create_issue(path: Path, repo: str) -> None:
    filename = path.name
    rel_path = path.relative_to(REPO_ROOT).as_posix()
    lang = path.parent.name
    problem = extract_problem_name(path)

    if issue_already_exists(repo, filename):
        print(f"Issue already exists for {filename}. Skipping.")
        return

    title = f"Fix and complete the {problem} solution ({filename})"

    body = f"""## Fix and complete the `{problem}` solution

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
    subprocess.run(cmd, check=True)


def main() -> int:
    repo = os.environ.get("GITHUB_REPOSITORY", "Huerte/algo-solutions-python")
    changed_files = get_changed_solution_files()

    flagged = [f for f in changed_files if is_in_progress(f)]
    if not flagged:
        print("No in-progress solution files detected in this commit.")
        return 0

    print(f"Found {len(flagged)} in-progress file(s): {[f.name for f in flagged]}")
    for file_path in flagged:
        create_issue(file_path, repo)

    return 0


if __name__ == "__main__":
    sys.exit(main())

