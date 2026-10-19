# Beginner's Guide to Trading — author not stated on the title slide (possibly Gagan Kalra, inferred from a self-referencing LinkedIn link on p. 6)

- **Source file:** Google Drive "Beginner's guide to trading.pdf" (slide deck exported to PDF, 27 pages, 4.7 MB, mostly chart images)
- **Text file used:** text/unknown_beginners_guide_trading.txt  (page basis: slides, one slide per PDF page, taken from the PDF text layer)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not a printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage. The deck has no printed page numbers.
  - Checked with `verify_citations.py` before finishing.
- **Coverage:** Read lines 1-343 of the text file (the whole file; the brief said 342 lines, the file has 343) and reached the last marker, [[PAGE 27]]. Nothing was skimmed. Slide 4 has no text at all. Slides 9-11, 14-15, 18-23 and the chart examples on slides 24-26 are images with only a title or short caption in the text layer, so their chart content (Wyckoff phases, candle drawings, S&P charts, indicator panels, the blue/green/red lines on the trade examples) was not available to me. *Coordinator check: the coordinator re-ran verify_citations (27/27 ok) and an exact-page strict check (0 off-by-one), and confirmed all five field tables have exactly the 12 template rows. Spot-checked by grep: Graham current ratio and Slater 15% EPS growth p.8, '8 days' SMA p.18, VWMA set-up p.24-26, '2nd candle' entry p.25-26, 30-point and 80-point stops with 1:1 targets p.25-26; all matched. The file is 343 lines (the coordinator's brief said 342).*

## 1. The method in brief
This is a short beginner primer for public-market trading. It covers market basics (OHLC, volume, spread, slippage, liquidity, volatility) [p. 2, 3], trading psychology and choosing a style [p. 5, 6], a fundamentals slide with two classic screens (Benjamin Graham value, Jim Slater growth) [p. 7, 8], then "Glimpses into World of TA": trend structure and Wyckoff, candlesticks, a moving-average crossover, and chart patterns [p. 9-23]. The one personal method is "My set up 1" [p. 24-26], a VWMA 9 / SMA 9 / Momentum 9 crossover entry with a fixed-distance 1:1 target and stop, used on 15-minute charts for intraday or daily charts for swing or positional trades [p. 24].

The deck states no track record, win rate, backtest or performance figure. The only evidence is two worked chart examples (Reliance, 30 points; PVR, 80 points) [p. 25, 26], and their charts are images. The author says fundamental analysis "wont tell you" when to enter or exit [p. 7], so the fundamental screens are stock-selection filters only.

## 2. Strategies

### 2.1 Benjamin Graham value criteria (screen)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | value (fundamental screen) | 7, 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Current ratio at least 2; positive earnings in each of previous 10 years; dividend paid for at least 20 years; earnings up at least a third over last 10 years; price not more than 15 times the 3-year average earnings. The slide says "for illustrative purposes only" | 8 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | All five criteria above hold (the slide lists them without saying "all"). Wider idea: companies trading below book value | 7, 8 |
| Entry trigger & order type | Not found in this text. The deck says fundamentals cannot time entry or exit | 7 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Current ratio minimum | 2 | none | 8 |
| Years of positive earnings | 10 | none | 8 |
| Years of dividends paid | 20 | none | 8 |
| Earnings increase over 10 years | at least one third | none | 8 |
| Max price / 3-year average earnings | 15 | none | 8 |
| Book value test | "trading below their book value" (no ratio given) | none | 7 |

**Key quotes**
- "Must have current ratio of at least 2" [p. 8]
- "Should have reported positive earnings in previous 10 years" [p. 8]
- "Should have paid dividend for at least 20 years" [p. 8]
- "the current stock price should not be more than 15 times" [p. 8]
- "Benjamin Graham’s value investing is all about identifying companies trading" [p. 7]

**Pseudocode**
```
# forward-test only; run on each snapshot date
for stock in universe:
    pass = current_ratio >= 2
       and min(eps[-10y:]) > 0
       and dividend_paid_each_year[-20y:]
       and eps_avg_last_3y_recent >= eps_avg_3y_ten_years_ago * (1 + 1/3)   # ASSUMPTION
       and price <= 15 * mean(eps[-3y:])
    if pass: add to candidate list
# no entry/exit rule in the book
```

**Ambiguities & assumptions**
- The book gives no entry, exit, stop, sizing or holding period. ASSUMPTION: treat this only as a candidate list, with the price-action rules of the user's choice added separately.
- "Earnings ... increase of at least a third over last 10 years" does not say how to measure it. ASSUMPTION: compare the average of the latest 3 years of EPS with the average of the 3 years ending 10 years ago.
- The slide says criteria are "for illustrative purposes only" [p. 8] and also mentions book value [p. 7] but sets no price-to-book threshold. Not found in this text.
- Whether all five must hold is not stated. ASSUMPTION: all five.

### 2.2 Jim Slater growth criteria (screen)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | growth-momentum (fundamental screen; no price-action component stated) | 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | EPS growth 15% per annum (over 100% total in previous 5 years); ROCE above 20%; debt below 50% of net assets; net operating cash flow above operating profit | 8 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | PEG of 1 or less with PE below growth rate; variant: PE between 12 and 15 with growth rate of 20-25% | 8 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| EPS growth per annum | 15% | total above 100% over previous 5 years | 8 |
| Return on capital employed | above 20% | none | 8 |
| Debt / net assets | below 50% | none | 8 |
| Net operating cash flow vs operating profit | higher | none | 8 |
| PEG | 1 or less | with PE less than growth rate | 8 |
| PE band (variant) | 12-15 | with growth rate 20-25% | 8 |

**Key quotes**
- "EPS should grow at 15% per annum ( totalling in excess of 100% in previous 5 years)" [p. 8]
- "Return on Capital Employed should be greater than 20%" [p. 8]
- "Debts below 50% of Net assets" [p. 8]
- "Net operating cash flows should be higher than operating profits" [p. 8]
- "Buying shares in companies with PEG of 1 ( or less) with PE ratio less than its growth rate" [p. 8]
- "Buying growth shares with PE ratio between 12-15 and growth rate of 20-25%" [p. 8]

**Pseudocode**
```
# forward-test only
for stock in universe:
    base = eps_cagr_5y >= 0.15 and eps[-1]/eps[-6] > 2.0     # ASSUMPTION: "in excess of 100%" means a more than doubling
       and roce > 0.20 and total_debt < 0.5 * net_assets
       and cfo > operating_profit
    A = base and peg <= 1 and pe < growth_rate_pct
    B = base and 12 <= pe <= 15 and 0.20 <= growth_rate <= 0.25
    if A or B: candidate
```

**Ambiguities & assumptions**
- Entry, exit and stop are not given. ASSUMPTION: candidate list only.
- Growth rate used in PEG and "PE less than growth rate" is not defined. ASSUMPTION: trailing 5-year EPS CAGR in percent.
- "Total in excess of 100% in previous 5 years" next to 15% per annum is slightly inconsistent (15% for 5 years compounds to about 101%, so it matches only barely). ASSUMPTION: require both.
- Whether the two PE/PEG lines are alternatives or both required is not stated. ASSUMPTION: alternatives (A or B).
- "Net assets" is not defined. ASSUMPTION: book value of equity.

### 2.3 "8 over 21" moving-average crossover (S&P, 15-minute)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following (crossover implied by "8 over 21"; the rule itself is not spelled out) | 18 |
| Timeframe & holding period | Shown on S&P over a 15 minute timeframe. Holding period not found in this text | 18 |
| Universe / eligibility filters | Only S&P shown. Not found in this text | 18 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Two simple moving averages: 8-period (blue line) and 21-period (red line). Slide labels them "8 days SMA" and "21 days SMA" although the chart is 15 minutes | 18 |
| Entry trigger & order type | Not stated; slide is a chart plus title. "8 over 21" implies the 8 SMA above the 21 SMA | 18 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fast SMA length | 8 | none | 18 |
| Slow SMA length | 21 | none | 18 |
| Chart timeframe | 15 minutes (S&P) | the slide label says "days" | 18 |
| General MA purpose | trend direction, support and resistance; lagging | none | 17 |

**Key quotes**
- "My favourite ( 8 over 21)" [p. 18]
- "S&P over 15 mins timeframe" [p. 18]
- "8 days SMA" [p. 18]
- "21 days SMA" [p. 18]
- "Is a lagging indicator" [p. 17]

**Pseudocode**
```
# ASSUMPTION-heavy; book gives only the two lengths
sma8 = SMA(close, 8); sma21 = SMA(close, 21)
if sma8 crosses above sma21 on bar t: go long at open of bar t+1
if sma8 crosses below sma21: exit long at open of next bar      # ASSUMPTION
# no stop, target or sizing in the book
```

**Ambiguities & assumptions**
- The slide says "15 mins timeframe" but labels the lines "8 days SMA" and "21 days SMA". Both versions recorded [p. 18]. ASSUMPTION: 8 and 21 bars of the chart's own timeframe; on our data test daily bars (8/21 days).
- The slide gives no entry or exit text, no short/long statement and no stop. ASSUMPTION: long on bullish cross, exit on bearish cross, no shorting.
- Intraday 15-minute data is not available to us; only a daily variant can be tested.
- Whether this is a separate system or an alternative to "My set up 1" is not stated. Treated as separate.

### 2.4 "My set up 1" — buy side (VWMA 9 / SMA 9 / Momentum 9)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / crossover momentum entry | 24, 25 |
| Timeframe & holding period | 15-minute charts for intraday; daily charts for swings or positional. Holding period beyond "swings or positional" not found in this text | 24 |
| Universe / eligibility filters | Not found in this text. Examples are Reliance (buy) and PVR (sell); charts on TradingView or Investing | 24, 25, 26 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | VWMA crosses SMA from below; the spot candle goes above both VWMA and SMA; Momentum goes above 0 | 25 |
| Entry trigger & order type | Enter in the 2nd candle made after the spot goes above VWMA and SMA. Order type not stated | 25 |
| Initial stop-loss | Loss level fixed at the same distance as the trade range (30 points in the Reliance example) below the entry candle (red line) | 25 |
| Exits: profit-taking | Take profit at 1:1 risk reward, drawn about 30 points above the entry candle (green line) | 25 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| VWMA length | 9 ("change the default setting to 9") | none | 24 |
| SMA length | 9 | none | 24 |
| Momentum length | 9 | none | 24 |
| Momentum threshold | above 0 | none | 25 |
| Entry candle | 2nd candle after the spot goes above both lines | none | 25 |
| Reward:risk | 1:1 ("generally") | none | 25 |
| Trade range / stop / target distance | 30 points in the Reliance example (entry-candle upper and lower limits) | 80 points in the PVR sell example | 25, 26 |
| Chart timeframe | 15 minutes intraday; daily for swing/positional | none | 24 |

**Key quotes**
- "VWMA ( change the default setting to 9)" [p. 24]
- "for swings or positional ( daily charts)" [p. 24]
- "VWMA crosses SMA from below" [p. 25]
- "Spot candle should go above both VWMA and SMA" [p. 25]
- "Momentum should go above 0" [p. 25]
- "Take entry in the 2nd candle which is made after the spot goes above VWMA and SMA" [p. 25]
- "I generally use 1:1 risk reward ratio for this trade" [p. 25]
- "our trade range is 30 points of swing in reliance" [p. 25]
- "the loss lvl has been defined as 30 points below the entry candle" [p. 25]

**Pseudocode**
```
vwma = sum(close*volume, 9) / sum(volume, 9)       # ASSUMPTION: price source = close
sma  = SMA(close, 9)
mom  = close - close[9]                            # ASSUMPTION: charting-platform Momentum = close - close 9 bars ago
for each bar t:
    if vwma[t-1] <= sma[t-1] and vwma[t] > sma[t]:        # cross from below
        S = first bar >= t with close > max(vwma, sma) and mom > 0   # "spot candle"; ASSUMPTION: look ahead up to 3 bars
        if S exists: E = S + 2          # ASSUMPTION: "2nd candle made after" spot candle
            entry = open[E]             # ASSUMPTION
            R = high[E] - low[E]        # ASSUMPTION: "upper limit and lower limit of entry candle"
            stop = entry - R; target = entry + R
            manage: exit at target or stop; if both in same bar, assume stop first   # ASSUMPTION
            intraday (15m): force exit at session close                              # ASSUMPTION
```

**Ambiguities & assumptions**
- "Spot" is not defined. It may mean the price/candle (p. 25 says "Spot candle"). ASSUMPTION: the candle whose close is above both lines.
- "2nd candle which is made after the spot goes above" may be the bar immediately after the spot bar or the one after that. ASSUMPTION: spot bar + 2 (literal count of bars made after it); alternative spot bar + 1 should be tested.
- Entry price and order type are not stated. ASSUMPTION: market at the open of the entry candle.
- The trade range definition is shown only by blue lines on a chart image. The text says the lines mark the "upper limit and lower limit of entry candle". ASSUMPTION: R = high minus low of the entry candle. The example (30 points on Reliance) could instead be a discretionary choice.
- Stop and target are "30 points below/above the entry candle". It is unclear whether measured from the entry candle's open, close, low or high. ASSUMPTION: from the entry price.
- "generally use 1:1" implies other ratios are sometimes used; none are stated.
- No time stop, trailing stop, position sizing or max positions in this text. ASSUMPTION: none; one position per stock at a time.
- Daily-bar trades have no stated gap handling. ASSUMPTION: if the open gaps beyond the stop, exit at the open.
- Momentum indicator formula is not given. See pseudocode ASSUMPTION.

### 2.5 "My set up 1" — sell side (mirror)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / crossover momentum entry (short) | 26 |
| Timeframe & holding period | Same as the buy side: 15-minute intraday; daily for swing or positional | 24 |
| Universe / eligibility filters | Not found in this text. Example: PVR | 26 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | VWMA crosses SMA from above; the spot candle goes below both VWMA and SMA; Momentum goes below 0 | 26 |
| Entry trigger & order type | Enter in the 2nd candle made after the spot goes below VWMA and SMA. Order type not stated | 26 |
| Initial stop-loss | Loss level 80 points above the entry candle in the PVR example (red line), the same distance as the trade range | 26 |
| Exits: profit-taking | Take profit at 1:1, about 80 points below the entry candle (green line) | 26 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| VWMA / SMA / Momentum lengths | 9 / 9 / 9 | none | 24 |
| Momentum threshold | below 0 | none | 26 |
| Entry candle | 2nd candle after the spot goes below both lines | none | 26 |
| Reward:risk | 1:1 | none | 26 |
| Trade range / stop / target distance | 80 points in the PVR example | none | 26 |

**Key quotes**
- "VWMA crosses SMA from above" [p. 26]
- "Spot candle should go below both VWMA and SMA" [p. 26]
- "Momentum should go below 0" [p. 26]
- "Take entry in the 2nd candle which is made after the spot goes below VWMA and SMA" [p. 26]
- "our trade range is 80 points of swing in PVR" [p. 26]

**Pseudocode**
```
# mirror of 2.4 with signs reversed
if vwma crosses below sma and close < min(vwma, sma) and mom < 0: arm short
E = spot bar + 2; entry = open[E]; R = high[E] - low[E]
stop = entry + R; target = entry - R
# NSE cash: no overnight short; allow only intraday (15m) variant, force exit at session close
# on daily data use the signal only as a long-exit / avoid-entry filter
```

**Ambiguities & assumptions**
- All ambiguities of 2.4 apply. The sell side is stated separately on p. 26 and is a separate testable variant.
- Shorting: the Indian cash market has no overnight short. ASSUMPTION: test the short side only as an intraday trade (needs 15-minute data we lack) or skip it; on daily data use it only as an exit/avoid signal.

## 3. Risk & money-management rules
- Reward:risk is "generally" 1:1 on "My set up 1", with stop and target the same distance from entry [p. 25, 26].
- Do not take positions in a market you do not understand [p. 5].
- Avoid revenge trading or averaging your way out of the market (no adding to losers) [p. 6].
- Be ready to reverse a decision when the market turns; the main cause of losing trades is not accepting a decision was wrong [p. 6].
- Part-time traders who cannot watch the screen should use good-till-cancelled orders so targets and stop losses are not missed [p. 5].
- Slippage is the loss from the spread; higher liquidity means a narrower spread [p. 3].
- No position size, risk per trade, drawdown rule or exposure cap is given. Not found in this text.

## 4. Non-codable guidance
- Choose a trading style: news-junkies suit scalping and day trading (prone to noise and overtrading); part-time traders suit swing, positional and trend trading [p. 5].
- Pride is the most dangerous factor; you trade to make money, not to prove anything [p. 6].
- Do not follow the herd; know your own motivation [p. 6].
- Avoid too much information, which gives a false sense of confidence; do not be fooled by randomness [p. 6].
- Fundamental analysis assesses the "rational" price but cannot time entry or exit; look at leverage, cash flow and intangibles [p. 7].
- Trends: higher highs and higher lows in an uptrend, lower highs and lower lows in a downtrend [p. 9]. Wyckoff phases and the S&P monthly example are charts only [p. 9, 10].
- Candlestick definitions (no entry or exit rule is stated for any of them):
  - Bearish engulfing: sellers in control, reversal if at the end of an uptrend [p. 12].
  - Bullish engulfing: buyers in control, reversal at the end of a downtrend, continuation in an uptrend [p. 13].
  - Morning star: 3-candle bullish reversal at the bottom of a downtrend [p. 14].
  - Evening star: 3-candle bearish reversal at the top of an uptrend [p. 15].
  - Marubozu: candle with no shadows; bull marubozu shows aggressive buying, bear marubozu further selling pressure [p. 16].
- Moving averages smooth price, help find trend direction and support/resistance, and lag [p. 17].
- Chart patterns shown only as titles over S&P chart images, with no rules: double bottom [p. 19], head and shoulders (daily) [p. 20], inverse head and shoulders (weekly) [p. 21], cup and handle (daily) [p. 22], flag (weekly) [p. 23].
- Closing line: "Buy low and sell high" and "Sell high and buy low" [p. 27].

## 5. Adapting to NSE (Indian equities)
- **Data required:**
  - Graham and Slater screens: current ratio, EPS history (10 years), dividend history (20 years), P/E, PEG, ROCE, debt, net assets, operating cash flow, operating profit.
  - 8/21 SMA: close.
  - My set up 1: open, high, low, close, volume (daily); the author's primary intraday version needs 15-minute OHLCV.
- **Testability with our data:**
  - Backtestable on 2005-2026 daily data: the daily-bar version of 2.3 and of 2.4 (long side). The long and short sides of 2.4/2.5 on daily bars are valid per p. 24 (daily charts).
  - Forward-test only: 2.1 and 2.2 (fundamentals are point-in-time snapshots only from Feb 2026, 3-year growth fields from May 2026; the 10-year and 20-year history rules cannot be reproduced from snapshots).
  - Needs data we do not have: the 15-minute versions (2.3 as shown, 2.4/2.5 intraday).
  - No candlestick or chart-pattern rule is stated, so nothing to test.
- **Market-structure differences:**
  - ASSUMPTION: the deck's examples use US indexes and Indian stocks (Reliance, PVR) in index points/rupees. Convert fixed point distances to the entry-candle range or a percentage; "30 points" and "80 points" are not transferable levels.
  - No overnight shorting in the NSE cash market: ASSUMPTION: drop the sell side for daily tests, or test it only intraday.
  - Circuit limits and gaps can skip stops; costs: STT, brokerage and about 0.1% slippage. A 1:1 target on a narrow daily candle could be eaten by costs, so ASSUMPTION: skip trades where R is below 1% of price.
  - Liquidity: ASSUMPTION: restrict to liquid stocks (for example a minimum average daily traded value).
  - Index: use NIFTYBEES or an equal-weight index for any "S&P-like" index test; Nifty history exists only from 2024.

## 6. Verdict
- **Codeability:** Partly. Only "My set up 1" has stated entry, target and stop (with several undefined terms); the 8/21 SMA slide gives only the two lengths; Graham and Slater are screens without entry or exit.
- **Priority for backtesting:** Low. It is a beginner primer with no performance claims and the only complete trade rule uses 15-minute data we lack; a daily test of "My set up 1" is cheap and worth one run.
- **Top 3 things a coder is most likely to get wrong:**
  1. Counting the "2nd candle" after the spot candle (S+1 vs S+2) and defining "spot" and the entry price.
  2. Treating the example "30 points" / "80 points" as fixed values rather than the entry-candle range, and measuring the stop and target from the wrong price.
  3. Treating the 8/21 SMA slide as a complete system (it has none of entry, exit or stop) and ignoring the "15 mins" vs "days" label conflict; also back-testing the Graham/Slater screens with look-ahead fundamentals.
