# 🤖 AI Research Agent

An AI-powered research assistant that automatically discovers AI startups from the web, extracts company information using Large Language Models (LLMs), removes duplicates, and uploads the final results directly to Google Sheets.

---

## 📌 Project Overview

Searching for startup information manually is time-consuming and repetitive.

This project automates the entire research workflow by:

- Understanding the user's research query
- Generating optimized web search queries
- Searching multiple websites
- Scraping webpage content
- Extracting company names and descriptions using AI
- Removing duplicate companies
- Uploading the final results directly to Google Sheets
- Displaying the results through a Streamlit web interface

---

## 🚀 Features

- AI-powered query analysis
- Automatic search query generation
- Web scraping from multiple sources
- LLM-based company extraction
- Duplicate removal
- CSV generation
- Google Sheets integration
- Streamlit user interface

---

## 🛠 Technologies Used

- Python
- Streamlit
- BeautifulSoup
- Requests
- DuckDuckGo Search (DDGS)
- OpenRouter API
- Google Sheets API
- gspread
- pandas

---

## 📂 Project Structure

```
AI-Research-Agent/
│
├── app/
│   ├── ai_analyzer.py
│   ├── cleaner.py
│   ├── csv_exporter.py
│   ├── data_processor.py
│   ├── extractor.py
│   ├── google_sheets.py
│   ├── llm_client.py
│   ├── main.py
│   ├── query_analyzer.py
│   ├── scraper.py
│   ├── search_engine.py
│   ├── search_planner.py
│   └── ui.py
│
├── data/
│   └── results.csv
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shwetha-29/AI-Research-Agent.gits
```

---

### 2. Open the project

```bash
cd AI-Research-Agent
```

---

### 3. Create a virtual environment

```bash
python -m venv venv
```

---

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Configure environment variables

Create a `.env` file.

Example:

```text
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

### 7. Add Google credentials

Download your Google Service Account JSON file and save it as:

```
credentials.json
```

Enable:

- Google Sheets API
- Google Drive API

Share your target Google Sheet with the service account email.

---

## ▶ Running the Project

Launch the Streamlit application:

```bash
streamlit run app/ui.py
```

---

## 🖥 Usage

1. Open the Streamlit application.
2. Enter a research query.
3. Click **Run Research**.
4. The system:
   - Searches the web
   - Extracts company information
   - Removes duplicates
   - Uploads the results to Google Sheets
5. Click **Open Results in Google Sheets** to view the output.

---

## 📊 Example Query

```
Top AI startups in India
```

---

## Example Output

| Company | Description | Source |
|----------|-------------|--------|
| Sarvam AI | AI startup working on foundational models | analyticsinsight.net |
| Krutrim | India's first AI unicorn | wireunwired.com |
| Haptik | Conversational AI platform | techround.co.uk |

---

## 🔒 Environment Variables

```
OPENROUTER_API_KEY
```

---

## 📄 License

This project is developed for educational purposes.
