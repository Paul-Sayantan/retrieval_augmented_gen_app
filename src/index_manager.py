# We have generated embeddings for our PDF chunks. 
# Now we need a place in Azure AI Search to store 
# those chunks and their vectors.
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
)
from src.config import AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY
INDEX_NAME = "local-rag-index"
credential = AzureKeyCredential(AZURE_SEARCH_KEY)

index_client = SearchIndexClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    credential=credential,
)
def create_search_index():
    fields = [
        SearchField(
            name="id", #	Unique identifier for each chunk
            type=SearchFieldDataType.String,
            key=True,
        ),
        SearchField(
            name="file_name", #     Original PDF filename
            type=SearchFieldDataType.String,
            filterable=True,
        ),
        SearchField(
            name="content", #       Extracted text chunk
            type=SearchFieldDataType.String,
            searchable=True,
        ),
        SearchField(
            name="content_vector", #      Embedding vector
            type=SearchFieldDataType.Collection(
                SearchFieldDataType.Single
            ),
            searchable=True,
            vector_search_dimensions=1536,
            vector_search_profile_name="my-vector-profile",
        ),
    ]
    vector_search = VectorSearch(
        algorithms=[
            HnswAlgorithmConfiguration(name="my-hnsw")
        ],
        profiles=[
            VectorSearchProfile(
                name="my-vector-profile",
                algorithm_configuration_name="my-hnsw",
            )
        ],
    )
    index = SearchIndex(
        name=INDEX_NAME,
        fields=fields,
        vector_search=vector_search,
    )
    index_client.create_or_update_index(index)
    print(f"Search index '{INDEX_NAME}' created successfully.")

        