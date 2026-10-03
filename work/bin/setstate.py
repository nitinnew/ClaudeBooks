import json, os, sys
P = "/home/user/ClaudeBooks/work/state.json"
s = json.load(open(P)) if os.path.exists(P) else {}
key = sys.argv[1]
for kv in sys.argv[2:]:
    k, v = kv.split("=", 1)
    s.setdefault(key, {})[k] = int(v) if v.isdigit() and k in ("strategies","citations_ok","citations_checked") else v
json.dump(s, open(P, "w"), indent=1)
