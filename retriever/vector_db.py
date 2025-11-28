import chromadb
from chromadb.config import Settings
from config.settings import CHROMA_PERSIST_DIR

client = chromadb.Client(
    Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory=CHROMA_PERSIST_DIR
    )
)

def get_collection():
    return client.get_or_create_collection("rag_docs")
