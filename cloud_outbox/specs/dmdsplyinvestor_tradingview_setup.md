# MY TRADINGVIEW SETUP - Explained! — Trendline Investor (@dmdsplyinvestor)

- **Source file:** Google Drive invest/my_tradingview_setup_-__thread_by_dmdsplyinvestor___jul 15, 23_from_rattibha.pdf (Twitter thread, 12 tweets, 2023-07-15, PDF by rattibha.com)
- **Text file used:** text/dmdsplyinvestor_tradingview_setup.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage.
  - Checked with `python ../work/bin/verify_citations.py specs/dmdsplyinvestor_tradingview_setup.md text/dmdsplyinvestor_tradingview_setup.txt`.
- **Coverage:** Read lines 1-128 of the text file in full, through the last marker [[PAGE 11]]. Page 2 is empty; pages 4, 7 and 9 contain only video links (the three videos, plus the YouTube explainer links on pages 3, 6 and 9, were not available, so any rules shown only in them are unknown); page 11 is the Rattibha disclaimer. Nothing skimmed. Reading done by a Sonnet sub-agent. The coordinator read the whole 128-line text itself, re-ran the verifier and an exact-page check, and confirmed every table citation against pp. 1-10.

## 1. The method in brief

This is a short indicator SETUP, not a full trading system. The author uses three TradingView indicators on both weekly and daily charts [p. 10]: the Commodity Channel Index (CCI, length 34) to assess bullishness, Mansfield Relative Strength against CNX500 (52-period MA) to assess outperformance, and Pivot Points High Low (default settings) to assess trend changes [p. 3, 6, 8]. The thread says what each indicator is for and how to set it up, and why the lengths were chosen (fewer signals), but it does not give any entry trigger, stop-loss, exit, position-sizing or portfolio rule. No track record or test results are presented.

Intended market: stocks traded in India (the benchmark is CNX500, a Nifty 500 index) [p. 6]. The only claimed "edge" is qualitative: longer settings give fewer, better signals ("Lesser the better!") [p. 5].

## 2. Strategies

### 2.1 CCI(34) + Mansfield RS(52) vs CNX500 + Pivot Points High Low filter setup

This is a single combined indicator setup. The thread treats the three indicators as parts of one toolkit ("the 3 Indicators I use") [p. 10], so it is not split. What is stated are indicator readings; how they combine into trades is not stated.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend / momentum filter setup (indicator toolkit); no complete system stated | 1, 10 |
| Timeframe & holding period | Weekly and daily charts. Holding period: not found in this text | 10 |
| Universe / eligibility filters | Not found in this text (benchmark for RS is CNX500; no stock screen stated) | 6 |
| Market / regime filter | Not found in this text. Closest item: RS is measured against CNX500 to assess outperformance | 6 |
| Setup conditions | Bullish momentum: CCI above 100; bearish: CCI below -100. Outperformance: Mansfield RS (symbol CNX500, MA length 52); the thread gives no numeric threshold, only the purpose "to assess Outperformance". Trend change: Pivot Points High Low, default settings | 3, 6, 8 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text. Only: pivots "assess trend changes" and CCI below -100 "indicates bearishness"; no exit rule is stated | 3, 8 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| CCI length | 34 bars (indicator: TradingView built-in Commodity Channel Index, "Technicals" section) | Default is 20, which gives more signals; reader should test values across multiple stocks | 3, 5 |
| CCI bullish level | Above 100 | none | 3 |
| CCI bearish level | Below -100 | none | 3 |
| Relative strength indicator | 'Mansfield Relative strength' | none | 6 |
| RS comparison symbol | CNX500 | none | 6 |
| RS MA length | 52 (52 weeks on weekly charts, a 1 year MA of RS) | Lower number gives more signals | 6, 8 |
| Pivot Points High Low | Default settings | 5,5,5,5 sometimes, depending on trend strength; changing it is only for "more signals" | 8, 10 |
| Chart timeframes | Weekly and daily | none | 10 |
| CCI and RS settings changes | Not changed | none | 10 |

**Key quotes**

- "Above 100, indicates bullishness" [p. 3]
- "Below -100, indicates bearishness" [p. 3]
- "Length - change this to 34 from default 20" [p. 3]
- "The default 20 will give more buy/sell signals than 34. Lesser the better!" [p. 5]
- "'This is not RSI' but RS." [p. 6]
- "change symbol to 'CNX500' & keep MA(Moving average) length 52" [p. 6]
- "it is the 1 year moving average of the Relative strength" [p. 8]
- "Search for 'Pivot Points High Low' in Tradingview" [p. 8]
- "Use the default settings" [p. 8]
- "these are the 3 Indicators I use on both weekly &" [p. 10]
- "I do not change the settings of CCI & RS." [p. 10]
- "I might switch to 5,5,5,5." [p. 10]

**Pseudocode** (thread's filters only; the combining rule is an assumption)

```
# Thread-stated indicator readings (weekly and daily bars)
cci34      = CCI(typical_price, 34)          # TradingView built-in CCI, length 34
bullish    = cci34 > 100
bearish    = cci34 < -100

# Mansfield RS vs CNX500, 52-bar MA  (formula NOT in this text; see Ambiguities)
rs         = MansfieldRS(stock_close, bench_close, ma_len=52)

# Pivot Points High Low, default left/right lengths (values NOT in this text);
# alternative 5,5,5,5 when trend is strong
pivots     = PivotHighLow(high, low, left=L, right=R)   # L,R: see Ambiguities

# ASSUMPTION: combined long candidate (the thread does not state how to combine)
long_candidate = bullish AND rs_outperforming AND last_pivot_structure_is_higher_highs_higher_lows
# Entry, stop, exit, sizing: not found in this text
```

**Ambiguities & assumptions**

- Mansfield RS definition: not found in this text. ASSUMPTION: usual formula (not from this text) is RS = (stock_close / bench_close), then Mansfield RS = (RS / SMA(RS, 52) - 1) * 100; outperformance = Mansfield RS above zero (equivalently RS above its 52-bar MA). The thread only says to keep MA length 52 and compare to CNX500.
- CCI price source and constant (0.015): not found in this text. ASSUMPTION: TradingView built-in default (hlc3 source).
- CCI +100/-100 is described as "Above 100" and "Below -100"; whether signals use crossings or the level state is not stated. ASSUMPTION: state-based (cci > 100 means bullish), with crossing of 100 treated as the event.
- Pivot Points High Low default left/right lengths: not found in this text (the "5,5,5,5" alternative suggests four inputs, but the default values are not given). ASSUMPTION: use 5,5,5,5 for both normal and strong-trend cases, because the default is not stated; sensitivity test with smaller values.
- What a pivot "trend change" means: not found in this text. ASSUMPTION: uptrend = sequence of higher pivot highs and higher pivot lows; trend change = a pivot low lower than the previous pivot low, or a pivot high lower than the previous one.
- How the three indicators combine, weekly versus daily priority, entries, stops, exits, sizing and holding period: not found in this text. ASSUMPTION: weekly chart sets direction (CCI > 100 and RS above its MA); daily chart used for timing; entry at next bar open after daily conditions turn true; exit when daily CCI < -100 or a lower pivot low forms. These are our assumptions, not the author's rules.
- "Which timeframe to use for which indicator": the thread says "both weekly & daily" without detail [p. 10].
- Author says test values: "I would suggest testing the values over multiple stocks" [p. 5], so 34 and 52 are suggestions, not fixed requirements.
- Videos on pages 4, 7 and 9 (and linked YouTube explainers) were not available and may contain more rules.

## 3. Risk & money-management rules

Not found in this text. The thread gives no risk-per-trade, stop-loss, drawdown, exposure or position-limit rule.

## 4. Non-codable guidance

- The author says the CCI length is a personal choice: "I would suggest testing the values over multiple stocks & assessing how it works" and the reader must "find an optimum value that fits your trading style/needs" [p. 5].
- Pivot settings are changed discretionarily ("depending on the strength of the trend") [p. 10].
- RS is a relative measure, not RSI: the author stresses the two are "completely different indicators" [p. 6].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLC (high, low, close) for each stock; weekly bars resampled from daily (Friday close or last trading day of week); benchmark close series for CNX500 (Nifty 500). Volume is not used by the thread.
- **Testability with our data:** CCI(34) and Pivot Points High Low use only the stock's own OHLC, so they can be backtested over 2005-2026. Mansfield RS needs the CNX500 series; our Nifty index history starts only in 2024, so the 2005-2023 history needs a proxy. ASSUMPTION: use an equal-weight index built from the stock panel (for example the 500 most liquid stocks by trailing traded value, rebalanced monthly or quarterly, using the delisted-inclusive panel), or NIFTYBEES as a cheaper proxy where it exists. Check that results are not sensitive to the proxy by comparing with real Nifty 500 data from 2024 onward. No fundamentals are needed. Delivery % not used.
- **Market-structure differences:** the thread gives no entry or exit rule, so costs cannot be calibrated to it. ASSUMPTION: apply STT, brokerage and about 0.1% slippage per trade, long-only (no overnight shorting in the cash market, so "bearish" readings serve only as exits or avoid-signals), and skip entries on circuit-locked days. ASSUMPTION: restrict the universe to stocks above a minimum traded-value threshold to avoid illiquid small caps. Weekly signals use trading weeks that can be short around holidays.

## 6. Verdict

- **Codeability:** Partly. The three indicator filters are codable (the exact formula for Mansfield RS and the Pivot default lengths must be assumed), but the thread states no entry, stop, exit or sizing rule.
- **Priority for backtesting:** Low. It is only an indicator configuration with no stated trading rules or results; testing it requires us to invent most of the system, so it is better treated as a filter component for other strategies.
- **Top 3 things a coder is most likely to get wrong:**
  1. Confusing Mansfield RS with RSI, or computing it on the wrong series (it must be stock versus benchmark, with a 52-bar MA on the weekly chart), and using a weak benchmark proxy before 2024.
  2. Inventing the Pivot Points High Low default lengths or ignoring that pivots are confirmed only after the right-hand bars, which causes look-ahead bias if the pivot is used on the pivot bar itself.
  3. Treating the thread as a complete system: no entry, stop, exit or sizing is given, so any combined rule is an assumption, and mixing weekly and daily signals without using only completed weekly bars causes look-ahead bias.
