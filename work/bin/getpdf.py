"""usage: getpdf.py <toolresult.json> <outname>  -> decode base64 download, report pages + text layer"""
import base64, json, sys, pymupdf, os
src, name = sys.argv[1], sys.argv[2]
d = json.load(open(src))
out = f"/home/user/ClaudeBooks/work/pdfs/{name}"
open(out, "wb").write(base64.b64decode(d["content"]))
print(d.get("title"), d.get("mimeType"), os.path.getsize(out), "bytes")
if out.endswith(".pdf"):
    doc = pymupdf.open(out)
    n = len(doc)
    chars = [len(p.get_text().strip()) for p in doc]
    with_text = sum(1 for c in chars if c > 50)
    print(f"pages={n} pages_with_text={with_text} total_chars={sum(chars)} encrypted={doc.is_encrypted} needs_pass={doc.needs_pass}")
    if len(sys.argv) > 3:
        import re
        txt = "\n".join(doc[i].get_text() for i in range(min(int(sys.argv[3]), n)))
        txt = re.sub(r"\s+", " ", txt)
        print("--- first pages:", txt[:1500])
