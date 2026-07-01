def create_plan(question: str, intent: str):

    plan = {
        "intent": intent,
        "steps": []
    }

    if intent == "MEDICAL_QUERY":

        plan["steps"] = [
            "Retrieve relevant documents",
            "Generate answer",
            "Return sources"
        ]

    elif intent == "BUSINESS_QUERY":

        plan["steps"] = [
            "Generate SQL",
            "Execute SQL",
            "Generate business answer"
        ]

    elif intent == "CALCULATION":

        plan["steps"] = [
            "Perform calculation",
            "Generate response"
        ]

    else:

        plan["steps"] = [
            "Answer directly"
        ]

    return plan