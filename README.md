# 🛡️ EU Digital Resilience Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)](https://streamlit.io)

**Interactive compliance assessment tool for NIS2 and DORA regulations** — built for CISOs, compliance officers, and security professionals.

## 🎯 What It Does

This tool provides **step-by-step guided assessments** for EU cybersecurity regulations:

### ✅ NIS2 – Audit Log Readiness
- Log export format & quality checks
- Retention policy compliance (18+ months requirement)
- Integrity verification (hashing, tamper-proofing)
- Access control & monitoring
- Incident response testing

### ✅ DORA – Third-Party Risk Assessment
- Vendor inventory completeness
- Contract clause analysis (right-to-audit, SLAs)
- Past incident review
- Data criticality assessment
- Exit/contingency planning

**Each assessment generates:**
- 📊 Risk score (0-100) with color-coded risk level
- 📋 Detailed findings with context
- 💡 Actionable recommendations
- 📄 Professional PDF report (downloadable)
- 📧 Optional anonymous sharing (GDPR-compliant)

---

## 🚀 Quick Start

### Local Setup

```bash
# Clone the repository
git clone https://github.com/gcasaldi/eu-digital-resilience-toolkit.git
cd eu-digital-resilience-toolkit

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

### Deploy to Streamlit Cloud (Free)

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy from your forked repo
5. ✨ Live app in 2 minutes!

### Deploy to Hugging Face Spaces (Free)

1. Create a Space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Select **Streamlit** as SDK
3. Upload files or connect via Git
4. Add secrets in Space settings (for email feature)

---

## 📧 Email Configuration (Optional)

To enable the **"Send Anonymous Report"** feature:

1. Copy the example secrets file:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   ```

2. Edit `.streamlit/secrets.toml` with your SMTP credentials:
   ```toml
   [email]
   smtp_server = "smtp.gmail.com"
   smtp_port = 587
   sender_email = "your.email@gmail.com"
   sender_password = "your_app_password"
   recipient_email = "giulia@example.com"
   ```

3. **For Gmail**: Generate an [App Password](https://support.google.com/accounts/answer/185833) (don't use your regular password)

4. **For production**: Use SendGrid, AWS SES, or Mailgun (see `.streamlit/secrets.toml.example` for examples)

⚠️ **Never commit `secrets.toml` to git!** (already in `.gitignore`)

---

## 📖 How to Use

### 1. Choose Your Assessment
Select either:
- **DORA – Third-Party Risk Assessment**
- **NIS2 – Audit Log Readiness**

### 2. Answer Guided Questions
The tool walks you through 3-4 steps with:
- Smart dropdown menus
- Contextual tips and warnings
- Real-time validation

### 3. Get Your Report
- View your **compliance score** and **risk level**
- Review **findings** and **recommendations**
- Download **PDF report** for documentation
- Optionally share anonymized results for research

---

## 🧠 Why This Tool?

### For You (Job Seekers / Professionals)
✅ **Portfolio piece**: Interactive web app (not just code)  
✅ **Domain expertise**: Shows knowledge of NIS2, DORA, compliance  
✅ **Real-world utility**: Solves actual CISO pain points  
✅ **Engagement**: Recruiter can *try it* in 2 minutes  

### For Organizations
✅ **Quick gap analysis**: No consultants needed for initial assessment  
✅ **Documentation**: PDF reports for audits/board presentations  
✅ **Education**: Helps teams understand compliance requirements  
✅ **Privacy-first**: No data leaves your browser (except optional email)  

---

## 🔐 Privacy & GDPR Compliance

- **No data collection** by default (runs client-side in your browser)
- **Optional sharing**: Checkbox opt-in for anonymous report submission
- **No tracking**: No analytics, cookies, or third-party scripts
- **Transparent**: All code is open-source (MIT license)

---

## 🛠️ Tech Stack

- **Frontend/Backend**: [Streamlit](https://streamlit.io) (Python)
- **PDF Generation**: [FPDF2](https://pyfpdf.github.io/fpdf2/)
- **Email**: Python `smtplib` (SMTP/TLS)
- **Deployment**: Streamlit Cloud, Hugging Face Spaces, or any Python host

---

## 📋 Roadmap

- [ ] Add **ISO 27001** compliance module
- [ ] Integrate **ML-based risk prediction** (scikit-learn)
- [ ] Support **CSV data upload** (e.g., bulk vendor assessment)
- [ ] Multi-language support (IT, FR, DE)
- [ ] API endpoint for programmatic access
- [ ] Slack/Teams integration for alerts

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Giulia Casaldi**  
Cybersecurity professional | AI/ML enthusiast | EU regulations specialist

- GitHub: [@gcasaldi](https://github.com/gcasaldi)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📬 Feedback & Collaboration

Have suggestions? Found a bug? Want to collaborate?

- Open an [Issue](https://github.com/gcasaldi/eu-digital-resilience-toolkit/issues)
- Use the **"Send Anonymous Report"** feature in the app
- Email: giulia@example.com

---

## ⭐ Support This Project

If you find this tool useful:
- ⭐ Star this repository
- 🐦 Share on social media
- 📝 Write a blog post about it
- 🤝 Contribute code or ideas

**Made with ❤️ for the cybersecurity community**
