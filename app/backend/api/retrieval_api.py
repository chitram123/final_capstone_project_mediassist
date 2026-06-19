from fastapi import APIRouter

from rag.retriever import retrieve_chunks

router = APIRouter()

@router.post("/retrieve")
async def retrieve(data: dict):

    question = data["question"]

    chunks = retrieve_chunks(question)

    return {
        "retrieved_chunks": chunks
    }