import os
import requests

API_KEY = os.getenv("PROXYCURL_API_KEY")
BASE_URL = "https://api.enrichlayer.com"

def enrich_lead(domain_or_linkedin):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    if "linkedin.com/company" in domain_or_linkedin:
        enrich_url = f"{BASE_URL}/linkedin/company"
        params = {"url": domain_or_linkedin}
    else:
        # First resolve domain to LinkedIn URL
        resolve_url = f"{BASE_URL}/linkedin/company/resolve"
        resolve_params = {"domain": domain_or_linkedin}
        resolve_res = requests.get(resolve_url, headers=headers, params=resolve_params)
        if resolve_res.status_code == 200 and resolve_res.json().get("linkedin_company_url"):
            linkedin_url = resolve_res.json().get("linkedin_company_url")
            enrich_url = f"{BASE_URL}/linkedin/company"
            params = {"url": linkedin_url}
        else:
            return {
                "domain": domain_or_linkedin,
                "name": "Unknown",
                "industry": "Unknown",
                "employee_count": 0,
                "location": "Unknown",
            }

    res = requests.get(enrich_url, headers=headers, params=params)
    if res.status_code == 200:
        data = res.json()
        return {
            "domain": domain_or_linkedin,
            "name": data.get("name", "Unknown"),
            "industry": data.get("industry", "Unknown"),
            "employee_count": data.get("employee_count", 0),
            "location": data.get("hq", {}).get("location", "Unknown")
        }
    else:
        return {
            "domain": domain_or_linkedin,
            "name": "Unknown",
            "industry": "Unknown",
            "employee_count": 0,
            "location": "Unknown",
        }

def score_lead(lead):
    score = 0
    if lead["industry"] in ["Information Technology", "Software", "Artificial Intelligence", "Research Services"]:
        score += 40
    if 50 <= lead["employee_count"] <= 500:
        score += 40
    if "united states" in lead["location"].lower():
        score += 20
    return score