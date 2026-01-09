# app.py - EU Digital Resilience Toolkit
# Homepage and Overview
# Privacy-first, actionable, defensible

import streamlit as st

st.set_page_config(
    page_title="EU Digital Resilience Toolkit", 
    page_icon="🛡️", 
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------
# Homepage
# -----------------------------

def main():
    st.title("🛡️ EU Digital Resilience Toolkit")
    st.markdown("""
    ### Integrated NIS2 & DORA Compliance Assessment
    *Privacy-first | Actionable | Audit-ready*
    """)
    
    st.divider()
    
    # Introduction
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        #### About This Toolkit
        
        The **EU Digital Resilience Toolkit** is a comprehensive assessment framework designed to help 
        organizations evaluate their compliance posture against two critical EU regulations:
        
        - **NIS2 Directive** (Network and Information Security)
        - **DORA Regulation** (Digital Operational Resilience Act)
        
        This tool operationalizes EU cyber regulations into an integrated resilience assessment that is:
        
        - ✅ **Privacy-First**: All data stays in your browser, no data is collected or stored
        - ✅ **Actionable**: Get specific, prioritized recommendations
        - ✅ **Audit-Ready**: Generate professional reports for compliance documentation
        - ✅ **Comprehensive**: Covers 4 critical domains with 100-point scoring
        
        ⚠️ **Important**: This assessment is a readiness and risk evaluation tool. It does not constitute 
        legal advice. Organizations should consult legal counsel for compliance strategy.
        """)
    
    with col2:
        st.info("""
        **Quick Start**
        
        1. Navigate to **Risk Assessment** in the sidebar
        2. Complete the 4-phase evaluation
        3. Review your results and gaps
        4. Export your report
        
        **Time Required**: ~5-10 minutes
        """)
    
    st.divider()
    
    # Features
    st.markdown("### 🎯 Assessment Domains")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        #### 1️⃣ Governance
        - Sector classification
        - ICT risk framework
        - Board oversight
        - Cloud governance
        
        **Max Score**: 25 pts
        """)
    
    with col2:
        st.markdown("""
        #### 2️⃣ Logging
        - Centralized collection
        - Retention policies
        - Log integrity
        - Real-time monitoring
        
        **Max Score**: 25 pts
        """)
    
    with col3:
        st.markdown("""
        #### 3️⃣ Third-Party
        - Vendor inventory
        - Audit rights
        - SLA management
        - Supply chain monitoring
        
        **Max Score**: 25 pts
        """)
    
    with col4:
        st.markdown("""
        #### 4️⃣ Incident Response
        - Response processes
        - Reporting capability
        - Resilience testing
        - RTO/RPO definition
        
        **Max Score**: 25 pts
        """)
    
    st.divider()
    
    # Risk Scoring
    st.markdown("### 📊 Risk Classification")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **🟢 LOW RISK**
        
        **Score**: 85-100 points
        
        Strong compliance posture with minimal gaps. Organization demonstrates mature 
        security controls and governance processes.
        """)
    
    with col2:
        st.warning("""
        **🟡 MEDIUM RISK**
        
        **Score**: 65-84 points
        
        Moderate compliance gaps that require attention. Some controls in place but 
        improvements needed to meet regulatory requirements.
        """)
    
    with col3:
        st.error("""
        **🔴 HIGH RISK**
        
        **Score**: 0-64 points
        
        Significant compliance gaps requiring immediate action. Critical controls 
        missing or inadequate to meet EU regulatory standards.
        """)
    
    st.divider()
    
    # Use Cases
    st.markdown("### 💼 Common Use Cases")
    
    use_cases = [
        {
            "title": "Pre-Audit Preparation",
            "description": "Financial institutions preparing for NIS2/DORA compliance audits",
            "icon": "🏦"
        },
        {
            "title": "Vendor Risk Assessment",
            "description": "Evaluate third-party providers' security and compliance posture",
            "icon": "🤝"
        },
        {
            "title": "Board Reporting",
            "description": "Executive summaries for board-level cyber risk discussions",
            "icon": "📊"
        },
        {
            "title": "Compliance Consulting",
            "description": "Quick client assessments for scoping and proposal development",
            "icon": "💼"
        },
        {
            "title": "Continuous Improvement",
            "description": "Quarterly tracking of security posture improvements",
            "icon": "📈"
        },
        {
            "title": "Gap Analysis",
            "description": "Identify specific regulatory gaps and prioritize remediation",
            "icon": "🔍"
        }
    ]
    
    cols = st.columns(3)
    for i, use_case in enumerate(use_cases):
        with cols[i % 3]:
            st.markdown(f"""
            **{use_case['icon']} {use_case['title']}**
            
            {use_case['description']}
            """)
    
    st.divider()
    
    # CTA
    st.markdown("### 🚀 Ready to Start?")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.info("""
        Navigate to **🔍 Risk Assessment** in the sidebar to begin your comprehensive 
        NIS2/DORA compliance evaluation.
        
        The assessment takes approximately 5-10 minutes and will provide you with:
        - Overall risk score (0-100)
        - Domain-specific breakdowns
        - Identified regulatory gaps
        - Prioritized recommendations
        - Downloadable reports (TXT, CSV)
        """)
    
    st.divider()
    
    # Footer
    st.markdown("""
    ---
    
    **EU Digital Resilience Toolkit v1.0**  
    Framework: NIS2 Directive + DORA Regulation (integrated assessment)
    
    📚 [Documentation](README.md) | 🐛 [Report Issues](https://github.com/gcasaldi/eu-digital-resilience-toolkit/issues) | 
    ⭐ [Star on GitHub](https://github.com/gcasaldi/eu-digital-resilience-toolkit)
    """)

if __name__ == "__main__":
    main()

