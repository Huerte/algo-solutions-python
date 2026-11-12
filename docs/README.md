# Algorithm Solutions - GitHub Pages

A searchable, filterable web interface for browsing algorithm solutions by language and problem.

## Features

- 🔍 **Search** by problem name or file name
- 🏷️ **Filter** by programming language (Python, JavaScript, C++, Java)
- 🔗 **Direct links** to problem sources and GitHub files
- 📱 **Responsive design** - works on desktop and mobile
- ⚫ **Dark mode support** - respects system preferences
- 📦 **No build required** - works directly with GitHub Pages

## How to Update the Solution Index

When new solutions are added to the `solutions/` directory, the `data.json` file needs to be regenerated.

### Automatic Method (CI/CD)
The ideal solution is to add this to GitHub Actions so `data.json` is regenerated on every merge to main.

### Manual Method
Run the included PowerShell script to regenerate the index:

```powershell
powershell -ExecutionPolicy Bypass -File generate-index.ps1
```

Or on Unix/macOS:
```bash
node generate-index.js
```

## File Structure

```
docs/
├── index.html      # Main page
├── style.css       # Styling
├── script.js       # JavaScript for filtering/searching
├── data.json       # Solution index (auto-generated)
└── README.md       # This file
```

## How It Works

1. **data.json** is generated from the solution files by reading the headers
2. **script.js** fetches data.json and provides filtering/searching in real-time
3. **index.html** displays the results in a responsive grid

Each solution card shows:
- Problem name (from header comment)
- File name
- Programming language
- Link to GitHub file
- Link to problem source (if available)

## Contributing

To add solutions:
1. Add your solution file to `solutions/<language>/practice<number>.<ext>`
2. Include header comments with problem name and source link
3. The index will be regenerated automatically

## Example Header Format

```python
# Problem: Two Sum
# Source: https://leetcode.com/problems/two-sum/
# Note: Classic hash map solution
```

---

**Site URL:** https://aaqibhafeezkhan.github.io/algo-solutions-python/
