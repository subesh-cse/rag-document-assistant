from src.loader import load_documents_from_folder
from src.splitter import split_documents
from src.embeddings import create_vector_store
from src.retriever import get_retriever
from src.generator import generate_answer


# 🔹 Step 1: Build vector store
def build_vector_store(folder_path):
    print("📂 Folder path:", folder_path)

    documents = load_documents_from_folder(folder_path)
    print("📄 Documents loaded:", len(documents))

    chunks = split_documents(documents)
    print("🧩 Chunks created:", len(chunks))

    if not chunks:
        raise ValueError("❌ No chunks created. PDF loading failed.")

    vector_store = create_vector_store(chunks)
    return vector_store


# 🔹 Step 2: Run query
def run_query(vector_store, query):
    retriever = get_retriever(vector_store)

    docs = retriever.invoke(query)

    # 🔥 Smart query detection
    q = query.lower()
    if any(k in q for k in ["summary", "main idea", "overview", "summarize", "explain document"]):
        docs = docs[:6]
    else:
        docs = docs[:3]

    if not docs:
        return {
            "answer": "No relevant information found.",
            "sources": [],
            "confidence": 0.0
        }

    # Confidence
    max_docs = 6
    confidence = len(docs) / max_docs
    confidence = round(min(confidence, 1.0), 2)

    # Build context
    context = "\n\n".join([
        f"[Source: {doc.metadata.get('source','unknown')}]\n{doc.page_content}"
        for doc in docs
    ])

    answer = generate_answer(context, query)

    return {
        "answer": answer,
        "sources": docs,
        "confidence": confidence
    }