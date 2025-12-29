# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-29

### Added
- ✨ **NIS2 Audit Log Readiness module** with 6-step assessment
- ✨ **DORA Third-Party Risk Assessment module** with vendor evaluation
- 📊 Risk scoring algorithm (0-100 scale with Low/Medium/High levels)
- 📄 PDF report generation with findings and recommendations
- 📧 Optional anonymous report sharing via SMTP (GDPR-compliant)
- 🎨 Interactive UI with progress bars and step navigation
- 🔐 Secure secrets management via `.streamlit/secrets.toml`
- 📚 Comprehensive documentation (README, DEPLOYMENT, EXAMPLES, CONTRIBUTING)
- 🧪 Email testing utility (`test_email.py`)
- 🏗️ GitHub Actions workflow for CI/CD
- 📦 Easy deployment to Streamlit Cloud, Hugging Face, Docker

### Security
- No data collection by default (client-side processing)
- Opt-in email sharing with user consent checkbox
- App password support for Gmail SMTP
- `.gitignore` configured to prevent secrets leakage

### Documentation
- README.md with quick start and deployment guides
- DEPLOYMENT.md with platform-specific instructions
- EXAMPLES.md with real-world use cases
- CONTRIBUTING.md for community contributors

## [0.1.0] - 2024-12-28

### Added
- Initial project structure
- Basic DORA module (placeholder)
- PDF generation foundation

---

## Future Releases

### [1.1.0] - Planned
- ISO 27001 compliance module
- CSV export for bulk assessments
- Internationalization (IT, FR, DE)

### [2.0.0] - Planned
- ML-based risk prediction (scikit-learn)
- Historical tracking dashboard
- API endpoints for integration
- Slack/Teams notifications
