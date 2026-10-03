# Secrets of a Pivot Boss — Franklin O. Ochoa, Jr. (311 Publishing, 2010)

- **Source file:** Google Drive `secrets-of-a-pivot-boss-.pdf` (file id `1c1AgbaPMn4J7-1c4vvmKau2uhdd0Gkba`, 1,568,887 bytes), 314 PDF pages with a text layer.
- **Text file used:** text/ochoa_secrets_pivot_boss.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number). Here the printed page numbers coincide with the PDF index.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/ochoa_secrets_pivot_boss.md text/ochoa_secrets_pivot_boss.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 314]], including Appendix A (pivot statistics) and Appendix B (VBA code). Charts are images; only captions and prose are available.

## 1. The method in brief

The book is a toolkit of price-derived support/resistance levels, each computed from the prior period's high, low and close (or, for the Money Zone, its volume profile):

- **Floor Pivots,** with the Central Pivot Range (CPR) [p. 112–114, 136].
- **The Camarilla Equation** [p. 183–185].
- **Money Zone / Market Profile** value area and point of control [p. 60–68].

Trades come from four candlestick reversal triggers (wick, extreme, outside, doji) [p. 31–55] at these levels, interpreted with four pieces of context:

- **Pivot trend:** buy at support in an uptrend, sell at resistance in a downtrend [p. 124].
- **Two-day relationships:** today's range vs. yesterday's (Higher/Lower/Inside/Outside Value) [p. 139–153].
- **Pivot width:** a narrow CPR means a trend day; a wide CPR means a range day [p. 154–163].
- **The open** relative to the prior range and value [p. 72–76].

Most examples are 5–15-minute futures charts. Ch. 9 applies the same rules to weekly, monthly and yearly pivots for swing and position traders [p. 235–257].

**Evidence:**
- Chart anecdotes.
- One 8-month YM touch-statistics study: the CP is touched on 63% of days and L1 on 73.3% [p. 290–296].
- The author's claim to have back-tested the extreme reversal "over countless years" [p. 38], without numbers.

## 2. Strategies

Common definitions (from the prior period's H, L, C):

```
PP = (H+L+C)/3 ; BC = (H+L)/2 ; TC = 2*PP - BC        (swap so TC >= BC)
R1 = 2PP - L ; S1 = 2PP - H ; R2 = PP + (H-L) ; S2 = PP - (H-L)
R3 = R1 + (H-L) ; S3 = S1 - (H-L) ; R4 = R3 + (R2-R1) ; S4 = S3 - (S1-S2)
Camarilla: Hn/Ln = C ± (H-L)*1.1/k with k = 12,6,4,2 for n = 1..4 ; H5 = (H/L)*C ; L5 = C - (H5 - C)
```

[p. 113–114, 136, 183–185]

### 2.1 Wick reversal setup

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | candlestick reversal trigger | 31 |
| Timeframe & holding period | Any bar size; examples 5-min intraday | 36–38 |
| Universe / eligibility filters | Any liquid market | 117 |
| Market / regime filter | Best at "overvalued/undervalued" areas (pivot levels, initial-balance extremes) | 34, 36 |
| Setup conditions | Wick ≥ 2× body (prefers 2.5–3.5×); bullish: close in the top 35% of the range (stricter variants 5–25%); bearish: mirror | 32–34 |
| Entry trigger & order type | Signal bar; optional confirmation: the next bar closes beyond the wick candle's extreme (above its high for longs) | 37 |
| Initial stop-loss | Beyond the wick candle's extreme (examples: "fixed loss stop below the low of the wick reversal candlestick") | 232 |
| Exits: profit-taking | Next pivot level (e.g. R1/H3) per context | 129, 232 |
| Exits: trailing / time / signal | Not specific to the setup | — |
| Position sizing | Not stated | — |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Wick/body ratio | 2.5 (code default) | 2:1 minimum, 2.5–3.5 ideal, 3:1 and 3.5:1 in examples | 32, 36–37, 298 |
| Close percentage | 0.25 (code `Body_Percentage`) | 35% max; 5–25% stricter | 33–34, 298 |
| Doji-wick case | if O = C, range ≥ multiplier × (H − C) | — | 298 |
| Marubozu case | O = H = C (or O = L = C) and range ≥ 50-bar average range | — | 298 |

**Key quotes**

- "A wick that is between 2.5 to 3.5 times larger than the size of the body is ideal." [p. 34]
- "For a bullish reversal wick to exist, the close of the bar should fall within the top 35 percent of the overall range of the candle." [p. 34]
- "requiring the close price of the bar following the reversal wick candlestick to be lower than the low of the wicking candle (reverse for longs)" [p. 37]

**Pseudocode**

```
bull: (C>O and (O-L) >= 2.5*(C-O) or C<O and (C-L) >= 2.5*(O-C)) and (H-C) <= 0.25*(H-L)
bear: mirror with the upper wick and (C-L) <= 0.25*(H-L)
optional confirm (bull): C[t+1] > H[t]   -> enter at O[t+2] (or close of t+1)
```

**Ambiguities & assumptions**

- The code's bullish branch measures the wick as O − L for green candles and C − L for red candles [p. 298]. ASSUMPTION: the lower wick = min(O, C) − L.

### 2.2 Extreme reversal setup

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion ("rubber band") two-bar reversal | 38 |
| Timeframe & holding period | Any; examples 15-min, often the first 30 min of the session | 41–43 |
| Market / regime filter | Best on pull-backs in the direction of an existing trend; can fail against an aggressive trend | 43–44 |
| Setup conditions | Bar 1: range ≈ 2× the average range of the lookback (50–100% larger); body > 50% of its range (watch > 85%); body > average body. Bar 2: opposite colour | 39–40, 299 |
| Entry trigger & order type | Signal at bar 2's close (enter next bar) | 299 |
| Initial stop-loss | Not specified for the setup itself | — |
| Exits | Pivot targets per context | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Range multiplier | 2.0 | 1.5–2.0 depending on volatility | 39, 299 |
| Body share of bar 1 | ≥ 0.525 (code) | > 50%, caution > 85% | 40, 299 |
| Lookback | 50 bars | — | 299 |

**Key quotes**

- "The first bar of the pattern is about two times larger than the average size of the candles in the lookback period." [p. 40]
- "The body of the first bar of the pattern should encompass more than 50 percent of the bar’s total range, but usually not more than 85 percent." [p. 40]
- "The extreme reversal setup is a fabulous signal that I’ve back tested over countless years of data on many instruments, different timeframes, and using various trade management methodologies." [p. 38]

**Pseudocode**

```
long  if (O[1]-C[1]) >= 0.525*(H[1]-L[1]) and (H[1]-L[1]) > 2*SMA(H-L,50) and (O[1]-C[1]) > SMA(|C-O|,50) and C > O
short mirror
```

### 2.3 Outside reversal setup

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | two-bar reversal (failed breakout) | 44–46 |
| Setup conditions | Bull: L < L[1] and C > H[1]; bear: H > H[1] and C < L[1]; the bar is 5–25% larger than the average bar | 45–46 |
| Entry trigger & order type | Signal bar close | 300 |
| Initial stop-loss / exits | Not specified for the setup itself | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Bar-size multiplier | 1.25 × average range (code) | 1.05–1.25 | 45–46, 300 |
| Lookback | 50 | up to 250 | 300 |

**Key quotes**

- "the current bar’s low must be lower than the prior bar’s low and the current bar’s close must be higher than the prior bar’s high" [p. 45]
- "The engulfing bar is usually 5 to 25 percent larger than the size of the average bar in the lookback period." [p. 46]

**Pseudocode**

```
long  if L < L[1] and C > H[1] and (H-L) >= 1.25*SMA(H-L,50) ; short mirror
```

### 2.4 Doji reversal setup

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | indecision reversal after a move | 49–52 |
| Timeframe | Prefers ≥ 15-min bars; higher timeframe = more reliable | 54 |
| Setup conditions | \|C − O\| ≤ 10% of the range; bullish doji high below SMA(10) (bearish: low above SMA(10)) | 52 |
| Entry trigger | One of the next two bars closes above the doji high (bullish) / below the doji low (bearish), and that bar is green/red | 52, 301 |
| Initial stop-loss / exits | Not specified for the setup itself | — |

**Key quotes**

- "The open and close price of the doji should fall within 10 percent of each other, as measured by the total range of the candlestick." [p. 52]
- "For a bullish doji, the high of the doji candlestick should be below the ten-period simple moving average (H < SMA(10))." [p. 52]

**Pseudocode**

```
doji[d] := |C-O| <= 0.10*(H-L) ; bull if doji[d] and H[d] < SMA(C,10)[d] and exists t in {d+1,d+2}: C[t] > H[d] and C[t] > O[t] (first such t) -> long
```

### 2.5 Floor-pivot trend play (buy S1/CPR in an uptrend, sell R1/CPR in a downtrend)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend pull-back at pivot support | 124–131 |
| Timeframe & holding period | Intraday entries on daily pivots; the same logic on weekly/monthly pivots for swing/position trades | 130, 237–238 |
| Market / regime filter | Uptrend persists while price stays above S1 (daily closes); a close beyond R1 in a downtrend flips it to an uptrend; a close below S1 ends the uptrend | 125–126, 130 |
| Setup conditions | Uptrend; open between S1 and R1 | 129 |
| Entry trigger & order type | Pull-back to S1 or the CPR plus a candle trigger (e.g. a wick reversal) | 125, 129 |
| Initial stop-loss | "fixed loss stop set to a new low" | 129 |
| Exits: profit-taking | R1 or R2 (the nearest pivot when the pivots are wide) | 125, 129 |
| Position sizing | Not stated | — |

**Key quotes**

- "Buy at support in an uptrend and sell at resistance in a downtrend." [p. 124]
- "This pattern of trending behavior will usually last as long as price remains above S1 support while in an uptrend, or below R1 resistance while in a downtrend." [p. 125]

**Pseudocode** (daily pivots, intraday or daily bars)

```
trend = up after a daily close > R1 (from down); down after a daily close < S1 (from up)
up & S1 < open < R1: limit/trigger buy at max(TC, S1-touch) on a wick-reversal confirm; stop = session low - tick; target R1 (R2 if CPR narrow)
```

### 2.6 Breakaway play (narrow pivots + gap beyond the prior range)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-day breakout | 131–134 |
| Setup conditions | Advance warning: an abnormally narrow CPR, Inside Value two-day relationship or narrow value area. Trigger day: open gaps beyond the prior day's range and beyond R1 (S1), but not far past the second layer | 87–91, 131–133, 154–159 |
| Entry trigger & order type | Let the first 15-min bar finish; enter on its successful test of the gapped pivot (e.g. a bullish wick reversal at R1) at the next bar's open; or "ambush" with a limit order at the pivot | 131–133 |
| Initial stop-loss | Below the day's low | 133 |
| Exits | 1.5 ATR trailing stop (2 ATR in Ch. 4); exit 15 min before the close; targets R3/R4 | 90, 132–133, 158–159 |

**Key quotes**

- "the third and fourth layers are 30 percent more likely to be tested when price gaps beyond the first layer of the indicator." [p. 132]
- "In addition, the gap should occur no farther than the second layer of the pivots." [p. 132]
- "I then allowed the 1.5 ATR cushion on my trailing profit stop to do the rest of the work" [p. 133]
- "Typically, an extremely tight central pivot range indicates the market traded sideways or consolidated in the prior period of time" [p. 154]

**Pseudocode** (daily-bar adaptation)

```
narrow = (TC-BC)/PP ranks in the bottom 20% of its last 60 days  (ASSUMPTION)
if narrow and O > H[1] and O > R1 and O <= R2*1.0x: buy at the open (or at R1 limit if touched); stop = L of day; exit on close (intraday) or trail 1.5*ATR(14)
```

### 2.7 CPR two-day relationship / "buy the dip at the CPR"

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend continuation pull-back | 139–153, 166–172 |
| Setup conditions | Higher Value (today's BC > yesterday's TC) or Overlapping Higher Value, and the prior close above its CPR; the open is above BC (better: above TC). Bearish mirror for Lower Value | 140–147 |
| Entry trigger & order type | Pull-back to the CPR plus a candle trigger, early in the session | 140, 171 |
| Initial stop-loss | Beyond the far side of the CPR (short example: stop above TC) | 172 |
| Exits: profit-taking | New high/low within the trend, or R1/R2 (S1/S2) | 140, 172 |
| Rejection rule | An open beyond the CPR against the bias reverses it (e.g. a Higher Value day opening below BC → sell the CPR) | 142, 146 |

Two-day bias table: Higher = bullish; Overlapping Higher = moderately bullish; Lower = bearish; Overlapping Lower = moderately bearish; Unchanged = sideways/breakout; Outside = sideways; Inside = breakout [p. 139].

**Key quotes**

- "If the market opens the day anywhere above the bottom of the pivot range, you will look to buy a pull-back to the range ahead of a move to new highs." [p. 140]

### 2.8 Trailing-centrals swing trade (CPR trend on daily bars)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | swing trend-following | 167–169 |
| Timeframe & holding period | Multi-day, daily CPR (the same code works on monthly pivots) | 168, 309 |
| Entry trigger | A close above the CPR that breaks a downtrend; prefers price holding above the CPR for two days; afterwards buy the dips to the CPR | 168 |
| Initial stop / trailing | Long: exit when price closes below the bottom central pivot (BC), updated daily; short: TC. The code exits intrabar on L ≤ BC | 168, 309 |

**Key quotes**

- "you will look for price to hold above the central pivot range for two consecutive days." [p. 168]
- "You would remain in the uptrend until price closes below the bottom central pivot, at which point you would liquidate your trade." [p. 168]

**Pseudocode** (daily)

```
entry long at next open after C[t] > TC[t] and C[t-1] <= TC[t-1] (trend break)   # variant: require C > TC two days
exit at next open after C[t] < BC[t]   # code variant: exit intrabar when L <= BC
```

**Ambiguities & assumptions**

- The prose exits on a close below BC [p. 168]; the code exits on a touch (L ≤ BC) [p. 309]. Test both.

### 2.9 Magnet trade (gap fill to the CPR)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | gap-fade intraday | 173–179 |
| Setup conditions | Moderate gap at the open; CPR sits near the prior close; best in earnings months (Jan/Apr/Jul/Oct); gap ups preferred; a gap into R1/S1 helps, pivots in the way hurt | 173–177 |
| Entry trigger | Reversal candle in the first bars (doji/wick), or a stop order back through the gapped pivot | 173, 178 |
| Exits | Target = the CPR (any of its three lines); don't wait all day | 173–174 |
| Evidence | CP touched on 63% of days; author's mechanical versions "well over 80 percent" accurate in earnings season | 174, 178 |

**Key quotes**

- "Gaps that are too large don’t tend to fill as easily as those that are moderate in size." [p. 174]
- "the central pivot point is reached 63 percent of the time at some point during the day." [p. 174]

### 2.10 Camarilla third-layer reversal (H3 short / L3 long)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion at H3/L3 | 187–191 |
| Market / regime filter | Better after a wide-range (trend) day; in an uptrend buy L3 only, in a downtrend sell H3 | 191, 229–231 |
| Entry trigger | Test of H3, then a confirmation bar with high < H3 and close < prior close (or any Ch. 2 candle trigger); enter at the confirmation close / next open | 188 |
| Initial stop-loss | At/just above H4 (long: below L4) | 187, 189 |
| Exits | Target L3 (long: H3) | 187, 189 |
| Variant | Abnormally wide pivots: also fade H1/H2/L1/L2 ("hidden layers") | 217–219 |

**Key quotes**

- "any short position taken at the H3 pivot level should carry a stop loss at, or just above, the H4 pivot level." [p. 187]
- "If the following bar’s high falls below H3 and its close is below the prior bar’s close, you have all the confirmation needed to fire off a short trade." [p. 188]

### 2.11 Camarilla fourth-layer breakout (H4 long / L4 short)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout | 192–198 |
| Setup conditions | Prefer a narrow L3–H3 width, an Inside Value two-day relationship, or a prior range day | 197, 204, 215 |
| Entry trigger | Close above H4 (not the first touch) after it has acted as resistance | 193–194 |
| Initial stop-loss | At/just below H3 (short: above L3) | 193, 195 |
| Exits | Target H5 (L5); on a true trend day trail instead (1.5 ATR) | 193, 224 |

**Key quotes**

- "A close above this resistance level is typically the confirmation required for a bullish trade." [p. 194]

### 2.12 Higher-timeframe (monthly) CPR pull-back trend

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | position-trading trend pull-back | 250–252 |
| Timeframe & holding period | Daily chart, monthly pivots (weeks to months) | 238–239, 250 |
| Setup conditions | Prior month closes above the coming month's CPR; the new month opens above BC; Higher Value month-to-month relationships | 251–252 |
| Entry trigger | Pull-back to the monthly CPR (with candle confirmation) | 251, 256 |
| Exits | New highs within the trend (no fixed rule) | 251 |
| Related | A daily exaggerated wick reversal at a multi-timeframe pivot cluster: enter at its close / next open, hold 5–10 days | 275 |

**Key quotes**

- "If price closes the prior month above the pivot range for the following month, continued trending behavior is likely to occur." [p. 251]
- "Instead, taking an entry at the close of the wick candlestick, or at the open of the following bar, will usually prove highly profitable over the following five to ten days." [p. 275]

**Pseudocode** (daily bars, monthly pivots)

```
monthly PP/BC/TC from the prior month's H,L,C
cond: Close(prev month) > TC(this month) and Open(first day) > BC
entry: first daily touch of [BC,TC] with C > TC that day (or wick reversal) -> buy next open
stop: daily close < BC (ASSUMPTION) ; exit: trailing-centrals (2.8) on monthly CPR
```

### 2.13 Golden Pivot Zone (CPR + Camarilla/Money Zone confluence)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | confluence pull-back | 266–273 |
| Setup conditions | Bullish GPZ: L3 (or a Money Zone level) lies within [BC, TC]; bearish: H3 within the CPR. For a long: open above the CPR and the prior close above the prior CPR; in an uptrend | 266–268 |
| Entry trigger | Test of the GPZ with a candle trigger | 268–271 |
| Exits | Next pivot (R1/H3 for longs; S1/L3 for shorts) | 267–268 |

**Key quotes**

- "the Golden Pivot Zone occurs when one of the pivot levels from either the Camarilla Equation or the Money Zone lies within the central pivot range" [p. 266]
- "First, price should open the day above the central pivot range. Second, the prior session’s closing price should fall above the prior day’s central pivot range." [p. 268]

**Pseudocode**

```
bullGPZ = BC <= L3 <= TC ; if uptrend and O > TC and C[1] > TC[1]: buy the first touch of the zone + wick reversal; target R1/H3
```

## 3. Risk & money-management rules

- Know the entry, target and stop before entering [p. 286].
- Use trend-day exits (trailing 1.5–2 ATR, exit near the close) on narrow-pivot or breakaway days, and fixed targets on wide-pivot days [p. 87, 90, 159, 163].
- After R2/S2, begin liquidating; L3/L4 are reached rarely (17.6% / 5.5% of days) [p. 291].
- Trade smaller or stand aside on wide-CPR, Outside Value days [p. 159–160].
- Bet bigger when confluence aligns ("double-down") [p. 261]. No sizing formula is given.
- Drop markets that don't respect pivots [p. 282].

## 4. Non-codable guidance

- **Day types:** Trend, Double-Distribution, Typical, Expanded Typical, Trading Range, Sideways. These are judged from the initial balance (first hour) [p. 19–28].
- **Money Zone:** the value area, POC and volume-at-price need intraday TPO/volume data. Virgin POC/VPOC "magnets" are said to be filled within a week, citing "upwards of 80 percent" from unnamed research [p. 96–107, 100].
- **Daily flight plan:** two-day relationships, width, virgin levels, hot zones [p. 282–285].
- **Pivot statistics** (YM, Nov 2008 – Jun 2009) [p. 290–296]:
  - CP touched 63%, L1 73.3%, L2 38.2%, L3 17.6%, L4 5.5%.
  - When the CP is not touched, a close beyond L1 occurs on 73.8% of days.

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - Daily OHLC for floor/CPR/Camarilla pivots on daily bars (2.1–2.4, 2.8, 2.12, 2.13) and for monthly/weekly pivots.
  - 5–15-minute bars for the intraday plays (2.5–2.7, 2.9–2.11).
  - Intraday volume-at-price for the Money Zone.
- **Testability with our data:** Daily-bar adaptations are fully backtestable from 2005:
  - candle triggers at monthly/weekly pivots;
  - the trailing-centrals swing;
  - the monthly CPR dip-buy;
  - narrow-CPR breakouts using the gap at the open.

  The intraday versions need an intraday data source.
- **Market-structure differences:**
  - Long-only cash: test the long sides.
  - The CPR is widely used by Indian retail traders, which arguably helps the "self-fulfilling" premise [p. 112, 182].
  - Gaps on NSE are frequent, so the magnet/breakaway gap filters need percentage thresholds. ASSUMPTION: a moderate gap = 0.3–1.0% of the prior close.
  - Costs: intraday turnover makes STT, brokerage and slippage material; report net.

## 6. Verdict

- **Codeability:** Partly.
  - Fully codable: pivot formulas, the four candle triggers (with code [p. 298–301]), the trailing-centrals stop [p. 309], and the Camarilla reversal/breakout rules.
  - Needs thresholds the book leaves open: "trend", "narrow/wide" and "moderate gap".
  - Not codable: day-type reading.
- **Priority for backtesting:** Medium.
  - Worth testing on NSE daily data: the trailing-centrals swing (2.8), the monthly CPR dip-buy (2.12) and narrow-CPR breakouts (2.6), since daily OHLC is all they need.
  - The intraday plays need minute data.
  - Evidence is anecdotal apart from the YM touch statistics.
- **Top 3 things a coder is most likely to get wrong**
  1. Using the book's printed S2 formula, `S2 = Pivot - (High + Low)` [p. 113–114], which is a typo; the standard (and consistent with R2) is PP − (H − L).
  2. Not swapping TC and BC when the formula inverts them: the higher line is always TC [p. 136].
  3. Buying the first touch of H4 instead of waiting for a close above it [p. 193–194], or taking the gap trade without the limit that the gap must not reach beyond the second layer [p. 132].
