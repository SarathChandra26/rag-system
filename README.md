Simple RAG System (Retrieval Augmented Generation)
A clean, modular, and production-ready RAG pipeline built using Python, ChromaDB, SentenceTransformers, and OpenRouter LLMs.

This repository contains a moderate-complexity RAG system designed for academic projects, AI portfolios, research demonstrations, and practical learning. It follows a clear modular architecture, adheres to industry-aligned practices, and demonstrates a complete end-to-end RAG workflow—from document ingestion to LLM-powered response generation.

The goal of this project is to implement a reliable, simple, and professional RAG system that is easy to explain, extend, and deploy.

-------------------------------------------------
KEY FEATURES
-------------------------------------------------

1. PDF Ingestion
Extracts text from multi-page PDF documents with consistent formatting.

2. Intelligent Text Cleaning
Removes noise, extra spaces, and unwanted formatting.

3. Adaptive Document Chunking
Splits large text into meaningful segments while preserving semantic continuity.

4. High-Quality Embeddings
Uses all-MiniLM-L6-v2 for fast, accurate semantic embeddings.

5. Vector Database (ChromaDB)
Stores embeddings in a persistent ChromaDB instance (DuckDB + Parquet).

6. Context Retrieval
Retrieves the most relevant chunks using cosine similarity.

7. LLM Answer Generation
Uses OpenRouter with meta-llama/llama3-8b-instruct for contextual responses grounded in the retrieved content.

8. Clean, Modular Architecture
Well-separated modules for ingestion, embedding, retrieval, LLM generation, and orchestration.

-------------------------------------------------
SYSTEM ARCHITECTURE
-------------------------------------------------

PDF → Ingestion → Cleaning → Chunking → Embedding → Vector Database → Retrieval → LLM (OpenRouter) → Final Answer

This structure mirrors real-world production RAG workflows.

-------------------------------------------------
FOLDER STRUCTURE
-------------------------------------------------

rag_simple/
│ main.py
│ requirements.txt
│ .env
│ README.md
│
├── config/
│       settings.py
│
├── ingestion/
│       ingest.py
│       loader.py
│       cleaner.py
│       chunker.py
│       embedder.py
│
├── retriever/
│       vector_db.py
│       retriever.py
│
├── llm/
│       generator.py
│       prompts.py
│
└── orchestrator/
        rag_controller.py

-------------------------------------------------
INSTALLATION
-------------------------------------------------

1. Clone the repository:

git clone https://github.com/<your-username>/rag_simple
cd rag_simple

2. Install dependencies:

pip install -r requirements.txt

3. Configure environment variables:
Create a file named .env with the following content:

OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=meta-llama/llama3-8b-instruct
CHROMA_PERSIST_DIR=./chroma_db

The system is now ready.

-------------------------------------------------
USAGE
-------------------------------------------------

To ingest a PDF:

python main.py --ingest "E:\Notes\Unit1.pdf"

To ask a question:

python main.py --query "Explain the concept on page 3."

Example output:

ANSWER:
<LLM-generated, context-grounded response>

-------------------------------------------------
APPLICATIONS
-------------------------------------------------

• B.Tech/M.Tech Minor & Major Projects
• University AI/ML coursework
• Information retrieval experiments
• Portfolio projects
• Study assistant / exam preparation tool
• Demonstrating practical RAG knowledge

-------------------------------------------------
TECH STACK
-------------------------------------------------

• Python 3.8+
• SentenceTransformers (MiniLM)
• ChromaDB (duckdb+parquet backend)
• OpenRouter API
• pypdf

-------------------------------------------------
LICENSE
-------------------------------------------------

This project is licensed under the MIT License.

-------------------------------------------------
CONTRIBUTING
-------------------------------------------------

Contributions are welcome. Feel free to open issues or pull requests.

-------------------------------------------------
If this project helped you, please give it a star on GitHub!
-------------------------------------------------
