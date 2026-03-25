# Load the documents

def load_documents():
    
    with open("doc1.md", "r", encoding="utf-8") as f:
        doc1 = f.read()
    
    with open("doc2.md", "r", encoding="utf-8") as f:
        doc2 = f.read()
    
    return [doc1, doc2]

# Add Chunking Function

def chunk_text(text, chunk_size=200):
    
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    
    return chunks

# Process All Documents

def process_documents(docs):
    
    all_chunks = []
    
    for doc in docs:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)
    
    return all_chunks