def generate_response(results):
    """
    Combines outputs from multiple tools
    into one user-friendly response.
    """

    final_answer = ""

    for item in results:

        tool = item["tool"]
        answer = item["result"]["answer"]

        if tool == "SQL_TOOL":
            final_answer += "Business Information\n"
            final_answer += answer + "\n\n"

        elif tool == "RAG_TOOL":
            final_answer += "Medical Information\n"
            final_answer += answer + "\n\n"

        elif tool == "CALCULATOR_TOOL":
            final_answer += "Calculation Result\n"
            final_answer += answer + "\n\n"

    return final_answer.strip()