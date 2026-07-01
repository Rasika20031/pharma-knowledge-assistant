from app.services.retrieval import retrieve_context
from app.services.generation import generate_answer

from app.services.sql_generator import generate_sql
from app.services.sql_executor import execute_sql
from app.services.sql_answer_generator import generate_sql_answer
from app.services.query_rewriter import (
    rewrite_query
)
import os



def rag_tool(question: str):

    rewritten_question = (
        rewrite_query(
            question
        )
    )

    print("\n" + "=" * 50)

    print(
        "ORIGINAL QUESTION:"
    )

    print(question)

    print(
        "\nREWRITTEN QUESTION:"
    )

    print(
        rewritten_question
    )

    print("=" * 50)

    documents, metadata = retrieve_context(
        rewritten_question
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
                    item.get(
                        "source",
                        ""
                    )
                ),
                "page": item.get(
                    "page",
                    "Unknown"
                )
            }

            if (
                source_info
                not in unique_sources
            ):

                unique_sources.append(
                    source_info
                )

    return {
        "answer": answer,
        "sources": unique_sources[:1]
    }


def sql_tool(question: str):

    print("\n==========================")
    print("SQL TOOL")
    print("==========================")

    sql_query = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql_query)

    result = execute_sql(sql_query)

    print("\nSQL Result:")
    print(result)

    answer = generate_sql_answer(
        question,
        sql_query,
        result
    )

    print("\nGenerated Answer:")
    print(answer)

    return {
        "sql": sql_query,
        "result": result,
        "answer": answer,
        "source": "sales.db"
    }