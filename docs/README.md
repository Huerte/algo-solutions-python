# Algorithm Solutions - GitHub Pages

A searchable, filterable web interface for browsing algorithm solutions by language, topic, and problem.

## Features

- Search by problem name or file name
- Filter by programming language and algorithm topic
- Direct links to problem sources and solution files
- Responsive layout and system dark-mode support
- No build step required for GitHub Pages

## How to Update the Solution Index

The index is generated from solution file headers and problem names.

### Automatic Method

The GitHub Actions workflow regenerates `docs/data.json` when files under `solutions/` change on `main`. It has explicit permission to commit the generated index.

### Manual Method

From the repository root, run the PowerShell wrapper:

```powershell
powershell -ExecutionPolicy Bypass -File .\\generate-index.ps1
```

On Linux or macOS, run the Python generator:

```bash
python3 .github/scripts/generate-index.py
```

Both commands use the same generator, so the generated index stays consistent across platforms.

## Topic Metadata

Add an optional `Topics` header to a solution to override automatic topic detection. Separate multiple topics with commas.

Python example:

```python
# Problem: Two Sum
# Source: https://leetcode.com/problems/two-sum/
# Topics: Arrays, Hash Table, Two Pointers
```

JavaScript/C++/Java example:

```javascript
// Problem: Valid Parentheses
// Source: https://leetcode.com/problems/valid-parentheses/
// Topics: Strings, Stack & Queue
```

When no `Topics` header is present, the generator assigns topics using the problem title. Unmatched titles are placed in **General** and can be given more specific topics through the header.

## File Structure

```
docs/
├── index.html
├── style.css
├── script.js
├── data.json
└── README.md
```

Each solution card shows its problem name, language, topics, source link (when available), and repository file link.

**Site URL:** https://aaqibhafeezkhan.github.io/algo-solutions-python/
