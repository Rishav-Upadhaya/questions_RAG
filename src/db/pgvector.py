from langchain_community.vectorstores import PGVector
import os
from dotenv import load_dotenv

load_dotenv()


def pgvectordb(pages_split, embeddings, COLLECTION_NAME):
    CONNECTION_STRING = os.getenv("DATABASE_URL")

    try:
        vector_store = PGVector.from_documents(
            documents=pages_split,
            embedding=embeddings,
            collection_name=COLLECTION_NAME,
            connection_string=CONNECTION_STRING,
        )
        print(f"Created pgvector store")
    except Exception as e:
        print(f"Error creating vector store: {e}")
        raise

    retriever = vector_store.as_retriever(
        # search_type="similarity",
        search_kwargs={"k": 5}
    )
    return retriever