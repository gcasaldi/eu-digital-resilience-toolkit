# app.py - EU Digital Resilience Toolkit
# Integrated NIS2/DORA Compliance Assessment
# Privacy-first, actionable, defensible

import streamlit as st
from dataclasses import dataclass
from datetime import datetime
import csv
from io import StringIO

st.set_page_config(
    page_title="EU Digital Resilience Toolkit", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Data Models
# -----------------------------
@dataclass
class AssessmentResult:
    timestamp: str
    sector: str
    scope: str
    governance_score: int
    logging_score: int
    third_party_score: int
    incident_score: int
    total_score: int
    risk_level: str
    findings: list
    recommendations: list
    regulatory_gaps: dict

def calculate_risk_level(score: int) -> str:
    """Risk classification based on total score"""
    if score >= 85:
        return "LOW"
    elif score >= 65:
        return "MEDIUM"
    else:
        return "HIGH"

def generate_text_report(result: AssessmentResult) -> str:
    """Generate professional text report"""
    report = f"""
================================================================================
EU DIGITAL RESILIENCE ASSESSMENT REPORT
================================================================================

Generated: {result.timestamp}
Sector: {result.sector}
Regulatory Scope: {result.scope}

--------------------------------------------------------------------------------
EXECUTIVE SUMMARY
--------------------------------------------------------------------------------

Total Risk Score: {result.total_score}/100
Risk Classification: {result.risk_level}

Domain Breakdown:
  - Governance & Scope:        {result.governance_score}/25
  - Logging & Monitoring:      {result.logging_score}/25
  - ICT Third-Party Risk:      {result.third_party_score}/25
  - Incident & Resilience:     {result.incident_score}/25

--------------------------------------------------------------------------------
REGULATORY GAPS IDENTIFIED
--------------------------------------------------------------------------------
"""
    
    for domain, gaps in result.regulatory_gaps.items():
        if gaps:
            report += f"\n{domain}:\n"
            for gap in gaps:
                report += f"  - {gap}\n"
    
    report += f"""
--------------------------------------------------------------------------------
FINDINGS ({len(result.findings)} items)
--------------------------------------------------------------------------------
"""
    for i, finding in enumerate(result.findings, 1):
        report += f"{i}. {finding}\n"
    
    report += f"""
--------------------------------------------------------------------------------
RECOMMENDATIONS ({len(result.recommendations)} items)
--------------------------------------------------------------------------------
"""
    for i, rec in enumerate(result.recommendations, 1):
        priority = "[HIGH]" if i <= 3 else "[MEDIUM]" if i <= 6 else "[LOW]"
        report += f"{priority} {rec}\n"
    
    report += """
--------------------------------------------------------------------------------
DISCLAIMER
--------------------------------------------------------------------------------
This assessment is a readiness and risk evaluation tool. It does not constitute
legal advice. Organizations should consult legal counsel for compliance strategy.

Tool: EU Digital Resilience Toolkit v1.0
Framework: NIS2 Directive + DORA Regulation (integrated assessment)
================================================================================
"""
    return report

def generate_csv_export(result: AssessmentResult) -> str:
    """Generate CSV export for data analysis"""
    output = StringIO()
    writer = csv.writer(output)
    
    writer.writerow(['Metric', 'Value'])
    writer.writerow(['Timestamp', result.timestamp])
    writer.writerow(['Sector', result.sector])
    writer.writerow(['Regulatory Scope', result.scope])
    writer.writerow(['Total Score', result.total_score])
    writer.writerow(['Risk Level', result.risk_level])
    writer.writerow(['Governance Score', result.governance_score])
    writer.writerow(['Logging Score', result.logging_score])
    writer.writerow(['Third-Party Score', result.third_party_score])
    writer.writerow(['Incident Score', result.incident_score])
    writer.writerow([])
    
    writer.writerow(['Findings'])
    for finding in result.findings:
        writer.writerow([finding])
    writer.writerow([])
    
    writer.writerow(['Recommendations'])
    for rec in result.recommendations:
        writer.writerow([rec])
    
    return output.getvalue()

# -----------------------------
# Assessment Logic
# -----------------------------

def assess_governance(data: dict) -> tuple:
    """Phase 1: Governance & Scope - 25 points"""
    score = 25
    findings = []
    recs = []
    gaps = []
    
    # Sector classification (5 pts)
    if data.get('sector') in ['Unknown', 'Not applicable']:
        score -= 3
        gaps.append("NIS2/DORA: Sector classification unclear")
        recs.append("Determine if organization qualifies as Essential/Important Entity (NIS2) or Financial Entity (DORA)")
    
    # ICT risk framework (10 pts)
    if data.get('risk_framework') != "Yes, documented and tested":
        score -= 8
        findings.append("No mature ICT risk management framework in place")
        gaps.append("NIS2 Art. 21 / DORA Art. 6: ICT risk management framework missing")
        recs.append("Establish documented ICT risk management framework covering identification, protection, detection, response, recovery")
    elif data.get('risk_framework') == "Partially documented":
        score -= 4
        findings.append("ICT risk framework exists but not fully operationalized")
        recs.append("Complete ICT risk framework documentation and conduct annual testing/validation")
    
    # Governance oversight (5 pts)
    if data.get('board_oversight') != "Yes, quarterly reviews":
        score -= 4
        findings.append("Insufficient board-level oversight of ICT and cyber risks")
        gaps.append("NIS2 Art. 20 / DORA Art. 5: Management body accountability")
        recs.append("Establish quarterly board reporting on ICT risks, incidents, and resilience metrics")
    
    # Cloud usage assessment (5 pts)
    cloud_types = data.get('cloud_usage', [])
    if len(cloud_types) >= 2 and data.get('cloud_governance') != "Yes, formalized":
        score -= 3
        findings.append(f"Significant cloud usage ({len(cloud_types)} service types) without formalized governance")
        gaps.append("DORA Art. 28: Cloud service provider governance")
        recs.append("Implement cloud governance framework: inventory, risk assessment, contractual controls, exit strategies")
    
    return score, findings, recs, gaps

def assess_logging(data: dict) -> tuple:
    """Phase 2: Logging & Monitoring - 25 points"""
    score = 25
    findings = []
    recs = []
    gaps = []
    
    # Centralized logging (7 pts)
    if data.get('centralized_logging') != "Yes, SIEM deployed":
        score -= 6
        findings.append("Logs not centralized in SIEM/log management platform")
        gaps.append("NIS2 Art. 21: Log collection and monitoring")
        recs.append("Deploy SIEM solution (Splunk, ELK, Sentinel) for centralized log collection and correlation")
    
    # Log retention (7 pts)
    retention = data.get('log_retention')
    if retention not in ["18-24 months", "24+ months"]:
        score -= 6
        findings.append(f"Log retention ({retention}) below regulatory minimum (18 months)")
        gaps.append("NIS2: 18-month minimum retention for audit logs")
        recs.append("CRITICAL: Extend log retention to minimum 18 months for all security-relevant logs")
    
    # Log integrity (5 pts)
    if data.get('log_integrity') != "Yes, automated verification":
        score -= 4
        findings.append("Log integrity not cryptographically verified")
        gaps.append("NIS2/DORA: Log tamper-evidence for audit purposes")
        recs.append("Implement automated log hashing (SHA-256) with secure hash storage and periodic verification")
    
    # Cloud log integration (3 pts)
    cloud_types = data.get('cloud_usage', [])
    if cloud_types and data.get('cloud_logs_integrated') != "Yes, all sources":
        score -= 3
        findings.append("Cloud platform logs not fully integrated into central monitoring")
        recs.append("Integrate all cloud provider logs (AWS CloudTrail, Azure Monitor, GCP Cloud Logging) into SIEM")
    
    # Real-time monitoring (3 pts)
    if data.get('realtime_monitoring') != "Yes, 24/7 SOC":
        score -= 2
        findings.append("No 24/7 security monitoring capability")
        recs.append("Establish 24/7 SOC or engage managed detection and response (MDR) provider")
    
    return score, findings, recs, gaps

def assess_third_party(data: dict) -> tuple:
    """Phase 3: ICT Third-Party Risk - 25 points"""
    score = 25
    findings = []
    recs = []
    gaps = []
    
    # Critical vendor inventory (6 pts)
    if data.get('vendor_inventory') != "Yes, complete and current":
        score -= 5
        findings.append("ICT third-party inventory incomplete or outdated")
        gaps.append("DORA Art. 28: Register of ICT third-party providers")
        recs.append("Maintain current register of all ICT third-party providers with criticality classification")
    
    # Contractual audit rights (6 pts)
    if data.get('audit_rights') != "Yes, in all critical contracts":
        score -= 5
        findings.append("Right-to-audit clauses missing in critical vendor contracts")
        gaps.append("DORA Art. 30: Contractual audit and access rights")
        recs.append("Negotiate right-to-audit, security testing rights, and access to SOC 2/ISO certifications in all critical contracts")
    
    # Incident notification SLAs (5 pts)
    if data.get('incident_notification_sla') not in ["24 hours", "12 hours"]:
        score -= 4
        findings.append("Vendor incident notification SLAs inadequate or undefined")
        gaps.append("DORA Art. 19: Incident reporting by ICT providers")
        recs.append("Require 24-hour notification for security incidents in all critical vendor contracts")
    
    # Cloud exit strategies (4 pts)
    cloud_types = data.get('cloud_usage', [])
    if cloud_types and data.get('cloud_exit_plan') != "Yes, tested annually":
        score -= 4
        findings.append("Cloud exit/portability strategies not tested")
        gaps.append("DORA Art. 28: Exit strategies for critical cloud providers")
        recs.append("Develop and test annual cloud exit plans: data portability, alternative CSPs, 90-day transition timeline")
    
    # Supply chain risk monitoring (4 pts)
    if data.get('supply_chain_monitoring') != "Yes, continuous assessment":
        score -= 3
        findings.append("No continuous monitoring of third-party security posture")
        recs.append("Deploy third-party risk monitoring platform (BitSight, SecurityScorecard, Prevalent) for continuous assessment")
    
    return score, findings, recs, gaps

def assess_incident(data: dict) -> tuple:
    """Phase 4: Incident & Resilience - 25 points"""
    score = 25
    findings = []
    recs = []
    gaps = []
    
    # Incident response process (7 pts)
    if data.get('incident_process') != "Yes, documented and tested":
        score -= 6
        findings.append("Incident response process not mature")
        gaps.append("NIS2 Art. 23: Incident handling and reporting")
        recs.append("Establish documented incident response plan with quarterly tabletop exercises")
    
    # 24-hour reporting capability (7 pts)
    if data.get('24h_reporting') != "Yes, process established":
        score -= 6
        findings.append("Cannot meet 24-hour initial incident notification requirement")
        gaps.append("NIS2 Art. 23: 24-hour early warning, 72-hour notification deadlines")
        recs.append("CRITICAL: Establish 24/7 incident detection and 24-hour reporting capability to authorities")
    
    # Resilience testing (5 pts)
    if data.get('resilience_testing') not in ["Quarterly", "Bi-annually"]:
        score -= 4
        findings.append("Insufficient resilience and recovery testing frequency")
        gaps.append("DORA Art. 24: ICT resilience testing")
        recs.append("Conduct resilience testing at least bi-annually: disaster recovery, incident response, threat-led penetration testing (TLPT)")
    
    # RTO/RPO defined (3 pts)
    if data.get('rto_rpo_defined') != "Yes, for all critical systems":
        score -= 2
        findings.append("Recovery time/point objectives not defined for all critical systems")
        recs.append("Define and document RTO/RPO for all critical ICT systems and applications")
    
    # Cloud incident integration (3 pts)
    cloud_types = data.get('cloud_usage', [])
    if cloud_types and data.get('cloud_incident_integration') != "Yes":
        score -= 2
        findings.append("Cloud provider incidents not integrated into organizational incident response")
        recs.append("Integrate cloud provider incident notifications into organizational incident management workflow")
    
    return score, findings, recs, gaps

# -----------------------------
# UI Components
# -----------------------------

def show_header():
    st.title("🛡️ EU Digital Resilience Toolkit")
    st.markdown("""
    **Integrated NIS2 & DORA Compliance Assessment**  
    *Privacy-first | Actionable | Audit-ready*
    
    This tool operationalizes EU cyber regulations into an integrated resilience assessment.  
    **Not legal advice** - for readiness evaluation and gap analysis only.
    """)
    st.divider()

def show_progress(current_phase: int):
    phases = [
        "1. Governance & Scope",
        "2. Logging & Monitoring", 
        "3. ICT Third-Party Risk",
        "4. Incident & Resilience",
        "5. Results & Report"
    ]
    
    cols = st.columns(5)
    for i, phase in enumerate(phases):
        with cols[i]:
            if i < current_phase:
                st.success(f"✓ {phase}", icon="✅")
            elif i == current_phase:
                st.info(f"→ {phase}", icon="▶️")
            else:
                st.text(f"  {phase}")

# -----------------------------
# Main Application Flow
# -----------------------------

def main():
    show_header()
    
    # Initialize session state
    if 'phase' not in st.session_state:
        st.session_state.phase = 0
        st.session_state.data = {}
    
    show_progress(st.session_state.phase)
    st.markdown("---")
    
    # Phase 0: Governance & Scope
    if st.session_state.phase == 0:
        st.subheader("Phase 1: Governance & Scope Identification")
        st.caption("Establish regulatory applicability and governance maturity")
        
        col1, col2 = st.columns(2)
        
        with col1:
            sector = st.selectbox(
                "Organization sector",
                ["Financial services", "Energy", "Transport", "Digital infrastructure", 
                 "Healthcare", "Public administration", "Manufacturing", "Other/Mixed"]
            )
            
            scope = st.multiselect(
                "Regulatory scope (select all that apply)",
                ["NIS2 Essential Entity", "NIS2 Important Entity", "DORA Financial Entity", 
                 "Not directly in scope"]
            )
            
            risk_framework = st.select_slider(
                "ICT risk management framework maturity",
                options=["No framework", "Ad-hoc processes", "Partially documented", 
                        "Yes, documented and tested"],
                value="Partially documented"
            )
        
        with col2:
            board_oversight = st.select_slider(
                "Board-level oversight of ICT/cyber risks",
                options=["No oversight", "Annual review", "Bi-annual reviews", "Yes, quarterly reviews"],
                value="Annual review"
            )
            
            cloud_usage = st.multiselect(
                "Cloud services in use",
                ["IaaS (AWS, Azure, GCP)", "SaaS (M365, Salesforce, etc.)", 
                 "PaaS", "Managed security services", "None"]
            )
            
            if cloud_usage and "None" not in cloud_usage:
                cloud_governance = st.selectbox(
                    "Cloud governance framework",
                    ["No specific framework", "Informal processes", "Yes, formalized"]
                )
            else:
                cloud_governance = "N/A"
        
        st.session_state.data.update({
            'sector': sector,
            'scope': ', '.join(scope) if scope else 'Unknown',
            'risk_framework': risk_framework,
            'board_oversight': board_oversight,
            'cloud_usage': [c for c in cloud_usage if c != "None"],
            'cloud_governance': cloud_governance
        })
        
        if st.button("Continue to Logging Assessment →", type="primary", use_container_width=True):
            st.session_state.phase = 1
            st.rerun()
    
    # Phase 1: Logging
    elif st.session_state.phase == 1:
        st.subheader("Phase 2: Logging, Monitoring & Auditability")
        st.caption("Visibility, traceability, and evidence readiness (NIS2 + DORA overlap)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            centralized_logging = st.selectbox(
                "Centralized log collection",
                ["No centralization", "Partial (some sources)", "Yes, SIEM deployed"]
            )
            
            log_retention = st.selectbox(
                "Log retention period",
                ["<6 months", "6-12 months", "12-18 months", "18-24 months", "24+ months"]
            )
            
            log_integrity = st.selectbox(
                "Log integrity verification (hashing, WORM)",
                ["No verification", "Manual spot-checks", "Yes, automated verification"]
            )
        
        with col2:
            if st.session_state.data.get('cloud_usage'):
                cloud_logs_integrated = st.selectbox(
                    "Cloud platform logs integrated into SIEM",
                    ["No", "Partially", "Yes, all sources"]
                )
            else:
                cloud_logs_integrated = "N/A"
            
            realtime_monitoring = st.selectbox(
                "Real-time security monitoring",
                ["No active monitoring", "Business hours only", "Yes, 24/7 SOC"]
            )
        
        st.session_state.data.update({
            'centralized_logging': centralized_logging,
            'log_retention': log_retention,
            'log_integrity': log_integrity,
            'cloud_logs_integrated': cloud_logs_integrated,
            'realtime_monitoring': realtime_monitoring
        })
        
        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("← Back", use_container_width=True):
                st.session_state.phase = 0
                st.rerun()
        with col_b:
            if st.button("Continue to Third-Party Assessment →", type="primary", use_container_width=True):
                st.session_state.phase = 2
                st.rerun()
    
    # Phase 2: Third-Party
    elif st.session_state.phase == 2:
        st.subheader("Phase 3: ICT Third-Party & Supply Chain Risk")
        st.caption("Dependency management and vendor governance (DORA + NIS2 overlap)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            vendor_inventory = st.selectbox(
                "ICT third-party provider inventory",
                ["No inventory", "Informal list", "Yes, complete and current"]
            )
            
            audit_rights = st.selectbox(
                "Contractual audit and access rights",
                ["Not in contracts", "In some contracts", "Yes, in all critical contracts"]
            )
            
            incident_notification_sla = st.selectbox(
                "Vendor incident notification SLA",
                ["No SLA", "72+ hours", "24 hours", "12 hours"]
            )
        
        with col2:
            if st.session_state.data.get('cloud_usage'):
                cloud_exit_plan = st.selectbox(
                    "Cloud exit/portability strategy",
                    ["No exit plan", "Documented but not tested", "Yes, tested annually"]
                )
            else:
                cloud_exit_plan = "N/A"
            
            supply_chain_monitoring = st.selectbox(
                "Continuous third-party risk monitoring",
                ["No monitoring", "Annual assessments", "Yes, continuous assessment"]
            )
        
        st.session_state.data.update({
            'vendor_inventory': vendor_inventory,
            'audit_rights': audit_rights,
            'incident_notification_sla': incident_notification_sla,
            'cloud_exit_plan': cloud_exit_plan,
            'supply_chain_monitoring': supply_chain_monitoring
        })
        
        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("← Back", use_container_width=True):
                st.session_state.phase = 1
                st.rerun()
        with col_b:
            if st.button("Continue to Incident Assessment →", type="primary", use_container_width=True):
                st.session_state.phase = 3
                st.rerun()
    
    # Phase 3: Incident & Resilience
    elif st.session_state.phase == 3:
        st.subheader("Phase 4: Incident Reporting & Operational Resilience")
        st.caption("Preparedness for disruption and crisis response (NIS2 + DORA)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            incident_process = st.selectbox(
                "Incident response process",
                ["No formal process", "Process exists, not tested", "Yes, documented and tested"]
            )
            
            reporting_24h = st.selectbox(
                "Capability to report incidents within 24 hours",
                ["No", "Uncertain", "Yes, process established"]
            )
            
            resilience_testing = st.selectbox(
                "Resilience testing frequency",
                ["Never", "Annually", "Bi-annually", "Quarterly"]
            )
        
        with col2:
            rto_rpo_defined = st.selectbox(
                "RTO/RPO defined for critical systems",
                ["No", "For some systems", "Yes, for all critical systems"]
            )
            
            if st.session_state.data.get('cloud_usage'):
                cloud_incident_integration = st.selectbox(
                    "Cloud provider incidents integrated into IR process",
                    ["No", "Yes"]
                )
            else:
                cloud_incident_integration = "N/A"
        
        st.session_state.data.update({
            'incident_process': incident_process,
            '24h_reporting': reporting_24h,
            'resilience_testing': resilience_testing,
            'rto_rpo_defined': rto_rpo_defined,
            'cloud_incident_integration': cloud_incident_integration
        })
        
        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("← Back", use_container_width=True):
                st.session_state.phase = 2
                st.rerun()
        with col_b:
            if st.button("Generate Assessment Report ✓", type="primary", use_container_width=True):
                st.session_state.phase = 4
                st.rerun()
    
    # Phase 4: Results
    elif st.session_state.phase == 4:
        st.subheader("Assessment Results & Report")
        
        # Run all assessments
        gov_score, gov_findings, gov_recs, gov_gaps = assess_governance(st.session_state.data)
        log_score, log_findings, log_recs, log_gaps = assess_logging(st.session_state.data)
        tp_score, tp_findings, tp_recs, tp_gaps = assess_third_party(st.session_state.data)
        inc_score, inc_findings, inc_recs, inc_gaps = assess_incident(st.session_state.data)
        
        total_score = gov_score + log_score + tp_score + inc_score
        risk_level = calculate_risk_level(total_score)
        
        all_findings = gov_findings + log_findings + tp_findings + inc_findings
        all_recs = gov_recs + log_recs + tp_recs + inc_recs
        all_gaps = {
            'Governance & Scope': gov_gaps,
            'Logging & Monitoring': log_gaps,
            'ICT Third-Party Risk': tp_gaps,
            'Incident & Resilience': inc_gaps
        }
        
        # Create result object
        result = AssessmentResult(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M UTC"),
            sector=st.session_state.data.get('sector', 'Unknown'),
            scope=st.session_state.data.get('scope', 'Unknown'),
            governance_score=gov_score,
            logging_score=log_score,
            third_party_score=tp_score,
            incident_score=inc_score,
            total_score=total_score,
            risk_level=risk_level,
            findings=all_findings,
            recommendations=all_recs,
            regulatory_gaps=all_gaps
        )
        
        # Display results
        st.success(f"✓ Assessment Complete")
        
        # Metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Total Score", f"{total_score}/100")
        with col2:
            color = "🟢" if risk_level == "LOW" else "🟡" if risk_level == "MEDIUM" else "🔴"
            st.metric("Risk Level", f"{color} {risk_level}")
        with col3:
            st.metric("Governance", f"{gov_score}/25")
        with col4:
            st.metric("Logging", f"{log_score}/25")
        with col5:
            st.metric("Third-Party", f"{tp_score}/25")
        
        col6, col7, col8 = st.columns(3)
        with col6:
            st.metric("Incident", f"{inc_score}/25")
        with col7:
            st.metric("Findings", len(all_findings))
        with col8:
            st.metric("Recommendations", len(all_recs))
        
        st.divider()
        
        # Detailed results
        tab1, tab2, tab3 = st.tabs(["📋 Regulatory Gaps", "🔍 Findings", "💡 Recommendations"])
        
        with tab1:
            for domain, gaps in all_gaps.items():
                if gaps:
                    st.markdown(f"**{domain}**")
                    for gap in gaps:
                        st.warning(gap)
        
        with tab2:
            for i, finding in enumerate(all_findings, 1):
                st.markdown(f"{i}. {finding}")
        
        with tab3:
            for i, rec in enumerate(all_recs, 1):
                priority = "🔴 HIGH" if i <= 3 else "🟡 MEDIUM" if i <= 6 else "🟢 LOW"
                st.markdown(f"**{priority}** - {rec}")
        
        st.divider()
        
        # Export options
        st.subheader("📥 Export Report")
        
        col_exp1, col_exp2, col_exp3 = st.columns(3)
        
        with col_exp1:
            text_report = generate_text_report(result)
            st.download_button(
                label="📄 Download Text Report",
                data=text_report,
                file_name=f"eu_resilience_assessment_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        
        with col_exp2:
            csv_report = generate_csv_export(result)
            st.download_button(
                label="📊 Download CSV Data",
                data=csv_report,
                file_name=f"eu_resilience_assessment_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col_exp3:
            if st.button("🔄 Start New Assessment", use_container_width=True):
                st.session_state.phase = 0
                st.session_state.data = {}
                st.rerun()

if __name__ == "__main__":
    main()
