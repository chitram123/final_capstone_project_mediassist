from fastapi import APIRouter

from rag.retriever import retrieve_chunks
from llm import generate_answer

router = APIRouter()

@router.post("/chat")
async def chat(data: dict):

    question = data["question"]

    chunks = retrieve_chunks(question)

    answer = generate_answer(
        question,
        chunks
    )

    return {
        "answer": answer
    }