from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from openai import OpenAI
import os

# -------------------------------
# 🔹 Load Embedding Model
# -------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')


# -------------------------------
# 🔹 OpenRouter Client (SECURE WAY)
# -------------------------------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
# -------------------------------
# 🔹 Create FAISS Index
# -------------------------------
def create_index(chunks):
    
    embeddings = model.encode(chunks)
    
    dim = embeddings.shape[1]
    
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    
    return index, embeddings


# -------------------------------
# 🔹 Retrieval Function
# -------------------------------
def retrieve(query, chunks, index, k=3):
    
    query_embedding = model.encode([query])
    
    distances, indices = index.search(query_embedding, k)
    
    results = [chunks[i] for i in indices[0]]
    
    return results


# -------------------------------
# 🔹 LLM Answer Generation
# -------------------------------
def generate_answer(query, context):
    
    prompt = f"""
You are an AI assistant for construction domain.

STRICT RULES:
- Answer ONLY from the provided context
- Do NOT use outside knowledge
- Keep the answer clear and concise
- If the answer is not present, respond EXACTLY with: I don't know

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="openrouter/free",  
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()


# -------------------------------
# 🔹 Full RAG Pipeline
# -------------------------------
def rag(query, chunks, index, k=3):
    
    retrieved_chunks = retrieve(query, chunks, index, k)
    
    context = "\n\n".join(retrieved_chunks)
    
    answer = generate_answer(query, context)
    
    return retrieved_chunks, answer