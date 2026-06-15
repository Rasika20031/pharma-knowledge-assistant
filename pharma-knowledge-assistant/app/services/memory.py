memory_store = {}


def add_to_memory(
    session_id,
    question,
    answer
):

    if session_id not in memory_store:
        memory_store[session_id] = []

    memory_store[session_id].append(
        {
            "question": question,
            "answer": answer
        }
    )


def get_memory(
    session_id
):

    return memory_store.get(
        session_id,
        []
    )


def clear_memory(
    session_id
):

    if session_id in memory_store:
        memory_store[session_id] = []