from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_embedding_model():
    model = SentenceTransformer(MODEL_NAME)
    return model

def generate_embeddings(chunks):
    model = load_embedding_model()

    texts = [chunk.page_content for chunk in chunks]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings