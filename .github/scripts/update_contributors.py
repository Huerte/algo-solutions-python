#!/usr/bin/env python3
"""
Fetches contributors from the GitHub API and updates the Contributors
section in README.md between the CONTRIBUTORS:START / CONTRIBUTORS:END markers.

Required env vars:
  GITHUB_TOKEN      - GitHub token with repo read access
  GITHUB_REPOSITORY - e.g. "Huerte/algo-solutions"
  README_PATH       - path to README.md (default: README.md)
"""
import os
import re
import sys
import time

import requests

REPO = os.environ.get("GITHUB_REPOSITORY", "Huerte/algo-solutions")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README_PATH = os.environ.get("README_PATH", "README.md")

# Guard: fail fast if the token is missing — the API will 403 without it.
if not TOKEN:
    print("ERROR: GITHUB_TOKEN env var is not set.", file=sys.stderr)
    sys.exit(1)

BOT_PATTERNS = re.compile(r"\[bot\]|(-bot$)|(^bot-)", re.IGNORECASE)

MARKER_START = "<!-- CONTRIBUTORS:START -->"
MARKER_END = "<!-- CONTRIBUTORS:END -->"

AVATAR_SIZE = 64
AVATAR_MARGIN = 2

# Guard: shared session with a UA header so GitHub doesn't rate-limit us
# as an anonymous client.
SESSION = requests.Session()
SESSION.headers.update(
    {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
)


def is_bot(user: dict) -> bool:
    login = user.get("login", "")
    return user.get("type") == "Bot" or bool(BOT_PATTERNS.search(login))


def _get_with_retry(url: str, params: dict, max_retries: int = 5) -> requests.Response:
    """
    Guard: retries on transient 5xx errors and rate-limit (429/403) responses
    with exponential backoff. Raises on permanent client errors (4xx except
    429/403) so callers get a clear error instead of a silent bad state.
    """
    wait = 5
    for attempt in range(1, max_retries + 1):
        resp = SESSION.get(url, params=params, timeout=20)

        if resp.status_code == 200:
            return resp

        # Rate limit: respect Retry-After if present, else back off.
        if resp.status_code in (403, 429):
            retry_after = int(resp.headers.get("Retry-After", wait))
            print(
                f"Rate limited (HTTP {resp.status_code}). "
                f"Waiting {retry_after}s before retry {attempt}/{max_retries}...",
                file=sys.stderr,
            )
            time.sleep(retry_after)
            wait = min(wait * 2, 120)
            continue

        # Transient server error — back off and retry.
        if resp.status_code >= 500:
            print(
                f"Server error {resp.status_code} on attempt {attempt}/{max_retries}. "
                f"Retrying in {wait}s...",
                file=sys.stderr,
            )
            time.sleep(wait)
            wait = min(wait * 2, 120)
            continue

        # Permanent client error (404, 401, etc.) — fail immediately.
        resp.raise_for_status()

    # Guard: if all retries exhausted, give up with a clear message.
    raise RuntimeError(f"Request to {url} failed after {max_retries} retries.")


def fetch_contributors() -> list[dict]:
    # Pull from /contributors (commit-based, may lag a few minutes after a merge).
    commit_contributors: dict[str, dict] = {}
    page = 1
    while True:
        resp = _get_with_retry(
            f"https://api.github.com/repos/{REPO}/contributors",
            params={"per_page": 100, "page": page, "anon": "false"},
        )
        batch = resp.json()

        # Guard: ensure the API returned a list, not an error object.
        if not isinstance(batch, list):
            print(
                f"ERROR: Unexpected response from /contributors: {batch}",
                file=sys.stderr,
            )
            sys.exit(1)

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
        resp = _get_with_retry(
            f"https://api.github.com/repos/{REPO}/pulls",
            params={"state": "closed", "per_page": 100, "page": page},
        )
        batch = resp.json()

        # Guard: ensure the API returned a list.
        if not isinstance(batch, list):
            print(
                f"ERROR: Unexpected response from /pulls: {batch}",
                file=sys.stderr,
            )
            sys.exit(1)

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

        login = c.get("login", "")
        avatar = c.get("avatar_url", "")
        profile = c.get("html_url", f"https://github.com/{login}")

        # Guard: skip entries with missing required fields.
        if not login or not avatar:
            print(f"WARNING: Skipping contributor with incomplete data: {c}")
            continue

        anchors.append(
            f'<a href="{profile}" title="{login}">'
            f'<img src="{avatar}&s={AVATAR_SIZE}" '
            f'width="{AVATAR_SIZE}" height="{AVATAR_SIZE}" '
            f'alt="{login}" style="border-radius:50%;margin:{AVATAR_MARGIN}px">'
            f"</a>"
        )

    # Guard: if no valid contributors were found, return an empty block rather
    # than writing broken HTML.
    if not anchors:
        print("WARNING: No valid contributors to render.", file=sys.stderr)
        return '<p align="center">\n<!-- No contributors found -->\n</p>'

    # No whitespace between anchors — prevents GitHub from inserting a space
    # character between each avatar when rendering inline HTML.
    return '<p align="center">\n' + "".join(anchors) + "\n</p>"


def update_readme(html: str) -> bool:
    # Guard: verify README exists before trying to open it.
    if not os.path.isfile(README_PATH):
        print(f"ERROR: README file not found at '{README_PATH}'.", file=sys.stderr)
        sys.exit(1)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Guard: both markers must exist or we'd corrupt the file.
    if MARKER_START not in content or MARKER_END not in content:
        print(
            f"ERROR: Markers not found in {README_PATH}. "
            "Add <!-- CONTRIBUTORS:START --> and <!-- CONTRIBUTORS:END -->.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Guard: markers must be in the right order.
    if content.index(MARKER_START) > content.index(MARKER_END):
        print(
            f"ERROR: CONTRIBUTORS:START appears after CONTRIBUTORS:END in {README_PATH}.",
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
    humans = [c for c in contributors if not is_bot(c)]
    print(f"Found {len(humans)} human contributor(s).")
    for c in humans:
        print(f"  - {c['login']}")

    # Guard: warn (but don't fail) if contributor list is unexpectedly empty.
    if not humans:
        print(
            "WARNING: No human contributors found. README will not be updated.",
            file=sys.stderr,
        )
        sys.exit(0)

    html = build_html(contributors)
    changed = update_readme(html)

    if changed:
        print(f"README updated with {len(humans)} contributor(s).")
    else:
        print("No update needed.")


if __name__ == "__main__":
    main()
