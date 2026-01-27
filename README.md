# 🛡️ EU Digital Resilience Toolkit

**Master Check-list 2026** - Comprehensive compliance assessment for NIS2, DORA, GDPR, AI Act, and Cyber Resilience Act

[![Deploy to GitHub Pages](https://github.com/gcasaldi/eu-digital-resilience-toolkit/actions/workflows/pages.yml/badge.svg)](https://github.com/gcasaldi/eu-digital-resilience-toolkit/actions/workflows/pages.yml)
[![Test App](https://github.com/gcasaldi/eu-digital-resilience-toolkit/actions/workflows/test.yml/badge.svg)](https://github.com/gcasaldi/eu-digital-resilience-toolkit/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg)](https://streamlit.io)

## 🚀 Live Demo

**Access the tool here:** [https://gcasaldi.github.io/eu-digital-resilience-toolkit/](https://gcasaldi.github.io/eu-digital-resilience-toolkit/)

## 📋 Overview

The EU Digital Resilience Toolkit is a comprehensive, privacy-first assessment framework designed to help organizations prepare for the complex EU regulatory landscape of 2026. It covers six critical compliance areas across multiple regulations.

### Covered Regulations

- 🔐 **NIS2 Directive** - Cybersecurity for essential & important entities
- 🏦 **DORA** - Digital Operational Resilience for financial sector  
- 🛡️ **GDPR** - Data protection and privacy compliance
- 🤖 **AI Act** - Artificial Intelligence governance and ethical AI
- ⚙️ **Cyber Resilience Act** - Security requirements for digital products
- ⚖️ **D.Lgs. 231/2001** - Organizational Model for corporate liability

## 🎯 6 Assessment Areas

1. **Governance & Legal** (20 pts) - Board accountability, Model 231, CISO/DPO/AI Officer
2. **Risk & Asset Management** (15 pts) - Unified inventory, AI classification, DPIA, SBOM
3. **Supply Chain** (15 pts) - ICT supplier register, contract clauses 2026
4. **Incident Response** (15 pts) - Multi-channel notifications (24h CSIRT, 72h GDPR)
5. **Technical Measures** (20 pts) - MFA, Zero Trust, encryption, immutable backups
6. **AI & Ethics** (15 pts) - Transparency, bias testing, human oversight

## ✨ Key Features

- ✅ **100% Client-Side** - All data stays in your browser, complete privacy
- ✅ **Comprehensive** - 50+ questions with specific regulatory article references
- ✅ **Policy/Implementation/Evidence** - Three-tier verification for audit rigor
- ✅ **Actionable** - Prioritized recommendations with regulatory gap identification
- ✅ **Exportable** - Generate TXT and CSV reports
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
