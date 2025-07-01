import streamlit as st
import pandas as pd
from utils import enrich_lead, score_lead
st.title("lead enrichment and scoreing tool")
uploaded_file= st.file_uploader("upload a csv file for domain and linkedin url",type=["csv"])
if uploaded_file:
    df=pd.read_csv(uploaded_file)
    st.write("preview of uploaded leads",df.head())

    enriched_leads = []
    for index,row in df.iterrows():
         domain = row.get("domain") or row.get("linkedin")
         enriched = enrich_lead(domain)
         enriched["score"] = score_lead(enriched)
         enriched_leads.append(enriched)

    result_df = pd.DataFrame(enriched_leads)
    st.write("### Enriched & Scored Leads", result_df.head())

    csv = result_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "enriched_leads.csv", "text/csv")
