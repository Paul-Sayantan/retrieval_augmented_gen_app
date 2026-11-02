# What this does:
# - Finds PDF files in documents/.
# - Extracts text from every page.
# - Stores each PDF's filename and extracted text.
# - Returns the documents as a Python list.

from pathlib import Path
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS_FOLDER = PROJECT_ROOT / "documents"


def load_pdf_documents():
    documents = []

    for pdf_path in DOCUMENTS_FOLDER.glob("*.pdf"):
        reader = PdfReader(pdf_path)

        text = "\n".join(
            page.extract_text() or "" for page in reader.pages
        )

        documents.append({
            "file_name": pdf_path.name,
            "content": text,
        })

    return documents