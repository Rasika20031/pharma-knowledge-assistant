from app.services.retrieval import retrieve_context
from app.services.generation import generate_answer

from app.services.sql_generator import generate_sql
from app.services.sql_executor import execute_sql
from app.services.sql_answer_generator import generate_sql_answer

import os


def rag_tool(question: str):

    documents, metadata = retrieve_context(
        question
    )

    context = "\n".join(
        documents
    )

    answer = generate_answer(
        question,
        context
    )

    # If answer not found, don't return sources
    if (
        "could not find" in answer.lower()
        or "not found in the uploaded documents" in answer.lower()
    ):
        return {
            "answer": answer,
            "sources": []
        }

    unique_sources = []

    for item in metadata:

        if item:

            source_info = {
                "document": os.path.basename(
                    item.get("source", "")
                ),
                "page": item.get(
                    "page",
                    "Unknown"
                )
            }

            if source_info not in unique_sources:

                unique_sources.append(
                    source_info
                )

    return {
        "answer": answer,
        "sources": unique_sources
    }


def sql_tool(question: str):

    sql_query = generate_sql(
        question
    )

    result = execute_sql(
        sql_query
    )

    answer = generate_sql_answer(
        question,
        sql_query,
        result
    )

    return {
        "sql": sql_query,
        "result": result,
        "answer": answer
    }