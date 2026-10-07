# The Parabolic SAR Trading Strategy (report) — author not stated in the text (publisher: tradingstrategyguides.com, named on p. 19-20)

- **Source file:** Google Drive: Report-Parabolic SAR Trading Strategy.pdf
- **Text file used:** text/unknown_parabolic_sar_strategy.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
- **Coverage:** Read lines 1-322 (the whole file), last [[PAGE 20]] reached. Page 1 has no text (cover). Pages 4, 12, 14, 15, 16, 18 and 20 carry little text (promo banners, chart captions, chart images only); page 15 and 19 hold the stop/exit chart captions only. No sections skipped. Reading done by a Sonnet sub-agent; the coordinator re-ran the verifier and an exact-page check, read the full text itself, and expanded 2.2 to the full template. The promo text on pages 4, 12 and 20 contains no trading rules.

## 1. The method in brief
A trend-reversal entry system combining Parabolic SAR (standard settings) with a 20-period and a 40-period moving average. A trade is taken when the SAR dot flips to the new side of price and the 20 MA has crossed the 40 MA in the same direction, entering on the next candle [p. 2, 3, 8]. The report says it works on any time frame and any market, best when the market trends and poorly in sideways markets [p. 2, 3]. Worked examples (forex, pips) show wins of +203, +74, +331 and +112 pips; no statistics or win rate are given [p. 9, 11, 12, 15].

## 2. Strategies

### 2.1 Parabolic SAR + 20/40 MA reversal (long and short)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following / trend-reversal entry | 2, 3 |
| Timeframe & holding period | Any time frame; examples 4-hour EURUSD, 1-hour USDCAD; holding until exit signal | 3, 12, 15 |
| Universe / eligibility filters | Any market (Forex, Stocks, Options, Futures); none other stated | 2 |
| Market / regime filter | Best when market trending; not at best in sideways/choppy market. No objective filter given | 2 |
| Setup conditions | Short: SAR dot above candle AND 20 MA below 40 MA. Long: SAR dot below candle AND 20 MA above 40 MA. Either may occur first | 8, 10 |
| Entry trigger & order type | Enter the very next price candle after both conditions are met (order type not stated) | 8, 10 |
| Initial stop-loss | 30-50 pips from entry, using prior support/resistance; 40 pips in the example | 9, 10 |
| Exits: profit-taking | No fixed target | 9 |
| Exits: trailing / time / signal | Exit when 20 and 40 MA cross again; or (optional) when SAR dot reverses to the other side of the candle; discretionary early exit if up +100 pips and dot reverses | 9, 10 |
| Position sizing | Not found in this report | |
| Adding to / pyramiding | Not found in this report | |
| Portfolio limits | Not found in this report | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Parabolic SAR | Standard settings | none | 3 |
| Slow MA length | 40 | MA type not stated | 3 |
| Fast MA length | 20 | MA type not stated | 3 |
| Stop distance | 30-50 pips (40 in example) | S/R based | 9 |
| Entry delay | next candle | none | 8 |

**Key quotes**
- "Parabolic Sar Dot must change to be above price candle" [p. 5]
- "the 20 period moving average will cross and go below the 40 period" [p. 6]
- "As long as we have both elements the entry criteria is met." [p. 8]
- "Enter the very next price candle after the parabolic sar dot appears above candle." [p. 8]
- "The stop loss you will place 30-50 pips away from your entry." [p. 9]
- "Your exit criteria is when the 20 and 40 period lines cross over again." [p. 10]
- "You can use either exit strategy." [p. 9]

**Pseudocode**
```
on each bar close:
  sar_below = SAR < close ; sar_above = SAR > close      # standard SAR (0.02, 0.2)
  ma_fast = MA(close,20); ma_slow = MA(close,40)
  long_ok  = sar_below and ma_fast > ma_slow
  short_ok = sar_above and ma_fast < ma_slow
  # trigger: the bar on which the later of (SAR flip, MA cross) completes
  if flat and long_ok_just_became_true: buy at next bar open
  stop = entry - 40 pips (clamp 30-50, or nearest S/R)
  exit long: ma_fast crosses below ma_slow (primary) OR SAR flips above (option B)
  short: mirror (NSE cash: skip shorts or use futures)
```

**Ambiguities & assumptions**
- Page 10 says for long "the 40 period moving average will cross and go below the 20", i.e. 20 above 40; consistent with Rule 4. ASSUMPTION: long = 20 MA above 40 MA.
- Whether the signal needs the SAR flip and MA cross to be recent, or merely both states true: text says either may occur first, no time limit. ASSUMPTION: trigger on the bar where both states first become true together; ignore stale states.
- Page 7 implies that if SAR flips back before the MA cross, one waits for the next flip. Consistent with the state-based rule.
- MA type (SMA/EMA), price source, SAR step/max: "Standard Settings" only. ASSUMPTION: SMA of close; SAR 0.02/0.2.
- Exit choice (MA recross vs SAR flip) left to the trader. ASSUMPTION: MA recross as primary (used in all examples [p. 9, 19]); test SAR flip as a variant.
- Stop in pips; for NSE ASSUMPTION: 40 pips replaced by prior swing low/high or 2 x ATR(14) within a percentage band.
- Position sizing, profit target, pyramiding: not found in this book.

### 2.2 Variant: SAR-flip exit
Same entry as 2.1; the only change is the exit, which the report offers as an equal alternative ("You can use either exit strategy." [p. 9]). Example: +32 pips with the SAR-flip exit vs +203 pips with the MA-cross exit on the same trade [p. 9].

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following / trend-reversal entry, faster exit | 2, 9 |
| Timeframe & holding period | Any time frame; shorter holds than 2.1 because the SAR flips before the MAs recross | 3, 9 |
| Universe / eligibility filters | Any market (Forex, Stocks, Options, Futures) | 2 |
| Market / regime filter | Best in trending markets; no objective filter | 2 |
| Setup conditions | As 2.1: SAR on the trade side of price AND 20 MA vs 40 MA aligned, in either order | 8, 10 |
| Entry trigger & order type | Very next candle after both conditions are met | 8, 10 |
| Initial stop-loss | 30-50 pips from entry, at prior support/resistance | 9, 10 |
| Exits: profit-taking | No fixed target | 9 |
| Exits: trailing / time / signal | Exit when the SAR dot reverses to the other side of the candle | 9 |
| Position sizing | Not found in this report | - |
| Adding to / pyramiding | Not found in this report | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this report | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Parabolic SAR | Standard settings | none | 3 |
| Fast / slow MA | 20 / 40 | MA type not stated | 3 |
| Stop distance | 30-50 pips (40 in example) | S/R based | 9 |
| Exit | SAR flip | MA recross (2.1); hybrid: take the SAR-flip exit once up about +100 pips | 9 |

**Key quotes**
- "when the parabolic sar dot reverses appears at the bottom of the candle" [p. 9]
- "If you are up +100 pips and the dot changes to reversal consider getting out then and taking your profit." [p. 9]

**Pseudocode**
```
entry and stop exactly as 2.1
exit long when SAR > close (dot flips above the candle); exit short when SAR < close
hybrid variant 2.2b: exit on MA recross, but switch to the SAR-flip exit once open profit >= K
  (K = 100 pips on forex; ASSUMPTION for NSE: K = 2 x ATR(14) at entry)
```

**Ambiguities & assumptions**
- The text gives the SAR flip as an exit only for the short example and the +100 pips hybrid; for longs it states only the MA recross exit [p. 10]. ASSUMPTION: apply the mirrored SAR-flip exit to longs too.
- The +100 pips threshold is discretionary ("consider"). ASSUMPTION: 2 x ATR(14) on NSE daily bars.
- Exit on the close of the flip bar vs next open: not stated. ASSUMPTION: next bar open, matching the next-candle entry rule.

## 3. Risk & money-management rules
- Stop 30-50 pips from entry, based on prior support/resistance [p. 9, 10].
- "No strategy can give you a 100% win ratio so always be placing your stops at the appropriate areas." [p. 11]
- No risk-per-trade, sizing or drawdown rules in the text.

## 4. Non-codable guidance
- Check different time frames and what the market is doing [p. 11].
- Practise both short and long trades [p. 11].
- Choose the exit approach depending on how strong the trend is and how far in profit [p. 9].
- Promotional claims ("Guaranteed") on pp. 4, 12 are marketing, not rules.

## 5. Adapting to NSE (Indian equities)
- **Data required:** daily OHLC (SAR and MA on close); volume only for liquidity filter.
- **Testability with our data:** fully backtestable on 2005-2026 daily data; intraday time frames need data we do not have. No fundamentals needed.
- **Market-structure differences:** Examples are forex pips. ASSUMPTION: use daily bars, long only (no overnight shorting in cash); convert stop to ATR/percentage or swing level; model STT, brokerage and 0.1% slippage; enter at next open; skip circuit-locked days; ASSUMPTION: add a trend filter (e.g. ADX or price above 200 DMA) to approximate "best when trending", flagged as an addition not in the report.

## 6. Verdict
- **Codeability:** Fully (long and short entries/exits are mechanical; stop width and MA type need assumptions).
- **Priority for backtesting:** Low-Medium; simple, no evidence beyond four cherry-picked examples, and MA crossover systems are whipsaw-prone.
- **Top 3 things a coder is most likely to get wrong:** (1) treating the SAR flip and MA cross as needing to be simultaneous instead of order-independent states; (2) entering on the signal bar instead of the next candle; (3) using pip stops and shorts on NSE cash without adaptation.
