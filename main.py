import os
import requests

def send_telegram_message(message):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    
    if not token or not chat_id:
        print("⚠️ Telegram token or chat ID missing. Skipping alert.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Telegram message sent successfully!")
    else:
        print(f"❌ Failed to send Telegram message: {response.text}")

def fetch_and_notify():
    message = (
        "🚀 Daily ServiceNow Job Opportunities (1-3 YOE) 🚀\n\n"
        "Here are today's top portals for active ServiceNow roles:\n\n"
        "1. Indeed India / Global\n"
        "🔗 [View Indeed Jobs](https://in.indeed.com/q-servicenow-developer-1-year-experience-jobs.html)\n\n"
        "2. LinkedIn Jobs\n"
        "🔗 [View LinkedIn Jobs](https://www.linkedin.com/jobs/search/?keywords=ServiceNow%20Developer)\n\n"
        "3. ServiceNow Careers (Direct)\n"
        "🔗 [ServiceNow Careers](https://careers.servicenow.com/jobs/)\n\n"
        "4. SimplyHired (Remote)\n"
        "🔗 [View SimplyHired Jobs](https://www.simplyhired.co.in/search?q=servicenow+developer&l=remote)\n\n"
        "Good luck with your applications today! 🎯"
    )
    
    # Print to logs as fallback
    print(message)
    
    # Send directly to Telegram
    send_telegram_message(message)

if __name__ == "__main__":
    fetch_and_notify()
