def analyze_query(query):

    query = query.lower()

    result = {
        "action": "find",
        "category": None,
        "topic": None,
        "location": None
    }

    if "startup" in query:
        result["category"] = "company"

    if "india" in query:
        result["location"] = "India"

    if "ai" in query:
        result["topic"] = "AI startups"

    return result