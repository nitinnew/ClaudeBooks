# A Handbook of Technical Analysis — Elearnmarkets (publisher; individual author not stated)

- **Source file:** Google Drive "A Handbook of Technical Analysis.pdf" (45 pages; short Indian handbook, NOT David Lim's "The Handbook of Technical Analysis")
- **Text file used:** text/unknown_handbook_ta_short.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. The printed footers ("1 | P a g e") and table-of-contents numbers are offset and never used.
  - Before finishing, `verify_citations.py` was run on this file (result in the final report).
- **Coverage:** Read lines 1-1092 in full (all 45 pages; last `[[PAGE 45]]` reached; nothing skimmed). Chart/figure-only pages with no rule text: 1, 4, 6, 10, 15, 18, 21, 28, 37, 42, 44. All charts are images and are not in the text, so chart-based examples could not be inspected. The publisher is identified only on [p. 45] (Elearnmarkets.com); no individual author is named and no track record or test results are given anywhere. *Coordinator check: the coordinator re-ran verify_citations (44/44 ok) and an exact-page strict check (0 off-by-one), and confirmed all 19 field tables have exactly the 12 template rows. 11 unquoted citations were spot-checked by grep and page read: Elearnmarkets publisher p.45, delivery-% filter p.20, neckline rules p.22/24, hammer and gap rules p.29-30, 2-3 candle confirmation p.30/33/34, bullish engulfing close above previous day's high p.33, SMA lengths 5/8/13 and 100/200 p.38, RSI 70/30 p.39-40, ADX 20 or 25 p.41; all matched.*

## 1. The method in brief

This is an introductory primer, not a system. It covers chart types [p. 7], trends, trendlines, role reversal and channels [p. 11-17], volume and delivery % [p. 19-20], classical chart patterns [p. 22-27], eight candlestick patterns [p. 29-36] and four indicators (SMA, RSI, ADX; the chapter says "four" but covers three) [p. 38-41]. The author's stance is that technical analysis "is not a definitive science, rather a probabilistic discipline" [p. 5] and that traders "combine indicators and price patterns" rather than rely on a single signal [p. 43].

No timeframe, market, universe, position-sizing rule or backtest/track record is given. The edge claimed is only that patterns "work more number of times than they fail" [p. 5]. Rules are mostly qualitative; a handful carry numbers (2x shadow-to-body ratio, 2-3 candle confirmation window, RSI 70/30, ADX 20/25, SMA lengths). Where the book gives no entry/stop/target, the spec marks the gap as not found rather than filling it from outside knowledge.

## 2. Strategies

Common to all 2.x unless stated otherwise: timeframe is not specified. The book says the same concepts apply to every time frame and "Generally higher the time frame of chart, relatively higher is the probability" [p. 7]. Universe, regime filter, position sizing, pyramiding and portfolio limits are not found in this text.

### 2.1 Uptrend trendline pullback buy
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following (buy pullback to rising trendline) | 13 |
| Timeframe & holding period | Not stated; any timeframe (higher is said to be more reliable). Hold until stop or trendline break | 7, 13 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Market must be in an uptrend (higher highs and higher lows) | 11, 13 |
| Setup conditions | Rising trendline drawn through two pull-back lows; a third touch without a break validates it; more validations = more important | 13 |
| Entry trigger & order type | Buy "near the trend line" on a pull-back to it; order type and exact trigger not stated | 13 |
| Initial stop-loss | A stop-loss "below which" to cut the position; exact distance not stated | 13 |
| Exits: profit-taking | "sells higher"; no target rule | 13 |
| Exits: trailing / time / signal | Trendline break: price may reverse, continue with less force, or go sideways; no explicit exit rule | 13 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Points to draw trendline | 2 pull-back lows | third touch validates | 13 |
| Swing-low definition | Not stated | "lowest points of periodic pull-backs" | 13 |
| Touch tolerance (how near is "near") | Not stated | - | 13 |
| Stop distance below line | Not stated | - | 13 |

**Key quotes**
- "To be precise we need two lows" [p. 13]
- "the third move towards the trend-line is used to validate the trend line" [p. 13]
- "it is often easier to make money if one buys near the trend line and sells higher" [p. 13]
- "A trend is said to reverse when the sequence is broken." [p. 11]

**Pseudocode**
```
# uses daily OHLC
swing_lows = pivot lows (ASSUMPTION: low is lowest of N=5 bars each side)
L = line through last two swing_lows, slope > 0
valid = third swing low touches L (within tol) and no close < L between
if valid and low[t] <= L[t]*(1+tol) and close[t] > L[t]:   # ASSUMPTION tol=1%
    BUY next open
    stop = L[t] * (1 - 0.02)        # ASSUMPTION: 2% below line
exit: close < L[t]*(1-0.02) -> SELL next open (ASSUMPTION)
      stop hit -> SELL
target: none in book (ASSUMPTION: trail via line)
```

**Ambiguities & assumptions**
- Swing/pivot definition, touch tolerance and stop distance are not given. ASSUMPTION: pivot N=5 bars, tolerance 1%, stop 2% below line.
- "Validation" is by the third touch; whether to buy at the third touch or only after it is unclear. ASSUMPTION: buy at the third touch or later touches, not on the second.
- Profit target and trailing rule: not found in this book.

### 2.2 Downtrend trendline (short at pull-back; on NSE use as exit/avoid signal)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following (short) | 14 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Down-trend (lower lows and lower highs) | 11, 14 |
| Setup conditions | Falling line through two pull-back highs, extended downward; more validations = more important | 14 |
| Entry trigger & order type | Pull-backs towards the line are "low risk points for short selling" | 14 |
| Initial stop-loss | "stop loss little above the trend line" | 14 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Line break: trend may continue with less pace, reverse or go sideways | 14 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Points to draw line | 2 pull-back highs | - | 14 |
| Stop above line | "little above" (not quantified) | - | 14 |

**Key quotes**
- "a trendline is formed by joining pull-back highs" [p. 14]
- "Pull backs towards the trend-lines are low risk points for short selling" [p. 14]

**Pseudocode**
```
H = line through last two swing highs, slope < 0
if high[t] >= H[t]*(1-tol) and close[t] < H[t]: SHORT (not possible in NSE cash; use as "do not buy"/exit signal)
stop = H[t]*(1+0.02)   # ASSUMPTION
```

**Ambiguities & assumptions**
- Same unquantified parameters as 2.1. ASSUMPTION: mirror 2.1 values.
- No target, no trailing rule. Not found in this book.

### 2.3 Role reversal (broken support/resistance flips)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | other (support/resistance flip, trend-following) | 16 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Price breaks a support/resistance line "strong move through"; broken support becomes resistance and broken resistance becomes support | 16 |
| Entry trigger & order type | No entry rule given (implication only: use flipped level as support/resistance) | 16 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| "Strong move" through the line | Not quantified | - | 16 |

**Key quotes**
- "If the price rises above a resistance line, it will often become support." [p. 16]
- "it is important that the prices make a strong move through" [p. 16]

**Pseudocode**
```
# level R (prior resistance or trendline). Break = close > R*(1+b)   # ASSUMPTION b=2% as "strong move"
# after break, R is support: buy on pull-back to R if close stays > R   # ASSUMPTION: entry/stop not in book
```

**Ambiguities & assumptions**
- The book gives only the concept; entry, stop and "strong move" threshold are not found. ASSUMPTION: b=2% (or 1x ATR(14)) and stop 2% below R.

### 2.4 Channel boundary reversal trade
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion (range/channel) | 16 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Uptrend, downtrend or consolidation where price moves rhythmically in a parallel channel | 16 |
| Setup conditions | Channel drawn parallel to the trendline | 16 |
| Entry trigger & order type | Channel boundaries are "good points for reversal trades" | 16 |
| Initial stop-loss | "small stop losses" (not quantified) | 16 |
| Exits: profit-taking | Not found in this text (implied opposite boundary) | - |
| Exits: trailing / time / signal | "Once price is out of the channel, the trend or range of the stock is broken." | 17 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Stop size | "small" | - | 16 |
| Channel parallel-line construction | Not stated | - | 16 |

**Key quotes**
- "The channel boundaries are good points for reversal trades with small stop losses." [p. 16]
- "Once price is out of the channel, the trend or range of the stock is broken." [p. 17]

**Pseudocode**
```
lower = trendline through swing lows; upper = parallel line through the highest swing high between them  # ASSUMPTION
BUY when low touches lower*(1+tol) and close > lower; stop just below lower (ASSUMPTION 1.5%)
TARGET = upper (ASSUMPTION); EXIT if close outside channel (p. 17)
```

**Ambiguities & assumptions**
- Target and stop size not stated. ASSUMPTION: target opposite boundary, stop 1.5% beyond boundary.

### 2.5 Volume and delivery-% confirmation (filter)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | other (confirmation filter, not standalone) | 19 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Range-bound phases generally have low volume | 19 |
| Setup conditions | Judge volume relative to its average over a period, never in absolute terms | 19 |
| Entry trigger & order type | Up-move + high volume: may go greater distance; up-move + low volume: lack of conviction, likely to retrace | 19 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Down-move + high volume: may cover greater distance; down-move + low volume: may reverse | 19, 20 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Average-volume lookback | Not stated ("certain time periods") | - | 19 |
| "High" / "low" volume threshold | Not stated | - | 19 |
| Delivery % high threshold | Not stated | - | 20 |

**Key quotes**
- "traded volume in absolute term has no significance" [p. 19]
- "it is relative to average volume over" [p. 19]
- "a fall in price with high delivery % is known as" [p. 20]

**Pseudocode**
```
relvol = volume / SMA(volume, N)         # ASSUMPTION N=20
high_vol = relvol > 1.5 ; low_vol = relvol < 1.0   # ASSUMPTION thresholds
deliv_high = delivery_pct > its own SMA(delivery_pct, 20) * 1.2   # ASSUMPTION
use as AND-filter on other setups: breakouts need high_vol; price rise with deliv_high = positive conviction; price fall with deliv_high = negative
```

**Ambiguities & assumptions**
- No thresholds. ASSUMPTION values above. Delivery % is only available for recent years in our data.

### 2.6 Head and Shoulders / Inverse Head and Shoulders
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal pattern breakout | 22 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | H&S needs a prior uptrend; inverse H&S needs a "sustained down trend" | 22, 23 |
| Setup conditions | Three consecutive tops, middle (head) higher than the two shoulders; neckline joins the intermediate troughs; inverse is the mirror image | 22, 23 |
| Entry trigger & order type | On break below neckline take short trade (inverse: break above neckline, long); order type not stated | 22, 23 |
| Initial stop-loss | Above the top of the nearest shoulder (inverse: mirror, below the nearest shoulder) | 22, 23 |
| Exits: profit-taking | Target = distance from neckline to head, projected from the break point | 22 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Target | head-to-neckline distance projected from break | - | 22 |
| Stop | above the nearest shoulder top | - | 22 |
| Volume confirmation | high volume on down leg of right shoulder and on break = higher conviction | optional | 22 |
| Shoulder symmetry / min duration | Not stated | - | 22 |

**Key quotes**
- "usually a short trade is taken with a stop-loss above the top of the nearest shoulder" [p. 22]
- "The target is usually" [p. 22]
- "the rule of stop loss and target are similar" [p. 23]

**Pseudocode**
```
find pivots LS < H > RS with H > LS and H > RS (H highest); neckline N through troughs between them
if prior trend up and close < N(t): signal SHORT (bearish; on NSE cash = exit/avoid)
   stop = RS_high (the nearer shoulder); target = break_price - (H_high - N_at_head)
inverse: mirror, BUY on close > N; stop = lowest of nearer shoulder; target = break + (N_at_head - H_low)
optional filter: volume at break > SMA(volume,20)   # ASSUMPTION
```

**Ambiguities & assumptions**
- Break defined as close beyond neckline? Not stated. ASSUMPTION: close beyond neckline.
- "Nearest shoulder" for stop is ambiguous (right shoulder is the nearest in time). ASSUMPTION: right shoulder extreme.
- Pivot sensitivity, shoulder similarity and duration limits: not found in this book.

### 2.7 Triple Top / Triple Bottom neckline break
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal pattern breakout | 24 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Reversal of the prior trend | 24 |
| Setup conditions | Price tests a support/resistance level three times and cannot break through | 24 |
| Entry trigger & order type | Entry "at the break of a neckline" | 24 |
| Initial stop-loss | "small stop-loss" (not quantified) | 24 |
| Exits: profit-taking | Target = distance between peaks/troughs and the neckline | 24 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of tests | 3 | - | 24 |
| Target | peak-to-neckline height | - | 24 |
| Level-matching tolerance | Not stated | - | 24 |

**Key quotes**
- "A trade entry is" [p. 24]
- "the target is measured as the distance" [p. 24]

**Pseudocode**
```
level P tested 3 times (highs within tol=1%, ASSUMPTION); neckline N = lowest trough between peaks
if close < N: SHORT (NSE: exit/avoid); stop = N*(1+0.02) (ASSUMPTION); target = N - (P - N)
bottoms: mirror (BUY on close > neckline)
```

**Ambiguities & assumptions**
- Stop "small" is not quantified; neckline definition not given in text (chart). ASSUMPTION as above. Double top/bottom (p. 23) has no trade rule in the book and is in Section 4.

### 2.8 Hammer (bullish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (candlestick) | 29 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Occurs after a prolonged down-trend | 29 |
| Setup conditions | Small body, lower shadow at least 2x body, negligible upper shadow, close near open; ideally gap-down open; green body slightly more bullish | 29 |
| Entry trigger & order type | Buy when price moves above the hammer's high (within the next 2-3 days; gap-up open also counts); unconfirmed hammer "has no real significance" | 29 |
| Initial stop-loss | Below the low of the candle | 29 |
| Exits: profit-taking | None: "there are no target setup" for candlestick patterns | 29 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lower shadow / body | >= 2 | - | 29 |
| Confirmation window | next 1 day to "two three days" | - | 29 |
| Upper shadow | negligible (not quantified) | - | 29 |
| "Prolonged" downtrend | Not defined | - | 29 |

**Key quotes**
- "Ideally the lower shadow should be at least twice the length of the body." [p. 29]
- "A hammer like candle, without validation has no real significance." [p. 29]
- "a buy trade can be taken with a stop loss below the low of the candle" [p. 29]

**Pseudocode**
```
body=abs(C-O); lower=min(O,C)-L; upper=H-max(O,C)
hammer = downtrend and body>0 and lower>=2*body and upper<=0.1*body(ASSUMPTION) and C near O
if hammer at bar h: within bars h+1..h+3: if high > H[h] (or open gap above H[h]): BUY at H[h] stop-entry (ASSUMPTION)
stop = L[h]; no target
downtrend: ASSUMPTION close < SMA(50) and falling over 10 days
```

**Ambiguities & assumptions**
- Downtrend definition, "negligible", "near" open not defined. ASSUMPTION as above.
- Exit/target absent: ASSUMPTION a coder must add a rule (e.g. 2R or trailing); not from the book.

### 2.9 Shooting Star (bearish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (candlestick, short) | 30 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Sustained up-trend | 30 |
| Setup conditions | Gap-up open, price pushed up then sold; close near open; small body, upper shadow at least 2x body, small/negligible lower shadow; red body slightly more bearish | 30 |
| Entry trigger & order type | Short if price moves below the candle's low within next 2-3 candles | 30 |
| Initial stop-loss | Above the high of the candle | 30 |
| Exits: profit-taking | No target for candlestick patterns | 29 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Upper shadow / body | >= 2 | - | 30 |
| Confirmation window | next 2-3 candles | - | 30 |

**Key quotes**
- "The upper shadow of the candle should be at least twice the length of the body." [p. 30]
- "a short trade should be taken with stop loss above the high" [p. 30]

**Pseudocode**
```
star = uptrend and upper>=2*body and lower<=0.1*body (ASSUMPTION) and close near open
if low[t] < L[star] within 3 bars: SHORT at L[star]; stop = H[star]  (NSE cash: use as exit of longs / avoid)
```

**Ambiguities & assumptions**
- Gap-up open is "should", so may be optional. ASSUMPTION: not required. No short selling overnight on NSE; use as a long-exit signal.

### 2.10 Inverted Hammer (bullish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (candlestick) | 32 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | After a sustained down-trend | 32 |
| Setup conditions | Gap-down open; small body (red or green); upper wick at least 2x body; small/negligible lower shadow; green body more bullish; less bullish than the hammer | 32 |
| Entry trigger & order type | Buy once price moves above the candle's high | 32 |
| Initial stop-loss | Below the low of the candle | 32 |
| Exits: profit-taking | No target for candlestick patterns | 29 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Upper wick / body | >= 2 | - | 32 |
| Confirmation window | Not stated for this pattern | - | 32 |

**Key quotes**
- "the upper wick should be at least twice the body of the candle" [p. 32]
- "The confirmation of the pattern comes" [p. 32]

**Pseudocode**
```
pattern = downtrend and upper>=2*body and lower<=0.1*body(ASSUMPTION)
BUY when high > H[pattern] within 3 bars (ASSUMPTION window); stop = L[pattern]
```

**Ambiguities & assumptions**
- Confirmation window not stated here. ASSUMPTION: 3 bars as for sibling patterns.

### 2.11 Hanging Man (bearish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (candlestick, short) | 32 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | After a sustained up-move | 32 |
| Setup conditions | Hammer-shaped: small body at top (red or green), lower shadow at least 2x body, very small or no upper shadow; red more bearish | 32 |
| Entry trigger & order type | Short when price moves below the candle's low | 32 |
| Initial stop-loss | Above the high of the candle | 32 |
| Exits: profit-taking | No target for candlestick patterns | 29 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lower shadow / body | >= 2 | - | 32 |
| Confirmation window | Not stated | - | 32 |

**Key quotes**
- "a lower shadow at least twice the length" [p. 32]
- "The confirmation of the pattern" [p. 32]

**Pseudocode**
```
hm = uptrend and lower>=2*body and upper<=0.1*body (ASSUMPTION)
if low < L[hm] within 3 bars: SHORT / exit longs; stop = H[hm]
```

**Ambiguities & assumptions**
- Identical shape to hammer; only the trend context differs. Window ASSUMPTION 3 bars. Short side not tradable overnight on NSE cash.

### 2.12 Bullish Engulfing (two-candle bullish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (candlestick) | 33 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Prior downtrend | 33 |
| Setup conditions | Red candle followed by green candle whose body engulfs the first red body | 33 |
| Entry trigger & order type | Buy if the highest point of both candles is breached on the upside within next 2-3 candles | 33 |
| Initial stop-loss | Below the low of the two candles | 33 |
| Exits: profit-taking | No target for candlestick patterns | 29 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Confirmation window | next 2-3 candles | - | 33 |
| Engulf test | green body engulfs red body | text also says close above previous day's high | 33 |

**Key quotes**
- "The body of the green" [p. 33]
- "within next 2-3 candles" [p. 33]
- "stop-loss below the low of the two candlestick patterns" [p. 33]

**Pseudocode**
```
e = downtrend and C[t-1]<O[t-1] and C[t]>O[t] and O[t]<=C[t-1] and C[t]>=O[t-1]
pattern_high = max(H[t-1],H[t]); pattern_low = min(L[t-1],L[t])
if high > pattern_high within t+1..t+3: BUY; stop = pattern_low
```

**Ambiguities & assumptions**
- The text says the close should be "above previous day's high" (stricter than body engulfing) and calls the pattern "bearish engulfing" in the confirmation sentence (typo). ASSUMPTION: body engulfing only (open <= prior close, close >= prior open).

### 2.13 Bearish Engulfing (two-candle bearish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (candlestick, short) | 34 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Prior up-trend | 34 |
| Setup conditions | Green candle, then next day gaps up above the previous close and closes red with body totally engulfing the first body; larger 2nd candle = more bearish | 34 |
| Entry trigger & order type | Short if within next 2-3 candles price moves below the low of the two candles | 34 |
| Initial stop-loss | Above the top of the two candles | 34 |
| Exits: profit-taking | No target for candlestick patterns | 29 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Confirmation window | next 2-3 candles | - | 34 |
| 2nd candle size | larger = more bearish | no number | 34 |

**Key quotes**
- "Larger the 2nd candle, more bearish is the pattern." [p. 34]
- "the price moves below the low of the two candles" [p. 34]

**Pseudocode**
```
b = uptrend and C[t-1]>O[t-1] and O[t]>C[t-1] and C[t]<O[t] and C[t]<=O[t-1]
if low < min(L[t-1],L[t]) within t+1..t+3: SHORT / exit longs; stop = max(H[t-1],H[t])
```

**Ambiguities & assumptions**
- Gap-up is stated as part of the pattern; difference from 2.12 (no gap required). ASSUMPTION: follow text, require O[t] > C[t-1].

### 2.14 Piercing Pattern (bullish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (candlestick) | 34 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated (assumed downtrend as it is "similar to the bullish engulfing pattern") | 34 |
| Setup conditions | As bullish engulfing, but 2nd candle closes beyond the halfway mark of the first body instead of engulfing | 34 |
| Entry trigger & order type | Buy when price crosses the high of the two candles within next 2-3 candles | 34 |
| Initial stop-loss | Below the low of the candle | 34 |
| Exits: profit-taking | No target for candlestick patterns | 29 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Penetration of first body | beyond halfway mark | - | 34 |
| Confirmation window | next 2-3 candles | - | 34 |

**Key quotes**
- "closes crossing the halfway mark of the body of the first candle" [p. 34]

**Pseudocode**
```
p = downtrend and red[t-1] and green[t] and C[t] > (O[t-1]+C[t-1])/2 and C[t] < O[t-1]
BUY if high > max(H[t-1],H[t]) within 3 bars; stop = min(L[t-1],L[t])   # "low of the candle": ASSUMPTION both candles
```

**Ambiguities & assumptions**
- "low of the candle" is ambiguous (one or both). ASSUMPTION: lowest of the two. Gap-down open of 2nd candle not stated.

### 2.15 Dark Cloud Cover (bearish)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (candlestick, short) | 35 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated (assumed uptrend, "similar to the bearish engulfing pattern") | 35 |
| Setup conditions | As bearish engulfing, but the 2nd candle crosses 50% of the first candle's body instead of engulfing | 35 |
| Entry trigger & order type | Short once a candle breaches the bottom of the pattern | 35 |
| Initial stop-loss | Above the high of the candle | 35 |
| Exits: profit-taking | No target for candlestick patterns | 29 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Penetration of first body | 50% | - | 35 |
| Confirmation window | Not stated | - | 35 |

**Key quotes**
- "it crosses 50% the body of the first candle" [p. 35]
- "breaches the bottom of the pattern" [p. 35]

**Pseudocode**
```
d = uptrend and green[t-1] and red[t] and O[t] > C[t-1] (ASSUMPTION) and C[t] < (O[t-1]+C[t-1])/2 and C[t] > O[t-1]
SHORT / exit longs if low < min(L[t-1],L[t]) within 3 bars (ASSUMPTION); stop = max(H[t-1],H[t])
```

**Ambiguities & assumptions**
- Window and the gap-up are not stated. ASSUMPTION as above.

### 2.16 Price versus SMA (slope and cross)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 39 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Medium-term SMA with positive slope = positive medium-term trend (and vice versa) | 39 |
| Setup conditions | SMA = mean of last n closes; short-term 5, 8, 13; medium 20, 34, 50; long 100, 200 | 38 |
| Entry trigger & order type | Price breaching a moving average from down to up is a bullish sign (no entry order specified) | 39 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Price breaching a MA from above and closing below is bearish | 39 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| SMA length (short) | not fixed | 5, 8, 13 | 38 |
| SMA length (medium) | not fixed | 20, 34, 50 | 38 |
| SMA length (long) | not fixed | 100, 200 | 38 |
| Example | 9-period SMA | - | 38 |

**Key quotes**
- "For shorter-term SMA, we can use 5,8,13 etc." [p. 38]
- "If a medium term moving average is having a positive slope" [p. 39]
- "closing below is" [p. 39]

**Pseudocode**
```
sma = SMA(close, N)        # ASSUMPTION N=50 (book gives list only)
long_regime = sma[t] > sma[t-k]   # ASSUMPTION k=5 for slope
BUY signal: close[t-1] < sma[t-1] and close[t] > sma[t]
EXIT signal: close[t-1] > sma[t-1] and close[t] < sma[t]
```

**Ambiguities & assumptions**
- The book offers no single recommended length; N, slope window k, and whether the upward cross needs a close above the MA ("down to up" vs "closing below" on the bearish side) are open. ASSUMPTION: close-based on both sides. No stop is given.

### 2.17 Short/medium SMA crossover
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 39 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Shorter-term SMA vs medium-term SMA | 39 |
| Entry trigger & order type | Shorter SMA crosses medium SMA from below = bullish crossover | 39 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Shorter SMA crossing below medium SMA = bearish crossover | 39 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Short SMA | not fixed | 5, 8, 13 | 38 |
| Medium SMA | not fixed | 20, 34, 50 | 38 |

**Key quotes**
- "If we find a shorter term moving average crossing a medium term moving average from below" [p. 39]
- "often considered a signal of bearishness" [p. 39]

**Pseudocode**
```
fast=SMA(close,F); slow=SMA(close,S)   # ASSUMPTION F=13, S=34 (both from the book's lists; pair not given)
BUY next open when fast crosses above slow; SELL when fast crosses below slow
```

**Ambiguities & assumptions**
- Pair not specified. ASSUMPTION: 13/34 plus sensitivity test over {5,8,13} x {20,34,50}. Note that the sentence on p. 39 says "often", so signal quality is not claimed.

### 2.18 RSI overbought/oversold combined with a reversal pattern
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion (indicator + pattern) | 40 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | RSI(14 default): above 70 overbought, below 30 oversold, 30-70 normal | 39, 40 |
| Entry trigger & order type | Long: RSI breaches 30 from below and a bullish reversal pattern is observed. Short: RSI breaches 70 and a bearish reversal pattern is seen | 40 |
| Initial stop-loss | "with stop loss" (value not stated) | 40 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RSI period | 14 (default) | change to alter sensitivity | 40 |
| Overbought | 70 | - | 39 |
| Oversold | 30 | - | 39 |
| Formula | RSI = 100 - 100/(1+RS); RS = avg gain / avg loss over period | smoothing not stated | 40 |

**Key quotes**
- "It is considered overbought when it goes above 70" [p. 39]
- "The default setting for Relative Strength Index is 14" [p. 40]
- "if RSI breaches 30 from below and we observe a bullish reversal" [p. 40]

**Pseudocode**
```
rsi = RSI(close,14)  # ASSUMPTION: Wilder smoothing (book names Wilder; averaging method not given)
bull_setup = rsi crossed (above) 30 within last K bars (ASSUMPTION K=3) and a bullish pattern from 2.8/2.10/2.12/2.14 confirmed
BUY; stop = pattern stop of that setup
bear_setup (rsi>70 + bearish pattern): exit longs / avoid (no NSE cash shorting)
```

**Ambiguities & assumptions**
- "breaching 30 from below" is ambiguous (crossing up through 30 after being below, vs touching below 30). The text for the short side says "breaching the 70 level" without direction. ASSUMPTION: long on cross back above 30; short/exit on cross back below 70 (mirror). The book also calls RSI "a leading indicator" [p. 39]; no testable claim.
- Alignment window between RSI and pattern: not found in this book.

### 2.19 ADX trend-strength filter with +DI/-DI cross
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following (trend-strength filter and direction) | 41 |
| Timeframe & holding period | Not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | ADX above 20 or 25 = trending phase (up or down) | 41 |
| Setup conditions | ADX with +DI and -DI lines | 41 |
| Entry trigger & order type | +DI crosses -DI from below: market generally moves up; -DI crosses +DI from below: market generally moves down | 41 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| ADX trend threshold | 20 or 25 | either | 41 |
| ADX period | Not stated | - | 41 |

**Key quotes**
- "When ADX is above 20 or 25, generally Market is considered to be in a trending phase." [p. 41]

**Pseudocode**
```
adx,pdi,mdi = ADX(14)   # ASSUMPTION period 14 (Wilder default, not in book)
if adx>25 (ASSUMPTION; book says 20 or 25) and pdi crosses above mdi: BUY
exit: mdi crosses above pdi, or adx<20 (ASSUMPTION)
```

**Ambiguities & assumptions**
- Whether ADX must be above threshold at the cross is not stated. ASSUMPTION: yes. ADX period and stop: not found in this book.

## 3. Risk & money-management rules

- Always keep a stop loss when buying a trendline pull-back: "the investor should maintain a stop loss point" [p. 13].
- Short pull-backs to a down-trend line use a stop little above the line [p. 14]; channel trades use small stops [p. 16].
- Classical patterns provide a measured target; candlestick patterns give entry and stop but no target [p. 29].
- Pattern confirmation is required before entry for candlesticks (price beyond the candle's high/low within the next 2-3 candles) [p. 29, 30, 33, 34].
- Position sizing, risk per trade, max exposure, drawdown rules: not found in this text.

## 4. Non-codable guidance

- Technical analysis is "more of an art than science"; probabilities differ by stock and phase; build own judgment by logging predictions and reviewing them [p. 5].
- Higher time frames are generally more reliable [p. 7].
- Trend structure: primary, secondary and minor trends; markets consolidate at times and then break up or down [p. 11, 12].
- Double top/bottom: price tests support/resistance twice and fails to break; "one of the most reliable patterns" for intermediate/long-term reversals; no entry, stop or target stated [p. 23].
- Triangles (symmetrical, ascending, descending): last from a couple of weeks (ideally over 12 weeks) to months; usually continuation, sometimes reversal; no entry rule [p. 25].
- Flags and pennants: continuation after a sharp move; usually 1-3 weeks (1-12 possible, ideally 1-4); no entry rule [p. 26].
- Wedges: 3-6 months; falling wedge in uptrend bullish, rising wedge in downtrend bearish; no entry rule [p. 27].
- Doji: signals indecision and caution after a trend; no rule given [p. 35, 36].
- Traders combine indicators and price patterns; rarely rely on one [p. 43].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily open, high, low, close, volume; delivery % (for 2.5); optionally NIFTYBEES/equal-weight index (not required by the book). No fundamentals.
- **Testability with our data:** all rules are price/volume based, so everything is backtestable on 2005-2026 daily OHLCV except delivery % rules (only recent years). Pattern definitions (swings, necklines, trendlines, "prolonged trend") are discretionary and must be algorithmised with ASSUMPTIONs; results measure the coder's definitions, not the book's.
- **Market-structure differences:**
  - Short-side rules (2.2, 2.6 bearish side, 2.7 tops, 2.9, 2.11, 2.13, 2.15, RSI>70 short, -DI cross) cannot be traded as overnight cash shorts on NSE. ASSUMPTION: use them as long-exit/avoid signals, or intraday only.
  - Gap-up/gap-down conditions are meaningful with NSE daily opens, but circuit limits can distort gaps in small caps. ASSUMPTION: skip stocks locked in circuit that day.
  - Costs: ASSUMPTION STT plus brokerage plus 0.1% slippage per side; candlestick patterns have small stops, so costs matter.
  - ASSUMPTION: liquidity filter (e.g. median 20-day turnover above a threshold) since the book has none.

## 6. Verdict

- **Codeability:** Partly. Entry/stop/target rules exist for trendlines, H&S, triple tops, 8 candlesticks, SMA, RSI and ADX, but pivots, trend context, tolerances and stops are not parameterised, and position sizing and exits are absent for most.
- **Priority for backtesting:** Low. Introductory material with no edge evidence or track record; useful only as a baseline set of textbook rules (candlestick confirmation, SMA crossover, RSI+pattern, ADX filter).
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating an unconfirmed candlestick as a signal; the book requires a breach of the candle's high/low (low for shorts) within about 2-3 candles, with the stop at the candle extreme, and gives no target.
  2. Using the bearish rules as shorts on NSE cash, and misreading the trend context ("prolonged"/"sustained" trend is undefined, so the pattern must be filtered by an explicit trend definition).
  3. Inventing precise parameters (SMA pair, ADX period, RSI smoothing, stop distances) and presenting them as the author's; the book gives only lists of lengths (5, 8, 13; 20, 34, 50; 100, 200), RSI 14/70/30 and ADX 20/25.
