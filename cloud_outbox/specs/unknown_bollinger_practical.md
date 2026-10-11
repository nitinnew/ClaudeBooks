# Bollinger Bands Practical Application Skills — author not stated in the text

- **Source file:** Google Drive: Bollinger Bands Practical Application Skills.pdf
- **Text file used:** text/unknown_bollinger_practical.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - Verified with `python ../work/bin/verify_citations.py specs/unknown_bollinger_practical.md text/unknown_bollinger_practical.txt`.
- **Coverage:** Read lines 1-50 of the text file (the whole file, 9 pages), last `[[PAGE 9]]` reached. The source charts are images and are not in the text, so every chart illustration is unseen. Nothing was skimmed. This is a very short machine-translated note ("rail" = band, "K-line" = candlestick chart). It is not "Bollinger on Bollinger Bands". Reading done by a Sonnet sub-agent. The coordinator read the whole 50-line text itself, re-ran the verifier and an exact-page check, and confirmed every unquoted table citation against pp. 2-9.

## 1. The method in brief
The note describes the Bollinger (BOLL) indicator as three lines (upper, middle, lower "rails") and gives seven qualitative reading rules: the position of the price relative to the middle rail tells the trend [p. 1]. In a rising band-set, the middle rail is the buy zone [p. 2]. In a falling band-set, the middle rail is the sell zone [p. 3]. In a flat (oscillating) band-set, buy at the lower rail and sell at the upper rail [p. 4]. Price persistently below or above the middle rail signals a weak market or a strong uptrend [p. 5, 6]. Contracting bands mean wait [p. 7]. Expanding bands mean expected rise, but a break above the upper rail followed by a sell-off may start a downtrend [p. 8]. The summary frames the lower band as support and the upper band as pressure, and says to combine with news and other indicators [p. 9].

No band period, standard-deviation multiplier, timeframe, market, stop-loss, position sizing, exit rule or track record is given anywhere in the text. Every numeric definition below is an `ASSUMPTION:` and is not found in this text.

## 2. Strategies

### 2.1 Trend-up pullback buy at the middle rail
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (pullback to middle band in an uptrend) | 2 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text. Page 9 says to combine with the stock's fundamental news and other indicators | 9 |
| Market / regime filter | The three lines must be running up and the K-line chart must be above the middle rail | 2 |
| Setup conditions | Three rails running up; price above the middle rail | 2 |
| Entry trigger & order type | Buy when price is "in the position of the middle rail" (the best time to buy). Order type not stated | 2 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text. Page 9 says the pressure level (upper line) is the time to sell | 9 |
| Exits: trailing / time / signal | Not found in this text (the converse rule on page 3 implies exit/sell when the bands turn down and price is below the middle rail) | 3 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| BB period | Not found in this text | none | - |
| Std-dev multiplier | Not found in this text | none | - |
| "Running up" definition | Not found in this text | none | 2 |
| "At the middle rail" tolerance | Not found in this text | none | 2 |

**Key quotes**
- "When the three orbital lines running up, the K chart is in the middle of the rail above" [p. 2]
- "the position of the middle rail is the best time to" buy [p. 2]

**Pseudocode**
```
# ASSUMPTION params (not in text): N=20, K=2.0, slope_lookback=5, tol=0.01
mid = SMA(close,N); sd = STDEV(close,N); up = mid+K*sd; lo = mid-K*sd
rising = (up > up[slope_lookback]) and (mid > mid[slope_lookback]) and (lo > lo[slope_lookback])
touch  = (low <= mid*(1+tol)) and (close >= mid)
if rising and close > mid and touch:  BUY at next open
exit (ASSUMPTION): close < mid for 2 consecutive closes, or fire 2.2 condition
```

**Ambiguities & assumptions**
- Period and multiplier are not in this text. ASSUMPTION: 20 and 2.0 (not found in this text).
- "Running up" is undefined. ASSUMPTION: all three bands higher than 5 bars ago.
- "In the position of the middle rail" is undefined (touch, cross, close near?). ASSUMPTION: bar low within 1% of, or below, the middle band while close stays at or above it.
- No stop or profit target. ASSUMPTION: stop = close below middle band for 2 closes; profit exit = 2.3 upper-band sell. Mark both as not found in this text.

### 2.2 Trend-down sell at the middle rail
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following short / exit signal | 3 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Three rails running down and K-line below the middle rail | 3 |
| Setup conditions | Three rails running down; price below the middle rail | 3 |
| Entry trigger & order type | Sell at the position of the middle rail (the "perfect time to sell"). Order type not stated | 3 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| BB period / multiplier | Not found in this text | none | - |
| "Running down" definition | Not found in this text | none | 3 |

**Key quotes**
- "When the three orbital lines run down when the K chart is below the" [p. 3]
- "sell sell sell!" [p. 3]

**Pseudocode**
```
# Mirror of 2.1. NSE cash has no overnight shorting.
falling = all three bands lower than 5 bars ago (ASSUMPTION)
touch   = (high >= mid*(1-tol)) and (close <= mid)
if falling and close < mid and touch:
    if in_long_position: SELL (exit)      # ASSUMPTION: use as exit/avoid only
    else: ignore (or intraday short only, if the user opts in)
```

**Ambiguities & assumptions**
- The text does not say whether "sell" means exit a long or open a short. ASSUMPTION: exit longs and block new longs; no overnight short on NSE cash.
- Same period, multiplier and "running down" assumptions as 2.1 (not found in this text).

### 2.3 Range-bound band-touch mean reversion
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion (buy lower band, sell upper band) | 4, 9 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Oscillating market with the three rails parallel | 4 |
| Setup conditions | Three rail lines parallel (flat) | 4 |
| Entry trigger & order type | Buy at the lower rail position. Page 9: the lower line is the support level and "the time to buy the stock". Order type not stated | 4, 9 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Sell at the upper rail position (pressure level) | 4, 9 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| BB period / multiplier | Not found in this text | none | - |
| "Parallel" definition | Not found in this text | none | 4 |
| "At the lower/upper rail" tolerance | Not found in this text | none | 4 |

**Key quotes**
- "the three rail lines are" parallel [p. 4]
- "The lower line is the support level of the stock and the upper line is the pressure level." [p. 9]

**Pseudocode**
```
# ASSUMPTION: N=20, K=2, flat if |band slope over 10 bars| < 1% of price for all three bands
flat = max(abs(up/up[10]-1), abs(mid/mid[10]-1), abs(lo/lo[10]-1)) < 0.01
if flat and low <= lo:  BUY (next open, or at lo)
if in_long and high >= up: SELL
# ASSUMPTION stop: close < lo*(0.97) or flat becomes False and close < mid
```

**Ambiguities & assumptions**
- Page 9 states the support/pressure rule generally, without restricting it to flat bands; page 4 restricts it to oscillating markets. ASSUMPTION: apply only when flat (page 4 version), since the general version would conflict with 2.1/2.2.
- Stop-loss and sizing not found in this text; assumed above.
- "Touch" undefined. ASSUMPTION: intraday low at or below the lower band.

### 2.4 Band expansion ("open mouth") and failed upper-band break
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout/trend-continuation, with a reversal warning | 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Bands opening (diverging) | 8 |
| Setup conditions | Three rails open mouth | 8 |
| Entry trigger & order type | "Expected to rise" (implies a long bias). No explicit trigger or order type | 8 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | A break through the upper rail followed by a sell-off is "very likely" to start a reversal to a downtrend, so exit | 8 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| "Open mouth" definition | Not found in this text | none | 8 |
| "Sold off" definition | Not found in this text | none | 8 |

**Key quotes**
- "Three rail line open mouth, expected to rise." [p. 8]
- "break through the" upper rail line to be sold off [p. 8]

**Pseudocode**
```
# ASSUMPTION: N=20, K=2; width = (up-lo)/mid; expanding = width > width[1] > width[2] and width > 1.2*min(width,20)
if expanding and close > mid and up rising: LONG bias (enter next open)
if high > up and close < up (close back inside) -> exit long (reversal warning)
```

**Ambiguities & assumptions**
- The note does not say whether "expected to rise" applies when the bands open downward. ASSUMPTION: only when price is above the middle rail and the upper band is rising.
- Sell-off after upper-band break is undefined. ASSUMPTION: a bar whose high exceeds the upper band and whose close is back below it.
- Entry trigger, stop and size are not found in this text.

### 2.5 State observations and filters (not separately tradable)
These have no trade action stated and are used as filters or regime labels only.
- Price always below the middle rail means a weak market [p. 5]. Use: block new longs.
- Price always above the middle rail means a strong uptrend [p. 6]. Use: allow 2.1 / 2.4.
- Three rails shrinking means an oscillating market, so choose to wait and see the direction of the new trend [p. 7]. Use: stand aside, no entries until bands open (2.4) or are parallel (2.3).
- Page 9: the note is a reference only and must be combined with news and other indicators [p. 9].

**Key quotes**
- "it represents a weak market!" [p. 5]
- "it represents a strong uptrend!" [p. 6]

**Ambiguities & assumptions**
- "Always" below/above the middle rail is undefined. ASSUMPTION: last 10 closes all on one side (not found in this text).
- "Shrinkage" undefined. ASSUMPTION: band width (up-lo)/mid below its 20-bar 20th percentile or falling 3 bars in a row.

## 3. Risk & money-management rules
- None stated: no stop-loss, risk per trade, sizing or drawdown rule is found in this text.
- Page 9 advises not to rely on a single technical pattern and to combine with the stock's fundamental news and other technical indicators [p. 9]. Not codable as stated.

## 4. Non-codable guidance
- The indicators are "just a reference" and the user should not rely on a single technical pattern for buying and selling [p. 9].
- Following the support/pressure principle is said to take "your own thinking logic" to the next level [p. 9].
- The charts illustrating each rule are images and were not available in the text [p. 1-8].

## 5. Adapting to NSE (Indian equities)
- **Data required:** daily OHLC (close for bands; high/low for touches). Volume and delivery % optional.
- **Testability with our data:** all rules can be backtested on 2005-2026 daily prices once the band parameters are fixed by assumption. No fundamentals are needed (the "basic news" mentioned on page 9 cannot be tested). Nifty/NIFTYBEES is not required by the text.
- **Market-structure differences:**
  - No overnight shorting in the NSE cash market. ASSUMPTION: rules 2.2 (and the downtrend side of 2.3) are used only as exit / no-entry signals.
  - Circuit limits can block lower-band buys or middle-rail sells at a limit; assume the fill fails on a locked bar.
  - ASSUMPTION: costs of STT + brokerage and 0.1% slippage per side; 2.3 turns over fast, so costs matter.
  - ASSUMPTION: restrict to liquid stocks (e.g., minimum average traded value) since the text gives no universe.

## 6. Verdict
- **Codeability:** Partly. The decision logic is clear qualitatively, but there are no parameters, stops, sizing or exit rules, so all numbers are assumptions.
- **Priority for backtesting:** Low-Medium. It is a generic indicator note with no author, evidence or specifics; useful only as a baseline Bollinger rule set (2.1 and 2.3 are the testable core).
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the rules as fully specified. Period, multiplier, "running up", "parallel" and "shrinkage" are all invented thresholds and must be flagged as assumptions.
  2. Applying the lower-band-buy / upper-band-sell rule (page 4, 9) in all regimes. The text restricts it to oscillating markets; in trends it conflicts with rules 2.1/2.2/2.4.
  3. Implementing "sell" as a short on NSE cash and ignoring that no stop-loss or exit is given for the buys.
