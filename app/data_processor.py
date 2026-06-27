def remove_duplicates(results):

    seen_urls = set()
    unique_results = []

    for result in results:

        url = result["url"]

        if url not in seen_urls:
            seen_urls.add(url)
            unique_results.append(result)

    return unique_results