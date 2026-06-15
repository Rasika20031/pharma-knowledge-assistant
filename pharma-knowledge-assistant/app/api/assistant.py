from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import uuid

from app.services.agent import choose_tools
from app.services.tool_registry import TOOLS

from app.services.intent_classifier import (
    classify_intent
)

from app.services.memory_db import (
    save_memory,
    get_memory
)

router = APIRouter(tags=["Assistant"])


class AssistantRequest(BaseModel):
    question: str
    session_id: Optional[str] = None


@router.post("/assistant")
def assistant(request: AssistantRequest):

    # Auto-create session
    session_id = request.session_id

    if not session_id:
        session_id = str(uuid.uuid4())

    # Load memory
    memory = get_memory(session_id)

    print(f"Session ID: {session_id}")
    print(f"Memory Size: {len(memory)}")

    # Intent Classification
    intent = classify_intent(
        request.question
    )

    print(f"Intent: {intent}")

    # ------------------------
    # GREETING
    # ------------------------
    if intent == "GREETING":

        answer = "Hello! How can I help you today?"

        save_memory(
            session_id,
            request.question,
            answer
        )

        return {
            "session_id": session_id,
            "intent": intent,
            "answer": answer
        }

    # ------------------------
    # SHORT_VAGUE
    # ------------------------
    if intent == "SHORT_VAGUE":

        answer = (
            "Could you provide more details "
            "about what you'd like to know?"
        )

        save_memory(
            session_id,
            request.question,
            answer
        )

        return {
            "session_id": session_id,
            "intent": intent,
            "answer": answer
        }

    # ------------------------
    # OUT_OF_SCOPE
    # ------------------------
    if intent == "OUT_OF_SCOPE":

        answer = (
            "I can assist with pharmaceutical "
            "information, sales analytics "
            "and calculations."
        )

        save_memory(
            session_id,
            request.question,
            answer
        )

        return {
            "session_id": session_id,
            "intent": intent,
            "answer": answer
        }

    # ------------------------
    # BUSINESS / MEDICAL /
    # CALCULATION / COMPLEX
    # ------------------------

    tool_names = choose_tools(
        request.question
    )

    print(f"Selected Tools: {tool_names}")

    results = []

    for tool_name in tool_names:

        tool = TOOLS.get(tool_name)

        if not tool:
            continue

        tool_result = tool(
            request.question
        )

        print(f"{tool_name} Result:")
        print(tool_result)

        results.append(
            {
                "tool": tool_name,
                "result": tool_result
            }
        )

    save_memory(
        session_id,
        request.question,
        str(results)
    )

    return {
        "session_id": session_id,
        "memory_size": len(
            get_memory(session_id)
        ),
        "intent": intent,
        "tools_used": tool_names,
        "results": results
    }