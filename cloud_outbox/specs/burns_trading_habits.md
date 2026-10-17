# Trading Habits: 39 of the World's Most Powerful Stock Market Rules — Steve Burns & Holly Burns

- **Source file:** Google Drive: Trading_Habits_39_of_the_Worlds_Most_Powerful_Stock_Market_Rules.pdf (64 pages; Stolly Media, 2015)
- **Text file used:** text/burns_trading_habits.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/burns_trading_habits.md text/burns_trading_habits.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read lines 1-1254 (the whole file) in two chunks; last `[[PAGE 64]]` reached; nothing skimmed. Blank pages (no text layer): 1, 6, 49 (cover/image pages). Pages 2 and 64 are very short (title / table of contents). Page 49 sits between rule 28 (p.48) and rule 29 (p.50) and may be an image page, so a chart or caption there, if any, could not be read. *Coordinator check: the coordinator re-ran verify_citations (26/26 ok) and an exact-page strict check (0 off-by-one). 13 unquoted section-3 and 2.x citations were spot-checked by grep (break-even win rates p.12, 1% rule p.53, $120/200-share example p.54, three-trade/3% cap p.55, drawdown design p.42, 10-day range p.59, no averaging down p.57, 70 RSI example p.58, 50%/100% recovery p.50, earnings caveat p.15, 200-day SMA p.28, gap rules p.25-26); all matched. All five 2.x field tables have exactly the 12 template rows (correction, 2026-10-17: an earlier version of this note said 2.1 and 2.4 had an extra row; that came from a row-count script that also matched Parameters rows whose names begin with 'Entry').*

## 1. The method in brief

The book is a list of 39 short rules, not a single mechanical system. The author (Steve Burns) is an end-of-day, long-term trend follower who prefers moving averages, support/resistance, RSI and MACD signals over opinions [p. 13]. The rules combine into a loose trend-following framework: trade in the direction of the long-term trend (weekly chart first, then daily) [p. 17]; use the 200-day SMA as the line between uptrend and downtrend [p. 28, 29]; enter on breakouts, initial strength, gaps or pullbacks to key levels [p. 32, 33, 25, 13]; place a stop outside normal noise and size the position so the stop costs no more than 1% of capital [p. 48, 53, 54]; run winners with a trailing stop (a close below the 5-day EMA or 10-day SMA in strong trends) [p. 48]; cap total open risk at 3% (three trades at 1%) [p. 55]. The claimed edge is asymmetric payoff (cut losers short, let winners run) plus strict risk control, not a high win rate [p. 10, 11, 12].

The book gives no backtests, track record or performance statistics. The only numbers are illustrative examples (Apple at $120, SPY RSI levels) [p. 15, 54] and a table of break-even win rates for given reward/risk ratios [p. 12]. Many entry details (breakout definition, lookback lengths, RSI period, stop buffer in ATR terms) are not given, so every codable setup below needs ASSUMPTION parameters. The author points to a separate book (Moving Averages 101) for detailed moving-average signals [p. 22]; that is not part of this text.

Markets: US stocks, SPY, commodities, and (in passing) options and futures. Timeframe: daily charts for entries and exits, weekly chart for trend context [p. 16, 17, 27].

## 2. Strategies

Strategy 2.1 is the one coherent system that the rules combine into (trend filter + breakout/strength entry + noise-proof stop + 1% sizing + 5 EMA / 10 SMA trailing exit). The other four are setups the book describes separately (200-day timing, pullback buying, gap-and-go, breakout retest); they can be run with the same stop, sizing and exit rules from section 3. The 5-day EMA versus 10-day SMA trailing exit is a one-parameter choice of exit and is handled as a parameter in 2.1, not as a separate strategy.

### 2.1 Trend-following breakout / strength entry with noise-proof stop and 5 EMA / 10 SMA trailing exit

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (momentum / breakout). The author says trend followers and breakout traders typically have a lower win rate and larger winners | 10, 32 |
| Timeframe & holding period | Daily chart, end-of-day signals; weekly chart used first to set the long-term trend. Holding period open-ended: let winners trend as far as possible (weeks to months for breakouts) | 16, 17, 27, 11, 32 |
| Universe / eligibility filters | Small watch list of specific stocks or setups the trader has studied; growth stocks and commodities trend further than index or big-cap stocks. No liquidity, price or volume filters stated | 30, 26, - |
| Market / regime filter | Go long when price is above the 200-day SMA (40-week MA on weekly as the long-term equivalent); the 200-day can be an extra qualifier on top of an entry signal. Start with the weekly chart for the long-term trend and trade in its direction. In bear markets or below the 200-day the author favours shorting, which is not available in the NSE cash market | 28, 29, 17 |
| Setup conditions | Uptrend defined as price above the key moving average / higher highs and higher lows. Best entries are at an initial breakout over resistance out of a price range into a new price zone, or at a breakout to a 52-week or all-time high (bull-market characteristic). Prefer entering after an initial move in your direction rather than a falling knife. Exact lookback for the range or high is not given | 21, 32, 24, 34 |
| Entry trigger & order type | Buy breakouts and initial strength. Decision based on the last 30 minutes of the day / end-of-day close; profits taken in the morning. Order type not stated (no limit/stop-entry detail) | 33, 27 |
| Initial stop-loss | Before entry, find the level that shows you are wrong; place it outside the range of normal price action and noise, just beyond the obvious support (for example 1% below a moving average) and preferably as an end-of-day (close-based) stop rather than a hard broker stop. The stop must be one with a low probability of being hit. Intraday: step in and exit manually if down more than 1% of total capital | 48, 54, 60 |
| Exits: profit-taking | No fixed profit target for trend trades; exit with a trailing stop. For a long-running strong growth stock that fails to make a new high and closes below the 5-day EMA for the first time in ten days, consider locking in profit. Profit targets, where used, should be at technical resistance levels, not at a personal money target | 11, 58, 39 |
| Exits: trailing / time / signal | In strong trends the 5-day EMA or 10-day SMA is an excellent end-of-day stop if price closes below it. Raise stops as the trade trends. No time stop stated | 48 |
| Position sizing | Find the stop first, then size so the loss at the stop is at most 1% of total trading capital: shares = (1% x capital) / (entry - stop). Example: $100,000 account, stop $5 below a $120 price gives 200 shares | 53, 54 |
| Adding to / pyramiding | Never add to a losing trade. Adding to winners: not found in this text | 57, - |
| Portfolio limits (max positions, correlation, heat) | No more than three open trades at once, 1% risk each, so at most 3% total capital at risk; 0% exposure is allowed in volatile or directionless markets. Correlation limits not stated | 55, - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Long-term trend filter | Close above 200-day SMA | 40-week MA on weekly chart | 28 |
| Trailing exit MA | 5-day EMA close-below, or 10-day SMA close-below | Both named as options; which suits which stock is not specified | 48 |
| Risk per trade | 1% of total trading capital | 0.5% to 1% if max drawdown target is 5%; "for bigger accounts, 1% may be too much" | 53, 42 |
| Max concurrent trades / total open risk | 3 trades / 3% | 0% allowed | 55 |
| Stop buffer beyond obvious level | About 1% below a moving average | Or end-of-day (close-based) stop instead of a buffer | 54 |
| Manual intraday exit threshold | Loss above 1% of total capital | - | 54 |
| Breakout reference high | Not found in this text | 52-week high, all-time high named as examples of bull-market breakouts | 24 |
| Stop distance in volatility terms | Not found in this text | Size by trading range of the last ten days; be able to handle a 50% increase in range | 59 |
| Entry price vs breakout level (confirmation) | Not found in this text | Wait for an initial move in the intended direction | 34 |

**Key quotes**

- "Buy initial strength, short initial weakness, buy breakouts, sell breakdowns short, and let a winner run with a trailing stop loss" [p. 33]
- "In strong trends, the 5 day EMA or 10 day SMA can be an excellent end of day stop if price closes below these levels." [p. 48]
- "Stop losses should be placed outside the range of normal price action and out of the reach of ‘noise’." [p. 48]
- "you find the price level that will show you that your trade is wrong, and position size so that your maximum loss would be 1% of your total trading capital." [p. 39]
- "You should set a stop loss a little beyond a moving average like 1% below, or as an end of day stop" [p. 54]
- "I strongly urge you to make a habit of studying moving average systems, backtesting them" [p. 22]
- "The primary characteristic of a bull market is the ability to repeatedly breakout to new highs." [p. 24]
- "I recommend that you never have more than three trades open at any one time, risking no more than 1% on each." [p. 55]

**Pseudocode**

```
# Inputs: daily OHLCV per stock; capital; params below (ASSUMPTION values marked)
PARAMS: SMA_TREND = 200; BREAKOUT_N = 250 (ASSUMPTION: ~52-week high); TRAIL = "EMA5" or "SMA10";
        RISK_PCT = 0.01; MAX_POS = 3; STOP_BUFFER = 0.01 (book: ~1% below a MA)
EACH DAY t after the close:
  # exits first
  for each open long pos:
     if close[t] < stop_level[pos]:                      # initial / structural stop, close-based
         exit at next open (ASSUMPTION: next-day open execution)
     elif TRAIL == "EMA5"  and close[t] < EMA(close,5)[t]:   exit next open
     elif TRAIL == "SMA10" and close[t] < SMA(close,10)[t]:  exit next open
  # entries
  if open_positions < MAX_POS and total_open_risk + RISK_PCT <= 0.03:
     for each stock in watchlist (ASSUMPTION: whole liquid universe, ranked by 3-month return):
        if close[t] > SMA(close,200)[t]
           and close[t] >= highest(high, BREAKOUT_N)[t-1]       # ASSUMPTION: breakout of 52-wk high
           and close[t] > close[t-1]:                            # ASSUMPTION: strength confirmation
              structural_stop = SMA(close,50)[t] * (1 - STOP_BUFFER)   # ASSUMPTION: stop under 50-day SMA
              risk_per_share = close[t] - structural_stop
              if risk_per_share > 0:
                  shares = floor(RISK_PCT * equity / risk_per_share)
                  buy shares at next open (ASSUMPTION; book says decide in last 30 minutes / at the close)
```

**Ambiguities & assumptions**

- The book never defines the breakout (lookback, close vs intraday, volume). ASSUMPTION: close at or above the prior 250-day high, tested also with 20/55-day highs as sensitivity checks; none of these is the author's.
- Where the structural stop sits is not specified for a breakout trade; the book only says outside noise and beyond obvious support, with examples of the 200-day SMA and 1% below a moving average [p. 15, 54]. ASSUMPTION: stop = lowest of (breakout level, 50-day SMA) minus 1%, evaluated on closing basis; test the 200-day SMA as an alternative for wider stops.
- 5-day EMA versus 10-day SMA: the book names both for strong trends without saying which to choose [p. 48]. ASSUMPTION: test both and report separately; default 10-day SMA (looser, fewer whipsaws).
- Whether the trailing exit replaces or supplements the initial stop: not stated. ASSUMPTION: the initial stop stays until the trail MA rises above it; the exit is whichever is hit first.
- Exit only after a close below the MA, which implies next-bar execution. The author mentions the closing hour for decisions [p. 27]; a daily backtest cannot trade the last 30 minutes. ASSUMPTION: signal at the close, fill at the next open.
- Intraday 1% manual exit [p. 54] is discretionary and cannot be backtested on daily bars. ASSUMPTION: omitted, or approximated by an exit at the stop level if the daily low breaches it.
- Universe selection (the author's small watch list) is discretionary [p. 30]. ASSUMPTION: liquid NSE stocks above a median traded-value threshold, since the book gives no filter.

### 2.2 200-day SMA trend timing (long above, flat below)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following / trend filter (index or stock timing) | 28, 29 |
| Timeframe & holding period | Daily chart; holds while price stays above the 200-day SMA (months to years) | 28 |
| Universe / eligibility filters | Stock indexes and individual stocks; the author uses it on SPY and growth stocks. No other filter | 28, 29 |
| Market / regime filter | The 200-day SMA itself is the regime line: above it is uptrend/bull, below it is downtrend/bear | 28 |
| Setup conditions | Index or stock closes back over the 200-day SMA after a prolonged bear market (first sign of a new bull market); can be combined with another signal, e.g. SPY breaks over the 50 RSI and price is over the 200-day | 29, 41 |
| Entry trigger & order type | Buy when price closes (and keeps closing) above the 200-day SMA. Order type not stated | 29, 41 |
| Initial stop-loss | Exit when price closes below the 200-day SMA (this is the stop). Alternatively a stop a little beyond the line, such as 1% below, or end-of-day based | 28, 54 |
| Exits: profit-taking | None stated for this timing rule | - |
| Exits: trailing / time / signal | Buy-and-hold investors can reduce drawdown by exiting long positions when price closes below the 200-day. Price that fails to rally back and close over it is a short signal (shorting not available in NSE cash) | 28 |
| Position sizing | Not specified for this rule; general 1% risk rule applies (see section 3) | 53 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text for this rule (general 3-trade / 3% cap in section 3) | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend MA | 200-day SMA of close | 40-week MA on weekly chart | 28 |
| Exit trigger | Close below the 200-day SMA | Stop about 1% beyond a moving average | 28, 54 |
| Re-entry trigger | Close back over the 200-day SMA | Index "starts closing back over" it; number of closes not stated | 29 |
| Confirmation filter | Not found in this text | Example: SPY breaks over 50 RSI while above 200-day | 29 |

**Key quotes**

- "The 200 day is a trend trader’s first warning sign that the trend has changed." [p. 28]
- "Buy and hold investors can reduce their drawdowns in trading capital if they exit their long positions when price closes below this line." [p. 28]
- "Waiting for stock index prices to start closing back over the 200 day can be a key level for investors to get back in after a prolonged bear market." [p. 29]
- "The 200 day can be used as a trading system filter, acting as another qualifier before taking entry signals." [p. 29]
- "there is nothing inherently magical about the 200 day." [p. 28]

**Pseudocode**

```
# Daily close series C for the index proxy (NIFTYBEES) or for each stock
sma200 = SMA(C, 200)
signal_long[t] = C[t] > sma200[t]
# state machine, signals at close, fills next open (ASSUMPTION)
if not in_position and C[t] > sma200[t] (and C[t-1] > sma200[t-1]  # ASSUMPTION: 2 consecutive closes):
    buy
if in_position and C[t] < sma200[t]:
    sell to cash          # no short side on NSE cash
```

**Ambiguities & assumptions**

- No whipsaw filter, buffer or confirmation count is given for entry or exit. ASSUMPTION: test a plain close-vs-SMA rule and a variant with a 1% band (the 1% buffer idea comes from p. 54, not from this rule).
- Position size for an index-timing use is not stated. ASSUMPTION: 100% invested when above the line, cash when below, for the index; single stocks use the 1% rule with a stop at the 200-day SMA.
- The shorting half of the rule cannot be run in NSE cash. ASSUMPTION: long-only, go to cash or a liquid-ETF/ bond proxy when below.

### 2.3 Pullback buy in an uptrend (50-day SMA / RSI 30 / 5-day EMA dips)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback / dip-buying inside an uptrend (mean-reversion entry, trend filter) | 13, 15, 17 |
| Timeframe & holding period | Daily chart; hold until a price target (back to the 50-day SMA or uptrend highs) or a trailing exit; swing to multi-week | 15, 58 |
| Universe / eligibility filters | Growth stocks in uptrends, large indexes (SPY). 50-day SMA is the key support for growth stocks in uptrends. Other filters not stated | 17, 15 |
| Market / regime filter | Price over the 200-day SMA (example: pullback to the 30 RSI on a daily chart inside an uptrend over the 200-day SMA). Also supports at the 200-day itself in young bull markets | 13, 28 |
| Setup conditions | Pullback of a stock or index to the 50-day SMA, or RSI reaching 30 on the daily chart while above the 200-day SMA. Entry near the 200-day with the stock having not closed below it for 18 months is cited as a low-risk example. Strongest uptrends repeatedly pull back to the 5-day EMA on the way to new highs. Buying the dip needs a signal; fear is not a signal. Also: bounce off the 30 RSI on bad news in an uptrend over the 200-day reinforces the setup | 13, 15, 31, 32, 47 |
| Entry trigger & order type | Buy at the level (50-day SMA touch or RSI 30) at the end of the day; no order type stated. Also see rule 15: odds improve when you wait for an initial move up before entering | 13, 27, 34 |
| Initial stop-loss | Close below the 200-day SMA (Apple example: stop $1.20 below the entry, about 1% over the 200-day, end-of-day stop); or a level 1% beyond a moving average | 15, 54 |
| Exits: profit-taking | Target a rally back to the 50-day SMA (about 6% in the example) or back to the uptrend highs (about 10%); reward should be two or three times the capital at risk. For an index long, consider locking in profit as RSI approaches 70 | 15, 58 |
| Exits: trailing / time / signal | Trailing stop where possible; 5-day EMA / 10-day SMA close-below exit in strong trends | 15, 48 |
| Position sizing | 1% of capital at risk, size from the stop distance. Apple example: 100 shares at $120 with a $1.20 stop in a $100,000 account | 53, 54, 15 |
| Adding to / pyramiding | Never average down on a losing trade; major funds add at 50-day SMA pullbacks (describing others, not a rule for the trader) | 57, 17 |
| Portfolio limits (max positions, correlation, heat) | 3 trades / 3% total risk (section 3) | 55 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Dip level | 50-day SMA | 200-day SMA; 5-day EMA in strong uptrends | 13, 28, 31 |
| RSI oversold level | 30 on daily chart | Index downtrends bounce near 30; uptrends stall near 70 | 13, 31 |
| RSI period | Not found in this text | - | - |
| Trend filter | Price above 200-day SMA | - | 13 |
| Reward / risk required | 2x to 3x capital at risk | 6% and 10% targets in the Apple example | 15 |
| Stop | Close below 200-day SMA | 1% below a moving average | 15, 54 |
| Distance above 200-day at entry | 1% in the Apple example (illustrative only) | - | 15 |

**Key quotes**

- "buying a pullback in the S & P 500 Index to the 50 day SMA, or the prices reaching the 30 RSI on a daily chart inside an uptrend over the 200 day SMA, is based on quantifiable facts." [p. 13]
- "Your reward should be two or three times larger than your capital at risk to make the trade worth the risk." [p. 15]
- "Even the strongest uptrends in stocks and markets tend to pull back to the 5 day exponential moving average repeatedly on their way to new highs." [p. 31]
- "Fear is not a signal in itself." [p. 32]
- "One key level is the 50 day SMA for growth stocks in uptrends." [p. 17]

**Pseudocode**

```
PARAMS: RSI_N = 14 (ASSUMPTION), RSI_LEVEL = 30, MA_DIP = 50, TARGET_RR = 2
EACH DAY t after the close, for each stock:
  if C[t] > SMA(C,200)[t]:                                   # uptrend filter
     dip = (L[t] <= SMA(C,50)[t] and C[t] >= SMA(C,50)[t]*0.99)   # ASSUMPTION: touch + hold tolerance
           or RSI(C,RSI_N)[t] <= RSI_LEVEL
     if dip and C[t] > O[t]:                                  # ASSUMPTION: initial up-move confirmation (rule 15)
         stop = SMA(C,200)[t] * 0.99                          # ASSUMPTION: 1% beyond the 200-day (p.54)
         risk = C[t] - stop
         if risk > 0 and (target = max(SMA(C,50)[t], swing_high_60d) ) - C[t] >= 2*risk:
             shares = floor(0.01*equity / risk); buy next open
  exits: close < stop (EOD) ; high >= target ; or close < SMA(C,10) after a profit (ASSUMPTION)
```

**Ambiguities & assumptions**

- RSI period is not given. ASSUMPTION: 14 (convention, not the author's).
- Whether the 50-day SMA entry is a touch, a close below, or a bounce is not stated. ASSUMPTION: intraday low reaches the 50-day SMA and the close holds at or above 99% of it.
- A stop at the 200-day SMA can be far from a 50-day SMA entry, so 1% sizing may give small positions. The book accepts this ("position size correctly") [p. 60]. ASSUMPTION: no minimum position.
- "Uptrend highs" target: lookback undefined. ASSUMPTION: highest high of the last 60 days.
- The target (2-3x risk) and the trailing exit are alternatives in the text; ASSUMPTION: use the target as the initial exit and the 10-day SMA trail once the position shows a profit above 1R.

### 2.4 Gap-and-go (buy a strong gap up)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Momentum / gap continuation | 25 |
| Timeframe & holding period | Daily bars; trend over days, weeks or months if the gap holds | 25 |
| Universe / eligibility filters | Growth stocks and commodities gap and trend more than indexes or big caps; trade only watch-list markets with solid gap rules | 25, 26 |
| Market / regime filter | Location matters: a gap up out of a downtrend from oversold (RSI 30 to 40) has better odds than a gap late in an uptrend (RSI 60 to 70, overbought). Exhaustion gaps late in a long trend on large volume that end the day lower than the open or high may end the trend | 25, 26 |
| Setup conditions | A large gap up (larger gap, greater odds of continuation); the low of the gap day holds (gap and go) rather than filling the same day. If the gap has not filled in the first hour, it likely will not fill that day. Gap size threshold: not found in this text | 25 |
| Entry trigger & order type | Three options: (a) best: buy the first pullback to the low of the gap day; (b) buy into the gap in the morning (riskier); (c) buy the gap at the end of the day | 25 |
| Initial stop-loss | For the end-of-day entry: a close below the low of the gap-up day. For the pullback entry, stop not stated beyond the gap-day low context | 25 |
| Exits: profit-taking | Not found in this text for gaps | - |
| Exits: trailing / time / signal | General trailing rule (5 EMA / 10 SMA close-below) applies; exhaustion gap warning (large volume, close well below open) | 48, 26 |
| Position sizing | General 1% rule (stop distance from gap-day low) | 53, 54 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | General 3 trades / 3% | 55 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Gap size | Not found in this text (larger is better) | - | 25 |
| Stop | Close below the gap-day low | - | 25 |
| RSI context | Gap from RSI 30 to 40 preferred over 60 to 70 | RSI period not stated | 25 |
| First-hour fill test | Gap unfilled after first hour implies it will likely not fill that day | Intraday; not testable on daily bars | 25 |
| Entry style | First pullback to the gap-day low (best), morning buy, or end-of-day buy | - | 25 |

**Key quotes**

- "The best way to trade a gap is to buy the first pullback to the low of the gap day." [p. 25]
- "You can also buy the gap at the end of the day with your stop as a close below the low of the gap up day." [p. 25]
- "The larger the market gaps, the greater the odds of continuation and a trend." [p. 25]
- "Gaps late into a long trend can signal the end of a trend." [p. 26]

**Pseudocode**

```
PARAMS: GAP_MIN = 3% (ASSUMPTION), ENTRY_MODE in {"EOD", "PULLBACK"}, WINDOW = 10 (ASSUMPTION)
gap day t qualifies if:
   O[t] >= H[t-1] * (1 + GAP_MIN)          # ASSUMPTION: clean gap above prior high
   and C[t] >= O[t] and L[t] > H[t-1]      # ASSUMPTION: gap not filled intraday ("gap and go")
   and C[t] > SMA(C,200)[t]                # ASSUMPTION: regime filter (p.29)
EOD mode:      buy at next open after t; stop = close below L[t]; shares = 1% * equity / (entry - L[t])
PULLBACK mode: for d in t+1 .. t+WINDOW: first day with L[d] <= H[t]  (ASSUMPTION: pullback into the gap area)
               and C[d] >= L[t]: buy at next open; stop = close below L[t]
exit: close < EMA5 or close < SMA10 (trailing), or stop above
```

**Ambiguities & assumptions**

- No gap size, volume or window for the pullback entry. ASSUMPTION: gap of at least 3% from the prior day's high, entry window 10 trading days, no volume filter.
- Pullback entry: "the low of the gap day" is ambiguous (the pullback touches the gap-day low, or the gap-day open/prior close). ASSUMPTION: touch of the gap-day low, stop close below it, so the pullback entry has almost no stop distance; test the entry with a limit at the prior-day high (the gap edge) as a variant.
- Morning entry and the one-hour test need intraday data we do not have. ASSUMPTION: only the end-of-day and pullback modes are tested.
- Exhaustion-gap exclusion is discretionary. ASSUMPTION: skip if the gap occurs when RSI(14) of the prior close is above 70 or price is more than 30% above the 200-day SMA.

### 2.5 Breakout and retest of old resistance (buy the first pullback to the breakout level)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout / pullback continuation (support-resistance flip) | 19, 20 |
| Timeframe & holding period | Daily chart; enter a new trend and hold for weeks to months | 20, 32 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not stated for this setup; the author generally favours longs in the direction of the long-term trend and above the 200-day | 17, 29 |
| Setup conditions | A stock in a trading range with a resistance level that has been tested repeatedly (more tests, greater odds of breaking) breaks out above that resistance. Example: old $105 resistance, breakout to $108 | 19 |
| Entry trigger & order type | Buy the first pullback to the breakout level (old resistance as new support), because the odds are good that price returns to it at least once. Order type not stated | 19, 20 |
| Initial stop-loss | Not specified for this setup. General rules: outside normal noise, a little beyond the obvious level (about 1% beyond), end-of-day close based | 48, 54 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | General 5 EMA / 10 SMA trailing exit | 48 |
| Position sizing | General 1% rule | 53 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | General 3 trades / 3% | 55 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Resistance definition (touches, tolerance) | Not found in this text | "The more times resistance and supports are tested, the greater the odds that they will break" | 20 |
| Breakout confirmation | Not found in this text | Wait for an initial move (rule 15) | 34 |
| Pullback window | Not found in this text | Returns "at least one more time" | 19 |
| Stop | Beyond the retest level, end-of-day, about 1% buffer | General rule | 54 |

**Key quotes**

- "If a stock had an old $105 resistance level and it suddenly breaks out to $108, the odds are good that it will return at least one more time to $105." [p. 19]
- "so old resistance becomes new support in an uptrend." [p. 20]
- "The more times resistance and supports are tested, the greater the odds that they will break into a trend" [p. 20]

**Pseudocode**

```
PARAMS: RES_LOOKBACK = 60, MIN_TOUCHES = 2, TOL = 1% (ASSUMPTION), RETEST_WINDOW = 15
resistance R = highest high of last RES_LOOKBACK days where >= MIN_TOUCHES highs within TOL of R (ASSUMPTION)
breakout day b: close[b] > R*(1+0.5%) (ASSUMPTION)
retest: first day d in (b, b+RETEST_WINDOW] with L[d] <= R*(1+TOL) and C[d] >= R  -> buy at close[d]
stop: close < R*(1-0.01);  size = 1% equity / (C[d] - R*0.99)
exit: close < EMA5 or SMA10 (ASSUMPTION: whichever default from 2.1)
no retest within window -> no trade
```

**Ambiguities & assumptions**

- The book does not quantify touches, tolerance, breakout margin or retest window; all values above are ASSUMPTION. The book itself calls pattern/line breakouts discretionary and hard to backtest [p. 13].
- Stop location for a retest is not stated; ASSUMPTION: 1% below the breakout level, close-based (borrowing the 1% buffer idea from p. 54).

## 3. Risk & money-management rules

| Rule | Detail | Page |
|---|---|---|
| Win rate vs reward/risk | Break-even win rate: 1:1 needs >50%, 1:2 >33%, 1:3 >25%, 1:5 >17% | 12 |
| Cut losers short, let winners run | Cap downside, leave upside open; stop loss on every trade | 10, 11, 48 |
| Known stop before entry | Know the stop location before entering; find the stop first, then size | 48, 54 |
| 1% rule | Never lose more than 1% of total trading capital on any one trade (via sizing from the stop distance). The rule does not mean trading 1% of capital | 53 |
| Size from stop | Example: $100,000, Apple at $120, stop $5 below gives 200 shares | 54 |
| 3% worst-day cap | Max three open trades risking 1% each; total open risk at most 3%; 0% exposure allowed in volatile or directionless markets | 55 |
| Drawdown design | For a 5% max drawdown risk 0.5% to 1% per trade; example targets 20% annual return with 5% max drawdown, or 30% with 10% | 42 |
| Drawdown measured from equity high | Drawdown is measured from the most recent new equity high, not the starting equity | 42 |
| Scale down when losing | Reduce position size as performance worsens, increase in winning streaks; adjust to the market type | 56 |
| Size by setup quality | Largest size on the rare best setups, normal size on common high-probability setups, smallest on first signals out of a range or volatility period | 52 |
| Volatility adjustment | Know the trading range over the last ten days and size to handle a 50% increase in it; size for the worst case | 59 |
| Stop discipline | Once chosen, a stop is set in stone; do not argue, bargain or hope after it triggers | 51 |
| No averaging down | Never add to a losing trade | 57 |
| Protect big open gains | Never let a statistically significant unrealized gain turn into a realized loss; use trailing stops or targets; example 70 RSI on SPY, 5-day EMA close after ten up days | 58 |
| Large drawdown recovery | A 50% drawdown needs a 100% gain to recover | 50 |
| Position size emotional limit | Reduce size until you can trade unemotionally (judgment, not testable) | 38 |
| Earnings-event caution | Low-risk setup holds only if earnings are not released the next day | 15 |
| End-of-day stop mechanics | Use end-of-day stops and smaller sizes to avoid intraday noise; no hard broker stop exactly at the 200-day | 54 |

## 4. Non-codable guidance

- Hope, ego and emotion are the worst signals; replace opinions with signals, ego with position sizing, emotions with a trading plan [p. 8, 9, 35, 44].
- Trade reactive signals, not predictions; opinions and news are not signals, though a market rising on bad news (or falling on good news) reinforces a trade [p. 41, 47].
- The easy trade is usually the losing one; the profitable entries (deep fear dips, breakouts) are emotionally difficult [p. 32, 33].
- Contrarian awareness: extreme sentiment suggests the move is late, but needs a technical signal [p. 36, 46].
- When there is nothing to do, do nothing; avoid boredom trades and chasing [p. 40].
- Take the planned small loss for the sake of nerves and capital [p. 37, 51].
- Decide the drawdown you can endure before starting, and design the system to avoid reaching it [p. 42, 43].
- Faith in yourself must be earned through competence and discipline [p. 45].
- Focus on a few markets and setups; know how your stocks react to key averages [p. 30].
- Trade like a business; focus on process rather than money made or lost at any moment [p. 38, 39].
- Study, backtest and keep learning; practise rules until they become habits [p. 8, 9, 61].
- The best trades work almost right away; do not catch falling knives [p. 34].
- Interpretation of support/resistance and trend lines is discretionary and hard to backtest [p. 13].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily OHLCV (open, high, low, close, volume) for SMA/EMA, RSI, highs/lows, gap detection and stops; adjusted prices for splits and bonuses. Index history: NIFTYBEES (or an equal-weight index built from the stock panel) for 2.2 and optional market filter. Weekly bars can be derived from daily. Delivery % and fundamentals are not used by the book.
- **Testability with our data:** All five strategies are price-only and can be backtested over 2005-2026 with the daily panel (including delisted stocks, which removes survivorship bias). Not testable: the last-30-minutes entry decision, the first-hour gap-fill test, the morning-entry gap option and the intraday 1% manual exit [p. 25, 27, 54], since these need intraday data. Sentiment/news tells [p. 36, 47] cannot be tested. No fundamentals are required.
- **Market-structure differences:** The book is US-centred and endorses shorting (bear-market short side, gap-down shorts).
  - ASSUMPTION: long-only; below the 200-day or on short signals go to cash. Short signals could optionally be used as an exit/avoid filter only.
  - ASSUMPTION: signals computed on the daily close with execution at the next day's open (the author acts in the last 30 minutes; a close-price fill is an alternative test). Include STT, brokerage and about 0.1% slippage per side.
  - ASSUMPTION: gap trades (2.4) face circuit limits: skip stocks hitting upper circuit at the open (no fill possible) and treat gap-up fills at the open, not the prior close.
  - ASSUMPTION: the 1% rule is applied to the account equity; with a 3-position cap, expect many days with 100% cash. Position value caps (such as 25% of equity per name) should be added for tight stops, since 1% sizing with a very close stop gives very large positions; the book's examples have 100 to 500 shares at around $120 against a $100,000 account [p. 15, 53].
  - ASSUMPTION: a liquidity floor (median daily traded value) since the book does not give one and small caps carry wide spreads.
  - Stop gaps: NSE stocks can gap through close-based stops; backtest at the next open, not at the stop price.

## 6. Verdict

- **Codeability:** Partly. The risk rules (1% risk, 3% cap, size from stop) and the 200-day, 5 EMA and 10 SMA rules are fully codable, but the entry setups (breakout, retest, gap, dip) are described qualitatively, with most parameters missing.
- **Priority for backtesting:** Medium. The 200-day timing and the 5 EMA / 10 SMA trailing exits with 1% risk sizing are cheap to test and give a robust risk shell for other systems; the entries themselves are underspecified and carry no evidence in the book.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the book as one precise system: the entry definitions (breakout lookback, dip touch, gap size, retest window) are not in the text, so results depend on ASSUMPTION parameters, not the author's rules.
  2. Sizing: the 1% rule is the risk to stop (shares = 1% x equity / (entry - stop)), not 1% of capital invested; the stop must be chosen first and be noise-proof, and total open risk must stay at or below 3% with at most three trades [p. 53, 54, 55].
  3. Exit mechanics: stops and the 5 EMA / 10 SMA exits are close-based (end-of-day), not intraday hard stops; the trailing MA exit triggers only on a close below, and a daily backtest must fill at the next open [p. 48, 54].
