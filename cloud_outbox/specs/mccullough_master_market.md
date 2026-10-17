# Master the Market — Keith McCullough (Hedgeye; foreword by Mike Taylor)

- **Source file:** Google Drive "Master The Market by Keith McCullough.pdf" (53 pages)
- **Text file used:** text/mccullough_master_market.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python ../work/bin/verify_citations.py specs/mccullough_master_market.md text/mccullough_master_market.txt`.
- **Coverage:** Read lines 1-2042 of the text file (all 53 pages; last marker reached [[PAGE 53]]). Every page had text. The figures are images and are NOT in the text: the four-quadrant GIP diagram (pp. 25-27), the "what we like / don't like in each quadrant" asset-class chart (p. 26), and the ETF vs. hedge-fund AUM chart (pp. 17-18). The per-quadrant asset allocation is therefore not recoverable from this text. Pages 1-6 (praise, contents, foreword), 15/21/29/34/40/47/51 (chapter summaries), 16-20 and 30-31, 35, 41-46, 48-50 (anecdotes, media/conflict stories) were read in full but contain almost no rules (marketing and autobiography). *Coordinator check: the coordinator re-ran verify_citations (34/34 ok) and an exact-page strict check (0 off-by-one), and confirmed the three 2.x field tables have exactly the 12 template rows. 12 unquoted citations were spot-checked by grep and page read (6% stop after MAX and the old -12% p.38, MIN/MAX by asset class p.36, 50-150bps increments p.39, Trade/Trend/Tail 3 weeks / 3 months / 3 years p.33, rate-of-change quads p.24-25/29, Risk Range inputs p.32, Pods p.24, Lower Highs / Higher Lows p.37-38); all matched.*

## 1. The method in brief

The book is a short, promotional primer on Hedgeye's "Full Cycle Investing" process. It says the process combines three things: "Proprietary and quantitative-based risk management signals", top-down macro analysis and bottom-up fundamental research [p. 10]. The author's central claim is that the process is rules-based and repeatable, so the investor can make "high-probability bets" and be "more right than wrong"; it says the best investors expect a success rate of 55-65% [p. 9, p. 11]. The stated priority is to preserve capital (drawdown arithmetic is shown: -20% needs +25%, -50% needs +100%) rather than to maximise short-term return [p. 11]. The time frame is the whole economic cycle, not days or weeks [p. 10]. The process was designed for a "go-anywhere" macro portfolio of US-listed asset classes, ETFs and US single stocks [p. 10, p. 29, p. 34].

There are two quantitative pillars. (1) The GIP (Growth, Inflation, Policy) model classifies a country into one of four "Quads" from the year-over-year rate of change (accelerating or slowing) of growth and of inflation [p. 25, p. 26]. It then picks asset classes by back-tested quad performance [p. 26]. The asset-class chart is an image, so the mapping is not in the text. (2) Risk Range™ Signals use "price, volume and volatility" to produce a dynamic, "probable" buy-low / sell-high range, over Trade (3 weeks or less), Trend (3 months or more) and Tail (3 years or less) durations. They identify breakouts and breakdowns [p. 32, p. 33]. The Risk Range is explicitly proprietary and no formula is given. A third, bottom-up tool ("Pods": rate of change of revenue growth, earnings/cash-flow growth, and free-cash-flow ROIC) is described as the origin of the Quads [p. 24]. Chapter 4 gives the only fully specified trading rules: min/max position sizes by asset class, buy-the-dip conditions, scale-in/scale-out increments and exit rules [p. 36 to p. 39].

Evidence is anecdotal and promotional. The book lists calls made by Hedgeye (85% cash in early 2008, bullish US stocks April 2009, long US stocks 2016, short US stocks October 2018, crash call in early 2020, a -25% crash warning in January 2022) with no statistics, dates of exit, or return numbers [p. 9]. It claims Hedgeye is "consistently 3 to 6 months ahead of Wall Street" [p. 26]. No backtest results are reported. The reader should treat the book as a process outline, not as a complete strategy specification.

## 2. Strategies

### 2.1 GIP Quad regime classifier (Growth / Inflation rate-of-change)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: top-down macro regime classification (asset-allocation tilt by regime) | 25, 26 |
| Timeframe & holding period | Full-cycle (months to years); regime is tracked on a year-over-year rate-of-change basis; the book gives no holding period or rebalance frequency per quad. Hedgeye tracks it daily with predictive algorithms | 10, 25, 27 |
| Universe / eligibility filters | Country level: the US and "the top 50 economies"; asset classes (not single stocks). No other eligibility filter given | 27 |
| Market / regime filter | This IS the regime filter: Quad 1 = growth accelerating, inflation slowing; Quad 2 = growth accelerating, inflation accelerating; Quad 3 = growth slowing, inflation accelerating; Quad 4 = growth slowing, inflation slowing | 26 |
| Setup conditions | Track growth (GDP) and inflation on a year-over-year rate-of-change basis; ask "heating up or cooling down" for each; the pair of answers fixes the Quad. Central bank policy response is the third element (typical response labels: neutral, hawkish, in-a-box, dovish) | 25, 26 |
| Entry trigger & order type | Not found in this text (a change of Quad is the implied trigger to re-tilt allocation, but the author states no order type, timing or threshold). What to own per quad is in an image chart not in the text | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Signal exit: when the data change the Quad (or the likelihood of the outcome you are positioned for), change positioning: "you don't argue with the data" | 9 |
| Position sizing | Not found in this text for quads (see 2.2 and Section 3 for the generic MIN/MAX sizing by asset class) | 36 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Growth measure | GDP, year-over-year rate of change; accelerating vs. slowing | Hedgeye runs "predictive tracking algorithms" (forecasts), not just reported data | 25, 27 |
| Inflation measure | "inflation" (index not named in this text), year-over-year rate of change; accelerating vs. slowing | CPI is not named in this text | 25 |
| Number of regimes | 4 (Quad 1-4) | - | 26 |
| Policy response labels | neutral, hawkish, in-a-box, dovish (one per quad; mapping order not stated explicitly) | - | 26 |
| Asset-class preferences per quad | Not found in this text (image chart on p. 26) | - | 26 |
| Lead over consensus | "3 to 6 months ahead of Wall Street" (claim, not a parameter) | - | 26 |

**Key quotes**
- "Growth accelerating, Inflation slowing (QUAD 1);" [p. 26]
- "Growth slowing, Inflation accelerating (QUAD 3);" [p. 26]
- "We track both on a year-over-year rate of change basis" [p. 25]
- "Are growth and inflation heating up or cooling down?" [p. 25]
- "(neutral, hawkish, in-a-box or dovish)" [p. 26]
- "back-testing of the different asset classes that perform best in each of the four quadrants" [p. 26]
- "Hedgeye is consistently 3 to 6 months ahead of Wall Street." [p. 26]

**Pseudocode** (classifier only; the allocation step is NOT in the text)
```
# inputs: monthly/quarterly series G (real GDP level or growth proxy), P (inflation index)
yoyG[t] = G[t]/G[t-12m] - 1          # year-over-year growth rate
yoyP[t] = P[t]/P[t-12m] - 1          # year-over-year inflation rate
dG[t]   = yoyG[t] - yoyG[t-1]        # ASSUMPTION: "accelerating" = yoy rate higher than previous period
dP[t]   = yoyP[t] - yoyP[t-1]
growth_acc = dG[t] > 0
infl_acc   = dP[t] > 0
if growth_acc and not infl_acc: quad = 1
if growth_acc and infl_acc:     quad = 2
if not growth_acc and infl_acc: quad = 3
if not growth_acc and not infl_acc: quad = 4
# allocation step (book: back-tested asset-class preferences per quad; chart not in text)
# ASSUMPTION: derive empirically: for each quad, compute average forward 1-3 month return of
# each candidate asset (equity index, gold, bond ETF...) and hold the top-ranked ones.
```

**Ambiguities & assumptions**
- Acceleration is defined only verbally ("accelerating", "slowing", "heating up or cooling down") on a "year-over-year rate of change basis" [p. 25]. The book does not say whether "accelerating" means the yoy rate rose versus the prior period, versus the prior year, or versus a forecast. ASSUMPTION: change in yoy rate versus the previous observation (second difference of the level).
- The book states Hedgeye uses forecasting algorithms [p. 27]; the forecasting method is not given. ASSUMPTION: use realised data with publication lag; this will lag Hedgeye's claimed 3 to 6 month lead.
- The inflation series (CPI? PCE? other) and the growth series (GDP only? nowcast?) are not specified beyond "GDP" and "inflation" [p. 25]. ASSUMPTION: headline CPI yoy and real GDP yoy.
- What to own/avoid in each quad is not in the text (image chart, p. 26). Not found in this book; do not import outside material. ASSUMPTION: learn the mapping from the data via a quad-conditional return study.
- Policy ("P" in GIP): the book gives four labels for the typical government response [p. 26] but does not state the mapping order and gives no data rule. ASSUMPTION: ignore Policy as a trading input; use it only as a label.
- Whether the quad is evaluated on a fixed schedule or continuously (Hedgeye tracks "every single day" [p. 44]) is not specified. ASSUMPTION: evaluate monthly when new data print.

### 2.2 Risk Range™ core-position framework (buy the dip at the LRR, scale out on Lower Highs, exit on TRADE+TREND break)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion within a trend (buy low end of a dynamic range when TRADE and TREND are bullish), with trend-following exits | 33, 37, 38 |
| Timeframe & holding period | Multi-duration: Trade = 3 weeks or less; Trend = 3 months or more; Tail = 3 years or less. Core positions are held while TRADE and TREND remain supportive | 33, 39 |
| Universe / eligibility filters | "any asset that ticks" (index, ETF, single stock, commodity, bond; crypto classified as a commodity). Candidate tickers can come from bottom-up fundamental analysts | 32, 33, 36 |
| Market / regime filter | Prefer assets bullish on all three durations (Trade, Trend, Tail): "safer" to buy the dip. Breakdowns (TRADE and TREND support broken) are not bought | 33, 39 |
| Setup conditions | Best dips: (A) Bullish on both TRADE and TREND; (B) Risk Range showing a series of Higher Lows and Higher Highs; (C) ticker nearing the LRR (low end of the Risk Range). Less good: Bullish TRADE and TREND but Higher Lows and Lower Highs in the Risk Range; such positions sit toward the bottom of the long-only allocation | 37 |
| Entry trigger & order type | Buy incrementally when price is near the low end of the Risk Range while A, B, C hold; order type not stated. Buy/sell increments are usually 50-150bps of capital, and size depends on where price is in the range (more at the low end) | 37, 39 |
| Initial stop-loss | Stop-out is "rarely" the exit. Old rule: -12% stop loss. Current rule: 6%, but only AFTER the position has been taken to its MAX size (what 6% is measured on is not stated) | 38 |
| Exits: profit-taking | Sell at the top end of the probable range (Risk Range high). Exit because of "so much money made" is "rarely" the reason | 32, 38 |
| Exits: trailing / time / signal | Signal ladder: (a) Lower-Highs in the Risk Range: start reducing position SIZE; (b) Lower-Highs AND break of immediate-term TRADE support: cut to the MIN position; (c) Lower-Highs, TRADE break, AND break of intermediate-term TREND: out. Recap: break of TRADE and TREND support = out | 38, 39 |
| Position sizing | MIN/MAX % of total capital by asset class: Commodities 1-4%; Equities 2-6%; Fixed Income 3-10%; Single stocks long 1-3%, short 0.5-2%. Actual MIN/MAX set by asset volatility (more volatile = smaller) | 36 |
| Adding to / pyramiding | Add in 50-150bps increments of capital. Add less aggressively when TRADE is breaking down; do NOT buy more if TRADE breaks and a TREND breakdown is implied by the Risk Ranges | 39 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text beyond the per-position MIN/MAX above | 36 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| TRADE duration | 3 weeks or less | - | 33 |
| TREND duration | 3 months or more | - | 33 |
| TAIL duration | 3 years or less | - | 33 |
| Risk Range inputs | price, volume, volatility (index or ticker level) | formula proprietary; ranges update intraday | 32 |
| Commodities MIN/MAX | 1% / 4% | scaled by volatility | 36 |
| Equities MIN/MAX | 2% / 6% | scaled by volatility | 36 |
| Fixed income MIN/MAX | 3% / 10% | scaled by volatility | 36 |
| Single stock long MIN/MAX | 1% / 3% | - | 36 |
| Single stock short MIN/MAX | 0.5% / 2% | - | 36 |
| Buy/sell increment | 50-150bps of capital | smaller adds when TRADE is breaking down | 39 |
| Hard stop | 6% after reaching MAX position | old rule -12% | 38 |
| Expected success rate | 55% to 65% for the world's best investors | - | 11 |

**Key quotes**
- "uses price, volume and volatility at the index or ticker level" [p. 32]
- "Importantly, these ranges move intraday" [p. 32]
- "is a duration of 3 weeks or less" [p. 33]
- "is a duration of 3 months or more" [p. 33]
- "is a duration of 3 years or less" [p. 33]
- "signaling Bullish on both my TRADE and TREND durations" [p. 37]
- "a series of Higher Lows and Higher Highs" [p. 37]
- "When that ticker is nearing the LRR" [p. 37]
- "Those positions fall towards the bottom of my Long Only Asset Allocation." [p. 37]
- "run with a -12% stop loss rule. Now I use 6%" [p. 38]
- "I start to reduce the SIZE of the" [p. 38]
- "breaks immediate-term TRADE support, I take the position" [p. 38]
- "and then breaks intermediate-term TREND" [p. 38]
- "If something breaks TRADE and TREND support" [p. 39]
- "in increments of 50-150bps of my capital" [p. 39]
- "do NOT buy more" [p. 39]

**Pseudocode** (the Risk Range itself is proprietary; the block below uses a clearly marked proxy)
```
# ---- ASSUMPTION PROXY for the proprietary Risk Range (NOT Hedgeye's formula) ----
# The book names only three inputs (price, volume, volatility) and says the range is "probable"
# and dynamic [p. 32]. Proxy below uses daily OHLCV only.
for each stock S, each day t:
    # TRADE range (3 weeks or less -> 15 trading days, ASSUMPTION)
    mid_T  = volume-weighted avg of typical price over last 15 days   # uses volume
    sig_T  = stdev of daily close-to-close change over last 15 days   # volatility
    LRR[t] = mid_T - k*sig_T*sqrt(1)  ; URR[t] = mid_T + k*sig_T      # ASSUMPTION k = 1.5 (not in book)
    # TREND (3 months or more -> 63 trading days, ASSUMPTION)
    trend_bull = close[t] > SMA(close, 63)                            # ASSUMPTION definition of 'bullish TREND'
    trade_bull = close[t] > mid_T                                     # ASSUMPTION definition of 'bullish TRADE'
    # Higher Lows / Higher Highs on the range series (compare to 5 days ago, ASSUMPTION)
    HL = LRR[t] > LRR[t-5] ;  HH = URR[t] > URR[t-5]
    LH = URR[t] < URR[t-5]
    trade_support = LRR[t-1]   # 'TRADE support' = prior day's LRR (ASSUMPTION)
    trend_support = SMA(close, 63)

# ---- ENTRY / ADD ----
if trade_bull and trend_bull and HL and HH and close[t] <= LRR[t] + 0.25*(URR[t]-LRR[t]):  # 'nearing LRR'
    # best dip
    add 0.50%..1.50% of capital (50-150bps) to position, scaled by closeness to LRR,
    capped at MAX_pct[asset_class]; min position on first buy = MIN_pct[asset_class]
elif trade_bull and trend_bull and HL and LH:
    # less good set-up: allowed but rank at the bottom of the long list, smaller increment (50bps)
if trade_breaking_down (close < trade_support): add_size = 0 or at most 50bps ;
if close < trade_support and close < trend_support: do not add

# ---- EXIT ----
if LH:                                         position = reduce size (ASSUMPTION: by 50-150bps per step)
if LH and close < trade_support:               position = MIN_pct
if LH and close < trade_support and close < trend_support: position = 0
if close < trade_support and close < trend_support: position = 0
if position == MAX_pct and close <= entry_avg*(1-0.06): position = 0     # 6% stop (reference ambiguous)
if close >= URR[t]: sell/trim (top end of range)
```

**Ambiguities & assumptions**
- The Risk Range calculation is proprietary; only the inputs (price, volume, volatility) and the properties (probable range, dynamic, moves intraday) are given [p. 32]. Not found in this book: the formula, lookbacks, volume/volatility weights, the number of standard deviations, how TRADE/TREND/TAIL ranges differ. ASSUMPTION: the proxy above, uncalibrated; any backtest result describes the proxy, not Hedgeye.
- The durations are inconsistent in wording: "Trade is 3 weeks or less", "Trend is 3 months or more", "Tail is 3 years or less" [p. 33]. "Or more" for Trend and "or less" for Tail look like opposite directions of the bound. ASSUMPTION: Trade ~15 trading days, Trend ~63 trading days (3 months), Tail ~756 trading days (3 years).
- "Bullish" / "Bearish" TRADE or TREND is never defined numerically; the text speaks of "support" being held or broken [p. 38, p. 39]. ASSUMPTION: bullish = close above the respective proxy level (see pseudocode). Also, "Bullish/Bearish TREND" phase-transition thresholds are mentioned only as "critical thresholds" [p. 33] with no values.
- "High-Highs and Higher-Lows in my Risk Ranges" [p. 39] (also written Higher Lows and Higher Highs on p. 37) refers to successive values of the LRR/URR themselves, not of price. The comparison window is not given. ASSUMPTION: 5 trading days.
- "nearing the LRR" has no distance threshold [p. 37]. ASSUMPTION: lowest quarter of the LRR-to-URR range.
- The 6% stop applies "AFTER I've gone to my MAX position" [p. 38]. It is not stated whether 6% is adverse price move from average cost, or loss on the position, or loss of portfolio capital. ASSUMPTION: 6% adverse move from average cost on that position. Before MAX size is reached there is no stated stop; the process signals are the exit.
- How far to reduce on "Lower-Highs" ("start to reduce the SIZE") is not specified [p. 38]; the text gives only the later steps (MIN, then out). ASSUMPTION: cut by one 100bps increment per signal day.
- Cutting the position to the minimum: MIN is by asset class [p. 36]; for an Indian stock use the single-stock long MIN of 1% [p. 36].
- MIN and MAX are "generalized" and set from volatility [p. 36], but no volatility-scaling formula is given. ASSUMPTION: use the book's table as is, unscaled.
- The sell side (taking profit at the top of the range) is stated as a principle [p. 32, p. 37] but sell increments at the URR are not specified. ASSUMPTION: trim 50-150bps when close >= URR if TRADE/TREND are still bullish; the author says an exit because "you've made so much money" is "rarely" the answer [p. 38].
- Short side: the book gives single-stock short sizes (0.5-2%) [p. 36] but no short-entry rule except the implied mirror (Bearish durations). Not found in this book. ASSUMPTION: long-only for NSE (no overnight cash shorting).

### 2.3 "Pods" bottom-up rate-of-change screen (revenue, earnings/cash flow, capital allocation)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Growth-momentum (fundamental rate-of-change: longs = accelerating, shorts = decelerating) | 24 |
| Timeframe & holding period | Not found in this text (year-over-year rate-of-change evaluation; company models) | 24 |
| Universe / eligibility filters | Individual companies "out of favor with conventional consensus", cash-flow focused (Falconhenge mission statement). No numeric filters | 23 |
| Market / regime filter | Combine with top-down macro overlay (the Quad) | 24, 28 |
| Setup conditions | Score each company on three Pods by year-over-year rate of change: Pod 1 revenue growth; Pod 2 cash flow or earnings growth (depending on company); Pod 3 capital allocation (free cash flow returns on invested capital). Each Pod is either accelerating or decelerating | 24 |
| Entry trigger & order type | Predict inflection points: accelerating = long, decelerating = short. Trigger timing and order type not stated | 24 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Implied: exit/flip when the Pod trend reverses; not explicitly stated | - |
| Position sizing | Falconhenge: "highly concentrated" portfolio (no numbers). Hedgeye later sizes single stocks per 2.2 (longs 1-3%) | 23, 36 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pod 1 | Rate of change of revenue growth | year-over-year | 24 |
| Pod 2 | Rate of change of cash flow or earnings growth | company dependent | 24 |
| Pod 3 | Free cash flow return on invested capital | rate of change | 24 |
| Signal | accelerating = long, decelerating = short | - | 24 |
| Score aggregation | Not found in this text (how three Pods combine to a score) | - | 24 |

**Key quotes**
- "Pod #1: The rate of change of Revenue Growth" [p. 24]
- "We would always evaluate companies in terms of the year-over-year rate of change" [p. 24]
- "Companies decelerating were shorts and companies accelerating were longs." [p. 24]
- "Our Mission: To Manage a High Conviction, Highly Concentrated Portfolio." [p. 23]

**Pseudocode**
```
# requires point-in-time fundamentals (we have these only from Feb 2026 => forward test only)
for each company i, each report date t:
    revAcc = (rev_yoy[t] - rev_yoy[t-1]) > 0
    earnAcc = (earn_or_cf_yoy[t] - earn_or_cf_yoy[t-1]) > 0
    roicAcc = (fcf_roic[t] - fcf_roic[t-1]) > 0           # ASSUMPTION: FCF/invested capital, compare to prior period
    score = revAcc + earnAcc + roicAcc                     # ASSUMPTION: equal weights; book gives none
    long if score == 3 ; avoid/exit if score <= 1          # ASSUMPTION thresholds
```

**Ambiguities & assumptions**
- The book describes Pods as the pre-Hedgeye Falconhenge method that inspired the Quads [p. 24, p. 25], not as a current tested system; no thresholds, weights, holding period or results are given for it (only that one quarter had "a quarterly return in the high teens" [p. 24]). Treat as a low-confidence, partly codable idea.
- "Cash flow or Earnings Growth (depending on the company)" [p. 24]: which metric per company is discretionary. ASSUMPTION: use earnings growth (EPS or PAT) for all.
- Pod 3 "capital allocation" is defined as free cash flow returns on invested capital [p. 24]; the definition of invested capital is not given. ASSUMPTION: (CFO - capex) / (equity + debt).
- Scoring/aggregation and the cut-offs for long vs short are not given. Not found in this book.

## 3. Risk & money-management rules

- Preserve capital first: large drawdowns prevent redeploying capital; recovery arithmetic is shown (-10% needs +11%, -20% needs +25%, -50% needs +100%, -90% needs +900%) [p. 11].
- Expect to be right only 55-65% of the time; use a repeatable rules-based process and change positioning when the data change, not the other way round [p. 9, p. 11, p. 12].
- Set MIN/MAX position sizes per asset class before entering a trade: commodities 1-4%, equities 2-6%, fixed income 3-10%, single stocks long 1-3% and short 0.5-2%; set actual limits by the asset's volatility (more volatile = smaller) [p. 36].
- Establish rules for sizing, for the reasons to exit, and do not "double down on failure" once a mistake is made [p. 36].
- Scale in and out in increments of 50-150bps of capital; no "all-in" [p. 39].
- Add less when TRADE is breaking down; do not add if TRADE breaks and a TREND breakdown is implied [p. 39].
- Stop-loss: previously -12%; now 6% after the position reaches MAX [p. 38].
- Exit ladder for core positions: Lower-Highs reduce size; plus TRADE break goes to MIN; plus TREND break is out [p. 38]. Break of TRADE and TREND support = out [p. 39].
- Bullish on all three durations (Trade, Trend, Tail) is a safer dip to buy [p. 33].
- Total gross/net exposure, number of positions, cash allocation rules: Not found in this text (the book mentions only that in early 2008 Hedgeye "signaled investors should go to 85% cash" [p. 9]).

## 4. Non-codable guidance

- A rules-based process "takes the sting out of mistakes"; follow your rules and explain to yourself why you violate them [p. 36, p. 39].
- Avoid "resulting": judge decisions by process quality rather than outcome [p. 11].
- Being right on the outlook but wrong on timing is the classic mistake; the market is on its own timetable [p. 8].
- Avoid groupthink and consensus ("who else owns it?"); numbers do not lie, people do [p. 30, p. 31, p. 35].
- Dr. Gio Valiante's "5 ways to win": talent, work harder, differentiated view, process, hire [p. 23].
- Long-term averages are not signals; do not rely on buy-and-hold comfort; act on the signal without arguing [p. 12, p. 13].
- Bottom-up analysts' ideas are run through the Risk Range for an agnostic quantitative check [p. 33].
- Daily routine (macro data before 5 a.m., Risk Range review, early notes by 6:30-7:00 a.m.) is Hedgeye's workflow, not a rule [p. 50].
- Chapters 5 and 6 (conflicts of interest, media, sell-side ratings) are commentary only [p. 41 to p. 49].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - 2.1 GIP: GDP (level or growth) and inflation (CPI) time series for the country, ideally a monthly proxy. India GDP/CPI history is NOT in our dataset; we would need an external series (e.g. national accounts, CPI releases). Also needed for asset classes to allocate to: index/ETF prices (NIFTYBEES, gold/bond ETFs if available).
  - 2.2 Risk Range proxy: daily OHLCV for each stock (price, volume, derived volatility); optional delivery % as a volume-quality proxy (recent years only).
  - 2.3 Pods: point-in-time revenue, earnings/cash flow and FCF/invested capital by period.
- **Testability with our data:**
  - 2.2 can be backtested on 2005-2026 daily OHLCV, but only as a proxy because Hedgeye's Risk Range formula is proprietary. The 50-150bps scaling and MIN/MAX table can be replicated exactly; the TRADE/TREND signal definitions are our assumptions.
  - 2.1 cannot be backtested without external India GDP/CPI history (not in our dataset). Instruments in the book are mostly US, so the book's asset-class mapping (an image, not in the text) does not transfer; the classifier can be run on external macro series and mapped to NIFTYBEES, sector baskets, or an equal-weight index built from the stock panel. The Nifty index history only starts in 2024, so use NIFTYBEES or an equal-weight panel index for earlier years. GDP is published quarterly with revisions and lags: avoid look-ahead.
  - 2.3 can only be forward-tested (fundamentals only from Feb 2026; 3-year growth fields from May 2026).
- **Market-structure differences:**
  - The book's universe is US ETFs and asset classes; the NSE cash market has no overnight shorting, so the short-side sizes (0.5-2%) and Bearish signals only serve as exits/cash. ASSUMPTION: long-only; exit to cash on breakdown.
  - Circuit limits can prevent exits at signalled prices. ASSUMPTION: execute at next open and skip names that hit circuits; apply about 0.1% slippage plus STT and brokerage.
  - Small, illiquid stocks distort volume/volatility inputs. ASSUMPTION: apply a minimum average daily traded value filter (value not in the book).
  - 50-150bps increments imply a diversified account; with NSE costs, frequent small adds are expensive. ASSUMPTION: keep the book's increments but test a wider minimum trade size.
  - ASSUMPTION: for a stock-level backtest use MIN 1% / MAX 3% (single stock long) and a 6% stop after MAX.

## 6. Verdict

- **Codeability:** Partly. The quad classification logic (acceleration/deceleration of yoy growth and inflation) and the position sizing / scaling / exit ladder are explicit, but the Risk Range formula and the per-quad asset mapping are proprietary or in an image and not in the text.
- **Priority for backtesting:** Medium. The sizing and exit-ladder rules are clean and cheap to test on a price proxy, but the proxy departs from the real signal, and the macro model needs India macro data we lack and has no reported results.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the proxy Risk Range as Hedgeye's proprietary signal; the book gives only inputs (price, volume, volatility), so results are not a test of the book's edge.
  2. Mis-defining "accelerating": the Quad uses the rate of change (second derivative) of growth and inflation on a yoy basis, not the level or direction of the level, and macro data have publication lags and revisions (look-ahead risk).
  3. Applying the stop and the exit ladder wrongly: the 6% stop applies only after the position reaches MAX, the Lower-Highs / TRADE / TREND ladder is progressive (reduce, then MIN, then out), and buying/selling is in 50-150bps increments rather than all-in.
