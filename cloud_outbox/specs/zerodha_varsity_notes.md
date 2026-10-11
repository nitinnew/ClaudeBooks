# Zerodha Varsity (personal notes, Word document) — Zerodha Varsity (notes compiled by the user)

- **Source file:** Google Drive invest/Zerodha varsity.docx (526 KB)
- **Text file used:** text/zerodha_varsity_notes.txt  (page basis: docx_rendered_pages (Word's saved page breaks))
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (Word's last-rendered page index, not any printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - Before finishing, `python ../work/bin/verify_citations.py specs/zerodha_varsity_notes.md text/zerodha_varsity_notes.txt` was run.
- **Coverage:** Read lines 1-205 of 205 in full (long lines folded, none truncated); last `[[PAGE N]]` reached: 11 of 11; nothing skimmed. The 2 embedded images in the .docx are not captured in the text (so chart examples, e.g. the MACD and Bollinger Band charts, are not seen). Page basis: docx_rendered_pages (Word's saved page breaks). Reading done by a Sonnet sub-agent. The coordinator extracted the text at Word's saved page breaks, re-ran the verifier and an exact-page check, moved the ADX and Alligator citations (sections 2.10-2.11) from p. 8 to p. 7 where that text sits, and spot-checked 10 table citations and corrected two parameter rows from pp. 10, 11 to pp. 9, 11 (Aroon p. 8; ATR bands pp. 8-9; S&R look-back pp. 2, 9, 10; volume, 4% and RRR 1.5 rules pp. 9, 11).

## 1. The method in brief
These are the user's personal notes, copied and summarised from Zerodha Varsity (Indian market education, Technical Analysis module). They are a collection of single-indicator rules (Heikin Ashi, EMA crossover, RSI, MACD, Bollinger Bands, ADX, Alligator, Aroon, ATR bands) plus a discretionary-but-structured swing-trading workflow. The workflow, called "The Scout" and "The Grand Checklist", scans the Nifty 50 on end-of-day data for a candlestick pattern in the last 3-4 candles, then confirms with prior trend, volume, support/resistance coinciding with the stop-loss, Dow Theory context, a minimum risk-reward ratio, and MACD/RSI [p. 10, 11]. The claimed edge is confluence: "The more confirming factors we use to study the trend and reversal, more robust is the signal" [p. 5].

The notes give no backtest results, win rates or track record. They are fragmentary: many indicator parameters (MACD periods, ATR period, Heikin Ashi formula, candlestick pattern definitions) are not given. Headings "Super Trend", "Combine with SMI and donchain channe", "Parabolic SAR" and "Moving averages" carry no rules [p. 1].

## 2. Strategies
Convention: each indicator rule set is its own subsection with the full table. "Not found in this text" is shown as `-` in the Page column.

### 2.1 Heikin Ashi candle trend signals (Partly codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 1 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Hollow/green HA candles with no lower shadow = strong uptrend; hollow/green = uptrend; small body with upper and lower shadows = trend change; filled/red = downtrend; filled/red with no higher shadow = strong downtrend | 1 |
| Entry trigger & order type | Uptrend: add to long and exit shorts. Trend-change candle: risk-loving traders may buy or sell, others wait for confirmation. Downtrend: add to short, exit longs. Order type not stated | 1 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Strong uptrend: "Let your profits ride"; strong downtrend: stay short until trend changes | 1 |
| Exits: trailing / time / signal | Exit long when candles turn filled/red; exit short when hollow/green | 1 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Add to long in uptrend (green candles); add to short in downtrend (red candles) | 1 |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| HA candle formula | Not given (standard HA assumed) | - | - |
| "Small body" threshold | Not given | - | - |

**Key quotes**
- "There are five primary signals that identify trends and buying opportunities" [p. 1]
- "indicate a strong uptrend: Let your profits ride!" [p. 1]
- "Stay short until there's a change in trend." [p. 1]

**Pseudocode**
```
HA_close=(O+H+L+C)/4; HA_open=(prev HA_open+prev HA_close)/2; HA_high=max(H,HA_open,HA_close); HA_low=min(L,HA_open,HA_close)
green = HA_close>HA_open; red = HA_close<HA_open
strong_up = green and HA_open==HA_low (no lower shadow)
strong_dn = red and HA_open==HA_high (no upper shadow)
LONG_ONLY (NSE cash): enter/hold long when green; add on continued strong_up; exit when red (or small-body doji with both shadows -> wait)
```

**Ambiguities & assumptions**
- Formula and definition of "no shadow"/"small body" not given. ASSUMPTION: standard HA formula; no shadow = wick < 5% of candle range; small body = body < 25% of range.
- Entry/exit price not stated. ASSUMPTION: enter on next open after the signal candle closes; no stop-loss in source, so ASSUMPTION: exit at first red HA candle.
- Shorts cannot be held overnight in NSE cash; short signals used only as long exits.

### 2.2 Smart money: price and volume rising together (Partly codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / momentum | 2 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Price and volume both increasing = big player interested; expectation turns bullish | 2 |
| Entry trigger & order type | Look at a buying opportunity in the stock; order type not stated | 2 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Measure of "increasing" price/volume | Not given | - | - |

**Key quotes**
- "If both the price and the volume are increasing this only means one thing" [p. 2]
- "following the smart money seems like a wise idea" [p. 2]

**Pseudocode**
```
signal = close > close[n] and volume > volume[n]  # n undefined in source
```

**Ambiguities & assumptions**
- No lookback, magnitude, stop or exit. ASSUMPTION: n=1 day, price up and volume above its 10-day average (the 10-day average is used in the Scout, p. 11); treat as a confirmation filter, not a standalone strategy.

### 2.3 EMA crossover system (Fully codable; four pairs as one parameterised strategy)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 2 |
| Timeframe & holding period | Daily EMAs. 9/21: up to a few sessions; 25/50: up to few weeks; 50/100: up to few months; 100/200: long term, possibly over a year | 2 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Short-term EMA greater than long-term EMA | 2 |
| Entry trigger & order type | Buy (fresh long) when short EMA turns greater than long EMA; order type not stated | 2 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Exit (square off) when short EMA turns lesser than long EMA; stay in trade while condition holds | 2 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| (short, long) EMA | none preferred | (9,21), (25,50), (50,100), (100,200) | 2 |

**Key quotes**
- "Buy (fresh long) when the short term moving averages turns greater than the long term moving average" [p. 2]
- "Exit the long position (square off) when the short term moving average turns lesser than the longer-term moving average" [p. 2]
- "longer the time frame, the lesser the number of trading signals" [p. 2]

**Pseudocode**
```
for (s,l) in pairs: ema_s=EMA(close,s); ema_l=EMA(close,l)
if flat and ema_s>ema_l and ema_s[1]<=ema_l[1]: buy next open
if long and ema_s<ema_l: sell next open
```

**Ambiguities & assumptions**
- Price source (close) not stated; ASSUMPTION: close. No stop or sizing: ASSUMPTION: crossover exit only, equal-weight. Short side ignored in NSE cash.

### 2.4 Support and resistance construction (Partly codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | other (level-identification tool) | 2 |
| Timeframe & holding period | Long-term S&R useful for swing trading; short-term S&R for intraday and BTST | 3 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Load data (short-term S&R: 3-6 months; long-term: 12-18 months); find at least 3 price action zones at the same price, well spaced in time; fit a horizontal line | 2, 3 |
| Entry trigger & order type | Not found in this text (S&R used as confirmation for entry/stop, see 2.15) | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Target set at the next support or resistance (see 2.15) | 11 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lookback, short-term S&R | 3-6 months | - | 2 |
| Lookback, long-term S&R | 12-18 months | "at least 2 years" when plotting S&R in the swing workflow | 2, 9 |
| Min price action zones | 3 | more spacing = stronger | 3 |
| Price-zone tolerance | Not given | - | - |

**Key quotes**
- "load at least 3-6 months of data points" [p. 2]
- "identify at least 3 price action zones" [p. 3]
- "Connect the three price action zones with a horizontal line." [p. 3]
- "Sharp reversals at a particular price point" [p. 3]

**Pseudocode**
```
zones = swing highs/lows where price hesitated or reversed (tolerance tol)
cluster zones by price within tol; keep clusters with >=3 zones separated by >= min_gap days
level = mean(cluster); support if level < close else resistance
```

**Ambiguities & assumptions**
- Zone definition ("hesitated", "sticky") is visual. ASSUMPTION: swing pivot with 3-bar left/right confirmation; tol = 1% of price; min_gap = 20 trading days.
- Lookback conflict: 12-18 months (p. 2) versus "at least 2 years" (p. 9). ASSUMPTION: 18 months for long-term, 2 years when used inside the swing checklist as p. 9-10 states.

### 2.5 RSI overbought/oversold (Fully codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion (with momentum alternative) | 3 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | If RSI stays fixed in a region for long, it indicates excess momentum: trade in the same direction rather than reverse | 3 |
| Setup conditions | RSI 0-30 oversold; 70-100 overbought (classical). Author prefers 0-20 and 80-100 | 3 |
| Entry trigger & order type | Oversold: look at buying; overbought: look at selling | 3 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lookback | 14 days | user may explore | 3 |
| Oversold / overbought | 20 / 80 (author's preference) | 30 / 70 classical | 3 |

**Key quotes**
- "A value between 0 and 30 is considered oversold" [p. 3]
- "I personally prefer to use 0-20 level and 80-100" [p. 3]
- "RSI is not used often as a standalone indicator by traders" [p. 3]

**Pseudocode**
```
r=RSI(close,14)
if r<20 (or 30): buy; if r>80 (or 70): exit long (shorts not possible in cash)
```

**Ambiguities & assumptions**
- Exit not given. ASSUMPTION: exit when RSI crosses back above 50, or after 10 days. The "same direction" prolonged-region rule has no duration; ASSUMPTION: skip it. Source says it is not standalone; ASSUMPTION: test it as a filter on 2.15.

### 2.6 MACD centerline and signal-line crossover (Partly codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / momentum | 4 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Variant A: MACD line crosses the zero line. Variant B: MACD line crosses its 9-day EMA signal line | 4 |
| Entry trigger & order type | A: cross from negative to positive = look at buying; B: MACD above signal = buying opportunity | 4 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Opposite cross: look at selling | 4 |
| Position sizing | Not found in this text (MACD used to increase size in 2.15) | 11 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Signal line | 9-day EMA of MACD | - | 4 |
| Fast/slow EMA | Not found in this text | - | - |

**Key quotes**
- "A 9-day signal line is an exponential moving average (EMA) of the MACD line." [p. 4]
- "a bulk of the movie would already be done" [p. 4]
- "the trader should look at buying opportunities" [p. 4]

**Pseudocode**
```
macd=EMA(close,12)-EMA(close,26); sig=EMA(macd,9)
A: long if macd crosses above 0; exit if crosses below 0
B: long if macd crosses above sig; exit if crosses below sig
```

**Ambiguities & assumptions**
- Fast and slow periods are not found in this text. ASSUMPTION: 12/26. The two variants are separate testable systems; the source argues B is earlier. "Look at buying" is not a hard order; ASSUMPTION: enter next open.

### 2.7 Bollinger Bands mean reversion (Fully codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion | 4 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Works in sideways markets, fails in a trending market (envelope expansion) | 5 |
| Setup conditions | 20-day SMA centre; bands at +2 SD and -2 SD | 4 |
| Entry trigger & order type | Short when price touches upper band; go long when price touches lower band | 4 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Expect reversion to the average (middle band) | 4 |
| Exits: trailing / time / signal | If the trade does not work almost immediately, check for envelope expansion (discretionary) | 5 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| SMA length | 20 | - | 4 |
| Band width | 2 SD | - | 4 |

**Key quotes**
- "The central black line is the 20 day SMA." [p. 4]
- "short the stock when the price touches the upper band" [p. 4]
- "BB works well in sideways markets and fails in a trending market" [p. 5]
- "I expect the trade to start working in my favour almost immediately" [p. 5]

**Pseudocode**
```
m=SMA(close,20); sd=STD(close,20); up=m+2sd; lo=m-2sd
long if low<=lo (or close<=lo); exit when close>=m
long-only on NSE cash; upper-band signals are exits only
```

**Ambiguities & assumptions**
- "Touches" means intrabar or close not stated; ASSUMPTION: close <= lower band. No stop. ASSUMPTION: time-stop of 5 days (from "almost immediately") and exit at the middle band. Regime filter: ASSUMPTION: skip when ADX(14) > 25 (ADX from p. 7).

### 2.8 Fibonacci retracement entry confirmation (Partly codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | pullback entry (confirmation tool) | 5 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Stock has had a sharp run-up | 5 |
| Setup conditions | Wait for retracement to 61.8%, 38.2% or 23.6% levels | 5 |
| Entry trigger & order type | Confirmation tool only: used with candlestick pattern, S&R at stop-loss, above-average volume | 5 |
| Initial stop-loss | Stop-loss should coincide with a Fibonacci level (adds conviction) | 5 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | "strong buy" when all confirm (no sizes stated) | 5 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Retracement levels | 61.8%, 38.2%, 23.6% | - | 5 |
| Swing anchor points | Not given | - | - |

**Key quotes**
- "Fibonacci retracement levels such as 61.8%, 38.2%, and 23.6%" [p. 5]
- "use the Fibonacci retracement as a confirmation tool" [p. 5]

**Pseudocode**
```
fib_ok = stop_price within tol of (swing_high - r*(swing_high-swing_low)) for r in {.236,.382,.618}
conviction_score += fib_ok
```

**Ambiguities & assumptions**
- Swing selection and tolerance not given. ASSUMPTION: last confirmed swing low to swing high; tol = 0.5% of price. 50% not listed in this text; not used.

### 2.9 Dow Theory patterns: range, breakout, flag, double/triple (Partly codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | range-trading / breakout | 6 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Check primary and secondary trend; a long trade against the secondary trend is worth a second thought | 9, 10 |
| Setup conditions | Range: stock oscillates between two price points. Breakout: above-average volume and sharp surge. Flag: second window to buy. Double/triple formations: reversal patterns | 6 |
| Entry trigger & order type | Buy at the lower price point of a range, sell at the higher; buy range breakout; buy flag | 6 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Sell at the higher price point of the range | 6 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Breakout volume | "above-average" | average length not given | 6 |
| Market phases | accumulation, mark up, distribution, markdown | - | 5, 6 |

**Key quotes**
- "A trader can buy at the lower price point, and sell at a higher price point." [p. 6]
- "A good breakout is characterized by above-average volumes and a sharp surge in prices." [p. 6]
- "the flag formation offers another window to buy" [p. 6]

**Pseudocode**
```
range: hi=max(high,N), lo=min(low,N) over a window with >=2 touches each; buy near lo, sell near hi
breakout: close>hi and volume>avg_vol(10) and (close/hi-1)>=x
```

**Ambiguities & assumptions**
- Window N, touch tolerance, "sharp surge" size and flag geometry are not given; "Dow Theory works on 9 basic tenets" but only phases and patterns are listed. ASSUMPTION: N=60 days, surge >= 3%, volume > 10-day average. Flag and double/triple tops are visual; treat as not codable without extra definitions.

### 2.10 ADX with DI crossover (Fully codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 7 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | ADX above 25 strong trend; below 20 no strength; 20-25 grey area | 7 |
| Setup conditions | ADX is 25 (above 25) | 7 |
| Entry trigger & order type | Buy when +DI crosses over -DI (ADX at 25); sell when -DI crosses over +DI | 7 |
| Initial stop-loss | Low of the signal candle (buy); high of signal candle (short) | 7 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Trade stays valid until stop-loss is breached, even if the DI crossover reverses | 7 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| ADX period | 14 | - | 7 |
| ADX threshold | 25 | below 20 weak; 20-25 grey | 7 |

**Key quotes**
- "A buy signal is generated when ADX is 25" [p. 7]
- "The stop loss is usually the low of the signal candle" [p. 7]
- "The trade stays valid till the stoploss is breached" [p. 7]
- "The default lookback period for ADX is 14 days" [p. 7]

**Pseudocode**
```
if ADX14>=25 and +DI crosses above -DI: buy next open; stop=low[signal]
exit only when low <= stop (no profit target)
```

**Ambiguities & assumptions**
- "ADX is 25" is read as ">= 25". ASSUMPTION: ">= 25". No target, so a loss-only exit means open-ended hold; ASSUMPTION: add an ATR trail or 3x risk target as a test variant only. Stop can be very close; ASSUMPTION: skip if stop distance < 0.5%.

### 2.11 Alligator (13/8/5 SMAs) (Fully codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 7 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | When 13, 8, 5 MAs are intertwined or flat = no-trade zone; stay out | 7 |
| Setup conditions | Buy: all three MAs separated; price > 5MA > 8MA > 13MA. Sell: price < 5MA < 8MA < 13MA | 7 |
| Entry trigger & order type | Signal confirms trend; "it is upto the trader to identify a good entry point within this trend" | 7 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not stated; implied when order breaks / MAs intertwine | 7 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Jaw / teeth / lips | 13 / 8 / 5 simple MAs | displacement mentioned, size not given | 7 |

**Key quotes**
- "The price is above the 5MA, 5MA is above 8MA, and 8MA is above 13 MA." [p. 7]
- "it is upto the trader to identify a good entry point within this trend" [p. 7]
- "Offsetting or displacing the moving average reduces the number of whipsaws in the average." [p. 7]

**Pseudocode**
```
up = close>sma5>sma8>sma13 and gaps > eps
enter long on first bar up becomes true; exit when not up
```

**Ambiguities & assumptions**
- "Separated" gap, entry timing, exit and displacement not given. ASSUMPTION: gap eps = 0.1% of price; enter on first bar of alignment; exit when close < 8MA or alignment breaks; no displacement. Use SMA of close as stated.

### 2.12 Aroon (25-day) crossover (Fully codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Aroon Up = days since last 25-day high; Aroon Down = days since last 25-day low; range 0-100 | 8 |
| Entry trigger & order type | Buy when Aroon Up above 50 and Aroon "low" (Down) below 30; sell when Aroon Down above 50 and Aroon Up below 30 | 8 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lookback | 25 days | - | 8 |
| Up/Down thresholds | 50 / 30 | - | 8 |

**Key quotes**
- "The default value for Aroon is 25 days." [p. 8]
- "A buy is generated when Aroon up is above 50 and Aroon low is below 30" [p. 8]

**Pseudocode**
```
up=100*(25-days_since_high25)/25; dn=100*(25-days_since_low25)/25
buy if up>50 and dn<30; sell/exit if dn>50 and up<30
```

**Ambiguities & assumptions**
- Exit not given. ASSUMPTION: exit long on the sell condition. "Aroon low" read as Aroon Down. Formula normalisation (25 vs 26 bars) not given; ASSUMPTION: 25-bar window.

### 2.13 Aroon Oscillator (Fully codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Oscillator = Aroon Up minus Aroon Down, range -100 to +100 | 8 |
| Entry trigger & order type | Positive = uptrend favoured; surge above +50 = strong upside move; below -50 = strong downside move. No explicit entry stated | 8 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Strength threshold | +50 / -50 | zero line as centre | 8 |

**Key quotes**
- "a surge above +50 would reflect a strong upside move" [p. 8]
- "time and price favour an uptrend when the indicator is positive" [p. 8]

**Pseudocode**
```
osc=aroon_up-aroon_down; long if osc>50 (strong) or >0 (weak); exit if osc<0
```

**Ambiguities & assumptions**
- Only interpretation, no trade rule. ASSUMPTION: long when osc crosses above +50; exit when it crosses below 0.

### 2.14 ATR band breakout (Partly codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout / trend-following | 9 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Upper band = moving average + ATR; lower band = moving average - ATR | 8 |
| Entry trigger & order type | Price penetrating the upper envelope: expect continuation higher (long); below lower: continues lower | 9 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| MA type/length, ATR period, multiplier | Not found in this text | - | - |

**Key quotes**
- "The ATR value is added to the moving average value" [p. 8]
- "If the stock price penetrates either the upper or lower envelop" [p. 9]
- "an alternative to the Bollinger Bands trading system" [p. 9]

**Pseudocode**
```
ma=SMA(close,n); up=ma+ATR(14); lo=ma-ATR(14)
long if close>up; exit if close<ma
```

**Ambiguities & assumptions**
- The text positions it as an alternative to Bollinger Bands, which are mean-reverting (2.7), but the described expectation is continuation. Both versions recorded; ASSUMPTION: follow the stated continuation rule. ASSUMPTION: SMA(20), ATR(14), multiplier 1, exit at MA.

### 2.15 Scout and Grand Checklist: candlestick swing trade (Partly codable)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | candlestick reversal swing with confluence | 10, 11 |
| Timeframe & holding period | End of day data; positional trades, with option to square off intraday if target hits the same day | 10 |
| Universe / eligibility filters | Nifty 50 stocks | 10 |
| Market / regime filter | Establish primary and secondary trend; if the long trade is counter to the secondary trend, think twice | 10, 11 |
| Setup conditions | Recognisable candlestick pattern in the last 3 (max 4) candles; prior trend opposite to pattern (downtrend for bullish, uptrend for bearish); volume >= 10-day average; S&R coincides with pattern stop-loss | 10, 11 |
| Entry trigger & order type | After steps pass and RRR >= 1.5; order type not stated | 11 |
| Initial stop-loss | As defined by the candlestick pattern; S&R should coincide; reject if S&R is more than 4% away from the stop-loss | 11 |
| Exits: profit-taking | Target = next support or resistance level | 11 |
| Exits: trailing / time / signal | Do nothing until target or stop-loss; may trail the stop-loss | 11 |
| Position sizing | Increase trade size if MACD and RSI confirm and there is spare cash (no formula) | 11 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Usually at most 1 or 2 of 4-5 shortlisted stocks qualify | 11 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pattern window | last 3 candles | max 4 | 10 |
| Volume | >= 10-day average volume | "above average volumes on both buy and sell day" | 9, 11 |
| Stop to S&R distance | <= 4% | - | 11 |
| Min RRR | 1.5 | beginners as high as possible | 9, 11 |
| Chart lookback | 6 months to 1 year (S&R: 2 years) | scalper 5 days | 9, 10 |

**Key quotes**
- "my attention is only on the recent 3 or maximum of 4 candles" [p. 10]
- "The volume should be at least equal to or more than the 10-day average volume." [p. 11]
- "If the S&R level is more than 4% away from the stoploss" [p. 11]
- "The minimum RRR should be at least 1.5" [p. 11]
- "do nothing until your target is achieved, or stoploss is triggered" [p. 11]

**Pseudocode**
```
for s in NIFTY50: if pattern(s, last 3 bars) and prior_trend matches:
  if volume>=SMA(volume,10) and abs(sr_level-stop)/stop<=0.04:
    target=next S&R beyond entry; rrr=(target-entry)/(entry-stop)
    if rrr>=1.5: buy next open, stop=pattern stop; hold until target or stop (optional trailing)
  size up if MACD and RSI confirm
```

**Ambiguities & assumptions**
- Candlestick patterns are not defined here (Bullish Marubozu is the only one named, with shadow length judged relative to range; p. 11). ASSUMPTION: test a small set (engulfing, hammer, morning star) with standard definitions. "Prior trend" is not defined; ASSUMPTION: close < SMA(50) for bullish. Only the first-listed S&R test (4%) is numeric; "Nifty 50 universe" ASSUMPTION: replace with top-50 by turnover as point-in-time constituents are unavailable. Target uses the S&R of 2.4.

### 2.16 Not found / non-codable headings
- "Super Trend", "Combine with SMI and donchain channe", "Parabolic SAR" and "Moving averages" appear only as headings with no rules [p. 1]. Not codable from this text.
- Dow Theory "9 basic tenets" are announced but not listed beyond the three phases [p. 5].

## 3. Risk & money-management rules
- Minimum risk-reward ratio of 1.5 for an active trader; beginner as high as possible [p. 10]; RRR >= 1.5 in the Scout [p. 11].
- Stop-loss must coincide with an S&R level; reject if S&R is more than 4% from the stop [p. 5, 11].
- Scale up trade size if indicators confirm; otherwise go ahead with the original plan [p. 10].
- Once placed, do nothing until target or stop; trailing the stop is acceptable [p. 11].
- No position-size formula, risk per trade, or drawdown rule is found in this text.

## 4. Non-codable guidance
- Deciding not to trade is a decision; at most 1 or 2 of 4-5 shortlisted stocks qualify [p. 11].
- Spend 15-20 minutes on each shortlisted chart [p. 11].
- RSI parameters: explore the ones that work for you [p. 3].
- Use indicators as confirmation, not standalone [p. 3, 5].
- Missed trade: wait for a retracement or flag [p. 5, 6].
- Risk-loving traders may act on a Heikin Ashi trend-change candle; others wait for confirmation [p. 1].
- Use Zerodha Pi, end-of-day data [p. 10].

## 5. Adapting to NSE (Indian equities)
- **Data required:** Daily OHLC and volume (all strategies); optional delivery % as a volume-quality proxy; Nifty 50 constituents (point-in-time membership list); no fundamentals needed.
- **Testability with our data:** Everything in 2.1-2.14 can be backtested on 2005-2026 prices. 2.15 can be backtested only after pattern rules are fixed; Nifty 50 membership is needed (ASSUMPTION: use top 50 by trailing turnover). Nothing needs fundamentals. Intraday square-off cannot be tested on daily bars.
- **Market-structure differences:** The material is already Indian-market oriented. Short signals (HA, ADX sell, Alligator sell, Bollinger upper band, RSI overbought) cannot be held overnight in NSE cash: ASSUMPTION: use them as long-exit signals only. Apply STT, brokerage and 0.1% slippage; short-horizon systems (9/21 EMA, Bollinger, RSI) are most cost-sensitive. Circuit limits can block stop execution: ASSUMPTION: fill stops at next open if gapped. Delisted stocks included, so EMA and ADX systems must handle exit on delisting.

## 6. Verdict
- **Codeability:** Partly. Indicator rules (EMA, RSI, MACD, BB, ADX, Alligator, Aroon) are codable; candlestick, S&R, Dow patterns and the checklist need discretionary elements defined, and several parameters are missing.
- **Priority for backtesting:** Medium. Indicator systems are quick, standard tests with no source evidence; the Scout checklist is the only multi-factor system but is discretionary.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating "buying opportunity" statements (RSI, MACD, smart money) as hard entry/exit orders when the source gives no exit or stop.
  2. Implementing short signals in the NSE cash market, and ignoring that the ADX trade has a stop but no target.
  3. Coding S&R and candlestick confluence loosely: the 4% stop-to-S&R test, 3-candle window, prior-trend and 10-day volume conditions must all be combined, and the S&R needs 3 well-spaced zones.
