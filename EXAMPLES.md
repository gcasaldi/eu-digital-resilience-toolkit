## Example Use Cases

### Use Case 1: Pre-Audit Preparation (Financial Institution)

**Scenario**: A small bank needs to prepare for NIS2 compliance audit.

**Steps**:
1. Run "NIS2 – Audit Log Readiness" assessment
2. Answer questions based on current Splunk/SIEM setup
3. Receive score: 72/100 (Medium Risk)
4. Key findings:
   - ❌ Retention only 12 months (need 18+)
   - ❌ No integrity verification (hashing)
   - ✅ Access tracking in place
5. Download PDF report
6. Present to IT management with recommendations
7. Implement fixes, re-run assessment

**Result**: 3 months later, score improves to 91/100 (Low Risk). Ready for audit.

---

### Use Case 2: Vendor Risk Review (Healthcare Provider)

**Scenario**: Hospital uses 15+ cloud vendors, needs DORA compliance.

**Steps**:
1. Run "DORA – Third-Party Risk Assessment" for each critical vendor
2. For AWS:
   - ✅ Contract in place
   - ✅ Right to audit clause
   - ✅ Exit plan documented
   - Score: 95/100 (Low Risk)
3. For small MSSP:
   - ❌ No right to audit
   - ❌ No exit plan
   - ⚠️ Handles patient data
   - Score: 45/100 (High Risk)
4. Prioritize MSSP for contract renegotiation

**Result**: Identify high-risk vendors, justify budget for legal review.

---

### Use Case 3: Board Presentation (Startup)

**Scenario**: Startup raising Series A, investors ask about compliance.

**Steps**:
1. CEO runs both assessments
2. NIS2: 88/100 (Low Risk) ✅
3. DORA: 67/100 (Medium Risk) ⚠️
4. Download both PDFs
5. Add to investor data room
6. In pitch: "We're proactive on EU compliance, see attached reports"

**Result**: Shows maturity, differentiates from competitors.

---

### Use Case 4: Freelance Consultant

**Scenario**: You offer compliance consulting, need quick assessment tool.

**Steps**:
1. During client discovery call, share Streamlit app link
2. Client fills it out live (5 minutes)
3. You review results together
4. Use findings to quote project scope:
   - Low score → full compliance project
   - High score → limited advisory engagement
5. PDF becomes scope-of-work appendix

**Result**: Faster sales cycle, data-driven proposals.

---

### Use Case 5: Internal IT Team (Self-Assessment)

**Scenario**: IT manager wants to track improvement over time.

**Steps**:
1. Run assessment quarterly (Q1, Q2, Q3, Q4)
2. Track scores in spreadsheet:
   - Q1 2024: 65/100
   - Q2 2024: 78/100
   - Q3 2024: 89/100
3. Present trend to CISO: "22% improvement year-to-date"
4. Use recommendations to prioritize roadmap

**Result**: Data-driven security improvements, KPI for team.

---

## Sample Outputs

### Low Risk Example (NIS2: 92/100)

**Findings**:
- ✅ Logs exported in JSON format
- ✅ 18-month retention policy documented
- ✅ SHA256 hashing implemented
- ✅ Access logs reviewed monthly

**Recommendations**:
- Maintain current practices
- Consider extending retention to 24 months for critical systems
- Quarterly review of access controls

---

### High Risk Example (DORA: 38/100)

**Findings**:
- ❌ No vendor inventory
- ❌ Contracts missing right-to-audit clauses
- ❌ No past incident assessment
- ❌ Critical data handled without exit plan

**Recommendations**:
- **URGENT**: Create vendor inventory within 30 days
- Hire legal to review/amend contracts
- Conduct vendor security assessments
- Develop exit strategy for top 3 critical vendors
- Consider cyber insurance for vendor-related risks

---

## ROI Examples

### Time Saved
- Manual assessment: 8-16 hours (consultant or internal)
- This tool: 5 minutes
- **Saved**: ~15 hours per assessment

### Cost Saved
- External consultant: €1,500-€5,000 per assessment
- This tool: Free (open source)
- **Saved**: €1,500-€5,000

### Ongoing Value
- Quarterly re-assessments (4x/year)
- Total time saved/year: 60 hours
- Total cost saved/year: €6,000-€20,000

---

## Integration Ideas

### With Existing Tools

**Jira/Monday.com**:
- Export recommendations → create tickets
- Track remediation progress
- Link PDF report to epic

**Slack/Teams**:
- Post scores to #security channel
- Alert if score drops below threshold

**GRC Platforms** (Vanta, Drata, Secureframe):
- Upload PDF as evidence
- Track compliance over time

**SIEM/SOAR**:
- Trigger assessment after incident
- Auto-fill based on SIEM data (future feature)

---

## Adaptation for Other Frameworks

This tool's structure can be adapted for:

- **ISO 27001**: Add controls checklist
- **SOC 2**: Focus on security, availability, confidentiality
- **GDPR**: Data processing, breach response
- **PCI-DSS**: Payment card data specific checks
- **NIST CSF**: Map to 5 framework functions

**Template**:
1. Define 10-15 key questions
2. Assign point values
3. Define risk thresholds
4. Write recommendations database
5. Plug into same Streamlit UI

---

## Testimonials (Hypothetical)

> "This tool saved us 20 hours of prep work for our NIS2 audit. The PDF report went straight into our evidence package."  
> — Maria S., CISO at FinTech Startup

> "Simple, fast, and actually useful. I run it quarterly to track our third-party risk posture."  
> — John D., Compliance Manager at Hospital Group

> "As a freelance consultant, this tool helps me scope projects in real-time during client calls."  
> — Sophie L., Independent Security Consultant

---

## Next Steps

1. **Try it yourself**: `streamlit run app.py`
2. **Customize**: Add your organization's specific requirements
3. **Share**: Deploy publicly or use internally
4. **Contribute**: Add new modules (ISO 27001, SOC 2, etc.)
5. **Feedback**: Use the "Send Anonymous Report" feature

**Questions?** Open an issue on GitHub or email giulia@example.com
