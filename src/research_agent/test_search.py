from research_agent.search import search_web


def main():
    query = "Latest developments in Generative AI"

    print("\n[Searching the web...]")

    results = search_web(query)

    for i, result in enumerate(results, start=1):
        print(f"\nResult {i}")
        print("Title:", result["title"])
        print("URL:", result["url"])
        print("Content:", result["content"])


if __name__ == "__main__":
    main()