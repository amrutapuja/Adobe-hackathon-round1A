import os
import json
import fitz  
from utils import extract_outline

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def process_pdfs():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename.replace(".pdf", ".json"))

            title, outline = extract_outline(pdf_path)

            output_json = {
                "title": title,
                "outline": outline
            }

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_json, f, indent=2)

if __name__ == "__main__":
    process_pdfs()
