def clean_companies(companies):

    ai_keywords = [
        "ai",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "generative",
        "llm",
        "large language model",
        "computer vision",
        "nlp",
        "speech",
        "chatbot",
        "voice",
        "robotics",
        "diagnostic",
        "prediction",
        "analytics",
        "automation",
        "agent",
    ]

    non_ai_terms = [
        "software development services",
        "cloud migration",
        "managed services",
        "product engineering",
        "web development",
        "mobile app development",
        "it consulting",
        "digital transformation",
        "cloud consulting",
        "system integration",
        "staffing",
        "outsourcing",
    ]

    # Products instead of companies
    product_names = {
        "bharatgpt",
        "samvaad",
        "sarvam translate",
        "sarvam-translate",
        "thermalytix",
        "vue.ai",
        "unifyai",
    }

    # Generic words
    category_words = [
        "startup",
        "startups",
        "companies",
        "company",
        "directory",
        "ecosystem",
        "industry",
        "category",
        "categories",
        "applications",
        "specialists",
        "platform",
    ]

    # Websites / media
    banned_names = {
        "inc42",
        "forbes",
        "wikipedia",
        "linkedin",
        "medium",
        "analytics insight",
        "analytics vidhya",
        "indiaai",
        "y combinator",
        "yc",
        "zinnov",
        "grapevine",
    }

    # Large enterprises instead of startups
    banned_companies = {
        "tcs",
        "tata consultancy services",
        "infosys",
        "wipro",
        "hcl",
        "hcl technologies",
        "tech mahindra",
        "bosch",
        "bosch ltd",
        "oracle",
        "oracle financial services software",
        "birlasoft",
        "persistent systems",
        "lt technology services",
        "l&t technology services",
        "zoho",
        "affle",
    }

    # Programs / initiatives
    banned_programs = {
        "managementx",
        "d2cx",
        "brandlabs",
    }

    seen = set()
    cleaned = []

    for company in companies:

        name = company.get("company", "").strip()
        description = company.get("description", "").strip()
        source_url = company.get("source_url", "").strip()

        if not name:
            continue

        lower_name = name.lower()

        normalized = (
            lower_name
            .replace(".ai", "")
            .replace(" ai", "")
            .replace(".sh", "")
            .replace(" technologies", "")
            .replace(" technology", "")
            .replace(" systems", "")
            .replace(" solutions", "")
            .replace(" labs", "")
            .replace(" ltd", "")
            .replace(",", "")
            .strip()
        )

        # Minimum length
        if len(name) < 3:
            continue

        # Description required
        if len(description) < 25:
            continue

        desc_lower = description.lower()

        # Remove media names
        if normalized in banned_names:
            continue

        # Remove products
        if normalized in product_names:
            continue

        # Remove enterprise companies
        if normalized in banned_companies:
            continue

        # Remove accelerator/program names
        if normalized in banned_programs:
            continue

        # Remove generic categories
        if any(word == normalized for word in category_words):
            continue

        # Remove consulting/service companies
        if any(term in desc_lower for term in non_ai_terms):
            continue

        # Must mention AI
        if not any(keyword in desc_lower for keyword in ai_keywords):
            continue

        # Remove obvious junk
        if any(word in normalized for word in [
            "event",
            "summit",
            "article",
            "report",
            "initiative",
            "program",
            "conference",
            "community",
        ]):
            continue

        # Normalize duplicates
        duplicate_key = (
            normalized
            .replace("health analytix", "")
            .replace("india", "")
            .replace("private limited", "")
            .replace("pvt ltd", "")
            .strip()
        )

        if duplicate_key in seen:
            continue

        seen.add(duplicate_key)

        cleaned.append({
            "company": name,
            "description": description,
            "source_url": source_url,
        })

    return cleaned