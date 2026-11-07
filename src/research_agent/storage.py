import os
import pickle
import faiss


def save_vector_store(index, chunks, path="data/vector_store"):
    os.makedirs(path, exist_ok=True)

    faiss.write_index(
        index,
        os.path.join(path, "index.faiss")
    )

    with open(os.path.join(path, "chunks.pkl"), "wb") as file:
        pickle.dump(chunks, file)

    print("\nVector store saved successfully!")


def load_vector_store(path="data/vector_store"):
    index_path = os.path.join(path, "index.faiss")
    chunks_path = os.path.join(path, "chunks.pkl")

    if not os.path.exists(index_path) or not os.path.exists(chunks_path):
        raise FileNotFoundError("Vector store not found. Build it first.")

    index = faiss.read_index(index_path)

    with open(chunks_path, "rb") as file:
        chunks = pickle.load(file)

    print("\nVector store loaded successfully!")

    return index, chunks