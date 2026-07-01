def reflect(answer: str):

    """
    Decide whether the answer is
    good enough or needs another attempt.
    """

    answer_lower = answer.lower()

    failure_phrases = [
        "could not find",
        "not found",
        "no information",
        "unable to answer",
        "don't know"
    ]

    for phrase in failure_phrases:

        if phrase in answer_lower:

            return {
                "success": False,
                "reason": phrase
            }

    return {
        "success": True,
        "reason": None
    }