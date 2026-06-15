import requests


def classify_intent(question: str):

    question_lower = question.lower().strip()

    # =========================
    # GREETING
    # =========================

    greeting_words = [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening",
        "good afternoon"
    ]

    if question_lower in greeting_words:
        return "GREETING"

    # =========================
    # SHORT / VAGUE
    # =========================

    if len(question.split()) <= 2:
        return "SHORT_VAGUE"

    # =========================
    # CALCULATION
    # =========================

    calculator_keywords = [
        "+",
        "-",
        "*",
        "/",
        "calculate",
        "multiply",
        "divide",
        "percentage",
        "percent"
    ]

    if any(
        keyword in question_lower
        for keyword in calculator_keywords
    ):
        return "CALCULATION"

    # =========================
    # COMPLEX QUERY
    # =========================

    business_keywords = [
        "sales",
        "revenue",
        "performance",
        "metric",
        "count",
        "total"
    ]

    medical_keywords = [
        "used for",
        "indication",
        "side effect",
        "side effects",
        "dosage",
        "treatment"
    ]

    has_business = any(
        keyword in question_lower
        for keyword in business_keywords
    )

    has_medical = any(
        keyword in question_lower
        for keyword in medical_keywords
    )

    if has_business and has_medical:
        return "COMPLEX_QUERY"

    # =========================
    # SUMMARIZATION
    # =========================

    summary_keywords = [
        "summarize",
        "summary"
    ]

    if any(
        keyword in question_lower
        for keyword in summary_keywords
    ):
        return "SUMMARIZATION"

    # =========================
    # LLM FALLBACK
    # =========================

    prompt = f"""
You are an intent classifier.

Classify the question into exactly one of these intents:

BUSINESS_QUERY
MEDICAL_QUERY
OUT_OF_SCOPE

Question:
{question}

Return only the intent name.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    result = response.json()["response"].strip()

    print("Intent:")
    print(result)

    if "BUSINESS_QUERY" in result:
        return "BUSINESS_QUERY"

    if "MEDICAL_QUERY" in result:
        return "MEDICAL_QUERY"

    if "OUT_OF_SCOPE" in result:
        return "OUT_OF_SCOPE"

    return "MEDICAL_QUERY"