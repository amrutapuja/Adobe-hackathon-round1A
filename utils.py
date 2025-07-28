import fitz  # PyMuPDF

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title") or "Untitled Document"
    headings = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b["type"] == 0:  # text block
                for line in b["lines"]:
                    text = " ".join(span["text"] for span in line["spans"]).strip()
                    font_size = line["spans"][0]["size"]

                    if font_size > 17:
                        level = "H1"
                    elif font_size > 14:
                        level = "H2"
                    elif font_size > 12:
                        level = "H3"
                    else:
                        continue

                    if text and len(text) > 3 and len(text.split()) < 20:
                        headings.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })

    return title, headings
