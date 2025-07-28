import fitz  # PyMuPDF

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = ""

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                line_text = " ".join([span["text"] for span in line["spans"]]).strip()
                font_size = line["spans"][0]["size"]

                if not title and page_num == 1:
                    title = line_text

                if len(line_text) > 5:
                    if font_size >= 18:
                        level = "H1"
                    elif font_size >= 14:
                        level = "H2"
                    elif font_size >= 11:
                        level = "H3"
                    else:
                        continue
                    outline.append({
                        "level": level,
                        "text": line_text,
                        "page": page_num
                    })

    return {"title": title, "outline": outline}
