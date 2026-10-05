# The Master Swing Trader Toolkit: The Market Survival Guide — Alan S. Farley (McGraw-Hill, 2010)

- **Source file:** Google Drive `0229_The Master Swing Trader Toolkit.pdf` (file id `1gC7mBKgEUnxkW9D29NFrtL4O9_2wCg4S`, 5,332,819 bytes), 353 PDF pages with a text layer.
- **Text file used:** text/farley_master_swing_toolkit.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index). The printed page number is usually PDF page − 21 (printed p. 147 = [[PAGE 168]]), but always take N from the marker, not from the contents list.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/farley_master_swing_toolkit.md text/farley_master_swing_toolkit.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage (redo under correction 4, replaces the 24 KB condensed version):**
  - **Read sequentially, line by line: [[PAGE 1]] to [[PAGE 347]].** This covers the title and copyright pages, contents, foreword, preface, acknowledgments, Chapters 1–12, the four "Real World" case studies, the glossary, the bibliography and the first index page.
  - **Scanned only: the rest of the index ([[PAGE 347]]–[[PAGE 353]])**, which holds keyword/page entries and the author bio, and no rules.
  - Chart images are not in the text layer; figure captions were read and used.
  - **Correction to the previous version (for the laptop importer):** the old Coverage line said "every page read sequentially, [[PAGE 1]] to [[PAGE 343]]". In that pass, the copyright and contents block ([[PAGE 5]]–[[PAGE 12]]) was only partly viewed. This redo reads it in full. The pages have no trading rules but confirm the chapter map used below.
  - **Narrative chapters** (Ch. 5 "The Nature of Winning", Ch. 7 "Market Entry", Ch. 11 "The Nature of Losing") were read in full. Their codable rules (expectancy, yo-yo limits, anticipation entries, drawdown shutdowns) are in sections 2–3.

## 1. The method in brief

Farley's "survivalist" swing-trading method is built for markets in which program algorithms deliberately trap the crowd.

**Core view**
- Traps are the main force in modern markets; price "seeks volume" at the stops of the majority [p. 28].
- Trade behind, ahead of or against the crowd, never with it [p. 156]. Prefer anticipation entries near support/resistance over reactive breakout chasing [p. 186–187].
- The recurring signal is the **failure of a failure**: a pattern fails just long enough to shake out weak hands, then works [p. 142, 151, 281].

**Trade planning with swing analysis**
- Profit target = the next barrier between entry and the prior swing high/low.
- Failure target = the price that breaks the setup.
- Prefer trades with few barriers to the target and many barriers behind the entry [p. 140].
- Require roughly ≥ 3:1 reward:risk [p. 169, 208].
- Every breakout runs an action → reaction → resolution (1-2-3) cycle [p. 59–60].

**Toolset**
- 5-3-3 Stochastics on every chart; 14-7-7 for position traders [p. 99–100].
- Smoothed RSI(14,7) or 17-17-1 Stochastics for the 21–28-day cycle [p. 101].
- 50/200 EMAs on daily, 60-min and 15-min charts [p. 49, 153].
- Bollinger Bands (20,2) [p. 75].
- Price-vs-200-day-EMA relative-strength sort [p. 100–101].
- Fibonacci 38/50/62/78% [p. 139, 160].

**Context filters**
- The calendar: options expiration, window dressing, Fed days, earnings, turnaround Tuesday [p. 79–90].
- Index-futures behaviour and breadth, used for trend-day detection [p. 53, 203, 247].
- A daily "collar" that sets how aggressive to be [p. 306–315].

**Evidence:** worked chart examples only (eSignal charts, 2006–2009 US stocks and ETFs). There are no backtests or statistics.

## 2. Strategies

Ratings: **Fully** = every entry/stop/exit element stated or a stated default exists; **Partly** = entry stated but a key element is discretionary.

| # | Strategy | Codable | Pages |
|---|---|---|---|
| 2.1 | First-hour range breakout/breakdown | Fully | 168–170 |
| 2.2 | Gap-day first-hour mechanics: reverse-break failure of a failure | Fully | 279–282 |
| 2.3 | Bilateral range entry | Fully | 169–172 |
| 2.4 | 50-day EMA magnet pullback (after a fresh breakout) | Fully | 153–157 |
| 2.5 | 50-day EMA narrow-range short (bounce from below) | Fully | 156 |
| 2.6 | Continuation-gap retracement buy/sell | Partly | 40–41, 222, 268–270 |
| 2.7 | Breakaway-gap pullback / post-gap range | Partly | 266–267 |
| 2.8 | Exhaustion-gap fade | Partly | 269–270 |
| 2.9 | Fibonacci whipsaw (62/78 failure of a failure) | Fully | 162–163 |
| 2.10 | 2B failed-breakout short | Fully | 148 |
| 2.11 | Narrow-range short at support | Fully | 149 |
| 2.12 | Pullback short into resistance, with the support-break analog filter | Partly | 148–150 |
| 2.13 | Tiered Fibonacci pullback buy (38/50/62) | Fully | 206–208 |
| 2.14 | Parabolic-move ledge buy (half size, one retry) | Partly | 208 |
| 2.15 | Range fade (countertrend within a mature range) | Fully | 166–168 |
| 2.16 | Falling-knife tiered / outer-limit entry | Partly | 165–166 |
| 2.17 | Stop-run (rinse-job) reversal entry | Fully | 232, 235, 272–274 |
| 2.18 | Options-expiration magnetic-strike trades | Partly | 83–87 |
| 2.19 | Post-earnings and post-news re-entry | Partly | 88–90, 259–260 |
| 2.20 | Weekly-chart remote entry (DCA into range support) | Fully | 215–218 |
| 2.21 | Strength/weakness basket (Dow components ≥ 10% above the 200-day EMA) | Fully | 209–211 |
| 2.22 | Stealth breakout (creep into multi-tested resistance) | Partly | 251 |
| 2.23 | Overlay: trailing-stop and exit protocol | Fully | 231–235, 319–322 |
| 2.24 | Overlay: daily collar (exposure and scaling regime) | Partly | 306–315 |
| 2.25 | Overlay: market filters (trend day, VIX, calendar, long-cycle RS) | Partly | 53, 103, 151, 203, 247–248, 307 |

### 2.1 First-hour range breakout/breakdown

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday breakout (opening-range) | 168 |
| Timeframe & holding period | 5-min chart for execution and management; 15-min bars of the last two days for the target. Intraday; exit at the close if the trailing stop is not hit | 169 |
| Universe / eligibility filters | Highly liquid: stocks > 5M shares/day average, or index/sector ETFs. Keep a standing watch list of groups that don't all move together | 168 |
| Market / regime filter | The range must be built by swings both ways. Skip if the stock is already trending at the end of the first hour | 169 |
| Setup conditions | Wait 30 minutes and draw the high/low on a 5-min chart; adjust over the next 30 minutes to get the first-hour range | 169 |
| Entry trigger & order type | Buy above the range high, or short below the range low, plus "a few cents". Full size at once; the signal may come late in the session | 168 |
| Initial stop-loss | 15–20% of the range height back inside the range from the broken edge (22–24 range: long stop 23.60–23.70). Physical stop, not mental | 168 |
| Exits: profit-taking | Target = the last major swing in the trade direction on the last two days of 15-min bars | 168–169 |
| Exits: trailing / time / signal | If there is no swing: tight trailing stop, exit at the close. Expect a quick profit; if none, whipsaw odds rise | 168–169 |
| Position sizing | Full position immediately (no scaling) | 168 |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Trade only if reward ≥ 3 × risk | 169 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Range window | 60 min (30 + 30 adjust) | aggressive: 3–4 five-minute bars; on gap days 45 min–2 h; defensive: 2–4-day post-gap range | 169, 280 |
| Entry buffer | "a few cents" | — | 168 |
| Stop depth | 15–20% of range height | Yum example: 20% stop | 168, 170 |
| Liquidity | > 5M shares/day | ETFs preferred | 168 |
| Min reward:risk | 3:1 | example 3.5:1 (30 → 30.70, stop 29.80) | 169 |

**Key quotes**
- "Buy when price rallies above the high of the first hour range, or sell short when it falls under the range low." [p. 168]
- "Calculate the height of the first hour range, placing a stop loss 15% to 20% under the high for a breakout, or above the low for a breakdown." [p. 168]
- "look for trades in which the realized profit will be at least three times the risk of price rolling over and triggering the stop." [p. 169]
- "The first hour range is established by swings in both directions." [p. 169]
- "These issues should not be traded using this strategy." [p. 169]

**Pseudocode**
```
bars = 5-min bars from 09:30
H = max(high[09:30..10:30]); L = min(low[09:30..10:30])
require swings_both_ways(bars[09:30..10:30]) and not trending_at(10:30)       # p.169
R = H - L
target_long  = last_major_swing_high(15-min bars, last 2 days) above H        # p.168-169
entry_long   = H + buffer ; stop_long = H - 0.175*R                          # 15-20% (p.168)
if target_long is None: use tight trail, exit at close
if (target_long - entry_long) >= 3*(entry_long - stop_long):                  # p.169
    place buy-stop at entry_long (full size)
mirror for short: entry = L - buffer ; stop = L + 0.175*R
```

**Ambiguities & assumptions**
- **"A few cents".** ASSUMPTION: buffer = max(2 ticks, 0.02 × R).
- **"Last major swing".** ASSUMPTION: the most recent 15-min pivot high (3 bars each side) above entry within the prior two sessions.
- **"Trending at the end of the first hour".** ASSUMPTION: last 3 five-minute closes all beyond the range midpoint in one direction, with no counter-swing pivot.
- **Tight trailing stop.** ASSUMPTION: trail by 2 × the 5-min ATR(14).

### 2.2 Gap-day first-hour mechanics (reverse-break failure of a failure)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday gap continuation / failure-of-a-failure | 279–281 |
| Timeframe & holding period | 15-min bars (4 bars = first hour); intraday, may carry into the next gap day | 279 |
| Universe / eligibility filters | Liquid stocks gapping on news (example: tier-one upgrade) | 279 |
| Market / regime filter | Check whether the gap pushes price into or through longer-term S/R | 281 |
| Setup conditions | Draw: gap-fill line = prior close; reverse-break line = range edge nearest the gap fill; breakout-trigger line = the far edge | 279 |
| Entry trigger & order type | (a) Breakout: price exceeds the trigger line in the gap direction. (b) Failure of a failure: after breaking the reverse-break line, price re-crosses back above it (gap up) → enter in the gap direction | 279, 281 |
| Initial stop-loss | (b): just below the reverse-break line | 281 |
| Exits: profit-taking | Retest of the session high (gap up) / low (gap down) | 281 |
| Exits: trailing / time / signal | Pinball from the gap-fill line to the reverse break and back through the gap fill = failure signal (exit / reverse) | 281 |
| Position sizing | Not specified | — |
| Adding to / pyramiding | The example adds on a second-day range break | 281–282 |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| First-hour definition | four 15-min bars | 3–4 five-minute bars (aggressive); 2–4-day range (defensive) | 279–280 |
| Typical behaviour | first attempt beyond the range fails, second succeeds (tiny C&H) | — | 279 |

**Key quotes**
- "The line nearest the gap fill becomes the “reverse break line.”" [p. 279]
- "Violation of the reverse break is likely to trigger price acceleration toward the gap fill line" [p. 281]
- "It’s a great trade because the risk, once the buying signal is taken, can be well managed with a stop loss just below the reverse break line." [p. 281]

**Pseudocode**
```
gapfill = prior_close ; rng = first_hour(15-min x4) ; up_gap = open > prior_close
rev = rng.low if up_gap else rng.high ; trig = rng.high if up_gap else rng.low
if up_gap:
    if price > trig: enter_long(stop = rev - tick)                         # breakout (p.279, 281)
    if crossed_below(rev) and later crossed_above(rev):
        enter_long(stop = rev - tick)                                       # failure of a failure (p.281)
    if touched(gapfill) and crossed_above(rev) and crossed_below(gapfill): exit/flag failure   # p.281
mirror for down gaps
```

**Ambiguities & assumptions**
- **No profit target beyond "retest of the high".** ASSUMPTION: exit at the session high, else at the close.
- **Stop for the plain breakout entry** is not stated. ASSUMPTION: same as 2.1 (15–20% of the range).

### 2.3 Bilateral range entry

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Range breakout either direction (OCO) | 169–172 |
| Timeframe & holding period | Daily or intraday; multi-day in the example | 171–172 |
| Universe / eligibility filters | Narrow, well-defined S/R | 171 |
| Market / regime filter | Equal odds and reward on both sides; clean triggers both sides | 171 |
| Setup conditions | Rectangle / consolidation at a balance point | 169 |
| Entry trigger & order type | Stop orders just outside the range: buy above resistance, short below support (example: buy ~37.40, short ~34.80 on a 35–37 box) | 172 |
| Initial stop-loss | 15–20% of the pattern width behind the breakout level (2-pt box → 30–40¢: long stop ~36.80, short ~35.50) | 172 |
| Exits: profit-taking | Short side example: test of the swing low (31) | 172 |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Stop depth | 15–20% of width | — | 172 |
| Entry offset | ~0.40 outside a 2-pt range | stalk in real time instead | 172 |

**Key quotes**
- "Calculate 15% to 20% of the pattern width and place the stop loss that far behind the breakout or breakdown level." [p. 172]
- "the best trade is usually in the direction that’s opposite to our bias." [p. 171]

**Pseudocode**
```
box = consolidation(high=R, low=S) ; W = R - S
oco: buy_stop at R + 0.2*W  (stop R + 0.2*W - 0.175*W) ; sell_stop at S - 0.2*W (stop S - 0.2*W + 0.175*W)
cancel the other leg on fill
```

**Ambiguities & assumptions**
- **Entry offset.** The 37.40/34.80 example on a 35–37 box implies ~0.4 points (20% of width) beyond the edges. ASSUMPTION: 0.2 × W offset, and stop measured from the broken edge as stated.
- **Targets.** ASSUMPTION: the next swing high/low (2.23 protocol).

### 2.4 50-day EMA magnet pullback (after a fresh breakout)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Pullback / failure-of-a-failure | 153–156 |
| Timeframe & holding period | Daily setup, 60-min for timing; days to weeks | 154 |
| Universe / eligibility filters | Stocks/ETFs that just broke out (long) or broke down (short mirror) | 154, 156 |
| Market / regime filter | Use in "anything less than ideal market conditions"; trade behind/against the crowd | 156 |
| Setup conditions | After a new breakout, set an alert 1–2 points above the 50-day EMA; wait days or weeks. Variant: a natural support (e.g., C&H trendline) fails and drops price into the EMA | 154–155 |
| Entry trigger & order type | Buy as the selloff gathers steam into the EMA, or when the 60-min chart prints an upside reversal pattern there | 154 |
| Initial stop-loss | Not stated for this setup. Related example: re-entry stop under the low of the recovery bar after a failure of a failure above the 50-day EMA | 317–318 |
| Exits: profit-taking | Resolution phase: back above the original breakout level | 156 |
| Exits: trailing / time / signal | 2.23 protocol | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Moving average | 50-day EMA (EMA preferred to SMA) | 50-period EMA on 15/60-min (noisier) | 154, 157 |
| Alert distance | 1–2 points above the EMA | — | 154 |
| Timing chart | 60-min reversal | — | 154 |

**Key quotes**
- "Find the 50-day EMA on a new breakout and place an alert a point or two above it." [p. 154]
- "look to buy when the selloff gathers steam into the moving average, or wait until the pattern in the next lower time frame" [p. 154]
- "we need the discipline to wait for a breakout or breakdown to fail and accelerate toward the 50-day EMA" [p. 156]

**Pseudocode**
```
if new_breakout(daily, lookback=60): armed = True ; breakout_level = level
if armed and low <= EMA50 + alert_pts:
    wait for 60-min reversal (close > high of prior 60-min swing) near EMA50 -> buy   # p.154
    stop = min(low of reversal bar, EMA50 - k*ATR)            # ASSUMPTION
    target = breakout high / prior swing high ; manage per 2.23
```

**Ambiguities & assumptions**
- **"New breakout".** ASSUMPTION: close above a 60-day high within the last 20 sessions.
- **"Point or two".** Dollar-based in the book; ASSUMPTION: 0.5 × daily ATR(14).
- **"60-minute upside reversal pattern".** ASSUMPTION: a 60-min close above the high of the most recent 60-min lower-high pivot.
- **Stop.** ASSUMPTION: below the reversal low, never placed exactly at the EMA (avoid MA stops [p. 230]).

### 2.5 50-day EMA narrow-range short (bounce from below)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Short at resistance (narrow-range) | 156 |
| Timeframe & holding period | Daily | 156 |
| Universe / eligibility filters | A stock that broke down on strong volume and sold off | 156 |
| Market / regime filter | Shorts below the 50-day EMA are with-trend | 166 |
| Setup conditions | Recovery bounce back up to the 50-day EMA stalls; price bars contract across the EMA | 156 |
| Entry trigger & order type | Sell short within the narrow-range bars at EMA resistance (limit order, "upticks" give fills) | 156 |
| Initial stop-loss | Any buying spike above the moving average → exit | 156 |
| Exits: profit-taking | Not specified (selling resumes "with a fury") | 156 |
| Exits: trailing / time / signal | 2.23 protocol | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Narrow range | contracted bars across the EMA | NR7 definition in glossary | 156, 337 |

**Key quotes**
- "The trick is to watch this play in progress and to sell short within the narrow range bars at moving average resistance." [p. 156]
- "any buying spike above the moving average tells you to get out of the trade." [p. 156]

**Pseudocode**
```
if breakdown_on_volume(lookback=20) and bounce reaches EMA50 and NR(3 bars) straddling EMA50:
    short at close of NR bar ; stop = max(high of NR bars) + tick         # "spike above the MA" (p.156)
```

**Ambiguities & assumptions**
- **Narrow range.** ASSUMPTION: 2–3 consecutive bars each with range < 0.7 × ATR(14), each touching the EMA.
- **Target.** ASSUMPTION: the prior selloff low.

### 2.6 Continuation-gap retracement buy/sell

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Pullback to a gap (anticipation) | 40–41, 268–270 |
| Timeframe & holding period | Daily (also 60-min) | 268 |
| Universe / eligibility filters | Trend with a continuation gap: price kept moving and doubled the extension before the gap; or, after three waves, a gap near 50% of the move | 41, 268 |
| Market / regime filter | Void if price gaps down (up) to reach the entry target; avoid if hole-in-the-wall + 50-day EMA break + heavy volume | 222 |
| Setup conditions | Retracement approaching/entering the gap | 40 |
| Entry trigger & order type | Limit order within the gap's boundaries; defensive: wait until price enters the gap and moves forcefully away | 268–269 |
| Initial stop-loss | Not quantified | — |
| Exits: profit-taking | Bounce should reach ≥ 38% retracement of the countertrend wave; the trend should resume into a third primary wave | 40–41 |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Gap identification | extension doubled after the gap | gap near the 50% point of a 3-wave move | 41, 268 |
| Minimum bounce | 38% of the countertrend wave | — | 40 |

**Key quotes**
- "Specifically, a retracement approaching or entering the gap should reverse sharply, before it gets filled." [p. 40]
- "Wait until you can count three distinct trend waves, up or down." [p. 268]
- "In a nutshell, a selloff into a continuation gap can be bought except when price gaps down to reach the entry target." [p. 222]

**Pseudocode**
```
gap = continuation_gap(trend)          # 50% of 3-wave move or extension doubled (p.41, 268)
if pullback reaches gap and not gapped_into(gap):
    limit buy at gap_top (aggressive) | wait: low inside gap then close > gap_top (defensive)
    stop = gap_bottom - k*ATR          # ASSUMPTION (gap fill = failure)
    target1 = pullback_start - 0.38*(pullback_start - pullback_low)... ; target2 = trend high
```

**Ambiguities & assumptions**
- **Stop.** Not stated. ASSUMPTION: a close below the gap's far edge (a full fill) is the failure point.
- **Three-wave counting.** ASSUMPTION: zig-zag with a 5% (or 2 × ATR) reversal threshold.

### 2.7 Breakaway-gap pullback / post-gap range

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Gap continuation (two variants) | 266–267 |
| Timeframe & holding period | Daily | 267 |
| Universe / eligibility filters | Breakaway gap out of a base (new trend) | 266 |
| Market / regime filter | Not specified | — |
| Setup conditions | (a) A post-gap range develops; (b) a low-volume countertrend flag retracing ≤ 50% of the trend wave that includes the gap | 266–267 |
| Entry trigger & order type | (a) Range breakout in the gap direction; (b) at the gap fill if reached, or on the flag breakout/breakdown | 266–267 |
| Initial stop-loss | Not specified | — |
| Exits: profit-taking | Primary trend should carry beyond the breakout high / selloff low | 267 |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Key quotes**
- "it makes sense to buy a low volume decline after a notable break- out, or to sell the low volume bounce after a notable breakdown." [p. 267]
- "Enter right at the gap fill if the coun- terwave reaches that far, or wait for a flag breakout or breakdown." [p. 267]

**Pseudocode**
```
if breakaway_gap(base_len>=20, gap > 1*ATR):
    flag = countertrend with volume < 0.8*avg and retrace <= 0.5*wave
    enter at gap_fill (limit) or on flag break ; stop below flag low   # ASSUMPTION
```

**Ambiguities & assumptions**
- **Partly codable:** no stop or volume threshold. ASSUMPTION: "low volume" = below the 20-day average; stop below the flag low.

### 2.8 Exhaustion-gap fade

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Countertrend reversal after a climax gap | 269–270 |
| Timeframe & holding period | Daily | 269 |
| Universe / eligibility filters | Extended (parabolic) trend that prints a gap which then fills | 269–270 |
| Market / regime filter | Not specified | — |
| Setup conditions | Parabolic move; gap fills (example: within the first hour) | 269 |
| Entry trigger & order type | Short on a bounce into the last swing high prior to the gap, or after a notable reversal (example: a down gap) | 269 |
| Initial stop-loss | Not specified | — |
| Exits: profit-taking | Reversal expected at the same angle as the primary trend | 270 |
| Exits: trailing / time / signal | Already-positioned traders take profits on the gap | 270 |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Key quotes**
- "enter a trade in the opposite direction of the trend in place prior to the gap." [p. 270]
- "The trader can enter the short sale on a bounce into the last swing high, prior to the gap (1), or wait for a notable reversal" [p. 269]

**Pseudocode**
```
if trend_return(10d) > X and gap_up and gap_filled_same_day:
    short on rally to swing_high_before_gap or on next down-gap ; stop above gap-day high   # ASSUMPTION
```

**Ambiguities & assumptions**
- **Partly codable:** "parabolic" is undefined. ASSUMPTION: a 10-day return > 3 × the 60-day median 10-day return, and the gap filled intraday.

### 2.9 Fibonacci whipsaw (62/78 failure of a failure)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Pullback failure-of-a-failure (countertrend wave fails at deep retracement) | 162–163 |
| Timeframe & holding period | Any; best within a larger trend; example on 60-min with hours-long hold | 163 |
| Universe / eligibility filters | Instrument in a larger-scale trend | 163 |
| Market / regime filter | Trade in the direction of the larger trend | 163 |
| Setup conditions | Countertrend swing pierces the 62% retracement and tags 78% | 163 |
| Entry trigger & order type | Enter when price crosses back through the 62% level; add on pullbacks (e.g., at 50%) | 162–163 |
| Initial stop-loss | Just beyond the 62% retracement | 163 |
| Exits: profit-taking | Inception point of the countertrend swing (prior low/high), or hold for trend resumption | 163 |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Add at the 50% retracement pause | 163 |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pierce level | 62% | Gartley 78%; Butterfly 127% extension | 163 |
| Tag level | 78% | — | 163 |
| Add level | 50% | — | 163 |

**Key quotes**
- "Use this crossing as your initial entry signal," [p. 162]
- "giving the trader an oppor- tunity to add to the short position, with a stop loss just above the 62% retracement." [p. 163]

**Pseudocode**
```
# downtrend example (MasterCard)
A = swing high ; B = swing low (inception of bounce) ; leg = A - B
if high >= B + 0.786*leg after crossing B + 0.618*leg:
    when close < B + 0.618*leg: short ; stop = B + 0.618*leg + buffer         # p.163
    add on pause near B + 0.5*leg ; target = B                               # p.163
```

**Ambiguities & assumptions**
- **Stop buffer.** ASSUMPTION: 0.25 × ATR above the 62% level.
- **Cross-verification requirement** for Fib trades in general ("never trade a Fibonacci retracement level in a vacuum" [p. 161]). ASSUMPTION: no extra confluence required for the whipsaw variant, since it is itself a failure signal.

### 2.10 2B failed-breakout short

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Failed breakout reversal (short) | 148 |
| Timeframe & holding period | All time frames; best on daily | 148 |
| Universe / eligibility filters | Instrument at a new high; best when the breakout came on high volume "after much effort" | 148 |
| Market / regime filter | Short-sale vetoes in 2.25 (RSI bottom-20% turn, BB 75–100% outside, opex/month-end) | 151 |
| Setup conditions | Breakout fails back under the last swing high, usually within 1–3 bars | 148 |
| Entry trigger & order type | Sell when price trades through the low of the first recovery bounce | 148 |
| Initial stop-loss | Not stated. ASSUMPTION below | — |
| Exits: profit-taking | Not stated | — |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Failure window | 1–3 bars | "can occur much later" | 148 |

**Key quotes**
- "The 2B reversal sets up when a financial instrument at a new high fails a breakout by dropping under the last swing high." [p. 148]
- "The actual sell signal triggers when price trades through the low of the first recovery bounce." [p. 148]

**Pseudocode**
```
if high[t0] > prior_swing_high and within 1..3 bars close < prior_swing_high:
    bounce = first up-bar after failure ; short when low < low(bounce)        # p.148
    stop = high[t0] + tick (ASSUMPTION) ; target = next support / 2.23
```

**Ambiguities & assumptions**
- **Stop and target** are not in this book. ASSUMPTION: stop above the failed high; target = prior swing low.

### 2.11 Narrow-range short at support

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Anticipatory short in congestion | 149 |
| Timeframe & holding period | Daily | 149 |
| Universe / eligibility filters | Developing downtrend | 149 |
| Market / regime filter | Short-sale vetoes (2.25) | 151 |
| Setup conditions | Tight 2–3-day congestion at a key support after a selloff | 149 |
| Entry trigger & order type | Sell short within the 2–3-day range | 149 |
| Initial stop-loss | Buy-stop just above the short-term high | 149 |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Key quotes**
- "Enter the sell order within the two- or three-day range, placing a buy cover stop just above the short-term high" [p. 149]

**Pseudocode**
```
if downtrend and range(last 2-3 days) < 0.6*ATR and near support:
    short at mid-range limit ; stop = max(high[last 3]) + tick                 # p.149
```

**Ambiguities & assumptions**
- **"Tight", "key support", "downtrend".** ASSUMPTION: 3-day range < 0.6 × ATR(14); support = the prior swing low within 2%; downtrend = close < EMA50 < EMA200.

### 2.12 Pullback short into resistance, with the support-break analog filter

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Short on a weak rally (failure/confirmation) | 148–150 |
| Timeframe & holding period | Daily, 60-min | 149–150 |
| Universe / eligibility filters | Instrument with obvious technical damage, usually in a downtrend; weakest sectors | 148, 152 |
| Market / regime filter | Analog filter: in the prior 1–2 years, past support breaks were followed by a spike above new resistance and then another selloff (failure/confirmation). Don't short at a price with many historic reversals. Vetoes in 2.25 | 149–150 |
| Setup conditions | Breakdown, then a squeeze back above the breakdown level (e.g., to the 62% retracement, 20-day SMA or a partially filled gap) | 149–150 |
| Entry trigger & order type | Short when the rally spikes into/above resistance and rolls over; failure-of-a-failure sell when price re-crosses the broken support | 148, 150 |
| Initial stop-loss | Not stated | — |
| Exits: profit-taking | Not stated | — |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Analog look-back | 1 year | 1–2 years; average Fib retracement of post-break bounces | 149 |
| Resistance candidates | 20-day SMA, partially filled gap | 62% retracement (example) | 149–150 |

**Key quotes**
- "The second scenario presents the most advantageous short selling conditions." [p. 149]
- "don’t sell short if the instrument printed a series of notable reversals near that price." [p. 150]
- "This “failure of a failure” signal offers more reliable trade entry for two reasons" [p. 151]

**Pseudocode**
```
analog = [bounce_retrace(b) for b in support_breaks(last 252-504 days)]
if pattern(analog) == "failure/confirmation":                                   # p.149
    level = mean(analog) Fib level ~ nearest of (SMA20, gap, 0.62 retr)
    after breakdown: when rally reaches level and closes back below broken support: short
    stop = rally high + tick (ASSUMPTION)
```

**Ambiguities & assumptions**
- **Partly codable:** classifying past breaks needs thresholds. ASSUMPTION: "spike above new resistance" = a close above the broken support within 10 sessions, followed by a new low within 20.

### 2.13 Tiered Fibonacci pullback buy (38/50/62)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Pullback buy with scaled entries ("buying the dip") | 206–208 |
| Timeframe & holding period | Daily; days | 206–207 |
| Universe / eligibility filters | Stock pulling back after a strong rally wave | 206 |
| Market / regime filter | Only if the average entry passes the 3:1 test | 208 |
| Setup conditions | Fibonacci grid on the last rally wave | 206 |
| Entry trigger & order type | Limit buys: ¼ at 38%, ¼ at 50%, ½ at 62% (300/300/600 of 1,200 shares) | 206 |
| Initial stop-loss | Entered right after the third fill, around the 70% retracement; out if price reaches 78% | 206 |
| Exits: profit-taking | Swing inception point (the prior high) | 207 |
| Exits: trailing / time / signal | After a stop-out, watch for the failure-of-a-failure re-entry when price rallies back above 62% | 206 |
| Position sizing | Planned total split 25/25/50; you may get only part if price turns early | 206–208 |
| Adding to / pyramiding | This is the scaling plan; no adds beyond it | 206 |
| Portfolio limits | Reward from the average entry to the next resistance ≥ 3 × the distance to the stop | 208 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Tiers | 38 / 50 / 62% | — | 206 |
| Weights | 25 / 25 / 50% | — | 206 |
| Stop | ~70% retracement | exit at 78% | 206 |
| Min reward:risk | 3:1 from average entry | — | 208 |
| Example | fills 16.32, 15.89, 15.45 → avg 15.77; target 17.73 | trade C: 600 shares avg 20.01 | 206–207 |

**Key quotes**
- "Put up a Fibonacci grid, buying 300 shares at the 38% retracement, 300 shares at the 50% retracement, and 600 shares at the 62% retracement." [p. 206]
- "Enter the stop loss immediately after buying the third position, placing it around the 70% level to avoid whipsaws" [p. 206]
- "The distance from this number up to the next resistance level (profit target/reward) should be at least three times the distance down to your stop loss" [p. 208]

**Pseudocode**
```
A = wave low ; B = wave high ; L = B - A
tiers = [(B-0.382L, .25), (B-0.5L, .25), (B-0.618L, .5)]
avg = weighted avg of tier prices ; stop = B - 0.70L ; target = next resistance (B)
if (target - avg) >= 3*(avg - stop):                                   # p.208
    place limit buys at tiers ; after 3rd fill set stop                  # p.206
    exit at target ; on stop, watch close > B-0.618L for re-entry (2.9 logic)
```

**Ambiguities & assumptions**
- **Stop before the third fill.** Not stated. ASSUMPTION: a provisional stop at 70% from the first fill.
- **"Strong rally wave".** ASSUMPTION: a leg ≥ 3 × ATR(14) with ≥ 70% up-closes.

### 2.14 Parabolic-move ledge buy (half size, one retry)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Pullback after a parabolic move (no Fib levels reached) | 208 |
| Timeframe & holding period | Daily | 208 |
| Universe / eligibility filters | Pullbacks after parabolic rallies/selloffs, unlikely to reach 38% | 208 |
| Market / regime filter | Reward:risk "looks" favorable | 208 |
| Setup conditions | Small ledges/consolidations inside the parabolic leg | 208 |
| Entry trigger & order type | Limit orders at the ledges, totalling half normal exposure; the last entry scrapes against whatever support exists | 208 |
| Initial stop-loss | Tight, just under (above, for shorts) the final entry | 208 |
| Exits: profit-taking | Not specified (2.23) | — |
| Exits: trailing / time / signal | If stopped: reboot once with the other half; if that fails, move on | 208 |
| Position sizing | ½ normal per attempt, two attempts max | 208 |
| Adding to / pyramiding | No | — |
| Portfolio limits | Not specified | — |

**Key quotes**
- "place orders at those levels that add up, in total, to just half your normal exposure" [p. 208]
- "If this trade fails, it’s time to cry uncle and move on to a new opportunity." [p. 208]

**Pseudocode**
```
ledges = consolidation_levels(parabolic_leg) below price (top 2-3)
attempt 1: limits at ledges sum 0.5*size ; stop below last ledge
if stopped: attempt 2 with 0.5*size on fresh ledges ; if stopped: abandon
```

**Ambiguities & assumptions**
- **Partly codable:** ledge detection. ASSUMPTION: ≥ 2 overlapping bars with range < 0.5 × ATR inside the leg.

### 2.15 Range fade (countertrend within a mature range)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Countertrend range trading | 166–168 |
| Timeframe & holding period | Any; until the other side of the range | 167–168 |
| Universe / eligibility filters | Well-defined trading range; recommended for newer traders | 165–166 |
| Market / regime filter | Let congestion set up first (most whipsaws come early); best in the "sweet spot" before price goes dull ahead of the break | 166 |
| Setup conditions | Support/resistance boundaries | 166 |
| Entry trigger & order type | Buy weakness at support / sell strength at resistance, at a single price level; no chasing | 167 |
| Initial stop-loss | Just outside support/resistance | 167 |
| Exits: profit-taking | Other side of the range, then look to reverse | 167–168 |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Avoid repeated re-entries | 167 |
| Portfolio limits | Not specified | — |

**Key quotes**
- "Set your stop loss just outside support or resistance." [p. 167]
- "Try to get it right the first time because too many reentries, triggered by poor timing, will eat up the trade’s profitability." [p. 167]
- "Once established, the position should be held until price pulls into the other side of the trading range." [p. 168]

**Pseudocode**
```
if range_age >= N and touches(S) >= 2 and touches(R) >= 2:
    limit buy at S + eps ; stop = S - buffer ; target = R - eps ; then short at R, stop R + buffer
    max 1 re-entry per side
```

**Ambiguities & assumptions**
- **Maturity.** ASSUMPTION: range ≥ 15 bars with ≥ 2 touches per side; buffer = 0.25 × ATR.

### 2.16 Falling-knife tiered / outer-limit entry

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Countertrend high-volatility buy | 165–166 |
| Timeframe & holding period | Daily/intraday | 166 |
| Universe / eligibility filters | A plunging stock near a predicted reversal level (S/R, retracement, gap) | 166 |
| Market / regime filter | Experienced traders only | 165 |
| Setup conditions | Expected reversal level from support/retracement analysis | 166 |
| Entry trigger & order type | (a) Tiered limit orders on both sides of the expected level; (b) a single order just below the extreme level where everyone else gives up | 166 |
| Initial stop-loss | (a) Just below the last order; exit everything if hit | 166 |
| Exits: profit-taking | Example exit: 62% bounce of the last selloff leg, with cross-verification | 321–322 |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Small positions (example) | 167 |
| Adding to / pyramiding | Within the tiers only | 166 |
| Portfolio limits | Not specified | — |

**Key quotes**
- "Break up your position into tiered limit orders on both sides of the expected reversal level." [p. 166]
- "Then place a stop loss just below the last order, and exit the entire position if price drops that far." [p. 166]
- "This outer limit often identifies the exact turning point because it washes out everyone else" [p. 166]

**Pseudocode**
```
lvl = expected reversal level
variant A: limits at lvl+a, lvl, lvl-a ; stop = lvl - a - buffer           # p.166
variant B: single limit at lvl - b (where variant-A stop sits) ; stop ASSUMPTION
exit near 62% retracement of last down leg if confluent (p.321-322)
```

**Ambiguities & assumptions**
- **Tier spacing.** ASSUMPTION: a = 0.5 × ATR; variant B's order sits at the variant-A stop (per the Fuqi caption [p. 167]); variant-B stop = 1 × ATR below the fill.

### 2.17 Stop-run (rinse-job) reversal entry

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Fade a stop-gunning thrust beyond S/R | 232, 235, 272–274 |
| Timeframe & holding period | Intraday to 3–5 sessions | 274 |
| Universe / eligibility filters | Ranges with obvious stop clusters; index futures signals are most predictive | 272 |
| Market / regime filter | Not on trend days (2.25) | 248 |
| Setup conditions | Price thrusts through support/resistance (common stop level) and momentum fades; or a daily hammer/doji at a range edge | 235, 273 |
| Entry trigger & order type | Enter as soon as momentum fades after the stops run, back inside the range | 235 |
| Initial stop-loss | One tick beyond the rinse-job extreme (Chevron: < 1 pt above the 60-min high) | 232, 235 |
| Exits: profit-taking | Range rinse: expect a trend out of the opposite side of the range | 273 |
| Exits: trailing / time / signal | Intraday: price must snap back by the close of the next 15-min bar; daily: the imbalance lasts 3–5 sessions | 272, 274 |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Snap-back window | close of the next 15-min bar | — | 272 |
| Edge duration | 3–5 sessions | — | 274 |

**Key quotes**
- "stand aside until the commonly placed stops are run, and then jump in as soon as momentum fades." [p. 235]
- "place the stop loss one tick below the rinse job extreme." [p. 235]
- "the buy-sell imbalance will persist for just three to five sessions before new money comes in" [p. 274]

**Pseudocode**
```
lvl = range support (long case)
if low < lvl - x and close back > lvl within next 15-min bar:          # p.272
    buy ; stop = rinse_low - tick                                        # p.235
    target = range resistance / breakout of opposite side ; time stop 5 sessions (daily version)
```

**Ambiguities & assumptions**
- **Thrust size.** ASSUMPTION: x ≥ 0.25 × ATR beyond the level. "Momentum fades" = the first bar closing back inside the range.

### 2.18 Options-expiration magnetic-strike trades

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Calendar / mean-reversion to round numbers | 83–87 |
| Timeframe & holding period | Expiration week, days | 84 |
| Universe / eligibility filters | Highly liquid optionable stocks; best: stocks recovering with higher lows, trading at 28–29, 38–39, 48–49 | 84 |
| Market / regime filter | Not at a new high (strong stock) / new low (weak stock); expect no follow-through on breakouts during expiration week | 83–84 |
| Setup conditions | (a) Wed–Fri: a strong stock sells off into a strike; (b) early in the week: liquid stocks just under/over a magnetic level | 84 |
| Entry trigger & order type | (a) Buy (or short after a rally into a strike) Wed–Fri afternoon; (b) get on board for a trip into the number | 84 |
| Initial stop-loss | Not specified | — |
| Exits: profit-taking | The round-number strike; take profits aggressively | 84 |
| Exits: trailing / time / signal | Dynamic trailing stop a fixed length behind price once within 20–30¢ of the strike | 84 |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Reduce exposure in expiration week; midweek shakeout (Tue–Thu) → step aside | 86–87 |

**Key quotes**
- "Buy between Wednesday and Friday afternoon after a strong stock sells off into a strike, or sell short after it rallies into a strike." [p. 84]
- "Issues that are trading toward eights or nines, i.e., 28–29, 38–39, and 48–49, are almost perfectly positioned" [p. 84]

**Pseudocode**
```
if is_expiration_week:
    (b) Mon-Tue: if stock in uptrend recovery (higher lows) and price in [k*10-2, k*10-1]: buy ; target = k*10
        trail fixed d once within 0.20-0.30 of target
    (a) Wed-Fri: if strong stock fell into strike S (|close-S| small): buy ; exit by next week
```

**Ambiguities & assumptions**
- **Partly codable:** strike = highest open interest, which needs options data. ASSUMPTION: round multiples of 5/10 as a proxy. Trail d = 0.10.

### 2.19 Post-earnings and post-news re-entry

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Event pullback (after the news has been absorbed) | 88–90, 259–260 |
| Timeframe & holding period | Daily + 60-min; days | 90, 260 |
| Universe / eligibility filters | Stocks with fresh earnings/news | 90 |
| Market / regime filter | Exit before the scheduled release; never hold through earnings unhedged | 88, 236 |
| Setup conditions | Solid report: 2–3 days of selling into, but not through, intermediate support. Any news gap: assume the reversal reaches the 60-min 50-period EMA | 90, 260 |
| Entry trigger & order type | Buy a 60-min basing pattern at support; or tiered limit orders near the 60-min 50-EMA. Conservative: wait for a lower-TF breakout (60-min bull flag). Short side: let the bounce run, short at resistance such as the gap-down day's open | 90, 260 |
| Initial stop-loss | Hold "until the primary trend reasserts itself or your stop gets hit" (level not given) | 260 |
| Exits: profit-taking | Spike through the pre-release high | 90 |
| Exits: trailing / time / signal | Exit immediately if a double top forms at the news-day high | 260 |
| Position sizing | Tiered small pieces | 260 |
| Adding to / pyramiding | Within the tiers | 260 |
| Portfolio limits | Not specified | — |

**Key quotes**
- "play the stock into the minutes ahead of an earnings report, but get out before the numbers are actually released." [p. 88]
- "Look for a 60-minute basing pattern at this level, and enter the trade in anticipation of a buying spike up and through the prerelease high." [p. 90]
- "Assume the reversal will eventually reach the 50-period EMA before there’s a major counterswing." [p. 260]

**Pseudocode**
```
exit all positions in stock before scheduled release                      # p.88
after release (good news gap up):
    wait 2-3 sessions of selling ; require low > intermediate support
    tiers near EMA50(60-min) ; stop below support (ASSUMPTION)
    target = pre-release high ; exit if double top at news-day high       # p.90, 260
```

**Ambiguities & assumptions**
- **"Intermediate support" and "60-min basing pattern".** ASSUMPTION: support = the 20-day low before the report; base = ≥ 6 sixty-minute bars with range < 1 × daily ATR.

### 2.20 Weekly-chart remote entry (DCA into range support)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position trade, range-support accumulation | 215–218 |
| Timeframe & holding period | Weekly charts; weeks to months; orders placed on weekends | 215 |
| Universe / eligibility filters | Slower movers; ETFs preferred; 10–15-year look-back for swings | 217 |
| Market / regime filter | Weekly 5-3-3 Stochastics: buy on the upswing, sell on the downswing; weekly BB(20,2) | 217 |
| Setup conditions | Breakout followed by a weekly trading range (example: support ~73 after a rally to 77.50) | 215 |
| Entry trigger & order type | Three reduced-size limit orders in the lower half of the range (75, 74, 73, average ~74); or one limit at support, or two pieces either side of it | 215–216 |
| Initial stop-loss | Just under the sideways pattern (~72); loose, beyond the current swing | 215, 217 |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Review on evenings/weekends only | 218 |
| Position sizing | Small positions, no margin | 217 |
| Adding to / pyramiding | DCA aligned with S/R | 217 |
| Portfolio limits | Limit orders only; never market orders; never chase | 218 |

**Key quotes**
- "this number, you enter three reduced-size positions, at 75, 74, and 73, over the course of a few weeks." [p. 215]
- "Build the position over time with dollar cost averaging, but line up your entries with large-scale support and resistance." [p. 217]

**Pseudocode**
```
weekly: range = (S, R) after breakout ; lower_half = [S, (S+R)/2]
place 3 limit buys evenly in lower_half (1/3 normal size each) ; stop = S - buffer
require weekly Stoch(5,3,3) turning up for new orders (ASSUMPTION per p.217 #9)
```

**Ambiguities & assumptions**
- **Exit.** Not given. ASSUMPTION: range top / weekly BB upper band.

### 2.21 Strength/weakness basket (Dow components ≥ 10% above the 200-day EMA)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Basket momentum / index outperformance | 209–211 |
| Timeframe & holding period | Multi-day; too labour-intensive for day/overnight flips | 210 |
| Universe / eligibility filters | Index/sector components; filter: at least 10% above the 200-day EMA (Dow example) | 211 |
| Market / regime filter | Enter when the index chart triggers (breakout, narrow range or pullback) | 211 |
| Setup conditions | Sort components by price change or % distance from the 200-day MA | 210 |
| Entry trigger & order type | Buy (or short) the whole basket on the index signal | 211 |
| Initial stop-loss | Index/sector chart signal, composite chart signal, or a flat $/% stop on the whole group | 211 |
| Exits: profit-taking | Same three methods | 211 |
| Exits: trailing / time / signal | Judge vs the index; no point if not beating it "by a wide margin" | 211 |
| Position sizing | Equal shares when prices are similar; 2–3× shares for much cheaper stocks | 211 |
| Adding to / pyramiding | No individual changes after entry; trade as one instrument | 211 |
| Portfolio limits | Total basket risk within account tolerance | 211 |

**Key quotes**
- "A simple filtering process utilizes a subgroup of issues that are at least 10% above the 200-day EMA." [p. 211]
- "it’s absolutely vital that the entire basket be traded as a single instrument in order to maintain its risk characteristics." [p. 211]

**Pseudocode**
```
members = [s for s in DJIA if close/EMA200(s) - 1 >= 0.10]                  # p.211
on index_signal(DJIA: breakout | NR | pullback): buy equal-$ basket(members)
stop: basket composite drawdown >= X% or index signal reverse ; benchmark vs index
```

**Ambiguities & assumptions**
- **Index signal and X.** ASSUMPTION: index close above its 20-day high; X = 5%.

### 2.22 Stealth breakout (creep into multi-tested resistance)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Anticipatory breakout | 251 |
| Timeframe & holding period | 15-min bars; intraday to days | 251 |
| Universe / eligibility filters | Level that has failed multiple times in the last 3–5 sessions | 251 |
| Market / regime filter | Not specified | — |
| Setup conditions | Slow crawl toward the level: a series of small 15-min bars with no pullbacks | 251 |
| Entry trigger & order type | Expect the level to be hit and expanded through quickly (example: Brandywine, 4 reversals at 8.34, then a creep and vertical breakout) | 250–251 |
| Initial stop-loss | Not specified | — |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Key quotes**
- "This slow crawl will print a series of small bars with no pullbacks on the 15-minute chart." [p. 251]

**Pseudocode**
```
R = level with >=3 rejections in last 3-5 sessions
if last k 15-min bars: higher lows, range < 0.5*avg range, distance to R shrinking: buy-stop at R + tick
stop = low of creep sequence (ASSUMPTION)
```

**Ambiguities & assumptions**
- **Partly codable:** entry/stop are not given. ASSUMPTION: k = 6 bars; buy-stop just above R; stop below the creep's start.

### 2.23 Overlay: trailing-stop and exit protocol

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Exit/stop overlay for all setups | 231–235, 319–322 |
| Timeframe & holding period | One time frame below the trade chart | 233 |
| Universe / eligibility filters | All positions | — |
| Market / regime filter | — | — |
| Setup conditions | Profit target fixed before entry (next S/R reduced by barriers); failure target = where the pattern breaks | 140, 231, 303 |
| Entry trigger & order type | — | — |
| Initial stop-loss | Where the pattern breaks; avoid exact trendlines/round numbers/MAs. Momentum entries: flat-$ stop or the 8-bar SMA on 15-min (60-min for bigger breakouts). Avoid % stops unless no structure exists | 230–231, 235, 317 |
| Exits: profit-taking | Sell blind into the profit target; old gap fills and confluent 62% retracements are blind-exit levels; exit on rapid bar expansion | 319, 321 |
| Exits: trailing / time / signal | No trailing until wide-range bars eject in your favor. Then trail behind congestion on the lower TF (60-min for daily, 15-min for 60-min), moving up after each new sideways pattern. At ~75% of the way to target trail aggressively, and place a second order at the target. Near target: 10/15/20¢ trail. Time stop: exit before target if the holding window is closing | 233, 319–321 |
| Position sizing | — | — |
| Adding to / pyramiding | Re-entry after a stop is allowed with fresh analysis (Schlumberger failure of a failure) | 244, 317–318 |
| Portfolio limits | — | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Aggressive-trail trigger | ~75% of entry→target | — | 233 |
| Momentum MA stop | 8-bar SMA, 15-min | 60-min 8-bar | 235 |
| Near-target trail | 10/15/20¢ | — | 319 |
| % stop (fallback) | 2/5/10% | — | 317 |

**Key quotes**
- "Continue this process until the position reaches about 75% of the distance between the entry and the profit target." [p. 233]
- "pull up an 8-bar SMA on the 15-minute chart, and exit the trade if price violates it." [p. 235]
- "Traders gain tremendous discipline by selling blind into a profit target." [p. 319]

**Pseudocode**
```
stop = initial_failure_stop
if not trailing and wide_range_bar_in_favor: trailing = True
if trailing:
    stop = max(stop, low of latest consolidation on lower TF)              # p.233
if progress >= 0.75*(target-entry): stop = max(stop, price - 0.15) ; also place limit sell at target   # p.233, 319
if time_in_trade >= holding_window and price < target: exit                 # p.320-321
```

**Ambiguities & assumptions**
- **"Wide range bar".** ASSUMPTION: range ≥ 1.5 × ATR(14) closing in the top (bottom) 25%.
- **Consolidation zone.** ASSUMPTION: ≥ 3 overlapping lower-TF bars.

### 2.24 Overlay: daily collar (exposure and scaling regime)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Regime-based exposure/sizing overlay | 306–315 |
| Timeframe & holding period | Set each morning; also multi-day | 306, 310 |
| Universe / eligibility filters | Portfolio | 305 |
| Market / regime filter | Aggressive when index futures trend in lockstep through barriers with few obstacles ahead; defensive when they diverge, sit between barriers, against an overnight gap, or into FOMC/labor reports | 306–311 |
| Setup conditions | — | — |
| Entry trigger & order type | Aggressive: all-in, scale out. Loose-collar scaling: 3–4 pieces in declining size, or equal pieces with a pre-computed average entry. Defensive: two smaller pieces; the second equal piece only once the trade shows a profit; no third | 311, 313–315 |
| Initial stop-loss | With equal pieces in a moving market, keep the first stop until fully positioned, then re-set | 314 |
| Exits: profit-taking | — | — |
| Exits: trailing / time / signal | Defensive: shorter holding periods, fewer overnights | 311 |
| Position sizing | Defensive total exposure ≤ ⅓ of the account; supportive ≤ 90% of equity; margin only with years of profitability | 312 |
| Adding to / pyramiding | As above | 313–315 |
| Portfolio limits | Max $ loss per trade fixed in advance | 305 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Defensive exposure cap | ⅓ of the account | — | 312 |
| Aggressive exposure cap | 90% of equity | — | 312 |
| Scale pieces | 3–4 (loose); 2 (defensive) | Apple example 500/300/200 | 313–315 |

**Key quotes**
- "Limit your exposure to just one-third of total account size during adverse periods, when a defensive collar is utilized." [p. 312]
- "Trade three to four pieces in declining size." [p. 313]
- "Limit yourself to just two pieces applied at the right time, with each segment smaller than usual" [p. 315]

**Pseudocode**
```
collar = AGGRESSIVE if (sp_trend == nq_trend != FLAT and both cleared barrier and VIX < 25) else DEFENSIVE   # ASSUMPTION mapping
if overnight_gap_against_book or event_day(FOMC, NFP): collar = DEFENSIVE        # p.310-311
cap = 0.90*equity if collar == AGGRESSIVE else equity/3                          # p.312
pieces = [0.5, 0.3, 0.2] if AGGRESSIVE else [0.5 (entry), 0.5 (only if in profit)]   # p.313-315
```

**Ambiguities & assumptions**
- **Partly codable:** the collar is a judgment. ASSUMPTION mapping: aggressive requires the S&P and Nasdaq-100 futures both above (below) their prior 3-day high (low), and VIX < 25 [p. 307].

### 2.25 Overlay: market filters (trend day, VIX, calendar, long-cycle RS)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Filters / vetoes applied to the setups above | 53, 103, 151, 203, 247–248, 307 |
| Timeframe & holding period | Intraday and daily | — |
| Universe / eligibility filters | Relative-strength scan: top (bottom) 25% by % of 52-week high (low), then rank by (Close − EMA200)/EMA200 × 100. Liquidity ≥ 200k shares/day (60-day avg); small-cap sweet spot 200k–500k | 100–101, 196–197 |
| Market / regime filter | **Trend day** (skip reversal/fade setups 2.15, 2.17): up/down volume ≥ 80:20 with breadth beyond ±1,800–2,000; or TICK repeatedly beyond ±1,000, A/D beyond ±1,500 on both exchanges, up/down volume > 4:1, or index futures ±2%. **VIX:** risk rises sharply above 25 and again above 35. **Long-cycle:** avoid longs when smoothed RSI(14,7) or 17-17-1 Stochastics is above the upper line and turning down | 103, 203, 248, 307 |
| Setup conditions | **Short vetoes:** smoothed RSI(14,7) in the bottom 20% and turning up; a bar 75–100% outside the lower 20-period Bollinger Band; options-expiration week or month-end unless in a momentum bear market | 151–152 |
| Entry trigger & order type | **Stochastics 5-3-3 timing:** act on a lower high (higher low) near 80/20 followed by expansion; don't exit merely at an extreme | 98–99 |
| Initial stop-loss | — | — |
| Exits: profit-taking | — | — |
| Exits: trailing / time / signal | **Calendar:** dump into Tuesday's open after a trend carries from the prior week; exit before scheduled news | 106, 259 |
| Position sizing | Single-digit stocks: cut the intended size by ¼ to ½ | 197 |
| Adding to / pyramiding | — | — |
| Portfolio limits | — | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RS scan cut | top/bottom 25% | — | 101 |
| Trend-day volume | ≥ 80% one side | 90:10 days ~12/yr | 203 |
| VIX thresholds | 25, 35 | 10–25 low-risk regime | 307 |
| Power spike | volume ≥ 3 × 60-day avg + wide-range bar from S/R | — | 158 |

**Key quotes**
- "Run the 52-week high or low scan first, creating a list that contains just stocks in the top 25% for a strength list or bottom 25% for a weakness list." [p. 101]
- "Look for a lopsided tape in which 80% or more of total volume comes in on the buy side during a rally and sell side during a selloff." [p. 203]
- "Stand aside when the indicator reaches the bottom 20% of its range and then turns higher." [p. 151]
- "never sell short when a price bar drops 75% to 100% outside the bottom band." [p. 151–152]
- "The best signals unfold when Stochastics makes a lower high (or higher low) near the 80-20 line and then expands in the opposite direction." [p. 99]
- "Avoid long positions when the long-cycle indicator is pressed above the upper line and turning over" [p. 103]
- "Trading risk increased geometrically when VIX broke 25 and again when it broke 35." [p. 307]

**Pseudocode**
```
trend_day = (upvol_share >= .80 and |adv-dec| >= 1800) or (|TICK| > 1000 repeatedly) or (|futures_ret| >= .02)
short_veto = (rsi_s(14,7) in bottom 20% and rising) or (bar_below_lower_BB20 frac >= .75) or opex_week or month_end
long_veto  = rsi_s(14,7) > 80 and falling
universe   = top25(pct_of_52w_high) ranked by (C-EMA200)/EMA200
```

**Ambiguities & assumptions**
- **"Repeatedly".** ASSUMPTION: ≥ 3 TICK prints beyond ±1,000 before 11:00.
- **"Bottom 20% of its range"** for RSI. ASSUMPTION: RSI < 20 on a 0–100 scale. "Month-end" = the last 3 sessions.

### Non-codable / no-rule material (summary)

| Item | Content | Page |
|---|---|---|
| Level II tactics | Lowball quotes before the open; "step down, step up" re-entry after program selling (enter when a counter-impulse retakes 100% of the last stable level); pop tops/bottoms | 56–57 |
| QQQ trend-day short (case) | Short the bounce into the broken first-hour range; hold overnight if the final-hour low is untested | 53–55 |
| Overnight shock triage | Premarket bids just before 8:00; sell gap-through-support stocks 5–20¢ under the market if running lower | 66–69 |
| Fed-day cycle | Sidelines before 2:15 p.m.; action-reaction-resolution over the week | 81–82 |
| Window dressing and seasonality | Month/quarter-end markup, first day of the month positive, second day negative; Nov–Dec opex rally | 79–80, 112–113 |
| Shock spirals and VIX tactics | 5-/15-min and weekly patterns work; 60-min/daily chaos; VIX into resistance = buy equities | 93–95 |
| Ten reversal clues | Taylor 3-bar, BB pierce > 75%, Tuesday, 2B, volatility stall, blow-off, lower-TF reversal, candles, threes, hole-in-the-wall | 106–107 |
| Five Ss in pullbacks, yo-yo cures, trading-plan building blocks | Selection, Scalping, Size, Sidelines, Shorting; daily trade ration and gain/loss thresholds | 122–135 |
| Anticipation / rock-and-a-hard-place | Enter when one side "blinks"; NR7 coiled spring with stop beyond the NR7 bar | 187–189 |
| Morning mavericks and rotation | Green on a red open; leaders/laggards; 40-sector sort after the first hour | 201–203 |
| Tape-reading tells | Opening price principle, % in range, TICK ±1,400 third time, bid stretch at capitulation | 245–252 |
| Premarket checklist (15 items), end-of-day checklist (10 items) | Discretionary routines | 239–241, 257–259 |
| Psychology chapters | Performance cycles, overtrading, 20 trading mistakes, washing out, mastery traits | 286–300, 324–326 |

## 3. Risk & money-management rules

- **Reward:risk.** Require ≥ 3:1 from entry to target vs stop (first-hour trades [p. 169]; averaging entries [p. 208]). The Senior Housing example computes 9:1 [p. 303].
- **Stops:** initial stop where the pattern breaks, adjusted for rinse jobs; or lower-time-frame stops with planned re-entries until the total loss hits tolerance [p. 229–231]. Avoid stops at trendlines, round numbers and moving averages [p. 230]. Check how price behaved at common stop levels in the past [p. 234].
- **Expectancy:** (PW × AW) − (PL × AL) must be positive [p. 121].
- **Daily limits (yo-yo cure):** a fixed number of trades per session; a daily gain threshold ≥ 2× the daily loss threshold, then stop for the day [p. 130]. Example daily shutdown: $250 [p. 298].
- **Drawdown:** set a "fail-safe" drawdown level; stop trading and review when it is reached [p. 296]. Cut the average weekly trade count in half after a bad stretch [p. 291].
- **Sizing:** fix the maximum $ loss per trade in advance [p. 305]. Ignore margin when sizing [p. 205, 208]. Use smaller size for volatile stocks and small caps, larger for slow movers [p. 205]. Single-digit stocks get ¼–½ less [p. 197]. Increase average size slowly and step back if results don't follow [p. 209].
- **Margin:** avoid margin until a consistent profit record exists [p. 183]; collar caps in 2.24 [p. 312].
- **Events:** never hold through earnings unhedged [p. 88, 236]; sidelines before Fed decisions [p. 82]; never trade economic releases directly [p. 262]. Budget for 3–4 event shocks a year [p. 275].
- **Account structure:** keep a large part of wealth off-limits for the first five years; main account ≥ $50,000 for PDT headroom [p. 185].

## 4. Non-codable guidance

- **Diabolical thinking:** ask "which side has the biggest targets on their backs" [p. 28]. The lazy trade gets punished [p. 213].
- **Trend relativity:** longer time frames take priority; a daily selloff bounces at weekly support, and a 60-min uptrend fails at daily resistance [p. 74, 200].
- **Context and swing proportionality:** swings repeat their lengths; vertical swings end sooner; ranges often fill the first 38% of a return trip [p. 138, 143].
- **Convergence-divergence** reading between index futures, sectors and positions [p. 145–147].
- **Personal fit:** match holding period, instruments and style to lifestyle; keep a journal [p. 122–128].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - 5/15/60-min and daily OHLCV for NIFTY 50 / F&O stocks, NIFTY/BANKNIFTY futures and index ETFs;
  - India VIX;
  - NSE F&O open interest by strike (2.18);
  - corporate results calendar (2.19);
  - NSE advance/decline counts (2.25).
- **Testability with our data:**
  - mechanical after the stated assumptions: 2.1–2.5, 2.9–2.11, 2.13, 2.15, 2.17, 2.20, 2.21, 2.23, 2.25;
  - need extra labelling or event data: 2.6–2.8, 2.12, 2.14, 2.16, 2.18, 2.19, 2.22, 2.24.
- **Market-structure differences:**
  - **Session:** 09:15–15:30 IST, so the first hour is 09:15–10:15. The pre-open call auction (09:00–09:08) replaces the US premarket; the US 8:00 a.m. quote-painting rule does not transfer. ASSUMPTION: use GIFT Nifty as the overnight proxy.
  - **Shorting:** NSE cash shorts are intraday only. Multi-day shorts (2.5, 2.10–2.12) must use stock futures.
  - **Expiry calendar:** NSE monthly/weekly expiry falls on a fixed weekday that has changed over time. ASSUMPTION: check the current calendar, and remap the book's "Wed–Fri of expiration week" to the 2–3 sessions before expiry.
  - **Liquidity filters:** convert share-count filters (5M; 200k–500k) to turnover (₹ crore/day). Convert cent-based buffers, stops and trails (a few cents, 20–30¢, 10–20¢) to tick or ATR multiples (NSE tick ₹0.05 for most stocks; ASSUMPTION).
  - **Breadth:** NYSE TICK has no NSE analogue. Scale advance/decline thresholds to the universe size (ASSUMPTION).
  - **Circuit limits** can block exits on gap days (relevant to 2.2, 2.7 and 2.8).

## 6. Verdict

- **Codeability:** Medium-high for a narrative book. Several setups carry explicit numeric rules:
  - first-hour range: 15–20% stop, 3:1 filter;
  - bilateral range;
  - tiered Fibonacci buy: 38/50/62, 70% stop, 3:1;
  - Fibonacci whipsaw;
  - 50-EMA plays;
  - rinse-job entry;
  - the collar exposure caps.

  Gap, earnings and expiration plays are partly discretionary.
- **Priority for backtesting:**
  - High: 2.1 (intraday NIFTY futures and liquid F&O stocks), 2.13, 2.9 and 2.4 (daily pullbacks), with the 2.23 exit overlay and the 2.25 filters.
  - Medium: 2.2, 2.3, 2.15, 2.17 and 2.21.
  - Low: 2.18 (needs OI) and 2.19 (needs event data).
- **Top 3 things a coder is most likely to get wrong**
  1. Placing the first-hour (and bilateral) stop at the far end of the range. The book puts it 15–20% of the range height back inside from the broken edge, and skips trades without ≥ 3:1 room to the last 15-min swing [p. 168–169, 172].
  2. Treating continuation-gap and 50-EMA pullbacks as automatic buys. The continuation-gap trade is void when price *gaps* into the level [p. 222]. The 50-EMA trade comes after a fresh breakout has pulled all the way back, ideally confirmed by a 60-min reversal [p. 154].
  3. Trailing too early or using the Stochastics extreme as the signal. Trailing starts only after wide-range bars eject in your favor, and tightens at ~75% of the way to target [p. 233]. The Stochastics signal is the lower-high/higher-low pattern near 80/20, not the crossing [p. 98–99].
