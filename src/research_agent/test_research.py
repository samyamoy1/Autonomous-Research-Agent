from research_agent.research import collect_research


def main():
    topic = "Retrieval Augmented Generation"

    sources = collect_research(
        topic,
        max_sources=3
    )

    print("\n========== RESEARCH SUMMARY ==========")

    print("Total sources collected:", len(sources))

    for i, source in enumerate(sources, start=1):
        print(f"\nSource {i}")
        print("Title:", source["title"])
        print("URL:", source["url"])
        print("Content length:", len(source["content"]))
        print("Preview:", source["content"][:300])


if __name__ == "__main__":
    main()