# The Art of Simple and Profitable Trading: 3 Profitable Trading Strategies That Work in Any Market — Dr. Santosh More

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/The Art of Simple & Profitable - Dr. Santosh More.pdf` (file id `1b-NAOsmCOwQdfHWhWLcd8ijZNnZhZt4F`, 5,241,581 bytes; © 2022 Dr. Santosh More [p. 4])
- **Text file used:** text/more_simple_profitable.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter. (This ePub-style PDF has no printed page numbers.)
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/more_simple_profitable.md text/more_simple_profitable.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 49]]. Pages 1–3 and 48 are images with no text. All charts, including the six "Case Study" / "Entry-Exit Rule" chart pages for the three systems [p. 40–45], are images; only their captions are in the text. Chapters 1–8 [p. 8–38] are a beginner primer (candles, patterns, indicators, risk). Rules are taken from Chapter 9 [p. 38–45] and Chapter 8 [p. 35–37].

## 1. The method in brief

A beginner's primer that ends with three simple indicator systems, each with a fixed 1:2 reward:risk target [p. 39–44]: (1) an 8/13/21 EMA alignment trend system with entries on pullbacks to the EMAs confirmed by a candlestick pattern; (2) a 55-EMA "envelope" (EMA of highs and EMA of lows) breakout with a 50-period RSI crossing 52/48; (3) a 0.5-deviation Bollinger Band breakout confirmed by MACD. The author says the systems work "in any market and any timeframe" and advises confirming trend on a higher timeframe [p. 39]. Risk: 1% of capital per trade, stop and target placed at entry [p. 35–37]. Written by an Indian trainer, with dollar examples, for stocks, forex, crypto and commodities; F&O deliberately left out [p. 9]. No backtests or statistics; the case-study charts are images.

## 2. Strategies

### 2.1 Trading System #1 — 3 EMA (8/13/21) trend-following pullback

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following pullback | 39 |
| Timeframe & holding period | Any timeframe; confirm trend on a higher timeframe; holding until stop or target | 39 |
| Universe / eligibility filters | Any instrument | 39 |
| Market / regime filter | Higher-timeframe trend confirmation (no rule given) | 39 |
| Setup conditions | Buy: EMA 8 > EMA 13 > EMA 21 | 39 |
| Entry trigger & order type | Buy on a retracement to the EMAs after one of the book's candlestick patterns forms (hammer, bullish pin bar, bullish engulfing, inside bar/harami, bullish marubozu, morning star) | 16–19, 39 |
| Initial stop-loss | Below the swing low | 39 |
| Exits: profit-taking | Take profit at least 2× the entry–stop distance (1:2) | 39 |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | 1% of capital at risk: shares = (1% × capital) ÷ (entry − stop) | 37 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Key quotes**

- "Buy Setup: EMA 8 is higher than EMA 13, and EMA 13 is higher than EMA 21." [p. 39]
- "We will enter to Buy on a retracement at the EMA’s and after the formation of any Candlestick Pattern, we discussed before." [p. 39]
- "Exit Setup: We will place Stop Loss below the Swing Low. Our Take Profit will be at least double the distance between Entry and the Stop Loss to get a 1:2 Risk Reward Ratio." [p. 39]

**Pseudocode** (daily bars)

```
aligned_t  = EMA8_t > EMA13_t > EMA21_t
retrace_t  = L_t <= EMA8_t and L_t >= EMA21_t * 0.99                 # ASSUMPTION: low tags the EMA ribbon, not far below EMA21
candle_t   = bullish_engulfing | hammer/pin bar (lower wick >= 2x body, close in top third) | inside bar breakout | bullish marubozu
signal_t   = aligned_t and retrace_t and candle_t
             and weekly close > weekly EMA21                         # ASSUMPTION: "higher timeframe" trend check
buy at O_{t+1}
stop   = lowest low of last 5 bars * 0.995                           # ASSUMPTION: "swing low" = 5-bar low
target = entry + 2 * (entry - stop)
shares = floor(0.01 * equity / (entry - stop))
exit at stop or target; ASSUMPTION time stop 20 sessions
```

**Ambiguities & assumptions**

- **Which candlestick patterns count** and how to code them: "any Candlestick Pattern, we discussed before" [p. 39]. The book's own definitions are loose (it describes the hammer as having "a big upper body and a lower wick" [p. 16] and calls the harami "a 'Pin Bar' in the western world" [p. 18]). ASSUMPTION: use standard definitions of bullish engulfing, hammer/pin bar, inside bar and morning star.
- **"Retracement at the EMA's"** is undefined. ASSUMPTION: the day's low reaches EMA8 while staying above EMA21.
- **Take profit "at least" 2R** [p. 39]. ASSUMPTION: exactly 2R base case; 3R variant (the book's general example is 1:3 [p. 35]).

### 2.2 Trading System #2 — 55-EMA high/low envelope + RSI(50)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / breakout | 41 |
| Timeframe & holding period | Any timeframe | 39 |
| Universe / eligibility filters | Any instrument | 39 |
| Market / regime filter | Higher-timeframe trend confirmation (no rule given) | 39 |
| Setup conditions | Envelope = EMA 55 of highs and EMA 55 of lows; RSI with period 50 | 41 |
| Entry trigger & order type | Buy when price closes above the EMA-55-of-highs **and** RSI(50) crosses above 52 | 41 |
| Initial stop-loss | Below the EMA-55-of-lows | 42 |
| Exits: profit-taking | At least 2× the entry–stop distance (1:2) | 42 |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | 1% risk | 37 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Key quotes**

- "For this System, we will use EMA 55 applying at High, and EMA 55 at Low." [p. 41]
- "Buy Setup: Prices close above the EMA 55 High and RSI 50 crosses above Level 52." [p. 41]
- "Sell Setup: Prices close below the EMA 55 High and RSI 50 crosses below Level 48." [p. 41]
- "Exit Setup: We will place Stop Loss below the 55 EMA Low." [p. 42]
- "In our Strategy, we will use customized parameters of the RSI and not the default one." [p. 30]

**Pseudocode**

```
EH = EMA(H, 55); EL = EMA(L, 55); R = RSI(C, 50)
both_t   = C_t > EH_t and R_t > 52
signal_t = both_t and not both_{t-1}                 # both true on t, at least one newly true (ASSUMPTION)
buy at C_t ; stop = EL_t * 0.995 ; target = entry + 2*(entry - stop)
shares = floor(0.01*equity/(entry-stop))
```

**Ambiguities & assumptions**

- **"RSI 50"** is read as RSI with period 50 (the author says he uses customised RSI parameters [p. 30]); the levels 52/48 sit just around the 50 midline, consistent with a long-period RSI. ASSUMPTION: RSI(50).
- **Simultaneity:** "We will enter to Buy when both conditions are met." [p. 41] — not whether both must turn true on the same bar. ASSUMPTION: both true on the signal bar, with at least one becoming true that bar.
- **Sell setup typo:** the short rule says close below the "EMA 55 High" [p. 41]; the symmetric rule would be the EMA 55 Low. Shorts are excluded for NSE cash anyway (Section 5).
- **Stop "below the 55 EMA Low"** can be far from entry when the envelope is wide; there is no maximum. ASSUMPTION: skip trades whose stop distance exceeds 10%.

### 2.3 Trading System #3 — Bollinger Bands (0.5 deviation) + MACD breakout

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout / momentum | 43–44 |
| Timeframe & holding period | Any timeframe | 39 |
| Universe / eligibility filters | Any instrument | 39 |
| Market / regime filter | Higher-timeframe trend confirmation (no rule given) | 39 |
| Setup conditions | Bollinger Band with 0.5 standard deviation; MACD(12,26,9) | 29, 44 |
| Entry trigger & order type | Buy when price closes above the upper band, MACD line above signal line, and histogram above zero | 44 |
| Initial stop-loss | Text says "above the upper Bollinger Band" (contradictory for a long; see Ambiguities) | 44 |
| Exits: profit-taking | At least 2× the entry–stop distance (1:2) | 44 |
| Exits: trailing / time / signal | Not stated | — |
| Position sizing | 1% risk | 37 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Key quotes**

- "For this System, we will use Bollinger Band with 0.5 Deviation and MACD." [p. 44]
- "Buy Setup: Prices close above the upper Bollinger Band, the MACD line is above the Signal Line and the Histogram is above the ‘0’ Line." [p. 44]
- "Exit Setup: We will place Stop Loss above the upper Bollinger Band." [p. 44]
- "When the Signal Line crosses above the MACD line, it is a Buy signal" [p. 29]

**Pseudocode**

```
mid = SMA(C,20); up = mid + 0.5*SD(C,20); lo = mid - 0.5*SD(C,20)     # ASSUMPTION: 20-period basis (book gives only the 0.5 deviation)
macd = EMA12-EMA26; sig = EMA(macd,9); hist = macd - sig
signal_t = C_t > up_t and C_{t-1} <= up_{t-1} and macd_t > sig_t and hist_t > 0
buy at C_t ; stop = lo_t * 0.995  (variant: mid_t)                    # ASSUMPTION (see Ambiguities)
target = entry + 2*(entry - stop) ; 1% risk sizing
```

**Ambiguities & assumptions**

- **Stop placement contradiction:** "Stop Loss above the upper Bollinger Band" [p. 44] is stated once for both setups; it is only valid for the short setup. ASSUMPTION: for longs, stop below the lower 0.5-SD band; variant below the middle line.
- **MACD definition is inverted** in the indicator chapter: a buy is when "the Signal Line crosses above the MACD line" [p. 29], while the system requires "the MACD line is above the Signal Line" [p. 44]. ASSUMPTION: follow the system rule (MACD line above signal, histogram > 0), which is the standard bullish reading.
- **Bollinger period** not given. ASSUMPTION: 20.
- **"when both conditions are met"** though three conditions are listed [p. 44]. ASSUMPTION: all three.

## 3. Risk & money-management rules

- Place stop loss and take profit with every trade, at entry; "Never trade without a Stop Loss and maintain the Risk to Reward Ratio." [p. 35, 47]
- Risk 1% of capital per trade; size = risk ÷ (entry − stop) (worked example: $100,000, 1%, buy 80 / stop 75 → 200 units) [p. 37].
- Reward:risk 1:3 in the general example (wins 4 of 10 still profitable), raise to 1:4–1:6 with experience [p. 35–36]; the three systems use at least 1:2 [p. 39–44].
- Large drawdowns are hard to recover (10% → 11%, 50% → 100%, 90% → 900%) [p. 37–38].

## 4. Non-codable guidance

- Use a higher timeframe to confirm the trend [p. 39].
- Candlestick reversal patterns matter most at support/resistance [p. 17–20].
- Avoid trading or trade only small swings in sideways trends [p. 21].
- Keep a trade record; don't trade when your emotional state is poor; take breaks [p. 47].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLC (EMAs of close, high and low; RSI(50); Bollinger(20, 0.5); MACD(12,26,9)); weekly bars for the higher-timeframe check.
- **Testability with our data:** All three long setups are fully backtestable on 2005–2026 daily prices; no fundamentals or index data needed (unless a regime filter is added).
- **Market-structure differences:**
  - The book is market-agnostic (examples in dollars; stocks, forex, crypto). Sell setups need overnight shorting, which the NSE cash market does not allow. ASSUMPTION: long-only; sell signals = stay flat.
  - Add a liquidity floor (not in the book). ASSUMPTION: 20-day average traded value ≥ Rs. 1 crore and price ≥ Rs. 20.
  - Stop/target orders on daily bars: if both are touched in the same bar, ASSUMPTION: the stop fills first (conservative). Gaps through the stop fill at the open.
  - Costs: STT, brokerage, ~0.1% slippage per side; with 2R targets and tight Bollinger stops (System 3) costs are a large share of R.

## 6. Verdict

- **Codeability:** Fully for Systems 2 and 3 (indicator thresholds and a fixed 2R target); partly for System 1 (pullback and candlestick confirmation need coded definitions).
- **Priority for backtesting:** Low. Three generic indicator systems with fixed 2R targets, no evidence offered, and two internal contradictions (stop side in System 3, MACD signal direction); cheap to test but unlikely to add anything new beyond the other EMA/crossover specs.
- **Top 3 things a coder is most likely to get wrong**
  1. Using the default RSI(14) in System 2: the book's "RSI 50" with levels 52/48 means a 50-period RSI [p. 30, 41].
  2. Using the default 2-standard-deviation Bollinger Bands in System 3: the book uses 0.5 deviation [p. 44].
  3. Copying the System 3 stop literally ("above the upper Bollinger Band") for a long trade; a long needs the stop below the entry.
