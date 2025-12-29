## 🎯 Deployment Options

### Option 1: Streamlit Community Cloud (Recommended)

**Pros**: Free, zero config, auto-updates from GitHub  
**Cons**: Limited to public repos (or paid Streamlit plan)

**Steps**:
1. Push your code to GitHub (public or private repo)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repo, branch, and `app.py`
5. Add secrets:
   - Click "Advanced settings" → "Secrets"
   - Paste contents of your `.streamlit/secrets.toml`
6. Click "Deploy"!

**Your app will be live at**: `https://YOUR_USERNAME-eu-digital-resilience-toolkit.streamlit.app`

---

### Option 2: Hugging Face Spaces

**Pros**: Free, ML-community visibility, supports private Spaces  
**Cons**: Slightly slower than Streamlit Cloud

**Steps**:
1. Create account at [huggingface.co](https://huggingface.co)
2. Create new Space: [huggingface.co/new-space](https://huggingface.co/new-space)
   - Name: `eu-digital-resilience-toolkit`
   - SDK: **Streamlit**
   - Visibility: Public or Private
3. Clone the Space repo:
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/eu-digital-resilience-toolkit
   cd eu-digital-resilience-toolkit
   ```
4. Copy your files:
   ```bash
   cp /path/to/your/app.py .
   cp /path/to/your/requirements.txt .
   ```
5. Commit and push:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push
   ```
6. Add secrets in Space settings (same format as `.streamlit/secrets.toml`)

**Your app will be live at**: `https://huggingface.co/spaces/YOUR_USERNAME/eu-digital-resilience-toolkit`

---

### Option 3: Docker + Any Cloud (AWS, GCP, Azure, Fly.io)

**Pros**: Full control, can use private networks  
**Cons**: Requires Docker knowledge, potentially not free

**Dockerfile**:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY .streamlit .streamlit

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Deploy to Fly.io** (example):
```bash
# Install flyctl
curl -L https://fly.io/install.sh | sh

# Login
flyctl auth login

# Launch app
flyctl launch --name eu-compliance-toolkit

# Set secrets
flyctl secrets set SMTP_PASSWORD=your_password

# Deploy
flyctl deploy
```

---

### Option 4: Local/Intranet (For Sensitive Data)

**Use case**: Corporate environments where data cannot leave premises

**Steps**:
1. Install on internal server:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure `.streamlit/secrets.toml` with internal SMTP
3. Run with specific port and host:
   ```bash
   streamlit run app.py --server.port 8080 --server.address 0.0.0.0
   ```
4. Access at `http://YOUR_SERVER_IP:8080`
5. Optional: Put behind nginx/Apache for HTTPS

---

## 🔐 Secrets Management by Platform

| Platform | How to Add Secrets |
|----------|-------------------|
| **Streamlit Cloud** | App settings → Secrets → Paste TOML |
| **Hugging Face** | Space settings → Variables and secrets → Add |
| **Docker** | Environment variables or Docker secrets |
| **Heroku** | Config Vars in dashboard |
| **Fly.io** | `flyctl secrets set KEY=value` |

---

## 📊 Monitoring & Analytics (Optional)

Add simple usage tracking (GDPR-compliant):

```python
# In app.py, add at bottom:
import streamlit as st

# Track page views (anonymous)
if "views" not in st.session_state:
    st.session_state.views = 0
    # Optional: log to file or send to analytics API
    # requests.post("https://your-analytics.com/event", json={"event": "page_view"})
```

**Recommended tools**:
- Plausible Analytics (privacy-focused)
- PostHog (self-hosted)
- Simple log file analysis

---

## 🚀 Performance Tips

1. **Cache heavy computations**:
   ```python
   @st.cache_data
   def expensive_calculation():
       # ...
   ```

2. **Lazy load large data**:
   ```python
   if st.button("Load vendors"):
       data = load_vendors()
   ```

3. **Optimize PDF generation**:
   - Use smaller fonts
   - Compress images if adding logos
   - Limit report length

4. **Use CDN for assets** (if adding images/logos)

---

## 🆘 Troubleshooting

### "ModuleNotFoundError: No module named 'fpdf'"
```bash
pip install fpdf2
```

### "Email sending failed: Authentication failed"
- Gmail: Use [App Password](https://support.google.com/accounts/answer/185833), not regular password
- Enable "Less secure app access" (not recommended, use App Password instead)

### "Streamlit app won't start"
```bash
# Check Python version (needs 3.8+)
python --version

# Reinstall Streamlit
pip uninstall streamlit
pip install streamlit
```

### "PDF has garbled characters"
- FPDF uses latin-1 encoding by default
- For special characters, consider using `reportlab` instead

---

## 📞 Need Help?

- GitHub Issues: [github.com/gcasaldi/eu-digital-resilience-toolkit/issues](https://github.com/gcasaldi/eu-digital-resilience-toolkit/issues)
- Streamlit Forum: [discuss.streamlit.io](https://discuss.streamlit.io)
- Email: giulia@example.com
