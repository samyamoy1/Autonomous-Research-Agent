from research_agent.embeddings import load_embedding_model
from research_agent.vector_store import search_vector_store
from research_agent.storage import load_vector_store
from research_agent.llm import generate_response


SYSTEM_PROMPT = """
You are a research assistant.

Answer the user's question using ONLY the provided context.

Rules:
1. Do not invent facts.
2. If the context does not contain the answer, say so.
3. Cite sources using their URLs.
4. Write clear and structured answers.
"""


def answer_question(question):

    # Step 1: Load saved vector database
    index, chunks = load_vector_store()

    # Step 2: Load embedding model
    model = load_embedding_model()

    # Step 3: Retrieve relevant chunks
    results = search_vector_store(
        question,
        index,
        chunks,
        model,
        top_k=5
    )

    # Step 4: Prepare context
    context = ""

    for result in results:
        context += f"""
Source: {result['title']}
URL: {result['url']}
Content: {result['content']}
"""

    # Step 5: Generate answer
    user_prompt = f"""
Question:
{question}

Retrieved Context:
{context}

Answer using the retrieved context.
Include source URLs.
"""

    return generate_response(SYSTEM_PROMPT, user_prompt)