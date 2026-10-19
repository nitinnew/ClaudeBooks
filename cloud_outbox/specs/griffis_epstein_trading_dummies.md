# Trading For Dummies, 2nd Edition — Michael Griffis and Lita Epstein

- **Source file:** Google Drive "Trading for Dummies ( etc.) (z-lib.org).pdf" (387 pages); Wiley Publishing, copyright 2009 (2nd edition) per the copyright page [p. 4]
- **Text file used:** text/griffis_epstein_trading_dummies.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - N is taken ONLY from the nearest `[[PAGE N]]` marker above the passage. Printed page numbers (running heads, contents, index) are never used; they are offset by 18 from the PDF index.
  - Table "Page" columns hold the bare PDF page number(s).
  - Verified with `verify_citations.py` before finishing (see Coverage).
- **Coverage:** Text file has 17,145 lines and 387 `[[PAGE N]]` markers. Read sequentially with the Read tool: lines 1-11100 and 11190-15166 (front matter, Parts I-VI, chapters 1-22, up to `[[PAGE 367]]` where the index begins). Not read row by row: lines 11101-11189 (numeric spreadsheet rows of Figure 15-1, inside `[[PAGE 269]]`; the table's first and last rows and the surrounding text were read). Index (lines 15157-17089, `[[PAGE 367]]`-`[[PAGE 386]]`) was only spot-read (first 10 lines) and checked by script for any non-index prose (no line longer than 70 characters) and for stop/pyramiding/position-trading terms: it holds only terms and printed page numbers, no rules. Back cover (`[[PAGE 387]]`) read; marketing copy only. Last `[[PAGE N]]` reached: 387. Chapters 1-4 (brokers, computers), 7 (analyst calls), 18-20 (derivatives, forex, licences) were read at normal pace and contain no testable stock rules. Charts are images and are not in the text; no pages were garbled beyond occasional OCR hyphenation. *Coordinator check: the coordinator re-ran verify_citations (74/74 ok) and an exact-page strict check (0 off-by-one), and confirmed all 22 field tables have exactly the 12 template rows. 10 unquoted citations were spot-checked by grep: 20-day Donchian test p.268-271 (18 losing trades p.269), 50-day EMA system p.265-266, 50-day MA p.193, bullish percent index p.227/230, curve fitting p.194/200/267, higher-low trailing stops p.168-178/216-217, 5-6% and 1-2% loss caps, Wiley 2nd edition p.4; all matched. The two parts not read row by row (the Figure 15-1 numeric rows at lines 11101-11189 and the index pages 367-386) are stated in the Coverage line.*

## 1. The method in brief

The authors (Griffis, a stockbroker/trader, and Epstein, a financial writer) teach **position trading**: entering and exiting stocks (and ETFs) on trends that last "a few weeks or months and maybe even a year or more" [p. 19], using daily and weekly bar charts [p. 140]. The method is a top-down funnel: (1) fundamental macro read of the business cycle and sector rotation, (2) classify the market into six phases (bullish transition, bull, bullish pullback, bearish transition, bear, bearish pullback) using weekly index charts, weekly MACD and the bullish percent index [p. 221, p. 227, p. 229], (3) pick the "strongest stocks in the strongest sectors" with growing earnings and high relative strength [p. 233], (4) enter on simple chart events — chiefly a breakout from a long trading range, a pullback after the breakout, a cup-and-handle, or a double bottom [p. 142, p. 162, p. 163], and (5) manage risk with stops set at the technical point where the trade has "failed", trailing stops under higher lows, and exit when the trend ends [p. 213, p. 217].

The claimed edge is not predictive power: "Technical analysis is not a forecasting tool. It is a trading tool and nothing more." [p. 138]. The edge is discipline — short losses, let profits run, trade with the dominant trend, avoid bottom-fishing, averaging down and chasing. The authors give **no systematic backtest or track record**. The only quantified results in the book are illustrative: a 20-day Donchian breakout test on QQQQ that "lost money during the entire test period" with 30 trades of which 18 lost [p. 268, p. 269]; a hypothetical short-ETF trade stopped out for a 4.2 percent loss [p. 250]; and a few pullback swing trades in one stock (NOV) [p. 281, p. 282]. Treat every rule below as a hypothesis to test, not a proven edge. Chapters 18-20 (derivatives, forex, licences) contain no testable stock rules; the authors state of swing/day trading, derivatives and forex: "We definitely won’t be sharing any strategies for actually participating in these types of trading" [p. 22].

## 2. Strategies

Conventions used in all sections below: "daily bar" means NSE daily OHLCV; "tomorrow's open" is the next session's opening price; "avg volume" is the average daily volume over a look-back the book does not specify (ASSUMPTION: 50 sessions, excluding the signal day). Where the book gives US-dollar amounts (5 or 10 cents, 25 cents per share) these are converted to percent-of-price assumptions in the Ambiguities of each strategy.

### 2.1 Trading-range breakout (confirmed entry)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout / trend-following entry from a base | 142, 155 |
| Timeframe & holding period | Daily and weekly charts; position trade held for weeks to months (trend lasting at least several weeks to several months) | 140, 154 |
| Universe / eligibility filters | Strongest stocks in strongest sectors with high relative strength; leading stock in a leading industry; earnings growing faster than average; actively traded (low-volume stocks are hard to exit); avoid stocks without earnings for long trades; avoid small, thinly traded companies | 160, 201, 232, 233, 101 |
| Market / regime filter | Trade with the dominant trend: buy breakouts and take full positions in a bull market phase; small partial positions in a bullish transition; confirm on the chart one time period higher (daily on weekly) | 234, 233, 357 |
| Setup conditions | Stock range-bound (support = lower boundary, resistance = upper boundary) for at least six to eight weeks, preferably longer; boundaries drawn from closing prices on daily/weekly bars; longer and tighter ranges give better breakouts | 158, 159, 161 |
| Entry trigger & order type | Resistance zone violated by a significant amount (more than 5 or 10 cents) on volume at least 50 percent above average (more is better); wait at least one day, possibly two or three, to confirm the stock does not fall back into the range; alternative: GTC buy-stop slightly above breakout price only if market is in bull phase, range is long and tight and breakout obvious | 159, 161, 243 |
| Initial stop-loss | Approach 1: exit immediately if price falls back below the resistance level (tight, whipsaw-prone). Approach 2: exit below the mid-point of the trading range (wider, fewer whipsaws; favoured by position traders). Authors do not recommend a fixed-percentage stop. Keep stop a few cents away from the obvious price | 213, 214, 244 |
| Exits: profit-taking | No fixed target stated; ride the trend and trim into a runaway move ("consider trimming your position as the stock reaches for the stratosphere") | 359 |
| Exits: trailing / time / signal | Raise stop to the most recent higher low (or the one before) after each higher high; exit on trend-end signals (see 2.20) | 217, 216 |
| Position sizing | Hypothetical: $100,000 portfolio, 10 positions, $10,000 (10 percent) each; half-size ($5,000) in bullish transition; loss per position kept below 5-6 percent, or 1-2 percent of total trading capital | 236, 206 |
| Adding to / pyramiding | Add to winners only when the system triggers new signals in the direction of the trend; never average down | 359 |
| Portfolio limits (max positions, correlation, heat) | Start with 10-15 positions; hard to justify more than 20; in bullish transition commit no more than 40-50 percent of capital; fully invested in a bull market | 360, 236, 234 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Minimum base length | 6-8 weeks, preferably longer | longer ranges better | 158, 161 |
| Breakout margin above resistance | more than 5 or 10 cents | none | 159 |
| Breakout volume vs average | at least 50 percent above average | BAX example: nearly 3x average (8M vs 2.7M) | 159, 160 |
| Confirmation wait | 1 day, possibly 2-3 days | immediate buy-stop in strong bull phase | 161, 243 |
| Boundary definition | closing prices | intraday highs/lows | 159 |
| Stop level | resistance level or range mid-point | none; no percent stop | 213 |
| Risk per position | below 5-6 percent of position, or 1-2 percent of capital | none | 206 |

**Key quotes**

- "we want to see the stock trade through its resistance zone on much higher volume than the average" [p. 159]
- "Waiting for a short while — at least one day, possibly two or three — to confirm the trading range breakout can be helpful" [p. 161]
- "Finding a good trading signal is important; avoiding bad trading signals is more important." [p. 161]
- "We prefer using closing prices on a daily or weekly bar chart to define the upper and lower boundaries" [p. 159]
- "if the ETF were to fall below the resistance line ($67.47) after it breaks out above it, you should exit." [p. 213]

**Pseudocode**

```
for each stock S, each day t (after close):
  base = last N_base closes where (max(close) - min(close)) / mean(close) small   # ASSUMPTION below
  if len(base) < 40 sessions: continue
  R = max(close over base);  Sup = min(close over base);  Mid = (R + Sup)/2
  if close[t] > R*(1+margin) and volume[t] >= 1.5*avgvol and market_phase in {bull, bullish_pullback, bullish_transition}:
      mark S as "breakout signal" on day t
  if S has breakout signal and for the next k=2 sessions close stays > R:
      BUY at open of day after confirmation (size per phase: full in bull, half in transition)
  stop = R (tight variant) or Mid (position-trader variant)
  every day: if close < stop (or low < stop for intraday trigger): SELL at next open
  trail: after each new swing high, stop = max(stop, most recent higher low)
```

**Ambiguities & assumptions**

- Range tightness and "narrow" are visual in the book. ASSUMPTION: base counts only if (highest close - lowest close) / average close over the base is <= 15 percent for >= 40 trading sessions.
- 5 or 10 cents has no scale for NSE prices. ASSUMPTION: breakout close >= resistance close x 1.002 (0.2 percent) as the minimum margin.
- Volume lookback not given. ASSUMPTION: 50-session average volume.
- The book mentions both a one-to-three day wait and an immediate buy-stop; ASSUMPTION: use the 2-day confirmation as the default and test the immediate version as a variant.
- Stop: book offers two approaches (resistance or mid-point) and says position traders prefer the second; ASSUMPTION: test both, default to the range mid-point. Skip entries where (entry - stop)/entry exceeds 10 percent (book says keep loss per position below 5-6 percent but gives no filter; this is an addition).
- Not found in this book: ATR-based stops, position sizing by risk formula, profit target.

### 2.2 Pullback entry after a range breakout (authors' favourite)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout-retest / pullback entry | 142 |
| Timeframe & holding period | Daily bars; days to weeks of setup, then weeks to months hold | 142, 154 |
| Universe / eligibility filters | Same as 2.1: strongest stocks in strongest sectors, high relative strength, growing earnings | 233, 201 |
| Market / regime filter | Same as 2.1; more caution on second and later breakouts and in transition or pullback market phases | 243, 234 |
| Setup conditions | (1) High-volume breakout from a long range, (2) pullback on low volume, (3) price near the old resistance (former resistance often turns into support) | 142, 163 |
| Entry trigger & order type | Buy immediately as the stock begins trading higher after the low-volume pullback (described as a relatively low-risk, high-reward trade) | 142 |
| Initial stop-loss | Not separately stated; by the book's logic the trade has failed if price falls back into the range (below resistance) or below the mid-point | 213, 214 |
| Exits: profit-taking | Not found in this book (no target) | - |
| Exits: trailing / time / signal | Higher-low trailing stop and trend-end exits (2.20) | 217 |
| Position sizing | As 2.1 | 206, 236 |
| Adding to / pyramiding | As 2.1 | 359 |
| Portfolio limits (max positions, correlation, heat) | As 2.1 | 360 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pullback volume | "low volume" (no number) | none | 142 |
| Pullback depth | back to near the breakout level (XYZ example: back to $19 after a surge to $21 from a $17-$18.75 range) | none | 141 |
| Re-entry volume | high-volume buying resumes | none | 142 |

**Key quotes**

- "Of these three alternatives, our favorite is the middle one" [p. 142]
- "Buy immediately as the stock begins trading higher after the low-volume pullback." [p. 142]
- "If you miss the breakout entry point for a stock that you want, waiting is better than entering a position as a trend accelerates." [p. 358]

**Pseudocode**

```
on breakout day B (per 2.1 definitions, high volume):  record R, avgvol, B
for days B+1 .. B+20 (ASSUMPTION window):
   pullback_ok = close < close[B] and mean(volume[B+1..t]) < avgvol and low[t] >= R*(1 - tol)
   if pullback_ok and close[t] > close[t-1] and volume[t] > volume[t-1]:
        BUY at next open
stop: close < R (tight) or < Mid (loose); trail as 2.1
```

**Ambiguities & assumptions**

- The book never defines "low volume" or how deep a pullback may be. ASSUMPTION: pullback average volume < 50-session average; pullback low must stay within 3 percent below resistance; look-back 20 sessions after breakout.
- "Begins trading higher" is not defined. ASSUMPTION: first up-close with volume above the previous session's volume.
- The book says former resistance acts as support [p. 163]; no stop distance is quantified for this variant. ASSUMPTION: stop 1 percent below the pullback low.
- Not found in this book: targets, time stop.

### 2.3 Cup and handle breakout

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout (transition pattern) | 162 |
| Timeframe & holding period | Daily bars; weeks-to-months trend ride | 162, 154 |
| Universe / eligibility filters | As 2.1 | 233 |
| Market / regime filter | As 2.1 | 234 |
| Setup conditions | Rounded, saucer-shaped bottom (cup) followed by a modest shakeout (handle) | 162 |
| Entry trigger & order type | Trigger: price breaks above the handle on high volume (AAPL example: late April, small breakout gap) | 163 |
| Initial stop-loss | Not stated for this pattern ("you need an exit strategy"); former resistance acts as support after the break | 163 |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | As 2.20 | 217 |
| Position sizing | As 2.1 | 206 |
| Adding to / pyramiding | As 2.1 | 359 |
| Portfolio limits (max positions, correlation, heat) | As 2.1 | 360 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Cup depth / length | not given | visual | 162 |
| Handle definition | "modest shakeout formation" | visual | 162 |
| Breakout volume | "high volume" (use 2.1: at least 50 percent above average) | none | 163 |

**Key quotes**

- "The trigger occurs when the stock price breaks above the handle on high volume." [p. 163]
- "The cup and handle is a reliable trading pattern, but that doesn’t mean the pattern never fails." [p. 163]

**Pseudocode**

```
detect cup: price falls from left rim L to bottom B and recovers to ~L over >= 30 sessions (rounded: low-curvature test)   # ASSUMPTION
detect handle: shallow pullback of <= 1/3 of the cup depth lasting 5-20 sessions after right rim
if close > max(high of handle) and volume >= 1.5*avgvol: BUY next open
stop: below handle low;  trail as 2.1/2.20
```

**Ambiguities & assumptions**

- The book gives no numeric definition of cup or handle. ASSUMPTION: cup depth 15-35 percent, length 30-120 sessions, handle retraces <= one third of the cup depth over 5-20 sessions, stop below the handle low.
- Fully discretionary pattern recognition; low priority for coding.

### 2.4 Double-bottom breakout (standard entry)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal / transition breakout | 163 |
| Timeframe & holding period | Daily; weeks to months | 163, 154 |
| Universe / eligibility filters | As 2.1 | 233 |
| Market / regime filter | As 2.1 | 234 |
| Setup conditions | W shape (need not be perfect); authors prefer the right-hand trough slightly lower than the left (shakes out weak owners) | 163 |
| Entry trigger & order type | Break above the mid-point peak between the two troughs (the pivot point), ideally on higher-than-average volume (NEM: trigger just below $43, volume more than 15M = 50 percent above average) | 163 |
| Initial stop-loss | Not specified for the standard entry; the alternative entry uses the low of the reversal bar | 164 |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | As 2.20 | 217 |
| Position sizing | As 2.1 | 206 |
| Adding to / pyramiding | As 2.1 | 359 |
| Portfolio limits (max positions, correlation, heat) | As 2.1 | 360 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trough spacing | NEM example June 2007 and Aug 2007 (about 2 months) | not stated as a rule | 163 |
| Right trough vs left | slightly lower preferred | not required | 163 |
| Breakout volume | higher than average (example 50 percent above) | none | 163 |

**Key quotes**

- "the trigger point occurs when the stock breaks above the mid-point peak between the two troughs" [p. 163]
- "Ideally, higher-than-average volume confirms the trigger." [p. 163]

**Pseudocode**

```
find swing lows L1 < L2-ish (L2 within [-5%, +2%] of L1) separated by 20-60 sessions with a swing high P between them (pivot)   # ASSUMPTION
if close > P and volume >= 1.5*avgvol: BUY next open
stop: below min(L1, L2)   # ASSUMPTION; book: failure = below lowest low
```

**Ambiguities & assumptions**

- No numeric trough tolerance or spacing. ASSUMPTION as in pseudocode; stop below the lowest low (consistent with the aggressive variant's "falls below the lowest low" failure rule [p. 164]).

### 2.5 Double bottom — aggressive early entry on single-day reversal

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion / early reversal entry | 164 |
| Timeframe & holding period | Daily; hold until price tests the pivot point | 164 |
| Universe / eligibility filters | Aggressive traders only; "W" particularly deep, pivot many points above the trough | 164 |
| Market / regime filter | Not stated | - |
| Setup conditions | Price holds near or just below the left-hand trough; volume confirms the reversal; or a single-day reversal pattern confirms | 164 |
| Entry trigger & order type | Enter on the trading day after the single-day reversal bar at the right trough (NEM buy trigger 16 Aug, entry next day) | 164 |
| Initial stop-loss | Below the low of the reversal bar (NEM: below $37.60); failed if the stock falls below the lowest low | 164 |
| Exits: profit-taking | Hold until the stock tests the pivot point | 164 |
| Exits: trailing / time / signal | Exit if price falls below the lowest low | 164 |
| Position sizing | Risk "relatively small" because of the nearby stop; no size rule beyond section 3 | 164, 206 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry timing | next trading day after reversal bar | none | 164 |
| Stop | below reversal bar low | below lowest low | 164 |
| Target | pivot point (mid-point peak) | none | 164 |

**Key quotes**

- "your stop would be below $37.60, the low for that reversal bar." [p. 164]
- "If the stock falls below the lowest low, you’ll know your trade has failed and you must exit." [p. 164]

**Pseudocode**

```
if W-pattern left trough L1 exists and day t is a bullish reversal bar (open near high, close at/near high after intraday dip, see 2.22)
   and low[t] within [-3%, +3%] of L1 and volume[t] >= avgvol:
      BUY at open t+1;  stop = low[t];  target = pivot P
exit: low < stop -> sell; high >= P -> sell (or hand to 2.4 rules)
```

**Ambiguities & assumptions**

- "Particularly deep" and "many points away" are undefined. ASSUMPTION: pivot >= 15 percent above the trough.
- Book calls this aggressive; risk/reward unquantified.

### 2.6 Bear-trap long (failed downside breakout)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Failed-signal reversal | 163 |
| Timeframe & holding period | Daily; weeks to months | 163 |
| Universe / eligibility filters | Stock meets all fundamental criteria; earnings strong and growing; sector performing well; economy on an upswing | 181, 182 |
| Market / regime filter | Economy on an upswing | 182 |
| Setup conditions | Downside breakout from a trading range that preceded by a long period of declining prices; price reverses and re-enters the range (bear trap) | 163 |
| Entry trigger & order type | Enter a long position as soon as the stock price re-enters the trading range | 163 |
| Initial stop-loss | Not stated | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | If a failed signal occurs on an open position, exit | 181 |
| Position sizing | As section 3 | 206 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Prior decline | "long period of declining prices" | undefined | 181 |
| Re-entry | back inside prior range | none | 181 |

**Key quotes**

- "you may want to enter a long position as soon as the stock price reenters the trading range." [p. 181]
- "selling pressure has evaporated in the stock" [p. 181]

**Pseudocode**

```
if close[t-1] < Support (downside breakout from range of >= 40 sessions, prior downtrend) and close[t] >= Support:
   if fundamentals_ok(S) and sector_strong(S): BUY next open
stop: ASSUMPTION low of the trap bar
```

**Ambiguities & assumptions**

- Fundamental conditions (forward-test only on our data). Stop not given; ASSUMPTION: below the lowest low of the failed breakdown.

### 2.7 Simple moving-average slope-and-cross system (long side; authors' confirmation variant)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following | 191 |
| Timeframe & holding period | Daily closes; DIA example 30-day SMA, held from 24 Jul 2006 to 27 Feb 2007 (about seven months) | 191 |
| Universe / eligibility filters | Stock must be trending; fails when range-bound; period must be chosen carefully | 191 |
| Market / regime filter | Not stated for this system (authors elsewhere want the dominant trend and the economic cycle considered) | 174 |
| Setup conditions | Moving average slopes upward | 191 |
| Entry trigger & order type | Buy when the MA slopes upward and the closing price crosses above the MA. Authors' tempering: require price to stay above the SMA for several days after the signal before entering | 191, 192 |
| Initial stop-loss | No separate stop; position is closed when price closes below the MA | 191 |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Close the position when price closes below the MA; authors want several days below the SMA (or another coincident sell signal, e.g. a chart pattern from chapter 10) before exiting | 191, 192 |
| Position sizing | Not found in this book for this system (see section 3) | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

Short side in the book (sell short when MA slopes down and close crosses below; cover when close above MA) [p. 191] is not tradable on NSE cash and is excluded.

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| MA type | SMA in the DIA example | EMA also described | 191, 186 |
| MA length | 30-day (example) | authors use a 30-day or 50-day SMA for exits; nine-period called nearly useless | 191, 193 |
| Confirmation days (entry) | "several days" | no number | 192 |
| Confirmation days (exit) | "several days"; elsewhere "a couple of days" | no number | 192 |
| Slope test | MA slopes upward (no formula) | no formula | 191 |

**Key quotes**

- "Buy when the moving average slopes upward and the closing price crosses above the moving average." [p. 191]
- "Close the position when the price closes below the moving average." [p. 191]
- "These trend-following systems fail miserably when a stock is range bound" [p. 191]
- "we might temper the buy signal in the simple mechanical strategy described earlier" [p. 192]

**Pseudocode**

```
sma = SMA(close, 30)
slope_up = sma[t] > sma[t-1]            # ASSUMPTION: 1-day slope; test 5-day
buy_signal = slope_up and close[t] > sma[t] and close[t-1] <= sma[t-1]
enter at open t+1 only if close stays > sma for next 2 sessions (ASSUMPTION: "several days" = 2-3)
exit: close < sma for 2 consecutive sessions -> sell at next open (ASSUMPTION 2 days)
```

**Ambiguities & assumptions**

- "Several days" is undefined; ASSUMPTION 3 days entry confirmation and 2 days exit confirmation (the book says "a couple of days" for the exit on p. 192).
- MA length for entry is not specified beyond the 30-day chart example; ASSUMPTION: 30-day SMA and a 50-day variant.
- The book warns of whipsaws and says the DIA exit came during a retracement; no remedy is quantified.

### 2.8 Long-period SMA as trend-health exit, with buy-on-pullback entry

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (exit rule) plus pullback entry | 193 |
| Timeframe & holding period | Daily chart; hold while the trend lasts | 193 |
| Universe / eligibility filters | Stocks already in an uptrend (price riding above rising SMA) | 193 |
| Market / regime filter | If economy appears near a peak (chapter 5), tighten exits and shorten the SMA | 193 |
| Setup conditions | Rising SMA; stock trades down toward the SMA and reverses | 192, 193 |
| Entry trigger & order type | Position traders: second-chance entry (buy on a pullback) after missing the first breakout; short-term traders buy when price closes near or just below a rising MA | 193 |
| Initial stop-loss | Not stated for the pullback entry | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Exit when price closes below the long-term SMA and stays below for a couple of days; use as one of several exit signals | 192 |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| SMA length for exit | 30-day or 50-day | 50-day if the trend has existed for a relatively long period; shorter when economy nears a peak | 193 |
| Days below SMA before exit | "a couple of days" | none | 192 |

**Key quotes**

- "we use a long-period SMA to monitor the health of a trend" [p. 193]
- "if the price closes below a relatively long-term moving average and remains below it for a couple of days, we use that signal to exit our position" [p. 192]
- "Typically, we select either a 30-day or 50-day SMA, depending on the duration of the existing trend" [p. 193]

**Pseudocode**

```
trend_len = days since the trend (higher highs/higher lows) began
N = 50 if trend_len is long (ASSUMPTION > 120 sessions) else 30; if market_phase is bearish_transition: N = 30
exit: close < SMA(N) for 2 consecutive sessions -> sell next open
pullback_entry (optional): SMA(N) rising and close[t] <= SMA(N)*1.01 and close[t] > close[t-1] -> buy next open
```

**Ambiguities & assumptions**

- "Relatively long period" and "economy nearing a peak" are discretionary. ASSUMPTION: 50-day if the stock's uptrend is older than 120 sessions or the Nifty proxy shows a bearish transition (2.11); else 30-day.
- Pullback proximity ("near or just below") is undefined. ASSUMPTION: within 1 percent above to 2 percent below the SMA.

### 2.9 Slow stochastic (14,3,3) buy signal inside an uptrend

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Momentum timing within trend | 196 |
| Timeframe & holding period | Chart timeframe not stated (Apple example spans several months, signals in Feb, April, August, November); position horizon | 195 |
| Universe / eligibility filters | Stock in a dominant uptrend | 196 |
| Market / regime filter | Not stated | - |
| Setup conditions | Slow stochastic (N typically 14, %K smoothed by 3, %D = 3-period MA of %K); in an uptrend | 194, 196 |
| Entry trigger & order type | Buy when the oscillator moves from below to above 20 percent | 195 |
| Initial stop-loss | Not stated | - |
| Exits: profit-taking | Sell signal (from above to below 80) is generated by the indicator but "few ... represented good selling" while trending higher | 195 |
| Exits: trailing / time / signal | Not stated; use other exits (2.20) | - |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| N | 14 | other time frames possible | 194 |
| Slowing | 3-period MA of fast %K | MA period and SMA/EMA type configurable | 194, 195 |
| %D | 3-period MA of %K | none | 194 |
| Oversold / overbought | 20 / 80 | none | 195 |

**Key quotes**

- "When the stochastic oscillator moves from below to above 20 percent, triggering a buy signal" [p. 195]
- "readings that stay above 80 percent or below 20 percent are not enough to generate trading signals" [p. 195]
- "The stochastic oscillator signals many overbought conditions within an uptrend and rarely generates useful sell signals." [p. 196]
- "that generates too many signals, a very high percentage of which are false" [p. 195]

**Pseudocode**

```
fastK = 100*(close - LL14)/(HH14 - LL14);  slowK = SMA(fastK, 3);  slowD = SMA(slowK, 3)
uptrend = rule from 2.20 (higher highs and higher lows) or close > SMA(50) rising
buy if uptrend and slowK[t-1] < 20 and slowK[t] >= 20 -> buy next open
```

**Ambiguities & assumptions**

- The book does not say which line (%K or %D) crosses 20; ASSUMPTION: slow %K. Exit/stop not given; combine with 2.20.

### 2.10 Weekly MACD (12, 26, 9) trend signal

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following indicator | 196 |
| Timeframe & holding period | Weekly charts (authors' preference) | 197 |
| Universe / eligibility filters | Stocks, ETFs and broad indexes | 198 |
| Market / regime filter | Used to classify the market (see 2.11) | 229 |
| Setup conditions | MACD = EMA12 - EMA26 of closes; signal line = EMA9 of MACD | 196, 197 |
| Entry trigger & order type | Uptrend signalled when the MACD line crosses above the centre (zero) line; downtrend when it crosses below. MACD crossing above its signal line is only an early indication of a possible new uptrend | 198 |
| Initial stop-loss | Not stated | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | MACD below zero line = downtrend signal; divergences are warnings (bearish divergence: price higher highs, MACD lower highs) | 198, 199 |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fast / slow / signal EMA | 12 / 26 / 9 periods (weekly bars) | other traders vary; Appel uses different values; risk of curve fitting | 197, 200 |
| EMA seed | first close or SMA of first N | either method | 187 |

**Key quotes**

- "When using MACD, we prefer weekly charts." [p. 197]
- "we prefer using the position of the MACD line relative to the zero line as an indication that the stock has begun trending" [p. 198]
- "a divergence that is counter to the dominant trend is less likely to be a reliable trading signal" [p. 199]

**Pseudocode**

```
weekly_close -> ema12, ema26 ; macd = ema12 - ema26 ; sig = ema(macd, 9)
uptrend_flag = macd > 0 ; trend_start_signal = macd[t-1] <= 0 and macd[t] > 0
early_warning = macd crosses above sig while macd < 0
bear_div = price makes higher highs while macd makes lower highs
```

**Ambiguities & assumptions**

- The book gives no entry/exit trade rules for individual stocks from MACD alone beyond identifying a trend; ASSUMPTION: use as a filter or entry trigger in combination with 2.1/2.2; EMA seeding differences change early values (book warns about inconsistency [p. 189]), so use a long warm-up.

### 2.11 Six-phase market regime model with phase-based exposure (chapter 13)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Market-timing / regime allocation overlay | 221 |
| Timeframe & holding period | Weekly index charts; check weekly or monthly | 227, 222 |
| Universe / eligibility filters | Broad market index (S&P 500, Nasdaq Composite) or a high-volume index ETF | 228, 232 |
| Market / regime filter | Phases: bullish transition, bull market, bullish pullback, bearish transition, bear market, bearish pullback | 221 |
| Setup conditions | Bull market: MACD line > zero and > trigger line, series of higher highs and higher lows. Bear market: MACD < zero and < trigger, lower highs and lower lows. Bullish transition or bearish pullback: MACD < zero and crosses above trigger. Bearish transition or bullish pullback: MACD > zero and crosses below trigger. Bullish percent index (BPI) used to separate transition from pullback | 228, 229, 230 |
| Entry trigger & order type | Bullish transition: small partial positions, strongest stocks in strongest sectors, range breakouts, tight stops, ETF if needed. Bull market: buy breakouts and take full positions, fully (100 percent) invested, no new shorts. Bullish pullback: continue full positions on breakouts but selective | 233, 234 |
| Initial stop-loss | Bullish transition: keep stops very tight and honor them. Bull: may loosen stops a bit. Pullbacks and transitions: tighten stops | 234, 235 |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Bearish transition: tighten stops on all positions, exit any long at first sign of trouble. Bear market: no new longs, exit existing longs at first sign of trouble. Bearish pullback: no new longs | 235 |
| Position sizing | $100,000 example: half-size $5,000 positions in bullish transition (20 percent committed), cap 40-50 percent in transition; full $10,000 positions (10 positions) in bull; leverage up to 2x allowed; become more conservative after each pullback | 236, 237 |
| Adding to / pyramiding | In bullish transition add small positions as stocks break out; in bull add to existing positions or new leaders | 236 |
| Portfolio limits (max positions, correlation, heat) | Keep the number of positions small; transition cap 40-50 percent of capital | 236 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| MACD | 12/26/9 weekly (trigger line = 9 EMA signal) | none | 197, 229 |
| BPI oversold/overbought | below 30 percent / above 70 percent | needs 6 percent change to flip | 230 |
| BPI reversal trigger | 6 percent change in stocks on buy signals | none | 230, 231 |
| Transition exposure | 20 percent initial, cap 40-50 percent | none | 236 |
| Bull exposure | 100 percent, optionally leveraged to about 200 percent | none | 236 |
| Index trend filter | S&P 500 closing well below its 52-week MA = deterioration example | none | 217 |

**Key quotes**

- "A bull market is indicated when the MACD line is greater than the zero line and greater than the trigger line." [p. 229]
- "In a bull market, your primary goal is to become fully invested." [p. 234]
- "The idea: Trade aggressively when you’re confident in your market assessment, but protect your capital when you’re uncertain." [p. 233]
- "When you’re certain a bear market has begun, don’t enter new long positions." [p. 235]
- "set an upper limit to the amount of capital that you’re willing to commit during a bullish transition phase" [p. 236]

**Pseudocode**

```
weekly index series (NIFTYBEES or equal-weight index of the stock panel; Nifty index only from 2024)
macd, sig = weekly MACD(12,26,9)
hh_hl = last two swing highs and lows rising ; lh_ll = both falling
if macd>0 and macd>sig: phase = BULL
elif macd<0 and macd<sig: phase = BEAR
elif macd<0 and cross_up(macd,sig): phase = BULLISH_TRANSITION_or_BEARISH_PULLBACK
elif macd>0 and cross_down(macd,sig): phase = BEARISH_TRANSITION_or_BULLISH_PULLBACK
disambiguate transition vs pullback with BPI state or prior-phase memory (see ambiguities)
exposure: BULL 100% ; BULLISH_PULLBACK 100% selective with tighter stops ; BULLISH_TRANSITION <=20% initial, cap 40-50% ;
          BEARISH_TRANSITION no new longs, exit on first weakness ; BEAR 0% long ; BEARISH_PULLBACK 0% new longs
```

**Ambiguities & assumptions**

- The MACD rules give two meanings for each crossover state; the book says to use BPI and pattern analysis to tell them apart [p. 230]. ASSUMPTION: a "cross up while below zero" is a bullish transition if the previous phase was BEAR (or bearish pullback), else a bearish pullback; mirror for the cross down. Use the previous confirmed phase as memory.
- BPI needs point-and-figure buy signals for all stocks in an index [p. 230], which we cannot compute from OHLCV without implementing P&F. ASSUMPTION: replace BPI by percent of the stock panel (liquid names) whose close is above its own 50-day SMA, with the same 30/70 percent thresholds and a 6-point change filter; this is NOT the book's indicator.
- The book says no single detail declares a bull or bear market [p. 222]; the MACD-only version above is a simplification.
- Hedging with options is recommended in pullback/transition phases [p. 234, p. 235] and short selling in bear phases [p. 235]; neither is applied here (cash equity long-only). Leverage (margin) is optional in the book; ASSUMPTION: no leverage.
- Not found in this book: exact stop distances ("very tight", "a bit").

### 2.12 50-day EMA cross system (basic, long only)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (moving-average) | 265 |
| Timeframe & holding period | Daily; designed for position trading; tested on ten years of data | 265, 266 |
| Universe / eligibility filters | Stock(s) of your choice; short selling not permitted in this example | 265 |
| Market / regime filter | Not stated | - |
| Setup conditions | Today's close crosses and closes above the 50-day EMA | 265 |
| Entry trigger & order type | Buy at tomorrow's opening price when today's price crosses and closes above the 50-day EMA | 265 |
| Initial stop-loss | None other than the exit signal | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Sell at tomorrow's opening price when today's price crosses and closes below the 50-day EMA | 265 |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| EMA length | 50 days | test 9-, 25-, 100-day; SMA instead of EMA | 266 |
| Test history | ten years | 10-20 years of end-of-day data | 266, 264 |
| Execution | next day's open | none | 265 |

**Key quotes**

- "Buy at tomorrow’s opening price when today’s price crosses and closes above the 50-day exponential moving average (EMA)." [p. 265]
- "this simple system works fairly well when stock prices are trending, but it’s likely to trigger many losing trades when the prices of stocks are range bound" [p. 266]

**Pseudocode**

```
ema50 = EMA(close, 50)
buy  : close[t] > ema50[t] and close[t-1] <= ema50[t-1]  -> buy open[t+1]
sell : close[t] < ema50[t] and close[t-1] >= ema50[t-1]  -> sell open[t+1]
```

**Ambiguities & assumptions**

- No reported results. EMA seed not specified for the test; ASSUMPTION: seed with first close and discard the first 150 sessions. Include costs (about 0.1 percent slippage plus STT/brokerage).

### 2.13 50-day EMA system with whipsaw filter (confirmed version)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (filtered) | 266 |
| Timeframe & holding period | Daily; position trading | 265, 266 |
| Universe / eligibility filters | Stocks of your choice | 265 |
| Market / regime filter | Filters out trading-range situations through the added conditions | 266 |
| Setup conditions | (1) Today's close above the 50-day EMA; (2) price crossed above the 50-day EMA sometime during the last 5 days; (3) today's 50-day EMA is greater than the 50-day EMA from 5 days ago | 266 |
| Entry trigger & order type | Buy at tomorrow's open when all three conditions are true | 266 |
| Initial stop-loss | None other than the sell rule | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Sell at tomorrow's open when today's price crosses and closes below the 50-day EMA (rule from 2.12; the book states the filter only for the buy rule) | 265, 266 |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| EMA length | 50 | 9/25/100, SMA | 266 |
| Cross lookback | 5 days | none | 266 |
| Slope lookback | 5 days | none | 266 |

**Key quotes**

- "The stock crossed above the 50-day EMA sometime during the last 5 days." [p. 266]
- "Today’s 50-day EMA is greater than the 50-day EMA from 5 days ago." [p. 266]
- "they reduce the number of whipsaw trades for most stocks" [p. 266]

**Pseudocode**

```
cond1 = close[t] > ema50[t]
cond2 = any(close[k] > ema50[k] and close[k-1] <= ema50[k-1] for k in t-4..t)
cond3 = ema50[t] > ema50[t-5]
buy open[t+1] if cond1 and cond2 and cond3
sell open[t+1] if close[t] < ema50[t] and close[t-1] >= ema50[t-1]
```

**Ambiguities & assumptions**

- The book says the filter delays entries and lowers profit per trade but improves overall profitability ("makes the overall system more profitable") without data [p. 266]. Test it; do not assume it.

### 2.14 20-day Donchian-type close-breakout system

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout / trend-following (channel breakout) | 268 |
| Timeframe & holding period | Daily; example QQQQ; entry Sept 5 2007 at $49.56 to exit 9 Nov 2007 (about 2 months) | 269, 270 |
| Universe / eligibility filters | Not stated (tested on QQQQ ETF) | 270 |
| Market / regime filter | Not stated | - |
| Setup conditions | 20 prior trading days of data (current day excluded from the channel) | 270 |
| Entry trigger & order type | Buy at tomorrow's open when today's close is above the highest high of the last 20 days | 268 |
| Initial stop-loss | None other than the sell rule | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Sell at tomorrow's open when today's close is below the lowest low of the last 20 days. Suggested improvements to test: stop out if the low (instead of the close) falls below the Donchian low; use a 5- or 10-day exit channel; trailing stop | 268, 270 |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry channel | 20 days (highest high) | none | 268 |
| Exit channel | 20 days (lowest low) | 5 or 10 days | 268, 270 |
| Execution | next day's open | stop on intraday low | 268, 270 |
| Reported test | 30 trades, 18 losers; 13 of the losers were profitable at some point; system lost money overall | none | 268, 269 |

**Key quotes**

- "Buying at tomorrow’s opening price when today’s closing price is above the highest high price that occurred during the last 20 days." [p. 268]
- "Selling at tomorrow’s opening price when today’s closing price is below the lowest low that occurred over the last 20 days." [p. 268]
- "In the Donchian Channels system, buy signals apparently work better than sell signals." [p. 270]
- "Notice that the formula doesn’t include the current row." [p. 270]

**Pseudocode**

```
HH20[t] = max(high[t-20..t-1]) ; LL20[t] = min(low[t-20..t-1])      # excludes today
state = LONG if close[t] > HH20[t] ; FLAT if close[t] < LL20[t] ; else unchanged
trade at open[t+1] on state changes ; record MFE/MAE per trade
variants: exit channel 5 or 10 ; exit if low[t] < LL ; trailing stop
```

**Ambiguities & assumptions**

- The test period for the 30-trade result is not stated (Figure 15-1 shows from Sept 2007). The book says "initial results don’t look promising" [p. 268] — prior evidence is negative for the base rule; the improvements are untested in the book.
- The channel uses highs/lows but the signal compares the close to the channel (as in the book's spreadsheet [p. 270]).

### 2.15 Swing trade: buy-stop on an orderly pullback in a trending stock

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback (short-term swing) | 279 |
| Timeframe & holding period | Daily charts (and intraday 1- to 60-minute bars); typical swing trade lasts no more than a few days, up to a few weeks; NOV example thrust lasted ten trading days | 277, 279, 281 |
| Universe / eligibility filters | Actively traded, relatively large stocks; trending (ADX above about 30, or chapter 9 methods; +DMI above -DMI = up); high average daily range; strong sector; tight bid-ask spread; low-priced stocks poor | 278 |
| Market / regime filter | Trade with the dominant short-term trend; fundamentals have little impact on a time scale of days | 277, 279 |
| Setup conditions | Identified trending stock with a flag/pennant pullback; classic setup: orderly pullback where the high of each bar is lower than the previous bar's high | 279 |
| Entry trigger & order type | Day buy-stop just above the intraday high of the last bar; if not filled, cancel at end of day and re-enter just above the high of the most recent bar | 280 |
| Initial stop-loss | Stop-loss just below the intraday low of the lowest bar in the pullback (NOV: below the previous bar's low $28.74, or the entry day low $28.90) | 280, 281 |
| Exits: profit-taking | Not stated (exit by stop) | - |
| Exits: trailing / time / signal | Each day reset the stop to just below the low of the most recent bar | 280, 281 |
| Position sizing | Swing traders often trade 1,000-share increments; risk less than 5 percent, perhaps as little as 2 percent, of trading capital per trade; 10 percent is too much | 277, 287 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Usually ten or fewer simultaneous positions | 277 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| ADX trend threshold | more than about 30 | none | 278 |
| Buy-stop offset | "just above" last bar high | no number | 280 |
| Stop offset | "just below" low | no number | 280 |
| Risk per trade | below 5 percent, maybe 2 percent | 10 percent too much | 287 |
| Max positions | 10 or fewer | none | 277 |

**Key quotes**

- "The classic setup is finding an orderly pullback in which the high of each bar on a chart of the pullback is lower than the previous one." [p. 279]
- "Select your buy-stop price so it’s just above the intraday high price shown in the last bar of the chart." [p. 280]
- "As long as the trade is active, continue adjusting the stop price to be just below the intraday low of the most recent bar on the chart." [p. 280]
- "Swing trades don’t always work out, of course." [p. 282]

**Pseudocode**

```
trend: ADX(14) > 30 and +DI > -DI  (or higher highs/higher lows); liquid; spread tight
pullback: at least 2 consecutive bars with lower highs after a swing high
each day t: place buy_stop = high[t] + tick (ASSUMPTION 0.1%); if high[t+1] >= buy_stop -> filled at max(open[t+1], buy_stop)
after fill: stop = min(low of pullback bars) - tick ; each day stop = low[prev bar] - tick, never lowered
if low <= stop: exit at min(open, stop)
```

**Ambiguities & assumptions**

- ADX period not given; ASSUMPTION 14. "Just above/below" has no number; ASSUMPTION one tick or 0.1 percent. Minimum number of pullback bars not given; ASSUMPTION 2-5 bars.
- The NOV pullback trades were: one winner, one about breakeven, one loser [p. 281, p. 282]; no statistics are reported.
- Intraday refinements need intraday data we lack; this version uses daily bars only.
- Lowest-bar stop and previous-bar-low stop are both allowed in the text; ASSUMPTION: initial stop at pullback low, then trail to prior bar low.

### 2.16 Swing trade: trend channel

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following swing (channel support) | 282 |
| Timeframe & holding period | Daily chart; intraday fine-tuning | 282, 283 |
| Universe / eligibility filters | As 2.15 | 278 |
| Market / regime filter | Channel identified on the daily chart (trend line and parallel line over the highs) | 282, 171 |
| Setup conditions | Price approaches the lower (support) channel line in an uptrend | 282 |
| Entry trigger & order type | Take position in the trend direction as price nears the support channel line; intraday refinement: intraday low near the support line followed by a higher high and a higher low | 282, 283 |
| Initial stop-loss | Stop-loss just below the support channel line | 282, 283 |
| Exits: profit-taking | Exit as price approaches the upper (resistance) channel line, using intraday charts for reversal hints | 282, 283 |
| Exits: trailing / time / signal | Stopped out below the channel | 283 |
| Position sizing | As 2.15 | 287 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | As 2.15 | 277 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Channel construction | trend line under the lows plus parallel line over the highs | trend line from two most recent lows, drawn right to left | 171 |
| Entry zone | near the support line | no number | 282 |

**Key quotes**

- "As the stock price approaches the upper or resistance channel line, that signals when to exit your position." [p. 282]
- "After entering a position, your stop-loss order is entered just below the support channel line." [p. 282]
- "We believe trading in the direction opposite that of a dominant trend and a stock’s fundamental picture is foolhardy" [p. 173]

**Pseudocode**

```
fit lower line through the last two swing lows (right-to-left); upper line parallel through the swing high
if close within 1% of lower line and trend up: buy next open ; stop = lower line*(1-0.5%)
exit when high >= upper line*(0.99) or stop hit
```

**Ambiguities & assumptions**

- Trend-line drawing is discretionary; the book says no universal consensus exists [p. 170]. ASSUMPTION: swing-low definition = lowest low with 3 bars lower on each side; thresholds in the pseudocode are mine. The authors themselves say channel entries/exits are "very difficult" and not their primary method [p. 173].

### 2.17 Swing trade: range-bound stock with pivot-point entry (countertrend)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion within a range (countertrend) | 283 |
| Timeframe & holding period | Daily or weekly charts to identify the range; short holds | 283 |
| Universe / eligibility filters | Range-bound stock; as 2.15 liquidity rules | 278, 283 |
| Market / regime filter | Close shorts and switch to trend-following if resistance breaks | 284 |
| Setup conditions | Price approaching the support line | 283 |
| Entry trigger & order type | Buy limit just above support, or wait for a pivot point (three-bar pattern whose middle bar has a lower low than both neighbours) and enter an order on the next bar; intraday: higher high and higher low or gap higher | 283, 284 |
| Initial stop-loss | Immediately below the pivot-bar low, or just below the support line | 283 |
| Exits: profit-taking | Exit when the stock reverses near resistance | 284 |
| Exits: trailing / time / signal | Upside break of resistance: treat as a bullish breakout (see 2.1) | 284 |
| Position sizing | As 2.15 | 287 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | As 2.15 | 277 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pivot definition | three bars, middle low lowest | none | 283 |
| Entry bar | the next bar | none | 283 |

**Key quotes**

- "A pivot point is a three-bar pattern in which the low price of the middle bar is lower than the lows of the bars on either side of it." [p. 283]
- "The protective stop is placed either immediately below the low of the pivot bar or just below the support channel line." [p. 283]

**Pseudocode**

```
range from daily closes (>= 6-8 weeks as 2.1) ; support S, resistance R
if low[t-1] < low[t-2] and low[t-1] < low[t] and low[t-1] <= S*1.03: buy open[t+1] ; stop = low[t-1]*(1-0.2%)
exit when high >= R*0.98 ; if close > R*1.002 treat as breakout (2.1)
```

**Ambiguities & assumptions**

- "Approaches support" unquantified; ASSUMPTION within 3 percent. The authors discourage countertrend systems for position traders [p. 261]; low priority.

### 2.18 Swing trade: low short-term volatility ratio (volatility expansion)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Volatility breakout | 286 |
| Timeframe & holding period | Short swing; daily data | 286 |
| Universe / eligibility filters | Stocks with histories of large moves that are currently quiet | 278, 286 |
| Market / regime filter | Not stated | - |
| Setup conditions | Historic volatility ratio = short-term HV divided by long-term HV; common ratio 6-day HV over 100-day HV; below 50 percent marks a candidate | 286 |
| Entry trigger & order type | Place buy stop above the high and sell-short stop below the low of the current bar; whichever is hit first fills (or trade in the direction of the trend from conventional analysis) | 286 |
| Initial stop-loss | Not stated | - |
| Exits: profit-taking | Not stated | - |
| Exits: trailing / time / signal | Not stated | - |
| Position sizing | As 2.15 | 287 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | As 2.15 | 277 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Short HV window | 6 days | none | 286 |
| Long HV window | 100 days | none | 286 |
| Ratio threshold | below 50 percent | none | 286 |

**Key quotes**

- "One common ratio compares a 6-day historic volatility with a 100-day historic volatility." [p. 286]
- "Whenever the value of that ratio is less than 50 percent, the stock is a candidate for a swing-trading position." [p. 286]

**Pseudocode**

```
HV(n) = stdev(ln(close/close[-1]), n) * sqrt(252)     # ASSUMPTION: standard close-to-close
ratio = HV(6)/HV(100)
if ratio < 0.5: next day buy_stop = high[t]; (short leg not tradable on NSE cash) ; stop/exit: ASSUMPTION 2.15 trailing
```

**Ambiguities & assumptions**

- HV formula not given ("math is complex"). Stops and exits not given. The short leg cannot be used on NSE cash overnight; long leg only (reduces the setup to a one-sided bet).

### 2.19 Gap signals (breakout, continuation, island, filled gap)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Event-based trend confirmation / exit signals | 173 |
| Timeframe & holding period | Daily charts mostly; sometimes weekly | 173 |
| Universe / eligibility filters | As 2.1 | 233 |
| Market / regime filter | Island-gap longs only if the new trend aligns with fundamentals | 176 |
| Setup conditions | Gap = today's open above prior close and (for an obvious gap) today's low above prior high; common gap mid-range: ignore | 173, 174 |
| Entry trigger & order type | Breakout gap (exceeds range high/low simultaneously with a gap): good entry in the direction of the gap. Continuation gap in an uptrend (low clearly above prior high): trend very strong; short-term traders may enter, position traders confirm the trade | 174, 175 |
| Initial stop-loss | If the gap is filled, the signal has failed and you exit | 181 |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Exhaustion gap (often very large volume) and island gap (two gaps isolating bars) signal trend end/exit; filled breakout gap is bearish, filled continuation gap = exit, price trading back into the island = exit | 175, 176, 181 |
| Position sizing | As section 3 | 206 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Gap definition | open above prior close, low above prior high | overlapping gaps ignored | 173 |
| Exhaustion clue | very large volume | none | 175, 176 |

**Key quotes**

- "A breakout gap often provides excellent trading signals to enter a new position, in the direction of the gap." [p. 174]
- "A gap that’s filled negates the trading signal that it generated." [p. 181]
- "An island gap usually is a good indicator that the prior trend has been extinguished" [p. 176]

**Pseudocode**

```
gap_up[t] = low[t] > high[t-1]  (obvious gap)
breakout_gap = gap_up[t] and close[t] > R (range high from 2.1)
continuation_gap = gap_up[t] and uptrend (HH/HL)
island: gap_up at t0 followed by gap_down at t1 within <= 5 bars -> exit longs
filled: close[t] <= high[gap day-1] after breakout/continuation gap -> exit
```

**Ambiguities & assumptions**

- Exhaustion vs continuation cannot be told apart in advance (book admits this [p. 175]). ASSUMPTION: flag a continuation gap on volume > 3x average as a possible exhaustion and tighten the stop; island width <= 5 bars. NSE circuit limits can create gap-and-lock days: treat locked sessions separately.

### 2.20 Trend riding: higher-low trailing stop and trend-end exits

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Exit / trade-management module (trend-following) | 217 |
| Timeframe & holding period | Daily with weekly confirmation; weeks to months | 172, 173 |
| Universe / eligibility filters | Applies to any open long from 2.1-2.14 | 217 |
| Market / regime filter | Consider fundamentals and economic cycle before holding through a retracement | 180 |
| Setup conditions | Uptrend = series of higher highs and higher lows | 168 |
| Entry trigger & order type | Not applicable | - |
| Initial stop-loss | Not applicable here (see each entry) | - |
| Exits: profit-taking | Trim into a runaway move; plan exits leaving something on the table | 359 |
| Exits: trailing / time / signal | Trailing stop: after the ETF makes a higher high reset the stop to the most recent higher low, or the one before it (GLD example about $72.00 interim closing low). Trend-end hints (any one may suffice): price gaps with high volume; price closes significantly below its moving average; price fails to reach a higher price after the gap. Close below a trend line for longer than a day or two = trend may have ended; if a short-term trend line breaks check the weekly chart: exit right away if the weekly shows a break in higher highs/higher lows. Multi-step retracement: wait unless island reversal or downside break of a flag/pennant/range; exit if the stock makes another lower high and trades below the next lower low | 216, 217, 172, 173, 179, 180 |
| Position sizing | Not applicable | - |
| Adding to / pyramiding | Not applicable here (see 2.1) | - |
| Portfolio limits (max positions, correlation, heat) | Not applicable here | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trail anchor | most recent higher low (or the one before) | closing low used in GLD example | 217 |
| Days below trend line | longer than a day or two | none | 172 |
| Three-step retracement | at least 1 lower high and 1 lower low | none | 178 |
| Five-step retracement | two lower highs and two lower lows | none | 178 |
| Weekly check | one time increment higher | none | 172, 173 |

**Key quotes**

- "Use the higher lows to define your stop points." [p. 217]
- "After the ETF has made a higher high, reset the stop to either the most recent higher low, or the one just before it." [p. 217]
- "if it establishes another lower high and trades below its next lower low, it’s time to exit" [p. 180]
- "Any one of these events may carry enough weight for you to close your position." [p. 217]

**Pseudocode**

```
swing_lows = pivots with 3 lower-bar confirmation (ASSUMPTION)
on new higher high: stop = max(stop, most_recent_swing_low_close)         # closing low, as in GLD example
exit next open if close < stop
exit next open if gap_with_volume>=2x avg and close<SMA(30) and no new high within 5 bars       # combine the 3 hints, ASSUMPTION
exit if weekly higher-high/higher-low pattern breaks (weekly close < previous weekly swing low)
```

**Ambiguities & assumptions**

- The book gives the hints qualitatively; "significantly below" the MA is undefined (ASSUMPTION: 2 percent below the 30-day SMA). Whether stops use closes or lows is mixed (GLD uses a closing low). ASSUMPTION: closing-basis exits triggering at the next open.

### 2.21 Trade-candidate screen: relative strength plus fundamentals plus sector

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Stock-selection filter (growth/momentum) | 201 |
| Timeframe & holding period | Used before position-trade entries | 201 |
| Universe / eligibility filters | Candidate when the stock: shows fundamentals of a strong company; has earnings growing faster than average; is in a strong sector; operates in a growing economy; is approaching a technical buy signal; performs better than the average stock. Prefer companies with a history of positive reported earnings | 201, 116 |
| Market / regime filter | Growing economy; trade with the market phase (2.11) | 201 |
| Setup conditions | Relative strength No. 2 = percentage change in stock price / percentage change in index over the same period (authors' preference), or stock price / index | 200 |
| Entry trigger & order type | Entries come from 2.1-2.4 | - |
| Initial stop-loss | Not applicable | - |
| Exits: profit-taking | Hold while the stock stays relatively strong versus other stocks; replace positions that begin to underperform with emerging leaders (extra patience for profitable ones; close losers without a second thought) | 233, 210 |
| Exits: trailing / time / signal | As 2.20 | 217 |
| Position sizing | Not applicable | - |
| Adding to / pyramiding | Not applicable | - |
| Portfolio limits (max positions, correlation, heat) | As 2.1 | 360 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Relative strength | percent change stock / percent change index | price ratio; IBD six-month rank | 200, 201 |
| RS look-back | not stated (IBD uses six months) | none | 201 |
| Interest coverage warning | company in trouble below 3 | none | 107 |
| Quick ratio | at least 1 to 1 for a good credit risk | none | 115 |
| P/E historic reasonable range | 10 to 15 | none | 118 |
| Minimum liquidity | stocks with low trading volume are riskier | no number | 101 |

**Key quotes**

- "The goal when examining a stock’s relative strength is not necessarily to find the best performing stocks in the universe of all stocks" [p. 201]
- "but rather to find stocks that are performing better than the average stock as each stock signals a buy" [p. 201]
- "If we were allowed to choose only one piece of fundamental data to guide our trading, we’d choose the earnings growth rate" [p. 116]
- "Analysts generally consider a company in trouble whenever its interest coverage ratio falls below 3." [p. 107]
- "When we trade, we want the strongest stocks in the strongest sectors" [p. 92]

**Pseudocode**

```
RS_i = (close_i[t]/close_i[t-126] - 1) / (idx[t]/idx[t-126] - 1)     # ASSUMPTION: 6-month look-back, index = NIFTYBEES or equal-weight panel
rank RS_i ; candidate if RS_i above universe median (book: 'better than the average stock')
fundamentals (forward-test only): EPS growth > universe median AND positive trailing EPS AND interest coverage >= 3
sector: sector return in top third of sectors over 6 months (needs sector tags)
```

**Ambiguities & assumptions**

- Sector strength is measured in the book by ranking industry groups by price performance (Investor’s Business Daily ranks nearly 200 groups) or sector ETFs [p. 92]; our data has no sector tags, so ASSUMPTION: build sectors externally.
- If index return is near zero or negative the ratio form (percent/percent) is unstable. ASSUMPTION: use the difference of returns (stock minus index) instead for ranking.
- Fundamental thresholds other than interest coverage < 3 and quick ratio >= 1 are not given; EPS growth is "the bigger the better" [p. 232].

### 2.22 Bullish single-bar reversal (buy opportunity after a decline)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion / reversal signal | 153 |
| Timeframe & holding period | Daily bars | 153 |
| Universe / eligibility filters | Confirmed by volume (higher than average) | 150, 153 |
| Market / regime filter | Not stated | - |
| Setup conditions | Bullish reversal bar: opens at (or near) the high, trades lower, and closes at (or near) the high of the bar; preceded by several periods of falling prices | 153 |
| Entry trigger & order type | The pattern often represents a buying opportunity; in the aggressive double-bottom variant entry is the next trading day | 153, 164 |
| Initial stop-loss | Below the reversal bar's low (from 2.5) | 164 |
| Exits: profit-taking | Not stated | - |
| Exits: trailing / time / signal | Not stated | - |
| Position sizing | Not stated | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Prior decline | "several periods" | none | 153 |
| Volume | above average | none | 150 |

**Key quotes**

- "Whenever a bullish reversal bar is preceded by several periods of falling prices, for example, its pattern often represents a buying opportunity." [p. 153]
- "Volume confirms price" [p. 150]

**Pseudocode**

```
bar t: open[t] >= high[t] - 0.2*(high-low) ; close[t] >= high[t] - 0.2*(high-low) ; low[t] < open[t] - 0.5*(high-low)   # ASSUMPTION
precondition: close[t-1] < close[t-4] (3 down-bars) ; volume[t] > avgvol
buy open[t+1] ; stop low[t]
```

**Ambiguities & assumptions**

- Thresholds in the pseudocode are mine; "several periods" taken as 3-5 bars. The book says single bars must be read in context [p. 154], so this is a weak standalone signal.

## 3. Risk & money-management rules

Account-level rules stated by the authors (all long-side relevant; margin and derivatives rules are US-specific):

| Rule | Detail | Page |
|---|---|---|
| Loss cap per position | Try to keep losses below 5 or 6 percent for any position; or keep loss from any single position below 1 or 2 percent of total trading capital | 206 |
| Stops are mandatory | Set an entry point and exit point before entering; ruthlessly adhere to stop-loss points; protect profits with trailing stops; exit when the trend ends | 205, 206 |
| Stop method | Predetermined-percentage stop is advocated by others but not recommended; use technical analysis to identify when a trade has failed | 213 |
| Stop placement | Keep stop away from the obvious price (breakout at $35.75: stop at $35.69 or $35.63, not $35.74) | 244 |
| Stop fill risk | A stop becomes a market order and gaps can fill it at the open or worse; stop-limit orders may never fill in a fast market | 220, 50 |
| Recovery maths | A 50 percent loss needs a 100 percent gain; 75 percent needs 300 percent | 212 |
| Capital preservation | Protect principal first; do not let a large profit turn small, a small profit turn into a loss, or a small loss turn large | 211 |
| Never average down | Add only to winners (pyramiding) on new signals; trim pyramids at first sign of trouble | 359 |
| Diversification | Start with 10 or 15 positions; eight may be enough; imagining why you need more than 20 is difficult | 360 |
| Concentration | Do not put a huge portion of principal in one stock | 219 |
| Exposure by market phase | Bullish transition: small partial positions, 20 percent committed in the example, cap 40-50 percent; bull market: fully (100 percent) invested; bear: no new long positions | 236, 234, 235 |
| Leverage | Margin initial 50 percent; maintenance 25 percent; a 40 percent fall in a margined stock cost 80 percent of equity; never satisfy a margin call, close the position | 253, 254 |
| Swing trade risk | Risk under 5 percent, possibly 2 percent, of capital per swing trade; 10 percent is too much | 287 |
| Slippage assumption | Start with 25 cents per share of slippage in tests and adjust | 272 |
| Entries | Never place market orders after hours; use stop, limit or stop-limit orders | 358 |
| Confirm on higher timeframe | Always confirm analysis on the chart one time period higher | 357 |
| Start small | Begin with a small sum of money and increase activity as experience grows | 37 |
| Replace laggards | Replace underperformers with emerging leaders; close losing positions without a second thought | 210 |
| System testing | Avoid curve fitting; use blind (out-of-sample) simulation; discount systems whose profits come from a single or few trades | 194, 266, 267 |
| Order overcommitment | Open GTC buy-stops can all trigger at once; keep enough buying power | 249 |

## 4. Non-codable guidance

- Trading is a business; stocks are inventory; do not fall in love with a stock or a trading system [p. 208, p. 358].
- "Paper loss" rationalizations are foolhardy; selling a loser is emotionally harder than opening a position [p. 208].
- Do not take a losing trade personally [p. 357, p. 358].
- When in doubt, close the position; devise a strategy and execute the plan rather than winging it [p. 357].
- Watch for signals, do not anticipate them; do not chase breakouts or runaway stocks [p. 365, p. 247].
- Avoid paralysis by analysis; choose two or three tools and learn them [p. 183, p. 363].
- Prefer visual pattern analysis over blind reliance on indicators; computer indicators are not more accurate [p. 183].
- Technical analysis is a trading tool, not fortune telling; it need not be right half the time [p. 138, p. 146].
- Decide entries and exits before the day begins (day trading) and focus either on trades or on rules [p. 303].
- Keep a trading journal recording entry/exit system, stops moved and why, MFE, MAE and review it weekly or monthly [p. 272, p. 273, p. 366].
- Fundamental economic reading (Fed policy, industrial production, sector rotation, the seven steps for using data) is judgement-heavy: wait for confirmation before acting on interest-rate hints [p. 223, p. 99, p. 100].
- Analyst calls (tone, response speed, analyst mood, employee satisfaction) are research aids, not triggers [p. 130, p. 131, p. 132].
- Taylor three-day swing cycle is discretionary and hard to test [p. 285].
- Day-trading opening-gap pattern (gap fills in the first minutes; unfilled after 5-10 minutes suggests the day's trend) has no consensus and needs intraday data [p. 298].
- Success rate of day traders is 10-30 percent [p. 297]; the authors are not day traders [p. 291].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV (open for next-day-open fills, high/low for channels and stops, volume for confirmation); an index series for market phase and relative strength (NIFTYBEES or an equal-weight index built from the panel; the Nifty index only exists from 2024); weekly bars resampled from daily; sector tags for the strongest-sector filter (not in our stated data); fundamentals fields (EPS growth, interest coverage, quick ratio, P/E) from Feb 2026 snapshots (3-year growth from May 2026); delivery percent is not used by the book.
- **Testability with our data:**
  - Backtestable on 2005-2026 prices: 2.1-2.5 and 2.22 (pattern rules need the ASSUMPTION parameters), 2.7, 2.8, 2.9, 2.10, 2.12, 2.13, 2.14, 2.15-2.17 (daily-bar version), 2.18 long leg, 2.19, 2.20, and the RS part of 2.21; the price-only part of 2.11 using MACD on NIFTYBEES (or the equal-weight index), with the BPI replaced by the proxy described there.
  - Forward-test only (fundamental snapshots from Feb/May 2026): EPS growth, interest coverage, quick ratio, P/E in 2.21 and in the stock-selection filters of 2.1-2.6.
  - Needs data we do not have: intraday bars for the swing intraday refinements and all day-trading rules; point-and-figure BPI; sector classification (unless added); options for the hedges in 2.11; bid-ask spread data for the tight-spread filter.
- **Market-structure differences (all adaptations are ASSUMPTIONS):**
  - No overnight shorting in the NSE cash market: drop every short, shorted-ETF and countertrend-short rule (bear phases, 2.18 short leg, 2.17 short at resistance); bear and bearish phases mean cash, not short.
  - Replace the 5-10 cent breakout margin and 25 cents per share slippage with percentages: breakout margin 0.2 percent of price; slippage 0.1 percent per side plus STT and brokerage.
  - Circuit limits: skip entries and treat stops as unfillable on days when a stock opens locked at a circuit; gap rules (2.19) should flag locked sessions.
  - Liquidity: the authors warn that small caps are thinly traded and hard to exit [p. 233]; ASSUMPTION: restrict to stocks with median daily turnover above a fixed rupee threshold (e.g. INR 5 crore) and use delisted names to avoid survivorship bias.
  - Dominant-trend filter: use NIFTYBEES/equal-weight index in place of S&P 500/Nasdaq.
  - Margin trading is excluded (leverage and PDT rules do not map); T+3 settlement and free-riding rules are US-specific.
  - Tax: STCG/LTCG rules differ; wash-sale rule does not apply.
  - Execution: use next-day open fills as in the book's own system tests (2.12-2.14).

## 6. Verdict

- **Codeability:** Partly. The book's MA, Donchian, MACD, stochastic, breakout-with-volume and swing pullback rules can be coded exactly or with small assumptions; chart-pattern recognition (cup and handle, double bottom, trend lines), the market-phase model (BPI), sector rotation and fundamentals are discretionary or need unavailable data.
- **Priority for backtesting:** Medium. It is a generic primer with no performance evidence, but the entry/exit rules (volume-confirmed range breakout with 1-3 day confirmation, 30/50-day SMA trend exit, higher-low trailing stop, weekly-MACD market filter) are simple and cheap to test, and its one reported system (20-day Donchian) lost money, which makes the modifications worth checking.
- **Top 3 things a coder is most likely to get wrong:**
  1. Look-ahead and execution: the book's systems trade at tomorrow's open after a close-based signal and compute the Donchian channel from the previous 20 days only (excluding today); using same-day close fills or including the current bar hides the failure of the base rule.
  2. Treating discretionary phrases as precise: "several days" confirmation, "low volume" pullback, "significantly below" the MA, "tight" range and the 5-10 cent margin must be parametrized and tested across ranges, not tuned (the authors warn about curve fitting).
  3. The market-phase model: MACD states have two meanings each (transition vs pullback) and the BPI is point-and-figure-based; a naive MACD-only implementation, or applying the 2026 fundamental snapshots to history, misrepresents the method.
