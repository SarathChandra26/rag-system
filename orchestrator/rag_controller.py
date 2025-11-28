from retriever.retriever import retrieve
from llm.generator import generate_answer

def rag_answer(query):
    retrieved = retrieve(query, top_k=3)
    context = "\n\n".join(retrieved)
    answer = generate_answer(query, context)
    return answer
