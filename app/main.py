from ai_analyzer import analyze_query_ai
from search_planner import generate_search_queries
from search_engine import search_web
from data_processor import remove_duplicates
from scraper import scrape_page
from extractor import extract_companies
from csv_exporter import save_to_csv
from cleaner import clean_companies
from google_sheets import upload_to_google_sheets

BAD_DOMAINS = [
    "forbes.com",
    "companiesmarketcap.com",
    "pickmyurl.in",
    "wikipedia.org",
    "linkedin.com",
    "youtube.com",
    "reddit.com",
    "grokipedia.com",
    "topstartups.io",
    "medium.com",
    "cutshort.io",
]


def main(query):

    analysis = analyze_query_ai(query)

    if analysis is None:
        print("Could not analyze query.")
        return

    print("\nAnalysis Result:")
    print(analysis)

    search_queries = generate_search_queries(analysis)

    print("\nSearch Queries:")

    for q in search_queries:
        print("-", q)

    print("\nSearching Web...\n")

    results = search_web(search_queries)

    results = remove_duplicates(results)

    print(f"\nUnique Results Found: {len(results)}\n")

    all_companies = []

    print("\n" + "=" * 80)
    print("SCRAPING + AI EXTRACTION")
    print("=" * 80)

    processed = 0

    for result in results:

        url = result["url"]

        if any(domain in url for domain in BAD_DOMAINS):
            print(f"\nSkipping: {url}")
            continue

        print(f"\nProcessing: {url}")

        scraped_data = scrape_page(url)

        if not scraped_data:
            continue

        companies = extract_companies(scraped_data)

        for company in companies:
            company["source_url"] = url

        all_companies.extend(companies)

        processed += 1

        if processed >= 20:
            break

    # -----------------------------
    # Clean extracted companies
    # -----------------------------
    all_companies = clean_companies(all_companies)

    print(f"\nTotal Companies After Cleaning: {len(all_companies)}")

    # -----------------------------
    # Save Results
    # -----------------------------
    print("\nSaving to CSV...")

    save_to_csv(all_companies)

    print("\nUploading to Google Sheets...")

    upload_to_google_sheets("data/results.csv")

    print("\nDone.")


if __name__ == "__main__":
    query = input("Enter your research query: ")
    main(query)