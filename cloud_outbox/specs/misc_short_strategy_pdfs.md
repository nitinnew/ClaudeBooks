# Short strategy PDFs (bundle) — various authors

- **Source file:** Bundle of 17 short PDFs (Google Drive), concatenated in text/misc_short_strategy_pdfs.txt. Files, page ranges (continuous `[[PAGE N]]` numbering) and the author/publisher as stated on the pages themselves:
  - "Learn price action(1).pdf", pp. 1-20: LearnPriceAction.com, "Guide to Price Action Entry Signals" [p. 1]. Forex-oriented.
  - "Price Action Analysis in Trading(1)(8).pdf", pp. 21-36: winningtrade.in (no personal author named) [p. 36]. NSE charts via Zerodha Kite.
  - "How to Trade with Support and Resistance(1)(8).pdf", pp. 37-55: winningtrade.in (no personal author named) [p. 55].
  - "Support-and-Resistance-Trading-Strategy-PDF.pdf", pp. 56-76: thetradingresource.com [p. 57, 76]. Forex (CAD/JPY) example.
  - "Guide to trendline trading.pdf", pp. 77-94: author/publisher NOT stated in the text (title only: "The complete guide to trend line trading") [p. 77].
  - "Supply and Demand Zone.pdf", pp. 95-170: "Trade Like Pro. The Ultimate Trading Kit to Master Supply & Demand", Jode Lebin, (c) 2017 [p. 96]. Forex.
  - "P.O.3 patterns.pdf", pp. 171-186: JayFX / "Jay Forex House" (t.me/JayFxHouse), "Power of Three" notes [p. 171, 186].
  - "Breakouts & Breakdowns.pdf", pp. 187-200: author/publisher NOT stated in the text; NSE charts from TradingView [p. 189].
  - 14 Multi Year Breakouts.pdf, pp. 201-205: @ADX_Learner (Avdhesh) [p. 201].
  - "RSI 73 v1.pdf", pp. 206-214: Tradetron platform backtest report (strategy "RSI 73 V1") [p. 206].
  - "neo wave patterns 206.pdf", pp. 215-236: Glenn Neely / NEoWave, Inc., 1995 conference slides [p. 215].
  - "Trading Divergence Interview with Ashwani Gujral.pdf", pp. 237-242: Stocks & Commodities V. 23:3 (64-71), Technical Analysis Inc.; interview of Ashwani Gujral by Jayanthi Gopalakrishnan [p. 237].
  - "How to see charts in multiple ways.pdf", pp. 243-248: author NOT stated [p. 243].
  - "Basics of Technical Analysis.pdf", pp. 249-299: Elearnmarkets, "Handbook of Technical Analysis" module (image-only, fully OCR'd) [p. 249].
  - "Start Buying Stock For Beginners.pdf", pp. 300-352: Laz Viera, (c) 2020 [p. 302].
  - "40 Trading Cheatcodes.pdf", p. 353: author NOT stated; Drive plain-text rendering that ends mid-word ("close enou") [p. 353].
  - "Pivot Points Calculations.pdf", p. 354: author NOT stated; Drive plain-text rendering [p. 354].
- **Text file used:** text/misc_short_strategy_pdfs.txt  (page basis: pdf_pages; each PDF's text layer, with pages lacking a text layer RapidOCR'd by the coordinator; numbering continuous across all 17 files)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/misc_short_strategy_pdfs.md text/misc_short_strategy_pdfs.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read sequentially, text-file lines 1-7993, from [[PAGE 1]] to the last marker [[PAGE 354]]; nothing skimmed. OCR'd pages (noisy: dropped spaces, chart-axis numbers, mirrored garbled lines): Learn price action pp. 12, 14; Price Action Analysis pp. 23, 24, 25, 35; S/R pp. 43, 47; SRT eBook pp. 67, 68, 69; Supply and Demand p. 95; Breakouts & Breakdowns pp. 187, 189, 190, 195, 199, 200; 14 Multi Year Breakouts p. 204; all of Basics of Technical Analysis pp. 249-299 (some sentences are unreadable mirrored garbage, notably the hammer confirmation window on p. 279); Start Buying Stock pp. 300, 307, 315, 319, 326, 332, 336, 339, 345. Pages 241-242 (Gujral) and 237 carry duplicated-line text layers. Many chart-only pages (e.g. pp. 14-15, 181-185, 202-205, 211-214, 229-236) contain no rule text. NOT in this text (over the ~7 MB connector limit or failed download, so no rules from them): Price-Action-Trading-Guide.pdf (7.7 MB), 6_Fibonacci_Types_that_Create_the_Most_Precise_Price_Targets_and_Reversal_Zones.pdf (6.99 MB; download crashed the connector), What is Supply and Demand New (1).pdf.pdf (12.8 MB), neo_wave.pdf (12.7 MB), Flirting with Stocks_ Stock Market Investing for Beginners.pdf (15.1 MB), Advance Techniques In Day Trading_-1.pdf (14.7 MB). Split out as separate queue items (full books, processed separately): "Trading for Dummies", "DAY_TRADING_STRATEGIES_THE_COMPLETE_GUIDE...", "Price action trading guide.pdf" (swing-trading-strategies.com), "Beginner's guide to trading.pdf".

## 1. The method in brief

This is a grab-bag of seventeen short documents, not one method. Most are price-action / classical technical-analysis primers (candlestick triggers, support-resistance, trend lines, supply-demand zones, chart patterns, breakouts) written for forex or NSE charts, with discretionary entries and very few numbers. Concrete, testable rules exist for: pin/engulfing/inside-bar triggers [p. 6-19], confirmed candlestick reversal patterns with stops [p. 279-289], support-resistance zone construction [p. 42, 51-55], a monthly/weekly/daily "SRT Combo" [p. 71-75], four trend-line techniques [p. 81-92], a rectangle-zone supply and demand method with 3:1 reward:risk [p. 134-158], Gujral's intraday stochastic-divergence setup [p. 238-241], head-and-shoulders / triple-top / triangle rules [p. 270-275], volume-and-retest breakout handling [p. 193-198, 201, 353], moving-average / RSI / ADX settings [p. 291-295] and a pivot-point formula [p. 354].

Evidence is thin. The only quantified performance is a Tradetron backtest report for "RSI 73 V1" (26 Oct 2020 to 21 Apr 2023, 1-minute intraday, win rate 45.11%, total ROI 400.80% on Rs. 25,000 capital, max drawdown -33.88%) [p. 206-207], but the report contains no entry or exit rules, so it cannot be reproduced. Gujral claims "You can make four points a day on the S&P" [p. 242] without a test. Everything else is illustrated with hand-picked charts.

## 2. Strategies

### 2.1 Pin bar, engulfing bar and inside bar entry triggers (Learn price action, pp. 1-20)

Source file: "Learn price action(1).pdf" (LearnPriceAction.com). Partly codable: setups are defined, entry types are given for pin bar and inside bar, stops are given, but no profit target or sizing.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal / continuation candlestick trigger (price action) | 5, 10, 13, 16 |
| Timeframe & holding period | Not found in this text (forex examples; inside bar compared with the previous day's range) | 13 |
| Universe / eligibility filters | Not found in this text (forex currency pairs) | - |
| Market / regime filter | Trade in line with the trend; a pin bar in a trending market gives better risk:reward; best inside bars form in trending markets in the trend direction; support/resistance and trend lines are the places to use the triggers | 7, 13, 16-17 |
| Setup conditions | Bearish pin bar: forms after several bullish candles, nose higher than the top of the previous candle, nose at least 75% of the candle size, body less than 16% (mirror for bullish). Engulfing bar: candle completely covers the previous candle's range, taking out its high and low (can engulf more than one candle). Inside bar: the second bar is inside the high-low range of the previous (mother) bar | 6, 11, 13 |
| Entry trigger & order type | Pin bar, three alternatives: (a) aggressive: enter on a 50% retrace of the pin bar/reversal candle wick (tighter stop, higher reward and risk); (b) medium: enter as soon as the reversal candle has closed; (c) conservative: enter on a break above/below the pin bar's high or low. Inside bar: buy stop / sell stop at the high or low of the mother bar. Engulfing bar entry order: Not found in this text | 8-9, 16 |
| Initial stop-loss | Pin bar: behind the tail. Inside bar: behind the inside bar's high/low, or (lower-risk option per author) behind the mother bar's high/low. Alternative stops: confluence stop (S/R, previous highs/lows, MAs, trend lines, channels, with padding if repeatedly hunted); volatility stop (wider in high volatility, tighter when calm) | 18-20 |
| Exits: profit-taking | No target rule. Resistance zones are said to be good places for exits; in high volatility widen targets, in low volatility use closer targets | 17, 20 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pin bar nose (wick) length | >= 75% of candle size | - | 6 |
| Pin bar body | < 16% of candle | - | 6 |
| Pin bar entry | 50% retrace / on close / on break of high-low | three styles given | 8-9 |
| Inside bar entry | stop order at mother-bar high (buy) or low (sell) | - | 16 |
| Stop placement | beyond pin-bar tail; beyond inside-bar or mother-bar extreme | confluence or volatility stop | 18-20 |
| Trend lines | at least three major points | - | 18 |

**Key quotes**

- "The nose must be at least 75% of the candle size and the candle body must be less than 16%." [p. 6]
- "This entry involves taking a 50% retrace of the pin bar or other reversal candles wick." [p. 8]
- "The most commonly used entry with the inside bar is to place a buy stop or sell stop at the high or low of the mother bar." [p. 16]
- "You can place a stop loss behind the tail of the pin bar whether it’s bearish or bullish." [p. 18]
- "If you want a lower risk inside bar stop loss strategy, then it’s behind the mother bars high or low." [p. 19]

**Pseudocode** (daily bars; fields O,H,L,C)

```
range = H - L
# Bullish pin bar (mirror for bearish)
lower_tail = min(O,C) - L ; body = abs(C-O)
pin_bull = lower_tail >= 0.75*range and body < 0.16*range and L < L[1] and uptrend_filter
# Inside bar
inside = H < H[1] and L > L[1]          # mother bar = bar[1]
# Entries (choose one style per backtest)
pin: buy at close(signal bar) | buy at H(signal) + tick next bars | limit at L + 0.5*range  (50% retrace)
inside bar: place buy stop at H[1] (mother high) for N bars (ASSUMPTION N=3)
stop = L(signal) - tick (pin)  or  L[1] - tick (inside, mother-bar stop)
```

**Ambiguities & assumptions**
- Book says "nose" for the wick and does not say whether 75% is of the full range or of the wick vs body: ASSUMPTION: nose = long wick; wick/(H-L) >= 0.75 and body/(H-L) < 0.16.
- "50% retrace" does not say of what (wick vs whole candle): ASSUMPTION: 50% of the candle's high-low range, measured from the tail tip.
- No trend definition: ASSUMPTION: close above 50-day SMA for long setups.
- No target: ASSUMPTION: 2R fixed target (no 2R in text; test 1R-3R).
- Engulfing bar entry/stop/target are not found in this text: ASSUMPTION: enter on break of the engulfing bar's high, stop below its low.
- Order validity (how many bars the stop order stays live) not found: ASSUMPTION: 3 bars.

### 2.2 Confirmed candlestick reversal patterns with stop rules, plus RSI 70/30 filter (Elearnmarkets, pp. 278-289, 293-294)

Source file: "Basics of Technical Analysis.pdf" (Elearnmarkets, OCR). Engulfing-bar variant overlaps 2.1: here the engulfing pattern needs confirmation within 2-3 candles, while 2.1 takes the entry on the next bar's break/close without a confirmation window. Partly codable.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal (candlestick pattern + confirmation breakout) | 278-289 |
| Timeframe & holding period | Not found in this text (module charts are daily Nifty/stocks) | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Hammer after a prolonged downtrend; inverted hammer after a sustained down move; shooting star and hanging man after a sustained uptrend; engulfing patterns need a preceding down/up-trend; doji matters after a trending move | 279, 281, 283-285, 289 |
| Setup conditions | Hammer: small body near the top, lower shadow >= 2x body, negligible upper shadow. Shooting star: mirror (upper shadow >= 2x body, small lower shadow). Inverted hammer: small body, upper wick >= 2x body, tiny lower shadow. Hanging man: hammer shape after an up-move. Bullish engulfing: red candle then a blue candle whose body engulfs the first body. Bearish engulfing: mirror. Piercing: second candle closes beyond the halfway mark of the first body but does not engulf. Dark cloud cover: second candle crosses 50% of the first body but does not engulf | 279, 281, 283-288 |
| Entry trigger & order type | After the pattern, wait for confirmation: shooting star confirmed if price moves below its low within the next 2-3 candles; bullish engulfing / piercing confirmed when price passes the high of the two candles within the next 2-3 candles; bearish engulfing confirmed when price moves below the low of the two candles within 2-3 candles; hammer / inverted hammer confirmed when price moves above the candle high (hammer window is garbled in the OCR); hanging man confirmed when price moves below its low. Then take the trade (order type not stated) | 279, 281, 283, 284, 285-288 |
| Initial stop-loss | Longs: below the low of the pattern candle (two-candle patterns: below the low of both candles). Shorts: above the high of the pattern candle (or of both candles) | 279, 281, 283, 284, 286-288 |
| Exits: profit-taking | Not found in this text (the module says candlestick patterns lack the target setup available for classical chart patterns) | 278 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

RSI add-on (same file): a short trade when RSI breaches 70 together with a bearish reversal pattern; a long trade when RSI crosses from below 30 to above with a bullish reversal pattern, each with a stop [p. 294].

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Hammer / shooting star / inverted hammer shadow | >= 2x body | - | 279, 281, 283 |
| Confirmation window | next 2-3 candles | hammer: "next day or ..." (garbled) | 281, 285-288 |
| Piercing / dark cloud penetration | beyond 50% of first body | - | 287-288 |
| RSI period | 14 (default) | can be changed for sensitivity | 293 |
| RSI levels | overbought > 70, oversold < 30 | - | 293-294 |

**Key quotes**

- "Now confirmation of the shooting star pattern comes if the price moves below the low of the candle within the next 2-3 candles." [p. 281]
- "if the highest point of these two candlesticks is breached on the upside within the next 2-3 candles" [p. 285]
- "upon confirmation with a stop-loss below the low of the two candlestick" [p. 286]
- "A hammer like a candle, without validation, has no real significance." [p. 279]
- "it closes crossing the halfway mark of the body of the first candle." [p. 287]
- "breaching the 70 levels and at the same time we spot a bearish reversal pattern" [p. 294]

**Pseudocode**

```
# Bullish engulfing (daily): downtrend ; O1>C1 (red) ; C2>O2 ; O2<=C1 and C2>=O1
setup = engulf_bull(bar[i-1], bar[i])
level = max(H[i-1], H[i]); stop = min(L[i-1], L[i])
for k in 1..3: if H[i+k] > level: buy at level (stop order) ; stop as above ; break
# RSI variant: require RSI14 crossing up through 30 within the same window as the bullish pattern
```

**Ambiguities & assumptions**
- Order type, position size, target, exit are not found in this text: ASSUMPTION: buy-stop at the confirmation level, 1% risk, exit at 2R or on close below stop.
- Hammer confirmation window is garbled in OCR: ASSUMPTION: same 2-3 candles as the other patterns.
- Trend for 'prolonged downtrend' undefined: ASSUMPTION: close < 50-day SMA and 20-day return < 0.
- Bearish patterns (shooting star, hanging man, bearish engulfing, dark cloud) cannot be shorted in the NSE cash market: use as exit signals for longs.
- RSI 'breaches 30 from below to above' timing relative to the pattern is not defined: ASSUMPTION: RSI crossed up through 30 within 3 bars of the pattern.

### 2.3 Support and resistance zone drawing and trading (winningtrade.in, pp. 37-55)

Source file: "How to Trade with Support and Resistance(1)(8).pdf". Partly codable: the zone construction and strength factors are explicit, entries are only sketched.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Support/resistance zone reversal and breakout | 42, 53-54 |
| Timeframe & holding period | Mark levels on the higher timeframe (e.g. weekly) then trade on the lower (daily); the higher the timeframe, the higher the probability | 45 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | In an uptrend, shorting at resistance is low probability; go long at support or on a break of the last high. In a downtrend, do not buy support; short at resistance or on a break of the last swing low | 53-54 |
| Setup conditions | Zone drawing: (1) on a line chart mark the line at the rejections; (2) on the candlestick chart mark the high or low of the candles near that line to form a zone. Zone sources: prior bar high/low, swing highs and lows, congestion areas, rejection areas, flipped levels, gaps, Fibonacci retracements (23.6, 38.2, 50, 61.8, 100%), trend lines and moving averages. Strength: fewer prior tests (first retrace strongest), higher relative volume, strong departure from the zone, little time spent at the zone, large distance travelled before return | 42, 46, 50-52 |
| Entry trigger & order type | Buy at support in an uptrend / short at resistance in a downtrend, or on a breakout beyond the last swing high/low; exact trigger candle or order type not found in this text | 53-54 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text. Break signals: support tends to break in a downtrend and resistance in an uptrend; repeated tests weaken a level; higher lows into resistance usually break out; lower highs into support usually break down; tight consolidation at resistance suggests it will break | 52-55 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fibonacci retracement ratios | 23.6, 38.2, 50, 61.8, 100% | - | 50 |
| Zone width | candle high/low near the rejection line | no number | 42 |
| Number of tests | first retrace strongest; more tests weaken the level | no number | 51-52 |

**Key quotes**

- "Step 1 switch to a line chart and mark the line with the rejections." [p. 42]
- "Step 2 again switch to the candlestick chart, mark the high or low of the candle near the marked line and make the zone" [p. 42]
- "The more times Support or Resistance (SR) is tested, the weaker it becomes and breaks the level" [p. 52]
- "Higher lows into Resistance usually result in a breakout (formed ascending triangle)." [p. 53]
- "Instead, going long at Support is a better trade or break out from last high" [p. 53]

**Pseudocode**

```
swing_hi/lo = pivots(window=ASSUMPTION 5)
zone_top = max(H of bars within 2% of rejection line); zone_bot = min(...)   # ASSUMPTION tolerance
level_strength = 1/(1+n_prior_tests) + vol_ratio_at_zone + departure_size
long if uptrend and low touches zone_bot..zone_top and bullish close ; stop below zone_bot
breakout long if close > last_swing_high
```

**Ambiguities & assumptions**
- No numeric tolerance for 'near the line': ASSUMPTION: 1.0 x ATR(14) or 2%.
- No stops or targets: ASSUMPTION: stop 0.5 ATR beyond the zone; target next opposite zone.
- 'Uptrend' undefined: ASSUMPTION: higher-high/higher-low swing sequence on the daily chart.
- Overlaps with 2.4 (true S/R rules) and 2.9 (zones); kept separate because each defines the zone differently.

### 2.4 SRT Combo: true support/resistance + monthly/weekly/daily + trend-line break (thetradingresource.com, pp. 59-75)

Source file: "Support-and-Resistance-Trading-Strategy-PDF.pdf". Partly codable (the example is a short; stops not specified).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Multi-timeframe level + pattern + trend-line-break entry (reversal/trend-following) | 71-75 |
| Timeframe & holding period | Monthly (level and bias), weekly (confirmation), daily (entry) | 71-74 |
| Universe / eligibility filters | Author says it works for stocks, futures and forex | 75 |
| Market / regime filter | Long-term trend must be confirmed (bearish in the example); short-term daily trend is counter (bullish) before the trend-line break | 75 |
| Setup conditions | Monthly: a TRUE S/R level (see criteria) is broken; price pulls back and the old support becomes resistance; a doji forms at it. Weekly: level still clear, multiple rejections, price fails to break through the new resistance convincingly. Daily: ascending triangle (bearish reversal pattern per author) | 71-74 |
| Entry trigger & order type | Short when the short-term daily trend line is broken (order type not stated). Mirror for longs not shown | 74-75 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Risk:reward 1:2 or 1:3 (1:3 more likely when entry is close to the level); how to derive it is out of scope of the eBook | 74-75 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

True S/R criteria (8): most obvious on the chart; ideally a swing high/low; price slows, shows long-wick rejections and then moves away quickly; has acted as both support and resistance; multiple rejections; recent in time; reaction on two timeframes; narrow zone [p. 62-63]. Indicators for locating levels: moving averages, trend lines, Fibonacci levels, pivot points, RSI key levels [p. 65].

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Timeframes | Monthly / weekly / daily | - | 71 |
| Risk:reward | 1:2 or 1:3 | - | 74-75 |
| Minimum rejections | "multiple" (no number) | - | 63 |
| Zone width | "narrow" (no number) | - | 63 |

**Key quotes**

- "It should ideally be a swing high or swing low" [p. 62]
- "The price should have multiple rejections at this level" [p. 63]
- "We will use three timeframes for our analysis. Monthly , weekly and daily." [p. 71]
- "The break of the short-term trend line gives us the trade entry point." [p. 74]
- "The risk to reward ratio should be 1:2 or 1:3." [p. 74]

**Pseudocode**

```
level = swing level on monthly with >=3 rejections (ASSUMPTION) and both-role history
broken = monthly close beyond level ; pullback_to_level and doji(monthly or weekly)
weekly: failed to reclaim level (close on wrong side) for >= 2 weeks (ASSUMPTION)
daily: short-term trendline (2+ swing highs) ; enter on close beyond trendline
stop = beyond recent swing ; target = entry +/- 2R or 3R
```

**Ambiguities & assumptions**
- Stop not given: ASSUMPTION: beyond the daily swing high/low that formed the pattern.
- 'Multiple rejections', 'narrow', 'recent' have no numbers: ASSUMPTION: >= 3 rejections, zone <= 1.5 ATR(14), within 3 years.
- Only the bearish case is shown. ASSUMPTION: long-side mirror for NSE (shorting not available in cash).
- Chart-pattern labelling on p. 67-69 calls an ascending triangle a bearish reversal; Elearnmarkets (p. 275) treats it as a long on resistance breakout (see 2.11).

### 2.5 Trend-line bounce entry (trend-line guide pp. 78-87; Elearnmarkets pp. 261-266)

Source files: "Guide to trendline trading.pdf" (author not stated) and "Basics of Technical Analysis.pdf". Versions: the guide enters on a reversal candle at the line, ideally where the line meets support/resistance [p. 86-87]; Elearnmarkets buys near the line after it has been validated by a third touch, with a stop-loss below it [p. 261-262].

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback entry | 86-87, 261-263 |
| Timeframe & holding period | Any (day, swing or position trading) | 78 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Trend direction = slope of the trend line (rising = uptrend). A flattening line indicates range conditions; a steepening line indicates stronger trend or buying climax | 84-85 |
| Setup conditions | Draw correctly: focus only on major swing points, connect at least 2, adjust to get the most touches (body or wick). Elearnmarkets: two lows form the line, the third move toward it validates it; more validations means more important. Best opportunities where the trend line coincides with support/resistance | 81, 86, 261-262 |
| Entry trigger & order type | Guide: enter on a reversal candlestick pattern (Hammer, Bullish Engulfing etc.) after price bounces off the line. Elearnmarkets: buy near the line. Downtrend: pullbacks to the line are low-risk shorts | 86-87, 262-263 |
| Initial stop-loss | Elearnmarkets: stop-loss below the line / chart marker; for shorts a little above the line. Guide: only says trading near the line allows a tighter stop | 86, 262-263 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | See 2.7 for the trailing technique | 90 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Swing points to define line | >= 2 major | 3 (Learn price action p. 18: minimum three major points) | 81, 18 |
| Touches for validation | third touch | - | 261 |
| Channel | two parallel lines | - | 83, 265 |

**Key quotes**

- "Connect at least 2 major swing points" [p. 81]
- "Adjust it so that you get the most number of touches (whether it’s body or wick)" [p. 81]
- "you can use reversal candlestick patterns (like the Hammer, Bullish Engulfing, etc.) as your entry trigger." [p. 86]
- "we need two lows to join to form a trendline during an up-move." [p. 261]
- "Pullbacks towards the trend-lines are low-risk points for short selling with a stop loss little above the trend line." [p. 263]

**Pseudocode**

```
pivots = swing lows (window=ASSUMPTION 5); line through two latest higher pivot lows
valid = third touch within tolerance (ASSUMPTION 0.5*ATR14) and no close below line
signal: bullish candle pattern (2.1/2.2) with L within tolerance of line
buy next open / stop above signal high ; stop = line - 0.5*ATR14 (ASSUMPTION) ; line re-fit after break/recovery
```

**Ambiguities & assumptions**
- 'Major swing point' not numerically defined: ASSUMPTION: fractal pivot with 5 bars each side on daily chart.
- No target or position sizing: ASSUMPTION: 2R target or the trailing method in 2.7.
- Line must be 'adjusted' after a break and recovery [p. 83]; no rule for when: ASSUMPTION: refit on each new confirmed pivot.

### 2.6 Trend-line breakout of a pullback (trend-line guide pp. 88-89)

Source file: "Guide to trendline trading.pdf".

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend continuation breakout (pullback entry) | 88-89 |
| Timeframe & holding period | Any | 78 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Existing uptrend (pullback within it) | 88 |
| Setup conditions | Wait for a pullback in an uptrend; draw a trend line connecting the highs of the pullback | 88 |
| Entry trigger & order type | Enter when price breaks the pullback trend line; if it does not, stay out until buyers regain control | 88-89 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | See 2.7 | 90 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Points on pullback line | highs of the pullback (at least 2) | - | 81, 88 |
| Break confirmation | "breaks" (close vs intrabar not stated) | - | 88 |

**Key quotes**

- "Wait for a pullback in an uptrend" [p. 88]
- "Draw a Trend Line connecting the highs of the pullback" [p. 88]
- "If the price breaks the Trend Line, then enter the trade" [p. 88]

**Pseudocode**

```
uptrend = close > SMA50 and higher highs/lows (ASSUMPTION)
pullback = from swing high H_a down to swing low; descending line through >=2 lower highs
buy when close > line_value(today)    # ASSUMPTION: daily close break
stop = pullback low - tick (ASSUMPTION)
```

**Ambiguities & assumptions**
- Intrabar vs close break not stated: ASSUMPTION: daily close.
- Stop and target not found: ASSUMPTION: stop at the pullback low; exit via 2.7.

### 2.7 Riding trends with a trend-line trailing stop (trend-line guide pp. 90-91)

Source file: "Guide to trendline trading.pdf".

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following exit / trailing stop | 90 |
| Timeframe & holding period | Not found in this text (rides "massive trends") | 90 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Does not work well when the trend goes parabolic (trend lines steeper, almost straight; candle ranges larger) | 90-91 |
| Setup conditions | An upward trend line already drawn under price | 90 |
| Entry trigger & order type | Not applicable (exit technique; combine with 2.5/2.6) | - |
| Initial stop-loss | Trail the stop loss below the trend line | 90 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Exit the trade if price closes below the trend line. If parabolic: trail the stop on the current market swing and exit on a close below it | 90-91 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Exit trigger | close below trend line | stop trailed below line | 90 |
| Parabolic flag | steeper lines AND larger candle ranges | no numbers | 91 |

**Key quotes**

- "Trail your stop loss below the Trend Line" [p. 90]
- "Exit the trade if the price closes below the Trend Line" [p. 90]
- "The trend lines get steeper (almost like a straight line)" [p. 91]
- "The range of the candles get larger" [p. 91]

**Pseudocode**

```
each day: line = refit(uptrend line) ; stop = line_value(today) - tick
parabolic = slope(line) > 1.5*slope_at_entry and range_avg(5) > 1.5*range_avg(20)   # ASSUMPTION thresholds
if parabolic: stop = max(stop, last_swing_low)
exit if close < line_value (or < last_swing_low when parabolic)
```

**Ambiguities & assumptions**
- Parabolic thresholds are qualitative: ASSUMPTION: slope >= 1.5x and 5-day average range >= 1.5x the 20-day average.
- 'Current market swing' trailing: ASSUMPTION: most recent confirmed swing low (5-bar fractal).

### 2.8 Trend reversal confirmation after a trend-line break (trend-line guide pp. 92-94)

Source file: "Guide to trendline trading.pdf".

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal (three-step structure) | 92 |
| Timeframe & holding period | Any | 78 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Prior downtrend with a descending trend line | 92 |
| Setup conditions | (1) price breaks above the downward trend line; (2) a higher low forms (sellers exhausted) | 92 |
| Entry trigger & order type | (3) price breaks the swing high: market likely to reverse higher. Conclusion: if a trend line breaks, wait for the re-test and see if it holds | 92, 94 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Steps | 3 (break line, higher low, break swing high) | re-test of the broken line | 92, 94 |

**Key quotes**

- "Wait for the price to break above the Trend Line" [p. 92]
- "Wait for a higher low to form" [p. 92]
- "If the price breaks the swing high, the market is likely to reverse higher" [p. 92]

**Pseudocode**

```
if downtrend and close > line: state = 1
if state==1 and a swing low forms above the prior swing low: state = 2 ; swing_high_ref = highest high since the low before the break
if state==2 and close > swing_high_ref: buy ; stop = higher-low - tick (ASSUMPTION)
```

**Ambiguities & assumptions**
- Which swing high ('the swing high') is not specified: ASSUMPTION: the high between the prior low and the higher low.
- Stop/target not found: ASSUMPTION: stop under the higher low; target 2R.
- Re-test requirement on p. 94 is an alternative; ASSUMPTION: do not require it in the base test, add as a variant.

### 2.9 Supply and demand zone limit-order strategy with three timeframes (Jode Lebin, pp. 123-163)

Source file: "Supply and Demand Zone.pdf" (Trade Like Pro). Written for forex; fully rule-based in the zone drawing, filters, stops and 3:1 reward:risk, but market-structure and 'curve' judgements are visual. Partly codable.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion / reversal at institutional order zones (limit orders), with trend and curve filters | 123-125, 139-150 |
| Timeframe & holding period | Three-timeframe sets by style: Scalping 15m/5m/1m; Day 1h/15m/5m or 4h/1h/15m; Swing Daily/4h/1h or Weekly/Daily/4h; Position Monthly/Weekly/Daily. Roles: highest = curve and major zones; middle = trend; lowest = entry zone drawing and execution | 139, 142 |
| Universe / eligibility filters | Not found in this text (forex pairs) | - |
| Market / regime filter | Higher timeframe: identify trending/reversing/ranging and major zones; price high in the curve near supply: only sell; low in the curve near demand: only buy; at equilibrium (middle) wait for evidence or do nothing. Do not buy high in the curve/near supply; do not sell low in the curve/near demand | 139, 143 |
| Setup conditions | Zone structures: rally-base-drop (supply, reversal), drop-base-rally (demand, reversal), rally-base-rally (demand, in uptrend), drop-base-drop (supply, in downtrend). Base of one to six candles is excellent (demand: fewer than six). Supply zone: top line at top of the basing candles including wicks, bottom line at bottom of the basing candles including only bodies. Demand zone: top line at top of bodies, bottom line at bottom including wicks. Quality filters: fresh level (price never returned: fresh; touched once: non-fresh; more than once: used up, skip); original level (not created by an earlier zone); overlapping zones across or within timeframes; reward:risk of at least 3:1 (2:1 acceptable); base without many candles, without long thin tails, without doji; engulfing candle at retest as confirmation | 127-137, 151-163 |
| Entry trigger & order type | Pending limit order at the zone edge nearest to price: buy limit at the top line of the demand zone; sell limit at the bottom line of the supply zone; wait for price to return. If you miss a trade, do not chase | 149-150, 143 |
| Initial stop-loss | Beyond the far edge: stop loss at the bottom line of the demand zone / top line of the supply zone | 142, 149-150 |
| Exits: profit-taking | Either reward:risk of 3:1, or the opposing supply (for buys) / demand (for sells) zone, closing progressively as the market moves | 142, 149-150 |
| Exits: trailing / time / signal | Trailing stops may be used to secure profits; once set, do not move the stop farther away. If price retests the zone but keeps ranging, wait for an engulfing candle before deciding to keep or close | 163, 166-167 |
| Position sizing | Risk only 1% of capital per trade; risk-per-trade scale: low 1-2%, medium 2-5%, high 5%+ of equity; after consecutive losses halve size or take a break | 123, 167 |
| Adding to / pyramiding | Not found in this text (author says not to open large positions to make up losses) | 167 |
| Portfolio limits (max positions, correlation, heat) | Be aware of correlated pairs (e.g. short EURUSD and long USDCAD double the USD exposure); keep total exposure controlled | 166 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Base candles | 1 to 6 (demand: fewer than 6) | many-candle bases reject | 133, 136, 160 |
| Reward:risk filter | >= 3:1 | 2:1 "also a good ratio"; swing trader 9:1, scalper ~0.8:1 | 158, 168 |
| Freshness | 0 touches = fresh; 1 = non-fresh; >1 = used up | - | 151 |
| Risk per trade | 1% | 1-2% low risk scale | 123, 167 |
| Supply zone lines | top = highest wick of base; bottom = lowest body of base | demand mirrored | 134, 137 |
| Entry price | proximal line (demand top / supply bottom) | - | 149-150 |

**Key quotes**

- "A base with a range of one to six candles is considered an excellent base structure." [p. 133]
- "draw two horizontal lines, one at the top of the basing candles including the tails (wicks)" [p. 134]
- "if the price is near supply zone and high in the curve, we only sell in the market" [p. 139]
- "We place our buy limit order at the top line of the demand zone" [p. 149]
- "if the price has not touched it then the level is fresh, if it did touch it once then the level is non-fresh and if it touched it more than once then the level is called used up" [p. 151]
- "If the market doesn’t give us a 3:1 ratio, we stay away from the trade" [p. 158]
- "Only risk 1% of your capital per trade." [p. 167]

**Pseudocode**

```
# Daily entry timeframe on NSE (long only)
find base: 1..6 consecutive bars with small ranges (ASSUMPTION: range < 0.5*ATR14)
leg_out: next 1-3 bars with range >= 1.5*ATR14 up (DBR or RBR)       # ASSUMPTION
zone_top = max(open,close of base bars) ; zone_bot = min(L of base bars)
fresh = no bar after leg_out has L <= zone_top
curve_ok = close below 50% of the highest-timeframe range (low in curve)
target = max(entry + 3*(entry - zone_bot), nearest opposing supply zone_bot)
rr = (target-entry)/(entry-zone_bot) ; require rr >= 3
place buy limit at zone_top ; stop = zone_bot - tick ; size = 1% equity / (entry - stop)
```

**Ambiguities & assumptions**
- 'Strong drop/rally' and 'small pause' are visual: ASSUMPTION: leg-out candle(s) with range >= 1.5x ATR and base bars with range < 0.5x ATR.
- 'Price in the curve' is a visual cup/hat shape on the highest timeframe: ASSUMPTION: position of close within the trailing 52-week range (< 40% = low, > 60% = high).
- Zone definition contradiction: the supply zone is quoted as 1.13237-1.13874 [p. 124] but the order placed at 1.3237 [p. 125] (typo in the source): ASSUMPTION: follow the line rules on p. 134/137.
- Example at p. 145 sells while 'Trend: uptrend' (high in curve) yet step two on p. 142 does not state a rule that the trend must agree: ASSUMPTION: curve rule overrides, trend not required.
- Stop is exactly the far line with no buffer: ASSUMPTION: 1 tick (or 0.1 ATR) buffer for NSE.
- Both 3:1 reward:risk (p. 142, 158) and an opposing-zone exit (p. 142, 149-150) are given: ASSUMPTION: take profit at the nearer of the two if reward:risk >= 3 holds for the nearer.

### 2.10 Gujral momentum-divergence (stochastic) intraday setup (Stocks & Commodities interview, pp. 237-242)

Source file: "Trading Divergence Interview with Ashwani Gujral.pdf" (Technical Analysis Inc., 2005). Partly codable; designed for 5-minute index charts.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion / divergence (buy dips after an up move, sell rallies after a down move) | 238-239 |
| Timeframe & holding period | 5-minute chart for intraday traders (can time entries on longer frames); 30-minute chart as filter; positions usually not carried home except in extraordinary circumstances or when the market closes at highs | 238, 240 |
| Universe / eligibility filters | Index (S&P 500, Nifty-type index chart; he trades index futures from the index chart). Market breadth also used (not available per instrument) | 238-239 |
| Market / regime filter | Daily ADX above 30: setups work very well and trades go with the trend; when ADX is not showing a strong trend keep volume low and book profits quickly (range-bound: ADX declining below 30, buy at support and sell at resistance, volume 60% of trending volume). 30-minute slow stochastic above 80 and weakening: take only 5-minute sell setups; oversold and strengthening: only buy setups. Breadth: strong positive breadth facilitates buys, strong negative sells, marginal breadth discourages trading | 240-241 |
| Setup conditions | Buy setup: slow stochastic makes a low for the day but the market (price) does not make a new low for the day. Sell setup: slow stochastic makes a high for the day but price does not make a new high. If a strong trend keeps slow stochastic from reaching extremes, fast stochastic can be used (fast stochastic overbought and price above the 20-period EMA gives a low-risk short). If stochastic rises and price also makes a new high, stop looking for the sell setup | 238-239, 241 |
| Entry trigger & order type | Triggers: previous two-bar low (for sells) / high (for buys) on the five-minute chart, or price going through the 20-period EMA in the direction of the trade; sidebar: previous 10-minute lows, breakdown/breakout through the 20-period MA, or entering as the extreme is reached with a standard stop. Preferably as slow stochastic comes down from 80 or moves up above 20 | 240-241 |
| Initial stop-loss | The high of the day for a sell setup; the low of the day for a buy setup | 239, 241 |
| Exits: profit-taking | Book profit at the next opposite setup (buy setup exits at the next sell setup). In range-bound markets take quicker profits, preferably as slow stochastic reaches the other end | 240-241 |
| Exits: trailing / time / signal | If breadth weakens while long, tighten stops; breadth near 1-to-1 means take profits quickly; when a trend starts stalling, get out | 240, 242 |
| Position sizing | Not more than 2% of total account equity at risk on any one trade; range-bound market volume 60% of trending volume | 238, 240 |
| Adding to / pyramiding | Once a position is deep in the money, look for consolidations (bull/bear flags) to add; every addition is a fraction of the original position so break-even does not run up near the market | 238 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text (trades one index; sells index straddles in choppy markets) | 238 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry timeframe | 5-minute | longer frames possible | 238 |
| Filter timeframe | 30-minute slow stochastic | - | 240 |
| Stochastic levels | overbought above 80 / oversold below 20 (given for the 30-minute filter) | - | 240 |
| Stochastic periods | Not found in this text | - | - |
| Moving average | 20-period EMA | "20-period moving average" | 239, 241 |
| Daily ADX | > 30 trend; < 30 range | ADX period not stated | 240-241 |
| Risk per trade | <= 2% of equity | - | 238 |
| Range-market size | 60% of trending size | - | 240 |

**Key quotes**

- "I do not risk more than 2% of total account equity on any one trade." [p. 238]
- "Now, the buy setup means the momentum makes a low for the day, whereas the price does not." [p. 238]
- "you use the high of the day as your stop, for the sell setup" [p. 239]
- "How do you book a profit? You wait until the next opposite setup occurs again." [p. 240]
- "If it’s above 30, these setups work very well." [p. 240]
- "In a trending market, when ADX>30, take trades only in the direction of the trend" [p. 241]

**Pseudocode** (needs intraday bars)

```
slow = stochastic_slow(ASSUMPTION 14,3,3) on 5m ; fast = stochastic_fast(ASSUMPTION 14,3)
buy_setup: slow made day-low (slow == min(slow today)) AND low_of_day not new vs prior day-low reference
sell_setup mirror
filter: ADX_daily > 30 (trade only with trend) ; 30m slow stoch > 80 -> sells only, < 20 -> buys only
trigger_short: low < min(low[1], low[2]) or close crosses below EMA20 ; stop = high_of_day
exit: next opposite setup ; risk 2% max
```

**Ambiguities & assumptions**
- Stochastic and ADX periods not found in this text: ASSUMPTION: slow 14/3/3, fast 14/1, ADX 14.
- 'The market does not make a new low for the day' is relative to the earlier low: ASSUMPTION: the price low at the time of the indicator low is higher than the day's earlier price low (classic divergence).
- Two versions of the trigger (two-bar high/low p. 240; 10-minute lows p. 241): ASSUMPTION: use the previous two-bar high/low as the primary and the EMA20 breakout as the variant.
- Stop at the day's high/low can be very wide in India; ASSUMPTION: cap by 2% equity sizing.
- Not testable on our daily data: needs intraday OHLCV and breadth.

### 2.11 Classical chart patterns: head and shoulders, double/triple tops and bottoms, triangles (Elearnmarkets pp. 269-277; cross-checked with pp. 67-69, 53)

Source file: "Basics of Technical Analysis.pdf". Head-and-shoulders and triple patterns have explicit stop/target rules; the others are descriptive. Versions on triangles conflict (see Ambiguities). Partly codable.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal and continuation patterns (breakout of neckline / boundary) | 269-277 |
| Timeframe & holding period | Triangles last a couple of weeks (ideally more than 12 weeks) to several months; flags and pennants one to three weeks (can last 1-12 weeks); wedges usually three to six months | 274, 276-277 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Head and shoulders after an uptrend (bearish); inverse head and shoulders after a sustained downtrend; double/triple patterns after a sustained trend; triangles generally continuation | 270-272, 274 |
| Setup conditions | H&S: head higher than two shoulders, neckline through the troughs. Double/triple top or bottom: level tested two or three times without a break. Ascending triangle: flat resistance with rising lows; descending triangle: flat support with falling highs; symmetrical triangle | 270-275 |
| Entry trigger & order type | H&S: short on an ultimate break below the neckline. Inverse H&S: mirror long on neckline break. Triple top/bottom: entry at the break of the neckline. Ascending triangle: enter long on a breakout of the resistance; descending triangle: short on break below support | 270-272, 275 |
| Initial stop-loss | H&S: above the top of the nearest shoulder (inverse: mirror). Triple top/bottom: a small stop-loss | 270-272 |
| Exits: profit-taking | H&S: distance between neckline and head, projected from the break point. Triple: distance between the peaks/troughs and the neckline. Volume: higher volume on the right-shoulder down leg and on the breakout means higher conviction | 270, 272 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| H&S target | head-to-neckline distance from break | - | 270 |
| H&S stop | above nearer shoulder top | - | 270 |
| Triple target | peak-to-neckline distance | - | 272 |
| Triangle duration | > 12 weeks ideal | a couple of weeks to months | 274 |
| Flag duration | 1-3 weeks | up to 12 weeks | 276 |
| Wedge duration | 3-6 months | - | 277 |

**Key quotes**

- "ultimate break below the neckline, usually, a short trade is taken with a" [p. 270]
- "The target is usually considered as the distance between the neckline and head, projected from the point of break." [p. 270]
- "Trade entry is initiated at the break of a neckline with a small stop-loss and the target is measured as the distance between peaks/troughs and the neckline." [p. 272]
- "Traders will enter into a long position on a breakout of the resistance" [p. 275]
- "Higher lows into Resistance usually result in a breakout (formed ascending triangle)." [p. 53]

**Pseudocode**

```
# Inverse H&S (long): 3 troughs L1,H(lowest),L2 with H < L1,L2 ; neckline = line through the two intervening highs
signal: close > neckline (after sustained downtrend)
stop = min(L1,L2 shoulder low) - tick ; target = neckline_at_break + (neckline_at_head - head_low)
```

**Ambiguities & assumptions**
- Pattern detection needs numeric tolerances not given: ASSUMPTION: shoulders within 15% of each other in height, pivots from 5-bar fractals, minimum 20 bars between shoulders.
- Triangle direction conflict: Elearnmarkets p. 275 trades the ascending triangle as a long breakout; the SRT eBook p. 68 labels it a bearish reversal pattern in an uptrend, and the SRT trade summary uses it as a short bias [p. 74-75]; winningtrade says higher lows into resistance usually break out [p. 53]. ASSUMPTION: follow the majority (two files): long on breakout of the flat top.
- No stop/target for triangles, double tops/bottoms, flags, wedges: ASSUMPTION: stop at the opposite pattern boundary, target = pattern height projected from breakout (not in text).
- Double top/bottom and triangle entries are only described qualitatively: treat as 'Partly codable'.

### 2.12 Breakout with volume confirmation and retest entry (Breakouts & Breakdowns, 14 Multi Year Breakouts, 40 Trading Cheatcodes)

Source files: "Breakouts & Breakdowns.pdf" (author not stated, NSE charts) pp. 191-200; "14 Multi Year Breakouts.pdf" (@ADX_Learner) p. 201; "40 Trading Cheatcodes.pdf" p. 353; price-volume table also in Elearnmarkets pp. 266-268. Partly codable; no stops, targets or numeric volume multiple.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout / breakdown with retest | 191-194, 201 |
| Timeframe & holding period | Not found in this text (examples: Nifty 15-minute, weekly stocks, monthly multi-year charts) | 195, 199-200, 204 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Flat 200 EMA on higher timeframes = directionless market; avoid trading around earnings; first 30 minutes of the market is noise | 353 |
| Setup conditions | Breakout = price breaches resistance; breakdown = price falls below support. Level for a zone: highest line of a resistance zone is the breakout level, lowest line of a support zone is the breakdown level. Strong breakout: large volume (volume breakout) or significant time spent near the level (follows consolidation). Weak: gap up/gap down breakouts and low-volume breakouts. A retracement of more than 50% means the trend is highly likely to reverse or pause | 191, 193, 199-200 |
| Entry trigger & order type | Three entry points A, B, C are shown for breakout traders (picture only). Retest: previously broken support re-tested as resistance or vice versa. ADX_Learner: best to buy near the retest, or buy if RR is favourable, do not rush. Cheatcodes: first pullback after a breakout is the safest entry (item 11) versus breakouts without retests are real, do not always wait (item 35) | 192, 194, 201, 353 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

Volume rules: higher-than-average volume during a breakout confirms it; volume divergence warns of a false breakout [p. 197]. Price/volume table: rising price + rising volume = increasing demand, bullish; rising price + falling volume = decreasing demand, bearish; falling price + rising volume = increasing supply, bearish; falling price + falling volume = decreasing supply, bullish [p. 198]. Cheatcodes: do not trust the breakout if the candle closes with a long wick (item 36) [p. 353]. Volume levels are relative to the average over certain periods [p. 267]; delivery % with a price rise signals conviction [p. 268].

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Volume threshold | "higher than average" (no multiple) | volume average over certain periods (Volume(20) on chart) | 197, 267 |
| Retracement reversal | > 50% | - | 193 |
| Breakout level | top of resistance zone | - | 193 |
| ADX on monthly chart | ADX(8,13,25) displayed | no rule | 204 |

**Key quotes**

- "Strong breakouts are accompanied with large volumes, therefore they are also called volume breakouts." [p. 193]
- "Breakout / breakdown due to gap up/gap down are weak ones." [p. 193]
- "Best way to trade breakout to buy near retest or buy if RR is favourable." [p. 201]
- "The first pullback after a breakout is the safest entry." [p. 353]
- "Breakouts without retests are real — don’t always wait." [p. 353]
- "Don’t trust the breakout if the candle closes with a long wick." [p. 353]

**Pseudocode**

```
res = top of resistance zone (2.3 zone) ; breakout day: close > res and volume > 2.0*avgvol20 (ASSUMPTION)
reject if gap_up (open > res*1.01) or upper_wick > 50% of range (ASSUMPTION)
retest: first pullback with low <= res*1.01 within 20 days (ASSUMPTION) -> buy on close back above res
variant B: buy next day open after breakout
stop = below retest low ; exit = 2R or close below res
```

**Ambiguities & assumptions**
- No volume multiple, no definition of 'significant time near the level': ASSUMPTION: volume >= 2x 20-day average; >= 10 bars within 3% of the level.
- Retest-versus-no-retest contradiction between items 11 and 35 [p. 353] and the multi-year advice [p. 201]: ASSUMPTION: backtest both variants separately.
- A and B and C entry points are shown as a diagram only [p. 192]: not recoverable from the text.
- 'Multi-year breakout' stocks are chart images only [p. 201-205]; no numeric definition (lookback, RR): ASSUMPTION: close above the highest monthly close of the prior 36 months.

### 2.13 Moving average, RSI and ADX trend settings (Elearnmarkets, pp. 290-295)

Source file: "Basics of Technical Analysis.pdf". Indicator definitions and thresholds, no standalone entry/stop/target system. Partly codable as filters.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend filter / signal indicators | 291-295 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | ADX above 20 or 25: trending phase (up or down); +DI crossing above -DI: upward; -DI above +DI: downward. Medium-term MA with positive slope: positive medium-term trend | 292, 295 |
| Setup conditions | SMA periods: short 5, 8, 13; medium 20, 34, 50; long 100, 200. Example chart plots SMA 8, 50, 200. RSI default 14, overbought above 70, oversold below 30 (RSI formula 100 - 100/(1+RS)). ADX chart uses DI(14,14) | 291-293, 295 |
| Entry trigger & order type | Price breaching an MA from down to up is bullish; closing above/below an MA from the upside/below is bullish/bearish; a shorter-term MA crossing above a medium-term MA is a bullish crossover, below it a bearish crossover (signal of bullishness/bearishness). Order type not stated | 292 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Reverse crossover (implied) | 292 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| SMA periods | 5/8/13, 20/34/50, 100/200 | trader's choice | 291 |
| RSI period / levels | 14 / 70, 30 | period changeable | 293 |
| ADX trending threshold | 20 or 25 | - | 295 |
| DI period | 14 | chart label | 295 |

**Key quotes**

- "For shorter-term SMA, we can use 5,8,13, etc. For Medium term 20, 34, 50, and for longer-term 100,200 can be used." [p. 291]
- "If a medium-term moving average is having a positive slope, the trend is considered to be positive in the medium-term" [p. 292]
- "The default setting for the Relative Strength Index is 14" [p. 293]
- "When ADx is above 20 or 25, generally the market is considered to be in" [p. 295]

**Pseudocode**

```
bull_x = SMA(8) crosses above SMA(50) ; trend_ok = ADX14 > 25 and +DI > -DI
long when bull_x and trend_ok ; exit when SMA(8) crosses below SMA(50)    # exit rule is ASSUMPTION
```

**Ambiguities & assumptions**
- No complete system; pairings (8/50, 50/200) are only the plotted example: ASSUMPTION: test 8/50 and 50/200.
- ADX 20 vs 25 not resolved: ASSUMPTION: 25.
- Stops and exits not found: ASSUMPTION: crossover reversal exit and 2 ATR stop.

### 2.14 Pivot point levels (Pivot Points Calculations, p. 354)

Source file: "Pivot Points Calculations.pdf" (author not stated). Indicator only: a formula to project the next period's support/resistance. Fully codable as an indicator, no trade rule.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Support/resistance level calculation | 354 |
| Timeframe & holding period | Daily, weekly and monthly pivots from the data of the current period used for the next period | 354 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Pivot Point = (High + Low + 2 x Close) / 4; Pivot High = 2 x PP - Low; Pivot Low = 2 x PP - High | 354 |
| Entry trigger & order type | Not found in this text; author only says show patience and wait until the market shows it is ready, and use pivots to identify resistance and support | 354 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| PP | (H + L + 2C)/4 | - | 354 |
| Upper level | 2 x PP - L | - | 354 |
| Lower level | 2 x PP - H | - | 354 |
| Periods | daily, weekly, monthly | - | 354 |

**Key quotes**

- "(High+ Low +2 x Close)/4 = Pivot Point" [p. 354]
- "Pivot Point x 2 - Low = Pivot High" [p. 354]
- "Pivot Point x 2 - High = Pivot Low" [p. 354]
- "I use them for daily , weekly and monthly." [p. 354]

**Pseudocode**

```
PP = (H + L + 2*C)/4 on prior day/week/month bar
R1 = 2*PP - L ; S1 = 2*PP - H
use as reaction levels (e.g. buy bounce at S1 with a candle trigger from 2.1) # entry is ASSUMPTION
```

**Ambiguities & assumptions**
- The formula differs from the standard (H+L+C)/3 pivot; implement as written: (H+L+2C)/4.
- Names 'Pivot High/Low' are the first resistance/support only; further levels not given.
- No entry or exit rule: ASSUMPTION: use as targets/zone anchors in 2.3.

## 3. Risk & money-management rules

- Lebin: risk only 1% of capital per trade; scale low risk 1-2%, medium 2-5%, high 5% or more of equity [p. 123, 167].
- Lebin: after consecutive losses cut size by 50% or take a break; do not open larger positions to make up losses [p. 167].
- Lebin: do not move the stop farther away once set; set and forget; always use a stop loss [p. 166-167].
- Lebin: reward:risk filter of 3:1 (2:1 acceptable); swing 9:1, scalper about 0.8:1 [p. 158, 168]. Watch correlated positions [p. 166].
- Gujral: no more than 2% of account equity per trade; do not carry losses home; no marginal profits overnight; add in fractions of the original position; range-bound volume 60% of trending [p. 238, 240].
- LearnPriceAction: always use a stop loss, test strategies on demo first; stops adapt to volatility [p. 20].
- Cheatcodes: never hold intraday trades overnight; the closer to the stop, the calmer; if you cannot sleep with the trade on you are overleveraged; avoid revenge trades [p. 353].
- SRT eBook: use risk:reward 1:2 or 1:3 [p. 74].
- Elearnmarkets: maintain a stop-loss when buying near a trend line [p. 262].

## 4. Non-codable guidance

Triage of every file (codable = has at least one rule set written up in section 2):

| File | Pages | Triage | Why / where |
|---|---|---|---|
| Learn price action(1).pdf | 1-20 | Codable (partly) | 2.1 pin bar / engulfing / inside bar; also stop styles |
| Price Action Analysis in Trading(1)(8).pdf | 21-36 | Not codable | Candle-reading heuristics only (body size, wick length, Wyckoff effort vs result, two- and three-bar expectations); no entry, stop, target or numbers [p. 21-34]. |
| How to Trade with Support and Resistance(1)(8).pdf | 37-55 | Codable (partly) | 2.3 zone construction and break rules |
| Support-and-Resistance-Trading-Strategy-PDF.pdf | 56-76 | Codable (partly) | 2.4 SRT Combo; chart-pattern pictures pp. 67-69 labels only |
| Guide to trendline trading.pdf | 77-94 | Codable (partly) | 2.5-2.8 |
| Supply and Demand Zone.pdf | 95-170 | Codable (partly) | 2.9; chapters 1-3 and 6 are forex/economics background [p. 100-120, 169-170] |
| P.O.3 patterns.pdf | 171-186 | Not codable | Smart-money-concept patterns (P1, P2, P3 points, FVG, strong/weak highs, CHoCH, liquidity) are discretionary and carry no stop, target or numbers; entry is 'lower timeframe confirmation you personally use' [p. 172-176]. |
| Breakouts & Breakdowns.pdf | 187-200 | Codable (partly) | 2.12 (qualitative only); accumulation/distribution intro p. 188 |
| 14 Multi Year Breakouts.pdf | 201-205 | Not codable on its own | 14 chart images with one sentence of advice [p. 201]; merged into 2.12 |
| RSI 73 v1.pdf | 206-214 | Not codable | Tradetron backtest report only; the strategy rules (RSI levels, entries, exits) are absent. Stats: capital Rs. 25000, 614 trading days, win rate 45.11%, total ROI 400.80%, Sharpe 0.97, max drawdown -33.88%, avg 9.57 trades per day, 1-minute intraday [p. 206-207]. 'Not found in this text': any RSI level. |
| neo wave patterns 206.pdf | 215-236 | Not codable | Elliott/NEoWave pattern descriptions (diametric, neutral, extracting triangles, terminals) with no entry, stop or target; only qualitative timing notes such as wave-C taking about half of A+B [p. 228]. |
| Trading Divergence Interview with Ashwani Gujral.pdf | 237-242 | Codable (partly) | 2.10 (intraday) |
| How to see charts in multiple ways.pdf | 243-248 | Not codable | A series of rhetorical questions over monthly/weekly/daily/hourly charts; only a note that retracement was about 70% [p. 245]. |
| Basics of Technical Analysis.pdf | 249-299 | Codable (partly) | 2.2, 2.5 (trend lines), 2.11, 2.13; chart types, trends, volume are definitions [p. 252-268] |
| Start Buying Stock For Beginners.pdf | 300-352 | Not codable | US buy-and-hold beginner guide: budgeting 50/30/20, index funds, dividends, brokers; no technical or screening rules [p. 305-351]. |
| 40 Trading Cheatcodes.pdf | 353 | Partly (folded in 2.12) | One-line heuristics; text truncated mid-word at item 40 [p. 353]. |
| Pivot Points Calculations.pdf | 354 | Codable (indicator only) | 2.14 |

Discretionary or psychological guidance (not testable):
- Price-action reading depends on context: a candle must be analysed against previous candles; a cluster of wicks vs a single long wick has different meaning [p. 22, 32].
- Support/resistance as order-flow psychology (longs, shorts and uncommitted buying the dip) [p. 39-40].
- Choose a trading style that fits personality; do not change systems at the first sign of trouble [p. 121-122].
- Keep a trading journal; write a trading plan [p. 122-123].
- Do not predict the market; react; trade less and watch more [p. 353].
- Gujral: have a perspective of the daily trend and draw support/resistance before planning the day's trade [p. 242].
- Stops hit by a pin bar failure are information, not a failure of the trader [p. 18].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily OHLCV for all of 2.1-2.9, 2.11-2.14 (open, high, low, close, volume); delivery % is optional (mentioned on p. 268); weekly and monthly bars derived from daily; index history (NIFTYBEES proxy before 2024) for trend regime; intraday 5-minute and 30-minute OHLCV plus market breadth for 2.10 (not in our data).
- **Testability with our data:** 2.1, 2.2, 2.3, 2.4, 2.5-2.8, 2.9, 2.11, 2.12, 2.13, 2.14 can be backtested on 2005-2026 daily prices (long side only), though zone/pattern detection needs the coded ASSUMPTION tolerances. 2.10 (5-minute stochastic divergence, breadth) needs intraday data we do not have; a daily-bar analogue (daily slow stochastic divergence vs 20-day price low) is an ASSUMPTION, not the author's rule. No fundamentals are used by any of these files.
- **Market-structure differences:**
  - Forex methods (2.1, 2.4, 2.9) use 24-hour markets and pips; in NSE use daily gaps and ATR instead. ASSUMPTION: treat the open as a gap risk; limit orders fill at the open if gapped through.
  - No overnight shorting in the cash market: bearish patterns (shooting star, hanging man, dark cloud, bearish engulfing, descending triangle, supply-zone shorts) can only serve as exits or filters. ASSUMPTION: long-only testing; test shorts separately as futures/synthetic only if wanted.
  - Circuit limits: breakouts/gaps (2.12) can lock; skip signals on days where the stock is at a circuit limit. ASSUMPTION: exclude bars with high==low==close at circuit.
  - Costs: STT, brokerage and about 0.1% slippage; stop-limit distances below about 0.5% are unrealistic. ASSUMPTION: apply 0.1% slippage each side and discard trades with stop distance < 1%.
  - Small-cap liquidity: ASSUMPTION: require average traded value >= Rs. 5 crore and price >= Rs. 20 (not in the sources).

## 6. Verdict

- **Codeability:** Partly. Most files are descriptive primers; rule sets with real numbers are limited to 2.1 (pin bar ratios), 2.2 (candle patterns with 2-3 bar confirmation), 2.9 (zone drawing, 3:1) and 2.14 (pivot formula). Entry, stop and exit are discretionary or missing in the others.
- **Priority for backtesting:** Low-Medium. Candidate worth testing: 2.9 supply-demand zones (daily, long-only) and 2.12 volume breakout with retest, because their zone/level definitions are objective once tolerances are fixed; the rest are generic patterns with weak evidence (no author results besides an unreproducible Tradetron report).
- **Top 3 things a coder is most likely to get wrong:**
  1. Zone geometry in 2.9: supply uses wicks on the far edge and bodies on the near edge (demand mirrored), the entry is the near edge, the stop the far edge; and 'fresh' means zero touches since the leg-out [p. 134, 137, 149-151].
  2. Confirmation windows and stops of the candle patterns in 2.2: the trade only triggers after a break of the pattern high/low within 2-3 candles and the stop is beyond the whole one- or two-candle pattern, not the signal candle alone [p. 281, 285-288].
  3. Treating files that only look like systems as rules: the RSI 73 report [p. 206-207], the P.O.3 patterns [p. 172-176] and the 14 multi-year breakouts [p. 201] have no codable entry/exit and must not be given invented parameters.
