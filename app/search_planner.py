def generate_search_queries(analysis):

    topic = analysis.get("topic", "")
    location = analysis.get("location", "India")

    topic_lower = topic.lower()

    ai_keywords = [
        "ai",
        "artificial intelligence",
        "machine learning",
        "generative ai",
        "llm",
        "deep learning",
    ]

    if any(keyword in topic_lower for keyword in ai_keywords):

        return [
            "top AI startups in India",
            "best AI startups in India",
            "Indian AI startups list",
            "generative AI startups India",
            "AI companies in India",
            "AI unicorns in India",
            "enterprise AI startups India",
            "healthcare AI startups India"
            "Indian AI startup tracker",
            "Indian AI companies list",
            "top generative AI companies India",
            "AI SaaS startups India",
            "AI healthcare startups India",
            "AI fintech startups India"
        ]

    return [
        f"best {topic} companies in {location}",
        f"leading {topic} companies in {location}",
        f"list of {topic} companies in {location}"
    ]