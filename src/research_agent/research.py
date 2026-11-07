from research_agent.search import search_web
from research_agent.scraper import scrape_webpage


def collect_research(topic, max_sources=3):
    # Step 1: Search the web
    print("\n[Searching the web...]")

    search_results = search_web(
        query=topic,
        max_results=max_sources
    )

    collected_sources = []

    # Step 2: Visit each webpage
    for i, result in enumerate(search_results, start=1):
        title = result["title"]
        url = result["url"]

        print(f"\n[Reading source {i}/{len(search_results)}]")
        print("Title:", title)

        try:
            content = scrape_webpage(url)

            if not content.strip():
                print("[Skipped: No readable content]")
                continue

            collected_sources.append({
                "title": title,
                "url": url,
                "content": content
            })

            print("[Successfully collected]")

        except Exception as e:
            print("[Failed to scrape]", str(e))

    return collected_sources