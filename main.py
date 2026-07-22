def fetch_best_servicenow_sources():
    print("🤖 ServiceNow Developer Job Opportunities & Search Engines (1-3 YOE):\n")
    
    portals = [
        {
            "site": "Indeed India / Global",
            "best_for": "1-3 YOE Roles, Hybrid & Remote",
            "url": "https://in.indeed.com/q-servicenow-developer-1-year-experience-jobs.html"
        },
        {
            "site": "LinkedIn Jobs",
            "best_for": "Direct Recruiter Outreach & Global Companies",
            "url": "https://www.linkedin.com/jobs/search/?keywords=ServiceNow%20Developer"
        },
        {
            "site": "ServiceNow Careers (Direct)",
            "best_for": "Product, AI, Platform & Associate Engineering",
            "url": "https://careers.servicenow.com/jobs/"
        },
        {
            "site": "SimplyHired",
            "best_for": "Remote ServiceNow Developer Openings",
            "url": "https://www.simplyhired.co.in/search?q=servicenow+developer&l=remote"
        },
        {
            "site": "Remote Rocketship",
            "best_for": "100% Remote Global/Offshore Opportunities",
            "url": "https://www.remoterocketship.com/country/india/jobs/servicenow-developer/"
        }
    ]
    
    for idx, item in enumerate(portals, 1):
        print(f"{idx}. {item['site']}")
        print(f"   Focus Area:  {item['best_for']}")
        print(f"   Direct Link: {item['url']}\n")

if _name_ == "_main_":
    fetch_best_servicenow_sources()
