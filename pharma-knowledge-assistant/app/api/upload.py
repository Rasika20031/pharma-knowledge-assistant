from fastapi import APIRouter, UploadFile, File
import os

from app.services.ingestion import ingest_pdf

router = APIRouter(tags=["Upload"])

UPLOAD_DIR = "app/data/documents"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    chunks = ingest_pdf(file_path)

    return {
        "message": "Upload successful",
        "chunks_created": chunks
    }
