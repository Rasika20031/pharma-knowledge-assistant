from app.db.chroma_db import get_collection
from app.services.embedding import get_embedding


# def retrieve_context(question: str):

#     collection = get_collection()

#     question_embedding = get_embedding(
#         question
#     )

#     results = collection.query(
#         query_embeddings=[
#             question_embedding
#         ],
#         n_results=5,
#         include=[
#             "documents",
#             "metadatas",
#             "distances"
#         ]
#     )

#     documents = []
#     metadata = []

#     # Smaller distance = better match
#     THRESHOLD = 1.5

#     for doc, meta, dist in zip(
#         results["documents"][0],
#         results["metadatas"][0],
#         results["distances"][0]
#     ):

#         if dist <= THRESHOLD:

#             documents.append(doc)
#             metadata.append(meta)

#     return documents, metadata




from app.db.chroma_db import get_collection
from app.services.embedding import get_embedding


def retrieve_context(question: str):

    collection = get_collection()

    question_embedding = get_embedding(
        question
    )

    results = collection.query(
        query_embeddings=[
            question_embedding
        ],
        n_results=5,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    print(
        "\nQUESTION:",
        question
    )

    print(
        "\nDISTANCES:",
        results["distances"][0]
    )

    print(
        "\nSOURCES:"
    )

    for meta in results["metadatas"][0]:

        print(meta)

    documents = []
    metadata = []

    THRESHOLD = 1.5

    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):

        if dist <= THRESHOLD:

            documents.append(doc)
            metadata.append(meta)

    return documents, metadata