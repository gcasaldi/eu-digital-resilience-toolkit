// EU Digital Resilience Toolkit - Main Application Logic

// Get assessment engine from assessment.js
const { 
    assessmentData, 
    phases, 
    assessmentQuestions,
    assessGovernance,
    assessLogging,
    assessThirdParty,
    assessIncident,
    calculateRiskLevel
} = window.assessmentEngine;

let currentPhase = 0;

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    setupNavigation();
    initializeAssessment();
});

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
    currentPhase = 0;
    window.assessmentEngine.currentPhase = 0;
    
    // Reset assessment data
    Object.keys(assessmentData).forEach(key => {
        assessmentData[key] = Array.isArray(assessmentData[key]) ? [] : '';
    });
    
    showView('assessment');
    document.querySelector('[data-view="assessment"]').classList.add('active');
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('[data-view="assessment"]').classList.add('active');
    
    renderPhase();
}

// Initialize assessment UI
function initializeAssessment() {
    renderPhase();
}

// Render current phase
function renderPhase() {
    updateProgress();
    
    if (currentPhase === 4) {
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
    
    let html = `
        <div class="phase-content">
            <h2>${phaseQuestions.title}</h2>
            <p class="phase-subtitle">${phaseQuestions.subtitle}</p>
            <form id="phase-form">
    `;
    
    phaseQuestions.questions.forEach(question => {
        // Check conditional display
        if (question.conditional && !question.conditional()) {
            return;
        }
        
        html += `<div class="form-group">`;
        html += `<label for="${question.id}">${question.label}</label>`;
        
        if (question.type === 'select') {
            html += `<select id="${question.id}" name="${question.id}">`;
            html += `<option value="">-- Select an option --</option>`;
            question.options.forEach(option => {
                const selected = assessmentData[question.id] === option ? 'selected' : '';
                html += `<option value="${option}" ${selected}>${option}</option>`;
            });
            html += `</select>`;
        } else if (question.type === 'checkbox') {
            html += `<div class="checkbox-group">`;
            question.options.forEach(option => {
                const checked = Array.isArray(assessmentData[question.id]) && 
                                assessmentData[question.id].includes(option) ? 'checked' : '';
                html += `
                    <label class="checkbox-label">
                        <input type="checkbox" name="${question.id}" value="${option}" ${checked}>
                        ${option}
                    </label>
                `;
            });
            html += `</div>`;
        }
        
        html += `</div>`;
    });
    
    html += `</form></div>`;
    content.innerHTML = html;
    
    // Add event listeners to form elements
    addFormListeners();
    
    // Update navigation buttons
    updateNavigationButtons();
}

// Add event listeners to form elements
function addFormListeners() {
    const form = document.getElementById('phase-form');
    if (!form) return;
    
    // Handle select elements
    form.querySelectorAll('select').forEach(select => {
        select.addEventListener('change', function() {
            assessmentData[this.name] = this.value;
            // Re-render to show/hide conditional questions
            renderPhase();
        });
    });
    
    // Handle checkboxes
    form.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            if (!Array.isArray(assessmentData[this.name])) {
                assessmentData[this.name] = [];
            }
            
            if (this.checked) {
                if (!assessmentData[this.name].includes(this.value)) {
                    assessmentData[this.name].push(this.value);
                }
            } else {
                const index = assessmentData[this.name].indexOf(this.value);
                if (index > -1) {
                    assessmentData[this.name].splice(index, 1);
                }
            }
            
            // Re-render to show/hide conditional questions
            renderPhase();
        });
    });
}

// Update progress bar and steps
function updateProgress() {
    const progressFill = document.getElementById('progress-fill');
    const progressSteps = document.getElementById('progress-steps');
    
    const progressPercentage = (currentPhase / (phases.length - 1)) * 100;
    progressFill.style.width = `${progressPercentage}%`;
    
    let stepsHTML = '';
    phases.forEach((phase, index) => {
        let className = 'progress-step ';
        if (index < currentPhase) {
            className += 'completed';
        } else if (index === currentPhase) {
            className += 'active';
        } else {
            className += 'pending';
        }
        
        const icon = index < currentPhase ? '✓' : index === currentPhase ? '→' : '';
        stepsHTML += `<div class="${className}">${icon} ${phase.name}</div>`;
    });
    
    progressSteps.innerHTML = stepsHTML;
}

// Update navigation buttons
function updateNavigationButtons() {
    const btnBack = document.getElementById('btn-back');
    const btnNext = document.getElementById('btn-next');
    
    // Show/hide back button
    if (currentPhase === 0) {
        btnBack.style.display = 'none';
    } else {
        btnBack.style.display = 'block';
    }
    
    // Update next button text
    if (currentPhase === 3) {
        btnNext.textContent = 'Generate Assessment Report ✓';
    } else {
        btnNext.textContent = 'Continue →';
    }
}

// Navigate to next phase
function nextPhase() {
    if (currentPhase < phases.length - 1) {
        currentPhase++;
        window.assessmentEngine.currentPhase = currentPhase;
        renderPhase();
        window.scrollTo(0, 0);
    }
}

// Navigate to previous phase
function previousPhase() {
    if (currentPhase > 0) {
        currentPhase--;
        window.assessmentEngine.currentPhase = currentPhase;
        renderPhase();
        window.scrollTo(0, 0);
    }
}

// Render assessment results
function renderResults() {
    const govResult = assessGovernance(assessmentData);
    const logResult = assessLogging(assessmentData);
    const tpResult = assessThirdParty(assessmentData);
    const incResult = assessIncident(assessmentData);
    
    const totalScore = govResult.score + logResult.score + tpResult.score + incResult.score;
    const riskLevel = calculateRiskLevel(totalScore);
    
    const allFindings = [
        ...govResult.findings,
        ...logResult.findings,
        ...tpResult.findings,
        ...incResult.findings
    ];
    
    const allRecs = [
        ...govResult.recs,
        ...logResult.recs,
        ...tpResult.recs,
        ...incResult.recs
    ];
    
    const allGaps = {
        'Governance & Scope': govResult.gaps,
        'Logging & Monitoring': logResult.gaps,
        'ICT Third-Party Risk': tpResult.gaps,
        'Incident & Resilience': incResult.gaps
    };
    
    const content = document.getElementById('assessment-content');
    const riskColor = riskLevel === 'LOW' ? '🟢' : riskLevel === 'MEDIUM' ? '🟡' : '🔴';
    
    let html = `
        <div class="results-summary">
            <h2>✓ Assessment Complete</h2>
            <div class="score-display">
                <div class="score-item">
                    <span class="score-value">${totalScore}/100</span>
                    <span class="score-label">Total Score</span>
                </div>
                <div class="score-item">
                    <span class="score-value">${riskColor} ${riskLevel}</span>
                    <span class="score-label">Risk Level</span>
                </div>
            </div>
        </div>
        
        <div class="score-display" style="background: white; padding: 20px; border-radius: 12px; margin-bottom: 20px;">
            <div class="score-item">
                <span class="score-value">${govResult.score}/25</span>
                <span class="score-label">Governance</span>
            </div>
            <div class="score-item">
                <span class="score-value">${logResult.score}/25</span>
                <span class="score-label">Logging</span>
            </div>
            <div class="score-item">
                <span class="score-value">${tpResult.score}/25</span>
                <span class="score-label">Third-Party</span>
            </div>
            <div class="score-item">
                <span class="score-value">${incResult.score}/25</span>
                <span class="score-label">Incident</span>
            </div>
        </div>
        
        <div class="results-details">
            <div class="result-section">
                <h3>📋 Regulatory Gaps Identified</h3>
    `;
    
    for (const [domain, gaps] of Object.entries(allGaps)) {
        if (gaps.length > 0) {
            html += `<h4>${domain}</h4>`;
            gaps.forEach(gap => {
                html += `<div class="gap-item">${gap}</div>`;
            });
        }
    }
    
    html += `
            </div>
            
            <div class="result-section">
                <h3>🔍 Findings (${allFindings.length} items)</h3>
                <ul>
    `;
    
    allFindings.forEach(finding => {
        html += `<li>${finding}</li>`;
    });
    
    html += `
                </ul>
            </div>
            
            <div class="result-section">
                <h3>💡 Recommendations (${allRecs.length} items)</h3>
    `;
    
    allRecs.forEach((rec, index) => {
        const priority = index < 3 ? 'high' : index < 6 ? 'medium' : 'low';
        const priorityText = index < 3 ? '🔴 HIGH' : index < 6 ? '🟡 MEDIUM' : '🟢 LOW';
        html += `<div class="recommendation-item priority-${priority}"><strong>${priorityText}</strong> - ${rec}</div>`;
    });
    
    html += `
            </div>
        </div>
        
        <div class="export-section">
            <h3>📥 Export Report</h3>
            <div class="export-buttons">
                <button class="btn-primary" onclick="exportTextReport()">📄 Download Text Report</button>
                <button class="btn-primary" onclick="exportCSVReport()">📊 Download CSV Data</button>
                <button class="btn-secondary" onclick="restartAssessment()">🔄 Start New Assessment</button>
            </div>
        </div>
    `;
    
    content.innerHTML = html;
    
    // Hide navigation buttons on results page
    document.getElementById('btn-back').style.display = 'block';
    document.getElementById('btn-next').style.display = 'none';
    
    // Store results for export
    window.assessmentResults = {
        totalScore,
        riskLevel,
        scores: {
            governance: govResult.score,
            logging: logResult.score,
            thirdParty: tpResult.score,
            incident: incResult.score
        },
        findings: allFindings,
        recommendations: allRecs,
        gaps: allGaps,
        data: assessmentData
    };
}

// Export functions
function exportTextReport() {
    const results = window.assessmentResults;
    if (!results) return;
    
    const timestamp = new Date().toISOString().split('T')[0];
    const sector = assessmentData.sector || 'Unknown';
    const scope = Array.isArray(assessmentData.scope) ? assessmentData.scope.join(', ') : 'Unknown';
    
    let report = `
================================================================================
EU DIGITAL RESILIENCE ASSESSMENT REPORT
================================================================================

Generated: ${new Date().toLocaleString()}
Sector: ${sector}
Regulatory Scope: ${scope}

--------------------------------------------------------------------------------
EXECUTIVE SUMMARY
--------------------------------------------------------------------------------

Total Risk Score: ${results.totalScore}/100
Risk Classification: ${results.riskLevel}

Domain Breakdown:
  - Governance & Scope:        ${results.scores.governance}/25
  - Logging & Monitoring:      ${results.scores.logging}/25
  - ICT Third-Party Risk:      ${results.scores.thirdParty}/25
  - Incident & Resilience:     ${results.scores.incident}/25

--------------------------------------------------------------------------------
REGULATORY GAPS IDENTIFIED
--------------------------------------------------------------------------------

`;
    
    for (const [domain, gaps] of Object.entries(results.gaps)) {
        if (gaps.length > 0) {
            report += `\n${domain}:\n`;
            gaps.forEach(gap => {
                report += `  - ${gap}\n`;
            });
        }
    }
    
    report += `
--------------------------------------------------------------------------------
FINDINGS (${results.findings.length} items)
--------------------------------------------------------------------------------

`;
    
    results.findings.forEach((finding, index) => {
        report += `${index + 1}. ${finding}\n`;
    });
    
    report += `
--------------------------------------------------------------------------------
RECOMMENDATIONS (${results.recommendations.length} items)
--------------------------------------------------------------------------------

`;
    
    results.recommendations.forEach((rec, index) => {
        const priority = index < 3 ? '[HIGH]' : index < 6 ? '[MEDIUM]' : '[LOW]';
        report += `${priority} ${rec}\n`;
    });
    
    report += `
--------------------------------------------------------------------------------
DISCLAIMER
--------------------------------------------------------------------------------
This assessment is a readiness and risk evaluation tool. It does not constitute
legal advice. Organizations should consult legal counsel for compliance strategy.

Tool: EU Digital Resilience Toolkit v1.0
Framework: NIS2 Directive + DORA Regulation (integrated assessment)
================================================================================
`;
    
    downloadFile(`eu_resilience_assessment_${timestamp}.txt`, report, 'text/plain');
}

function exportCSVReport() {
    const results = window.assessmentResults;
    if (!results) return;
    
    const timestamp = new Date().toISOString().split('T')[0];
    
    let csv = 'Metric,Value\n';
    csv += `Timestamp,${new Date().toLocaleString()}\n`;
    csv += `Sector,${assessmentData.sector || 'Unknown'}\n`;
    csv += `Regulatory Scope,"${Array.isArray(assessmentData.scope) ? assessmentData.scope.join(', ') : 'Unknown'}"\n`;
    csv += `Total Score,${results.totalScore}\n`;
    csv += `Risk Level,${results.riskLevel}\n`;
    csv += `Governance Score,${results.scores.governance}\n`;
    csv += `Logging Score,${results.scores.logging}\n`;
    csv += `Third-Party Score,${results.scores.thirdParty}\n`;
    csv += `Incident Score,${results.scores.incident}\n`;
    csv += '\nFindings\n';
    
    results.findings.forEach(finding => {
        csv += `"${finding}"\n`;
    });
    
    csv += '\nRecommendations\n';
    results.recommendations.forEach(rec => {
        csv += `"${rec}"\n`;
    });
    
    downloadFile(`eu_resilience_assessment_${timestamp}.csv`, csv, 'text/csv');
}

function downloadFile(filename, content, mimeType) {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}

function restartAssessment() {
    currentPhase = 0;
    window.assessmentEngine.currentPhase = 0;
    
    // Reset assessment data
    Object.keys(assessmentData).forEach(key => {
        assessmentData[key] = Array.isArray(assessmentData[key]) ? [] : '';
    });
    
    renderPhase();
    window.scrollTo(0, 0);
}

// Make functions available globally
window.startAssessment = startAssessment;
window.nextPhase = nextPhase;
window.previousPhase = previousPhase;
window.exportTextReport = exportTextReport;
window.exportCSVReport = exportCSVReport;
window.restartAssessment = restartAssessment;
