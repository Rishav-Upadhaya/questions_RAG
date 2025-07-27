import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def doc_loader():
    # 1. Configure source directory
    pdf_dir = "./Database/questions"
    if not os.path.isdir(pdf_dir):
        raise FileNotFoundError(f"PDF directory not found: {pdf_dir}")

    # 2. Bulk-load all PDFs in the directory
    loader = PyPDFDirectoryLoader(pdf_dir, glob="*.pdf", recursive=True)
    try:
        raw_docs = loader.load()
    except Exception as e:
        raise RuntimeError(f"Failed to load PDFs: {e}")

    print(f"[INFO] Loaded {len(raw_docs)} raw document parts from PDF directory")

    # 3. Split into manageable chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs_split = splitter.split_documents(raw_docs)
    print(f"[INFO] Split into {len(docs_split)} chunks")

    # 4. Ensure persistence directory exists
    persist_dir = "/home/rishavupadhaya/Projects/Langchain_Prac/LeapFrog/Database/chromadb"
    os.makedirs(persist_dir, exist_ok=True)

    # 5. Define collection name for your vector store
    collection_name = "questions_analysis"

    return docs_split, persist_dir, collection_name
