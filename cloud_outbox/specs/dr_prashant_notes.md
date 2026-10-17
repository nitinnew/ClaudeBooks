# Chart Patterns Notes and Candlestick Patterns Notes — Dr Prashant Bansal

- **Source file:** Google Drive: "Chart Patterns Notes by Dr Prashant.pdf" (pages 1-9) and "Candlestick Patterns Notes by Dr Prashant.pdf" (pages 10-17), concatenated (resource key dr_prashant_notes). Author named in page footers only.
- **Text file used:** text/dr_prashant_notes.txt  (page basis: pdf_pages, column-aware RapidOCR of page images; the PDFs have no text layer)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (continuous PDF page index across both files: chart notes = p. 1-9, candlestick notes = p. 10-17). The candlestick PDF's own footer reads "Page 1".."Page 8" and the chart PDF's footer "Page 1".."Page 9"; those printed footers are NOT used.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - Before finishing, `python ../work/bin/verify_citations.py specs/dr_prashant_notes.md text/dr_prashant_notes.txt` was run and fixed to zero wrong page / zero not found.
- **Coverage:** Read lines 1-521 of the text file (the whole file, one read); last marker reached [[PAGE 17]]; nothing skimmed. OCR caveats: spaces are often dropped inside words (quotes below keep the OCR spacing); the footer lines "Dr Prashant Bansal", "ChartPatterns-Notes"/"CandlestickPatterns-Notes" and "Page N" fall mid-page and were ignored; the inverted-hammer text on p. 13 is garbled; the bull-harami text on p. 13 is cut off at "second green candle". All pattern illustrations are images and are not in the text: only stray labels survive (Breakout and Retest on p. 3-7 and 9; Stop Loss and Entry on p. 14; "closing should be more than 50% of previous candle" on p. 11). The third file (Trading Psychology Notes) is not included. *Coordinator check: both PDFs are page images (the text layer held only the footer), so the coordinator OCR'd all 17 pages with a column-aware RapidOCR pass (left column, then right). The coordinator re-ran verify_citations (95/95 ok) and an exact-page strict check (0 off-by-one), and confirmed all 29 field tables have exactly the 12 template rows (2.0 is a shared-definitions table, not a strategy). Spot-checked by grep: triangles break 'any direction' p.9, piercing 50% close p.11, wedges p.4, rectangles p.5, three white soldiers p.12, harami cut off at 'second green' p.13, Stop Loss/Entry labels p.14, evening-star 'completely' rule p.15; all matched.*

## 1. The method in brief

These are two pattern cheat-sheets, not a trading system. Each page gives a one-paragraph definition of a chart pattern (p. 1-9) or candlestick pattern (p. 10-17) and, for chart patterns, a one-line "breakout confirmed once ..." rule (price closes beyond a support or resistance level or trendline). The candlestick pages give only structural definitions (shape of one to three candles plus the trend they occur in) and no confirmation or entry trigger. The patterns are classed as reversal (double/triple top and bottom, head and shoulders, wedges, cup and handle, all single and multi-candle candlestick patterns) or continuation (rectangles, flags, symmetrical triangles) patterns.

No timeframe, market, universe, stop-loss, profit target, position size, holding period, win rate, back-test or track record is given anywhere in this text. Those fields are marked "Not found in this text" in every strategy below, and any default used in the pseudocode is an `ASSUMPTION:` of this specification, not the author's. Because the text is an image-OCR of terse notes, many definitions are ambiguous (for example, how "equal" two tops must be, or what counts as a "downtrend"); the Ambiguities of each strategy and section 2.0 record the defaults chosen.

## 2. Strategies

Twenty-nine patterns have a codable definition and are listed as separate strategies (2.1-2.16 chart patterns, 2.17-2.29 candlestick patterns). They are not grouped as mirror pairs because the text never states exact mirrors (it says only that the bear flag is "an upside down version of the bull flag" [p. 6] and that the shooting star is "inverse of the hanging" man [p. 16]). Ascending triangle, descending triangle and doji have no testable trigger and are listed in section 4.

### 2.0 Shared definitions used by the pseudocode (not a strategy; all values are ASSUMPTIONS of this spec)

The text gives none of these; every pattern below needs them.

| Item | ASSUMPTION default | Reason |
|---|---|---|
| Daily bars | Pattern detection on daily OHLC; signal evaluated on bar close; order at next day's open | Timeframe not found in this text |
| Swing pivot (fractal) | bar i is a pivot high if high[i] is the max of high[i-N..i+N], N = 5; the pivot is only known at bar i+N (avoid look-ahead) | Text refers to highs/lows without defining them |
| "Equal" levels (tops, bottoms, shoulders) | within TOL_EQ = 3% of each other | Text says only "two consecutive" highs, "similar in height" |
| Uptrend / downtrend before a reversal pattern | downtrend: close < SMA(50) and SMA(50) < SMA(50) 10 bars ago; uptrend: mirror | Text says "occurs at downtrend" / "end of uptrend" with no definition |
| Candle geometry | body = abs(C-O); range = H-L; upper = H-max(O,C); lower = min(O,C)-L; bull = C>O; bear = C<O | Standard OHLC arithmetic |
| Doji | body <= 10% of range | Text: opening and closing prices "almost equal" [p. 17] |
| Breakout / breakdown | bar CLOSE beyond the level or trendline | Text says "breaks" / "falls below" without close or intraday |
| Long-only handling (NSE cash) | Bullish signals = buy at next open; bearish signals = exit or avoid a long, no short | No overnight shorting in NSE cash |
| Exits and stops | Not found in this text. For a back-test only: stop = pattern invalidation extreme, exit on opposite pattern or after 20 bars | Needed to run any back-test |

### 2.1 Double Top (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal, bearish (called an extremely bearish technical reversal pattern) | 1 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated; pattern forms after an asset has reached a high price | 1 |
| Setup conditions | Price reaches a high two consecutive times with a moderate decline between the two highs | 1 |
| Entry trigger & order type | Confirmed once price falls below a support level equal to the low between the two prior highs. Order type not stated | 1 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| TOL_EQ (how equal the tops/bottoms must be) | Not found in this text | ASSUMPTION: 3% | - |
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| MIN_DECL (what counts as moderate decline between highs) | Not found in this text | ASSUMPTION: 5% of the lower high | 1 |

**Key quotes**

- "A double top is anextremely" [p. 1]
- "high price two consecutive times" [p. 1]
- "support levelequal to thelow" [p. 1]
- "between the twopriorhighs." [p. 1]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  H1,H2 = last two confirmed pivot highs (i1<i2), |H1-H2|/max(H1,H2) <= TOL_EQ
  L = min(low[i1..i2])                     # low between the two highs
  require (min(H1,H2)-L)/min(H1,H2) >= MIN_DECL
  if close[t] < L and t > i2 and no close < L in (i2, t): SIGNAL_BEARISH at t   # exit/avoid long
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Book says the confirmation level is the low between the two highs but does not say whether a close or an intraday break is needed. ASSUMPTION: close below L.
- Book gives no tolerance for the two highs being equal and no minimum decline or minimum spacing. ASSUMPTION: TOL_EQ 3%, MIN_DECL 5%, at least 5 bars between highs.

### 2.2 Double Bottom (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal, bullish (called an extremely bullish technical reversal pattern) | 1 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated; pattern forms after an asset has reached a low price | 1 |
| Setup conditions | Price reaches a low two consecutive times with a moderate support (rebound) between the two lows | 1 |
| Entry trigger & order type | Confirmed once price goes above a resistance level equal to the high between the two prior lows. Order type not stated | 1 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| TOL_EQ (how equal the tops/bottoms must be) | Not found in this text | ASSUMPTION: 3% | - |
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| MIN_REBOUND (what counts as moderate support between lows) | Not found in this text | ASSUMPTION: 5% of the higher low | 1 |

**Key quotes**

- "A doublebottom isanextremely" [p. 1]
- "lowprice two consecutive times" [p. 1]
- "resistance level equal to the high" [p. 1]
- "between thetwopriorlows." [p. 1]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  L1,L2 = last two confirmed pivot lows (i1<i2), |L1-L2|/max(L1,L2) <= TOL_EQ
  Hm = max(high[i1..i2])                   # high between the two lows
  require (Hm-max(L1,L2))/max(L1,L2) >= MIN_REBOUND
  if close[t] > Hm and t > i2 and no close > Hm in (i2, t): BUY at open[t+1]
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Close versus intraday break is not stated. ASSUMPTION: close above Hm.
- Tolerance for equal lows and the size of the rebound are not given. ASSUMPTION: TOL_EQ 3%, MIN_REBOUND 5%.

### 2.3 Triple Top (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal, bearish (extremely bearish technical reversal pattern) | 2 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated; pattern forms after an asset has reached a high price | 2 |
| Setup conditions | Price reaches a high three consecutive times with a moderate decline between the three highs | 2 |
| Entry trigger & order type | Confirmed once price falls below a support level equal to the low between the three prior highs. Order type not stated | 2 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| TOL_EQ (how equal the tops/bottoms must be) | Not found in this text | ASSUMPTION: 3% | - |
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| MIN_DECL | Not found in this text | ASSUMPTION: 5% | 2 |

**Key quotes**

- "high price three consecutive times" [p. 2]
- "asupportlevel equal to thelow" [p. 2]
- "between the three prior highs." [p. 2]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  H1,H2,H3 = last three confirmed pivot highs (i1<i2<i3), all within TOL_EQ of each other
  L = min(low[i1..i3])      # ASSUMPTION: lowest low between the three highs (text: "the low between")
  if close[t] < L and t > i3 and not yet triggered: SIGNAL_BEARISH at t
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Book says one support level equal to the low between the three highs; there are two inter-peak lows. ASSUMPTION: use the lower of the two (min over i1..i3).
- Same tolerance/close-versus-intraday gaps as double top.

### 2.4 Triple Bottom (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal, bullish (described as bullish; the word extremely is not used) | 2 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated; pattern forms after an asset has reached a low price | 2 |
| Setup conditions | Price reaches a low three consecutive times with a moderate support between the three lows | 2 |
| Entry trigger & order type | Confirmed once price goes above a resistance level equal to the high between the three prior lows. Order type not stated | 2 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| TOL_EQ (how equal the tops/bottoms must be) | Not found in this text | ASSUMPTION: 3% | - |
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| MIN_REBOUND | Not found in this text | ASSUMPTION: 5% | 2 |

**Key quotes**

- "a moderatesupportbetween the" [p. 2]
- "resistance level equal to the high" [p. 2]
- "between the threeprior lows." [p. 2]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  L1,L2,L3 = last three confirmed pivot lows (i1<i2<i3), all within TOL_EQ
  Hm = max(high[i1..i3])    # ASSUMPTION: higher of the two inter-trough highs is the highest high in the span
  if close[t] > Hm and t > i3 and not yet triggered: BUY at open[t+1]
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Which of the two inter-trough highs is the resistance is not stated. ASSUMPTION: the higher one (more conservative breakout).

### 2.5 Head and Shoulders (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal, bearish (the text calls it a chart formation; direction is implied by the support break) | 3 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Baseline with three peaks: the outside two are similar in height and the middle one is highest | 3 |
| Entry trigger & order type | Breakout confirmed once the asset breaks the support level. Order type not stated; a Retest label appears on the illustration only | 3 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| TOL_EQ (how equal the tops/bottoms must be) | Not found in this text | ASSUMPTION: 3% | - |
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| Support level definition (neckline) | Called support level; not defined | ASSUMPTION: neckline = line through the two troughs between the peaks; horizontal = lower of the two troughs | 3 |

**Key quotes**

- "baseline withthree peaks,where" [p. 3]
- "theoutsidetwoaresimilarin" [p. 3]
- "height and the middle is highest &" [p. 3]
- "breaks support level &it" [p. 3]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  P1,P2,P3 = last three confirmed pivot highs; P2 > max(P1,P3); |P1-P3|/max(P1,P3) <= TOL_EQ
  S = min(low between P1..P2, low between P2..P3)           # support level (neckline), horizontal
  if close[t] < S and t > idx(P3) and not yet triggered: SIGNAL_BEARISH at t
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Support level is not defined (neckline not named). ASSUMPTION: horizontal line at the lower of the two troughs.
- Retest is drawn on the illustration (p. 3) but no retest entry rule is written. ASSUMPTION: ignore retest; enter on the break only.
- Prior-uptrend requirement is not stated. ASSUMPTION: require uptrend per 2.0 before the left shoulder.

### 2.6 Inverse Head and Shoulders (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal, bullish (described as similar to head and shoulders but inverted) | 3 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Used to predict reversals in downtrends (described relative to the head and shoulders top) | 3 |
| Setup conditions | Price falls to a trough and rises; falls below the previous trough and rises again; then falls again but not as far as the second trough | 3 |
| Entry trigger & order type | Once the final trough is made, price heads upward and breaks resistance. Order type not stated; a Retest label appears on the illustration only | 3 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| TOL_EQ (how equal the tops/bottoms must be) | Not found in this text | ASSUMPTION: 3% | - |
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| Resistance level definition (neckline) | Called resistance; not defined | ASSUMPTION: horizontal at the higher of the two peaks between the troughs | 3 |

**Key quotes**

- "Aninversehead and shoulders is" [p. 3]
- "fallsbelowtheprevioustrough" [p. 3]
- "pricefallsagainbutnotasfaras" [p. 3]
- "upward & breaks resistance" [p. 3]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  T1,T2,T3 = last three confirmed pivot lows; T2 < T1; T2 < T3; T3 > T2     # head lowest, final trough above the head
  R = max(high between T1..T2, high between T2..T3)       # resistance
  if close[t] > R and t > idx(T3) and not yet triggered: BUY at open[t+1]
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Text does not require shoulders to be similar in height (unlike the head and shoulders top); it requires only that the third trough is not as low as the second. ASSUMPTION: also require |T1-T3| within 10% (looser than TOL_EQ) - or drop it for a literal reading.
- Retest shown on illustration only. ASSUMPTION: enter on the break.

### 2.7 Rising Wedge (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal (identifies possible trend reversals); breakout direction is downward | 4 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Upward-sloping price chart with two converging trendlines; usually accompanied by decreasing trading volume | 4 |
| Entry trigger & order type | Breakout confirmed once price breaks the support trendline and goes downward. Order type not stated; a Retest label appears on the illustration only | 4 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| Volume decline | Described as usual, not required | ASSUMPTION: optional filter, volume SMA(10) falling across the pattern | 4 |
| Minimum touches per trendline | Not found in this text | ASSUMPTION: 2 pivot lows and 2 pivot highs | - |

**Key quotes**

- "The rising wedge is a technical" [p. 4]
- "decreasing trading volume." [p. 4]
- "breakoutconfirmedonceit" [p. 4]
- "break support trendline goes" [p. 4]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  fit upper line through last 2-3 pivot highs, lower line through last 2-3 pivot lows
  require both slopes > 0 and lower slope > upper slope (converging, rising)
  if close[t] < lower_line(t): SIGNAL_BEARISH at t
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Volume decline is described as usual (accompanying), not as a requirement. ASSUMPTION: do not require it; test as a filter.
- Prior-trend context is not stated for the rising wedge. ASSUMPTION: no trend filter.

### 2.8 Falling Wedge (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal when found in a downward trend; breakout direction is upward | 4 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | When this pattern is found in a downward trend it is considered a reversal pattern | 4 |
| Setup conditions | Market makes lower lows and lower highs with a contracting range (converging trendlines) | 4 |
| Entry trigger & order type | Breakout confirmed once price breaks the resistance trendline and goes upward. Order type not stated; a Retest label appears on the illustration only | 4 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| Minimum touches per trendline | Not found in this text | ASSUMPTION: 2 pivot lows and 2 pivot highs | - |
| Downtrend definition | Not found in this text | ASSUMPTION: see 2.0 | 4 |

**Key quotes**

- "makeslowerlowsandlower" [p. 4]
- "highs with a contracting range." [p. 4]
- "areversalpattern,breakout" [p. 4]
- "resistance trendline and goes" [p. 4]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  require downtrend per 2.0
  fit upper line (pivot highs) and lower line (pivot lows); both slopes < 0 and upper slope steeper (range contracting)
  if close[t] > upper_line(t): BUY at open[t+1]
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- The definition says lower lows and lower highs with a contracting range; it does not say which line is steeper. ASSUMPTION: converging, i.e. upper line falls faster than lower line.

### 2.9 Bullish Rectangle (continuation)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation, bullish | 5 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs when price pauses during a strong trend | 5 |
| Setup conditions | Price temporarily bounces between two parallel levels before the trend continues | 5 |
| Entry trigger & order type | Breakout confirmed once price breaks its resistance and goes in the upward direction. Order type not stated | 5 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Strong trend definition | Not found in this text | ASSUMPTION: close > SMA(50) and 20-bar return > 10% before the box | 5 |
| Parallel-level tolerance | Not found in this text | ASSUMPTION: highs within 3% and lows within 3%; at least 2 touches each | - |
| Minimum box length | Not found in this text | ASSUMPTION: 10 bars | - |

**Key quotes**

- "occur when a price pauses" [p. 5]
- "during a strong trend and" [p. 5]
- "two parallel levels before the" [p. 5]
- "resistance & goes in upward" [p. 5]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  require prior strong uptrend (ASSUMPTION definition above)
  box = last K>=10 bars where pivot highs within TOL and pivot lows within TOL (>=2 touches each)
  R = max(high over box)
  if close[t] > R: BUY at open[t+1]
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Strong trend and the duration of the pause are not defined. ASSUMPTION: as in Parameters.

### 2.10 Bearish Rectangle (continuation)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation, bearish | 5 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs when a price pauses during a strong downtrend | 5 |
| Setup conditions | Price temporarily bounces between two parallel levels before the trend continues | 5 |
| Entry trigger & order type | Breakout confirmed once price breaks its support and goes in the downward direction. Order type not stated | 5 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Strong downtrend definition | Not found in this text | ASSUMPTION: close < SMA(50) and 20-bar return < -10% before the box | 5 |
| Parallel-level tolerance | Not found in this text | ASSUMPTION: highs and lows each within 3%, at least 2 touches each | - |
| Minimum box length | Not found in this text | ASSUMPTION: 10 bars | - |

**Key quotes**

- "occurswhenapricepauses" [p. 5]
- "during a strong downtrend and" [p. 5]
- "two parallel levels before the" [p. 5]
- "support&goesindownward" [p. 5]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  require prior strong downtrend
  box = last K>=10 bars with parallel highs/lows (>=2 touches each)
  S = min(low over box)
  if close[t] < S: SIGNAL_BEARISH at t   # exit/avoid long on NSE cash
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- As bullish rectangle. On NSE cash this is an exit/avoid signal only.

### 2.11 Bullish Flag (continuation)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation, bullish (good continuation pattern) | 6 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Found in stocks with strong uptrends | 6 |
| Setup conditions | The pole is a vertical rise in the chart; the flag results from a period of consolidation | 6 |
| Entry trigger & order type | Breakout confirmed once price breaks from the upper side of the flag. Order type not stated; a Retest label appears on the illustration only | 6 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pole size (vertical rise) | Not found in this text | ASSUMPTION: >= 15% rise in <= 10 bars | 6 |
| Flag length | Not found in this text | ASSUMPTION: 5-20 bars, counter-trend, retracing <= 50% of pole | - |
| Upper flag line | Upper side of the flag | ASSUMPTION: line through flag pivot highs, or highest high of the flag | 6 |

**Key quotes**

- "found in stocks with strong" [p. 6]
- "The pole is the result of a" [p. 6]
- "flag results froma period of" [p. 6]
- "confirmedonceitbreaksfrom" [p. 6]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  pole = a rise of >= POLE_PCT within <= POLE_BARS ending at bar p
  flag = bars p+1..t-1 (5..20) consolidating, retracement <= 50% of pole
  U = max(high over flag)       # upper side of the flag
  if close[t] > U: BUY at open[t+1]
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Pole size, flag duration, flag slope and retracement are not given. ASSUMPTION: as above.
- The text says the flag is a consolidation; it does not say parallel or sloping down (the bear flag text mentions parallel trendlines, p. 6). ASSUMPTION: use the flag high as the upper side.

### 2.12 Bearish Flag (continuation)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation, bearish (upside-down version of the bull flag) | 6 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | The flagpole forms on an almost vertical panic price drop | 6 |
| Setup conditions | After the vertical drop, a bounce with parallel upper and lower trendlines forms the flag | 6 |
| Entry trigger & order type | Breakout confirmed once the chart breaks from the lower trendline. Order type not stated; a Retest label appears on the illustration only | 6 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pole size (drop) | Not found in this text | ASSUMPTION: >= 15% fall in <= 10 bars | 6 |
| Flag length | Not found in this text | ASSUMPTION: 5-20 bars | - |
| Trendline tolerance | Parallel upper and lower trendlines | ASSUMPTION: use lowest low of the flag | 6 |

**Key quotes**

- "beaish flag is an upside" [p. 6]
- "verticalpanic price drop as" [p. 6]
- "parallel upper and lower" [p. 6]
- "break fromlower trendline." [p. 6]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  pole = a fall of >= POLE_PCT within <= POLE_BARS ending at bar p
  flag = bars p+1..t-1 (5..20) bouncing in parallel channel
  Lw = min(low over flag)
  if close[t] < Lw: SIGNAL_BEARISH at t   # exit/avoid long on NSE cash
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- As bullish flag. The text explicitly calls it the inverted version of the bull flag, so the mirrored parameters are used.

### 2.13 Bullish Symmetrical Triangle (continuation)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation, bullish | 7 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated beyond being a bullish continuation pattern | 7 |
| Setup conditions | Two converging trend lines that are symmetrical in relation to the horizontal line; the top line is a bearish trendline creating the resistance | 7 |
| Entry trigger & order type | Breakout confirmed once the chart breaks resistance and goes in the upward direction. Order type not stated; a Retest label appears on the illustration only | 7 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| Minimum touches | Not found in this text | ASSUMPTION: 2 pivot highs and 2 pivot lows | - |
| Prior uptrend | Implied by continuation | ASSUMPTION: uptrend per 2.0 | 7 |

**Key quotes**

- "A bullishsymmetrical triangle" [p. 7]
- "by two converging trend lines" [p. 7]
- "creating theresistance," [p. 7]
- "breakoutconfirmedonce chart" [p. 7]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  require uptrend per 2.0 before the triangle
  upper = line through last 2+ pivot highs (slope < 0); lower = line through last 2+ pivot lows (slope > 0)
  if close[t] > upper(t): BUY at open[t+1]
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Symmetry is not quantified. ASSUMPTION: absolute slopes within a factor of 2 of each other.
- The text does not say what the preceding trend is, only that the pattern is a bullish continuation. ASSUMPTION: prior uptrend.

### 2.14 Bearish Symmetrical Triangle (continuation)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation, bearish | 7 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated beyond being a bearish continuation pattern | 7 |
| Setup conditions | Two converging trend lines symmetrical about the horizontal line; the lower support line is a bullish trendline | 7 |
| Entry trigger & order type | Breakout confirmed once price breaks support and goes in the downward direction. Order type not stated; a Retest label appears on the illustration only | 7 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pivot window N | Not found in this text | ASSUMPTION: 5 bars | - |
| Minimum touches | Not found in this text | ASSUMPTION: 2 pivot highs and 2 pivot lows | - |
| Prior downtrend | Implied by continuation | ASSUMPTION: downtrend per 2.0 | 7 |

**Key quotes**

- "A bearish symmetrical" [p. 7]
- "continuation chart pattern." [p. 7]
- "lower support line is bullish" [p. 7]
- "trendline,breakout confirmed" [p. 7]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  require downtrend per 2.0 before the triangle
  upper = line through pivot highs (slope < 0); lower = line through pivot lows (slope > 0)
  if close[t] < lower(t): SIGNAL_BEARISH at t   # exit/avoid long on NSE cash
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- As bullish symmetrical triangle.

### 2.15 Cup and Handle (bullish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal/buy-setup (called a technical indicator; handle signals a buying opportunity) | 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Price movement resembles a tea cup followed by a downward-trending price pattern; the drop, or handle, signals a buying opportunity | 8 |
| Entry trigger & order type | Breakout confirmed once price breaks the neckline/resistance and goes upward. Order type not stated | 8 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Cup depth and length | Not found in this text | ASSUMPTION: cup 30-120 bars, depth 12-35% (rounded, left rim ~ right rim within 5%) | - |
| Handle depth and length | Not found in this text | ASSUMPTION: 5-20 bars, retracement <= 50% of cup depth | - |
| Neckline | neckline/resistance | ASSUMPTION: horizontal at the cup's rim high (higher of left rim and handle high) | 8 |

**Key quotes**

- "technicalindicatorwherethe" [p. 8]
- "followedbyadownward" [p. 8]
- "signalabuying opportunity to" [p. 8]
- "neckline/resistance & goes" [p. 8]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  cup = U-shaped decline and recovery (left rim LR, bottom B, right rim RR within 5% of LR)
  handle = 5..20 bars of pullback after RR, depth <= 50% of (LR-B)
  N = max(high[LR], high[RR..handle])                      # neckline
  if close[t] > N: BUY at open[t+1]
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Text is very brief: no dimensions, no volume rule, no handle limits. ASSUMPTION: as above; use a rounding test such as a quadratic fit R^2 >= 0.7.
- The neckline is the same as resistance in the text. ASSUMPTION: horizontal line at the rim high.

### 2.16 Inverted Cup and Handle (bearish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal, bearish (upside-down cup and handle) | 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Formed after a pullback from a swing low before a sell-off to the prior swing low | 8 |
| Setup conditions | Stalls due to underlying support, then stalls like a bear flag with slight upward pressure | 8 |
| Entry trigger & order type | Breaks down below support. Order type not stated | 8 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Cup/handle dimensions | Not found in this text | ASSUMPTION: mirror of 2.15 | - |
| Support | Underlying support | ASSUMPTION: horizontal at the prior swing low / handle low | 8 |

**Key quotes**

- "The inverted Cup and Handle" [p. 8]
- "sell-offtothepriorswing low" [p. 8]
- "muchlikeabearflagwith" [p. 8]
- "breaking down below support." [p. 8]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
for each bar t:
  inverted rounded top, then a handle of slight upward drift (5..20 bars)
  S = support = min(low) of the handle / prior swing low        # ASSUMPTION
  if close[t] < S: SIGNAL_BEARISH at t   # exit/avoid long on NSE cash
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- The description is garbled and partly self-contradictory (a pullback from a swing low, then a sell-off to the prior swing low). ASSUMPTION: treat as a mirror of cup and handle with a breakdown trigger.
- No dimensions, no explicit confirmation sentence like the other patterns; the trigger is inferred from breaking down below support.

### 2.17 Hammer (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle reversal, bullish | 10 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at the end of the downtrend | 10 |
| Setup conditions | Body at the top side with a lower shadow which should be double the body size; little or no upper shadow | 10 |
| Entry trigger & order type | Not found in this text; the text gives the pattern as a bullish-reversal indication only | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Lower shadow / body | 2x (double the body) | none | 10 |
| Upper shadow | little or no | ASSUMPTION: <= 10% of range | 10 |

**Key quotes**

- "Hammer is single candlestick" [p. 10]
- "whichshould be double than" [p. 10]
- "this candle has little or no" [p. 10]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
bullish_hammer(t): downtrend(t-1) and lower[t] >= 2*body[t] and upper[t] <= 0.10*range[t] and body[t] > 0
if bullish_hammer(t): BUY at open[t+1]   # ASSUMPTION: entry; the text gives none
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- No entry trigger or confirmation candle. ASSUMPTION: act on the next bar's open.
- Body colour is not stated. ASSUMPTION: either colour accepted.

### 2.18 Piercing Pattern (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal, bullish | 11 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at downtrend | 11 |
| Setup conditions | First candle is bearish; second candle opens gapped down but closes above 50% of the previous candle | 11 |
| Entry trigger & order type | Not found in this text; the text gives the pattern as a bullish-reversal indication only | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Close above | 50% of previous candle | ASSUMPTION: of the previous candle body midpoint | 11 |
| Gap down | Second candle opens as gap down | ASSUMPTION: open[t] < close[t-1] | 11 |

**Key quotes**

- "second candle open as gap." [p. 11]
- "down but closes above 50%" [p. 11]
- "CLOSINGSHOULDBE" [p. 11]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
piercing(t): downtrend(t-1) and bear[t-1] and open[t] < close[t-1]
             and close[t] > (open[t-1]+close[t-1])/2 and close[t] < open[t-1] and bull[t]
if piercing(t): BUY at open[t+1]   # ASSUMPTION
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- 50% of the previous candle: body or full range is not stated. ASSUMPTION: body midpoint.
- Gap down relative to the prior close or prior low is not stated. ASSUMPTION: below prior close (weaker). Test also the stricter open below prior low.
- The text does not say the close must stay below the first candle's open (to be distinct from engulfing). ASSUMPTION: require it.

### 2.19 Bullish Engulfing (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal, bullish | 11 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at downtrend | 11 |
| Setup conditions | Second candle (green) completely engulfs the first candle; engulfing means covering the previous candle | 11 |
| Entry trigger & order type | Not found in this text; the text gives the pattern as a bullish-reversal signal only | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Engulf | Second candle completely covers first | ASSUMPTION: second body covers first body (open[t] <= close[t-1], close[t] >= open[t-1]) | 11 |

**Key quotes**

- "Bullish Engulfing pattern is a" [p. 11]
- "engulfing means covering" [p. 11]
- "second candle is green" [p. 11]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
bull_engulf(t): downtrend(t-1) and bear[t-1] and bull[t]
                 and open[t] <= close[t-1] and close[t] >= open[t-1]
if bull_engulf(t): BUY at open[t+1]   # ASSUMPTION
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Engulfing of the body versus the full high-low range is not stated; the label on the image reads second candle engulfing the first candle. ASSUMPTION: bodies.
- The text does not say the first candle is red. ASSUMPTION: require bearish first candle (consistent with the downtrend setting).

### 2.20 Morning Star (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle reversal, bullish | 12 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at downtrend | 12 |
| Setup conditions | Three candles: first bearish, second a doji (neutral market), third bullish | 12 |
| Entry trigger & order type | Not found in this text; the third bullish candle is described as showing the market ready to go upward | 12 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Doji | Second candle a doji | ASSUMPTION: body <= 10% of range | 12 |

**Key quotes**

- "The morning star pattern is" [p. 12]
- "its made of three candle first" [p. 12]
- "is bearish, second is doji" [p. 12]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
morning_star(t): downtrend(t-2) and bear[t-2] and doji[t-1] and bull[t]
if morning_star(t): BUY at open[t+1]   # ASSUMPTION; t is the third candle
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Gap requirements and the third candle's close relative to the first candle are not stated for the morning star. ASSUMPTION: require close[t] > midpoint of candle t-2 body. (The evening star text does require the doji to be outside the bodies; the morning star text does not say so.)

### 2.21 Three White Soldiers (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle reversal, bullish | 12 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at downtrend | 12 |
| Setup conditions | Three bullish candles without long shadows; every next candle opens within the previous candle's body | 12 |
| Entry trigger & order type | Not found in this text; the text gives the pattern as a bullish-reversal indication only | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Shadow limit | Do not have long shadows | ASSUMPTION: each shadow <= 25% of range | 12 |
| Open location | Opens within previous candle's body | none | 12 |

**Key quotes**

- "its made of three bullish" [p. 12]
- "they dont have long" [p. 12]
- "every next candle open's" [p. 12]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
three_white(t): downtrend(t-3) and bull[t-2] and bull[t-1] and bull[t]
   and open[t-1] within body[t-2] and open[t] within body[t-1]
   and upper/range and lower/range <= 0.25 for the 3 candles
if three_white(t): BUY at open[t+1]   # ASSUMPTION
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Higher closes are not mentioned but implied. ASSUMPTION: require close[t] > close[t-1] > close[t-2].
- Long shadow is not quantified. ASSUMPTION: 25% of range.

### 2.22 Bullish Harami (bullish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal, bullish | 13 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at downtrend | 13 |
| Setup conditions | First candle is a big red candle, second is a small bullish candle within the range of the previous candle's body | 13 |
| Entry trigger & order type | Not found in this text; the text gives the pattern as a bullish-reversal indication only | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| First candle | Big red | ASSUMPTION: body >= 1.5x the average body of the last 10 bars | 13 |
| Second candle | Small, bullish, inside previous body | ASSUMPTION: body fully inside body of candle t-1 | 13 |

**Key quotes**

- "The bullish harami pattern is a" [p. 13]
- "candle is big red candle and" [p. 13]
- "then second is bullish small" [p. 13]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
bull_harami(t): downtrend(t-1) and bear[t-1] and body[t-1] >= 1.5*avg_body(10)
   and bull[t] and open[t] >= close[t-1] and close[t] <= open[t-1]
if bull_harami(t): BUY at open[t+1]   # ASSUMPTION
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- The sentence ends at: first candle shows bearish trend, second green candle (text cut off at p. 13).
- Big and small are not quantified; within the range of the previous candle's body is ambiguous between body and full range. ASSUMPTION: second body inside first body.

### 2.23 Inverted Hammer (bullish reversal, garbled text)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle reversal; direction not stated in the text | 13 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at end of downtrend | 13 |
| Setup conditions | Text is garbled; legible fragments mention the lower side with a big hammer pattern and the body of the candle | 13 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Upper shadow / body | Not found in this text | ASSUMPTION: >= 2x body (mirror of hammer) | - |
| Lower shadow | Not found in this text | ASSUMPTION: little or none | - |

**Key quotes**

- "Inverted hammer pattern" [p. 13]
- "occur at end of downtrend," [p. 13]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
inv_hammer(t): downtrend(t-1) and upper[t] >= 2*body[t] and lower[t] <= 0.10*range[t] and body[t] > 0
if inv_hammer(t): BUY at open[t+1]   # ASSUMPTION; direction bullish inferred from downtrend location
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Only the first lines are legible: it occurs at the end of a downtrend; the remaining sentence is cut and mentions lower side and hammer. Shape (long upper shadow, body at the lower end) and bullish direction are NOT stated in this text. ASSUMPTION: inverse of the hammer, bullish reversal. Mark as low confidence.

### 2.24 Hanging Man (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle reversal, bearish | 14 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Forms at the end of uptrend | 14 |
| Setup conditions | Body located at the upside with a long lower shadow which should be double the size of the body; no or small upper shadow | 14 |
| Entry trigger & order type | Not found in this text; the text says it indicates market may fall after this. Stop Loss and Entry labels exist only on the illustration | 14 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Lower shadow / body | 2x (doubled) | none | 14 |
| Upper shadow | no or small | ASSUMPTION: <= 10% of range | 14 |

**Key quotes**

- "Hanging man pattern forms at" [p. 14]
- "body of candle is located at" [p. 14]
- "thiscandlehas no or small" [p. 14]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
hanging_man(t): uptrend(t-1) and lower[t] >= 2*body[t] and upper[t] <= 0.10*range[t] and body[t] > 0
if hanging_man(t): SIGNAL_BEARISH at t   # exit/avoid long
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- The illustration has labels Stop Loss and Entry (p. 14) but the text states no levels or rule. ASSUMPTION: ignore; entry/exit as in 2.0.
- The shape is identical to the hammer; only the preceding trend differs. A coder must pass the trend filter correctly.

### 2.25 Bearish Engulfing (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal, bearish | 14 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at the end of uptrend | 14 |
| Setup conditions | Two candles: first is green, second is a bearish red candle that engulfs the first (covering the green candle with the red candle) | 14 |
| Entry trigger & order type | Not found in this text; the text gives the pattern as a bearish-reversal indication only | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Engulf | Red candle covers green candle | ASSUMPTION: second body covers first body | 14 |

**Key quotes**

- "Bearish engulfing pattern is" [p. 14]
- "bearish red candle which" [p. 14]
- "covering green candle with" [p. 14]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
bear_engulf(t): uptrend(t-1) and bull[t-1] and bear[t]
                 and open[t] >= close[t-1] and close[t] <= open[t-1]
if bear_engulf(t): SIGNAL_BEARISH at t   # exit/avoid long
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Body versus full range engulfing not stated. ASSUMPTION: bodies.
- The text does not state that this is the exact mirror of the bullish engulfing, so it is specified separately although the rule is symmetric.

### 2.26 Evening Star (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle reversal, bearish | 15 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at the end of uptrend | 15 |
| Setup conditions | Three candles: first bullish, second a doji (neutral), third a red bearish candle; the second candle should be completely out of the real bodies of the first and third candle | 15 |
| Entry trigger & order type | Not found in this text; the red third candle is said to signal the start of a bearish trend | 15 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Doji | Second candle a doji | ASSUMPTION: body <= 10% of range | 15 |
| Doji location | Completely out of real bodies of first and third | ASSUMPTION: doji body entirely above the bodies of candles 1 and 3 (a gap up) | 15 |

**Key quotes**

- "The eveing star is multiple" [p. 15]
- "made up of three candle first" [p. 15]
- "completely out of real bodies" [p. 15]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
evening_star(t): uptrend(t-2) and bull[t-2] and doji[t-1] and bear[t]
   and min(open[t-1],close[t-1]) > max(open[t-2],close[t-2])
   and min(open[t-1],close[t-1]) > max(open[t],close[t])
if evening_star(t): SIGNAL_BEARISH at t
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- The stated rule is that the doji is completely out of the real bodies of candles 1 and 3, without saying above; in an uptrend above is implied. ASSUMPTION: above both.
- This strict gap rule may make the pattern rare on daily NSE data. Test also a relaxed version without the gap condition.

### 2.27 Three Black Crows (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle reversal, bearish | 15 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at the end of uptrend | 15 |
| Setup conditions | Three red candles without long shadows; all three open within the previous candle's body | 15 |
| Entry trigger & order type | Not found in this text; the text gives the pattern as a bearish-reversal indication only | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Shadow limit | Do not have long shadows | ASSUMPTION: each shadow <= 25% of range | 15 |

**Key quotes**

- "The three black crows is" [p. 15]
- "it consist three red candle" [p. 15]
- "all three candleopens within" [p. 15]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
three_crows(t): uptrend(t-3) and bear[t-2] and bear[t-1] and bear[t]
   and open[t-1] within body[t-2] and open[t] within body[t-1]
   and shadows <= 25% of range for the 3 candles
if three_crows(t): SIGNAL_BEARISH at t
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Lower closes are not stated but implied. ASSUMPTION: require close[t] < close[t-1] < close[t-2].
- The text says all three candles open within the previous candle's body, which for the first candle has no previous candle in the pattern. ASSUMPTION: apply to candles 2 and 3 only.

### 2.28 Bearish Harami (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal, bearish | 16 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs after uptrend | 16 |
| Setup conditions | First candle is a big bullish candle; second is a small bearish candle within the range of the previous bullish candle | 16 |
| Entry trigger & order type | Not found in this text; the text says it shows the market may fall now | 16 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| First candle | Big bullish | ASSUMPTION: body >= 1.5x average body of last 10 bars | 16 |
| Second candle | Small, bearish, inside previous candle | ASSUMPTION: body inside body of candle t-1 | 16 |

**Key quotes**

- "Bearish harami is multiple" [p. 16]
- "candle is bullish big candle" [p. 16]
- "& second candle is small" [p. 16]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
bear_harami(t): uptrend(t-1) and bull[t-1] and body[t-1] >= 1.5*avg_body(10)
   and bear[t] and open[t] <= close[t-1] and close[t] >= open[t-1]
if bear_harami(t): SIGNAL_BEARISH at t
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- Same body versus range ambiguity as the bullish harami; the bearish harami text says multiple candlestick but describes two candles.

### 2.29 Shooting Star (bearish reversal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle reversal, bearish | 16 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs at the end of uptrend | 16 |
| Setup conditions | Body located at the lower side with a long upper shadow; formed when opening and closing prices are near to each other; inverse of the hanging man | 16 |
| Entry trigger & order type | Not found in this text; the text gives the pattern as a bearish reversal signal only | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend filter | Pattern occurs at the stated trend | ASSUMPTION: per 2.0 | - |
| Upper shadow / body | Long upper shadow | ASSUMPTION: >= 2x body (mirror of hanging man 2x) | 16 |
| Open near close | Opening and closing near each other | ASSUMPTION: body <= 30% of range | 16 |
| Lower shadow | Not found in this text | ASSUMPTION: <= 10% of range | - |

**Key quotes**

- "Shooting star occurs at the" [p. 16]
- "located at lower side and" [p. 16]
- "it is inverse of the hanging" [p. 16]

**Pseudocode** (uses the 2.0 definitions; OHLC fields only)

```
shooting_star(t): uptrend(t-1) and upper[t] >= 2*body[t] and lower[t] <= 0.10*range[t]
if shooting_star(t): SIGNAL_BEARISH at t
```

**Ambiguities & assumptions**

- Not found in this text: timeframe, universe, stop-loss, profit target, trailing/time exits, sizing, pyramiding, portfolio limits, author's test results. ASSUMPTION: defaults in 2.0 for back-testing only.
- The text says long upper shadow but gives no ratio; the 2x ratio is borrowed from the hanging man by the text's own inverse of the hanging man statement. ASSUMPTION: 2x.

## 3. Risk & money-management rules

Not found in this text. The notes contain no risk-per-trade, stop-loss, position-size, drawdown or exposure rules. The words Stop Loss and Entry appear once, as image labels on the hanging-man page (p. 14), with no levels. ASSUMPTION: apply the generic back-test defaults in 2.0 and measure results per pattern before any sizing rule is added.

## 4. Non-codable guidance

- Ascending triangle (p. 9): right-angled triangle with a horizontal resistance and rising lows, said to show buying pressure increasing; the text then says it can break from any direction, so there is no directional trigger. A coder may test a breakout-either-side variant under an ASSUMPTION, but it is not the author's rule.
- Descending triangle (p. 9): formed in the downtrend as a continuation, with horizontal support and lower highs, selling pressure increasing; again it can break from any direction. Same treatment.
- Doji (p. 17): sideways/indecision candle with open and close almost equal and a very small body with long shadows; no trade rule. It is used only as a component of the morning and evening stars (see 2.0 for the numeric proxy).
- Candlestick basics (p. 10): green candle = strength/buying, red candle = weakness/selling; the candle shows the current mood of the market. Interpretation only.
- Retest labels on the illustrations for head and shoulders, inverse head and shoulders, wedges, flags and symmetrical triangles (p. 3-4, 6-7) imply a retest entry, but no text rule exists.
- The text uses emphatic words (extremely bearish, extremely bullish) with no measure of reliability; treat as rhetoric, not a probability.

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily OHLC (open, high, low, close) only. Volume is mentioned for the rising wedge (decreasing volume, p. 4) as an optional filter. No delivery %, index or fundamentals required.
- **Testability with our data:** All patterns are testable on the 2005-2026 daily panel (about 3,700 stocks, split/bonus adjusted, delisted included), as pure price-pattern event studies. Nothing needs fundamentals or index history. Because the text has no exits, back-tests need an assumed exit (2.0), and results measure the pattern, not the author's system.
- **Market-structure differences:**
  - The cash market has no overnight shorting: bearish patterns (double/triple top, head and shoulders, rising wedge, bearish rectangle/flag/triangle, inverted cup, hanging man, bearish engulfing, evening star, three black crows, bearish harami, shooting star) become exit-or-avoid signals for longs. ASSUMPTION: no shorts; optionally test shorting via futures only on F&O stocks.
  - Costs: STT, brokerage and about 0.1% slippage per side. Candle patterns fire very often, so net edge after costs is likely thin. ASSUMPTION: charge 0.1% slippage plus statutory costs on each leg.
  - Circuit limits and illiquid small caps make gaps and wicks unreliable. ASSUMPTION: require average traded value over 20 days above a liquidity floor (for example Rs 1 crore) and skip bars at circuit limits.
  - Pattern geometry is not scale-free for low-priced stocks (tick size). ASSUMPTION: use percentage tolerances, and skip stocks priced under Rs 20.
  - Look-ahead: pivot highs/lows are confirmed N bars late; use only data available at the signal bar.

## 6. Verdict

- **Codeability:** Partly. Geometry and confirmation sentences are codable (chart patterns have a stated breakout trigger), but there are no thresholds, trend definitions, stops, targets or sizing, and the candlestick pages have no trigger at all.
- **Priority for backtesting:** Low. No exits, risk rules or evidence are given, so it is only a pattern-signal battery to test the hit rate and forward returns of each pattern with assumed defaults; it is cheap to run once a pivot and candle library exists.
- **Top 3 things a coder is most likely to get wrong:**
  1. Look-ahead bias from pivots (using a swing high before it is confirmed N bars later) and from entering on the breakout bar's close or the same bar's low rather than the next open.
  2. Treating bearish patterns as shorts on NSE cash and treating the candlestick patterns as trades by themselves when the text gives no entry trigger; also omitting the trend filter (hammer and hanging man have identical shapes and differ only in the preceding trend).
  3. Hardcoding tolerances the text does not give (equal tops, 2x shadows apply only to hammer and hanging man; 50% for piercing) and misreading the evening star's doji-outside-the-bodies rule or the garbled inverted hammer.
