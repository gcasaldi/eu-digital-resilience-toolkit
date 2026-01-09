# 📊 Guida al Sistema di Punteggio - EU Digital Resilience Toolkit

## Panoramica

L'assessment utilizza un sistema di punteggio su **100 punti totali**, suddivisi equamente tra 4 domini critici da 25 punti ciascuno.

## Scala di Rischio

| Punteggio Totale | Livello di Rischio | Descrizione |
|------------------|-------------------|-------------|
| 85-100 | 🟢 **BASSO** | Eccellente postura di conformità e resilienza |
| 65-84 | 🟡 **MEDIO** | Buone basi, alcuni gap da colmare |
| 0-64 | 🔴 **ALTO** | Significative carenze, azione immediata richiesta |

## Dettaglio Punteggi per Dominio

### 1️⃣ Governance & Scope (25 punti)

**Distribuzione:**
- **Classificazione settore** (5 punti)
  - Settore non identificato/applicabile: -3 punti
  - Gap normativo: "NIS2/DORA: Sector classification unclear"
  
- **Framework ICT Risk Management** (10 punti)
  - Nessun framework: -8 punti
  - Framework parziale: -4 punti
  - Framework documentato e testato: punteggio pieno
  - Gap normativo: "NIS2 Art. 21 / DORA Art. 6: ICT risk management framework missing"

- **Supervisione Board** (5 punti)
  - Review meno frequenti di quarterly: -4 punti
  - Review quarterly: punteggio pieno
  - Gap normativo: "NIS2 Art. 20 / DORA Art. 5: Management body accountability"

- **Governance Cloud** (5 punti)
  - Uso significativo cloud (≥2 servizi) senza governance: -3 punti
  - Governance formalizzata: punteggio pieno
  - Gap normativo: "DORA Art. 28: Cloud service provider governance"

**Soglie di Valutazione:**
- 🟢 Eccellente: 20-25 punti (≥80%)
- 🟡 Accettabile: 15-19 punti (60-79%)
- 🔴 Insufficiente: <15 punti (<60%)

---

### 2️⃣ Logging & Monitoring (25 punti)

**Distribuzione:**
- **Logging Centralizzato** (7 punti)
  - Nessun SIEM: -6 punti
  - SIEM deployed: punteggio pieno
  - Gap normativo: "NIS2 Art. 21: Log collection and monitoring"

- **Retention Log** (7 punti)
  - Retention <18 mesi: -6 punti (CRITICO!)
  - 18+ mesi: punteggio pieno
  - Gap normativo: "NIS2: 18-month minimum retention for audit logs"

- **Integrità Log** (5 punti)
  - Nessuna verifica automatica: -4 punti
  - Verifica automatica (hashing): punteggio pieno
  - Gap normativo: "NIS2/DORA: Log tamper-evidence for audit purposes"

- **Integrazione Log Cloud** (3 punti)
  - Cloud in uso ma log non integrati: -3 punti
  - Tutti i log cloud integrati: punteggio pieno

- **Monitoring Real-time** (3 punti)
  - Nessun SOC 24/7: -2 punti
  - SOC 24/7 attivo: punteggio pieno

**Soglie di Valutazione:**
- 🟢 Eccellente: 20-25 punti (≥80%)
- 🟡 Accettabile: 15-19 punti (60-79%)
- 🔴 Insufficiente: <15 punti (<60%)

---

### 3️⃣ ICT Third-Party Risk (25 punti)

**Distribuzione:**
- **Inventario Vendor** (6 punti)
  - Inventario incompleto/datato: -5 punti
  - Inventario completo e aggiornato: punteggio pieno
  - Gap normativo: "DORA Art. 28: Register of ICT third-party providers"

- **Diritti di Audit** (6 punti)
  - Clausole audit mancanti: -5 punti
  - Audit rights in tutti i contratti critici: punteggio pieno
  - Gap normativo: "DORA Art. 30: Contractual audit and access rights"

- **SLA Notifica Incident** (5 punti)
  - SLA >24h o assente: -4 punti
  - SLA ≤24h: punteggio pieno
  - Gap normativo: "DORA Art. 19: Incident reporting by ICT providers"

- **Piano Exit Cloud** (4 punti)
  - Cloud in uso ma nessun piano testato: -4 punti
  - Piano testato annualmente: punteggio pieno
  - Gap normativo: "DORA Art. 28: Exit strategies for critical cloud providers"

- **Monitoring Supply Chain** (4 punti)
  - Nessun monitoring continuo: -3 punti
  - Assessment continuo: punteggio pieno

**Soglie di Valutazione:**
- 🟢 Eccellente: 20-25 punti (≥80%)
- 🟡 Accettabile: 15-19 punti (60-79%)
- 🔴 Insufficiente: <15 punti (<60%)

---

### 4️⃣ Incident & Resilience (25 punti)

**Distribuzione:**
- **Processo Incident Response** (7 punti)
  - Processo non maturo/non testato: -6 punti
  - Processo documentato e testato: punteggio pieno
  - Gap normativo: "NIS2 Art. 23: Incident handling and reporting"

- **Capacità Reporting 24h** (7 punti)
  - Incapacità di notificare entro 24h: -6 punti (CRITICO!)
  - Processo stabilito per 24h: punteggio pieno
  - Gap normativo: "NIS2 Art. 23: 24-hour early warning, 72-hour notification deadlines"

- **Test Resilienza** (5 punti)
  - Frequenza <bi-annuale: -4 punti
  - Test bi-annuali o quarterly: punteggio pieno
  - Gap normativo: "DORA Art. 24: ICT resilience testing"

- **RTO/RPO Definiti** (3 punti)
  - RTO/RPO non definiti per tutti i sistemi: -2 punti
  - RTO/RPO completi: punteggio pieno

- **Integrazione Incident Cloud** (3 punti)
  - Cloud in uso ma incident non integrati: -2 punti
  - Incident cloud integrati: punteggio pieno

**Soglie di Valutazione:**
- 🟢 Eccellente: 20-25 punti (≥80%)
- 🟡 Accettabile: 15-19 punti (60-79%)
- 🔴 Insufficiente: <15 punti (<60%)

---

## Interpretazione dei Risultati

### Punteggio 85-100 (RISCHIO BASSO)
- ✅ Eccellente conformità a NIS2/DORA
- ✅ Postura di resilienza matura
- ✅ Pronto per audit regolatori
- 📝 Mantenimento e miglioramento continuo

### Punteggio 65-84 (RISCHIO MEDIO)
- ⚠️ Fondamenti solidi ma gap da colmare
- 📋 Gap normativi specifici identificati
- 🎯 Piano d'azione prioritizzato necessario
- ⏱️ Timeline: 60-90 giorni per remediation

### Punteggio 0-64 (RISCHIO ALTO)
- 🚨 Carenze significative
- 🔴 Azione immediata richiesta
- 📊 Raccomandazioni ad alta priorità critiche
- ⏱️ Timeline: intervento immediato (30 giorni)

---

## Output dell'Assessment

### 📊 Report Generato

L'assessment produce:

1. **Metriche quantitative**
   - Punteggio totale /100
   - Breakdown per dominio
   - Livello di rischio
   - Percentuale di conformità

2. **Gaps normativi**
   - Articoli specifici NIS2/DORA non soddisfatti
   - Raggruppati per dominio
   - Riferimenti legislativi precisi

3. **Findings operativi**
   - Carenze tecniche e organizzative
   - Impatto su conformità
   - Suddivisi per area

4. **Raccomandazioni prioritizzate**
   - 🔴 Alta priorità (azioni immediate)
   - 🟡 Media priorità (30-60 giorni)
   - 🟢 Bassa priorità (miglioramento continuo)

5. **Riepilogo risposte**
   - Tutte le risposte fornite
   - Organizzate per fase
   - Riferimento per audit interno

---

## Note Importanti

⚠️ **Disclaimer**: Questo assessment è uno strumento di valutazione della readiness e del rischio. Non costituisce consulenza legale. Le organizzazioni devono consultare esperti legali per la strategia di conformità.

🔒 **Privacy**: Tutti i dati rimangono nel browser. Nessuna informazione viene raccolta o memorizzata.

📅 **Aggiornamenti**: Il toolkit viene aggiornato con le evoluzioni normative NIS2/DORA.

---

## Utilizzo Audit

Il report generato può essere utilizzato per:
- ✅ Documentazione compliance interna
- ✅ Preparazione audit esterni
- ✅ Board reporting
- ✅ Gap analysis per consulenti
- ✅ Baseline per programmi di remediation

**Esportazioni disponibili:**
- 📄 Report testuale (TXT)
- 📊 Dati strutturati (CSV)
- 🔗 Riferimenti normativi completi
