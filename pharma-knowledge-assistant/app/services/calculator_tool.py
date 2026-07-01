import re


def calculator_tool(question: str):

    expression = question.lower()

    expression = expression.replace("what is", "")
    expression = expression.replace("calculate", "")

    # Keep only numbers and operators
    expression = re.sub(
        r"[^0-9+\-*/(). ]",
        "",
        expression
    )

    expression = expression.strip()

    try:

        result = eval(expression)

        return {
            "expression": expression,
            "result": result,
            "answer": f"The answer is {result}"
        }

    except Exception as e:

        print(f"Calculator Error: {e}")

        return {
            "expression": expression,
            "result": None,
            "answer": "Unable to calculate."
        }