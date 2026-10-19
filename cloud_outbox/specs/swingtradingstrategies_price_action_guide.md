# Price Action Trading Guide — swing-trading-strategies.com (no personal author name given in the text)

- **Source file:** Google Drive "Price action trading guide.pdf" (128 pages, 4.0 MB). A second copy, "Price-Action-Trading-Guide.pdf" (7.7 MB), could not be downloaded (over the connector limit). It may be the same book or a different edition; this spec was NOT checked against it. Copyright line in the text: "Copyright 2014 © www.swing-trading-strategies.com"; the author writes in first person and gives no personal name anywhere in the text (a date of 5 Dec 2014 appears at [p. 120]).
- **Text file used:** text/swingtradingstrategies_price_action_guide.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/<key>.md text/<key>.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read the whole text file, lines 1-3114, in sequential chunks, from [[PAGE 1]] to the last marker [[PAGE 128]]. Nothing was skimmed. Short pages: 1, 69, 71, 108, 118, 128. Pages 1 and 128 contain only the copyright footer; page 3 is a legal disclaimer; page 2 is the table of contents. Charts are images and are NOT in the text; the pages with almost no text (3 or fewer content lines: 1, 34, 54, 59, 69, 71, 75, 108, 109, 118, 128) are essentially chart-only, and many other pages are partly chart. Where the text says "as shown on the chart below" the rule is therefore not recoverable (for example the "3 ways" to place a triangle stop-loss at [p. 58] is image-only). *Coordinator check: the extraction agent wrote and verified the full spec, then hit the weekly usage limit before sending its final report. Its notes end 'spec complete, verified', and the coordinator confirmed the spec has sections 1-6 and 13 strategies. The coordinator re-ran verify_citations (52/52 ok) and an exact-page strict check (0 off-by-one), and confirmed all 13 field tables have exactly the 12 template rows. 9 unquoted citations were spot-checked by grep: 'intercepted' trend end p.33, 2% risk p.8/119, half off mid-channel p.51, triangle 'two peaks' p.55 and close outside p.57, railway tracks p.86-87, Fibonacci 50/61.8 p.93-96, risk-reward p.116, confluence p.110-114; all matched.*

## 1. The method in brief

A discretionary, "naked chart" price-action method written mainly for forex (pips, MetaTrader 4, a forex news calendar), but the author states the concepts apply to any market [p. 12]. It reads trend from swing structure (higher highs/higher lows vs lower highs/lower lows, per Dow theory) [p. 32-33], and then trades pullbacks (buy on the downswing in an uptrend, sell on the upswing in a downtrend) [p. 43] at obvious levels (horizontal support/resistance, flipped levels, channel edges, trendlines, 50%/61.8% Fibonacci retracements, moving averages used only as dynamic support/resistance) once a reversal candlestick or chart-pattern signal appears there [p. 45-48, 93-96, 98-107]. The claimed edge is mass psychology: many traders watch the same levels and patterns, so "trade the obvious" and stack several factors into a "confluence" [p. 15-16, 110, 124-126]. Larger timeframes (monthly/weekly/daily) define the setup and a smaller timeframe (1hr, 4hr, even 5min) is used only to time the entry and shrink the stop [p. 46, 116-119].

There is no systematic evidence. The book gives no win rate, no backtest and no equity curve. Evidence is a handful of hand-picked chart anecdotes (a NZDUSD 1,100-pip move [p. 46]; one confluence trade, 138 pips and 125 pips [p. 112-113]; one losing trendline trade [p. 100]). Almost every rule is described qualitatively, with no numeric thresholds for swings, candle shapes, "close to" a level, or stop distances. All numeric parameters below are therefore marked ASSUMPTION unless the text states them. The book is a teaching text, not a rule-book, so it is only "Partly" codable.

## 2. Strategies

Conventions used in all subsections: "Daily bars" is our data. The book is largely about forex and intraday entries; where the book's rule needs an intraday chart, the daily-bar adaptation is flagged. The book gives no numeric definition of a swing high/low; one shared ASSUMPTION is made (see 2.1 Pseudocode) and re-used by all other strategies.

### 2.1 Trend structure + swing pullback entry (buy the downswing in an uptrend)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback. Entry on a reversal candlestick at a support/resistance level inside the trend. | 43 |
| Timeframe & holding period | Setups from monthly/weekly/daily/4hr; entries from lower timeframes. Swing-trade holding ("it may be a week or two before the profit target is hit" for a daily-chart setup). No fixed holding period. | 100, 119 |
| Universe / eligibility filters | Not found in this text (written for forex; says concepts apply to any market). Avoid entries just before major scheduled news. | 12, 8 |
| Market / regime filter | Trend from price structure only: uptrend = higher highs + higher lows; downtrend = lower highs + lower lows; sideways = range between support and resistance. "You only need to use price action to tell you if a trend is up, down or sideways." A trend ends when a higher low (uptrend) or lower high (downtrend) is intercepted/broken. Do not buy in a downtrend or sell in an uptrend (exception: channels). | 32, 33, 35, 39 |
| Setup conditions | Uptrend present; price makes a downswing (pullback) into support (or Fibonacci level); do not buy near/at resistance. | 39, 43, 37 |
| Entry trigger & order type | A bullish reversal candlestick on the pullback (e.g. at support). Order type not stated for this setup (elsewhere: pending buy-stop above the signal candle, see 2.8). | 43 |
| Initial stop-loss | Not found in this text for this setup (stop is "large" if you buy at the wrong spot in the swing; size position by stop distance). | 42 |
| Exits: profit-taking | Not found in this text for this setup (generic: previous swing high/resistance used elsewhere). | - |
| Exits: trailing / time / signal | Trend-break exit: a higher low being intercepted signals end of uptrend. No trailing rule for this setup. | 33 |
| Position sizing | "Large stop loss does not necessarily mean large risk if you do position sizing based on the stop loss distance." | 42 |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Swing high/low definition | Not stated (described as peaks and troughs; drawn on chart) | - | 45 |
| Number of swings to call a trend | Not stated (Dow: HH+HL for up, LH+LL for down) | - | 33 |
| Min swing size / ATR filter | Not stated | - | - |
| Signal candle types | "reversal candlesticks" (see 2.8) | - | 43 |
| Stop distance | Not stated | - | - |
| Target / R:R | Not stated | - | - |

**Key quotes**
- "and higher lows until a higher low gets intercepted" [p. 33]
- "And you only need to use price action to tell you if a trend is up, down or" [p. 32]
- "you should be looking to buy on the downswing" [p. 43]
- "buying near or at a resistance level" [p. 39]
- "Large stop loss does not necessarily mean large risk if you do position" [p. 42]

**Pseudocode** (shared helper definitions are used by 2.2-2.13)
```
# SHARED HELPERS (ASSUMPTION: N = 3 bars each side; book gives no numeric rule)
swing_high(i)  = high[i] == max(high[i-N .. i+N])      # confirmed N bars later
swing_low(i)   = low[i]  == min(low[i-N .. i+N])
H1,H2 = last two confirmed swing highs; L1,L2 = last two confirmed swing lows (H2,L2 newer)
UPTREND   = (H2 > H1) and (L2 > L1)
DOWNTREND = (H2 < H1) and (L2 < L1)
SIDEWAYS  = otherwise
trend_broken_up   = close < L2        # ASSUMPTION: a close below the latest higher low = "intercepted"
trend_broken_down = close > H2
bull_reversal(bar) = any of: hammer, bullish engulfing, bullish harami, piercing line, dragonfly doji,
                     bullish railway track (definitions: 2.8)
at_support(bar)    = low[bar] within TOL of a horizontal support level (2.2)  # TOL = ASSUMPTION 0.5 * ATR(14)

# STRATEGY 2.1 (long side only for NSE cash)
for each stock, each day t (after close):
    if UPTREND and not trend_broken_up and last_bar_is_downswing (close[t] < close[t-1] or price below last swing high):
        if at_support(t) and bull_reversal(t) and not near_resistance(t):
            place BUY stop at high[t] (+tick) for day t+1, valid 1 day     # ASSUMPTION (book silent)
            stop = low[t] - tick                                           # ASSUMPTION
            target = H2 (last swing high)                                  # ASSUMPTION
            qty = risk_amount / (entry - stop)
exit: stop hit, target hit, or trend_broken_up
```

**Ambiguities & assumptions**
- Swing definition missing: ASSUMPTION: fractal N=3 on daily bars (also test N=2, 5).
- "Intercepted" is not defined (touch vs close beyond; wick vs body). ASSUMPTION: daily close beyond the swing point.
- Stop, target and order type for this generic setup are not found in this book; ASSUMPTION: stop below signal-candle low, target previous swing high, buy-stop above signal-candle high.
- Short side is described symmetrically [p. 43] but NSE cash has no overnight shorting. ASSUMPTION: long-only; use downtrend signals as exit/avoid filters.
- Whether "downswing" requires a minimum depth or number of down bars is not stated.

### 2.2 Support / resistance reversal (horizontal levels, flipped levels, dynamic levels)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion at a level, usually with the trend (pullback). Support/resistance trading is "the core of price action trading". | 44 |
| Timeframe & holding period | Significant levels come from monthly, weekly, daily charts; entry timeframe 4hr/1hr/30/15/5min. Holding period not stated. | 46 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Flipped levels: in a downtrend broken support acts as resistance (sell); in an uptrend broken resistance acts as support (buy). Do not sell near support or buy near resistance. | 47-48, 39 |
| Setup conditions | Horizontal support: price fell, hit a level and bounced up; resistance: price rose, hit a level and reversed. When price returns, "expect that it will get rejected from that level again". Significant = formed on large timeframes. Levels weaken: after about 2-3 tests "expect a breakout of the level". | 45, 46, 127 |
| Entry trigger & order type | Reversal candlestick at the level (bullish at support/flipped resistance, bearish at resistance/flipped support). Order type not stated here. | 45, 47, 48 |
| Initial stop-loss | Not found in this text for this setup (generic: stop on the far side of the level / rejection candle in 2.3). | - |
| Exits: profit-taking | Not found in this text for this setup (price runs to "the next significant support level" in the NZDUSD example). | 46 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | See Section 3. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Level formation timeframe | monthly, weekly, daily = "significant" | - | 46 |
| Min touches to validate a level | Not stated (price "bounces" at least once) | - | 45 |
| Touches before expected break | 2-3 on average | - | 127 |
| Zone width / tolerance | Not stated ("level or zone") | - | 45 |

**Key quotes**
- "large timeframes like the monthly, weekly and daily charts" [p. 46]
- "So when price heads back to that support or resistance level, you should expect" [p. 45]
- "So when you see such happening, you should be looking for bearish reversal" [p. 47]
- "From my observations, 2-3 times is the average," [p. 127]

**Pseudocode**
```
levels = cluster(swing_highs + swing_lows, tol=TOL)       # ASSUMPTION: cluster within 0.5*ATR(14)
level.strength = touches; level is SIGNIFICANT if formed on weekly/monthly or visible on daily  # ASSUMPTION daily min
flip: if close breaks support by > TOL then support becomes resistance (and vice versa)
long: price within TOL of support or flipped-resistance-turned-support, UPTREND (2.1), bull_reversal(bar)
      and level.tests_so_far <= 3                          # ASSUMPTION from p.127 "2-3 times"
      entry = buy stop above signal high; stop = min(signal low, level - TOL)   # ASSUMPTION
      target = next resistance above
```

**Ambiguities & assumptions**
- "Expect a breakout after 2-3 tests" is an observation, not a filter. ASSUMPTION: skip level if already tested more than 3 times.
- Zone width, how a level is "broken" (close vs wick), and how many weekly/monthly levels to keep: not stated. ASSUMPTION: close beyond level by 0.5 ATR = broken.
- Stop and target for this setup not found in this book; ASSUMPTION as above.
- Dynamic support/resistance is covered in 2.11 (trendlines) and 2.12 (MAs).

### 2.3 Channel trading
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion within a channel (can trade against the main trend). | 39, 49 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Three channel types: uptrend, downtrend, sideways/horizontal. Channels are the stated exception to the rule of trading only with the trend. | 49, 39 |
| Setup conditions | Angled channels: draw trendlines from 2 points, wait for price to touch later. Horizontal channels: can start trading at point #2 because a prior support/resistance is already visible. | 50, 51 |
| Entry trigger & order type | Look for reversal candlesticks to buy or sell at the channel edge. Order type not stated. | 51 |
| Initial stop-loss | "just outside the channel or just above the high of the candlestick (for a sell order) or just below the low of the candlestick (for a buy order) that touched the channel and shows signs of rejection". | 51 |
| Exits: profit-taking | Wait for price to reach the other end of the channel; may take half the profits off in the middle of the channel. | 51 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Points to draw an angled channel line | 2 | - | 50 |
| Partial profit | half off at mid-channel | optional ("may") | 51 |
| Stop offset | "just outside" (no number) | - | 51 |

**Key quotes**
- "Place your stop loss on just outside the channel" [p. 51]
- "reach the other end of the channel to take profit or exit the trade" [p. 51]
- "You may also decide to take half the profits off" [p. 51]

**Pseudocode**
```
fit channel: lower line through 2+ swing lows, upper line through 2+ swing highs, parallel (ASSUMPTION: parallel lines)
long when low touches lower line within TOL and bull_reversal(bar):
    entry = buy stop above signal high   # ASSUMPTION
    stop  = min(signal.low, lower_line) - tick
    target1 = midline (sell half); target2 = upper line
```

**Ambiguities & assumptions**
- How the second (parallel) line is anchored, and how many touches validate a channel: not stated. ASSUMPTION: 2 swing lows define the base line, a parallel line through the intervening swing high.
- Position size and R:R minimum: not found. Channel breaks (what to do when the channel fails) are not covered.
- Short side not usable in NSE cash (ASSUMPTION: long at lower edge only).

### 2.4 Triangle patterns (symmetrical, ascending, descending): breakout or retest
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout / continuation (also retest pullback entry). | 53, 58 |
| Timeframe & holding period | Pattern seen on 4hr, confirmation/entry on 1hr in the author's example. Holding period not stated. | 56 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Symmetrical: continuation pattern, breakout in direction of the prior trend (uptrend: expect upside; downtrend: expect downside). Ascending: bullish continuation in an uptrend, also a bullish reversal in a downtrend. Descending: bearish continuation in a downtrend, also bearish reversal at the end of an uptrend; "regardless of where it forms, it's a bearish chart pattern". | 53, 54, 60, 62 |
| Setup conditions | Symmetrical: price converges to a point; minimum 2 peaks and 2 troughs to draw the two trendlines. Ascending: rising support with flat resistance (implied by name; text shows image). Descending: "descending resistance levels and a fairly horizontal support levels converging to a point". | 55, 61 |
| Entry trigger & order type | Variant A (initial breakout): a candlestick breaks the triangle and closes outside it, then place a pending buy-stop / sell-stop to catch the move. Author prefers waiting for the close outside to avoid false breakouts; sometimes enters with a sell-stop "just a few pips under the support level" and watches the 1hr close. Variant B (retest): wait for price to retest the broken trendline/level (now acting as the opposite level) then buy/sell. Avoid entering on an extremely long breakout candle (stop too large, tends to reverse); use the retest instead. | 56, 57, 58, 63 |
| Initial stop-loss | "3 ways" to place the stop are shown on a chart image only (not in text); the same options apply to all three triangles. | 58, 60 |
| Exits: profit-taking | Ascending: previous resistance, or the "x" pips distance (triangle height), or 2x or 3x that distance. Descending: previous support/lows/troughs, or the triangle height projected. | 60, 63, 64 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Min touches to draw triangle | 2 peaks + 2 troughs | - | 55 |
| Confirmation | candle close outside the pattern | pending stop without close ("a few pips" beyond) | 56, 63 |
| Max breakout-candle size | Not stated ("extremely long" is avoided) | - | 57 |
| Profit target multiple of height | 1x | 2x or 3x | 60 |
| Retest entry | after broken line is retested | - | 58 |

**Key quotes**
- "candlestick has broken the triangle and closed below/above it" [p. 56]
- "I will place a pending buy stop/sell stop order to catch the" [p. 56]
- "The stop loss distance is too large." [p. 57]
- "Trade the retest of the trendline that is broken" [p. 58]
- "I prefer to target previous resistance levels as my take profit target." [p. 60]
- "is to measure the height of" [p. 64]

**Pseudocode**
```
detect triangle: >=2 swing highs forming upper line U and >=2 swing lows forming lower line Lw, converging (apex ahead)
   asc: U flat (|slope|<eps), Lw rising; desc: Lw flat, U falling; sym: both converging   # eps ASSUMPTION
   height = U_start - Lw_start (widest part)       # ASSUMPTION: "x" = height at pattern start (text image-only)
direction: sym -> prior trend; asc -> up; desc -> down (long-only: take up-breakouts)
Variant A: breakout bar t with close[t] > U(t) (up) and (high-low)[t] <= K*ATR (reject "extremely long" bars, K ASSUMPTION 2.0)
           entry buy stop at high[t] next day
Variant B: after breakout, wait for retest low[t'] <= U(t')+TOL and bull_reversal; entry above that bar
stop  = ASSUMPTION: below the lowest of last swing low inside pattern (book's 3 options are image-only)
target = max(prior resistance, entry + 1*height)   # test also 2x, 3x
```

**Ambiguities & assumptions**
- Stop-loss placement (3 options) exists only in an image at p. 58: not found in text. ASSUMPTION: stop below the triangle's last swing low (long).
- "Extremely long breakout candle" has no numeric cut-off. ASSUMPTION: range > 2 x ATR(14) skip, enter on retest.
- The "x" pips profit measure is undefined in text beyond "measure the height of the triangle" [p. 64]. ASSUMPTION: height at the widest point.
- Triangle lines may be fit with any swing definition; no tolerance given. Retest tolerance not stated.
- Short entries (descending triangle) not available in NSE cash; use as exit/avoid signal.

### 2.5 Head & shoulders and inverse head & shoulders
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal pattern (breakout of neckline or retest). | 64, 65, 68 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | H&S is bearish reversal at the end of an uptrend. Inverse H&S is the bullish reversal (end of downtrend, implied by "just the opposite"). | 65, 68 |
| Setup conditions | Left shoulder high; pullback (beginning neckline); new higher high (head); pullback (continuing neckline); rally that fails to take out the previous high (right shoulder); neckline "drawn from the beginning neckline to the continuing neckline". | 65, 66 |
| Entry trigger & order type | Inverse H&S: buy the initial neckline breakout, or wait for the retest of the broken neckline and buy using bullish reversal candlesticks as confirmation. H&S entry details are on a chart image only; by symmetry, sell the breakout or retest (ASSUMPTION). | 67, 70 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | "I use previous lows or troughs"; or distance (pips) from neckline to head projected from the neckline breakout. Inverse: previous highs, or head-to-neckline distance. | 67, 70 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Neckline | line through the two troughs (H&S) | - | 66 |
| Shoulder symmetry tolerance | Not stated | - | - |
| Measured-move target | head-to-neckline distance | previous low/high | 67, 70 |

**Key quotes**
- "The head and shoulders pattern is a bearish reversal pattern" [p. 65]
- "trendline for this pattern should be drawn from the beginning neckline to" [p. 66]
- "I use previous lows or troughs to set my take profit target." [p. 67]
- "I often tend to place my profit target on previous highs." [p. 70]

**Pseudocode**
```
inverse H&S (long): swing lows LS, HEAD, RS with HEAD < LS and HEAD < RS; RS > HEAD; neckline through the two intervening swing highs
   prior trend = DOWNTREND (2.1)
   A: close > neckline(t) -> buy stop above that bar high
   B: after breakout, price returns to neckline within TOL and bull_reversal(bar) -> buy
   stop = ASSUMPTION: below RS low
   target = max(previous swing high, neckline + (neckline - HEAD.low))
H&S (bearish): mirror; on NSE cash use as exit/avoid signal for longs
```

**Ambiguities & assumptions**
- Stop and entry detail for H&S (chart image only) not found in text. ASSUMPTION: stop beyond right shoulder.
- Shoulder-height/time symmetry, neckline slope tolerance and minimum pattern length are not given.
- Both targets given ("previous lows" vs measured move) without rule for choosing. ASSUMPTION: use nearer of the two.

### 2.6 Double bottom / double top
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal pattern; 3 entry styles (breakout, retest, buy second bottom/sell second peak). | 72, 74 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Double bottom: bullish reversal pattern forming in an existing downtrend. Double top: bearish reversal found in an uptrend; once the neckline is broken it confirms a downtrend. | 70, 73 |
| Setup conditions | Two bottoms (peaks) at similar level with a neckline; no numeric rule. | 72 |
| Entry trigger & order type | #1 trade the neckline breakout. #2 wait for the retest of the broken neckline (now support, or resistance for tops) and buy/sell, with bullish/bearish reversal candlestick. #3 buy on bottom 2 (sell on peak 2) on a reversal candlestick: "the technique I like most". | 72, 74, 75 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | If bought on bottom 2: neckline, or any previous highs above. If buying the neckline breakout: project the bottom-to-neckline distance. Double top: previous lows, or neckline-to-highest-peak range projected from the breakout. | 72, 76 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Equality tolerance of the two bottoms | Not stated | - | - |
| Entry style | 3 styles | author prefers #3 (bottom 2 / peak 2) | 72, 74 |
| Target | neckline (if entered at bottom 2) | previous highs; projected height if breakout entry | 72 |

**Key quotes**
- "#3: Buy on bottom 2." [p. 72]
- "If you buy on bottom 2, you can use the neckline as your take profit" [p. 72]
- "The technique I like most to take a sell trade on Peak 2" [p. 74]
- "Use previous low (support levels) to set take profit targets." [p. 76]

**Pseudocode**
```
double bottom (long): swing lows B1, B2 with |B2-B1| <= TOL (ASSUMPTION 1*ATR(14)); neckline = highest high between B1 and B2; prior trend DOWN
  style3: at bar t low within TOL of B1 and bull_reversal(t) -> buy stop above high[t]; stop = B2.low - tick (ASSUMPTION); target = neckline
  style1: close > neckline -> buy; target = neckline + (neckline - min(B1,B2))
  style2: after breakout, retest of neckline with bull_reversal -> buy
double top (bearish): mirror, use only as exit for longs on NSE
```

**Ambiguities & assumptions**
- The text lists the three ways with a duplicated "#2" numbering for double tops; the retest is the third way. 
- Stop-loss rules not found in text. ASSUMPTION: beyond pattern extreme.
- Style #3 buys before the pattern is confirmed; whether to require the second bottom to be a confirmed swing is unspecified.

### 2.7 Triple bottom / triple top
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal pattern (breakout, retest, or buy third bottom / sell third peak). | 78, 79 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Triple bottom: bullish reversal found in a downtrend; neckline break and a move up confirms the trend is up. Triple top: in an uptrend it signals the end of the uptrend when the neckline is broken. Both occur rarely. | 77, 79 |
| Setup conditions | Three bottoms (peaks) with a neckline; no numeric rule. | 77, 79 |
| Entry trigger & order type | Wait for neckline break and trade the initial breakout (conservative); or retest of broken neckline with a bullish/bearish reversal candlestick; or (preferred) take the third bottom / peak 3 on a bullish/bearish reversal candlestick. | 78, 79, 80 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Triple bottom: as for double bottom. Triple top: neckline if trading at peak 3; if trading the neckline breakout, project the distance from neckline to highest peak, or use a previous low. | 78, 80 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of touches | 3 | - | 77, 79 |
| Equality tolerance | Not stated | - | - |
| Preferred entry | third bottom / peak 3 on reversal candle | breakout; retest | 78, 79 |

**Key quotes**
- "I prefer to take trades on the 3rd bottom by watching the price action." [p. 78]
- "If you take a trade at peak 3, you profit target can be the neckline." [p. 80]

**Pseudocode**
```
triple bottom: swing lows B1,B2,B3 within TOL, neckline = highest swing high between them; prior trend DOWN
  preferred: at B3 low touches level (TOL) and bull_reversal -> buy stop above high; stop = below B3 low (ASSUMPTION); target = neckline
  alt: close > neckline -> buy; target = neckline + (neckline - lowest bottom)
```

**Ambiguities & assumptions**
- Same as 2.6 (tolerances, stops absent). Frequency is low, so statistical power on NSE will be poor.

### 2.8 Reversal candlestick patterns at support/resistance (the "nine" candlestick patterns, plus candle blending)
The chapter title says nine patterns but the text lists ten numbered items (#1 doji ... #10 spinning top) [p. 81, 87]. Pattern recognition is the entry signal used by 2.1, 2.2, 2.3, 2.5-2.7, 2.10-2.13.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal (counter-swing) signal at a level; also used as a "with-trend pullback" trigger. | 81 |
| Timeframe & holding period | Any timeframe; author uses 1hr/4hr for entries. Not stated for holding. | 119 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Pattern is valid only in the matching context: bullish patterns in a downtrend or at support; bearish patterns in an uptrend or at resistance. The hanging man "must form in an uptrend". | 81, 82, 86 |
| Setup conditions | Patterns (all qualitative): Doji (cross, gravestone, dragonfly, long-legged); bullish/bearish engulfing (2nd candle completely engulfs 1st); bullish/bearish harami (short candle of opposite colour covered by the first candle's shadow); dark cloud cover (bullish candle then bearish candle closing at about the midway point of the first); piercing line (mirror: 2nd bullish closes "somewhere up" the midpoint); shooting star (bearish; single candle; aliases bearish pin bar); hammer ("very long tail and a short upper wick or none at all"); hanging man (hammer shape in an uptrend); railway track (two candles of almost the same length and body, mirror images); spinning top (small body, upper and lower shadows longer than body, nearly equal shadows). Context: "When these candlesticks form at support and resistance levels or Fibonacci levels they are great trade entry signals." | 81-87 |
| Entry trigger & order type | General: act on the pattern at the level. Specific triggers given: break of the high of a hammer ("as soon as the high of the hammer candlestick is broken, price will shoot up"); sell-stop "just a few pips under the low" of a bearish harami; breakout of spinning top high/low (2.9). Other patterns: order type not stated. | 124, 117, 88 |
| Initial stop-loss | Not found in this text as a general rule (for the harami example the stop is outside the resistance line; for channels see 2.3). | 117, 51 |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

Candle blending (page 89-92): a higher-timeframe candle equals the combination of its lower-timeframe candles (e.g. one 1hr candle = two 30-minute candles), so a pattern missing on one timeframe may appear on a "partner" timeframe. "A Dark cloud cover when blended also forms a shooting star"; a piercing line blended forms a hammer [p. 92]. The author uses it to find hammer/shooting-star signals when only another pattern is visible.

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Dark cloud / piercing close | at about the midway point of the first candle | "somewhere up the mid-point" | 83, 84 |
| Hammer shape | long lower tail, short or no upper wick | no ratio given | 85 |
| Spinning top shadows | both exceed the body; "almost the same length" | - | 87, 88 |
| Doji body | none or very tiny | - | 88 |
| Railway track | two candles of almost the same length and body | - | 87 |
| All numeric thresholds (wick/body ratios, % of range) | Not stated | - | - |
| Blending | combine the two lower-timeframe candles of one higher-timeframe candle | - | 90-92 |

**Key quotes**
- "they are great trade entry signals." [p. 81]
- "the mindway point of the first candlestick." [p. 83]
- "The second bullish candlestick should close somewhere up" [p. 84]
- "It has a very long tail and a short upper wick or none at all." [p. 85]
- "must form in an uptrend" [p. 86]
- "the hammer candlestick is broken, price will shoot up!" [p. 124]
- "A Dark cloud cover when blended also forms a shooting star." [p. 92]

**Pseudocode**
```
# ASSUMPTION thresholds (book gives none); body = |C-O|, range = H-L, upper = H-max(O,C), lower = min(O,C)-L
doji:        body <= 0.1*range
spinning:    0.1*range < body <= 0.3*range and upper > body and lower > body and |upper-lower| <= 0.25*range
hammer:      lower >= 2*body and upper <= 0.1*range and body>0 ; context downtrend/support -> bullish
hanging_man: same shape in UPTREND -> bearish
shooting_star: upper >= 2*body and lower <= 0.1*range, context uptrend/resistance -> bearish
bull_engulf: C[-1]<O[-1] and C>O and O<=C[-1] and C>=O[-1]        # ASSUMPTION body engulfing
bull_harami: C[-1]<O[-1] and long body[-1] and C>O and H<=H[-1] and L>=L[-1]   # "covered by the shadow of first candle"
piercing:    C[-1]<O[-1] and C>O and C>=(O[-1]+C[-1])/2 and C<O[-1]
dark_cloud:  mirror of piercing
railway:     opposite colours, |body1-body2| <= 0.1*max(body) and similar ranges
signal_valid = pattern and context(trend or level)       # level = at_support / at_resistance from 2.2
LONG ENTRY (hammer): buy stop at high[t] + tick on day t+1 (only the hammer trigger is stated in the book); other patterns: ASSUMPTION same trigger
stop = low[t] - tick; target = next resistance
blend2(bar_a, bar_b): O=O_a, C=C_b, H=max(H_a,H_b), L=min(L_a,L_b)    # 2-day blended bar on daily data (ASSUMPTION)
```

**Ambiguities & assumptions**
- No quantitative candle definitions anywhere; all thresholds above are ASSUMPTION.
- Harami says the second candle is "completely covered by the shadow of first candle" [p. 82]: ambiguous between body-in-body and range-in-range. ASSUMPTION: second candle's range inside first candle's range.
- Engulfing text is truncated in the text layer ("completely engulfs" with no object) [p. 82]. ASSUMPTION: body engulfs body.
- Railway-track text says the second candle of a bearish track "is bullish" [p. 87]; this is an apparent typo (should be bearish). ASSUMPTION: opposite colours.
- Chapter says nine patterns but numbers ten; harami, engulfing, dark cloud, piercing, railway are 2-candle, others 1-candle.
- Spinning top "bearish" vs "bullish" is by candle colour (see 2.9).
- Stop-loss and profit targets for single-candle signals are not found in this book.
- "Uptrend" / "resistance level" context uses the vague definitions in 2.1/2.2.

### 2.9 Spinning top / doji indecision breakout (trigger on break of the candle's high or low)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout of an indecision candle at a level, with the trend or reversal. | 88, 114 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | A bearish spinning top in a support area or downtrend becomes a bullish reversal signal when its high is broken; a bullish spinning top at resistance or in an uptrend becomes bearish when its low is broken. A doji in the dominant downtrend: sell on the break of the doji low (confluence example). | 87, 88, 114 |
| Setup conditions | Spinning top with small body, shadows both longer than the body and about equal; at support or resistance. Doji: indecision between buyers and sellers. | 87, 88, 114 |
| Entry trigger & order type | The next candle breaking the high (long) or low (short) of the spinning top/doji; "the breakout of the low of doji candlestick was what the sellers were waiting for". Order type not stated. | 88, 114 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trigger | break of the spinning-top high (long) / low (short) by the next candle | - | 88 |
| Spinning top body | "a few steps wider" than a doji; short | no ratio | 88 |
| Validity window for the break | Not stated | - | - |

**Key quotes**
- "when the high of tha bearish spinning top is broken to the" [p. 88]
- "signals the move in that direction of breakout!" [p. 88]
- "the breakout of the low of doji candlestick was what the sellers were" [p. 114]

**Pseudocode**
```
at day t: spinning_top(t) and at_support(t) and DOWNTREND-or-support context -> long setup
   buy stop at high[t]+tick on t+1 (ASSUMPTION: order valid for 3 days; book silent on how long the setup stays valid)
   stop = low[t]-tick (ASSUMPTION); cancel if low[t+1..] makes new low before trigger
```

**Ambiguities & assumptions**
- Setup validity window, stop and target are not found in this book. ASSUMPTION: valid 3 bars, stop at the candle's opposite extreme, target next resistance.
- "Bearish spinning top" means a red candle in this text (color-based).

### 2.10 Fibonacci retracement + reversal candlestick
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion / trend pullback entry. | 93, 94 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Used in an uptrend (retrace of upswing -> buy at the pullback) and in a downtrend (retrace of a downswing -> sell the rally). | 94, 96, 97 |
| Setup conditions | Draw the retracement between a major peak and trough: in a downtrend click the previous peak and drag to the trough where price reversed; in an uptrend from trough to peak. Levels: 23.6%, 38.2%, 50%, 61.8%, 100%; "the two fib levels I use the most are the 50% and the 61.8%". Price must reach a Fibonacci level and show rejection. | 93, 94 |
| Entry trigger & order type | Reversal candlestick (e.g. spinning top at 50%) at the Fibonacci level; the author dislikes buying/selling on the Fibonacci level alone. Combine with reversal candlesticks, trendlines, support/resistance. Order type not stated. | 95, 96 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fib levels used | 50% and 61.8% | 23.6%, 38.2%, 100% listed but not used | 93 |
| Swing anchors | "major peak and trough" | - | 93 |
| Required confirmation | reversal candlestick | + S/R, trendlines | 96 |
| Tolerance around level | Not stated | - | - |

**Key quotes**
- "The two fib levels I use the most are the 50% and the 61.8%." [p. 93]
- "But personally, I do not like that approach." [p. 96]
- "price confluence" [p. 94]

**Pseudocode**
```
uptrend (2.1): swing low L2 -> swing high H2 (most recent completed upswing)
fib50 = H2 - 0.5*(H2-L2); fib618 = H2 - 0.618*(H2-L2)
zone = [fib618, fib50] widened by TOL (ASSUMPTION; the doji example at p.114 uses "50-61.8 fibonacci retracement zone")
signal: low[t] enters zone and bull_reversal(t) and close[t] > fib618 (ASSUMPTION no close below 61.8)
entry: buy stop above high[t]; stop = below min(low[t], L2) (ASSUMPTION); target = H2
```

**Ambiguities & assumptions**
- Which swing pair counts as "major" is not defined. ASSUMPTION: the latest completed swing from 2.1 helpers with leg >= 3 ATR.
- No stop/target rules for Fibonacci entries are given. ASSUMPTION as above.

### 2.11 Trendline touch trade (with re-draw after a break)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback to a dynamic line. | 98, 99 |
| Timeframe & holding period | Daily chart setups held "a week or two" if the target is hit. | 100 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Downtrend: downward trendline (min 2 peaks) and short on touch; uptrend: upward trendline (min 2 troughs) and buy on touch. | 98, 99 |
| Setup conditions | "you need a minimum of 2 peaks to draw a downward trendline"; 2 troughs for an upward line. If a trendline breaks, look for another trendline above (below); there can be two or more trendlines at any time. | 98, 101 |
| Entry trigger & order type | Price returns to the trendline plus a bullish (bearish) reversal candlestick as confirmation ("highly recommended"). After a stop-out at the first line, short again at the 2nd line on a bearish reversal candle. | 98, 100, 101 |
| Initial stop-loss | "my stop loss is tight"; specific placement not stated (price breaking the trendline stopped the example trade). | 100 |
| Exits: profit-taking | Previous level (example target 1.1290, a pre-identified level) ; reward "more than 3 times what I risked". | 100 |
| Exits: trailing / time / signal | Trailing stop mentioned ("my trailing stop gets hit"); rule not stated. | 100 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Re-entry on a second trendline after a stop-out (not an add). | 101 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Min points for trendline | 2 | - | 98 |
| Trendline break meaning | trend has changed OR false break | - | 101 |
| Stop distance | tight, not numeric | - | 100 |
| Reward multiple | > 3R in the example | 7R in a different example | 100, 112 |

**Key quotes**
- "you need a minimum of 2 peaks to draw a downward trendline" [p. 98]
- "The use of bearish reversal candlesticks as trade confirmation is highly" [p. 98]
- "potential reward of more than 3 times what I risked for this trade" [p. 100]
- "you should also look to sell if you get bearish reversal candlestick signal" [p. 101]

**Pseudocode**
```
uptrend line: through 2 latest swing lows (rising); check price has not closed below it
long when low[t] <= line(t)+TOL and bull_reversal(t):
    buy stop above high[t]; stop = min(low[t], line(t)) - 1*ATR*0.25 (ASSUMPTION); target = last swing high
if closed below line -> mark broken; search next line (2 other lows) below; repeat
```

**Ambiguities & assumptions**
- Which two points to use, and the slope/line-fitting method are unspecified (discretionary). ASSUMPTION: the two most recent swing lows.
- Break definition not given (close vs intraday). ASSUMPTION: close beyond line.
- Stop and trailing rules not found. ASSUMPTION: stop just below the signal candle; trail under higher lows.

### 2.12 Moving averages as dynamic support/resistance
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback to a moving average. | 106 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Trend is NOT taken from the moving averages (they lag); the author uses price structure for trend and moving averages only for dynamic support/resistance. In a nice trending market the approach is effective. | 103, 106 |
| Setup conditions | Downtrend: price rallies up to the moving average lines and bounces down. Uptrend: price pulls back down to them and bounces up. Moving-average type and period are not stated (the text refers to "moving average lines"). | 104, 105 |
| Entry trigger & order type | Look for a reversal candlestick as price starts to go back to touch the moving average lines: shooting star, bearish harami, spinning top, dark cloud cover, hanging man to sell in a downtrend; pin bars, dojis, piercing line, bullish harami to buy in an uptrend. | 106 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| MA type and lengths | Not stated | "moving average lines" (plural) | 104 |
| Touch tolerance | Not stated | - | - |
| Role of MA | dynamic support/resistance only | not a trend filter | 103 |

**Key quotes**
- "The only thing I see useful in moving averages is for dynamic support and" [p. 103]
- "candlesticks as price starts to go back to touch the moving average lines" [p. 106]

**Pseudocode**
```
MA = EMA(close, 20) and EMA(close, 50)      # ASSUMPTION: book names no period (test 20/50, 21/55)
trend from swing structure (2.1) only
long: UPTREND and low[t] <= MA(t)+TOL and close[t] >= MA(t)-TOL and bull_reversal(t)
      buy stop above high[t]; stop = below signal low; target = last swing high
```

**Ambiguities & assumptions**
- MA type/period are not stated ("not found in this book"). ASSUMPTION as above.
- Stop, target and tolerance not given.

### 2.13 Confluence trade (composite of the above)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Counter-swing pullback entry at a multi-factor zone, with the trend ("trade the obvious"). | 110, 124 |
| Timeframe & holding period | Setup on the daily chart; entry on the 1hr chart in the worked example. Holding period not stated. | 110, 111 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Overall trend must agree: example list "the overall trend is down" + resistance level + 61.8 Fibonacci level. | 110 |
| Setup conditions | Two or more levels coincide (confluence): trendline, previous broken support (flipped resistance), Fibonacci 61.8% (worked example), also the doji example with 4 factors: dominant downtrend, doji indecision, 50-61.8 Fibonacci zone, moving averages as dynamic resistance. Other confluence: major support + upward trendline + bullish piercing line. | 110, 111, 114, 125, 126 |
| Entry trigger & order type | Wait for price to hit the confluence zone on the lower timeframe and print a reversal candlestick (shooting star in the example); "That was my clue to execute a short trade right there". Doji variant: break of the doji low. | 111, 114 |
| Initial stop-loss | Worked example risked 50 pips (placement relative to structure not stated in text). | 112 |
| Exits: profit-taking | Previous swing low as target (215 pips, quoted as "7 times what I risked"). Actual: 138 pips on the first trade; a second trade made 125 pips. | 112 |
| Exits: trailing / time / signal | A trailing stop-loss was used on the second trade until stopped out when price moved back up (rule not stated). | 113 |
| Position sizing | See Section 3 (2% risk example). | 119 |
| Adding to / pyramiding | Second, separate trade in the same direction in the example; no rule. | 112, 113 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Min factors for confluence | "two or more" | 3 in worked example, 4 in doji example | 110, 111, 114 |
| Fib level | 61.8% | 50-61.8 zone | 111, 114 |
| Stop | 50 pips (example) | - | 112 |
| Target | previous swing low | - | 112 |

**Key quotes**
- "where two or more levels intersect each other" [p. 110]
- "I risked 50 pips for this trade" [p. 112]
- "my profit target which is 215 pips" [p. 112]
- "I used trailing stop loss as shown below" [p. 113]
- "Just Trade the obvious!" [p. 126]

**Pseudocode**
```
score(t) = [trend aligned] + [at horizontal S/R or flipped level] + [in fib 50-61.8 zone] + [at trendline] + [at MA]   # each 0/1
if score >= 2 (ASSUMPTION; book: "two or more" levels) and bull_reversal(t) (long) :
    buy stop above high[t]; stop = below min(low[t], zone low)
    target = previous swing high; trail below higher lows after +1R (ASSUMPTION; book says only "trailing stop")
```

**Ambiguities & assumptions**
- Text claims 215 pips target = "7 times" a 50-pip risk [p. 112]; 215/50 is about 4.3. Internal inconsistency; no rule extracted from the multiple.
- Number of factors required for a trade is not stated beyond "two or more levels". ASSUMPTION: >= 2 plus reversal candle.
- No mathematical zone tolerance.

## 3. Risk & money-management rules

| Rule | Detail | Page |
|---|---|---|
| Risk per trade | Author's illustration: risk about 2% of the account per trade ("Instead of losing 2% of my trading account" in a gap-through-stop disaster; example of a $10,000 account risking 2% = $200). The text states it as an example, not a mandated universal rule. | 8, 119 |
| Position sizing from stop distance | Size by stop distance: a wide stop is not large risk if the position is sized to it. Example: 80-pip daily stop -> 0.25 lot; 20-pip 1hr stop -> 1 standard lot for the same $200 risk. | 42, 119 |
| Reward vs risk | No fixed minimum. Statements: "making your winners larger than your losing trades" is part of the edge; example trade "potential reward of more than 3 times what I risked"; another example of about 4 to 7 times; "if your losses are small but your profits are large, you will always be in be out in front". | 13, 100, 112, 124 |
| News/event risk | Check an economic calendar before entering; if a high-impact release is close, do not enter, or trade small, unless the stop can be placed behind a major support/resistance level. For a running profitable trade, tighten the stop or take partial profits ahead of news. Gaps can jump the stop-loss (one case: lost nearly half the account instead of 2%). | 7, 8, 9 |
| Stop tightness via multi-timeframe | Use the lower timeframe to enter so that the stop is smaller and a larger position can be traded for the same risk. | 116, 119 |
| Partial profits | Optionally take half off at the middle of a channel. | 51 |
| Do not chase | "If the bus leaves you" - if late for the entry, wait for a retrace/retest/pullback. | 127 |
| Do not buy overextended breakouts | Author will not buy a breakout of an overextended move; waits for a pullback. | 123 |
| After losing streak | Take a break, "Take a week off from" trading. | 127 |
| After winning streak | Do not get overconfident and risk more. | 127 |
| Max positions / portfolio heat / drawdown limits / correlation | Not found in this text. | - |
| Time stop | Not found in this text. | - |

## 4. Non-codable guidance

- Price action reflects collective behaviour; many traders watch the same obvious levels, patterns and candlesticks, so "trade the obvious" [p. 15-16, 124-126].
- Chart time: study past charts to see why big moves began, then spot the same patterns live; "learning comes from observing and doing" [p. 14, 113, 115].
- Price action is not the holy grail and will not make you rich or an overnight success; use risk management [p. 13].
- Discretionary judgement on whether a trend is intact or reversing ("develop the skill to judge") [p. 35].
- Levels are not "lines drawn in concrete"; they eventually break [p. 127].
- Second-guessing a valid setup is the main psychological challenge [p. 107].
- Ignore analysts' opinions; use independent judgment from the chart [p. 127].
- Find the timeframe that fits your personality and work circumstances; beginners should use 1hr or 4hr for entries [p. 119, 127].
- Larger timeframes hide reliable setups visible on smaller timeframes [p. 122].
- Be patient for right setups, do not chase [p. 13, 127].
- Fundamental analysis is largely ignored ("everything is already discounted"), but major scheduled news must be respected [p. 6].
- Pure price action (no indicators) vs "not-so-pure" (adding moving averages, oscillators) [p. 16-17, 103].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily OHLCV only (open, high, low, close, volume, plus delisting-adjusted history). Volume is optional (the book does not use volume or delivery %). An index series (NIFTYBEES or an equal-weight panel index) is optional as a trend filter; the book uses no index filter. Higher timeframes (weekly/monthly bars) can be resampled from daily. No fundamentals required.
- **Testability with our data:**
  - Backtestable on 2005-2026 daily bars: swing-structure trend classification, horizontal support/resistance levels, flipped levels, channels, triangles, head & shoulders, double/triple tops and bottoms, candlestick patterns (using ASSUMPTION thresholds), spinning-top/doji breakouts, Fibonacci 50%/61.8% pullbacks, trendline touches, moving-average pullbacks, confluence scoring.
  - Not testable as written: the book's lower-timeframe entry refinement (1hr/4hr/5min entries within a daily or weekly setup, chapters 16 and the examples at pages 111-123) and candle blending across 30-minute/1hr/4hr bars [p. 89-92]; we only have daily bars. ASSUMPTION: test daily entries on weekly setups (weekly resample), accepting larger stops, or blend two daily bars.
  - Not testable: economic-news filter [p. 8-9] (no event calendar in our data; could proxy with results/budget dates but out of scope); discretionary chart-drawing (trendlines, channels, "significant" levels) needs a deterministic algorithm, which is an interpretation of the book.
  - Forward-testing only: none (no fundamentals used).
- **Market-structure differences and proposed adaptations:**
  - Forex pips vs stocks: convert pip-based stops/targets to price % or ATR multiples. ASSUMPTION: stop in ATR(14) units; targets as multiples of the pattern height (1x, 2x, 3x for triangle per [p. 60]).
  - No overnight shorting in NSE cash: ASSUMPTION: long-only; the book's bearish setups (resistance rejection, bearish patterns, head & shoulders, double/triple tops, descending triangles) become exit signals or no-trade filters; intraday short (MIS) is not testable on daily bars; futures not in data.
  - Gaps: the author's own warning about stops being jumped [p. 7-8] applies more to NSE gaps; use next-day open fills for stop-market orders and add slippage 0.1% plus STT/brokerage.
  - Circuit limits: stocks at circuit cannot be entered/exited; flag days with open=high=low=close or limit hits (ASSUMPTION).
  - Order types: buy-stop above the signal candle high is simulated as a next-day stop order: fill = max(open, trigger) if high >= trigger.
  - Liquidity: ASSUMPTION: restrict to stocks with a minimum average daily traded value (e.g. above Rs 5 crore over 20 days) because the book gives no universe rule.
  - Corporate actions: data is adjusted for splits and bonuses, so level and swing detection on adjusted prices is consistent.

## 6. Verdict

- **Codeability:** Partly. The setup families (trend structure, levels, patterns, candles, Fibonacci, trendlines, MAs, confluence) are all describable, but almost none has numeric definitions, stops or exits; a coder must supply all parameters (each marked ASSUMPTION), so results will measure the coder's interpretation as much as the book.
- **Priority for backtesting:** Low-Medium. There is no track record, and entries lack defined exits, so the value lies in a small number of well-posed variants (swing pullback + candle at a level, Fibonacci 50-61.8% pullback + candle, double bottom entry, triangle/consolidation breakout with retest) tested long-only on daily bars with a multi-parameter sweep; the broad "trade the obvious" claim is unlikely to be separable from generic candle-pattern results.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating swing highs/lows and "trend" as exact: the book defines trend only qualitatively (HH/HL, LH/LL) and a trend ends when a higher low is "intercepted" [p. 33]. Look-ahead bias is easy: a swing point needs N bars to confirm; using it on the bar it forms leaks the future.
  2. Coding candlestick patterns as standalone signals instead of context-gated ones: the book states a pattern counts only at support/resistance, Fibonacci levels or in the matching trend, e.g. a hammer in an uptrend is a hanging man [p. 81, 86]; and the trigger is the break of the signal candle's high/low (not the close of the pattern itself) [p. 124, 88].
  3. Implementing the multi-timeframe entry refinement and pips-based stops/targets on daily bars, and short signals on NSE cash: the author's stop sizes and the 1hr/4hr entries (and the 2%-risk sizing example) rely on lower timeframes and forex lots [p. 116-119]; the shorts are not tradable overnight.
