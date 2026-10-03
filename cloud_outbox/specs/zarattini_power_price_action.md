# The Power of Price Action Reading — Carlo Zarattini & Marios Stamatoudis (Concretum Research working paper, 28 June 2024)

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/The Power Of Price Action Reading by Carlo Zarattini.pdf` (file id `1s1KUbH29jaGJzdSlUISDgfnUFy_I9pLv`, 1,009,797 bytes), 30 PDF pages with a text layer. The author line in the inventory ("Carlo Zarattini") omits the co-author Marios Stamatoudis.
- **Text file used:** text/zarattini_power_price_action.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index; the paper's printed page numbers happen to coincide)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/zarattini_power_price_action.md text/zarattini_power_price_action.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 30]]. The literature review (pp. 4–7), author biographies (p. 29) and references (p. 30) contain no trading rules. The figures are images; their captions and the text describing them were used.

## 1. The method in brief

The paper studies US stocks that **gap up ≥ 6%** (open price ≥ $2, pre-market volume ≥ 200,000 shares; 9,794 events from 2016 to 2023) [p. 8].

**Mechanical rules have no edge.** Six rule-based long strategies (buy the open, 5-minute ORB, trailing stop, scaled targets) are unprofitable or only marginal. The average gap drifts down after day 1 [p. 10–12].

**Discretionary selection adds the edge.** A discretionary trader (Stamatoudis) screened anonymised 2-year daily charts and approved about 18% of the gaps. Applying the best mechanical rule set to those gaps alone turned it profitable (+0.25R peak) [p. 15–16].

**Micromanagement adds more.** When the trader also chose the intraday entry, set the stop at the low of the day, and took 25% partial exits trailed on the 10-, 20- and 50-day MAs, the results were [p. 22–25]:

| Measure | Value |
|---|---|
| Trades | 1,580 |
| Win rate | 18% |
| Average trade | +1.03R |
| Average win | +10.10R |
| Average loss | −1.02R |
| Risk per trade | 0.25% |
| Total return | 3,968% over 8 years |
| CAGR | 59.1% |
| Sharpe ratio | 1.70 |
| Maximum drawdown | 35% |

The reproducible part for us is the **gap-and-go ORB scaffold**. The selection factors are the human edge and are only loosely codeable.

## 2. Strategies

### 2.1 Mechanical gap-up opening-range breakout ladder (baseline; negative to marginal)

| Field | Rule (as stated by the authors) | Page |
|---|---|---|
| Type | gap continuation (long only) | 8, 10–12 |
| Universe / eligibility filters | NYSE/Nasdaq stocks, survivorship-free; open ≥ 6% above the prior close; open ≥ $2; pre-market volume ≥ 200,000 shares | 8 |
| Variant 1: Open, no stop | Buy at 09:30; hold 30 days; no stop (risk unit = 1 ATR) | 10–11 |
| Variant 2: Open, 1 ATR stop | Buy at 09:30; stop 1 ATR below the entry; hold 30 days | 10 |
| Variant 3: All OR | Buy-stop at the high of the first 5-minute bar; stop 1 cent below that bar's low; hold 30 days or until stopped | 10 |
| Variant 4: Pos OR | As Variant 3, but only if the first 5-minute bar is positive (close > open) | 10 |
| Variant 5: Pos OR + Trailing | As Variant 4, plus a trailing stop on the 10-day SMA | 10 |
| Variant 6: Pos OR + Trailing + 4 Targets | As Variant 5, plus sell 25% at each of 2R, 4R, 8R and 10R | 10–11 |
| Results | Variant 1 bottoms at −0.25R after 8 days; Variant 2 at −0.17R; Variants 3–5 improve but stay unprofitable; Variant 6 is "slightly profitable from the tenth day" — no exploitable edge | 11–12 |
| Context stats | Average gap ~25–28%; stocks rise from about −26% to 0% over the 15 days before the gap; after the gap they drift down, settling about +15% above the pre-gap close by day 16. The top 1% of gappers reach about +85% by day 16 | 8–10, 13 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Gap threshold | open ≥ +6% vs the prior close | — | 8 |
| Minimum price | $2 | — | 8 |
| Pre-market volume | ≥ 200,000 shares | — | 8 |
| Opening range | first 5 minutes | — | 10 |
| Stop | 1 cent below the OR low | 1 ATR (14-day) | 10 |
| Trailing | 10-day SMA | — | 10 |
| Targets | 25% at each of 2R, 4R, 8R, 10R | — | 10–11 |
| Maximum hold | 30 days | — | 10 |

**Key quotes**

- "An opening price at least 6% higher than the previous closing price." [p. 8]
- "Enter at the break of the 5-minute opening range high, with a stop loss placed 1 cent below the low of the first 5-minute candle, holding for 30 days or until the stop is hit." [p. 10]
- "four profit targets, selling 25% of shares at each target set at 2R, 4R, 8R, and 10R" [p. 10]
- "Following the overnight gap, stock prices typically drift downward gradually." [p. 10]
- "Despite this improvement, the profitability remains marginal and does not indicate any significant exploitable trading edge using these basic mechanical rules." [p. 12]

**Pseudocode** (1-minute intraday on the gap day; daily bars afterwards)

```
gap day d: O_d >= 1.06*C_{d-1} and O_d >= 2 and premarket_vol_d >= 200_000
OR = first 5-min bar (09:30-09:35): ORH, ORL, ORO, ORC
pos_or = ORC > ORO                                    # Variant 4+
entry: buy-stop at ORH + 0.01 during day d only ; stop = ORL - 0.01 ; R = entry - stop
targets: sell 25% at entry + 2R, 4R, 8R, 10R           # Variant 6
trail: from d+1, exit remainder at close if C < SMA(C,10) (ASSUMPTION: trailing on daily close)
time stop: exit all at close of day d+30
```

### 2.2 Discretionary-filtered gap-and-go with micromanagement (the paper's edge)

| Field | Rule (as stated by the authors) | Page |
|---|---|---|
| Type | gap continuation + human chart selection | 14–25 |
| Selection: favoured | (1) The gap follows a neglect period; (2) the gap breaks out of a multi-week or multi-month range; (3) the gap comes early in the momentum cycle | 16, 27 |
| Selection: avoided | A gap immediately after a gap on the previous day (exhaustion) | 16 |
| Selection basis | Anonymised 2-year daily charts (no ticker, dates, prices or volume); about 18% approved (1,721 of 9,794) | 15 |
| Entry | 5-minute ORB, or anticipating it. If the stock breaks the day's low, wait for a prior daily support level; higher lows after a drop are favoured; strength near estimated EMAs/VWAP; one entry attempt only | 19 |
| Initial stop-loss | Just below the low of the day (not at deeper support levels) | 19 |
| Position management | Four 25% parts. Let the full position run for the first ~3 days; then exit parts on a daily close below the 10-day and 20-day MAs; use the 50-day MA for a remaining runner after multiple R; take partials into parabolic moves | 19–20, 22 |
| Position sizing | Risk 0.25% of equity per trade (loss at the stop) | 23 |
| Results (filter only, Variant 6 rules) | Peaks at +0.25R, 12 days after entry | 16 |
| Results (filter + micromanagement) | +0.55R on the gap day; 0.80R by day 4. 1,580 trades, 18% wins, average +1.03R, wins +10.10R, losses −1.02R. CAGR 59.1%, volatility 29.9%, Sharpe 1.7, max DD 35%, every year positive, $0.01/share costs | 22, 25 |

**Key quotes**

- "After analyzing the daily charts of all 9,794 gap events in our database, the trader approved 1,721 gaps, approximately 18% of the original dataset." [p. 15]
- "Gaps Following a Neglect Period: These are favored as they signal renewed interest and potential upward momentum." [p. 16]
- "Avoiding Gaps Following Consecutive Gaps: Gaps that occur immediately after a gap on the previous day are not favored, as they often suggests potential exhaustion." [p. 16]
- "Stop losses are typically placed just below the low of the day rather than at key support levels." [p. 19]
- "Initial exits are based on trailing the 10-day and 20-day moving averages, with positions exited when a candle closes below these averages." [p. 20]
- "these trades are usually sized so that if a stop loss is hit, the resulting loss at the portfolio level equates to 0.25%." [p. 23]
- "The trade hit rate, at 18%, indicates that approximately one in five trades are winners" [p. 25]

**Pseudocode** (a coded proxy for the human filter; every threshold is an ASSUMPTION)

```
gap event as 2.1
neglect:      ATR(20)/C and avg dollar volume over d-60..d-1 in bottom 30% of their own 2-year history
              and |C_{d-1}/C_{d-60} - 1| < 15%
range_break:  O_d > max(H over d-60..d-1)                      # multi-week/month range breakout
early_cycle:  C_{d-1} < 1.5 * min(C over d-250..d-1)           # not already extended
no_double:    O_{d-1} < 1.04*C_{d-2}                           # previous day was not a gap
select if range_break and no_double and (neglect or early_cycle)
entry: ORB as 2.1 (Pos OR); stop = low of day so far - 0.01 (moves with LOD until entry)
size: qty = floor(0.0025*equity / (entry - stop))
manage: days 1-3 hold all (unless stopped);
        from d+3: sell 25% at first close < SMA10, 25% at first close < SMA20,
        runner 50%: if open gain >= 3R trail on SMA50 close, else on SMA20 ; max hold 50 days
        parabolic: if C >= entry + 8R within 10 days, sell 25% at close (ASSUMPTION)
```

**Ambiguities & assumptions**

- The selection factors are qualitative ("neglect period", "early in the momentum cycle"). The coded proxies above are ours, not the authors'. The paper's edge comes from one expert's judgement and may not be captured by them.
- The micromanaged entry is discretionary (1-minute bars, "anticipating" breakouts, VWAP/EMA estimates). The coded version uses the plain ORB.
- The 35% max drawdown is at 0.25% risk per trade, so trades evidently overlapped heavily in strong bull phases (late 2020–2021).

## 3. Risk & money-management rules

- Risk 0.25% of equity per trade [p. 23].
- Stop at the low of the gap day. Weakness on the gap day means exit quickly; the 1-ATR-stop result shows losses accumulate otherwise [p. 11, 19].
- Scale out in four 25% parts; trail the rest on the 10-, 20- and 50-day MAs [p. 19–20].
- One entry attempt per gap [p. 19].
- The expected payoff profile is a low win rate with a heavy right tail: 18% wins, average win 10R [p. 25].

## 4. Non-codable guidance

- The trader's edge is pattern reading of the prior 2-year daily chart: neglect, range breakout, momentum-cycle stage [p. 16].
- The intraday "price-action reading" for entries (patience after a drop, higher lows, VWAP strength) [p. 19].

## 5. Adapting to NSE (Indian equities)

- **Data required:** 1- or 5-minute bars for the gap day; daily OHLCV; pre-open session data (NSE's 09:00–09:08 call auction gives the equilibrium open and its volume as the "pre-market" analogue).
- **Testability with our data:** 2.1 is fully testable with intraday data (or approximately with daily data: entry above the first-5-minute high is not available from daily bars). 2.2 is testable only via the proxy filter.
- **Market-structure differences:**
  - Price bands (2/5/10/20%) cap gaps and can lock a stock at the upper circuit. Exclude stocks opening at the upper band (no fills, no ORB).
  - Most NSE stocks are in 20% bands. A +6% gap threshold is comparable but less rare. Test 4%, 6% and 8%.
  - Pre-open volume threshold (ASSUMPTION): pre-open traded value ≥ Rs. 2 crore, in place of 200,000 shares.
  - Minimum price (ASSUMPTION): Rs. 50, in place of $2, to avoid penny stocks.
  - T+1 settlement and no overnight cash shorting do not matter (the strategy is long only).

## 6. Verdict

- **Codeability:** Partial. 2.1 is fully mechanical but is shown by the authors themselves to lack an edge. 2.2's edge rests on discretionary selection and entry; only a proxy can be coded.
- **Priority for backtesting:** Medium. It is useful as a rigorously specified gap-and-go scaffold (ORB entry, LOD stop, 2/4/8/10R ladder or MA-trail exits) and a benchmark to beat. The proxy filter (range breakout + no consecutive gap + neglect) is a cheap, testable hypothesis on NSE gappers.
- **Top 3 things a coder is most likely to get wrong**
  1. Reporting the 3,968% / Sharpe 1.7 result as achievable mechanically. It required the trader's hand-picked 18% of gaps **and** discretionary micromanagement. Mechanical rules were flat to negative [p. 12, 16, 22].
  2. Stopping at the 1-ATR level or a distant support. The paper's stop is the opening-range low or low of day, and exits are on **daily closes** below the 10- and 20-day MAs, not intraday touches [p. 10, 19–20].
  3. Ignoring the requirements that the first 5-minute bar be positive ("Pos OR") and that the gap not follow a gap the day before [p. 10, 16].
