# The Candlestick Trading Bible — author not stated in the text

- **Source file:** Google Drive: THE CANDLESTICK TRADING BIBLE(1).pdf
- **Text file used:** text/unknown_candlestick_trading_bible.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
- **Coverage:** Read lines 1-3239 (the whole file), last `[[PAGE 168]]` reached. Pages with no text beyond the page number and running title (chart images only): 1, 116, 119 (the pin-bar/engulfing/inside-bar charts on other pages are also images, but their pages carry caption text). No chapters skipped. The text names no author (it credits Munehisa Homma with inventing candlesticks, p. 4, which does not make him the author). Reading done by a Sonnet sub-agent. The coordinator re-ran the verifier and an exact-page check, spot-checked 10 unquoted table citations, and read pages 147-168 itself (the agent's notes log stopped at line 2799); the section 3 money-management rules on pp. 162-166 are captured.

## 1. The method in brief
A discretionary price-action method built on Japanese candlestick signals (pin bar, engulfing bar, inside bar, inside-bar false breakout) traded on 4H/daily charts [p. 70]. Every trade needs three things: trend, level, signal [p. 79]. Trend is read visually from higher highs/higher lows (or lower highs/lower lows) [p. 52-53]; levels are horizontal support/resistance (incl. broken levels that flip), trend lines, the 8/21 moving averages, 50%/61% Fibonacci retracements, and supply/demand zones [p. 96]; the signal is a candlestick pattern forming at the level. Top-down analysis (weekly then daily then 4H) must agree [p. 70]. Beginners are told to trade with the trend; ranging markets are traded from the boundaries, choppy markets are skipped [p. 79]. Money management: stop beyond the pattern, target at next S/R, minimum 2:1 reward-to-risk, risk 1-2% per trade [p. 133-135].

Evidence: none is a systematic test. The author claims 20 years of personal use [p. 14] and quotes Bulkowski that a bearish inside bar in a bull market indicates a reversal about 65% of the time and continuation 52% [p. 138]. Example trades are chart illustrations only (e.g. NZDUSD daily [p. 100]). The method was written for forex (pips, lots, "forex brokers" [p. 162]); stocks are never mentioned.

## 2. Strategies

Common definitions (all strategies):
- Uptrend = series of higher highs and higher lows; downtrend = lower highs and lower lows [p. 51]. No indicator needed [p. 52].
- Trend/market structure must be judged on bigger time frames "such the 4H, the daily or the weekly" [p. 53].
- Market types: trending, ranging (at least two touches of support and two of resistance [p. 103]), choppy (no clear boundaries; stay away) [p. 68].

### 2.1 Pin bar with the trend (aggressive entry)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback / candlestick reversal-at-level | 88 |
| Timeframe & holding period | 4H or daily (1H, 4H, daily are primary); higher frame (weekly/daily) checked first; holding until target/stop, no time limit | 70, 83 |
| Universe / eligibility filters | Forex written; "any financial market"; no liquidity filter | 4 |
| Market / regime filter | Clear uptrend or downtrend; skip choppy markets; pin bar with trend only; higher-timeframe level/trend must not oppose | 53, 79, 84 |
| Setup conditions | Pullback to support/resistance (or flipped level), the 21 MA when no static level can be drawn, optionally 50%/61% Fib; pin bar = very small real body, very long tail, longer tail is stronger; bullish pin bar in uptrend, bearish in downtrend; at least one or two confluence factors | 81, 85, 88, 89, 96, 97 |
| Entry trigger & order type | Enter immediately after the pin bar closes without waiting for confirmation | 92 |
| Initial stop-loss | Beyond the long tail (above tail for shorts) | 93 |
| Exits: profit-taking | Next support level (shorts) / next resistance (longs); must offer at least 2:1 | 93, 133 |
| Exits: trailing / time / signal | None stated; "don't never look back" once stop and target are set | 135 |
| Position sizing | Risk no more than 2% of equity per trade, 1% for beginners | 135 |
| Adding to / pyramiding | Not stated; a second pin bar later in the same trend is taken as a new trade | 102 |
| Portfolio limits (max positions, correlation, heat) | Not stated | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pin bar tail vs body | shadow at least 2x real body (given for the shooting star) | longer tail is more powerful | 37, 85 |
| Trend filter | HH/HL or LH/LL visual | 4H/daily/weekly | 53 |
| Dynamic level | 21-period moving average | 8 and 21 MA | 89, 96 |
| Fibonacci levels | 50% and 61% | | 96 |
| Min reward:risk | 2:1 | 3:1 and 5:1 shown as examples | 133, 134 |
| Risk per trade | 2% | 1% beginner | 135 |
| MA type | simple (stated for the engulfing/MA strategy) | | 117 |

**Key quotes**
- "you wait for a pin bar to occur after a pullback to support or resistance level" [p. 88]
- "entering the market immediately after the pin bar closes without waiting for a confirmation" [p. 92]
- "your stop loss above the long tail" [p. 93]
- "The pin bar formed in line with the direction of the market is more powerful" [p. 84]

**Pseudocode**
```
for each daily (or 4H) bar t:
  trend = HH/HL swing structure on daily (or weekly for 4H trading)
  body = abs(C-O); upper = H-max(O,C); lower = min(O,C)-L
  bull_pin = trend==UP and lower >= 2*body and lower > 2*upper and body small relative to range
  level_ok = L within tol of (prior swing high now support | rolling 21-SMA | Fib 50/61 of last impulse | S/D zone)
  if bull_pin and level_ok and rr_to_next_resistance >= 2:
      buy at close[t] (or open[t+1]); stop = L[t]; target = next resistance
      size = 0.01..0.02*equity / (entry-stop)
  mirror for shorts (not executable on NSE cash, see section 5)
```

**Ambiguities & assumptions**
- Pin bar thresholds: book gives only "very long tail" and (for shooting star) twice the body [p. 37]. ASSUMPTION: tail >= 2x body and >= 60% of range, opposite shadow < 25% of range.
- "Near" a level has no tolerance. ASSUMPTION: within 0.5 ATR(14) of the level.
- Trend definition has no swing-size rule. ASSUMPTION: swing = 3-bar fractal on daily, trend up if last two swing highs and lows are rising.
- Stop offset beyond the tail is not given. ASSUMPTION: 0 to 0.1% beyond the extreme.
- Target "next S/R" is discretionary. ASSUMPTION: nearest prior swing high within 120 bars, else 3R.
- Moving-average period 21 (8 also used); "not found in this book": ATR, volume or delivery filters.

### 2.2 Pin bar with the trend (conservative 50% entry)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback, limit entry | 93 |
| Timeframe & holding period | As 2.1 | 70 |
| Universe / eligibility filters | As 2.1 | |
| Market / regime filter | As 2.1 | 88 |
| Setup conditions | Same trend + level + pin bar as 2.1 | 93 |
| Entry trigger & order type | Enter after price retraces 50% of the pin bar range (limit order); may never fill | 93, 95 |
| Initial stop-loss | Beyond the pin bar tail (as 2.1) | 93 |
| Exits: profit-taking | Next support/resistance; "more than 5:1" achievable | 93, 94 |
| Exits: trailing / time / signal | None stated | |
| Position sizing | 1-2% risk | 135 |
| Adding to / pyramiding | Not stated | |
| Portfolio limits (max positions, correlation, heat) | Not stated | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry retracement | 50% of pin bar range | | 93 |
| Fill risk | market may not retrace and trade is missed | | 95 |

**Key quotes**
- "entering the market after 50% of the range bar retracement" [p. 93]
- "the market sometimes doesn't retrace to 50% of the range bar" [p. 95]

**Pseudocode**
```
after a valid 2.1 pin bar on day t (not yet entered):
  entry_limit = L[t] + 0.5*(H[t]-L[t])   # long; short mirrored
  stop = L[t]; place limit for days t+1..t+N
  if not filled in N days: cancel
```

**Ambiguities & assumptions**
- Which "range" (full bar high-low or tail only) is not stated. ASSUMPTION: full high-low range.
- Order validity window not stated. ASSUMPTION: 3 daily bars.
- Stop distance becomes smaller (entry nearer stop); book claims better R:R [p. 94].

### 2.3 Pin bar in range-bound markets (support/resistance boundaries, Bollinger confirmation, breakout pullback)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion at range boundaries; breakout-retest variant | 103, 105 |
| Timeframe & holding period | 4H/daily | 70 |
| Universe / eligibility filters | Skip choppy markets | 68 |
| Market / regime filter | Range = at least two touches of support and two of resistance | 103 |
| Setup conditions | Pin bar rejected strongly from range support/resistance; optional confirmation by false breakout of the Bollinger band | 103, 105, 106 |
| Entry trigger & order type | Buy order after the pin bar closes, or wait for 50% of the pin bar range | 104 |
| Initial stop-loss | Stop "above the support level" for the first long example and "below the support level" for the second (contradictory) | 104 |
| Exits: profit-taking | Near the opposite boundary / next resistance | 104 |
| Exits: trailing / time / signal | None | |
| Position sizing | 1-2% risk | 135 |
| Adding to / pyramiding | Not stated | |
| Portfolio limits (max positions, correlation, heat) | Not stated | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Range touches | 2 support + 2 resistance | | 103 |
| Bollinger Bands | not specified (period/deviation not given) | used only as confirmation | 106, 108 |
| Breakout variant | trade breakout of key level or the retrace to breakout point | | 105 |

**Key quotes**
- "going long when prices reaches the support level and going short when prices approach the resistance level" [p. 103]
- "don't never try to trade inside the range" [p. 160]
- "use it always in combination with horizontal key levels" [p. 108]

**Pseudocode**
```
range = last support S and resistance R each touched >=2 times, no HH/HL trend
if bull_pin at S (L<=S+tol, close>S) and [optional low pierced lower Bollinger band and closed back inside]:
   buy at close; stop = below S (see ambiguity); target = R - buffer
mirror at R (short not available on NSE cash)
```

**Ambiguities & assumptions**
- Stop for the first example is described as "above the support level" [p. 104], which is geometrically wrong for a long; the second example says below. ASSUMPTION: stop just below the pin bar low or support, whichever is lower.
- Bollinger parameters not found in this book. ASSUMPTION: 20 period, 2 SD.
- "Strongly rejected" undefined. ASSUMPTION: same pin bar test as 2.1.

### 2.4 Engulfing bar with the trend at key levels (S/R, 8/21 MA, Fib 50/61%, trend line, supply/demand)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback / reversal at level | 112 |
| Timeframe & holding period | Daily and 4H (MA version); bigger frames for S/D zones | 117, 130 |
| Universe / eligibility filters | Any market; no filters | 123 |
| Market / regime filter | Clearly definable uptrend or downtrend; MAs not to be used in range-bound markets | 111, 117 |
| Setup conditions | Second real body opposite colour to and entirely engulfing the first; at a key level: S/R, flipped level, trend line, 8/21 SMA in trend direction, 50% or 61% Fib, or supply/demand zone | 111, 117, 120, 122, 130 |
| Entry trigger & order type | Order immediately after the signal forms | 134 |
| Initial stop-loss | Below the candlestick pattern | 134 |
| Exits: profit-taking | Next support or resistance level | 134 |
| Exits: trailing / time / signal | None stated | |
| Position sizing | Risk 2% max (1% beginner); trade only if potential at least 2:1 | 133, 135 |
| Adding to / pyramiding | Not stated | |
| Portfolio limits (max positions, correlation, heat) | Not stated | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Moving averages | 21 and 8 simple | 200 SMA shown as another common use, not endorsed | 117 |
| Fibonacci | 50% and 61% | | 120 |
| Min R:R | 2:1 | 3:1 example | 133, 134 |
| S/D zone quality | strong departure from zone, good R:R, daily/4H | | 130 |
| Engulf scope | at least one prior candle fully engulfed | body engulf (Nison criteria) | 16, 111 |

**Key quotes**
- "we simply buy when price pullbacks to the moving average and an engulfing bar pattern forms" [p. 118]
- "if you see an engulfing bar pattern matches up with 50% or 61 % levels, it is a powerful price action trading signal" [p. 120]
- "put your stop loss below the candlestick pattern" [p. 134]
- "make sure your trade has a potential of 2:1 risk to reward ratio" [p. 133]

**Pseudocode**
```
bull_engulf = C[t]>O[t] and C[t-1]<O[t-1] and O[t]<=C[t-1] and C[t]>=O[t-1]
uptrend (HH/HL) and (L[t] near SMA21 or SMA8 | Fib 50/61 of last swing | flipped support | demand zone)
potential = (next_resistance - close)/(close - L[t]) >= 2
-> buy at close[t]/open[t+1]; stop = min(L[t],L[t-1]); target = next resistance; risk 1-2%
```

**Ambiguities & assumptions**
- Body vs full-range engulfing: p. 16 says "fully engulfs the previous candle" (range), p. 111 says bodies. ASSUMPTION: real-body engulfing of the prior body, opposite colour, stop at pattern low.
- Pattern stop vs entry on close gives wide stop. ASSUMPTION: no max stop cap.
- Moving average slope condition: "if the moving average is trending down" [p. 118] undefined. ASSUMPTION: SMA21 slope over 5 bars has the trend sign.

### 2.5 Engulfing bar in ranging markets (boundary, breakout/pullback, false breakout)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion at boundaries; breakout; false-breakout reversal | 127, 128 |
| Timeframe & holding period | 4H/daily | 130 |
| Universe / eligibility filters | Skip choppy markets where levels cannot be identified | 127 |
| Market / regime filter | Range-bound with horizontal support/resistance (the book says markets spend more than 70% of time ranging) | 125 |
| Setup conditions | Engulfing bar at major support/resistance or supply/demand zone; or at a false breakout of that level | 127, 129, 134 |
| Entry trigger & order type | Order immediately after the signal | 134 |
| Initial stop-loss | Below the pattern | 134 |
| Exits: profit-taking | Next S/R (range opposite side) | 134 |
| Exits: trailing / time / signal | None | |
| Position sizing | 1-2% risk; R:R at least 2:1 | 133, 135 |
| Adding to / pyramiding | Not stated | |
| Portfolio limits (max positions, correlation, heat) | Not stated | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Range frequency claim | more than 70% of time | trends 30% of time (p. 53) | 125, 53 |
| Strategies | boundary / breakout or pullback / false breakout | | 127, 128 |

**Key quotes**
- "the first strategy is going to be about trading this price action pattern from major support and resistance levels" [p. 127]
- "The third strategy is to trade the false breakout of the major support or resistance level." [p. 128]

**Pseudocode**
```
range detected (2+2 touches); engulfing bar closes at S (long) or false-breakout (wick beyond S, close back inside) 
buy close; stop below pattern; target R; require RR>=2
```

**Ambiguities & assumptions**
- Breakout/false-breakout rules are only illustrated; no numeric rules. ASSUMPTION: false breakout = bar low below S by any amount and close above S.

### 2.6 Inside bar breakout in the direction of the trend (continuation)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following continuation breakout | 140 |
| Timeframe & holding period | Daily and 4H recommended for beginners | 146 |
| Universe / eligibility filters | None | |
| Market / regime filter | Strong trend, trade with it; not against it for newbies | 140, 146 |
| Setup conditions | Inside bar (second bar contained within the mother bar) in line with trend, at a key level (S/R, Fib, MA, pivot points), with two or more confluence factors | 140, 142, 146, 147 |
| Entry trigger & order type | Sell order after the breakout of the inside bar pattern (safest entry); aggressive entry before breakout is "tricky and dangerous" | 141, 144 |
| Initial stop-loss | Above the mother candle (for a short) | 141 |
| Exits: profit-taking | Next support level | 141 |
| Exits: trailing / time / signal | None | |
| Position sizing | 1-2% risk | 135 |
| Adding to / pyramiding | Three inside-bar opportunities to join one downtrend are shown; each a separate trade | 141 |
| Portfolio limits (max positions, correlation, heat) | Not stated | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Inside bar | second bar fully inside first (mother) | p. 40 Harami text says "close outside the previous one" (contradiction) | 137, 40 |
| Bulkowski stats | reversal 65%, continuation 52% (bull market, bearish inside bar) | | 138 |
| Key levels | S/R, Fib retracement, MA, pivot points | | 142 |

**Key quotes**
- "You can place a sell order after the breakout of the pattern" [p. 141]
- "your stop loss order should be placed above the mother candle" [p. 141]
- "the safest entry should be after the breakout of this pattern" [p. 144]

**Pseudocode**
```
inside[t] = H[t]<H[t-1] and L[t]>L[t-1]
uptrend and level_ok: buy stop at H[t-1] (mother high) valid next N bars; stop = L[t-1]; target next resistance
```

**Ambiguities & assumptions**
- Breakout level: the book says "breakout of the pattern"; unclear whether of the inside bar or mother bar. ASSUMPTION: mother bar high/low (matches stop placement).
- Harami definition contradiction (p. 40 vs p. 137). ASSUMPTION: p. 137 containment definition.
- Order expiry not given. ASSUMPTION: 3 bars.

### 2.7 Inside bar false breakout (fade of the failed break)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal / trap-fade; also continuation when with trend | 148, 150 |
| Timeframe & holding period | Daily/4H | 146 |
| Universe / eligibility filters | None | |
| Market / regime filter | Trending (trade with trend) or range (trade at horizontal levels) | 151, 156 |
| Setup conditions | Price breaks out of the inside bar then quickly reverses to close within the mother bar's range; near S/R, S/D zone, Fib 50/61%, 21 MA or trend line, or horizontal levels in a range | 148, 151 |
| Entry trigger & order type | Sell order after the close of the break bar | 157 |
| Initial stop-loss | Above the break bar (short) | 157 |
| Exits: profit-taking | Next support level | 157 |
| Exits: trailing / time / signal | None | |
| Position sizing | 1-2% risk | 135 |
| Adding to / pyramiding | Not stated | |
| Portfolio limits (max positions, correlation, heat) | Not stated | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Close condition | within the mother bar range | | 148 |
| Fib levels | 50% and 61% | | 154 |
| Levels list | S/R, S/D, Fib, 21 MA, trend lines, horizontals | | 151 |

**Key quotes**
- "breaks out from the inside bar pattern and then quickly reverses to close within the range of the mother bar" [p. 148]
- "You place a selling order after the close of the break bar, and you set your stop loss above it" [p. 157]
- "not all false breakouts are worth trading" [p. 157]

**Pseudocode**
```
inside[t-1] relative to t-2 (mother). On bar t: H[t]>H[t-2] (break up) and close[t] < H[t-2] and close[t] > L[t-2]
-> bearish false break; if downtrend/at resistance level: short at close[t]; stop = H[t]; target next support
bullish mirror: L[t]<L[t-2] and close[t]>L[t-2] -> buy at close[t]; stop = L[t]; target next resistance
```

**Ambiguities & assumptions**
- Whether the break must be a single bar or may take several bars to fail; book says "quickly". ASSUMPTION: within 1-2 bars after the inside bar.
- Bullish case entry/stop mirror not written out separately [p. 149-150]. ASSUMPTION: mirror image.
- Example "risking say 50 points for 400 points profits" [p. 157] is illustrative, not a parameter.

### 2.8 Counter-trend setups at higher-timeframe levels (top-down)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Counter-trend reversal | 74 |
| Timeframe & holding period | Weekly for level, daily for signal | 75 |
| Universe / eligibility filters | None | |
| Market / regime filter | Price at an important weekly support/resistance, rejected twice; for experienced traders only | 75, 77 |
| Setup conditions | Daily pin bar and/or inside bar false breakout near the weekly level | 75, 76 |
| Entry trigger & order type | As 2.1 / 2.7 | |
| Initial stop-loss | As 2.1 / 2.7 | |
| Exits: profit-taking | Not specified | |
| Exits: trailing / time / signal | None | |
| Position sizing | As elsewhere | 135 |
| Adding to / pyramiding | Not stated | |
| Portfolio limits (max positions, correlation, heat) | Not stated | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Frames | weekly then daily; 4H then weekly+daily | 1H uses daily | 70 |

**Key quotes**
- "if the weekly and the daily charts analysis align with the 4h chart, you can then take your trading decision" [p. 70]
- "if you are a beginner, i highly recommend you to stick with the trend" [p. 77]

**Pseudocode**
```
weekly_level = swing high/low touched twice with rejection
if daily signal (pin bar or inside-bar false break) at weekly_level against daily trend: use 2.1/2.7 entry/exit rules
```

**Ambiguities & assumptions**
- Exits not specified beyond examples. ASSUMPTION: target next daily S/R, min 2R.
- This is a filter/variant rather than a separate system; keep as an optional overlay in backtests.

### 2.9 Other candlestick patterns (definitions, no trade rules)
Pattern definitions only, "not going to show you how to trade them" [p. 14]; each "can't be traded alone": bullish/bearish engulfing [p. 16-18], Doji [p. 20-22] (at trend end, take profits [p. 22]), dragonfly [p. 23] and gravestone Doji [p. 25-26] (must be near resistance [p. 26]), morning star [p. 28] (third candle gaps up and closes above midpoint of first body [p. 28]) and evening star [p. 31], hammer [p. 34], shooting star [p. 37] (shadow twice body [p. 37]), Harami [p. 40], tweezers top/bottom [p. 43-45]. Not testable as standalone strategies; they are usable as filter/flags only. Gaps are rare on forex but common on NSE daily data.

## 3. Risk & money-management rules
- Risk no more than 2% of equity per trade; 1% for beginners [p. 135].
- Only take trades with reward at least 2x the risk; "Don't never enter a trade in which the profit is less than the amount of money you risked" [p. 163]; 3:1 example [p. 134].
- Always place a hard stop-loss; no mental stops [p. 165]. Set stop and target, then "don't never look back" [p. 135].
- Think in dollars risked, not pips; position size from lots/pip value [p. 162-163].
- Do not risk money you cannot afford to lose; start small [p. 165-166].
- Expect losing streaks; case study 3 wins and 7 losses at 3:1 still profitable [p. 134].
- Do not trade choppy markets [p. 79]; smaller time frames produce false signals [p. 70].
- No portfolio heat, max-position or drawdown rules are given (not found in this book).

## 4. Non-codable guidance
- Learn pattern psychology, not names [p. 45-46]; practice screen time [p. 50].
- Banks stop-hunt novices; false breakout is the "manipulation" explanation [p. 148].
- Quality setups are no guarantee; supply and demand moves the market [p. 82].
- Be patient, sniper-like selectivity [p. 99]; accept losses [p. 135].
- Counter-trend trading needs experience [p. 77]; keep the analysis simple [p. 77].
- Practise before funding an account [p. 108].

## 5. Adapting to NSE (Indian equities)
- **Data required:** daily OHLC (volume optional); weekly bars derived from daily; NIFTYBEES/equal-weight index for market trend context (optional). No fundamentals or delivery % needed.
- **Testability with our data:** all rules are price-based and backtestable on 2005-2026 daily data. 4H and 1H cannot be tested (daily only); restrict to daily with weekly as higher frame. Discretionary parts (what counts as trend, key level, "choppy") need formal proxies and are the main source of error.
- **Market-structure differences:** The book was written for forex (pips, lots, mini lots [p. 162-163]) and never mentions stocks. Forex trades 24 hours with few gaps; NSE has overnight gaps and circuit limits, so stops can slip and morning/evening star gap rules may behave differently.
  - ASSUMPTION: test long side only; short signals (bearish pin bars, engulfing, false breakouts) become "exit/avoid" signals since overnight shorting is not possible in the cash market.
  - ASSUMPTION: apply a liquidity filter (e.g. 20-day average traded value above a threshold) as the book has none.
  - ASSUMPTION: include STT/brokerage and 0.1% slippage; fixed-fractional sizing at 1% risk with stop at pattern low, capped position size at e.g. 10-20% of equity because stops may be tight.
  - ASSUMPTION: no weekly Fibonacci automation beyond last impulse leg between confirmed swings.

## 6. Verdict
- **Codeability:** Partly: entry patterns, stops, 2:1 target filter and sizing are codable; trend, key-level and confluence identification are discretionary and need proxy definitions.
- **Priority for backtesting:** Low to Medium: no tested evidence is given, the logic is classic and largely discretionary, and shorting (half the signals) is not available; the long-only pin bar/engulfing/inside-bar-at-support variants are cheap to test.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating raw candlestick patterns as signals without the trend + level + higher-timeframe filters the author insists on [p. 79, 96].
  2. Pattern definitions: pin bar thresholds, engulfing body vs range [p. 16 vs 111], inside bar vs Harami [p. 40 vs 137].
  3. Entry timing and stops: aggressive entry at close with stop beyond the tail/pattern, vs breakout entry above the mother bar, vs 50% retracement limit orders that may not fill [p. 93, 141].
