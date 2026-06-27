import json
import os
import re

from dotenv import load_dotenv

load_dotenv()


def rule_based_analysis(query):

    query_lower = query.lower()

    result = {
        "action": "find",
        "category": None,
        "topic": None,
        "location": None
    }

    if "internship" in query_lower:
        result["category"] = "internships"

    elif "job" in query_lower:
        result["category"] = "jobs"

    elif "startup" in query_lower:
        result["category"] = "company"

    elif "company" in query_lower:
        result["category"] = "company"

    elif "laptop" in query_lower:
        result["category"] = "laptops"

    elif "product" in query_lower:
        result["category"] = "products"

    else:
        result["category"] = "general"

    locations = [
        "india",
        "chennai",
        "bangalore",
        "bengaluru",
        "mumbai",
        "hyderabad",
        "delhi",
        "pune"
    ]

    for location in locations:

        if location in query_lower:
            result["location"] = location.title()

    topic = query.lower()

    remove_words = [
        "find",
        "top",
        "best",
        "leading",
        "companies",
        "company",
        "startups",
        "startup",
        "in india",
        "in chennai",
        "in bangalore",
        "in bengaluru",
        "in mumbai",
        "in hyderabad",
        "in delhi",
        "in pune"
    ]

    for word in remove_words:
        topic = topic.replace(word, "")

    topic = re.sub(r"\s+", " ", topic)

    topic = topic.strip()

    if topic == "":
        topic = query

    result["topic"] = topic.upper()

    return result


def analyze_query_ai(query):

    try:

        from google import genai

        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        prompt = f"""
Convert the user query into EXACTLY this JSON format.

{{
  "action": "find",
  "category": "company",
  "topic": "",
  "location": "India"
}}

Rules:
- Return ONLY valid JSON.
- No markdown.
- No explanation.
- topic should contain the main subject.
- category should be one of:
  company, internships, jobs, products, laptops, general

User Query:
{query}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        data = json.loads(text)

        required_keys = {
            "action",
            "category",
            "topic",
            "location"
        }

        if not required_keys.issubset(data.keys()):
            raise Exception("Invalid JSON structure")

        return data

    except Exception:

        print("\nGemini unavailable.")
        print("Using fallback analyzer.")

        return rule_based_analysis(query)