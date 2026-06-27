import requests
from bs4 import BeautifulSoup


def scrape_page(url):

    try:

        headers = {
            "User-Agent":
            "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return {
            "url": url,
            "content": text
        }

    except Exception as e:

        print(f"Scraping Error: {e}")

        return None