"""Check that quoted passages in a strategy spec appear in the book text on the cited page.

Usage: python verify_citations.py <spec.md> <book.txt> [--fix]

Finds every "quote" ... [p. N] pair in the spec, searches the book text for the
quote (whitespace/punctuation-insensitive, using its longest fragment when the
quote contains an ellipsis) and reports OK / WRONG PAGE / NOT FOUND.
With --fix, rewrites WRONG PAGE citations in place to the page where the quote was found.
"""
import re
import sys


def norm(s):
    # letters/digits only: tolerant of OCR-split words ("i t") and punctuation differences
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def load_pages(path):
    pages, cur, buf = {}, 1, []
    for line in open(path, encoding="utf-8", errors="replace"):
        m = re.match(r"^\[\[PAGE (\d+)\]\]", line)
        if m:
            pages[cur] = norm(" ".join(buf))
            cur, buf = int(m.group(1)), []
        else:
            buf.append(line)
    pages[cur] = norm(" ".join(buf))
    return pages


def find_pages(pages, quote):
    frags = [norm(f) for f in re.split(r"\.\.\.|…", quote)]
    frag = max(frags, key=len)
    if len(frag) < 20:
        return None
    # match on any of several 25-char windows, so a single OCR typo doesn't cause a miss
    w = 25
    wins = {frag[i:i + w] for i in range(0, max(1, len(frag) - w + 1), max(1, (len(frag) - w) // 4 or 1))}
    hits = [p for p, t in pages.items() if any(x in t for x in wins)]
    if not hits:  # quote may straddle a page break
        keys = sorted(pages)
        hits = [a for a, b in zip(keys, keys[1:]) if any(x in pages[a] + pages[b] for x in wins)]
    return hits


# Quotes may not span lines. Short quotes (scare-quotes) are still consumed by the pattern so they
# cannot pair with a later quote's closing mark; they are then skipped (fewer than 15 characters).
QUOTE_CITE = re.compile(r'["“]([^"“”\n]+?)["”](?:[^\n\["“]{0,40}\[p\. ?(\d+)(?:[–-](\d+))?\])?')


def main():
    spec_path, text_path = sys.argv[1], sys.argv[2]
    fix = "--fix" in sys.argv
    pages = load_pages(text_path)
    spec = open(spec_path, encoding="utf-8").read()
    ok = wrong = missing = 0
    fixes = []
    for m in QUOTE_CITE.finditer(spec):
        if m.group(2) is None or len(m.group(1)) < 15:
            continue
        quote, lo = m.group(1), int(m.group(2))
        hi = int(m.group(3) or lo)
        hits = find_pages(pages, quote)
        if hits is None:
            continue
        if not hits:
            missing += 1
            print(f"NOT FOUND   [p. {m.group(2)}] {quote[:90]}")
        elif any(lo - 1 <= h <= hi + 1 for h in hits):
            ok += 1
        else:
            wrong += 1
            print(f"WRONG PAGE  cited p.{lo}{'-' + str(hi) if hi != lo else ''} -> found p.{hits} : {quote[:70]}")
            # the same phrase can recur (e.g. an indicator defined early, used later): take the hit nearest the citation
            fixes.append((m, min(hits, key=lambda h: abs(h - lo))))
    print(f"\nquotes checked: {ok + wrong + missing}  ok: {ok}  wrong page: {wrong}  not found: {missing}")
    if fix and fixes:
        for m, page in reversed(fixes):
            cite_start = spec.rindex("[p.", 0, m.start(2))
            cite_end = spec.index("]", m.start(2)) + 1
            spec = spec[:cite_start] + f"[p. {page}]" + spec[cite_end:]
        open(spec_path, "w", encoding="utf-8").write(spec)
        print(f"fixed {len(fixes)} quote citations in place")


if __name__ == "__main__":
    main()
