# Rule Book Safest Trader ("Step By Step Guide How to learn TRADING") — Safest Trader (handle; author not named)

- **Source file:** Google Drive invest/RULE BOOK SAFEST TRADER.pdf (14 pages, scanned handwritten notes, no text layer)
- **Text file used:** text/unknown_rule_book_safest_trader.txt  (page basis: pdf_pages (OCR of handwriting; page breaks aligned by coordinator)). The PDF has no text layer; the text is Google Drive's own OCR of the handwriting (Drive connector read_file_content), with the [[PAGE N]] markers placed by the coordinator by aligning it with a page-by-page RapidOCR pass.
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage.
- **Coverage:** All 444 lines of the text file read, from line 1 to the last line, ending at [[PAGE 14]]; nothing skipped. OCR quality is poor to fair: frequent misreads (e.g. "Broaker", "Brofit", "worng", "F40" = F&O, "BN" = Bank Nifty, "Hers-Zero" = hero-zero, "Psychlogical"), a few lines are Hindi/Hinglish (paraphrased only where the meaning is clear), and several passages are fragmentary or scrambled in reading order. Page 14 is a second copy of page 7 ("RULES FOR INTRADAY"), with a small OCR difference (2:25 on p. 7 vs 2:45 on p. 14). Diagrams, arrows, boxes and layout on the handwritten pages (especially the p. 5 flowchart and the p. 7 timetable) may be lost or mis-ordered in the OCR, so the mappings below are reconstructions and are flagged as such. Reading done by a Sonnet sub-agent. Text preparation by the coordinator: a local RapidOCR pass on the handwriting was mostly illegible, so the text file is Google Drive's OCR (connector read_file_content), written into the file by the coordinator with page breaks placed by matching each page's headings to the RapidOCR page output (p. 1 road map ... p. 14 repeat of p. 7). The coordinator re-ran the verifier and an exact-page check and confirmed the table citations against the page contents.

## 1. The method in brief

A beginner-oriented set of handwritten rule sheets for Indian index/stock F&O and intraday trading (Nifty, Bank Nifty, NSE hours 9:15 to 3:30) [p. 2]. It opens with a learning roadmap (open a demat account, candlesticks, support/resistance, trendlines, chart patterns, price action, paper trading, find the trend, fix entry/target/stop-loss, psychology) [p. 1]. The "edge" claimed is discipline plus trend-following price action: trade only with the trend, wait for confirmation (price at support/resistance, volume, open interest, a 9 EMA break-and-retest with a rejection candle), avoid the volatile open and the sideways midday, cap trades per day, always use a stop-loss, and keep reward:risk at 1:2 or better [pp. 4, 5, 6, 9, 10, 11].

There are no backtests, win rates or track record anywhere in the text. Numbers given are mostly time windows, trade-count caps, reward:risk ratios and a few indicator settings (9 EMA, 20 EMA, 50 EMA, 200 EMA). Stop-loss placement, position-size formulas and exact entry order types are not stated.

## 2. Strategies

### 2.1 9 EMA break-and-retest with price action (5 min / 15 min)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback/retest entry using a 9-period EMA and a rejection candle; works long and short | 9 |
| Timeframe & holding period | 5 Min TF, with 15 Min TF for a bigger target; intraday (holding period not stated explicitly) | 9 |
| Universe / eligibility filters | Not found in this text for stock selection. Examples given use index levels (18000, 18100, 45000, 45500), so Nifty/Bank Nifty is implied. Check volume at entry and open interest | 9, 10 |
| Market / regime filter | Does not work in consolidating / sideways market; good in trending market; always trade with trend | 9, 10 |
| Setup conditions | EMA (9) must break above or below price, then wait for a retest. Retest candle must be a rejection candle containing wick/shadow (full-body candle: avoid trade). Check important support/resistance, volume, psychological numbers, candle size and body | 9, 10 |
| Entry trigger & order type | After the retest candle, a confirmation candle: red in downtrend, green in uptrend. Exact trigger price and order type not stated | 9 |
| Initial stop-loss | Not found in this text for this strategy (p. 11 says only "Stoploss should be small") | - |
| Exits: profit-taking | Risk:reward 1:2 / 1:3 / 1:4; 15 Min TF for a big target; "as soon as possible profit book" on expiry day | 9, 8 |
| Exits: trailing / time / signal | Not found in this text. Time-of-day profit-booking zones are in 2.5 | - |
| Position sizing | Not found in this text. On expiry keep quantity lower | 8 |
| Adding to / pyramiding | Never average | 8 |
| Portfolio limits (max positions, correlation, heat) | No per-strategy limit. Trade-count caps are in section 3 | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| EMA period | 9 (heading "9 EMA Strategy with price Action") | none | 9 |
| Signal timeframe | 5 Min | 15 Min for bigger target | 9 |
| Reward:risk | at least 1:2 | 1:2, 1:3, 1:4 | 9 |
| Retest candle | rejection candle with wick/shadow | full-body candle avoided | 9 |
| Confirmation candle colour | red (short), green (long) | none | 9 |
| Psychological levels to avoid | 18000, 18100, 45000, 45500 | pattern: round hundreds/five-hundreds, e.g. 40000, 40500, 41000 | 9, 10 |

**Key quotes**
- "Retest Candle should be rejection candle or" [p. 9]
- "Confirmation Candle should be [Red] in downtrend." [p. 9]
- "Risk Reward ratio -" [p. 9]
- "1:21:3/1:4" [p. 9]
- "Avoid at Psychlogical No." [p. 9]
- "Always check Volume at the time of Entry" [p. 10]
- "trade with trend." [p. 10]
- "do Average!!!" [p. 8]

**Pseudocode** (5-minute bars; ema9 = EMA(close, 9))
```
trend = trend_filter()                 # ASSUMPTION below
for each bar t:
  if time not in allowed_windows (see 2.5): continue
  if near_psych_level(close[t]): continue            # within X of a round level
  # SHORT (mirror for LONG)
  if trend == DOWN:
    if state == IDLE and close[t] < ema9[t] and close[t-1] >= ema9[t-1]:
        state = BROKEN                                 # EMA break
    elif state == BROKEN:
        if high[t] >= ema9[t] and upper_wick(t) >= k * body(t) and not full_body(t):
            state = RETEST; retest = t                 # rejection candle at the EMA
        elif close[t] > ema9[t] + tol: state = IDLE    # failed
    elif state == RETEST:
        if close[t] < open[t]:                         # red confirmation candle
            entry = low[t] (stop order below confirmation)  # ASSUMPTION
            sl    = high[retest]                       # ASSUMPTION
            tp    = entry - R * (sl - entry), R = 2    # 1:2 to 1:4
            volume_ok = volume[t] > avg_volume(n)      # ASSUMPTION
        state = IDLE
  exit at tp, sl, or end-of-day square-off
```

**Ambiguities & assumptions**
- "EMA should be break alsove or below": the OCR is scrambled. It reads as price breaking above/below the EMA, then a retest. ASSUMPTION: a bar closing across the 9 EMA is the break.
- Entry trigger is not stated, only that a confirmation candle follows the retest. ASSUMPTION: stop-entry beyond the confirmation candle's extreme.
- Stop-loss is not stated. ASSUMPTION: beyond the retest candle's extreme.
- "Trend" is not defined. ASSUMPTION: price on the correct side of the 20 EMA (p. 4) or 50/200 EMA (p. 12) on the higher timeframe; the book does not tie these together.
- "rejection candle", "wick", "volume" and "open interest" thresholds are not given. ASSUMPTION: wick at least 1x body; volume above its 20-bar average; open interest not testable with our data.
- "Avoid at Psychlogical No.": the buffer around the level is not given. ASSUMPTION: skip if price is within 0.1% of a multiple of 500 (Bank Nifty) or 100 (Nifty).
- Whether R=1:2, 1:3 or 1:4 depends on timeframe is not stated. ASSUMPTION: R = 2 on 5 min, R = 3 on 15 min.

### 2.2 Trend / support-resistance decision flowchart

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following with support/resistance location; breakout in sideways markets | 5 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | First step is "What's the trend": bullish, sideways, bearish. Don't trade against the trend | 5, 4 |
| Setup conditions | Bullish: is price at support? Bearish: is price at resistance? Sideways: wait for breakout. (Flowchart reconstructed from OCR) | 5 |
| Entry trigger & order type | Bullish and at support: BUY. Bearish and at resistance: SELL. Sideways: wait for breakout. Order type not stated | 5 |
| Initial stop-loss | Always use a stop-loss; placement not stated | 4 |
| Exits: profit-taking | Not found in this text for this flowchart (general: reward:risk at least 1:2, p. 11) | 11 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Never average (listed under expiry rules) | 8 |
| Portfolio limits (max positions, correlation, heat) | See section 3 | 6 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend states | bullish / sideways / bearish | none | 5 |
| Pullback reference in uptrend | EMA 20 or support | none | 4 |
| Trend definition | Not found in this text | - | - |
| Support/resistance definition | "Important Support and Important Resistance" levels the market respected in the past | none | 10 |

**Key quotes**
- "WHAT'S" [p. 5]
- "PRICE AT RESISTANCE" [p. 5]
- "WATT FOR" [p. 5]
- "BREAKOUT" [p. 5]
- "EMA 20" [p. 4]
- "downtrend respect the" [p. 4]
- "Check your Important levels (Important Support" [p. 10]

**Pseudocode**
```
trend = classify(close)                       # ASSUMPTION below
if trend == BULL and price_at_support():  BUY
elif trend == BEAR and price_at_resistance(): SELL
elif trend == SIDEWAYS: wait; if close breaks range high/low with volume: trade the break
else: no trade
stop = nearest opposite level (ASSUMPTION); target >= 2R
```

**Ambiguities & assumptions**
- The OCR of the flowchart order is "YES NO NO YES / BUY DON'T DON'T SELL TRADE TRADE". Reading it as bullish-left/bearish-right is a reconstruction; arrows may be lost.
- Trend classification is not defined. ASSUMPTION: bull if close > EMA(50) > EMA(200) on daily, bear if the opposite, sideways otherwise (borrowed from p. 12 inputs, not stated here).
- "Price at support / resistance": no tolerance given. ASSUMPTION: within 0.5 ATR(14) of a swing high/low level touched at least twice.
- Sideways "wait for breakout": direction, confirmation and volume thresholds not given. ASSUMPTION: close beyond a 20-bar range with volume above its 20-bar average.
- In a bearish market the cash segment cannot short overnight; intraday short is allowed.

### 2.3 Swing trading / intraday stocks strategy (50 and 200 EMA)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following swing/intraday on stocks (F&O stocks) | 12 |
| Timeframe & holding period | Time frames 1D, 4H, 1H (OCR "1D and 4H 1H"); swing or intraday | 12 |
| Universe / eligibility filters | Volume should be high; F&O stocks, with liquidity / limit-order issues noted. Use screeners: Chartink, Option Box, Ticker tape | 12 |
| Market / regime filter | For better return the market should have positive sentiment: Nifty 50 and Sensex in green | 12 |
| Setup conditions | Price should be above 50 and 200 EMA for Buy (the line for Sell is garbled; "Sell" appears next to it) | 12 |
| Entry trigger & order type | Not found in this text. Mentions "limit Order issues" in illiquid F&O stocks | 12 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text. Judge by ROI, not by the profit size of index F&O | 12 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Trend EMAs | 50 and 200 | none | 12 |
| Timeframes | 1D, 4H, 1H | none | 12 |
| Volume | "high" (no number) | none | 12 |
| Market sentiment | Nifty 50 and Sensex both green | none | 12 |
| Stock F&O expiry | monthly, last Thursday | index weekly expiry for comparison | 12 |

**Key quotes**
- "Volume should be High" [p. 12]
- "1D and 4H 1H" [p. 12]
- "should above" [p. 12]
- "50 and 200 EMA" [p. 12]
- "Expiry is Monthly Explay not weekly like Nifty and BN." [p. 12]
- "Just look at [Return on Investment (ROI)" [p. 12]

**Pseudocode** (daily version)
```
if close[t] > ema50[t] and close[t] > ema200[t] and volume[t] > avg_volume(20)*V
   and market_green(nifty_or_niftybees):
    buy next open                         # ASSUMPTION
    stop = below recent swing low / 2*ATR   # ASSUMPTION
    exit when close < ema50 or target 2R    # ASSUMPTION
# sell side: not testable in cash (no overnight short)
```

**Ambiguities & assumptions**
- The text lacks any entry trigger beyond "above 50 and 200 EMA"; ASSUMPTION: the first close above both EMAs, or a pullback to the 50 EMA that holds.
- The Sell condition is garbled. ASSUMPTION: mirror (below both EMAs), tested only as intraday short.
- "High volume" is not quantified. ASSUMPTION: volume at least 1.5x its 20-day average.
- Stop-loss and exit are not given anywhere for this strategy. ASSUMPTION: as in the pseudocode.
- The Sensex reference is not available in our data. ASSUMPTION: use NIFTYBEES close vs its 20 EMA as the "green" proxy (before 2024 Nifty index is not available).

### 2.4 Loss-recovery plan (risk overlay)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Risk overlay / constrained mode after losses: breakout trading on supply-demand zones | 11 |
| Timeframe & holding period | Intraday implied (trades per day); avoid scalping | 11 |
| Universe / eligibility filters | Trade only the Nifty 50 index | 11 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Only 1-2 strategies / setups; focus on breakout trading; work on demand and supply zone | 11 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Stop-loss should be small ("max." value garbled in OCR) | 11 |
| Exits: profit-taking | Target should be big, at least 1:2 / 1:3 RR | 11 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Only 2 trades per day | 11 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Max trades per day | 2 | none | 11 |
| Setups allowed | 1-2 | none | 11 |
| Instrument | Nifty 50 index | none | 11 |
| Reward:risk | at least 1:2 | 1:2, 1:3 | 11 |
| Stop-loss size | "Small" (max value unreadable) | none | 11 |

**Key quotes**
- "Only 2 Trades per day." [p. 11]
- "Trade Only Nifty 50 index." [p. 11]
- "atleast 1:2|1:3 RR" [p. 11]
- "Avoid Scalping." [p. 11]
- "Work On Demand and supply" [p. 11]
- "Slow and Steady Recover it." [p. 11]

**Pseudocode**
```
if in_recovery_mode:                      # trigger not stated, ASSUMPTION: account below prior equity high
    max_trades_per_day = 2
    allowed_setups = first two of strategy list
    instrument = NIFTY50 only
    require reward_risk >= 2
    no scalping (min holding time ASSUMPTION: > 15 min)
```

**Ambiguities & assumptions**
- The text does not say when recovery mode starts or ends. ASSUMPTION: starts after a drawdown of 10% from peak, ends at a new equity high (numbers invented as a coder default, not from the text).
- "Demand and supply zone" is not defined. ASSUMPTION: base candles before an impulsive move of at least 2 ATR.
- The max stop-loss value after "max." is unreadable.
- Not testable on our cash data (index trading only, intraday).

### 2.5 Time-of-day filter for intraday F&O (overlay)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Intraday time filter / session map | 4, 7 |
| Timeframe & holding period | Intraday, 9:15 to 3:30 | 2 |
| Universe / eligibility filters | F&O (index options and futures) | 4, 7 |
| Market / regime filter | 11:30 to 2:00 market mostly sideways, with an exception of a trending market once in a month | 7 |
| Setup conditions | Windows per p. 7 table (see below). Choose either first half or second half only | 7 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Always use a stop-loss | 4 |
| Exits: profit-taking | Profit booking can be seen at 2:20 / 2:25 / 3:00 (p. 14: 2:20 / 2:45 / 3:00) | 7, 14 |
| Exits: trailing / time / signal | The 3 PM candle: people square off positions | 8 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

Time windows as read from the OCR (behaviour labels are aligned to times by position and may be mis-assigned):

| Window | Behaviour / rule | Page |
|---|---|---|
| 9:15 to 9:30 | Highly volatile / profit-booking candle; beginners avoid (p. 7: avoid 9:15 to 9:25); BTST traders book profit | 4, 7 |
| 9:30 to 11:30 (p. 4 says 9:30 - 12:00) | First half, big momentum | 4, 7 |
| 11:30 to 2:00 (p. 4 says 12:00-1:30) | Market sideways / SL hunting; avoid, option premium decays | 4, 7 |
| 2:00 to 3:05 (p. 4 says 1:30 3:30) | Big momentum expectations; second half | 4, 7 |
| 3:05 to 3:30 | Market closing decided; stay smart | 7 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Avoid-open window | 9:15 to 9:30 | 9:15 to 9:25 (p. 7) | 4, 7 |
| Midday sideways window | 11:30 to 2:00 | 12:00 to 1:30 (p. 4) | 4, 7 |
| Profit-booking times | 2:20, 2:25, 3:00 | 2:20, 2:45, 3:00 (p. 14); p. 4 lists 2:20, 2:45, 3:00 | 4, 7, 14 |

**Key quotes**
- "9:15 to 9:30 To Trade at Avoid (specially for Beginners)" [p. 4]
- "Avoid this time (Sideways decay)" [p. 4]
- "avoid 9:15 to 9:25 TF Very fast Mover" [p. 7]
- "Avoid full day trading choose either first Half" [p. 7]
- "Market Mostly times Sideways" [p. 7]
- "At 2:20 / 2:45/3:00 Profit Booking" [p. 14]

**Pseudocode**
```
allowed = (09:30 <= t < 11:30) or (14:00 <= t < 15:05)    # choose ONE half per day
blocked = 09:15-09:30, 11:30-14:00
flatten at 15:15 (ASSUMPTION), consider partial profit booking near 14:20 and 15:00
```

**Ambiguities & assumptions**
- Pages 4 and 7 disagree on the midday window (12:00 - 1:30 vs 11:30 - 2:00). ASSUMPTION: use p. 7 (the dedicated intraday sheet, repeated on p. 14).
- The profit-booking time is 2:25 on p. 7 and 2:45 on p. 14; p. 4 shows 2:45. ASSUMPTION: 2:45 (two of three copies).
- Needs intraday bars, which we do not hold.

## 3. Risk & money-management rules

| Rule | Detail | Page |
|---|---|---|
| Trades per day | 2-3 trades, 3-4 maximum | 6 |
| Daily loss limit | Fix a loss limit for the day; if reached, close the system | 6 |
| Expiry day | Reduce quantities; beginners try to avoid expiry-day trade (move to next expiry) | 6, 8 |
| After profit in first half | Avoid overtrading | 6 |
| After loss in first half | Do not try to cover the loss that day (may lose more than you can afford) | 6 |
| Cut losses, let winners run | Cut your losses and hold winning trade | 6 |
| Always use a stop-loss | Do not lose too much on a single trade; follow money and risk management | 4 |
| Overtrading | On expiry, overtrading can give the day's profit back to the market (Hinglish, paraphrased) | 8 |
| No averaging | Never average | 8 |
| Multiple confirmation | Confirm before entering a trade | 8 |
| Reward:risk | Minimum 1:2 (1:2 to 1:4) | 9, 11 |
| Recovery mode | Only 2 trades per day, small stop, big target | 11 |
| Position-size policy | Start with very small capital, plan increases as capital grows and decreases after losses; no numbers | 13 |
| Per-trade risk % / account-level drawdown stop | Not found in this text | - |

**Key quotes**
- "Loss limit for day." [p. 6]
- "Close the system." [p. 6]
- "On Expiry Reduce your Quantities" [p. 6]
- "then avoid overtrading." [p. 6]
- "Start to trade your system with very small amount of capital" [p. 13]
- "decrease your trade size, in" [p. 13]

## 4. Non-codable guidance

- Roadmap for beginners: demat account, candlesticks, support/resistance, trendlines, chart patterns, price action, paper trading, find the trend, fix entry/target/stop-loss, psychology and mindset [p. 1].
- Do not try to time the market ("it went up too much, it will fall now" and the reverse) (Hindi/Hinglish, paraphrased) [p. 4].
- Trend is your friend; respect the trend [p. 4].
- Check how much the market respected a level in the past; it will matter in future (Hindi, paraphrased) [p. 10].
- Track Nifty 50 and Bank Nifty components, especially Reliance, HDFC and ICICI [p. 8].
- Try to avoid hero-zero trades, especially beginners [p. 8].
- Trading-errors vs success page: learn how trading works, probability, find a proven system, personally prove it, complete trading plan, risk control [p. 13].
- Useful tools: TradingView, NSE option chain, Opstra, Investing.com, Moneycontrol, Chartink, Smallcase, CNBC, INDmoney [p. 3].
- Index facts: Nifty 50 and Bank Nifty (12 banks) listed on NSE/BSE; market hours 9:15 to 3:30, closed Saturday/Sunday [p. 2].

## 5. Adapting to NSE (Indian equities)

- **Data required:** 5-minute and 15-minute OHLCV (2.1, 2.5), 1H/4H/1D OHLCV (2.3), volume, open interest (options/futures), Nifty/Sensex daily close for the sentiment filter. Delivery % not used.
- **Testability with our data:** We hold only daily NSE OHLCV (2005-2026) for stocks. 2.3 can be tested at 1D with daily volume and an index proxy (NIFTYBEES before 2024). 2.2 can be approximated on daily bars. 2.1, 2.4 and 2.5 need intraday bars (and open interest, Nifty index options/futures), which we do not have, so they cannot be backtested. No fundamentals are used.
- **Market-structure differences:** The notes are for index F&O (weekly expiry, options). Our cash-equity data has no options or futures. ASSUMPTION: test stock versions only on F&O-eligible liquid stocks, long-only for multi-day holds; shorts only intraday. Apply STT, brokerage and about 0.1% slippage. Circuit limits and limit-order issues in illiquid stocks (p. 12) matter.

## 6. Verdict

- **Codeability:** Partly. 2.3 and 2.2 are codable on daily bars with assumptions; 2.1 is codable but needs intraday data; the stop-loss, entry trigger and sizing are not specified, and the source is handwritten OCR with scrambled lines.
- **Priority for backtesting:** Low. There is no author evidence, key parameters are missing, and most of it needs intraday data and index derivatives we do not hold. Only 2.3 on daily bars is worth a quick test.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating OCR-reconstructed rules (flowchart branches, time-window mapping, the Sell line on p. 12) as exact; these are reconstructions.
  2. Inventing stops/entries that the notes never give; the stop-loss, trend definition and volume thresholds are all `ASSUMPTION` defaults.
  3. Applying intraday F&O timing and 9 EMA retest logic to daily cash-equity data, where the time windows and weekly-expiry rules have no meaning.
