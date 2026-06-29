from fastapi import APIRouter, UploadFile, File
import shutil
from pathlib import Path

from backend.multimodal.ocr import extract_text
from backend.multimodal.report_analyzer import analyze_report

router = APIRouter()


@router.post("/analyze-image")
async def analyze_image(
    file: UploadFile = File(...)
):

    # Save uploaded image
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).resolve().parents[3]

    image_dir = PROJECT_ROOT / "data" / "images"

    image_dir.mkdir(parents=True, exist_ok=True)

    image_path = image_dir / file.filename

    

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # OCR
    extracted_text = extract_text(
        str(image_path)
    )

    # Report Analysis
    summary = analyze_report(
        extracted_text
    )

    return {
        "ocr_text": extracted_text,
        "analysis": summary
    }