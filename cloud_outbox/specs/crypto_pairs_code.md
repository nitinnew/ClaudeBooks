# Pairs-trading and EMA code snippets (bundle) — author unknown

- **Source file:** Drive bundle "Pairs-trading and EMA code snippets" (3 files): (a) "Cointegration Pairs Trading Infy TCS.py" (IDE HTML export of "Cointegration recovered.py"), (b) "EMA Trading Startegy.py.html" (IDE HTML export of "EMA Trading Startegy.py"), (c) "ETH_XRP Pair Trading_17 Mar 2022.pdf" (14-page console log). Author: unknown (file path suggests a user "ajit"; the name appears only in the export path "E:\ajit\Quantitative Finance\...").
- **Text file used:** text/crypto_pairs_code.txt  (page basis: pdf_pages for the log; the two code files are each one transcribed "page")
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - p. 1 = pairs-trading script (87 lines); p. 2 = EMA script (100 lines); pp. 3-16 = ETH/XRP console log (the log's own footer "Page k of 14" is k = N - 2; do not use it).
  - Code is cited by the file's own line numbers ("line 15"), always with the page of the file: pairs script = [p. 1], EMA script = [p. 2]. Log lines carry their own line numbers (1-711) which are NOT used here.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
- **Coverage:** Read all of text/crypto_pairs_code.txt, lines 1-974 (two chunks), through the last marker `[[PAGE 16]]` (log ends at "Page 14 of 14"); nothing skimmed. Transcription note: pp. 1-2 are code transcribed by the coordinator from Drive's plain-text rendering of the IDE HTML exports, with the files' own line numbers and restored indentation (no tokens changed). Font issue in pp. 3-16: the PDF font renders the digit 4 as "~" (e.g. "cumulative net return so far: ~0.31%" = 40.31%; "12.~~%" = 12.44%), and in places as "li", "l.i" or "M" (e.g. "10.9li%" = 10.94%, "5M" = line 564); the "cumulative net return so" text is truncated and its tails ("far: 10.9li%") are displaced on pp. 11-12. Values are therefore read as 4 where an unambiguous digit is missing; those readings are my reconstruction and are marked as such. The log does not show the script parameters or tickers used for the ETH/XRP run (see 2.3). *Coordinator check: the two .py/.html files are not supported by the connector's binary download in a saveable form, so the coordinator took Drive's plain-text rendering of each IDE HTML export and transcribed the code with the original line numbers (indentation restored, no tokens changed). The ETH/XRP log PDF comes from its text layer. The coordinator re-ran verify_citations (15/15 ok) and an exact-page strict check (0 off-by-one), and confirmed the three field tables have exactly the 12 template rows. Log counts were verified by grep: 101 logged days (66 'no trading' in the log; the 67th match is the code's print statement), -8.6~% on 2021-02-12, ~5.59% (= 45.59%) on 2021-05-15, final ~0.31% (= 40.31%); all matched.*

## 1. The method in brief
The bundle holds three artefacts from one unnamed individual's "Quantitative Finance" folder; there is no prose, thesis or explanation, only code and a run log.

(1) A rolling-window cointegration pairs strategy, tested on INFY.NS / TCS.NS, 2019-01-16 to 2021-02-24 [p. 1]. Each day a hedge ratio b between the two prices is chosen to minimise a Dickey-Fuller-style t-statistic of the spread over the previous 252 observations; if that t-statistic is below -2.5 the pair is deemed "cointegrated" and the strategy goes long the cheaper-vs-fair-value stock and short the other, one unit each, for one day; otherwise it is flat [p. 1]. Fee is 0.001 per unit of position change [p. 1]. The text contains no INFY/TCS results.

(2) A long-only EMA crossover class (30/75 EMA on Adj Close, INFY, 2010-01-01 to 2022-03-10, capital 50000) [p. 2]. No results are shown.

(3) A console log of the pairs script run on ETH-USD / XRP-USD, 2021-02-08 to 2021-05-19: the log's last printed cumulative net return is ~0.31% (= 40.31% by the "~ = 4" font reading) [p. 16]. This is an author-run, in-sample, fee-light result with the execution caveats listed in 2.1 and 2.3.

## 2. Strategies

### 2.1 Rolling cointegration pairs trade (INFY.NS / TCS.NS script)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion / statistical-arbitrage pairs trade (market-neutral long/short, equal +/-1 unit legs) | 1 |
| Timeframe & holding period | Daily bars from yfinance; position decided from close of day t and held one day (return `returns[t]` = close[t+1]/close[t] - 1, line 22); re-decided every day, so holding period is 1 day or a run of same-sign days | 1 |
| Universe / eligibility filters | Single hard-coded pair `stocks = ['INFY.NS','TCS.NS']` (line 10); eligibility = rolling t-stat of spread <= t_threshold (-2.5) on the last 252 closes (lines 15, 51-52) | 1 |
| Market / regime filter | None other than the cointegration t-stat gate; when `t_opt > t_threshold` signal = 0 and the position is closed (lines 51-53) | 1 |
| Setup conditions | For t = 252..len(data)-1: fit b by Nelder-Mead minimising the t-stat of an OLS of diff_diff on lagged diff (no constant, no lagged differences) where diff = (a + b*stock1) - stock2 over rows t-252..t-1 and a = mean(stock2 - b*stock1) (lines 34-46); start value of b = stock2[t]/stock1[t] (line 43); `fair_value = a_opt + b_opt*data[stock1][t]` (line 48); gate: `t_opt <= -2.5` (line 51) | 1 |
| Entry trigger & order type | `signal = np.sign(fair_value - data[stock2][t])` (line 55): +1 = long stock2 and short stock1; -1 = long stock1 and short stock2 (lines 68-71). No entry threshold on the size of the deviation (any non-zero sign trades). Order type not stated; the return model implies execution at the close of day t, the same close used to compute the signal | 1 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Signal exit only: position goes to 0 when `t_opt > t_threshold`; flips sign when the sign of (fair_value - price2) changes; no stop, target or max-hold (lines 51-56) | 1 |
| Position sizing | Fixed +/-1 unit per leg; `gross_return = signal*returns[stock2][t] - signal*returns[stock1][t]` (line 56). The hedge ratio b_opt is NOT used to size legs (used only inside fair_value) | 1 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | One pair, one position at a time; no limits stated | 1 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| stocks | ['INFY.NS','TCS.NS'] (stock1 = INFY.NS, stock2 = TCS.NS) | none | 1 |
| start / end (data download) | '2019-01-16' / '2021-02-24' | none | 1 |
| fee | 0.001 | none; charged as `fee*abs(signal - old_signal)` (line 57) | 1 |
| window | 252 rows | none | 1 |
| t_threshold | -2.5 | none | 1 |
| Optimiser | scipy Nelder-Mead on b, start = stock2[t]/stock1[t] | none | 1 |
| Price field | `prices['Close']` (line 21) | not found whether adjusted | 1 |

**Key quotes**
- Parameters: "window = 252" and "t_threshold = -2.5" [p. 1].
- Hedge-ratio objective: "#defining the unit root function: stock2 = a + b*stock1" [p. 1].
- Optimisation: "res1 = spop.minimize(unit_root, data[stock2][t]/data[stock1][t], method='Nelder-Mead')" [p. 1].
- Gate: "if t_opt > t_threshold:" [p. 1].
- Signal: "signal = np.sign(fair_value - data[stock2][t])" [p. 1].
- Return: "gross_return = signal*returns[stock2][t] - signal*returns[stock1][t]" [p. 1].
- Cost: "fees = fee*abs(signal - old_signal)" [p. 1].

**Pseudocode** (faithful to the code; `P1`,`P2` = Close of stock1 INFY.NS, stock2 TCS.NS; `ret_i[t] = P_i[t+1]/P_i[t] - 1`, with the last element appended as 0, line 22)
```
for t in window .. N-1:                       # line 32
    # fit on rows t-window .. t-1 (row t excluded from the fit)
    unit_root(b):
        a        = mean(P2[t-w:t] - b*P1[t-w:t])
        fair     = a + b*P1[t-w:t]
        diff     = fair - P2[t-w:t]
        dd       = diff[1:] - diff[:-1]
        OLS(dd ~ diff[:-1]), no constant -> return coef / stderr   # a t-stat, expected negative
    b0    = P2[t]/P1[t]                        # uses day-t prices as start guess
    b_opt = argmin_b unit_root(b)  (Nelder-Mead);  t_opt = min value
    a_opt = mean(P2[t-w:t] - b_opt*P1[t-w:t])
    fair_t = a_opt + b_opt*P1[t]
    if t == window: old_signal = 0
    if t_opt > -2.5: signal = 0; gross = 0
    else: signal = sign(fair_t - P2[t]);  gross = signal*ret2[t] - signal*ret1[t]
    net = gross - 0.001*abs(signal - old_signal)
    old_signal = signal
equity = cumprod(1 + net)    # lines 82-83
```
signal +1 = long stock2 / short stock1; -1 = long stock1 / short stock2.

**Ambiguities & assumptions** (every code bug / look-ahead / execution issue found)
1. Same-bar signal and execution (line 55-56): the signal uses close[t] (`data[stock2][t]`, `data[stock1][t]`), and the credited return `returns[t]` is the t -> t+1 return. This is not look-ahead in the arithmetic, but it assumes the trade is filled at the very close used to compute the signal. ASSUMPTION: for NSE testing, signal at close[t], fill at close[t] with 0.1% slippage added (closest to the author), with a stricter variant filling at open[t+1].
2. Reporting date is the signal date: the "day" printed (line 64) is `data.index[t]` but the return shown is for t -> t+1. The last row's return is a fabricated 0 (np.append(..., 0), line 22). ASSUMPTION: drop the final row.
3. Hedge ratio unused in sizing: legs are +1 / -1 in return terms (line 56) although b_opt is fitted; b only affects fair_value. So the spread P&L is not the P&L of the cointegrating spread (stock2 - b*stock1) unless b is about 1. ASSUMPTION: replicate the author's equal-weight legs as the base case; test a beta-weighted variant separately.
4. Return normalisation: gross return = r2 - r1 is per 1 unit of notional on each leg (2 units gross exposure), not divided by 2. ASSUMPTION: report as given, and a version divided by 2 for capital-based returns.
5. Fee model: `fee*abs(signal - old_signal)` charges 0.001 once per unit change of signal, i.e. 0.001 to open a two-leg position, 0.002 on a flip, 0.001 to close; two legs each pay a fee in reality, so costs look understated by about half. The first row uses old_signal = 0 (line 49-50). ASSUMPTION: charge fee per leg per trade (0.002 per entry or exit, 0.004 per flip) plus STT.
6. Cointegration test is not a standard Engle-Granger test: no constant, no lagged differences (ADF with 0 lags), b chosen to minimise the t-stat (so the statistic is biased downward), and -2.5 is unexplained. The text gives no source for the threshold. ASSUMPTION: replicate exactly; flag that the gate passes more often than a calibrated test would.
7. Nelder-Mead start value uses day-t prices (line 43) while the fit window excludes day t; the minimum is local and depends on that start. Result differences are possible across scipy versions. ASSUMPTION: use the same start guess.
8. Signal has no dead zone: sign() of any deviation from the window-mean spread (a_opt makes the in-window mean deviation zero), so the position flips on small noise, creating high turnover and fee drag. Exit/entry thresholds, stops and time exits: not found in this text.
9. Data alignment: `returns[stock]` is built from positional arrays of each stock's own downloaded series (line 22) while `data` aligns on index; any date mismatch or NaN between the two tickers shifts returns. Price field is `Close` (line 21); whether adjusted for dividends/splits depends on yfinance version; not found in this text.
10. Compatibility: `float(res1.x)` on a 1-element array (line 45), `res.params[0]` and integer keys on a DatetimeIndex (`data[stock2][t]`) fail or warn on newer numpy/pandas; ASSUMPTION: use `.iloc` and `res1.x[0]`.
11. The `signal == 0` branch is printed as "no trading", `signal == 1` as long stock2 / short stock1, and else (signal -1) as long stock1 / short stock2 (lines 66-71).

### 2.2 EMA 30/75 crossover, long only (INFY, class MovingAverageCrossover)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (moving-average crossover state), long only | 2 |
| Timeframe & holding period | Daily Yahoo data; held while short EMA > long EMA (from buy bar's close to the close of the sell bar) | 2 |
| Universe / eligibility filters | One ticker, `'INFY'` (no ".NS" suffix in the call, line 94) | 2 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | EMAs of `Adj Close`: short span 30 and long span 75, `ewm(span=..., adjust=False).mean()` (lines 64-65), seeded from the first price, no warm-up or minimum-periods rule | 2 |
| Entry trigger & order type | On a row where `row.short_ma > row.long_ma and not self.is_long`: record `price_when_buy = row.Price` (same row's price) and set is_long = True, print 'Buy' (lines 54-59). State-based (not an edge-detected cross). Order type not stated; fill at that row's Adj Close | 2 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Signal exit: `row.short_ma < row.long_ma and self.is_long` -> append `self.capital * row.Price/price_when_buy` to equity, is_long = False, print 'Sell' (lines 45-51). An open position at the end of data is never closed or marked | 2 |
| Position sizing | Entire capital in one trade (no shares/lots, no cost); `capital` = 50000 is never updated | 2 |
| Adding to / pyramiding | None: `not self.is_long` blocks multiple longs (comment lines 52-53) | 2 |
| Portfolio limits (max positions, correlation, heat) | One position, one instrument | 2 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| capital | 50000 | none | 2 |
| stock | 'INFY' | none | 2 |
| start / end | datetime(2010, 1, 1) / datetime(2022, 3, 10) | none | 2 |
| short_period | 30 | none | 2 |
| long_period | 75 | none | 2 |
| EMA adjustment | `adjust=False` (recursive EMA, alpha = 2/(span+1) implicit in pandas) | none | 2 |
| Price field | 'Adj Close' | none | 2 |
| Costs | none modelled | not found in this text | 2 |

**Key quotes**
- "stock_data['Price'] = ticker['Adj Close']" [p. 2].
- "self.data['short_ma'] = self.data['Price'].ewm(span=self.short_period, adjust=False).mean()" [p. 2].
- "if row.short_ma < row.long_ma and self.is_long:" [p. 2].
- "self.equity.append(self.capital * row.Price/price_when_buy)" [p. 2].
- "elif row.short_ma > row.long_ma and not self.is_long:" [p. 2].
- "strategy = MovingAverageCrossover(50000, 'INFY', start_date, end_date, 30, 75)" [p. 2].

**Pseudocode**
```
price = AdjClose[date]
short_ma = EMA(price, span=30, adjust=False)   # recursive, seeded at first price
long_ma  = EMA(price, span=75, adjust=False)
is_long = False; equity = [capital]
for each row in date order:
    if short_ma < long_ma and is_long:
        equity.append(capital * price / price_when_buy)    # capital is constant (50000)
        is_long = False
    elif short_ma > long_ma and not is_long:
        price_when_buy = price
        is_long = True
print equity[-1]
```
Note: `equity[-1]` is 50000 times the return of the LAST CLOSED trade only. A faithful compounded equity would be `equity_after = equity_before * price/price_when_buy`.

**Ambiguities & assumptions**
1. Equity quirk (lines 48, 19): each closed trade appends `self.capital * row.Price/price_when_buy` where `self.capital` is the initial 50000 and is never updated. Entries are independent single-trade values, not a running balance; `print(strategy.equity[-1])` (line 100) is not the final wealth, and the equity plot (lines 85-88) is a per-trade list, not time-based. ASSUMPTION: compute compounded equity (running_equity *= exit/entry), and report the author's version separately only for replication.
2. Open position at the end of data is ignored (no mark-to-market). ASSUMPTION: mark to last close in our backtest.
3. Same-bar execution: signal uses the EMA including the current row's price and the trade is booked at that row's price (lines 56, 48). ASSUMPTION: fill at the signal day's close with 0.1% slippage (author-equivalent), plus a stricter variant filling at next open.
4. Entry is state-based, not a crossover event: on the first rows both EMAs are equal (seeded from the first price); the first bar where short_ma > long_ma opens a long even if no real cross occurred, and a long EMA of span 75 has not converged for roughly the first 75-ish bars. ASSUMPTION: require 75+ bars of warm-up before the first signal and treat entry as "short > long and not in position".
5. Ticker is 'INFY' (line 94), which on Yahoo is not the NSE listing 'INFY.NS' used in the pairs script; the text does not say which exchange is meant. ASSUMPTION: use NSE INFY.
6. `Adj Close` column: newer yfinance defaults can drop this column; adjusted-price basis may differ. ASSUMPTION: use split/bonus-adjusted daily close from our data.
7. No transaction cost, tax, slippage, integer lot sizing or stop; no short side (a short EMA below the long EMA just means flat). No performance numbers in the text. Anything else (position sizing, stop, filter): not found in this text.

### 2.3 Pairs script applied to ETH-USD / XRP-USD (author-run console log)
Same rules as 2.1; only the run log (pp. 3-16) is new. The log does not show the script header, so tickers are inferred from the printed lines and parameters are not confirmed.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Same as 2.1: rolling cointegration pairs trade, long/short crypto | 3 |
| Timeframe & holding period | Daily rows (7 days per week; consecutive calendar days appear, e.g. 2021-02-13, 2021-02-14); log runs 2021-02-08 to 2021-05-19 | 3, 16 |
| Universe / eligibility filters | ETH-USD and XRP-USD (stock1 = ETH-USD, stock2 = XRP-USD inferred: first printed position is "long position on XRP-USD and short position on ETH-USD" = signal +1 in 2.1 line 69) | 3 |
| Market / regime filter | Same t-stat gate; many "no trading" runs (66 of the 101 logged days; for example 2021-03-06 to 2021-03-14 and 2021-03-31 to 2021-05-02) | 6, 7, 9, 10, 11, 12, 13, 14 |
| Setup conditions | Same as 2.1; the log does not show window or threshold used (252 / -2.5 not confirmed) | - |
| Entry trigger & order type | Same as 2.1: sign of fair value minus price of stock2 | 3 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Same as 2.1: flat when gate fails (a close costs 0.1%: e.g. "net daily return: -0.1%" on a no-trade day after a position) | 6 |
| Position sizing | Equal +/-1 per leg (fee 0.1% per signal unit visible: first day gross ~.2% vs net ~.1%, i.e. 4.2% vs 4.1% reading ~ = 4) | 3 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | One pair, one position | 3 |

**Parameters** (as visible in the log only)

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Tickers | ETH-USD, XRP-USD | none | 3 |
| First logged day | 2021-02-08 | none | 3 |
| Last logged day | 2021-05-19 | none | 16 |
| Fee | 0.1% per signal unit change (consistent with fee = 0.001; not printed) | none | 3, 6 |
| Window / t_threshold | Not shown in the log | not found in this text | - |

**Reported outcome (author-run, in-sample)**
- Logged days: 101 (2021-02-08 to 2021-05-19): 35 with a position, 66 "no trading".
- Final cumulative net return printed: "cumulative net return so far: ~0.31%" [p. 16] = 40.31% on the "~ = 4" font reading, on 2021-05-19. The log shows no summary, no Sharpe, drawdown or trade count, and the plot is not in the text.
- Path (readings of "~" as 4): first day 2021-02-08 net ~.1% = 4.1% [p. 3]; low about -8.64% on 2021-02-12 [p. 3]; 37.2% on 2021-03-16 [p. 7]; fell to 10.94% by 2021-03-31 and stayed there to 2021-05-02 with no trading [p. 9, 10]; high 45.59% on 2021-05-15 [p. 15]; ended 40.31% on 2021-05-19 [p. 16].
- Large single-day swings: net -12.62% on 2021-02-11 [p. 3] and -11.31% on 2021-03-21 [p. 8]; +16.62% on 2021-05-14 (read) [p. 15].
- Last-day caveat: the log does not show whether 2021-05-19 is the final data row; if it is, its return would be the appended 0 (see 2.1 item 2). The log is also labelled by signal date (return is t -> t+1).

**Key quotes**
- "long position on XRP-USD and short position on ETH-USD" [p. 3].
- "cumulative net return so far: ~0.31%" [p. 16].
- "net daily return: -12.62%" [p. 3].
- "gross daily return: 16.72%" [p. 15].

**Pseudocode**: identical to 2.1 with stock1 = ETH-USD, stock2 = XRP-USD.

**Ambiguities & assumptions**
1. Font renders 4 as "~" (also "li", "l.i", "M"), so every number containing a 4 is a reconstruction; digits in the log with no 4 are unaffected. ASSUMPTION: "~" = 4. Cross-check done: day 1 gross ~.2% -> net ~.1% matches a 0.1% entry fee, and 1.041 x 1.0801 = 1.1244 matches "12.~~%" (12.44%).
2. Gross 100% long and 100% short in highly volatile crypto with daily re-hedge at equal weights; returns are per unit of one leg. Result is one in-sample 3.5-month run: no out-of-sample claim, no costs beyond 0.1% per signal-unit.
3. Parameters of the crypto run (window, threshold, start date of download, fee value) are not in the log; the 2.1 values are an ASSUMPTION. Look-ahead and execution issues of 2.1 (same-close fill, equal weights, fee per unit) apply identically here. Crypto trades 24/7 so a "close" is a UTC 00:00 snapshot.

## 3. Risk & money-management rules
- No stop-loss, drawdown limit, volatility scaling or exposure cap in either script. Not found in this text.
- Pairs: fixed +/-1 per leg [p. 1]; fee 0.001 per signal-unit change [p. 1].
- EMA: all capital in one trade, capital fixed at 50000 [p. 2]; no costs modelled [p. 2].

## 4. Non-codable guidance
- None; the bundle is code and a run log only. The only comments are code comments describing the EMA logic [p. 2] and the interface printing "no trading" / positions [p. 1].

## 5. Adapting to NSE (Indian equities)
- **Data required:** daily OHLCV for INFY and TCS (Close/open for fills) for 2005-2026; for the EMA: adjusted close for any NSE stock universe. No delivery %, index or fundamentals needed.
- **Testability with our data:**
  - 2.2 EMA 30/75 crossover is fully backtestable on our daily panel (long-only, cash delivery, no overnight shorting needed); can be run on INFY and extended to all ~3,700 stocks, with costs (STT, brokerage, about 0.1% slippage) added, correct compounding and warm-up.
  - 2.1 pairs strategy needs simultaneous long and short legs held overnight. That is not possible in the NSE cash market; it would require single-stock futures, for which we have no data. Only a synthetic (frictionless, paper) test of the long-short return series from our INFY and TCS prices is possible, as a measure of signal quality, not as a tradable result. ASSUMPTION: if run synthetically, add 0.1% slippage per leg plus futures-style costs at an assumed rate; mark the results as non-tradable.
  - 2.3 ETH/XRP: crypto data is not in our dataset; the log is the only evidence, in-sample and un-reproducible here.
- **Market-structure differences:** circuit limits can block fills on either leg; cash shorting is intraday only (a leg-by-leg intraday version would need minute data, not available); lot sizes and margin for futures; STT/brokerage; the 252-day window equals about 1 trading year on NSE but about 8.3 months on 7-day crypto data (the log uses calendar-day rows, so window 252 is not comparable). ASSUMPTION: for NSE use 252 trading rows.

## 6. Verdict
- **Codeability:** Fully (both scripts are complete code; every rule is explicit); but the pairs strategy is only partly implementable on NSE cash because of the short leg.
- **Priority for backtesting:** Low for the pairs strategy (not tradable in cash, no futures data, crypto result in-sample); Medium-Low for the EMA 30/75 crossover (simple single-instrument benchmark, easy to run across the full universe with correct compounding).
- **Top 3 things a coder is most likely to get wrong:**
  1. Replicating the EMA equity "quirk": using initial capital instead of running equity gives a meaningless final value; also omitting the end-of-data open position and EMA seeding/warm-up.
  2. Pairs timing and sizing: signal and fill on the same close with the t -> t+1 return, equal +/-1 legs although b_opt is fitted, and the last-row 0 return.
  3. Reading the ETH/XRP log with "~" = 4 (and "li", "l.i", "M"), and treating its result (40.31%) as tradable evidence; also fees applied once per signal change rather than per leg.
