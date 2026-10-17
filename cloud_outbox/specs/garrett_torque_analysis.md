# Investing for Profit with TORQUE Analysis of Stock Market Cycles — William C. Garrett

- **Source file:** Google Drive "William_C__Garrett_Investing_for.pdf" (243 pages, scanned book, no text layer; Prentice-Hall, Inc., Englewood Cliffs, N.J.; copyright year shown on the copyright page as 1973, the (c) sign is lost in OCR [p. 2])
- **Text file used:** text/garrett_torque_analysis.txt  (page basis: pdf_pages, RapidOCR of page scans)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter (printed page = PDF page + 8 in the body of this book).
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/<key>.md text/<key>.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read the whole text file, lines 1-13796, sequentially, last `[[PAGE 243]]` reached (nothing skipped; the index, pp. 235-243, was read but contains no rules). OCR caveats: spaces are often dropped in headings and short lines; running heads/printed page numbers appear at page tops and were ignored; all figures are images and are OCR'd as axis-number noise, so chart content is unreliable on pp. 24, 25, 29-31, 34, 39-42, 45, 48, 50, 52, 59, 68-71, 74, 85, 97-98, 101, 108-109, 111, 113, 120-121, 125-126, 138, 140-141, 143, 147, 152-153, 155, 157-159, 166-168, 173, 175, 179, 185, 187, 189, 201, 203-204, 212, 214, 217, 220-221, 223, 225, 229, 231-232. The two core data tables (Table 4.1, Table 4.2: moving totals and cyclical strengths, pp. 132-133) are OCR'd column by column with columns scrambled and are NOT usable as data; Tables 6.1 (p. 208) and 6.2 (p. 210) are also scrambled (only row-level stock names and some numbers are legible; the text commentary on pp. 209 and 211 was used for the averages). Short pages (1, 6, 11, 18, 25, 50, 52, 113, 212, 214, 217, 220, 223, 225, 229, 232, 243) are title/chart/index pages. Table 1.1 (p. 27) and Table 2.1 (p. 87) and Table 3.1 (p. 101) are also column-scrambled; their formulas are explained in the prose. *Coordinator check: the PDF is a scan with no text layer, so the coordinator ran RapidOCR on all 243 pages (200 dpi). The coordinator re-ran verify_citations (44/44 ok) and an exact-page strict check (0 off-by-one), and confirmed all six field tables have exactly the 12 template rows. 10 unquoted citations were spot-checked by grep and page read: buying-volume example 19.76M = 12.24M + 7.52M p.124 (OCR 'shares' with commas), price/volume factors p.134-135, asymptote 120/90 p.161, 39-week and 104-week totals p.137/153, 221-week cycle p.154, consensus of cycles p.154/161, 'in no way a valid forecaster' p.53, hand-picked Table 6.1 stocks p.209, Prentice-Hall p.2; all matched.*

## 1. The method in brief

Garrett's thesis is that stock prices respond directly to only two influences, the economic outlook and market cycles [p. 19], and that cycles are rhythmic swings in the balance of buying and selling pressure. He claims cycles cause "probably. more than half of the extent of a price swing" [p. 5], that the DJI contains a chord of harmonic-length cycles (about 2 weeks/10 trading days, 10 weeks, 25 weeks, 78 weeks (first estimated as 75), 221 weeks (first estimated as 225; the 4.25-year cycle), plus longer 8.5-year and 17-year cycles, and a sixth cycle of about 5 weeks added late) [p. 28, p. 38, p. 49, p. 137, p. 222], and that individual stocks swing with these cycles in varying degree [p. 202-p. 205, see 2.4]. "TORQUE analysis" is his measurement method: price movement (stocks advancing vs declining) divided by volume balance (buying vs selling volume), computed on end-formed moving totals whose length equals the cycle radius (half the cycle length) [p. 117, p. 131, p. 135]. The resulting ratio, plotted with 100 as equilibrium, swings between cycle-specific ceilings and floors ("asymptotes") and is used to judge where each cycle is in its swing [p. 174-p. 175]. The method was built on US data (DJI 1897-1972, NYSE advances/declines and volume), for the market average first and for individual NYSE stocks second; the intended use is buying at cycle troughs and selling (leading) cycle peaks over holding periods of weeks to years [p. 193, p. 195, p. 205].

Evidence offered is almost entirely illustrative: charts of the DJI with cycle tracks for 1966-1970, trough dates of the 4.25-year cycle (1949, 1953, 1957, 1962, 1966, 1970) [p. 156], a few worked stock examples and two tables of selected stocks' percentage swings between cycle lows and highs [p. 208-p. 211]. The book contains no systematic backtest of buy/sell signals, no trade list, no win rate, and no equity curve. The author himself says the five-cycle synthesis is "in no way a valid forecaster" [p. 53] and that "forecasting remains an art" [p. 176]. Treat the book as an indicator definition (fully computable) plus discretionary interpretation (partly codable).

## 2. Strategies

### 2.1 TORQUE multi-cycle market timing (market-level indicator and trough/peak rules)

Codeability: the indicator is Fully codable from breadth and volume data; the buy/sell decision rules are Partly codable (judgement about when a cycle is "approaching an asymptote" and when cycles are in "consensus").

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Cycle/breadth-based market timing (mean-reversion between cycle troughs and peaks, with the cycle chord acting as trend), applied to a market average | 117, 193 |
| Timeframe & holding period | Chord of cycles: 2-week, 10-week, 25-week, 78-week, 221-week (4.25-year), plus a late-added 5-week cycle. Holding period follows the cycle chosen (78-week cycle swings last about nine months; 4.25-year cycle has about two years or better on the upside). No fixed holding period for the market. | 137, 218, 207, 222 |
| Universe / eligibility filters | Market average only (DJI used for price travel; all NYSE issues for advances/declines; NYSE volume). Book says the same cycles appear in S&P 500, NYSE, ASE and OTC averages. | 124, 117, 200 |
| Market / regime filter | Long cycles supply the trend for short cycles; trend (flat vs up) changes cycle asymptotes: in an uptrend the downswing fails to equalize the upswing, in a downtrend the upswing fails to reach the top asymptote. | 175-176 |
| Setup conditions | (a) Compute TORQUE value for each cycle from end-formed moving totals. (b) A cycle approaching its asymptote (ceiling or floor) is expected to reverse. (c) A genuine major trough is one where several/all cycles trough together ("consensus of cycles"). (d) Place the first trough using average length, amplitude, and synchronization. | 135-136, 175, 154, 172 |
| Entry trigger & order type | Buy when cycles are troughing/turning up (esp. when several cycles trough together); no order type, price trigger or confirmation bar is specified. Not found as a mechanical rule. | 154, 193 |
| Initial stop-loss | Not found in this text (only: if a stock bought as cycles turn up goes against you, "write off the loss as quickly and cheaply as possible"). | 194 |
| Exits: profit-taking | Sell at/near cycle peaks, preferably "lead the peak somewhat" rather than wait for the absolute top; price peaks are hard to identify because price cycles roll over the top. | 193, 195, 170 |
| Exits: trailing / time / signal | Signal exit: cycle approaches upper asymptote or turns down; bullishness assumed from trough to rounding peak and bearishness from peak to trough. No trailing stop or time stop. | 175, 199 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Daily upward "travel" of the index | (high - prior close) + (close - low); worked example prior close 766.16, high 780.53, low 763.76, close 776.70 gives 14.37 + 12.94 = 27.31 | If high is below prior close, no upward move from close to high; upward move is low-to-close only (OXY example) | 122, 124, 128 |
| Daily downward travel | high - low (example 16.77); net = up - down = close - prior close (10.54) | In OXY example down = prior close - low | 122, 124, 128 |
| Buying volume | Total volume x upward travel / (upward + downward travel); selling volume = total - buying (example 19.76 million shares gives 12.24 million buying, 7.52 million selling) | Tick counting is an alternative but "all methods are only good approximations" | 124 |
| Price movement input | Daily count of advancing stocks and declining stocks (A-D) substitutes for index price movement | - | 128, 129 |
| Moving-total length for 2-week (10-day) cycle | 5 trading days (cycle radius) | - | 136 |
| Moving-total length for 10-week (50-day) cycle | 25 trading days | - | 135 |
| Moving-total length for 25-week cycle | 65 trading days (13 weeks) | 25-week cycle is 125 days, so exact half would be 62.5 | 29, 151, 179 |
| Moving-total length for 78-week cycle | 39 weeks (three quarters), adjusted from half of 75 weeks | Original estimate 75 weeks | 137 |
| Moving-total length for 221-week cycle | 104 weeks (two years), adjusted from half of 225 weeks | Original estimate 225 weeks | 137 |
| Moving-total length for 5-week cycle | Not stated | Half the cycle would be about 12-13 days | 222 |
| Trend lines | 10-day (two-week) trend and 50-day (10-week) trend: moving totals of full cycle length divided by length ("For cycles we use half the length, for trends the full length") | Fig. 4.11-4.15 labelled "5 Trends Combined" (components not defined) | 135, 153 |
| Total type | End-formed (plotted at the last input), not centered; lag of a total is half its length | Centered totals discussed and rejected | 137, 138 |
| Price factor | Sum of advances over N days / sum of declines over N days | Practical limit of the 10-day cycle price factor about 2-to-1 | 135, 134 |
| Volume factor | Sum of buying volume over N days / sum of selling volume over N days | - | 135 |
| TORQUE (cyclical strength) | Price factor / volume factor; example Monday wk 44: 0.7619 / 0.9965 = 0.7646 | Charts scale equilibrium as 100 | 135, 136, 160 |
| Worked 10-day example, Monday wk 48 | 5-day: 2.2484 / 1.3598 = 1.6535; 25-day: 1.0977 / 1.0381 = 1.0574 | - | 134 |
| Worked 25-week example (mid-1970 low) | A/D ratio 64%, volume balance 76%, cycle 64/76 = 84% | - | 151 |
| Practical limit of A-D price ratio | 1-to-2 to 2-to-1 (angles 26 deg 34' to 63 deg 26') | - | 119 |
| Asymptotes, 2-week cycle | Swings about 50 to 200 | - | 161 |
| Asymptotes, 10-week cycle | About 75 to 150 swing; ceiling 130 | Ceiling 130 unchanged in 1953-57 bull version | 161, 174 |
| Asymptotes, 25-week cycle | 120 to 90 (1966-70); ceiling 120 unchanged in 1953-57, low about 95 | - | 161, 174, 175 |
| Asymptotes, 78-week cycle | 110 to 95; high about 109.5 and low a little under 92 in 1966-70 | - | 161, 174 |
| Asymptotes, 221-week (4.25-year) cycle | 105 to 97.5 on charts; 95 and 105 limits; ceiling "raised to a possible 112" in the strongly bullish 1953-57 version | 4.25-year cycle amplitude about 10% | 161, 174, 172, 207 |
| Synchronization test | Count of cycles troughing together: 1966 trough had 25-, 78-, 221-week in week 41 and 10-week in week 36; 1970 low had all five | - | 177 |
| Reported 10-week trough dates vs DJI troughs | Weeks 37/1966, 15/1967, 35/1967, 44/1967, 12/1968, 33/1968, 31/1969, 41/1969, 51/1969, 17/1970, 27/1970, 47/1970 | - | 161 |
| 4.25-year (221-week) trough dates | June 1949, September 1953, October 1957, June 1962, October 1966, July 1970 (ideal timing would have been Oct 1970); next projected Sept-Oct 1974 | Gap to ideal 13 weeks in 1970 | 156, 172 |
| Volume vs 52-week moving average (auxiliary) | DJI swung about 12 points above and 18 below its 52-week MA; volume about 150% at peaks and 65% at lows; peaks/troughs 50% from trend at 100 | - | 188-190 |
| Velocity index (auxiliary) | 5-day DJI travel / 5-day NYSE volume; 1970 average 2.68 DJI points per million shares, range about 1.5 to 4.7 | - | 148-149 |

**Key quotes**

- "the net movement of price divided by the net amount of volume cquals the cyclical strength factor" [p. 117]
- "we start with ycsterday's closing price and consider that the average moved only upward from this figure to today's high" [p. 122]
- "multiply the volume on the exchange by the amount of upward travel and divide by the total travel" [p. 124]
- "a cyclical radius of a 50-day cycle is simply a 25-day total of daily figures" [p. 135]
- "we now use totals of 39 weeks" [p. 137]
- "we use end-formed totals instead of centered ones" [p. 138]
- "the 25-week rhythm matches the swings of the 65-day" [p. 151]
- "The real troughs of the market, then, occur when there is a combination of cycles troughing" [p. 154]
- "a cycle is likely to reverse or alternate, when it approaches the limits" [p. 175]
- "price troughs are easy to spot but price peaks are difficult to establish" [p. 170]
- "we prefer to lead the peak somewhat instead of trying for the absolute top" [p. 195]

**Pseudocode**

```
# Data: index_high, index_low, index_close (daily), total_volume (daily),
#       adv_count, dec_count (daily breadth)
for each day t:
    up   = max(index_high - index_close[t-1], 0) + (index_close - index_low)
    down = up - (index_close - index_close[t-1])          # = high-low in the ordinary case
    buy_vol  = total_volume * up / (up + down)
    sell_vol = total_volume - buy_vol
radius_days = {"2wk": 5, "10wk": 25, "25wk": 65, "78wk": 195, "221wk": 520}   # 5 days/week
for cyc, N in radius_days.items():
    A = rolling_sum(adv_count, N); D = rolling_sum(dec_count, N)
    B = rolling_sum(buy_vol, N);   S = rolling_sum(sell_vol, N)   # end-formed (trailing)
    torque[cyc] = 100 * (A / D) / (B / S)
# Signals (discretionary in the book; this is one mechanical reading):
asym = {"2wk": (50,200), "10wk": (75,130), "25wk": (90,120), "78wk": (92,110), "221wk": (95,105)}
trough_flag[cyc] = torque[cyc] has made a local minimum within ~band of asym floor
consensus_trough = count(trough_flag within +/- 2 weeks across cycles) >= K  # K not given; book cites 3 of 5 (1966) and 5 of 5 (1970)
BUY (index/ETF) when consensus_trough and 78wk & 221wk torque turning up
SELL/flat when 25wk, 78wk torque near asym ceiling and turning down (lead the peak)
```

**Ambiguities & assumptions**

- The book never states a mechanical entry/exit rule from the TORQUE values. It says reversals come near the asymptotes [p. 175] and that real troughs are where several cycles trough together [p. 154]. ASSUMPTION: trough = local minimum of TORQUE confirmed N days later; consensus = at least 3 of the 5 cycles within 2 weeks, with the 78-week and 221-week cycles turning up. Optimise K, N on 2005-2015 and test 2015-2026.
- Asymptote values differ by passage (e.g. 25-week "120 and 90" on p. 161 vs 120 and about 95 on p. 175; 10-week 75-150 on p. 161 vs ceiling 130 on p. 174). ASSUMPTION: use ceilings 130/120/110/105 and floors 75/90/95/95 as starting points and treat them as historical (the author says "asymptotes, like trend, are historical in nature" [p. 175]) so re-estimate on a rolling basis.
- Lengths of the 25-week total (62.5 vs 65 days; the 13-week total label on p. 179) and the 5-week cycle total are not exact. ASSUMPTION: 65 days and 13 days.
- Advances/declines are NYSE counts (1,482 issues traded on the sample day in 1967 [p. 26]); the universe size changes the absolute totals but not the ratios. ASSUMPTION: use the full NSE panel (adjusted for listing/delisting) and compute ratios only.
- The book gives only the two worked cases for up/down travel (high above prior close, and high below prior close); the single formula in the pseudocode is a generalization. ASSUMPTION: it holds for gaps. A-D are counted vs prior close; an unchanged stock is neither. Not specified. ASSUMPTION: unchanged counts as neither.
- No performance statistics for these rules exist in the book; the only "tests" are retrospective chart readings: the 25-week cycle "can be said to have troughed on time only about eight times" in 11 versions [p. 161], and the 10-week trough list above [p. 161].

### 2.2 Extrusion forecast of the moving totals (short-term TORQUE direction)

Codeability: Partly (the arithmetic is exact; estimating future input is a judgement).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Short-term forecast of the direction of an end-formed moving total (and hence of the cycle TORQUE value) | 180-181 |
| Timeframe & holding period | Any of the cycles; the 5-day input cycle is projected ahead by the length of each total (e.g. 39 weeks) | 180 |
| Universe / eligibility filters | Market breadth totals (advances) | 180 |
| Market / regime filter | Total's direction matters most near an asymptote, where reversal is expected | 181 |
| Setup conditions | Draw the balance point of the 5-day advances total (about 3300 in 1970, range about 1300 to 5300). Past input values that will drop out of the total (outgo) are "extruded" forward; if the outgo values are high the total will tend to fall unless new input matches them. | 180 |
| Entry trigger & order type | Not found as an explicit trade rule; used to anticipate cycle troughs and peaks. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Reverse expectation when input fails to meet the extruded outgo; the total reverses when the cycle reaches an asymptote. | 181 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Input series | 5-day moving total of advances | - | 180 |
| Total lengths used in Fig. 5.7 | 5-week, 13-week, 39-week, 2-year moving advances totals | - | 178, 179 |
| Balance point of the 5-day advances total (1970) | About 3300; swings from about 1300 to 5300 | Level scales with the number of issues | 180 |
| Change of end-formed total | New input minus outgo (input from N days earlier) | - | 180 |
| Observed lag (1970) | Shortest total troughed at market bottom; 39-week total about six weeks later; 2-year total in the fourth quarter (Nov 1970) | Lag about half the total's length | 178, 181 |

**Key quotes**

- "The end-formed moving total, then, will move up or down by the net difference between the new input figure and the outgo figure from 39 weeks previous" [p. 180]
- "prediction of the movement of the total consists largely of estimating what the input is likely to be" [p. 181]
- "when a cycle reaches or approaches an asymptote, it will reverse its direction" [p. 181]

**Pseudocode**

```
N = total length in days (e.g. 195)
outgo_next = adv_count[t - N + 1]            # value that will be subtracted tomorrow
expected_input = 3300 (or 0.5*(adv_count+dec_count) average)   # balance point
delta_forecast = expected_input - outgo_next
if delta_forecast > 0 : total expected to rise; else expected to fall
combine with TORQUE value vs asymptotes from 2.1
```

**Ambiguities & assumptions**

- The book never tests the extrusion forecast; it only shows 1970 as an illustration [p. 180-p. 181]. ASSUMPTION: forecast input = trailing 25-day mean of daily advances (the "balance point").
- Balance point 3300 is NYSE-specific. ASSUMPTION: recompute as long-run mean of the 5-day advances total on the NSE panel.

### 2.3 Mechanical cycle timetable (ideal trough dates and five-cycle sine synthesis)

Codeability: Partly (the synthesis is exactly specified; the placement of the zero point and re-synchronization are judgemental).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Calendar/phase projection of cycle troughs (time-based cycle model) | 172, 53 |
| Timeframe & holding period | Cycle lengths 10 trading days, 10 weeks, 25 weeks, 75/78 weeks, 225/221 weeks; double cycle 450 weeks (8.5-year) | 28, 35 |
| Universe / eligibility filters | Market average (DJI) | 38-59 |
| Market / regime filter | Business recessions can lengthen cycles (e.g. 1957-58 recession delayed the 1962 trough); outlook affects cycle lengths | 46 |
| Setup conditions | Start the timetable at a firm trough where cycles are synchronized (the "pinpoint" trough at week 0 or week 450); project later troughs at the average length. After a clock-setting trough, a whole new timetable begins. | 51, 161, 172 |
| Entry trigger & order type | Not found as a rule; timetable only gives expected dates of troughs. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Time-based: the thrust to the apex takes about half the cycle length (10-week cycle: about five weeks); timing is adjusted when longer cycles break into harmonic pieces. | 131, 37 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Cycle lengths in weeks | 2 (10 trading days), 10, 25, 75 (later 78), 225 (later 221) | 8.5-year, 17-year, 34-year longer cycles | 28, 137 |
| Synthesis sine spacing | Each cycle given amplitude 1.0000; sine values spaced equally between zero and 1 over the weeks in its half cycle (10-week: 0.0000, 0.3090, 0.5878, 0.8090, 0.9511, 1.0000) | 25-week half cycle has 12.5 weeks, never quite reaches 1.0000 (0.1253, 0.2487, 0.3681, 0.4818, 0.5878, 0.6846, 0.7705, 0.8443, 0.9048, 0.9511, 0.9823, 0.9880) | 33 |
| Combination | Sum the five cycle values (divide by five for an average), then average each two adjacent intervals to smooth | - | 33-34 |
| Synthesis peak / return to zero | Peaks at weeks 112-113; low at week 220; returns to zero only at week 450 (double cycle) | Book says 450 weeks = 8.65 years in one place and 8.5 years elsewhere | 34-35, 49 |
| 17-year cycle ideal troughs | June 1898, June 1915, June 1932, June 1949, June 1966, June 1983, anchored on June 1932 low | 4.25-year cycle fits four times in 17 years | 38 |
| Reported timing misses | 4.25-year cycle never bottomed on time from 1897 to 1932 and was correct only in 1949 and 1953; 17-year cycle on time only in 1949 | Late by three months in 1966 | 39 |
| 78-week cycle details | Troughs 41st wk 1966, 14th wk 1968, 36th wk 1969 (ideal wk 41), 27th wk 1970; mechanical next 78 weeks from 1970 trough (actual trough 47th wk 1971, 72 weeks) | - | 156 |
| Ideal 25-week and 10-week nadir marks | First 25-week trough 25 weeks after the synchronized trough, second 50 weeks after | - | 161 |
| Reported trough fit | 25-week cycle "troughed on time only about eight times" of 11 versions | - | 161 |

**Key quotes**

- "by spacing sine values equally between zero and" [p. 32]
- "we average the strength between each of two intervals" [p. 34]
- "in no way a valid forecaster" [p. 53]
- "it should have troughed in June 1949, again in June 1966" [p. 38]
- "Not counting the 1932 trough, the 4.25-year cycle never bottomed" [p. 39]
- "we must project that the next cyclical low of the 221-week cycle will come" [p. 156]
- "The key to correct forecasting, then, is the placement of the first trough of a" [p. 172]

**Pseudocode**

```
anchor = date of a major synchronized trough (e.g., all 5 TORQUE cycles at floor)
for each cycle c with length L_c weeks:
    ideal_trough[c, k] = anchor + k * L_c weeks
# five-cycle synthesis (reference model, optional):
for week w in 0..450:
    S[w] = sum_c sin(pi * (w mod L_c) / L_c)  # book uses half-cycle sine spacing, folded
    S_smooth[w] = 0.5*(S[w] + S[w-1])
re-anchor at each new consensus trough (see 2.1)
```

**Ambiguities & assumptions**

- The book explicitly says the synthesis "is in no way a valid forecaster" [p. 53] and that its use is to study past price rallies/recoils. ASSUMPTION: test the timetable only as an information feature (distance to next ideal trough), not as a stand-alone timing system.
- Cycle lengths are US/DJI-derived and rounded (75 to 78, 225 to 221) for seasonal (quarterly) fit [p. 137]. ASSUMPTION: re-estimate dominant periods on NSE data by spectral analysis before using the US lengths.
- How the synthesis is "folded" beyond week 225 is only described in prose [p. 35, p. 49]. ASSUMPTION: mirror about week 225.

### 2.4 Individual-stock cycle-trough buying (stock selection by cycle response, fundamentals and group)

Codeability: Partly (the response criteria and sell rules are qualitative).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Cycle-timed swing/position trading of selected stocks (buy at cycle troughs, sell near peaks) | 193, 195 |
| Timeframe & holding period | Long swings follow the 4.25-year and 78-week cycles; 78-week-cycle dips described as good buys "for holding periods of about six months"; 78-week swings about nine months; short-cycle swings (5-week to 25-week) for stocks that depart from the long cycles | 205, 218, 215 |
| Universe / eligibility filters | Prefer stocks that are (1) in a good earning situation and (2) most responsive to cyclical pull; also a good group. Responsiveness judged by how the stock tracked the 221-, 78-, 25-week and short cycles; "if a stock fails to respond to a short cycle, its performance is suspect". | 193, 206 |
| Market / regime filter | Buy when the market cycles are turning up from a trough (esp. several cycles troughing together); in a flat/down long-cycle trend, selling matters more than buying. | 154, 198 |
| Setup conditions | Stock price near its low at the last 4.25-year trough while the cycle is ready to start up = "cheap"; stock price near its last peak price while the cycle peaks = "high" | 226 |
| Entry trigger & order type | Buy at a cycle trough; the chart studies show stocks beginning to move about four weeks after the cycle trough (Control Data). No order type specified. | 193, 211 |
| Initial stop-loss | No numeric stop. "If you select a stock when cycles are turning upward and the stock goes against you, the purchase was a mistake. Write off the loss as quickly and cheaply as possible". | 194 |
| Exits: profit-taking | Sell as close as possible to a cyclical peak, leading it somewhat; a stock may decline up to 66% of its thrust and still advance (technicians' rule) | 195, 233 |
| Exits: trailing / time / signal | Sell when cycles recoil; "hold on" while the stock moves in your direction but watch for reversion to the cycles; track anti-cyclical stocks with short cycles and trade only short swings | 226, 215, 233 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fundamental / group / market split of a stock's rise | About 25% fundamentals, 25% group, 50% market action | Another passage: half of buyers attracted by cyclical market movement | 193, 197 |
| Cheap test | Price about equal to low at last 4.25-year trough and cycle ready to start up | - | 226 |
| High test | Price about equal to high at last peak and cycle peaking | - | 226 |
| Pullback tolerance | Stock may retrace up to 66% of a thrust (thrust 5 points, recoil 3 points) and still likely to make new highs unless the limit is violated | - | 233 |
| Holding period after 78-week trough | About six months (Southern Pacific example) | 78-week up-swing about nine months | 205, 218 |
| Base odds | Mathematical odds of profit "only 50-50", improvable by buying at a cyclical low, good fundamentals and technical pattern | - | 226 |
| Stock-vs-cycle check | Compare the stock's turns to the 221-, 78-, 25-week and 5-week cycles at troughs | Stocks with minimal response (Commonwealth Edison) vs high response (Southern Pacific) | 202-205 |
| Reported result, 10 Dow stocks (Table 6.1) | Average gain from the 1962 low to cycle highs 167% (1964), 204% (1968), 240% (1972-73); retraced to 59% gain at 1966 lows and 64% at 1970 lows (selected stocks, hindsight) | Table's AVERAGE row OCR shows 167, 59, 204, 212; text says 240 | 208, 209 |
| Reported result, 10 volatile stocks (Table 6.2) | Average gain 159% in the Jul 1970 to early 1971 swing and 120% in the Nov 1971 to 1972 swing of the 78-week cycle; buy-at-high/sell-at-low would have lost 45% (Bangor Punta) and 48% (Global Marine) | Gilbert Flexi-Van about 400% and Gulf & Western 296% on both swings combined | 210, 211 |
| Reported result, Control Data | About $30 to $165 in the first year after the 1966 trough; 1970 low $30 to about $85 (+180%) then back to $32 | - | 211, 213 |
| Reported result, Natomas | $10 (1966 low) to $21, $42, spike to $130 in 1969, $15 (1970 low) to $100 mid-1971, then $50 | - | 213 |

**Key quotes**

- "buy stocks at a trough and sell at a peak" [p. 193]
- "the best cyclical results are obtained from buying" [p. 193]
- "about 25% of a stock's upward movement is due to" [p. 193]
- "if a stock fails to respond to a short cycle, its performance is suspect" [p. 206]
- "SX was a good buy for holding periods of about six months" [p. 205]
- "if a stock is selling at a price about equal to its low at the last trough" [p. 226]
- "a stock may decline as much as 66% from a high" [p. 233]
- "The best move, in our opinion, is to track its movement with the short cycles" [p. 215]
- "the mathematical odds of turning a profit from a stock are only 50-50" [p. 226]

**Pseudocode**

```
# per stock, per day:
cyc_state[c] = phase of market TORQUE cycle c from 2.1 (trough/rising/peak/falling)
resp[stock, c] = fraction of the last K market troughs of cycle c at which the stock
                 made its own local low within +/- W days   # ASSUMPTION definition
eligible = (fundamental screen OK) and resp[stock, 78wk] >= r_min and resp[stock, 25wk] >= r_min
BUY at close when market consensus_trough (2.1) and eligible and
     close <= low_at_last_221wk_trough * (1 + x)            # "cheap" test, x ASSUMPTION 10%
SELL when 78wk/25wk TORQUE near ceiling and turning down (lead the peak)
     or stock retraces > 66% of its last thrust            # technician's rule
     or purchase 'goes against you' with market cycles up -> exit at once (loss cut)
hold ~ 6 months for 78wk trough buys
```

**Ambiguities & assumptions**

- "Responsive" is never quantified; only observed from charts [p. 203-p. 205, p. 206]. ASSUMPTION: use correlation of stock returns to the market TORQUE-cycle changes, or the hit-rate defined above.
- The "cheap/high" tests are qualitative. ASSUMPTION: within 10% of the previous trough low (cheap) or 10% of the previous peak (high).
- Fundamental screening is mentioned but no criteria are given ("good earning situation"); the Table 6.1 stocks were chosen in hindsight and the author admits avoiding stocks that did poorly [p. 209]; Table 6.2 stocks are called "selected volatile stocks" [p. 210]. ASSUMPTION: use only price/volume rules in a backtest; fundamentals are forward-test only.
- The loss-cut rule gives no percentage. ASSUMPTION: exit if the stock closes below the entry-day low or X% (e.g., 8%) below entry; tune.
- The book's selling and short-selling comments (for example "shorting a weak stock at a long-cycle peak is much more rewarding" [p. 230]) are not usable in the Indian cash market.

### 2.5 Seasonal volume/price calendar filter

Codeability: Partly (the average monthly percentages are given; thresholds and rules are not).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Seasonal / calendar filter overlay on the cycle method | 110-114 |
| Timeframe & holding period | Monthly pattern; relation to the 25-week cycle and to the six-month tax holding period | 114 |
| Universe / eligibility filters | Market average (DJI price, NYSE volume, 1898-1966; four 17-year cycles) | 110 |
| Market / regime filter | Pattern differs by 17-year period (summer rally disappeared after 1932); seasonal volume low shifts between February/July/August | 112-114 |
| Setup conditions | Volume lows in February and July-August; volume weak and prices weak in February-March, May-June (June-July) and September-October; October volume rises while prices fall | 110-112, 188 |
| Entry trigger & order type | Not found as a rule. Implied: do not expect strong buying power in volume-poor months; market lows have clustered in June and October (1949 Jun, 1953 Sep, 1957 Oct, 1962 Jun, 1966 Oct). | 112, 188 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| January volume index (68-year average, 100 = monthly average) | 106.89 (sum of four 17-year cycle percentages 100.40, 106.12, 107.96, 113.08, as the text presents them) | - | 110 |
| February volume index | 98.7 (low month) | August also a low | 110 |
| Monthly price index | January 100.41, peak April 101.38; low October with secondary trough July | - | 110, 111 |
| Weak periods | February-March, May-June, September-October | June-July falling on decreasing volume; September-October falling on increasing volume | 112, 188 |
| Price June to July (1949-66 period) | 102.34% to 96.28% of average | - | 114 |
| Volume seasonal minus 25-week cycle | Cycle extends February-March to July-August and again to February-March; tax investors wait nine months to get the full 25-week cycle | - | 114 |
| Weekly volume chart (5-year average = 100) | Lows early February/late March, July, late August-early September | - | 186-187 |

**Key quotes**

- "From the chart, we find that January is a high-volume month" [p. 110]
- "June-July represents a market falling because of decreasing volume" [p. 112]
- "there is a reason for weakness in the market in February-March, May-June and again in September-October" [p. 188]
- "find that the sixth month of their" [p. 114]

**Pseudocode**

```
month_vol_index[m] = mean over years(monthly_volume[m] / mean_monthly_volume_of_year) * 100
month_price_index[m] = mean over years(monthly_avg_price[m] / mean_monthly_price_of_year) * 100
filter: reduce long exposure in months where both indexes < 100 (Feb, Jul, Aug, Oct)  # ASSUMPTION
```

**Ambiguities & assumptions**

- The book gives the pattern but no trading rule. ASSUMPTION: test as a binary month filter on the 2.1 signal and as a pure calendar anomaly on Indian data (NSE has different holidays, March fiscal year-end, Diwali, tax dates), re-estimating month indexes rather than importing the US ones.
- Text numbers: the January 106.89 figure is the "sum of the percentages" of four cycles as stated; the text states 100.40, 106.12, 107.96 and 113.08 which average about 106.89 (the sum would be about 427.56). ASSUMPTION: it is the mean.

### 2.6 Expanding-triangle thrust projection

Codeability: Partly (pattern identification needs a rule; the projection rule is simple).

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Price-pattern breakout projection (technical overlay) | 44, 66 |
| Timeframe & holding period | Weekly swings of the Dow; triangle of five revolutions of the short cycles | 44 |
| Universe / eligibility filters | Market average (examples 1929, 1959-61) | 47, 66 |
| Market / regime filter | Occurs near cycle peaks; "expanding top" connotation | 66 |
| Setup conditions | Expanding triangle: higher peaks and lower troughs for five revolutions of the short cycles | 44 |
| Entry trigger & order type | Not found as a rule. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Target: the final thrust (rally) from the triangular base is expected to be about twice as long as the final leg of the triangle | 44, 66 |
| Exits: trailing / time / signal | Failure triangle after the thrust marks the cycle peak | 66 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Thrust multiple | Final thrust about 2x the final downward leg | "often enough" and "nearly always" in two passages | 44, 66 |
| 1960 example | Final downward leg about 100 points, predicted thrust fell short by 22 points; rally ran 178 points from 564 to 742 | - | 44 |
| 1929 example | Thrust carried 86 points, "more than twice" the final 34-point leg | - | 47 |
| 1960-61 example | Triangle concluding in last quarter of 1960 thrust prices from about 570 to about 700 | - | 66 |

**Key quotes**

- "which will often enough be twice as long as the final leg of the triangle" [p. 44]
- "from which a thrust nearly always doubles the final leg" [p. 66]

**Pseudocode**

```
detect 5 consecutive swing points with peaks rising and troughs falling (expanding triangle)
final_leg = |last_swing_high - last_swing_low|
target = last_swing_low + 2 * final_leg
```

**Ambiguities & assumptions**

- Both examples fall short of or exceed "twice" (178 vs about 200 predicted; 86 vs 68) so the multiple is approximate. ASSUMPTION: treat 2x as a target with a +/-25% band.
- Swing definition is not given. ASSUMPTION: use fractal/zig-zag with the 10-week cycle length.

## 3. Risk & money-management rules

- No position sizing, risk-per-trade, drawdown or exposure rules are found in this text.
- Cut a losing purchase quickly: "Write off the loss as quickly and cheaply as possible" if a stock bought when cycles turn up goes against you [p. 194].
- "we must be prepared to reverse our course promptly if expectations fail to fulfill" and a mistake in a cyclical market is "generally incorrectable, except at great cost" [p. 164, p. 163].
- Sell near, and slightly ahead of, cyclical peaks rather than wait for the exact top [p. 195].
- Watch stocks closely when the short cycles recoil from their peaks, since some stocks will decline while the market cycle is still up [p. 233].
- Stocks that depart from the cycles are dangerous to capital; trade them only for short-cycle gains [p. 215].
- The odds on any purchase are 50-50 unless improved by the cycle, fundamentals and technical pattern [p. 226].
- Hold a stock moving your way, but be alert for the day it reverts to cyclical influence [p. 226].
- Buy-and-hold is described as an approach suited to the 1949-66 uptrend and inadequate for flat or declining markets [p. 162].

## 4. Non-codable guidance

- Investing as a business: do not hold losers hoping to get even; selling is a decision that must be made without attachment [p. 64-p. 65, p. 194].
- Ego and emotion: without cycle knowledge, hope (greed) and fear run 180 degrees off-course, causing buying at tops and selling at bottoms [p. 207].
- Three required skills: prompt independent judgement, mastering cycle forecasting, recognising seeds of cyclical change [p. 163].
- Forecasting is an art needing judgement about asymptotes and cycle breakdowns [p. 176]; cycles must be learned by doing [p. 234].
- Cycles can break into shorter harmonic pieces in a poor outlook, so the longer cycle can seem to vanish [p. 37].
- Combine cycles with fundamentals and technicals; maximum price movement comes from favorable fundamentals and favorable cycles together, and cycles win in the long run [p. 197-p. 198].
- Randoms (news shocks) matter only if trend-changing; the cyclical field absorbs them [p. 104-p. 107].
- Elliott Wave counts are overlaid on cycles for interpretation [p. 233-p. 234]; gold-price multipliers and inflation commentary are macro opinion [p. 195-p. 197].
- Theoretical framework (Fibonacci additive 0.118, phi, thrust/recoil geometry, magnetic field and epicycle analogies, Great Pyramid) is explanatory rather than operational [p. 76-p. 89].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily OHLC and volume for all ~3,700 stocks (to compute daily advances/declines vs prior close and total traded shares), an index proxy with daily high/low/close (NIFTYBEES OHLCV, or an equal-weight index built from the panel; for the Dow-style "travel" the book sums each stock's high and low separately [p. 124], so build index_high = mean of stock highs, index_low = mean of stock lows). Optional: delivery % (recent years only) as an alternative to the buy/sell volume split.
- **Testability with our data:** The TORQUE indicator (2.1), extrusion (2.2) and seasonal calendar (2.5) can be computed and backtested for 2005-2026 (about 21 years, i.e. about 5 repetitions of a 4.25-year cycle and 13 of the 78-week cycle: thin for the longest cycle). The 221-week and 78-week lengths are US/DJI-derived and need re-estimation on NSE. Stock-level selection (2.4) can be backtested only on price/volume rules; fundamental filters can be forward-tested only (snapshots from Feb 2026). The chart-reading judgements ("approaching an asymptote", "consensus of cycles") need rule definitions that the book does not supply.
- **Market-structure differences:** (1) No overnight shorting in cash: skip the short side (for example the book's short at a long-cycle peak [p. 230]) and go to cash or NIFTYBEES instead. (2) Advances/declines on NSE include illiquid small caps and stocks hitting circuit limits that may remain unchanged or move in locked days; ASSUMPTION: count only stocks above a liquidity floor (for example median daily traded value above a threshold) and treat locked limit days as normal advances/declines. (3) 0.1% slippage, STT and brokerage hurt the short 2-week/5-week cycle trades; ASSUMPTION: trade only the 25-week, 78-week and 221-week cycles after costs. (4) The TORQUE ratio is scale-free so NYSE-count constants (3300, 1300-5300) must be re-estimated for NSE universe size. (5) Index high/low by summing stock highs and lows over-states range relative to a true index high/low; the book acknowledges the Dow's calculated high and low are "calculated prices" [p. 122]. (6) Trading calendar (different holidays and trading days per year): holidays are filled by the interpolation rule [p. 136]. (7) Seasonal pattern of volume (US February/August lows, tax-holding six months) will not carry over; the Indian fiscal year ends March and Diwali clusters in Oct/Nov, so estimate from NSE.

## 6. Verdict

- **Codeability:** Partly: the TORQUE indicator (advance/decline ratio over volume buy/sell ratio on cycle-radius moving totals) is fully specified and computable, but the buy/sell decisions rest on chart judgement (asymptotes, consensus of cycles, stock "response") and no entry/exit/stop/size rules or backtests are given.
- **Priority for backtesting:** Medium: the indicator is cheap to compute from our panel and the cycle-radius, volume-split and A/D-over-volume construction is a distinctive breadth-volume oscillator worth testing, but there is no author-reported edge beyond hand-picked charts.
- **Top 3 things a coder is most likely to get wrong** when implementing this book's method:
  1. Using centered or wrong-length moving totals: totals must be end-formed and equal HALF the cycle length (5, 25, 65 days, 39 weeks, 104 weeks), not the full cycle length (which measures trend, not amplitude) [p. 131, p. 135, p. 137].
  2. Mis-splitting volume: buying volume is total volume x upward travel / (upward + downward travel) using the index's high-low travel against the prior close, not up-tick or up-day volume, and the final TORQUE is the A/D ratio divided by the buy/sell ratio, not either alone [p. 122, p. 124, p. 135].
  3. Treating asymptotes and cycle lengths as fixed constants: the book says asymptotes are historical and change with trend (95-105 vs up to 112), and cycle timing resets at each synchronized trough, so hard-coded 221/78/25-week schedules from 1949 would drift [p. 175, p. 161, p. 176].
