import os
import requests
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

# === ALERT TOGGLE SETTINGS ===
ENABLE_EMAIL_ALERT = os.getenv("ENABLE_EMAIL_ALERT", "false").lower() == "true"
ENABLE_TELEGRAM_ALERT = os.getenv("ENABLE_TELEGRAM_ALERT", "false").lower() == "true"

# === EMAIL CONFIG ===
if ENABLE_EMAIL_ALERT:
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL_ADDRESS = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# === TELEGRAM CONFIG ===
if ENABLE_TELEGRAM_ALERT:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_alert():
    subject = "🚨 Child Monitoring Alert!"
    body = "⚠️ ALERT! No person detected for 10 seconds. Please check immediately."

    # === EMAIL ALERT ===
    if ENABLE_EMAIL_ALERT:
        try:
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = EMAIL_RECEIVER

            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_RECEIVER, msg.as_string())
            server.quit()
            print("✅ Email alert sent successfully!")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")

    # === TELEGRAM ALERT ===
    if ENABLE_TELEGRAM_ALERT:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": body
            }
            response = requests.post(url, data=payload)
            if response.status_code == 200:
                print("✅ Telegram alert sent successfully!")
            else:
                print(f"❌ Failed to send Telegram alert: {response.text}")
        except Exception as e:
            print(f"❌ Telegram API Error: {e}")
