from research_agent.research import collect_research
from research_agent.chunking import split_documents
from research_agent.embeddings import generate_embeddings

topic = "Retrieval Augmented Generation"

sources = collect_research(topic, max_sources=3)

chunks = split_documents(sources)

embeddings = generate_embeddings(chunks)

print("\nTotal chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)
print("First embedding:")
print(embeddings[0])