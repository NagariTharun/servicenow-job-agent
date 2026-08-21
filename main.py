import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

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

def fetch_linkedin_jobs():
    print("Fetching jobs from LinkedIn...")
    jobs_list = []
    # f_TPR=r86400 means "Only show jobs posted in the last 24 hours"
    url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=ServiceNow+Developer&location=India&f_TPR=r86400&start=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            job_listings = soup.find_all('li')
            
            for job in job_listings[:4]: # Grab top 4 LinkedIn jobs
                title_elem = job.find('h3', class_='base-search-card__title')
                if not title_elem: continue
                
                title = title_elem.text.strip()
                company_elem = job.find('h4', class_='base-search-card__subtitle')
                company = company_elem.text.strip() if company_elem else "Unknown Company"
                location_elem = job.find('span', class_='job-search-card__location')
                location = location_elem.text.strip() if location_elem else "India"
                link_elem = job.find('a', class_='base-card__full-link')
                job_url = link_elem['href'].split('?')[0] if link_elem and 'href' in link_elem.attrs else "#"
                
                jobs_list.append(f"🔹 *{title}*\n🏢 {company} | 📍 {location}\n🔗 [Apply Here]({job_url})")
    except Exception as e:
        print(f"LinkedIn error: {e}")
        
    return jobs_list

def fetch_remotive_jobs():
    print("Fetching jobs from Remotive...")
    jobs_list = []
    url = "https://remotive.com/api/remote-jobs?search=servicenow"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            jobs = response.json().get("jobs", [])
            for job in jobs[:3]: # Grab top 3 Remote jobs
                title = job.get("title", "N/A")
                company = job.get("company_name", "Unknown Company")
                job_url = job.get("url", "#")
                jobs_list.append(f"🔹 *{title}*\n🏢 {company} | 📍 Remote\n🔗 [Apply Here]({job_url})")
    except Exception as e:
        print(f"Remotive error: {e}")
        
    return jobs_list

def fetch_and_notify():
    # Gather jobs from both sources
    linkedin_jobs = fetch_linkedin_jobs()
    remotive_jobs = fetch_remotive_jobs()
    
    if not linkedin_jobs and not remotive_jobs:
        send_telegram_message("No new ServiceNow jobs found today across LinkedIn or Remotive. Check back tomorrow! 🎯")
        return

    # Build the combined Telegram message
    message = f"🚀 *New ServiceNow Jobs ({datetime.now().strftime('%Y-%m-%d')})* 🚀\n\n"
    
    if linkedin_jobs:
        message += "🔷 *LINKEDIN (WFO / Hybrid / Remote)*\n"
        message += "\n\n".join(linkedin_jobs) + "\n\n"
        
    if remotive_jobs:
        message += "🔶 *REMOTIVE (100% Remote)*\n"
        message += "\n\n".join(remotive_jobs) + "\n\n"
        
    message += "Good luck with your applications today! 🎯"
        
    send_telegram_message(message)
    print("✅ Combined message sent successfully!")

if __name__ == "__main__":
    fetch_and_notify()
