# from pypdf import PdfReader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from app.db.chroma_db import get_collection
# import uuid


# def ingest_pdf(file_path: str):

#     reader = PdfReader(file_path)

#     text = ""

#     for page in reader.pages:
#         text += page.extract_text() + "\n"

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     chunks = splitter.split_text(text)

#     collection = get_collection()

#     for chunk in chunks:
#         # collection.add(
#         #     documents=[chunk],
#         #     ids=[str(uuid.uuid4())]
#         # )
#         collection.add(
#         documents=[chunk],
#         ids=[str(uuid.uuid4())],
#         metadatas=[
#             {
#                 "source": file_path
#             }
#         ]
#     )

#     return len(chunks)

from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.db.chroma_db import get_collection
from app.services.embedding import get_embedding
import uuid


def ingest_pdf(file_path: str):

    reader = PdfReader(file_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    collection = get_collection()

    total_chunks = 0

    for page_num, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if not page_text:
            continue

        chunks = splitter.split_text(page_text)

        for chunk_index, chunk in enumerate(chunks):

            embedding = get_embedding(
                chunk
            )

            collection.add(
                documents=[chunk],
                embeddings=[embedding],
                ids=[str(uuid.uuid4())],
                metadatas=[
                    {
                        "source": file_path,
                        "page": page_num,
                        "chunk_id": chunk_index
                    }
                ]
            )

            total_chunks += 1

    return total_chunks