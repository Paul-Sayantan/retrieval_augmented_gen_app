from openai import AzureOpenAI

from src.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_API_VERSION,

    AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
)

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)

def generate_embedding(text):
    response = client.embeddings.create(
        input=text,
        model = AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
    )
    return response.data[0].embedding