 ## 🚀 Lead Enrichment & Scoring Tool

A lightweight Streamlit-based tool to enrich B2B leads using company domain or LinkedIn URLs and generate a lead quality score based on industry, size, and location. Ideal for sales and marketing teams needing smarter prospecting.

---

 📌 Features

- 🔍 Enriches leads using [EnrichLayer API] or similar tools
- 🏷️ Extracts:
  - Company Name
  - Industry
  - Employee Count
  - Location
  - LinkedIn Profile URL
- 📊 Assigns lead **score** based on business relevance
- 📤 CSV upload & download
- ✅ Simple, clean UI via Streamlit

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/GudduaVedant/lead-enrichment-tool.git
cd lead-enrichment-tool
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # For Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file:

env
Copy
Edit
ENRICHLAYER_API_KEY=your_api_key_here
▶️ Running the App
bash
Copy
Edit
streamlit run app.py
Then open your browser at http://localhost:8501

📥 Input Format
Upload a CSV file with either:

A domain column (e.g., openai.com)

Or a linkedin column (e.g., https://www.linkedin.com/company/openai)

📤 Output Columns
Column	Description
name	Company name
industry	Business sector
employee_count	Estimated number of employees
location	Headquarter or operational region
LinkedIn Profile	Company LinkedIn URL
score	Lead score (0–100)

🧠 Scoring Logic (Simplified)
+40 points for relevant industries

+30 for medium-sized teams

+30 for specific locations

🧾 License
MIT License — free for personal and commercial use.

🙋‍♂️ Author
Built by Vedant Joshi
LinkedIn

