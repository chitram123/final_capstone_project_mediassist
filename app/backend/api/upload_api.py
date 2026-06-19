from fastapi import APIRouter, UploadFile, File
from ingest import ingest_document
import os

router = APIRouter()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../"
    )
    )

    file_path = os.path.join(
    BASE_DIR,
    "data",
    "raw_data",
    file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    total_chunks = ingest_document(file_path)


    return {
        "status": "success",
        "filename": file.filename,
        "message": "Document ingested successfully",
        "chunks_created": total_chunks
    }