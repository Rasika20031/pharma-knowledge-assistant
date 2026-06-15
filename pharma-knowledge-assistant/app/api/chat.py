from fastapi import APIRouter
from pydantic import BaseModel

from app.services.retrieval import retrieve_context
from app.services.generation import generate_answer

from app.services.memory import (
    add_to_memory,
    get_memory
)

router = APIRouter(tags=["Chat"])


class ChatRequest(BaseModel):
    session_id: str
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    # Retrieve chunks + metadata
    retrieved = retrieve_context(
        request.question
    )

    # Build context
    context = "\n".join(
        retrieved["documents"]
    )

    # Get memory
    memory = get_memory(
        request.session_id
    )

    # Generate answer using Ollama
    answer = generate_answer(
        request.question,
        context
    )

    # Store interaction
    add_to_memory(
        request.session_id,
        request.question,
        answer
    )

    # Updated memory
    updated_memory = get_memory(
        request.session_id
    )

    # Extract unique sources
    sources = []

    for item in retrieved["metadata"]:

        if item:

            source = item.get("source")

            if source and source not in sources:

                sources.append(source)

    return {
        "session_id": request.session_id,
        "question": request.question,
        "answer": answer,
        "sources": sources,
        "memory_size": len(updated_memory)
    }