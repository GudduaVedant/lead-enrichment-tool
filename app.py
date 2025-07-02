import streamlit as st
import pandas as pd
from utils import enrich_lead, score_lead

st.title("🔍 Lead Enrichment & Scoring Tool")

uploaded_file = st.file_uploader("📤 Upload CSV (with 'domain' or 'linkedin' column)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Preview of Uploaded Leads", df.head())

    enriched_leads = []
    for _, row in df.iterrows():
        source = row.get("linkedin") or row.get("domain")
        if not source:
            continue

        enriched = enrich_lead(source)
        enriched["source"] = source
        enriched["score"] = score_lead(enriched)
        enriched_leads.append(enriched)

    result_df = pd.DataFrame(enriched_leads)
    result_df.rename(columns={"linkedin_url": "LinkedIn Profile"}, inplace=True)

    st.write("✅ Enriched & Scored Leads", result_df[[
        "name", "industry", "employee_count", "location", "LinkedIn Profile", "score"
    ]])

    csv = result_df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download Results", csv, "enriched_leads.csv", "text/csv")
