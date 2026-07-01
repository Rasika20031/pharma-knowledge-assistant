from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import uuid
from app.services.planner import create_plan
from app.services.executor import execute_plan
# from app.services.agent import choose_tools
# from app.services.tool_registry import TOOLS

from app.services.response_generator import generate_response

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

    print("\nMEMORY:")
    print(memory)



# ------------------------
# FOLLOW-UP DETECTION
# ------------------------

    question = request.question

    follow_up_words = [
        "it",
        "its",
        "they",
        "them",
        "their"
    ]

    if memory:

        last_question = None

        for item in reversed(memory):

            previous_question = item[
                "question"
            ]

            if (
                previous_question.lower()
                != question.lower()
            ):

                last_question = (
                    previous_question
                )

                break

        if (
            last_question
            and any(
                word in question.lower().split()
                for word in follow_up_words
            )
        ):

            question = (
                f"{question} "
                f"Regarding: {last_question}"
            )

            print(
                "\nFOLLOW-UP DETECTED:"
            )

            print(
                question
            )
    



    # ------------------------
    # INTENT CLASSIFICATION
    # ------------------------

    intent = classify_intent(
        question
    )

    print(f"Intent: {intent}")





    # ------------------------
    # EXECUTION PLAN
    # ------------------------

    plan = create_plan(
        question,
        intent
    )

    print("\n==============================")
    print("EXECUTION PLAN")
    print("==============================")

    for index, step in enumerate(
        plan["steps"],
        start=1
    ):

        print(
            f"Step {index}: {step}"
        )

    # ------------------------
    # GREETING
    # ------------------------

    if intent == "GREETING":

        answer = (
            "Hello! How can I help you today?"
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

    tool_names, results = execute_plan(
        question,
        plan
    )
    final_answer = generate_response(results)
    save_memory(
        session_id,
        request.question,
        final_answer
    )
    

    return {
        "session_id": session_id,
        "memory_size": len(
            get_memory(session_id)
        ),
        "intent": intent,
        "plan": plan,
        "tools_used": tool_names,
        "answer": final_answer,
        "results": results
    }