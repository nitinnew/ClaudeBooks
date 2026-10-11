# The Volume Secret — Nigel Hawkes / Hawkeye Traders LLC (named on pp. 1-3)

- **Source file:** Google Drive: Volume_Secret_Master.pdf
- **Text file used:** text/unknown_volume_secret_master.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/<key>.md text/<key>.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read lines 1-1445 (entire file), last `[[PAGE 45]]` reached. Page 40 has no body text (header only; the Hawkeye GBP/USD chart image is presumably there); pages 1 and 2 are cover/promotional text only. No chapter was skipped; pp. 3-6 (author biography), 44-45 (promotion) and pp. 15-17 (trader examples) were read and contain no entry/exit rules. Charts are images and are not in the text; only their captions/commentary were available. Reading done by a Sonnet sub-agent (notes log covers lines 1-1445). The coordinator re-ran the verifier and an exact-page check, spot-checked 10 unquoted table citations, and confirmed the p. 17 arithmetic error (70 x 55 - 30 x 15 = 3400 pips, not the stated 2905).

## 1. The method in brief

This is a short free e-book (about 45 PDF pages) that markets the proprietary "Hawkeye" volume-price-analysis (VPA) indicator suite by Hawkeye Traders LLC (2013). The core claim is that "Volume is the ONLY leading indicator" and that all lagging indicators (MACD, stochastic, moving averages, RSI, Bollinger bands, Elliott) are useless for forecasting [pp. 6, 10]. Volume combined with price (including the bar's open, which the author says Wyckoff and volume spread analysis ignore) reveals whether each bar's volume is buying, selling or neutral [pp. 25, 34]. The Hawkeye indicator itself looks at the open, high, low and close of the previous 20 bars and runs "over 360 calculations" per bar [p. 34]; those calculations are NOT disclosed, so the proprietary indicator cannot be reproduced from this book. Hawkeye also paints a trend dot (green rising, red falling) from "a complex series of calculations" on price and volume [p. 38], also undisclosed.

What the book does disclose is a set of qualitative Wyckoff-style volume principles: volume confirming or failing to confirm a trend [pp. 19-20, 32], ultra-high volume with no price follow-through as a climax/reversal sign [pp. 20-22, 33], high-volume areas as support/resistance and volume validating breakouts [pp. 22-23, 33]. No thresholds, stops, targets or position sizing are given for any of them. The only quantified items are generic: the 1% risk rule [p. 37], the 20-bar lookback [p. 34], and a set of four illustrative trader expectancy examples [pp. 15-17].

Markets and timeframes: the book is NOT written for one market. It says the indicator "works in all markets" and all timeframes, from daily/weekly swing and trend trading down to intraday scalping [p. 34]. Examples shown are forex GBP/USD scalping with tick volume [p. 39], YM Dow e-mini futures on a short time chart [p. 41], corn futures on a daily chart [p. 42] and Honeywell (US equity) [p. 43]. The author says he trades commodities (coffee, cocoa) holding days to weeks and the ES and YM indices intraday [p. 5]. Evidence: only anecdote (hundreds of users, "hedge funds incorporate it" [pp. 5-6]) and an academic citation that unusually large trading activity precedes large subsequent returns [pp. 18-19]. No backtest statistics, win rates or equity curves are presented.

## 2. Strategies

The book contains no complete, rule-based system. The three subsections below are the closest testable proxies built only from the qualitative statements, using plain OHLCV in place of Hawkeye's proprietary buy/sell volume classification. Every numeric threshold in them is an ASSUMPTION and is flagged as such; the book supplies none.

### 2.1 Volume-confirmed breakout (long side)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout with volume confirmation (Wyckoff-style volume price analysis) | 33 |
| Timeframe & holding period | Not specified for this setup. Book says the method works on all timeframes: swing/trend on daily and weekly down to intraday scalping; commodities held "over days and weeks" | 5, 34 |
| Universe / eligibility filters | None stated. Needs real exchange volume; the book says equities and futures report volume | 34 |
| Market / regime filter | None stated | 34 |
| Setup conditions | Price consolidating on low volume (price congestion); high volume appears at the bottom of each reversal inside the range, read as buying/accumulation and a price support region | 22, 33 |
| Entry trigger & order type | Breakout above the range on rising volume is valid; a pickup in volume signals a breakout is due. Order type not stated | 22, 33 |
| Initial stop-loss | Not specified in this book (only that such an entry is a "LOW RISK TRADE") | 22 |
| Exits: profit-taking | Not specified | |
| Exits: trailing / time / signal | Not specified for this setup. Generic: volume falling while price rises warns the trend is losing strength | 20, 32 |
| Position sizing | Generic only: risk 1% of capital per trade | 37 |
| Adding to / pyramiding | Not specified | |
| Portfolio limits (max positions, correlation, heat) | Not specified | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lookback for "previous bars" in Hawkeye volume classification | 20 bars (open, high, low, close) | none | 34 |
| Low-volume consolidation definition | not given | none | 33 |
| Breakout volume threshold ("rising volume") | not given | none | 33 |
| Risk per trade | 1% of account | "a simple rule of thumb" | 37 |

**Key quotes**
- "A breakout occurring on rising volume is a valid breakout" [p. 33] (the text breaks across a line; see the page).
- "When the market is consolidating on low volume, a pickup in volume can signify that a breakout is due." [p. 33]
- "Breakouts and market spikes can be validated or voided with the help of volume." [p. 24]
- "Points where the market trades on high volume are the points of strong support and resistance" [p. 22]

**Pseudocode** (proxy; all numbers ASSUMPTION)
```
N = 20                       # ASSUMPTION: range lookback (book gives 20 only for the Hawkeye classifier, p. 34)
rangeHigh = max(High[t-N .. t-1]); rangeLow = min(Low[t-N .. t-1])
avgVol = mean(Volume[t-N .. t-1])
consolidating = (rangeHigh - rangeLow) / Close[t-1] <= 0.10          # ASSUMPTION
lowVolBase = mean(Volume[t-5 .. t-1]) < avgVol                         # ASSUMPTION: "low volume" consolidation
accumulation = exists day d in last N with Close[d] > Open[d] and Volume[d] > 1.5*avgVol and Low[d] near rangeLow   # ASSUMPTION proxy for high volume at range bottoms
IF consolidating and lowVolBase and accumulation
   and Close[t] > rangeHigh and Volume[t] > Volume[t-1] and Volume[t] > 1.5*avgVol:    # ASSUMPTION
     BUY at next open
STOP: ASSUMPTION low of breakout bar (book gives none)
EXIT: ASSUMPTION close below rangeHigh on rising volume, or 2 consecutive higher-price bars with falling volume
SIZE: qty = 1% * equity / (entry - stop)
```

**Ambiguities & assumptions**
- Book gives no numeric definition of "low volume", "high volume", "consolidation" or "rising volume". ASSUMPTION: relative to the 20-bar average volume as in the pseudocode.
- The book relies on chart reading of Hawkeye red/green/white volume bars to tell buying from selling volume; plain OHLCV has only a bar-colour proxy. ASSUMPTION: up bar (close > open) with high volume = buying volume.
- No stop, target or exit rule exists in this book: not found in this book.

### 2.2 Volume climax / exhaustion reversal

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion / reversal (climax-based), both directions described | 20, 33 |
| Timeframe & holding period | Not specified; corn daily chart example shown. Reversals "happen not over a single day, but over a series of days" | 33, 42 |
| Universe / eligibility filters | None stated | |
| Market / regime filter | Requires an existing trend (uptrend for a top climax) | 20 |
| Setup conditions | In an uptrend an ultra-high volume bar appears, "particularly true if the extreme volume is associated with no equivalent reaction in the price"; a narrow-spread bar that falls (or fails to rise) on ultra-high volume is read as selling volume. Climax = volume larger than any historical spikes nearby, often after several days of above-average volume | 20, 21, 22, 33 |
| Entry trigger & order type | Look for clues from the price itself, "often followed by a particular candle or price bar pattern" (not defined). Corn example: climax then high selling volume then price falls, a short opportunity. Order type not stated | 33, 42 |
| Initial stop-loss | Not specified | |
| Exits: profit-taking | Not specified | |
| Exits: trailing / time / signal | Not specified | |
| Position sizing | Generic 1% rule | 37 |
| Adding to / pyramiding | Not specified | |
| Portfolio limits (max positions, correlation, heat) | Not specified | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Climax volume | "larger than any historical spikes nearby" (no number) | none | 33 |
| Narrow spread | not quantified | none | 21, 22 |
| Prior high-volume duration | "several days" | none | 33 |

**Key quotes**
- "an ultra-high volume bar appears. This is OFTEN a signal that the trend is about to reverse" [p. 20] (check the text; it is broken across lines).
- "Conversely any reversal from a falling market cannot occur without an increase in volume" [p. 19]
- "volume spikes are extreme (in other words larger than any historical spikes nearby)" [p. 33]
- "will crown a point of market reversal" [p. 33]

**Pseudocode** (proxy; thresholds ASSUMPTION)
```
N = 20
avgVol = mean(Volume[t-N .. t-1]); avgRange = mean(High-Low over t-N .. t-1)
uptrend = Close[t-1] > Close[t-N]                                  # ASSUMPTION trend test
climax = Volume[t] >= max(Volume[t-N .. t-1])                      # "larger than any nearby spike"
narrowNoProgress = (High[t]-Low[t]) < avgRange and Close[t] <= Close[t-1]    # ASSUMPTION
IF uptrend and climax and narrowNoProgress:
    EXIT any long at next open                                      # NSE cash: no shorting; short only via F&O (ASSUMPTION)
    # reversal long (downtrend mirror): downtrend and climax and Close[t] > Open[t] -> BUY next open (ASSUMPTION)
STOP/TARGET: not in book. ASSUMPTION: 2*ATR(14) stop.
```

**Ambiguities & assumptions**
- The book does not say whether to trade the reversal or just exit longs; the corn example calls it "a great trading opportunity to the short side" [p. 42]. ASSUMPTION: use as a long-exit signal and, for downtrend climaxes, as a long-entry candidate.
- The confirming "particular candle or price bar pattern" is not defined: not found in this book.
- Seeming contradiction: ultra-high volume with a falling narrow-spread bar is selling volume [pp. 21-22], while a volume climax at the end of a downtrend marks a bottom [pp. 19, 33]. ASSUMPTION: direction of the signal follows the bar colour at the climax within an existing trend.

### 2.3 Volume trend-health filter (continuation / weakness)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following filter / trend-exhaustion warning | 32 |
| Timeframe & holding period | All timeframes; commodity trends held days to weeks | 5, 34 |
| Universe / eligibility filters | None stated | |
| Market / regime filter | This is the regime test itself | 32 |
| Setup conditions | Uptrend is strong and healthy if volume increases as price moves with the trend and decreases on pullbacks; downtrend mirror. Rising price with falling volume means trend unlikely to continue, until sellers take control, "usually signified by an increase in volume on a down bar" | 32 |
| Entry trigger & order type | Not specified. Tale-of-Hawkeye example: after a drift, look to go long "once we begin to see increased buying volume with green volume bars" (scalping, forex) | 39 |
| Initial stop-loss | Not specified | |
| Exits: profit-taking | Not specified | |
| Exits: trailing / time / signal | Exit/avoid when price rises on falling volume, or on a down bar with rising volume | 20, 32 |
| Position sizing | Generic 1% rule | 37 |
| Adding to / pyramiding | Not specified | |
| Portfolio limits (max positions, correlation, heat) | Not specified | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Volume trend measure (slope/MA of volume) | not given | none | 32 |
| Trend definition | not given (Hawkeye trend dots undisclosed) | none | 38 |

**Key quotes**
- "An uptrend is strong and healthy if" [p. 32] (see the page; the sentence continues on the next lines).
- "In a trend, the volume will go with the trend, so expect to see the volume fall away in the" [p. 20]
- "if we have a rising trend but falling volume, then this is WEAK" [p. 20] (reworded in the text as "Conversely, if we have a rising trend but falling volume, then this is WEAK.")
- "Volume confirms the strength of a trend or suggests its weakness." [p. 19]

**Pseudocode** (proxy; ASSUMPTION)
```
trendUp = SMA(Close,20) rising and Close > SMA(Close,20)           # ASSUMPTION
upVolAvg = mean(Volume on up days, last 10); downVolAvg = mean(Volume on down days, last 10)
healthy = trendUp and upVolAvg > downVolAvg                        # volume expands with trend, contracts on pullbacks
weak = trendUp and slope(SMA(Volume,5)) < 0 and slope(Close,5) > 0 # price up, volume down
IF weak or (Close[t] < Open[t] and Volume[t] > 1.5*SMA(Volume,20)): exit longs / do not add
IF healthy: hold or allow breakout entries from 2.1
```

**Ambiguities & assumptions**
- No quantification of "increases" or "decreases"; ASSUMPTION: up-day vs down-day mean volume over 10 bars and 5-bar volume slope.
- The book says volume "determines the trend with more accuracy" [p. 25] but gives no formula; trend definition is Hawkeye-proprietary [p. 38].

### 2.4 Hawkeye volume indicator and trend dots (proprietary, NOT codable)

Concept description only; no rules to implement.
- Volume bars are classified as buying (green), selling (red) or neutral (white) [p. 43]; classification uses the open/high/low/close of the previous 20 bars and "over 360 calculations" per bar [p. 34]; the author claims about "90% degree of accuracy" on forex tick volume [p. 36].
- The indicator "weights these bars and triggers powerful and accurate entry and exit signals" [p. 43]; the signal logic is not disclosed.
- Trend is painted as green dot (rising) or red dot (falling) from price and volume [p. 38].
- Multiple time frames are combined "giving high probability trades with low risk entries" [p. 44]; no rule given.
- Chart-based illustrations: GBP/USD scalping, rising green trend with declining green volume then red volume without traction, then wait for increased green volume to go long [p. 39]; YM falling red volume then a spike in green volume then rising green volume and an uptrend [p. 41]; corn daily with rising green volume ending in a selling climax then red volume and price fall [p. 42]; Honeywell weak rally on low falling green volume, then increasing red volume and the stock falling [p. 43].
- Volume spread analysis (VSA) is criticised as subjective and as giving conflicting signals [p. 25].

## 3. Risk & money-management rules

- Two kinds of risk: monetary risk per trade and the trade's own probability risk [p. 37].
- 1% rule: risk at most 1% of capital per trade (example: $10 on a $1000 account); this defines contract size and the maximum stop distance [p. 37].
- Expectancy illustrations: Trader 1 wins 60 of 100 at 25 pips and loses 40 at 45 pips for a net -300 pips; Trader 2 wins 40 at 45 pips and loses 60 at 25 pips for +300 pips; Trader 3 25/25 with 50% wins breaks even before spread; Trader 4 70 wins at 55 pips and 30 losses at 15 pips [pp. 15-17]. The lesson: cut losses short and let winners run; winners must exceed losers [p. 16].
- Note an arithmetic error: Trader 4's stated 2905 pips [p. 17] does not match 70 x 55 - 30 x 15 = 3400 pips.
- No drawdown limits, max exposure, max open positions or stop placement rules are given: not found in this book.

## 4. Non-codable guidance

- Volume is "the fuel of the market"; price and volume must be studied together, not separately [pp. 27, 31].
- Volume leads price; momentum persists after volume falls like an oil tanker coasting [p. 31].
- Exits are where real profit or loss is realised; fear of losing profit causes early exits and holding losers [p. 15].
- Have a trading plan and follow it with no emotion about wins or losses [p. 17].
- Single volume spikes on news can halt price temporarily and fade quickly; reversals take several days [p. 33].
- News impact is judged by whether volume rises with price on the release [p. 30].
- Forex tick volume shows activity, not size: low Asia, large London, medium US; deviations from that daily pattern matter; a sudden collapse of tick activity can end a move [pp. 35-36].
- Claimed 70-80% of retail trading accounts lose money [pp. 14, 16].
- Heavy promotion of Hawkeye software and free training rooms [pp. 44-45]; unsupported performance claims should be treated with caution.

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV only (Open, High, Low, Close, Volume) for each stock; optional delivery % as a better buying-pressure proxy; NIFTYBEES for market context. No fundamentals needed.
- **Testability with our data:** the 2.1-2.3 proxies can be backtested on 2005-2026 daily data. The Hawkeye 360-calculation buy/sell/neutral classifier, trend dots and multi-timeframe signals cannot be reproduced (undisclosed). Intraday, tick and forex examples (pp. 39, 41) need intraday or tick data we do not have. The book was written for forex, futures (YM, corn, coffee, cocoa), and US equities across all timeframes [pp. 5, 34, 39-43], so only the daily-equity portion is relevant to NSE.
- **Market-structure differences:**
  - No overnight shorting in the cash market: ASSUMPTION: use only long entries and treat bearish signals (climax tops, falling-volume rallies) as exits or filters.
  - Circuit limits can distort volume-spread signals on limit-up/limit-down days: ASSUMPTION: skip signals on circuit days.
  - Costs: STT, brokerage and about 0.1% slippage: ASSUMPTION: apply 0.1% slippage each side; avoid low-liquidity small caps (e.g. require 20-day average traded value above a threshold).
  - Real exchange volume exists for NSE equities, so the tick-volume proxy discussion for forex does not apply.
  - ASSUMPTION: delivery % could refine "buying volume" classification but the book does not use it.

## 6. Verdict

- **Codeability:** Partly. The disclosed principles (volume-confirmed breakouts, climaxes, trend health) can be proxied with OHLCV, but every threshold, stop and exit is missing and the core Hawkeye indicator is undisclosed.
- **Priority for backtesting:** Low. It is a marketing e-book with no entry/exit rules, no stops, no results; the proxies are generic volume-breakout ideas that are better specified in other books.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the proxies as the Hawkeye method: the buying/selling/neutral volume classification (360 calculations on 20-bar OHLC) is proprietary and not reproduced by up-bar/down-bar volume.
  2. Inventing precise thresholds ("ultra-high", "narrow spread", "low volume") and presenting them as the author's; the book gives none.
  3. Misreading high volume with a down/narrow bar in an uptrend as bullish; the book says it is selling volume [pp. 21-22], while high volume at lows of a range is accumulation [p. 22]; direction depends on context.
