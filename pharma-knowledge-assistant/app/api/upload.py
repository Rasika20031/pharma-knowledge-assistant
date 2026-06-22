from fastapi import APIRouter, UploadFile, File
import os

from app.services.ingestion import ingest_pdf

router = APIRouter(tags=["Upload"])

UPLOAD_DIR = "app/data/documents"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_pdf(
    files: list[UploadFile] = File(...)
):

    total_chunks = 0

    uploaded_files = []

    for file in files:

        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            buffer.write(
                await file.read()
            )

        chunks = ingest_pdf(
            file_path
        )

        total_chunks += chunks

        uploaded_files.append(
            file.filename
        )

    return {

        "message":
            "Upload successful",

        "uploaded_files":
            uploaded_files,

        "chunks_created":
            total_chunks
    }