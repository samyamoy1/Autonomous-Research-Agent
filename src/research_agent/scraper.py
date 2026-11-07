import requests
from bs4 import BeautifulSoup


def scrape_webpage(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unnecessary elements
    for element in soup(["script", "style", "nav", "footer", "header"]):
        element.decompose()

    # Extract webpage text
    text = soup.get_text(separator=" ", strip=True)

    return text