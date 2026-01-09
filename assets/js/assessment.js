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
        subtitle: 'NIS2 Art. 20-21 / DORA Art. 5-6 - Establish regulatory applicability and governance maturity',
        questions: [
            {
                id: 'sector',
                label: 'Organization sector (NIS2 Annex I & II / DORA Art. 2)',
                type: 'select',
                options: [
                    'Financial services (Banking, Insurance, Investment)',
                    'Energy (Electricity, Oil, Gas, Hydrogen)',
                    'Transport (Air, Rail, Water, Road)',
                    'Digital infrastructure (DNS, TLD, Cloud, Data centers)',
                    'Healthcare (Hospitals, Medical devices, Pharmaceuticals)',
                    'Public administration (Central, Regional government)',
                    'Water supply and wastewater',
                    'Digital providers (Online marketplaces, Search engines, Social networks)',
                    'Space sector',
                    'Manufacturing (Critical products)',
                    'Postal and courier services',
                    'Waste management',
                    'Chemicals production',
                    'Food production and distribution',
                    'Research organizations',
                    'Other/Not listed'
                ]
            },
            {
                id: 'scope',
                label: 'Regulatory scope - Does your organization qualify as: (select all that apply)',
                type: 'checkbox',
                options: [
                    'NIS2 Essential Entity (>250 employees OR >€50M turnover in critical sector)',
                    'NIS2 Important Entity (>50 employees OR >€10M turnover in important sector)',
                    'DORA Financial Entity (Credit institution, Payment institution, E-money institution)',
                    'DORA ICT Third-Party Service Provider to financial entities',
                    'Critical ICT Third-Party Service Provider (designated by authorities)',
                    'Not directly in scope (but considering voluntary compliance)'
                ]
            },
            {
                id: 'risk_framework',
                label: 'ICT risk management framework maturity (NIS2 Art. 21 / DORA Art. 6)',
                type: 'select',
                options: [
                    'No formal ICT risk management framework in place',
                    'Basic ad-hoc ICT risk assessments performed irregularly',
                    'ICT risk framework documented but not regularly tested or updated',
                    'Comprehensive framework with ISO 27001, NIST CSF, or equivalent',
                    'Advanced framework with continuous monitoring, annual testing, and board approval'
                ]
            },
            {
                id: 'board_oversight',
                label: 'Management body accountability and oversight (NIS2 Art. 20 / DORA Art. 5)',
                type: 'select',
                options: [
                    'No formal board/management oversight of ICT risks',
                    'Ad-hoc reporting to management when incidents occur',
                    'Annual board review of ICT and cybersecurity risks',
                    'Quarterly board reports on ICT risks, incidents, and metrics',
                    'Monthly oversight with dedicated board cyber committee and training'
                ]
            },
            {
                id: 'critical_functions',
                label: 'Critical or important functions identification (DORA Art. 6.1)',
                type: 'select',
                options: [
                    'Critical functions not formally identified',
                    'Partial identification of critical business processes',
                    'Comprehensive mapping of critical and important functions',
                    'Full mapping with supporting ICT assets and dependencies documented'
                ]
            },
            {
                id: 'cloud_usage',
                label: 'Cloud and outsourced ICT services in use (NIS2 Art. 21.2(d) / DORA Art. 28)',
                type: 'checkbox',
                options: [
                    'Public cloud IaaS (AWS, Azure, GCP, Oracle Cloud)',
                    'SaaS applications (M365, Google Workspace, Salesforce, ServiceNow)',
                    'Platform services - PaaS (databases, analytics, AI/ML)',
                    'Managed security services (SOC, SIEM, EDR, threat intel)',
                    'Payment processing and financial transaction services',
                    'Cloud-based backup and disaster recovery',
                    'Third-party hosting or colocation services',
                    'No cloud or outsourced ICT services'
                ]
            },
            {
                id: 'cloud_governance',
                label: 'ICT third-party risk management framework (DORA Art. 28-30)',
                type: 'select',
                options: [
                    'No formal third-party risk management process',
                    'Basic vendor assessment at contract signature only',
                    'Annual vendor risk reviews with basic security questionnaires',
                    'Comprehensive program: due diligence, contracts, monitoring, exit plans',
                    'Advanced program with continuous monitoring, audits, and concentration risk management'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('No cloud or outsourced ICT services')
            },
            {
                id: 'security_awareness',
                label: 'Cybersecurity awareness and training program (NIS2 Art. 21.2(f))',
                type: 'select',
                options: [
                    'No formal security awareness training',
                    'Annual basic security awareness for all employees',
                    'Regular training with phishing simulations and role-based modules',
                    'Comprehensive program with quarterly training, testing, and board-level cyber literacy'
                ]
            }
        ]
    },
    logging: {
        title: 'Phase 2: Logging, Monitoring & Detection',
        subtitle: 'NIS2 Art. 21.2(b)(c) / DORA Art. 17 - Event detection, logging, and security monitoring',
        questions: [
            {
                id: 'centralized_logging',
                label: 'Centralized security event logging (NIS2 Art. 21 / DORA Art. 17)',
                type: 'select',
                options: [
                    'No centralized logging - logs remain on individual systems',
                    'Basic log aggregation for some critical systems only',
                    'Centralized log management platform (SIEM) deployed for most systems',
                    'Enterprise SIEM with correlation, alerting, and retention (Splunk, QRadar, Sentinel, Chronicle)'
                ]
            },
            {
                id: 'log_retention',
                label: 'Security log retention period (NIS2: minimum 18 months)',
                type: 'select',
                options: [
                    'Less than 6 months',
                    '6-12 months',
                    '12-18 months (borderline compliance)',
                    '18-24 months (NIS2 compliant)',
                    '24+ months (exceeds requirements)'
                ]
            },
            {
                id: 'log_coverage',
                label: 'Log sources covered (NIS2 Art. 21 / DORA Art. 17)',
                type: 'checkbox',
                options: [
                    'Network devices (firewalls, routers, switches, IDS/IPS)',
                    'Endpoint security (antivirus, EDR, host-based firewalls)',
                    'Authentication systems (Active Directory, SSO, MFA)',
                    'Critical applications and databases',
                    'Cloud infrastructure and services (AWS, Azure, GCP)',
                    'Email and collaboration platforms',
                    'Physical access control systems',
                    'Privileged access management (PAM) systems'
                ]
            },
            {
                id: 'log_integrity',
                label: 'Log integrity and tamper-evidence (DORA Art. 17.4)',
                type: 'select',
                options: [
                    'No log integrity verification mechanisms',
                    'Manual periodic reviews and spot-checks',
                    'Automated hashing (SHA-256) with periodic verification',
                    'WORM storage or write-once logging with cryptographic signatures',
                    'Blockchain-based or immutable log storage with real-time verification'
                ]
            },
            {
                id: 'cloud_logs_integrated',
                label: 'Cloud provider logs integrated (AWS CloudTrail, Azure Monitor, GCP Cloud Logging)',
                type: 'select',
                options: [
                    'Cloud logs not collected or monitored',
                    'Basic cloud logs collected but not integrated with SIEM',
                    'Cloud logs partially integrated (some services)',
                    'All cloud provider logs fully integrated into central SIEM'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('No cloud or outsourced ICT services')
            },
            {
                id: 'realtime_monitoring',
                label: 'Continuous security monitoring and SOC operations (NIS2 Art. 21.2(c))',
                type: 'select',
                options: [
                    'No active security monitoring',
                    'Business hours only (8x5) monitoring',
                    'Extended hours monitoring (12x5 or 16x5)',
                    '24/7 internal SOC with on-call escalation',
                    '24/7 SOC (internal or outsourced MDR) with threat hunting'
                ]
            },
            {
                id: 'threat_detection',
                label: 'Threat detection and correlation capabilities',
                type: 'select',
                options: [
                    'No automated threat detection',
                    'Basic signature-based detection (antivirus, IDS)',
                    'SIEM correlation rules and use cases implemented',
                    'Advanced detection with UEBA, ML-based anomaly detection',
                    'Threat intelligence integration and automated response (SOAR)'
                ]
            },
            {
                id: 'vulnerability_scanning',
                label: 'Vulnerability management and scanning (NIS2 Art. 21.2(a))',
                type: 'select',
                options: [
                    'No regular vulnerability scanning',
                    'Annual or ad-hoc vulnerability assessments',
                    'Quarterly vulnerability scans of external assets',
                    'Monthly internal and external vulnerability scans',
                    'Continuous vulnerability scanning with automated remediation tracking'
                ]
            }
        ]
    },
    third_party: {
        title: 'Phase 3: ICT Third-Party Risk Management',
        subtitle: 'DORA Art. 28-30 / NIS2 Art. 21.2(d) - Supply chain security and vendor governance',
        questions: [
            {
                id: 'vendor_inventory',
                label: 'Register of ICT third-party providers (DORA Art. 28.1)',
                type: 'select',
                options: [
                    'No formal inventory of ICT service providers',
                    'Informal list maintained in spreadsheets',
                    'Documented inventory but not regularly updated',
                    'Comprehensive register with criticality classification',
                    'Full register with contracts, SLAs, dependencies, and concentration risk analysis'
                ]
            },
            {
                id: 'vendor_due_diligence',
                label: 'Pre-contractual due diligence process (DORA Art. 28.3)',
                type: 'select',
                options: [
                    'No formal due diligence before engaging vendors',
                    'Basic financial and legal checks only',
                    'Security questionnaires for critical vendors',
                    'Comprehensive assessment: security, financial, operational, reputational',
                    'Advanced due diligence with on-site audits, certifications review (SOC 2, ISO 27001), and residual risk acceptance'
                ]
            },
            {
                id: 'audit_rights',
                label: 'Contractual audit and access rights (DORA Art. 30.2(g))',
                type: 'select',
                options: [
                    'No audit rights in ICT service contracts',
                    'Generic audit clauses without specifics',
                    'Audit rights in some critical contracts',
                    'Full audit rights (on-site, documentation, systems) in all critical contracts',
                    'Comprehensive rights: audits, pentesting, access to SOC reports, subcontractor oversight'
                ]
            },
            {
                id: 'incident_notification_sla',
                label: 'Vendor incident notification requirements (DORA Art. 19 / NIS2 Art. 23)',
                type: 'select',
                options: [
                    'No incident notification requirements in contracts',
                    'Generic incident reporting clause without SLA',
                    'Incident notification within 72 hours',
                    'Notification within 24 hours for security incidents',
                    'Immediate notification (2-4 hours) with detailed root cause analysis required'
                ]
            },
            {
                id: 'data_location',
                label: 'Data localization and cross-border requirements (DORA Art. 28.6)',
                type: 'select',
                options: [
                    'No requirements on data location',
                    'Aware of data locations but no contractual controls',
                    'Contractual requirements for EU/EEA data storage',
                    'EU data residency enforced with regular verification',
                    'Full control: EU residency, no foreign access, encryption key management'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('No cloud or outsourced ICT services')
            },
            {
                id: 'cloud_exit_plan',
                label: 'Exit strategies and data portability (DORA Art. 28.8)',
                type: 'select',
                options: [
                    'No exit strategy or transition planning',
                    'Basic exit plan documented but never tested',
                    'Exit strategy documented with annual review',
                    'Tested exit plans with alternative providers identified',
                    'Comprehensive strategy: tested annually, backup providers, 90-day transition capability'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('No cloud or outsourced ICT services')
            },
            {
                id: 'subcontractor_oversight',
                label: 'Subcontracting and fourth-party risk (DORA Art. 30.3)',
                type: 'select',
                options: [
                    'No visibility into vendor subcontractors',
                    'Awareness of major subcontractors but no oversight',
                    'Contractual notification requirements for subcontractors',
                    'Approval rights for critical subcontractors',
                    'Full oversight: approval, audits, direct contracts, concentration limits'
                ]
            },
            {
                id: 'supply_chain_monitoring',
                label: 'Continuous third-party risk monitoring (DORA Art. 28.10)',
                type: 'select',
                options: [
                    'No ongoing monitoring of vendor risk',
                    'Ad-hoc reviews when issues arise',
                    'Annual vendor risk assessments',
                    'Quarterly reviews with security ratings (BitSight, SecurityScorecard)',
                    'Continuous monitoring: threat intel, breach notifications, financial health, compliance status'
                ]
            },
            {
                id: 'concentration_risk',
                label: 'ICT concentration risk management (DORA Art. 28.9)',
                type: 'select',
                options: [
                    'No assessment of vendor concentration risk',
                    'Aware of major vendors but no formal analysis',
                    'Documented analysis of critical vendor dependencies',
                    'Active concentration risk mitigation with multi-vendor strategy',
                    'Comprehensive program: limits, diversification, alternative providers, scenario testing'
                ]
            }
        ]
    },
    incident: {
        title: 'Phase 4: Incident Management & Operational Resilience',
        subtitle: 'NIS2 Art. 23 / DORA Art. 17-19 - Incident response, reporting, and business continuity',
        questions: [
            {
                id: 'incident_process',
                label: 'Incident response plan and procedures (NIS2 Art. 23 / DORA Art. 17)',
                type: 'select',
                options: [
                    'No formal incident response process',
                    'Basic process documented but not tested',
                    'Documented IR plan with defined roles and escalation',
                    'Comprehensive IR plan tested annually with tabletop exercises',
                    'Advanced IR capability: tested quarterly, automated playbooks, retainer agreements'
                ]
            },
            {
                id: 'incident_classification',
                label: 'Incident classification and severity criteria (NIS2 Art. 23.3)',
                type: 'select',
                options: [
                    'No formal incident classification system',
                    'Basic severity levels (high/medium/low)',
                    'Defined criteria for significant incidents (availability, confidentiality, integrity impact)',
                    'Comprehensive taxonomy aligned with NIS2/DORA thresholds',
                    'Advanced system with automated classification and regulatory notification triggers'
                ]
            },
            {
                id: 'reporting_24h',
                label: '24-hour early warning capability (NIS2 Art. 23.4)',
                type: 'select',
                options: [
                    'Unable to detect and report incidents within 24 hours',
                    'Limited capability, depends on business hours',
                    '24/7 detection but manual reporting process',
                    'Established 24-hour notification process to CSIRT/authorities',
                    'Automated detection and reporting within 24 hours with detailed initial assessment'
                ]
            },
            {
                id: 'notification_authorities',
                label: 'Incident notification to authorities (NIS2: 24h early, 72h notification, final report)',
                type: 'select',
                options: [
                    'No process for regulatory incident notification',
                    'Aware of requirements but process not documented',
                    'Documented process for 72-hour notification',
                    'Full process: 24h early warning, 72h detailed, final report with root cause',
                    'Tested notification process with CSIRT, pre-established communication channels'
                ]
            },
            {
                id: 'resilience_testing',
                label: 'ICT resilience testing frequency (DORA Art. 24 / NIS2 Art. 21.2(h))',
                type: 'select',
                options: [
                    'No resilience or DR testing performed',
                    'Ad-hoc testing when time permits',
                    'Annual disaster recovery tests',
                    'Bi-annual comprehensive resilience testing',
                    'Quarterly testing including TLPT (Threat-Led Penetration Testing) for critical entities'
                ]
            },
            {
                id: 'bcp_documentation',
                label: 'Business continuity plans (BCP) and crisis management (NIS2 Art. 21.3)',
                type: 'select',
                options: [
                    'No business continuity or crisis management plans',
                    'Basic BCP documented but outdated',
                    'BCP and crisis management plans documented and reviewed annually',
                    'Comprehensive plans tested annually with defined RPO/RTO',
                    'Advanced BCM program with quarterly tests, alternate sites, and supply chain continuity'
                ]
            },
            {
                id: 'rto_rpo_defined',
                label: 'Recovery objectives (RTO/RPO) for critical systems (DORA Art. 11)',
                type: 'select',
                options: [
                    'No RTO/RPO defined',
                    'Informal recovery expectations',
                    'RTO/RPO defined for some critical systems',
                    'Comprehensive RTO/RPO for all critical functions',
                    'Granular RTO/RPO with automated monitoring and tested recovery procedures'
                ]
            },
            {
                id: 'backup_strategy',
                label: 'Backup and recovery strategy (DORA Art. 12 / NIS2 Art. 21.2(e))',
                type: 'select',
                options: [
                    'No systematic backup strategy',
                    'Basic backups but not regularly tested',
                    'Regular backups with annual restore testing',
                    'Comprehensive strategy: daily backups, quarterly restore tests, offsite storage',
                    'Advanced: continuous replication, immutable backups, automated recovery, tested monthly'
                ]
            },
            {
                id: 'patch_management',
                label: 'Patch and vulnerability management (NIS2 Art. 21.2(a))',
                type: 'select',
                options: [
                    'No formal patch management process',
                    'Ad-hoc patching when reminded',
                    'Monthly patching cycle for critical systems',
                    'Systematic process: critical patches within 30 days, testing, exceptions tracked',
                    'Advanced: emergency patches <7 days, automated deployment, zero-day response plan'
                ]
            },
            {
                id: 'cloud_incident_integration',
                label: 'Cloud provider incident integration (DORA Art. 19)',
                type: 'select',
                options: [
                    'No integration of cloud provider incidents',
                    'Aware of cloud provider status pages',
                    'Cloud incidents manually tracked',
                    'Automated alerts from cloud providers integrated into IR process',
                    'Full integration: automated tickets, impact assessment, customer notification'
                ],
                conditional: () => assessmentData.cloud_usage && assessmentData.cloud_usage.length > 0 && !assessmentData.cloud_usage.includes('No cloud or outsourced ICT services')
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
