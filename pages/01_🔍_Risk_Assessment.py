# Risk Assessment Page - EU Digital Resilience Toolkit
# Integrated NIS2/DORA Compliance Assessment

import streamlit as st
from dataclasses import dataclass
from datetime import datetime
import csv
from io import StringIO
from fpdf import FPDF

st.set_page_config(
    page_title="Risk Assessment - EU Digital Resilience Toolkit", 
    page_icon="🔍", 
    layout="wide"
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

# -----------------------------
# Real-Time Feedback System
# -----------------------------

def get_answer_feedback(question_id: str, answer: str) -> dict:
    """
    Fornisce feedback real-time per ogni risposta con:
    - status: 'optimal', 'acceptable', 'needs_improvement', 'critical'
    - message: spiegazione della valutazione
    - advice: cosa fare per migliorare
    - icon: emoji per visualizzazione
    """
    
    feedback_db = {
        # GOVERNANCE & SCOPE
        'risk_framework': {
            'Yes, documented and tested': {
                'status': 'optimal',
                'icon': '✅',
                'message': '🎯 Eccellente! Framework ICT risk maturo e pienamente operativo.',
                'advice': '''**BEST PRACTICE ATTIVA** ✨

✓ Framework documentato e testato annualmente
✓ Conforme NIS2 Art. 21 e DORA Art. 6

**Prossimi passi per mantenere l'eccellenza:**
1. Review annuale del framework (PDCA cycle)
2. Benchmark con ISO/IEC 27005 o NIST CSF 2.0
3. Integra nuove minacce cyber (AI-powered attacks, supply chain)
4. Mantieni aggiornato risk register con scoring CVSS 3.1+
5. Conduci tabletop exercises semestrali

**Riferimenti:** ISO 27001:2022 Annex A.5.7, NIST CSF 2.0 Govern function'''
            },
            'Partially documented': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': '⚡ Framework esistente ma non completamente maturo - Serve completamento.',
                'advice': '''**AZIONE RICHIESTA - Gap da colmare** 📋

⚠️ Framework parziale = rischio di blind spots

**Piano di completamento (60 giorni):**
1. **Settimana 1-2:** Gap analysis vs ISO 27005 o NIST CSF
2. **Settimana 3-4:** Documenta processi mancanti (Risk ID, Assessment, Treatment)
3. **Settimana 5-6:** Definisci risk appetite e tolerance levels
4. **Settimana 7-8:** Test pilota del framework su area critica

**Deliverable richiesti:**
- Risk management policy approvata da Board
- Risk register aggiornato con scoring
- Processo PDCA documentato
- Evidence di test framework

**Strumenti consigliati:** ServiceNow GRC, Archer, RiskLens
**Budget stimato:** €15-30k (consultancy + tool)'''
            },
            'Ad-hoc processes': {
                'status': 'needs_improvement',
                'icon': '🔴',
                'message': '🚨 Gestione ICT risk non strutturata - Gap normativo CRITICO!',
                'advice': '''**PRIORITÀ ALTA - Violazione NIS2/DORA imminente** ⚠️

❌ Processi ad-hoc = non compliance
❌ Risk assessment non ripetibile
❌ No evidenze per audit

**Piano di remediation URGENTE (90 giorni):**

**FASE 1 - Quick wins (giorni 1-30):**
• Nomina Risk Owner con reporting a Board
• Adotta framework standard (ISO 27005 o NIST CSF)
• Inventory asset ICT critici (priorità: Tier 1)
• Quick risk assessment su top 10 asset

**FASE 2 - Formalizzazione (giorni 31-60):**
• Documenta policy ICT risk management
• Crea risk register strutturato
• Definisci processo risk assessment ricorrente
• Implementa risk treatment plan

**FASE 3 - Test e validazione (giorni 61-90):**
• Test framework su scenario reale
• Board review formale
• Training team operativo
• Preparazione evidenze audit

**Investimento richiesto:**
- Consultancy: €30-50k
- GRC Platform: €10-20k/anno
- Training: €5-10k

**Riferimenti normativi:** NIS2 Art. 21, DORA Art. 6, ISO 27001 Clause 6.1'''
            },
            'No framework': {
                'status': 'critical',
                'icon': '🚨',
                'message': '⛔ CRITICO! Assenza TOTALE framework ICT risk - Violazione diretta NIS2 Art. 21 e DORA Art. 6!',
                'advice': '''**EMERGENZA COMPLIANCE - Azione IMMEDIATA richiesta** 🚨

⛔ RISCHIO ALTISSIMO:
• Sanzioni NIS2: fino a €10M o 2% fatturato
• Sanzioni DORA: fino a €10M o 5% fatturato
• Liability management per cyber incidents
• Impossibilità certificazioni (ISO, SOC2)

**PIANO DI EMERGENZA (120 giorni MAX):**

**SETTIMANA 1-2 - Crisis mode:**
✓ Escalation C-level IMMEDIATA
✓ Board meeting straordinario su cyber risk
✓ Engage consultancy specializzata (Big4 o boutique)
✓ Freeze nuovi progetti ICT non critici

**MESE 1 - Foundation:**
1. Nomina CISO o interim risk manager
2. Selezione framework (raccomandato: NIST CSF 2.0 per rapidità)
3. Asset inventory critico (focus su Crown Jewels)
4. Quick threat assessment (top 10 scenari)
5. Risk register iniziale (template NIST)

**MESE 2-3 - Implementation:**
1. Documentazione policy e procedure
2. Risk assessment completo (qualitativo + quantitativo)
3. Risk treatment plan con prioritization
4. Governance structure (RACI, escalation)
5. Tool selection e deployment (GRC platform)

**MESE 4 - Validation:**
1. Test framework su incident simulato
2. Board approval formale
3. Internal audit preparatorio
4. Gap remediation finale

**INVESTIMENTO CRITICO:**
• Consultancy urgente: €50-80k
• GRC platform: €20-40k/anno
• CISO interim: €100-150k/anno
• Training organization: €10-15k
• **TOTALE Anno 1: €180-285k**

**ALTERNATIVE RAPIDE:**
- vCISO as-a-service (€5-10k/mese)
- Framework pre-packaged (ISO 27001 toolkit)
- Managed GRC service

**Riferimenti:** NIS2 Directive Art. 21, DORA Regulation Art. 6, ISO/IEC 27005:2022, NIST CSF 2.0'''
            }
        },
        
        'board_oversight': {
            'Yes, quarterly reviews': {
                'status': 'optimal',
                'icon': '✅',
                'message': '🎯 Ottimo! Supervisione Board allineata a best practice internazionali.',
                'advice': '''**GOVERNANCE EXCELLENCE** 🏆

✓ Board oversight trimestrale attivo
✓ Conforme NIS2 Art. 20 e DORA Art. 5
✓ Accountability chiara su cyber risk

**Best practice per mantenere l'eccellenza:**

**Contenuto Board Report (template):**
📊 **Executive Summary:** Top 3 rischi cyber del trimestre
📈 **KRI/KPI Dashboard:** MTTD, MTTR, vulnerabilità critiche, patching rate
🔍 **Incident Review:** Breach/near-miss del trimestre con RCA
💰 **Budget & Investments:** Cyber spend vs industry benchmark
🎯 **Compliance Status:** NIS2/DORA readiness, audit findings
🚀 **Strategic Initiatives:** Progetti cyber in corso, roadmap

**Training Board raccomandato:**
• Cyber risk basics (annuale)
• Threat landscape update (semestrale)
• Tabletop exercise (annuale)

**Metriche chiave da trackare:**
- % asset critici protetti
- Cyber risk exposure (€ value at risk)
- Third-party risk score
- Incident response readiness

**Riferimenti:** NACD Cyber Risk Oversight Handbook, NIST CSF Govern, ISO 27001:2022 Clause 5.1'''
            },
            'Bi-annual reviews': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': '📅 Oversight presente ma frequenza sotto best practice (raccomandato: trimestrale).',
                'advice': '''**MIGLIORAMENTO CONSIGLIATO** 📈

⚠️ Bi-annual = possibile ritardo decision-making
⚠️ Cyber landscape evolve troppo veloce per 6 mesi

**Piano upgrade a Quarterly (30 giorni):**

**Step 1 - Template Board Report:**
• Crea dashboard standardizzato (max 10 slide)
• KPI predefiniti: MTTD, MTTR, vulnerabilità, patching
• Format: Executive summary + deep dive opzionale

**Step 2 - Processo leggero:**
• Review trimestrale: 30-45 min dedicated time
• Report pre-read (invio 48h prima)
• Focus su: trend, incident, decisioni budget
• No deep-dive tecnico (solo se richiesto)

**Step 3 - Automation:**
• Dashboard auto-generated (GRC tool)
• KPI collection automatizzata
• Template pre-populated

**Quick wins:**
- Q1/Q3: Full review (45 min)
- Q2/Q4: Light update (20 min)

**Contenuto essenziale trimestrale:**
1. Threat landscape update
2. Incident/near-miss review
3. Compliance status
4. Top 3 risks requiring Board decision
5. Budget variance

**Effort stimato:** 4-6 ore/trimestre (CISO + team)
**Beneficio:** Faster decision-making, better risk awareness'''
            },
            'Annual review': {
                'status': 'needs_improvement',
                'icon': '🔴',
                'message': '🚨 Frequenza INSUFFICIENTE - Non conforme NIS2 Art. 20 (richiede "regular" oversight)!',
                'advice': '''**AZIONE CORRETTIVA RICHIESTA** ⚠️

❌ Annual review = gap normativo NIS2/DORA
❌ Cyber risk invisibile al Board 11 mesi/anno
❌ Decisioni strategiche senza cyber input

**PIANO REMEDIATION (60 giorni):**

**FASE 1 - Setup (giorni 1-30):**

**Governance structure:**
1. Designa Board Cyber Champion (Audit Committee Chair)
2. Definisci reporting line: CISO → CEO → Board
3. Slot fisso agenda Board meeting (30 min)
4. Calendar annuale (4 review trimestrali)

**Template Board Report standard:**
1. Executive Summary (1 slide)
   - Cyber posture score (0-100)
   - Top 3 rischi del trimestre
   - Decisioni richieste al Board

2. Risk Dashboard (1 slide)
   - Heat map: likelihood vs impact
   - Trend (vs trimestre precedente)
   - Industry comparison

3. Incident Review (1 slide)
   - Security incidents trimestre
   - Root cause analysis
   - Remediation status

4. Compliance & Audit (1 slide)
   - NIS2/DORA readiness %
   - Audit findings open/closed

5. Investments & ROI (1 slide)
   - Cyber spend vs budget
   - Project status

**FASE 2 - First Quarterly Review (giorni 31-45):**
• Presenta Board report template
• Richiedi approval governance formale
• Conduct training Board su cyber risk basics
• Set KPI/KRI baseline

**FASE 3 - Ritmo operativo (giorni 46-60):**
• Automatizza data collection (GRC tool)
• Pre-meeting brief (48h prima)
• Post-meeting action items tracking

**Contenuti minimi review trimestrale:**
✓ Cyber risk posture score
✓ Incident significativi (>severity 3)
✓ Vulnerabilità critiche (CVSS >9)
✓ Third-party incidents impattanti
✓ Compliance gap critici
✓ Budget variance >10%

**Tools consigliati:**
- GRC platform: ServiceNow, Archer
- Risk quantification: RiskLens, FAIR
- Board portal: Diligent, BoardEffect

**Investimento:**
- GRC tool/dashboard: €10-15k
- Board training: €5-8k

**Riferimenti:** NIS2 Art. 20, DORA Art. 5, ENISA Guidelines'''
            },
            'No oversight': {
                'status': 'critical',
                'icon': '🚨',
                'message': '⛔ CRITICO! Assenza TOTALE di Board accountability - Violazione DIRETTA NIS2 Art. 20 e DORA Art. 5!',
                'advice': '''**EMERGENZA GOVERNANCE - Board personalmente liable** 🚨

⛔ **RISCHIO LEGALE ALTISSIMO:**
• NIS2: Responsabilità PERSONALE membri Board
• DORA: Sanzioni fino a €5M su individui
• Liability civile in caso breach
• Reputational damage
• Impossibilità D&O insurance coverage

**SCENARIO REALE:** In caso di cyber incident con data breach, Board può essere ritenuto responsabile per negligenza nell'oversight ICT risk. Precedenti: Target ($18M settlement), Equifax ($700M).

**AZIONE IMMEDIATA (30 GIORNI):**

**SETTIMANA 1 - Crisis Management:**
☐ Board meeting straordinario URGENTE
☐ Legal counsel su liability exposure
☐ Engage consultancy governance
☐ CEO + CISO (o nominare interim) briefing

**SETTIMANA 2 - Quick Structure:**

**1. Nomina responsabile Board:**
• Designa Cyber Risk Champion nel Board
• Tipicamente: Chair Audit Committee
• Alternativa: create Risk Committee dedicato

**2. Define accountability:**
Board → approva cyber strategy, budget, risk appetite
CEO → accountable per execution
CISO → responsible per cyber program
Business → risk owners per area

**3. Immediate reporting:**
• Monthly report primi 3 mesi (bootstrap)
• Poi trimestrale standard
• Escalation 24h per critical incident

**SETTIMANA 3-4 - Formalizzazione:**

**Board Cyber Charter (documento formale):**
1. Scope responsabilità Board
2. Frequency review (min. trimestrale)
3. Reporting structure
4. Escalation triggers
5. Training requirements
6. Decision rights

**First Board Report urgente:**
1. CURRENT STATE (Red Alert)
   - Inventory asset critici
   - Known vulnerabilities (CVSS >7)
   - Incident history (12 mesi)
   - Compliance gap
   - Liability exposure (€)

2. IMMEDIATE ACTIONS (30 giorni)
   - Quick wins security
   - Incident response plan
   - Cyber insurance review

3. 90-DAY PLAN
   - Governance structure
   - Risk assessment completo
   - Framework ICT risk
   - Tool deployment

4. BUDGET REQUEST
   - Emergency measures
   - Consultancy
   - Tools & technology
   - Headcount (CISO team)

**Training Board OBBLIGATORIO:**
• Cyber Risk Fundamentals: 4 ore (ASAP)
• NIS2/DORA Legal Requirements: 2 ore
• Incident Response Tabletop: 3 ore

**INVESTIMENTO URGENTE:**
- Legal counsel: €15-25k
- Consultancy governance: €30-50k
- Board training: €10-15k
- CISO interim (se mancante): €100-150k/anno
- Quick security assessment: €20-30k
- **TOTALE emergency: €175-270k**

**MILESTONE 30 GIORNI:**
✓ Board Cyber Charter approvato
✓ Responsible Board member nominato
✓ First cyber briefing completato
✓ Emergency action plan in execution
✓ Calendar trimestrale definito
✓ Reporting template agreed

**POST 30 GIORNI - BAU:**
• Quarterly Board review
• Annual strategy review
• Bi-annual training refresh
• Annual tabletop exercise

**Riferimenti:** NIS2 Art. 20, DORA Art. 5, NACD Director Handbook on Cyber Risk Oversight'''
            }
        },
        
        'cloud_governance': {
            'Yes, formalized': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Framework cloud governance formalizzato correttamente.',
                'advice': 'Mantieni inventario aggiornato, rivedi contratti annualmente, monitora compliance SLA.'
            },
            'Informal processes': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'Processi cloud non formalizzati - Rischio governance.',
                'advice': 'AZIONE: Formalizza cloud governance: 1) Inventario completo servizi cloud; 2) Risk assessment per CSP; 3) Policy uso cloud; 4) Clausole contrattuali standard (audit rights, data portability, exit); 5) Monitoring continuo.'
            },
            'No specific framework': {
                'status': 'critical',
                'icon': '🔴',
                'message': 'Cloud usage significativo senza governance - Gap DORA Art. 28!',
                'advice': 'PRIORITÀ ALTA: Implementa cloud governance framework. Include: registro CSP, classificazione criticità, due diligence vendor, exit strategy, concentration risk assessment. Budget: tools + legal review contratti.'
            }
        },
        
        # LOGGING & MONITORING
        'centralized_logging': {
            'Yes, SIEM deployed': {
                'status': 'optimal',
                'icon': '✅',
                'message': '🎯 SIEM operativo - Eccellente capacità di log management e correlation.',
                'advice': '''**LOG MANAGEMENT EXCELLENCE** 🛡️

✓ SIEM centralizzato deployato
✓ Visibility su security events
✓ Conforme NIS2 log requirements

**Ottimizzazione continua:**

**Coverage check (trimestrale):**
📍 Network layer: firewall, IDS/IPS, proxy, VPN
📍 Endpoint: workstations, servers, mobile
📍 Cloud: AWS CloudTrail, Azure Monitor, GCP Logging
📍 Applications: web apps, database, API gateway
📍 Security tools: AV, EDR, email gateway, WAF
📍 Identity: AD/LDAP, SSO, MFA

**Target coverage:** >95% asset critici

**Use cases da monitorare:**
1. Failed authentication (brute force)
2. Privilege escalation
3. Lateral movement
4. Data exfiltration patterns
5. Malware execution
6. Config changes unauthorized
7. Account anomalies
8. External access anomalies

**Alert tuning:**
• Review settimanale false positive rate
• Target: <5% FP, >95% detection rate
• Playbook automated per alert comuni

**Performance metrics:**
- Log ingestion rate: GB/day
- Search query performance: <5 sec
- Alert MTTD: <15 min
- Retention compliance: 18+ mesi

**Tools integration essenziali:**
- SOAR per automation (Cortex, Phantom, Demisto)
- Threat intel feeds (STIX/TAXII)
- Ticketing system (ServiceNow, Jira)

**Riferimenti:** NIST SP 800-92 Log Management, ISO 27001 A.12.4'''
            },
            'Partial (some sources)': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': '⚡ Log collection parziale - Visibilità INCOMPLETA! Blind spots = rischio.',
                'advice': '''**AZIONE PRIORITARIA - Completare integrazione** 🔧

⚠️ Partial logging = partial visibility = HIGH RISK
⚠️ Attacker può sfruttare blind spots
⚠️ Incident investigation incompleta

**PIANO COMPLETAMENTO (45 giorni):**

**FASE 1 - Inventory (giorni 1-10):**
☐ Audit log sources correnti integrate
☐ Gap analysis vs inventory asset totale
☐ Prioritize by criticality (Tier 1 → Tier 3)
☐ Identify log format per source

**FASE 2 - Integration prioritaria (giorni 11-30):**

**Priority 1 (CRITICAL - giorni 11-20):**
✓ Domain Controllers (autenticazione)
✓ Firewall perimeter
✓ Database servers (dati sensibili)
✓ VPN/Remote access
✓ Email gateway
✓ Cloud console (AWS/Azure/GCP)

**Priority 2 (HIGH - giorni 21-30):**
✓ File servers
✓ Web application servers
✓ Endpoint (sample rappresentativo)
✓ Network switches core
✓ Backup systems
✓ Security tools (AV, EDR)

**FASE 3 - Validation (giorni 31-45):**
✓ Test log ingestion per source
✓ Create baseline dashboards
✓ Configure initial detection rules
✓ Document log schema mapping
✓ Setup retention policy

**Technical implementation:**

**Per ogni log source:**
1. Identify log location/API
2. Choose collector type (agent, syslog, API)
3. Configure forwarding
4. Normalize log format (CEF, JSON)
5. Test connectivity
6. Validate parsing
7. Create use cases

**Common integration methods:**
- Syslog forwarder (rsyslog, syslog-ng)
- Agent-based (Splunk UF, Beats, Sentinel agent)
- API polling (REST, webhook)
- Cloud-native integration (EventBridge, Event Hub)

**Target metrics post-integration:**
- Coverage asset critici: >90%
- Log ingestion volume: +30-50%
- Correlation rules: +20-30 nuove
- Detection capability: +40%

**Quick wins immediati:**
1. Cloud platforms (AWS CloudTrail, Azure Monitor)
2. O365/M365 Audit Logs
3. EDR tools (CrowdStrike, SentinelOne)
4. Critical database servers

**Effort stimato:**
- Engineering time: 80-120 ore
- Testing: 20-30 ore
- Documentation: 10-15 ore

**Costi aggiuntivi possibili:**
- Licensing SIEM (volume-based): €5-15k/anno
- Collectors hardware/VM: €2-5k
- Professional services: €10-20k

**Riferimenti:** NIST SP 800-92, CIS Controls v8 (8.2-8.5)'''
            },
            'No centralization': {
                'status': 'critical',
                'icon': '🚨',
                'message': '⛔ CRITICO! Log NON centralizzati - Impossibile audit trail, correlation e investigation!',
                'advice': '''**EMERGENZA LOGGING - Blindness operativa totale** 🚨

⛔ **RISCHIO ESTREMO:**
• Zero visibility su security events
• Incident investigation impossibile
• Audit/compliance fail garantito
• MTTR (Mean Time To Respond): INFINITE
• Violazione diretta NIS2 Art. 21

**REAL-WORLD IMPACT:**
"Senza log centralizzati, breach discovery media: 200+ giorni. Con SIEM: 24-48 ore. Difference = €millions in damage."

**PIANO EMERGENZA (60 GIORNI):**

**SETTIMANA 1-2 - Decision & Setup:**

**1. Platform selection urgente:**

**Option A - Cloud SIEM (fastest):**
✓ Microsoft Sentinel (Azure)
✓ Google Chronicle
✓ Sumo Logic
✓ Pros: Quick deploy, scalable, low capex
✓ Timeline: 2-3 settimane
✓ Cost: €5-20k/mese (pay-as-you-go)

**Option B - Self-hosted:**
✓ Splunk Enterprise
✓ ELK Stack (Elasticsearch-Logstash-Kibana)
✓ IBM QRadar
✓ Pros: Data control, customization
✓ Timeline: 4-6 settimane
✓ Cost: €30-100k license + infrastructure

**Option C - Hybrid:**
✓ Splunk Cloud
✓ Elastic Cloud
✓ Pros: Balance control/speed
✓ Timeline: 3-4 settimane

**RACCOMANDAZIONE URGENTE:** Cloud SIEM (Sentinel o Chronicle) per speed-to-value

**2. Quick deployment plan:**

**Week 1:**
☐ Platform procurement/signup
☐ Sizing: estimate log volume (GB/day)
☐ Network setup (connectivity, bandwidth)
☐ Identify SME/integrator

**Week 2:**
☐ Deploy collectors (agents/forwarders)
☐ Integrate critical sources (DC, firewall, cloud)
☐ Configure baseline ingestion

**SETTIMANA 3-6 - Core Implementation:**

**Priority log sources (deploy in order):**

**Week 3 - Identity & Access:**
1. Active Directory / LDAP
2. VPN / Remote access
3. Cloud IAM (AWS IAM, Azure AD)
4. MFA systems
5. Privileged access management

**Week 4 - Perimeter & Network:**
1. Firewalls
2. IDS/IPS
3. Proxy/Web gateway
4. Email security gateway
5. DNS servers

**Week 5 - Endpoints & Servers:**
1. Critical servers (DB, app, file)
2. Endpoint sample (10-20%)
3. Cloud workloads (EC2, VMs)
4. Containers/K8s (if applicable)

**Week 6 - Applications & Cloud:**
1. Web applications
2. APIs
3. Cloud console activity (CloudTrail, Monitor)
4. SaaS apps (O365, Salesforce)
5. Security tools (EDR, AV)

**SETTIMANA 7-8 - Use Cases & Operationalization:**

**Implement detection use cases:**
1. Failed login brute force (>5 failed/5min)
2. Privilege escalation detection
3. After-hours access anomalies
4. Geo-impossible logins
5. Malware execution (EDR alerts)
6. Data exfiltration patterns (large uploads)
7. Unauthorized config changes
8. Account creation/deletion

**Dashboards essenziali:**
- Executive: security posture overview
- SOC: real-time alerts & incidents
- Compliance: audit log coverage
- Threat hunting: custom queries

**Alerting setup:**
- Critical: immediate notification (SMS/email)
- High: 15-min SLA
- Medium: 1-hour SLA
- Low: daily digest

**DELIVERABLE 60 GIORNI:**
✓ SIEM platform operativo
✓ >70% asset critici integrati
✓ 15-20 use cases attivi
✓ SOC dashboards deployed
✓ Incident response playbook
✓ Retention policy configured (18+ mesi)
✓ Documentation completa

**INVESTIMENTO EMERGENZA:**

**Cloud SIEM (raccomandato):**
- Platform subscription: €10-25k/anno
- Professional services (integrator): €30-50k
- Training team: €5-10k
- **Total Year 1: €45-85k**

**Self-hosted SIEM:**
- Licensing: €50-150k (perpetual o subscription)
- Infrastructure (servers, storage): €20-40k
- Professional services: €50-80k
- Ongoing maintenance: €15-30k/anno
- **Total Year 1: €135-300k**

**Quick Start Option:**
- Managed SIEM service (MSSP): €8-15k/mese
- Include: platform + monitoring + analyst
- Fastest time-to-value (1-2 settimane)

**CRITICAL SUCCESS FACTORS:**
1. Executive sponsorship (budget approval)
2. Dedicated project team (PM + engineers)
3. Integrator/vendor support
4. Phased approach (critical sources first)
5. Training SOC team parallel a deployment

**IMMEDIATE WINS (primi 7 giorni):**
- Cloud platform logs (CloudTrail/Monitor)
- Domain Controller logs
- Firewall logs
- VPN logs
→ Visibility su 60-70% attack surface

**POST GO-LIVE:**
- Monthly: review coverage, expand sources
- Quarterly: tune alerts, add use cases
- Bi-annual: platform health check
- Annual: SOC maturity assessment

**Riferimenti:** NIST SP 800-92, SANS SIEM Implementation Guide, Gartner SIEM Market Guide, NIS2 Directive Art. 21'''
            }
        },
        
        'log_retention': {
            '24+ months': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Retention conforme e oltre requisiti minimi.',
                'advice': 'Ottimo! Verifica storage capacity planning per crescita log volume.'
            },
            '18-24 months': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Retention allineata a requisiti NIS2 (18 mesi minimi).',
                'advice': 'Conforme. Considera estensione a 24 mesi per incident investigation complesse.'
            },
            '12-18 months': {
                'status': 'needs_improvement',
                'icon': '🔴',
                'message': 'Retention sotto requisiti NIS2 - Non conforme!',
                'advice': 'AZIONE IMMEDIATA: Estendi retention a minimo 18 mesi per log security-relevant (authentication, access, changes, alerts). Verifica storage capacity. Timeline: 30 giorni.'
            },
            '6-12 months': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Retention molto sotto requisiti - Violazione compliance.',
                'advice': 'URGENTE: Estendi retention a 18-24 mesi. Valuta: 1) Archive storage (S3 Glacier, Azure Cool); 2) Compression; 3) Tiering strategy. Impatto: audit trail, forensics, investigation.'
            },
            '<6 months': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'GRAVE! Retention inadeguata - Evidenze insufficienti per audit.',
                'advice': 'CRITICO: Implementa retention 18+ mesi IMMEDIATAMENTE. Senza evidenze log adeguate: 1) Audit impossibili; 2) Investigation limitata; 3) Sanzioni normative. Budget storage prioritario.'
            }
        },
        
        'log_integrity': {
            'Yes, automated verification': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Log integrity protetta - Evidenze tamper-proof.',
                'advice': 'Eccellente! Verifica backup hash database e test restore periodici.'
            },
            'Manual spot-checks': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': 'Verifiche manuali - Non scalabile e incomplete.',
                'advice': 'MIGLIORAMENTO: Automatizza log hashing (SHA-256) con storage hash separato. Implementa scheduled verification jobs. Tools: syslog-ng signature, OSSEC integrity checking.'
            },
            'No verification': {
                'status': 'critical',
                'icon': '🔴',
                'message': 'Log non protetti da tampering - Evidenze non affidabili!',
                'advice': 'PRIORITÀ ALTA: Implementa log integrity protection: 1) Cryptographic hashing (SHA-256); 2) WORM storage o blockchain; 3) Automated verification; 4) Secure hash storage. Senza integrity, log non validi in audit/legal proceedings.'
            }
        },
        
        'cloud_logs_integrated': {
            'Yes, all sources': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Cloud logs completamente integrati - Visibilità completa.',
                'advice': 'Ottimo! Verifica alerting su eventi cloud critici (privilege escalation, config changes).'
            },
            'Partially': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'Integrazione cloud logs parziale - Blind spots possibili.',
                'advice': 'AZIONE: Completa integrazione cloud logs nel SIEM. Priorità: AWS CloudTrail, Azure Activity Log, GCP Cloud Logging, M365 Audit Logs. Configura forwarding a SIEM.'
            },
            'No': {
                'status': 'critical',
                'icon': '🔴',
                'message': 'Cloud logs non monitorati - Rischio security significativo!',
                'advice': 'URGENTE: Attiva integrazione cloud logs. Setup: 1) Enable logging (CloudTrail/Monitor/Logging); 2) Configure SIEM forwarders; 3) Create detection rules; 4) Dashboard cloud activity. Cloud è attack surface critica!'
            }
        },
        
        'realtime_monitoring': {
            'Yes, 24/7 SOC': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'SOC 24/7 operativo - Capacità detection ottimale.',
                'advice': 'Eccellente! Verifica MTTD (Mean Time To Detect) e coverage use cases.'
            },
            'Business hours only': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'Monitoring limitato a orario lavorativo - Gap coverage 67%!',
                'advice': 'AZIONE: Estendi monitoring a 24/7. Opzioni: 1) Managed SOC (MDR provider); 2) Follow-the-sun model; 3) Automated playbooks + on-call. Attack avvengono H24, specialmente weekend/notti.'
            },
            'No active monitoring': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Nessun monitoring attivo - Detection impossibile.',
                'advice': 'URGENTE: Attiva security monitoring. Quick wins: 1) Deploy EDR con automated response; 2) Subscribe MDR service; 3) Configure SIEM alerting; 4) Setup on-call rotation. Senza monitoring, breach detection in media 200+ giorni!'
            }
        },
        
        # THIRD-PARTY RISK
        'vendor_inventory': {
            'Yes, complete and current': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Inventario vendor completo e aggiornato.',
                'advice': 'Eccellente! Mantieni update trimestrale e classifica per criticità.'
            },
            'Informal list': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'Inventario non formalizzato - Gap governance.',
                'advice': 'AZIONE: Formalizza registro ICT third-party. Include: ragione sociale, servizi, dati trattati, criticità, certificazioni, contatti, contratto. Template DORA compliant. Update: trimestrale.'
            },
            'No inventory': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Nessun inventario vendor - Violazione DORA Art. 28!',
                'advice': 'URGENTE: Crea registro completo ICT providers. Process: 1) Survey business units; 2) Audit contratti; 3) Classifica criticità; 4) Risk assessment; 5) Remediation plan. Unknown dependencies = unknown risk!'
            }
        },
        
        'audit_rights': {
            'Yes, in all critical contracts': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Audit rights in contratti critici - Conforme DORA.',
                'advice': 'Ottimo! Esercita audit rights periodicamente, richiedi SOC 2 reports.'
            },
            'In some contracts': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'Audit rights non completi - Coverage parziale.',
                'advice': 'AZIONE: Negozia audit rights in tutti contratti critici al rinnovo. Clausole: 1) Right to audit security controls; 2) Accesso SOC 2/ISO reports; 3) Penetration test rights; 4) Incident notification 24h.'
            },
            'Not in contracts': {
                'status': 'critical',
                'icon': '🔴',
                'message': 'Nessun audit right - Impossibile verification security vendor!',
                'advice': 'PRIORITÀ ALTA: Rivedi contratti critici. Richiedi: 1) Annual right to audit; 2) Security questionnaire rights; 3) Incident disclosure 24h; 4) Access to certifications; 5) Subprocessor transparency. Senza audit rights = blind trust.'
            }
        },
        
        'incident_notification_sla': {
            '12 hours': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'SLA notification 12h - Best practice.',
                'advice': 'Eccellente! Verifica vendor rispetti SLA, testa notification flow.'
            },
            '24 hours': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'SLA 24h allineato a requisiti DORA Art. 19.',
                'advice': 'Conforme. Testa notification process annualmente, verifica contatti aggiornati.'
            },
            '72+ hours': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'SLA 72h inadeguato per incident response efficace.',
                'advice': 'AZIONE: Negozia SLA 24h al rinnovo contratti. 72h troppo lento per: 1) Containment; 2) Notification authorities; 3) Customer communication. Richiedi severity-based SLA.'
            },
            'No SLA': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Nessun SLA incident notification - Risk inaccettabile!',
                'advice': 'URGENTE: Definisci SLA incident notification in tutti contratti critici. Minimo: 24h per incident security. Include: 1) Severity definition; 2) Notification channels; 3) Information required; 4) Penalties per breach SLA.'
            }
        },
        
        'cloud_exit_plan': {
            'Yes, tested annually': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Exit strategy cloud testata - Portabilità garantita.',
                'advice': 'Eccellente! Verifica data export format, timeline transition, costi exit.'
            },
            'Documented but not tested': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': 'Exit plan non testato - Eseguibilità incerta.',
                'advice': 'MIGLIORAMENTO: Testa exit plan annualmente. Verifica: 1) Data export completo; 2) Alternative CSP identificati; 3) Timeline 90 giorni max; 4) Costi exit; 5) Continuità business durante transition.'
            },
            'No exit plan': {
                'status': 'critical',
                'icon': '🔴',
                'message': 'Nessuna exit strategy - Lock-in risk e violazione DORA!',
                'advice': 'PRIORITÀ ALTA: Sviluppa cloud exit strategy. Include: 1) Data portability plan; 2) Alternative CSP shortlist; 3) Export procedures; 4) Timeline transition (target 90 giorni); 5) Business continuity durante migration. Lock-in = rischio concentration.'
            }
        },
        
        'supply_chain_monitoring': {
            'Yes, continuous assessment': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Monitoring continuo third-party risk attivo.',
                'advice': 'Ottimo! Verifica coverage vendor critici, configura alerting su security incidents.'
            },
            'Annual assessments': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': 'Assessment annuale - Frequenza sotto best practice.',
                'advice': 'MIGLIORAMENTO: Implementa continuous monitoring. Tools: BitSight, SecurityScorecard, Prevalent. Benefit: real-time risk posture, breach detection, cyber rating changes. Assessment annuale troppo lento.'
            },
            'No monitoring': {
                'status': 'critical',
                'icon': '🔴',
                'message': 'Nessun monitoring vendor - Supply chain blind spot!',
                'advice': 'URGENTE: Attiva third-party risk monitoring. Options: 1) Platform automated (BitSight/SecurityScorecard); 2) Questionnaire periodici; 3) Vulnerability scanning vendor-facing systems; 4) News monitoring breach vendor. Supply chain attack in crescita 40% YoY!'
            }
        },
        
        # INCIDENT & RESILIENCE
        'incident_process': {
            'Yes, documented and tested': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Incident response process maturo e testato.',
                'advice': 'Eccellente! Mantieni playbook aggiornati, conduci tabletop quarterly.'
            },
            'Process exists, not tested': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'IR process non testato - Efficacia non verificata.',
                'advice': 'AZIONE: Testa incident response process trimestralmente. Scenari: 1) Ransomware; 2) Data breach; 3) DDoS; 4) Insider threat; 5) Cloud compromise. Misura MTTR, identifica gaps, aggiorna playbook.'
            },
            'No formal process': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Nessun processo incident response - Caos in caso breach!',
                'advice': 'URGENTE: Crea incident response plan. Include: 1) IR team + roles; 2) Detection & triage; 3) Containment procedures; 4) Eradication & recovery; 5) Communication plan; 6) Authority notification; 7) Post-incident review. Template: NIST SP 800-61. Timeline: 45 giorni.'
            }
        },
        
        '24h_reporting': {
            'Yes, process established': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Capacità reporting 24h attiva - Conforme NIS2.',
                'advice': 'Ottimo! Testa notification flow semestralmente, mantieni contatti authorities aggiornati.'
            },
            'Uncertain': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'Incertezza su capability 24h - Gap processo critico!',
                'advice': 'AZIONE: Formalizza processo reporting 24h. Setup: 1) Identify incident notification authorities (CSIRT, DORA lead authority); 2) Prepare notification templates; 3) Define severity criteria; 4) 24/7 on-call rotation; 5) Test workflow. NIS2 richiede early warning 24h!'
            },
            'No': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Impossibile reporting 24h - Violazione diretta NIS2 Art. 23!',
                'advice': 'URGENTE: Implementa capability reporting 24h. Requirement: 1) 24/7 detection (SOC/MDR); 2) Incident classification process; 3) Notification templates; 4) Escalation paths; 5) Authority contacts; 6) On-call team. Sanzioni NIS2 per late reporting!'
            }
        },
        
        'resilience_testing': {
            'Quarterly': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Testing trimestrale - Best practice resilienza.',
                'advice': 'Eccellente! Varia scenari (DR, ransomware, DDoS), misura RTO/RPO effettivi.'
            },
            'Bi-annually': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Testing semestrale allineato requisiti DORA.',
                'advice': 'Conforme. Include test: DR, incident response, business continuity, security controls.'
            },
            'Annually': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': 'Testing annuale - Frequenza minima accettabile.',
                'advice': 'MIGLIORAMENTO: Aumenta frequenza testing a semestrale. DORA richiede test regolari. Scenari priority: disaster recovery, ransomware response, data breach, third-party failure.'
            },
            'Never': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Nessun resilience testing - RTO/RPO non verificati!',
                'advice': 'URGENTE: Pianifica resilience testing program. Anno 1: 1) Q1: Tabletop DR; 2) Q2: Technical DR test; 3) Q3: Incident response drill; 4) Q4: Full failover test. Misura: RTO actual, RPO, detection time, recovery time. Senza test, recovery plan = fantasia!'
            }
        },
        
        'rto_rpo_defined': {
            'Yes, for all critical systems': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'RTO/RPO definiti per tutti sistemi critici.',
                'advice': 'Ottimo! Verifica RTO/RPO con testing, allinea backup/HA strategy.'
            },
            'For some systems': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': 'RTO/RPO parziali - Coverage incompleta.',
                'advice': 'AZIONE: Completa definizione RTO/RPO per tutti sistemi critici. Process: 1) Business impact analysis; 2) Define acceptable downtime; 3) Define acceptable data loss; 4) Design backup/HA strategy; 5) Document in DR plan.'
            },
            'No': {
                'status': 'critical',
                'icon': '🔴',
                'message': 'RTO/RPO non definiti - Impossibile recovery planning!',
                'advice': 'PRIORITÀ ALTA: Condurre business impact analysis (BIA). Output: 1) Critical systems inventory; 2) RTO target per system; 3) RPO target per system; 4) Dependencies; 5) Recovery priorities. Senza RTO/RPO, backup strategy inefficace e recovery caotica.'
            }
        },
        
        'cloud_incident_integration': {
            'Yes': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Cloud incident integrati in IR process.',
                'advice': 'Ottimo! Verifica notification da CSP, testa escalation workflow.'
            },
            'No': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'Cloud incident non integrati - Gap IR process.',
                'advice': 'AZIONE: Integra cloud incident in IR workflow. Setup: 1) Subscribe CSP incident notifications; 2) Configure alerting (email/webhook); 3) Update IR playbook con cloud scenarios; 4) Define escalation paths; 5) Test notification flow. Cloud outage = business impact!'
            }
        }
    }
    
    # Return feedback for the specific question and answer
    if question_id in feedback_db:
        if answer in feedback_db[question_id]:
            return feedback_db[question_id][answer]
    
    # Default feedback if not found
    return {
        'status': 'info',
        'icon': 'ℹ️',
        'message': 'Risposta registrata.',
        'advice': ''
    }


def show_realtime_feedback(question_id: str, answer: str):
    """Mostra feedback real-time per una risposta con layout WOW"""
    if not answer or answer == 'N/A':
        return
    
    feedback = get_answer_feedback(question_id, answer)
    
    # Container con bordo per enfatizzare il feedback
    if feedback['status'] == 'optimal':
        st.markdown("---")
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### ✅")
        with col2:
            st.success(f"**{feedback['message']}**", icon="✅")
        
        if feedback['advice']:
            with st.expander("💡 **Best Practice & Raccomandazioni Avanzate**", expanded=True):
                st.markdown(f"""
                <div style='background-color: #d4edda; padding: 20px; border-radius: 10px; border-left: 5px solid #28a745;'>
                {feedback['advice']}
                </div>
                """, unsafe_allow_html=True)
        st.markdown("---")
    
    elif feedback['status'] == 'acceptable':
        st.markdown("---")
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### ⚠️")
        with col2:
            st.warning(f"**{feedback['message']}**", icon="⚠️")
        
        if feedback['advice']:
            with st.expander("📋 **Piano di Miglioramento Raccomandato**", expanded=True):
                st.markdown(f"""
                <div style='background-color: #fff3cd; padding: 20px; border-radius: 10px; border-left: 5px solid #ffc107;'>
                {feedback['advice']}
                </div>
                """, unsafe_allow_html=True)
        st.markdown("---")
    
    elif feedback['status'] == 'needs_improvement':
        st.markdown("---")
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 🔴")
        with col2:
            st.error(f"**{feedback['message']}**", icon="🔴")
        
        if feedback['advice']:
            with st.expander("🔧 **Azioni Correttive RICHIESTE - Piano Dettagliato**", expanded=True):
                st.markdown(f"""
                <div style='background-color: #f8d7da; padding: 20px; border-radius: 10px; border-left: 5px solid #dc3545;'>
                {feedback['advice']}
                </div>
                """, unsafe_allow_html=True)
        st.markdown("---")
    
    elif feedback['status'] == 'critical':
        st.markdown("---")
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("### 🚨")
        with col2:
            st.error(f"**⚠️ ATTENZIONE CRITICA ⚠️**\n\n{feedback['message']}", icon="🚨")
        
        if feedback['advice']:
            with st.expander("⚡ **PIANO DI EMERGENZA - Azione IMMEDIATA Richiesta**", expanded=True):
                st.markdown(f"""
                <div style='background-color: #f8d7da; padding: 25px; border-radius: 10px; border-left: 8px solid #dc3545; box-shadow: 0 4px 6px rgba(220, 53, 69, 0.3);'>
                <h4 style='color: #dc3545; margin-top: 0;'>🚨 SITUAZIONE CRITICA</h4>
                {feedback['advice']}
                </div>
                """, unsafe_allow_html=True)
        st.markdown("---")

def calculate_risk_level(score: int) -> str:
    """Risk classification based on total score"""
    if score >= 85:
        return "LOW"
    elif score >= 65:
        return "MEDIUM"
    else:
        return "HIGH"

def show_answer_feedback(value: str, optimal_values: list, good_values: list = []):
    """Mostra feedback visivo immediato per una risposta"""
    if not value:
        return
    
    if not good_values:
        good_values = []
    
    if value in optimal_values:
        st.success("✓ Risposta ottimale per conformità NIS2/DORA", icon="✅")
    elif good_values and value in good_values:
        st.info("○ Risposta accettabile - Considera miglioramenti", icon="ℹ️")
    else:
        st.warning("⚠ Gap identificato - Vedi raccomandazioni nei risultati", icon="⚠️")

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


def generate_pdf_report(result: AssessmentResult) -> bytes:
    """Generate professional PDF report with branding"""
    
    pdf = FPDF()
    pdf.add_page()
    
    # Header with gradient effect (simulated with colored rectangle)
    pdf.set_fill_color(102, 126, 234)  # Purple gradient color
    pdf.rect(0, 0, 210, 40, 'F')
    
    # Title
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 15, '', 0, 1)  # Spacing
    pdf.cell(0, 10, 'EU DIGITAL RESILIENCE', 0, 1, 'C')
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 8, 'ASSESSMENT REPORT', 0, 1, 'C')
    
    # Reset color and add spacing
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    
    # Info box
    pdf.set_font('Arial', '', 10)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 6, f'Generated: {result.timestamp}', 0, 1, 'C', True)
    pdf.cell(0, 6, f'Sector: {result.sector} | Scope: {result.scope}', 0, 1, 'C', True)
    pdf.ln(10)
    
    # Executive Summary Section
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(102, 126, 234)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, ' EXECUTIVE SUMMARY', 0, 1, 'L', True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)
    
    # Risk Score with color coding
    risk_colors = {
        'LOW': (76, 175, 80),
        'MEDIUM': (255, 152, 0),
        'HIGH': (244, 67, 54)
    }
    risk_color = risk_colors.get(result.risk_level, (128, 128, 128))
    
    pdf.set_font('Arial', 'B', 14)
    pdf.set_fill_color(*risk_color)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 12, f'  TOTAL SCORE: {result.total_score}/100  |  RISK LEVEL: {result.risk_level}  ', 0, 1, 'C', True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(8)
    
    # Domain Breakdown
    pdf.set_font('Arial', 'B', 13)
    pdf.cell(0, 8, 'Domain Breakdown:', 0, 1, 'L')
    pdf.set_font('Arial', '', 11)
    
    domains = [
        ('Governance & Scope', result.governance_score),
        ('Logging & Monitoring', result.logging_score),
        ('ICT Third-Party Risk', result.third_party_score),
        ('Incident & Resilience', result.incident_score)
    ]
    
    for domain, score in domains:
        percentage = int((score / 25) * 100)
        # Color code based on performance
        if percentage >= 80:
            bar_color = (76, 175, 80)
        elif percentage >= 60:
            bar_color = (255, 152, 0)
        else:
            bar_color = (244, 67, 54)
        
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(85, 6, f'  {domain}:', 0, 0, 'L')
        pdf.set_font('Arial', '', 10)
        pdf.cell(35, 6, f'{score}/25', 0, 0, 'L')
        
        # Progress bar
        bar_width = percentage * 0.5  # Max 50mm
        pdf.set_fill_color(*bar_color)
        pdf.rect(pdf.get_x(), pdf.get_y() + 1, bar_width, 4, 'F')
        pdf.cell(55, 6, f'  ({percentage}%)', 0, 1, 'L')
    
    pdf.ln(10)
    
    # Regulatory Gaps Section
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(244, 67, 54)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, ' REGULATORY GAPS', 0, 1, 'L', True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)
    
    gap_count = sum(len(gaps) for gaps in result.regulatory_gaps.values())
    if gap_count > 0:
        pdf.set_font('Arial', '', 9)
        for domain, gaps in result.regulatory_gaps.items():
            if gaps:
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(0, 6, f'{domain}:', 0, 1, 'L')
                pdf.set_font('Arial', '', 9)
                for gap in gaps[:5]:  # Limit gaps per domain
                    pdf.multi_cell(0, 5, f'  - {gap}')
                pdf.ln(2)
    else:
        pdf.set_font('Arial', 'I', 10)
        pdf.cell(0, 6, 'No critical regulatory gaps identified.', 0, 1, 'L')
    
    # Findings Section
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(255, 152, 0)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, f' KEY FINDINGS ({len(result.findings)} items)', 0, 1, 'L', True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)
    
    if result.findings:
        pdf.set_font('Arial', '', 9)
        for i, finding in enumerate(result.findings[:15], 1):  # Limit to 15 findings
            pdf.multi_cell(0, 5, f'{i}. {finding}')
            pdf.ln(1)
    else:
        pdf.set_font('Arial', 'I', 10)
        pdf.cell(0, 6, 'No critical findings.', 0, 1, 'L')
    
    pdf.ln(8)
    
    # Recommendations Section
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(76, 175, 80)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, f' RECOMMENDATIONS ({len(result.recommendations)} items)', 0, 1, 'L', True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)
    
    if result.recommendations:
        # High Priority
        pdf.set_font('Arial', 'B', 11)
        pdf.set_fill_color(255, 235, 238)
        pdf.cell(0, 7, ' HIGH PRIORITY', 0, 1, 'L', True)
        pdf.set_font('Arial', '', 9)
        
        for i, rec in enumerate(result.recommendations[:5], 1):
            pdf.multi_cell(0, 5, f'[HIGH] {rec}')
            pdf.ln(1)
        
        # Medium Priority
        if len(result.recommendations) > 5:
            pdf.ln(3)
            pdf.set_font('Arial', 'B', 11)
            pdf.set_fill_color(255, 243, 224)
            pdf.cell(0, 7, ' MEDIUM PRIORITY', 0, 1, 'L', True)
            pdf.set_font('Arial', '', 9)
            
            for i, rec in enumerate(result.recommendations[5:10], 6):
                pdf.multi_cell(0, 5, f'[MEDIUM] {rec}')
                pdf.ln(1)
    else:
        pdf.set_font('Arial', 'I', 10)
        pdf.cell(0, 6, 'No recommendations needed - excellent compliance posture!', 0, 1, 'L')
    
    # Footer
    pdf.ln(15)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(128, 128, 128)
    pdf.multi_cell(0, 4, 'Disclaimer: This assessment is a readiness and risk evaluation tool. It does not constitute legal advice. Organizations should consult legal counsel for compliance strategy.')
    pdf.ln(3)
    pdf.cell(0, 4, 'EU Digital Resilience Toolkit v1.0 | Framework: NIS2 + DORA', 0, 0, 'C')
    
    return pdf.output(dest='S')


# -----------------------------
# Assessment Logic
# -----------------------------

def get_practical_advice(question_id: str, answer: str) -> str:
    """Genera consigli pratici specifici basati sulla risposta"""
    advice_map = {
        'risk_framework': {
            'No framework': "📋 AZIONE IMMEDIATA: Adotta un framework standard come ISO 27001 o NIST Cybersecurity Framework. Inizia con un gap assessment e documenta le procedure ICT esistenti. Timeline: 3-6 mesi.",
            'Ad-hoc processes': "📊 Formalizza i processi esistenti in un framework documentato. Implementa ciclo PDCA (Plan-Do-Check-Act) e pianifica test annuali. Timeline: 2-3 mesi.",
            'Partially documented': "✅ Completa la documentazione mancante e pianifica test di validazione trimestrale del framework. Timeline: 1 mese."
        },
        'board_oversight': {
            'No oversight': "🚨 CRITICO: Stabilisci immediatamente reporting mensile al board su rischi ICT. Nomina un responsabile cybersecurity con linea diretta al management. Timeline: immediato.",
            'Annual review': "📈 Aumenta la frequenza a revisioni trimestrali. Implementa dashboard rischi ICT per il board con metriche KRI (Key Risk Indicators). Timeline: 1 mese.",
            'Bi-annual reviews': "⬆️ Passa a cadenza trimestrale con metriche standardizzate e trend analysis. Timeline: immediato."
        },
        'centralized_logging': {
            'No centralization': "🔴 CRITICO: Deploy SIEM (es. Splunk, ELK Stack, Microsoft Sentinel) entro 60 giorni. Inizia con log critici (autenticazione, accessi privilegiati, firewall). Budget: €20-50k/anno.",
            'Partial (some sources)': "🔧 Completa integrazione di tutte le sorgenti log. Priorità: server critici, database, cloud services, endpoint. Timeline: 30-45 giorni."
        },
        'log_retention': {
            '<6 months': "🚨 NON CONFORME: Estendi retention a minimo 18 mesi IMMEDIATAMENTE. Configura storage dedicato per log audit. Costo storage: ~€500-2000/TB/anno.",
            '6-12 months': "⚠️ NON CONFORME: Porta retention a 18+ mesi. Implementa tiering storage (hot/warm/cold) per ottimizzare costi. Timeline: 2 settimane.",
            '12-18 months': "📊 Quasi conforme: Estendi a 24 mesi per best practice e margine sicurezza. Timeline: 1 settimana."
        },
        'log_integrity': {
            'No verification': "🔐 Implementa hashing crittografico automatico (SHA-256) per tutti i log. Usa WORM storage o blockchain per log critici. Soluzione: syslog-ng, rsyslog con firma digitale. Timeline: 2-3 settimane.",
            'Manual spot-checks': "🤖 Automatizza verifica integrità con script schedulati. Implementa alerting su anomalie hash. Timeline: 1 settimana."
        },
        'vendor_inventory': {
            'No inventory': "📋 URGENTE: Crea registro ICT providers entro 30 giorni. Template: vendor name, servizi, criticità, dati processati, paese hosting. Tool: Excel/SharePoint o GRC platform.",
            'Informal list': "🗂️ Formalizza inventario con campi strutturati: SLA, certificazioni (SOC2, ISO27001), audit rights, exit strategy. Review trimestrale. Timeline: 2 settimane."
        },
        'audit_rights': {
            'Not in contracts': "⚖️ CRITICO: Rinegozia contratti critici con clausole audit (on-site + report SOC2). Per nuovi contratti: inserisci clausola standard pre-approvata da legal. Timeline: 3-6 mesi.",
            'In some contracts': "📄 Estendi audit rights a TUTTI i vendor critici. Priorità: cloud providers, processori pagamenti, gestori dati sensibili. Timeline: 2-4 mesi."
        },
        'incident_notification_sla': {
            'No SLA': "⏱️ CRITICO: Negozia SLA 24h per incident notification in tutti i contratti. Template clausola: 'Security incidents must be reported within 24 hours of detection'. Timeline: immediate per nuovi, 3-6 mesi per rinegoziazione.",
            '72+ hours': "⚠️ 72h è insufficiente per NIS2. Richiedi upgrade a 24h max. Argomenta con requisiti normativi obbligatori. Timeline: 1-3 mesi."
        },
        'incident_process': {
            'No formal process': "📖 CRITICO: Sviluppa Incident Response Plan (IRP) completo entro 60 giorni. Include: ruoli, escalation, comunicazione, contenimento, recovery. Conduci tabletop exercise. Template: NIST 800-61.",
            'Process exists, not tested': "🎯 Pianifica tabletop exercise trimestrale. Simula scenari realistici: ransomware, data breach, DDoS. Documenta lesson learned. Timeline: 30 giorni per primo test."
        },
        '24h_reporting': {
            'No': "🚨 CRITICO NIS2: Stabilisci processo per early warning 24h alle autorità. Designa CSIRT interno, hotline H24, template pre-approvati. Contatta CSIRT nazionale. Timeline: immediato.",
            'Uncertain': "✅ Testa il processo con simulazione. Verifica: chi notifica, a chi, con quale template, entro quale tempistica. Documenta procedura. Timeline: 2 settimane."
        },
        'resilience_testing': {
            'Never': "🔴 CRITICO: Pianifica test resilienza entro 90 giorni. Inizia con disaster recovery test (backup restore). Poi penetration test. Budget: €10-30k per test completo.",
            'Annually': "📈 Aumenta frequenza a bi-annuale per DORA compliance. Alterna DR test e threat-led penetration testing (TLPT). Timeline: pianifica ora."
        },
        'cloud_governance': {
            'No specific framework': "☁️ URGENTE: Implementa cloud governance framework. Include: inventory servizi, risk assessment per CSP, contratti DORA-compliant, exit strategy. Timeline: 2-3 mesi.",
            'Informal processes': "📋 Formalizza con policy documentate: approvazione servizi cloud, security baseline, data residency, backup strategy. Timeline: 1 mese."
        }
    }
    
    return advice_map.get(question_id, {}).get(answer, "")

def assess_governance(data: dict) -> tuple:
    """Phase 1: Governance & Scope - 25 points
    
    Detailed scoring:
    - Sector classification: 5 pts
    - ICT risk framework: 10 pts
    - Board oversight: 5 pts
    - Cloud governance: 5 pts
    """
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
    """Phase 2: Logging & Monitoring - 25 points
    
    Detailed scoring:
    - Centralized logging: 7 pts
    - Log retention: 7 pts
    - Log integrity: 5 pts
    - Cloud log integration: 3 pts
    - Real-time monitoring: 3 pts
    """
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
    """Phase 3: ICT Third-Party Risk - 25 points
    
    Detailed scoring:
    - Vendor inventory: 6 pts
    - Audit rights: 6 pts
    - Incident notification SLA: 5 pts
    - Cloud exit strategies: 4 pts
    - Supply chain monitoring: 4 pts
    """
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
    """Phase 4: Incident & Resilience - 25 points
    
    Detailed scoring:
    - Incident response process: 7 pts
    - 24h reporting capability: 7 pts
    - Resilience testing: 5 pts
    - RTO/RPO defined: 3 pts
    - Cloud incident integration: 3 pts
    """
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
# Adaptive Questionnaire Logic
# -----------------------------

def estimate_questions_count(scope: list) -> int:
    """Estimate total number of questions based on selected scope"""
    base_questions = 8  # Core governance questions (universal)
    
    count = base_questions
    if any("NIS2" in s for s in scope):
        count += 15  # NIS2-specific questions
    if any("DORA" in s for s in scope):
        count += 12  # DORA-specific questions
    if any("GDPR" in s for s in scope):
        count += 6   # GDPR-specific questions
    if any("AI Act" in s for s in scope):
        count += 8   # AI Act-specific questions
    if any("CRA" in s for s in scope):
        count += 5   # CRA-specific questions
    
    return count

def is_question_applicable(question_id: str, scope: list) -> bool:
    """
    Determine if a question is applicable based on selected scope.
    Returns True if question should be shown.
    """
    # Question applicability mapping
    question_scope_map = {
        # UNIVERSAL (sempre applicabili)
        'risk_framework': ['ALL'],
        'board_oversight': ['ALL'],
        'roles_assigned': ['ALL'],
        'security_policies': ['ALL'],
        'employee_training': ['ALL'],
        'asset_inventory': ['ALL'],
        'vulnerability_management': ['ALL'],
        'patch_management': ['ALL'],
        'mfa': ['ALL'],
        'encryption': ['ALL'],
        'backup': ['ALL'],
        'incident_response_plan': ['ALL'],
        
        # NIS2-specific
        '24h_reporting': ['NIS2'],
        'csirt_notification': ['NIS2'],
        'supply_chain_risk': ['NIS2'],
        'log_retention_18m': ['NIS2'],
        
        # DORA-specific
        'cloud_governance': ['DORA'],
        'ict_third_party_register': ['DORA'],
        'concentration_risk': ['DORA'],
        '2h_esa_notification': ['DORA'],
        'rto_rpo_defined': ['DORA'],
        'resilience_testing': ['DORA'],
        
        # GDPR-specific
        'dpia_conducted': ['GDPR'],
        'data_breach_72h': ['GDPR'],
        'dpo_appointed': ['GDPR'],
        'data_mapping': ['GDPR'],
        'consent_management': ['GDPR'],
        
        # AI Act-specific
        'ai_classification': ['AI Act'],
        'ai_risk_assessment': ['AI Act'],
        'ai_transparency': ['AI Act'],
        'ai_human_oversight': ['AI Act'],
        'training_data_quality': ['AI Act'],
        
        # CRA-specific
        'sbom_available': ['CRA'],
        'vulnerability_disclosure': ['CRA'],
        'security_updates': ['CRA'],
    }
    
    # Get applicable scopes for this question
    applicable_scopes = question_scope_map.get(question_id, ['ALL'])
    
    # If question is universal, always show
    if 'ALL' in applicable_scopes:
        return True
    
    # Check if any of the question's scopes match user's selection
    for scope_item in scope:
        for applicable in applicable_scopes:
            if applicable in scope_item:
                return True
    
    return False

# -----------------------------
# UI Components
# -----------------------------

def show_progress(current_phase: int):
    phases = [
        "0. Scope Selection",
        "1. Governance",
        "2. Technical Security", 
        "3. Third-Party Risk",
        "4. Incident Response",
        "5. Results"
    ]
    
    cols = st.columns(len(phases))
    for i, phase in enumerate(phases):
        with cols[i]:
            if i < current_phase:
                st.success(f"✓ {phase}", icon="✅")
            elif i == current_phase:
                st.info(f"→ {phase}", icon="▶️")
            else:
                st.text(f"  {phase}")

# -----------------------------
# Main Assessment Flow
# -----------------------------

def main():
    st.title("🔍 EU Digital Resilience Assessment")
    
    # Hero section with gradient background
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; margin-bottom: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.2);'>
        <h2 style='color: white; margin: 0; text-align: center;'>🛡️ Comprehensive NIS2 & DORA Compliance Assessment</h2>
        <p style='color: #e0e7ff; text-align: center; font-size: 18px; margin-top: 10px;'>
            Valuta la tua postura di resilienza digitale e identifica i gap normativi in modo interattivo
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key features badges
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div style='text-align: center; padding: 15px; background: #e8f5e9; border-radius: 10px;'>
            <div style='font-size: 32px;'>✅</div>
            <div style='font-weight: bold; color: #2e7d32;'>100% Privacy</div>
            <div style='font-size: 12px; color: #558b2f;'>Zero data collection</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 15px; background: #e3f2fd; border-radius: 10px;'>
            <div style='font-size: 32px;'>⚡</div>
            <div style='font-weight: bold; color: #1565c0;'>Real-Time</div>
            <div style='font-size: 12px; color: #1976d2;'>Feedback immediato</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style='text-align: center; padding: 15px; background: #fff3e0; border-radius: 10px;'>
            <div style='font-size: 32px;'>📊</div>
            <div style='font-weight: bold; color: #e65100;'>Report Completi</div>
            <div style='font-size: 12px; color: #ef6c00;'>Export TXT/CSV</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div style='text-align: center; padding: 15px; background: #fce4ec; border-radius: 10px;'>
            <div style='font-size: 32px;'>🎯</div>
            <div style='font-weight: bold; color: #c2185b;'>Best Practice</div>
            <div style='font-size: 12px; color: #d81b60;'>Consigli actionable</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Initialize session state
    if 'phase' not in st.session_state:
        st.session_state.phase = 0
        st.session_state.data = {}
    
    show_progress(st.session_state.phase)
    st.markdown("---")
    
    # Phase 0: SCOPE SELECTION ONLY (Standalone)
    if st.session_state.phase == 0:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 12px; margin-bottom: 30px;'>
            <h3 style='color: white; margin: 0; text-align: center;'>🎯 Fase 0: Configurazione Assessment</h3>
            <p style='color: #e0e7ff; text-align: center; margin: 10px 0 0 0; font-size: 16px;'>
                Seleziona le normative applicabili per personalizzare il questionario
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Ambito Normativo Applicabile")
        st.info("""
        💡 **Questionario Adattivo:** Seleziona SOLO le normative che si applicano alla tua organizzazione. 
        Il questionario si adatterà automaticamente mostrando solo le domande rilevanti!
        
        - **NIS2**: Settori critici (energia, trasporti, sanità, PA, etc.)
        - **DORA**: Entità finanziarie (banche, assicurazioni, pagamenti)
        - **GDPR**: Trattamento dati personali
        - **AI Act**: Utilizzo sistemi di intelligenza artificiale
        - **CRA**: Prodotti digitali con componenti software
        """)
        
        scope = st.multiselect(
            "Seleziona tutte le normative applicabili alla tua organizzazione",
            [
                "NIS2 Entità Essenziale (>250 dip. O >€50M in settore critico)",
                "NIS2 Entità Importante (>50 dip. O >€10M in settore importante)",
                "DORA Entità Finanziaria (Banca, Assicurazione, Pagamenti)",
                "DORA Fornitore ICT Terzo per entità finanziarie",
                "GDPR - Trattamento dati personali",
                "AI Act - Utilizzo sistemi IA",
                "Cyber Resilience Act - Prodotti digitali con componenti digitali",
                "Non direttamente in scope (valutazione volontaria)"
            ],
            help="💡 Seleziona tutte le opzioni che si applicano. Il questionario si configurerà di conseguenza."
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🏢 Dimensione Organizzazione")
        organization_size = st.selectbox(
            "Dimensione della tua organizzazione",
            [
                "Microimpresa (<10 dipendenti, <€2M fatturato)",
                "Piccola impresa (10-49 dipendenti, €2-10M fatturato)",
                "Media impresa (50-249 dipendenti, €10-50M fatturato)",
                "Grande impresa (≥250 dipendenti O ≥€50M fatturato)",
                "Ente pubblico/PA"
            ],
            help="💡 La dimensione determina l'applicabilità di alcune normative."
        )
        
        # Auto-determine sector based on scope selection
        if "DORA" in str(scope):
            sector = "Financial services"
        elif "NIS2" in str(scope):
            sector = "Critical Infrastructure (NIS2)"
        else:
            sector = "Other/Mixed"
        
        # Store scope configuration
        st.session_state.data.update({
            'sector': sector,
            'scope': scope,
            'scope_str': ', '.join(scope) if scope else 'Valutazione volontaria',
            'organization_size': organization_size
        })
        
        # Show selected scope summary
        if scope:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div style='background: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 5px solid #4caf50;'>
                <h4 style='color: #2e7d32; margin: 0 0 10px 0;'>✅ Configurazione Questionario</h4>
            """, unsafe_allow_html=True)
            
            st.markdown(f"**Normative selezionate:** {len(scope)}")
            for s in scope:
                st.markdown(f"• {s}")
            
            # Calculate expected number of questions based on scope
            total_questions = estimate_questions_count(scope)
            st.markdown(f"\n**Domande previste:** ~{total_questions}")
            st.markdown(f"**Tempo stimato:** ~{total_questions // 3}-{total_questions // 2} minuti")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if scope and st.button("➡️ Inizia Assessment", type="primary", use_container_width=True):
            st.session_state.phase = 1
            st.rerun()
        elif not scope:
            st.warning("⚠️ Seleziona almeno una normativa per continuare")
    
    # Phase 1: Governance (Adaptive based on scope)
    elif st.session_state.phase == 1:
        scope = st.session_state.data.get('scope', [])
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px;'>
            <h3 style='color: white; margin: 0;'>🛡️ Fase 1: Governance & Compliance</h3>
            <p style='color: #ffe0e0; margin: 5px 0 0 0;'>Framework di gestione, responsabilità e accountability</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # UNIVERSAL: Risk Framework (always shown)
            st.markdown("#### 🏗️ Framework ICT Risk Management")
            risk_framework = st.select_slider(
                "Livello di maturità del framework ICT risk management",
                options=["No framework", "Ad-hoc processes", "Partially documented", 
                        "Yes, documented and tested"],
                value=st.session_state.data.get('risk_framework', "Partially documented"),
                help="💡 Framework conforme: ISO 27001, NIST CSF, COBIT. Deve coprire: identification, protection, detection, response, recovery."
            )
            show_realtime_feedback('risk_framework', risk_framework)
            
            # UNIVERSAL: Board Oversight
            st.markdown("#### 👔 Board-Level Oversight")
            board_oversight = st.select_slider(
                "Frequenza di supervisione Board su rischi ICT/cyber",
                options=["No oversight", "Annual review", "Bi-annual reviews", "Yes, quarterly reviews"],
                value=st.session_state.data.get('board_oversight', "Annual review"),
                help="💡 NIS2 e DORA richiedono accountability diretta del Board. Best practice: review trimestrali con KPI/KRI dashboard."
            )
            show_realtime_feedback('board_oversight', board_oversight)
            
            # UNIVERSAL: Security Policies
            st.markdown("#### 📋 Catalogo Policy Sicurezza")
            security_policies = st.selectbox(
                "Policy di sicurezza scritte e approvate formalmente",
                ["No policy", "Informal policies", "Some policies approved", "Complete catalog approved"],
                index=st.session_state.data.get('security_policies_idx', 0),
                help="💡 Policy essenziali: password, access control, backup, incident response, acceptable use."
            )
            show_realtime_feedback('security_policies', security_policies)
        
        with col2:
            # UNIVERSAL: Roles Assignment
            st.markdown("#### 👥 Nomine Formali")
            roles_assigned = st.selectbox(
                "CISO, DPO, Responsabile IA nominati con atto formale?",
                ["No formal roles", "Only DPO (GDPR required)", "CISO + DPO", "All roles with Board reporting"],
                index=st.session_state.data.get('roles_assigned_idx', 0),
                help="💡 Nomine formali con lettera di incarico, reporting line e budget dedicato."
            )
            show_realtime_feedback('roles_assigned', roles_assigned)
            
            # UNIVERSAL: Employee Training
            st.markdown("#### 🎓 Formazione Dipendenti")
            employee_training = st.selectbox(
                "Formazione security awareness per tutti i dipendenti",
                ["No training", "Informal emails", "Annual mandatory training", "Training + phishing simulation"],
                index=st.session_state.data.get('employee_training_idx', 0),
                help="💡 Formazione obbligatoria annuale con attestati: phishing, password, data protection."
            )
            show_realtime_feedback('employee_training', employee_training)
            
            # DORA-specific: Cloud Governance (only if DORA in scope)
            if any("DORA" in s for s in scope):
                st.markdown("#### ☁️ Cloud Governance (DORA)")
                cloud_governance = st.selectbox(
                    "Framework di governance per cloud services critici",
                    ["No framework", "Informal", "Formalized"],
                    index=st.session_state.data.get('cloud_governance_idx', 0),
                    help="💡 DORA Art. 28: Inventory CSP, risk assessment, exit strategy, concentration risk."
                )
                show_realtime_feedback('cloud_governance', cloud_governance)
            else:
                cloud_governance = "N/A"
        
        st.session_state.data.update({
            'risk_framework': risk_framework,
            'board_oversight': board_oversight,
            'security_policies': security_policies,
            'roles_assigned': roles_assigned,
            'employee_training': employee_training,
            'cloud_governance': cloud_governance
        })
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("⬅️ Indietro", use_container_width=True):
                st.session_state.phase = 0
                st.rerun()
        with col_b:
            if st.button("➡️ Continua a Technical Security", type="primary", use_container_width=True):
                st.session_state.phase = 2
                st.rerun()
    
    # Phase 2: Technical Security (Adaptive)
    elif st.session_state.phase == 2:
        scope = st.session_state.data.get('scope', [])
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px;'>
            <h3 style='color: white; margin: 0;'>🔐 Fase 2: Technical Security Measures</h3>
            <p style='color: #e0f7ff; margin: 5px 0 0 0;'>Controlli tecnici, encryption, vulnerability management</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🗄️ Centralizzazione Log")
            centralized_logging = st.selectbox(
                "Sistema di log collection centralizzato",
                ["No centralization", "Partial (some sources)", "Yes, SIEM deployed"],
                help="💡 SIEM platforms: Splunk, ELK, Microsoft Sentinel, Chronicle. Centralizzazione essenziale per correlation e investigation."
            )
            show_realtime_feedback('centralized_logging', centralized_logging)
            
            st.markdown("#### ⏱️ Retention Period")
            log_retention = st.selectbox(
                "Periodo di retention log di sicurezza",
                ["<6 months", "6-12 months", "12-18 months", "18-24 months", "24+ months"],
                help="💡 NIS2 richiede MINIMO 18 mesi. Best practice: 24+ mesi per investigation complesse."
            )
            show_realtime_feedback('log_retention', log_retention)
            
            st.markdown("#### 🔒 Integrity Protection")
            log_integrity = st.selectbox(
                "Verifica integrità log (hashing, WORM storage)",
                ["No verification", "Manual spot-checks", "Yes, automated verification"],
                help="💡 Log integrity garantisce evidenze tamper-proof per audit e legal proceedings. Tech: SHA-256 hashing, WORM storage, blockchain."
            )
            show_realtime_feedback('log_integrity', log_integrity)
        
        with col2:
            if st.session_state.data.get('cloud_usage'):
                st.markdown("#### ☁️ Cloud Logs Integration")
                cloud_logs_integrated = st.selectbox(
                    "Log cloud platform integrati in SIEM",
                    ["No", "Partially", "Yes, all sources"],
                    help="💡 Sources: AWS CloudTrail, Azure Monitor, GCP Cloud Logging, M365 Audit Logs. Essenziale per visibility attack surface cloud."
                )
                show_realtime_feedback('cloud_logs_integrated', cloud_logs_integrated)
            else:
                cloud_logs_integrated = "N/A"
            
            st.markdown("#### 🔴 Real-Time Monitoring")
            realtime_monitoring = st.selectbox(
                "Capacità di monitoring security real-time",
                ["No active monitoring", "Business hours only", "Yes, 24/7 SOC"],
                help="💡 24/7 SOC (Security Operations Center) o MDR (Managed Detection & Response). Cyber attacks avvengono H24, specialmente weekend/notti."
            )
            show_realtime_feedback('realtime_monitoring', realtime_monitoring)
        
        st.session_state.data.update({
            'centralized_logging': centralized_logging,
            'log_retention': log_retention,
            'log_integrity': log_integrity,
            'cloud_logs_integrated': cloud_logs_integrated,
            'realtime_monitoring': realtime_monitoring
        })
        
        # Show real-time score estimate with WOW effect
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 12px;'>
            <h4 style='color: white; margin: 0;'>📊 Anteprima Punteggio Fase 2</h4>
        </div>
        """, unsafe_allow_html=True)
        
        temp_score, _, _, _ = assess_logging(st.session_state.data)
        col_a, col_b, col_c = st.columns([3, 1, 1])
        with col_a:
            progress_color = "#4caf50" if temp_score >= 20 else "#ff9800" if temp_score >= 15 else "#f44336"
            st.markdown(f"""
            <div style='background: white; padding: 15px; border-radius: 10px; margin-top: 10px;'>
                <div style='color: #666; font-size: 14px; margin-bottom: 5px;'>Punteggio Logging & Monitoring</div>
                <div style='background: #e0e0e0; height: 30px; border-radius: 15px; overflow: hidden;'>
                    <div style='background: {progress_color}; width: {int((temp_score/25)*100)}%; height: 100%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;'>
                        {temp_score}/25 ({int((temp_score/25)*100)}%)
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            score_icon = "🟢" if temp_score >= 20 else "🟡" if temp_score >= 15 else "🔴"
            st.markdown(f"""
            <div style='background: white; padding: 15px; border-radius: 10px; margin-top: 10px; text-align: center;'>
                <div style='font-size: 40px;'>{score_icon}</div>
                <div style='font-weight: bold; color: #333;'>{temp_score}/25</div>
            </div>
            """, unsafe_allow_html=True)
        with col_c:
            performance = "Eccellente" if temp_score >= 20 else "Buono" if temp_score >= 15 else "Da migliorare"
            perf_color = "#4caf50" if temp_score >= 20 else "#ff9800" if temp_score >= 15 else "#f44336"
            st.markdown(f"""
            <div style='background: white; padding: 15px; border-radius: 10px; margin-top: 10px; text-align: center;'>
                <div style='color: #666; font-size: 12px;'>Valutazione</div>
                <div style='font-weight: bold; color: {perf_color};'>{performance}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("⬅️ Indietro", use_container_width=True):
                st.session_state.phase = 0
                st.rerun()
        with col_b:
            if st.button("➡️ Continua a Third-Party Risk", type="primary", use_container_width=True):
                st.session_state.phase = 2
                st.rerun()
    
    # Phase 2: Third-Party
    elif st.session_state.phase == 2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 25px; border-radius: 12px; margin-bottom: 25px;'>
            <h3 style='color: white; margin: 0;'>🔗 Fase 3: ICT Third-Party & Supply Chain Risk</h3>
            <p style='color: #fff8e0; margin: 5px 0 0 0;'>Gestione dipendenze e governance vendor (overlap DORA + NIS2)</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📋 Inventory Vendor")
            vendor_inventory = st.selectbox(
                "Registro ICT third-party providers",
                ["No inventory", "Informal list", "Yes, complete and current"],
                help="💡 DORA Art. 28 richiede registro completo: vendor name, servizi, criticità, dati trattati, paese hosting, certificazioni."
            )
            show_realtime_feedback('vendor_inventory', vendor_inventory)
            
            st.markdown("#### 🔍 Audit Rights")
            audit_rights = st.selectbox(
                "Diritti di audit nei contratti vendor",
                ["Not in contracts", "In some contracts", "Yes, in all critical contracts"],
                help="💡 Clausole audit essenziali: on-site inspection, SOC 2 report access, penetration test rights, subprocessor disclosure."
            )
            show_realtime_feedback('audit_rights', audit_rights)
            
            st.markdown("#### ⏰ Incident Notification SLA")
            incident_notification_sla = st.selectbox(
                "SLA notifica incident da vendor",
                ["No SLA", "72+ hours", "24 hours", "12 hours"],
                help="💡 DORA Art. 19 richiede notification tempestiva. Best practice: 24h per incident security, 12h per critical. Include severity levels."
            )
            show_realtime_feedback('incident_notification_sla', incident_notification_sla)
        
        with col2:
            if st.session_state.data.get('cloud_usage'):
                st.markdown("#### 🚪 Cloud Exit Strategy")
                cloud_exit_plan = st.selectbox(
                    "Piano di exit/portability cloud",
                    ["No exit plan", "Documented but not tested", "Yes, tested annually"],
                    help="💡 Exit strategy include: data export procedures, alternative CSP shortlist, timeline 90 giorni, costi exit, business continuity."
                )
                show_realtime_feedback('cloud_exit_plan', cloud_exit_plan)
            else:
                cloud_exit_plan = "N/A"
            
            st.markdown("#### 📡 Continuous Monitoring")
            supply_chain_monitoring = st.selectbox(
                "Monitoring continuo rischio third-party",
                ["No monitoring", "Annual assessments", "Yes, continuous assessment"],
                help="💡 Tools: BitSight, SecurityScorecard, Prevalent. Monitoraggio real-time: cyber rating, breach detection, vulnerability disclosure."
            )
            show_realtime_feedback('supply_chain_monitoring', supply_chain_monitoring)
        
        st.session_state.data.update({
            'vendor_inventory': vendor_inventory,
            'audit_rights': audit_rights,
            'incident_notification_sla': incident_notification_sla,
            'cloud_exit_plan': cloud_exit_plan,
            'supply_chain_monitoring': supply_chain_monitoring
        })
        
        # Show real-time score estimate with WOW effect
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style='background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 20px; border-radius: 12px;'>
            <h4 style='color: white; margin: 0;'>📊 Anteprima Punteggio Fase 3</h4>
        </div>
        """, unsafe_allow_html=True)
        
        temp_score, _, _, _ = assess_third_party(st.session_state.data)
        col_a, col_b, col_c = st.columns([3, 1, 1])
        with col_a:
            progress_color = "#4caf50" if temp_score >= 20 else "#ff9800" if temp_score >= 15 else "#f44336"
            st.markdown(f"""
            <div style='background: white; padding: 15px; border-radius: 10px; margin-top: 10px;'>
                <div style='color: #666; font-size: 14px; margin-bottom: 5px;'>Punteggio Third-Party Risk</div>
                <div style='background: #e0e0e0; height: 30px; border-radius: 15px; overflow: hidden;'>
                    <div style='background: {progress_color}; width: {int((temp_score/25)*100)}%; height: 100%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold;'>
                        {temp_score}/25 ({int((temp_score/25)*100)}%)
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            score_icon = "🟢" if temp_score >= 20 else "🟡" if temp_score >= 15 else "🔴"
            st.markdown(f"""
            <div style='background: white; padding: 15px; border-radius: 10px; margin-top: 10px; text-align: center;'>
                <div style='font-size: 40px;'>{score_icon}</div>
                <div style='font-weight: bold; color: #333;'>{temp_score}/25</div>
            </div>
            """, unsafe_allow_html=True)
        with col_c:
            performance = "Eccellente" if temp_score >= 20 else "Buono" if temp_score >= 15 else "Da migliorare"
            perf_color = "#4caf50" if temp_score >= 20 else "#ff9800" if temp_score >= 15 else "#f44336"
            st.markdown(f"""
            <div style='background: white; padding: 15px; border-radius: 10px; margin-top: 10px; text-align: center;'>
                <div style='color: #666; font-size: 12px;'>Valutazione</div>
                <div style='font-weight: bold; color: {perf_color};'>{performance}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("⬅️ Indietro", use_container_width=True):
                st.session_state.phase = 1
                st.rerun()
        with col_b:
            if st.button("➡️ Continua a Incident & Resilience", type="primary", use_container_width=True):
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
            show_answer_feedback(incident_process, ["Yes, documented and tested"])
            # Real-time feedback
            show_realtime_feedback('incident_process', incident_process)
            
            reporting_24h = st.selectbox(
                "Capability to report incidents within 24 hours",
                ["No", "Uncertain", "Yes, process established"]
            )
            show_answer_feedback(reporting_24h, ["Yes, process established"])
            # Real-time feedback
            show_realtime_feedback('24h_reporting', reporting_24h)
            
            resilience_testing = st.selectbox(
                "Resilience testing frequency",
                ["Never", "Annually", "Bi-annually", "Quarterly"]
            )
            show_answer_feedback(resilience_testing, ["Bi-annually", "Quarterly"], ["Annually"])
            # Real-time feedback
            show_realtime_feedback('resilience_testing', resilience_testing)
        
        with col2:
            rto_rpo_defined = st.selectbox(
                "RTO/RPO defined for critical systems",
                ["No", "For some systems", "Yes, for all critical systems"]
            )
            # Real-time feedback
            show_realtime_feedback('rto_rpo_defined', rto_rpo_defined)
            
            if st.session_state.data.get('cloud_usage'):
                cloud_incident_integration = st.selectbox(
                    "Cloud provider incidents integrated into IR process",
                    ["No", "Yes"]
                )
                # Real-time feedback
                show_realtime_feedback('cloud_incident_integration', cloud_incident_integration)
            else:
                cloud_incident_integration = "N/A"
        
        st.session_state.data.update({
            'incident_process': incident_process,
            '24h_reporting': reporting_24h,
            'resilience_testing': resilience_testing,
            'rto_rpo_defined': rto_rpo_defined,
            'cloud_incident_integration': cloud_incident_integration
        })
        
        # Show real-time score estimate
        st.divider()
        st.markdown("#### 📊 Anteprima Punteggio Fase 4")
        temp_score, _, _, _ = assess_incident(st.session_state.data)
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.progress(temp_score / 25, text=f"Punteggio Incident: {temp_score}/25 ({int((temp_score/25)*100)}%)")
        with col_b:
            score_icon = "🟢" if temp_score >= 20 else "🟡" if temp_score >= 15 else "🔴"
            st.metric("Valutazione", f"{score_icon} {temp_score}/25")
        
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
        st.success(f"✓ Assessment Completo - {result.timestamp}")
        
        # Main Score Card
        st.markdown("### 📊 Riepilogo Punteggi")
        col1, col2, col3 = st.columns([2, 2, 3])
        with col1:
            risk_color = "normal" if risk_level == "LOW" else "inverse" if risk_level == "MEDIUM" else "off"
            st.metric(
                "Punteggio Totale", 
                f"{total_score}/100",
                delta=f"{total_score - 50} vs baseline",
                delta_color=risk_color
            )
        with col2:
            color_icon = "🟢" if risk_level == "LOW" else "🟡" if risk_level == "MEDIUM" else "🔴"
            st.metric("Livello di Rischio", f"{color_icon} {risk_level}")
        with col3:
            compliance_pct = int((total_score / 100) * 100)
            st.metric("Conformità Stimata", f"{compliance_pct}%")
        
        # Score Breakdown with Visual Indicators
        st.markdown("### 🎯 Dettaglio per Dominio")
        
        col1, col2, col3, col4 = st.columns(4)
        domains = [
            ("Governance & Scope", gov_score, 25, col1),
            ("Logging & Monitoring", log_score, 25, col2),
            ("ICT Third-Party", tp_score, 25, col3),
            ("Incident & Resilience", inc_score, 25, col4)
        ]
        
        for domain_name, score, max_score, column in domains:
            with column:
                percentage = int((score / max_score) * 100)
                delta = score - max_score
                delta_color = "normal" if score >= max_score * 0.85 else "inverse" if score >= max_score * 0.65 else "off"
                st.metric(
                    domain_name, 
                    f"{score}/{max_score}",
                    delta=f"{percentage}%",
                    delta_color=delta_color
                )
                # Visual progress bar
                bar_color = "🟢" if percentage >= 85 else "🟡" if percentage >= 65 else "🔴"
                bar_fill = "█" * int(percentage / 10)
                bar_empty = "░" * (10 - int(percentage / 10))
                st.caption(f"{bar_color} {bar_fill}{bar_empty} {percentage}%")
        
        st.divider()
        
        # Summary Stats
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Gaps Normativi", sum(len(gaps) for gaps in all_gaps.values()))
        with col2:
            st.metric("Findings Totali", len(all_findings))
        with col3:
            high_priority = len([r for i, r in enumerate(all_recs, 1) if i <= 3])
            st.metric("Raccomandazioni Alta Priorità", high_priority)
        with col4:
            st.metric("Raccomandazioni Totali", len(all_recs))
        
        st.divider()
        
        # Detailed results with better organization
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📋 Gaps Normativi", 
            "🔍 Findings Dettagliati", 
            "💡 Raccomandazioni",
            "🎯 Suggerimenti Pratici",
            "📝 Risposte Assessment"
        ])
        
        with tab1:
            st.markdown("#### Gap di Conformità Identificati")
            st.caption("Aree che richiedono attenzione per la conformità NIS2/DORA")
            
            total_gaps = 0
            for domain, gaps in all_gaps.items():
                if gaps:
                    total_gaps += len(gaps)
                    with st.expander(f"**{domain}** - {len(gaps)} gap", expanded=True):
                        for i, gap in enumerate(gaps, 1):
                            st.error(f"**Gap {i}:** {gap}", icon="⚠️")
            
            if total_gaps == 0:
                st.success("✓ Nessun gap normativo critico identificato!", icon="✅")
        
        with tab2:
            st.markdown("#### Findings Operativi")
            st.caption("Problemi e carenze identificati durante l'assessment")
            
            if all_findings:
                # Group by domain
                st.markdown("**Governance & Scope**")
                for i, finding in enumerate(gov_findings, 1):
                    st.warning(f"{i}. {finding}", icon="🔸")
                
                st.markdown("**Logging & Monitoring**")
                for i, finding in enumerate(log_findings, 1):
                    st.warning(f"{i}. {finding}", icon="🔸")
                
                st.markdown("**ICT Third-Party Risk**")
                for i, finding in enumerate(tp_findings, 1):
                    st.warning(f"{i}. {finding}", icon="🔸")
                
                st.markdown("**Incident & Resilience**")
                for i, finding in enumerate(inc_findings, 1):
                    st.warning(f"{i}. {finding}", icon="🔸")
            else:
                st.success("✓ Nessun finding critico!", icon="✅")
        
        with tab3:
            st.markdown("#### Piano d'Azione Raccomandato")
            st.caption("Azioni prioritizzate per migliorare la postura di resilienza")
            
            # High Priority
            high_recs = [(i, rec) for i, rec in enumerate(all_recs, 1) if i <= 3]
            if high_recs:
                st.markdown("##### 🔴 ALTA PRIORITÀ - Azioni Immediate")
                for i, rec in high_recs:
                    st.error(f"**{i}.** {rec}", icon="🔴")
            
            # Medium Priority
            medium_recs = [(i, rec) for i, rec in enumerate(all_recs, 1) if 3 < i <= 8]
            if medium_recs:
                st.markdown("##### 🟡 MEDIA PRIORITÀ - Azioni a 30-60 giorni")
                for i, rec in medium_recs:
                    st.warning(f"**{i}.** {rec}", icon="🟡")
            
            # Low Priority
            low_recs = [(i, rec) for i, rec in enumerate(all_recs, 1) if i > 8]
            if low_recs:
                st.markdown("##### 🟢 BASSA PRIORITÀ - Miglioramenti Continui")
                for i, rec in low_recs:
                    st.info(f"**{i}.** {rec}", icon="🟢")
            
            if not all_recs:
                st.success("✓ Eccellente! Tutte le best practice implementate.", icon="✅")
        
        with tab4:
            st.markdown("#### 🎯 Guida Pratica Passo-Passo")
            st.caption("Suggerimenti operativi specifici per ogni gap identificato")
            
            # Collect all practical advice based on answers
            advice_items = []
            
            # Governance advices
            if st.session_state.data.get('risk_framework') != "Yes, documented and tested":
                advice = get_practical_advice('risk_framework', st.session_state.data.get('risk_framework', ''))
                if advice:
                    advice_items.append(("Governance", "ICT Risk Framework", advice, "🔴" if "CRITICO" in advice or "IMMEDIATA" in advice else "🟡"))
            
            if st.session_state.data.get('board_oversight') != "Yes, quarterly reviews":
                advice = get_practical_advice('board_oversight', st.session_state.data.get('board_oversight', ''))
                if advice:
                    advice_items.append(("Governance", "Board Oversight", advice, "🔴" if "CRITICO" in advice else "🟡"))
            
            if st.session_state.data.get('cloud_governance') not in ["Yes, formalized", "N/A"]:
                advice = get_practical_advice('cloud_governance', st.session_state.data.get('cloud_governance', ''))
                if advice:
                    advice_items.append(("Governance", "Cloud Governance", advice, "🟡"))
            
            # Logging advices
            if st.session_state.data.get('centralized_logging') != "Yes, SIEM deployed":
                advice = get_practical_advice('centralized_logging', st.session_state.data.get('centralized_logging', ''))
                if advice:
                    advice_items.append(("Logging", "Centralized Logging", advice, "🔴" if "CRITICO" in advice else "🟡"))
            
            if st.session_state.data.get('log_retention') not in ["18-24 months", "24+ months"]:
                advice = get_practical_advice('log_retention', st.session_state.data.get('log_retention', ''))
                if advice:
                    advice_items.append(("Logging", "Log Retention", advice, "🔴"))
            
            if st.session_state.data.get('log_integrity') != "Yes, automated verification":
                advice = get_practical_advice('log_integrity', st.session_state.data.get('log_integrity', ''))
                if advice:
                    advice_items.append(("Logging", "Log Integrity", advice, "🟡"))
            
            # Third-Party advices
            if st.session_state.data.get('vendor_inventory') != "Yes, complete and current":
                advice = get_practical_advice('vendor_inventory', st.session_state.data.get('vendor_inventory', ''))
                if advice:
                    advice_items.append(("Third-Party", "Vendor Inventory", advice, "🔴" if "URGENTE" in advice else "🟡"))
            
            if st.session_state.data.get('audit_rights') != "Yes, in all critical contracts":
                advice = get_practical_advice('audit_rights', st.session_state.data.get('audit_rights', ''))
                if advice:
                    advice_items.append(("Third-Party", "Audit Rights", advice, "🔴" if "CRITICO" in advice else "🟡"))
            
            if st.session_state.data.get('incident_notification_sla') not in ["24 hours", "12 hours"]:
                advice = get_practical_advice('incident_notification_sla', st.session_state.data.get('incident_notification_sla', ''))
                if advice:
                    advice_items.append(("Third-Party", "Incident SLA", advice, "🔴" if "CRITICO" in advice else "🟡"))
            
            # Incident advices
            if st.session_state.data.get('incident_process') != "Yes, documented and tested":
                advice = get_practical_advice('incident_process', st.session_state.data.get('incident_process', ''))
                if advice:
                    advice_items.append(("Incident", "Incident Response", advice, "🔴" if "CRITICO" in advice else "🟡"))
            
            if st.session_state.data.get('24h_reporting') != "Yes, process established":
                advice = get_practical_advice('24h_reporting', st.session_state.data.get('24h_reporting', ''))
                if advice:
                    advice_items.append(("Incident", "24h Reporting", advice, "🔴"))
            
            if st.session_state.data.get('resilience_testing') not in ["Quarterly", "Bi-annually"]:
                advice = get_practical_advice('resilience_testing', st.session_state.data.get('resilience_testing', ''))
                if advice:
                    advice_items.append(("Incident", "Resilience Testing", advice, "🔴" if "CRITICO" in advice else "🟡"))
            
            # Display advices grouped by priority
            if advice_items:
                # Sort: critical first
                critical_items = [item for item in advice_items if item[3] == "🔴"]
                medium_items = [item for item in advice_items if item[3] == "🟡"]
                
                if critical_items:
                    st.markdown("##### 🔴 PRIORITÀ CRITICA - Azione Immediata Richiesta")
                    for domain, area, advice, _ in critical_items:
                        with st.expander(f"**[{domain}] {area}**", expanded=True):
                            st.markdown(advice)
                            st.divider()
                            st.caption("💡 **Next Steps**: Assegna owner, definisci timeline, allocare budget, trackare progress")
                
                if medium_items:
                    st.markdown("##### 🟡 PRIORITÀ MEDIA - Pianifica Remediation")
                    for domain, area, advice, _ in medium_items:
                        with st.expander(f"**[{domain}] {area}**"):
                            st.markdown(advice)
                            st.divider()
                            st.caption("💡 **Next Steps**: Documenta nel piano di remediation, assegna responsabile")
            else:
                st.success("🎉 Eccellente! Nessun suggerimento critico. Tutte le aree sono conformi.", icon="✅")
                st.info("💡 Continua con il monitoraggio continuo e aggiornamento delle policy in base alle evoluzioni normative.")
        
        with tab5:
            st.markdown("#### Le Tue Risposte")
            st.caption("Riepilogo delle risposte fornite durante l'assessment")
            
            # Display all answers in organized format
            st.markdown("##### 1️⃣ Governance & Scope")
            st.text(f"Settore: {st.session_state.data.get('sector', 'N/A')}")
            st.text(f"Ambito normativo: {st.session_state.data.get('scope', 'N/A')}")
            st.text(f"Framework ICT risk: {st.session_state.data.get('risk_framework', 'N/A')}")
            st.text(f"Supervisione board: {st.session_state.data.get('board_oversight', 'N/A')}")
            cloud_list = st.session_state.data.get('cloud_usage', [])
            st.text(f"Cloud in uso: {', '.join(cloud_list) if cloud_list else 'Nessuno'}")
            st.text(f"Governance cloud: {st.session_state.data.get('cloud_governance', 'N/A')}")
            
            st.markdown("##### 2️⃣ Logging & Monitoring")
            st.text(f"Logging centralizzato: {st.session_state.data.get('centralized_logging', 'N/A')}")
            st.text(f"Retention log: {st.session_state.data.get('log_retention', 'N/A')}")
            st.text(f"Integrità log: {st.session_state.data.get('log_integrity', 'N/A')}")
            st.text(f"Log cloud integrati: {st.session_state.data.get('cloud_logs_integrated', 'N/A')}")
            st.text(f"Monitoring real-time: {st.session_state.data.get('realtime_monitoring', 'N/A')}")
            
            st.markdown("##### 3️⃣ ICT Third-Party Risk")
            st.text(f"Inventario vendor: {st.session_state.data.get('vendor_inventory', 'N/A')}")
            st.text(f"Diritti di audit: {st.session_state.data.get('audit_rights', 'N/A')}")
            st.text(f"SLA notifica incident: {st.session_state.data.get('incident_notification_sla', 'N/A')}")
            st.text(f"Piano exit cloud: {st.session_state.data.get('cloud_exit_plan', 'N/A')}")
            st.text(f"Monitoring supply chain: {st.session_state.data.get('supply_chain_monitoring', 'N/A')}")
            
            st.markdown("##### 4️⃣ Incident & Resilience")
            st.text(f"Processo incident response: {st.session_state.data.get('incident_process', 'N/A')}")
            st.text(f"Reporting 24h: {st.session_state.data.get('24h_reporting', 'N/A')}")
            st.text(f"Test resilienza: {st.session_state.data.get('resilience_testing', 'N/A')}")
            st.text(f"RTO/RPO definiti: {st.session_state.data.get('rto_rpo_defined', 'N/A')}")
            st.text(f"Integrazione incident cloud: {st.session_state.data.get('cloud_incident_integration', 'N/A')}")
        
        st.divider()
        
        # Export options with improved design
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 12px; margin-bottom: 15px;'>
            <h3 style='color: white; margin: 0; text-align: center;'>📥 Export Report Professionale</h3>
            <p style='color: #e0e7ff; text-align: center; margin: 5px 0 0 0;'>Scarica il report in diversi formati per documentazione e audit</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_exp1, col_exp2, col_exp3, col_exp4 = st.columns(4)
        
        with col_exp1:
            text_report = generate_text_report(result)
            st.download_button(
                label="📄 TXT Report",
                data=text_report,
                file_name=f"eu_resilience_assessment_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain",
                use_container_width=True,
                help="Report testuale completo con tutti i dettagli"
            )
        
        with col_exp2:
            csv_report = generate_csv_export(result)
            st.download_button(
                label="📊 CSV Data",
                data=csv_report,
                file_name=f"eu_resilience_assessment_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv",
                use_container_width=True,
                help="Dati strutturati per analisi in Excel/Google Sheets"
            )
        
        with col_exp3:
            pdf_report = generate_pdf_report(result)
            st.download_button(
                label="📑 PDF Report",
                data=pdf_report,
                file_name=f"eu_resilience_assessment_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                mime="application/pdf",
                use_container_width=True,
                help="Report PDF professionale per presentazioni e audit"
            )
        
        with col_exp4:
            if st.button("🔄 Nuovo Assessment", use_container_width=True, help="Ricomincia da capo con un nuovo assessment"):
                st.session_state.phase = 0
                st.session_state.data = {}
                st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Success message
        st.success("""
        ✅ **Assessment Completato con Successo!**
        
        I report sono pronti per il download. Usa i pulsanti sopra per scaricare nei formati desiderati.
        I dati rimangono privati nel tuo browser e non vengono salvati sul server.
        """, icon="✅")

if __name__ == "__main__":
    main()
