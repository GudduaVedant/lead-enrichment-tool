import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ENRICHLAYER_API_KEY")

def score_lead(lead):
    score = 0
    if lead.get("industry") in ["AI Research", "Fintech", "Automation"]:
        score += 40
    if 50 < lead.get("employee_count", 0) < 5000:
        score += 30
    if lead.get("location") in ["San Francisco", "California", "Remote"]:
        score += 30
    return score

def enrich_lead(domain_or_url):
    if "linkedin.com" in domain_or_url:
        endpoint = "https://api.enrichlayer.com/linkedin/company"
        params = {"url": domain_or_url}
    else:
        endpoint = "https://api.enrichlayer.com/linkedin/company/resolve"
        params = {"domain": domain_or_url}

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(endpoint, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    return {
        "name": data.get("name", "Unknown"),
        "industry": data.get("industry", "Unknown"),
        "employee_count": data.get("employee_count", 0),
        "location": data.get("location", "Unknown"),
        "linkedin_url": data.get("linkedin_profile_url", domain_or_url)  # safe fallback
    }
