# So far, Azure AI Search retrieves relevant chunks. Now we'll send those chunks and the user's question to an Azure OpenAI chat model to generate an answer.

# Our flow:

# Question → Hybrid Search → Relevant chunks → Azure OpenAI → Answer


from openai import AzureOpenAI
from src.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_CHAT_DEPLOYMENT,
)
from src.retrieval import retrieve_documents 

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)
def generate_answer(question):
    documents = retrieve_documents(question) #Retrieves relevant chunks from Azure AI Search

    if not documents:
        return "No relevant documents found."
    context = ""                             # Combines retrieved chunks into one text
    for document in documents:
        context += document["content"] + "\n\n"

    response = client.chat.completions.create(   # Generates the answer
        model=AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=[
            {
                "role": "system",  # Gives instructions to the chat model
                "content": (
                    "Answer the question using only the "
                    "provided context. If the answer is not "
                    "available, say you don't have enough information."
                ),
            },
             {
                "role": "user",   # Sends context and the question
                "content": f"Context:\n{context}\nQuestion: {question}",
            },
        ],
    )
    return response.choices[0].message.content  # Returns the generated answer