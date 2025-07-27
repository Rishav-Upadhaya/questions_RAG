# RAG Agent

This is a question-answering system for analyzing educational questions. It uses large language models (LLMs) and document search to answer user questions based on PDF files you provide. The system is modular and can be extended with new tools or document stores.

---

## Table of Contents
- [What is this?](#what-is-this)
- [Main Features](#main-features)
- [How it Works (Architecture)](#how-it-works-architecture)
- [Installation](#installation)
- [Setup and Configuration](#setup-and-configuration)
- [How to Use](#how-to-use)
- [How to Extend or Customize](#how-to-extend-or-customize)
- [Dependencies](#dependencies)

---

## What is this?
This tool answers questions about educational content. It reads PDF files you put in a folder, stores their content in a vector database, and uses a language model to answer your questions. It is designed for analyzing question patterns, trends, and making predictions about future questions.

## Main Features
- Answers questions using your own PDF documents.
- Finds and analyzes repeated questions, topics, and trends.
- Predicts possible future questions based on past data.
- Uses Google Gemini LLM for high-quality answers.
- Stores document data in ChromaDB (or pgvector, if you want).
- Easy to add new tools or change the workflow.
- Command-line interface for direct use.

## How it Works

- The user types a question.
- The LLM decides if it needs to search your documents.
- If yes, it uses the retriever tool to find relevant text from your PDFs.
- The LLM uses this information to answer your question.
- The process repeats if needed, until the LLM is ready to answer.

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rishav-Upadhaya/questions_RAG.git
   cd questions_RAG
   ```
2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables**
   - Create a file named `.env` in the project root folder.
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
   - If you want to use pgvector, also add:
     ```
     DATABASE_URL=your_pgvector_connection_string
     ```
4. **Add your PDF files**
   - Put all the PDF files you want to analyze in the folder: `Database/questions/`

## Setup and Configuration

- You can change:
  - Which LLM model to use
  - LLM temperature (controls randomness)
  - Embedding model for document search
  - PDF chunk size and overlap (how documents are split)
  - Where to store the vector database
  - How many results to return from search
- You can also change how documents are loaded and split in `src/utils/doc_loader.py`.

## How to Use

### Command-Line (Recommended)
Run this command in your terminal:
```bash
python src/main.py
```
- The program will ask you to type a question.
- Type your question and press Enter.
- To stop, type `exit` or `quit` and press Enter.

### Programmatic Use
You can also use this in your own Python code:
```python
from src.main import running_agent

running_agent()  # Starts the interactive question-answering loop
```

## How to Extend or Customize

### Add a New Tool
- Create a new file in `src/tools/` for your tool.
- Add your tool to the list in `src/tools/tools.py`.
- If needed, update the workflow in `src/utils/graph.py` to use your tool.

### Change the System Prompt
- Edit `src/utils/systemprompt.py`.
- The prompt controls how the LLM answers and what style it uses.

### Use a Different Vector Store
- By default, this uses ChromaDB (`src/db/chromadb.py`).
- To use pgvector, see `src/db/pgvector.py` and update the retriever in `src/tools/retriever.py`.

### Change State or Workflow
- The agent's state is defined in `src/state/models.py`.
- The workflow (which steps the agent takes) is in `src/utils/graph.py`.

## Dependencies
- `langchain-core`
- `langchain-google-genai`
- `langchain-community`
- `langchain-chroma`
- `langgraph`
- `chromadb`
- `pypdf`
- `python-dotenv`

See `requirements.txt` for exact versions.
