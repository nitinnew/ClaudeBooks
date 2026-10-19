# Day Trading Strategies (Book 2): The Complete Guide with All the Advanced Tactics for Stock and Options Trading Strategies — Andrew Elder

- **Author note:** This is by **Andrew Elder** (© 2020, self-published-style ebook). It is NOT Alexander Elder (author of *Trading for a Living* / the Triple Screen system). Nothing in this spec comes from Alexander Elder's work; no Triple Screen, Force Index, Impulse System or 2%/6% rule appears in this text.
- **Source file:** Google Drive "DAY_TRADING_STRATEGIES_THE_COMPLETE_GUIDE_WITH_ALL_THE_ADVANCED.pdf" (203 pages)
- **Text file used:** text/elder_day_trading_strategies_book2.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index.
  - Verified with `python ../work/bin/verify_citations.py specs/elder_day_trading_strategies_book2.md text/elder_day_trading_strategies_book2.txt`.
- **Coverage:** Read lines 1-4487 of the text file (the whole file) in sequential chunks; last `[[PAGE N]]` reached = 203. Page 1 is blank; pages 24, 182, 198 and 203 are near-empty (chapter-title or one-line pages). No pages were skimmed or garbled; some chapters (7 forex fundamentals, 17-22 broker/market primers, 23 tools, 26 diversification, 27 options rules) were read in full but contain no testable stock rules, so they are summarised in Sections 3-4 only. *Coordinator check: the coordinator re-ran verify_citations (44/44 ok) and an exact-page strict check (0 off-by-one), and confirmed all 11 field tables have exactly the 12 template rows. 11 unquoted citations were spot-checked by grep and page read: 9/20 EMA crossover p.50-51, float under 100 million p.160, relative volume p.161, 5%-a-day / 50-day scan p.164, 1% risk p.18/20, 2% 'ridiculously high' p.31, 0.25% p.32-33, breakeven stops p.9/13, catalyst p.6/161, 'fallen angel' named only p.202; all matched.*

## 1. The method in brief

The book is a 28-chapter, loosely organised overview of day trading, not a single system. Its stated philosophy: day traders should ignore company fundamentals and trade only chart patterns, technical indicators and price action, but must identify the "catalyst" behind a move [p. 6]. It says over 60% of volume is algorithmic, so retail traders should focus on stocks with heavy retail interest that gap on news [p. 7], and should master a few minimal setups rather than many [p. 7-8]. The only fully described day-trading setups are the ABCD pattern [p. 11-13], the Bull Flag [p. 14] and a momentum-stock screen with exit rules [p. 160-165]. The rest is a survey: support/resistance range trading [p. 48-49, 72-74], breakouts [p. 88-89], moving-average and candlestick tools [p. 50-52], ATR [p. 71-72], pivot points [p. 78, 90-91], contrarian trading [p. 91-92], news trading [p. 75], scalping [p. 76-77, 118-122], pairs trading [p. 91], and long chapters on options, futures, forex, commodities and crypto.

The claimed edge is behavioural and structural (buy quiet consolidations after a surge, take profits in wild periods [p. 14]; strict stop and risk limits [p. 18, 32-33]). The book presents **no backtests, no track record and no performance statistics for any strategy**. The only numbers about results are illustrative: a 35% hit-rate strategy has a 91% chance of a 10-trade losing streak [p. 31], and "the best options traders have a winning percentage of about 80%" [p. 183]. Anecdotal example only: OPTT rose from $7.70 to $9.40 on a deal announcement [p. 12]. Timeframe is intraday (positions closed the same day), with some multi-day discussion [p. 86]. Most of the text is generic and several chapters (e.g. 2, 7, 8 opening paragraph) appear to be rewritten from unrelated sources (corporate risk management, forex ATR); treat the ATR "range bound strategy" text [p. 71-72] and the "Gann" material [p. 60-62] as weak.

## 2. Strategies

Strategy status summary (codability on daily NSE bars): 2.1 ABCD (partly, intraday-native), 2.2 Bull Flag (partly), 2.3 Momentum stock screen and exits (partly; the most explicit numbers), 2.4 Support/resistance range trading (partly), 2.5 Breakout (partly), 2.6 EMA 9/20 crossover (partly), 2.7 ATR volatility expansion and trailing stop (partly), 2.8 Classical chart patterns (partly, weakly specified), 2.9 Candlestick and volume reversal signals (partly), 2.10 Pivot-point highs/lows (partly), 2.11 Contrarian (partly). News trading, scalping, pairs trading, retracement, options, futures, forex, commodity and crypto material is listed in Section 4 as non-codable on our data.

### 2.1 ABCD pattern (intraday pullback long)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday pullback/continuation long after a catalyst surge; "self-fulfilling prophecy" pattern that "you just follow the trend" | 11 |
| Timeframe & holding period | Intraday. Example surge happened "at around 9 am"; exit when price makes a new low or at target/momentum loss. Holding period not stated beyond the day | 12, 13 |
| Universe / eligibility filters | Stocks with a fundamental catalyst and high retail interest/volume (gappers); beginners' size under 1000 shares. No price/volume numbers for this setup | 6, 7, 9, 12 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Stock surges up from point A to a new high of the day (point B); then wait for a pullback whose low (point C) is a higher support than A and holds; monitor the consolidation | 12 |
| Entry trigger & order type | Buy "closer to the price point C" once price is seen holding support at C, anticipating the move to D or higher. Order type not stated. Some traders wait "a bit more near D" to confirm the pattern (called riskier, reduces profit) | 12, 13 |
| Initial stop-loss | Stop at C; sell when price goes lower than C. Never enter without an identified stop | 11, 13 |
| Exits: profit-taking | Sell half of the shares near point D and move the stop to breakeven; sell the rest at the target | 13 |
| Exits: trailing / time / signal | Sell the rest if price loses momentum or sellers take control of price action; a new low after D is "a clear exit signal"; volume spike near D noted | 12, 13 |
| Position sizing | Max risk 1% of capital per trade; position risk = shares x (entry - stop), e.g. 500 x ($20-$19) = $500; beginners limit size below 1000 shares | 9, 18 |
| Adding to / pyramiding | Scaling in (e.g. 400/400 or 100/200/500 of 800 shares) described but "not recommended for beginners"; averaging down a loser is not the same thing and can wipe out an account | 9, 10 |
| Portfolio limits (max positions, correlation, heat) | Newbies should do only one or two day trades per day | 166 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Point B | New high of the day | none | 12 |
| Point C | Higher low than A that holds as support | none (no retracement % given) | 12 |
| Entry price | Near C | optionally near D after completion | 12, 13 |
| Stop | At C | none | 13 |
| Partial exit | Half the shares near D, stop to breakeven | none | 13 |
| Max risk per trade | 1% of capital | 0.25% for beginners | 18, 32 |
| Target (D) | Not specified numerically | "your target" | 13 |

**Key quotes**
- "The ABCD Pattern is the simplest pattern you can trade" [p. 11]
- "Your stop could be at C." [p. 13]
- "you can sell half of your shares near point D" [p. 13]
- "When the stock made a new low, it was a clear exit signal." [p. 12]

**Pseudocode** (intraday definition; needs minute bars, which we do not have; see daily adaptation below)

```
# intraday (book version)
A = start of surge; B = new high of day after A
C = first pullback low after B with C > A that holds (price stops making lower lows)
if flat and C identified:
    BUY near C; stop = C; risk = entry - C
    shares = floor(0.01 * equity / risk)         # 1% max risk [p.18]
if price near D (D = prior high B or beyond): SELL half; stop = entry (breakeven)
SELL rest at target, or on momentum loss, or on new low, or if price < C
```

Daily-bar ASSUMPTION version (swing ABCD): A = swing low (lowest low of last 10 days, 2-bar fractal), B = highest high after A that is a 20-day high, C = first swing low after B with low(C) > low(A) confirmed by a close above the C-day high; BUY next open; stop = low(C) - 0.1% (slippage buffer); sell half at B (prior high; "near D" treated as >= B), move stop to entry, sell rest on close < low(C) or after N=10 bars.

**Ambiguities & assumptions**
- Book gives no retracement depth, no target for D, no time limit and no volume filter. ASSUMPTION: D target = B + (B - C) (equal-leg), the textbook ABCD measure; this is NOT from the book.
- "Near C" is undefined. ASSUMPTION: entry on first bar after C is confirmed (higher low printed and close above prior bar high).
- Intraday data is required; the daily version changes the strategy into a multi-day swing and is an ASSUMPTION.
- The book also says a trader cannot "ascertain the stop" at B [p. 11], so entry at B is excluded.

### 2.2 Bull Flag momentum

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Momentum continuation (flag after a pole); treated by the author as a scalp | 14 |
| Timeframe & holding period | Short-lived: "get in quickly, make money, and then exit"; flags "tend to last around two weeks on average" in the generic chart-pattern chapter (different timeframe) | 14, 57, 58 |
| Universe / eligibility filters | Same stocks-in-play/catalyst idea as 2.1 and 2.3. Not found specifically for flags | 6, 7 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Pole = "different large candles rising"; flag = "a sequence of small candles that move sideways" (consolidation) where price does not decrease significantly because buyers still participate; flags are associated with falling volume (non-falling volume suggests reversal) | 14, 58 |
| Entry trigger & order type | Participate during the quiet (flag) period, not by chasing the stock while price is rising. Exact trigger (e.g. break of flag high) not stated | 14 |
| Initial stop-loss | Not found for this pattern (generic: place stop as soon as you enter; support or MA methods) | 78, 158 |
| Exits: profit-taking | "take their profits during wild periods"; generic momentum exits: sell half at target, extension bar | 14, 161, 162 |
| Exits: trailing / time / signal | Generic momentum rule: a candle closing red before target means exit (unless half already sold) | 162 |
| Position sizing | Generic 1% risk rule | 18 |
| Adding to / pyramiding | Not found for this pattern | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this pattern | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pole | Several large rising candles (count/size not given) | none | 14 |
| Flag | Sequence of small sideways candles; volume falling | duration "around two weeks on average" (generic flags/pennants) | 14, 57, 58 |
| Flag shape | Flag = parallel support/resistance; pennant = converging lines | none | 57 |

**Key quotes**
- "Successful day traders usually aim to participate in the trade during quiet periods and take their profits during wild periods." [p. 14]
- "frequently associated with falling volume" [p. 58]

**Pseudocode** (ASSUMPTION-heavy; book gives no numbers)

```
pole = last K bars (K=3..8) with total gain >= 15% and mostly up-closes      # ASSUMPTION
flag = following 3..10 bars with range < 0.5 * pole range and avg volume < pole avg volume
if flag valid and close > flag_high: BUY next open                          # ASSUMPTION trigger
stop = flag_low;  target = entry + pole_height                              # ASSUMPTION (measured move)
exit rule per 2.3 (red-close / extension bar)
```

**Ambiguities & assumptions**
- No numeric definition of pole or flag, no breakout trigger, no stop, no target. All numbers above are ASSUMPTIONs (textbook defaults, not from the author).
- "Chasing the stock" is warned against, which conflicts with a breakout-of-flag entry. ASSUMPTION: enter on the first close above the flag high, not on extended pole bars.
- Conclusion lists "bag [sic] flag momentum" and a separate advanced "bull flag" strategy [p. 202] but no further detail is in the text (not found in this book).

### 2.3 Momentum stock screen, gap entry and exits (Chapter 24, plus p. 77-78)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Momentum / gap-and-go day trade | 77, 160 |
| Timeframe & holding period | Intraday: "Give the stock most of the day to breathe" before exiting; close positions by the end of day | 77, 78 |
| Universe / eligibility filters | Float below 100 million shares; relative volume at least twice the average; daily chart consistently beating its moving average and trending away from support/resistance; catalyst helpful but "not, strictly speaking, required". Volatility scan: stocks that "moved at least 5 percent every day for the past 50 days" (75 or 100 days more reliable), volume above four million shares within the past month, exclude leveraged ETFs; or evening list of prior-day big movers with average volume above one million | 160, 161, 164, 165 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Chart the stock's trend; confirm it will not reverse by reviewing where it hit its highest and lowest points; the expected move must exceed its normal peaks and valleys; check news (earnings dates; wait until release details are known) | 77, 165 |
| Entry trigger & order type | "wait for a gap and then enter your trade"; order type not stated | 77 |
| Initial stop-loss | Place the stop-loss order as soon as you enter. Level not stated (generic methods: just below a prior support level, or just below the moving average) | 78, 158 |
| Exits: profit-taking | Set profit target before entry; if the trend is stronger than expected, sell half and set a new, better target for the rest | 161 |
| Exits: trailing / time / signal | A candle that closes red before the target means exit ASAP, unless half is already sold (then hold through the first red candle unless the stop is hit); an "extension bar" (spike candle) means lock in profits quickly | 162 |
| Position sizing | Not specific to this setup; generic 1% max risk, beginner size below 1000 shares | 9, 18 |
| Adding to / pyramiding | Not found for this setup | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this setup; newbies limited to 1-2 day trades per day | 166 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Float | < 100 million shares | none | 160 |
| Relative volume | >= 2x average ("the minimum being twice") | higher is better | 161 |
| Trend filter | Price consistently beating its moving average (MA length not given) | none | 161 |
| Daily move (volatility scan) | >= 5% every day | none | 164 |
| Scan lookback | 50 days | 75 or 100 days "even more reliable" | 164 |
| Volume (scan) | > 4 million shares within the past month | > 1 million average volume for the evening list | 164, 165 |
| Expected daily move of target stocks | "as much as 30 percent each day" | none | 160 |
| Partial exit | Sell half when trend exceeds expectation | none | 161 |
| Exit candle | First red-closing candle before target | skip if half already sold | 162 |
| Penny-stock definition | Under $5 per share (SEC) | none | 159 |

**Key quotes**
- "the stocks with the highest momentum are generally going to have a float that is less than 100 million shares" [p. 160]
- "with the minimum being twice what the current average is" [p. 161]
- "wait for a gap and then enter your trade" [p. 77]
- "a candle that closes in the red" [p. 162]
- "sell off half of your holdings" [p. 161]
- "This list should ideally return stocks that have moved at least 5 percent every" [p. 164]

**Pseudocode** (daily adaptation, all ASSUMPTION except thresholds quoted above)

```
universe: stocks with 50-day history; liquid (avg vol 50d turnover > threshold)   # float not available
signal day t (evening scan):
    rvol_t = volume_t / mean(volume, 50) >= 2                                      # [p.161]
    close_t > MA(close, 20) and MA rising                                          # MA length ASSUMPTION
    optional volatility test: count of days in last 50 with abs(close/prev_close-1) >= 5% (ASSUMPTION reading of "moved at least 5 percent every day"; literal version selects almost nothing)
entry day t+1: if open_{t+1} > close_t * (1 + gap_min)  (gap_min=2%, ASSUMPTION): BUY at open (gap entry [p.77])
stop = low of day t (or entry - 1.0*ATR14)                                          # ASSUMPTION
target = entry + 2 * (entry - stop)                                                 # ASSUMPTION; payout ratio 2 [p.41]
manage: when price >= target -> sell half, set new target, stop to breakeven
        if close < open (red candle) and target not hit: SELL at next open unless half already sold
        extension bar: if range > 2.5 * ATR14 and close near high: SELL
time exit: at most 1 day (book is intraday); ASSUMPTION extend to 5 days for daily bars
```

**Ambiguities & assumptions**
- "Moved at least 5 percent every day for the past 50 days" is impossible literally for almost any stock. ASSUMPTION: interpret as average absolute daily % change (or daily high-low range / close) >= 5% over 50 days; even that will select only very speculative small caps hitting circuit limits in NSE.
- The author states catalyst is not strictly required [p. 161] but earlier says never stop until you find the catalyst [p. 6]. ASSUMPTION: no catalyst filter (no news data).
- MA length, gap size, stop distance and profit target are all missing. All assumed.
- "Extension bar" is undefined beyond "a candle with a spike". ASSUMPTION as in pseudocode.
- Float is not in our data. Relative volume is said to "reset every night at midnight" [p. 161] implies intraday cumulative volume; daily bars can only use full-day volume of the signal day (look-ahead if used same day), so the signal day is t and the entry is t+1.

### 2.4 Support/resistance range trading

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion within a range | 48, 74 |
| Timeframe & holding period | Any ("Ranges can last for any length of time, and can even go on for months"); trade is held from support to near resistance | 73 |
| Universe / eligibility filters | Stock that "repeatedly swing[s] between two pricing levels for a relatively extended period of time"; range estimated by drawing support and resistance on the same chart | 72 |
| Market / regime filter | Do not use trend strategies when counter-trend participation grows; ranges end in a breakout up or down | 73, 99 |
| Setup conditions | Support = low of the range, resistance = upper price point (also: resistance = a previous high, support = a previous low) | 48, 135 |
| Entry trigger & order type | "The trader seeks to enter their position at a point of support" (once support is established it is the entry level) | 48, 74 |
| Initial stop-loss | Stop-loss slightly below support (also: "just a bit below" the previous support level) | 48, 49, 158 |
| Exits: profit-taking | Sell "when the share price gets close to resistance levels"; take a limited profit and repeat rather than wait for higher highs | 49, 74 |
| Exits: trailing / time / signal | Break below support signals a bearish trend (exit) | 49, 135 |
| Position sizing | Generic 1% risk | 18 |
| Adding to / pyramiding | Not found for this setup | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this setup | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Support/resistance lookback | Not given | "any length of time" | 73 |
| Stop buffer below support | "slightly below" (no number) | "just a bit below" | 49, 158 |
| Profit target | "close to resistance" | modest, rule-based | 49, 74 |

**Key quotes**
- "The trader seeks to enter their position at a point of support." [p. 48]
- "gets close to resistance levels" [p. 49]
- "It’s better to ensure a limited profit" [p. 74]
- "a break below the support levels" [p. 135]

**Pseudocode**

```
support = lowest low of last N bars (N=40, ASSUMPTION); resistance = highest high of last N bars
range_valid = (resistance - support)/support between 8% and 30% and >=2 touches each side   # ASSUMPTION
if range_valid and low_t <= support*(1+0.01) and close_t > support: BUY next open
stop = support * (1 - 0.01)                                                                 # ASSUMPTION buffer
target = resistance * (1 - 0.01)
exit: close < support*(0.99) (range broken) or time stop 20 bars (ASSUMPTION)
```

**Ambiguities & assumptions**
- No quantitative definition of a range, number of touches, buffer or target. All assumed.
- Long only on NSE cash; the short-at-resistance mirror is not testable.

### 2.5 Breakout (with-trend, near structure)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout / trend continuation | 88, 89 |
| Timeframe & holding period | Not specified; also an intraday variant (opening range breakouts named in the Conclusion but not described) | 202 |
| Universe / eligibility filters | Market currently or recently at a "drastic high or low"; not for markets without strong direction | 89 |
| Market / regime filter | Trade with the trend; do not trade breakouts against the trend; if there are no strong signs of trending, "use with caution" | 88, 89 |
| Setup conditions | Choose a price point (swing high/low or support/resistance) that, once hit, signals a positive swing; breakouts from congested "buildups" where sellers are not pressing; trade near structure so a stop can be placed | 88, 89 |
| Entry trigger & order type | Place an order "above the high" (stop-style order above resistance for longs); also consider the time you are willing to give the stock to reach the price. A break above resistance marks the start of a bullish trend | 89, 135 |
| Initial stop-loss | Structure-based (stop beyond the swing/structure level); "you will never know where to put your stop loss" if far from structure | 88 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Time allowance for the price point is mentioned; no other exit | 89 |
| Position sizing | Generic 1% risk | 18 |
| Adding to / pyramiding | Not found for this setup | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this setup | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Breakout level | Swing high/low or support/resistance | none numeric | 88 |
| Trend filter | "Trade with the trend" (method not given) | none | 88 |
| Time allowance | "the amount of time you are willing to give the stock" (not quantified) | none | 89 |

**Key quotes**
- "you should not trade breakouts against the trends" [p. 88]
- "Trade near the stricture" [p. 88]
- "If there are no strong signs of trending use with caution." [p. 89]
- "Once the price breaks through the upper" [p. 64]

**Pseudocode**

```
trend_up = close > SMA(close,50) and SMA(close,50) rising        # ASSUMPTION trend definition
level = highest high of last 20 bars (before today)               # ASSUMPTION: swing high / resistance
buildup = range of last 5 bars < 0.5 * ATR14*5 and volume not rising against   # ASSUMPTION
if trend_up and buildup and high_t > level: BUY at level (stop order) / next open if gapped
stop = lowest low of buildup (structure)
exit: ASSUMPTION - trail with 3*ATR14 (see 2.7), or time stop 10 bars
```

**Ambiguities & assumptions**
- The text says "above the high or slightly above the low" [p. 89] which is garbled; ASSUMPTION: long breakout above recent high, short breakout below low (short not testable).
- No profit target; ASSUMPTION uses 2.7 trailing stop.
- "stricture"/"structure" typos in the book; interpreted as chart structure (support/resistance).

### 2.6 Exponential moving average 9/20 crossover

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (MA crossover) | 51 |
| Timeframe & holding period | Chart "framed in terms of days" example (Apple); holding period not stated | 50, 51 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | 9-day EMA and 20-day EMA; exponential preferred over simple because it weights recent prices more | 51 |
| Entry trigger & order type | "when the 9-day moving average crosses above the 20-day moving average, the price enters an upward trend" (implied buy); order type not stated | 51 |
| Initial stop-loss | Not found for this setup (generic: just below the moving average) | 158 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | 9-day EMA passing below the 20-day EMA = downward trend (implied exit) | 51 |
| Position sizing | Generic 1% risk | 18 |
| Adding to / pyramiding | Not found for this setup | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this setup | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fast EMA | 9 | 9-period example | 50, 51 |
| Slow EMA | 20 | none | 51 |
| MA type | Exponential | simple MA rejected as equal-weighted | 51 |
| Stop under MA | "just below the moving average" | none | 158 |

**Key quotes**
- "Notice that when the 9-day moving average" [p. 51]
- "crosses above the 20-day moving average, the price enters an upward trend." [p. 51]
- "traders prefer to use exponential moving averages" [p. 51]
- "they don’t always work because they are easily misled" [p. 196]

**Pseudocode**

```
ema9 = EMA(close, 9); ema20 = EMA(close, 20)
if ema9[t-1] <= ema20[t-1] and ema9[t] > ema20[t]: BUY next open
stop = (ASSUMPTION) min(ema20[t], low_t) * 0.99, per "just below the moving average" [p.158]
exit: ema9 < ema20 -> SELL next open
```

**Ambiguities & assumptions**
- Entry/exit are inferred from the description of the trend change; the book never says "buy"/"sell" explicitly for the crossover. ASSUMPTION: long on cross-up, flat on cross-down.
- The book later cautions that candlestick and MA signals can be misled by temporary counter-moves [p. 196]. No filter is offered.

### 2.7 ATR volatility-expansion and ATR trailing stop

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Volatility-breakout filter plus trailing-stop method | 71, 72 |
| Timeframe & holding period | Not specified (pip-based forex language: "past three weeks its 300 pips") | 72 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Low-volatility environment: "there is a good chance that volatility could expand soon"; look at the "multi-year ATR low value" | 71, 72 |
| Setup conditions | ATR measures volatility only, not direction; shrinking candle ranges reduce ATR; the market cycles between low and high volatility; seek an explosive breakout after low ATR | 71 |
| Entry trigger & order type | Not found (direction must come from elsewhere; "when a market breaks down, there may be a big move that may follow") | 72 |
| Initial stop-loss | Use ATR to set a buffer so the stop is not hit prematurely (multiple not given) | 72 |
| Exits: profit-taking | "ATR indicator should also help predict market reversal": if ATR-sized range has been used up over a period the market may reverse (forex pips example) | 72 |
| Exits: trailing / time / signal | "use the multiple of that value to trailing your stop loss" | 72 |
| Position sizing | Not found for this setup | - |
| Adding to / pyramiding | Not found for this setup | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this setup | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| ATR period | Not given | none | 71 |
| Trailing multiple | "a multiple of" ATR (number not given) | none | 72 |
| Low-ATR reference | multi-year ATR low | none | 72 |

**Key quotes**
- "environment, then there is a good chance that volatility could expand soon." [p. 71]
- "ATR value and make sure that you use the multiple of that value to" [p. 72]
- "Especially the multi-year" [p. 72]

**Pseudocode**

```
atr = ATR(14)                                              # period ASSUMPTION
low_vol = atr / close <= percentile(atr/close, 10%) over last 500 bars   # ASSUMPTION for "multi-year ATR low"
if low_vol and breakout signal (see 2.5): BUY
trail_stop = max(trail_stop, highest_close_since_entry - 3 * atr)        # multiple ASSUMPTION (author gives none)
exit when close < trail_stop
```

**Ambiguities & assumptions**
- The ATR chapter is titled "Range Trading or Channel Trading" but describes ATR (and mislabels it "average accurate range"). It supplies no direction rule and no numbers. All settings are ASSUMPTION.

### 2.8 Classical chart patterns (flags, pennants, H&S, cup and handle, triangles, triple bottom)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Pattern-based reversal/continuation | 56-64 |
| Timeframe & holding period | Flags/pennants last about two weeks on average; others not stated | 57, 58 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Ascending triangle forms in an upward trend (bullish continuation); descending triangle in a downtrend (bearish) | 62, 63 |
| Setup conditions | Flag: parallel support/resistance; pennant: converging lines; falling volume. Head and shoulders: three peaks, side peaks smaller than the head, drop expected at right shoulder (reverse H&S for rises). Cup with handle: peak, hard fall, rebound, then a handle as early holders sell. Triple bottom: price rebounds to the same level after each of three lows. Bullish (symmetrical) triangle: converging trend lines; upper line tests resistance | 57, 58, 59, 62, 63 |
| Entry trigger & order type | Triangle: price breaks through the upper trend line = breakout (volume and speed pick up). Reverse H&S: breakout after the second shoulder. Cup: buy as the handle starts to form. Triple bottom: breakout after third bottom | 59, 60, 62, 63, 64 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found for these patterns | - |
| Adding to / pyramiding | Not found for these patterns | - |
| Portfolio limits (max positions, correlation, heat) | Not found for these patterns | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Flag/pennant duration | about two weeks on average | none | 57, 58 |
| Volume in flag | falling (non-falling = likely reversal) | none | 58 |
| Triple bottom count | 3 lows to the same level | none | 62 |
| Inverse H&S | 3 lows, shoulders equal, then breakout | none | 63 |
| Gann angles | 1x2, 1x1, 2x1 (also 8x1, 4x1, 1x4, 1x8), 1x1 = 45 degrees on a square chart | none | 61, 62 |

**Key quotes**
- "frequently associated with falling volume" [p. 58]
- "the head and shoulders formation of three peaks" [p. 58]
- "Once the price breaks through the upper" [p. 64]
- "The 1x2 angle indicates that one unit of price moves for every two units of" [p. 62]

**Pseudocode** (generic pivot-based detector; every threshold is an ASSUMPTION)

```
pivots = swing highs/lows (fractal width 3)
triple bottom: three pivot lows within 2% of each other, spaced >=5 bars; BUY on close above highest pivot-high between them
ascending triangle: flat highs (within 1%) + rising pivot lows over >=20 bars; BUY on close above flat high with volume > 1.5x avg
stop = last pivot low; target = pattern height added to breakout
```

**Ambiguities & assumptions**
- The chapter gives only verbal descriptions, no measurable tolerances, no stops and no targets. Treat as low-priority; any codified version is the coder's own.
- Gann angles are described as "not universally trusted" [p. 60] and need chart scaling; excluded from backtest.
- Some descriptions are internally odd (e.g. cup and handle "reaches its peak price prior to dropping hard and fast" [p. 59]; "Bullish triangle" is a symmetrical triangle [p. 63]). ASSUMPTION: use standard geometric definitions instead.

### 2.9 Candlestick and volume reversal signals

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal (price + volume confirmation) | 50, 52 |
| Timeframe & holding period | One-day candles used in the example; holding not stated | 50 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Bullish signal after a long price decline; bearish signal at peak price | 50 |
| Setup conditions | Long: share price has been dropping for a long period and a large bullish candle appears, confirmed by volume above average. Short/sell: price at peak, bearish candle with higher-than-average volume. Engulfing: a candle larger than the previous opposite candle (e.g. large green after red at a low) is "usually a sign of a trend reversal" | 50, 52 |
| Entry trigger & order type | Buy after the large bullish candle with high volume ("probably move up"); order type not stated | 50 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Bearish high-volume candle at a peak = sell/drop expected | 50 |
| Position sizing | Not found for this setup | - |
| Adding to / pyramiding | Not found for this setup | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this setup | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Volume confirmation | above the average ("high-volume"), average length not given | none | 50 |
| "Long period" of decline | Not given | none | 50 |
| "Large" candle | Not given (engulfs previous opposite candle) | none | 52 |

**Key quotes**
- "A high-volume trading day is a strong indicator that the price" [p. 50]
- "Usually, this is a sign of a trend reversal." [p. 52]

**Pseudocode**

```
downtrend = close < SMA(close,50) and close <= lowest close of last 40 bars * 1.10        # ASSUMPTION
bull_engulf = close>open and open<=prev_close and close>=prev_open and prev_close<prev_open
if downtrend and bull_engulf and volume > 1.5*mean(volume,20): BUY next open              # 1.5x ASSUMPTION
stop = low of engulfing candle; exit by 2.6-style trend change or time stop 10 bars        # ASSUMPTION
```

**Ambiguities & assumptions**
- All thresholds assumed. The bearish version needs shorting, not available overnight; use only as an exit signal.

### 2.10 Pivot-point highs and lows

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion at historical highs/lows | 78, 90, 91 |
| Timeframe & holding period | Intraday close-out ("close out your position by the end of the day") although the support/resistance is read from daily, monthly or yearly charts | 78 |
| Universe / eligibility filters | Securities you trade every day, whose highs and lows you know; otherwise use historical charts | 78, 90 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Mark highs and lows ("R" resistance, "S" support) on daily/monthly charts and determine a clear top and bottom | 78, 90 |
| Entry trigger & order type | Buy when the stock gets to the lowest point; sell/short at the highest | 91, 78 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Hold for it to reach the high point on the chart "or at least higher than where you started" | 91 |
| Exits: trailing / time / signal | Close the position by end of day (day-trading version) | 78 |
| Position sizing | Not found for this setup | - |
| Adding to / pyramiding | Not found for this setup | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this setup | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lookback for highs/lows | Not given | daily, monthly or yearly chart | 78 |
| Calculated pivot formula (P, R1, S1) | Not found in this book | - | - |

**Key quotes**
- "you will want to close out your position by the end of the day" [p. 78]
- "When the stock gets to the lowest point," [p. 91]

**Pseudocode**

```
hi = highest high of last 250 bars; lo = lowest low of last 250 bars          # lookback ASSUMPTION
if low_t <= lo * 1.02: BUY next open; target = midpoint(lo,hi) (ASSUMPTION); stop = lo*0.97
```

**Ambiguities & assumptions**
- "Pivot points" here is discretionary support/resistance, not the floor-trader P/R1/S1 formula (not found in this book). Overlaps with 2.4; keep only one in the backtest.

### 2.11 Contrarian (buy weakness, sell strength)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Contrarian / value-flavoured mean reversion | 91, 92 |
| Timeframe & holding period | Not specified (sell "once they are performing well"/after recovery) | 92 |
| Universe / eligibility filters | Out-of-favour securities with a low P/E ratio; priced well below intrinsic value | 92 |
| Market / regime filter | Enter when others are pessimistic | 92 |
| Setup conditions | Assets that have been performing poorly, "overpriced" vs "bargain" judgement | 92 |
| Entry trigger & order type | Buy assets that have been falling in price; no technical trigger given | 92 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Sell once they perform well / after the company has recovered | 92 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found for this setup | - |
| Adding to / pyramiding | Not found for this setup | - |
| Portfolio limits (max positions, correlation, heat) | Not found for this setup | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| P/E | "low" (no number) | none | 92 |
| Drawdown / lookback defining "falling" | Not given | none | 92 |

**Key quotes**
- "purchasing assets that are performing poorly, and sell" [p. 92]
- "securities that have a low P/E ratio." [p. 92]

**Pseudocode**

```
candidates = bottom 10% by 60-day return and liquid                               # ASSUMPTION
BUY next open; exit when 60-day return rank > median or after 40 bars; stop = -15%   # all ASSUMPTION
P/E filter = forward test only (fundamentals snapshots from Feb 2026)
```

**Ambiguities & assumptions**
- Pure description; nothing measurable. Low priority, price-only version only.

## 3. Risk & money-management rules

| Rule | Detail | Page |
|---|---|---|
| Max risk per trade | 1% of total capital per trade (stocks and forex) | 18, 20 |
| Beginner risk per trade | Not more than 0.25% of the account; 2% called "ridiculously high" for beginners; in practice "far below 0.25%" if limits are to be respected | 31, 32, 33 |
| Position risk formula | Position risk = shares x (entry - stop), e.g. 500 x ($20-$19) = $500 | 18 |
| Loss-streak math | 35% hit rate gives 91% chance of ten consecutive losses | 31 |
| Drawdown | Over 10% drawdown is "99% unlikely" to recover (author's claim); pros: monthly drawdown limit 2% (fund manager) and 4% (prop trader); beginner target 2% | 32 |
| Drawdown limits | Daily limit as a number of losses; weekly about 1%; monthly 2-3% of account; four losses at 0.25% trigger the weekly limit | 33 |
| Recovery period | Track time to recover from max drawdown to new equity high | 34 |
| Gain-protection | After two or more winners, or a session gain above 0.5%, stop trading if gains dip below 0.25% or two more trades are lost | 40 |
| Payout ratio | Aim for payout ratio of about 2; no partial exits for beginners (contradicts the half-off scaling example) | 41, 9 |
| Event rule (beginners) | Stop trading one hour before earnings, rate decisions, NFP and special events and resume one hour after; near profit take lower profit before event; near stop close the trade before event; mid-road trades ride the event | 41, 42 |
| Daily trade count | Newbies concentrate on one or two day trades per day | 166 |
| Position size | Beginners below 1000 shares; scale-in only for pros | 9 |
| Stops placement | Support method (just a bit below prior support) or moving average method (just below the MA); program stop and profit limits on the platform | 158, 171 |
| Options allocation | No more than 15% of total portfolio in options | 95 |
| Stock allocation / diversification | Dedicate 10% or less of the portfolio to a few stocks you believe in; 90% index fund / 10% single stock; ideal portfolio of 25-30 securities; asset-class choice drives returns (about 6% of variance from selection and timing) | 127, 136, 174, 177 |
| Pattern day trader | US rule: $25,000 minimum capital, four trades in a week qualifies (US only); options: max three day trades per five days to avoid the label | 18, 199 |
| Scalping markets | Do not trade more than two markets at a time | 122 |
| Friday close (multiday) | Close operations on Friday evening before the market closes to avoid Monday gaps | 86 |
| Correlation | Do not hold offsetting positions in positively correlated stocks (e.g. short steel while long property developers) | 170 |

## 4. Non-codable guidance

- Psychology: greed, fear and regret; set daily win/loss amounts and stop when exhausted [p. 28-30, 171]; do not average down [p. 9-10].
- Preparation: exercise, diet, sleep, lifestyle, mental prep; entries should be an automatic go/no-go decision during the session [p. 35-37, 186-187].
- Business planning: instruments, markets and timing (the open is probably best for liquidity; the afternoon is "a graveyard"), capital, risk limits, technical system, events, review system, practice [p. 38-42]; trade journal fields (date, instrument, entry, stop, distance, size, reasons, exit, P/L, mental state), mental journal, review after each session [p. 43-45, 189].
- Catalyst identification for a stock running up to 70% [p. 6]; algo competition [p. 7]; only master a few setups [p. 7-8].
- News trading: trade early in the day when the news first comes out; avoid insider-based trading [p. 75-76, 165, 195-196]. Needs news and intraday data; not testable.
- Scalping: bid-ask spread, tick data, broker choice, minimum EUR 12,000 for two mini-futures lots [p. 76-77, 118-122]. Not testable.
- Retracement strategy ("sell on the high and use the profits to buy back in") [p. 90] and pairs trading (long one stock, short another in the same sector) [p. 91, 80-83]: need shorting and intraday data; not testable in NSE cash.
- Trend/range reading, counter-trend participation and "turning points" (a major support/resistance level; do not change bias until it decisively breaks) [p. 97-103]: discretionary.
- Options (strangles, straddles, LEAPS, married puts, spreads, Greeks, buying calls/puts with a $50 per contract profit goal or $30 for conservative, out-of-the-money by a dollar or two) [p. 104-110, 181-200]: not testable on NSE cash.
- Futures margin examples, corn/soybean examples, basis/spread/hedging trades [p. 111-117]; forex platforms, pairs, fundamentals phases [p. 65-70, 80-83, 137-143]; commodities fundamentals [p. 144-148]; crypto wedge charts [p. 149-154]. None testable here.
- Stock-market primers, indices, bull/bear (20%) and correction (10%) definitions, ways to invest [p. 123-136]. Fundamental ratios: current ratio below 1 and debt ratio above 1 are called warning signs [p. 134] (fundamental data forward-test only).
- Software tools: screeners (StockFetcher, Finviz, Chartmill, Stockrover), auto traders, streaming quotes, level 2 quotes for penny stocks (< $5) [p. 155-163, 159].
- Common mistakes: excessive trading, winging it, unrealistic expectations, changing strategies, not analysing trades, ignoring correlations, greed [p. 166-171].
- Conclusion names "reversal trading", "moving average trading", "opening range breakouts", "stock in play" and "fallen angel" as strategies, but none is described in the text (not found in this book) [p. 202].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV (adjusted) for the full panel; delivery % (optional filter, ASSUMPTION, not from the book); a market proxy (NIFTYBEES or equal-weight panel index) only if a regime filter is added (the book has none). Float, intraday/minute bars, level 2, news, options/futures, forex and crypto data are not available. P/E and current/debt ratio only as forward tests from 2026 snapshots.
- **Testability with our data:**
  - **Backtestable on daily bars as an ASSUMPTION-based adaptation (2005-2026):** 2.4 support/resistance range trading, 2.5 breakout, 2.6 EMA 9/20 crossover (the only rule with explicit indicator settings that the author states on daily charts), 2.7 ATR (settings assumed), 2.8 patterns (weak), 2.9 candlestick/volume reversal, 2.10 highs/lows, 2.11 price-only contrarian, and the daily-bar translation of 2.3 (relative volume >= 2x, trend above MA, gap-up entry, red-close exit, half off at target) and 2.2/2.1 (swing versions).
  - **Needs intraday data (not available):** the book's native versions of 2.1 ABCD (point A/B/C/D within one session), 2.2 Bull Flag candles, 2.3 gap entry with same-day exits and intraday relative volume, pivot-point intraday close-out, news trading, scalping, opening range breakouts, intraday volatility monitoring [p. 165] and extension-bar logic as written.
  - **Forward-test only:** low P/E and current/debt-ratio screens [p. 92, 134].
  - **Not testable in NSE cash:** options, futures, forex, commodity, crypto, pairs trading (long/short), short-selling versions of every pattern, CFD/broker topics.
- **Market-structure differences and proposed adaptations (all ASSUMPTION):**
  - Day-trading rules close positions the same day; with daily bars we must hold at least one overnight, so results are swing trades, not day trades. Compare with hold = 1, 3, 5, 10 bars.
  - Daily gap entry: signal at close of day t, buy at open of t+1 (avoids look-ahead from same-day relative volume).
  - No overnight shorting in NSE cash: run long-only. Intraday shorts exist for MIS but cannot be tested without intraday data.
  - Circuit limits: 30%-a-day movers [p. 160] and 5%-a-day movers [p. 164] will often be circuit-locked or illiquid; cap entries by traded value and skip days where open equals a circuit limit. Float below 100 million [p. 160] cannot be applied; use a liquidity floor instead (e.g. median 20-day traded value).
  - Costs: STT, brokerage and about 0.1% slippage matter most for scalp-style, high-turnover rules. The book's 1% risk per trade [p. 18] with stops of 1-3% gives position sizes that are small relative to equity; use the book's 1% max and a 0.25% beginner variant as two sizing arms.
  - US-specific rules ($25,000 pattern-day-trader minimum, 4:1 leverage, 3 day trades in 5 days) [p. 16, 18, 199] do not apply to NSE.

## 6. Verdict

- **Codeability:** Partly. Only the ABCD, momentum screen and risk rules have enough numbers; most strategies are verbal descriptions with no thresholds, and the native versions need intraday data we lack.
- **Priority for backtesting:** Low. There is no author-reported edge or test result, almost every parameter is missing, and the generic items (EMA 9/20 crossover, support/resistance, breakout) are commonplace. Worth a quick run of 2.3 (daily gap + relative volume + half-off exit) and 2.6 as baselines.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating intraday patterns (ABCD, bull flag, gap entry) as daily-bar rules without flagging that the author's stops, partial exits and "end of day" closes assume the same session; and using same-day volume or gap information that is not known at the entry time (look-ahead).
  2. Taking textbook defaults (ATR period, trailing multiple, MA length for the trend filter, target = equal-leg) as the author's values; the book gives none of them. Likewise reading "moved at least 5 percent every day for the past 50 days" literally.
  3. Mixing the book's contradictory risk numbers (1% max [p. 18], 2% called too high [p. 31], 0.25% beginner [p. 32], weekly 1% [p. 33]) and its contradiction on partial exits (scale out half at the first target [p. 9] vs "don't bother with partial exits" [p. 41]); choose one set explicitly.
