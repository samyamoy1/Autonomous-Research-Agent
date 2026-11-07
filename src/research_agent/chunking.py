from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(sources):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = []

    for source in sources:
        documents = text_splitter.create_documents(
            texts=[source["content"]],
            metadatas=[{
                "title": source["title"],
                "url": source["url"]
            }]
        )

        chunks.extend(documents)

    return chunks