// EU Digital Resilience Toolkit - NIS2 Gold Standard Assessment 2026
// Complete coverage: NIS2, DORA, GDPR, AI Act, CRA, ISO 27001, NIST CSF

// Assessment data storage
const assessmentData = {
    // Area 1: Governance (29 points)
    board_approval: '',
    executive_training: '',
    model_231_updated: '',
    roles_assigned: '',
    iso_27001_compliance: '',  // NEW
    nist_csf_adoption: '',       // NEW
    security_policies_catalog: '',  // NEW - NIS2 Art. 21.2
    employee_security_training: '',  // NEW - NIS2 Art. 21.2
    
    // Area 2: Risk Management (19 points)
    unified_asset_inventory: '',
    ai_classification: '',
    dpia_conducted: '',
    sbom_available: '',
    risk_assessment_frequency: '',
    key_personnel_inventory: '',  // NEW - NIS2 Art. 21.2
    continuous_improvement: '',   // NEW - ISO 27001 / NIS2
    
    // Area 3: Supply Chain (22 points)
    ict_supplier_register: '',
    contract_clauses_2026: '',
    supplier_certifications: '',
    concentration_risk: '',
    subcontractor_oversight: '',
    exit_management: '',         // NEW - NIS2 Art. 21.2
    shadow_it_control: '',       // NEW
    byod_policy: '',             // NEW
    
    // Area 4: Incident Response (18 points)
    notification_procedure: '',
    severity_classification: '',
    emergency_channels: '',
    incident_reporting_log: '',
    simulation_exercises: '',
    digital_forensics_capability: '',  // NEW
    
    // Area 5: Technical + Physical Security (27 points)
    mfa_zerotrust: '',
    encryption: '',
    vulnerability_management: '',
    patch_management_sla: '',    // NEW - NIS2 Art. 21.2
    immutable_backups: '',
    network_segmentation: '',
    logging_monitoring: '',
    physical_security: '',       // NEW
    environmental_controls: '',  // NEW
    business_continuity_rto: '', // NEW - Domanda killer!
    
    // Area 6: AI & Ethics (15 points)
    ai_transparency: '',
    training_data_quality: '',
    human_oversight: '',
    ai_systems_in_use: '',
    ai_risk_assessment: '',
    ai_documentation: '',
    
    // Additional fields
    sector: '',
    scope: [],
    organization_size: ''
};

const phases = [
    { id: 0, name: '1. Governance & Legal', key: 'governance' },
    { id: 1, name: '2. Risk & Asset Management', key: 'risk_management' },
    { id: 2, name: '3. Supply Chain', key: 'supply_chain' },
    { id: 3, name: '4. Incident Response', key: 'incident' },
    { id: 4, name: '5. Technical Measures', key: 'technical' },
    { id: 5, name: '6. AI & Ethics', key: 'ai_ethics' },
    { id: 6, name: '7. Results', key: 'results' }
];

// Assessment Questions - 6 Aree Complete
const assessmentQuestions = {
    governance: {
        title: '🛡️ AREA 1: Governance e Responsabilità Legale',
        subtitle: 'NIS2 Art. 20 / DORA Art. 5 / AI Act Art. 16 - CdA & Legal Compliance',
        questions: [
            {
                id: 'sector',
                label: 'Settore organizzazione (NIS2 Annex I & II / DORA Art. 2)',
                helpText: 'In che settore lavorate? Ad esempio: banca, ospedale, energia, trasporti. Ogni settore ha regole diverse.',
                type: 'select',
                options: [
                    'Servizi finanziari (Banche, Assicurazioni, Investimenti)',
                    'Energia (Elettricità, Gas, Idrogeno)',
                    'Trasporti (Aereo, Ferroviario, Marittimo)',
                    'Sanità (Ospedali, Dispositivi medici, Farmaceutico)',
                    'Infrastrutture digitali (DNS, Cloud, Data center)',
                    'Pubblica amministrazione (Governo centrale/regionale)',
                    'Acqua e acque reflue',
                    'Provider digitali (Marketplace, Motori ricerca, Social network)',
                    'Spazio',
                    'Manifatturiero (Prodotti critici)',
                    'Servizi postali e corrieri',
                    'Gestione rifiuti',
                    'Produzione chimica',
                    'Produzione e distribuzione alimentare',
                    'Ricerca',
                    'Altro/Non elencato'
                ]
            },
            {
                id: 'organization_size',
                label: 'Dimensione organizzazione',
                helpText: 'Quante persone lavorano nella vostra azienda e quanto fatturate all\'anno? Questo determina quali leggi si applicano.',
                type: 'select',
                options: [
                    'Microimpresa (<10 dipendenti, <€2M fatturato)',
                    'Piccola impresa (10-49 dipendenti, €2-10M fatturato)',
                    'Media impresa (50-249 dipendenti, €10-50M fatturato)',
                    'Grande impresa (≥250 dipendenti O ≥€50M fatturato)',
                    'Ente pubblico/PA'
                ]
            },
            {
                id: 'scope',
                label: 'Ambito normativo applicabile (seleziona tutti applicabili)',
                helpText: 'Quali leggi europee riguardano la vostra azienda? Selezionate tutte quelle applicabili (NIS2, DORA, GDPR, AI Act...).',
                type: 'checkbox',
                options: [
                    'NIS2 Entità Essenziale (>250 dip. O >€50M in settore critico)',
                    'NIS2 Entità Importante (>50 dip. O >€10M in settore importante)',
                    'DORA Entità Finanziaria (Banca, Assicurazione, Pagamenti)',
                    'DORA Fornitore ICT Terzo per entità finanziarie',
                    'GDPR - Trattamento dati personali',
                    'AI Act - Utilizzo sistemi IA',
                    'Cyber Resilience Act - Prodotti digitali con componenti digitali',
                    'Non direttamente in scope (conformità volontaria)'
                ]
            },
            {
                id: 'board_approval',
                label: '✅ POLICY: Il CdA ha approvato formalmente il piano di conformità 2026? (NIS2/DORA/AI Act)',
                helpText: 'I capi dell\'azienda (Consiglio di Amministrazione) hanno approvato ufficialmente il piano per rispettare le nuove leggi del 2026? Serve una decisione formale scritta.',
                type: 'select',
                options: [
                    'No - Nessuna approvazione formale del CdA',
                    'Parziale - Discusso ma non approvato formalmente',
                    'Sì - Piano approvato ma datato (>12 mesi)',
                    'Sì - Piano approvato nel 2025/2026 con delibera formale',
                    'Sì - Piano approvato con revisioni trimestrali documentate'
                ]
            },
            {
                id: 'executive_training',
                label: '✅ IMPLEMENTAZIONE: Formazione obbligatoria - Esistono prove (attestati) che i vertici abbiano ricevuto formazione?',
                helpText: 'I dirigenti e il management hanno fatto corsi di formazione sulla sicurezza informatica? Servono attestati che provino la frequenza.',
                type: 'select',
                options: [
                    'No - Nessuna formazione ai vertici',
                    'Informale - Briefing senza attestazione',
                    'Base - Formazione generica annuale con attestati',
                    'Avanzata - Formazione specialistica cybersecurity + IA con attestati',
                    'Eccellente - Formazione trimestrale certificata con test di verifica'
                ]
            },
            {
                id: 'model_231_updated',
                label: '✅ LOG: Modello Organizzativo 231 - È stato aggiornato per i nuovi reati informatici e AI Act?',
                helpText: 'Il Modello 231 (regole per evitare responsabilità penale dell\'azienda) è aggiornato con i nuovi reati informatici e sull\'intelligenza artificiale?',
                type: 'select',
                options: [
                    'No - Modello 231 non presente',
                    'No - Modello 231 presente ma mai aggiornato per cyber/IA',
                    'Parziale - Aggiornato solo per reati informatici',
                    'Sì - Aggiornato nel 2025/2026 includendo cyber e IA',
                    'Sì - Aggiornato con analisi rischi specifica e protocolli operativi'
                ]
            },
            {
                id: 'roles_assigned',
                label: '✅ Nomine formali - CISO, DPO, Responsabile sorveglianza IA nominati con atto formale?',
                helpText: 'Ci sono persone nominate ufficialmente per gestire sicurezza (CISO), privacy (DPO) e intelligenza artificiale? Servono lettere di incarico formali.',
                type: 'select',
                options: [
                    'No - Nessuna nomina formale',
                    'Parziale - Solo DPO nominato (obbligo GDPR)',
                    'Buono - CISO e DPO nominati formalmente',
                    'Ottimo - CISO, DPO e Resp. IA nominati con lettera di incarico',
                    'Eccellente - Tutti nominati con reporting line al CdA e budget dedicato'
                ]
            },
            {
                id: 'iso_27001_compliance',
                label: '🌐 FRAMEWORK INTERNAZIONALE: ISO/IEC 27001:2022 - L\'azienda ha un SGSI (Sistema Gestione Sicurezza Informazioni)?',
                helpText: 'Avete un sistema organizzato per gestire la sicurezza informatica secondo lo standard ISO 27001? È come avere un \'libretto delle istruzioni\' certificato.',
                type: 'select',
                options: [
                    'No - Nessun SGSI implementato',
                    'In preparazione - SGSI in fase di progettazione',
                    'Parziale - SGSI informale senza certificazione',
                    'Sì - SGSI documentato conforme ISO 27001 (non certificato)',
                    'Sì - ISO 27001:2022 certificata con audit annuali'
                ]
            },
            {
                id: 'nist_csf_adoption',
                label: '🌐 FRAMEWORK INTERNAZIONALE: NIST CSF 2.0 - Mappate le 6 funzioni (Govern/Identify/Protect/Detect/Respond/Recover)?',
                helpText: 'Usate il framework NIST (una checklist americana molto usata) per verificare di aver coperto tutte le aree di sicurezza? Ha 6 funzioni principali da seguire.',
                type: 'select',
                options: [
                    'No - Funzioni NIST non mappate',
                    'Conoscenza base - Team conosce NIST ma non applicato',
                    'Parziale - Alcune funzioni mappate informalmente',
                    'Buono - Tutte le 6 funzioni mappate e documentate',
                    'Eccellente - NIST CSF 2.0 completamente integrato con metriche KPI'
                ]
            },
            {
                id: 'security_policies_catalog',
                label: '📋 POLICY CATALOG: Catalogo politiche sicurezza - Avete policy scritte e approvate formalmente? (NIS2 Art. 21.2)',
                helpText: 'Avete un elenco di tutte le politiche di sicurezza scritte e approvate dal management? (Policy password, policy accessi, policy backup, ecc.).',
                type: 'select',
                options: [
                    'No - Nessuna policy scritta',
                    'Parziale - Alcune policy informali non approvate',
                    'Buono - Policy principali scritte ma non tutte approvate',
                    'Ottimo - Catalogo policy completo approvato dal CdA',
                    'Eccellente - Policy catalog + review annuale + versioning documentato'
                ]
            },
            {
                id: 'employee_security_training',
                label: '👥 FORMAZIONE DIPENDENTI: Security awareness - Tutti i dipendenti hanno formazione annuale obbligatoria? (NIS2 Art. 21.2)',
                helpText: 'Tutti i dipendenti (non solo i dirigenti) ricevono formazione annuale su phishing, password sicure, protezione dati? Con attestati?',
                type: 'select',
                options: [
                    'No - Nessuna formazione per dipendenti',
                    'Informale - Email periodiche ma no formazione strutturata',
                    'Base - Formazione annuale generica per tutti',
                    'Avanzata - Formazione obbligatoria con test di verifica',
                    'Eccellente - Formazione + simulazioni phishing + attestati + refresh trimestrale'
                ]
            }
        ]
    },
    
    risk_management: {
        title: '📈 AREA 2: Gestione del Rischio e Asset',
        subtitle: 'DORA Art. 6 / NIS2 Art. 21 / GDPR Art. 30 / AI Act Art. 9 - IT & Security',
        questions: [
            {
                id: 'unified_asset_inventory',
                label: '✅ POLICY: Inventario unificato - Include hardware, software, dati personali (GDPR) e sistemi IA?',
                helpText: 'Avete una lista completa di tutti i computer, programmi, dati e sistemi di intelligenza artificiale che usate? Tutto deve essere catalogato in un unico registro.',
                type: 'select',
                options: [
                    'No - Nessun inventario asset',
                    'Parziale - Solo inventario IT hardware',
                    'Buono - Inventario IT + software ma non dati personali/IA',
                    'Ottimo - Inventario completo IT + registro GDPR separato',
                    'Eccellente - Inventario unificato integrato (IT + dati + IA) con classificazione'
                ]
            },
            {
                id: 'ai_classification',
                label: '✅ IMPLEMENTAZIONE: I sistemi IA sono classificati per livello rischio? (AI Act Art. 6)',
                helpText: 'I sistemi di intelligenza artificiale che usate sono classificati in base a quanto sono rischiosi? (Basso, medio, alto, inaccettabile rischio).',
                type: 'select',
                options: [
                    'Non applicabile - Nessun sistema IA in uso',
                    'No - Sistemi IA presenti ma non classificati',
                    'Parziale - Classificazione informale',
                    'Sì - Classificazione formale (Rischio minimo/Limitato/Alto/Inaccettabile)',
                    'Sì - Classificazione + valutazione conformità per sistemi Alto Rischio'
                ]
            },
            {
                id: 'dpia_conducted',
                label: '✅ LOG: DPIA (Valutazione Impatto Privacy) - Eseguita per trattamenti rischiosi? (GDPR Art. 35)',
                helpText: 'Avete fatto la DPIA (Valutazione Impatto Privacy)? È un documento che spiega i rischi per la privacy quando usate dati sensibili.',
                type: 'select',
                options: [
                    'No - Mai eseguita DPIA',
                    'Parziale - DPIA eseguita ma datata (>3 anni)',
                    'Sì - DPIA eseguita per alcuni trattamenti ad alto rischio',
                    'Sì - DPIA per tutti i trattamenti ad alto rischio (ultimi 24 mesi)',
                    'Sì - DPIA aggiornate con revisione annuale e documentate'
                ]
            },
            {
                id: 'sbom_available',
                label: '✅ Software Bill of Materials (SBOM) - Disponibile per monitorare vulnerabilità? (CRA)',
                helpText: 'Avete la \'lista ingredienti\' (SBOM) di ogni software che usate? Serve per sapere se ci sono componenti vulnerabili, come controllare la scadenza del cibo.',
                type: 'select',
                options: [
                    'No - Nessun SBOM disponibile',
                    'Parziale - SBOM solo per software critico',
                    'Sì - SBOM per software sviluppato internamente',
                    'Sì - SBOM richiesto ai fornitori per software acquistato',
                    'Sì - SBOM completo con monitoraggio automatico vulnerabilità (CVE)'
                ]
            },
            {
                id: 'risk_assessment_frequency',
                label: 'Frequenza valutazione rischi ICT (DORA Art. 6 / NIS2 Art. 21)',
                helpText: 'Ogni quanto tempo controllate i rischi informatici? (Mai, una volta l\'anno, ogni 6 mesi, continuamente?).',
                type: 'select',
                options: [
                    'Mai - Nessuna valutazione rischi ICT',
                    'Ad-hoc - Solo quando richiesto',
                    'Annuale - Valutazione annuale documentata',
                    'Semestrale - Valutazione ogni 6 mesi',
                    'Continua - Monitoraggio continuo con reporting trimestrale al CdA'
                ]
            },
            {
                id: 'key_personnel_inventory',
                label: '👤 GESTIONE RISORSE UMANE: Inventario persone chiave - Mappati accessi privilegiati e competenze critiche? (NIS2 Art. 21.2)',
                helpText: 'Avete un registro di chi ha accessi da amministratore e quali persone hanno competenze critiche? (Se una persona chiave si ammala/lascia l\'azienda, sapete chi può sostituirla?).',
                type: 'select',
                options: [
                    'No - Nessun inventario persone chiave',
                    'Parziale - Solo lista admin IT generica',
                    'Buono - Registro accessi privilegiati documentato',
                    'Ottimo - Inventario completo + skills matrix + backup roles',
                    'Eccellente - Inventario + succession planning + knowledge management'
                ]
            },
            {
                id: 'continuous_improvement',
                label: '🔄 MIGLIORAMENTO CONTINUO: Ciclo PDCA sicurezza - Processo review annuale con metriche KPI? (ISO 27001 / NIS2)',
                helpText: 'Avete un processo organizzato per migliorare continuamente la sicurezza? Review annuale, KPI misurabili, azioni correttive documentate?',
                type: 'select',
                options: [
                    'No - Nessun processo di miglioramento strutturato',
                    'Informale - Miglioramenti ad-hoc senza pianificazione',
                    'Base - Review annuale ma senza KPI formali',
                    'Buono - Review annuale con KPI + piano azioni correttive',
                    'Eccellente - Ciclo PDCA completo + dashboard KPI + audit interni trimestrali'
                ]
            }
        ]
    },
    
    supply_chain: {
        title: '🤝 AREA 3: Supply Chain e Terze Parti',
        subtitle: 'DORA Art. 28-30 / NIS2 Art. 21.2(d) - Procurement & Legal',
        questions: [
            {
                id: 'ict_supplier_register',
                label: '✅ POLICY: Registro fornitori ICT - Distingue tra fornitori generici e critici? (DORA/NIS2)',
                helpText: 'Avete un registro di tutti i fornitori di tecnologia (cloud, software, hosting)? Devono essere catalogati e classificati per importanza.',
                type: 'select',
                options: [
                    'No - Nessun registro fornitori ICT',
                    'Base - Lista Excel generica',
                    'Buono - Registro con classificazione criticità',
                    'Ottimo - Registro DORA-compliant con tutti i dettagli richiesti',
                    'Eccellente - Registro integrato con risk scoring e monitoring continuo'
                ]
            },
            {
                id: 'contract_clauses_2026',
                label: '✅ IMPLEMENTAZIONE: Clausole contrattuali 2026 - Diritto audit, patch management, exit strategy?',
                helpText: 'I contratti con i fornitori tecnologici includono clausole specifiche del 2026? (Diritto a ispezionare, aggiornamenti di sicurezza, piano di uscita).',
                type: 'select',
                options: [
                    'No - Contratti standard senza clausole specifiche',
                    'Parziale - Solo alcune clausole in alcuni contratti',
                    'Buono - Clausole presenti nei nuovi contratti (post 2025)',
                    'Ottimo - Clausole in tutti contratti critici + rinegoziazione vecchi contratti',
                    'Eccellente - Clausole complete + SLA misurabili + penali definite'
                ]
            },
            {
                id: 'supplier_certifications',
                label: '✅ LOG: Certificazioni fornitori - Richieste evidenze ISO 27001, SOC 2, attestazioni NIS2?',
                helpText: 'Chiedete ai fornitori certificati che dimostrino che sono sicuri? (ISO 27001, SOC 2, ecc.) E li verificate davvero?',
                type: 'select',
                options: [
                    'No - Nessuna richiesta di certificazioni',
                    'Informale - Richieste ma non verificate',
                    'Buono - Certificazioni richieste e archiviate per fornitori critici',
                    'Ottimo - Certificazioni verificate annualmente',
                    'Eccellente - Verifiche on-site + audit di terza parte + continuous monitoring'
                ]
            },
            {
                id: 'concentration_risk',
                label: 'Gestione rischio concentrazione fornitori (DORA Art. 28.9)',
                helpText: 'Dipendete troppo da un singolo fornitore? (Es: tutto su AWS). Avete un piano B se quel fornitore ha problemi?',
                type: 'select',
                options: [
                    'No - Nessuna analisi concentrazione',
                    'Consapevole - Identificati fornitori principali ma no azioni',
                    'Documentato - Analisi concentrazione eseguita',
                    'Attivo - Strategie di mitigazione implementate',
                    'Avanzato - Limiti definiti, diversificazione, fornitori alternativi testati'
                ]
            },
            {
                id: 'subcontractor_oversight',
                label: 'Visibilità su subcontrattori di quarto livello (DORA Art. 30.3)',
                helpText: 'I vostri fornitori usano subappaltatori? Sapete chi sono e cosa fanno? Avete controllo sulla catena completa?',
                type: 'select',
                options: [
                    'No - Nessuna visibilità su subcontrattori',
                    'Parziale - Conoscenza di alcuni subcontrattori principali',
                    'Buono - Obbligo contrattuale di notifica subcontrattori',
                    'Ottimo - Diritto di approvazione per subcontrattori critici',
                    'Eccellente - Oversight completo con audit diretti su subcontrattori'
                ]
            },
            {
                id: 'exit_management',
                label: '🚪 EXIT MANAGEMENT: Offboarding - Processo revoca accessi dipendenti/fornitori che lasciano? (NIS2 Art. 21.2)',
                helpText: 'Quando un dipendente o fornitore lascia l\'azienda, avete una procedura per revocare immediatamente tutti gli accessi? (Account, badge, VPN, ecc.).',
                type: 'select',
                options: [
                    'No - Nessun processo formale di offboarding',
                    'Manuale - Revoca accessi su richiesta HR ma no checklist',
                    'Base - Checklist offboarding ma revoca non immediata',
                    'Buono - Processo documentato con revoca entro 24h',
                    'Eccellente - Revoca automatica integrata con HR + audit trimestrale account dormienti'
                ]
            },
            {
                id: 'shadow_it_control',
                label: '🔍 SHADOW IT: Controllo app/cloud non autorizzati - Sapete quali tool usano i dipendenti? (Cloud non censito = rischio)',
                helpText: 'Shadow IT = software/app che i dipendenti usano senza permesso (Dropbox personale, WhatsApp per lavoro). Li controllate o bloccate?',
                type: 'select',
                options: [
                    'No - Nessun controllo su Shadow IT',
                    'Consapevolezza - Sappiamo che esiste ma non monitoriamo',
                    'Discovery - Tool CASB/monitoring per identificare app non autorizzate',
                    'Policy - Shadow IT identificato + policy uso + formazione',
                    'Controllo totale - CASB + DLP + blocco automatico app non autorizzate'
                ]
            },
            {
                id: 'byod_policy',
                label: '📱 BYOD & IoT: Policy BYOD (Bring Your Own Device) + IoT aziendali (stampanti, telecamere, termostati smart)?',
                helpText: 'BYOD = portare il proprio telefono/PC al lavoro. Avete regole per gestire questi dispositivi personali? E i dispositivi IoT (stampanti smart, telecamere)?',
                type: 'select',
                options: [
                    'No - Nessuna policy BYOD, dispositivi personali non gestiti',
                    'Policy base - Regole scritte ma non enforced tecnicamente',
                    'MDM parziale - Mobile Device Management solo per alcuni dispositivi',
                    'MDM completo - Tutti i dispositivi BYOD gestiti + containerization',
                    'Zero Trust IoT - MDM + network segmentation + inventario IoT completo'
                ]
            }
        ]
    },
    
    incident: {
        title: '🚨 AREA 4: Incident Response e Notifiche',
        subtitle: 'NIS2 Art. 23 / DORA Art. 17-19 / GDPR Art. 33 - SOC & Compliance',
        questions: [
            {
                id: 'notification_procedure',
                label: '✅ POLICY: Piano incident response prevede notifica 24h CSIRT (NIS2), poche ore ESA (DORA), 72h Garante (GDPR)?',
                helpText: 'Se c\'è un attacco informatico, sapete esattamente a chi comunicarlo e in quanto tempo? (CSIRT entro 24h, Garante Privacy entro 72h, ecc.)',
                type: 'select',
                options: [
                    'No - Nessun piano di notifica multicanale',
                    'Parziale - Piano generico senza tempistiche specifiche',
                    'Buono - Piano documenta i diversi obblighi ma non testato',
                    'Ottimo - Piano documentato e testato annualmente',
                    'Eccellente - Piano testato con simulazioni, procedure automatizzate, template pre-approvati'
                ]
            },
            {
                id: 'severity_classification',
                label: '✅ IMPLEMENTAZIONE: Criteri classificazione gravità - Quando incidente è "significativo" vs "grave" vs "violazione dati"?',
                helpText: 'Come decidete se un incidente è \'grave\' o \'molto grave\'? Servono criteri chiari scritti per non sbagliare le notifiche alle autorità.',
                type: 'select',
                options: [
                    'No - Nessun criterio di classificazione',
                    'Generico - Classificazione soggettiva caso per caso',
                    'Definito - Criteri scritti ma non allineati a NIS2/DORA/GDPR',
                    'Allineato - Criteri conformi alle soglie normative',
                    'Avanzato - Criteri dettagliati + decision tree + classificazione automatica via SIEM'
                ]
            },
            {
                id: 'emergency_channels',
                label: '✅ LOG: Canali comunicazione emergenza - Sistemi protetti fuori rete aziendale per gestire crisi?',
                helpText: 'Se la rete aziendale è compromessa, come comunicate durante la crisi? Avete telefoni dedicati, app criptate tipo Signal, sistemi fuori dalla rete?',
                type: 'select',
                options: [
                    'No - Solo email aziendale',
                    'Parziale - Telefoni cellulari ma no processo formale',
                    'Buono - Canali alternativi identificati (es. Signal, telefono dedicato)',
                    'Ottimo - Sistema di crisis communication out-of-band testato',
                    'Eccellente - Sistema ridondante + crittografato + testato trimestralmente'
                ]
            },
            {
                id: 'incident_reporting_log',
                label: 'Registro incidenti di sicurezza - Mantiene storico con analisi root cause? (NIS2 Art. 23)',
                helpText: 'Tenete un registro di tutti gli incidenti di sicurezza con analisi delle cause? Serve per imparare dagli errori e dimostrare agli auditor.',
                type: 'select',
                options: [
                    'No - Nessun registro incidenti',
                    'Informale - Incidenti tracciati in ticket generici',
                    'Base - Registro incidenti dedicato',
                    'Buono - Registro con root cause analysis per incidenti significativi',
                    'Eccellente - Registro completo + lessons learned + KPI trending + reporting al CdA'
                ]
            },
            {
                id: 'simulation_exercises',
                label: 'Esercitazioni e simulazioni cyber crisis (NIS2 Art. 21.2(h))',
                helpText: 'Fate prove di emergenza informatica? (Come le prove antincendio). Simulate attacchi ransomware per vedere se le procedure funzionano?',
                type: 'select',
                options: [
                    'Mai - Nessuna esercitazione',
                    'Ad-hoc - Solo quando richiesto',
                    'Annuale - Tabletop exercise annuale',
                    'Semestrale - Esercitazioni ogni 6 mesi con report',
                    'Trimestrale - Simulazioni avanzate (Red Team) + reporting al CdA'
                ]
            },
            {
                id: 'digital_forensics_capability',
                label: '🔬 DIGITAL FORENSICS: Capacità investigative - Potete preservare prove digitali senza inquinare i log?',
                helpText: 'Se c\'è un attacco, sapete preservare le prove digitali senza inquinare i log? Serve un team con certificazioni forensi e strumenti appositi.',
                type: 'select',
                options: [
                    'No - Nessuna capacità forense',
                    'Base - Team IT sa fare backup ma senza chain of custody',
                    'Procedure - Procedure forensi documentate + tool base',
                    'Team dedicato - Team interno con certificazioni (GCFA, EnCE)',
                    'Eccellenza forense - Team + write-blockers + chain of custody + partnership con forenser esterni'
                ]
            }
        ]
    },
    
    technical: {
        title: '⚙️ AREA 5: Misure Tecniche e Cyber Hygiene',
        subtitle: 'NIS2 Art. 21.2 / DORA Art. 9 / CRA - IT Operations',
        questions: [
            {
                id: 'mfa_zerotrust',
                label: '✅ POLICY: MFA (Autenticazione a due fattori) + Zero Trust - Attivi su tutti accessi?',
                helpText: 'MFA = doppia verifica per accedere (password + codice SMS/app). Zero Trust = non fidarsi mai, verificare sempre. Usati ovunque?',
                type: 'select',
                options: [
                    'No - Nessuna MFA implementata',
                    'Parziale - MFA solo per VPN o admin',
                    'Buono - MFA per tutti gli utenti, ma no Zero Trust',
                    'Ottimo - MFA universale + principi Zero Trust in implementazione',
                    'Eccellente - MFA phishing-resistant (FIDO2) + Zero Trust completo'
                ]
            },
            {
                id: 'encryption',
                label: '✅ IMPLEMENTAZIONE: Crittografia - Dati sensibili cifrati "at rest" e "in transit"? (GDPR/NIS2)',
                helpText: 'Crittografia = cifrare i dati così nessuno li può leggere se rubati. I dati sono cifrati sia quando viaggiano in rete che quando sono salvati sui dischi?',
                type: 'select',
                options: [
                    'No - Nessuna crittografia sistematica',
                    'Parziale - Solo dati in transito (HTTPS)',
                    'Buono - Crittografia at rest per database critici',
                    'Ottimo - Crittografia at rest e in transit per tutti dati sensibili',
                    'Eccellente - Crittografia end-to-end + key management HSM + rotazione chiavi'
                ]
            },
            {
                id: 'vulnerability_management',
                label: '✅ LOG: Vulnerability Management - Processo automatizzato per scan e patch entro tempi certi? (CRA/NIS2)',
                helpText: 'Cercate regolarmente le falle nei sistemi (scan vulnerabilità) e le correggete velocemente con le patch? Entro quanti giorni?',
                type: 'select',
                options: [
                    'No - Nessun processo vulnerability management',
                    'Manuale - Scan manuali sporadici',
                    'Base - Scan mensili con patching best-effort',
                    'Buono - Scan settimanali + patching critico <30 giorni',
                    'Eccellente - Scan continui + patching critico <7 giorni + metriche SLA'
                ]
            },
            {
                id: 'patch_management_sla',
                label: '⏱️ PATCH MANAGEMENT SLA: Tempi massimi applicazione patch - SLA documentati per vulnerabilità critiche? (NIS2 Art. 21.2)',
                helpText: 'Avete tempi massimi scritti per applicare le patch di sicurezza? (Es: vulnerabilità critiche entro 7 giorni). Con penali se non rispettate?',
                type: 'select',
                options: [
                    'No - Nessun SLA definito per patching',
                    'Informale - Best effort ma no tempi garantiti',
                    'Base - SLA generici (es. "entro 30 giorni")',
                    'Buono - SLA differenziati per criticità (7/15/30 giorni)',
                    'Eccellente - SLA stringenti + dashboard tempo medio patch + escalation automatica'
                ]
            },
            {
                id: 'immutable_backups',
                label: '✅ Business Continuity - Backup immutabili (anti-ransomware) e testati?',
                helpText: 'I backup sono \'immutabili\' (impossibili da modificare/cancellare dai ransomware)? E li testate per vedere se funzionano davvero?',
                type: 'select',
                options: [
                    'No - Nessun backup o backup non protetti',
                    'Base - Backup regolari ma non immutabili',
                    'Buono - Backup immutabili (WORM) ma non testati',
                    'Ottimo - Backup immutabili testati semestralmente',
                    'Eccellente - Backup immutabili + air-gapped + test mensili + RTO documentati'
                ]
            },
            {
                id: 'network_segmentation',
                label: 'Segmentazione rete e microsegmentation (NIS2 Art. 21.2)',
                helpText: 'La rete è divisa in zone separate (produzione, uffici, ospiti)? Come compartimenti stagni su una nave: se uno allaga, gli altri restano asciutti.',
                type: 'select',
                options: [
                    'No - Rete piatta senza segmentazione',
                    'Base - VLAN di base per separare reti',
                    'Buono - Segmentazione per zone (DMZ, produzione, uffici)',
                    'Ottimo - Microsegmentazione con firewall interni',
                    'Eccellente - Microsegmentazione software-defined + Zero Trust network'
                ]
            },
            {
                id: 'logging_monitoring',
                label: 'Logging centralizzato e SIEM (NIS2 Art. 21 / DORA Art. 17)',
                helpText: 'Tutti i log (registrazioni attività) sono raccolti in un sistema centrale (SIEM) che li analizza 24/7 per trovare anomalie?',
                type: 'select',
                options: [
                    'No - Log locali non centralizzati',
                    'Parziale - Log aggregati ma no SIEM',
                    'Buono - SIEM implementato per sistemi critici',
                    'Ottimo - SIEM enterprise con retention 18+ mesi',
                    'Eccellente - SIEM + SOAR + threat intelligence + 24/7 SOC'
                ]
            },
            {
                id: 'physical_security',
                label: '🏢 PHYSICAL SECURITY: Accesso data center/server room - Log accessi fisici? Badge? Telecamere? (spesso dimenticato!)',
                helpText: 'Chi entra nelle stanze server? C\'è controllo accessi fisico con badge, telecamere, registri? Un intruso fisico può fare danni quanto un hacker.',
                type: 'select',
                options: [
                    'No - Nessun controllo accessi fisici',
                    'Base - Stanze chiuse a chiave ma senza log',
                    'Buono - Badge elettronici con log accessi',
                    'Ottimo - Badge + videosorveglianza + log correlati',
                    'Eccellente - Biometria + mantrap + monitoraggio H24 + procedure visitatori'
                ]
            },
            {
                id: 'environmental_controls',
                label: '🌡️ ENVIRONMENTAL: Protezione disastri naturali - Antincendio, anti-allagamento, UPS, generatori?',
                helpText: 'Le sale server sono protette da incendi, allagamenti, blackout? (Sistemi anti-incendio, UPS, generatori di emergenza, aria condizionata).',
                type: 'select',
                options: [
                    'No - Nessuna protezione ambientale',
                    'Minima - Solo UPS base',
                    'Buona - UPS + rilevazione incendi + estintori',
                    'Ottima - UPS + generatori + soppressione incendi + clima controllato',
                    'Eccellente - Ridondanza geografica + dual power feed + monitoraggio ambientale H24'
                ]
            },
            {
                id: 'business_continuity_rto',
                label: '⚡ DOMANDA KILLER: Se stacchiamo Internet OGGI, tra quanto tempo l\'azienda smette di fatturare? (RTO reale)',
                helpText: '🔥 DOMANDA KILLER: RTO = Recovery Time Objective = tempo massimo di fermo. Se oggi cade Internet, quanto resiste il business prima di fermarsi?',
                type: 'select',
                options: [
                    'Immediatamente - Business si ferma subito',
                    'Poche ore - Possiamo lavorare 2-4 ore poi stop',
                    '1 giorno - Abbiamo procedure manuali per 24h',
                    '2-3 giorni - DR site attivabile in 48-72h',
                    'Mai - Hot standby/active-active, failover automatico <1h'
                ]
            }
        ]
    },
    
    ai_ethics: {
        title: '🤖 AREA 6: Intelligenza Artificiale ed Etica',
        subtitle: 'AI Act - Data Science & Compliance',
        questions: [
            {
                id: 'ai_systems_in_use',
                label: 'Sistemi IA attualmente in uso nell\'organizzazione',
                helpText: 'Quali sistemi di intelligenza artificiale usate? (Chatbot, riconoscimento facciale, decisioni automatiche, GPT, ecc.).',
                type: 'checkbox',
                options: [
                    'Nessun sistema IA in uso',
                    'Chatbot e assistenti virtuali',
                    'Sistemi di riconoscimento biometrico (volto, voce, impronte)',
                    'Sistemi di recruiting o valutazione HR',
                    'Sistemi di credit scoring o valutazione rischio finanziario',
                    'Sistemi di analisi predittiva per decisioni automatizzate',
                    'Sistemi di sorveglianza o sicurezza',
                    'IA per diagnostica medica o healthcare',
                    'IA generativa (GPT, LLM, generazione immagini)',
                    'Sistemi di automazione processi (RPA con ML)'
                ]
            },
            {
                id: 'ai_transparency',
                label: '✅ POLICY: Trasparenza IA - Gli utenti sanno quando interagiscono con IA? (AI Act Art. 52)',
                helpText: 'Quando una persona parla con un\'IA, sa che sta parlando con una macchina e non con un umano? Deve essere comunicato chiaramente.',
                type: 'select',
                options: [
                    'Non applicabile - Nessun sistema IA rivolto a utenti',
                    'No - Nessuna disclosure agli utenti',
                    'Parziale - Disclosure in privacy policy ma non evidente',
                    'Sì - Notifica chiara all\'avvio interazione (es. "Chatbot IA")',
                    'Sì - Disclosure + spiegazione capacità e limitazioni + opt-out disponibile'
                ]
            },
            {
                id: 'training_data_quality',
                label: '✅ IMPLEMENTAZIONE: Qualità dati addestramento - Dati privi di bias e conformi GDPR? (AI Act Art. 10)',
                helpText: 'I dati usati per addestrare l\'IA sono di buona qualità e senza pregiudizi (bias)? Se addestri un\'IA con dati sbagliati, darà risposte sbagliate.',
                type: 'select',
                options: [
                    'Non applicabile - Solo IA di terze parti pre-addestrate',
                    'No - Nessuna analisi qualità/bias dati',
                    'Parziale - Analisi qualità dati ma no verifica bias',
                    'Buono - Data quality check + analisi bias documentata',
                    'Eccellente - Data governance completa + bias testing + audit trail + conformità GDPR'
                ]
            },
            {
                id: 'human_oversight',
                label: '✅ LOG: Sorveglianza umana - Garantito intervento umano per decisioni IA ad alto rischio? (AI Act Art. 14)',
                helpText: 'Per decisioni importanti prese dall\'IA (assunzioni, prestiti, diagnosi), c\'è sempre un umano che controlla e può intervenire?',
                type: 'select',
                options: [
                    'Non applicabile - Nessun sistema IA ad alto rischio',
                    'No - Sistemi completamente automatizzati',
                    'Parziale - Revisione umana solo su richiesta',
                    'Sì - Human-in-the-loop per tutte decisioni significative',
                    'Sì - Human oversight + diritto contestazione + log decisioni + audit trail'
                ]
            },
            {
                id: 'ai_risk_assessment',
                label: 'Valutazione rischi sistemi IA ad alto rischio (AI Act Art. 9)',
                helpText: 'I sistemi di IA ad alto rischio (es: assumere personale, dare prestiti) sono stati valutati formalmente per i rischi e documentati?',
                type: 'select',
                options: [
                    'Non applicabile - Nessun sistema alto rischio',
                    'No - Sistemi alto rischio non valutati',
                    'In corso - Valutazione in preparazione',
                    'Sì - Valutazione conformità eseguita e documentata',
                    'Sì - Valutazione + test + documentazione tecnica + dichiarazione conformità UE'
                ]
            },
            {
                id: 'ai_documentation',
                label: 'Documentazione tecnica sistemi IA (AI Act Art. 11)',
                helpText: 'Avete documentazione tecnica completa dei sistemi IA? Come funzionano, con quali dati, quanto sono accurati, quali errori possono fare?',
                type: 'select',
                options: [
                    'No - Nessuna documentazione tecnica IA',
                    'Minima - Documentazione di base dai fornitori',
                    'Parziale - Documentazione per alcuni sistemi critici',
                    'Buona - Documentazione dettagliata per tutti sistemi IA',
                    'Completa - Doc tecnica + log decisioni + accuratezza + bias testing + update procedure'
                ]
            }
        ]
    }
};

// Scoring functions
function assessGovernance(data) {
    let score = 20;
    let findings = [];
    let recs = [];
    let gaps = [];

    // Board approval
    if (!data.board_approval || data.board_approval.includes('Nessuna approvazione')) {
        score -= 5;
        findings.push("CdA non ha approvato formalmente il piano di conformità 2026");
        gaps.push("NIS2 Art. 20 / DORA Art. 5: Accountability del management body richiesta");
        recs.push("CRITICO: Ottenere approvazione formale del CdA per il piano di conformità con delibera documentata");
    } else if (data.board_approval.includes('Parziale') || data.board_approval.includes('datato')) {
        score -= 3;
        recs.push("Aggiornare piano di conformità e ottenere nuova approvazione CdA");
    }

    // Executive training
    if (!data.executive_training || data.executive_training.includes('Nessuna formazione')) {
        score -= 4;
        findings.push("Vertici aziendali non hanno ricevuto formazione su cybersecurity e IA");
        gaps.push("NIS2 Art. 20.2(a): Formazione del management body obbligatoria");
        recs.push("Organizzare formazione certificata per il CdA su cyber risks e regolamentazione IA");
    } else if (data.executive_training.includes('Informale')) {
        score -= 2;
        recs.push("Formalizzare la formazione dei vertici con attestati e test di verifica");
    }

    // Model 231
    if (!data.model_231_updated || data.model_231_updated.includes('non presente') || data.model_231_updated.includes('mai aggiornato')) {
        score -= 4;
        findings.push("Modello Organizzativo 231 non aggiornato per reati informatici e AI Act");
        gaps.push("D.Lgs. 231/2001: Modello deve includere nuovi reati cyber e violazioni AI Act");
        recs.push("Aggiornare Modello 231 includendo protocolli per prevenzione reati informatici e violazioni AI");
    }

    // Roles assigned
    if (!data.roles_assigned || data.roles_assigned.includes('Nessuna nomina')) {
        score -= 5;
        findings.push("CISO, DPO e Responsabile IA non formalmente nominati");
        gaps.push("NIS2/DORA/GDPR/AI Act: Ruoli chiave devono essere formalmente designati");
        recs.push("CRITICO: Nominare formalmente CISO, DPO e Responsabile sorveglianza IA con lettera di incarico");
    } else if (data.roles_assigned.includes('Parziale') || data.roles_assigned.includes('Solo DPO')) {
        score -= 3;
        recs.push("Completare le nomine mancanti (CISO, Responsabile IA) con reporting line al CdA");
    }

    // Organization scope check
    if (data.scope && data.scope.length === 0) {
        score -= 2;
        gaps.push("Ambito normativo non identificato - verificare applicabilità NIS2/DORA/AI Act");
    }
    
    // ISO 27001 compliance (NEW - 3 pts)
    if (!data.iso_27001_compliance || data.iso_27001_compliance.includes('Nessun SGSI')) {
        score -= 3;
        findings.push("Manca Sistema di Gestione Sicurezza Informazioni (SGSI) secondo ISO 27001");
        gaps.push("ISO 27001: Standard mondiale per SGSI - fondamentale per audit strutturato");
        recs.push("CRITICO: Implementare SGSI conforme ISO 27001:2022 come base per conformità NIS2/DORA");
    } else if (data.iso_27001_compliance.includes('In preparazione') || data.iso_27001_compliance.includes('informale')) {
        score -= 2;
        recs.push("Completare implementazione SGSI e considerare certificazione ISO 27001 per maggiore credibilità");
    } else if (data.iso_27001_compliance.includes('non certificato')) {
        score -= 1;
        recs.push("Considerare certificazione ISO 27001 da ente accreditato per validazione esterna");
    }
    
    // NIST CSF adoption (NEW - 2 pts)
    if (!data.nist_csf_adoption || data.nist_csf_adoption.includes('non mappate')) {
        score -= 2;
        findings.push("Funzioni NIST CSF 2.0 non mappate - manca framework operativo");
        gaps.push("NIST CSF: Best practice per mappare Govern/Identify/Protect/Detect/Respond/Recover");
        recs.push("Mappare controlli esistenti alle 6 funzioni NIST CSF 2.0 per gap analysis strutturata");
    } else if (data.nist_csf_adoption.includes('Conoscenza') || data.nist_csf_adoption.includes('Parziale')) {
        score -= 1;
        recs.push("Completare mapping NIST CSF e integrare con metriche KPI per misurare maturità");
    }
    
    // Security policies catalog (NEW - 2 pts)
    if (!data.security_policies_catalog || data.security_policies_catalog.includes('Nessuna policy')) {
        score -= 2;
        findings.push("Manca catalogo policy di sicurezza formalmente approvate");
        gaps.push("NIS2 Art. 21.2: Politiche di sicurezza devono essere documentate e approvate");
        recs.push("CRITICO: Creare catalogo policy scritte (password, accessi, backup, etc) con approvazione CdA");
    } else if (data.security_policies_catalog.includes('Parziale') || data.security_policies_catalog.includes('non tutte approvate')) {
        score -= 1;
        recs.push("Completare approvazione formale di tutte le policy e implementare review annuale");
    }
    
    // Employee security training (NEW - 2 pts)
    if (!data.employee_security_training || data.employee_security_training.includes('Nessuna formazione')) {
        score -= 2;
        findings.push("Dipendenti non ricevono formazione security awareness obbligatoria");
        gaps.push("NIS2 Art. 21.2(g): Training awareness per tutti i dipendenti obbligatorio");
        recs.push("CRITICO: Implementare programma formazione annuale obbligatoria per tutti con test e attestati");
    } else if (data.employee_security_training.includes('Informale')) {
        score -= 1;
        recs.push("Formalizzare training con piattaforma e-learning, test verifica e attestati tracciabili");
    }

    return { score, findings, recs, gaps };
}

function assessRiskManagement(data) {
    let score = 19;
    let findings = [];
    let recs = [];
    let gaps = [];

    // Unified asset inventory
    if (!data.unified_asset_inventory || data.unified_asset_inventory.includes('Nessun inventario')) {
        score -= 4;
        findings.push("Assenza inventario unificato asset ICT, dati personali e sistemi IA");
        gaps.push("DORA Art. 8 / NIS2 Art. 21 / GDPR Art. 30: Registro asset obbligatorio");
        recs.push("CRITICO: Creare inventario unificato che integra asset IT, registro GDPR e sistemi IA");
    } else if (data.unified_asset_inventory.includes('Parziale') || data.unified_asset_inventory.includes('solo inventario IT')) {
        score -= 2;
        recs.push("Completare inventario includendo mappatura dati personali e sistemi IA");
    }

    // AI classification
    if (data.ai_classification && data.ai_classification.includes('presenti ma non classificati')) {
        score -= 3;
        findings.push("Sistemi IA in uso non classificati per livello di rischio");
        gaps.push("AI Act Art. 6: Classificazione sistemi IA per livello rischio obbligatoria");
        recs.push("Eseguire classificazione formale sistemi IA secondo AI Act (Minimo/Limitato/Alto/Inaccettabile)");
    } else if (data.ai_classification && data.ai_classification.includes('Parziale')) {
        score -= 1;
        recs.push("Formalizzare classificazione IA e condurre valutazione conformità per sistemi Alto Rischio");
    }

    // DPIA conducted
    if (!data.dpia_conducted || data.dpia_conducted.includes('Mai eseguita')) {
        score -= 4;
        findings.push("DPIA (Data Protection Impact Assessment) mai eseguita");
        gaps.push("GDPR Art. 35: DPIA obbligatoria per trattamenti ad alto rischio");
        recs.push("Eseguire DPIA per tutti i trattamenti ad alto rischio e sistemi IA che trattano dati personali");
    } else if (data.dpia_conducted.includes('datata')) {
        score -= 2;
        recs.push("Aggiornare le DPIA esistenti (raccomandato ogni 2-3 anni o al cambio sostanziale)");
    }

    // SBOM availability
    if (!data.sbom_available || data.sbom_available.includes('Nessun SBOM')) {
        score -= 2;
        findings.push("Software Bill of Materials (SBOM) non disponibile");
        gaps.push("Cyber Resilience Act: SBOM richiesto per monitoraggio vulnerabilità");
        recs.push("Richiedere SBOM a tutti fornitori software e creare SBOM per sviluppi interni");
    } else if (data.sbom_available.includes('Parziale')) {
        score -= 1;
        recs.push("Estendere SBOM a tutti i componenti software e attivare monitoraggio CVE automatico");
    }

    // Risk assessment frequency
    if (data.risk_assessment_frequency && data.risk_assessment_frequency.includes('Mai')) {
        score -= 2;
        findings.push("Valutazione rischi ICT mai eseguita");
        gaps.push("DORA Art. 6 / NIS2 Art. 21: Valutazione rischi ICT periodica obbligatoria");
        recs.push("Implementare processo di risk assessment ICT con frequenza almeno annuale");
    }
    
    // Key personnel inventory (NEW - 2 pts)
    if (!data.key_personnel_inventory || data.key_personnel_inventory.includes('Nessun inventario')) {
        score -= 2;
        findings.push("Manca inventario persone chiave con accessi privilegiati");
        gaps.push("NIS2 Art. 21.2: Gestione risorse umane deve includere mapping competenze critiche");
        recs.push("CRITICO: Mappare accessi amministratori e competenze critiche + backup roles");
    } else if (data.key_personnel_inventory.includes('Parziale') || data.key_personnel_inventory.includes('generica')) {
        score -= 1;
        recs.push("Completare inventario con skills matrix e succession planning per ruoli critici");
    }
    
    // Continuous improvement (NEW - 2 pts)
    if (!data.continuous_improvement || data.continuous_improvement.includes('Nessun processo')) {
        score -= 2;
        findings.push("Manca processo strutturato di miglioramento continuo");
        gaps.push("ISO 27001 / NIS2: Ciclo PDCA con KPI e azioni correttive obbligatorio");
        recs.push("Implementare ciclo PDCA con review annuale, KPI sicurezza e audit interni");
    } else if (data.continuous_improvement.includes('Informale') || data.continuous_improvement.includes('senza KPI')) {
        score -= 1;
        recs.push("Formalizzare processo miglioramento con KPI misurabili e dashboard executive");
    }

    return { score, findings, recs, gaps };
}

function assessSupplyChain(data) {
    let score = 22;
    let findings = [];
    let recs = [];
    let gaps = [];

    // ICT supplier register
    if (!data.ict_supplier_register || data.ict_supplier_register.includes('Nessun registro')) {
        score -= 4;
        findings.push("Registro fornitori ICT assente");
        gaps.push("DORA Art. 28.1: Registro fornitori ICT terzi obbligatorio");
        recs.push("CRITICO: Creare registro fornitori ICT con classificazione criticità secondo DORA");
    } else if (data.ict_supplier_register.includes('Lista Excel')) {
        score -= 2;
        recs.push("Formalizzare registro fornitori con tutti i campi DORA (contratti, SLA, criticality, dependencies)");
    }

    // Contract clauses 2026
    if (!data.contract_clauses_2026 || data.contract_clauses_2026.includes('standard senza clausole')) {
        score -= 4;
        findings.push("Contratti fornitori ICT privi clausole DORA/NIS2 2026");
        gaps.push("DORA Art. 30: Clausole contrattuali specifiche obbligatorie");
        recs.push("CRITICO: Aggiornare contratti con clausole audit, incident notification, exit strategy, patch SLA");
    } else if (data.contract_clauses_2026.includes('Parziale')) {
        score -= 2;
        recs.push("Completare rinegoziazione contratti esistenti per includere tutte le clausole DORA/NIS2");
    }

    // Supplier certifications
    if (!data.supplier_certifications || data.supplier_certifications.includes('Nessuna richiesta')) {
        score -= 3;
        findings.push("Certificazioni di sicurezza fornitori non richieste");
        gaps.push("DORA Art. 30.2(f): Evidenza conformità fornitori richiesta");
        recs.push("Richiedere certificazioni ISO 27001, SOC 2 Type II o attestazioni conformità NIS2 a fornitori critici");
    } else if (data.supplier_certifications.includes('non verificate')) {
        score -= 1;
        recs.push("Implementare processo verifica annuale certificazioni fornitori");
    }

    // Concentration risk
    if (data.concentration_risk && data.concentration_risk.includes('Nessuna analisi')) {
        score -= 2;
        findings.push("Rischio concentrazione fornitori non analizzato");
        gaps.push("DORA Art. 28.9: Gestione rischio concentrazione ICT obbligatoria");
        recs.push("Condurre analisi concentrazione fornitori e definire strategie mitigazione");
    }

    // Subcontractor oversight
    if (data.subcontractor_oversight && data.subcontractor_oversight.includes('Nessuna visibilità')) {
        score -= 2;
        findings.push("Nessuna visibilità su subcontrattori fornitori ICT");
        gaps.push("DORA Art. 30.3: Oversight su subcontrattori richiesto");
        recs.push("Inserire clausola obbligo notifica e approvazione subcontrattori critici");
    }
    
    // Exit management (NEW - 2 pts)
    if (!data.exit_management || data.exit_management.includes('Nessun processo')) {
        score -= 2;
        findings.push("Manca processo offboarding - rischio accessi non revocati");
        gaps.push("NIS2 Art. 21.2(f): Gestione accessi deve includere revoca immediata alla cessazione");
        recs.push("CRITICO: Implementare checklist offboarding con revoca accessi entro 24h + audit account dormienti");
    } else if (data.exit_management.includes('Manuale') || data.exit_management.includes('no checklist')) {
        score -= 1;
        recs.push("Automatizzare revoca accessi integrandola con sistema HR + alert account inattivi >90 giorni");
    }
    
    // Shadow IT control (NEW - 3 pts)
    if (!data.shadow_it_control || data.shadow_it_control.includes('Nessun controllo')) {
        score -= 3;
        findings.push("Shadow IT non controllato - dipendenti usano app/cloud non autorizzati");
        gaps.push("NIS2/DORA/GDPR: Cloud non censito = rischio data breach e violazione contratti");
        recs.push("CRITICO: Implementare CASB (Cloud Access Security Broker) per discovery e controllo Shadow IT");
    } else if (data.shadow_it_control.includes('Consapevolezza') || data.shadow_it_control.includes('Discovery')) {
        score -= 2;
        recs.push("Implementare policy uso cloud + DLP (Data Loss Prevention) + formazione utenti su rischi Shadow IT");
    } else if (data.shadow_it_control.includes('Policy')) {
        score -= 1;
        recs.push("Aggiungere enforcement automatico con blocco app non autorizzate via CASB/proxy");
    }
    
    // BYOD and IoT policy (NEW - 2 pts)
    if (!data.byod_policy || data.byod_policy.includes('Nessuna policy')) {
        score -= 2;
        findings.push("Dispositivi personali (BYOD) e IoT aziendali non gestiti");
        gaps.push("NIS2/CRA: Stampanti, telecamere, termostati smart = attack vector comune");
        recs.push("Implementare MDM (Mobile Device Management) per BYOD + inventario IoT + network segmentation");
    } else if (data.byod_policy.includes('Policy base') || data.byod_policy.includes('MDM parziale')) {
        score -= 1;
        recs.push("Estendere MDM a tutti dispositivi + containerization dati aziendali + policy wipe remoto");
    }

    return { score, findings, recs, gaps };
}

function assessIncidentResponse(data) {
    let score = 15;
    let findings = [];
    let recs = [];
    let gaps = [];

    // Notification procedure
    if (!data.notification_procedure || data.notification_procedure.includes('Nessun piano')) {
        score -= 5;
        findings.push("Piano notifica incidenti multicanale (NIS2/DORA/GDPR) assente");
        gaps.push("NIS2 Art. 23 / DORA Art. 19 / GDPR Art. 33: Procedure notifica specifiche obbligatorie");
        recs.push("CRITICO: Creare piano incident response con tempistiche notifica: 24h CSIRT, 2-4h ESA, 72h Garante");
    } else if (data.notification_procedure.includes('generico')) {
        score -= 3;
        recs.push("Dettagliare piano notifica con tempistiche specifiche per ogni autorità e testarlo");
    } else if (data.notification_procedure.includes('non testato')) {
        score -= 1;
        recs.push("Testare piano notifica con simulazione completa almeno annualmente");
    }

    // Severity classification
    if (!data.severity_classification || data.severity_classification.includes('Nessun criterio')) {
        score -= 3;
        findings.push("Criteri classificazione gravità incidenti non definiti");
        gaps.push("NIS2 Art. 23.3: Criteri identificazione incidenti significativi richiesti");
        recs.push("Definire criteri oggettivi classificazione incidenti allineati a soglie NIS2/DORA/GDPR");
    } else if (data.severity_classification.includes('soggettiva')) {
        score -= 2;
        recs.push("Formalizzare criteri classificazione con decision tree e soglie quantitative");
    }

    // Emergency channels
    if (!data.emergency_channels || data.emergency_channels.includes('Solo email')) {
        score -= 3;
        findings.push("Canali comunicazione emergenza inadeguati (solo email aziendale)");
        gaps.push("Best practice NIS2: Canali out-of-band per crisis management");
        recs.push("Implementare sistema comunicazione crisi out-of-band (es. Signal, telefoni dedicati)");
    } else if (data.emergency_channels.includes('no processo')) {
        score -= 1;
        recs.push("Formalizzare processo utilizzo canali emergenza e testare trimestralmente");
    }

    // Incident reporting log
    if (data.incident_reporting_log && data.incident_reporting_log.includes('Nessun registro')) {
        score -= 2;
        findings.push("Registro incidenti di sicurezza non mantenuto");
        gaps.push("NIS2 Art. 23: Documentazione incidenti obbligatoria");
        recs.push("Creare registro incidenti con root cause analysis e lessons learned");
    }

    // Simulation exercises
    if (data.simulation_exercises && data.simulation_exercises.includes('Mai')) {
        score -= 2;
        findings.push("Nessuna esercitazione cyber crisis mai condotta");
        gaps.push("NIS2 Art. 21.2(h): Testing resilienza ICT obbligatorio");
        recs.push("Pianificare esercitazioni tabletop almeno annuali per test piano incident response");
    }
    
    // Digital forensics capability (NEW - 3 pts)
    if (!data.digital_forensics_capability || data.digital_forensics_capability.includes('Nessuna capacità')) {
        score -= 3;
        findings.push("Nessuna capacità di digital forensics per preservare prove");
        gaps.push("NIS2/DORA: Se hackerati, autorità chiederanno le prove - necessaria chain of custody");
        recs.push("CRITICO: Formare team su digital forensics + acquisire write-blockers + definire chain of custody");
    } else if (data.digital_forensics_capability.includes('Base') || data.digital_forensics_capability.includes('Procedure')) {
        score -= 2;
        recs.push("Certificare team (GCFA, EnCE) e stabilire partnership con forensi esterni per casi complessi");
    } else if (data.digital_forensics_capability.includes('Team dedicato')) {
        score -= 1;
        recs.push("Aggiungere tool avanzati (Encase, FTK, X-Ways) e procedure automated evidence collection");
    }

    return { score, findings, recs, gaps };
}

function assessTechnicalMeasures(data) {
    let score = 25;  // Aumentato da 20 a 25 per includere Physical + Environmental + BC
    let findings = [];
    let recs = [];
    let gaps = [];

    // MFA and Zero Trust
    if (!data.mfa_zerotrust || data.mfa_zerotrust.includes('Nessuna MFA')) {
        score -= 5;
        findings.push("Multi-Factor Authentication (MFA) non implementata");
        gaps.push("NIS2 Art. 21.2(b): MFA obbligatoria per accessi ICT");
        recs.push("CRITICO: Implementare MFA per tutti gli utenti, priorità account privilegiati e accessi remoti");
    } else if (data.mfa_zerotrust.includes('solo per VPN')) {
        score -= 3;
        recs.push("Estendere MFA a tutti i servizi e iniziare implementazione Zero Trust architecture");
    } else if (data.mfa_zerotrust.includes('no Zero Trust')) {
        score -= 1;
        recs.push("Completare implementazione Zero Trust con microsegmentazione e least privilege");
    }

    // Encryption
    if (!data.encryption || data.encryption.includes('Nessuna crittografia')) {
        score -= 4;
        findings.push("Crittografia dati sensibili non implementata");
        gaps.push("GDPR Art. 32 / NIS2 Art. 21.2(c): Cifratura dati obbligatoria");
        recs.push("CRITICO: Implementare cifratura at-rest per database e at-transit per tutte comunicazioni");
    } else if (data.encryption.includes('Parziale')) {
        score -= 2;
        recs.push("Estendere crittografia a tutti i dati sensibili con key management centralizzato");
    } else if (data.encryption.includes('Buono')) {
        score -= 1;
        recs.push("Implementare key management con HSM e rotazione automatica chiavi");
    }

    // Vulnerability management
    if (!data.vulnerability_management || data.vulnerability_management.includes('Nessun processo')) {
        score -= 5;
        findings.push("Vulnerability e patch management non implementato");
        gaps.push("NIS2 Art. 21.2(a) / CRA: Gestione vulnerabilità sistematica obbligatoria");
        recs.push("CRITICO: Implementare vulnerability scanning continuo e patch management con SLA <30 giorni per critical");
    } else if (data.vulnerability_management.includes('Manuale')) {
        score -= 3;
        recs.push("Automatizzare vulnerability scanning e patch deployment");
    } else if (data.vulnerability_management.includes('Base')) {
        score -= 1;
        recs.push("Ridurre SLA patching critico a <7 giorni e implementare metriche compliance");
    }
    
    // Patch management SLA (NEW - 2 pts)
    if (!data.patch_management_sla || data.patch_management_sla.includes('Nessun SLA')) {
        score -= 2;
        findings.push("Mancano SLA definiti per applicazione patch di sicurezza");
        gaps.push("NIS2 Art. 21.2(a): Patch management con tempi definiti obbligatorio");
        recs.push("CRITICO: Definire SLA patch per criticità (7 giorni critical, 15 high, 30 medium) con escalation");
    } else if (data.patch_management_sla.includes('Informale') || data.patch_management_sla.includes('generici')) {
        score -= 1;
        recs.push("Stringere SLA patch critiche e implementare dashboard tempo medio patching");
    }

    // Immutable backups
    if (!data.immutable_backups || data.immutable_backups.includes('Nessun backup') || data.immutable_backups.includes('non protetti')) {
        score -= 4;
        findings.push("Backup immutabili anti-ransomware non implementati");
        gaps.push("NIS2 Art. 21.3 / DORA Art. 12: Backup sicuri e testati obbligatori");
        recs.push("CRITICO: Implementare backup immutabili (WORM) con test restore mensili");
    } else if (data.immutable_backups.includes('non testati')) {
        score -= 2;
        recs.push("Testare restore backup almeno trimestralmente e documentare RTO/RPO");
    } else if (data.immutable_backups.includes('Ottimo')) {
        score -= 1;
        recs.push("Considerare implementazione air-gapped backup per massima protezione ransomware");
    }

    // Network segmentation
    if (data.network_segmentation && data.network_segmentation.includes('piatta senza')) {
        score -= 1;
        findings.push("Rete non segmentata - rischio lateral movement");
        recs.push("Implementare segmentazione rete almeno a livello VLAN per zone funzionali");
    }

    // Logging and monitoring
    if (data.logging_monitoring && data.logging_monitoring.includes('non centralizzati')) {
        score -= 1;
        findings.push("Logging non centralizzato - difficoltà incident detection");
        gaps.push("NIS2 Art. 21 / DORA Art. 17: SIEM e log retention 18+ mesi richiesti");
        recs.push("Implementare SIEM enterprise con retention minimo 18 mesi");
    }
    
    // Physical security (NEW - 3 pts)
    if (!data.physical_security || data.physical_security.includes('Nessun controllo')) {
        score -= 3;
        findings.push("Sicurezza fisica data center inadeguata - manca controllo accessi fisici");
        gaps.push("ISO 27001 A.11 / Best Practice: Physical security spesso dimenticata ma critica");
        recs.push("CRITICO: Implementare badge elettronici + log accessi + videosorveglianza per server room");
    } else if (data.physical_security.includes('Base') || data.physical_security.includes('Buono')) {
        score -= 2;
        recs.push("Aggiungere biometria per aree critiche + correlazione log fisici con log digitali");
    } else if (data.physical_security.includes('Ottimo')) {
        score -= 1;
        recs.push("Implementare mantrap (doppia porta) e procedure visitatori con escort obbligatorio");
    }
    
    // Environmental controls (NEW - 3 pts)
    if (!data.environmental_controls || data.environmental_controls.includes('Nessuna protezione')) {
        score -= 3;
        findings.push("Nessuna protezione da disastri naturali - server vulnerabili");
        gaps.push("ISO 27001 A.11.1.4 / NIS2: Protezione da eventi fisici richiesta");
        recs.push("CRITICO: Installare UPS + rilevazione incendi + sistema soppressione + generatore backup");
    } else if (data.environmental_controls.includes('Minima') || data.environmental_controls.includes('Buona')) {
        score -= 2;
        recs.push("Aggiungere generatore + monitoraggio temperatura/umidità H24 con alerting");
    } else if (data.environmental_controls.includes('Ottima')) {
        score -= 1;
        recs.push("Considerare ridondanza geografica (sito DR) per massima resilienza");
    }
    
    // Business Continuity RTO - DOMANDA KILLER! (NEW - 4 pts)
    if (!data.business_continuity_rto || data.business_continuity_rto.includes('Immediatamente')) {
        score -= 4;
        findings.push("DOMANDA KILLER: Business si ferma immediatamente senza Internet - RTO inadeguato");
        gaps.push("NIS2/DORA: Business Continuity = Resilienza Operativa Digitale - CRITICO per NIS2/DORA");
        recs.push("CRITICO MASSIMO: Implementare DR site + procedure manuali + comunicazione offline - RTO target <4h");
    } else if (data.business_continuity_rto.includes('Poche ore') || data.business_continuity_rto.includes('1 giorno')) {
        score -= 3;
        findings.push("RTO business troppo lungo - vulnerabilità operativa");
        recs.push("Implementare warm standby con RTO <8h + documentare procedure failover");
    } else if (data.business_continuity_rto.includes('2-3 giorni')) {
        score -= 2;
        recs.push("Ridurre RTO con hot standby o active-active per servizi critici");
    } else if (data.business_continuity_rto.includes('hot standby')) {
        score -= 1;
        recs.push("Ottimizzare failover automatico e testare almeno semestralmente");
    }

    return { score, findings, recs, gaps };
}

function assessAIEthics(data) {
    let score = 15;
    let findings = [];
    let recs = [];
    let gaps = [];

    // Check if AI systems are in use
    const aiInUse = data.ai_systems_in_use && data.ai_systems_in_use.length > 0 && 
                     !data.ai_systems_in_use.includes('Nessun sistema IA in uso');

    if (!aiInUse) {
        // No AI systems - full score but note for future
        recs.push("Nessun sistema IA attualmente in uso - monitorare futuri utilizzi per conformità AI Act");
        return { score, findings, recs, gaps };
    }

    // AI transparency
    if (!data.ai_transparency || data.ai_transparency.includes('Nessuna disclosure')) {
        score -= 4;
        findings.push("Utenti non informati quando interagiscono con sistemi IA");
        gaps.push("AI Act Art. 52: Obbligo trasparenza per sistemi IA che interagiscono con persone");
        recs.push("Implementare notifica chiara agli utenti quando interagiscono con sistemi IA");
    } else if (data.ai_transparency.includes('Parziale')) {
        score -= 2;
        recs.push("Rendere disclosure IA più evidente e accessibile all'utente");
    }

    // Training data quality
    if (!data.training_data_quality || data.training_data_quality.includes('Nessuna analisi')) {
        score -= 4;
        findings.push("Qualità e bias dei dati di addestramento IA non verificati");
        gaps.push("AI Act Art. 10: Governance qualità dati per sistemi IA obbligatoria");
        recs.push("Implementare data quality assessment e bias testing per tutti sistemi IA sviluppati internamente");
    } else if (data.training_data_quality.includes('no verifica bias')) {
        score -= 2;
        recs.push("Integrare analisi bias nei dati di addestramento con metodologie standardizzate");
    }

    // Human oversight
    if (!data.human_oversight || data.human_oversight.includes('completamente automatizzati')) {
        score -= 4;
        findings.push("Sistemi IA ad alto rischio senza sorveglianza umana");
        gaps.push("AI Act Art. 14: Human oversight obbligatorio per sistemi IA ad alto rischio");
        recs.push("CRITICO: Implementare human-in-the-loop per tutte decisioni significative prese da sistemi IA");
    } else if (data.human_oversight.includes('solo su richiesta')) {
        score -= 2;
        recs.push("Rendere human oversight obbligatorio e automatico, non opzionale");
    }

    // AI risk assessment
    if (data.ai_risk_assessment && data.ai_risk_assessment.includes('non valutati')) {
        score -= 2;
        findings.push("Sistemi IA ad alto rischio non sottoposti a valutazione conformità");
        gaps.push("AI Act Art. 9: Valutazione conformità obbligatoria per IA alto rischio");
        recs.push("Eseguire valutazione conformità completa per tutti sistemi IA classificati ad alto rischio");
    }

    // AI documentation
    if (data.ai_documentation && data.ai_documentation.includes('Nessuna documentazione')) {
        score -= 1;
        findings.push("Documentazione tecnica sistemi IA inadeguata");
        gaps.push("AI Act Art. 11: Documentazione tecnica dettagliata richiesta");
        recs.push("Creare documentazione tecnica completa per tutti sistemi IA secondo template AI Act");
    }

    return { score, findings, recs, gaps };
}

function calculateRiskLevel(score) {
    // Nuovo massimo: 29+19+22+18+27+15 = 130 punti (NIS2 Gold Standard)
    // Ricalibro soglie proporzionalmente
    const maxScore = 130;
    const percentage = (score / maxScore) * 100;
    
    if (percentage >= 85) return "LOW";      // ≥111 punti
    if (percentage >= 65) return "MEDIUM";   // ≥85 punti  
    return "HIGH";                            // <85 punti
}

// Export everything to window
window.assessmentEngine = {
    assessmentData,
    phases,
    assessmentQuestions,
    assessGovernance,
    assessRiskManagement,
    assessSupplyChain,
    assessIncidentResponse,
    assessTechnicalMeasures,
    assessAIEthics,
    calculateRiskLevel
};
