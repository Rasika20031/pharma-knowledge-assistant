def choose_tools(question: str):

    question_lower = question.lower()

    selected_tools = []

    # ------------------------
    # SQL KEYWORDS
    # ------------------------

    sql_keywords = [
        "sales",
        "revenue",
        "count",
        "total",
        "highest",
        "lowest",
        "average",
        "performance",
        "sum",
        "doctor",
        "hcp",
        "customer",
        "territory",
        "region",
        "visit",
        "visits",
        "call",
        "calls",
        "sell",
        "sell out",
        "market",
        "brand",
        "prescription",
        "prescriptions",
        "growth",
        "trend",
        "report",
        "list",
        "show",
        "top",
        "bottom"
    ]

    # ------------------------
    # RAG KEYWORDS
    # ------------------------

    rag_keywords = [
        "drug",
        "medicine",
        "medication",
        "tablet",
        "used for",
        "treatment",
        "indication",
        "contraindication",
        "mechanism",
        "mechanism of action",
        "side effect",
        "side effects",
        "dosage",
        "dose",
        "symptoms",
        "disease",
        "clinical",
        "adverse",
        "benefits"
    ]

    # ------------------------
    # CALCULATOR KEYWORDS
    # ------------------------

    calculator_keywords = [
        "+",
        "-",
        "*",
        "/",
        "calculate",
        "multiply",
        "divide",
        "percentage",
        "percent",
        "growth",
        "increase",
        "decrease"
    ]

    # ------------------------
    # SQL ROUTING
    # ------------------------

    if any(keyword in question_lower for keyword in sql_keywords):
        selected_tools.append("SQL_TOOL")

    # ------------------------
    # RAG ROUTING
    # ------------------------

    if any(keyword in question_lower for keyword in rag_keywords):
        selected_tools.append("RAG_TOOL")

    # ------------------------
    # CALCULATOR ROUTING
    # ------------------------

    if any(keyword in question_lower for keyword in calculator_keywords):
        selected_tools.append("CALCULATOR_TOOL")

    # ------------------------
    # DEFAULT TOOL
    # ------------------------

    if not selected_tools:
        selected_tools.append("RAG_TOOL")

    # Remove duplicates

    selected_tools = list(dict.fromkeys(selected_tools))

    # ------------------------
    # DEBUG LOGS
    # ------------------------

    print("\n==============================")
    print("TOOL ROUTER")
    print("==============================")
    print(f"Question : {question}")
    print(f"Selected : {selected_tools}")

    return selected_tools