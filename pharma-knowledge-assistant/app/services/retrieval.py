# from app.db.chroma_db import get_collection


# # def retrieve_context(question: str):

# #     collection = get_collection()

# #     results = collection.query(
# #         query_texts=[question],
# #         n_results=3
# #     )

# #     docs = results["documents"][0]

# #     return "\n".join(docs)



# def retrieve_context(question: str):

#     collection = get_collection()

#     results = collection.query(
#         query_texts=[question],
#         n_results=3
#     )

#     documents = results["documents"][0]
#     metadata = results["metadatas"][0]

#     return {
#         "documents": documents,
#         "metadata": metadata
#     }

from app.db.chroma_db import get_collection
# from app.services.embedding import generate_embedding
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
        n_results=3
    )

    documents = results["documents"][0]
    metadata = results["metadatas"][0]

    return documents, metadata