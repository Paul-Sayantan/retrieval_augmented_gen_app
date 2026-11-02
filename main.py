# from src.config import (
#     AZURE_SEARCH_ENDPOINT,
#     AZURE_OPENAI_ENDPOINT,
#     AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
# )

# print("Configuration loaded successfully.")
# print("Search endpoint:", AZURE_SEARCH_ENDPOINT)
# print("OpenAI endpoint:", AZURE_OPENAI_ENDPOINT)
# print("Embedding deployment:", AZURE_OPENAI_EMBEDDING_DEPLOYMENT)

# from src.document_loader import load_pdf_documents

# documents = load_pdf_documents()

# print(f"Number of PDFs loaded: {len(documents)}")

# for document in documents:
#     print("File:", document["file_name"])
#     print("Extracted text length:", len(document["content"]))
#     print("Text preview:", document["content"][:300])

# from src.text_chunker import split_text

# for document in documents:
#     chunks = split_text(document["content"])
#     print("total chunks:", len(chunks))

#     for i,chunk in enumerate(chunks):
#         print(f"\nChunk {i+1}:")
#         print(chunk[:100])

# from src.embeddings import generate_embedding
# for document in documents:
#     chunks = split_text(document["content"])
#     first_chunk = chunks[0]

#     embedding = generate_embedding(first_chunk)
#     print("Embedding dimensions:", len(embedding))
#     print("First 5 embedding values:", embedding[:5])

# from src.index_manager import create_search_index
# create_search_index()

# from src.ingestion import ingest_documents
# ingest_documents()

# from src.retrieval import retrieve_documents
# question = "What experience does the candidate have with retrieval?"
# retrieve_documents(question)

# Expected result: Azure AI Search should return the three most relevant chunks for your question.
# Note: This uses vector search only. We'll add keyword + vector hybrid search and then connect Azure OpenAI to generate a natural-language answer from the retrieved chunks.

from src.answer_generator import generate_answer

question = "What experience does the candidate have with retrieval?"

answer = generate_answer(question)

print("\nGenerated Answer:")
print(answer)