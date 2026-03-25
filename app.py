import streamlit as st
from data_loader import load_documents, process_documents
from rag_pipeline import create_index, rag

# -------------------------------
# 🔹 Page Config
# -------------------------------
st.set_page_config(page_title="Mini RAG Assistant", layout="wide")

# -------------------------------
# 🔹 Title
# -------------------------------
st.title("🏗️ Construction RAG Assistant")
st.markdown("Ask questions based on internal construction documents")

st.divider()

# -------------------------------
# 🔹 Clean Markdown Text (IMPORTANT FIX)
# -------------------------------
def clean_text(text):
    # Remove markdown headings and extra symbols
    text = text.replace("#", "")
    text = text.replace("##", "")
    text = text.replace("###", "")
    return text.strip()

# -------------------------------
# 🔹 Load Data (Cached)
# -------------------------------
@st.cache_resource
def load_data():
    docs = load_documents()
    chunks = process_documents(docs)
    index, _ = create_index(chunks)
    return chunks, index

chunks, index = load_data()

# -------------------------------
# 🔹 Input
# -------------------------------
query = st.text_input("💬 Enter your question:")

# -------------------------------
# 🔹 No Input Handling
# -------------------------------
if not query:
    st.warning("Please enter a question to proceed.")

# -------------------------------
# 🔹 Process Query
# -------------------------------
if query:
    with st.spinner("Thinking... 🤖"):
        retrieved_chunks, answer = rag(query, chunks, index)

    # ---------------------------
    # 🔹 Display Context
    # ---------------------------
    st.subheader("📄 Retrieved Context")

    for i, chunk in enumerate(retrieved_chunks):
        st.markdown(f"**📄 Context {i+1}:**")
        st.info(clean_text(chunk))   # ✅ cleaned text

    # ---------------------------
    # 🔹 Display Answer
    # ---------------------------
    st.subheader("🤖 Final Answer")
    st.success(answer)

# -------------------------------
# 🔹 Footer
# -------------------------------
st.divider()
st.caption("Built using RAG + FAISS + MiniLM + OpenRouter (Free LLM)")