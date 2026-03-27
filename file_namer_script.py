from pathlib import Path
import sys

if __name__ == "__main__":

    target = Path(r"C:\Programs\___LeetCode_Problems\practice_problem_solutions (2025)")

    if not target.exists():
        sys.exit(1)

    placeholder = "practice"

    files = [p for p in target.iterdir() if p.is_file()]

    temp_paths = []
    for i, path in enumerate(files):
        temp_path = path.with_name(f"__temp__{i}{path.suffix}")
        path.rename(temp_path)
        temp_paths.append(temp_path)

    for i, path in enumerate(temp_paths, 1):
        new_path = path.with_name(f"{placeholder}{i}{path.suffix}")
        path.rename(new_path)

    print("Done")