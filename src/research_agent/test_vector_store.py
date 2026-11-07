from research_agent.research import collect_research
from research_agent.chunking import split_documents
from research_agent.embeddings import (
    generate_embeddings,
    load_embedding_model
)
from research_agent.vector_store import (
    create_vector_store,
    search_vector_store
)


topic = "Retrieval Augmented Generation"

sources = collect_research(topic, max_sources=3)

chunks = split_documents(sources)

embeddings = generate_embeddings(chunks)

index = create_vector_store(embeddings)

model = load_embedding_model()

question = "How does RAG retrieve relevant documents?"

results = search_vector_store(
    question,
    index,
    chunks,
    model,
    top_k=3
)

print("\nRelevant results:")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Title:", result["title"])
    print("Similarity:", result["score"])
    print("URL:", result["url"])
    print("Content:", result["content"][:300])