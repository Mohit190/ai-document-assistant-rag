from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.pdf_loader import load_pdf
from app.utils.chunking import split_docs
from app.services.vector_store import store_documents

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    documents = load_pdf(file_path)

    chunks = split_docs(documents)

    store_documents(chunks)

    return {
        "message": "PDF uploaded successfully",
        "chunks": len(chunks)
    }