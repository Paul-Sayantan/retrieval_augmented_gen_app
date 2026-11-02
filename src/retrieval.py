# When a user asks a question, we need to:
# 1. Convert the question into an embedding.
# 2. Search Azure AI Search for similar document vectors.
# 3. Return the most relevant text chunks.

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery

from src.config import AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY
from src.index_manager import INDEX_NAME
from src.embeddings import generate_embedding

credential = AzureKeyCredential(AZURE_SEARCH_KEY)


search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=INDEX_NAME,
    credential=credential,
)

def retrieve_documents(question):
    question_embedding = generate_embedding(question)
    vector_query = VectorizedQuery(
        vector=question_embedding,
        fields="content_vector",
        k_nearest_neighbors=3, 	# Retrieves three nearest vector matches
    )
    results = search_client.search(
        search_text=question, # performs keyword search
        vector_queries=[vector_query], # performs vector search
        select=["file_name", "content"],
        top=3,                         # Returns up to three combined results
    )
    documents = []

    for result in results:
        documents.append({
            "file_name": result["file_name"],
            "content": result["content"],
        })

    return documents

    # for result in results:
    #     print("\nFile:", result["file_name"])
    #     print("Relevant content:", result["content"])
    #     print("Search score:", result["@search.score"]) # 	Shows the combined search ranking score