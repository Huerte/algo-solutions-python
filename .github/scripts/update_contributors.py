#!/usr/bin/env python3
"""
Fetches contributors from the GitHub API and updates the Contributors
section in README.md between the CONTRIBUTORS:START / CONTRIBUTORS:END markers.

Required env vars:
  GITHUB_TOKEN      - GitHub token with repo read access
  GITHUB_REPOSITORY - e.g. "Huerte/algo-solutions-python"
  README_PATH       - path to README.md (default: README.md)
"""
import os
import re
import sys

import requests

REPO = os.environ.get("GITHUB_REPOSITORY", "Huerte/algo-solutions-python")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README_PATH = os.environ.get("README_PATH", "README.md")

BOT_PATTERNS = re.compile(r"\[bot\]|(-bot$)|(^bot-)", re.IGNORECASE)

MARKER_START = "<!-- CONTRIBUTORS:START -->"
MARKER_END = "<!-- CONTRIBUTORS:END -->"


def is_bot(user: dict) -> bool:
    login = user.get("login", "")
    return user.get("type") == "Bot" or bool(BOT_PATTERNS.search(login))

AVATAR_SIZE = 64
AVATAR_MARGIN = 2


def fetch_contributors() -> list[dict]:
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    # Pull from /contributors (commit-based, may lag a few minutes after a merge)
    commit_contributors: dict[str, dict] = {}
    page = 1
    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{REPO}/contributors",
            headers=headers,
            params={"per_page": 100, "page": page, "anon": "false"},
            timeout=15,
        )
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        for c in batch:
            login = c.get("login", "")
            if login and not is_bot(c):
                commit_contributors[login] = c
        page += 1

    # Also pull merged PR authors — real-time, no lag.
    # This catches contributors whose commits haven't propagated to the
    # /contributors endpoint yet (e.g. immediately after a first merge).
    pr_contributors: dict[str, dict] = {}
    page = 1
    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{REPO}/pulls",
            headers=headers,
            params={"state": "closed", "per_page": 100, "page": page},
            timeout=15,
        )
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        for pr in batch:
            if not pr.get("merged_at"):
                continue
            user = pr.get("user") or {}
            login = user.get("login", "")
            if not login or is_bot(user):
                continue
            if login not in pr_contributors and login not in commit_contributors:
                pr_contributors[login] = {
                    "login": login,
                    "avatar_url": user.get("avatar_url", ""),
                    "html_url": user.get("html_url", f"https://github.com/{login}"),
                    "type": "User",
                }
        page += 1

    # Merge: commit_contributors first (sorted by commit count), then any
    # PR-only authors who aren't in the commit list yet.
    merged = list(commit_contributors.values()) + list(pr_contributors.values())
    return merged


def build_html(contributors: list[dict]) -> str:
    anchors: list[str] = []
    for c in contributors:
        if is_bot(c):
            continue
        login = c["login"]
        avatar = c["avatar_url"]
        profile = c["html_url"]
        anchors.append(
            f'<a href="{profile}" title="{login}">'
            f'<img src="{avatar}&s={AVATAR_SIZE}" '
            f'width="{AVATAR_SIZE}" height="{AVATAR_SIZE}" '
            f'alt="{login}" style="border-radius:50%;margin:{AVATAR_MARGIN}px">'
            f"</a>"
        )
    # No whitespace between anchors — prevents GitHub from inserting a space
    # character between each avatar when rendering inline HTML.
    return '<p align="center">\n' + "".join(anchors) + "\n</p>"


def update_readme(html: str) -> bool:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if MARKER_START not in content or MARKER_END not in content:
        print(
            f"ERROR: markers not found in {README_PATH}. "
            "Add <!-- CONTRIBUTORS:START --> and <!-- CONTRIBUTORS:END -->.",
            file=sys.stderr,
        )
        sys.exit(1)

    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL,
    )
    new_block = f"{MARKER_START}\n{html}\n{MARKER_END}"
    new_content = pattern.sub(new_block, content)

    if new_content == content:
        print("No changes — README already up to date.")
        return False

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main() -> None:
    print(f"Fetching contributors for {REPO}...")
    contributors = fetch_contributors()
    humans = [c for c in contributors if c.get("type") != "Bot"]
    print(f"Found {len(humans)} human contributor(s).")
    for c in humans:
        print(f"  - {c['login']}")

    html = build_html(contributors)
    changed = update_readme(html)

    if changed:
        print(f"README updated with {len(humans)} contributor(s).")
    else:
        print("No update needed.")


if __name__ == "__main__":
    main()

