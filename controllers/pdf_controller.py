# controllers/pdf_controller.py
from fastapi import APIRouter, UploadFile, File
from models.pdf_extractor import extract_text_from_pdf
from utils.chunker import chunk_text
from models.embedding_model import store_chunks

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Endpoint for uploading a PDF.
    It extracts text, splits it into chunks, and stores embeddings in Pinecone.
    """
    text = extract_text_from_pdf(file.file)
    chunks = chunk_text(text)
    store_chunks(chunks)
    return {"message": "PDF processed successfully", "num_chunks": len(chunks)}
