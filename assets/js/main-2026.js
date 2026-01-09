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
        
        // Add help text if available
        if (question.helpText) {
            html += `<p class="help-text">💡 ${question.helpText}</p>`;
        }
        
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
    console.log('=== RENDERING RESULTS ===');
    
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
    
    console.log('Assessment data:', assessmentData);
    
    // Calculate all scores
    const govResult = assessGovernance(assessmentData);
    const riskResult = assessRiskManagement(assessmentData);
    const scResult = assessSupplyChain(assessmentData);
    const irResult = assessIncidentResponse(assessmentData);
    const techResult = assessTechnicalMeasures(assessmentData);
    const aiResult = assessAIEthics(assessmentData);
    
    console.log('Scores:', {
        governance: govResult.score,
        risk: riskResult.score,
        supply: scResult.score,
        incident: irResult.score,
        technical: techResult.score,
        ai: aiResult.score
    });
    
    const totalScore = govResult.score + riskResult.score + scResult.score + 
                       irResult.score + techResult.score + aiResult.score;
    
    const riskLevel = calculateRiskLevel(totalScore);
    
    console.log('Total score:', totalScore, 'Risk level:', riskLevel);
    
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
    
    console.log('Findings:', allFindings.length, 'Gaps:', allGaps.length, 'Recommendations:', allRecs.length);
    
    // Hide progress
    const progressEl = document.getElementById('progress');
    if (progressEl) {
        progressEl.style.display = 'none';
    }
    
    // Render results view
    const content = document.getElementById('assessment-content');
    if (!content) {
        console.error('Assessment content element not found!');
        return;
    }
    
    console.log('Building results HTML...');
    
    let html = `
        <div class="results-container">
            <h2>📊 Risultati Assessment - Audit 2026</h2>
            <p style="text-align: center; color: var(--text-secondary); margin-bottom: 30px;">
                Generato il ${new Date().toLocaleDateString('it-IT')} alle ${new Date().toLocaleTimeString('it-IT')}
            </p>
            
            <div class="score-summary">
                <div class="total-score">
                    <h3>Punteggio Complessivo di Conformità</h3>
                    <div class="score-value">${totalScore}/130</div>
                    <div class="risk-badge risk-${riskLevel.toLowerCase()}">
                        ${riskLevel === 'LOW' ? '🟢 RISCHIO BASSO' : 
                          riskLevel === 'MEDIUM' ? '🟡 RISCHIO MEDIO' : 
                          '🔴 RISCHIO ALTO'}
                    </div>
                    <p style="margin-top: 15px; color: var(--text-secondary);">
                        ${riskLevel === 'LOW' ? 'Eccellente postura di conformità. Mantenere con audit periodici.' :
                          riskLevel === 'MEDIUM' ? 'Buone basi ma gap da colmare. Piano d\'azione prioritizzato necessario.' :
                          'Carenze significative. Azione immediata richiesta per conformità.'}
                    </p>
                    <p style="margin-top: 10px; font-size: 0.9rem; color: var(--text-secondary);">
                        📊 Punteggio massimo aggiornato a 118 punti (include framework internazionali, sicurezza fisica, forensics, Shadow IT)
                    </p>
                </div>
                
                <div class="area-scores">
                    <div class="area-score">
                        <div>
                            <strong>🛡️ Governance</strong>
                            <div class="score-bar">
                                <div class="score-bar-fill" style="width: ${(govResult.score/29)*100}%"></div>
                            </div>
                        </div>
                        <span>${govResult.score}/29</span>
                    </div>
                    <div class="area-score">
                        <div>
                            <strong>📋 Risk Management</strong>
                            <div class="score-bar">
                                <div class="score-bar-fill" style="width: ${(riskResult.score/19)*100}%"></div>
                            </div>
                        </div>
                        <span>${riskResult.score}/19</span>
                    </div>
                    <div class="area-score">
                        <div>
                            <strong>🔗 Supply Chain</strong>
                            <div class="score-bar">
                                <div class="score-bar-fill" style="width: ${(scResult.score/22)*100}%"></div>
                            </div>
                        </div>
                        <span>${scResult.score}/22</span>
                    </div>
                    <div class="area-score">
                        <div>
                            <strong>🚨 Incident Response</strong>
                            <div class="score-bar">
                                <div class="score-bar-fill" style="width: ${(irResult.score/18)*100}%"></div>
                            </div>
                        </div>
                        <span>${irResult.score}/18</span>
                    </div>
                    <div class="area-score">
                        <div>
                            <strong>🔒 Technical + Physical</strong>
                            <div class="score-bar">
                                <div class="score-bar-fill" style="width: ${(techResult.score/27)*100}%"></div>
                            </div>
                        </div>
                        <span>${techResult.score}/27</span>
                    </div>
                    <div class="area-score">
                        <div>
                            <strong>🤖 AI & Ethics</strong>
                            <div class="score-bar">
                                <div class="score-bar-fill" style="width: ${(aiResult.score/15)*100}%"></div>
                            </div>
                        </div>
                        <span>${aiResult.score}/15</span>
                    </div>
                </div>
            </div>
            
            ${allFindings.length > 0 ? `
            <div class="results-section">
                <h3>🔴 Findings Critici (${allFindings.length})</h3>
                <p style="color: var(--text-secondary); margin-bottom: 15px;">
                    Problemi e carenze identificati che richiedono attenzione immediata
                </p>
                <ul class="findings-list">
                    ${allFindings.map(f => `<li>${f}</li>`).join('')}
                </ul>
            </div>
            ` : '<div class="success-message">✅ Nessun finding critico - Eccellente postura di conformità!</div>'}
            
            ${allGaps.length > 0 ? `
            <div class="results-section">
                <h3>📋 Gap Normativi (${allGaps.length})</h3>
                <p style="color: var(--text-secondary); margin-bottom: 15px;">
                    Requisiti normativi specifici non soddisfatti - riferimenti legislativi
                </p>
                <ul class="gaps-list">
                    ${allGaps.map(g => `<li>${g}</li>`).join('')}
                </ul>
            </div>
            ` : ''}
            
            ${allRecs.length > 0 ? `
            <div class="results-section">
                <h3>💡 Piano d'Azione Raccomandato (${allRecs.length})</h3>
                <p style="color: var(--text-secondary); margin-bottom: 15px;">
                    Azioni concrete e prioritizzate per migliorare la postura di conformità
                </p>
                <ol class="recommendations-list">
                    ${allRecs.map((r, idx) => {
                        const priority = idx < 3 ? '🔴 ALTA PRIORITÀ' : idx < 8 ? '🟡 MEDIA PRIORITÀ' : '🟢 BASSA PRIORITÀ';
                        return `<li><span class="rec-priority">${priority}</span> ${r}</li>`;
                    }).join('')}
                </ol>
            </div>
            ` : ''}
            
            <div class="export-section">
                <h3>📥 Esporta Risultati</h3>
                <p style="color: var(--text-secondary); margin-bottom: 20px;">
                    Scarica il report completo per documentazione interna e preparazione audit
                </p>
                <div style="display: flex; gap: 15px; justify-content: center; flex-wrap: wrap;">
                    <button onclick="exportTextReport()" class="btn-secondary">
                        📄 Report Testuale (.txt)
                    </button>
                    <button onclick="exportCSVReport()" class="btn-secondary">
                        📊 Dati CSV (.csv)
                    </button>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <button onclick="startAssessment()" class="btn-primary" style="font-size: 1.1rem; padding: 15px 40px;">
                    🔄 Inizia Nuovo Assessment
                </button>
            </div>
            
            <div style="text-align: center; margin-top: 30px; padding: 20px; background: #f8fafc; border-radius: 8px;">
                <p style="color: var(--text-secondary); font-size: 0.9rem;">
                    ⚠️ <strong>Disclaimer:</strong> Questo assessment è uno strumento di valutazione della readiness e del rischio. 
                    Non costituisce consulenza legale. Le organizzazioni devono consultare esperti legali per la strategia di conformità.
                </p>
            </div>
        </div>
    `;
    
    console.log('Setting HTML content...');
    content.innerHTML = html;
    
    // Hide navigation buttons
    const btnBack = document.getElementById('btn-back');
    const btnNext = document.getElementById('btn-next');
    if (btnBack) btnBack.style.display = 'none';
    if (btnNext) btnNext.style.display = 'none';
    
    console.log('Results rendered successfully!');
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
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
    
    report += `OVERALL COMPLIANCE SCORE: ${totalScore}/130\n`;
    report += `RISK LEVEL: ${riskLevel}\n\n`;
    
    report += `AREA SCORES:\n`;
    report += `- Governance & Legal: ${govResult.score}/29\n`;
    report += `- Risk & Asset Management: ${riskResult.score}/19\n`;
    report += `- Supply Chain Security: ${scResult.score}/22\n`;
    report += `- Incident Response: ${irResult.score}/18\n`;
    report += `- Technical + Physical Security: ${techResult.score}/27\n`;
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

// Real-time feedback function - COMPREHENSIVE for ALL questions
function showFeedback(questionId) {
    const element = document.getElementById(questionId);
    const feedbackDiv = document.getElementById(`feedback-${questionId}`);
    
    if (!element || !feedbackDiv) {
        console.log('Feedback element not found for:', questionId);
        return;
    }
    
    const value = element.value;
    if (!value || value === '' || value === 'Seleziona una risposta...') {
        feedbackDiv.innerHTML = '';
        feedbackDiv.style.display = 'none';
        return;
    }
    
    console.log('Showing feedback for:', questionId, 'Value:', value);
    
    // Comprehensive feedback rules for ALL questions
    const feedbackRules = {
        // GOVERNANCE
        'board_approval': {
            best: 'Implementa piano pluriennale approvato formalmente dal CdA con delibera documentata e review semestrale',
            good: ['piano completo', 'pluriennale'],
            warning: ['Parziale', 'datato'],
            critical: ['Nessuna', 'non ha']
        },
        'executive_training': {
            best: 'Organizza formazione certificata annuale per tutti i membri del CdA su cyber risk e AI Act con attestati e test',
            good: ['certificata', 'annuale'],
            warning: ['Informale', 'occasionale'],
            critical: ['Nessuna', 'Mai']
        },
        'model_231_updated': {
            best: 'Aggiorna il Modello 231 includendo protocolli specifici per reati informatici, violazioni GDPR e AI Act',
            good: ['2026', 'completo'],
            warning: ['2024', 'parziale'],
            critical: ['non presente', 'mai', 'Obsoleto']
        },
        'roles_assigned': {
            best: 'Nomina formalmente CISO, DPO e Responsabile IA con lettera di incarico, reporting line al CdA e budget dedicato',
            good: ['formalmente nominati', 'tutti i ruoli'],
            warning: ['Parziale', 'Solo DPO'],
            critical: ['Nessuna', 'non nominati']
        },
        'iso_27001_compliance': {
            best: 'Implementa SGSI conforme ISO 27001:2022 come fondamento strutturale per NIS2/DORA - considera certificazione',
            good: ['certificata', 'ISO 27001'],
            warning: ['non certificato', 'informale'],
            critical: ['Nessun SGSI', 'In preparazione']
        },
        'nist_csf_adoption': {
            best: 'Mappa tutti i controlli alle 6 funzioni NIST CSF 2.0 (Govern/Identify/Protect/Detect/Respond/Recover) con KPI',
            good: ['integrato', 'KPI'],
            warning: ['Parziale', 'documentate'],
            critical: ['non mappate', 'Conoscenza base']
        },
        
        // RISK MANAGEMENT
        'unified_asset_inventory': {
            best: 'Crea inventario unificato che integra asset IT (CMDB), registro trattamenti GDPR e sistemi IA con classificazione criticità',
            good: ['unificato', 'completo'],
            warning: ['Parziale', 'solo IT'],
            critical: ['Nessun', 'non esiste']
        },
        'ai_classification': {
            best: 'Classifica tutti i sistemi IA secondo AI Act (Minimo/Limitato/Alto/Inaccettabile) e esegui valutazione conformità per alto rischio',
            good: ['classificati formalmente', 'valutazione'],
            warning: ['Parziale', 'in corso'],
            critical: ['non classificati', 'presenti ma non']
        },
        'dpia_conducted': {
            best: 'Esegui DPIA per tutti i trattamenti ad alto rischio e aggiornala ogni 2-3 anni o al cambio sostanziale',
            good: ['recente', 'aggiornata'],
            warning: ['datata', 'vecchia'],
            critical: ['Mai', 'non eseguita']
        },
        'sbom_available': {
            best: 'Richiedi SBOM (Software Bill of Materials) a tutti i fornitori e crea SBOM per sviluppi interni con monitoraggio CVE automatico',
            good: ['completo', 'tutti'],
            warning: ['Parziale', 'alcuni'],
            critical: ['Nessun', 'non disponibile']
        },
        
        // SUPPLY CHAIN
        'ict_supplier_register': {
            best: 'Crea registro fornitori ICT secondo DORA con: criticità, contratti, SLA, dipendenze, certificazioni, contatti emergenza',
            good: ['completo', 'formalizzato'],
            warning: ['Excel', 'lista'],
            critical: ['Nessun', 'non esiste']
        },
        'contract_clauses_2026': {
            best: 'Aggiorna contratti con clausole: audit rights, incident notification <24h, exit strategy, patch SLA, subcontractor approval',
            good: ['tutti aggiornati', 'clausole complete'],
            warning: ['Parziale', 'solo alcuni'],
            critical: ['standard', 'senza clausole']
        },
        'supplier_certifications': {
            best: 'Richiedi ISO 27001, SOC 2 Type II o attestazioni NIS2 a fornitori critici e verifica annualmente',
            good: ['richieste e verificate', 'ISO'],
            warning: ['richieste ma non', 'alcuni'],
            critical: ['Nessuna', 'non richieste']
        },
        'concentration_risk': {
            best: 'Analizza rischio concentrazione fornitori e definisci strategie mitigazione (fornitori alternativi, multi-cloud)',
            good: ['analisi', 'strategie'],
            warning: ['Parziale', 'informale'],
            critical: ['Nessuna', 'non analizzato']
        },
        'shadow_it_control': {
            best: 'Implementa CASB (Cloud Access Security Broker) + DLP per discovery, controllo e blocco automatico app non autorizzate',
            good: ['Controllo totale', 'CASB'],
            warning: ['Discovery', 'Policy'],
            critical: ['Nessun controllo', 'Consapevolezza']
        },
        'byod_policy': {
            best: 'MDM completo per tutti BYOD + containerization + network segmentation IoT + inventario completo dispositivi',
            good: ['Zero Trust IoT', 'MDM completo'],
            warning: ['MDM parziale', 'Policy base'],
            critical: ['Nessuna policy', 'non gestiti']
        },
        
        // INCIDENT RESPONSE
        'notification_procedure': {
            best: 'Crea piano incident response con tempistiche: 24h CSIRT, 2-4h ESA (DORA), 72h Garante (GDPR) - testalo annualmente',
            good: ['piano completo', 'testato'],
            warning: ['generico', 'non testato'],
            critical: ['Nessun', 'non esiste']
        },
        'severity_classification': {
            best: 'Definisci criteri oggettivi classificazione incidenti con decision tree e soglie quantitative allineate NIS2/DORA/GDPR',
            good: ['criteri formali', 'documentati'],
            warning: ['informali', 'soggettiva'],
            critical: ['Nessun', 'non definiti']
        },
        'emergency_channels': {
            best: 'Implementa sistema comunicazione crisi out-of-band (Signal, Teams separato, telefoni dedicati) e testalo trimestralmente',
            good: ['multipli', 'out-of-band'],
            warning: ['limitati', 'solo Teams'],
            critical: ['Solo email', 'inadeguati']
        },
        'digital_forensics_capability': {
            best: 'Team certificato (GCFA, EnCE) + write-blockers + chain of custody documentata + partnership forensi esterni',
            good: ['Team dedicato', 'certificazioni'],
            warning: ['Procedure', 'tool base'],
            critical: ['Nessuna capacità', 'senza chain']
        },
        
        // TECHNICAL MEASURES
        'mfa_zerotrust': {
            best: 'Implementa MFA per TUTTI gli utenti (priorità admin) e avvia Zero Trust architecture con microsegmentazione',
            good: ['Zero Trust', 'MFA tutti'],
            warning: ['MFA parziale', 'solo VPN'],
            critical: ['Nessuna MFA', 'solo password']
        },
        'encryption': {
            best: 'Implementa crittografia at-rest (database/file) e at-transit (TLS 1.3) con key management HSM e rotazione automatica',
            good: ['completa', 'HSM'],
            warning: ['Parziale', 'solo alcuni'],
            critical: ['Nessuna', 'dati in chiaro']
        },
        'vulnerability_management': {
            best: 'Implementa vulnerability scanning continuo e patch management automatizzato con SLA <7 giorni per CVE critiche',
            good: ['automatizzato', 'continuo'],
            warning: ['Manuale', 'periodico'],
            critical: ['Nessun', 'ad-hoc']
        },
        'immutable_backups': {
            best: 'Implementa backup immutabili WORM con regola 3-2-1, testa restore mensile e verifica RTO/RPO documentati',
            good: ['WORM', 'testati'],
            warning: ['backup ma non immutabili', 'non testati'],
            critical: ['Nessun', 'non protetti']
        },
        'physical_security': {
            best: 'Badge elettronici + biometria + videosorveglianza H24 + mantrap + log accessi correlati con eventi digitali',
            good: ['Biometria', 'monitoraggio H24'],
            warning: ['Badge + videosorveglianza', 'Buono'],
            critical: ['Nessun controllo', 'chiave senza log']
        },
        'environmental_controls': {
            best: 'UPS + generatori + soppressione incendi + clima controllato + monitoraggio ambientale H24 + ridondanza geografica',
            good: ['Eccellente', 'ridondanza'],
            warning: ['Ottima', 'generatori'],
            critical: ['Nessuna protezione', 'Solo UPS']
        },
        'business_continuity_rto': {
            best: '🔥 DOMANDA KILLER! Implementa hot standby/active-active con failover <1h. Test failover semestrale obbligatorio.',
            good: ['Mai', 'failover automatico'],
            warning: ['2-3 giorni', 'DR site'],
            critical: ['Immediatamente', 'Poche ore', 'si ferma']
        },
        
        // AI & ETHICS
        'ai_transparency': {
            best: 'Implementa notifica chiara e visibile quando utenti interagiscono con IA (banner, disclaimer, info page)',
            good: ['disclosure chiara', 'sempre visibile'],
            warning: ['Parziale', 'non sempre'],
            critical: ['Nessuna', 'utenti ignari']
        },
        'training_data_quality': {
            best: 'Implementa data quality assessment + bias testing per dati addestramento IA con metodologie standardizzate (Fairlearn, AIF360)',
            good: ['analisi completa', 'bias testing'],
            warning: ['analisi base', 'no bias'],
            critical: ['Nessuna', 'non verificati']
        },
        'human_oversight': {
            best: 'Implementa human-in-the-loop OBBLIGATORIO per decisioni significative prese da IA ad alto rischio - no override facile',
            good: ['obbligatorio', 'sempre presente'],
            warning: ['solo su richiesta', 'opzionale'],
            critical: ['completamente automatizzati', 'nessuna sorveglianza']
        }
    };
    
    const rule = feedbackRules[questionId];
    
    let feedbackClass = 'feedback-neutral';
    let feedbackIcon = 'ℹ️';
    let feedbackText = '';
    let bestPractice = '';
    
    if (rule) {
        bestPractice = rule.best;
        
        // Check critical
        if (rule.critical && rule.critical.some(keyword => value.toLowerCase().includes(keyword.toLowerCase()))) {
            feedbackClass = 'feedback-critical';
            feedbackIcon = '🔴';
            feedbackText = '<strong>CRITICO:</strong> Gap significativo di conformità. Azione immediata richiesta.';
        }
        // Check warning
        else if (rule.warning && rule.warning.some(keyword => value.toLowerCase().includes(keyword.toLowerCase()))) {
            feedbackClass = 'feedback-warning';
            feedbackIcon = '🟡';
            feedbackText = '<strong>ATTENZIONE:</strong> Miglioramento necessario a breve termine.';
        }
        // Check good
        else if (rule.good && rule.good.some(keyword => value.toLowerCase().includes(keyword.toLowerCase()))) {
            feedbackClass = 'feedback-good';
            feedbackIcon = '🟢';
            feedbackText = '<strong>OTTIMO:</strong> Conforme alle best practice!';
            bestPractice = 'Continua a mantenere questo livello di conformità con review periodiche.';
        }
        // Default neutral
        else {
            feedbackClass = 'feedback-neutral';
            feedbackIcon = 'ℹ️';
            feedbackText = '<strong>INFO:</strong> Risposta registrata.';
        }
    } else {
        // Generic feedback for questions without specific rules
        if (value.toLowerCase().includes('no') || value.toLowerCase().includes('nessun') || 
            value.toLowerCase().includes('mai') || value.toLowerCase().includes('assent')) {
            feedbackClass = 'feedback-critical';
            feedbackIcon = '🔴';
            feedbackText = '<strong>CRITICO:</strong> Questa risposta indica una potenziale non conformità.';
            bestPractice = 'Implementare controlli adeguati secondo le normative NIS2/DORA/GDPR/AI Act applicabili.';
        } else if (value.toLowerCase().includes('parzial') || value.toLowerCase().includes('informal') ||
                   value.toLowerCase().includes('alcuni') || value.toLowerCase().includes('limitato')) {
            feedbackClass = 'feedback-warning';
            feedbackIcon = '🟡';
            feedbackText = '<strong>ATTENZIONE:</strong> Implementazione parziale - completare per piena conformità.';
            bestPractice = 'Formalizzare e completare i processi esistenti con documentazione e test periodici.';
        } else if (value.toLowerCase().includes('sì') || value.toLowerCase().includes('completo') ||
                   value.toLowerCase().includes('ottimo') || value.toLowerCase().includes('certificat')) {
            feedbackClass = 'feedback-good';
            feedbackIcon = '🟢';
            feedbackText = '<strong>OTTIMO:</strong> Risposta positiva!';
            bestPractice = 'Mantenere questo livello con audit periodici.';
        }
    }
    
    let html = `<div class="${feedbackClass}">${feedbackIcon} ${feedbackText}`;
    if (bestPractice) {
        html += `<div style="margin-top: 8px; font-size: 0.85rem; opacity: 0.9;">💡 <strong>Best Practice:</strong> ${bestPractice}</div>`;
    }
    html += `</div>`;
    
    feedbackDiv.innerHTML = html;
    feedbackDiv.style.display = 'block';
    
    console.log('Feedback displayed for:', questionId);
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
    csv += `Governance & Legal,${govResult.score},29\n`;
    csv += `Risk & Asset Management,${riskResult.score},19\n`;
    csv += `Supply Chain Security,${scResult.score},22\n`;
    csv += `Incident Response,${irResult.score},18\n`;
    csv += `Technical + Physical Security,${techResult.score},27\n`;
    csv += `AI & Ethics,${aiResult.score},15\n`;
    csv += `TOTAL,${totalScore},130\n`;
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
