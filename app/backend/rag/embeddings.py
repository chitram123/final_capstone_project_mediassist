from sentence_transformers import SentenceTransformer
import numpy as np

# Initialize embedding model
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def create_embeddings(text_chunks):
    embeddings = embedding_model.encode(
        text_chunks,
        show_progress_bar=True
    )
    return np.array(embeddings).astype("float32")