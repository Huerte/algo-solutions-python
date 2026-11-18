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

MARKER_START = "<!-- CONTRIBUTORS:START -->"
MARKER_END = "<!-- CONTRIBUTORS:END -->"

AVATAR_SIZE = 48
AVATAR_MARGIN = 1


def fetch_contributors() -> list[dict]:
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    all_contributors: list[dict] = []
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
        all_contributors.extend(batch)
        page += 1

    return all_contributors


def build_html(contributors: list[dict]) -> str:
    anchors: list[str] = []
    for c in contributors:
        if c.get("type") == "Bot":
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

    html = build_html(contributors)
    changed = update_readme(html)

    if changed:
        print(f"README updated with {len(humans)} contributor(s).")
    else:
        print("No update needed.")


if __name__ == "__main__":
    main()

