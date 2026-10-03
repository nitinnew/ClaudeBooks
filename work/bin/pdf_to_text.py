"""Extract a text-layer PDF (or several, concatenated) to [[PAGE N]]-marked text with PyMuPDF (pip install pymupdf).
Usage: python pdf_to_text.py <key> <pdf> [<pdf> ...]   (pages numbered continuously; writes text/<key>.txt)"""
import os
import sys

import pymupdf

key, pdfs = sys.argv[1], sys.argv[2:]
os.makedirs("text", exist_ok=True)
parts, n = [], 0
for path in pdfs:
    for page in pymupdf.open(path):
        n += 1
        parts.append(f"[[PAGE {n}]]\n{page.get_text().strip()}\n")
open(os.path.join("text", key + ".txt"), "w", encoding="utf-8").write("\n".join(parts))
print(key, n, "pages")
