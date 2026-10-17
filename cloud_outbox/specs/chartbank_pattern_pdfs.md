# ChartBank pattern PDFs (Triangle, Flag, Cup and Handle, RSI divergence) — Chart Bank ("Mv")

- **Source file:** Google Drive folder of five short PDFs by Chart Bank. Four were read and concatenated:
  - "Triangle chart pattern by Chart Bank  Mv.pdf" = [[PAGE 1]]-[[PAGE 7]] (pp. 1-7)
  - "Flag pattern by Chartbank.pdf" = pp. 8-12
  - "Cup and Handle pattern by ChartBank.pdf" = pp. 13-16
  - "RSI divergence by Chartbank.pdf" = pp. 17-27
  - "Intraday strategy by Chartbank (1).pdf" = password-protected, NOT opened (skipped_drm); its contents are unknown and nothing in this spec is derived from it.
- **Text file used:** text/chartbank_pattern_pdfs.txt  (page basis: pdf_pages from each PDF's text layer, numbered continuously)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (continuous PDF page index across the four concatenated PDFs, not any printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage.
  - Verified with `python ../work/bin/verify_citations.py specs/chartbank_pattern_pdfs.md text/chartbank_pattern_pdfs.txt`.
- **Coverage:** Read text lines 1-456 in full (one read), last marker reached `[[PAGE 27]]` (all 27 markers). Four of five PDFs processed; the fifth ("Intraday strategy by Chartbank (1).pdf") is password-protected and was skipped_drm, not opened, not guessed. The charts are images and are not in the text: pp. 4, 5, 6, 10, 11, 12, 14, 15, 16 are essentially chart pages with a one-or-two-line caption; pp. 3, 21, 22, 23, 25 and 26 are chart pages with short captions; the numeric trade levels on those charts (entries, stops, target lines) are therefore not available. No page was garbled. *Coordinator check: four PDFs were downloaded and concatenated in the order Triangle (pp.1-7), Flag (pp.8-12), Cup and Handle (pp.13-16), RSI divergence (pp.17-27). 'Intraday strategy by Chartbank (1).pdf' (1ePFFRkib8bZAG0dMrP6-2nh4P4tArfGC, 1.62 MB) requires a user password (PyMuPDF needs_pass=1), so it was recorded as skipped_drm and deleted locally, with no attempt to open it by any other route. The coordinator re-ran verify_citations (33/33 ok) and an exact-page strict check (0 off-by-one), and confirmed all eight field tables have exactly the 12 template rows. 9 unquoted citations were spot-checked by grep and page read: prior trend 'few months' p.7, pennant and bottom-trend-line exit p.8-9, cup-and-handle 1/3rd and volume 'most important' p.13, RSI 14 and 70/30 p.17, 30-minute/hourly timeframes and the aggressive/safe entries p.20, no shorting p.26; all matched.*

## 1. The method in brief

Chart Bank ("Mv", signs off as "Chart bank – Mv" [p. 7]; the real name is not stated) teaches classical chart-pattern trading for NSE/Indian instruments (Bata, Tata Steel, Ashok Leyland, Deepak Fertilisers, Sundaram Brake Linings, Vedanta, Cipla, Nifty, Bank Nifty, Natural Gas are used as examples). The tutorials are informal and visual: continuation patterns (triangles, flag/pennant, cup and handle) are traded long on a closing-basis breakout confirmed by a volume surge, with a target equal to a measured-move height, and a reversal pattern (RSI divergence) is combined with trend-line breaks. Timeframes are daily/weekly/monthly for positional trades [p. 9] and 30-min/hourly for index intraday divergence trades [p. 20].

No statistical evidence is offered. Support is a handful of hand-picked winning chart examples (e.g. "achieved all the target" [p. 14]) with no losing trades, no sample counts, and no position-sizing or portfolio rules. The author states she/he does not short [p. 26]. Almost all numeric parameters (stop distance, volume multiples, minimum pattern length, trend-line fitting) are unstated and are marked ASSUMPTION below.

## 2. Strategies

Two reading notes. (1) The bear-side counterparts (descending triangle, bear flag, bearish divergence) are described only in a sentence or by mirror, with no trade example. (2) Hidden RSI divergence is NOT found in this text; only regular divergence is described (price higher high / RSI lower high, price lower low / RSI higher low) [p. 18].

### 2.1 Ascending triangle (long breakout)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation breakout (bullish). Triangles follow the original trend. | 1 |
| Timeframe & holding period | Any timeframe ("found in all the time frames"); the breakout must be a close on the timeframe the pattern is drawn on. Holding period not stated; positional daily/weekly/monthly is the general guidance for patterns. | 1, 7, 9 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Needs a stronger established prior trend (uptrend), at least a few months old. | 7 |
| Setup conditions | Horizontal resistance line plus rising support trend line; price must touch the trend line at least two times; at least 2 points per trend line; formed inside an ongoing uptrend; volume thin/reduced during consolidation. | 1, 7 |
| Entry trigger & order type | Price closes above the horizontal resistance (breakout point) on a closing basis for the chart timeframe; breakout should come on big volume. Order type not stated. A retest of the breakout point after breakout is described as normal (usable as a later entry/add is not stated). | 1, 7 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Target = height of the widest point of the triangle projected from the breakout point. Charts mention Tgt 1, 2, 5 (multiple targets) but levels are in images only. | 7, 3, 4 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Min touches on rising support line | 2 | 2 points to draw a line | 1, 7 |
| Prior trend age | at least a few months | not quantified | 7 |
| Breakout confirmation | close above horizontal resistance | closing basis in pattern timeframe | 7 |
| Volume in consolidation | thin/reduced | not quantified | 7 |
| Volume at breakout | big volume | not quantified | 7 |
| Target | widest height of triangle added to breakout point | multiple targets shown on charts | 7 |
| Stop-loss | not stated | - | - |

**Key quotes**
- "Price must touch the trend line by at least two times to form a valid pattern." [p. 1]
- "Upside breakout happens when the price breaks out the horizontal resistance line." [p. 1]
- "Price must close above the breakout point on a closing basis as per the time frame we are drawing the pattern" [p. 7]
- "The height of the widest point is the target from the breakout point" [p. 7]

**Pseudocode**
```
for each stock, timeframe TF in {D, W}:
  R = horizontal resistance (>=2 touches of highs within tol_R)
  S = rising support line (>=2 swing lows, slope > 0)
  require prior uptrend of >= trend_months          # ASSUMPTION trend_months = 3
  require avg_volume(consolidation) < avg_volume(prior trend)   # ASSUMPTION
  H = R - S_at_pattern_start                         # widest height
  entry: first TF bar with close > R and volume >= vol_mult * avg_vol(20)   # ASSUMPTION vol_mult=1.5
  buy at next bar open
  stop: ASSUMPTION low of breakout bar (borrowed from flag rule p.9); not stated for triangles
  target T1 = R + H
  exit at T1 or at stop
```

**Ambiguities & assumptions**
- Stop-loss is not found in this text for triangles. ASSUMPTION: low of the breakout candle (the flag rule on p. 9, applied by analogy; flagged as not the author's triangle rule).
- "Few months" prior trend and "thin volume" are unquantified. ASSUMPTION: prior trend >= 3 months, defined as close above a rising 50-day MA at pattern start; volume in consolidation below its 50-day average, breakout volume >= 1.5x 20-day average.
- Tolerance for "horizontal" resistance and for touches is not given. ASSUMPTION: highs within 1% of each other.
- Target multiplicity ("Tgt 1..5" on p. 3-6) is not defined in the text. ASSUMPTION: only the one stated target (widest height) is coded; others not found in this text.
- Retest of the breakout point is described as normal, not as an entry rule. ASSUMPTION: not used for entry.

### 2.2 Descending triangle (bearish breakdown)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation breakdown (bearish) | 1, 2 |
| Timeframe & holding period | Any timeframe; closing basis in pattern timeframe | 1, 7 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Prior trend should be established (a few months), here a downtrend. | 7 |
| Setup conditions | Horizontal support line followed by a falling resistance line; at least 2 points per trend line; thin volume during consolidation. | 2, 7 |
| Entry trigger & order type | Downside breakout when price breaks below the support line; close below the breakout point on closing basis. Order type not stated. | 2, 7 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Height of the widest point of the triangle from the breakout point (stated generally for triangles). | 7 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Touches | at least 2 points per line | - | 7 |
| Breakout confirmation | close below horizontal support | - | 7 |
| Target | widest height from breakout point | - | 7 |
| Stop | not stated | - | - |

**Key quotes**
- "Downside breakout happens when the price breaks below the support line." [p. 2]
- "This pattern is formed with horizontal support line followed by a falling resistance line." [p. 2]

**Pseudocode**
```
Mirror of 2.1: support S horizontal, falling resistance R.
Signal: close < S on TF. Target = S - widest_height.
NSE cash: no overnight short -> use as an exit/avoid-long signal for held longs,
or intraday short only (ASSUMPTION).
```

**Ambiguities & assumptions**
- No descending-triangle trade example, stop or sizing is given; the author states no shorting habit [p. 26].
- ASSUMPTION: on NSE cash, use as an exit/avoid signal for long positions; a short test only on futures or intraday, tested separately.

### 2.3 Symmetrical triangle (either-way breakout)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation breakout, either direction | 2 |
| Timeframe & holding period | Any timeframe; closing basis | 1, 7 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Direction bias from the previous trend: if previous trend up, upside breakout much more likely; if formed in downtrend, downside more likely. Prior trend at least a few months old. | 2, 7 |
| Setup conditions | Rising support line and falling resistance line converging; at least 2 points per line; volume dries up during consolidation. | 2, 3, 7 |
| Entry trigger & order type | Wait for a confirmed breakout: a close above or below the breakout point in the respective timeframe. Big volume on breakout. Order type not stated. | 2, 3, 7 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Target from widest point of triangle added to the breakout point; first target hit then retest of breakout point shown in examples. | 7, 3 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Breakout confirmation | close beyond breakout point | closing basis | 2, 7 |
| Volume at breakout | big volume | examples show volume dried up in consolidation | 3 |
| Target | widest height from breakout point | - | 7 |
| Stop | not stated | - | - |

**Key quotes**
- "Confirmed breakout happens when you get a price close above or below the breakout point in respective time frame." [p. 2]
- "if the previous trend is up then the chances of an upside breakout is much higher." [p. 2]
- "volumes are dried up during the consolidation period." [p. 3]
- "Normally after breakout, the price tends to retest the breakout point and starts its journey again" [p. 7]

**Pseudocode**
```
detect converging lines (>=2 touches each side), prior trend sign = sign(close - close[-N]) # ASSUMPTION N=60
if prior trend up: wait for close > upper line breakout point -> long
(downside breakout in uptrend: no long; treat as exit signal for longs)
target = breakout + widest_height
```

**Ambiguities & assumptions**
- It is not stated whether to trade against the prior trend if breakout goes that way; the text says to wait for the confirmed close. ASSUMPTION: long only on upside breakout regardless of prior trend, but prior-uptrend filter on.
- The "breakout point" is not defined exactly (trend line value on breakout bar versus apex region). ASSUMPTION: value of the upper trend line extended to the breakout bar.
- Stop not found in this text; same ASSUMPTION as 2.1.

### 2.4 Bull flag (and bear flag by mirror)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation breakout | 8 |
| Timeframe & holding period | Positional: daily / weekly / monthly. Longer timeframe gives a stronger breakout. Close must be above the trend line on that timeframe's closing basis. Examples: Bata weekly, Tata Steel daily. | 9, 10, 11 |
| Universe / eligibility filters | Stocks with strong uptrends. | 8 |
| Market / regime filter | Strong uptrend / steep vertical rise before the flag (the pole). | 8 |
| Setup conditions | Pole = steep rise; flag = sideways or slightly down consolidation of about one or two weeks; two parallel trend lines forming a small channel; slope generally opposite to the pole (down-sloping after a rise). | 8 |
| Entry trigger & order type | Buy when price breaks through the flag's upper trend line on a closing basis, with heavier volume (sharp volume increase). Order type not stated. | 8, 9 |
| Initial stop-loss | Breakout candle low is kept as immediate support; the bottom trend line of the flag is the final support. | 9 |
| Exits: profit-taking | Target = height of the pole added from the breakout point. | 9 |
| Exits: trailing / time / signal | Close below the breakout point shows weakness but do not exit in panic; exit when price closes below the bottom trend line of the flag. | 9 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Consolidation length | one or two weeks | not otherwise stated | 8 |
| Flag slope | opposite to pole direction | flat also possible (not perfectly flat in general) | 8 |
| Breakout confirmation | daily/weekly/monthly close above upper trend line | - | 9 |
| Volume on breakout | sharp increase / heavier | not quantified | 8 |
| Target | pole height from breakout point | - | 9 |
| Immediate stop reference | breakout candle low | - | 9 |
| Final stop / exit | close below flag's bottom trend line | - | 9 |
| Pole size threshold | not stated | - | - |

**Key quotes**
- "In general, the slope of the flag should move in the opposite direction of the initial sharp price movement" [p. 8]
- "The target is set based on the height of the Pole." [p. 9]
- "Normally I keep the respective breakout candle low as immediate support." [p. 9]
- "You can exit once the price closes below the bottom trend line of the flag." [p. 9]
- "This breakthrough should be on heavier volume to improve the signal of the chart pattern." [p. 8]

**Pseudocode**
```
find pole: rise of >= pole_pct over <= pole_bars   # ASSUMPTION pole_pct=20%, pole_bars=15 (unstated)
flag: 5-10 bars, two roughly parallel lines, slope <= 0
entry: close > upper flag line AND volume >= vol_mult*avg_vol(20)   # ASSUMPTION 1.5x
stop_initial = low(breakout bar)                                    # p.9 "immediate support"
exit_signal  = close < lower flag line (final)                      # p.9
target = breakout_price + pole_height
```

**Ambiguities & assumptions**
- Whether the stop is the breakout candle low (immediate support) or the bottom trend line (final support) is blurred: the author says both and says not to exit in panic when the close is below the breakout point [p. 9]. ASSUMPTION: hard stop = flag bottom trend line close (the stated exit), with a tighter variant using breakout candle low tested separately.
- Pole size, minimum slope and exact flag length are unstated. ASSUMPTIONs as above.
- Bear flag: the text says only that the buy or sell signal forms on break of support/resistance with the trend continuing in the prior direction [p. 8]; no separate bear-flag rules are given. ASSUMPTION: mirror, tested only as a long-exit signal on NSE cash.

### 2.5 Pennant (long, flag variant)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation breakout | 8 |
| Timeframe & holding period | Same as the flag: daily / weekly / monthly, closing basis. | 9 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Strong uptrend with a pole. | 8 |
| Setup conditions | Looks like a symmetrical triangle, support and resistance lines converge; does not need the multiple-test rule of triangles; direction less important than for flag; generally flat. Consolidation about one or two weeks after the pole. | 8, 9 |
| Entry trigger & order type | Price closes above the upper trend line on a closing basis; sharp volume increase. Order type not stated. | 8, 9 |
| Initial stop-loss | Breakout candle low as immediate support; bottom trend line is the final support. | 9 |
| Exits: profit-taking | Height of the pole from breakout point. | 9 |
| Exits: trailing / time / signal | Exit on a close below the bottom trend line. | 9 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Min touches per line | not required | triangles need them | 9 |
| Others | identical to 2.4 | - | 8, 9 |

**Key quotes**
- "The pennant pattern does not need to follow the same rules found in triangles" [p. 9]
- "the flag and pennant patterns are two continuation patterns that closely resemble each other" [p. 8]

**Pseudocode**: as 2.4 with converging lines instead of parallel (upper line slope < 0, lower line slope > 0, ASSUMPTION).

**Ambiguities & assumptions**
- The only difference from the flag is shape; the author treats the terms as interchangeable [p. 8]. ASSUMPTION: test jointly with 2.4 and as a separate shape flag in the backtest.

### 2.6 Cup and handle (long breakout)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Continuation breakout (bullish) | 13 |
| Timeframe & holding period | Not stated explicitly for this pattern. Cup 1 to 6 months, handle 1 to 4 weeks given as example. | 13 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Continuation of a bullish trend. | 13 |
| Setup conditions | Cup: U-shaped / rounding bottom, avoid V-shaped cups; roughly equal highs on both sides, slight slope acceptable; handle: small U about 1/3rd the height of the cup, must not go below the 1/3rd height, forms in shorter time than the cup; handle volume higher than cup volume. | 13 |
| Entry trigger & order type | Draw a straight trend line across the top connecting cup and handle; enter when the price of the handle part breaks above the trend line, ideally on big volume. Order type not stated. | 13 |
| Initial stop-loss | After breakout the trend line point is immediate support; the candle low is 2nd support; the low of the handle is the final support. | 13 |
| Exits: profit-taking | Target = breakout point + height of the cup measured from the bottom (example 100 + 20 = 120). | 13 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Handle depth | not below 1/3rd height (about 1/3rd of cup height) | - | 13 |
| Cup duration | 1 to 6 months (example) | - | 13 |
| Handle duration | 1 to 4 weeks (example), always shorter than cup | - | 13 |
| Volume | handle volume > cup volume; big volume on breakout | not quantified | 13 |
| Target | cup height from bottom + breakout point | - | 13 |
| Final stop | handle low | candle low (2nd), trend line (immediate) | 13 |

**Key quotes**
- "Avoid V shaped Cups" [p. 13]
- "The handle part should not go below the 1/3rd height and the width of the handle to be smaller than the cup size." [p. 13]
- "So if the height of the cup is say 20 points and the breakout point is 100 then the technical target is 100+20=120." [p. 13]
- "the low price of the handle part is your final support." [p. 13]
- "a perfect cup and handle pattern will have the increased volumes in handle part than the volumes in Cup part." [p. 13]

**Pseudocode**
```
cup: rounding base of 20-130 bars (1-6 months), left_high ~ right_high (within 5%? ASSUMPTION), reject V-shape
     (ASSUMPTION: reject as V-shape if the cup low is more than 10 bars from the cup midpoint, or fewer than 20% of cup bars close in the lowest third of the cup depth... simplified: require a rounded base, tested by a parabola/quadratic fit)
handle: 5-20 bars after right rim, handle_low >= rim - cup_depth/3, handle_bars < cup_bars
require mean(volume in handle) > mean(volume in cup)
TL = line through cup left high and handle high
entry: close > TL (handle breakout) with volume >= vol_mult*avg_vol(20)
stop: handle low (final); tighter variant breakout-candle low
target = breakout + (rim_high - cup_low)
```

**Ambiguities & assumptions**
- Reading of "handle ... 1/3rd height of CUP" and "should not go below the 1/3rd height" is ambiguous: handle height equals about a third of the cup, or the handle retraces no more than a third of the cup depth. ASSUMPTION: handle pullback depth <= 1/3 of cup depth from the rim.
- Which low is the stop is a three-level ladder (trend line, candle low, handle low) without a rule for choosing. ASSUMPTION: initial stop = handle low; exit on close below it.
- Volume claim (handle volume > cup volume) is stated as a quality filter on p. 13 but is also called the most important thing; no multiple stated. ASSUMPTION: handle mean volume > cup mean volume.
- Measuring "height of the cup from bottom" is relative to the rim/breakout level. ASSUMPTION: rim_high - cup_low.
- No numeric tilt tolerance for the rims. ASSUMPTION: rim highs within 10% of cup depth of each other.

### 2.7 Regular bullish RSI divergence (long reversal)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal / mean-reversion with trend-line breakout confirmation | 17, 19, 20 |
| Timeframe & holding period | Index intraday: 30-min or hourly chart. Stock positional: hourly or daily timeframe and above; equities and commodities daily/weekly. Holding period not stated (the 11600 example is an intraday booking). | 20, 24 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Works better when price is in a clear downtrend (for bullish); avoid looking for divergence in sideways markets. | 18 |
| Setup conditions | Price makes a lower low and RSI makes a higher low (needs minimum two touch points). RSI example uses a period of 14; 70/30 are overbought/oversold reference levels, not triggers. Combine with support/resistance trend lines, breakouts or reversal candles (e.g. bullish hammer). | 17, 18, 19, 20, 22 |
| Entry trigger & order type | Aggressive: go long immediately after finding divergence with minimum two touch points. Safe: wait for trend-line breakout confirmation (price breaks out of the falling resistance/wedge/triangle). Order type not stated. | 20, 22, 24 |
| Initial stop-loss | Support few points below the recent lows (example: divergence near 11600, support 11540). Earlier entry gives a smaller stop. | 20 |
| Exits: profit-taking | Next nearest resistance zone (found via trend lines / horizontal lines). Example: profit booked at 11685 for 75 points; price then ran to 11777. | 21, 23, 25 |
| Exits: trailing / time / signal | Not found in this text. Price may correct from the resistance zone and retest support. | 25 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RSI period | 14 (given as the example "if your RSI is set to 14") | not otherwise stated | 17 |
| Overbought / oversold | 70 / 30 | described as indicative only, not entry/exit triggers | 17 |
| Min touch points (divergence) | 2 | - | 20 |
| Intraday index timeframe | 30 min or hourly | - | 20 |
| Positional stock timeframe | hourly/daily and above | equities/commodities daily/weekly | 20, 24 |
| Stop | few points below recent low (support) | - | 20 |
| Target | nearest resistance zone | - | 23, 25 |
| Swing/pivot definition | not stated | - | - |

**Key quotes**
- "During Bullish divergence, price makes a lower low and the indicator makes higher low." [p. 18]
- "Divergence works better when the price is in clear uptrend or downtrend." [p. 18]
- "Aggressive players may go longs immediately after finding divergence with minimum two touch points." [p. 20]
- "Safe players can wait for breakout confirmation" [p. 20]
- "But the earlier you enter, your SL will be small." [p. 20]
- "Target can be next nearest resistance zone." [p. 23]
- "using RSI indicator alone is not wise" [p. 19]

**Pseudocode**
```
RSI = Wilder RSI(close, 14)                      # period 14 is the author's example (p.17); Wilder smoothing = ASSUMPTION
pivots: swing lows with k bars each side          # ASSUMPTION k=5 (unstated)
bullish_div at pivot low L2 vs previous pivot low L1 (distance 10-60 bars ASSUMPTION):
    low[L2] < low[L1] AND RSI[L2] > RSI[L1]
require downtrend context (close < SMA50)         # ASSUMPTION (author: clear downtrend)
Variant A (aggressive): buy at open after L2 confirmed (k bars later)
Variant B (safe): buy on close above falling price trend line / recent swing high after L2
stop = low[L2] - buffer                           # ASSUMPTION buffer 0.5 ATR(14); author: a few points below recent lows
target = nearest horizontal resistance (previous swing high) above entry
```

**Ambiguities & assumptions**
- Divergence swing detection, lookback and "two touch points" are discretionary. ASSUMPTION: pivot k=5, 10-60 bars between pivots.
- RSI period 14 is quoted only as an example of RSI basics [p. 17]; the author never says which period is used on the trade charts. ASSUMPTION: 14.
- Stop is a hand-drawn support; ASSUMPTION: below L2 low by 0.5 ATR.
- Target is a hand-drawn resistance. ASSUMPTION: the nearest prior swing high above the entry price within the last 120 bars.
- Hidden divergence (price higher low / RSI lower low, etc.) is not found in this text.
- Exits beyond target and stop (trailing, time) not found in this text.
- Intraday trades need 30-min/hourly data which we do not have (daily only); only the daily/weekly stock variant is testable.

### 2.8 Regular bearish RSI divergence (exit / avoid signal; long-only context)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal warning | 18 |
| Timeframe & holding period | Same as 2.7: 30-min/hourly for index intraday; hourly/daily and above for stocks. | 20 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Occurs in a clear uptrend; avoid in sideways ranges. | 18 |
| Setup conditions | Price makes a higher high and RSI makes a lower high. RSI can stay overbought while price makes new highs, so RSI alone is not enough. | 18, 19 |
| Entry trigger & order type | The author does not short and gives no bearish trade examples. Confirmation of reversal: price closes below the price trend line as well as the RSI trend line. | 19, 26 |
| Initial stop-loss | Not found in this text (for shorts); for longs: keep a strict SL. | 18, 19 |
| Exits: profit-taking | Book profit on bearish divergence in an uptrend (as an alternative to a strict SL); skip to the next stock. | 18, 19 |
| Exits: trailing / time / signal | Trend over once price closes below the price trend line and RSI breaks as well. | 19 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RSI period / levels | 14 as example; 70/30 indicative | - | 17 |
| Confirmation | close below price trend line and RSI trend line | - | 19 |
| Short stop/target | not stated | negative divergence is just opposite to positive divergence | 26 |

**Key quotes**
- "In bearish divergence, price makes a higher high and indicator makes lower high." [p. 18]
- "Once price closes below the price trend line as well as RSI, the uptrend is over and it confirms the reversal in trend." [p. 19]
- "Negative divergence is just opposite to positive divergence." [p. 26]
- "Since I don’t have the habit of doing short trading" [p. 26]

**Pseudocode**
```
bearish_div: high[H2] > high[H1] AND RSI[H2] < RSI[H1], in uptrend (ASSUMPTION close > SMA50)
exit_long (or no new long) when additionally close < price trend line (swing-low line) AND RSI < its trend line
# NSE cash: use as exit for longs; short side only intraday/futures (ASSUMPTION, not the author's practice)
```

**Ambiguities & assumptions**
- No bearish stop, target, or example is given; treat as mirror of 2.7 (ASSUMPTION), tested as an exit overlay for long strategies.
- RSI trend-line construction is discretionary. ASSUMPTION: drop it; use RSI crossing below its previous swing low as the RSI break.

## 3. Risk & money-management rules

- Position sizing, risk per trade, maximum positions and drawdown rules: not found in this text.
- Keep a strict stop-loss or book profit on bearish divergence in an uptrend [p. 18]; be very cautious after a confirmed reversal and skip to the next stock or maintain a strict SL [p. 19].
- Earlier entries on divergence mean a smaller stop [p. 20]; safer entries wait for breakout confirmation, or paper trade until the pattern is mastered [p. 20].
- Do not exit in panic when price closes below the flag breakout point; exit on a close below the flag's bottom trend line [p. 9].

## 4. Non-codable guidance

- Volume is called the most important check for a technical breakout [p. 13]; the breakout always comes with big volume in the author's examples [p. 6].
- Early identification of a pattern comes with familiarity [p. 15]; practise on paper trades [p. 20]; keep practising to master it [p. 27].
- Patterns are drawn by eye (trend lines, "naked eyes" [p. 26]); RSI is combined with support/resistance trend lines and reversal candles rather than used alone [p. 19].
- RSI 70/30 readings do not mean enter or exit; they are alerts [p. 17].
- Examples are cherry-picked winners (all targets achieved); no losing trades or frequencies are shown [p. 6, 14, 15].
- The Intraday strategy PDF (password-protected) was not read; any intraday rules from it are unknown.

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily and weekly OHLCV (open, high, low, close, volume) for 2005-2026; derived: RSI(14), moving averages, ATR, swing pivots, fitted trend lines. Delivery % optional as a volume-quality filter (ASSUMPTION). Index data (Nifty) not needed by the rules, only optionally as a regime filter via NIFTYBEES.
- **Testability with our data:** Triangles, flags, pennants, cup and handle and daily/weekly RSI divergence on stocks are testable on 2005-2026 daily/weekly bars once patterns are defined algorithmically. Not testable: the intraday 30-min/hourly index divergence trades (no intraday data, and Nifty history only from 2024), commodities (Natural Gas) and the discretionary hand-drawn trend lines (need a codified proxy). No fundamentals are used by the method.
- **Market-structure differences:** Author trades Indian stocks, indices and commodities; the cash market has no overnight shorting, so descending triangle, bear flag and bearish divergence become exit or avoid signals for long holdings (ASSUMPTION). STT, brokerage and about 0.1% slippage apply, which matters most for tight stops on intraday trades. Circuit limits can cause gap breakouts that cannot be filled at the signal price (ASSUMPTION: enter at next open, skip if the stock is at upper circuit). Liquidity filter on small caps is not in the text (ASSUMPTION: median value traded floor).
- ASSUMPTION: apply pattern detection on adjusted prices; use a 20-day average volume for volume tests.

## 6. Verdict

- **Codeability:** Partly. Rule skeletons (close beyond breakout line, measured-move target, stop at a stated low) are clear, but pattern recognition and trend-line drawing are discretionary and most numeric thresholds are unstated.
- **Priority for backtesting:** Medium. Cheap to test on daily data and the rules are simple, but there is no evidence in the text, no stop for triangles, and the pattern definitions will largely determine the result; the cup-and-handle and flag measured-move rules are the best-specified.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the "breakout" as an intraday cross instead of a close on the pattern's own timeframe, and not requiring the volume surge and thin-volume consolidation that the author calls essential [p. 7, 13].
  2. Applying a stop to triangles as if the author gave one (none is stated), and mixing up the flag's three support levels (breakout candle low, breakout point, bottom trend line) [p. 9].
  3. Presenting RSI(14) with 70/30 as the author's trading rule: they are only the basics example and warned not to be triggers; the real signal is the divergence plus trend-line break [p. 17, 19].
