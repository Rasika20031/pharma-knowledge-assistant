# import requests


# def generate_answer(question: str, context: str, memory):

#     conversation = ""

#     for item in memory:
#         conversation += (
#             f"User: {item['question']}\n"
#             f"Assistant: {item['answer']}\n\n"
#         )
#     prompt = f"""
# Answer ONLY using the provided context.
# If the answer is not present in the context,
# say that the information is not available.

# Previous Conversation:
# {conversation}

# Context:
# {context}

# Question:
# {question}


# """

#     response = requests.post(
#         "http://localhost:11434/api/generate",
#         json={
#             "model": "llama3",
#             "prompt": prompt,
#             "stream": False
#         }
#     )

#     response.raise_for_status()

#     result = response.json()

#     return result["response"]





import requests


def generate_answer(question: str, context: str):

    prompt = f"""
Answer the question using only the provided context.

If the answer is not present in the context, say:
'I could not find that information in the uploaded documents.'

Context:
{context}

Question:
{question}

Answer:
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

    return response.json()["response"]