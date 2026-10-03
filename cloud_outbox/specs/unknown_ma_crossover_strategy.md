# Moving Average Crossover Trading Strategy (Python script printout) — author not named

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/Moving Avg Crossover Trading Strategy.pdf` (file id `12YPdbZAFhU6l7TGlWJXONuEGM0fES4zs`, 610,513 bytes). A 4-page printout of a Python file whose header reads `File-E:\...\QuantitativeFinance\EMATrading Startegy.py` [p. 1]; no author or date (the script's data window ends 10 March 2022 [p. 4]).
- **Text file used:** text/unknown_ma_crossover_strategy.txt  (page basis: pdf_pages). **The PDF has no text layer; the text was produced by OCR in the cloud session** (RapidOCR on 200-dpi PyMuPDF renders, script `ocr_pdf.py`). Line numbers of the code appear as separate OCR lines; a few characters are misread (e.g. `50o00` for `50000`, full-width commas).
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter. (The printout's "Page N of 4" footers match the PDF index here.)
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/unknown_ma_crossover_strategy.md text/unknown_ma_crossover_strategy.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** All 4 pages OCR'd and read, [[PAGE 1]] to [[PAGE 4]] (code lines 1–100). OCR quality is good; the code is fully reconstructable.

## 1. The method in brief

A minimal backtest script for a long-only EMA crossover on one stock: compute a short and a long EMA of the adjusted close (pandas `ewm(span=…, adjust=False)`), go long when short EMA > long EMA, exit when short EMA < long EMA [p. 2–3]. The example run uses Infosys (`INFY` on Yahoo Finance, i.e. the US ADR ticker), 30/75 EMAs, capital 50,000, data 1 Jan 2010 – 10 Mar 2022 [p. 4]. No stop-loss, costs, position sizing or results are given. Note: the script's equity calculation does not compound (each closed trade is recorded as `capital × exit/entry` of the *initial* capital) [p. 2], so its equity curve is not a true account curve.

## 2. Strategies

### 2.1 EMA(30) / EMA(75) crossover, long-only

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 2 |
| Timeframe & holding period | Daily (Yahoo daily data); hold while short EMA > long EMA | 1–2 |
| Universe / eligibility filters | Single stock per run (example INFY) | 4 |
| Market / regime filter | None | — |
| Setup conditions | EMAs of adjusted close: `ewm(span=short_period, adjust=False)` and `ewm(span=long_period, adjust=False)` | 1–3 |
| Entry trigger & order type | When short EMA > long EMA and no position open: buy at that bar's price (adjusted close) | 2–3 |
| Initial stop-loss | None | — |
| Exits: profit-taking | None | — |
| Exits: trailing / time / signal | When short EMA < long EMA and a position is open: sell at that bar's price | 2 |
| Position sizing | Whole initial capital per trade (no compounding in the script) | 2 |
| Adding to / pyramiding | No (one position at a time) | 2 |
| Portfolio limits | Single stock | 4 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Short EMA span | 30 | constructor argument | 4 |
| Long EMA span | 75 | constructor argument | 4 |
| Price field | Adj Close | — | 2 |
| Test window | 2010-01-01 to 2022-03-10 | — | 4 |
| Capital | 50,000 | — | 4 |

**Key quotes**

- "When short MA crosses long MA, open long position" [p. 2]
- "When long MA crosses short MA, close the long position" [p. 2]
- "if row.short_ma < row.long_ma and self. is_long:" [p. 2]
- "ewm(span=self.short_period, adjust=False).mean()" [p. 3]
- "start_date = datetime.datetime(2010, 1, 1)" [p. 4]

**Pseudocode**

```
P = adjusted close
S = EMA(P, span=30, adjust=False); L = EMA(P, span=75, adjust=False)
flat → if S_t > L_t: buy at P_t (same bar; ASSUMPTION for live test: next open)
long → if S_t < L_t: sell at P_t (same bar; ASSUMPTION: next open)
equity: compound per trade (fix the script's non-compounding record); charge costs
note: the first bar after warm-up with S > L triggers an immediate buy (state-based, not cross-based)
```

**Ambiguities & assumptions**

- **State vs. cross**: the code enters whenever S > L while flat, not only on the crossing bar [p. 2]. At the start of the data this buys immediately if S > L. ASSUMPTION: require a fresh cross for the first entry (variant: replicate the script).
- **Same-bar fills** at the signal bar's close imply look-ahead-free but optimistic execution. ASSUMPTION: next-open fills as the base case.
- **No compounding / no costs** in the script's equity [p. 2]. ASSUMPTION: compound and charge costs.
- **Ticker**: `INFY` on Yahoo is the NYSE ADR, not the NSE share (`INFY.NS`). ASSUMPTION: test on NSE prices.
- EMA warm-up: `adjust=False` starts from the first price, so early EMA values are biased. ASSUMPTION: skip the first 150 bars.

## 3. Risk & money-management rules

None in the script (no stop, no sizing rule, no costs).

## 4. Non-codable guidance

None; the document is code only.

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily adjusted close (OHLC for next-open fills).
- **Testability with our data:** Fully backtestable on 2005–2026 NSE prices, single stock or across the universe.
- **Market-structure differences:** Long-only already; apply STT, brokerage and ~0.1% slippage; next-open fills; circuit days. ASSUMPTION: across-universe test with equal-weight positions, max 20 open, liquidity floor Rs. 1 crore/day.

## 6. Verdict

- **Codeability:** Fully. It is code; only execution-timing and compounding need fixing.
- **Priority for backtesting:** Low. A textbook EMA crossover with an arbitrary 30/75 pair, no risk rules and no reported results; crossover systems are already covered by the Burns and Ladha specs.
- **Top 3 things a coder is most likely to get wrong**
  1. Copying the script's equity bookkeeping (non-compounding, initial capital each trade) as if it were a real equity curve [p. 2].
  2. Using `adjust=True` (pandas default) instead of the script's `adjust=False` EMA [p. 3].
  3. Treating the entry as a crossover event; the script enters on the state S > L whenever flat [p. 2].
