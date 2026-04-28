# 📄 RAG AI Document Assistant

🚀 A production-style **Retrieval-Augmented Generation (RAG)** system that allows users to upload multiple PDFs and ask questions with **source-grounded AI answers**.

---

## 🌐 Live Demo

👉 https://rag-document-assistant-fk66kfih3bxb8ymaab8xzf.streamlit.app/

> ⚠️ Note: The live demo works best with **text-based PDFs**.
> OCR support for scanned PDFs is available in local setup.

---

## ✨ Why This Project?

* Implements a real-world **RAG pipeline** for document QA
* Provides **transparent answers with source context**
* Uses **semantic search (FAISS)** for accurate retrieval
* Designed with a **modular and scalable architecture**

---

## 🚀 Features

* 📤 Upload multiple PDF documents
* 🔍 Ask questions in natural language
* 🤖 AI-generated answers using OpenAI
* 📚 Source context display (explainability)
* 🧠 Confidence score for answers
* 📥 Download generated answers
* ⚡ Fast retrieval using FAISS

---

## 🧠 How It Works

This project implements a complete **RAG pipeline**:

### 1. Document Loading

* Extracts text using PyMuPDF
* (Optional) OCR fallback supported in local environments

### 2. Text Processing

* Cleaning & normalization
* Chunking with overlap

### 3. Embedding & Storage

* Sentence-transformer embeddings
* FAISS vector store

### 4. Retrieval & Generation

* Semantic search retrieves relevant chunks
* LLM generates grounded answers using retrieved context

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **LLM:** OpenAI (`gpt-4o-mini`)
* **Vector DB:** FAISS
* **Embeddings:** HuggingFace (MiniLM)
* **PDF Processing:** PyMuPDF
* **Framework:** LangChain

---

## 📸 Screenshots

### 🔹 User Interface

![UI](screenshots/ui.png)

### 🔹 AI Answer Output

![Answer](screenshots/answer.png)

### 🔹 Source Context

![Sources](screenshots/source.png)

---

## 📂 Project Structure

```
rag-document-assistant/
├── app.py
├── requirements.txt
├── src/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── generator.py
│   └── pipeline.py
├── screenshots/
├── notebooks/
```

---

## ⚙️ Quick Setup

```bash
git clone https://github.com/subesh-cse/rag-document-assistant.git
cd rag-document-assistant
pip install -r requirements.txt
setx OPENAI_API_KEY "your_api_key_here"
streamlit run app.py
```

---

## 🎯 Key Highlights

* Modular pipeline (loader → splitter → retriever → generator)
* Query-aware retrieval (summary vs factual queries)
* Source-grounded responses for reliability
* Clean Streamlit UI with real-time interaction

---

## 🔮 Future Improvements

* Chat history / conversational memory
* Reranking models for improved retrieval accuracy
* Cloud-compatible OCR integration
* Multi-format support (DOCX, TXT)
* Performance optimization & caching

---

## 👨‍💻 Author

**Subesh**
B.Tech CSE | Machine Learning Enthusiast


