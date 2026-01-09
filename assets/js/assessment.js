// EU Digital Resilience Toolkit - Assessment Logic

// Assessment data storage
let assessmentData = {
    sector: '',
    scope: [],
    risk_framework: '',
    board_oversight: '',
    cloud_usage: [],
    cloud_governance: '',
    centralized_logging: '',
    log_retention: '',
    log_integrity: '',
    cloud_logs_integrated: '',
    realtime_monitoring: '',
    vendor_inventory: '',
    audit_rights: '',
    incident_notification_sla: '',
    cloud_exit_plan: '',
    supply_chain_monitoring: '',
    incident_process: '',
    reporting_24h: '',
    resilience_testing: '',
    rto_rpo_defined: '',
    cloud_incident_integration: ''
};

let currentPhase = 0;
const phases = [
    { id: 0, name: 'Governance & Scope', key: 'governance' },
    { id: 1, name: 'Logging & Monitoring', key: 'logging' },
    { id: 2, name: 'ICT Third-Party Risk', key: 'third_party' },
    { id: 3, name: 'Incident & Resilience', key: 'incident' },
    { id: 4, name: 'Results & Report', key: 'results' }
];

// Assessment Questions
const assessmentQuestions = {
    governance: {
        title: 'Phase 1: Governance & Scope Identification',
        subtitle: 'Establish regulatory applicability and governance maturity',
        questions: [
            {
                id: 'sector',
                label: 'Organization sector',
                type: 'select',
                options: [
                    'Financial services',
                    'Energy',
                    'Transport',
                    'Digital infrastructure',
                    'Healthcare',
                    'Public administration',
                    'Manufacturing',
                    'Other/Mixed'
                ]
            },
            {
                id: 'scope',
                label: 'Regulatory scope (select all that apply)',
                type: 'checkbox',
                options: [
                    'NIS2 Essential Entity',
                    'NIS2 Important Entity',
                    'DORA Financial Entity',
                    'Not directly in scope'
                ]
            },
            {
                id: 'risk_framework',
                label: 'ICT risk management framework maturity',
                type: 'select',
                options: [
                    'No framework',
                    'Ad-hoc processes',
                    'Partially documented',
                    'Yes, documented and tested'
                ]
            },
            {
                id: 'board_oversight',
                label: 'Board-level oversight of ICT/cyber risks',
                type: 'select',
                options: [
                    'No oversight',
                    'Annual review',
                    'Bi-annual reviews',
                    'Yes, quarterly reviews'
                ]
            },
            {
                id: 'cloud_usage',
                label: 'Cloud services in use (select all that apply)',
                type: 'checkbox',
                options: [
                    'IaaS (AWS, Azure, GCP)',
                    'SaaS (M365, Salesforce, etc.)',
                    'PaaS',
                    'Managed security services',
                    'None'
                ]
            },
            {
                id: 'cloud_governance',
                label: 'Cloud governance framework',
                type: 'select',
                options: [
                    'No specific framework',
                    'Informal processes',
                    'Yes, formalized'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('None')
            }
        ]
    },
    logging: {
        title: 'Phase 2: Logging, Monitoring & Auditability',
        subtitle: 'Visibility, traceability, and evidence readiness (NIS2 + DORA overlap)',
        questions: [
            {
                id: 'centralized_logging',
                label: 'Centralized log collection',
                type: 'select',
                options: [
                    'No centralization',
                    'Partial (some sources)',
                    'Yes, SIEM deployed'
                ]
            },
            {
                id: 'log_retention',
                label: 'Log retention period',
                type: 'select',
                options: [
                    '<6 months',
                    '6-12 months',
                    '12-18 months',
                    '18-24 months',
                    '24+ months'
                ]
            },
            {
                id: 'log_integrity',
                label: 'Log integrity verification (hashing, WORM)',
                type: 'select',
                options: [
                    'No verification',
                    'Manual spot-checks',
                    'Yes, automated verification'
                ]
            },
            {
                id: 'cloud_logs_integrated',
                label: 'Cloud platform logs integrated into SIEM',
                type: 'select',
                options: [
                    'No',
                    'Partially',
                    'Yes, all sources'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('None')
            },
            {
                id: 'realtime_monitoring',
                label: 'Real-time security monitoring',
                type: 'select',
                options: [
                    'No active monitoring',
                    'Business hours only',
                    'Yes, 24/7 SOC'
                ]
            }
        ]
    },
    third_party: {
        title: 'Phase 3: ICT Third-Party & Supply Chain Risk',
        subtitle: 'Dependency management and vendor governance (DORA + NIS2 overlap)',
        questions: [
            {
                id: 'vendor_inventory',
                label: 'ICT third-party provider inventory',
                type: 'select',
                options: [
                    'No inventory',
                    'Informal list',
                    'Yes, complete and current'
                ]
            },
            {
                id: 'audit_rights',
                label: 'Contractual audit and access rights',
                type: 'select',
                options: [
                    'Not in contracts',
                    'In some contracts',
                    'Yes, in all critical contracts'
                ]
            },
            {
                id: 'incident_notification_sla',
                label: 'Vendor incident notification SLA',
                type: 'select',
                options: [
                    'No SLA',
                    '72+ hours',
                    '24 hours',
                    '12 hours'
                ]
            },
            {
                id: 'cloud_exit_plan',
                label: 'Cloud exit/portability strategy',
                type: 'select',
                options: [
                    'No exit plan',
                    'Documented but not tested',
                    'Yes, tested annually'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('None')
            },
            {
                id: 'supply_chain_monitoring',
                label: 'Continuous third-party risk monitoring',
                type: 'select',
                options: [
                    'No monitoring',
                    'Annual assessments',
                    'Yes, continuous assessment'
                ]
            }
        ]
    },
    incident: {
        title: 'Phase 4: Incident Reporting & Operational Resilience',
        subtitle: 'Preparedness for disruption and crisis response (NIS2 + DORA)',
        questions: [
            {
                id: 'incident_process',
                label: 'Incident response process',
                type: 'select',
                options: [
                    'No formal process',
                    'Process exists, not tested',
                    'Yes, documented and tested'
                ]
            },
            {
                id: 'reporting_24h',
                label: 'Capability to report incidents within 24 hours',
                type: 'select',
                options: [
                    'No',
                    'Uncertain',
                    'Yes, process established'
                ]
            },
            {
                id: 'resilience_testing',
                label: 'Resilience testing frequency',
                type: 'select',
                options: [
                    'Never',
                    'Annually',
                    'Bi-annually',
                    'Quarterly'
                ]
            },
            {
                id: 'rto_rpo_defined',
                label: 'RTO/RPO defined for critical systems',
                type: 'select',
                options: [
                    'No',
                    'For some systems',
                    'Yes, for all critical systems'
                ]
            },
            {
                id: 'cloud_incident_integration',
                label: 'Cloud provider incidents integrated into IR process',
                type: 'select',
                options: [
                    'No',
                    'Yes'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('None')
            }
        ]
    }
};

// Scoring functions
function assessGovernance(data) {
    let score = 25;
    let findings = [];
    let recs = [];
    let gaps = [];

    // Sector classification (5 pts)
    if (['Unknown', 'Not applicable'].includes(data.sector)) {
        score -= 3;
        gaps.push("NIS2/DORA: Sector classification unclear");
        recs.push("Determine if organization qualifies as Essential/Important Entity (NIS2) or Financial Entity (DORA)");
    }

    // ICT risk framework (10 pts)
    if (data.risk_framework !== "Yes, documented and tested") {
        score -= 8;
        findings.push("No mature ICT risk management framework in place");
        gaps.push("NIS2 Art. 21 / DORA Art. 6: ICT risk management framework missing");
        recs.push("Establish documented ICT risk management framework covering identification, protection, detection, response, recovery");
    } else if (data.risk_framework === "Partially documented") {
        score -= 4;
        findings.push("ICT risk framework exists but not fully operationalized");
        recs.push("Complete ICT risk framework documentation and conduct annual testing/validation");
    }

    // Governance oversight (5 pts)
    if (data.board_oversight !== "Yes, quarterly reviews") {
        score -= 4;
        findings.push("Insufficient board-level oversight of ICT and cyber risks");
        gaps.push("NIS2 Art. 20 / DORA Art. 5: Management body accountability");
        recs.push("Establish quarterly board reporting on ICT risks, incidents, and resilience metrics");
    }

    // Cloud usage assessment (5 pts)
    const cloudTypes = data.cloud_usage || [];
    if (cloudTypes.length >= 2 && data.cloud_governance !== "Yes, formalized") {
        score -= 3;
        findings.push(`Significant cloud usage (${cloudTypes.length} service types) without formalized governance`);
        gaps.push("DORA Art. 28: Cloud service provider governance");
        recs.push("Implement cloud governance framework: inventory, risk assessment, contractual controls, exit strategies");
    }

    return { score, findings, recs, gaps };
}

function assessLogging(data) {
    let score = 25;
    let findings = [];
    let recs = [];
    let gaps = [];

    // Centralized logging (7 pts)
    if (data.centralized_logging !== "Yes, SIEM deployed") {
        score -= 6;
        findings.push("Logs not centralized in SIEM/log management platform");
        gaps.push("NIS2 Art. 21: Log collection and monitoring");
        recs.push("Deploy SIEM solution (Splunk, ELK, Sentinel) for centralized log collection and correlation");
    }

    // Log retention (7 pts)
    const retention = data.log_retention;
    if (!["18-24 months", "24+ months"].includes(retention)) {
        score -= 6;
        findings.push(`Log retention (${retention}) below regulatory minimum (18 months)`);
        gaps.push("NIS2: 18-month minimum retention for audit logs");
        recs.push("CRITICAL: Extend log retention to minimum 18 months for all security-relevant logs");
    }

    // Log integrity (5 pts)
    if (data.log_integrity !== "Yes, automated verification") {
        score -= 4;
        findings.push("Log integrity not cryptographically verified");
        gaps.push("NIS2/DORA: Log tamper-evidence for audit purposes");
        recs.push("Implement automated log hashing (SHA-256) with secure hash storage and periodic verification");
    }

    // Cloud log integration (3 pts)
    const cloudTypes = data.cloud_usage || [];
    if (cloudTypes.length > 0 && data.cloud_logs_integrated !== "Yes, all sources") {
        score -= 3;
        findings.push("Cloud platform logs not fully integrated into central monitoring");
        recs.push("Integrate all cloud provider logs (AWS CloudTrail, Azure Monitor, GCP Cloud Logging) into SIEM");
    }

    // Real-time monitoring (3 pts)
    if (data.realtime_monitoring !== "Yes, 24/7 SOC") {
        score -= 2;
        findings.push("No 24/7 security monitoring capability");
        recs.push("Establish 24/7 SOC or engage managed detection and response (MDR) provider");
    }

    return { score, findings, recs, gaps };
}

function assessThirdParty(data) {
    let score = 25;
    let findings = [];
    let recs = [];
    let gaps = [];

    // Critical vendor inventory (6 pts)
    if (data.vendor_inventory !== "Yes, complete and current") {
        score -= 5;
        findings.push("ICT third-party inventory incomplete or outdated");
        gaps.push("DORA Art. 28: Register of ICT third-party providers");
        recs.push("Maintain current register of all ICT third-party providers with criticality classification");
    }

    // Contractual audit rights (6 pts)
    if (data.audit_rights !== "Yes, in all critical contracts") {
        score -= 5;
        findings.push("Right-to-audit clauses missing in critical vendor contracts");
        gaps.push("DORA Art. 30: Contractual audit and access rights");
        recs.push("Negotiate right-to-audit, security testing rights, and access to SOC 2/ISO certifications in all critical contracts");
    }

    // Incident notification SLAs (5 pts)
    if (!["24 hours", "12 hours"].includes(data.incident_notification_sla)) {
        score -= 4;
        findings.push("Vendor incident notification SLAs inadequate or undefined");
        gaps.push("DORA Art. 19: Incident reporting by ICT providers");
        recs.push("Require 24-hour notification for security incidents in all critical vendor contracts");
    }

    // Cloud exit strategies (4 pts)
    const cloudTypes = data.cloud_usage || [];
    if (cloudTypes.length > 0 && data.cloud_exit_plan !== "Yes, tested annually") {
        score -= 4;
        findings.push("Cloud exit/portability strategies not tested");
        gaps.push("DORA Art. 28: Exit strategies for critical cloud providers");
        recs.push("Develop and test annual cloud exit plans: data portability, alternative CSPs, 90-day transition timeline");
    }

    // Supply chain risk monitoring (4 pts)
    if (data.supply_chain_monitoring !== "Yes, continuous assessment") {
        score -= 3;
        findings.push("No continuous monitoring of third-party security posture");
        recs.push("Deploy third-party risk monitoring platform (BitSight, SecurityScorecard, Prevalent) for continuous assessment");
    }

    return { score, findings, recs, gaps };
}

function assessIncident(data) {
    let score = 25;
    let findings = [];
    let recs = [];
    let gaps = [];

    // Incident response process (7 pts)
    if (data.incident_process !== "Yes, documented and tested") {
        score -= 6;
        findings.push("Incident response process not mature");
        gaps.push("NIS2 Art. 23: Incident handling and reporting");
        recs.push("Establish documented incident response plan with quarterly tabletop exercises");
    }

    // 24-hour reporting capability (7 pts)
    if (data.reporting_24h !== "Yes, process established") {
        score -= 6;
        findings.push("Cannot meet 24-hour initial incident notification requirement");
        gaps.push("NIS2 Art. 23: 24-hour early warning, 72-hour notification deadlines");
        recs.push("CRITICAL: Establish 24/7 incident detection and 24-hour reporting capability to authorities");
    }

    // Resilience testing (5 pts)
    if (!["Quarterly", "Bi-annually"].includes(data.resilience_testing)) {
        score -= 4;
        findings.push("Insufficient resilience and recovery testing frequency");
        gaps.push("DORA Art. 24: ICT resilience testing");
        recs.push("Conduct resilience testing at least bi-annually: disaster recovery, incident response, threat-led penetration testing (TLPT)");
    }

    // RTO/RPO defined (3 pts)
    if (data.rto_rpo_defined !== "Yes, for all critical systems") {
        score -= 2;
        findings.push("Recovery time/point objectives not defined for all critical systems");
        recs.push("Define and document RTO/RPO for all critical ICT systems and applications");
    }

    // Cloud incident integration (3 pts)
    const cloudTypes = data.cloud_usage || [];
    if (cloudTypes.length > 0 && data.cloud_incident_integration !== "Yes") {
        score -= 2;
        findings.push("Cloud provider incidents not integrated into organizational incident response");
        recs.push("Integrate cloud provider incident notifications into organizational incident management workflow");
    }

    return { score, findings, recs, gaps };
}

function calculateRiskLevel(score) {
    if (score >= 85) return "LOW";
    if (score >= 65) return "MEDIUM";
    return "HIGH";
}

// Export to window for access from main.js
window.assessmentEngine = {
    assessmentData,
    currentPhase,
    phases,
    assessmentQuestions,
    assessGovernance,
    assessLogging,
    assessThirdParty,
    assessIncident,
    calculateRiskLevel
};
