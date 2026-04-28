import os
import re
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
import pytesseract
from PIL import Image
import fitz  # PyMuPDF


# ✅ Set your Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\subes\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def clean_text(text):
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    return text.strip()


def load_documents_from_folder(folder_path):
    all_docs = []

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)

            print(f"\n📄 Processing: {file}")

            loader = PyMuPDFLoader(file_path)

            try:
                docs = loader.load()
                print(f"➡ PyMuPDF pages: {len(docs)}")
            except Exception as e:
                print(f"❌ PyMuPDF failed: {e}")
                docs = []

            valid_docs = []

            # 🔹 Try normal extraction
            for doc in docs:
                text = clean_text(doc.page_content)

                if len(text.split()) > 10:
                    doc.page_content = text
                    doc.metadata["source"] = file
                    valid_docs.append(doc)

            # 🔥 OCR fallback
            if not valid_docs:
                print("⚠️ Using OCR...")

                pdf = fitz.open(file_path)

                for i, page in enumerate(pdf):
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                    text = pytesseract.image_to_string(img, config="--psm 6")
                    text = clean_text(text)

                    if len(text.split()) > 10:
                        valid_docs.append(
                            Document(
                                page_content=text,
                                metadata={"source": file, "page": i}
                            )
                        )

                pdf.close()

            print(f"✅ Final extracted pages: {len(valid_docs)}")

            all_docs.extend(valid_docs)

    print("\n📊 Total valid docs:", len(all_docs))

    return all_docs