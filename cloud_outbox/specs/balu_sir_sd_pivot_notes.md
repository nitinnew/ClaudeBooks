# Balu Sir course notes: "Standard deviation for beginners" webinar + "Centric Research Value" pivot note — Balu Sir (Balasubramanian, "PROFESS team")

- **Source file:** Google Drive invest/: "SD balu Sir 10 apr 22.pdf" (webinar slide deck) + "pivot balu sir.pdf" (note "MARCH - MANTHANA DT 31.03.2022") + "pivot.xlsx" (monthly Nifty table)
- **Text file used:** text/balu_sir_sd_pivot_notes.txt  (page basis: slides for the SD deck; pdf_pages for the pivot note; the text file concatenates three files with continuous page numbering)
  - `[p. 1]`-`[p. 50]` = the SD webinar slide deck (PDF)
  - `[p. 51]`-`[p. 53]` = the pivot / Centric Research Value (CRV) note (PDF)
  - `[p. 54]` = pivot.xlsx, rendered as a text table by the coordinator (monthly Nifty OHLC Feb 2021-Mar 2022 with monthly pivot, 3-month pivot average "CRV", TR and 3-month average TR)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (not the printed slide number, which equals the marker for the deck anyway)
- **Coverage:** Read lines 1-599 of the text file in full (the entire file), last marker reached `[[PAGE 54]]`. Pages with NO extractable text (slide images; their content is unrecoverable from text): 7, 21, 24, 25, 31, 32, 36-46 and 53. Many of these are almost certainly chart screenshots showing the Bollinger / VWAP / SD applications (pages 21-25, 31-32, 36-46) so the actual trade examples and any entry/exit rules shown on charts are NOT in this spec. Nothing with text was skipped. The author is named only as "Balu Sir"; the pivot note was "prepared by Ms.Nanda, Dr. Trupti and Mr. Prashant Konduru and verified by Balasubramanian" [p. 52]. Reading done by a Sonnet sub-agent. The coordinator built the combined text (pivot.xlsx was read through the Drive connector's text rendering because its download came back compressed inline), re-ran the verifier and an exact-page check, spot-checked 10 table citations (pp. 17, 22, 34, 51, 52) and re-did the p. 54 arithmetic (Dec 2021 TR 17640-16410 = 1230, sheet shows 1229; Oct 2021 TR 1151, sheet shows 1152; Mar 2022 pivot 16898.67).

## 1. The method in brief

Two small course handouts from an Indian (NSE, Nifty) intraday / short-term trading community. The first (SD webinar, 10 Apr 2022) is a beginner explanation of standard deviation (SD) as a measure of volatility, then applies it to Bollinger Bands (20 SMA +/- 2 SD), to "VWAP bands with SD lines" on a 15-minute chart as intraday support and resistance, and to the options-market 1-SD expected-move formula [p. 4, 19, 28-30, 34]. The core idea is mean reversion: "Any unusual price rise will try to revert to mean" [p. 6]. The deck gives definitions and formulas but almost no entry, stop or exit rules in extractable text; the chart pages that probably showed the setups are images (p. 21-25, 36-46).

The second handout (31.03.2022) introduces the "Centric Research Value" (CRV): the monthly pivot (High+Low+Close)/3, and the average of three consecutive monthly pivots, used as a monthly "fulcrum" / magnet level for Nifty and as a macro reference for positions [p. 51, 52]. The authors explicitly say CRV is "in experimental stage" and must not be used for day-to-day entries, exits or stop-losses [p. 52]. Evidence is a single worked example (Jan-Mar 2022 pivots average 17113, "will be visited by NIFTY in the month of APRIL in all probability") [p. 52] and a 14-month Nifty table [p. 54]. No back-test, win rate or track record is presented anywhere. The author states the intended trading is "intraday and very short term" with strategies from other webinars that are not part of this text [p. 52].

## 2. Strategies

Only loosely defined, level-based setups can be extracted. All are weak on entry/stop/exit rules; the ASSUMPTION lines carry the burden of making them testable.

### 2.1 Bollinger Band (20,2) mean reversion toward the middle band

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion (volatility-band based) | 6, 8, 22 |
| Timeframe & holding period | "Bollinger Bands are used on all timeframes, such as daily, hourly or five-minute charts." Holding period not stated | 19 |
| Universe / eligibility filters | Not found in this text (examples cited are Nifty-type index levels p. 20, and stocks contrasted by volatility p. 5) | 5, 20 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Middle band = 20 SMA; Upper = 20SMA + 2 x SD of price; Lower = 20SMA - 2 x SD of price. Slide titles: "Price reaction up from LBB towards MBB & down from MBB within the bounds of SD" and "Price reaction within the tube form of BB and during expansion" (chart content not in text) | 19, 22, 23 |
| Entry trigger & order type | Not found in this text. Implied by slide title: long when price reacts up from lower band toward the middle band | 22 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Implied target is the middle band (20 MA) ("towards MBB"); not stated as a rule | 6, 22 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| SMA period (middle band) | 20 | "often 20, but is adjusted to suit various trading styles"; 10 and 30 compared and rejected | 17, 19 |
| SD multiplier | 2 (denoted "(20,2)") | Bands drawn at 1 SD, 2 SD and 3 SD; "typically set at 2.0" | 14, 19 |
| SD definition | Sample SD (divide by N-1) | worked example: 10,8,10,8,8,4 gives 2.19 | 13 |
| Timeframes | Any | daily, hourly, five-minute | 19 |
| Band width interpretation | Higher SD multiplier: price reaches band less often | lower multiplier: easier to "breakout" | 19 |

**Key quotes**
- "Any unusual price rise will try to revert to mean" [p. 6]
- "Upper Band = 20SMA + ( standard deviation of price x 2)" [p. 19]
- "Lower Band = 20SMA - ( standard deviation of price x 2)" [p. 19]
- "The sma used for MBB is customarily 20 period sma." [p. 18]
- "reversion to mean value plays a role" [p. 8]
- "99.7% of the data is clustered around mean within the 3rd SD" [p. 14]
- "majority of price activity follows the pattern of" [p. 15]

**Pseudocode** (assumed; the deck gives only the indicator and the reversion idea)
```
# inputs: close series C (and H, L for intraday), N = 20, K = 2
mid   = SMA(C, N)
sd    = STDEV_SAMPLE(C, N)          # divide by N-1 [p. 13]
upper = mid + K*sd
lower = mid - K*sd
# long reversion setup (ASSUMPTION)
if C[t-1] <= lower[t-1] and C[t] > C[t-1]:    # touched/closed below lower band then turned up
    BUY at open[t+1]
    target = mid                                # "towards MBB"
    stop   = lowest low since signal           # ASSUMPTION, not in text
    exit when C >= mid or after M bars (time stop, ASSUMPTION M = 10)
# short side: only via futures/intraday MIS in India; mirror with upper band
```

**Ambiguities & assumptions**
- Entry trigger not defined (touch, close outside, or re-entry of the band). ASSUMPTION: signal bar closes below the lower band, enter next open when a bar closes above its prior close.
- No stop-loss rule. ASSUMPTION: stop at the signal-bar low (or 1 SD below the lower band); also exit if close < lower band for 3 consecutive bars (band "walk", the p. 23 title mentions expansion but gives no rule).
- Target: "towards MBB" only. ASSUMPTION: exit at the 20 SMA.
- Slide p. 20 example is internally inconsistent: 20 MA with "SD of 3.83%", "938.9 points(2 SD)", UBB 13194 implies mid = 12255.1 and LBB 11316.2, but the slide states LBB 11327.61. Treat as chart rounding; formulas p. 19 are authoritative.
- p. 4 says SD, relevant to understanding Bollinger Band, will be taken up along with its utility with VWAP; the actual combined rules were presumably on image pages 36-46 and are not recoverable.
- Page 26 mentions a Pine script "courtesy by Shri Madhav Sir" shared on request only; not in text.
- Regime: p. 23 title says "tube form of BB and during expansion" (squeeze vs expansion) but the text gives no rule. ASSUMPTION: skip reversion trades when band width (upper-lower)/mid is above its 120-bar 80th percentile (expansion).

### 2.2 Pull-back entry at the 20 MA (middle Bollinger band) in an up-move

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback (buy support at 20 MA) | 17 |
| Timeframe & holding period | Not stated (chart-based slide; no timeframe given). Holding period not stated | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Up-move: the middle band is chosen so that "price takes frequently the Support At the Moving Average during upmove" | 17 |
| Setup conditions | Price in an up-move and pulling back (correcting) toward the 20 MA | 17 |
| Entry trigger & order type | Enter on pull-back to the 20 MA; entering at the 30 MA means "you enter late" because the correction "falls short of average" | 17 |
| Initial stop-loss | Not found in this text (author notes with 10 MA "price gets penertrates too often. Chance of SL hitting more probable", implying the stop sits beyond the MA) | 17 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| MA period for support | 20 SMA | 10 MA (rejected: price penetrates too often), 30 MA (rejected: pull-back stops short, late entry) | 17 |

**Key quotes**
- "20 MA is more often does that" [p. 17]
- "10 MA : price gets penertrates" [p. 17]
- "30 MA: Here correction falls short of" [p. 17]
- "So in pull back, you enter" [p. 17]

**Pseudocode** (assumed)
```
trend_up = C > SMA(C, 50) and SMA(C,20) > SMA(C,20)[5]      # ASSUMPTION for "up-move"
if trend_up and L[t] <= SMA(C,20)[t] and C[t] > SMA(C,20)[t]:
    BUY at open[t+1]
    stop = min(L[t], L[t-1]) - 0.5*ATR(14)
    exit: close < SMA(C,20) for 2 bars, or trailing below 20 SMA
```

**Ambiguities & assumptions**
- Defines the best MA length only qualitatively (charts on p. 17 compare 10, 20, 30 MA). No numerical test.
- Up-move definition, stop, target all missing. ASSUMPTIONs as in the pseudocode (marked there).
- "Support" is the author's claim, not statistically shown.

### 2.3 VWAP bands with SD lines (intraday support and resistance, 15-minute)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday mean-reversion / support-resistance levels | 34 |
| Timeframe & holding period | Intraday, 15-minute ("15 mtf"); position closed within the day (implied, "during intraday") | 34 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Lines plotted: VWAP line, +1/+2/+3 SD and -1/-2/-3 SD from VWAP, plus a 20 MA line. "Range within a day is defined and price confinement within the bounds gives as a clue about S&R" | 34, 35 |
| Entry trigger & order type | Not found in this text (chart slides 36-46 are images) | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Chart timeframe | 15 minute | Not stated otherwise | 34 |
| SD band offsets from VWAP | +/-1, 2, 3 SD | - | 35 |
| Companion MA | 20 MA | - | 34, 35 |

**Key quotes**
- "VWAP BANDS WITH SD" [p. 34]
- "these serve as support and resistance during intraday" [p. 34]
- "Here are some slides showing the use of SD lines along with" [p. 34]
- "One can make use of the understanding of SD in combination with VWAP" [p. 47]

**Pseudocode** (assumed)
```
# per day, from 9:15 IST
vwap_t = cum(sum(typical_price*vol))/cum(sum(vol))
sd_t   = sqrt(cum(sum(vol*(tp-vwap_t)^2))/cum(sum(vol)))     # volume-weighted SD, ASSUMPTION
band(k) = vwap_t + k*sd_t, k in {-3,-2,-1,1,2,3}
# reversion long: price tags band(-2) and next 15m bar closes back above it -> BUY next open,
#   target vwap_t, stop below band(-3). Exit all by 15:15 IST.
```

**Ambiguities & assumptions**
- How SD is computed around VWAP (volume-weighted vs. simple SD of price over N bars; anchored at session open or rolling) is not stated. ASSUMPTION: session-anchored, volume-weighted.
- No entry/stop/target. ASSUMPTION as pseudocode; bands used as S/R only as the author states.
- The role of the 20 MA line relative to VWAP bands (filter or target) is not stated.
- Chart evidence on p. 36-46 is not recoverable.

### 2.4 Monthly pivot as support / resistance / bias level

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Level-based bias and support/resistance (mean-reversion to pivot) | 51 |
| Timeframe & holding period | Monthly pivot (daily and weekly pivots also "customary"); the study focuses on monthly | 51 |
| Universe / eligibility filters | "the underlying( index or stock)"; the worked example is Nifty | 51, 52 |
| Market / regime filter | Price above pivot: bullish; below: bearish | 51 |
| Setup conditions | Pivot = (High + Low + Close)/3 of the candle (monthly) | 51 |
| Entry trigger & order type | Not stated. Watch/plan positions around the level: "Whenever that value is approaching from down to up, we perceive that resistance is going to be offered by that value and vice versa" | 51 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text. Pivot "acts as balance": an over-extended price is expected to return to it | 51 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pivot formula | (H + L + C)/3, open excluded | R1-R3, S1-S3 mentioned but not used | 51 |
| Frequency | Monthly | daily, weekly | 51 |
| Reason for excluding open | static point, influenced by "big hands" | - | 51 |

**Key quotes**
- "Above this derived value, the market is bullish and below" [p. 51]
- "Pivot acts as magnet" [p. 51]
- "Monthly pivot gives a fair idea of the price of the underlying" [p. 51]
- "It is the fulcrum point of the" [p. 51]

**Pseudocode**
```
pivot_m = (H_m + L_m + C_m)/3                # prior completed month
bias[t] = +1 if close[t] > pivot_m else -1    # p. 51
# resistance event: price below pivot and rising to touch it; support event: price above and falling to it
# ASSUMPTION: trade the first touch in the next month:
#   if bias == -1 and high >= pivot_m: SHORT-SIDE signal (cash: exit/avoid long; futures: short)
#   if bias == +1 and low  <= pivot_m: LONG signal; stop = close below pivot_m - 0.5*ATR(14)
```

**Ambiguities & assumptions**
- The note does not say which month's pivot is "live": previous month's (as in standard pivots), or the current in-progress month. ASSUMPTION: the last completed month's pivot, effective from the next trading day.
- No trade rule beyond "resistance/support is offered". ASSUMPTION as pseudocode.
- Authors explicitly warn CRV-family values are not for day-to-day entries/stops [p. 52]; the monthly pivot is similarly a planning level.
- Claim "Pivot acts as magnet" is untested in the text.

### 2.5 Centric Research Value (CRV): 3-month average of monthly pivots as a monthly fulcrum / target

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Level-based mean-reversion / macro bias | 51, 52 |
| Timeframe & holding period | Monthly level, applied to the following month; for "rolled over positions" in futures; study for "intraday and very short term" strategies is separate | 52 |
| Universe / eligibility filters | Index or stock; the example is Nifty | 51, 52 |
| Market / regime filter | Position can ride "so long as this value is not breached" (CRV as bull/bear boundary) | 52 |
| Setup conditions | CRV = average of the monthly pivots of three consecutive months, computed at month end; e.g. Jan 17509, Feb 16931, Mar 16900 gives 51340/3 = 17113 | 51, 52 |
| Entry trigger & order type | Not found in this text. Authors say not to use CRV "to decide your entry" | 52 |
| Initial stop-loss | Not found in this text; authors say not to use CRV for stop loss calculations | 52 |
| Exits: profit-taking | Expectation that Nifty "will be visited" at the CRV level in the next month ("in all probability") | 52 |
| Exits: trailing / time / signal | "If one holds rolled over positions, they can ride on the rise so long as this value is not breached." Adjust positions when price is 400-500 points away from CRV | 52 |
| Position sizing | "we can adjust or positions judiciously" (no formula); CRV is "a sort of budget provision" | 52 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Averaging window | 3 consecutive monthly pivots (quarter, matching company reporting) | Table recomputes every month, rolling | 51, 54 |
| Pivot | (H+L+C)/3 | - | 51 |
| Distance considered large | 400-500 points on Nifty (about 2.3-2.9% of 17464) | - | 52 |
| Evaluation cadence | "MUNCH THIS CONCEPT EVERY MONTH AND CRUNCH THE EXCEL EVERY THREE MONTHS" | - | 52 |

**Key quotes**
- "Centric Research Value(CRV)" [p. 51]
- "17113 - this will be visited by NIFTY in the month of APRIL in all probability." [p. 52]
- "they can ride on the rise so long as this value is not breached." [p. 52]
- "CRV studies are in experimental stage." [p. 52]
- "Don’t use these values to decide your entry," [p. 52]
- "any price fluctuations due to unexpected events and geo" [p. 51]

**Pseudocode**
```
# at last trading day of month m
pivot[m]  = (H[m] + L[m] + C[m]) / 3
CRV[m]    = (pivot[m] + pivot[m-1] + pivot[m-2]) / 3          # p. 51, 52, 54
# testable claims for month m+1 (NIFTYBEES or stock):
visit[m+1]  = (L[m+1] <= CRV[m] <= H[m+1])                     # "will be visited"
bias[t]     = long if close[t] > CRV[m] else flat/avoid        # "so long as this value is not breached"
dist[t]     = close[t] - CRV[m]                                 # flag if |dist| >= 400-500 pts (~2.5%) -> trim / reassess
# ASSUMPTION for a trade: hold a long (cash or futures roll) while close > CRV; exit on first daily close < CRV;
#   trim half when close - CRV > 2.5% (ASSUMPTION converting 400-500 Nifty points)
```

**Ambiguities & assumptions**
- Window ambiguity: the CRV in the sheet row for month m uses pivots of m, m-1, m-2 (verified: e.g. 3/31/2022 17113 = avg of Mar, Feb, Jan) and is meant to be read in month m+1 [p. 52, 54]. ASSUMPTION: apply CRV[m] to month m+1.
- "Visited" is not defined (intraday touch vs close). ASSUMPTION: monthly high-low range includes CRV.
- The note says the 17113 figure is "in the last row" of the Excel, but in the text rendering of pivot.xlsx it is in the first data row (dates descending) [p. 52, 54]. Presentational only.
- The note says "only 400 -500 points deviation is seen at the moment" with CMP 17464 [p. 52], but 17464 - 17113 = 351. Treat the 400-500 figure as approximate.
- No stop-loss or position size rule exists; the authors disclaim using CRV for entries, exits, stops [p. 52]. Any strategy built on it is therefore the coder's construction.
- Sheet arithmetic check (p. 54), formula pivot = (H+L+C)/3, CRV = mean of 3 consecutive monthly pivots, TR = High - Low, 3M TR = mean of 3 TRs:
  - Monthly pivot: matches within 1 point in all 14 rows. Rounding is inconsistent: 3/31/2022 shows 16898 (exact 16898.67, would round to 16899; the note on p. 52 uses 16900); other rows are rounded normally (e.g. 2/28/2022 16930.67 shows 16931).
  - CRV: all 12 values match within 1 point. 2/28/2022 shows 17191 (mean of stated pivots 17191.67, truncated not rounded); 3/31/2022 17113 is consistent (17112.67 from stated pivots).
  - TR (High - Low): 12/31/2021 shows 1229 but 17640 - 16410 = 1230; 10/31/2021 shows 1152 but 18604 - 17453 = 1151. Other 12 rows match exactly.
  - 3-month average TR: 1/31/2022 shows 1390 versus 1390.67 (truncated); all other rows match when rounded.
  - So no material mismatch; only 1-point rounding/truncation inconsistencies and two 1-point TR typos. The formulas in the note are reproduced by the table.
  - Column header "Close*" has an unexplained asterisk. ASSUMPTION: marks the month-end (March 2022 = 17464, equal to the CMP in the note p. 52) close. The Yahoo Finance link cited on p. 54 carries a period2 value that falls before the end of March 2022, so the March row may have been appended manually.
  - The last two CRV cells (Mar and Feb 2021) are blank because three months of history are not available.

### 2.6 Non-codable / reference notes (no trade action stated)

These carry formulas that a coder may want as features but the text states no trading rule for them.

- **Options 1-SD expected move:** "(Stock price) x (Annualized Implied Volatility) x (Square Root of [days to expiration / 365]) = 1 standard deviation" [p. 28]. Worked example: Reliance 2200, IV 28%, 22 days gives "2200x 28% x SQRT (22/365) = 150 Rs", a "68% chance" of 2050-2350 [p. 30]. The author says it "gives a clue how to set up option hedge strategies" [p. 30] but gives no strategy. Needs implied volatility, which is not in our data.
- **Historical volatility:** "Daily volatility(%)= ( (Today’s Price-Yesterday’s Price)/Yesterday’s price))*100" and "Annualised IV = Daily volatility*sqrt(252)" [p. 29]; example "Daily Volatility = 1.264% ... Annual Volatility = 1.264% * SQRT (252) = 20.065%" [p. 33]. Note the slide's daily-volatility line is a daily return, whereas the 1.264% is evidently the SD of daily returns. Also the label "Annualised IV" is really annualised historical volatility.
- **Monthly True Range (TR) as rubber band:** "Range is difference between high and low. We can name it as the true range for monthly high low values", stretched ranges "come to an equilibrium size as decided by Pivot" [p. 51, 52]. Sheet columns TR and 3-month TR average on p. 54. Used "to choose the appropriate strike values" by advanced traders [p. 51]; no rule.
- **ATR(14) rationale on 15-minute chart:** 14 candles of 15 minutes = 3.5 hours, 9:15 to 12:45, "where the confluence at SMA 200 also lies" [p. 52]; given as the reason to take trades on the 15 min timeframe "which sir insists". No setup is given.
- **Volatility comparison:** Stocks like ITC, NTPC, NMDC have little price spread; Maruti, Adani Green, Piramal Ent. fluctuate a lot [p. 5]. Two-class example: both averages 625, SD 14 versus 78 [p. 4]. Two-stock example: both average 7% but the lower-volatility stock ends with more money (Rs. 1,224 vs Rs. 1,213) [p. 10, 11]. The slide shows Company A Year 1 as Rs. 1,100 though 11% on Rs. 1,000 is Rs. 1,110; this is a slide typo and the subsequent values (1,055, 1,213) correspond to 1,110.
- **Normal distribution reference:** 68% / 95% / 99.7% within 1 / 2 / 3 SD [p. 14].

## 3. Risk & money-management rules

- No position-sizing, risk-per-trade, drawdown or exposure rules are given in either document. Not found in this text.
- CRV is "a sort of budget provision": use it as a planning reference, and "Don’t use these values to decide your entry, exit stop loss calculations for day to day trades" [p. 52].
- CRV "provides reasonable reliability to our trading or investment decisions (risk and money management more precisely)" [p. 51] without giving mechanics.
- Positions may be adjusted "judiciously" depending on distance from CRV (400-500 points on Nifty) [p. 52].
- Higher volatility means higher risk and potential return; volatility compounding drag is illustrated on p. 10-11.

## 4. Non-codable guidance

- Mean reversion / equilibrium analogy: high-energy objects shed energy; prices out of bounds return to the mean (nickel example after the Ukraine war) [p. 6, 8].
- Day traders prefer reasonably high volatility; long-term low-risk investors prefer stable prices [p. 9].
- Reason for using HLC and not open in the pivot: the open is influenced by big players; fear and greed show in high, low, close [p. 51].
- Reason for 3-month window: companies report quarterly [p. 51]. Unexpected-event fluctuations are claimed not to affect CRV [p. 51].
- "Unbiased judgement, without being affected by daily movements, gap down and gap ups"; CRV as a macro view "as in the case of an eagle watching from the sky" [p. 52].
- Caution that the algorithms fail ("Street full of surprises") and mentoring is important [p. 48]; discipline / patience / neutrality diagram [p. 49].
- The note says the routine webinar / clubhouse strategies for intraday and very short term are not to be set aside; CRV only supplements them [p. 52]. Those strategies are not in this text.

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily and 15-minute OHLC with volume for stocks and NIFTYBEES (Bollinger, VWAP bands, pivots); intraday volume for VWAP; monthly OHLC aggregation for pivots/CRV; implied volatility and option chains only for the p. 28-30 formula (not available).
- **Testability with our data:** Bollinger (20,2) on daily bars, monthly pivot and CRV (NIFTYBEES monthly bars or equal-weight index, 2005-2026) are fully back-testable on daily data. The VWAP-band strategy needs intraday data; the data context lists only daily NSE OHLCV, so 2.3 is Not testable unless intraday bars are available. The options expected-move formula needs implied volatility (not in our data). No fundamentals are used. The Nifty index series only exists from 2024, so use NIFTYBEES; the author's own table is a single 14-month Nifty sample (p. 54) and is too short to validate CRV.
- **Market-structure differences:**
  - No overnight shorting in cash. ASSUMPTION: test long-only (buy at lower band / pullback / support) and treat short signals only as exit/avoid signals, or as intraday-only if intraday data exist.
  - The author talks about futures roll-over and options strikes [p. 51, 52]; futures/options are not in our data. ASSUMPTION: replicate "ride rolled over positions" with a long NIFTYBEES position held while close > CRV.
  - Costs: apply STT, brokerage and 0.1% slippage; band-reversion trades on 15-minute bars will be heavily cost-sensitive. ASSUMPTION: test on daily bars first.
  - Circuit limits could prevent entries/exits at band extremes in small caps. ASSUMPTION: restrict stock tests to liquid names (e.g. top 500 by turnover).
  - Pivots on individual stocks: the note speaks of "index or stock" [p. 51]; ASSUMPTION: calendar-month OHLC from adjusted daily data.

## 6. Verdict

- **Codeability:** Partly. Indicators (Bollinger bands, VWAP SD bands, monthly pivot, CRV) are precisely defined [p. 19, 51, 52]; no entry, stop, exit or sizing rule is stated, and the chart slides showing trade examples are images.
- **Priority for backtesting:** Low. There are no rules to test beyond indicators and the single claim "price will be visited at CRV next month"; no evidence is presented and the authors call CRV experimental [p. 52]. The cheapest worthwhile test is the monthly "CRV visited" hit rate and the "above CRV bullish" regime filter on NIFTYBEES, which takes minutes to run.
- **Top 3 things a coder is most likely to get wrong:**
  1. Using population SD (divide by N) instead of the sample SD (N-1) stated on p. 13, or using SD of price when the author's VWAP-band SD is unspecified; and misreading p. 29's "daily volatility" (a return) as an SD.
  2. Look-ahead in CRV: the CRV for month m+1 must use pivots of m, m-1, m-2 (complete months) and the monthly bar must be completed before use; also confusing the three-month window (pivot average, not average of highs/lows).
  3. Inventing entry/stop/exit rules and then attributing results to the author; the text explicitly says CRV should not be used for entries, exits or stop-losses [p. 52].
