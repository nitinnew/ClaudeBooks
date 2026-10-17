# 212° The Complete Trader — Rohan Mehta

- **Source file:** Google Drive "the complete trader.pdf" (179 pages). Published by Notion Press, Chennai, 2017 (first published 2017, copyright Rohan Mehta 2017) [p. 4]
- **Text file used:** text/mehta_complete_trader.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage.
  - Quotes were checked with `verify_citations.py` (see Coverage / end of run).
- **Coverage:** Read the entire text file, lines 1-5021, sequentially in 7 chunks; last marker reached is [[PAGE 179]] (About the Author). Pages 1-3, 72, 145, 155 have no text (cover/image pages). Pages 39, 60, 64, 86, 97, 117, 138 are near-empty (carry-over of "Accountable Person / Notes" lines or a single line). Nothing was skimmed. Several figures are images and therefore absent from the text layer: the trade sheet (p. 37-38), the Gold martingale back-test table (p. 101-102), the business-vs-trading comparison table (p. 157), the 10 heads of Ravana (p. 146), the gratitude diary (p. 120), the tongue-taming chart (p. 126), the flesh-vs-spirit chart (p. 129), and the EPW flow chart (p. 163). Rules that would only appear in those images are therefore "not found in this text". *Coordinator check: the coordinator re-ran verify_citations (49/49 ok) and an exact-page strict check (0 off-by-one), and confirmed all eight field tables have exactly the 12 template rows. 13 unquoted citations were spot-checked by grep and page read: 75 EMA / 200 DMA phases p.79-82, 21% trail p.95-96, previous-month-low Happy Loss and 50 EMA / 200 SMA close rules p.74, stop-and-reverse '365 Days' p.107, 12 trades a year p.111, 30-40% win rate p.105, 20% win rate and +565/-565 example p.52-53, PAT test p.91, martingale p.100-102, round-number 'decimal' breakout p.169, 999-day rule p.139, Notion Press p.4; all matched.*

## 1. The method in brief

This is overwhelmingly a mindset and discipline book for Indian traders (29 chapters). The author states plainly that it is not a system book: he says readers should not expect a "Holy Grail Trading System" or "My Personal Trading/Investing Systems" [p. 14] and "I am not going to give anyone a readymade trading system here" [p. 105]. The claimed edge is the trend-following asymmetry of "limited loss, unlimited profit": decide the loss (the "Happy Loss" stop) before entry, set no profit target, trail the stop, ride winners, accept a low win rate (he gives 20% [p. 52] and 30-40% [p. 105]), trade both long and short, and add to winners (pyramiding) while using a martingale-style size increase after losing trades [p. 99-102]. He describes himself as a medium- to long-term, end-of-day trader who does not want more than 4 trades a month [p. 28], who watches the market only about 30 minutes a day [p. 105], and who has built roughly 500 systems and runs 5 [p. 106]. He works with only two technical tools, moving averages and "swing" [p. 84] and two investing tools, profit after tax (PAT) and growth [p. 84].

The concrete, testable material is thin and concentrated in chapters 12-19 and 27: (a) a Bull/Bear/Pig phase classifier from the 75-day EMA and 200-day moving average vs. close [p. 79-82]; (b) "Formula No. 21", a 21% trailing exit from the highest price with a re-entry rule [p. 94-96]; (c) three simple entry examples (fresh 10-year high with the previous month's low as stop; close above/below the 50 EMA or 200 SMA; crossing a round-number price level) [p. 74, 169]; (d) an investment thesis with a handful of numeric checks (PAT highest in 5 years; price above the 200 DMA on daily, weekly and monthly charts) [p. 91]; (e) pyramiding and martingale position sizing [p. 99-102]; (f) system-acceptance rules (back-test at least 5 years or 3 cycles, "Turtle Score" = annual ROI% / max drawdown%) [p. 107, 110-111]. There is no complete mechanical system, no stop-distance rule except "previous month's low" and the 21% trail, and no risk-per-trade percentage.

Evidence presented is anecdotal: a 10-trade Nifty futures illustration of the two kinds of trader (+565 / -565 points, mirror-image numbers, not a real back-test) [p. 52-53]; a Gold martingale back-test shown only as a summary (total points 0, profit Rs 10,00,000) [p. 101-102]; and individual trades (Aurobindo Pharma 186 to ~1000 [p. 41], Biocon pyramided 500/800/985/1074 [p. 100], Jet Airways long near its 52-week high [p. 68], a real-estate stock shorted at 11 and covered near 8 [p. 68], a long S&P 500 from 2000 with a 1800 stop that reached 2300 [p. 115-116]). No CAGR, drawdown, win-rate or sample-size statistics for any rule are given. He reports a survey of 10,072 accounts of which 95% were in losses [p. 65].

## 2. Strategies

Only items with enough numbers to code are listed. Items in the book that are named but not defined (the "Swing" tool, the "5 Technical Queries" run daily, the "Turtle trading systems", the Gold stop-and-reverse signals) are listed as "not found in this book" in the relevant Ambiguities sections.

### 2.1 Bull / Bear / Pig phase classifier (75 EMA vs 200 DMA)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-state / regime classifier (trend-following filter). The book gives it as a state definition, not as a stand-alone entry system | 79 |
| Timeframe & holding period | Daily data; "Medium-term to Long-Term Time Frame or Horizon"; applies to index, stock, commodity or currency | 79 |
| Universe / eligibility filters | Any index, stock, commodity or currency; no liquidity or price filter stated | 79 |
| Market / regime filter | This is the regime itself: Bull = close above both averages and 75 EMA above 200 DMA; Bear = the mirror image; Pig = close between the two averages (see Parameters) | 79, 81, 82 |
| Setup conditions | Bull: 75 EMA and 200 DMA both below the close, and 75 EMA higher than 200 DMA. Bear: both above the close and 75 EMA lower than 200 DMA. Pig: one average above the close and the other below it, stock in a range with no major breakout | 79, 81, 82 |
| Entry trigger & order type | Not found in this text. The book does not say to buy on a Bull signal or short on a Bear signal; it only says to avoid fighting a Pig-phase stock until it enters Bull or Bear | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Phase change is the implied signal (Bull to Pig/Bear for longs). Reliance example: moved from Pig to Bull | 82, 83 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text. A larger gap between 75 EMA and 200 DMA means a stronger Bull phase | 80 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. Pig phase is described as a good time for option writers | 82 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fast average | 75-day EMA of close | none | 79 |
| Slow average | 200-day moving average ("DMA"; type not stated, "Daily Moving Average") | none | 79 |
| Bull test | close > 75 EMA and close > 200 DMA and 75 EMA > 200 DMA | none | 79 |
| Bear test | close < 75 EMA and close < 200 DMA and 75 EMA < 200 DMA | none | 81 |
| Pig test | exactly one of the two averages is above the close, and "in range, no major breakout" | range not defined | 82 |
| Strength measure | gap between 75 EMA and 200 DMA, bigger gap is a stronger Bull | no threshold | 80 |
| Worked example, Bull | Nifty on 21.2.2017: 75 EMA 8488, 200 DMA 8413, close 8907 | none | 79 |
| Worked example, Bear | Dow Jones, 12 Sep 2008: 75 EMA 11675, 200 DMA 12295, close 11421 | Dow later fell to 7882 | 81 |
| Worked example, Pig | ACC: 75 EMA 1418, 200 DMA 1508, close 1438 | none | 82 |
| Fundamental overlay | the same moving-average logic can be applied to PAT and Sales charts | no numbers | 85 |

**Key quotes**

- "When 75 EMA (Exponential Moving Average) and 200 (Daily Moving Average) are Positive below the close price" [p. 79]
- "When 75 EMA Value is higher than 200 DMA" [p. 79]
- "The bigger is the gap between 75 EMA and 200 DMA, the Stronger is the Bull Phase." [p. 80]
- "When 75 EMA Value is lesser than 200 DMA" [p. 81]
- "either one of the them – 75 or 200 remains positive or negative in comparison to closing price, and also the stock is in range, and no major breakout is found" [p. 82]
- "it is better not to fight with the stock till it enters the bear or bull phase" [p. 82]

**Pseudocode**

```
# daily bars, adjusted close C
ema75  = EMA(C, 75)
ma200  = SMA(C, 200)          # ASSUMPTION: simple MA
if C > ema75 and C > ma200 and ema75 > ma200: phase = BULL
elif C < ema75 and C < ma200 and ema75 < ma200: phase = BEAR
elif (C > ema75) != (C > ma200): phase = PIG
else: phase = PIG             # residual states, ASSUMPTION (see below)
strength = (ema75 - ma200) / ma200      # bigger => stronger Bull / Bear
# use: allow long entries only when phase == BULL; flat otherwise
```

**Ambiguities & assumptions**

- The three definitions do not cover every state: close above both averages while 75 EMA is below 200 DMA (and the reverse). ASSUMPTION: classify these residual states as Pig (no confirmed trend).
- The "in range, no major breakout" clause of Pig is not defined numerically. ASSUMPTION: ignore it and use only the two-average test.
- 200 "DMA" is not stated to be simple or exponential. ASSUMPTION: simple MA (the book uses "200 Days Simple Moving Average" on p. 74).
- The book gives no trade rule for Bull or Bear. ASSUMPTION: use the classifier only as a regime filter (long only in Bull for the NSE cash market).
- Whether EMA/DMA are computed on close is implied ("below the close price"). ASSUMPTION: close, evaluated at the daily close and acted on at the next open.

### 2.2 Formula No. 21 (21% trailing exit from the highest price, with re-entry)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trailing-stop exit plus re-entry rule for trend-following positions in stocks (positional / long-term) | 94, 95 |
| Timeframe & holding period | Daily charts by default; weekly or monthly charts for a less aggressive decision maker. Holding period is "till the time I make Profit from it" | 95, 96 |
| Universe / eligibility filters | Not found in this text. Examples of stocks that rarely broke the 21% zone: Dabur, HDFC Bank, Asian Paints, Pidilite | 96 |
| Market / regime filter | Not found in this text. Remark: in a bull phase some profit is given up; in a bear market the portfolio goes to cash | 96 |
| Setup conditions | A stock already bought (entry method is outside the formula). The rule is inactive until price is 21% above the purchase price (121 for a 100 purchase); before that the Happy Loss is the exit | 95 |
| Entry trigger & order type | Not found for the first entry. Re-entry: after exit, buy again when the stock closes above its previous highest price (191 in the example) on the daily chart | 95 |
| Initial stop-loss | The Happy Loss (pre-decided loss); the book's sample is a 3% risk (buy 100, stop 97). The formula itself gives no initial stop distance | 36, 95 |
| Exits: profit-taking | No profit target ("we don't have an upside Target") | 94 |
| Exits: trailing / time / signal | Once price is above entry +21%, exit when the stock closes below 21% under its highest price (example: high 191, exit if close below 150). Position then sits in cash or goes to new opportunities | 95 |
| Position sizing | Not found in this text for this formula (see 2.7 and section 3) | - |
| Adding to / pyramiding | Re-entry at a higher price after a stop-out is allowed ("notional loss"); pyramiding on breakouts is covered in 2.7 | 95, 99 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. Author's odds: of 10 stocks, 8 exit; of those 6 fall or stay flat and 2 need costlier re-entry | 95, 96 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trail percentage | 21% below the highest price | none | 95 |
| Activation threshold | price must exceed entry x 1.21 before the trail applies | none | 95 |
| Exit test | close below the trail level (a close, not an intraday touch) | none | 95 |
| Re-entry trigger | daily close above the previous highest price | none | 95 |
| Chart timeframe | daily | weekly or monthly as a less aggressive option | 95, 96 |
| Worked example | buy 100, run to 191, exit if close below 150, re-buy on close above 191 | 150 is not exactly 0.79 x 191 (= 150.9) | 95 |
| Author's back-test advice | test on own investment decisions of the last 10 years | none | 96 |
| Biocon use | bought at 500; re-entered at 800, 985 and 1074 on new breakouts; average stop at 800 per Formula 21 | none | 100 |

**Key quotes**

- "Above 121, whatever level the stock goes, from the highest price, when it breaches below 21% and closes below that price, it is the time to exit in the stock." [p. 95]
- "again when it closes above 191 on Daily Charts, we will again re-enter with the same theory of 21% again" [p. 95]
- "we don’t have an upside Target" [p. 94]
- "If you are not very aggressive decision maker, you can apply this same formula on Weekly or Monthly Charts as well." [p. 96]
- "Before executing this Formula, back test it on your personal decision of Investments from last 10 Years." [p. 96]

**Pseudocode**

```
# long position, daily bars
E  = entry price
HH = E                       # highest price since entry
stop_init = E * (1 - R)      # R = Happy Loss %, ASSUMPTION 0.03..0.10 (book example 3%)
state = IN
each day t (after close):
  HH = max(HH, close_t)      # ASSUMPTION: highest close
  if state == IN:
     trail_on = HH >= 1.21 * E
     stop = HH * 0.79 if trail_on else stop_init
     if close_t < stop: sell next open; HIGH_EXIT = HH; state = OUT
  elif state == OUT:
     if close_t > HIGH_EXIT: buy next open; E = fill; HH = fill; state = IN
```

**Ambiguities & assumptions**

- Only exit and re-entry are defined; the initial entry is not. ASSUMPTION: pair it with the entries in 2.3-2.5 or 2.6.
- The 21% is measured "from the highest price", but whether highest close or intraday high is not stated; the exit is on a close. ASSUMPTION: highest close.
- 191 down 21% is 150.9; the book writes 150. ASSUMPTION: use multiplier 0.79.
- After re-entry, "the same theory of 21% again" is not spelled out. ASSUMPTION: treat it as a fresh position (initial Happy Loss, trail activates only after +21% above the new entry).
- The Aurobindo trade exited near 1000 after a high of 1100 under the "system trailing happy loss" [p. 41], which is a much tighter trail (about 9%) than 21%. The book does not reconcile this. ASSUMPTION: use 21% as the only defined number; test 10-30% as sensitivity.
- Initial Happy Loss size is not given beyond the 3% sample. ASSUMPTION: use the previous month's low (from 2.3) or a fixed 8-10% stop; flag as free parameter.

### 2.3 All-time-high breakout (long) and all-time-low breakdown (short) with Happy Loss at previous month's low

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout / trend-following (long and short) | 68, 74 |
| Timeframe & holding period | Position held until the trend changes; no profit booking. Medium to long term | 75 |
| Universe / eligibility filters | Not found in this text for this rule. Author says "No Stock is too cheap to Short & No Stock is too expensive to buy" and measures in percentage terms | 169 |
| Market / regime filter | Not found in this text for this rule | - |
| Setup conditions | A fresh all-time high "done after at least 10 years" (longer is better); for shorts, stocks near the all-time low. Related examples: Jet Airways bought "at nearly 52 Week high"; a real-estate stock shorted on a negative breakout at 11 | 68, 74 |
| Entry trigger & order type | Breakout above the all-time high (long) or below the low (short). Order type not stated | 68, 74 |
| Initial stop-loss | Happy Loss = previous month's low (stated for the long case) | 74 |
| Exits: profit-taking | None; "Profit booking is for Amateurs; riding Profits is for Professionals" | 75 |
| Exits: trailing / time / signal | Exit when the trend changes or the (trailing) Happy Loss is hit. The real-estate short was covered near 8 (about 40%) as a trend reversal. Trailing method: Formula No. 21 (2.2) is the author's tool, but Aurobindo shows a tighter trail | 68, 75, 41 |
| Position sizing | Quantity set from the pre-decided risk (see section 3) | 38 |
| Adding to / pyramiding | Add at every new breakout level (see 2.7) | 99 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| High lookback | all-time high, at least 10 years old | 52-week high used in the Jet Airways example | 74, 68 |
| Initial stop | previous month's low | none | 74 |
| Back-test period for such rules | 10 years in any country | none | 68 |
| Short mirror | stock near its all-time low, negative breakout | no number | 68 |
| Jet Airways example | bought near 52-week high; first profitable quarter after 7 loss quarters | none | 68 |
| Real estate short | short from 11, exit near 8 | none | 68 |

**Key quotes**

- "All-time fresh high, that is done after at least 10 years – the longer the years, the better is the breakout, while keeping the Happy Loss as the previous month’s low" [p. 74]
- "and short stocks which are near its all- time low, one will make much more profit than doing vice verse." [p. 68]
- "I had seen a very good breakout in the stock and I bought Jet Airways at nearly 52 Week high" [p. 68]
- "212°: The Complete Trader doesn’t book profits till the time the trend changes" [p. 75]
- "Please note: Do the proper back testing before executing the system, considering your risk appetite." [p. 74]

**Pseudocode**

```
# daily bars; long side
hh10 = highest(high, 2520) shifted by 1 day     # ASSUMPTION: 10 years ~ 2520 sessions
if close > hh10 and history >= 2520 sessions and phase == BULL (optional):
    buy next open
    prev_month_low = lowest low of the previous calendar month at entry
    stop = prev_month_low         # fixed at entry; ASSUMPTION: then manage with 2.2
# short side mirror (research only in NSE cash): close < lowest(low, 2520)
#   stop = previous month's high  (ASSUMPTION)
```

**Ambiguities & assumptions**

- "All-time fresh high that is done after at least 10 years" could mean (a) the stock has not made a higher high for at least 10 years, or (b) the new high exceeds every price in the last 10 years. ASSUMPTION: (b) with a 10-year lookback; also run the 52-week and 3-year versions as sensitivity because 10-year highs are rare.
- Previous month's low is relative to the entry date (previous calendar month). The stop distance can be very large or tiny; no cap is given. ASSUMPTION: skip trades where stop distance exceeds 25% of entry price.
- Exit is not defined beyond the stop and "until the trend changes". ASSUMPTION: apply Formula No. 21 trail (2.2) after the initial stop.
- Whether breakout is by close or intraday high is not stated. ASSUMPTION: close above the prior 10-year high, buy next open.
- No market regime filter is stated. ASSUMPTION: optionally combine with 2.1 Bull phase.

### 2.4 Close above/below 50-day EMA or 200-day SMA (trend-following, stop-and-reverse)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following moving-average cross of price (stop-and-reverse, always in the market) | 74, 107 |
| Timeframe & holding period | End-of-day closes; positions are held around the year ("365 days"); author's own positional systems average about 12 trades a year | 107, 111 |
| Universe / eligibility filters | Not found in this text. The author trades index, commodities, ATM options and 7 cyclical equity sectors | 73 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Close above (long) or below (short) the 50-day EMA; or, as a separate rule, close above/below the 200-day SMA. A stock closing below the 200 DMA is called Negative | 74, 85 |
| Entry trigger & order type | The close crossing the average. Order type not stated; the author sets orders before the market opens | 74, 105 |
| Initial stop-loss | The reverse crossing is the Happy Loss (stop and reverse). No separate distance given | 107 |
| Exits: profit-taking | None; keep the Happy Loss in place and do not book profits while the market rises | 105 |
| Exits: trailing / time / signal | Exit and reverse when close crosses to the other side of the average | 105, 107 |
| Position sizing | Not found in this text for this rule (see 2.8 and section 3) | - |
| Adding to / pyramiding | Not found in this text for this rule (see 2.7 and 2.8) | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Rule A average | 50-day EMA of close | none | 74 |
| Rule B average | 200-day SMA of close | none | 74 |
| Direction | long above, short below ("closing above or below") | none | 74 |
| Back-test requirement | at least 5 years, covering bull, bear and sideways cycles | 3 recent cycles | 107, 109 |
| Position state | always long or short ("stop and reverse") | none | 107 |

**Key quotes**

- "Closing above or below 50 days Exponential Moving Average" [p. 74]
- "Closing above or below 200 Days Simple Moving Average" [p. 74]
- "the trading system should hold a stop and reverse thought process" [p. 107]
- "If the Market is going up – you Buy and still if it rises, you resist yourself from booking the profits and just keep the happy loss in place." [p. 105]

**Pseudocode**

```
# per instrument, daily close C
for avg in [EMA(C,50), SMA(C,200)]:        # two separate variants
    if C > avg and position != LONG:  go LONG at next open  (close any short)
    if C < avg and position != SHORT: go SHORT at next open (close any long)
# NSE cash adaptation: long-only; if C < avg go to cash
```

**Ambiguities & assumptions**

- The book calls these "very simple type of trading strategies, to begin with" [p. 74] and gives no filter against whipsaws. The author's own "Whipsaw Song" remark [p. 63] shows he expects whipsaws. ASSUMPTION: test raw, then with a 2% closing buffer as sensitivity.
- It is not stated whether the two rules are combined. ASSUMPTION: treat as two independent variants.
- Position size, risk per trade and instrument selection are not stated for this rule.
- Stop-and-reverse is defined for index and commodity-type trading; it needs shorting, which is not available overnight in NSE cash.

### 2.5 Round-number ("new decimal") breakout

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout (psychological price level) | 169 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Any stock; price level is measured in percentage terms (example: short a single-digit stock for 30%, long a Rs 30,000 stock for 60%) | 169 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Stock crosses a new power-of-ten price (10, 100, 1,000 or 10,000) for the first time (long), or breaks the first decimal (short) | 169 |
| Entry trigger & order type | The cross itself; order type not stated | 169 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Levels | 10, 100, 1,000, 10,000 | none | 169 |
| Direction | long on first cross above; short on break of the first decimal | "first decimal" not defined | 169 |
| Reported outcomes | shorted single-digit stock earned 30%; long a Rs 30,000 stock earned 60% | anecdotal | 169 |

**Key quotes**

- "if the stock crosses the a new decimal for the first time, i.e., 10, 100, 1,000 or 10,000, it’s the best time to long that stock" [p. 169]
- "It’s all about percentage" [p. 169]

**Pseudocode**

```
for L in [10, 100, 1000, 10000]:
    if prev_close < L <= close and max(high over all prior history) < L:   # first time ever
        long signal (buy next open)
# short side: "breaks the 1st decimal" is undefined -> ASSUMPTION: close below L after trading above it
```

**Ambiguities & assumptions**

- "First time" could mean first time ever or first time in the data window. ASSUMPTION: first time in adjusted history available (2005 onward), and for split-adjusted data the level must be tested on unadjusted prices, because adjusted prices distort round numbers.
- "Breaks the 1st decimal" is ambiguous. ASSUMPTION: a close below the power-of-ten level after the stock had been above it.
- Stops and exits are not specified. ASSUMPTION: use Formula No. 21 (2.2) with initial stop at previous month's low (2.3).

### 2.6 212° Investment Thesis (growth investing; PAT screen plus 200 DMA)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Growth investing with a technical trend check (fundamental-led, long-term) | 87, 91 |
| Timeframe & holding period | Long-term; exit by thesis or Formula No. 21. "Best holding period" is till the profit stops | 99, 96 |
| Universe / eligibility filters | Brands and must-use products; market leaders (Maruti share 49% to 45% as an example); companies in the Value Inflow stage. Never invest if the company does not pay salaries on time | 87, 88, 89, 91 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Numeric checks after the qualitative steps: last year's PAT is the highest in the past 5 years; the stock is above its 200 DMA on daily, weekly and monthly charts (all three). Extras: reserves exceeding market cap with zero debt is the icing; debt-to-equity is generally not a big concern | 91, 92 |
| Entry trigger & order type | Not found in this text (no price trigger given beyond the checks above) | - |
| Initial stop-loss | A Happy Loss must be decided before entry; the thesis checklist asks for at least 5 exit points. No number | 38, 92 |
| Exits: profit-taking | Time to Book Profits or review more at Value Stagnation; exit at Value Outflow | 91 |
| Exits: trailing / time / signal | Sell at once if management breaks integrity; sell as per the thesis; Formula No. 21 for trailing | 92, 99 |
| Position sizing | Not found in this text. Highest position should be in the investment with the highest returns | 99 |
| Adding to / pyramiding | Add as the company's profit grows (Maruti: PAT 1600 Cr to 2392 Cr, more positions as profits came) | 99, 100 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. Wealth bucket splits across 3 asset classes: equity, real estate, debt (no percentages) | 166, 167 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Profit after tax test | last year PAT is the highest in the past 5 years | none | 91 |
| Trend test | above 200 DMA on daily, weekly and monthly (all) | none | 91 |
| Cash/debt test | reserves above market cap with zero debt (bonus only) | not required | 92 |
| Debt/equity | not a big concern | none | 92 |
| Stage of company | enter at Value Inflow; review at Value Stagnation; exit at Value Outflow | no numeric tests | 91 |
| Thesis write-up | at most 500 words; 6 steps checked; pyramid plan; at least 5 exit points | none | 92 |
| Qualitative pillars | employees/dealers, creditors, customers, management lifestyle | not testable | 88, 89, 90 |
| Welspun India | 9 times in 2 years; sold immediately on integrity breach | anecdotal | 88, 92 |

**Key quotes**

- "Annual Profit after Tax is the data which I prioritize during the fundamental review." [p. 87]
- "The last year’s PAT should be at its highest in the past 5 years" [p. 91]
- "It should be technically above its 200 DMA Daily/ Weekly & Monthly all" [p. 91]
- "if the management does anything which breaks the Integrity, I will sell the stocks immediately" [p. 92]
- "Debt to equity is generally not a big concern to me" [p. 92]

**Pseudocode**

```
# forward-test only (point-in-time fundamentals needed)
eligible = stocks where
   PAT_FY_latest == max(PAT of last 5 fiscal years)           # PAT >0
   and close > SMA(close_daily,200)
   and close_weekly > SMA(close_weekly,200)                  # ASSUMPTION: 200 periods
   and close_monthly > SMA(close_monthly,200)               # needs ~16 years history
rank by PAT growth (YoY)   # ASSUMPTION; ranking not given
buy; manage exit with 2.2 (Formula No. 21)
```

**Ambiguities & assumptions**

- "200 DMA Daily/Weekly & Monthly all" may mean a 200-period average on each timeframe or the daily 200-DMA drawn on weekly and monthly charts. ASSUMPTION: 200-period average on each timeframe; a 200-month average needs about 16.7 years of data, so very few stocks qualify. Fallback: use 40-week and 10-month equivalents (200 trading days), flagged as non-book.
- Growth is the "biggest indicator" [p. 87] but no growth threshold is given. "Not found in this book."
- Value Inflow/Stagnation/Outflow stages have no numeric tests. "Not found in this book."
- The qualitative pillars (employee/dealer feedback, creditor integrity, customer satisfaction, promoter lifestyle) cannot be coded.
- PAT history needed for "highest in 5 years" is not available point-in-time before 2026 in our data.

### 2.7 Pyramiding in profits (add at every breakout level)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position-sizing / scaling overlay for winning trend trades (long or short) | 99 |
| Timeframe & holding period | Same as the underlying trend system; stocks held through 200-300% gains | 100 |
| Universe / eligibility filters | Any trade or investment that is working | 99 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Position is favourable (in profit); price makes new breakout levels; on the investment side, the company's profit grows | 99 |
| Entry trigger & order type | Add at each new breakout level; Biocon adds at 800, 985, 1074 after the first buy at 500 | 99, 100 |
| Initial stop-loss | Underlying system's Happy Loss; Biocon average stop at 800 per Formula No. 21 | 100 |
| Exits: profit-taking | Trading side: Formula No. 21 or the system's Happy Loss; investment side: sell as per thesis | 99 |
| Exits: trailing / time / signal | As above | 99 |
| Position sizing | Start with a smaller position because the outcome is unknown; the highest position should be in the investment with the highest returns. Size of each add not stated | 99 |
| Adding to / pyramiding | Add at every breakout level; also pyramid when the stock is 200-300% up | 99, 100 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Initial size | smaller than final ("lesser position") | no fraction | 99 |
| Add trigger | each new breakout level | no definition of level | 99 |
| Add size | not found in this book | none | - |
| Biocon sequence | 500, 800, 985, 1074 | none | 100 |
| Maruti sequence | PAT 1600 Cr then 2392 Cr; positions added as profit rose | none | 100 |
| Stage pyramiding is still done | even at 200-300% gains | none | 100 |

**Key quotes**

- "As Averaging in losses is a SIN, averaging in profits is a Virtue." [p. 99]
- "it’s better to take lesser position at the initial phase" [p. 99]
- "starts becoming favorable, add up at every breakout levels" [p. 99]
- "your highest position should be in the Trade or Investment which has the highest returns" [p. 99]

**Pseudocode**

```
size0 = fraction f0 of target size                      # ASSUMPTION f0 = 0.5
on each new N-day high after entry (N is not in the book; ASSUMPTION N = 63 sessions):
    if position in profit and adds_done < max_adds:
        add size0 * 0.5 (ASSUMPTION)
stop = Formula No. 21 trail on whole position (2.2)
```

**Ambiguities & assumptions**

- "Breakout level" is never defined. ASSUMPTION: a close above the highest close of the previous 63 sessions, at least 10% above the previous add price.
- Add size and number of adds are not given. ASSUMPTION: each add is half of the initial size, maximum 4 adds.
- Total risk after adds is not discussed. ASSUMPTION: cap total position at 3x the initial size and keep portfolio heat under the limit chosen in section 3.

### 2.8 Martingale (+1) position sizing for trend-following systems

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Position-sizing overlay (anti-martingale reversed: size up after losers) for trend-following, high-frequency of trades | 100, 101, 102 |
| Timeframe & holding period | Any trend-following system; shown on Gold (Indian price) as a long-short stop-and-reverse system | 101 |
| Universe / eligibility filters | Systems with "Bigger Profits and Smaller Losses"; futures-style contracts (Gold 1 kg lots, Bank Nifty) | 100, 101, 102 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Previous trade was a loss or break-even | 101 |
| Entry trigger & order type | Whatever the underlying system signals | 101 |
| Initial stop-loss | Underlying system's stop | 101 |
| Exits: profit-taking | Underlying system | 101 |
| Exits: trailing / time / signal | After a winning (big) trade return to the base quantity | 101 |
| Position sizing | Base quantity of 1 unit; add 1 more unit after each losing or break-even trade; reset to base after a winner. Cap example: maximum 1500 Bank Nifty with a base of 400 | 101, 102 |
| Adding to / pyramiding | Not applicable (size changes between trades, not within) | - |
| Portfolio limits (max positions, correlation, heat) | Upper limit of contracts for high-frequency systems; one needs Cash, Courage and Conviction | 102 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Increment | +1 contract after each non-winning trade | none | 101 |
| Reset | back to base after a winning trade | none | 101 |
| Base quantity | 1 contract (Gold); 400 (Bank Nifty) | none | 101, 102 |
| Cap | 1500 (Bank Nifty, with base 400) | none | 102 |
| Gold example sequence | trade 1 BE (1 lot), trade 2 loss (2), trade 3 profit (3), trade 4 back to 1, trade 6 two lots, trade 7 three lots, trade 10 six lots, big trade of 3000 points | contradictory about trade 5, see below | 101 |
| Reported result | total points earned 0 but profit of Rs 10,00,000 (equal-size: no profit) | single example | 102 |

**Key quotes**

- "One must add up positions in +1 format during every loss position." [p. 101]
- "If the position is exited with no Profit and Loss, still one has to add up" [p. 101]
- "After that bigger trade, one must again come to the basic positions." [p. 101]
- "I had decided that I will trade maximum 1500 BANK NIFTY, with a base quantity of 400" [p. 102]
- "The total points earned is 0 but we made a profit of 10,00,000 rupees." [p. 102]

**Pseudocode**

```
n_lose = 0
base = B ; cap = CAP
for each trade i (system signals direction):
    qty = min(base * (1 + n_lose), cap)
    execute trade with qty
    if pnl_i > 0:  n_lose = 0
    else:          n_lose += 1          # losses and break-evens both count
```

**Ambiguities & assumptions**

- The Gold example says the 5th trade was a profit ("in 5th trade, we did the base quantity as in 4th trade, we did profits") and then says the 6th trade used 2 contracts "as 5th was in loss" [p. 101]. The two statements contradict each other. ASSUMPTION: the rule is +1 after any non-winning trade; reset after a win.
- The "3000 points, i.e., 10,000" payoff and the Rs 10,00,000 total are given without a table (the table is an image). Not reproducible from the text.
- Whether the cap resets or the system halts at the cap is not stated. ASSUMPTION: stay at the cap until a win.
- This conflicts with the money-management lesson "Never increase or decrease positions just because last trade/Month/Year went profitable" [p. 102] only partly: that lesson refers to profits, while the martingale refers to losses. The book also asks the trader to have Cash, Courage and Conviction to continue after losses [p. 102].
- Risk of ruin on long losing streaks is not discussed. ASSUMPTION: test with cap = 4x base in the NSE adaptation.
- Chapter 28 repeats that Martingale in trend following is a "Holy Grail" [p. 174]; the claim is not backed by statistics.

## 3. Risk & money-management rules

| Rule | Detail | Page |
|---|---|---|
| Decide the loss first | Fix the stop (Happy Loss) before entry; trade-sheet fields include conviction, risk level, entry price, exit price, quantity, risk % on trade, total exposure | 37, 38 |
| Quantity from risk | Quantity is in proportion to the pre-decided risk, not to greed or fear. No fixed risk-per-trade percentage is given: not found in this book (sample trade shows 3% price risk: buy 100, stop 97) | 36, 38 |
| No profit target; trail the stop | Limited loss, unlimited profit; trail stops at every level; Formula No. 21 for the 21% trail | 51, 95, 106 |
| Never average a loser | Rakesh Jhunjhunwala quoted: never ever average. Turtle Wealth will not trade or invest in constantly falling prices. (Conflict: the trader/investor table says investors may average if pre-planned, p. 22) | 67, 22 |
| Pyramid winners | Add at every breakout level, smaller initial position | 99 |
| Martingale after losers | +1 unit after each non-winning trade, reset after a win, cap quantity | 101, 102 |
| Leverage: defensive | Zero leverage (Nifty 1000 units at 8000 requires Rs 80,00,000 capital) | 75 |
| Leverage: moderate | 1x to 3x leverage, capital 30-50% of contract size | 75, 76 |
| Leverage: maximum | 1:5 maximum for any trader; no leverage on equities | 76 |
| Author's own leverage | Moderate risk/reward, leverage 1:3 on positional systems with 2-3 trades a month | 106 |
| Three lanes | Attacking (stocks, commodities, midcaps, smallcaps, calculated leverage), moderate (index, commodities, large caps, midcaps, zero leverage), sideline (cash, bonds, FD); shift gears as opportunities change | 98 |
| Add on drawdown | "When to add up? When does a system hit a drawdown of 15%?" is posed as the question; no rule given | 76 |
| Stop a system | Give each system 999 days; then review if the system or market is at fault; Nickel was dropped after 3 years | 76, 77, 139 |
| Trial discipline | Same size (e.g., 1 contract) for the entire 999 days | 139 |
| Cash reserve | 6 months of expenses in bank or liquid FD; at least 1 Million in bank savings (wife's rule; currency not stated); many investors hold 20% cash | 102, 114 |
| Insurance | Enough life, health, office, home insurance | 102 |
| Diversification | Trade stocks, index, commodities; invest in midcap and small cap; wealth in equity, real estate, debt | 102, 166, 167 |
| Do not bet small on a proven system | Betting small on a confident system is a sin; the example invests only 3-5% in a system giving 20-30% a year | 149, 174 |
| Truck-load | When odds are all in favour, load positions heavily | 115 |
| Number of trades | Author prefers no more than 4 trades per month, 2-3 per month, about 12 per year (trend following) and about 24 per year (Turtle systems); avoids systems with 350-400 trades a year because of costs | 28, 106, 111 |
| Watch time | Check the market twice a day (open and close), 30 minutes maximum; decide stops and exposure before the market opens | 105, 153 |
| Weekly black-swan review | Every Monday 11:30, 45 minutes: where will we die, what if market falls 10% tomorrow | 171 |
| EPW model | Expenses (short-term, high leverage, covers monthly costs), Profits (medium to long term, calculated leverage), Wealth (long term, no leverage, three asset classes). No percentages | 164-167 |
| System acceptance | Back-test at least 5 years (or 3 cycles: bull, bear, sideways); drawdown measured from equity peak; Turtle Score = annual ROI% / maximum drawdown% above 1 for index and above 2 for stocks | 107, 110, 111 |
| Costs | Brokerage, taxes, impact cost, trade-mistake cost and emotional cost rise with trade count | 111 |
| Taxation (2017 context) | Long-term gains exempt from tax, short-term taxed | 160 |
| Choose a strict broker | A costlier broker who enforces risk management is preferred to a cheap one | 70, 71 |

**Key quotes**

- "Decide the Loss First before executing the Trade." [p. 37]
- "Let your risk measures decide the quantity rather than influence the money management with the emotional elements such as greed or fear" [p. 38]
- "As a rule in the market, I will never ever average." [p. 67]
- "1:5 is the maximum leverage that is recommended to any trader" [p. 76]
- "If the Turtle Score is above 1 in the index and above 2 in stocks, it indicates that it is a decent system" [p. 111]
- "Turtle Score = Annual R0I%/Maximum Drawdown%" [p. 111]
- "I generally believe one should have a time frame of minimum 5 years or 3 cycles" [p. 110]

## 4. Non-codable guidance

- Mindset: stop predicting ("I Don't Know" manifesto) [p. 43, 44]; price is the only truth [p. 43]; do the disliked thing first (Cold Water Shower) [p. 19].
- Flesh versus Spirit: flesh books early profits, avoids the Happy Loss and oversizes; spirit follows the system. Aurobindo Pharma case [p. 40, 41].
- Four monkeys: do not hear, watch, say or think bad; stop watching ticks and TV channels; affirmations [p. 55-59].
- The seven questions before any trade (what, when to buy, when to exit, when to book profit, how much, when to scale up, when to stop) are a planning checklist [p. 73-77].
- Discipline is claimed to be about 85-90% of the result and strategy 10-15% [p. 29, 30]; 98% self-rated discipline [p. 135].
- Nine discipline commandments: 999-day rule, trade like a beggar, journaling (including debiting losses first), delegation of a mechanical system to an executor, avoid quick-rich claims, disciplined life, trading buddy, goal card [p. 139-144].
- Delegation: the author delegated execution to a colleague who stops him if he overleverages [p. 141].
- Spiritual chapters (meditation at 4 am, gratitude letters, God as partner, serenity) [p. 118-132]; Ravana's ten qualities [p. 146-150].
- Daily schedule: exercise, 135 minutes of reading, 45-minute research block, review 500 charts, journal, 7 hours sleep [p. 152-154].
- Traderpreneur benefits including being able to short [p. 156-161]; short-side bias claims such as "95% are biased to do only long" [p. 69].
- 6 reasons for losses: early profits and late losses, averaging, buying low and selling high, no knowledge, long-only bias, low commission [p. 65-71].
- KIDS (Keep, Improve, Develop, Stop) self-review exercise [p. 176, 177].
- Compounding: 15% for 30 years is about 6500% rather than 450% [p. 171].
- Predictions in the book about specific stocks and markets are illustrations, and the author says they are not recommendations [p. 83, 88].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily adjusted OHLC (close, high, low) per stock, volume for a liquidity filter; for 2.6: annual PAT (profit after tax) history and optionally reserves, market cap and debt; for the phase classifier, the stock's own prices (index series via NIFTYBEES or an equal-weight index from the stock panel before 2024). Unadjusted prices are needed for the round-number rule (2.5). Delivery % is not needed by any rule in this book.
- **Testability with our data:**
  - Backtestable on 2005-2026 prices: 2.1 phase classifier (as a filter or on the index), 2.2 Formula No. 21 (once an entry is chosen), 2.3 all-time/10-year breakouts (needs at least 10 years of history, so signals start about 2015 for the 2005 start; a 3-year or 52-week version can start earlier), 2.4 moving-average crosses, 2.5 round-number breakouts, 2.7 pyramiding and 2.8 martingale overlays (as simulated sizing rules), plus Turtle Score as an evaluation metric.
  - Forward-test only: 2.6 investment thesis (PAT highest in 5 years needs point-in-time PAT history; our fundamentals start Feb 2026, growth fields from May 2026).
  - Not testable or not defined: qualitative thesis pillars (employees, dealers, creditors, customers, promoter lifestyle), "swing" tool, "5 Technical Queries", Gold stop-and-reverse signals, "Turtle trading systems", any option strategy (no options data).
- **Market-structure differences:**
  - Shorting. The book insists on trading both sides [p. 48, 69-70] but the NSE cash market has no overnight shorting. ASSUMPTION: implement long-only and treat Bear or below-average states as cash; evaluate short signals only as a separate research exercise (symmetric rules) or with futures if futures data ever become available.
  - Execution. The author trades EOD and sets orders before the open [p. 105]. ASSUMPTION: signals on the close, orders at next open, with 0.1% slippage plus STT and brokerage; apply circuit-limit awareness (a stop may not fill on a lower-circuit day; assume the exit occurs at the next available open).
  - Liquidity. The author likes cyclical, liquid assets for trading and consumption stocks for investing [p. 73]. ASSUMPTION: apply a minimum average traded value filter (for example Rs 1 crore daily) and exclude stocks under Rs 10 to avoid illiquid penny stocks, noting that the single-digit rule (2.5) conflicts with this filter.
  - Breakouts of 10-year highs are rare. ASSUMPTION: run 52-week, 3-year and 10-year variants; report the 10-year as the book version.
  - Martingale sizing (2.8) with futures-style contracts does not map directly to cash equities. ASSUMPTION: express size as multiples of a base rupee amount, with the cap at 4x base.
  - Survivorship: our data include delisted stocks, which matters for Formula No. 21 because the 21% trail will often exit before delisting; the oath not to trade constantly falling prices [p. 67] is consistent with this.
  - Taxes: the 2017 statements on long-term capital gains exemption [p. 160] are outdated; use current NSE tax rates.

## 6. Verdict

- **Codeability:** Partly. Only the Bull/Bear/Pig classifier, the Formula No. 21 exit and the martingale sizing are defined well enough to implement without guessing; the entries are sketches, there is no stock selection or ranking rule, no risk-per-trade percentage, and the fundamentals can only be forward-tested.
- **Priority for backtesting:** Medium. The ideas are generic trend-following (moving-average regime, 10-year highs, 21% trailing exit) and the book gives no performance statistics, but the 21% trail with re-entry and the phase filter are cheap to test on our data and are explicit enough to compare against standard variants.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating this as a complete system: Formula No. 21 is an exit-only rule and the phase classifier has no entry; any entry (10-year high, 50 EMA, round number) must be chosen and flagged as an assumption, and the 21% must be measured from the highest close with the +21% activation threshold, not from the entry price.
  2. The phase definitions leave residual states (close above both averages but 75 EMA below 200 DMA, and the reverse) undefined, and the Pig test mixes "one average above, one below the close" with an undefined "range" clause; also confusing the 75 EMA with the 200 simple average, or computing them on unadjusted prices.
  3. Applying the long-and-short stop-and-reverse and the martingale (+1 after every loss or break-even) literally on NSE cash equities: no overnight short, no cap by default, and no per-trade risk limit, which can produce ruin-sized positions in a losing streak; also contradictions across the book (20% vs 30-40% win rate, averaging forbidden vs allowed for investors, 2-3 trades a month vs always-in-market) must be resolved explicitly.
