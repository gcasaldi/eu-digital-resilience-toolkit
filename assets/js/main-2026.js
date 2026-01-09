// EU Digital Resilience Toolkit 2026 - Main Application Logic
// Created by Giovanni Casaldi | @gcasaldi

let currentPhase = 0;

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, initializing...');
    
    // Verify assessment engine is loaded
    if (!window.assessmentEngine) {
        console.error('Assessment engine not loaded!');
        return;
    }
    
    console.log('Assessment engine loaded successfully');
    setupNavigation();
    setupStartButton();
    renderPhase();
});

// Setup start assessment button
function setupStartButton() {
    const startBtn = document.getElementById('start-assessment');
    if (startBtn) {
        startBtn.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Start button clicked');
            startAssessment();
        });
    } else {
        console.error('Start button not found');
    }
}

// Setup navigation between views
function setupNavigation() {
    const navButtons = document.querySelectorAll('.nav-btn');
    navButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const view = this.getAttribute('data-view');
            showView(view);
            
            // Update active state
            navButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

function showView(viewName) {
    const views = document.querySelectorAll('.view');
    views.forEach(view => {
        view.classList.remove('active');
    });
    
    const targetView = document.getElementById(`${viewName}-view`);
    if (targetView) {
        targetView.classList.add('active');
    }
}

// Start assessment
function startAssessment() {
    console.log('Starting assessment...');
    currentPhase = 0;
    
    // Reset assessment data
    const { assessmentData } = window.assessmentEngine;
    Object.keys(assessmentData).forEach(key => {
        if (Array.isArray(assessmentData[key])) {
            assessmentData[key] = [];
        } else {
            assessmentData[key] = '';
        }
    });
    
    showView('assessment');
    
    // Update navigation active state
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    const assessmentNavBtn = document.querySelector('[data-view="assessment"]');
    if (assessmentNavBtn) {
        assessmentNavBtn.classList.add('active');
    }
    
    renderPhase();
}

// Update progress indicator
function updateProgress() {
    const { phases } = window.assessmentEngine;
    const progress = document.getElementById('progress');
    const progressBar = document.getElementById('progress-bar');
    const progressText = document.getElementById('progress-text');
    
    if (!progress || !progressBar || !progressText) {
        console.error('Progress elements not found');
        return;
    }
    
    // Total phases -1 (results phase doesn't count)
    const totalPhases = phases.length - 1;
    const percentage = (currentPhase / totalPhases) * 100;
    
    progressBar.style.width = percentage + '%';
    progressText.textContent = `Phase ${currentPhase + 1} of ${totalPhases}`;
    
    if (currentPhase === totalPhases) {
        progressText.textContent = 'Assessment Complete';
        progress.style.display = 'none';
    } else {
        progress.style.display = 'block';
    }
}

// Render current phase
function renderPhase() {
    const { phases, assessmentQuestions, assessmentData } = window.assessmentEngine;
    
    updateProgress();
    
    // Check if we're at results phase
    if (currentPhase === 6) {
        renderResults();
        return;
    }
    
    const phase = phases[currentPhase];
    const phaseQuestions = assessmentQuestions[phase.key];
    
    if (!phaseQuestions) {
        console.error('Phase questions not found:', phase.key);
        return;
    }
    
    const content = document.getElementById('assessment-content');
    if (!content) {
        console.error('Assessment content element not found');
        return;
    }
    
    let html = `
        <div class="phase-content">
            <h2>${phaseQuestions.title}</h2>
            <p class="phase-subtitle">${phaseQuestions.subtitle}</p>
            <form id="phase-form">
    `;
    
    phaseQuestions.questions.forEach(question => {
        html += `<div class="question-group">`;
        html += `<label>${question.label}</label>`;
        
        if (question.type === 'select') {
            const currentValue = assessmentData[question.id] || '';
            html += `<select id="${question.id}" name="${question.id}" onchange="showFeedback('${question.id}')" required>`;
            html += `<option value="">Seleziona una risposta...</option>`;
            question.options.forEach(option => {
                const selected = currentValue === option ? 'selected' : '';
                html += `<option value="${option}" ${selected}>${option}</option>`;
            });
            html += `</select>`;
            html += `<div id="feedback-${question.id}" class="feedback-box"></div>`;
        } else if (question.type === 'checkbox') {
            const currentValues = assessmentData[question.id] || [];
            question.options.forEach((option, idx) => {
                const checked = currentValues.includes(option) ? 'checked' : '';
                html += `
                    <div class="checkbox-group">
                        <input type="checkbox" id="${question.id}_${idx}" name="${question.id}" value="${option}" ${checked}>
                        <label for="${question.id}_${idx}">${option}</label>
                    </div>
                `;
            });
        } else if (question.type === 'textarea') {
            const currentValue = assessmentData[question.id] || '';
            html += `<textarea id="${question.id}" name="${question.id}" rows="3">${currentValue}</textarea>`;
        } else { // text input
            const currentValue = assessmentData[question.id] || '';
            html += `<input type="text" id="${question.id}" name="${question.id}" value="${currentValue}" required>`;
        }
        
        html += `</div>`;
    });
    
    html += `
            </form>
        </div>
    `;
    
    content.innerHTML = html;
    
    // Update navigation buttons
    updateNavigationButtons();
}

function updateNavigationButtons() {
    const btnBack = document.getElementById('btn-back');
    const btnNext = document.getElementById('btn-next');
    
    if (!btnBack || !btnNext) {
        console.error('Navigation buttons not found');
        return;
    }
    
    if (currentPhase === 0) {
        btnBack.style.display = 'none';
    } else {
        btnBack.style.display = 'inline-block';
    }
    
    if (currentPhase === 5) {
        btnNext.textContent = 'View Results →';
    } else {
        btnNext.textContent = 'Continue →';
    }
}

// Navigate to next phase
function nextPhase() {
    const { assessmentData, assessmentQuestions, phases } = window.assessmentEngine;
    const phase = phases[currentPhase];
    const phaseQuestions = assessmentQuestions[phase.key];
    
    if (!phaseQuestions) {
        currentPhase++;
        renderPhase();
        return;
    }
    
    // Save current phase data
    phaseQuestions.questions.forEach(question => {
        if (question.type === 'checkbox') {
            const checkboxes = document.querySelectorAll(`input[name="${question.id}"]:checked`);
            assessmentData[question.id] = Array.from(checkboxes).map(cb => cb.value);
        } else {
            const element = document.getElementById(question.id);
            if (element) {
                assessmentData[question.id] = element.value;
            }
        }
    });
    
    // Validate required fields
    const form = document.getElementById('phase-form');
    if (form && !form.checkValidity()) {
        form.reportValidity();
        return;
    }
    
    currentPhase++;
    renderPhase();
    window.scrollTo(0, 0);
}

// Navigate to previous phase
function previousPhase() {
    if (currentPhase > 0) {
        currentPhase--;
        renderPhase();
        window.scrollTo(0, 0);
    }
}

// Render results
function renderResults() {
    const {
        assessmentData,
        assessGovernance,
        assessRiskManagement,
        assessSupplyChain,
        assessIncidentResponse,
        assessTechnicalMeasures,
        assessAIEthics,
        calculateRiskLevel
    } = window.assessmentEngine;
    
    // Calculate all scores
    const govResult = assessGovernance(assessmentData);
    const riskResult = assessRiskManagement(assessmentData);
    const scResult = assessSupplyChain(assessmentData);
    const irResult = assessIncidentResponse(assessmentData);
    const techResult = assessTechnicalMeasures(assessmentData);
    const aiResult = assessAIEthics(assessmentData);
    
    const totalScore = govResult.score + riskResult.score + scResult.score + 
                       irResult.score + techResult.score + aiResult.score;
    
    const riskLevel = calculateRiskLevel(totalScore);
    
    // Combine all findings and recommendations
    const allFindings = [
        ...govResult.findings,
        ...riskResult.findings,
        ...scResult.findings,
        ...irResult.findings,
        ...techResult.findings,
        ...aiResult.findings
    ];
    
    const allGaps = [
        ...govResult.gaps,
        ...riskResult.gaps,
        ...scResult.gaps,
        ...irResult.gaps,
        ...techResult.gaps,
        ...aiResult.gaps
    ];
    
    const allRecs = [
        ...govResult.recs,
        ...riskResult.recs,
        ...scResult.recs,
        ...irResult.recs,
        ...techResult.recs,
        ...aiResult.recs
    ];
    
    // Hide progress
    document.getElementById('progress').style.display = 'none';
    
    // Render results view
    const content = document.getElementById('assessment-content');
    
    let html = `
        <div class="results-container">
            <h2>📊 Assessment Results - Audit 2026</h2>
            
            <div class="score-summary">
                <div class="total-score">
                    <h3>Overall Compliance Score</h3>
                    <div class="score-value">${totalScore}/100</div>
                    <div class="risk-badge risk-${riskLevel.toLowerCase()}">${riskLevel} RISK</div>
                </div>
                
                <div class="area-scores">
                    <div class="area-score">
                        <strong>Governance</strong>
                        <span>${govResult.score}/20</span>
                    </div>
                    <div class="area-score">
                        <strong>Risk Management</strong>
                        <span>${riskResult.score}/15</span>
                    </div>
                    <div class="area-score">
                        <strong>Supply Chain</strong>
                        <span>${scResult.score}/15</span>
                    </div>
                    <div class="area-score">
                        <strong>Incident Response</strong>
                        <span>${irResult.score}/15</span>
                    </div>
                    <div class="area-score">
                        <strong>Technical Measures</strong>
                        <span>${techResult.score}/20</span>
                    </div>
                    <div class="area-score">
                        <strong>AI & Ethics</strong>
                        <span>${aiResult.score}/15</span>
                    </div>
                </div>
            </div>
            
            ${allFindings.length > 0 ? `
            <div class="results-section">
                <h3>🔴 Critical Findings (${allFindings.length})</h3>
                <ul class="findings-list">
                    ${allFindings.map(f => `<li>${f}</li>`).join('')}
                </ul>
            </div>
            ` : '<div class="success-message">✅ No critical findings - Excellent compliance posture!</div>'}
            
            ${allGaps.length > 0 ? `
            <div class="results-section">
                <h3>📋 Regulatory Gaps (${allGaps.length})</h3>
                <ul class="gaps-list">
                    ${allGaps.map(g => `<li>${g}</li>`).join('')}
                </ul>
            </div>
            ` : ''}
            
            ${allRecs.length > 0 ? `
            <div class="results-section">
                <h3>💡 Recommended Actions (${allRecs.length})</h3>
                <ol class="recommendations-list">
                    ${allRecs.map(r => `<li>${r}</li>`).join('')}
                </ol>
            </div>
            ` : ''}
            
            <div class="export-section">
                <h3>Export Results</h3>
                <button onclick="exportTextReport()" class="btn-secondary">📄 Download Text Report</button>
                <button onclick="exportCSVReport()" class="btn-secondary">📊 Download CSV</button>
            </div>
            
            <button onclick="startAssessment()" class="btn-primary">🔄 Start New Assessment</button>
        </div>
    `;
    
    content.innerHTML = html;
    
    // Hide navigation buttons
    document.getElementById('btn-back').style.display = 'none';
    document.getElementById('btn-next').style.display = 'none';
}

// Export text report
function exportTextReport() {
    const { assessmentData } = window.assessmentEngine;
    
    const govResult = window.assessmentEngine.assessGovernance(assessmentData);
    const riskResult = window.assessmentEngine.assessRiskManagement(assessmentData);
    const scResult = window.assessmentEngine.assessSupplyChain(assessmentData);
    const irResult = window.assessmentEngine.assessIncidentResponse(assessmentData);
    const techResult = window.assessmentEngine.assessTechnicalMeasures(assessmentData);
    const aiResult = window.assessmentEngine.assessAIEthics(assessmentData);
    
    const totalScore = govResult.score + riskResult.score + scResult.score + 
                       irResult.score + techResult.score + aiResult.score;
    const riskLevel = window.assessmentEngine.calculateRiskLevel(totalScore);
    
    let report = `EU DIGITAL RESILIENCE AUDIT 2026 - ASSESSMENT REPORT\n`;
    report += `Generated: ${new Date().toLocaleString()}\n`;
    report += `=`.repeat(70) + `\n\n`;
    
    report += `OVERALL COMPLIANCE SCORE: ${totalScore}/100\n`;
    report += `RISK LEVEL: ${riskLevel}\n\n`;
    
    report += `AREA SCORES:\n`;
    report += `- Governance & Legal: ${govResult.score}/20\n`;
    report += `- Risk & Asset Management: ${riskResult.score}/15\n`;
    report += `- Supply Chain: ${scResult.score}/15\n`;
    report += `- Incident Response: ${irResult.score}/15\n`;
    report += `- Technical Measures: ${techResult.score}/20\n`;
    report += `- AI & Ethics: ${aiResult.score}/15\n\n`;
    
    const allFindings = [...govResult.findings, ...riskResult.findings, ...scResult.findings,
                         ...irResult.findings, ...techResult.findings, ...aiResult.findings];
    const allGaps = [...govResult.gaps, ...riskResult.gaps, ...scResult.gaps,
                     ...irResult.gaps, ...techResult.gaps, ...aiResult.gaps];
    const allRecs = [...govResult.recs, ...riskResult.recs, ...scResult.recs,
                     ...irResult.recs, ...techResult.recs, ...aiResult.recs];
    
    if (allFindings.length > 0) {
        report += `CRITICAL FINDINGS (${allFindings.length}):\n`;
        report += `-`.repeat(70) + `\n`;
        allFindings.forEach((finding, idx) => {
            report += `${idx + 1}. ${finding}\n`;
        });
        report += `\n`;
    }
    
    if (allGaps.length > 0) {
        report += `REGULATORY GAPS (${allGaps.length}):\n`;
        report += `-`.repeat(70) + `\n`;
        allGaps.forEach((gap, idx) => {
            report += `${idx + 1}. ${gap}\n`;
        });
        report += `\n`;
    }
    
    if (allRecs.length > 0) {
        report += `RECOMMENDED ACTIONS (${allRecs.length}):\n`;
        report += `-`.repeat(70) + `\n`;
        allRecs.forEach((rec, idx) => {
            report += `${idx + 1}. ${rec}\n`;
        });
        report += `\n`;
    }
    
    report += `\n` + `=`.repeat(70) + `\n`;
    report += `Report created by EU Digital Resilience Toolkit\n`;
    report += `Created by Giovanni Casaldi | @gcasaldi\n`;
    report += `https://gcasaldi.github.io/eu-digital-resilience-toolkit/\n`;
    
    const blob = new Blob([report], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `eu-resilience-audit-${Date.now()}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// Real-time feedback function
function showFeedback(questionId) {
    const element = document.getElementById(questionId);
    const feedbackDiv = document.getElementById(`feedback-${questionId}`);
    
    if (!element || !feedbackDiv) return;
    
    const value = element.value;
    if (!value) {
        feedbackDiv.innerHTML = '';
        return;
    }
    
    // Define feedback rules for critical questions
    const feedbackRules = {
        // Governance
        'board_approval': {
            good: ['piano completo approvato con delibera CdA', 'piano pluriennale'],
            warning: ['Parziale', 'datato 2024'],
            critical: ['Nessuna approvazione']
        },
        'executive_training': {
            good: ['formazione certificata annuale'],
            warning: ['Informale'],
            critical: ['Nessuna formazione']
        },
        'model_231_updated': {
            good: ['Sì, aggiornato 2026'],
            warning: ['Non presente', 'Obsoleto'],
            critical: ['mai aggiornato', 'non include']
        },
        'roles_assigned': {
            good: ['formalmente nominati'],
            warning: ['Parziale', 'Solo DPO'],
            critical: ['Nessuna nomina']
        },
        // Technical
        'mfa_zerotrust': {
            good: ['Zero Trust completo'],
            warning: ['MFA per tutti'],
            critical: ['solo per VPN', 'Nessuna MFA']
        },
        'encryption': {
            good: ['crittografia completa'],
            warning: ['Parziale'],
            critical: ['Nessuna crittografia']
        },
        'vulnerability_management': {
            good: ['processo automatizzato'],
            warning: ['Manuale'],
            critical: ['Nessun processo']
        },
        'immutable_backups': {
            good: ['WORM testati'],
            warning: ['Buono'],
            critical: ['Nessun backup', 'non protetti', 'non testati']
        }
    };
    
    const rule = feedbackRules[questionId];
    if (!rule) return;
    
    let feedbackClass = 'feedback-neutral';
    let feedbackIcon = 'ℹ️';
    let feedbackText = '';
    
    // Check critical
    if (rule.critical && rule.critical.some(keyword => value.includes(keyword))) {
        feedbackClass = 'feedback-critical';
        feedbackIcon = '🔴';
        feedbackText = '<strong>CRITICO:</strong> Questa risposta indica un gap significativo di conformità. Priorità massima.';
    }
    // Check warning
    else if (rule.warning && rule.warning.some(keyword => value.includes(keyword))) {
        feedbackClass = 'feedback-warning';
        feedbackIcon = '🟡';
        feedbackText = '<strong>ATTENZIONE:</strong> Richiede miglioramento. Implementare azioni correttive a breve termine.';
    }
    // Check good
    else if (rule.good && rule.good.some(keyword => value.includes(keyword))) {
        feedbackClass = 'feedback-good';
        feedbackIcon = '🟢';
        feedbackText = '<strong>OTTIMO:</strong> Risposta conforme alle best practice.';
    }
    
    if (feedbackText) {
        feedbackDiv.innerHTML = `<div class="${feedbackClass}">${feedbackIcon} ${feedbackText}</div>`;
        feedbackDiv.style.display = 'block';
    } else {
        feedbackDiv.innerHTML = '';
        feedbackDiv.style.display = 'none';
    }
}

// Export CSV report
function exportCSVReport() {
    const { assessmentData } = window.assessmentEngine;
    
    const govResult = window.assessmentEngine.assessGovernance(assessmentData);
    const riskResult = window.assessmentEngine.assessRiskManagement(assessmentData);
    const scResult = window.assessmentEngine.assessSupplyChain(assessmentData);
    const irResult = window.assessmentEngine.assessIncidentResponse(assessmentData);
    const techResult = window.assessmentEngine.assessTechnicalMeasures(assessmentData);
    const aiResult = window.assessmentEngine.assessAIEthics(assessmentData);
    
    const totalScore = govResult.score + riskResult.score + scResult.score + 
                       irResult.score + techResult.score + aiResult.score;
    const riskLevel = window.assessmentEngine.calculateRiskLevel(totalScore);
    
    let csv = `Area,Score,Max Score\n`;
    csv += `Governance & Legal,${govResult.score},20\n`;
    csv += `Risk & Asset Management,${riskResult.score},15\n`;
    csv += `Supply Chain,${scResult.score},15\n`;
    csv += `Incident Response,${irResult.score},15\n`;
    csv += `Technical Measures,${techResult.score},20\n`;
    csv += `AI & Ethics,${aiResult.score},15\n`;
    csv += `TOTAL,${totalScore},100\n`;
    csv += `RISK LEVEL,${riskLevel},\n\n`;
    
    csv += `Question,Response\n`;
    Object.keys(assessmentData).forEach(key => {
        const value = Array.isArray(assessmentData[key]) ? 
                     assessmentData[key].join('; ') : 
                     assessmentData[key];
        csv += `"${key}","${value}"\n`;
    });
    
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `eu-resilience-audit-${Date.now()}.csv`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}
