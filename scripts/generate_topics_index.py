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


COMMENT_PREFIX = r"^(?:#|//|--|/\*+|\*)\s*"


def parse_solution_file(path: Path) -> dict[str, str]:
    """Parse metadata, header fields, and status from a solution file."""
    content = path.read_text(encoding="utf-8-sig", errors="replace")
    lines = [line.strip() for line in content.splitlines()]
    non_empty = [line for line in lines if line]

    # Detect comment style for this file
    comment_pat = COMMENT_PREFIX

    status = "Complete"
    if not non_empty:
        status = "Empty (0 bytes)"
    elif len(non_empty) < 5:
        code_lines = [l for l in non_empty if not re.match(comment_pat, l)]
        if not code_lines:
            status = "Stub (<5 lines)"

    problem = ""
    source = ""
    note = ""
    declared_topic = ""
    found_problem_line = False
    found_source_line = False
    found_note_line = False
    found_topic_line = False

    for line in lines:
        if not found_problem_line:
            prob_match = re.match(
                comment_pat + r"(?:📜\s*)?Problem(?:\s*[:\-—–]+\s*|\s+)(.*?)\s*(?:\*/)?$",
                line, re.IGNORECASE,
            )
            if prob_match:
                found_problem_line = True
                problem = clean_problem_title(prob_match.group(1))
        if not found_source_line:
            source_match = re.match(comment_pat + r"Source:\s*(.*?)\s*(?:\*/)?$", line, re.IGNORECASE)
            if source_match:
                found_source_line = True
                source = source_match.group(1).strip()
        if not found_note_line:
            note_match = re.match(comment_pat + r"Note:\s*(.*?)\s*(?:\*/)?$", line, re.IGNORECASE)
            if note_match:
                found_note_line = True
                note = note_match.group(1).strip()
        if not found_topic_line and not declared_topic:
            topic_match = re.match(comment_pat + r"Topics?:\s*(.*?)\s*(?:\*/)?$", line, re.IGNORECASE)
            if topic_match:
                found_topic_line = True
                declared_topic = topic_match.group(1).strip()
        if re.search(
            comment_pat + r"(?:Status:\s*.*(?:in progress|needs|incomplete)|TODO\b).*",
            line, re.IGNORECASE,
        ):
            if not re.search(r"solved|complete", line, re.IGNORECASE):
                status = "In Progress / Needs Work"

    # Determine what is actually code (non-comment, non-blank)
    code_lines = [l for l in non_empty if not re.match(comment_pat, l)]
    has_code = bool(code_lines)

    # A file satisfies the third header requirement with EITHER Note or Topic.
    has_third_field = (found_note_line and note) or (found_topic_line and declared_topic)

    # Flag files whose headers are present but empty or missing
    if status not in ("In Progress / Needs Work", "Empty (0 bytes)", "Stub (<5 lines)"):
        missing_parts = []
        if found_source_line and not source:
            missing_parts.append("Source (blank)")
        if found_note_line and not note and not found_topic_line:
            missing_parts.append("Note (blank)")
        # Also flag fields that are entirely absent when the file has code
        if has_code:
            if not found_source_line:
                missing_parts.append("Source (missing)")
            if not has_third_field:
                missing_parts.append("Note or Topic (missing)")
        if missing_parts:
            status = f"Incomplete Header ({', '.join(missing_parts)})"

    # Fallback: try to extract problem title from first comment lines
    if not found_problem_line or not problem:
        for candidate in non_empty[:6]:
            if re.match(comment_pat + r"[A-Za-z0-9]", candidate) and not re.search(
                r"(?:source|note|status|topic|description):", candidate, re.IGNORECASE
            ):
                cleaned = re.sub(comment_pat + r"(?:📜\s*)?", "", candidate)
                cleaned = re.sub(
                    r"^(?:CodeWars|HackerRank|CodeChum|Geeksforgeeks|py\.checkio|LeetCode)\s*-\s*",
                    "", cleaned, flags=re.IGNORECASE,
                )
                problem = clean_problem_title(cleaned)
                break
        # Only mark Missing Header if we genuinely could not extract any title
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
    _SKIP_SUFFIXES = {".pyc", ".pyo", ".pyd"}
    all_files = (
        path for path in SOLUTIONS_DIR.rglob("practice*.*")
        if path.is_file()
        and not path.name.startswith(".")
        and "__pycache__" not in path.parts
        and path.suffix not in _SKIP_SUFFIXES
    )
    solution_files = sorted(all_files, key=lambda item: item.name)
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
            f"## Solutions Needing Attention",
            "",
            "These solutions need headers, test cases, or implementation fixes. They are ideal for contributor PRs.",
            f"**Total needing attention:** {len(incomplete)}",
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
    temp_file = TOPICS_FILE.with_suffix(".tmp")
    temp_file.write_text(markdown, encoding="utf-8")
    temp_file.replace(TOPICS_FILE)
    print(f"Generated {TOPICS_FILE} with updated classifications.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
