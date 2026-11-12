let allSolutions = [];

document.addEventListener('DOMContentLoaded', async () => {
    await loadSolutions();
    setupEventListeners();
    populateTopicFilter();
    filterAndDisplay();
});

async function loadSolutions() {
    const container = document.getElementById('solutionsList');
    try {
        const response = await fetch('data.json');
        if (!response.ok) {
            throw new Error(`Failed to load solution index (${response.status})`);
        }
        const data = await response.json();
        if (!Array.isArray(data)) {
            throw new Error('The solution index must contain a JSON array');
        }
        allSolutions = data.map(solution => ({
            ...solution,
            topics: Array.isArray(solution.topics) && solution.topics.length
                ? solution.topics
                : ['General']
        }));
    } catch (error) {
        console.error('Error loading solutions:', error);
        container.innerHTML = '<div class="no-results"><h2>Unable to load solutions</h2><p>Please refresh the page or try again later.</p></div>';
    }
}

function setupEventListeners() {
    document.getElementById('searchInput').addEventListener('input', filterAndDisplay);
    document.getElementById('languageFilter').addEventListener('change', filterAndDisplay);
    document.getElementById('topicFilter').addEventListener('change', filterAndDisplay);
}

function populateTopicFilter() {
    const topicFilter = document.getElementById('topicFilter');
    const topics = [...new Set(allSolutions.flatMap(solution => solution.topics))]
        .filter(Boolean)
        .sort((a, b) => a.localeCompare(b));

    topicFilter.replaceChildren(new Option('All topics', ''));
    topics.forEach(topic => topicFilter.add(new Option(topic, topic)));
}

function filterAndDisplay() {
    const searchTerm = document.getElementById('searchInput').value.trim().toLocaleLowerCase();
    const selectedLanguage = document.getElementById('languageFilter').value;
    const selectedTopic = document.getElementById('topicFilter').value;

    const filtered = allSolutions.filter(solution => {
        const searchableText = [
            solution.problem,
            solution.name,
            solution.filename,
            ...(solution.topics || [])
        ].join(' ').toLocaleLowerCase();
        const matchesSearch = !searchTerm || searchableText.includes(searchTerm);
        const matchesLanguage = !selectedLanguage || solution.language === selectedLanguage;
        const matchesTopic = !selectedTopic || solution.topics.includes(selectedTopic);
        return matchesSearch && matchesLanguage && matchesTopic;
    });

    displaySolutions(filtered);
}

function displaySolutions(solutions) {
    const container = document.getElementById('solutionsList');
    document.getElementById('resultCount').textContent = solutions.length;

    if (solutions.length === 0) {
        container.innerHTML = '<div class="no-results"><h2>No solutions found</h2><p>Try adjusting your search or filter criteria.</p></div>';
        return;
    }

    container.innerHTML = solutions.map(createSolutionCard).join('');
}

function createSolutionCard(solution) {
    const sourceHtml = solution.source
        ? `<div class="source-link"><a href="${escapeAttribute(solution.source)}" target="_blank" rel="noopener noreferrer">View problem source</a></div>`
        : '';
    const topicHtml = solution.topics.map(topic =>
        `<span class="topic-tag">${escapeHtml(topic)}</span>`
    ).join('');

    return `
        <article class="solution-card">
            <h3>${escapeHtml(solution.problem)}</h3>
            <p class="file-name">${escapeHtml(solution.filename)}</p>
            <div class="card-meta">
                <span class="language-badge ${escapeAttribute(solution.language)}">${capitalizeLanguage(solution.language)}</span>
                <div class="topic-list" aria-label="Topics">${topicHtml}</div>
            </div>
            <div><a href="https://github.com/Aaqibhafeezkhan/algo-solutions-python/blob/main/${solution.path.split('/').map(encodeURIComponent).join('/')}" target="_blank" rel="noopener noreferrer">View solution file</a></div>
            ${sourceHtml}
        </article>
    `;
}

function capitalizeLanguage(language) {
    const labels = {
        python: 'Python',
        javascript: 'JavaScript',
        cpp: 'C++',
        java: 'Java',
        typescript: 'TypeScript'
    };
    return labels[language] || language;
}

function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, character => ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    })[character]);
}

function escapeAttribute(value) {
    return escapeHtml(value);
}
