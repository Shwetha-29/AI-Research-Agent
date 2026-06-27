from ddgs import DDGS


def search_web(search_queries, max_results=5):

    results = []

    with DDGS() as ddgs:

        for query in search_queries:

            print(f"\nSearching: {query}")

            try:
                search_results = list(
                    ddgs.text(
                        query,
                        max_results=max_results
                    )
                )

                print(f"Found {len(search_results)} results")

                for item in search_results:

                    results.append({
                        "query": query,
                        "title": item.get("title", ""),
                        "url": item.get("href", ""),
                        "body": item.get("body", "")
                    })

            except Exception as e:
                print(f"Search Error: {e}")

    return results