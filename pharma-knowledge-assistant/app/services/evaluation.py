import pandas as pd

from app.services.tools import (
    rag_tool
)


def run_evaluation():

    df = pd.read_csv(
        "evaluation_dataset.csv"
    )

    results = []

    passed = 0

    for _, row in df.iterrows():

        question = row[
            "question"
        ]

        expected = str(
            row[
                "expected_answer"
            ]
        )

        response = rag_tool(
            question
        )

        actual = response[
            "answer"
        ]

        is_pass = (
            expected.lower()
            in actual.lower()
        )

        if is_pass:
            passed += 1

        results.append(
            {
                "question":
                    question,
                "expected":
                    expected,
                "actual":
                    actual,
                "result":
                    "PASS"
                    if is_pass
                    else "FAIL"
            }
        )

    accuracy = (
        passed
        / len(df)
    ) * 100

    print(
        "\n===== EVALUATION REPORT ====="
    )

    for item in results:

        print(
            f"\nQuestion: {item['question']}"
        )

        print(
            f"Expected: {item['expected']}"
        )

        print(
            f"Actual: {item['actual']}"
        )

        print(
            f"Result: {item['result']}"
        )

    print(
        f"\nAccuracy: {accuracy:.2f}%"
    )

    return {
        "accuracy": accuracy,
        "results": results
    }
