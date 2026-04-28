import streamlit as st
import os
import shutil

from src.pipeline import build_vector_store, run_query


# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="RAG AI Assistant",
    page_icon="📄",
    layout="centered"
)


# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("📌 About")
st.sidebar.write("""
This app allows you to:
- Upload one or more PDFs
- Ask questions
- Get AI-powered answers

Built using:
- RAG (Retrieval-Augmented Generation)
- FAISS Vector Store
- OpenAI API
""")


# -------------------------------
# Main Header
# -------------------------------
st.markdown("# 📄 RAG AI Document Assistant")
st.markdown("### 🔍 Ask questions from your PDFs using AI")

st.divider()


# -------------------------------
# Upload Section
# -------------------------------
st.subheader("📤 Upload Documents")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type="pdf",
    accept_multiple_files=True
)


# -------------------------------
# Query Section
# -------------------------------
st.subheader("💬 Ask a Question")

query = st.text_input(
    "Type your question here...",
    placeholder="e.g. Summarize this document in 3 points",
    disabled=not uploaded_files
)

st.divider()


# -------------------------------
# Session State Handling
# -------------------------------
if uploaded_files:
    current_files = [file.name for file in uploaded_files]

    if "last_uploaded" not in st.session_state:
        st.session_state.last_uploaded = None

    if current_files != st.session_state.last_uploaded:
        st.session_state.vector_store = None
        st.session_state.last_uploaded = current_files


# -------------------------------
# Processing
# -------------------------------
if uploaded_files:

    TEMP_DIR = "temp_pdfs"

    if "vector_store" not in st.session_state or st.session_state.vector_store is None:

        with st.spinner("📊 Processing documents..."):

            if os.path.exists(TEMP_DIR):
                shutil.rmtree(TEMP_DIR)

            os.makedirs(TEMP_DIR, exist_ok=True)

            for i, uploaded_file in enumerate(uploaded_files):
                file_path = os.path.join(TEMP_DIR, f"{i}_{uploaded_file.name}")

                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

            st.session_state.vector_store = build_vector_store(TEMP_DIR)

        st.success("✅ Documents processed successfully!")


    # -------------------------------
    # Query Processing
    # -------------------------------
    if query:

        with st.spinner("🔍 Searching for answer..."):

            vector_store = st.session_state.vector_store
            result = run_query(vector_store, query)

            answer = result["answer"]
            docs = result["sources"]
            confidence = result.get("confidence", 0)

        # Answer
        st.markdown("## 🤖 Answer")
        st.write(answer)

        # Confidence
        if confidence > 0.7:
            st.success(f"Confidence: {confidence * 100:.0f}%")
        elif confidence > 0.4:
            st.warning(f"Confidence: {confidence * 100:.0f}%")
        else:
            st.error(f"Confidence: {confidence * 100:.0f}%")

        # Download
        st.download_button(
            label="📥 Download Answer",
            data=answer,
            file_name="answer.txt",
            mime="text/plain"
        )

        st.divider()

        # Sources
        st.markdown("## 📚 Source Context")

        for i, d in enumerate(docs):
            with st.expander(f"📄 Source {i+1}"):

                st.markdown(f"**File:** {d.metadata.get('source', 'Unknown')}")

                preview = d.page_content[:300] + "..."
                st.markdown(f"**Preview:**\n\n{preview}")

    else:
        st.info("💡 Enter a question to query the documents.")

else:
    st.info("📂 Please upload at least one PDF.")
