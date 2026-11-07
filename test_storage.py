from research_agent.research import collect_research
from research_agent.chunking import split_documents
from research_agent.embeddings import generate_embeddings
from research_agent.vector_store import create_vector_store
from research_agent.storage import save_vector_store, load_vector_store


topic = "Retrieval Augmented Generation"

# Collect sources
sources = collect_research(topic, max_sources=3)

# Create chunks
chunks = split_documents(sources)

# Generate embeddings
embeddings = generate_embeddings(chunks)

# Create FAISS index
index = create_vector_store(embeddings)

# Save everything
save_vector_store(index, chunks)

# Load everything again
loaded_index, loaded_chunks = load_vector_store()

print("\nOriginal chunks:", len(chunks))
print("Loaded chunks:", len(loaded_chunks))
print("Stored vectors:", loaded_index.ntotal)