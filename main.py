import requests
import json

class ServiceNowJobAgent:
    def __init__(self, target_exp="1-3 years"):
        self.target_exp = target_exp
        self.keywords = ["ServiceNow Developer", "ServiceNow Engineer", "ServiceNow Consultant"]
        
    def fetch_jobs(self):
        """
        Simulates querying job aggregation APIs or career RSS feeds
        filtered specifically for ServiceNow development roles.
        """
        query = f"ServiceNow Developer {self.target_exp}"
        print(f"🤖 Searching active listings for: '{query}'...")
        
        # Example API Endpoint Structure (e.g., RapidAPI / Job Search APIs)
        # url = f"https://api.jobsearch.com/v1/jobs?q={query}"
        
        sample_results = [
            {
                "title": "ServiceNow Developer (HRSD / ITSM)",
                "experience": "1-3 Years",
                "location": "Remote / Flexible",
                "source": "LinkedIn Jobs",
                "url": "https://www.linkedin.com/jobs/search/?keywords=ServiceNow%20Developer"
            },
            {
                "title": "Associate ServiceNow Engineer",
                "experience": "2 Years",
                "location": "Bengaluru / Hybrid",
                "source": "Indeed",
                "url": "https://in.indeed.com/q-servicenow-developer-1-year-experience-jobs.html"
            }
        ]
        return sample_results

    def filter_and_format(self, jobs):
        print(f"\n✅ Found {len(jobs)} recent job matches:\n")
        for idx, job in enumerate(jobs, 1):
            print(f"{idx}. {job['title']}")
            print(f"   Experience: {job['experience']}")
            print(f"   Location:   {job['location']}")
            print(f"   Source:     {job['source']}")
            print(f"   Link:       {job['url']}\n")

# Run the Agent
if __name__ == "__main__":
    agent = ServiceNowJobAgent(target_exp="1-3 years")
    active_jobs = agent.fetch_jobs()
    agent.filter_and_format(active_jobs)
