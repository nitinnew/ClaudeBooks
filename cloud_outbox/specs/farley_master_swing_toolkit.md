# The Master Swing Trader Toolkit: The Market Survival Guide — Alan S. Farley (McGraw-Hill, 2010)

- **Source file:** Google Drive `0229_The Master Swing Trader Toolkit.pdf` (file id `1gC7mBKgEUnxkW9D29NFrtL4O9_2wCg4S`, 5,332,819 bytes), 353 PDF pages with a text layer.
- **Text file used:** text/farley_master_swing_toolkit.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index). The printed page number is usually PDF page − 21 (printed p. 147 = [[PAGE 168]]), but always take N from the marker, not from the contents list.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/farley_master_swing_toolkit.md text/farley_master_swing_toolkit.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 343]] (front matter, Chapters 1–12, glossary, bibliography).
  - **Skipped:** only the index, [[PAGE 344]]–[[PAGE 353]]. It is a keyword index with page numbers and contains no trading rules.
  - **Narrative chapters with few or no codable rules:**
    - Ch. 5 "The Nature of Winning" (psychology, plan building);
    - Ch. 7 "Market Entry" (capitalisation, margin, broker choice);
    - Ch. 11 "The Nature of Losing" (performance cycle, overtrading, drawdowns, washing out).
  - The rules those chapters do contain (expectancy formula, yo-yo daily limits, drawdown shutdown levels) are captured in sections 3–4.
  - Chart images are not readable; figure captions were read and used.

## 1. The method in brief

Farley's "survivalist" swing-trading method is built for markets where program algorithms deliberately trap the crowd.

- **Trade behind or against the crowd.** Prefer anticipation entries at support/resistance, and the "failure of a failure" re-entry after a rinse job, over reactive breakout chasing [p. 156, 186–187].
- **Plan every trade with swing analysis:**
  - profit target = the next barrier between entry and the prior swing high/low;
  - failure target = the price that breaks the setup;
  - require roughly ≥ 3:1 reward:risk [p. 140, 169, 208].
- **Recurring instruments:**
  - 5-3-3 Stochastics (all time frames), plus a long-cycle smoothed RSI(14,7) or 17-17-1 Stochastics [p. 99, 101];
  - 50- and 200-period EMAs (daily, 60-min, 15-min) [p. 49, 154];
  - Bollinger Bands (20,2) [p. 75];
  - Fibonacci 38/50/62/78.6% [p. 139, 160];
  - the first-hour range and the opening price [p. 168, 245].
- **Overlay layer:**
  - a calendar layer: expiration week, window dressing, Fed days, earnings, turnaround Tuesday [p. 79–91, 112–113, 240];
  - a "collar" that sets aggression (size, holding period, exposure from ⅓ to 90% of equity) by market regime [p. 306–313].
- **Evidence:** chart examples only (2006–2009 US equities, ETFs and index futures). There are no backtests or statistics.

## 2. Strategies

| # | Strategy | Timeframe | Entry rule (as stated) | Stop / exit (as stated) | Page |
|---|---|---|---|---|---|
| 2.1 | First-hour range breakout/breakdown | Intraday (5-min chart; 15-min for targets) | Liquid stocks (> 5M shares/day) or index/sector ETFs. Mark the high/low of the first 30 min, then adjust to 60 min; the range must be built by swings both ways (skip if already trending at the end of the first hour). Buy above the range high (sell below the low) plus a few cents; full size at once | Stop 15–20% of the range height back inside the range from the breakout level. Target = last major swing in that direction on the last two days of 15-min bars; if none, tight trailing stop and exit at the close. Take only if target ≥ 3× risk | 168–170 |
| 2.2 | Gap-day first-hour variant (reverse break / gap fill) | Intraday | After a gap, draw the gap-fill line (prior close), the range edge nearest the gap fill (reverse break line) and the far edge (breakout trigger). Enter in the gap direction above the trigger. Failure-of-a-failure: price breaks the reverse break line, touches the gap-fill line, then crosses back over the reverse break line → enter in the gap direction | Stop just below the reverse break line (failure-of-a-failure entry). A move from the reverse break line through the gap-fill line = failure signal | 279–282 |
| 2.3 | Bilateral rectangle / range entry | Daily or intraday | Narrow, well-defined S/R with favourable reward:risk on both sides: stop orders just outside the range (buy above resistance, short below support) | Stop 15–20% of the pattern width behind the breakout/breakdown level (example: 2-point rectangle → 30–40¢) | 169–172 |
| 2.4 | 50-day EMA "magnet" pullback | Daily, 60-min for timing | After a new breakout, set an alert 1–2 points above the 50-day EMA and wait (days or weeks). Buy as the selloff runs into the EMA, or when the 60-min chart prints an upside reversal there. Short mirror: after a breakdown, short inside narrow-range bars that stall across the 50-day EMA from below | Short variant: exit on any buying spike above the EMA. Long: not given explicitly (implied just under the EMA / reversal low) | 154–157 |
| 2.5 | Continuation-gap retracement | Daily | Identify a gap where price doubled the pre-gap extension, or (after three waves) the gap near the 50% point of the move. Place a limit order inside the gap; the retracement should reverse before the gap fills. Defensive version: wait for price to enter the gap and move forcefully away. Filter: no entry if price *gaps down* into the target | Bounce expected to reach ≥ 38% retracement of the countertrend wave. Stop not quantified | 40–41, 222, 268–270 |
| 2.6 | Fibonacci whipsaw (failure of a failure) | Intraday or daily | In a larger trend: stand aside as the counter-move pierces a deep retracement (62%) and tags 78%. Enter when price crosses back through the 62% level; add on pullbacks (e.g., at 50%) | Stop just beyond the 62% retracement; target = inception of the prior counter-swing | 162–163 |
| 2.7 | Defensive short sale (2B, pullback, narrow range, momentum) | Daily, 60-min | 2B: new high fails back under the last swing high within 1–3 bars; short when price trades through the low of the first recovery bounce. Pullback: short a weak rally that spikes into or above resistance and rolls over. NR: short within a 2–3-day range at support in a downtrend. Filters: do not short when the smoothed RSI(14,7) is in its bottom 20% and turning up, or when a bar closes 75–100% outside the lower Bollinger Band; avoid expiration week and month-end | NR: buy-stop just above the short-term high; momentum: percentage stop | 148–152 |
| 2.8 | Expiration-week magnetic strike | Daily/intraday, expiration week | Wed–Fri: buy a strong stock that has sold off into a round-number strike (short one that rallied into a strike). Or early in the week, buy liquid stocks trading just under a magnetic level (best: stocks recovering with higher lows, trading at 28–29, 38–39, 48–49) for a run to the round number; avoid strikes at new highs/lows | Dynamic trailing stop once price is within 20–30¢ of the strike; take profits aggressively | 84 |
| 2.9 | Tiered Fibonacci pullback buy ("dip" averaging) | Daily | After a strong rally wave: buy ¼ at the 38% retracement, ¼ at 50%, ½ at 62%. Only if (target − average entry) ≥ 3 × (average entry − stop). After a parabolic move with no Fib levels: half-size orders at ledges, one re-try | Stop around the 70% retracement after the third fill (out if the 78% level is reached); target = swing inception (prior high) | 206–208 |
| 2.10 | Post-earnings / post-news re-entry | Daily + 60-min | Exit before the report. After a solid report, 2–3 days of selling should hold intermediate support: buy a 60-min basing pattern there for a spike through the pre-release high. Short side: let the bounce run, then short at resistance such as the gap-down day's open. After any news gap: assume the reversal reaches the 60-min 50-period EMA; enter with tiered limit orders | Long: exit if a double top forms at the news-day high. Otherwise not quantified | 88–90, 260 |

**Supporting signal tools** (used inside the strategies above; each codable)

- **Relative-strength scan:** keep only stocks in the top 25% (bottom 25%) by % of 52-week high (low), then rank by (Close − EMA200)/EMA200 × 100 [p. 100–101].
- **5-3-3 Stochastics signal:** a lower high (higher low) near the 80/20 line, followed by expansion the other way, is an act-now signal. Do not exit merely because the indicator is overbought/oversold [p. 98–99].
- **Long-cycle filter:** RSI(14) smoothed 7 (or Stochastics 17-17-1); avoid longs when it is pressed above the upper line and turning over [p. 101–103].
- **Power-spike volume:** volume ≥ 3× the 60-day average, with a wide-range bar thrusting away from S/R [p. 158].
- **Trend-day detector:**
  - up/down volume ≥ 80:20 with breadth beyond ±1,800–2,000 [p. 203];
  - or TICK repeatedly beyond ±1,000, A/D beyond ±1,500 on both exchanges, up/down volume > 4:1, or index futures ±2%. On such days skip reversal trades [p. 248].
- **Ten reversal clues** [p. 106–107]:
  - 3 bars in one direction (Taylor);
  - a bar piercing a Bollinger Band by > 75% of its length;
  - Tuesday;
  - a 2B at a new high/low;
  - a volatility stall;
  - a volume blow-off;
  - a reversal on the lower time frame;
  - candlestick reversals;
  - three waves;
  - a hole-in-the-wall gap.

**Parameters**

- **Indicators:**
  - Stochastics 5-3-3 (position traders 14-7-7) [p. 99–100];
  - RSI 14 smoothed 7, or 17-17-1 Stochastics [p. 101];
  - Bollinger 20-period, 2 SD [p. 75]; weekly 20-week, 2 SD for remote trading [p. 217].
- **Moving averages:** EMA 50/200 on daily, 60-min and 15-min charts [p. 49, 156–157].
- **Liquidity:** first-hour strategy > 5M shares/day [p. 168]; general minimum 200k shares/day (60-day average), small-cap sweet spot 200k–500k [p. 196–197].
- **Size:** single-digit stocks get ½–¾ of normal size [p. 197].
- **Trend-day thresholds:** listed above [p. 203, 248].

**Key quotes**

- "Buy when price rallies above the high of the first hour range, or sell short when it falls under the range low." [p. 168]
- "Calculate the height of the first hour range, placing a stop loss 15% to 20% under the high for a breakout, or above the low for a breakdown." [p. 168]
- "look for trades in which the realized profit will be at least three times the risk of price rolling over and triggering the stop." [p. 169]
- "You’ll find that many stocks are already trending at the end of the first hour and not swinging back and forth. These issues should not be traded using this strategy." [p. 169]
- "The line nearest the gap fill becomes the “reverse break line.”" [p. 279]
- "Calculate 15% to 20% of the pattern width and place the stop loss that far behind the breakout or breakdown level." [p. 172]
- "Find the 50-day EMA on a new breakout and place an alert a point or two above it." [p. 154]
- "The trick is to watch this play in progress and to sell short within the narrow range bars at moving average resistance." [p. 156]
- "Specifically, a retracement approaching or entering the gap should reverse sharply, before it gets filled." [p. 40]
- "Wait until you can count three distinct trend waves, up or down." [p. 268]
- "In a nutshell, a selloff into a continuation gap can be bought except when price gaps down to reach the entry target." [p. 222]
- "Use this crossing as your initial entry signal," [p. 162]
- "The 2B reversal sets up when a financial instrument at a new high fails a breakout by dropping under the last swing high." [p. 148]
- "The actual sell signal triggers when price trades through the low of the first recovery bounce." [p. 148]
- "Stand aside when the indicator reaches the bottom 20% of its range and then turns higher." [p. 151]
- "Buy between Wednesday and Friday afternoon after a strong stock sells off into a strike, or sell short after it rallies into a strike." [p. 84]
- "Put up a Fibonacci grid, buying 300 shares at the 38% retracement, 300 shares at the 50% retracement, and 600 shares at the 62% retracement." [p. 206]
- "The distance from this number up to the next resistance level (profit target/reward) should be at least three times the distance down to your stop loss" [p. 208]
- "play the stock into the minutes ahead of an earnings report, but get out before the numbers are actually released." [p. 88]
- "Look for a 60-minute basing pattern at this level, and enter the trade in anticipation of a buying spike up and through the prerelease high." [p. 90]
- "Assume the reversal will eventually reach the 50-period EMA before there’s a major counterswing." [p. 260]
- "Run the 52-week high or low scan first, creating a list that contains just stocks in the top 25% for a strength list or bottom 25% for a weakness list." [p. 101]
- "The best signals unfold when Stochastics makes a lower high (or higher low) near the 80-20 line and then expands in the opposite direction." [p. 99]
- "Avoid long positions when the long-cycle indicator is pressed above the upper line and turning over" [p. 103]
- "Look for a minimum of three times the 60-day moving average of volume to print for that event." [p. 158]
- "Look for a lopsided tape in which 80% or more of total volume comes in on the buy side during a rally and sell side during a selloff." [p. 203]
- "Look for daily trends to reverse after three bars in either direction." [p. 106]
- "I recommend simple 15-minute charts, with 50- and 200-bar EMAs and a 5-3-3 Stochastics." [p. 49]

**Pseudocode** (most codable: 2.1, 2.3, 2.4, 2.6, 2.9)

```
# 2.1 First-hour range breakout (5-min bars, regular session)
universe: ADV60 > 5_000_000 shares or index/sector ETFs
FH_hi, FH_lo = high/low of bars 09:30–10:30
require: range built by >=1 swing each way (ASSUMPTION: at least one 5-min swing high and one swing low inside the hour)
skip if trending: ASSUMPTION close(10:30) in top/bottom 10% of FH range with monotonic 15-min bars
buffer = 0.02 (ASSUMPTION "a few cents"; use 0.1*ATR(5min) for non-US)
long  when price > FH_hi + buffer ; stop = FH_hi - 0.175*(FH_hi-FH_lo)
short when price < FH_lo - buffer ; stop = FH_lo + 0.175*(FH_hi-FH_lo)
target = last major 15-min swing high (low) over prior 2 sessions; require (target-entry) >= 3*(entry-stop)
if no swing: trailing stop (ASSUMPTION 0.5*FH range) ; exit at close
one trade per instrument per day (ASSUMPTION)

# 2.3 Bilateral range (daily)
range = rectangle of >= N bars (ASSUMPTION N=8) with width <= 1.5*ATR20*sqrt(N)
OCO: buy-stop at R + buffer ; sell-stop at S - buffer
stop = breakout level -/+ 0.175*(R-S)

# 2.4 50-EMA magnet (daily)
setup: close breaks above prior N-day high (ASSUMPTION N=50); thereafter alert when low <= EMA50 + 1.5 pts (ASSUMPTION scale 0.5*ATR20)
entry A: limit at EMA50 ; entry B: 60-min bullish reversal (close > prior 60-min high after touching EMA50)
stop: ASSUMPTION close < EMA50 - 0.5*ATR20 ; target: breakout high, then trail

# 2.6 Fibonacci whipsaw (short example)
in downtrend: swing H0 (high) -> L0 (low); counter-rally pierces L0+0.62*(H0-L0) and tags 0.786
short when price closes back below the 62% level; add at 50% level ; stop just above 62% (ASSUMPTION +0.25*ATR)
target = L0

# 2.9 Tiered Fib pullback buy
after rally L->H: limits 25% @ H-0.382*(H-L), 25% @ H-0.5*(H-L), 50% @ H-0.618*(H-L)
avg = weighted fill price ; stop = H-0.70*(H-L) after third fill (ASSUMPTION: use same stop for partial fills)
take trade only if (H - avg_planned) >= 3*(avg_planned - stop) ; target = H
```

**Ambiguities & assumptions**

- **"Add a few cents"** to the first-hour edges [p. 168] is not quantified. Assumed 2¢ (US), or a fraction of ATR elsewhere.
- **First-hour stop direction.** The stop is stated as 15–20% of range height "under the high" for a breakout [p. 168], i.e. back *inside* the range, not below the range low. The worked example (range 22–24 → stop 23.60–23.70) confirms this. Do not place it below the range low.
- **The "range built by swings" test** [p. 169] is discretionary. The skip-if-trending filter above is an ASSUMPTION.
- **Continuation-gap identification.** Two inconsistent rules: (a) price "doubles the extension prior to the gap" [p. 41]; (b) the gap lies near 50% of a completed three-wave move [p. 268]. Rule (b) needs hindsight, because the waves must be complete. Use (a) for live signals.
- **The long stop for the 50-EMA magnet trade is never given.** The book also warns that common stop spots (moving averages, round numbers) get "rinsed" [p. 230, 234]. Test ATR-based stops below the EMA.
- **The tiered-buy stop "around the 70% level"** [p. 206] applies after all three fills. Handling of partial fills is unspecified.
- **Expiration "magnetic strikes"** need open-interest data. The book also uses round and half-round numbers as a proxy [p. 83–85].
- **Collar regime inputs** are qualitative (VIX levels 25/35 are given as regime breaks [p. 307]). Mapping to ⅓ / 90% exposure is the only numeric rule [p. 312].

## 3. Risk & money-management rules

- **Reward:risk.** Require ≥ 3:1 from entry to target vs. stop (first-hour trades [p. 169]; averaging entries [p. 208]). The Senior Housing example computes 9:1 [p. 303].
- **Stop placement:**
  - put the initial stop where the pattern breaks, then adjust for rinse jobs;
  - or use a lower-time-frame stop with planned re-entries until total loss hits tolerance [p. 229–231].
  - Avoid stops at obvious levels (trendlines, round numbers, moving averages) [p. 230].
- **Momentum entries:** exit on a violation of the 15-min 8-bar SMA (60-min 8-bar for larger breakouts). Avoid fixed % stops unless no structure exists [p. 235, 317].
- **Trailing stops:**
  - after the first expansion, trail behind 60-min (or 15-min) congestion zones;
  - at about 75% of the way to target, trail aggressively;
  - place a second order at the target itself [p. 233];
  - or a fixed 10–20¢ trail near the target [p. 319].
- **Rinse-job entry stop:** one tick beyond the rinse extreme [p. 235].
- **Time stops.** Apply time-based stops to holding periods, and exit non-performing trades near the maximum intended time in market [p. 74, 316].
- **Collar / exposure** [p. 312–315]:
  - defensive regime: total exposure ≤ ⅓ of the account, at most two scale-ins;
  - supportive regime: up to 90% of equity, longer holds;
  - margin only with a multi-year profitable record.
- **Sizing:**
  - cut size for volatile and small-cap stocks; trade larger in slow movers [p. 205];
  - single-digit stocks get ½–¾ size [p. 197];
  - ignore margin when computing size [p. 205, 208].
- **Daily limits (yo-yo cure)** [p. 130]:
  - a fixed number of trades per day;
  - a daily gain threshold ≥ 2× the daily loss threshold, and stop trading for the day when either is hit.
- **Event and calendar rules:**
  - no positions held through earnings [p. 88, 236];
  - stand aside into Fed announcements [p. 82];
  - never trade economic releases directly [p. 262];
  - expect 3–4 event shocks a year [p. 275].
- **Drawdown:** set a fail-safe drawdown level and stop trading when it is reached [p. 296]. Example daily shutdown: $250 [p. 298].
- **Expectancy:** (PW × AW) − (PL × AL) must be positive [p. 121].

## 4. Non-codable guidance

- Tape reading and "tells":
  - stealth creep into resistance;
  - bid stretching 20–40¢ below the last print at a capitulation low;
  - the opening price principle;
  - % in range [p. 245–252].
- Diabolical/contrary thinking: trade behind, ahead of or against the crowd, never with it [p. 156]. Identifying who is trapped [p. 28–31, 189].
- Sector rotation reading (five common rotations) and "morning mavericks" [p. 137–138, 201–203].
- The trading plan's four blocks (prediction, timing, volatility, risk), personal-style fit, journaling, and the psychology of yo-yos, overtrading and drawdowns [p. 122–135, 286–300].
- Account structure: a PDT cushion of $50k, separate accounts by holding period [p. 185, 213].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - daily OHLCV and 5/15/60-minute bars for NIFTY 50 / F&O stocks and NIFTY/BANKNIFTY futures and index ETFs;
  - India VIX;
  - NSE F&O open interest by strike (for 2.8);
  - corporate results calendar (for 2.10).
- **Testability with our data:**
  - 2.1, 2.2, 2.3, 2.4, 2.6 and 2.9 and the RS / power-spike / Stochastics tools are mechanical after the assumptions above;
  - 2.5 is partly mechanical (rule a);
  - 2.7 needs short-selling: use stock futures, since NSE cash shorts are intraday only;
  - 2.8 needs NSE options OI. NSE monthly/weekly expiry is Thursday/Tuesday depending on the index and period (ASSUMPTION: check the current expiry calendar), so the book's "Wed–Fri" window must be remapped to the 2–3 sessions before expiry.
- **Market-structure differences:**
  - **Session:** 09:15–15:30 IST, so the first hour is 09:15–10:15. The pre-open call auction (09:00–09:08) replaces the US premarket; US 8:00 a.m. quote-painting and Globex-based rules do not transfer directly (use GIFT Nifty as the overnight proxy, ASSUMPTION).
  - **Liquidity filters:** the 5M-shares and 200k-share filters should be converted to turnover (e.g., ₹ crore per day). Cent-based buffers and stops (2¢, 20–30¢, 10–20¢ trails) should be converted to tick or ATR multiples (NSE tick ₹0.05 for most stocks; ASSUMPTION ₹0.01 for some segments).
  - **Breadth:** NYSE TICK and US breadth thresholds have no direct analogue. Use NSE advance/decline counts scaled to the universe size (ASSUMPTION).
  - **Circuit limits** on many stocks can block exits on gap days (relevant to 2.2 and the gap-down triage on p. 68–69).
  - **Results season** clusters differently (quarterly results, often after market hours or mid-session). Treat mid-session results as gap-equivalent events.

## 6. Verdict

- **Codeability:** Partial to good. The book is mostly discretionary prose, but several setups carry explicit numeric rules:
  - the first-hour breakout (range, 15–20% stop, 3:1 filter);
  - the bilateral range;
  - the tiered Fibonacci buy (38/50/62, 70% stop, 3:1);
  - the 50-EMA magnet;
  - the Fibonacci whipsaw;
  - the RS/power-spike scans.

  Regime "collars", tape-reading tells and calendar biases are mostly qualitative.
- **Priority for backtesting:** Medium-high for 2.1 (first-hour range, intraday NIFTY futures and liquid F&O stocks), 2.4 and 2.9 (daily pullback entries), and the RS scan plus 5-3-3 Stochastics timing. Medium for 2.6 and 2.7. Low for 2.8 (needs OI data) and 2.10 (needs event data).
- **Top 3 things a coder is most likely to get wrong**
  1. Placing the first-hour (and bilateral) stop at the opposite end of the range. The book puts it only 15–20% of the range height back inside the range from the breakout edge, and skips trades without ≥ 3:1 room to the last 15-min swing [p. 168–169, 172].
  2. Treating continuation-gap and 50-EMA pullbacks as automatic buys. The continuation-gap trade is void when price *gaps* into the level [p. 222], and the 50-EMA trade is meant to be taken after a fresh breakout has pulled all the way back, ideally confirmed by a 60-min reversal [p. 154].
  3. Using the Stochastics overbought/oversold crossing as the signal. Farley's signal is the lower-high/higher-low *pattern* near 80/20 followed by expansion, and he explicitly warns against exiting merely at an extreme [p. 98–99].
