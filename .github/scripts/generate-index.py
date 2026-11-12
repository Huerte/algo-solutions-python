#!/usr/bin/env python3
"""
Generate index.json for GitHub Pages from solution files.
Scans solutions directory and extracts problem information from file headers.
"""

import os
import json
import re
from pathlib import Path

def extract_header_info(filepath):
    """Extract problem name and source from file header."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [f.readline() for _ in range(10)]

        problem = None
        source = None

        for line in lines:
            # Match both # and // comment styles
            if match := re.match(r'^[#/]+\s+Problem:\s*(.+)$', line.strip()):
                problem = match.group(1).strip()
            elif match := re.match(r'^[#/]+\s+Source:\s*(.+)$', line.strip()):
                source = match.group(1).strip()

        return problem, source
    except Exception as e:
        print(f"Warning: Error reading {filepath}: {e}")
        return None, None

def generate_index():
    """Generate complete solutions index."""
    solutions = []
    languages = ['python', 'javascript', 'cpp', 'java']

    repo_root = Path(__file__).parent.parent.parent
    solutions_dir = repo_root / 'solutions'

    print(f"Scanning solutions directory: {solutions_dir}")

    for lang in languages:
        lang_dir = solutions_dir / lang
        if not lang_dir.exists():
            continue

        print(f"Processing {lang}...")

        for filepath in sorted(lang_dir.glob('practice*.py')) + \
                        sorted(lang_dir.glob('practice*.js')) + \
                        sorted(lang_dir.glob('practice*.cpp')) + \
                        sorted(lang_dir.glob('practice*.java')):

            if not filepath.is_file():
                continue

            problem, source = extract_header_info(filepath)
            problem = problem or filepath.stem

            solutions.append({
                'name': filepath.stem,
                'language': lang,
                'filename': filepath.name,
                'problem': problem,
                'source': source or '',
                'path': f'solutions/{lang}/{filepath.name}'
            })

    # Write index file
    output_path = repo_root / 'docs' / 'data.json'
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(solutions, f, indent=2)

    # Print summary
    print(f"\n✓ Index generated successfully!")
    print(f"  Total solutions: {len(solutions)}")
    print(f"  Output file: {output_path}")

    # Group by language
    by_lang = {}
    for sol in solutions:
        lang = sol['language']
        by_lang[lang] = by_lang.get(lang, 0) + 1

    print("\nSolutions by language:")
    for lang in languages:
        if lang in by_lang:
            print(f"  {lang}: {by_lang[lang]}")

if __name__ == '__main__':
    generate_index()
