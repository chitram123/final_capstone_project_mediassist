#Current reranking approach:
#The system currently relies on FAISS similarity scores to rank retrieved chunks.
#The top 3 most similar chunks are selected and returned as context for processing.

import faiss
import pickle
import numpy as np
import os

from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../"
        )
    )

# Load embedding model
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def retrieve_chunks(question, k=3):

    vector_store_path = os.path.join(
    BASE_DIR,
    "vector_store",
    "faiss_index"
    )
    chunk_path = os.path.join(
    BASE_DIR,
    "vector_store",
    "chunks.pkl"
)
    # Load FAISS index
    index = faiss.read_index(
        vector_store_path
    )

    # Load chunks
    with open(
        chunk_path,
        "rb"
    ) as f:

        text_chunks = pickle.load(f)

    # Create question embedding
    question_embedding = embedding_model.encode(
        [question]
    )

    # Search FAISS
    distances, indices = index.search(
        np.array(question_embedding).astype("float32"),
        k
    )

    retrieved_chunks = []

    for i in indices[0]:

        # FAISS can return -1
        if i != -1:
            retrieved_chunks.append(text_chunks[i])

    return retrieved_chunks
