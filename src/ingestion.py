# We have:
# 1. Extracted text from PDFs.
# 2. Split the text into chunks.
# 3. Generated embeddings.
# 4. Created an Azure AI Search vector index.
# Now we connect these steps and upload each chunk, 
# along with its embedding, to Azure AI Search.

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from src.config import AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY
from src.index_manager import INDEX_NAME
from src.document_loader import load_pdf_documents
from src.text_chunker import split_text
from src.embeddings import generate_embedding

credential = AzureKeyCredential(AZURE_SEARCH_KEY)

search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=INDEX_NAME,
    credential=credential,
)
def ingest_documents():
    documents = load_pdf_documents()

    search_documents = []
    for document in documents:
        chunks = split_text(document["content"])

        for i, chunk in enumerate(chunks):
            embedding = generate_embedding(chunk)
            search_documents.append({
                "id": f"{document['file_name'].replace('.', '_')}-{i}",
                "file_name": document["file_name"],
                "content": chunk,
                "content_vector": embedding,
            })
    if search_documents:
        result = search_client.upload_documents(
            documents=search_documents
        )
        print(f"Uploaded {len(result)} chunks.")
        for item in result:
            print(f"Document upload successful: {item.succeeded}")
        else:
            print("No documents found to upload.")
