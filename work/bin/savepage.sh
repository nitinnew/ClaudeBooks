#!/bin/bash
# usage: savepage.sh <toolresult file> <name>  -> saves listing, prints next token and finance-related titles
set -e
D=/home/user/ClaudeBooks/work/listings
cp "$1" "$D/$2.json"
jq -r '.nextPageToken // "NONE"' "$D/$2.json" > "$D/$2.token"
echo "count: $(jq '.files|length' "$D/$2.json")  first: $(jq -r '.files[0].title' "$D/$2.json")  last: $(jq -r '.files[-1].title' "$D/$2.json")"
echo "TOKEN: $(cat "$D/$2.token")"
RE='(?i)trad|stock|invest|chart|candle|market|option|strateg|swing|breakout|price.?action|technical|wave|elliott|fibon|pivot|nifty|momentum|trend|value|buffett|graham|lynch|minervini|darvas|wyckoff|indicator|rsi|macd|vwap|supply|demand|pattern|multibag|wealth|profit|portfolio|equity|bull|bear|algo|quant|backtest|setup|scalp|intraday|futures|forex|bible|secret|gann|astro|ichimoku|bollinger|volume|smc|ict|harmonic|fundamental|screen'
jq -r --arg re "$RE" '.files[] | select(.title|test($re)) | .title[0:90]' "$D/$2.json" | paste -sd'|' | fold -w 4000
