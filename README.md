# 🏗️ Mini RAG Assistant

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system for answering construction-related queries using internal company documents.

The system retrieves relevant document chunks and generates **grounded answers strictly from retrieved context**, ensuring transparency and minimizing hallucinations.

---

## ⚙️ Architecture
User Query → Embedding → FAISS Retrieval → LLM → Answer

---

## 🧠 Models Used
- **Embedding Model:** all-MiniLM-L6-v2 (sentence-transformers)  
- **LLM:** OpenRouter Free Model (Mistral-7B)

### Why these models?
- Lightweight and fast embedding model  
- Free LLM (cost-efficient and meets assignment requirement)  
- Good balance between performance and efficiency  

---

## 🔑 Key Features
- Semantic search using FAISS  
- Context-grounded answer generation  
- Transparent output (retrieved chunks + answer)  
- Streamlit-based chatbot interface  
- Cost-efficient (uses free LLM)

---

## ⚙️ How it Works
1. Documents are split into smaller chunks (~200 words)  
2. Each chunk is converted into embeddings  
3. FAISS index is created for similarity search  
4. User query is embedded and matched with top-k chunks  
5. LLM generates answer strictly from retrieved context  

---

## 🔍 Grounding Strategy
The LLM is explicitly instructed to:
- Answer **only from retrieved context**  
- Avoid using external knowledge  
- Return **"I don't know"** if the answer is not present  

This ensures:
✔ No hallucination  
✔ High reliability  
✔ Controlled output  

---

## 🔎 Transparency
The system explicitly displays:
- 📄 Retrieved document chunks  
- 🤖 Final generated answer  

This allows users to verify how the answer was derived.

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py