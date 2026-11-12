#!/usr/bin/env python3
"""Generate the searchable GitHub Pages index from solution headers."""

import json
import re
from pathlib import Path

LANGUAGE_EXTENSIONS = {
    "python": {".py"},
    "javascript": {".js"},
    "cpp": {".cpp", ".cc", ".cxx"},
    "java": {".java"},
    "typescript": {".ts", ".tsx"},
}

TOPIC_RULES = [
    ("Dynamic Programming", r"\b(dynamic programming|unique paths|minimum path|coin change|fibonacci|climbing stairs|longest increasing subsequence|wildcard matching|maximum subarray|kadane)\b"),
    ("Graphs", r"\b(graph|islands|word ladder|shortest path|escape path|flood fill|connected component|course schedule)\b"),
    ("Trees", r"\b(tree|bst|binary search tree|n-ary)\b"),
    ("Linked Lists", r"\b(linked list|rotate list|add two numbers|merge two sorted lists|remove duplicates from sorted list)\b"),
    ("Stack & Queue", r"\b(parentheses|braces|brackets|backspace|next greater element|queue|stack|parking system)\b"),
    ("Backtracking", r"\b(n-queens|permutation|permutations|subsets|combinations|combination sum|generate parentheses)\b"),
    ("Sliding Window", r"\b(longest substring|minimum window|subarray|sliding window|consecutive)\b"),
    ("Two Pointers", r"\b(3sum|4sum|two sum|pair with given|palindrome|merge intervals|backspaces in string)\b"),
    ("Matrix", r"\b(matrix|spiral|row with|max 1s|diagonal|rotate 90|flood fill)\b"),
    ("Sorting", r"\b(sort|sorting|rank|median|kth largest|relative ranks|height checker|frequency sorting)\b"),
    ("Searching", r"\b(search|missing number|missing element|find the difference|peak element|pivot index|nearest value)\b"),
    ("Hash Table", r"\b(two sum|frequency|counter|anagram|duplicate|intersection|common characters|common elements|good pairs|word order|most frequent)\b"),
    ("Strings", r"\b(string|word|sentence|character|vowel|consonant|camelcase|morse|regex|encryption|decode|encode|prefix|suffix|text|ip validation|phone number|credit card)\b"),
    ("Arrays", r"\b(array|subarray|elements|indices|index|triplets|pairs|partition|running sum|rotate array|jump game|candies|missing)\b"),
    ("Math", r"\b(number|digit|prime|factorial|gcd|multiple|sum|power|square root|binary to decimal|roman numeral|fibonacci|bits|xor|bitwise|area|duration|time delta|leap year)\b"),
    ("Greedy", r"\b(jump game|minimum operations|largest number|maximum number|assign|distribute|water bottles|hurdle|buy and sell|best time)\b"),
    ("Bit Manipulation", r"\b(bit|binary|xor|complement|set bits|ones|flips)\b"),
    ("Simulation", r"\b(simulator|simulate|design parking|calendar|tic-tac-toe|bouncing balls|counting valleys|fizzbuzz|game|solar system)\b"),
]

def extract_header_info(filepath):
    problem = None
    source = None
    topics = []
    with filepath.open("r", encoding="utf-8", errors="ignore") as file:
        for line in list(file)[:15]:
            match = re.match(r"^\s*(?:#|//|/\*+|\*|<!--)\s*(Problem|Source|Topics?)\s*:\s*(.*?)\s*(?:\*/|-->)?\s*$", line, re.IGNORECASE)
            if not match:
                continue
            key, value = match.group(1).lower(), match.group(2).strip()
            if key == "problem":
                problem = value
            elif key == "source":
                source = value
            else:
                topics.extend(item.strip() for item in re.split(r"[,;|]", value) if item.strip())
    return problem, source, topics

def infer_topics(problem):
    normalized = problem.lower()
    matches = [topic for topic, pattern in TOPIC_RULES if re.search(pattern, normalized)]
    return matches or ["General"]

def generate_index():
    repo_root = Path(__file__).resolve().parents[2]
    solutions_dir = repo_root / "solutions"
    output_path = repo_root / "docs" / "data.json"
    solutions = []

    for language, extensions in LANGUAGE_EXTENSIONS.items():
        language_dir = solutions_dir / language
        if not language_dir.is_dir():
            continue
        for filepath in sorted(language_dir.iterdir()):
            if not filepath.is_file() or filepath.suffix.lower() not in extensions:
                continue
            problem, source, topics = extract_header_info(filepath)
            problem = problem or filepath.stem
            solutions.append({
                "name": filepath.stem,
                "language": language,
                "filename": filepath.name,
                "problem": problem,
                "source": source or "",
                "topics": topics or infer_topics(problem),
                "path": filepath.relative_to(repo_root).as_posix(),
            })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(solutions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    counts = {language: sum(item["language"] == language for item in solutions) for language in LANGUAGE_EXTENSIONS}
    print(f"Generated {len(solutions)} solutions in {output_path}")
    for language, count in counts.items():
        if count:
            print(f"  {language}: {count}")

if __name__ == "__main__":
    generate_index()
