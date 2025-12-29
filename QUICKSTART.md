# 🚀 Quick Start for Giulia

## Local Testing (Right Now)

```bash
cd /workspaces/eu-digital-resilience-toolkit

# Install dependencies (if not done)
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

App will open at `http://localhost:8501`

---

## Deploy to Streamlit Cloud (5 minutes)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "feat: complete NIS2/DORA compliance toolkit"
   git push origin main
   ```

2. **Deploy**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select repo: `gcasaldi/eu-digital-resilience-toolkit`
   - Main file: `app.py`
   - Click "Deploy"

3. **Add secrets** (optional, for email):
   - In app dashboard → Settings → Secrets
   - Paste this:
     ```toml
     [email]
     smtp_server = "smtp.gmail.com"
     smtp_port = 587
     sender_email = "your.email@gmail.com"
     sender_password = "your_app_password"
     recipient_email = "giulia.casaldi@gmail.com"
     ```

4. **Share**:
   - Your app URL: `https://gcasaldi-eu-digital-resilience-toolkit.streamlit.app`
   - Add to LinkedIn, GitHub profile, resume

---

## Update Your GitHub Profile

**README.md badges** (add to your profile):
```markdown
🛡️ [NIS2/DORA Compliance Toolkit](https://github.com/gcasaldi/eu-digital-resilience-toolkit) - Interactive assessment tool for EU cybersecurity regulations
```

**LinkedIn post template**:
```
🚀 Just launched: EU Digital Resilience Toolkit

Interactive compliance assessments for NIS2 & DORA regulations.

✅ Step-by-step guided questions
✅ AI-assisted risk scoring
✅ Professional PDF reports
✅ Privacy-first (GDPR-compliant)

Perfect for CISOs, compliance teams, security professionals.

🔗 Try it live: [your-streamlit-url]
💻 Open source: github.com/gcasaldi/eu-digital-resilience-toolkit

#Cybersecurity #Compliance #NIS2 #DORA #InfoSec #Python
```

---

## Next Steps for Portfolio Impact

### Week 1:
- [ ] Deploy to Streamlit Cloud
- [ ] Add screenshot to README
- [ ] Post on LinkedIn
- [ ] Add to GitHub profile README

### Week 2:
- [ ] Write blog post on Medium/Dev.to
- [ ] Share in r/cybersecurity, r/Python
- [ ] Add "Star this repo" call-to-action

### Week 3:
- [ ] Record demo video (Loom, 2 min)
- [ ] Add to resume as "Project"
- [ ] Share with recruiters on LinkedIn

### Month 2:
- [ ] Add 1-2 more modules (ISO 27001, GDPR)
- [ ] Gather user feedback
- [ ] Consider adding to Hugging Face Spaces

---

## Email Setup (Optional)

**Gmail App Password**:
1. Enable 2FA on Gmail
2. Go to https://myaccount.google.com/apppasswords
3. Generate "App password" for "Mail"
4. Use that password (not your regular password)

**Alternative** (no email config needed):
- Users can still download PDF
- Email feature just won't work (graceful fallback)

---

## Testing Checklist

Before going public:

- [ ] Run both modules (DORA + NIS2)
- [ ] Generate PDF from each
- [ ] Test email sending (optional)
- [ ] Check mobile view (Streamlit responsive)
- [ ] Verify no errors in console
- [ ] Test with wrong answers → verify scoring logic

---

## Troubleshooting

**Port already in use**:
```bash
streamlit run app.py --server.port 8502
```

**Can't install streamlit**:
```bash
python -m pip install --upgrade pip
pip install streamlit==1.30.0
```

**PDF won't generate**:
```bash
pip install fpdf2
```

---

## Analytics (Optional)

Track usage without violating privacy:

```python
# Add to app.py
import datetime
with open("usage_log.txt", "a") as f:
    f.write(f"{datetime.datetime.now()}, module={module}, score={score}\n")
```

(Don't log IP, names, or sensitive data)

---

## Questions?

- GitHub Issues: For bugs/features
- Email yourself: Keep notes for improvements
- Community: Streamlit forum, r/Python

**You're ready to launch! 🎉**
