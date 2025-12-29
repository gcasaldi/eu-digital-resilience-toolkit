#!/bin/bash

# Quick launcher for EU Digital Resilience Toolkit
# Usage: ./run.sh

echo "🛡️  EU Digital Resilience Toolkit"
echo "=================================="
echo ""

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit not found. Installing dependencies..."
    pip install -r requirements.txt
fi

# Check if secrets are configured (optional)
if [ ! -f .streamlit/secrets.toml ]; then
    echo "⚠️  Email not configured (optional feature)"
    echo "   To enable: cp .streamlit/secrets.toml.example .streamlit/secrets.toml"
    echo "   Then edit .streamlit/secrets.toml with your SMTP credentials"
    echo ""
fi

echo "🚀 Starting application..."
echo "📱 Open browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop"
echo ""

streamlit run app.py
