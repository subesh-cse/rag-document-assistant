# 📄 RAG AI Document Assistant

🚀 A production-style **Retrieval-Augmented Generation (RAG)** system that lets users upload multiple PDFs and ask questions with **source-grounded AI answers**.

🔗 **Live Demo:** *(Add your Streamlit link here after deployment)*

---

## ✨ Why This Project?

* Handles **real-world PDFs** (including scanned documents via OCR)
* Provides **transparent answers with source context**
* Uses **semantic search (FAISS)** for accurate retrieval
* Designed with a **modular, scalable architecture**

---

## 🚀 Features

* 📤 Upload multiple PDF documents
* 🔍 Ask questions in natural language
* 🤖 AI-generated answers using OpenAI
* 📚 Source context display (explainability)
* 🧠 Confidence score for answers
* 📥 Download generated answers
* ⚡ Fast retrieval using FAISS
* 🧾 OCR fallback for scanned PDFs

---

## 🧠 How It Works

This project implements a full **RAG pipeline**:

1. **Document Loading**

   * PyMuPDF extraction
   * OCR fallback (Tesseract)

2. **Text Processing**

   * Cleaning & normalization
   * Chunking with overlap

3. **Embedding & Storage**

   * Sentence-transformer embeddings
   * FAISS vector store

4. **Retrieval & Generation**

   * Semantic search retrieves relevant chunks
   * LLM generates grounded answer with sources

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **LLM:** OpenAI (`gpt-4o-mini`)
* **Vector DB:** FAISS
* **Embeddings:** HuggingFace (MiniLM)
* **PDF Processing:** PyMuPDF + Tesseract OCR
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

* Robust **OCR fallback** for scanned PDFs
* Modular architecture (loader → splitter → retriever → generator)
* Query-aware retrieval (summary vs factual queries)
* Source-grounded answers for reliability
* Streamlit UI with real-time interaction

---

## 🔮 Future Improvements

* Chat history / conversational memory
* Reranking models (better retrieval quality)
* Multi-format support (DOCX, TXT)
* Cloud deployment & scaling

---

## 👨‍💻 Author

**Subesh**
B.Tech CSE | Machine Learning Enthusiast

