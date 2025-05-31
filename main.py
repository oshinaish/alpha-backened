from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CATEGORIZATION_FILE = "categorized_memory.json"

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        reader = PdfReader(file.file)
        lines = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                lines.extend(line.strip() for line in text.splitlines() if line.strip())

        if not lines:
            return {"status": "error", "message": "No text found in PDF."}

        return {
            "status": "success",
            "total_transactions": len(lines),
            "raw_transactions": lines
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/save-category")
async def save_category(payload: dict):
    line = payload.get("line")
    category = payload.get("category")

    if not line or not category:
        return {"status": "error", "message": "Missing line or category"}

    try:
        if os.path.exists(CATEGORIZATION_FILE):
            with open(CATEGORIZATION_FILE, "r") as f:
                memory = json.load(f)
        else:
            memory = {}

        memory[line] = category

        with open(CATEGORIZATION_FILE, "w") as f:
            json.dump(memory, f)

        return {"status": "success"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/get-categories")
async def get_categories():
    try:
        if os.path.exists(CATEGORIZATION_FILE):
            with open(CATEGORIZATION_FILE, "r") as f:
                memory = json.load(f)
        else:
            memory = {}

        return {"status": "success", "memory": memory}

    except Exception as e:
        return {"status": "error", "message": str(e)}
