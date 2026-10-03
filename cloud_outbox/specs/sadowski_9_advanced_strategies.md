# 9 Advanced and Profitable Trading Strategies — Roman Sadowski (HumbleTraders ebook, c. 2016)

- **Source file:** Google Drive `08_9_Advanced_and_Profitable_Trading_Strategies_Author_Roman_Sadowski.pdf` (file id `1jKIhtPi3uho_qINkoA4dRXi48vAoFkLh`, 3,707,104 bytes), 42 PDF pages with a text layer. The book is mostly chart screenshots with short text; the screenshots were not readable.
- **Text file used:** text/sadowski_9_advanced_strategies.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index; the ebook has no printed page numbers)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/sadowski_9_advanced_strategies.md text/sadowski_9_advanced_strategies.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 42]]. The table of contents lists 11 items, but only 9 strategies are described. "RSI Trading Strategy, 5 Systems + Back Test Results" and "Binary options trading strategy" appear only as links, with no content in this PDF [p. 2]. Strategy 1 refers to an external "performance section" that is not included [p. 5, 7].

## 1. The method in brief

A promotional forex-oriented ebook (HumbleTraders) sketching nine common retail setups:

1. a COT/stochastic momentum reversal;
2. a 20/60/100 MA crossover;
3. a Heikin-Ashi two-candle reversal with a stochastic filter;
4. a 4-hour correction ("overlap") swing breakout;
5. candlestick engulfing, long-shadow and hammer entries;
6. role reversal (broken resistance becomes support) with scaled limit entries;
7. a Bollinger squeeze;
8. NR4/NR7 range breakouts;
9. a 2-period RSI momentum rule.

Money management is the "3/1000 rule" (≤ 3% of capital per trade) [p. 42]. Evidence is anecdotal:
- MA crossover: 4 winning signals of 600, 200, 200 and 100 points; 6/12 correct [p. 9, 11];
- Heikin-Ashi: three sample trades, +300, +130 and +170 pips [p. 19–21].

There is no systematic backtest.

## 2. Strategies

| # | Strategy | Timeframe | Entry rule (as stated) | Stop / exit (as stated) | Page |
|---|---|---|---|---|---|
| 2.1 | Momentum reversal | Daily setup (weekly and daily stochastic), intraday entry | Trend bias from fundamentals/COT. In the bias direction, wait for weekly and daily stochastic > 70 (or < 30) after a clear rally (or fall), at major S/R; then seek an intraday reversal pattern; pending limit orders, often in the London session; Fibonacci retracements. Counter-bias setups only at reduced size | Not specified (held "up to several weeks"); 1–5 signals per month on USD majors | 5–7 |
| 2.2 | MA crossover | Daily (EURUSD example) | Buy when MA20 crosses above MA60; sell when it crosses below. MA100 = trend: price staying above/below it means "let it run" | Close on the opposite cross | 8–11 |
| 2.3 | Heikin-Ashi reversal | Daily | After a series of red HA candles, two completed green HA candles → long (mirror for short). Filters: stochastic (14,7,3) oversold/overbought; buy-stop a few pips above the 2nd reversal candle's high (sell-stop below the low); Accelerator Oscillator bar confirmation; avoid bank holidays, NFP, FOMC and central-bank speeches | Stop 100 pips flat or at local technical levels; move to breakeven at +50 pips; trail to major local highs/lows, or exit on the opposite signal | 11–18 |
| 2.4 | Swing correction breakout | 4-hour (240-min) | In a trend, a correction = many overlapping candles in a tight range (example: 26 candles within 100 points, daily range down to 20 points). Short when the first candle closes below the contracting range (long mirror: after two candles close above the correction's upper line, buy the next open) | Stop at the most recent minor swing high, or the correction's low for longs | 22–25 |
| 2.5 | Candlestick patterns | Any (daily examples) | Engulfing (body engulfs ≥ 1 prior body; more engulfed = stronger), long shadow (shadow ≥ 2× body), hammer: wait for the pattern candle to close, enter at the next candle's open | Stop at the pattern candle's extreme (low for bullish, high for bearish); trail for shadows and hammers | 25–29 |
| 2.6 | Role reversal (S/R flip) | Intraday/daily | In an uptrend (HH/HL), broken resistance becomes support; buy pullbacks to it, treating S/R as a zone. Split the order into thirds: 1/3 at the 20MA, 1/3 at role reversal, 1/3 at the 50% Fib (mirror for downtrends); pivots and Fibonacci as confluence | Not specified ("risk management must be applied") | 29–34 |
| 2.7 | Bollinger squeeze | 4-hour | BB(20,2) with band width approaching 0.0100 (about 100 points on EURUSD). Buy when a full candle completes above the middle SMA; sell when one completes below it | Stop at the prior candle's high/low, or a max loss of 3% of capital, whichever is smaller | 35–36 |
| 2.8 | Narrow range (NR4/NR7) | Daily | Narrowest candle of the last 4 or 7 days (open and close near the extremes); several NR bars together = a bigger break. Buy above its high, sell below its low | Stop at the NR candle's opposite extreme, trailed | 36–38 |
| 2.9 | 2-period RSI (momentum version) | Short-term | Buy when RSI(2) moves above 90; sell when it moves below 10; add on repeat signals in trends | Close on the opposing signal; "rigorous stop loss regime" (unspecified) | 39–40 |

**Key quotes**

- "One set at 20 periods, the next set at 60 periods and the last set at 100 periods." [p. 8]
- "This day trading strategy generates a BUY signal when the fast moving average ( or MA) crosses up over the slower moving average." [p. 8]
- "Although the system is not correct all the time, the above example was correct 6/12 or 50% of the time." [p. 11]
- "If the price prints two consecutive green candles, after a series of red candles, the downtrend is exhausted and the reversal is likely." [p. 14]
- "Enter long trade after two consecutive RED candles are completed and the Stochastic is above 70 mark" [p. 15]
- "Move position to break even after 50 pips in profit." [p. 18]
- "Stop loss 100 pips flat or use local technical levels to set stop losses." [p. 18]
- "The trade would involve selling when the first candle moved below the contracting range of the previous few candles" [p. 23]
- "The ‘shadow’ should be at least twice the length of the real body of the candle." [p. 28]
- "1/3 at 20MA, 1/3 at role reversal, 1/3 at 50% Fib retracement." [p. 34]
- "we are looking for contraction in the bands along with periods when the Bollinger band width is approaching 0.0100 or about 100 points." [p. 36]
- "It is based on identifying the candle of the narrowest range of the past 4 or 7 days." [p. 36]
- "A BUY signal is generated when the 2 period RSI moves above 90." [p. 39]
- "never ever ever ever risk more than 3% of your capital on any trade." [p. 42]

**Pseudocode** (selected, the most mechanical: 2.2, 2.3, 2.7, 2.8)

```
# 2.2 MA crossover (daily)
long when SMA20 crosses above SMA60 ; exit/short when SMA20 crosses below SMA60
optional trend filter: only long if C > SMA100 (book uses SMA100 as "trend indicator"; ASSUMPTION that it filters entries)

# 2.3 Heikin-Ashi reversal (daily)
HA_close=(O+H+L+C)/4 ; HA_open=(HA_open[-1]+HA_close[-1])/2 ; HA_high=max(H,HA_open,HA_close) ; HA_low=min(L,HA_open,HA_close)
long setup: >=3 red HA bars then 2 green HA bars completed and StochK(14,7,3) < 30 (ASSUMPTION: oversold, see ambiguity)
entry: buy-stop at H(2nd green) + 5 pips (ASSUMPTION "few pips"), valid 3 days
stop: entry - 100 pips (or below swing low) ; at +50 pips move stop to entry ; exit on opposite setup
skip if an NFP/FOMC/central-bank event is within 1 day

# 2.7 Bollinger squeeze (4h)
squeeze: (BB_upper-BB_lower) <= 0.0100 (EURUSD; ASSUMPTION scale = 0.85% of price for other instruments)
long when a 4h candle's low > SMA20 after squeeze ; short when high < SMA20
stop = min(distance to prior candle low, 3% equity risk)

# 2.8 NR7
NR7_t: range_t = min(range over last 7 bars) ; buy-stop at H_t ; sell-stop at L_t (OCO) ; stop at opposite extreme ; trail (ASSUMPTION: 2-bar low)
```

**Ambiguities & assumptions**

- **Heikin-Ashi filter is contradictory.** It says enter long after two RED candles with the stochastic above 70, and short after two GREEN candles below 30 [p. 15]. This contradicts the setup on p. 14 (long after two green candles following reds). The AC filter for shorts also says "red bar above the 0 line" [p. 16]. ASSUMPTION: long = two green HA candles after reds, with the stochastic coming out of oversold (< 30); short is the mirror.
- **HA high/low definitions contain typos** (both described as "high") [p. 11]. Use the standard definitions above.
- **The 2-period RSI rule is the opposite of the common Connors mean-reversion use** (buy RSI(2) < 10). The book's version is momentum: buy > 90, sell < 10 [p. 39–40]. Test as written, and optionally contrast with the mean-reversion version.
- **The Bollinger width "0.0100"** is an absolute EURUSD price width. ASSUMPTION: scale it as a percentage of price for other instruments.
- **No position sizing beyond 3% max risk;** "1000 per point" is unclear [p. 42].

## 3. Risk & money-management rules

- Risk at most 3% of capital per trade (the "3/1000 rule") [p. 42].
- Always use a stop-loss [p. 42].
- Heikin-Ashi money management: breakeven at +50 pips; 100-pip stop or a technical stop; trail to local extremes [p. 18].
- Avoid high-impact news days (NFP, FOMC, bank holidays, central-bank speeches) [p. 17].

## 4. Non-codable guidance

- Fundamental/COT bias for the momentum reversal [p. 5].
- Discipline: avoid trading on hearsay; follow a tested strategy; avoid overtrading [p. 41].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily and 4-hour (or 1-hour) OHLC for NIFTY/BANKNIFTY futures, liquid F&O stocks, or USDINR futures.
- **Testability with our data:** 2.2, 2.3, 2.5, 2.7, 2.8 and 2.9 are mechanical and testable after the assumptions above. 2.1 needs COT data (no direct NSE equivalent; FII/DII derivatives positioning is a possible proxy, ASSUMPTION). 2.4 and 2.6 are discretionary.
- **Market-structure differences:**
  - Pip and point thresholds (50/100 pips, 0.0100 band width) must be converted to ATR or % terms.
  - NSE has session gaps (unlike 24h FX), so intraday stop orders may gap. Treat gaps with next-open fills.
  - The NSE 4-hour bar is irregular (6h15m session). Use 75-minute or hourly bars as the analogue (ASSUMPTION).

## 6. Verdict

- **Codeability:** Partial. Several rules are simple and mechanical (MA cross, NR7, squeeze, RSI(2), engulfing). Others are discretionary or internally inconsistent, and there are no tested parameters beyond the anecdotes.
- **Priority for backtesting:** Low. These are generic retail setups covered better elsewhere (e.g., NR7 and Bollinger squeeze appear in other resources). It is useful mainly as a list of baseline rules to include in a generic signal library.
- **Top 3 things a coder is most likely to get wrong**
  1. Copying the Heikin-Ashi stochastic filter literally (long when the stochastic is > 70 after red candles), which contradicts the setup. Resolve the contradiction explicitly [p. 14–15].
  2. Implementing RSI(2) as mean reversion. The book's rule is momentum: buy above 90, sell below 10, close on the opposite signal [p. 39–40].
  3. Applying FX-pip thresholds (50/100 pips, 0.0100 width) unscaled to other instruments [p. 18, 36].
