"""
Quick Test Script for Email Functionality
Run this to verify your SMTP configuration works before deploying.

Usage:
    python test_email.py
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def test_smtp_connection(smtp_server, smtp_port, sender_email, sender_password):
    """Test SMTP connection and authentication"""
    try:
        print(f"🔌 Connecting to {smtp_server}:{smtp_port}...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        print("✅ TLS started")
        
        print(f"🔐 Authenticating as {sender_email}...")
        server.login(sender_email, sender_password)
        print("✅ Authentication successful")
        
        server.quit()
        print("✅ Connection closed successfully")
        return True
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed! Check your email/password.")
        print("   For Gmail: Use App Password, not regular password")
        print("   https://support.google.com/accounts/answer/185833")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def send_test_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email):
    """Send a test email"""
    try:
        msg = MIMEMultipart()
        msg['Subject'] = "Test Email - EU Digital Resilience Toolkit"
        msg['From'] = sender_email
        msg['To'] = recipient_email
        
        body = """
        This is a test email from the EU Digital Resilience Toolkit.
        
        If you received this, your SMTP configuration is working correctly! 🎉
        
        ---
        EU Digital Resilience Toolkit
        https://github.com/gcasaldi/eu-digital-resilience-toolkit
        """
        msg.attach(MIMEText(body, 'plain'))
        
        print(f"📧 Sending test email to {recipient_email}...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print("✅ Test email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("EU Digital Resilience Toolkit - Email Test")
    print("=" * 60)
    print()
    
    # Try to load from Streamlit secrets
    try:
        import streamlit as st
        if "email" in st.secrets:
            config = st.secrets["email"]
            smtp_server = config["smtp_server"]
            smtp_port = int(config["smtp_port"])
            sender_email = config["sender_email"]
            sender_password = config["sender_password"]
            recipient_email = config["recipient_email"]
            print("📝 Loaded configuration from .streamlit/secrets.toml")
        else:
            raise KeyError("No email config in secrets")
    except:
        print("📝 Enter your SMTP configuration:")
        smtp_server = input("SMTP Server (e.g., smtp.gmail.com): ").strip()
        smtp_port = int(input("SMTP Port (e.g., 587): ").strip())
        sender_email = input("Sender Email: ").strip()
        sender_password = input("Sender Password/App Password: ").strip()
        recipient_email = input("Recipient Email (for test): ").strip()
    
    print()
    print("Testing SMTP connection...")
    print("-" * 60)
    
    if test_smtp_connection(smtp_server, smtp_port, sender_email, sender_password):
        print()
        send_test = input("Send a test email? (y/n): ").strip().lower()
        if send_test == 'y':
            send_test_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email)
    else:
        print("\n⚠️  Fix the configuration issues above and try again.")
        sys.exit(1)
    
    print()
    print("=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)
