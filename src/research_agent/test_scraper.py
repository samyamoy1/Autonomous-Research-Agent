from research_agent.scraper import scrape_webpage


def main():
    url = "https://example.com"

    print("[Scraping webpage...]")

    content = scrape_webpage(url)

    print("\n[Extracted Content]")
    print(content)


if __name__ == "__main__":
    main()