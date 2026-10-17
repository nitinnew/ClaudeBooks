# Pattern cheat-sheets (bundle) — various authors

- **Source file:** Google Drive bundle "Pattern cheat-sheets" (11 files; 7 processed and concatenated, in this order):
  - "Big Book of Chart Pattern.pdf" = pp. 1-105. No author is named in the text; it states that its statistics are taken from Thomas Bulkowski's Encyclopedia of Chart Patterns [p. 5]. Each page carries a distribution watermark (t.me/tradersinnlibrary). Text layer; the even-numbered pages 6-104 and page 1 are chart images with no text.
  - "Chart Pattern Guide.pdf" = pp. 106-116. Image-only "Institutional Price Action Cheat Sheet" by Mansor Sapari aka CMS [p. 107], published under the "TECHNO charts" banner [p. 106]. Its candlestick sheet credits www.jbmarwood.com / @marwoodjoe [p. 109]. OCR'd by the coordinator (column-aware RapidOCR); mostly diagram labels, noisy, spaces dropped.
  - "Candlestick Patterns Ebook.pdf" = pp. 117-131. Metaverse Trading Academy (Rajkot, India), copyright 2023 [p. 118, p. 131].
  - "21_Candlesticks.pdf" = pp. 132-196. No author or publisher is stated in the text (examples are Thai stocks and the SET Index).
  - "DW candlesticks power.pdf" = pp. 197-247. "The Power of Candlesticks Applications", written by DAR Wong, APSRI (Acute Precision & Studies Research Inc.), March 2006 (third edition Nov 2007) [p. 197, p. 198].
  - "Mastering Candlestick Charts 1 and 2.pdf" = pp. 248-355. Pristine Capital Holdings, Inc. ("The Pristine Method"), copyright 1994-2007 [p. 249, p. 300]. Part 1 = pp. 248-298; Part 2 = pp. 299-355.
  - "How to read basic chart patterns.pdf" = pp. 356-361. Moneycontrol "Technical Classroom" article by Shabbir Kayyumi, printed 4/15/23 [p. 356]. Image-only; OCR'd by the coordinator; chart axis numbers appear as noise.
  - NOT PROCESSED (over the ~7 MB connector download limit, recorded as blocked_size): "All Chart Patterns.pdf" (11.2 MB; an identical-size duplicate "All Chart Patterns-1.pdf" exists), "Candlestick Chart Patterns DTT.pdf" (10.8 MB), "Candlestick-Pattern-Chart-Pattern-qnpte3.pdf" (10.7 MB), "3-chart-patterns.pdf" (15.0 MB). Nothing in this spec comes from those four files.
- **Text file used:** text/misc_pattern_cheatsheets.txt  (page basis: pdf_pages, numbered continuously across the 7 processed files; 361 markers)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (continuous PDF page index, not any printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage. Printed numbers (e.g. Big Book "4." footers, DAR Wong "42" headers, Pristine slide numbers) are NOT used.
  - Verified with `python ../work/bin/verify_citations.py specs/misc_pattern_cheatsheets.md text/misc_pattern_cheatsheets.txt`.
- **Coverage:** Read text lines 1-6849 (the whole file) in 9 sequential reads; last marker reached `[[PAGE 361]]` (all 361 markers). OCR'd files: "Chart Pattern Guide.pdf" (pp. 106-116) and "How to read basic chart patterns.pdf" (pp. 356-361). Chart-only pages with no extractable text: p. 1 and the even pages 6-104 of the Big Book (the chart images that accompany each pattern page); pp. 107-116 contain only diagram labels, so the numeric content of the CMS sheet's entry/stop/target diagrams is not available; the Pristine slides (pp. 248-355) and DAR Wong (pp. 197-247) have chart figures whose content is in images only. Pp. 187-196 of "21_Candlesticks.pdf" repeat the On Neck / In Neck / Thrusting / Side-by-Side White Lines texts (pp. 187-190 and 191-194 are duplicates), and Pristine Part 2 (pp. 299-355) repeats much of Part 1. Four of the eleven bundle files were not processed (blocked_size, listed above). *Coordinator check: 7 of the 11 bundle files were downloaded and merged with continuous page numbers. 'Chart Pattern Guide.pdf' (column-aware) and 'How to read basic chart patterns.pdf' are image-only, so the coordinator OCR'd them with RapidOCR. The coordinator re-ran verify_citations (47/47 ok) and an exact-page strict check (0 off-by-one), and confirmed the six field tables have exactly the 12 template rows. Spot-checked by grep and page read: 'above average volume' triggers through the Big Book, 10-pip / 15-pip stops p.122/126, DAR Wong EMA 4/9 p.239-240, overbought swap p.240, shadow entry '20 - 30 pips' p.242, windows 'covered within 55 market trading days' p.235, Pristine pp.248-355; all matched.*

## 1. The method in brief

This is a bundle of reference sheets, not one method. The CMS sheet and most of the Moneycontrol article are definitional (labels and diagrams, with only a generic entry/stop/target/volume paragraph on pp. 359-360); the other files add rules: the Big Book gives every one of its 50 chart patterns a breakout trigger (a close beyond the pattern boundary on above-average volume) plus a measured-move target, and cites Bulkowski for its statistics [p. 5]; Metaverse Trading Academy gives next-candle-open entries with fixed-pip stops for six candlestick reversals [p. 122, p. 126]; DAR Wong adds an indicator filter (EMA 4/9/20 and slow stochastic), a "shadow entry" 20-30 pips from the daily open, and an exit from the 9-day average range [p. 239, p. 242]; Pristine insists that candle names do not matter and that a signal is confirmed only when a prior candle's low (or high) is violated [p. 318, p. 254]; "21_Candlesticks" adds validity conditions and a next-day confirmation requirement for several candles [p. 137, p. 138].

Evidence is thin. The only reported statistics are in the Big Book gap pages (area gaps fill within a week nearly 90% of the time [p. 41]; about two-thirds of exhaustion gaps close within a week and over 90% within two [p. 47]) and a single sentence in DAR Wong that "plain" candlestick analysis has an accuracy of around 60% [p. 239]. All other statistical notes are directional ("tend to perform better"). Most patterns are described for US/FX/futures markets; time frames are daily/weekly (Big Book, Moneycontrol) or FX pips (Metaverse, DAR Wong).

Because the inventory rule is "extract only if rules beyond pattern definitions appear", six strategy sections follow (2.1-2.6). Every pattern that is only defined (shape and bullish/bearish meaning, no trigger/stop/target/statistic) is listed in the compact table in section 4 instead.

## 2. Strategies

### 2.1 Chart-pattern breakout with measured-move target (Big Book, 50 patterns; Moneycontrol version)

Source files: "Big Book of Chart Pattern.pdf" (pp. 4-105) and, for the generic entry/stop/target/volume statement, "How to read basic chart patterns.pdf" (pp. 359-361). The CMS "Chart Pattern Guide.pdf" shows Entry / SL / TP markers on diagrams for the same patterns (p. 113, p. 116) but gives no numbers, so it contributes nothing codable.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout. Each pattern is tagged reversal, continuation or non-directional, with a setup, a trigger and a projected move. | 5, 7 |
| Timeframe & holding period | Any aggregation period (fractal). Duration limits given on daily charts: cup (and inverted cup) at least 7 weeks; flag, pennant (bull and bear) at most 3-4 weeks. Horn and pipe patterns are defined on weekly charts. Moneycontrol: patterns are most accurate on daily, weekly, monthly. Holding period: until the projected target; no time exit stated. | 5, 15, 35, 59, 69, 361 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Identify the previous trend first; reversal patterns need a prior opposite trend, continuation patterns need the same-direction trend. Flags and pennants perform better when they break out in the direction of the prevailing market trend. Bulkowski-based notes: breakouts near the 1-year low (bullish) or 1-year high (bearish) tend to outperform. | 5, 35, 65, 19, 21 |
| Setup conditions | Per-pattern shape (see Parameters). Common requirements: volume diminishes through the formation (most patterns); triangles and wedges should break out within two-thirds to three-quarters of the way to the apex; wedges need at least five touches between the trend lines; broadening pattern needs at least two highs and lows. | 7, 93, 103 |
| Entry trigger & order type | Close beyond the pattern boundary (neckline / trend line / channel / high or low of formation) on above-average volume. Order type not stated. Moneycontrol: enter long if the price moves through the resistance line, short if through the support line; the pattern provides the entry point. | 7, 49, 359, 360 |
| Initial stop-loss | Big Book: Not found in this text. Moneycontrol: "the pattern provides an entry point and stop loss" but the stop level is only shown on a chart as 'stop loss price (stop exit price)' with no rule. | 360 |
| Exits: profit-taking | Measured-move target per pattern (see Parameters). Moneycontrol: profit target from a measurement of the pattern's high and low. | 360 |
| Exits: trailing / time / signal | Not found in this text. Cautions only: for three falling peaks / three rising valleys the measured move is not achieved with regularity; diamonds tend to fall back once the target high is reached. | 89, 91, 19 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Breakout confirmation (all patterns) | close beyond boundary on above-average volume | "above average" volume is never quantified | 7, 49 |
| Volume during formation | diminishes into the breakout, expands on breakout | cup follows cup shape (high at left lip, low at bottom, rising to right lip); H&S high on first shoulder decline, balanced at head, expands on neckline break | 15, 49 |
| Cup / inverted cup minimum duration | 7 weeks (daily chart) | shorter handle and deeper cup (left lip slightly higher than right) perform better | 15, 17 |
| Cup / inverted cup target | cup depth (right lip to cup bottom) added to / subtracted from right lip | - | 15, 17 |
| Flag / pennant (bull, bear) max duration | 3-4 weeks (daily chart) | flags without gaps and wider-range flags perform better; bull flags beat bear flags | 35, 37, 65, 67 |
| Flag / pennant target | length of the steep prior move added to / subtracted from the breakout level | - | 35, 37, 65, 67 |
| High and tight flag | consolidation of several days to several weeks after a doubling in price; target = one-half of the prior move added to breakout level | tighter (less range) performs better; throwbacks hurt | 39 |
| Double bottom / top (Adam & Adam, Adam & Eve, Eve & Eve) | trigger: close beyond the horizontal line through the intervening high (low) | target: distance from that line to the two lows (highs) added to (subtracted from) breakout level | 23, 25, 27, 29, 31, 33 |
| Triple bottom / top | same trigger; target = distance between the intervening high (low) and the lows (highs) | declining volume with heavy volume on the left bottom (top) performs better | 99, 101 |
| Head & shoulders family (inverted, complex, inverted continuation, normal, complex) | trigger: close beyond the neckline on above-average volume | target: first high (low) to head low (high) distance added to (subtracted from) neckline at the breakout; gap on breakout day and sloping neckline help | 49, 51, 53, 55, 57 |
| Broadening bottom / top | trigger: close above upper (below lower) trend line | target: highest high to lowest low before breakout, added to the highest high (subtracted from the lowest low) | 7, 9 |
| Diamond bottom / top | trigger: close beyond the trend line across the sloping highs (lows) | target: widest range of the diamond added to / subtracted from breakout level | 19, 21 |
| Bump-and-run reversal bottom / top | trigger: close beyond the trend line drawn across the lead-in phase, on an arithmetic chart | target: the highest (lowest) point of the lead-in phase | 11, 13 |
| Rectangle bottom / top | trigger: close above or below the channel | target: channel height added or subtracted according to the breakout direction | 73, 75 |
| Triangles (ascending, descending, symmetrical) | trigger: close beyond the flat / converging boundary; breakout within two-thirds to three-quarters to the apex | target: pattern height added / subtracted at the breakout level | 93, 95, 97 |
| Wedges (falling, rising) | trigger: close beyond the upper descending (lower ascending) trend line; at least five touches | target: the highest high (lowest low) of the formation | 103, 105 |
| Rounding bottom / top | trigger: close beyond the lip on above-average volume | target: height of the formation added / subtracted; lip may be hard to find | 77, 79 |
| Scallops (ascending, inverted ascending, descending, inverted descending) | trigger: close beyond the J boundary on above-average volume | target: pattern height from the breakout level | 81, 83, 85, 87 |
| Three falling peaks / three rising valleys | trigger: close below the lowest low (above the highest high) of the formation | target: pattern height; measured move not achieved with regularity | 89, 91 |
| Horn bottom / top (weekly) | trigger: close beyond the extreme of the 3-week range | target: 3-week range added / subtracted | 59, 61 |
| Pipe bottom / top (weekly) | trigger: close beyond the extreme of the two weekly spikes | target: two-pipe height added / subtracted | 69, 71 |
| Island reversal | trigger: gap back to the pre-island level on above-average volume | target: island range added to the highest high or subtracted from the lowest low; average island just over a month, from one day to over 6 months | 63 |
| Moneycontrol volume rule | reduction in volume from the start of the pattern until the breakout; breakout without volume is less reliable | volume matters more for bullish breakouts than bearish | 360 |

**Key quotes**
- "every price pattern there is a setup, a trigger and a projected move" [p. 5]
- "A close above the neckline with above average" [p. 49]
- "The volume should diminish through the pattern up" [p. 7]
- "Measure the length of the previous steep move leading" [p. 35]
- "The price target is obtained by measuring the right lip" [p. 15]
- "Enter long if the price moves through the resistance line" [p. 359]
- "Enter short if the price moves through the support line" [p. 359]
- "taking a measurement from the pattern's high and low" [p. 360]
- "The pattern should breakout within two-thirds to three-quarters of the way to the apex" [p. 93]

**Pseudocode** (daily bars; fields: open, high, low, close, volume)

```
avg_vol[t] = SMA(volume, N)                       # ASSUMPTION N = 50
for each stock s, each day t:
    for P in recognised_patterns(s, t):           # shape rules in Parameters; detection is the hard part
        if P.requires_prior_trend and not prior_trend_ok(P): continue
        B = P.boundary_price                      # neckline / trendline value at t / channel edge / formation extreme
        if P.direction == UP:   triggered = close[t] > B and volume[t] > avg_vol[t]
        if P.direction == DOWN: triggered = close[t] < B and volume[t] > avg_vol[t]
        if triggered:
            entry  = open[t+1]                    # ASSUMPTION (book gives no order type)
            target = measured_move(P, B)          # per Parameters table, e.g. B + (head_to_neckline distance)
            stop   = ASSUMPTION: opposite side of the pattern (e.g. below the pattern low for longs)
            if direction == UP: buy at entry; exit at target or stop
            # DOWN signals: no overnight shorting in NSE cash -> use as exit / avoid-list signal
```

**Ambiguities & assumptions**
- The Big Book gives no stop, no sizing, no time stop. ASSUMPTION: stop = beyond the opposite end of the pattern (for H&S the right shoulder low / neckline re-entry); test also a fixed R multiple.
- "Above average volume" is not defined. ASSUMPTION: volume on the breakout day > 1.5 x 50-day average volume; test 1.0x-2.0x.
- Typos in the source that a coder must not copy: horn top trigger reads "A close above the lowest low" [p. 61] (a bearish pattern; logically below); three rising valleys trigger reads "close below the highest high" [p. 91] (bullish; logically above); the bearish H&S is said to occur "at the bottom of a downtrend" [p. 55]; falling/rising wedges are labelled continuation patterns "within an uptrend / downtrend" [p. 103, p. 105], whereas the Moneycontrol sheet lists falling wedge as bullish and rising wedge as bearish [p. 358]. ASSUMPTION: apply the trigger in the direction named by the Directional Bias line.
- The target statements for several patterns are worded inconsistently (e.g. triangles: "Subtract the height of the highs and lowest low", p. 93). ASSUMPTION: use pattern height = highest high minus lowest low of the formation unless a pattern-specific rule is listed above.
- Pattern recognition itself (what counts as a valid shape, tolerance for "equal" highs/lows) is discretionary; Moneycontrol admits recognition "can be open to interpretation" [p. 361]. ASSUMPTION: restrict the first backtest to rule-detectable patterns (double top/bottom, triple top/bottom, rectangles, ascending/descending triangles, flags) with pivot-based detection.
- Rules from the CMS sheet (QM, QML, fakeout, SR flip) are labels only: not found in this book.

### 2.2 Gap patterns: area, breakaway, continuation, exhaustion, island; window rule

Source files: "Big Book of Chart Pattern.pdf" (pp. 41-47 and p. 63) and "DW candlesticks power.pdf" (p. 235).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion (area gap, exhaustion gap, island) and continuation / breakout (breakaway, continuation gap). | 41, 43, 45, 47, 63 |
| Timeframe & holding period | Daily; area gaps typically fill within a week; exhaustion gaps: nearly two-thirds close within one week, over 90% within two weeks; breakaway gaps often take six months or longer to close. DAR Wong: all windows (gaps) get covered, usually within 55 market trading days. | 41, 47, 43, 235 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Area gap: forms within or just after a consolidation. Breakaway: at the outset of a new trend after a consolidation. Continuation: near the middle of the trend. Exhaustion: late in the trend, after a continuation gap. | 41, 43, 45, 47 |
| Setup conditions | Area gap: common gap with a hook that typically fills within a week. Breakaway gap: volume significantly higher on gap day than the previous day and elevated for several days. Continuation gap: high but not unusually high volume; price holds the gap level. Exhaustion gap: large gap on high volume; the price pauses a couple of days and fails to make a new high or low. Island: gap one way, then a gap back to the pre-gap level, leaving an island. | 41, 43, 45, 47, 63 |
| Entry trigger & order type | Area gap: a close above or below the high or low of the gap day in the direction opposite to the gap. Breakaway: breakout from consolidation and continuation in the direction of the gap after the gap day. Continuation: a gap to a new high or low on higher volume mid-trend and price holds the gap. Exhaustion: price fails to make a new extreme and closes below (above) the low (high) of the gap day. Island: a gap back through the pre-island level on above-average volume. Order type not stated. | 41, 43, 45, 47, 63 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Area gap: gap fills, price returns to the pre-gap level. Breakaway: a move twice the size of the move to the high of the gap day. Continuation: prior move to the middle of the gap, projected from that middle value. Exhaustion: high or low of the day before the gap. Island: island high-low range added to the highest high or subtracted from the lowest low. | 41, 43, 45, 47, 63 |
| Exits: trailing / time / signal | Not found in this text (the 55-day and one/two-week windows are statistics, not exit rules). | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Area gap fill window | within a week, nearly 90% of the time | regardless of prevailing market direction | 41 |
| Breakaway gap size | larger gaps and gaps near a 12-month high or low perform better | - | 43 |
| Breakaway target | 2 x the move to the high of the gap day | wording ambiguous | 43 |
| Exhaustion gap fill | nearly two-thirds within one week; over 90% within two weeks | - | 47 |
| Island duration | average just over a month | one day to over 6 months; short patterns with wide range perform best; pullbacks/throwbacks hurt | 63 |
| Window cover time (DAR Wong) | usually within 55 market trading days | 'simple window' may show the start of a new trend; 'triangle window' = very strong breakaway trend | 235 |
| Volume | breakaway: high for several days; exhaustion: high | island: declines after first gap, expands on second | 43, 47, 63 |

**Key quotes**
- "typically fill within a week" [p. 41]
- "nearly 90% of the time regardless of the prevailing market direction" [p. 41]
- "within one week nearly two-thirds of exhaustion gaps" [p. 47]
- "All windows need to be covered eventually" [p. 235]
- "usually it will be covered within 55 market trading days" [p. 235]
- "price making a move that is two times the size of move to the high gap day" [p. 43]

**Pseudocode** (daily bars)

```
gap_up[t]   = low[t]  > high[t-1]      # DAR Wong window definition (day low above prior day high)
gap_down[t] = high[t] < low[t-1]
# Area-gap fade (long side only in NSE cash):
if gap_down[t] and in_or_just_after_consolidation(t):
    if close[t'] > high[gap_day] for some t' within 5 trading days:   # confirmation = close beyond gap-day extreme opposite to gap
        buy at open[t'+1]
        target = close[gap_day - 1]            # pre-gap level (gap fill)
# Exhaustion gap (bearish -> use as exit signal for longs):
if gap_up[t] and large_gap(t) and volume[t] is high and no_new_high_after(t) and close[t'] < low[t]:
    exit longs / do not buy; expected target = low[t-1]
```

**Ambiguities & assumptions**
- "Large", "consolidation" and "high volume" are not quantified. ASSUMPTION: gap > 2 x ATR(14) counts as large; volume > 1.5 x 50-day average counts as high.
- Breakaway target "two times the size of move to the high gap day" is unclear (move from where?). ASSUMPTION: measure from the pre-gap close to the high of the gap day and project twice that distance from the pre-gap close.
- Area-gap direction: the book labels it "Non-Directional / Reversal"; the trade is the gap fill, i.e. against the gap. ASSUMPTION: long only after a gap-down fill signal, because shorting the cash market overnight is not possible.
- NSE circuit limits and call-auction opening change what a gap is; test with adjusted prices only.
- No stop is given. ASSUMPTION: stop at the extreme of the gap day in the direction of the gap.

### 2.3 Candlestick reversal: buy/sell at next candle open with fixed-pip stop (Metaverse Trading Academy)

Source file: "Candlestick Patterns Ebook.pdf" (pp. 117-131), Metaverse Trading Academy, 2023. The ebook is FX-oriented (pips, "foreign exchange" disclaimer on p. 131).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick reversal / trend-direction entry. | 122, 126 |
| Timeframe & holding period | Not fixed: candle size depends on chart set-up ("an hour, a week, or a month"). Holding period not stated. | 130 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Trade 'in the direction of the trend' (the sheets say BUY / SELL in the direction of the trend at the next candle's open). Trend definition not given. The ebook adds that other indicators help determine trend direction. | 122, 126, 130 |
| Setup conditions | Bullish: morning star, shooting star (as labelled on the bullish sheet), bullish engulfing candle, tweezer bottom, piercing line. Bearish: evening star, shooting star, engulfing candle, tweezer top, dark cloud cover. Piercing line and dark cloud cover: close of the second candle must be beyond a 60% u-turn of the first candle. Tweezer pair: 'wick min. 60%' as shown on the diagram. Ideal candle: full body with small wicks; large bodies with small wicks mean one side is in control. | 122, 123, 126, 127, 121 |
| Entry trigger & order type | Bullish: buy at the opening of the next candle after the pattern completes. Bearish: sell at the opening of the next candle. | 122, 123, 126, 127 |
| Initial stop-loss | Bullish: protective stop loss order 10 pips below the low (engulfing: approximately 10 pips beyond the lows of the wicks). Bearish: protective stop 15 pips above the high. | 122, 123, 126, 127 |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry price | open of the candle after the pattern | - | 122, 126 |
| Long stop buffer | 10 pips below the low | 'approximately 10 pips beyond the lows of the wicks' | 122 |
| Short stop buffer | 15 pips above the high | 'approximately 15 pips beyond the HIGHS of the wicks' | 126 |
| Piercing / dark cloud close | beyond a 60% u-turn of the prior candle | - | 122, 123, 126, 127 |
| Candle colour convention | hollow / light = close above open (bullish); filled / dark = close below open (bearish) | colours user-selectable | 119 |

**Key quotes**
- "BUY at the opening of the next candle with a protective stop" [p. 122]
- "Protective Stop Loss Order 10 pips below the low" [p. 122]
- "Protective Stop Loss Order 15 pips above the high" [p. 126]
- "must be beyond a 60% u-turn" [p. 123]
- "SELL at the opening of the" [p. 126]

**Pseudocode** (daily bars; long side only)

```
if trend_up(s, t) and pattern in {BullEngulfing, MorningStar, BullishShootingStar(inverted-hammer-like), TweezerBottom, PiercingLine}(t):
    if pattern == PiercingLine: require close[t] > open[t-1] - 0.60 * (open[t-1] - close[t-1])   # >60% retracement of the red candle (ASSUMPTION reading of 60% u-turn)
    buy at open[t+1]
    stop = min(low[t-2..t]) - buffer                # buffer: book = 10 pips; NSE ASSUMPTION below
# Bearish counterparts (stop = max(high) + 15 pips) -> exit-long signal on NSE cash
```

**Ambiguities & assumptions**
- Pips do not exist for NSE equities. ASSUMPTION: replace 10 pips by max(Rs 0.05 tick x 2, 0.1% of price) for longs, and 15 pips by 0.15% for the short-side exit; test 0.5 x ATR(14) as an alternative.
- The "trend" filter is undefined. ASSUMPTION: close above 50-day SMA for longs.
- No profit target or trailing rule. ASSUMPTION: exit at 2R, or trail with the 3-day low; test both.
- The bullish-sheet "shooting star" is shown with the instruction "meets the criteria of the Bullish Shooting Star" (p. 122); shape criteria are in the images only. ASSUMPTION: treat it as an inverted hammer (small body, long upper wick, after a decline).
- Which candle's low is used for the stop (pattern low vs signal candle low) is not specified for morning star / piercing. ASSUMPTION: lowest low of the pattern candles.

### 2.4 Candlestick validity conditions with next-day confirmation ("21_Candlesticks")

Source file: "21_Candlesticks.pdf" (pp. 133-196); author not stated. The file lists "validity conditions" for several patterns and says that confirmation by the next candle(s) is required; it gives no entry order, stop or target.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick reversal with next-candle confirmation. | 137, 138, 145 |
| Timeframe & holding period | Daily candles; piercing 'often will end a minor downtrend' lasting five to fifteen trading days. Holding period not stated. | 142 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | 'Definite' prior downtrend (bullish patterns) or uptrend (bearish patterns), judged visually. Dark cloud cover more important at an important resistance area with strong end-of-day volume. | 137, 138, 141 |
| Setup conditions | Hammer / hanging man: lower shadow at least twice the body; no or very small upper shadow; body colour irrelevant (white body better for hammer, black better for hanging man). Shooting star: upper shadow at least twice the body, no or very small lower shadow. Bullish engulfing: white candle opening below prior close and closing above prior open. Dark cloud: black candle opening above prior high and closing more than halfway into prior white body. Piercing: white candle opening below prior low and closing more than halfway into prior black body. Morning star: long dark first day, indecision second day, third day long white reaching at least halfway into the first body. Bullish / bearish harami: second candle's open and close inside the first body (opens above prior close and closes below prior open, bullish case). | 137, 138, 145, 139, 141, 142, 144, 147, 148 |
| Entry trigger & order type | Next-day confirmation only: after hammer 'continued buying'; after hanging man or shooting star 'continued selling'. Marubozu: follow-through early the next day means the stock is likely to trend that way for the next few sessions. Order type not stated. | 137, 138, 145, 149 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Hammer / hanging man lower shadow | >= 2 x body | upper shadow none or very small | 137, 138 |
| Shooting star upper shadow | >= 2 x body | lower shadow none or very small | 145 |
| Dark cloud / piercing penetration | more than half of the prior body | larger penetration = stronger | 141, 142 |
| Morning star third candle | at least halfway into the first body | recovering nearly to the first day's high on strong volume noted as stronger | 144 |
| Evening star | star candle must gap higher; third black candle retreats substantially into first body; gap between days 2 and 3 makes it stronger but is unusual in equities | - | 143 |
| Homing pigeon confirmation | a following candle closes below the lowest low of the two pigeon candles (as printed; see Ambiguities) | the higher the second candle closes, the more convincing | 171, 195 |
| Deliberation block / advance block bearish confirmation | a falling candle overcomes the midpoint of the real body of the second (deliberation) or first (advance block) candle | - | 179, 180 |
| 8-10-12-13 new price lines | eight consecutive candles each with a higher high in an uptrend; last close above the top of the prior real body means rising prices are more likely | below it, falling prices more likely | 172 |
| Hammer/hanging-man next-day rule | next day must show continued buying (hammer) or selling (hanging man, shooting star) | - | 137, 138, 145 |

**Key quotes**
- "The lower shadow must be at least twice the size of the body." [p. 138]
- "The day after the Hammer is formed, one should witness continued buying." [p. 138]
- "The Upper shadow must be at least twice the size of the body." [p. 145]
- "closing more than half way into the body of the previous day’s white candle" [p. 141]
- "The day after the Shooting Star is formed, one should witness continued selling." [p. 145]
- "If there is follow through early the next day, the stock is likely to trend in that same direction" [p. 149]

**Pseudocode** (daily bars; long side)

```
hammer[t]   = downtrend(t) and lower_shadow[t] >= 2*body[t] and upper_shadow[t] <= small
signal[t]   = hammer[t] and close[t+1] > close[t]          # 'continued buying' next day  (ASSUMPTION reading)
if signal[t]: buy at open[t+2]; stop = low[t]               # stop is ASSUMPTION
# Same structure for engulfing / piercing / morning star using the open-close conditions in Parameters.
```

**Ambiguities & assumptions**
- 'Definite uptrend/downtrend' is judged visually. ASSUMPTION: downtrend = close < SMA(20) and SMA(20) falling; reverse for uptrend. Minor trend of 5-15 days for piercing [p. 142].
- 'Continued buying/selling' is not quantified. ASSUMPTION: next close above (below) the signal candle's close.
- 'Small' upper shadow: ASSUMPTION <= 10% of range.
- The bearish engulfing text on p. 140 repeats the bullish conditions word for word (downtrend, white candle) and the shooting-star colour sentence on p. 145 is truncated ("but a black"); use mirror-image of the bullish rule. Homing pigeon confirmation as printed ("below the Lowest Low", p. 171) contradicts its bullish-reversal label; ASSUMPTION: confirmation = close above the highest high of the two candles.
- No stop or target is given anywhere in this file.

### 2.5 DAR Wong: reversal sign + EMA(4,9,20) + slow stochastic, "shadow entry", 9-day-range exit

Source file: "DW candlesticks power.pdf" (pp. 197-247), DAR Wong, APSRI. Written for futures and FX (Nikkei, Dow, EUR/USD, gold examples). The author's accuracy claim and the entry/exit recipes are anecdotal.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick reversal with indicator confirmation; day-trade / next-day range trading. | 202, 239, 240 |
| Timeframe & holding period | Candlesticks to be used only from 30-min, 60-min charts and above (day, week, month). Trading reversals is described as perfect for day trading; continual patterns are held mid to long term. Next-day expectation: sell at day open and buy back at day close (or the reverse). Weekly chart read at week end to forecast the following week. | 202, 240, 241 |
| Universe / eligibility filters | Fast-moving, liquid markets (spot currencies, soft commodities, stock indices); do not use on slow-moving or low-liquidity instruments. | 202 |
| Market / regime filter | Avoid swing days (a series of doji or small-body candles); never trade if confused. A true reversal sign in a continual trend usually comes on day 9-21; reversal candles after 3-5 same-colour days are 'deceptive' and may resume the original trend. | 245, 244, 242, 241 |
| Setup conditions | A convincing candlestick reversal sign on the prior day, coinciding with: (a) Slow Stochastic K% and D% meeting at an extreme zone before the actual intersection; (b) the three EMAs (4, 9, 20) converging, or the 4-day EMA crossing the 20-day. If stochastic is neutral (10%-90%), the reversal day produces only a short-bodied turn. | 239, 240, 241 |
| Entry trigger & order type | 'Shadow entry': take the standard market opening price at local 8:00 am and place a potential entry 20-30 pips away from it, long or short; the distance is estimated by back-testing the average candle shadow length. For the next-day trade after a stochastic-extreme reversal sign: enter at day open. | 242, 240 |
| Initial stop-loss | A pre-planned stop loss order, always pre-set; level not given. | 242, 243 |
| Exits: profit-taking | Estimate the exit from the average of the previous 9 days' range, counted from the current day high or low. Sell at open / buy back at close for the stochastic-extreme case. | 241, 242, 240 |
| Exits: trailing / time / signal | In a continual trend, protect the position with a trailing or outright stop loss. After a true reversal sign expect a sharp reversal of at least 3-4 days, retracing up to 30% or even 50% before the trend resumes. | 234, 242, 243 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| EMA periods | 4, 9, 20 used concurrently | convergence on one close gives a high-probability new trend over the next 2-4 days | 239 |
| Slow stochastic (K% line) | 14 and 21 days average period | three-parameter software: (5,5,5) for FX, (14,3,3) for futures | 239, 240 |
| Stochastic neutral zone | 10% - 90% | extreme zones give a full-range next-day candle | 240 |
| Shadow-entry distance | 20-30 pips from the 8:00 am opening price | back-test average shadow length | 242 |
| Expected daily range | average of previous 9 days' range | - | 241 |
| True reversal day | between day 9 and day 21 of a continual trend | - | 242 |
| Reversal retracement | 30% to 50% | at least 3-4 days | 242, 243 |
| Accuracy of candlestick signs alone | around 60% | higher when combined with the two indicators | 239 |
| Three black crows / three white soldiers | the 4th day decides continuation or reversal; check other indicators | - | 224, 226 |

**Key quotes**
- "plain analysis of purely using candlestick signs" [p. 239]
- "marks an accuracy of around 60%" [p. 239]
- "Use 4, 9, 20 (EMA)" [p. 239]
- "place a potential entry away from the opening price" [p. 242]
- "taking the average of previous 9 days range" [p. 241]
- "Always enter the market with a pre-set stop loss order!" [p. 243]
- "Avoid trading in swing day like series of doji or small body" [p. 245]
- "Recommended to be used only from 30min, 60min chart and" [p. 202]

**Pseudocode** (daily bars; long side)

```
ema4, ema9, ema20 = EMA(close, 4/9/20)
K = slow_stochastic(high, low, close, 14, 3, 3)               # ASSUMPTION: (14,3,3) as in the futures setting
converge[t] = max(ema4,ema9,ema20)/min(ema4,ema9,ema20) - 1 < 0.5%     # ASSUMPTION threshold
bull_reversal[t] = candle_reversal_sign_bullish(t)            # from 2.3/2.4 definitions
if bull_reversal[t] and K[t] in extreme_low_zone and converge[t] and not swing_day(t):
    buy at open[t+1]
    target = open[t+1] + mean(range[t-8..t])                  # 9-day average range
    stop   = low[t]                                           # ASSUMPTION
    exit at close of the same day if intraday style (book: buy at open, sell at close)
```

**Ambiguities & assumptions**
- The text swaps terms: it says the lines meeting "at the bottom overbought zone" predict a full white next day, and "top oversold zone" predicts a sell [p. 240]. ASSUMPTION: low zone (below 10-20%) = oversold = bullish; high zone = bearish.
- Extreme zone and convergence tolerance are not quantified (only 10%-90% as neutral). ASSUMPTION: extreme = K below 10 or above 90.
- 'Shadow entry' is an intraday limit order below (above) the 8:00 am open; for NSE use the 9:15 open. ASSUMPTION: entry offset = 0.5 x average 9-day shadow length, limit order, valid for the day.
- 9-day average range is used to "estimate" the exit but no multiple is given. ASSUMPTION: 1.0 x.
- Stops are said to be mandatory but no level is given. ASSUMPTION: stop beyond the reversal candle's extreme.
- The ~60% accuracy figure has no sample, market or period behind it.
- Shorting the next-day open (sell then buy back at close) is an intraday trade; allowed in NSE cash only as an intraday square-off.

### 2.6 Pristine candle-reversal confirmation and breakout/breakdown reading (Mastering Candlestick Charts 1 and 2)

Source file: "Mastering Candlestick Charts 1 and 2.pdf" (pp. 248-355), Pristine Capital Holdings. Slide-format; Part 2 repeats Part 1 with additions. The author denies that candle names or indicators add edge [p. 251] and wants the reader to learn 'an objective method of knowing when to enter, where to place a stop, how to monitor' [p. 258].

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal / breakout confirmation by price (prior-bar high/low violation). | 318, 288 |
| Timeframe & holding period | No fixed time frame ("there is no such thing as a perfect time frame"). Form a bias on the longer time frame, then take the trade when the shorter time frame candles confirm. Holding period not stated; monitor bar by bar. | 345, 346, 353 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Context is required: accuracy of candle names without trend, support and resistance is 'useless'. Buy setup = 3 or more bars down in an uptrend; sell setup = 3 or more bars up in a downtrend (pull-back into the trend). | 254, 283, 282 |
| Setup conditions | Reversal candle at support / resistance with slowing momentum (narrow body NB, narrowing range bars NRB), or bottoming / topping tail bar (BT / TT: price closes above / below the bar's mid-point). Range-expansion (wide range) reversal bars have better odds; the larger the reversal bar relative to the prior bar and the deeper its retracement into the prior bar, the more 'potent'. Three or more bars moving into a gap followed by slowing momentum is a high-odds setup; one or two bars into a gap on expanding momentum suggests continuation. Multi-bar congestion is significant support or resistance; 1-3 bar reversals are less significant. | 284, 289, 323, 321 |
| Entry trigger & order type | A bearish signal is confirmed only when the bearish candle's low is violated. Chart annotation: 'Short under the low, stop above the high'; after low volatility a wide-range bar ('WRB') breakdown 'ignites' the move: short the breakdown or under the low of the -WRB. A WRB breakout or breakdown after a consolidation ignites a move in that direction. A top tail alone is not a reason to short. | 318, 352, 288, 336 |
| Initial stop-loss | Above the high of the signal bar (shorts); the signal is negated if that bearish candle's high is overcome on a closing basis first. Mirror for longs is implied, not stated. | 352, 318 |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Monitor bar-by-bar: after each candle ask whether it confirms, weakens or negates the prior message. Close position within the bar's range measures strength of follow-through (stronger close, greater odds of continuation). A return to the breakout point after a breakout is negative. | 330, 333, 295 |
| Position sizing | Not found in this text (only 'the time frame must be in alignment with your money management guidelines'). | 345 |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| First support / resistance | prior bar's low / prior bar's high | second level = pivot point | 320 |
| Piercing vs thrust | close beyond 1/2 of prior bar = piercing; less than half = thrust | - | 282, 283 |
| Close location | 40% / 50% / 60% bands of the bar's range shown as strength measure | - | 319 |
| Volume | expansion in volume should come with expansion in body range; expansion with contracting body may signal a turning point; with-trend moves on increasing volume, counter-trend on decreasing | volume is secondary and never a reason to enter by itself | 340, 343 |
| Reversal 'potency' | larger bar vs prior, deeper retracement, range expansion, retest of a prior low | - | 289, 290 |
| Time frames | bias from longer, confirmation in shorter | too many time frames cause confusion | 345 |

**Key quotes**
- "a bearish candle’s low must be violated to confirm a bearish signal" [p. 318]
- "If that bearish candle’s high is overcome on a closing basis first" [p. 318]
- "Short under the low, stop above the high" [p. 352]
- "A WRB Breakout or Breakdown, after a consolidation, ignites a move in that direction." [p. 312]
- "Three or more bars moving into a Gap, followed by" [p. 323]
- "Volume is secondary to price and is never a reason to enter a" [p. 343]
- "A Topping Tail (TT) alone is not a" [p. 336]

**Pseudocode** (daily bars; long mirror of the stated short rule)

```
# Long mirror of 'short under the low, stop above the high' (ASSUMPTION: the book states only the short form)
signal_bar = bullish_reversal_bar(t)        # BT or +COG at support after >= 3 down bars in an uptrend
if high[t+1] > high[signal_bar]:            # violation of the signal bar's high = confirmation
    buy at max(open[t+1], high[signal_bar]); stop = low[signal_bar]
    cancel setup if close[t'] < low[signal_bar] before trigger
```

**Ambiguities & assumptions**
- All terms (NB, NRB, WRB, COG, BT, TT, 'potent') are defined only by pictures and loose words. ASSUMPTION: WRB = range > 1.5 x average range of last 10 bars; NB = body < 30% of range; BT = close above 50% of the bar's range after a lower low.
- 'Buy setup: 3 or more bars down in uptrend' appears under a page captioned "Prices are trending lower, the potency of the reversal signals are increasing" [p. 283]; the pairing of setup and caption is confusing. ASSUMPTION: buy setup = pull-back of 3 or more down bars inside an uptrend.
- Profit target and sizing are not found in this book; ASSUMPTION: use a fixed 2R target or the next resistance (prior high).
- Pristine itself says the indicator add-ons do not raise reliability [p. 251]; do not add filters to the first test.

## 3. Risk & money-management rules

- Always enter with a pre-set stop loss order [p. 243]; "Never sit on a losing position" and "Never trade if you are confused" (DAR Wong 3N rule, with "Never think the market is wrong") [p. 244].
- In a continual (trend-following) trade, protect the position with a trailing or outright stop loss [p. 234].
- Fixed-pip protective stops: 10 pips beyond the low for longs, 15 pips beyond the high for shorts [p. 122, p. 126].
- The time frame traded must align with the trader's money management guidelines; changing time frames to stay in a trade is called one of Pristine's Seven Deadly Sins [p. 345].
- Defining an opportunity where the odds are in your favour and then following the trading and money-management rules is "all that you can do" [p. 298].
- Moneycontrol: chart patterns provide an entry point and stop loss and a target from the pattern height [p. 360].
- No position-size, risk-per-trade, drawdown or portfolio-heat rule appears in any of the seven files (not found in this text).

## 4. Non-codable guidance

- Candle names do not matter; the "message" of each candle (momentum slowing or reversing, greed and fear) does [p. 254, p. 297]. Never think beyond the current candle; a candle is not complete until its period ends [p. 338, p. 278].
- Signals that do not work are often the most powerful (red bars ignored, green bars ignored, no follow-through) [p. 254, p. 274].
- Focus on the message of candle language, not the money; trading is recognising, not predicting [p. 353].
- Pattern recognition is open to interpretation and subject to personal bias; false breakouts and exceptions occur [p. 361].
- Candlestick patterns have been "proven for few hundred years" and "no limitations" per DAR Wong; treat as marketing claims [p. 202]. Do not let greed take over; stay out when there is no clear market sign [p. 243, p. 244].
- Reversal signs after 3-5 same-colour days may be deceptive; a 'conditioned day' of small candles can precede the real move [p. 241, p. 242].
- Do not use too many time frames [p. 345].

### 4.1 Pattern definitions only (no trigger, stop, target or statistic): reference table

| Pattern | File | Page |
|---|---|---|
| Doji star | 21_Candlesticks | 133 |
| Long-legged doji | 21_Candlesticks | 134 |
| Gravestone doji | 21_Candlesticks | 135 |
| Dragonfly doji | 21_Candlesticks | 136 |
| Inverted hammer | 21_Candlesticks; Pristine; DAR Wong | 146, 261, 217 |
| Marubozu | 21_Candlesticks | 149 |
| Spinning top | 21_Candlesticks; Pristine | 150, 260 |
| High wave | 21_Candlesticks; Pristine | 151, 260 |
| Three black crows | 21_Candlesticks; DAR Wong (4th-day rule only) | 152, 224 |
| Three white soldiers | 21_Candlesticks; DAR Wong | 153, 226 |
| Tweezers top / bottom | 21_Candlesticks; DAR Wong (pincer) | 154, 222 |
| Stick sandwich | 21_Candlesticks | 156 |
| Dumpling top | 21_Candlesticks | 157 |
| Fry pan bottom | 21_Candlesticks | 158 |
| Tower top | 21_Candlesticks | 159 |
| Tower bottom | 21_Candlesticks | 160 |
| Mat hold | 21_Candlesticks | 161 |
| Abandoned baby | 21_Candlesticks | 163 |
| Tri-star doji | 21_Candlesticks | 163 |
| Above / below the stomach | 21_Candlesticks | 164 |
| Thrusting line | 21_Candlesticks; Pristine | 165, 189, 266 |
| Separating lines | 21_Candlesticks; Pristine | 166, 267 |
| Three line strike | 21_Candlesticks | 167 |
| Meeting line | 21_Candlesticks | 168 |
| Low price gapping play | 21_Candlesticks | 169 |
| High price gapping play | 21_Candlesticks | 170 |
| Scoop | 21_Candlesticks | 173 |
| J-hook / inverted J-hook | 21_Candlesticks | 174 |
| Cradle | 21_Candlesticks | 176 |
| Rising three methods | 21_Candlesticks | 177 |
| Falling three methods | 21_Candlesticks | 178 |
| Kicker | 21_Candlesticks | 181 |
| Unique three river bottom | 21_Candlesticks | 182 |
| Downside gap two rabbits | 21_Candlesticks | 182 |
| Three stars in the south | 21_Candlesticks | 183 |
| Concealing baby swallow | 21_Candlesticks | 183 |
| Ladder bottom | 21_Candlesticks | 184 |
| After bottom gap up | 21_Candlesticks | 184, 186 |
| Descent block | 21_Candlesticks | 185 |
| Deliberation block (bullish) | 21_Candlesticks | 185 |
| Squeeze alert | 21_Candlesticks | 186 |
| On neck line | 21_Candlesticks; Pristine | 187, 191, 265 |
| In neck line | 21_Candlesticks; Pristine | 188, 192, 265 |
| Side-by-side white lines | 21_Candlesticks | 190, 194 |
| Matching low | 21_Candlesticks | 196 |
| Pincer (double top / bottom candles) | DAR Wong | 222 |
| Fighting warriors | DAR Wong | 228 |
| Three mountains / Buddha top | DAR Wong | 230 |
| Three river beds | DAR Wong | 232 |
| Repelling lines | DAR Wong | 237 |
| Doji, gravestone, dragonfly, long-legged doji | Pristine | 259 |
| Bullish / bearish harami cross | Pristine | 264 |
| Wide range bar, narrow body, narrowing range bars, COG reversal bar | Pristine (terms) | 278, 279, 280, 281 |
| Quasi-Modo (QM / QML), fakeout V1 / V2, SR flip, MPL, flag A + flag B | CMS cheat sheet (labels only) | 107 |
| Basic bullish / bearish candlestick cheat sheet (hammer, engulfing, harami, morning / evening star, kicker, etc.) | CMS / jbmarwood sheet | 108, 109 |
| Japanese candle list (many named patterns, Indonesian labels: reversal / penerusan = continuation) | CMS sheet | 110, 111 |
| Harmonic patterns (Gartley, Bat, Butterfly, Crab, Cypher etc., Fibonacci ratios) | CMS sheet | 111, 114 |
| Elliott wave: impulse, diagonal, zigzag, flat, triangle | CMS sheet | 115 |
| Reversal / continuation chart-pattern lists (double top / bottom, H&S, rounding, triple; flag, pennant, triangles, rectangle, cup and handle) | Moneycontrol | 357, 358 |

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV (open, high, low, close, volume) for all rules; delivery % is optional (a volume-quality filter). Index data (NIFTYBEES or equal-weight index) only for trend context. No fundamentals are used. Weekly bars are needed for horn, pipe patterns (aggregate daily to weekly).
- **Testability with our data:** All of 2.1-2.6 are price-only and backtestable on 2005-2026 data. The practical difficulty is pattern detection, not data: only the rules that can be turned into pivot-based algorithms are testable (double / triple tops-bottoms, rectangles, triangles, flags, gaps, simple candle rules). Items that need images (CMS diagrams, Big Book charts, Pristine annotated examples) cannot be coded from this text. Pip-based stops (2.3, 2.5) must be converted. Intraday-flavoured rules (2.5: 8:00 am open entry, sell at open / buy back at close) need intraday data we do not have (only daily bars), so the shadow entry cannot be tested exactly.
- **Market-structure differences:** (i) The sources are written for FX, futures and US stocks; ASSUMPTION: apply to NSE stocks on daily/weekly bars only. (ii) No overnight shorting in NSE cash: bearish signals become exits or avoid-lists; ASSUMPTION: long-only test. (iii) Circuit limits can hide breakouts and gaps (a gap of 5/10/20% price band); ASSUMPTION: exclude stocks hitting circuit on the signal or entry day. (iv) STT, brokerage and about 0.1% slippage matter for patterns with small targets (candles with 10-pip stops); ASSUMPTION: require target >= 3 x round-trip costs. (v) Small-cap liquidity: ASSUMPTION: min 20-day average traded value Rs 1 crore. (vi) Splits and bonuses are adjusted in our data, so gap detection must use unadjusted gaps on corporate-action days only after checking.

## 6. Verdict

- **Codeability:** Partly. The breakout and gap rules (2.1, 2.2) and the candle conditions (2.3, 2.4) are numeric enough to code once pattern detection is defined; stops, sizing and exits are mostly missing, DAR Wong and Pristine are discretionary.
- **Priority for backtesting:** Low-to-Medium. Bulkowski-style breakout with measured-move target (2.1, restricted to double / triple tops-bottoms, triangles, rectangles, flags) and the gap-fill statistic (2.2) are worth one test; single-candle rules from the cheat sheets have no reported edge (DAR Wong cites ~60% with no sample [p. 239]).
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating pattern shapes as unambiguous: the sources define patterns visually, and the typos in the Big Book (horn top "above the lowest low", three rising valleys "below the highest high", wedge labels) will produce inverted signals if copied literally.
  2. Using pips and intraday opens (8:00 am shadow entry, next-candle open with 10/15 pip stops) on NSE daily data; and treating bearish rules as shorts although the NSE cash market has no overnight shorting.
  3. Ignoring the missing pieces: no stops, no sizing and an undefined "above average volume" in the Big Book, so any backtest depends entirely on the assumptions chosen; also reading the Pristine "buy setup / sell setup" labels backwards.
