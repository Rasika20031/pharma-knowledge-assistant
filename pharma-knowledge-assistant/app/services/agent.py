import requests

def choose_tools(question: str):

    question_lower = question.lower()

    selected_tools = []

    sql_keywords = [
        "sales",
        "revenue",
        "count",
        "total",
        "highest",
        "lowest",
        "average",
        "performance"
    ]

    rag_keywords = [
        "indication",
        "side effect",
        "side effects",
        "used for",
        "drug",
        "treatment"
    ]

    calculator_keywords = [
        "+",
        "-",
        "*",
        "/",
        "calculate",
        "multiply",
        "divide"
    ]

    if any(word in question_lower for word in sql_keywords):
        selected_tools.append("SQL_TOOL")

    if any(word in question_lower for word in rag_keywords):
        selected_tools.append("RAG_TOOL")

    if any(word in question_lower for word in calculator_keywords):
        selected_tools.append("CALCULATOR_TOOL")

    if not selected_tools:
        selected_tools.append("RAG_TOOL")

    return selected_tools