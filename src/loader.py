import os
import re
from langchain_community.document_loaders import PyMuPDFLoader


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text.strip()


def load_documents_from_folder(folder_path):
    all_docs = []

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)

            loader = PyMuPDFLoader(file_path)
            docs = loader.load()

            for doc in docs:
                text = clean_text(doc.page_content)

                if len(text.split()) > 10:
                    doc.page_content = text
                    doc.metadata["source"] = file
                    all_docs.append(doc)

    if not all_docs:
        raise ValueError("No readable text found in PDFs. Try a text-based PDF.")

    return all_docs