"""OCR a scanned PDF to [[PAGE N]]-marked text with RapidOCR on 200-dpi PyMuPDF renders.
Usage (from cloud_outbox): python ocr_pdf.py <key> <pdf>"""
import os, sys
import pymupdf
from rapidocr_onnxruntime import RapidOCR
key, path = sys.argv[1], sys.argv[2]
eng = RapidOCR()
parts = []
for n, page in enumerate(pymupdf.open(path), 1):
    png = page.get_pixmap(dpi=200).tobytes("png")
    res, _ = eng(png)
    # sort boxes top-to-bottom, then left-to-right
    lines = [r[1] for r in sorted(res or [], key=lambda r: (round(r[0][0][1] / 15), r[0][0][0]))]
    parts.append(f"[[PAGE {n}]]\n" + "\n".join(lines) + "\n")
os.makedirs("text", exist_ok=True)
open(os.path.join("text", key + ".txt"), "w", encoding="utf-8").write("\n".join(parts))
print(key, n, "pages (OCR)")
