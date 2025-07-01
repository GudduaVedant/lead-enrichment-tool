# README.md

# 🔍 Lead Enrichment & Scoring Tool

A lightweight Streamlit-based web tool to upload a list of company domains or LinkedIn URLs, enrich them using Proxycurl's API, score them based on business criteria, and export the results. Built in under 5 hours to solve real-world lead generation problems effectively.

---

## 🚀 Features
- Upload CSV file with company domains or LinkedIn company URLs
- Fetch real-time company enrichment data via Proxycurl
- Score leads based on industry, employee count, and location
- Preview and download the enriched lead list

---

## 📦 Requirements
Make sure you have Python 3.7+ installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

### Required `.env` file
Create a `.env` file in the root folder and add your Proxycurl API key:

```
PROXYCURL_API_KEY=your_api_key_here
```

---

## 🛠️ How to Run

```bash
streamlit run app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`) in your browser.

---

## 📁 Project Structure

```
lead-enrichment-tool/
├── app.py              # Main Streamlit app
├── utils.py            # Enrichment + scoring functions
├── requirements.txt    # Python dependencies
├── .env                # Proxycurl API key (not to be committed)
└── README.md           # This file
```

---

## 📤 Sample Input Format

Upload a CSV file like:

```
domain
https://www.linkedin.com/company/openai
stripe.com
zapier.com
```

---

## 📓 Notes
- Uses Proxycurl's company API for enrichment (Free for limited requests)
- Built for a 5-hour challenge focused on usability, business value, and rapid development

---

## 👤 Author
**Vedant Joshi**  
GitHub: [@GudduaVedant](https://github.com/GudduaVedant)

Feel free to fork, improve, or suggest features!
