# Risk Assessment Page - EU Digital Resilience Toolkit
# Integrated NIS2/DORA Compliance Assessment

import streamlit as st
from dataclasses import dataclass
from datetime import datetime
import csv
from io import StringIO

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
                'message': 'Eccellente! Framework ICT risk maturo e operativo.',
                'advice': 'Mantieni aggiornata la documentazione e conduci test annuali.'
            },
            'Partially documented': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': 'Framework esistente ma non completamente operativo.',
                'advice': 'AZIONE RICHIESTA: Completa la documentazione del framework, definisci processi per identificazione, protezione, detection, response e recovery. Pianifica test annuali del framework.'
            },
            'Ad-hoc processes': {
                'status': 'needs_improvement',
                'icon': '🔴',
                'message': 'Gestione ICT risk non strutturata - Gap normativo critico!',
                'advice': 'PRIORITÀ ALTA: Implementa un framework ICT risk formale secondo ISO 27001 o NIST CSF. Documenta policy, procedure e responsabilità. Timeline: 60-90 giorni.'
            },
            'No framework': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Assenza totale di framework ICT risk - Violazione NIS2 Art. 21 e DORA Art. 6.',
                'advice': 'URGENTE: Avvia immediatamente progetto di implementazione framework ICT risk. Coinvolgi management, definisci governance, identifica asset critici, valuta rischi. Budget consigliato: consultancy esterna + tools. Timeline: 90-120 giorni.'
            }
        },
        
        'board_oversight': {
            'Yes, quarterly reviews': {
                'status': 'optimal',
                'icon': '✅',
                'message': 'Ottimo! Supervisione board allineata alle best practice.',
                'advice': 'Mantieni reporting trimestrale con KPI cyber, metriche resilienza e trend incident.'
            },
            'Bi-annual reviews': {
                'status': 'acceptable',
                'icon': '⚠️',
                'message': 'Oversight presente ma frequenza sotto le best practice.',
                'advice': 'MIGLIORAMENTO: Aumenta frequenza reporting board a trimestrale. Includi: risk dashboard, incident significativi, investimenti cyber, compliance status.'
            },
            'Annual review': {
                'status': 'needs_improvement',
                'icon': '🔴',
                'message': 'Frequenza insufficiente - Non conforme NIS2 Art. 20.',
                'advice': 'AZIONE RICHIESTA: Formalizza reporting board trimestrale. Prepara template con: threat landscape, vulnerabilità critiche, KPI sicurezza, roadmap investimenti. Coinvolgi CISO nelle board meeting.'
            },
            'No oversight': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Assenza accountability board - Violazione diretta NIS2/DORA.',
                'advice': 'URGENTE: Stabilisci governance board immediata. Azioni: 1) Nomina board member responsabile cyber; 2) Pianifica training board su ICT risk; 3) Attiva reporting trimestrale formale. Timeline: 30 giorni.'
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
                'message': 'SIEM operativo - Capacità log management ottimale.',
                'advice': 'Assicurati di integrare tutte le fonti (network, endpoint, cloud, apps). Configura alerting real-time.'
            },
            'Partial (some sources)': {
                'status': 'needs_improvement',
                'icon': '⚠️',
                'message': 'Log collection parziale - Visibilità incompleta.',
                'advice': 'AZIONE: Completa integrazione log sources nel SIEM. Priorità: 1) Sistemi critici; 2) Cloud platforms; 3) Network devices; 4) Security tools. Verifica copertura >90% asset critici.'
            },
            'No centralization': {
                'status': 'critical',
                'icon': '🚨',
                'message': 'CRITICO! Log non centralizzati - Impossibile audit trail e investigation.',
                'advice': 'URGENTE: Deploy SIEM (Splunk, ELK, Microsoft Sentinel, Chronicle). Step: 1) Define use cases; 2) Select platform; 3) Deploy collectors; 4) Configure log sources; 5) Create dashboards. Timeline: 60 giorni. Budget: licensing + professional services.'
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
    """Mostra feedback real-time per una risposta"""
    if not answer or answer == 'N/A':
        return
    
    feedback = get_answer_feedback(question_id, answer)
    
    # Scegli il tipo di alert in base allo status
    if feedback['status'] == 'optimal':
        st.success(f"{feedback['icon']} **{feedback['message']}**", icon="✅")
        if feedback['advice']:
            with st.expander("💡 Best Practice"):
                st.info(feedback['advice'])
    
    elif feedback['status'] == 'acceptable':
        st.warning(f"{feedback['icon']} **{feedback['message']}**", icon="⚠️")
        if feedback['advice']:
            with st.expander("📋 Raccomandazioni"):
                st.warning(feedback['advice'])
    
    elif feedback['status'] == 'needs_improvement':
        st.error(f"{feedback['icon']} **{feedback['message']}**", icon="🔴")
        if feedback['advice']:
            with st.expander("🔧 Azioni Correttive Richieste"):
                st.error(feedback['advice'])
    
    elif feedback['status'] == 'critical':
        st.error(f"{feedback['icon']} **{feedback['message']}**", icon="🚨")
        if feedback['advice']:
            with st.expander("⚡ AZIONI URGENTI"):
                st.error(feedback['advice'])

def calculate_risk_level(score: int) -> str:
    """Risk classification based on total score"""
    if score >= 85:
        return "LOW"
    elif score >= 65:
        return "MEDIUM"
    else:
        return "HIGH"

def show_answer_feedback(value: str, optimal_values: list, good_values: list = None):
    """Mostra feedback visivo immediato per una risposta"""
    if not value:
        return
    
    good_values = good_values or []
    
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
# UI Components
# -----------------------------

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
# Main Assessment Flow
# -----------------------------

def main():
    st.title("🔍 Risk Assessment")
    st.markdown("""
    **Comprehensive NIS2 & DORA Compliance Assessment**  
    
    Complete this multi-phase assessment to evaluate your organization's digital resilience posture
    and identify regulatory gaps.
    """)
    st.divider()
    
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
            show_answer_feedback(risk_framework, 
                               ["Yes, documented and tested"], 
                               ["Partially documented"])
            # Real-time feedback
            show_realtime_feedback('risk_framework', risk_framework)
        
        with col2:
            board_oversight = st.select_slider(
                "Board-level oversight of ICT/cyber risks",
                options=["No oversight", "Annual review", "Bi-annual reviews", "Yes, quarterly reviews"],
                value="Annual review"
            )
            show_answer_feedback(board_oversight, 
                               ["Yes, quarterly reviews"], 
                               ["Bi-annual reviews"])
            # Real-time feedback
            show_realtime_feedback('board_oversight', board_oversight)
            
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
                # Real-time feedback
                show_realtime_feedback('cloud_governance', cloud_governance)
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
        
        # Show real-time score estimate
        st.divider()
        st.markdown("#### 📊 Anteprima Punteggio Fase 1")
        temp_score, _, _, _ = assess_governance(st.session_state.data)
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.progress(temp_score / 25, text=f"Punteggio Governance: {temp_score}/25 ({int((temp_score/25)*100)}%)")
        with col_b:
            score_icon = "🟢" if temp_score >= 20 else "🟡" if temp_score >= 15 else "🔴"
            st.metric("Valutazione", f"{score_icon} {temp_score}/25")
        
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
            show_answer_feedback(centralized_logging, ["Yes, SIEM deployed"])
            # Real-time feedback
            show_realtime_feedback('centralized_logging', centralized_logging)
            
            log_retention = st.selectbox(
                "Log retention period",
                ["<6 months", "6-12 months", "12-18 months", "18-24 months", "24+ months"]
            )
            show_answer_feedback(log_retention, 
                               ["18-24 months", "24+ months"], 
                               ["12-18 months"])
            # Real-time feedback
            show_realtime_feedback('log_retention', log_retention)
            
            log_integrity = st.selectbox(
                "Log integrity verification (hashing, WORM)",
                ["No verification", "Manual spot-checks", "Yes, automated verification"]
            )
            show_answer_feedback(log_integrity, ["Yes, automated verification"])
            # Real-time feedback
            show_realtime_feedback('log_integrity', log_integrity)
        
        with col2:
            if st.session_state.data.get('cloud_usage'):
                cloud_logs_integrated = st.selectbox(
                    "Cloud platform logs integrated into SIEM",
                    ["No", "Partially", "Yes, all sources"]
                )
                # Real-time feedback
                show_realtime_feedback('cloud_logs_integrated', cloud_logs_integrated)
            else:
                cloud_logs_integrated = "N/A"
            
            realtime_monitoring = st.selectbox(
                "Real-time security monitoring",
                ["No active monitoring", "Business hours only", "Yes, 24/7 SOC"]
            )
            # Real-time feedback
            show_realtime_feedback('realtime_monitoring', realtime_monitoring)
        
        st.session_state.data.update({
            'centralized_logging': centralized_logging,
            'log_retention': log_retention,
            'log_integrity': log_integrity,
            'cloud_logs_integrated': cloud_logs_integrated,
            'realtime_monitoring': realtime_monitoring
        })
        
        # Show real-time score estimate
        st.divider()
        st.markdown("#### 📊 Anteprima Punteggio Fase 2")
        temp_score, _, _, _ = assess_logging(st.session_state.data)
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.progress(temp_score / 25, text=f"Punteggio Logging: {temp_score}/25 ({int((temp_score/25)*100)}%)")
        with col_b:
            score_icon = "🟢" if temp_score >= 20 else "🟡" if temp_score >= 15 else "🔴"
            st.metric("Valutazione", f"{score_icon} {temp_score}/25")
        
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
            show_answer_feedback(vendor_inventory, ["Yes, complete and current"])
            # Real-time feedback
            show_realtime_feedback('vendor_inventory', vendor_inventory)
            
            audit_rights = st.selectbox(
                "Contractual audit and access rights",
                ["Not in contracts", "In some contracts", "Yes, in all critical contracts"]
            )
            show_answer_feedback(audit_rights, ["Yes, in all critical contracts"])
            # Real-time feedback
            show_realtime_feedback('audit_rights', audit_rights)
            
            incident_notification_sla = st.selectbox(
                "Vendor incident notification SLA",
                ["No SLA", "72+ hours", "24 hours", "12 hours"]
            )
            show_answer_feedback(incident_notification_sla, ["24 hours", "12 hours"])
            # Real-time feedback
            show_realtime_feedback('incident_notification_sla', incident_notification_sla)
        
        with col2:
            if st.session_state.data.get('cloud_usage'):
                cloud_exit_plan = st.selectbox(
                    "Cloud exit/portability strategy",
                    ["No exit plan", "Documented but not tested", "Yes, tested annually"]
                )
                # Real-time feedback
                show_realtime_feedback('cloud_exit_plan', cloud_exit_plan)
            else:
                cloud_exit_plan = "N/A"
            
            supply_chain_monitoring = st.selectbox(
                "Continuous third-party risk monitoring",
                ["No monitoring", "Annual assessments", "Yes, continuous assessment"]
            )
            # Real-time feedback
            show_realtime_feedback('supply_chain_monitoring', supply_chain_monitoring)
        
        st.session_state.data.update({
            'vendor_inventory': vendor_inventory,
            'audit_rights': audit_rights,
            'incident_notification_sla': incident_notification_sla,
            'cloud_exit_plan': cloud_exit_plan,
            'supply_chain_monitoring': supply_chain_monitoring
        })
        
        # Show real-time score estimate
        st.divider()
        st.markdown("#### 📊 Anteprima Punteggio Fase 3")
        temp_score, _, _, _ = assess_third_party(st.session_state.data)
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.progress(temp_score / 25, text=f"Punteggio Third-Party: {temp_score}/25 ({int((temp_score/25)*100)}%)")
        with col_b:
            score_icon = "🟢" if temp_score >= 20 else "🟡" if temp_score >= 15 else "🔴"
            st.metric("Valutazione", f"{score_icon} {temp_score}/25")
        
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
