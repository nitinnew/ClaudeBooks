# Candlesticks Analysis — Pradeep Iyer

- **Source file:** Google Drive invest/Definitive guide to candle stick.pdf (28 pages). The Drive file name differs from the book's own title, which is "Candlesticks Analysis" (author Pradeep Iyer, per the page headers).
- **Text file used:** text/unknown_definitive_guide_candlestick.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage. The table of contents on p. 2 lists the book's printed page numbers and chapter numbers; those are ignored.
- **Coverage:** Read all 409 lines of the text file, through the last marker `[[PAGE 28]]`. Pages with little or no text: 1 (cover, empty), 12, 14, 15, 18 and 24 (running header only; the content there is chart images). Several other pages carry only a one-line caption (13, 23, 25, 26, 27). All charts are images, so chart-only details (entry/exit marks, levels, the practice examples' answers) are not captured. Nothing was skimmed. Reading done by a Sonnet sub-agent. The coordinator re-ran the verifier and an exact-page check and spot-checked 10 table citations (entry/stop/target p. 17, mirror rule p. 19, hammer confirmation p. 20, trend rules p. 8, 2% risk and trade-count plan p. 5, 80-90% claim p. 9).

## 1. The method in brief

The author says 99% of traders lose money and that he was one of them until he switched to candlesticks and "made a fortune" [p. 3]. The method is: (a) mark support and resistance (S&R) levels, (b) trade only in a clear uptrend or downtrend, never a sideways trend [p. 8], (c) look for a candle pattern only at S&R, and use the next S&R as the target [p. 8], (d) size every trade so the loss is at most 2% of capital [p. 5]. He states that a candlestick pattern on its own succeeds only a little over 50% of the time, but combined with S&R and money management he claims an 80 to 90% success rate [p. 9]. No statistics, trade log or backtest are given; only single-chart anecdotes (moves of +70%, -25%, +25%, -8%, +28%) [p. 10, 11, 17, 19, 20].

The book teaches reading "the psychology of candles" (open, high, low, close as the story of buyers and sellers) rather than memorising many patterns [p. 9]. It then gives four patterns with rules: bullish engulfing [p. 17], bearish engulfing as a mirror image [p. 19], hammer [p. 20] and shooting star [p. 21]. Timeframes mixed: intraday (DLF, CANBK) and swing (ULTRACEMCO) examples [p. 23, 25, 26], but the rules are stated without a fixed timeframe. Designed for Indian stocks (RELIANCE, DLF, ULTRACEMCO, CANBK are named [p. 5, 23, 25, 26]). Rules are short and several are discretionary, especially support/resistance, "near the high of the day" and "after a down trend".

## 2. Strategies

### 2.1 Bullish engulfing at support

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick reversal pattern at support, long side (mean-reversion bounce) | 17 |
| Timeframe & holding period | Timeframe not stated for the pattern. Book shows day, swing and intraday uses. Holding until target (1:2 or next resistance) or stop. | 4, 17, 23, 25 |
| Universe / eligibility filters | Not found in this text (examples are large Indian stocks). | - |
| Market / regime filter | Stock must be in a down trend before the pattern; the author never trades a sideways trend. | 8, 17 |
| Setup conditions | 1) Must be at support. 2) Must be after a down trend. 3) Close greater than open and close near the high of the day. 4) Previous day close less than open (previous candle is a red candle). | 17 |
| Entry trigger & order type | Above the high of the engulfing candle (buy-stop style entry; order type not specified). | 17 |
| Initial stop-loss | Below the low of both the candles. | 17 |
| Exits: profit-taking | Target 1:2 (risk:reward) or the next resistance area. | 17, 8 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Max loss per trade 2% of capital; shares = max loss / (entry - stop). | 5 |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Max 2 trades per day for the first two months, rising to 4 per day after about 100 trades (day-trading plan). No other limits. | 5 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Close position in day's range | "near to the high of the day" (not quantified) | none | 17 |
| Trend definition | higher high + higher low = up; lower high + lower low = down | none | 8 |
| Entry | above engulfing candle high | none | 17 |
| Stop | below low of both candles | none | 17 |
| Target multiple | 1:2 | "or next resistance area"; later 1:3 or greater | 17, 5 |
| Risk per trade | 2% of capital | none | 5 |
| Engulfing strictness (body vs full range) | Not found in this text | - | - |

**Key quotes**
- "Must be at support." [p. 17]
- "Must be after a down trend." [p. 17]
- "Close must be greater than open and Close must be near to the high of the day" [p. 17]
- "Previous day close must be less than open" [p. 17]
- "Above the high of the engulfing candle" [p. 17]
- "Below the low of both the candles," [p. 17]
- "1:2 or next resistance area." [p. 17]
- "The stock moved up 25% after this bullish engulfing." [p. 17]

**Pseudocode**
```
# daily bars O,H,L,C; support levels S from section 2.5 helper
for each day t:
  if downtrend(t-1)                       # lower highs and lower lows (see 2.5)
     and C[t-1] < O[t-1]                  # previous day red
     and C[t] > O[t]                      # engulfing day green
     and (H[t]-C[t]) <= k*(H[t]-L[t])     # close near high; ASSUMPTION k=0.25
     and O[t] <= C[t-1] and C[t] >= O[t-1]# ASSUMPTION: body engulfs previous body
     and near_support(L[t] or min(L[t],L[t-1]))  :
        entry_level = H[t]
        stop = min(L[t], L[t-1])
        place buy-stop at entry_level valid day t+1 (ASSUMPTION)
        on fill: risk = entry - stop
                 qty = floor(0.02*equity / risk)
                 target = min(entry + 2*risk, next_resistance_above) # ASSUMPTION see below
```

**Ambiguities & assumptions**
- "Support" is discretionary (author draws levels by eye on 50+ charts [p. 8]). ASSUMPTION: support = a price zone (+/-1% or 0.5*ATR(14)) that contains at least 2 prior swing lows (swing = lowest low of 5 bars either side) and from which price reversed upward.
- "Down trend" is defined only as lower high and lower low [p. 8]. ASSUMPTION: last two confirmed swing highs and swing lows (5-bar swings) are both descending, evaluated before the pattern day.
- "Near the high" is not quantified. ASSUMPTION: close in the top 25% of the day's range.
- The rules do not say that the engulfing candle's body must engulf the prior body, only the four listed conditions. ASSUMPTION: also require the open <= previous close and the close >= previous open (standard definition; flag as not found in this book).
- Entry validity window: not found in this book. ASSUMPTION: order valid for the next 1 session; cancel if not triggered.
- Target "1:2 or next resistance area": ambiguous whether the nearer or farther applies. ASSUMPTION: take the nearer of the 1:2 target and next resistance; if next resistance gives less than 1:1, skip the trade.
- No stop-trailing or time stop. ASSUMPTION: exit at close of day 20 if neither stop nor target is hit (testing parameter, not from the book).
- Trading costs and the 2% rule applied to equity at entry: ASSUMPTION: use current account equity.

### 2.2 Bearish engulfing at resistance (mirror image)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick reversal pattern at resistance, short side (mirror of 2.1) | 19 |
| Timeframe & holding period | Not stated; example is a move of 8%. | 19 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Mirror of the bullish rule: must be after an up trend (by implication). Sideways never traded. | 19, 8 |
| Setup conditions | "Rules of the bearish engulfing are mirror image of those of bullish engulfing": at resistance, after an up trend, close below open and near the low of the day, previous day close above open. | 19, 17 |
| Entry trigger & order type | Mirror: below the low of the engulfing candle (inferred, not stated explicitly). | 19, 17 |
| Initial stop-loss | Mirror: above the high of both candles (inferred). | 19, 17 |
| Exits: profit-taking | Mirror: 1:2 or next support (inferred). | 19, 17 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Same 2% rule. | 5 |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Same as 2.1. | 5 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| All thresholds | Mirror of 2.1 | none | 19 |
| Example outcome | stock fell 8% | none | 19 |

**Key quotes**
- "Rules of the bearish engulfing are mirror image of those of bullish engulfing provided earlier in the chapter." [p. 19]
- "The stock fell 8%/" [p. 19]
- "See how the bearish engulfing candle at support is trapping short positions." [p. 27]

**Pseudocode**
```
# mirror of 2.1; in NSE cash market only usable as an EXIT signal for longs or as intraday short (MIS)
if uptrend and C[t-1]>O[t-1] and C[t]<O[t] and close near low and near_resistance:
    short_entry = L[t]; stop = max(H[t],H[t-1]); target = entry - 2*(stop-entry) or next support
```

**Ambiguities & assumptions**
- Entry, stop and target are not written out for the bearish case; the author only says they mirror. ASSUMPTION: exact mirror of 2.1.
- The p. 27 example ("Fake Candle") shows a bearish engulfing at support that traps shorts; this implies the pattern is not valid at support, which is consistent with rule 1 (must be at resistance), but no failure-handling rule is given.
- Cash-market shorting is overnight-restricted in India; see section 5.

### 2.3 Hammer at support (with next-candle confirmation)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick reversal pattern at support with confirmation, long side | 20 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Trade only in trends, never sideways; a down trend before the hammer is not explicitly required in the hammer rules. | 8, 20 |
| Setup conditions | 1) Small body. 2) Very less upper shadow. 3) Tail = minimum 2 times size of body. 4) Color may be green or red. Must form at support. | 20 |
| Entry trigger & order type | "Wait for next candle to be a bullish one before initiating trade." Exact entry price not given. | 20 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text for the hammer (the engulfing target of 1:2 or next resistance is the only target rule given). | 17 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | 2% rule. | 5 |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Same as 2.1. | 5 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lower tail / body | >= 2 | "minimum 2 times" | 20 |
| Body | "small" (unquantified) | none | 20 |
| Upper shadow | "very less" (unquantified) | none | 20 |
| Candle color | green or red | none | 20 |
| Confirmation | next candle bullish | none | 20 |
| Example outcome | +28% from entry | none | 20 |

**Key quotes**
- "Tail = minimum 2 times size of body" [p. 20]
- "Very less upper shadow" [p. 20]
- "Color may be green or red." [p. 20]
- "Once a hammer forms at support." [p. 20]
- "Wait for next candle to be a bullish one before initiating trade." [p. 20]
- "shot up 28% from entry" [p. 20]

**Pseudocode**
```
body = abs(C-O); lower = min(O,C)-L; upper = H-max(O,C); rng = H-L
hammer[t] = lower[t] >= 2*body[t] and upper[t] <= u*rng[t] and body[t] <= b*rng[t]  # ASSUMPTION u=0.1, b=0.33
if hammer[t-1] and near_support(L[t-1]) and C[t] > O[t]:      # next candle bullish
    entry = H[t] (buy-stop on day t+1)   # ASSUMPTION; book silent
    stop = L[t-1]                         # ASSUMPTION
    qty = floor(0.02*equity/(entry-stop))
    target = min(entry+2*(entry-stop), next_resistance)       # ASSUMPTION
```

**Ambiguities & assumptions**
- "Bullish" confirmation candle is undefined. ASSUMPTION: close > open and close > hammer high.
- Entry price, stop and target are not given for the hammer. ASSUMPTION: copy the engulfing structure (entry above confirmation-candle high; stop below hammer low; 1:2 or next resistance).
- A prior down trend is not listed for the hammer; the book only requires support. ASSUMPTION: also require a prior down trend (same test as 2.1), which is the usual definition, flagged as not in this book.
- "Small body" and "very less upper shadow" are unquantified; see pseudocode defaults.

### 2.4 Shooting star at resistance

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Candlestick reversal pattern at resistance, short side / exit signal | 21 |
| Timeframe & holding period | Not stated. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Prior trend must be up. | 21 |
| Setup conditions | 1) Prior trend must be up. 2) Upper wick = minimum 2*body. 3) No/small lower shadow. 4) Red body. (The chapter does not repeat "at resistance"; the book's general principle is to look for patterns only at S&R.) | 21, 8 |
| Entry trigger & order type | Not found in this text. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | 2% rule. | 5 |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Same as 2.1. | 5 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Upper wick / body | >= 2 | "minimum" | 21 |
| Lower shadow | none or small (unquantified) | none | 21 |
| Body color | red | none | 21 |

**Key quotes**
- "Prior trend must be up" [p. 21]
- "Upper wick = minimum 2*body" [p. 21]
- "No/small lower shadow" [p. 21]
- "Red body" [p. 21]

**Pseudocode**
```
shooting_star[t] = uptrend(t-1) and (H-max(O,C)) >= 2*abs(C-O) and (min(O,C)-L) <= 0.1*(H-L) and C<O and near_resistance(H[t])
# usage: exit signal for longs; or intraday short entry below L[t], stop above H[t], target 1:2 or next support (ASSUMPTION)
```

**Ambiguities & assumptions**
- No entry, stop or target in the book. ASSUMPTION: mirror of the hammer plus bearish confirmation; on NSE use as a long-exit signal (see section 5).
- "At resistance" is implied by the general principle [p. 8] but not in the pattern rules. ASSUMPTION: required.

### 2.5 Combined method: S&R + trend + pattern + 2% risk (the "putting it all together" framework)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Support/resistance-based candlestick reversal system (patterns 2.1 to 2.4), both long and short | 8, 22 |
| Timeframe & holding period | Intraday (DLF, CANBK) and swing (ULTRACEMCO) examples; no fixed timeframe. | 23, 25, 26 |
| Universe / eligibility filters | Not found in this text (examples are DLF, ULTRACEMCO, CANBK, RELIANCE). | 5, 23, 25, 26 |
| Market / regime filter | Trade only uptrend (higher highs and higher lows) or downtrend (lower highs and lower lows); never sideways. | 8 |
| Setup conditions | Candle patterns only at support or resistance. Candle read as buyer/seller psychology (long tails at support and a bull candle closing near the high = bullish). | 8, 9 |
| Entry trigger & order type | Pattern-specific (see 2.1 to 2.4). | 17, 20 |
| Initial stop-loss | Pattern-specific (engulfing: below low of both candles). | 17 |
| Exits: profit-taking | Targets are support and resistance; 1:2 or next resistance. | 8, 17 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Max loss 2% of capital per trade; start with at most 20% of total capital for one month on this method; larger once capital has doubled. | 5, 22 |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Max 2 trades per day for the first two months, 4 per day after about 100 trades; improve risk:reward from 1:2 to 1:3 or greater at that point. | 5 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Risk per trade | 2% of capital | none | 5 |
| Reward:risk | 1:2 | 1:3 or greater after ~100 trades | 5, 17 |
| Max trades/day | 2 | 4 after ~100 trades | 5 |
| Capital allocated to method | max 20% for the first month | larger once capital doubled | 22 |
| Virtual trading before live | 2 weeks | none | 22 |
| Backtest then live test size | 5000 to 10000 maximum | 3 to 6 months to become competent | 28 |
| Margin used in the sizing example | 3x | none | 5 |
| Claimed win rate | 80 to 90% | patterns alone "just a tad over 50%" | 9 |

**Key quotes**
- "We are going to look for our candle patterns only at support or resistance." [p. 8]
- "Our targets are going to be support and resistance." [p. 8]
- "As candlestick chart traders, we only trade uptrend and downtrend, never, a sideways trend." [p. 8]
- "we can achieve a success" [p. 9]
- "Our maximum loss on any deal should not exceed 2% of our capital." [p. 5]
- "We only accept a maximum of two deals each day." [p. 5]
- "allocate a maximum of 20% of your overall capital for one month" [p. 22]
- "It is highly recommended that you do 2 weeks of virtual trading before doing actual trading." [p. 22]

**Pseudocode**
```
levels = support/resistance zones from swing pivots (ASSUMPTION, see below)
for each day t (after close):
    trend = classify(last two swing highs/lows)   # up, down, sideways
    if trend == sideways: continue
    if trend == down and (bullish_engulfing[t] or confirmed_hammer[t]) and near_support: create long order
    if trend == up and (bearish_engulfing[t] or shooting_star[t]) and near_resistance: create short order (or exit longs)
    sizing: qty = floor(0.02*equity / abs(entry-stop))
    cap trades per day at 2 (4 after 100 trades)
    target = nearest opposing S/R level or 2R
```

**Ambiguities & assumptions**
- The "80 to 90%" claim is unsupported by data. Treat as unproven; backtest from scratch.
- S&R drawing is entirely discretionary. ASSUMPTION: algorithmic zone detection from swing pivots, zone width 0.5*ATR(14), at least 2 touches.
- The sizing example is garbled: "One hundred shares divided by 100 SL points results in fifty shares" [p. 5]. The numbers given (capital 50,000; 2% = 1000; entry 2500, stop 2480, target 2540) imply 1000 / 20 = 50 shares, risk:reward 1:2. ASSUMPTION: shares = 2% x equity / (entry - stop).
- Capital stated as "$50,000" with a "150000-point margin (3x)" for an Indian stock; currency inconsistent [p. 5]. ASSUMPTION: 2% is applied to own capital, not to margin.
- Where a trend is "sideways" is a residual category ("Else") [p. 8], so any ambiguous swing sequence is excluded.
- The 20% allocation is for the first month only; the later allocation is "larger sums" with no number. ASSUMPTION: 20% of capital allocated in the backtest throughout.
- Example 4 ("Fake Candle") [p. 27] shows a failed pattern; no rule is given for invalidating a pattern (for example a bearish engulfing at support). ASSUMPTION: only trade the pattern when its location rule is met.

## 3. Risk & money-management rules

- Risk per trade: max loss on any deal should not exceed 2% of capital; position size follows from the stop distance [p. 5].
- Reward:risk: record a profit at 1:2; aim for 1:3 or better after about 100 trades [p. 5].
- Trade count: at most 2 trades per day for the first two months; up to 4 per day after about 100 trades [p. 5].
- Capital allocation: max 20% of total capital for the method for one month; allocate larger sums once capital has doubled [p. 22].
- Preparation: 2 weeks of virtual trading before live [p. 22]; backtest, then forward-test live with only 5000 to 10000 [p. 28].
- Capital preservation: "make sure you do not lose your capital" [p. 22]. The author also says thinking and money management matter more than any technique [p. 5].
- No drawdown limit, portfolio heat limit or max open positions are stated (Not found in this text).

## 4. Non-codable guidance

- Master support and resistance first; draw them on at least fifty charts [p. 8].
- Read each candle as a story of buyers and sellers rather than memorise patterns [p. 9]; practice predicting the next move on given charts [p. 9, 13, 16].
- Practice on ten thousand charts with the bar replay feature [p. 16].
- Expect 3 to 6 months to become competent [p. 28].
- Paper-trade for 2 weeks before going live [p. 22].
- Offline support is offered by the author for a month after purchase [p. 28]; not relevant to coding.

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLC (and volume for liquidity filter). Intraday examples (DLF, CANBK) would need intraday bars, which we do not have (daily data only). Index/ETF data for trend context (NIFTYBEES) is optional; the book does not use a market filter.
- **Testability with our data:** the daily-bar versions of bullish engulfing, hammer, shooting star and bearish engulfing, the trend definition and the 2%/1:2 risk framework are fully backtestable on 2005-2026 prices, provided support/resistance is defined algorithmically (discretionary in the book). Intraday trades cannot be tested. No fundamentals or delivery % are needed.
- **Market-structure differences:**
  - Overnight shorting is not possible in the NSE cash market. ASSUMPTION: bearish engulfing and shooting star are used only as exit signals for existing longs, or as same-day intraday shorts (not testable on daily data), so the tested system is long-only.
  - Circuit limits: a stock locked at its limit cannot be entered or exited at the stop. ASSUMPTION: skip entries on days where the stock hit a circuit and apply stop at the next available price.
  - Gap risk: the stop below both candles may be gapped through at the open. ASSUMPTION: fill at the open if it gaps below the stop.
  - Costs: STT, brokerage and about 0.1% slippage. ASSUMPTION: apply 0.1% slippage each side plus statutory costs; the "3x margin" is intraday leverage and not used in daily-bar tests.
  - Liquidity: ASSUMPTION: restrict to stocks with 20-day average traded value above a minimum (for example Rs 5 crore) and cap position size at 1-2% of average daily volume.

## 6. Verdict

- **Codeability:** Partly. Candle shapes, trend (higher highs/lows) and the 2% risk plus 1:2 target are codable; support/resistance, "near the high", "small body" and stop/target for hammer and shooting star are discretionary or missing and need assumed definitions.
- **Priority for backtesting:** Medium. The method is simple and fast to test on daily bars, and the claim of 80 to 90% success is extraordinary and unsupported; likely worth a quick test to see how much S&R filtering adds to a bare engulfing/hammer signal. Short-side signals are of limited use on NSE cash.
- **Top 3 things a coder is most likely to get wrong:**
  1. Defining support/resistance loosely (or using look-ahead pivots): swing lows are only confirmed N bars later, and using unconfirmed or future pivots inflates results.
  2. Applying the stop and sizing incorrectly: stop is below the low of both engulfing candles, entry is above the engulfing candle's high (not the close), and shares = 2% of equity / (entry - stop); also gap-through-stop fills and the "next resistance" vs 1:2 target choice.
  3. Treating the short-side patterns as tradeable shorts on NSE cash, or testing the intraday examples on daily data.
