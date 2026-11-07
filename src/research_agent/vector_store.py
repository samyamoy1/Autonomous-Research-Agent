import faiss
import numpy as np


def create_vector_store(embeddings):
    embeddings = np.asarray(embeddings, dtype="float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    faiss.normalize_L2(embeddings)

    index.add(embeddings)

    return index


def search_vector_store(query, index, chunks, model, top_k=3):
    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    query_embedding = np.asarray(
        query_embedding,
        dtype="float32"
    )

    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, top_k)

    results = []

    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue

        results.append({
            "content": chunks[idx].page_content,
            "title": chunks[idx].metadata["title"],
            "url": chunks[idx].metadata["url"],
            "score": float(score)
        })

    return results