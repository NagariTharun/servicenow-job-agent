import os
import requests
from datetime import datetime

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
ADZUNA_APP_ID = os.environ.get("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.environ.get("ADZUNA_APP_KEY")

def send_telegram_message(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("⚠️ Telegram tokens missing. Skipping alert.")
        return
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True 
    }
    requests.post(url, json=payload)

def fetch_and_notify():
    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        print("⚠️ Adzuna credentials missing. Cannot fetch jobs.")
        return

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": "ServiceNow Developer",
        "results_per_page": 5,
        "max_days_old": 1, 
        "sort_by": "date"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error fetching from Adzuna")
        return
        
    jobs = response.json().get("results", [])

    if not jobs:
        send_telegram_message("No new ServiceNow jobs posted in the last 24 hours. Check back tomorrow! 🎯")
        return

    message = f"🚀 *New ServiceNow Jobs ({datetime.now().strftime('%Y-%m-%d')})* 🚀\n\n"
    
    for idx, job in enumerate(jobs, 1):
        title = job.get("title", "N/A")
        company = job.get("company", {}).get("display_name", "Unknown Company")
        job_url = job.get("redirect_url", "#")
        message += f"*{idx}. {title}*\n🏢 {company}\n🔗 [Apply Here]({job_url})\n\n"

    send_telegram_message(message)

if __name__ == "__main__":
    fetch_and_notify()
