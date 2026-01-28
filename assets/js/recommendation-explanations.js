// Recommendation Explanations - Detailed descriptions for each action
// Created by Giulia Casaldi | @gcasaldi

const recommendationExplanations = {
    // Governance recommendations
    "Aggiornare piano di conformità e ottenere nuova approvazione CdA": {
        why: "NIS2 Art. 20 e DORA Art. 5 richiedono accountability formale del management body. Senza approvazione documentata del Consiglio di Amministrazione, l'organizzazione non può dimostrare governance compliance.",
        what: "Preparare documento strategico che include: (1) Analisi gap attuali, (2) Piano di remediation con timeline, (3) Budget allocato, (4) KPI di misurazione progresso, (5) Ruoli e responsabilità assegnati.",
        how: "Convocare CdA straordinario entro 30 giorni. Presentare piano con supporto slide executive. Ottenere delibera formale. Documentare nel verbale. Comunicare approvazione a tutti stakeholder.",
        timeline: "15-20 giorni: 10gg preparazione documento + 5gg coordinamento CdA + 5gg comunicazione",
        deliverables: "Verbale CdA con delibera, Piano conformità approvato (PDF firmato), Email comunicazione ai dipendenti"
    },
    
    "Aggiornare Modello 231 includendo protocolli per prevenzione reati informatici e violazioni AI": {
        why: "D.Lgs. 231/2001 richiede che il Modello Organizzativo includa tutti i reati-presupposto. Reati informatici (Art. 24-bis) e violazioni AI Act sono nuovi rischi penali per l'ente. Senza aggiornamento, l'ente non ha esimente da responsabilità amministrativa.",
        what: "Integrare nel Modello 231 esistente: (1) Nuovi reati cyber (accesso abusivo, phishing, ransomware), (2) Violazioni AI Act (discriminazione algoritmica, mancata trasparenza), (3) Protocolli preventivi specifici, (4) Sistema disciplinare aggiornato, (5) Flussi informativi all'OdV.",
        how: "Step 1: Audit legale con supporto consulente 231 (5 giorni). Step 2: Redazione integrazione Modello (8 giorni). Step 3: Approvazione OdV e CdA (3 giorni). Step 4: Comunicazione e formazione dipendenti (4 giorni).",
        timeline: "20 giorni totali. Coinvolge: Legal dept, CISO, OdV, HR",
        deliverables: "Modello 231 aggiornato, Delibera CdA di adozione, Piano formazione dipendenti, Comunicazione OdV"
    },
    
    "CRITICO: Implementare SGSI conforme ISO 27001:2022 come base per conformità NIS2/DORA": {
        why: "ISO 27001 è lo standard internazionale per la gestione della sicurezza delle informazioni. Senza SGSI strutturato, la conformità NIS2/DORA è impossibile da dimostrare negli audit. Il SGSI fornisce framework sistematico per identificare asset, valutare rischi, implementare controlli.",
        what: "Implementare ISMS (Information Security Management System) secondo ISO 27001:2022 con: (1) Politica sicurezza, (2) Risk assessment strutturato, (3) Statement of Applicability (SoA), (4) Piano trattamento rischi, (5) Procedure operative, (6) Audit interni, (7) Management review.",
        how: "Fase 1 (mesi 1-2): Gap analysis e pianificazione. Fase 2 (mesi 3-6): Implementazione controlli Annex A. Fase 3 (mesi 7-9): Documentazione e audit interno. Fase 4 (mesi 10-12): Pre-assessment e certificazione. Richiedere supporto consulente certificato ISO 27001.",
        timeline: "10-12 mesi per certificazione completa. Quick win: SGSI operativo (non certificato) in 3 mesi",
        deliverables: "Politica ISMS, Risk register, SoA, Procedure operative, Certificato ISO 27001 (se certificazione richiesta)"
    },
    
    "Completare implementazione SGSI e considerare certificazione ISO 27001 per maggiore credibilità": {
        why: "SGSI già avviato ma non completato crea gap documentali. Certificazione ISO 27001 da ente accreditato (ACCREDIA in Italia) fornisce validazione terza parte che aumenta credibilità verso clienti, partner, assicurazioni.",
        what: "Completare elementi mancanti SGSI: Risk assessment aggiornato, SoA completo, procedure documentate, audit interno, management review. Poi valutare certificazione con ente certificatore (TÜV, Bureau Veritas, DNV, etc).",
        how: "Step 1: Gap analysis rispetto ISO 27001:2022 (3 giorni). Step 2: Completare documentazione mancante (15 giorni). Step 3: Audit interno (2 giorni). Step 4: Management review (1 giorno). Step 5: Se certificazione: Pre-assessment, Stage 1, Stage 2 audit.",
        timeline: "1-2 mesi per completamento SGSI. 3-4 mesi aggiuntivi per certificazione",
        deliverables: "SGSI completo, Report audit interno, Certificato ISO 27001 (se richiesto)"
    },
    
    "Completare mapping NIST CSF e integrare con metriche KPI per misurare maturità": {
        why: "NIST Cybersecurity Framework 2.0 fornisce linguaggio comune per misurare maturità cyber. Senza mapping, non si può stabilire baseline, misurare progressi, comunicare con board in termini di business risk.",
        what: "Mappare controlli esistenti alle 6 funzioni NIST CSF 2.0: Govern, Identify, Protect, Detect, Respond, Recover. Definire target profile e attuale maturity level. Creare dashboard KPI con metriche misurabili.",
        how: "Workshop 2 giorni con team security + risk. Usare NIST CSF Excel spreadsheet ufficiale. Per ogni categoria, definire: Tier corrente (1-4), Tier target, Gap, Azioni. Integrare con SGSI esistente.",
        timeline: "10 giorni: 2gg workshop + 5gg mappatura dettagliata + 3gg KPI dashboard",
        deliverables: "NIST CSF mapping completo, Current profile vs Target profile, Dashboard KPI in Excel/PowerBI"
    },
    
    "Completare approvazione formale di tutte le policy e implementare review annuale": {
        why: "NIS2 Art. 21.2 richiede politiche di sicurezza documentate e approvate dal management. Policy non approvate formalmente non sono vincolanti e non proteggono legalmente l'organizzazione.",
        what: "Completare catalogo policy (min 15 policy): Password, Access Control, Backup, Incident Response, Acceptable Use, BYOD, Remote Work, Data Classification, Encryption, Patch Management, Vendor Management, Business Continuity, Disaster Recovery, Change Management, Security Awareness.",
        how: "Per ogni policy: (1) Redazione/aggiornamento (owner: CISO), (2) Review legale, (3) Approvazione CdA/CEO, (4) Pubblicazione intranet, (5) Comunicazione obbligatoria dipendenti, (6) Firma acceptance, (7) Calendario review annuale.",
        timeline: "30 giorni: 2 giorni per policy × 15 policy = 30 giorni (parallelizzabile con team)",
        deliverables: "Policy repository aggiornato, Firma digitale dipendenti, Calendario review annuale"
    },
    
    // Supply Chain recommendations
    "Formalizzare registro fornitori con tutti i campi DORA (contratti, SLA, criticality, dependencies)": {
        why: "DORA Art. 28 richiede registro dettagliato ICT third-party providers. Senza registro strutturato, impossibile fare due diligence, monitorare rischi, gestire concentration risk, rispettare obblighi notifica a autorità.",
        what: "Creare registro Excel/GRC tool con campi: Vendor name, Servizi forniti, Criticality (Critical/Important/Standard), Dati processati, Paese hosting, Subcontrattori, Contratto (data, scadenza), SLA uptime/RTO/RPO, Certificazioni (ISO27001, SOC2), Audit rights (Yes/No), Insurance coverage, Incident notification SLA, Exit strategy, Costo annuale, Business owner.",
        how: "Fase 1: Survey business units per identificare tutti i fornitori IT (5 giorni). Fase 2: Classificazione criticità con business impact analysis (5 giorni). Fase 3: Audit contratti esistenti (10 giorni). Fase 4: Completamento dati mancanti via questionario vendor (15 giorni). Fase 5: Review trimestrale con Procurement.",
        timeline: "35 giorni per primo rilascio. Review trimestrale ongoing",
        deliverables: "Vendor register completo (Excel/SharePoint), Vendor criticality matrix, Processo review trimestrale"
    },
    
    "CRITICO: Aggiornare contratti con clausole audit, incident notification, exit strategy, patch SLA": {
        why: "DORA Art. 30 richiede clausole contrattuali specifiche per ICT providers. Contratti senza audit rights, notification SLA, exit strategy non sono DORA-compliant e creano rischio legale + operativo.",
        what: "Rinegoziare contratti critical vendors includendo: (1) Audit rights (on-site o third-party audit), (2) Incident notification (12-24h per security incident), (3) Exit strategy e portability dati (max 90 giorni), (4) Patch SLA (critical patch entro 48h), (5) Subcontracting approval, (6) Right to terminate per non-compliance, (7) Liability caps, (8) Insurance coverage min €5M, (9) GDPR DPA compliant.",
        how: "Step 1: Identificare top 10 critical vendors (2 giorni). Step 2: Preparare template clausole DORA con Legal (5 giorni). Step 3: Negoziazione contrattuale vendor by vendor (60 giorni - parallelizzabile). Step 4: Firma addendum/nuovo contratto. Step 5: Comunicazione interna nuovi SLA.",
        timeline: "90 giorni totali. Priorità: vendor critici first. Budget: legal fees €5-15k",
        deliverables: "Contratti aggiornati firmati, Template clausole DORA, Vendor compliance matrix"
    },
    
    "Implementare processo verifica annuale certificazioni fornitori": {
        why: "Certificazioni vendor (ISO 27001, SOC 2, PCI-DSS) scadono e devono essere monitorate. Vendor che perde certificazione rappresenta rischio compliance immediato. Processo annuale garantisce continuous assurance.",
        what: "Implementare processo strutturato: (1) Calendario verifica (anniversary contract date), (2) Richiesta certificati aggiornati, (3) Verifica validità su sito ente certificatore, (4) Archiviazione documentale, (5) Escalation se certificato scaduto/non rinnovato, (6) Risk assessment se downgrade vendor.",
        how: "Configurare reminder automatico in CRM/GRC tool. Template email richiesta certificati. Checklist verifica. Dashboard vendor compliance. Escalation policy: se vendor non fornisce certificato entro 30gg → risk assessment → possibile switch vendor.",
        timeline: "5 giorni setup iniziale. 2h/vendor annuali per verifica ongoing",
        deliverables: "Processo documentato, Template richiesta, Dashboard vendor compliance, Escalation policy"
    },
    
    // Incident Response recommendations
    "CRITICO: Stabilire processo 24h early warning e designare CSIRT interno": {
        why: "NIS2 Art. 23 richiede notifica incident significativi entro 24h (early warning) e 72h (report dettagliato) al CSIRT nazionale. Senza processo H24 e team designato, impossibile rispettare deadline legali. Sanzioni: fino €10M o 2% fatturato globale.",
        what: "Implementare: (1) CSIRT team interno (min 3 persone: CISO + 2 IT security), (2) Hotline H24 (reperibilità o outsourced SOC), (3) Incident severity matrix (Critical/High/Medium/Low), (4) Template notifica pre-approvati (24h e 72h), (5) Contatti CSIRT nazionale, (6) Playbook escalation, (7) Test trimestrali.",
        how: "Week 1: Designare CSIRT team con lettera incarico. Week 2: Configurare hotline (numero dedicato + email). Week 3: Creare severity matrix e template notifica. Week 4: Registrazione CSIRT nazionale e test. Budget: €8-15k per hotline annuale se outsourced.",
        timeline: "30 giorni per setup. Test trimestrale ongoing. Reperibilità H24 dal giorno 1",
        deliverables: "CSIRT team designato, Hotline attiva, Severity matrix, Template notifica, Contatti CSIRT nazionale"
    },
    
    "Sviluppare Incident Response Plan e condurre tabletop exercise trimestrale": {
        why: "NIS2 Art. 21.2(d) richiede procedure incident handling. Senza IRP documentato e testato, response time è lento, comunicazione caotica, evidenze perse, legal liability aumenta. Test trimestrali garantiscono muscle memory.",
        what: "Creare IRP completo con: (1) Ruoli e responsabilità CSIRT, (2) Fasi: Detection, Containment, Eradication, Recovery, Lessons Learned, (3) Escalation matrix, (4) Comunicazione interna/esterna, (5) Evidence preservation, (6) Playbook scenari (ransomware, data breach, DDoS, insider threat, supply chain attack). Condurre tabletop exercise trimestrale con scenari realistici.",
        how: "Usare template NIST 800-61 Incident Handling Guide. Workshop 2 giorni con CSIRT team per redazione. Approvazione CEO/CISO. Pubblicazione su wiki interno. Tabletop exercise: scenario 2h, team 6-10 persone, facilitatore esterno, debrief con action items.",
        timeline: "15 giorni per IRP completo. Tabletop exercise trimestrale (2h cadauno)",
        deliverables: "Incident Response Plan documentato, Playbook scenari, Report tabletop exercise, Action items remediation"
    },
    
    "Implementare backup offline immutabile e test recovery mensile": {
        why: "Ransomware moderni criptano anche backup online/cloud. Backup immutabile (air-gapped o Object Lock S3) è unica difesa. NIS2 richiede business continuity tested. Test recovery garantisce RTO/RPO effettivi, non teorici.",
        what: "Implementare 3-2-1-1 rule: 3 copie dati, 2 media diversi, 1 offsite, 1 offline/immutable. Setup: (1) Backup primario (daily incrementale), (2) Backup secondario cloud, (3) Backup offline (tape LTO o disk air-gapped), (4) Retention policy (30gg daily + 12 mensili), (5) Test recovery mensile (full restore DB critico).",
        how: "Soluzione tech: Veeam Backup con immutability, Commvault, Rubrik, o AWS S3 Glacier Vault Lock. Configurazione: 10 giorni. Test recovery: ultimo venerdì del mese, 4h window, documento test result con RTO/RPO achieved. Budget: €10-20k software + storage.",
        timeline: "15 giorni setup. Test mensile ongoing (4h cadauno)",
        deliverables: "Backup infrastructure immutabile, Recovery test report mensile, RTO/RPO baseline documentato"
    },
    
    // Technical Security recommendations
    "Implementare MFA obbligatorio per tutti gli utenti su tutti i sistemi": {
        why: "80% data breach iniziano con credenziali compromesse. MFA riduce rischio phishing del 99.9% (Microsoft research). NIS2 Art. 21.2(c) richiede controlli accesso basati su risk. Password-only è inaccettabile nel 2026.",
        what: "Rollout MFA universale: (1) Cloud apps (Microsoft 365, Google Workspace, Salesforce), (2) VPN accesso remoto, (3) Amministratori server/network, (4) Database produzione, (5) Sistemi critici business. Metodi: Authenticator app (Okta, Duo, Microsoft), FIDO2 hardware key per admin.",
        how: "Fase 1: Pilot MFA su IT team (1 settimana). Fase 2: Rollout admin/privileged users (2 settimane). Fase 3: Rollout users standard (4 settimane con supporto helpdesk). Comunicazione preventiva + training. Helpdesk preparato per reset MFA. Grace period 30gg, poi enforcement.",
        timeline: "8 settimane totali. Budget: €5-15/user/anno licensing",
        deliverables: "MFA enabled su 100% utenti, MFA policy documentata, Helpdesk procedure, Dashboard adoption rate"
    },
    
    "Implementare vulnerability scanning mensile e patch management con SLA 30gg": {
        why: "Vulnerabilità note sono porta ingresso #1 per attacchi. CVSS critical/high devono essere patchate rapidamente. NIS2 Art. 21.2(b) richiede vulnerability handling. Senza scanning regolare + patch disciplinato, exploit garantito.",
        what: "Setup: (1) Vulnerability scanner (Qualys, Rapid7, Tenable Nessus) su tutti asset IT, (2) Scan mensile automatico, (3) Categorizzazione CVSS (Critical>9, High 7-9, Medium 4-7), (4) Patch SLA: Critical 7gg, High 30gg, Medium 90gg, (5) Processo change management, (6) Test pre-prod, (7) Deployment finestre manutenzione, (8) Dashboard compliance.",
        how: "Deploy scanner agent-based su server, agentless su network device. Configurare scan schedule (ultimo weekend mese). Vulnerability Management workflow: Scan → Triage → Prioritize → Test patch → Deploy → Verify → Close. Integrare con ticketing system (Jira, ServiceNow).",
        timeline: "20 giorni setup. Scan mensile ongoing. Budget: €15-30k/anno licensing 500 asset",
        deliverables: "Vulnerability scanner operativo, Patch management policy, SLA compliance dashboard, Report mensile vulnerabilità"
    },
    
    "Implementare EDR/XDR su tutti endpoint e server con threat hunting": {
        why: "Antivirus tradizionale è inefficace contro malware moderno. EDR (Endpoint Detection Response) usa behavioral analysis + AI per rilevare ransomware, fileless malware, zero-day. XDR correla eventi endpoint + network + cloud. Threat hunting proattivo trova attaccanti già dentro perimetro.",
        what: "Deploy EDR/XDR solution: (1) Agent su workstation Windows/Mac, (2) Agent su server Linux/Windows, (3) Console SOC centralizzata, (4) Detection rules tuned, (5) Automated response (isolate endpoint), (6) Threat intelligence feed, (7) Threat hunting mensile, (8) Retention log 12 mesi. Vendor: CrowdStrike, SentinelOne, Microsoft Defender for Endpoint, Palo Alto Cortex.",
        how: "Fase 1: Pilot 50 endpoint (2 settimane). Fase 2: Rollout 500+ endpoint (6 settimane). Fase 3: Tuning false positive (4 settimane). Fase 4: Training SOC team. Fase 5: Threat hunting mensile (4h session). Integrare con SIEM.",
        timeline: "3 mesi rollout completo. Budget: €30-60/endpoint/anno",
        deliverables: "EDR/XDR operativo su 100% asset, SOC dashboard, Threat hunt report mensile, Incident response playbook integrato"
    },
    
    // AI & Ethics recommendations
    "Implementare AI Impact Assessment per sistemi ad alto rischio AI Act": {
        why: "AI Act (Reg UE 2024/1689) classifica sistemi IA in: rischio inaccettabile (vietati), alto rischio (requisiti stretti), rischio limitato (trasparenza), minimo (nessun obbligo). Sistemi alto rischio richiedono conformity assessment prima del deploy. Sanzioni: fino €35M o 7% fatturato.",
        what: "Per ogni sistema IA usato/sviluppato: (1) Classificazione rischio, (2) AI Impact Assessment se alto rischio (AIIA), (3) Risk management system, (4) Data governance, (5) Technical documentation, (6) Logging e tracciabilità, (7) Human oversight, (8) Accuracy/robustness/cybersecurity, (9) Transparency obblighi utenti.",
        how: "Step 1: Inventario sistemi IA in uso (HR recruiting, credit scoring, chatbot, fraud detection, etc). Step 2: Classificazione rischio usando Annex III AI Act. Step 3: AIIA template per sistemi alto rischio. Step 4: Gap remediation. Step 5: Documentazione tecnica. Considerare supporto legal specialized in AI Act.",
        timeline: "30-45 giorni per assessment. 3-6 mesi remediation se gap significativi",
        deliverables: "AI systems inventory, Risk classification matrix, AIIA completi, Technical documentation, Remediation plan"
    },
    
    "Designare AI Officer e implementare AI governance framework": {
        why: "AI Act richiede governance strutturata per sistemi IA. Senza AI Officer designato, manca ownership, accountability, expertise. AI governance framework garantisce: ethical use, bias mitigation, transparency, human oversight, compliance ongoing.",
        what: "Nominare AI Officer/AI Ethics Officer con: (1) Reporting line a CdA, (2) Budget dedicato, (3) Team cross-functional (Legal, IT, Business, HR, Ethics), (4) AI governance policy, (5) AI risk committee, (6) Review trimestrale sistemi IA, (7) Training dipendenti, (8) Whistleblowing channel per concern etici.",
        how: "Step 1: Job description AI Officer (mix competenze: tech, legal, ethics). Step 2: Nomina interna o hiring esterno. Step 3: Redazione AI Governance Policy. Step 4: Costituzione AI Risk Committee. Step 5: Calendario review trimestrali. Step 6: Training awareness AI ethics per dipendenti.",
        timeline: "60 giorni per nomina + setup governance. Ongoing operations",
        deliverables: "AI Officer nominato, AI Governance Policy, AI Risk Committee costituito, Training program AI ethics"
    }
    },
    
    "CRITICO: Nominare formalmente CISO, DPO e Responsabile sorveglianza IA con lettera di incarico": {
        why: "NIS2, DORA, GDPR e AI Act richiedono ruoli di governance specifici con responsabilità formali. Senza nomine ufficiali manca accountability legale. In caso di incident o violazione, assenza di ruoli designati aggrava responsabilità aziendale e personale (es. responsabilità amministrativa dirigenti).",
        what: "Designare formalmente: (1) CISO (Chief Information Security Officer) - responsabile sicurezza IT, (2) DPO (Data Protection Officer) - responsabile protezione dati personali GDPR, (3) AI Officer - responsabile governance sistemi intelligenza artificiale. Lettera di incarico deve specificare: mansioni, poteri, budget, reporting line (preferibilmente CdA), durata mandato.",
        how: "Step 1: Job description dettagliata per ogni ruolo. Step 2: Selezione candidati (interni o hiring esterno). Step 3: Lettera di incarico firmata da CEO/CdA con accettazione formale. Step 4: Comunicazione interna (email all staff). Step 5: Registrazione CISO/DPO presso autorità (se richiesto). Step 6: Allocation budget e risorse. Budget hiring: €60-120k/anno per CISO, €40-80k DPO, €50-90k AI Officer.",
        timeline: "30-60 giorni per nomine interne. 90-120 giorni se hiring esterno",
        deliverables: "Lettere di incarico firmate, Organigramma aggiornato, Comunicazione interna, Registrazione presso Garante Privacy (DPO)"
    },
    
    "CRITICO: Ottenere approvazione formale del CdA per il piano di conformità con delibera documentata": {
        why: "NIS2 Art. 20 stabilisce responsabilità diretta del management body per cyber resilience. DORA Art. 5 richiede approvazione strategia ICT risk. Senza delibera CdA, gli amministratori non hanno esercitato dovere di vigilanza (art. 2392 c.c.) e rischiano responsabilità personale in caso di incident grave.",
        what: "Sottoporre al CdA piano compliance strutturato con: (1) Executive summary rischi, (2) Gap analysis vs NIS2/DORA/GDPR/AI Act, (3) Roadmap remediation pluriennale, (4) Budget investimenti security (% fatturato), (5) KPI monitoraggio trimestrale, (6) Assegnazione responsabilità dirigenti.",
        how: "Preparare slide presentation (max 20 slide) con supporto consulente legal/security. Includere: scenario worst-case (ransomware, data breach, sanzioni), costo business disruption, ROI investimenti security. Convocare CdA dedicato (2h session). Ottenere delibera unanime. Verbalizzare nel libro verbali CdA. Archiviare documentazione firmata.",
        timeline: "15 giorni preparazione + convocazione CdA (in base a calendar)",
        deliverables: "Delibera CdA estratto verbale, Piano compliance approvato, Presentazione board, Email comunicazione dipendenti"
    },
    
    "Organizzare formazione certificata per il CdA su cyber risks e regolamentazione IA": {
        why: "NIS2 Art. 20.2(a) obbliga formazione management body su cyber risks. Amministratori senza formazione adeguata non possono esercitare vigilanza informata, valutare risk appetite, challenge il CISO. Ignoranza non è esimente in caso di responsabilità (business judgment rule richiede informed decision).",
        what: "Organizzare sessione formativa dedicata CdA (4-6 ore) su: (1) Panorama minacce 2026 (ransomware, supply chain attacks, AI-powered threats), (2) Obblighi NIS2/DORA/AI Act e sanzioni, (3) Governance best practice, (4) Cyber insurance, (5) Crisis management, (6) Case study incident reali. Certificato di partecipazione.",
        how: "Ingaggiare formatore qualificato (law firm specializzata cyber + CISO esterno come co-trainer). Formato: mezza giornata in presenza. Materiali: slide deck, handbook, checklist board. Test finale verifica apprendimento (non eliminatorio, ma dimostra diligenza). Attestato nominativo. Budget: €3-8k per sessione. Ripetere annualmente.",
        timeline: "20 giorni organizzazione. 4-6 ore sessione formativa",
        deliverables: "Certificato partecipazione per ogni amministratore, Materiali didattici, Test di verifica compilato, Documentazione archiviata"
    },
    
    "Implementare programma formazione annuale obbligatoria per tutti con test e attestati": {
        why: "NIS2 Art. 21.2(g) richiede training awareness per tutti i dipendenti. Human error è causa #1 di breach (phishing, password deboli, social engineering). Formazione obbligatoria con test misurabile riduce rischio e dimostra compliance negli audit. Attestati sono evidenza audit-ready.",
        what: "Implementare piattaforma e-learning con: (1) Moduli obbligatori annuali: Password hygiene, Phishing recognition, Data classification, Incident reporting, BYOD/remote work policy, Social engineering, Physical security. (2) Test finale per modulo (min 80% pass rate). (3) Attestato digitale. (4) Reminder automatici. (5) Dashboard HR compliance.",
        how: "Opzioni: (1) Piattaforma e-learning (KnowBe4, Proofpoint, Cyber Guru) con subscription €20-40/user/anno, oppure (2) Sviluppo interno con LMS aziendale. Contenuti: video 5-10 minuti, quiz interattivi, simulazioni phishing. Lancio: comunicazione CEO, deadline 60gg, escalation manager per non-compliant. Tracking HR.",
        timeline: "30 giorni setup piattaforma. Rollout 60 giorni con deadline compliance. Rinnovo annuale",
        deliverables: "Piattaforma e-learning operativa, Catalogo corsi, Dashboard compliance per HR, Attestati digitali per 100% dipendenti"
    },
    
    "Creare registro completo ICT providers entro 30 giorni": {
        why: "DORA Art. 28 richiede registro dettagliato ICT third-party providers. Ignorare vendor nascosti crea blind spot di rischio. Incident su fornitore sconosciuto può causare business disruption + sanzioni per mancata due diligence. Registro è prerequisito per concentration risk analysis.",
        what: "Creare spreadsheet/database strutturato con: Vendor name, Ragione sociale, Paese sede, Servizi forniti, Sistemi/dati accessibili, Classificazione (Critical/Important/Standard), Owner business, Referente vendor, Contratto (numero, data firma, scadenza), SLA (uptime, RTO, RPO), Certificazioni (ISO27001, SOC2, etc), Ultimo audit, Subcontrattori, Costo annuo, Note.",
        how: "Fase 1: Survey IT + Finance + Procurement per elenco vendor IT (5 giorni). Fase 2: Estensione a business units per shadow IT (5 giorni). Fase 3: Analisi fatture ultime 24 mesi per vendor dimenticati (3 giorni). Fase 4: Classificazione criticità business impact (5 giorni). Fase 5: Completamento campi via questionario (10 giorni). Fase 6: Review trimestrale update. Tool: Excel avanzato o SharePoint list o modulo GRC platform.",
        timeline: "30 giorni per versione 1.0 completa. Update trimestrale ongoing",
        deliverables: "Vendor register completo (min 50 campi), Vendor criticality matrix, Processo di update trimestrale, Dashboard vendor compliance"
    },
    
    "Implementare SIEM centralizzato con retention 12 mesi": {
        why: "NIS2 Art. 21.2(e) richiede logging centralizzato e correlazione eventi security. SIEM (Security Information Event Management) è strumento core per rilevare attacchi in real-time, investigation post-incident, audit trail, compliance. Retention 12 mesi permette forensics e rispetto obblighi GDPR breach notification.",
        what: "Deploy SIEM platform: (1) Log collection da tutti i sistemi critici (AD, firewall, server, database, cloud, endpoint), (2) Normalization e parsing, (3) Correlation rules per detection (es. brute force, lateral movement, data exfiltration), (4) Dashboard SOC, (5) Alerting real-time, (6) Retention 12+ mesi, (7) Role-based access control. Vendor: Splunk, QRadar, Sentinel, LogRhythm, Elastic SIEM.",
        how: "Fase 1: Sizing e selezione vendor (15 giorni). Fase 2: Deploy infrastruttura (10 giorni). Fase 3: Integration log sources priority 1 (20 giorni). Fase 4: Tuning correlation rules (30 giorni). Fase 5: Training SOC team (10 giorni). Fase 6: Go-live e monitoring 24x7. Budget: €30-150k/anno in base a log volume (GB/day).",
        timeline: "3 mesi per deployment completo. Tuning ongoing primi 6 mesi",
        deliverables: "SIEM operativo H24, Dashboard SOC, Correlation rules attive, Log retention 12+ mesi, Playbook investigation, SOC team trained"
    },
    
    "Implementare processo gestione vulnerabilità con scan automatici mensili": {
        why: "Vulnerabilità software sono vettore #1 di attacco. Exploit kit automatizzati scansionano internet per CVE recenti. Tempo medio exploit public vulnerability: 7 giorni. Senza vulnerability management, l'organizzazione è vulnerabile a ransomware, data breach, defacement. NIS2 richiede patch management disciplinato.",
        what: "Implementare Vulnerability Management Program: (1) Vulnerability scanner (Qualys, Tenable Nessus, Rapid7) su tutti asset, (2) Scan automatico mensile + on-demand, (3) Integrazione con asset inventory, (4) Prioritizzazione CVSS + EPSS + business context, (5) Workflow remediation (triage → assign → patch → verify), (6) SLA patch: Critical 7gg, High 30gg, Medium 90gg, (7) Dashboard compliance, (8) Reporting executive mensile.",
        how: "Deploy scanner agent-based (server) + agentless (network device/IoT). Configurare credentialed scan per deep inspection. Tuning per ridurre false positive. Integration con CMDB per asset context. Workflow ticketing: vulnerability detected → JIRA ticket auto-created → assign owner → patch in test → deploy prod → rescan verify. Metriche: Mean Time To Remediate (MTTR), Patch compliance %, Vulnerability backlog.",
        timeline: "30 giorni deployment scanner. Scan mensile ongoing. Budget: €15-40k/anno licensing",
        deliverables: "Vulnerability scanner operativo, Scan schedule mensile, Patch management policy con SLA, Dashboard vulnerability metrics, Executive report mensile"
    },
    
    "Implementare backup immutabile e test restore mensile RTO/RPO": {
        why: "Ransomware moderni criptano backup online accessibili dalla rete. Senza backup immutabile (air-gapped o Object Lock), recovery post-ransomware è impossibile. Business pagherebbe riscatto o perderebbe dati permanentemente. NIS2 richiede business continuity tested. RTO (Recovery Time Objective) e RPO (Recovery Point Objective) devono essere misurati con test reali, non assunti teorici.",
        what: "Implementare strategia backup 3-2-1-1: 3 copie dati, 2 media diversi, 1 offsite, 1 immutable/offline. Componenti: (1) Backup primario incrementale giornaliero, (2) Backup cloud secundario, (3) Backup offline (tape LTO9 o disk air-gapped disconnesso), (4) Immutability setting (WORM - Write Once Read Many), (5) Encryption AES-256, (6) Test restore mensile completo sistema critico, (7) Documentazione RTO/RPO achieved.",
        how: "Soluzioni tech: Veeam Backup & Replication con Immutability, Commvault, Rubrik, Cohesity, o AWS Backup con S3 Glacier Vault Lock. Architettura: Backup server dedicato → Storage primario (NAS) → Cloud tier (S3/Azure Blob) → Tape library offline. Test restore: ultimo venerdì mese, full restore DB produzione in ambiente test, misura tempo restore, verifica integrità dati, documenta RTO/RPO. Budget: €15-35k software + €10-20k storage hardware.",
        timeline: "20 giorni deployment. Test mensile ongoing (4-6h cadauno)",
        deliverables: "Backup infrastructure immutabile, Backup policy documentata, Test restore report mensile, RTO/RPO baseline misurato, Runbook disaster recovery"
    }
};

// Function to get detailed explanation for a recommendation
function getRecommendationExplanation(recommendationText) {
    // Try exact match first
    if (recommendationExplanations[recommendationText]) {
        return recommendationExplanations[recommendationText];
    }
    
    // Try partial match (for variations)
    for (let key in recommendationExplanations) {
        if (recommendationText.includes(key) || key.includes(recommendationText.substring(0, 30))) {
            return recommendationExplanations[key];
        }
    }
    
    // Default explanation if not found
    return {
        why: "Questa azione migliora la postura di compliance e riduce il rischio cyber dell'organizzazione.",
        what: "Implementare i controlli e le procedure necessarie per colmare il gap identificato.",
        how: "Pianificare l'implementazione con owner designato, timeline definita e budget allocato.",
        timeline: "Da definire in base alla complessità specifica",
        deliverables: "Documentazione conforme, procedure operative, evidenze audit-ready"
    };
}
