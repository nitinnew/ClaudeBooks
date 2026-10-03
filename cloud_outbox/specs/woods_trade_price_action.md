# How to Trade with Price Action (Master Edition) — Galen Woods (self-published, 2014)

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/How to Trade with Price Action - Master. Galen Woods.pdf` (file id `1PIk_tYiZCYNTuKRQgD7ffiNsSiTdhalo`, 3,789,221 bytes), 82 PDF pages with a text layer (page 1 is a blank cover image).
- **Text file used:** text/woods_trade_price_action.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers or table of contents; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/woods_trade_price_action.md text/woods_trade_price_action.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 82]], all 11 chapters. Chapter 2 (10 chart types) and Chapter 6 (order types) contain no trading rules beyond the entry-order convention used below; they were read and are summarised only in section 4. Chart images were not readable; the spec uses the text descriptions.

## 1. The method in brief

This is the "Master" volume of a 3-book compilation of Trading Setups Review articles, focused on intraday futures (ES, NQ, 6E, 6J) on 5–30-minute bars. It is not a single system. It contains:

- one small backtest on inside bars;
- a 20-period moving-average trend-and-pullback framework;
- a "re-entry" variant applicable to any pattern;
- several filters: avoid tight congestion, trade narrow-range bars only out of congestion, and don't fight a trend day.

Entries are generally buy-stops or sell-stops one tick beyond the signal bar, with a "pattern stop" just beyond the opposite end of the pattern [p. 55, 73].

The only statistics given come from the inside-bar study [p. 11–14]:

| Measure | Value |
|---|---|
| Market and bars | ES, 5-minute bars, Nov 2008–Nov 2013 |
| Trend filter | slope of the 20-period EMA |
| Reward:risk | 1:1 |
| Win rate, all inside bars | 37.33% (n = 4,107) |
| Win rate, filtered inside bars | 50% (wide-range bars closing in the trade direction) |
| Improvement on YM, NQ, TF, CL | about 8 points |

## 2. Strategies

### 2.1 Filtered inside-bar breakout (wide-range, trade-direction close)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | bar-pattern breakout, with-trend | 10–15 |
| Timeframe & holding period | 5-minute bars, regular session; holding until the 1R target or the stop | 11 |
| Universe | Index and commodity futures (ES, YM, NQ, TF, CL, ZN) | 11, 14 |
| Trend filter | Slope of the 20-period EMA (long if rising, short if falling) | 11 |
| Setup | An inside bar (high ≤ prior high, low ≥ prior low) whose range is > 75% of the prior bar's range ("wide range"), closing in the trade direction (close > open for longs) | 12–14 |
| Rejected filters | Relative volume (high or low), and body/range (directional vs doji), gave no material edge | 11–14 |
| Entry trigger & order type | Stop order one tick beyond the inside bar in the trend direction | 55 |
| Initial stop-loss | Pattern stop beyond the other end of the inside bar (ASSUMPTION: the book does not state the backtest stop explicitly; "pattern stop" is defined on p. 73) | 73 |
| Target | 1:1 reward:risk | 11 |
| Results | Unfiltered 37.33% wins (n = 4,107). Wide-range 52.69% (n = 167); narrow (< 25%) 50% (n = 32); direction-supporting 40.97% (n = 1,782); filtered combination ES 50%, YM 47.58%, NQ 48.04%, TF 49.89%, CL 51.17%, ZN 39.13% | 11–14 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend MA | 20-period EMA slope | — | 11 |
| Wide-range inside bar | range > 75% of the prior bar's range | narrow < 25% | 12 |
| Close direction | close in the trade direction | — | 13 |
| Reward:risk | 1:1 | — | 11 |

**Key quotes**

- "Within our back-testing period, the winning percentage of inside bars is 37.33% in a sample size of 4107." [p. 11]
- "A wide range bar takes up more than 75% of range of the preceding bar." [p. 12]
- "Choosing inside bars that support our trades is a better trading strategy." [p. 13]
- "Most of the futures contacts show an improvement of over 8%." [p. 14]
- "Our results are not meant to be used in isolation as a complete trading system." [p. 14]

**Pseudocode**

```
bar t is inside: H_t <= H_{t-1} and L_t >= L_{t-1}
wide: (H_t - L_t) > 0.75*(H_{t-1} - L_{t-1})
trend_up: EMA20_t > EMA20_{t-1}
long if inside and wide and trend_up and C_t > O_t:
    buy-stop at H_t + tick (valid for bar t+1 only — ASSUMPTION)
    stop = L_t - tick ; target = entry + (entry - stop)       # 1:1
short mirror image ; flat at session end (ASSUMPTION for an intraday test)
```

**Ambiguities & assumptions**

- The stop, order validity, and EMA slope look-back of the backtest are not stated. ASSUMPTION: stop at the opposite extreme of the inside bar, the order valid for one bar, slope measured over one bar.
- The 1:1 target means win rate ≈ edge. The author warns the assumptions are "naive and simplistic" [p. 14].
- The small samples (167 wide-range trades on ES) make the +15-point edge fragile.

### 2.2 20-period moving-average trend confirmation and pullback

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend pullback (intraday) | 39–42, 48–52 |
| Timeframe | 5-minute bars (NQ examples) | 41, 49 |
| Trend confirmation (bull) | (1) Price touches the 20-SMA; (2) a bar stays fully above it; (3) price pulls back toward it without any bar high below it; (4) the bull trend is confirmed when price exceeds the last extreme high. Bear: the mirror image | 39–40 |
| Alternative trend definitions | Price channel of MA(highs) and MA(lows): two bars fully above it = bull, two fully below = bear. Hourly-bar higher high/lower low. Trend-line breaks | 42, 44–46 |
| Context questions | Above or below the MA? How did price get there? How many bars overlap the MA? The MA's slope, and how often it changes | 48–50 |
| Entry | In a bull trend, buy when price retraces to the 20-period MA, timed with a bar pattern (e.g., a two-bar reversal at the MA). Bear: sell rallies to the MA | 50–51 |
| Target | Weak trend (shallow slope, slope flipping) → nearer targets | 50 |
| Trailing stop | The moving average itself | 51 |
| MA type | EMA or SMA; any intermediate period; keep it consistent | 48 |

**Key quotes**

- "Essentially, we are looking for a shallow pullback followed by a new high (low) to confirm a bull (bear) trend." [p. 39]
- "When two price bars stay completely above the channel, we define a bull trend." [p. 42]
- "In a bull trend, buy when prices retrace to the 20-period moving average." [p. 50]
- "Hence, a trailing stop based on a moving average locks in profit and at the same time gives enough room for whipsaw action." [p. 51]

**Pseudocode**

```
state machine per session (bull side):
  touched = any bar with L <= MA20 <= H
  above   = after touch, a bar with L > MA20
  pull    = later bars move toward MA20 with all H > MA20 (no bar high below MA)
  bull    = C > max(H since 'above') after pull
in bull: setup when L_t <= MA20_t*1.001 (ASSUMPTION "retrace to MA") and a two-bar reversal
         (C_t > O_t and C_t > H_{t-1}, ASSUMPTION)
         buy-stop H_t + tick ; stop L_t - tick ; trail stop = MA20 - tick ; exit at session end
target if MA slope over 10 bars < threshold (weak trend): last swing high (ASSUMPTION)
```

**Ambiguities & assumptions**

- "Retrace to the MA", "steep slope" and the trailing-stop offset are discretionary. The thresholds above are assumptions.

### 2.3 Re-entry after the original pattern is stopped out (trapped traders)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | failed-stop re-entry, with-trend | 59–70 |
| Concept | Skip the original setup; enter when its traders have been stopped out and price turns back in the original direction (the re-entry is the "trapped out" traders chasing) | 59–60, 66 |
| Long setup | (1) Bullish pin bar; (2) the next bar trades above the pin's high (original trigger); (3) price falls below the pin's low "but not too far below" (original stop hit); (4) buy when price breaks above any bullish bar | 66–67 |
| Short setup | Mirror image (the book's step 4 says "buy" for shorts; read as sell) | 67 |
| Filters | Market bias first: the winning example re-entered above the 20-EMA, the losing one below it. Avoid it when the original move already hit its projected target (fewer trapped traders) | 69–70 |
| Timing | Good re-entries occur soon after the original setup | 70 |
| Related trapped-trader setups | Hikkake (inside-bar breakout failure); two-legged pullback; pin bar beyond a major swing high or low | 60–63 |

**Key quotes**

- "Thus, in the re-entry trading strategy, we aim to skip the first entry and enter the market only upon the “re-entry” opportunity." [p. 66]
- "The market must fall below the low of the Pin Bar (but not too far below)" [p. 67]
- "Generally, good re-entries occur soon after the original setup." [p. 70]
- "The best pin bars are those that went beyond major swing highs and swing lows." [p. 63]

**Pseudocode**

```
pin bar (bullish) at t0: lower tail >= 2/3 of range, close in upper third (ASSUMPTION; book defines pins in another edition)
trigger: some bar t1 in (t0, t0+3] with H_t1 > H_t0
stopout: some bar t2 in (t1, t1+5] with L_t2 < L_t0 and L_t2 >= L_t0 - 1.0*range(t0)   # "not too far", ASSUMPTION
re-entry: first bar t3 in (t2, t2+5] with C_t3 > O_t3 and C_t3 > EMA20 ; buy-stop H_t3 + tick
stop: min(L from t2..t3) - tick ; target: 2R or prior swing high (ASSUMPTION; none given)
skip if price reached a measured target of the pattern that produced the pin (cannot code without a pattern detector)
```

**Ambiguities & assumptions**

- The book says "it is not mechanical" [p. 70]. "Not too far below", the time windows and the targets are all assumptions.

### 2.4 Narrow-range (NR7 / NR4-ID) pullback trigger with congestion and trend-day filters

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | volatility-contraction trigger inside a trend | 76–80 |
| Setup | A pullback in a trend ending in an NR7 (or NR4 inside) bar, outside any tight congestion | 77–78 |
| Congestion filter | Congestion = the market fails to close higher (lower) for ≥ 3 consecutive bars; stop trading once in congestion. Midday is usually the congestion phase. Do not trade narrow-range bars inside a tight range | 76–77 |
| Trend-day filter | A trend day opens near one extreme and closes near the other. Don't trade against it; note strength through the last swing high and weak counter-thrusts | 78–80 |
| Target | Conservative target at the last extreme | 78 |
| Overtrading | Overtraders should take one good trade a day | 74 |

**Key quotes**

- "Congestion patterns occur when the market fails to close higher (lower) for at least three consecutive price bars." [p. 77]
- "Do not trade narrow range bars within a tight congestion." [p. 77]
- "A trend day is one that opens near one extreme of the trading session and ends near the other extreme." [p. 78]
- "Day traders who overtrade should try taking one good trade a day." [p. 74]

**Pseudocode**

```
nr7_t: (H_t-L_t) = min(range over t-6..t)
congestion_t: no close > prior close for the last 3 bars AND no close < prior close for the last 3 bars?
              # book: "fails to close higher (lower) for at least three consecutive bars" — ASSUMPTION: neither a higher close nor a lower close beyond the 3-bar range
trend_up (2.2) and pullback (>= 2 lower highs) and nr7_t and not congestion:
     buy-stop H_t + tick ; stop L_t - tick ; target = last swing high ; one trade per session
```

## 3. Risk & money-management rules

- Use a pattern stop just below a bullish pattern or just above a bearish one [p. 73].
- Prefer setups whose reward:risk is healthy relative to the nearest opposing swing, and trade where the next resistance (support) is far away [p. 72, 78].
- Let profits run on large swings; don't exit with small profits each time [p. 72].
- Don't overtrade: at most one good trade a day for those prone to it [p. 74].
- No position-sizing rule is given.

## 4. Non-codable guidance

- **Chart types (Ch. 2):** volume, tick, range, Renko, Kagi, P&F and three-line-break charts change which patterns exist. For example, range bars eliminate inside bars and NR patterns. Use a new chart type only as a complement to time charts [p. 16–38].
- **Order types (Ch. 6):** use stop orders for breakouts and limit orders to fade breakouts of a tight range (an advanced technique) [p. 54–58].
- **Livermore tips:** start with the broad index trend; aim for big swings; separate trend errors from timing errors; avoid reversal trades [p. 71–74].
- Simulate before trading live [p. 81].

## 5. Adapting to NSE (Indian equities)

- **Data required:** 5-minute OHLCV for NIFTY and BANKNIFTY futures, or liquid F&O stocks; session times 09:15–15:30 IST. Daily bars are enough for a daily-timeframe variant of 2.1.
- **Testability with our data:** 2.1 is fully mechanical and the cheapest to test (on both intraday index futures and daily stocks). 2.2–2.4 need the assumptions noted above.
- **Market-structure differences:**
  - The opening 09:15–09:30 period is the most volatile and midday (12:00–13:30) the most congested. Apply the congestion filter by time-of-day as well.
  - Intraday cash positions are squared off automatically by brokers around 15:15–15:20, so force an exit before then.
  - Costs (STT, exchange charges, slippage) matter at a 1:1 reward:risk. Include ≥ 0.03% per side for futures in the test (ASSUMPTION).

## 6. Verdict

- **Codeability:** Yes for 2.1 (fully specified apart from the stop). Partial for 2.2–2.4 (discretionary thresholds).
- **Priority for backtesting:** Medium-Low. 2.1 is a quick, reproducible test that has published US-futures statistics to compare against. The rest are generic intraday tools. The author stresses this is not a complete system [p. 14, 70].
- **Top 3 things a coder is most likely to get wrong**
  1. Filtering inside bars to *narrow* range (the NR4/ID habit). The edge in the study came from **wide** inside bars (> 75% of the prior bar's range) that close in the trade direction [p. 12–14].
  2. Treating the re-entry rule as "take the pin bar". The original trigger must fire **and** be stopped out (but not by too much) before re-entering, with the bias filter [p. 66–69].
  3. Trading narrow-range triggers inside midday congestion, or against a trend day. Both are explicit no-trade filters [p. 77–80].
