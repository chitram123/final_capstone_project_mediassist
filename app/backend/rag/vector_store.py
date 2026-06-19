import faiss
import numpy as np
import pickle
import os

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../"
        )
    )

def create_faiss_index(embeddings):
    dimension = 384
    
    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings
    index.add(embeddings)

    # Save FAISS index
  
    vector_store_path = os.path.join(
    BASE_DIR,
    "vector_store",
    "faiss_index"
    )

    faiss.write_index(
        index,
        vector_store_path
    )
    print("FAISS index created successfully")

    return index


def save_chunks(text_chunks):

    chunks_path = os.path.join(
        BASE_DIR,
        "vector_store",
        "chunks.pkl"

    )

    with open(
        chunks_path,
        "wb"
    ) as f:

        pickle.dump(
            text_chunks,
            f
        )

    print("Chunks saved successfully")



