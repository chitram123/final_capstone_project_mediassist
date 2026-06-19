from sentence_transformers import CrossEncoder

# Load reranker model
reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_chunks(question, retrieved_chunks, top_k=3):

    # Create question-chunk pairs
    pairs = [
        [question, chunk]
        for chunk in retrieved_chunks
    ]

    # Calculate relevance scores
    scores = reranker_model.predict(pairs)

    # Combine chunks and scores
    ranked_results = list(
        zip(retrieved_chunks, scores)
    )

    # Sort by score descending
    ranked_results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # Return top chunks
    return ranked_results[:top_k]