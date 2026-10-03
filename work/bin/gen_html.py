"""Write cloud_outbox/index.html (artifact page) from manifest.json."""
import json, html, datetime
OUT = "/home/user/ClaudeBooks/cloud_outbox"
man = json.load(open(f"{OUT}/manifest.json"))
order = {"done":0,"in_progress":1,"todo":2,"needs_ocr":3,"possible_duplicate":4,"local_other_edition":5}
pri = {"H":0,"M":1,"L":2,"":3}
man.sort(key=lambda m: (order.get(m["status"], 9), pri.get(m["priority"], 3), m["key"]))
from collections import Counter
c = Counter(m["status"] for m in man)
e = html.escape
rows = []
for m in man:
    if m["status"] == "done":
        links = f'<a href="specs/{e(m["key"])}.md">spec</a> · <a href="text/{e(m["key"])}.txt">text</a> · <a href="logs/{e(m["key"])}.verify.txt">verify log</a>'
        cites = f'{m["citations_ok"]}/{m["citations_checked"]}'
    else:
        links, cites = "", ""
    rows.append(f'<tr><td><span class="pill s-{e(m["status"])}">{e(m["status"].replace("_"," "))}</span></td>'
                f'<td class="pri">{e(m["priority"])}</td><td class="t"><div class="title">{e(m["title"])}</div><div class="au">{e(m["author"])}</div><code>{e(m["key"])}</code></td>'
                f'<td class="num">{m["strategies"] or ""}</td><td class="num">{cites}</td><td class="cov">{e(m["coverage"])}</td><td class="lk">{links}</td></tr>')
summary = " · ".join(f'<b>{v}</b> {e(k.replace("_"," "))}' for k, v in sorted(c.items(), key=lambda kv: order.get(kv[0], 9)))
now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
page = f"""<title>Strategy Extraction Cloud Outbox</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400;500&family=Fraunces:opsz,wght@9..144,600&display=swap">
<style>
/* Layout: one ledger column — header strip, file list, then the manifest table (scrolls sideways on phones) */
:root {{ --bg:#f6f7f4; --fg:#1d2420; --muted:#5d6a63; --line:#d7ddd8; --accent:#1f6f54; --chip:#e6ece8;
  --done:#1f6f54; --todo:#7a6a2c; --ocr:#8a3b2e; --dup:#4b5b8a;
  --display:"Fraunces", Georgia, serif; --body:"IBM Plex Sans", system-ui, sans-serif; --mono:"IBM Plex Mono", ui-monospace, monospace; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#141916; --fg:#e3e8e4; --muted:#9aa79f; --line:#2c3530; --accent:#6cc4a0; --chip:#1f2622; --done:#6cc4a0; --todo:#d4bf6a; --ocr:#e08a77; --dup:#9fb0e6; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --bg:#141916; --fg:#e3e8e4; --muted:#9aa79f; --line:#2c3530; --accent:#6cc4a0; --chip:#1f2622; --done:#6cc4a0; --todo:#d4bf6a; --ocr:#e08a77; --dup:#9fb0e6; color-scheme:dark }}
body {{ background:var(--bg); color:var(--fg); font:15px/1.5 var(--body); }}
.wrap {{ max-width:1180px; margin:0 auto; padding-inline:16px; padding-block:28px 48px; display:grid; gap:22px; }}
h1 {{ font:600 clamp(1.6rem,4vw,2.2rem)/1.15 var(--display); margin:0; text-wrap:balance; }}
.sub {{ color:var(--muted); max-width:70ch; margin:6px 0 0; }}
.sum {{ font-variant-numeric:tabular-nums; }}
.files {{ display:flex; flex-wrap:wrap; gap:8px 18px; font-family:var(--mono); font-size:13px; }}
a {{ color:var(--accent); }} a:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
.tbl {{ overflow-x:auto; border-top:2px solid var(--fg); }}
table {{ border-collapse:collapse; width:100%; min-width:860px; }}
th {{ text-align:left; font:600 11px/1.2 var(--body); letter-spacing:.06em; text-transform:uppercase; color:var(--muted); padding:10px 8px; border-bottom:1px solid var(--line); }}
td {{ padding:9px 8px; border-bottom:1px solid var(--line); vertical-align:top; }}
.title {{ font-weight:600; }} .au {{ color:var(--muted); font-size:13px; }} code {{ font:12px var(--mono); color:var(--muted); }}
.num {{ font-variant-numeric:tabular-nums; text-align:right; font-family:var(--mono); font-size:13px; }}
.pri {{ font-family:var(--mono); font-weight:500; }} .cov {{ font-size:13px; color:var(--muted); max-width:34ch; }} .lk {{ font-size:13px; white-space:nowrap; }}
.pill {{ display:inline-block; font:500 11px/1 var(--mono); padding:4px 7px; border-radius:3px; background:var(--chip); white-space:nowrap; }}
.s-done {{ color:var(--done); }} .s-todo,.s-in_progress {{ color:var(--todo); }} .s-needs_ocr {{ color:var(--ocr); }} .s-possible_duplicate,.s-local_other_edition {{ color:var(--dup); }}
</style>
<div class="wrap">
<header><h1>Strategy Extraction Cloud Outbox</h1>
<p class="sub">Specs extracted from resources that exist only on Google Drive, for import and re-verification by the laptop session. Page markers <code>[[PAGE N]]</code> in each text file are what the spec citations refer to.</p></header>
<div class="sum">{summary} <span style="color:var(--muted)">· updated {now}</span></div>
<div class="files"><a href="inventory.md">inventory.md</a><a href="manifest.json">manifest.json</a><a href="tools/verify_citations.py">tools/verify_citations.py</a><a href="tools/pdf_to_text.py">tools/pdf_to_text.py</a></div>
<div class="tbl"><table><thead><tr><th>Status</th><th>Pri</th><th>Resource</th><th>Strat.</th><th>Cites ok</th><th>Coverage</th><th>Files</th></tr></thead><tbody>
{''.join(rows)}
</tbody></table></div>
<p class="sub">Not listed here: items already on the laptop, not strategy sources, and deferred media. See inventory.md for every Drive row.</p>
</div>"""
open(f"{OUT}/index.html", "w").write(page)
print("index.html", len(page))
