from research_agent.research import collect_research
from research_agent.chunking import split_documents


def main():
    topic = "Retrieval Augmented Generation"

    sources = collect_research(topic, max_sources=3)

    chunks = split_documents(sources)

    print("\n========== CHUNKING SUMMARY ==========")

    print("Total sources:", len(sources))
    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks[:3], start=1):
        print(f"\nChunk {i}")
        print("Title:", chunk.metadata["title"])
        print("URL:", chunk.metadata["url"])
        print("Content:", chunk.page_content[:200])


if __name__ == "__main__":
    main()