from rag.document_loader import load_doc
from rag.chunking import create_chunks
from rag.embeddings import create_embeddings
from rag.vector_store import (
    create_faiss_index,
    save_chunks
)


def ingest_document(file_path):

    #load doc
    documents = load_doc(file_path)
    
    #create chunks
    chunks = create_chunks(documents)

     # Extract text
    text_chunks = []

    for chunk in chunks:
        text_chunks.append(chunk.page_content)

    # Create embeddings
    embeddings = create_embeddings(text_chunks)

    # Create vector store
    create_faiss_index(embeddings)

    # Save chunks
    save_chunks(text_chunks)

    return len(text_chunks)