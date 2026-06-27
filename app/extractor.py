# app/extractor.py

import json
from llm_client import ask_llm


def fallback_extract(content, source_url=""):

    companies = []

    return companies


def extract_companies(scraped_data):

    if not scraped_data:
        return []

    content = scraped_data.get("content", "")
    source_url = scraped_data.get("url", "")

    if len(content) < 100:
        return []

    try:

        print("Using OpenRouter extraction.")

        prompt = f"""
Extract ONLY REAL AI STARTUPS OR AI COMPANIES from the text.

STRICT RULES:

Include:
- AI startups
- Generative AI startups
- AI SaaS companies
- AI infrastructure companies
- AI healthcare startups
- AI fintech startups
- AI robotics startups

Exclude:
- Government programs
- Government portals
- Government initiatives
- Events
- Conferences
- Summits
- Awards
- Websites
- News portals
- Articles
- Research papers
- Investors
- Venture capital firms
- Universities
- Incubators
- Accelerators
- Categories
- Generic AI terms

DO NOT return:
- INDIAai
- IndiaAI Portal
- IndiaAI Summit
- Raise 2020
- Startup India
- Government of India programs

Every result must be an actual company.

For each company provide:

- company
- description
- confidence (0-100)

Confidence guidelines:

100 = definitely a real company
90+ = clearly identified AI company
80+ = likely real AI company
Below 80 = uncertain

Return ONLY valid JSON.

Format:

[
  {{
    "company": "",
    "description": "",
    "confidence": 95
  }}
]

TEXT:

{content[:5000]}
"""

        response = ask_llm(prompt)

        text = response.strip()

        # Remove markdown blocks
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        # Recover JSON
        start = text.find("[")
        end = text.rfind("]")

        if start == -1 or end == -1:
            raise Exception("No JSON found")

        json_text = text[start:end + 1]

        companies = json.loads(json_text)

        filtered_companies = []

        for company in companies:

            confidence = company.get("confidence", 0)

            description = company.get("description", "").strip()

            # Keep only high-confidence results
            if confidence < 80:
                continue

            # Remove weak descriptions
            if len(description) < 30:
                continue

            company["source_url"] = source_url

            filtered_companies.append({
                "company": company.get("company", "").strip(),
                "description": description,
                "source_url": source_url
            })

        return filtered_companies

    except Exception as e:

        print("\nLLM Extraction Error:")
        print(e)

        return fallback_extract(
            content,
            source_url
        )