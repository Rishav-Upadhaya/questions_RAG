from langchain_chroma import Chroma

def chromadb(pages_split, embeddings, persit_directory, collection_name):
    try:
        vector_store = Chroma.from_documents(
            documents = pages_split,
            embedding=embeddings,
            persist_directory=persit_directory,
            collection_name=collection_name
        )
        print(f"Created ChromaDB vector store")
    except Exception as e:
        print(f"Error creating vector store: {e}")
        raise

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )
    return retriever