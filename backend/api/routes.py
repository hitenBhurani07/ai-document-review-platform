import logging
from pathlib import Path

from fastapi import APIRouter, Body, File, HTTPException, UploadFile

from backend.schemas.document import DocumentRequest, DocumentResponse
from backend.services.pipeline_service import analyze_document


logger = logging.getLogger(__name__)


router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/analyze-text", response_model=DocumentResponse)
def analyze_text(payload: DocumentRequest = Body(...)) -> DocumentResponse:
    """Analyze raw business document text and return a structured report."""
    text = payload.text.strip() if payload.text else ""
    if not text:
        raise HTTPException(status_code=400, detail="Text input cannot be empty")

    try:
        logger.info("Analyzing text input")
        result = analyze_document(text)
        return DocumentResponse(**result)
    except Exception as exc:
        logger.error("Error analyzing text: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error analyzing text: {exc}")


@router.post("/upload-document", response_model=DocumentResponse)
def upload_document(file: UploadFile = File(...)) -> DocumentResponse:
    """Upload a .txt document and return a structured report."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")

    suffix = Path(file.filename).suffix.lower()
    if suffix != ".txt":
        raise HTTPException(status_code=400, detail="Only .txt files are supported")

    try:
        raw_bytes = file.file.read()
        text = raw_bytes.decode("utf-8", errors="ignore").strip()
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Unable to read file: {exc}")

    if not text:
        raise HTTPException(status_code=400, detail="Uploaded file is empty")

    try:
        logger.info("Analyzing uploaded document: %s", file.filename)
        result = analyze_document(text)
        return DocumentResponse(**result)
    except Exception as exc:
        logger.error("Error analyzing upload: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error analyzing upload: {exc}")
