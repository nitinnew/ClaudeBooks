# New Trader, Rich Trader — Steve Burns & Holly Burns

- **Source file:** Google Drive New-Trader-Rich-Trader-PDF.pdf (125 pages; Stolly Media, 2017)
- **Text file used:** text/burns_new_trader_rich_trader.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/<key>.md text/<key>.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read the whole file, lines 1-2992 (end of file), through the last marker [[PAGE 125]]. Blank page: p. 1. Title/divider/front-matter pages with no method content: pp. 2-6, 9-10, 16, 35-36, 57, 63-65. Caption-only pages (chart images not in the text; the five uptrend charts and five downtrend charts the author studied cannot be inspected): pp. 97-105. Back matter (course adverts, author bio): pp. 122-125. Nothing was skimmed. *Coordinator check: the coordinator re-ran verify_citations (27/27 ok) and an exact-page strict check (0 off-by-one), and confirmed all six 2.x field tables have exactly the 12 template rows. 13 unquoted citations were spot-checked by grep (5% initial stop p.107, 20% sizing p.107, 7-10% stop p.69, 5 million shares p.95, 1 million shares p.27/50/69, 3% under the 10-day MA p.117, gross-profits payoff p.45, 200-day filter p.80, RSI p.77/92, 60% wins p.117, +42.6% p.118-119, earnings run-up p.59-60); all matched.*

## 1. The method in brief

The book is a parable (New Trader learns from Rich Trader) in three parts: Psychology (ch. 1-5), Risk (ch. 6-10) and Methodology (ch. 11-18). It is mostly a primer on process, not a rulebook. The one concrete system is built by New Trader in ch. 16 [p. 95-108] and then critiqued by Rich Trader in ch. 18 [p. 117-119]. It is a long-only, end-of-day trend-following system on a watchlist of "leader" growth stocks in established uptrends, using the 10-day moving average as entry zone and trailing stop, a 5% initial stop, 20% position size (1% account risk) and an S&P 500 moving-average regime filter. The authors' philosophy is trade the trend and do not predict: price and volume are the only signals [p. 86], trend traders win only 40%-60% of trades but win big and lose small [p. 93], and risk per trade should be 1% (2% if aggressive) of capital [p. 45].

Evidence is thin and hypothetical. New Trader's paper-trading record is 50 trades, 60% winners, payoff ratio a little over 2:1, +42.6% on $10,000, achieved in a rising market [p. 117, 118]. Rich Trader says to expect only about 20%-25% after costs and slippage [p. 119]. A first set of 10 test trades (7 wins, 3 losses, +$1,650) [p. 37, 38] is explicitly too small to prove anything. Other signals are mentioned as the mentor's personal favourites without parameters (10/50-day MA crossover, oversold reversion near RSI 30 or far from the 10-day EMA, breakouts of bases to all-time highs) [p. 77]. The book says nothing on short-side parameters beyond mirror-image remarks, and Rich Trader doubts the value of shorting [p. 119].

## 2. Strategies

### 2.1 Growth-leader 10-day MA trend system (New Trader's final system)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following on growth/momentum leaders; long only, pullback-to-support or breakout-through-MA entries | 106, 107 |
| Timeframe & holding period | Daily charts. Hold while the stock stays above its 10-day MA; "profits run" until the 10-day MA is lost; no fixed holding period. Rich Trader's own style: decisions in the first and last hour, end-of-day signals | 76, 107 |
| Universe / eligibility filters | Leaders in the hottest industries; within 5% of all-time high; trades over 5 million shares/day; earnings and/or sales up over 20% year over year for the same quarter; new product or business model with an edge. Earlier note: double-digit YoY earnings growth, at least 1 million shares/day, major exchanges only, no illiquid penny stocks. Stable chart: price above the 10-, 20- and 50-day MAs; has not lost the 50-day MA in the past six weeks; spends over 80% of time above the 10-day MA; 10-day MA has held for at least 10 trading days; low daily volatility (no large daily swings). Bollinger Bands (20-day MA, 2 standard deviations): price mostly along the top band | 69, 95, 96, 106 |
| Market / regime filter | Trade the system only when the S&P 500 has the 10-day MA above the 20-day MA and price above the 50-day MA. General advice: long only when the index is above its 200-day MA | 80, 107, 108 |
| Setup conditions | Stock is on the watchlist (all filters above) and in an established uptrend | 96, 107 |
| Entry trigger & order type | Buy as the stock trends up through the 10-day MA or bounces off it as support. A 5% price buffer is used "to filter out most of the random noise" at the buy point. Order type for this system is not stated; an earlier plan used an automatic buy stop at the start of an uptrend | 28, 107 |
| Initial stop-loss | 5% below the purchase price. At a 20% position this risks 1% of trading capital | 107 |
| Exits: profit-taking | No fixed target. The trade is exited when the trailing stop is hit; "sell when it pulled back to the 10-day moving average" produced the $30 exit in the example | 107, 118 |
| Exits: trailing / time / signal | Once the stock is trending 5% above the 10-day MA, set the stop at the current 10-day MA and move it up or down with the MA. This is also the sell signal when the trend reverses. Rich Trader suggests testing a stop 3% under the 10-day MA, or a 20-day MA stop. Added rule: do not hold through earnings | 107, 117, 118 |
| Position sizing | 20% of trading capital per trade ($2,000 on a $10,000 account); position size to grow as the account grows | 107 |
| Adding to / pyramiding | Not found in this text for this system. General rule: "Never add to a losing trade" | 120 |
| Portfolio limits (max positions, correlation, heat) | Not stated. Watchlist of five stocks; 20% size implies at most 5 positions; mentor uses 10%-20% sizes in most stocks | 77, 96, 107 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Proximity to all-time high | within 5% | "close to all-time highs" | 95 |
| Minimum share volume | 5 million/day | 1 million/day in other lists | 27, 50, 69, 95 |
| YoY earnings/sales growth | over 20% same quarter | "double-digit" earnings increases | 69, 95 |
| Entry MA | 10-day | 20-day, 21-day, 50-day also discussed | 67, 92, 107 |
| Bars above 10-day MA | over 80% of time | 10-day MA held at least 10 trading days | 96, 106 |
| 50-day MA not lost | past 6 weeks | - | 96 |
| Bollinger Bands | 20-day MA, 2 std dev | - | 96 |
| Initial stop | 5% below entry | 3% under the 10-day MA; 20-day MA stop; 7%-10% stop in growth-investing notes | 69, 107, 117 |
| Trailing stop switch | price 5% above the 10-day MA, then trail at 10-day MA | - | 107 |
| Position size | 20% of capital | 10%-20% | 69, 77, 107 |
| Risk per trade | 1% of capital | 2% (aggressive) | 45, 107 |
| Market filter | S&P 500 10-day MA over 20-day MA and price over 50-day MA | 10-day over 50-day; price over 200-day | 50, 80, 107, 108 |
| Earnings | do not hold through earnings | - | 118 |
| Reported results (paper) | 60% wins, payoff just over 2:1, avg win $212, avg loss $105, largest win $500, largest loss $125, +42.6% in 50 trades | expect 20%-25% live | 117, 118, 119 |

**Key quotes**
- "he would set a stop loss 5% below his purchase" [p. 107]
- "with a 20% position size of his total trading capital" [p. 107]
- "he would set the stop at the current 10-day" [p. 107]
- "the 10-day moving average above the 20-day moving average" [p. 107]
- "They were within 5% of all-time highs in price." [p. 95]
- "They each traded over five million shares a day, some much" [p. 95]
- "Volatility was not going to be his friend in a trend trading system." [p. 106]
- "you could experiment with 3% stops under the 10-day moving average" [p. 117]
- "add a rule that I don’t hold" [p. 118]
- "Your payoff ratio was a little over 2:1." [p. 117]

**Pseudocode**
```
# daily bars; run after the close, orders for next open (ASSUMPTION)
idx = NIFTYBEES (or equal-weight stock-panel index)              # S&P 500 proxy
regime_ok = SMA(idx,10) > SMA(idx,20) AND idx.close > SMA(idx,50)  # p107-108

watchlist(t) = stocks where:
   close >= 0.95 * max(high, all history to t)                     # p95
   AND turnover filter                                             # p95, ASSUMPTION for INR
   AND close > SMA10 AND close > SMA20 AND close > SMA50           # p96
   AND min(close[-30:] - SMA50[-30:]) > 0                           # 6 weeks, p96
   AND fraction(close > SMA10 over last N bars) > 0.80             # p96, N = ASSUMPTION 60
   [optional growth screen: YoY EPS/sales > 20%]                   # p95, forward-test only

ENTRY (regime_ok AND stock in watchlist AND no open position):
   trigger A: close crosses above SMA10 from below                 # "trended up through" p107
   trigger B: low <= SMA10*(1+tol) AND close > SMA10               # "bounced off" p107, tol = ASSUMPTION 1%
   buy next open
   size = 20% of equity                                             # p107
   stop = entry * 0.95                                              # p107

MANAGE each day:
   if high >= SMA10 * 1.05 at any time since entry: trailing = True # p107
   if trailing: stop = SMA10 (recomputed daily, may fall)           # p107
   exit if close < stop (ASSUMPTION: closing basis; p106 "didn't recover before the close")
   exit before earnings date (ASSUMPTION: needs earnings calendar)  # p118
   no pyramiding
```

**Ambiguities & assumptions**
- The book never says whether the 5% initial stop ratchets to the 10-day MA only after price is 5% above the MA, or whether the 5% above MA refers to price vs entry. Book says "started trending 5% above the 10-day moving average" [p. 107]. ASSUMPTION: trigger once any close is at least 5% above the current 10-day SMA; before that the fixed 5% stop applies.
- The p. 106-107 sentence "buy stocks on his watchlist at the 10-day moving average, when it was breached and didn't recover before the close" is internally confusing: it reads like an exit/stop condition and also like a re-entry. ASSUMPTION: treat it as a closing-basis exit when close < SMA10 (and below the entry buffer), with re-entry allowed on a fresh cross/bounce.
- Growth filters (20% YoY EPS/sales) and the "new product / edge" and "hottest industries" filters are qualitative or fundamental. ASSUMPTION: replace by a price-based leadership screen (within 5% of all-time high, positive 6-12 month relative strength vs index); fundamentals forward-test only.
- Volume 5 million shares (p. 95) vs 1 million (p. 27, 50, 69). ASSUMPTION: use the 5 million rule scaled to an INR turnover threshold on NSE; test 1 million as a looser variant.
- Stop 5% (p. 107) vs 7%-10% (p. 69) vs 3% under the 10-day MA or a 20-day MA stop (p. 117). ASSUMPTION: base case 5% initial stop and 10-day trailing; run 3% under MA and 20-day MA as variants as the mentor suggests.
- Market filter differs between pages (10>20 and >50 on p. 107-108; 10>50 on p. 50; price>200-day on p. 80). ASSUMPTION: use the p. 107-108 filter as base case since it belongs to this system.
- "10-day" vs "21-day" MA (p. 67) vs "20-day" elsewhere: ASSUMPTION: 20-day SMA is the 20-day; ignore the 21-day.
- SMA vs EMA is unstated for the MAs. ASSUMPTION: simple MAs (the 10-day EMA is named only for the mean-reversion setup, p. 77).
- Order type and fills: not found in this book for the final system. ASSUMPTION: market buy at next open after a close-based signal.
- Max positions, correlation limits and portfolio heat: not found in this book. ASSUMPTION: max 5 positions (5 x 20% = 100%; total heat 5 x 1% = 5%).

### 2.2 Moving-average trend following (10/50-day crossover and long-term MA filters; Rich Trader's own approach)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following, MA crossover, mostly on stock indexes/ETFs | 73, 77 |
| Timeframe & holding period | Daily; signals evaluated at end of day, adjusted only in the first or last hour; trades held weeks to months | 50, 73, 76 |
| Universe / eligibility filters | Stock indexes (stated for his own system); a diversified index may take a bigger position; for stocks, high-volume names | 73, 77, 83 |
| Market / regime filter | Long when 10-day MA is above the 50-day MA; reverse is bearish; or price above the 200-day MA for long-term uptrend | 50, 80 |
| Setup conditions | 10-day MA crosses over the 50-day MA; also price rising above long-term MAs (200-day, 250-day) signals a new uptrend | 77, 92 |
| Entry trigger & order type | Crossover of 10-day over 50-day; order type not stated | 77 |
| Initial stop-loss | Not found in this text for this system (generic rule: set the stop before the trade, risk 1%) | 45, 50 |
| Exits: profit-taking | "Trend traders ... take profits when trailing stops are hit"; no target | 59 |
| Exits: trailing / time / signal | Trailing stop; sell when price falls through a moving-average support; or a new low for a certain number of days (value not stated) | 59 |
| Position sizing | 10%-20% in most stocks and leveraged vehicles; bigger in a diversified index | 77 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | "I don't have a portfolio of stocks, I have trades and trading systems"; no numeric limit | 77 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fast/slow MA | 10-day / 50-day | 100-day, 200-day for indexes | 67, 77 |
| Long-term trend filter | price vs 200-day MA | 250-day MA | 80, 92 |
| Uptrend definition (stock) | price above 50-day MA | downtrend: price under 200-day MA | 90 |
| Exit lookback ("new low for a certain number of days") | not stated | - | 59 |
| Position size | 10%-20% | larger for diversified index | 77 |

**Key quotes**
- "I currently utilize a trend trading system using stock indexes." [p. 73]
- "crossing over the 50-day moving average as powerful trend" [p. 77]
- "moving average over the 50-day moving average is a good sign" [p. 50]
- "if price is above the 200-day moving average line, then you should be" [p. 80]
- "I like to limit risk exposure with only 10%-20% position sizes in" [p. 77]

**Pseudocode**
```
long_signal  = SMA(close,10) crosses above SMA(close,50)          # p77
exit_signal  = close < trailing_stop                              # p59
              OR SMA10 < SMA50 (ASSUMPTION, reverse cross)         # p50 "reverse is bearish"
              OR close < lowest(close, N) with N = ASSUMPTION 20   # p59 "new low for a certain number of days"
size = 10-20% equity (ASSUMPTION 20% stock, larger for broad ETF)
initial_stop = ASSUMPTION 5% below entry (borrowed from 2.1)
optional filter: idx.close > SMA(idx,200)                          # p80
```

**Ambiguities & assumptions**
- The book names the crossover but gives no exit, stop, or order details for it. ASSUMPTION: exit on reverse crossover (10-day below 50-day) or the trailing stop, whichever comes first.
- It is unclear whether crossover trades apply to individual stocks or only indexes. The mentor says his own system uses indexes [p. 73] but lists the crossover among his favourite signals [p. 77]. ASSUMPTION: test both NIFTYBEES/sector ETFs and liquid stocks.
- "New low for a certain number of days" has no value. ASSUMPTION: 20-day low as exit.
- The book also says "Three or four" indicators are plenty [p. 87]; no further parameters.

### 2.3 Pullback to moving average / Bollinger band support in an uptrend

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback entry (buy support) | 92, 94 |
| Timeframe & holding period | Daily; hold while support holds | 92 |
| Universe / eligibility filters | Watchlist stocks verified to be in an uptrend; ideally high volume leaders | 81, 92 |
| Market / regime filter | Be long in uptrends (S&P 500 or NASDAQ above 200-day MA) | 80, 92 |
| Setup conditions | Price has found support at the 10-day or 20-day MA over the last two months; or at the bottom of a Bollinger band that has held for a couple of months; or a specific price level | 81, 92 |
| Entry trigger & order type | Buy at the 20-day (or 10-day) MA inside a longer uptrend; "Don't hesitate, buy it when your signal says to" (order type not stated) | 81, 92 |
| Initial stop-loss | Not found in this text for this setup (see 2.1: 5% or under the MA) | 107 |
| Exits: profit-taking | Sell at the top of a Bollinger Band, or when an oscillator such as RSI reads overbought | 92 |
| Exits: trailing / time / signal | Let it ride if it does not lose the 20-day MA again; MA-based stop | 92 |
| Position sizing | Not specific; 1% risk rule | 45 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Support MA | 20-day | 10-day, 50-day, bottom Bollinger band | 81, 92 |
| Verification | price found support at the MA and rose in the last two months | - | 92 |
| Profit exit | upper Bollinger band / RSI overbought (level not stated) | - | 92 |
| Bollinger | 20-day, 2 std dev | - | 96 |

**Key quotes**
- "your system can consist of buying at the 20-day moving average" [p. 92]
- "or you can sell when it reaches the top of a Bollinger Band, or when it" [p. 92]
- "pullback was usually at the 10-day moving average." [p. 68]

**Pseudocode**
```
uptrend = close > SMA50 AND SMA50 rising AND idx regime ok
support_confirmed = in last 40 bars, >=2 touches where low<=SMA20*1.01 and close>SMA20 followed by higher close   # ASSUMPTION
entry: uptrend AND support_confirmed AND low<=SMA20*(1+0.01) AND close>SMA20 -> buy next open
stop: close < SMA20 (or 5% below entry; ASSUMPTION)
profit exit: close >= BB_upper(20,2) OR RSI(14) >= 70 (ASSUMPTION: 70)
```

**Ambiguities & assumptions**
- "Verified support" is a discretionary chart judgment. ASSUMPTION: at least two prior touches-and-bounces on the 20-day SMA within 40 bars.
- RSI period/overbought level not in book. ASSUMPTION: RSI(14) at 70.
- No stop value specified for this setup. ASSUMPTION: close below the 20-day SMA, or 5% from entry, whichever is closer.

### 2.4 Breakout to new high after a tight base (volume confirmation)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout / momentum | 90, 94 |
| Timeframe & holding period | Daily; hold as long as the trend lasts (day to over a year) | 28, 90 |
| Universe / eligibility filters | Highest-volume stocks and ETFs; leaders near all-time highs; liquid (1 million shares/day) | 27, 90 |
| Market / regime filter | Trade with the market trend | 80, 83 |
| Setup conditions | Stock in a tight range for a few months (example $95-$100) | 90 |
| Entry trigger & order type | Break to a new all-time high (example $101) on twice the average daily volume; an automatic buy stop at the beginning of the uptrend | 28, 90 |
| Initial stop-loss | Earlier plan: risk 2% of account (40 cents/share on a $9.35 entry, 500 shares). Final system: 5% | 27, 107 |
| Exits: profit-taking | Trail a stop and take profits if the stock pulls back 5% from its high (early plan); or sell on MA break | 27 |
| Exits: trailing / time / signal | 5% trailing pullback (early plan) | 27 |
| Position sizing | Early plan: $5,000 position on a $10,000 account; risk 2% ($200). Later 20% | 27, 107 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Base | tight range for a few months | - | 90 |
| Breakout volume | 2x average daily volume | - | 90 |
| Trailing pullback | 5% from high | - | 27 |
| Risk | 2% of account | 1% | 27, 45 |
| Liquidity | 1 million shares/day; daily range under 4% (or 5%) | 5 million in 2.1 | 23, 27 |

**Key quotes**
- "suddenly breaks to a new all-time high of $101, on twice" [p. 90]
- "would buy at the break to a new high, or when it breaks resistance of a" [p. 26]
- "He decided to put in a buy stop so that the stock would be" [p. 28]
- "He thought the best plan would be to trail a stop loss and take profits if it" [p. 27]

**Pseudocode**
```
base = (max(high,60) - min(low,60)) / close <= 12%             # ASSUMPTION: "tight range for a few months"
trigger: close > max(high, all history before today) AND volume >= 2 * SMA(volume,50)   # avg window ASSUMPTION 50
buy next open (or buy-stop at prior high + tick)
stop: entry - 5% (ASSUMPTION; early plan 2% account risk)
exit: close <= highest_close_since_entry * 0.95                 # p27 trailing 5%
```

**Ambiguities & assumptions**
- The book's early plan (New Trader) is his own pre-testing sketch and he says it was "too subjective" to program [p. 28]; the $95-$100 example is Rich Trader's illustration [p. 90]. "Tight" and "few months" are not quantified. ASSUMPTION: 60-bar range under 12%.
- Average volume window not given. ASSUMPTION: 50 days.
- The 5% trailing is measured from the high in the early plan; in 2.1 it is measured from the 10-day MA. ASSUMPTION: keep as separate variants.

### 2.5 Oversold mean-reversion in an uptrend (RSI near 30 / far below the 10-day EMA)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion within a long-term uptrend | 77, 94 |
| Timeframe & holding period | Daily; short swing (not stated) | 77 |
| Universe / eligibility filters | Market or stock in a historical uptrend | 94 |
| Market / regime filter | Not found in this text for this setup | - |
| Setup conditions | "oversold price levels extended far from the 10-day EMA and/or near the 30 RSI" | 77 |
| Entry trigger & order type | Buy the deep dip / long-term price support level; order type not stated | 94 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | "reversion to the mean" (target not stated; presumably back to the 10-day EMA) | 77 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | 10%-20% | 77 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RSI level | about 30 | RSI length not given | 77, 94 |
| Distance from 10-day EMA | "far" (not quantified) | - | 77 |

**Key quotes**
- "My favorite signals are oversold price levels extended far from" [p. 77]
- "attempts to create a good risk/reward ratio based on buying a deep dip" [p. 94]

**Pseudocode**
```
uptrend = close > SMA200 (ASSUMPTION)
oversold = RSI(14) <= 30 OR close < EMA10 * (1 - k)        # k = ASSUMPTION 8%
buy next open if uptrend AND oversold
exit: close >= EMA10 (mean reversion) OR stop 5% below entry (ASSUMPTION)
```

**Ambiguities & assumptions**
- The book gives only the idea; RSI period, distance threshold, uptrend definition, stop and exit target are not found in this book. All values above are ASSUMPTION and the strategy should be treated as exploratory.

### 2.6 Earnings run-up swing (buy before earnings, sell at historical run-up range)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Event-driven swing | 59, 60 |
| Timeframe & holding period | Buy about a month before the earnings announcement and exit before/at the announcement | 59, 118 |
| Universe / eligibility filters | Stocks whose pre-earnings moves are consistent (example: last four runs of +8%, +7%, +10%, +12% in the four weeks before earnings) | 59 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Known earnings date; historical run-up ranges for the stock | 59 |
| Entry trigger & order type | Buy a month before earnings (exact trigger not stated) | 59 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Take profits when the stock is up in the historical range; at 10% up "you already have all the profits you're going to get" | 59, 60 |
| Exits: trailing / time / signal | Stop at 7% gain if the stock retraces after being up 8% or more; exit before the announcement | 59, 60 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry timing | about 1 month before earnings | - | 59 |
| Profit-taking zone | historical range (example 7%-12%) | take profit near 10% | 59, 60 |
| Profit-locking stop | exit if retraces to +7% after reaching +8% | - | 59, 60 |

**Key quotes**
- "If you’re up 10% in this trade, the" [p. 60]
- "I had much better risk adjusted returns playing the expectation" [p. 118]

**Pseudocode**
```
for each stock with earnings date E:
   buy at close of E - 21 trading days            # ASSUMPTION for "a month before"
   hist_move = median(run-up over prior 4 announcements)
   target = hist_move
   if max_gain >= 8% and gain <= 7%: exit
   if gain >= min(target, 10%): exit
   exit at close of E - 1 regardless
```

**Ambiguities & assumptions**
- Needs a point-in-time earnings calendar, which we do not have. Initial stop and size are not found in this book. ASSUMPTION: 5% initial stop and 1%-risk sizing from section 3. The mentor gives this as an example, not a defined system.

## 3. Risk & money-management rules

| Rule | Page |
|---|---|
| Risk no more than 1% of capital per trade; 2% at most if aggressive ("maybe 2% if I wanted to be aggressive") | 45 |
| Never lose more than 1% on any one trade; start with the price where you are proven wrong and work back to position size ($100,000 account: $1,000 max loss) | 52 |
| Golden rule: do not lose more than 1% to 2% of capital on one trade | 120 |
| Determine the stop loss before placing the trade and honor it | 50 |
| Use the same capital position size on every trade | 50 |
| Growth-investing note: cut losses at predetermined 7%-10% maximum, with a position size of 10%-20% of capital | 69 |
| Rich Trader's own position size 10%-20% in most stocks and leveraged vehicles, larger in a diversified index | 77 |
| Early plan risk: 2% of account, $200 on a $5,000 position (40 cents/share on 500 shares) | 27 |
| Payoff ratio: hard to succeed under 1.5; most traders want at least 2:1 reward-to-risk | 45 |
| Payoff ratio defined as average win / average loss, but also described as gross profits / gross losses (contradiction) | 45, 75 |
| Keep stats: win %, payoff ratio, largest win/loss, average win/loss, largest and average % drawdown, longest losing and winning streaks, total % profit by period | 75, 76 |
| Drawdown arithmetic: a 20% loss needs 25% to recover; 50% needs 100% | 44, 45 |
| Testing: at least 30 trades across different market types; 50 to 100 hypothetical trades for a back test; 100 trades to see patterns; equity curve growing over a year | 20, 70, 76, 81 |
| Test on paper/simulator first, then trade small and slowly raise size | 74, 82 |
| Only trade stocks over 1 million shares/day; options with open interest over 1,000 contracts | 50 |
| Bid/ask spread under 0.10 is good, a penny or two ideal | 48 |
| Trade with the market trend: long in uptrends, short in downtrends or cash; 10-day MA above 50-day MA = uptrend; index above 200-day MA = long | 50, 80 |
| Use margin only to put on more trades of equal size, never one large trade | 50 |
| Avoid overnight/earnings risk: go to cash before after-hours announcements; do not hold through earnings | 50, 118 |
| Prefer lower-beta, slow stocks with consistent daily ranges | 50, 51 |
| Never add to a losing trade; do not trade something you do not understand | 120 |
| Do not change the plan during market hours; adjustments only in off hours | 39 |
| Honor the first planned stop; when a stock gaps below the stop, sell | 60, 115 |
| Costs: $20 commission on a $2,500 trade is 0.8%; use a per-share broker (about $1 per 100 shares) | 118 |
| Expected live return after costs: roughly 20%-25% in bull markets; realistic range for a good trader 10%-25% per year | 14, 119 |
| Double-check order entry (size, symbol, direction); have backup broker phone and internet | 49, 51 |

## 4. Non-codable guidance

- Realistic expectations: first-year losses are "tuition"; 10%-25% per year is good; focus on process, not profits [p. 14].
- Manage stress by cutting size or doing more testing; if unsure, do nothing [p. 19, 21].
- Trade only to make money, not for entertainment; plan while the market is closed, trade the system while it is open [p. 24, 25].
- Write a trading plan covering entry, exit, risk, size, universe, holding time and testing [p. 26-28].
- Keep a trading journal with feelings and rule breaches; stay humble; study hours daily [p. 32, 33].
- Be a business person, not a gambler; "Be the casino" [p. 39, 40, 41].
- Ego is the enemy: honor stops, never hope for a bounce, do not need to be right [p. 54, 60, 115].
- Rich Trader's psychology rules: read the plan daily, no distractions, no prediction, no hindsight, respect the market [p. 61].
- Choose a style that fits your personality (pullback buyer vs breakout buyer) and do not hop between systems [p. 73, 74].
- Do not predict; follow price and volume; limit indicators to three or four [p. 86, 87].
- Think in points, not dollars, while trading [p. 80].
- Five dynamics for high probability: trade with market trend, let the system decide, buy only at sweet spots, be an expert in the method and stocks, trade where the volume is [p. 83].
- Persevere; most quit [p. 66, 111].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily OHLCV for stocks (close, high, low, volume; traded value for the liquidity filter); NIFTYBEES or an equal-weight index from the stock panel as the "S&P 500" for the regime filter; optional delivery % as a liquidity/quality proxy; earnings announcement dates (not in our data); fundamentals (YoY EPS and sales growth) only for forward testing.
- **Testability with our data:**
  - Backtestable 2005-2026 on prices alone: 2.1 (without the growth screen), 2.2, 2.3, 2.4, 2.5, and the market filters (using NIFTYBEES or panel index).
  - Forward-test only: the 20% YoY earnings/sales growth screen (fundamentals are point-in-time only from Feb 2026, 3-year growth fields from May 2026).
  - Needs data we do not have: earnings calendar for "do not hold through earnings" and 2.6; analyst expectations; industry-group ranking ("hottest industries"); beta data (computable from the panel).
  - The five uptrend and five downtrend example charts (pp. 97-105) are images not present in the text.
- **Market-structure differences:**
  - Shorting: the book's downtrend mirror (price under 200-day MA, bottom Bollinger band) cannot be traded as overnight shorts in the NSE cash market. ASSUMPTION: long only, go to cash when the regime filter fails. The author himself sees little value in shorting [p. 119].
  - Liquidity: the 5 million (or 1 million) shares/day rule does not translate directly because INR prices differ. ASSUMPTION: require minimum average daily traded value (e.g. above a chosen INR crore threshold) and test two levels.
  - Costs: the book stresses commissions and slippage [p. 117-118]. ASSUMPTION: model STT, brokerage and about 0.1% slippage each side; with a 5% stop and many whipsaws around the 10-day MA, turnover will be high.
  - Circuit limits: a stop cannot be executed in a locked circuit; gap risk is larger than in the book. ASSUMPTION: assume stop fills at next available open (gap price) rather than the stop price.
  - Regime proxy: NIFTYBEES for the S&P 500; panel index before. ASSUMPTION.
  - Leverage: the book allows margin but advises equal-sized trades only; ASSUMPTION: no leverage in the backtest.
  - Earnings: Indian quarterly results dates are lumpy; skipping earnings requires a calendar; ASSUMPTION: omit in the first test and, as a variant, exit when abnormal volume or a gap above 8% appears the day after results (not in book).

## 6. Verdict

- **Codeability:** Partly. One system (2.1) is specified well enough to code (MA entries, 5% stop, 10-day trail, 20% size, index filter); the growth and "hottest industry" filters are qualitative and fundamental, and the other setups (2.2-2.6) give only signal names without full exits.
- **Priority for backtesting:** Medium. The 10-day MA trail with a 5% stop on near-high stocks is a simple, plausible momentum test and the index filter is clear, but the book's evidence is a 50-trade paper record in a bull market and several parameters are inconsistent.
- **Top 3 things a coder is most likely to get wrong:**
  1. Mixing up the initial stop and the trailing stop switch: the stop is 5% below entry until price is 5% above the 10-day MA, then it becomes the 10-day MA itself (which may be below the entry price) [p. 107].
  2. Using the wrong market filter or MA type: three different filters appear (10>20 and price>50 on p. 107-108, 10>50 on p. 50, 200-day on p. 80), and the volume threshold changes (1 million vs 5 million shares).
  3. Treating the growth criteria and "leader" selection as codable: the 20% YoY growth rule cannot be backtested on our data, and the stable-stock tests (over 80% of days above the 10-day MA, 50-day MA not lost in six weeks) must be implemented as lookbacks with assumed window lengths.
