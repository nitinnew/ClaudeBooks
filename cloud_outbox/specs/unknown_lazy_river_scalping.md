# The Lazy River Scalping Strategy (report) — author not stated in the text

- **Source file:** Google Drive invest/LazyRiverScalpingStrategy_2.pdf (10 pages)
- **Text file used:** text/unknown_lazy_river_scalping.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - Authorship: the report is signed only "-J" with contact e-mail JCrawford@learntotradeforprofit.com [p. 10]; no full author name is stated.
- **Coverage:** Read all 175 lines of the text file, through the last marker [[PAGE 10]]; nothing skimmed. Page 5 has almost no text (only the caption "Bearish Entry Example:"); pages 2, 3, 4, 6, 7, 8 and 9 also carry chart examples. All charts are images and are not in the text, so chart-only details (exact candle positions, example pip distances) are not captured. Reading done by a Sonnet sub-agent. The coordinator read the whole 175-line text itself, re-ran the verifier and an exact-page check, and confirmed the table citations against pp. 1-10.

## 1. The method in brief
A very short report describing one 5-minute scalping setup, "the Lazy River". The chart carries only a 20-period and a 50-period EMA (the "river") [p. 1]. The trader first requires a clear trend from the EMA alignment and slope [p. 2, 3], waits for price to pull back to touch the 20 or 50 EMA, checks that price did not stay beyond the 20 EMA for more than 3 candles, and enters when a candle closes back on the trend side of the 20 EMA [p. 4]. The stop sits 2-5 pips beyond the pullback extreme [p. 6]; half the position takes profit at 1:1, and the rest is trailed behind each new lower high (shorts) or higher low (longs) with no move to breakeven [p. 7, 8, 9].

The text speaks of "the pair" and uses pips throughout [p. 1, 2, 6], so the intended market is forex (currency pairs), although it also says "pennies, points, pips or ticks" [p. 1]. The claimed edge is simply trading with the trend and capturing small, repeated profits plus an optional runner. No track record, backtest, win rate or statistics are presented. The author recommends practice-account testing and tweaking [p. 1, 9].

## 2. Strategies

### 2.1 Lazy River 5-minute EMA pullback scalp (long and short)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following pullback continuation scalp (long and short, mirrored) | 1, 2, 3 |
| Timeframe & holding period | 5-minute chart; "quick trades" that "only need to go a short distance"; runner portion held while the trend continues (no fixed time limit) | 1, 8, 9 |
| Universe / eligibility filters | Not found in this text (only "the pair" / currency pairs implied; no liquidity, spread or session filter) | 1, 2 |
| Market / regime filter | Trend must be established on the same 5-min chart: price above both 20 and 50 EMA, 20 EMA above 50 EMA, both EMAs curving upwards, EMAs not crisscrossing frequently, 20 EMA "comfortably above" 50 EMA. Downtrend is the mirror image | 2, 3 |
| Setup conditions | (1) Bullish/bearish trend established; (2) price moves back to touch the 20 or 50 EMA; (3) "The River Holds Price": not more than 3 consecutive 5-min candles close above/below the 20 EMA (i.e. beyond it during the pullback) | 4 |
| Entry trigger & order type | (4) A close on the opposite side of the 20 EMA occurs, confirming continuation. Order type not stated; entry presumably at/after that candle's close | 4 |
| Initial stop-loss | Most recent low (long) / high (short) from the pullback into the river, plus 2-5 pips beyond it; avoid prices ending in "0" | 6 |
| Exits: profit-taking | Half of the position takes profit at 1:1 (distance equal to the stop distance from entry) | 7, 8 |
| Exits: trailing / time / signal | After first TP, stop is NOT moved to breakeven; it stays at the initial level until a trailing trigger. Trail: every time a lower high forms (shorts), stop goes 2-5 pips above the new high; mirror for longs (below the low). A lower high = the high candle has lower-priced candles on each side AND the market makes a new low. Remaining half is closed by the stop (no other exit stated) | 8, 9 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Chart timeframe | 5 minutes | none | 1 |
| Fast EMA period | 20 (exponential) | none | 1 |
| Slow EMA period | 50 (exponential) | none | 1 |
| Max consecutive closes beyond 20 EMA during pullback | 3 | "not more than 3" | 4 |
| EMA slope condition | "curving upwards/down" (no numeric threshold) | none | 2, 3 |
| EMA crisscross / separation | "should not crisscross each other frequently"; "comfortably" above/below (no numeric threshold) | none | 2, 3 |
| Stop buffer beyond pullback extreme | 2-5 pips | 2 to 5 | 6 |
| Round-number avoidance | Avoid stop on prices ending in "0" | none | 6 |
| Partial take-profit size | Half of the position | none | 7 |
| Partial take-profit distance | 1:1 of stop distance | none | 7 |
| Move to breakeven after TP1 | No | none | 8 |
| Trailing buffer beyond new lower high / higher low | 2-5 pips | 2 to 5 | 8 |
| Candle type | Candlestick or bar chart | user preference | 1 |

**Key quotes**
- "Select the 5 minutes time frame" [p. 1]
- "Price should be above both the 20 and 50 EMA." [p. 2]
- "Both 20 and 50 EMA should be curving upwards" [p. 2]
- "Price Moves Back to Touch 20 or 50 EMA" [p. 4]
- "not have more than 3 consecutive 5min candles" [p. 4]
- "A close on the opposite side of the 20 EMA occurs confirming continuation" [p. 4]
- "We simply use the most recent low" [p. 6]
- "prices that end in" [p. 6]
- "at a 1:1 ratio of our stop loss" [p. 7]
- "we do NOT move the stop loss to breakeven" [p. 8]
- "If and every time a lower high is established" [p. 8]
- "the market makes a new low" [p. 9]

**Pseudocode** (intraday 5-minute bars; long shown, short is the mirror)
```
data: 5m OHLC for a currency pair; ema20 = EMA(close,20); ema50 = EMA(close,50)

uptrend[t] = close>ema20 and close>ema50 and ema20>ema50
             and ema20[t]>ema20[t-k] and ema50[t]>ema50[t-k]      # "curving upwards"
             and crosses(ema20,ema50) in last M bars == 0          # "not crisscross frequently"
             and (ema20-ema50) >= min_sep                          # "comfortably above"

state machine for long:
  if uptrend and not in pullback and not in position:
      wait for a bar whose low <= ema20 or low <= ema50  -> pullback = true
      pullback_low = low; n_below = 0
  while pullback:
      pullback_low = min(pullback_low, low)
      if close < ema20: n_below += 1 else n_below = 0 (when close back above)
      if n_below > 3: cancel setup (river did not hold)
      if n_below >= 1 and next bar close > ema20 (close back on trend side):
          ENTER long at close (or next open)
          stop = pullback_low - buf        # buf in [2,5] pips, nudge off any price ending in "0"
          R = entry - stop
          tp1 = entry + R ; close 50% at tp1
          pullback = false
manage:
  at tp1: close half; leave stop where it is (no breakeven)
  trail (long): when a swing low forms (bar low lower than neighbours' lows on each side... mirror of lower high)
       AND market makes a new high -> stop = swing_low - buf  (only ever raise)
  remaining half exits when stop hit
short: mirror (close<ema20,close<ema50, ema20<ema50, both turning down; pullback touches EMA from below;
       stop = pullback_high + buf; trail above each new lower high that coincides with a new low)
```

**Ambiguities & assumptions**
- Condition 3 is worded "we not have more than 3 consecutive 5min candles close above/below the 20 EMA" [p. 4]. It does not say which side. ASSUMPTION: it means closes on the far side of the 20 EMA during the pullback (below it in an uptrend); more than 3 invalidates the setup.
- Whether a pullback may be "touch" only (wick) or must close beyond the EMA is not stated; the entry step requires "a close on the opposite side" [p. 4]. ASSUMPTION: the pullback requires at least one close beyond the 20 EMA, then entry on the first close back on the trend side.
- Entry order type and price not stated. ASSUMPTION: enter at the close of the confirming candle (market order).
- "Curving upwards", "crisscross frequently" and "comfortably above" have no numbers [p. 2, 3]. ASSUMPTION: slope = EMA greater than its value 3 bars ago; no more than 1 EMA cross in the last 20 bars; separation of at least 0.25 x ATR(14).
- "Most recent low (from the pullback into the Lazy River)" [p. 6]: ASSUMPTION: the lowest low between the first touch of the EMA and the entry bar.
- Pip buffer 2-5 [p. 6, 8]: ASSUMPTION: 3 pips (or the nearest value that avoids a price ending in "0").
- Trailing: the lower-high definition is given for shorts only; longs are "below the low" [p. 9]. ASSUMPTION: exact mirror. Whether trailing begins before TP1 is hit is not stated ("every time" suggests always); ASSUMPTION: trail starts only after TP1, since the stop is explicitly left at the initial level until then [p. 8].
- Not found in this text: position sizing, risk per trade, session/time-of-day filter, news filter, spread filter, daily loss limit, max trades, test results.

## 3. Risk & money-management rules
- Practise on a demo or very small account before going live [p. 1, 9].
- Per-trade risk is defined by the stop distance only (2-5 pips beyond the pullback extreme) [p. 6]; no risk percentage or account-level limit is given. Not found in this text.
- Stop is not moved to breakeven after the first partial profit [p. 8].

## 4. Non-codable guidance
- The author says the second half "takes discipline and steady monitoring of the charts" and that managing trades for optimal profit "only comes with time and experience" [p. 9].
- Encourages making the strategy "your own" and tweaking it to fit one's style [p. 1, 9].
- "Trend is your friend" is the guiding principle [p. 2].
- Chart examples (pages 2-9) illustrate the setups but are images; visual judgement of "curving" and "comfortably above" is discretionary.

## 5. Adapting to NSE (Indian equities)
- **Data required:** The method needs intraday 5-minute OHLC bars (open, high, low, close per 5 minutes) for each instrument. Daily OHLCV only is available to us, so the strategy as written CANNOT be tested. Delivery %, index and fundamentals are not used.
- **Testability with our data:** Needs data we do not have: 5-minute bars (entries, closes back through the 20 EMA, 3-candle count, 2-5 pip stop, 1:1 target and swing-high trail are all 5-minute concepts). Nothing can be backtested faithfully on 2005-2026 daily bars. A daily-bar variant would be a different strategy (swing trading, not scalping), not a test of this report's claims.
- **Market-structure differences:**
  - The report targets forex pairs (pips, "the pair") [p. 1, 2, 6]; no NSE equity-specific adaptation is stated. Pip buffers (2-5 pips) have no equity equivalent. ASSUMPTION: replace with a ticks/percent buffer, e.g. 0.05-0.10% of price or a fraction of ATR.
  - Daily-bar adaptation (defensible only as an exploratory proxy). ASSUMPTION: on daily bars use EMA20/EMA50 trend filter (close>both, EMA20>EMA50, both rising), pullback touching EMA20 or EMA50, at most 3 consecutive daily closes below EMA20, entry on the close back above EMA20, stop = pullback low minus 0.25 x ATR(14) (nudged off round numbers), sell half at 1R, trail remaining half under each higher low that coincides with a new high, no breakeven. Hold time would be days to weeks. Long-only.
  - No overnight shorting in the NSE cash market: the short side can only be intraday (MIS) or via futures; daily-bar adaptation is long-only. ASSUMPTION: skip shorts.
  - Costs: STT, brokerage and about 0.1% slippage per side; a scalping design with 1:1 targets of a few ticks would be severely hurt, so costs dominate any intraday version. Daily-bar version suffers far less.
  - Circuit limits and thin liquidity in small caps: ASSUMPTION: restrict to liquid stocks (e.g. top 500 by traded value) and skip bars at circuit limits.

## 6. Verdict
- **Codeability:** Partly. Entry, stop, partial target and trail rules are explicit, but the indicator conditions ("curving", "comfortably"), the pullback wording and order type need assumptions, and sizing is absent. It is fully codable only on 5-minute data we lack.
- **Priority for backtesting:** Low. The report is a thin, unevidenced forex scalping description; it needs intraday data, and a daily-bar version is merely a generic EMA pullback strategy.
- **Top 3 things a coder is most likely to get wrong:**
  1. Misreading the "River Holds Price" rule (which side, consecutive count, reset) and when the confirming close counts [p. 4].
  2. Applying the trailing rule: it needs a swing high/low with lower-priced candles on each side AND a new low/high, and the stop must not go to breakeven after TP1 [p. 8, 9].
  3. Treating pip-based buffers and the "avoid prices ending in 0" stop rule literally on equities or daily bars, and ignoring that costs dominate scalping returns [p. 6].
