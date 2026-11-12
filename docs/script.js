let allSolutions = [];

document.addEventListener('DOMContentLoaded', async () => {
    await loadSolutions();
    setupEventListeners();
    displaySolutions(allSolutions);
});

async function loadSolutions() {
    try {
        const response = await fetch('data.json');
        if (!response.ok) throw new Error('Failed to load data');
        allSolutions = await response.json();
        console.log(`Loaded ${allSolutions.length} solutions`);
    } catch (error) {
        console.error('Error loading solutions:', error);
        document.getElementById('solutionsList').innerHTML =
            '<div class="no-results"><h2>Error loading solutions</h2><p>Please try refreshing the page.</p></div>';
    }
}

function setupEventListeners() {
    const searchInput = document.getElementById('searchInput');
    const languageFilter = document.getElementById('languageFilter');

    searchInput.addEventListener('input', filterAndDisplay);
    languageFilter.addEventListener('change', filterAndDisplay);
}

function filterAndDisplay() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const selectedLanguage = document.getElementById('languageFilter').value;

    const filtered = allSolutions.filter(solution => {
        const matchesSearch = !searchTerm ||
            solution.problem.toLowerCase().includes(searchTerm) ||
            solution.name.toLowerCase().includes(searchTerm) ||
            solution.filename.toLowerCase().includes(searchTerm);

        const matchesLanguage = !selectedLanguage || solution.language === selectedLanguage;

        return matchesSearch && matchesLanguage;
    });

    displaySolutions(filtered);
}

function displaySolutions(solutions) {
    const container = document.getElementById('solutionsList');
    const resultCount = document.getElementById('resultCount');

    resultCount.textContent = solutions.length;

    if (solutions.length === 0) {
        container.innerHTML = `
            <div class="no-results" style="grid-column: 1 / -1;">
                <h2>No solutions found</h2>
                <p>Try adjusting your search or filter criteria</p>
            </div>
        `;
        return;
    }

    container.innerHTML = solutions.map(solution => createSolutionCard(solution)).join('');
}

function createSolutionCard(solution) {
    const sourceHtml = solution.source
        ? `<div class="source-link"><a href="${solution.source}" target="_blank" rel="noopener noreferrer">📚 View Problem Source</a></div>`
        : '';

    return `
        <div class="solution-card">
            <h3>${solution.name}</h3>
            <div class="problem-name">${escapeHtml(solution.problem)}</div>
            <div class="language-badge ${solution.language}">${capitalizeLanguage(solution.language)}</div>
            <div><a href="https://github.com/Aaqibhafeezkhan/algo-solutions-python/blob/main/${solution.path}" target="_blank" rel="noopener noreferrer">📂 View File</a></div>
            ${sourceHtml}
        </div>
    `;
}

function capitalizeLanguage(lang) {
    const map = {
        'python': 'Python',
        'javascript': 'JavaScript',
        'cpp': 'C++',
        'java': 'Java'
    };
    return map[lang] || lang;
}

function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}
