# The Simple Guide to Volume Weighted Average Price [VWAP] — Jitendra Jain & Yogesh Nanda

- **Source file:** Google Drive: invest/VWAP pdf.pdf
- **Text file used:** text/unknown_vwap_pdf.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage. Printed section numbers in the text are ignored.
- **Coverage:** Read lines 1-123 (the whole file) and reached the last marker `[[PAGE 8]]`. Page 8 has only the author header and no other text. Pages 1-7 carry very little text. All charts and screenshots are images and are not in the text, so the entry/exit rules for "VWAP Breakout" and "VWAP Reversal" (page 4, headings only) and the Zerodha/TradingView set-up (page 1, heading only) are not available. Reading done by a Sonnet sub-agent. The coordinator read the whole 123-line text itself, re-ran the verifier and an exact-page check, and confirmed the table citations against pp. 1-7.

## 1. The method in brief
A short, discretionary, INTRADAY guide to using the day's Volume Weighted Average Price as a bias line, an entry reference and a trailing stop, mainly for Indian index/stock/option trading (Zerodha, TradingView) [p. 1]. The authors say VWAP is a volume-based indicator that shows the "footprints" of larger players [p. 1]. They use it to form a bullish/bearish view (price above/below VWAP, two consecutive days' VWAPs, VWAP slope) [p. 2, 3], to trade VWAP breakouts and reversals (chart-only) [p. 4], to avoid false breakouts by waiting 1-2 candles [p. 5], as a trailing stop [p. 5], as an Anchored VWAP from a meaningful past price/day [p. 6], and on option and straddle charts for option sellers [p. 7].

There is no track record, back-test, sizing rule or risk framework. Almost every rule is a qualitative bias statement. Only a few are explicit enough to code, and all need intraday data except the Anchored VWAP.

## 2. Strategies

### 2.1 VWAP bias filters (single-day VWAP, 2-day VWAP, VWAP slope)
Grouped because the authors give only a view, with no trade action [p. 2, 3].

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday bias / trend filter (indicator view, not a stand-alone trade) | 2, 3 |
| Timeframe & holding period | Intraday chart of the current day; no holding period given | 2 |
| Universe / eligibility filters | "index / stock"; no liquidity or price filter | 2 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Single day: price above VWAP = bullish, below = bearish. Two days: price above both days' VWAP = bullish, below both = bearish. Today's VWAP lower than yesterday's = sellers ready to sell lower. Slope down = aggressive selling, slope up = aggressive buying | 2, 3 |
| Entry trigger & order type | Not found in this text (view only) | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| VWAP window | current day (reset daily) | 2 consecutive days used jointly | 2 |
| Slope measure | not defined (visual up/down) | - | 3 |
| Today vs yesterday VWAP | lower = bearish hint | - | 2 |

**Key quotes**
- "price above VWAP - Bullish" [p. 2]
- "Price Above both day VWAP - bullish" [p. 2]
- "If todays VWAP is lower then yesterdays VWAP" [p. 2]
- "If VWAP slope is uptrending it indicates buyers are buying aggressively" [p. 3]

**Pseudocode** (needs intraday bars; see section 5)
```
vwap_t = cumsum(typical_price_i * vol_i) / cumsum(vol_i)   # reset each session
bias_single = +1 if close_t > vwap_t, -1 if close_t < vwap_t, else 0
vwap_prev = final-of-day VWAP of previous session
bias_2day = +1 if close_t > max(vwap_t, vwap_prev); -1 if close_t < min(vwap_t, vwap_prev); else 0
slope_t = vwap_t - vwap_{t-n}   # sign only: >0 buyers aggressive, <0 sellers aggressive
```

**Ambiguities & assumptions**
- The text defines VWAP as "price where maximum volume for the day has taken place" [p. 1]. That is the volume point of control, not the volume-weighted average. It then describes the correct formula (price x volume summed / total volume) [p. 1]. ASSUMPTION: use the standard VWAP formula.
- Price for the volume x price product (tick, bar close or typical price) is not stated. ASSUMPTION: typical price (H+L+C)/3 on 1-minute or 5-minute bars.
- "Price above both day VWAP" does not say whether "yesterday's VWAP" is the final value or the plotted line carried forward. ASSUMPTION: yesterday's end-of-day VWAP as a horizontal level.
- The slope lookback and the threshold for "upward/downward" are not given. ASSUMPTION: sign of the 30-minute change in VWAP.
- Whether a bias is used on its own or alongside other signals is not stated. ASSUMPTION: treat as a filter for 2.2 and 2.3.

### 2.2 VWAP breakout / breakdown with 1-2 candle confirmation
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday breakout (cross of VWAP) | 4, 5 |
| Timeframe & holding period | Intraday; candle size not given | 5 |
| Universe / eligibility filters | Index, stock (also options, straddles) | 7 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Price crosses VWAP; "VWAP Brekout" heading with chart only. Warning that an index "gives falls breakdown below VWAP and immediately reverses" | 4, 5 |
| Entry trigger & order type | Wait "1-2 candles" to sustain above/below VWAP before acting; order type not stated | 5 |
| Initial stop-loss | Not found for the breakout itself (VWAP + points is stated only for option selling) | 7 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | VWAP trailing stop (see 2.3) | 5 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Confirmation candles | 1-2 | "sometimes" helps | 5 |
| Candle timeframe | not stated | - | - |
| Breakout buffer | not stated | - | - |

**Key quotes**
- "Waiting for 1-2 candles to sustain above of below VWAP can sometimes save from such false" [p. 5]
- "Sometimes index gives falls breakdown below VWAP and immediately reverses from there" [p. 5]

**Pseudocode** (needs intraday bars)
```
for each intraday bar t:
  up_confirmed   = all(close[t-k+1..t] > vwap[t-k+1..t]) and close[t-k] <= vwap[t-k]   # k in {1,2}
  down_confirmed = mirror
  if up_confirmed and flat:   go long at next bar open
  if down_confirmed and flat: short (futures/options only; cash market is long-only intraday-squareoff)
  exit: VWAP-cross trailing stop (2.3), else square off at session end
```

**Ambiguities & assumptions**
- The "VWAP Breakout" and "VWAP Reversal" entries are shown only as chart images [p. 4]. The text has no entry or exit rule. ASSUMPTION: a breakout is a close above/below VWAP held for k=2 candles.
- "Sometimes" indicates the filter is discretionary. ASSUMPTION: always require k=2, test k=1 as a variant.
- No stop-loss or target for this setup. ASSUMPTION: stop at VWAP minus a buffer (or an ATR fraction); square off at session close.

### 2.3 VWAP as trailing stop-loss
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Exit / trailing stop overlay | 5 |
| Timeframe & holding period | Intraday | 5 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | An open trade with a view in place | 5 |
| Entry trigger & order type | Not applicable | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Trail the stop "with certain points above VWAP"; the view is assumed to change when price crosses VWAP | 5 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Stop offset from VWAP | "certain points" (unspecified) | - | 5 |

**Key quotes**
- "we can trail our stop loss with certain points above" [p. 5]
- "assuming view changes with cross of VWAP." [p. 5]

**Pseudocode** (needs intraday bars)
```
long:  stop_t = vwap_t - offset   (exit if close < stop_t, i.e. VWAP cross)
short: stop_t = vwap_t + offset   (exit if close > stop_t)
```

**Ambiguities & assumptions**
- The text says "above VWAP" without the direction for longs vs shorts; the wording is ambiguous. ASSUMPTION: offset on the protective side of VWAP (below for longs, above for shorts).
- "Certain points" is not quantified. ASSUMPTION: 0.1% of price, test 0 to 0.3%.
- Exit on cross vs on close beyond the stop is unspecified. ASSUMPTION: exit on a bar close beyond the stop.

### 2.4 Anchored VWAP (AVWAP)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Support/resistance and positioning reference (positional) | 6 |
| Timeframe & holding period | Positional; plotted from a chosen past day, so multi-day | 6 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Anchor from "major top": price below that AVWAP = sellers comfortable holding; above it they "might start covering" | 6 |
| Entry trigger & order type | Not found in this text (no explicit entry rule) | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Anchor point | "previous meaningful benchmark price or day" chosen by the trader; example: major top | other anchors implied | 6 |

**Key quotes**
- "Normal VWAP is ploted for single day and it do not consider data of previous days." [p. 6]
- "Anchored volume weighted average price [AVWAP] is a plotted from previous meaningful" [p. 6]
- "and they are comfortable holding their positions" [p. 6]

**Pseudocode** (daily proxy possible; ASSUMPTION)
```
anchor = date of major swing high (e.g. highest close in last N days)
avwap_t = sum_{i=anchor..t}(tp_i * vol_i) / sum_{i=anchor..t}(vol_i)   # tp = (H+L+C)/3 daily
state_t = "supply overhead" if close_t < avwap_t else "sellers covering" if close_t > avwap_t
```

**Ambiguities & assumptions**
- How to define a "major top" is discretionary. ASSUMPTION: rolling 252-day highest high, or a fractal swing high.
- No action is specified when price crosses the AVWAP. ASSUMPTION: close above AVWAP of a major top is a long-bias filter.
- ASSUMPTION: using daily typical price x daily volume is an approximation, not true VWAP.

### 2.5 Non-codable / not-in-text items
- **VWAP Reversal** [p. 4]: heading and chart only, no text rule.
- **VWAP on option charts (option sellers)**: "sell only if its below VWAP" with stop at VWAP plus points; VWAP retest or breakdown is the entry with "very small stop loss" [p. 7]. Needs option-premium intraday data and short selling of options.
- **VWAP on straddle/strangle charts**: if the combined premium is below VWAP, sellers are "comfortable selling" [p. 7]. Needs options data.
- **Zerodha/TradingView set-up** [p. 1]: heading only.

## 3. Risk & money-management rules
- Stop for option selling: VWAP plus certain points; the authors claim a very small stop and better risk-reward [p. 7].
- Trailing stop relative to VWAP [p. 5].
- Position sizing, risk per trade, drawdown limits, max exposure: Not found in this text.

## 4. Non-codable guidance
- VWAP shows "footprints of larger players" [p. 1], an interpretation rather than a rule.
- Waiting for confirmation "can sometimes" avoid false breakouts, so it is discretionary [p. 5].
- Choice of the anchor for AVWAP is left to the trader [p. 6].
- VWAP "will give you decipline" as an option seller [p. 7].

## 5. Adapting to NSE (Indian equities)
- **Data required:** Standard VWAP needs intraday (1-minute or 5-minute) OHLCV for index, stocks, futures or options. Anchored VWAP can use daily OHLCV (high, low, close, volume).
- **Testability with our data:** Our data is daily OHLCV only (2005-2026).
  - Needs intraday data we do not have: single-day VWAP bias, 2-day VWAP, VWAP slope, VWAP breakout/reversal/false-breakout, VWAP trailing stop, and every option/straddle use. These cannot be backtested, and the 2-day comparison of today's vs yesterday's VWAP also needs the intraday VWAP.
  - Daily proxy: ASSUMPTION: a daily typical price (H+L+C)/3 is NOT true VWAP; it is only a crude per-day price. A rolling volume-weighted typical price over N days could stand in as a "multi-day VWAP" level; this is a different indicator and must not be reported as the book's VWAP.
  - Anchored VWAP from a major swing high/low is the one idea defensibly testable on daily data (ASSUMPTION: daily typical price weighted by daily volume, accumulated from an anchor bar). It is still an approximation of the true AVWAP.
  - Index history is only from 2024; use NIFTYBEES or an equal-weight index for index-level tests.
- **Market-structure differences:**
  - The cash market has no overnight shorting. Intraday shorting is possible with square-off the same day. ASSUMPTION: test long-side only on daily proxy.
  - STT, brokerage and about 0.1% slippage matter much more for intraday-frequency trading, so this style is cost-sensitive. ASSUMPTION: 0.1% slippage per side.
  - Circuit limits can freeze a stock, which breaks a VWAP-cross stop.
  - Illiquid small caps give noisy VWAP. ASSUMPTION: restrict to liquid stocks.

## 6. Verdict
- **Codeability:** Partly. The formulas are clear, but the rules are mostly qualitative and chart-based, and the key entries are images only.
- **Priority for backtesting:** Low. It cannot be backtested faithfully on daily data, and the text gives no results, sizing or exits.
- **Top 3 things a coder is most likely to get wrong:**
  1. Using a daily typical price or close as "VWAP" and treating the result as the book's intraday VWAP.
  2. Not resetting VWAP at each session start (and mixing it with the Anchored version, which does not reset).
  3. Taking the text's definition ("price where maximum volume ... has taken place") instead of the volume-weighted average formula, and inventing numeric thresholds (slope, stop offset, candle size) the text never gives.
