#character based chunking has bad output
#so implementing sentence aware chunking

import re

def split_text(text, chunk_size=1000, overlap=1):
    sentences = re.split(r"(?<=[.!?])\s+|\n+", text.strip())
    chunks=[]
    current_chunk = []

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        current_length = sum(len(s) for s in current_chunk)

        if current_chunk and current_length + len(sentence) > chunk_size:
            chunks.append(" ".join(current_chunk))

            current_chunk = current_chunk[-overlap:]

        current_chunk.append(sentence)

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks



    
    return chunks