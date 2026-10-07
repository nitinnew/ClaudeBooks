# Trendline Trading Strategy Secrets Revealed — Myronn Saremo (named in the copyright notice, p. 2)

- **Source file:** Google Drive: Trendline Trading Strategy Secret Revealed.pdf
- **Text file used:** text/unknown_trendline_strategy_secret.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - N taken only from the nearest `[[PAGE N]]` marker above the passage. The repeated website running header (www.forextrendlinetrading.com) is ignored.
- **Coverage:** Read lines 1-3881 (all) sequentially; last `[[PAGE N]]` reached = 114. No chapters skipped. Pages with no body text (header only, chart images): p. 8. p. 109 (one-page reversal-candlestick cheat sheet) is garbled/fragmentary text only. Many other pages are chart-only with 1-3 caption lines; all chart content is image-only and not recoverable from text. Reading done by a Sonnet sub-agent (notes log covers lines 1-3881 in 5 chunks). The coordinator re-ran the verifier and an exact-page check and spot-checked 10 unquoted table citations.

## 1. The method in brief
A discretionary, price-only (no indicators) trend-following swing method for forex: draw trendlines through 2+ obvious swing highs (downtrend line) or swing lows (uptrend line), and trade the bounce when price returns to touch or nearly touch the line, with the trend, using larger-timeframe (monthly to 1h) lines and entering on 1h/4h or smaller timeframes [p. 4, 7, 38, 43]. The claimed edge is low-risk entries (small stops beyond the touch candle), R:R above 1:3, and "3 secrets": trail the stop behind swing lows/highs instead of using profit targets, add on to the same trend move, and require a reversal candlestick (momentum) at the line [p. 52, 77, 82, 84, 88]. Evidence is anecdotal: screenshot trades (e.g. 800 pips on three USDCHF trades in a week, 561 pips on one GBPJPY trade, 373 vs 144 pips trailing vs target on one trade, 177 pips on 20 pip risk) [p. 3, 73, 78-81]. No statistics, win rate or systematic test are given. The book is written for forex (pips, lots, spreads, 1:100 leverage, MetaTrader), not equities [p. 111]; see section 5.

## 2. Strategies

### 2.1 Conservative trendline bounce (pending stop order after candle at the line)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following, buy/sell the touch of a trendline (with-trend bounce) | 4, 44, 45 |
| Timeframe & holding period | Lines drawn on monthly/weekly/daily/4h/1h; entries mainly 1h and 4h; trades held hours to days, even 2 weeks | 43, 107, 110 |
| Universe / eligibility filters | Any pair, any timeframe; prefer low spreads; analyse all pairs but do not take every setup | 4, 37, 111 |
| Market / regime filter | Trade with the trend (HH/HL for longs, LH/LL for shorts); strategy works in trending, not ranging markets; no trade if an opposing trendline or S/R is close ("not enough room"); avoid entry just before major news | 30, 56, 68, 112 |
| Setup conditions | Long: trendline through at least two higher lows; short: through at least two lower highs. Valid lines: obvious, significant swing points, line touches both points, no price obstruction between them, not drawn through bodies/wicks. Candle at CLOSE almost touches, touches or intersects the line but does not close significantly beyond it. Third or later touch is the entry, never point 2. Reversal candlestick at the line used as confirmation (see 2.5). Preferred: gentle slope, line touched more than once, S/R confluence | 7, 9, 20, 23, 24, 44, 45, 54, 107 |
| Entry trigger & order type | Short: sell stop a few pips (2-5, depends on spread) under the low of the candle at the line. Long: buy stop 2-5 pips plus spread above the high of that candle. If not triggered, move the order to the low (short) or high (long) of each subsequent candle (higher low / lower high); cancel if a candle closes significantly beyond the trendline | 44, 45, 53 |
| Initial stop-loss | Short: just above the high of the signal candle / nearby peak, default 5 pips above, optionally 10-15 pips. Long: 5 pips below the signal candle low / trough, optionally 10-15 pips. Place behind S/R. 1h/4h stops are often 20-60 pips | 44, 45, 52, 56 |
| Exits: profit-taking | Optional target at previous significant swing low (short) or higher high (long), checking larger timeframes if none visible; or Fibonacci 161.8 (preferred) / 261.8 extension; or minimum R:R 1:3; partial profit at S/R must exceed initial risk, e.g. half off after 100 pips | 44, 45, 52, 70 |
| Exits: trailing / time / signal | Preferred: no target; trail stop behind each new swing low (longs) / high (shorts); stop moved only when a new peak/trough forms (for shorts: when a candle makes a higher high, move to break-even after its close); tighten or take partials when approaching opposing trendline or horizontal S/R; exit when trend (HL/LH sequence) breaks | 33, 36, 69, 77, 78, 80, 111, 113, 114 |
| Position sizing | Fixed fractional: about 2% risk per trade; if planning 2-3 trades a day risk 1% each (3% a day max implied); lots = risk / stop distance | 43, 110 |
| Adding to / pyramiding | Add a new trade on the same trendy move only when the previous trade is in profit with profit locked or stop at break-even; same risk % on each add; stops cascade so total open risk is about 2% | 82, 83 |
| Portfolio limits (max positions, correlation, heat) | 1-3 trade opportunities per day; "don't overtrade"; no correlation rule given | 80, 110 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Min swing points per line | 2 | more touches = stronger | 7, 24 |
| Order offset from signal candle | 2-5 pips (+ spread) | depends on spread | 44, 45 |
| Stop beyond signal candle | 5 pips | 10-15 pips | 44, 45 |
| Typical 1h/4h stop | 20-60 pips | - | 56 |
| Keep breached trendline if price is within | 5-10 pips (5m); 20-40 pips (1h); 40-60 pips (4h) | no exact rule | 22 |
| Min R:R | 1:3 | system said to give above 1:3 | 52 |
| Fib extension targets | 161.8 | 261.8 | 52, 70 |
| Risk per trade | 2% | 1% if 2-3 trades/day | 110 |
| Trendline slope | gentle preferred | steep = weak | 24 |

**Key quotes**
- "Connect a minimum of 2 peaks (or highs)" [p. 7]
- "The trendline MUST touch" [p. 23]
- "Place Stop Loss just above the peak near the short trade entry area." [p. 44]
- "Place Stop Loss just below the low or trough in the trade entry area." [p. 45]
- "Set the profit target within previous significant low (or trough)." [p. 44]
- "Place your stop loss behind support and resistance levels." [p. 52]
- "I suggest you stick to the 2% rule." [p. 110]
- "Never chase a trade if you see you have missed a nice trade setup hours ago." [p. 56]

**Pseudocode** (daily bars as NSE adaptation, long side only; "significant" parameters are assumptions)
```
each day:
  swings = pivot lows with N=5 bars each side (N is ASSUMPTION; book: "more higher candlesticks on left and right")
  for each pair of pivot lows (a,b), b after a, with l(b) > l(a), no bar between a and b with low below the line
       (no obstruction), slope within gentle limit:
      line = through (a,b); touches = count of later bars with low within tol of line
      invalidate line if any close < line - sig (sig = ASSUMPTION: 1% or 0.5*ATR14) ; also if body long
  trend_ok = last two swing lows rising and last two swing highs rising
  if trend_ok and bar t has low <= line(t)+tol and close >= line(t)-sig and touches>=3rd touch:
      confirm = reversal pattern (section 2.5) on bar t  [optional switch]
      room_ok = no resistance / opposing line within 3 * stop distance of entry [ASSUMPTION]
      place buy stop at high(t) + offset; stop = low(t) - buf; cancel/move order daily:
          each next day, if not filled and close not significantly below line: set trigger = high(that day) if lower than before
  after fill: initial stop = low(t) - buf; position size = 2% * equity / (entry - stop)
  trail: when a new swing low forms above the old stop, raise stop to just below it
  exit: stop hit; or optional target = prior swing high; or R:R >= 3 partial
```

**Ambiguities & assumptions**
- "Significantly" beyond the line has "no exact formula" [p. 13]; considers close, body length, 1h/4h close. ASSUMPTION: close more than 0.5 ATR(14) beyond the line, or body larger than average body, invalidates.
- "Very close" / "almost touches" undefined. ASSUMPTION: bar low within 0.5 ATR(14) of the line.
- Trendline drawing is visual. ASSUMPTION: pivot-based automatic algorithm above; require line from two pivots at least 10 bars apart.
- Whether reversal candle is mandatory: summary says check before placing order "very important" [p. 107], but entry rules do not list it. ASSUMPTION: test both with and without.
- Profit target vs trailing: author prefers trailing but allows targets [p. 78, 111]. ASSUMPTION: trailing as base case, target 1:3 as variant.
- Pip values: ASSUMPTION: convert pips to percent/ATR (see section 5).
- Fib confluence and S/R confluence are "good practice" not mandatory [p. 29, 106].

### 2.2 Aggressive entry (market order at the touch)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following, early entry at the trendline | 46 |
| Timeframe & holding period | Trendlines from 1h up to monthly; watch on 5m-30m or 1h/4h; hold as 2.1 | 43, 46, 48 |
| Universe / eligibility filters | Any pair; larger-spread pairs need wider stops | 47, 111 |
| Market / regime filter | Same as 2.1 (trend direction, room to move, no news) | 56, 112 |
| Setup conditions | Valid trendline (as 2.1) touched or almost touched (1-5 pips short). Price rarely passes a holding line by more than 1-20 pips. If long candle is forming do not hesitate (price will not wait) | 47, 48 |
| Entry trigger & order type | Instant market order immediately when the trendline is touched or almost touched | 46, 48 |
| Initial stop-loss | 10-30 pips from entry (usually 10-20; 20-30 for wider-spread pairs); example 15 pips | 46, 47 |
| Exits: profit-taking | Targets similar to 2.1 (prior swing high/low) | 46 |
| Exits: trailing / time / signal | Move stop to break-even quickly once price moves away; then trail as 2.1 | 47, 78 |
| Position sizing | Same % risk; smaller stop allows bigger lots at same risk (2% example) | 43, 46, 47 |
| Adding to / pyramiding | Same as 2.1; if stopped out, re-enter via conservative entry when a reversal candle forms at 1h/4h | 51, 83 |
| Portfolio limits (max positions, correlation, heat) | Same as 2.1 | 80, 110 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Stop distance | 10-20 pips | 10-30 pips; 20-30 for large spreads | 46, 47 |
| "Almost touched" distance | 1-5 pips | - | 48 |
| Overshoot of a holding line | up to 1-20 pips | examples 12 pips | 47, 50 |
| Move to break-even | "very quickly" | no trigger value | 47 |

**Key quotes**
- "The Aggressive Entry Technique is entering at INSTANT MARKET ORDER" [p. 46]
- "Stop loss is placed 10-30 pips away from entry" [p. 46]
- "My stops with this technique are usually from 10-20 pips" [p. 47]
- "If you are new trader, stick to the conservative" [p. 51]

**Pseudocode**
```
if valid trendline (as 2.1) and trend_ok and low(t) <= line(t) + near_tol:   # intraday touch
    buy at market (next bar open on daily data); stop = entry - stopdist (stopdist = ASSUMPTION 1.0-1.5 ATR14)
    when price >= entry + 1R: stop = entry (break-even)  # ASSUMPTION trigger
    thereafter trail below new swing lows
```

**Ambiguities & assumptions**
- Break-even trigger not given quantitatively. ASSUMPTION: +1R (author's FAQ implies break-even only after a new swing forms [p. 113]; test both).
- Stop 10-30 pips is timeframe-specific; ASSUMPTION: convert to ATR multiples.
- Book says to combine both entry types but gives no switching rule [p. 51]. ASSUMPTION: test separately.

### 2.3 Breakout of a support/resistance level near a trendline
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout continuation near a trendline | 61, 62 |
| Timeframe & holding period | Trendline from 1h/4h; the S/R level often visible only on 30m-5m; hold as 2.1 | 65, 66 |
| Universe / eligibility filters | Any pair | 4 |
| Market / regime filter | With the trend; used when trendline entries were missed | 62, 65 |
| Setup conditions | Short: a support level forms very near a downward trendline (price need not return to the line). Long: a resistance level forms very near an upward trendline | 62, 63 |
| Entry trigger & order type | Buy stop above the resistance level (long) / sell stop below the support level (short), waiting for a breakout | 65 |
| Initial stop-loss | Two options: option 1 farthest away (avoids premature stop-out); option 2 near entry. Choose option 2 when entry is a safe distance away; option 1 may give poor R:R | 63, 64 |
| Exits: profit-taking | Not specified separately; as 2.1 | 66 |
| Exits: trailing / time / signal | As 2.1 (trail behind swing levels) | 69 |
| Position sizing | As 2.1 | 110 |
| Adding to / pyramiding | As 2.1 | 83 |
| Portfolio limits (max positions, correlation, heat) | As 2.1 | 110 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Distance of S/R level to trendline | "NEAR" / as near as possible | not quantified | 62 |
| Stop option | option 2 (closer) when entry not too close; option 1 otherwise | - | 63, 64 |

**Key quotes**
- "It is based on trading the breakout of support and resistance levels NEAR" [p. 62]
- "The support level must be near to the trendline as possible." [p. 62]

**Pseudocode**
```
long: given valid up-trendline, find last swing high H (resistance) with H - line(t) < k*ATR14 (k ASSUMPTION 1.0)
      place buy stop at H + offset; stop = option2: below breakout-candle/recent minor swing low; option1: below trendline-touch low
      cancel if close < line - sig
```

**Ambiguities & assumptions**
- Stop options 1 and 2 are only illustrated in charts. ASSUMPTION: option 1 = low of the last trendline touch, option 2 = low of last minor swing before breakout.
- "Near" undefined. ASSUMPTION: within 1 ATR14.
- Profit exit not stated for this variant. ASSUMPTION: same as 2.1.

### 2.4 Reversal candle after a trendline break ("fake-out" re-entry)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following re-entry after failed break | 103, 104 |
| Timeframe & holding period | 1h/4h candles (author's examples); hold as 2.1 | 103, 104 |
| Universe / eligibility filters | Any | 4 |
| Market / regime filter | Original trend direction; the trendline was apparently broken but the break candle is short-bodied | 14, 18 |
| Setup conditions | A candle intersects and closes beyond the trendline; within the next 1 or 2 candles a reversal pattern forms; that candle must be very close to the broken line (not a significant distance away) | 103, 104 |
| Entry trigger & order type | Take the trade (entry by pending order after the pattern, as in the author's example) | 95, 103 |
| Initial stop-loss | Not separately stated; ASSUMPTION as 2.1 | 44 |
| Exits: profit-taking | As 2.1 | 44 |
| Exits: trailing / time / signal | As 2.1 | 78 |
| Position sizing | As 2.1 | 110 |
| Adding to / pyramiding | As 2.1 | 83 |
| Portfolio limits (max positions, correlation, heat) | As 2.1 | 110 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Candles allowed after break | 1 or 2 | - | 103, 104 |
| Distance of reversal candle from line | "very close" | not quantified | 103, 104 |

**Key quotes**
- "The important factor here is the distance: it has got to happen very close to" [p. 104]
- "Just wait and watch the next 1 or 2 candles to see if you get a good reversal candlestick pattern forming." [p. 104]

**Pseudocode**
```
if bar t-k (k in {1,2}) closed beyond line and bar t is a reversal pattern (2.5) back toward trend
   and |close(t) - line(t)| < near_tol:   # near_tol ASSUMPTION 0.5 ATR14
    place entry stop beyond bar t extreme; stop = opposite extreme of bar t +/- buffer
```

**Ambiguities & assumptions**
- Conflicts with the line-invalid-on-significant-close rule [p. 13]; the author reconciles via distance and body length [p. 14, 104]. ASSUMPTION: apply only if break candle body is shorter than average body.
- Stop and target not specified. ASSUMPTION: as 2.1.

### 2.5 Reversal candlestick confirmation filter (momentum, "Secret #3")
Used as an entry confirmation at the trendline for 2.1-2.4; not a stand-alone system.
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick confirmation filter for trendline entries | 88, 107 |
| Timeframe & holding period | 1h and 4h (can be seen on either; 30m railway track equals 1h hammer) | 95, 108 |
| Universe / eligibility filters | Any | 4 |
| Market / regime filter | Pattern must occur on the trendline entry point in the matching direction | 89-95 |
| Setup conditions | Bullish at upward trendline: dragonfly doji, doji cross, bullish engulfing, piercing line, bullish harami, hammer, spinning top, bullish railway track. Bearish at downward trendline: gravestone doji, doji cross, bearish engulfing, dark cloud, bearish harami, shooting star, spinning top, bearish railway track | 88, 89-95 |
| Entry trigger & order type | After the pattern, place the stop order as in 2.1 | 95 |
| Initial stop-loss | As 2.1 | 44 |
| Exits: profit-taking | As 2.1 | 44 |
| Exits: trailing / time / signal | As 2.1 | 78 |
| Position sizing | As 2.1 | 110 |
| Adding to / pyramiding | As 2.1 | 83 |
| Portfolio limits (max positions, correlation, heat) | As 2.1 | 110 |

**Pattern definitions as given:** Doji: unusually short candle vs neighbours; open equals close [p. 89]. Engulfing (variation for forex): second candle's range engulfs the first, and its body is at least greater than the first body [p. 90]. Piercing/dark cloud: close beyond 50% of previous real body (at least half way into it) [p. 91, 92]. Harami: second candle (inside bar) forms within the previous candle [p. 92, 93]. Hammer/shooting star: long tail, short body, next candle breaking the hammer's high (or violating the shooting star's low) confirms [p. 93, 94]. Spinning top: short body, tight range, color irrelevant [p. 94]. Railway track: two long opposite-color candles of similar length; combined equals hammer/shooting star [p. 94, 95]. Optional Fibonacci confluence: 38.2, 50, 61.8 (61.8 preferred) [p. 106].

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Piercing/dark cloud penetration | at least 50% of previous body | - | 91, 92 |
| Fib confluence level | 61.8 | 38.2, 50 | 106 |
| Patterns required | any one of the 7 | - | 107 |

**Key quotes**
- "The last candlestick must penetrate" [p. 91]
- "Look for a bullish engulfing formation on upward trendline entry points" [p. 90]
- "Look for bullish railway track pattern on upward trendline entry points to" [p. 94]

**Pseudocode**
```
bull_reversal(t) = any of: dragonfly (open~close~high, long lower shadow), doji cross, bull engulf (range(t) engulfs range(t-1) and body(t) > body(t-1), t bullish),
  piercing (t-1 bearish, close(t) > mid body(t-1)), bull harami (t inside t-1 range, t bullish), hammer (lower shadow >= 2*body, small upper shadow),
  spinning top (body < 0.3*range), bull railway (t-1 long bear, t long bull, similar size)   # numeric thresholds ASSUMPTION
```

**Ambiguities & assumptions**
- No numeric definition of "short body", "long tail", "similar length", "unusually long". ASSUMPTION: body less than 30% of range for doji/spinning top (doji less than 10%), tail at least 2x body, lengths within 25%.
- Spinning top and doji cross are allowed in both directions; ASSUMPTION: require close in trade direction on next bar not demanded.
- Whether pattern must be on the touch candle, or any candle within the line zone: ASSUMPTION: the signal candle itself.

### 2.6 Trendline entry variations 1-4 (not coded)
The author shows four variations where a line is broken and later obeyed, in which "normal" trendlines cannot be drawn [p. 58, 59]. Only chart images are provided, no textual rules. Not codable; noted only [p. 59-61].

## 3. Risk & money-management rules
- Risk about 2% per trade; with 2 trades a day risk 1% each; with 3 trades a day, 3% daily and 1% each [p. 110].
- Position size from stop distance: smaller stops allow larger lots at same % risk [p. 43].
- Leverage 1:100 suggested; stop-based risk matters more than leverage [p. 111].
- Add-ons keep identical risk, never increase lot size because of profit [p. 83].
- Trade no more than 1-3 opportunities per day; do not overtrade [p. 80, 110].
- Move stops only when a new swing forms (not at fixed 1R) [p. 113].
- Protect profits at opposing trendlines or horizontal S/R: tighten stop, take partials, or exit [p. 111, 112].
- Avoid new trades just before major news [p. 68, 112].
- Never let a winner become a loser [p. 69].
- Demo for 3-6 months first [p. 107].

## 4. Non-codable guidance
- Judging "obvious" peaks and troughs, line significance and inner vs outer lines [p. 9, 10, 13].
- Judging momentum and whether a break is "significant" [p. 13, 14].
- Multi-timeframe chart review and colour-coded lines [p. 38].
- Leave the trade alone after placing orders; avoid revenge trading and late entries [p. 68, 69].
- Do not change opinion too quickly in a trade; follow the system without over-analysis [p. 96, 108].
- Do not add other indicators [p. 113].
- Trendline entry variations 1-4 (chart-only) [p. 59-61].

## 5. Adapting to NSE (Indian equities)
- **Data required:** daily OHLC (and ideally weekly resampled) for each stock; volume only for liquidity filter; Nifty proxy (NIFTYBEES or equal-weight panel) as optional trend filter. No delivery %, fundamentals or news data needed.
- **Testability with our data:** all rules based on price can be backtested 2005-2026 on daily bars. The book is written for forex with intraday (5m-4h) entries: our data is daily only, so 1h/4h/5m rules, 1h/4h close logic and smaller-timeframe entry timing cannot be tested. Daily/weekly trendlines with daily entries are testable. News avoidance is not testable. Discretionary line drawing needs an algorithmic proxy.
- **Market-structure differences:** (1) Forex pips and lot sizing do not apply. ASSUMPTION: express stops as ATR14 multiples or percent; size by 1-2% risk / stop distance. (2) No overnight shorting in NSE cash: ASSUMPTION: long-side (upward trendline) setups only; the short rules are for reference. (3) Timeframes: ASSUMPTION: treat weekly as "long term" and daily as "medium", entry on daily bars (stop order at signal-bar high, valid one day, re-set daily). (4) Gaps and circuit limits exist, unlike continuous forex: stops fill at the open gap price; skip if upper/lower circuit. (5) Costs: STT, brokerage, about 0.1% slippage; low-priced or illiquid small caps excluded via liquidity filter (ASSUMPTION: median 20-day traded value above a threshold). (6) Fixed-pip rules (5-10 pips breached-line tolerance, 10-30 pip stops) must be rescaled; ASSUMPTION: tolerance 0.25-0.5 ATR(14) on daily.

## 6. Verdict
- **Codeability:** Partly. Entry, stop, sizing, trailing and add-on mechanics are clear, but trendline drawing, "significant" breaks and "very close" are discretionary and need an assumed algorithm; intraday elements are not testable with daily data.
- **Priority for backtesting:** Medium. Simple, popular price-action concept with the trailing-stop and pyramiding rules worth testing on daily NSE data, but there is no evidence beyond screenshots and results will depend heavily on the line-detection algorithm.
- **Top 3 things a coder is most likely to get wrong:**
  1. Trendline construction: must connect significant pivots with no price obstruction, touch both points, and be invalidated by a significant close beyond (not any pierce); a regression line or a line through bodies and wicks is explicitly wrong [p. 20, 23].
  2. Entry logic: the stop order is placed beyond the signal candle's extreme and moved each bar until triggered (or cancelled on a significant close beyond the line); entering on the touch bar close or at point 2 is a listed mistake [p. 44, 53, 54].
  3. Trailing and add-ons: stops move only behind newly formed swing lows/highs (not fixed R), with no profit target in the preferred version; adds only when the prior position has locked profit, with the same risk each [p. 78, 83, 113].
