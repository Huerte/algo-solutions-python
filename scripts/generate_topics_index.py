#!/usr/bin/env python3
"""Generate and update TOPICS.md catalog dynamically from solution files."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = REPO_ROOT / "solutions"
TOPICS_FILE = REPO_ROOT / "TOPICS.md"

CATEGORY_KEYWORDS = {
    "Array": [
        "array", "matrix", "subarray", "vector", "rotate", "pivot", "element",
        "pascal triangle", "pascal's triangle", "spiral", "squares of", "two sum", "three sum", "3sum",
        "contains duplicate", "intersection", "move zero", "running sum",
        "remove duplicate", "intervals", "jump game", "diagonal", "stock",
        "partition", "grid", "range",
    ],
    "String": [
        "string", "substring", "palindrome", "anagram", "parenthes", "vowel",
        "word", "words", "character", "roman", "prefix", "suffix", "reverse",
        "isomorphic", "ransom", "needle", "haystack", "letter", "phone",
        "morse", "text", "consonant", "pascalcase", "snake_case", "snake case", "camelcase",
    ],
    "Math": [
        "prime", "sum", "digit", "integer", "factorial", "fibonacci", "number",
        "power", "divide", "multiply", "count odd", "gcd", "lcm", "even",
        "ugly", "happy", "square root", "sqrt", "add binary", "plus one",
        "multiple", "multiples", "area", "percentage", "rectangle",
    ],
    "Dynamic Programming": [
        "dynamic", "climbing stairs", "knapsack", "coin change", "robber",
        "longest common", "subsequence", "paths", "profit",
    ],
    "Hash Map / Set": [
        "hash", "hashmap", "map", "dict", "dictionary", "set", "counter",
        "frequency", "unique", "distinct",
    ],
    "Tree": [
        "tree", "node", "root", "ancestor", "depth", "bst", "leaf",
        "same tree", "symmetric",
    ],
    "Graph": [
        "graph", "island", "cycle", "connected", "clone graph", "network",
    ],
    "Sorting & Search": [
        "sort", "sorted", "search", "binary search", "rank", "order",
    ],
}


def sanitize_text(text: str) -> str:
    """Remove prohibited em-dashes and non-ASCII dashes."""
    return re.sub(r"[\u2014\u2013]", "-", text).strip()


def clean_problem_title(raw_title: str) -> str:
    """Clean leading punctuation, diff markers (+ and -), and emojis from problem name."""
    cleaned = sanitize_text(raw_title)
    # Remove leading symbols such as -, +, :, and whitespace
    cleaned = re.sub(r"^[^\w\s\"'(\[]+", "", cleaned).strip()
    # Normalize variants like '+1 Array' or '1 Array'
    if cleaned.lower() in ("1 array", "+1 array", "plus 1 array"):
        cleaned = "Plus One Array"
    return cleaned


def parse_solution_file(path: Path) -> dict[str, str]:
    """Parse metadata, header fields, and status from a solution file."""
    content = path.read_text(encoding="utf-8-sig", errors="replace")
    lines = [line.strip() for line in content.splitlines()]
    non_empty = [line for line in lines if line]

    status = "Complete"
    if not non_empty:
        status = "Empty (0 bytes)"
    elif len(non_empty) < 5:
        # Check if it has executable code or just placeholder comments
        code_lines = [l for l in non_empty if not l.startswith(("#", "//"))]
        if not code_lines:
            status = "Stub (<5 lines)"

    problem = ""
    source = ""
    declared_topic = ""

    for line in lines:
        if not problem:
            prob_match = re.match(r"^(?:#|//)\s*(?:📜\s*)?Problem(?:\s*[:\-—–]+\s*|\s+)(.*)$", line, re.IGNORECASE)
            if prob_match:
                problem = clean_problem_title(prob_match.group(1))
        if not source:
            source_match = re.match(r"^(?:#|//)\s*Source:\s*(.*)$", line, re.IGNORECASE)
            if source_match:
                source = source_match.group(1).strip()
        if not declared_topic:
            topic_match = re.match(r"^(?:#|//)\s*Topic:\s*(.*)$", line, re.IGNORECASE)
            if topic_match:
                declared_topic = topic_match.group(1).strip()
        if re.search(r"(?:#|//)\s*(?:Status:\s*.*(?:in progress|needs|incomplete)|TODO\b).*", line, re.IGNORECASE):
            if not re.search(r"solved|complete", line, re.IGNORECASE):
                status = "In Progress / Needs Work"

    if not problem:
        for candidate in non_empty[:4]:
            if re.match(r"^(?:#|//)\s*[A-Za-z0-9]", candidate) and not re.search(r"(?:source|note|status|topic|description):", candidate, re.IGNORECASE):
                cleaned = re.sub(r"^(?:#|//)\s*(?:📜\s*)?", "", candidate)
                cleaned = re.sub(r"^(?:CodeWars|HackerRank|CodeChum|Geeksforgeeks|py\.checkio|LeetCode)\s*-\s*", "", cleaned, flags=re.IGNORECASE)
                problem = clean_problem_title(cleaned)
                break
        if not problem:
            problem = "Unknown Problem"
            if status == "Complete":
                status = "Missing Header"

    # Category matching
    assigned_category = "Unclassified"
    search_scope = f"{declared_topic} {problem}".lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in search_scope for keyword in keywords):
            assigned_category = category
            break

    relative_path = path.relative_to(REPO_ROOT).as_posix()
    language = path.parent.name

    return {
        "file": path.name,
        "language": language,
        "path": relative_path,
        "problem": problem,
        "category": assigned_category,
        "status": status,
    }


def generate_topics_markdown() -> str:
    """Build markdown catalog content from all solutions dynamically."""
    solution_files = sorted(SOLUTIONS_DIR.rglob("practice*.*"), key=lambda item: item.name)
    records = [parse_solution_file(path) for path in solution_files]

    by_category: dict[str, list[dict[str, str]]] = defaultdict(list)
    for record in records:
        by_category[record["category"]].append(record)

    total_count = len(records)
    lines: list[str] = [
        "<!-- This file is dynamically generated by scripts/generate_topics_index.py. Do not edit manually. -->",
        "# Solution Classification by Topic",
        "",
        f"This catalog organizes all {total_count} problem solutions by category.",
        "Category counts and listings update dynamically via `python scripts/generate_topics_index.py`.",
        "The folder structure remains language-based (`solutions/<language>/practice<n>.<ext>`) to support active contributors.",
        "",
        "## Categories",
        "",
    ]

    # Category summary counts
    sorted_categories = sorted(by_category.keys(), key=lambda name: (name == "Unclassified", name))
    for category in sorted_categories:
        count = len(by_category[category])
        anchor = category.lower().replace(" ", "-").replace("/", "").replace("&", "")
        lines.append(f"- [{category}](#{anchor}) ({count})")
    lines.append("")

    for category in sorted_categories:
        items = sorted(by_category[category], key=lambda item: item["problem"].lower())
        lines.extend([
            f"## {category}",
            "",
            "| Problem | Language | File | Status |",
            "|---|---|---|---|",
        ])
        for item in items:
            lines.append(
                f"| {item['problem']} | {item['language']} | [{item['file']}]({item['path']}) | {item['status']} |"
            )
        lines.append("")

    incomplete = [record for record in records if record["status"] != "Complete"]
    if incomplete:
        lines.extend([
            f"## Solutions Needing Attention ({len(incomplete)})",
            "",
            "These solutions need headers, test cases, or implementation fixes. They are ideal for contributor PRs.",
            "",
            "| Problem | Language | File | Needs |",
            "|---|---|---|---|",
        ])
        for item in sorted(incomplete, key=lambda item: item["file"]):
            lines.append(
                f"| {item['problem']} | {item['language']} | [{item['file']}]({item['path']}) | {item['status']} |"
            )
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    markdown = generate_topics_markdown()
    TOPICS_FILE.write_text(markdown, encoding="utf-8")
    print(f"Generated {TOPICS_FILE} with updated classifications.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
