# Tools of the Trade (Investopedia compilation) — Investopedia (no byline)

- **Source file:** Google Drive invest/Tools of the Trade.docx (7.85 MB docx; the size is images). Text is a compilation of three Investopedia web pieces: "Tools of the Trade" (7 indicators, https://www.investopedia.com/articles/technical/04/040704.asp), an Ichimoku "Key Elements" section, and "Stochastics: An Accurate Buy and Sell Indicator".
- **Text file used:** text/investopedia_tools_of_trade.txt  (page basis: sections — one `[[PAGE N]]` per article section, no Word page breaks available). The docx is above the connector's binary-download limit, so the coordinator took the Google Drive plain-text rendering (complete; it ends at the article's last sentence) and wrote it out with hyperlink URLs removed.
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file. Section map: p.1 intro/overlays vs oscillators, p.2 OBV, p.3 A/D line, p.4 ADX, p.5 Aroon, p.6 MACD, p.7 RSI, p.8 Stochastic oscillator, p.9 Bottom Line, p.10 Ichimoku key elements, p.11 Stochastics article.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - Verified with `python ../work/bin/verify_citations.py specs/investopedia_tools_of_trade.md text/investopedia_tools_of_trade.txt`.
- **Coverage:** Read lines 1-177 of the text file in full; last `[[PAGE N]]` reached = 11. Nothing skimmed. Missing from the text: all charts/images in the docx, and the %D (D line) formula, which was an image and appears only as the placeholder "[formula image not present in the connector text]" (not found in this text; not filled from general knowledge). *Coordinator check: the docx (7.85 MB) is above the connector's binary-download limit, so the coordinator took Drive's complete plain-text rendering, removed the hyperlink URLs and split it into 11 section pages (page basis = article sections, not Word pages). The coordinator re-ran verify_citations (37/37 ok) and an exact-page strict check (0 off-by-one). Every Page-column value in 2.1-2.10 was checked against its indicator's section page (OBV p.2, A/D p.3, ADX p.4, Aroon p.5, MACD p.6, RSI p.7 and p.11, Stochastic p.8 and p.11, Ichimoku p.10); all are consistent. All 10 subsections have the full 12-row table.*

## 1. The method in brief

This is not a single system but an indicator primer for "day traders and technical analysts" [p. 1]. It splits indicators into overlays (same scale as price) and oscillators (plotted above/below price), and says it mainly covers oscillators [p. 1]. Seven indicators (OBV, A/D line, ADX, Aroon, MACD, RSI, Stochastic) are described with qualitative signal statements [p. 2-8], followed by an Ichimoku component glossary with two buy/sell cross statements [p. 10] and a second Stochastics piece [p. 11]. Rules are given as signal statements only; stops, targets, sizing, universe and backtest evidence are absent. The text itself says indicators are used "in tandem", can be combined with subjective chart-pattern analysis, and "can also be incorporated into automated trading systems given their quantitative nature" [p. 1]. The recommended way to choose is to "try them out in a demo account" [p. 9]. No performance or track-record evidence is presented anywhere.

Where the text gives no lookback, parameters are not stated here as the author's; they are marked ASSUMPTION. Stated in the text: Aroon period "typically 25" [p. 5], Stochastic 14 [p. 11], Ichimoku 9/26/52 [p. 10].

## 2. Strategies

Each subsection is one separately testable signal rule. Common gaps (apply to all 2.x unless overridden): holding period, universe, stops, targets, sizing and portfolio limits are "Not found in this text". Defaults are proposed under each Ambiguities block, marked ASSUMPTION.

### 2.1 On-Balance Volume (OBV) trend confirmation and price/OBV divergence

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Volume-based trend confirmation / divergence (filter; reversal warning) | 2 |
| Timeframe & holding period | Not found in this text (daily bars implied by "Each day") | 2 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | OBV is a running total of up volume minus down volume; up volume = volume on a day price rallied, down volume = volume on a day price fell. Rising price with rising OBV = trend continuation. Price rising while OBV falling = trend not backed by strong buyers, could reverse. | 2 |
| Entry trigger & order type | Not found in this text (OBV is described as a confirmation tool, not an entry trigger; no order type) | 2 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Price rising with OBV falling "could soon reverse" (warning, no explicit exit) | 2 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| OBV accumulation | +volume if close up, -volume if close down | none | 2 |
| Slope / divergence window | Not found in this text | none | - |

**Key quotes**
- "The indicator is a running total of up volume minus down volume." [p. 2]
- "If price and OBV are rising, that helps indicate a continuation of the trend." [p. 2]
- "If the price is rising but OBV is falling, that could indicate that the trend is not backed by strong buyers and could soon reverse." [p. 2]

**Pseudocode**
```
obv[0]=0
obv[t] = obv[t-1] + (vol[t] if close[t]>close[t-1] else -vol[t] if close[t]<close[t-1] else 0)
confirm_up   = slope(close, N)>0 and slope(obv, N)>0        # N = ASSUMPTION 20
bear_diverge = slope(close, N)>0 and slope(obv, N)<0        # warning flag / filter for longs
```

**Ambiguities & assumptions**
- Unchanged-close day treatment: not found in this text. ASSUMPTION: add 0.
- No slope/divergence window defined. ASSUMPTION: N=20 days, slope by linear regression sign (or 20-day change sign).
- No trade rule. ASSUMPTION: use as an entry filter (require OBV slope > 0 for longs) and a warning flag, tested as a filter on another entry.

### 2.2 Accumulation/Distribution (A/D) line trend confirmation and divergence

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Volume/money-flow trend confirmation / divergence | 3 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | A/D uses the period's range and where the close sits in it; close near the high gives volume more weight than a close near the midpoint. Trending up = buying interest, confirms uptrend. Falling = closes in lower portion of range, volume negative, confirms downtrend. | 3 |
| Entry trigger & order type | Not found in this text. Divergence: price trending lower while A/D starts rising "could signal higher prices to come" (no trigger defined) | 3 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | A/D starts falling while price is rising = "trend is in trouble and could reverse" (warning, no explicit exit) | 3 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| A/D formula (close location weighting) | Not found in this text (only described qualitatively) | none | 3 |
| Slope / divergence window | Not found in this text | none | - |

**Key quotes**
- "If a stock finishes near its high, the indicator gives volume more weight than if it closes near the midpoint of its range." [p. 3]
- "If the A/D starts falling while the price is rising, this signals that the trend is in trouble and could reverse." [p. 3]
- "if the price is trending lower and A/D starts rising, that could signal higher prices to come." [p. 3]

**Pseudocode**
```
clv[t]  = ((close-low) - (high-close)) / (high-low)     # ASSUMPTION: standard money-flow multiplier, not in text
ad[t]   = ad[t-1] + clv[t]*vol[t]
bear_div = slope(close,N)>0 and slope(ad,N)<0
bull_div = slope(close,N)<0 and slope(ad,N)>0           # candidate long watch-list flag
```

**Ambiguities & assumptions**
- Exact formula not given. ASSUMPTION: use the standard close-location-value formula above; zero-range bars set clv=0.
- Divergence window not given. ASSUMPTION: N=20.
- Text says OBV and A/D each "will work better in some cases" [p. 3] but gives no criteria to choose.

### 2.3 ADX / DI trend-state classification

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following filter / trend-strength classifier | 4 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | ADX below 20 = weak trend or ranging (DI+ and DI- crisscrossing); ADX above 40 = strong directional strength | 4 |
| Setup conditions | Uptrend: ADX above 20 and DI+ above DI-. Downtrend: ADX above 20 and DI- above DI+. | 4 |
| Entry trigger & order type | Not found in this text (states define trend; no explicit entry.) | 4 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Implied: state changes (DI- above DI+, or ADX falls below 20). Not stated as an exit rule. | 4 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| ADX trend threshold | 20 | weak below 20 | 4 |
| ADX strong-trend threshold | 40 | none | 4 |
| ADX / DI period | Not found in this text | none | - |

**Key quotes**
- "When the ADX is above 40, the trend is considered to have a lot of directional strength" [p. 4]
- "When the ADX indicator is below 20, the trend is considered to be weak or non-trending." [p. 4]
- "ADX above 20 and DI+ above DI-: That's an uptrend." [p. 4]

**Pseudocode**
```
uptrend   = ADX(n)>20 and DIplus(n)>DIminus(n)
downtrend = ADX(n)>20 and DIminus(n)>DIplus(n)
range_    = ADX(n)<20
strong    = ADX(n)>40
long_signal = uptrend and not uptrend[t-1]      # ASSUMPTION
exit_long   = not uptrend                       # ASSUMPTION
```

**Ambiguities & assumptions**
- ADX/DI period not given. ASSUMPTION: n=14 (standard; not stated by the author).
- ADX between 20 and 40: classed as trend per bullet rules; 40 only labelled "a lot of directional strength". ASSUMPTION: 40 is informational, not a gate.
- ADX exactly 20 and the gap 20 to "not above 20": not defined. ASSUMPTION: >20 means trend, <=20 means no trend.
- No entry/exit given. ASSUMPTIONS as in pseudocode. Short-side (downtrend) is for context only on NSE cash.

### 2.4 Aroon crossover

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following / trend-change detection | 5 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Aroon measures whether price is hitting new highs/lows over the calculation period (typically 25). Two lines: Aroon-up and Aroon-down. | 5 |
| Entry trigger & order type | Aroon-up crosses above Aroon-down = "first sign of a possible trend change"; confirmation of uptrend when Aroon-up hits 100 and stays relatively close while Aroon-down stays near zero. Order type not found in this text. | 5 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Reverse: Aroon-down crossing above Aroon-up and staying near 100 = downtrend in force | 5 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Aroon period | 25 ("typically") | none | 5 |
| Confirmation level | Aroon-up near 100, Aroon-down near zero (no numbers) | none | 5 |

**Key quotes**
- "(typically 25)" [p. 5]
- "When the Aroon-up crosses above the Aroon-down, that is the first sign of a possible trend change." [p. 5]
- "If the Aroon-up hits 100 and stays relatively close to that level while the Aroon-down stays near zero, that is positive confirmation of an uptrend." [p. 5]

**Pseudocode**
```
up   = 100*(25 - bars_since_highest_high(25))/25     # ASSUMPTION: standard formula, not in text
down = 100*(25 - bars_since_lowest_low(25))/25
cross_up = up>down and up[t-1]<=down[t-1]
confirmed = up>=70 and down<=30                      # ASSUMPTION thresholds
enter_long = cross_up (variant B: cross_up then confirmed within 10 bars)
exit_long  = down>up and down[t-1]<=up[t-1]
```

**Ambiguities & assumptions**
- "Near 100"/"near zero"/"relatively close" undefined. ASSUMPTION: up>=70 and down<=30.
- Formula not in text. ASSUMPTION: standard Aroon definition.
- Crossover is "first sign" only. ASSUMPTION: test both A (enter on cross) and B (wait for confirmation).

### 2.5 MACD signal-line cross filtered by the zero line

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend/momentum-following | 6 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | MACD above zero = upward phase; below zero = bearish period; zero-line side decides which signals to follow | 6 |
| Setup conditions | MACD line above zero (for longs). Signal line "moves slower" than MACD line. | 6 |
| Entry trigger & order type | Long: MACD crosses above signal line while MACD above zero ("watch for the MACD to cross above the signal line to buy"). Order type not found in this text. | 6 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | MACD crossing below signal line indicates price falling; with MACD below zero this is the possible short signal. Exit of longs on cross-down is implied, not stated. | 6 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Fast / slow / signal periods | Not found in this text | none | - |
| Zero-line filter | 0 | none | 6 |

**Key quotes**
- "When the MACD is above zero, the price is in an upward phase." [p. 6]
- "if the indicator is above zero, watch for the MACD to cross above the signal line to buy." [p. 6]
- "If the MACD is below zero, the MACD crossing below the signal line may provide the signal for a possible short trade." [p. 6]

**Pseudocode**
```
macd = EMA(close,12)-EMA(close,26); sig = EMA(macd,9)      # ASSUMPTION periods
enter_long = macd>0 and macd[t-1]<=sig[t-1] and macd>sig
exit_long  = macd<sig and macd[t-1]>=sig[t-1]              # ASSUMPTION
short_signal (not tradeable in NSE cash) = macd<0 and cross below sig
```

**Ambiguities & assumptions**
- Periods not given. ASSUMPTION: 12/26/9 EMAs (standard; not the author's).
- Text says "watch for", i.e. not mandatory entry. ASSUMPTION: enter at next open after signal bar's close.
- Long exit not stated. ASSUMPTION: exit on cross below signal line (regardless of zero line).
- MACD below zero and cross up: not addressed. ASSUMPTION: ignored.

### 2.6 RSI overbought/oversold re-cross

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion (counter-trend) | 7 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | In uptrends RSI holds above 30 and reaches 70+; in downtrends it holds below 70 and reaches 30 or below (context, not a stated filter) | 7 |
| Setup conditions | RSI above 70 = overbought, could decline; below 30 = oversold, could rally. Author warns "making this assumption is dangerous". | 7 |
| Entry trigger & order type | Buy when RSI drops below 30 and then rises back above 30; sell when RSI rises above 70 then drops below 70 ("some traders" do this). Order type not found in this text. | 7 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Sell on re-cross below 70 (stated as "before selling") | 7 |
| Exits: trailing / time / signal | Not found in this text beyond the above | 7 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Overbought / oversold | 70 / 30 | 80 / 20 mentioned for a "normalized" oscillator | 7, 11 |
| RSI period | Not found in this text | none | - |

**Key quotes**
- "When RSI moves above 70, the asset is considered overbought and could decline." [p. 7]
- "some traders wait for the indicator to rise above 70 and then drop below before selling, or drop below 30 and then rise back above before buying." [p. 7]
- "It is usually set at either the 20 to 80 range or the 30 to 70 range." [p. 11]

**Pseudocode**
```
r = RSI(close,14)                                   # ASSUMPTION period
enter_long = r[t-1]<30 and r[t]>=30                 # re-cross up
exit_long  = r[t-1]>70 and r[t]<=70                 # re-cross down
```

**Ambiguities & assumptions**
- Period not given. ASSUMPTION: 14 (author does not state it for RSI; 14 appears only for stochastics [p. 11]).
- Whether "drop below" must be a close and whether a trend filter applies: not stated. ASSUMPTION: close-based, optionally test with a trend filter (e.g. close above 200-day MA).
- Exit for a long bought at 30 re-cross when 70 is never reached: not found in this text. ASSUMPTION: add time stop of 20 bars and a 8% stop for testing only.
- Variant 20/80 thresholds are mentioned [p. 11]; test as alternative.

### 2.7 Stochastic oscillator 20/80 with trend filter (section p.8)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-filtered pullback / mean-reversion | 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | "Consider the overall price trend": signals taken in trend direction; in an uptrend 80+ readings are less consequential; in a downtrend 20 is less significant. Trend definition not given. | 8 |
| Setup conditions | Uptrend present; stochastic (0-100) drops below 20. Above 80 overbought, below 20 oversold. | 8 |
| Entry trigger & order type | Long: during an uptrend, indicator drops below 20 and rises back above it. Order type not found in this text. | 8 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Downtrend short setup: indicator above 80 then drops back below (mirror). No long-exit rule stated. | 8 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Overbought / oversold | 80 / 20 | none | 8 |
| Stochastic lookback | "a number of periods" (none given on this page); 14 on p. 11 | 14 days/weeks/months | 8, 11 |
| Trend definition | Not found in this text | none | - |

**Key quotes**
- "Values above 80 are considered overbought, while levels below 20 are considered oversold." [p. 8]
- "during an uptrend, when the indicator drops below 20 and rises back above it, that is possible buy signal." [p. 8]
- "During a downtrend, look for the indicator to move above 80 and then drop back below to signal a possible short trade." [p. 8]

**Pseudocode**
```
k = 100*(close - LL(14))/(HH(14) - LL(14))          # formula from p.11; period 14 per p.11
uptrend = close > SMA(close,50)                     # ASSUMPTION trend filter
enter_long = uptrend and k[t-1]<20 and k[t]>=20
exit_long  = k[t-1]>80 and k[t]<=80                 # ASSUMPTION mirror rule
```

**Ambiguities & assumptions**
- Trend definition absent. ASSUMPTION: close above 50-day SMA (or ADX uptrend state from 2.3).
- Whether the smoothed %D or the raw %K is used on p.8: not found in this text. ASSUMPTION: %K (raw) because only %K formula is in the text; %D smoothing length is not in this text.
- No long-exit rule. ASSUMPTION: mirror (80 re-cross down), or exit on trend-filter loss.
- Internal tension with p.11 (see 2.8): record both; this version is used as primary because it is explicit about the re-cross and trend filter.

### 2.8 Stochastics buy/sell (article on p.11, volume-confirmed)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Mean-reversion / overbought-oversold | 11 |
| Timeframe & holding period | Time unit can be days, weeks or months; 14 periods "most often used"; sector view example 14 months | 11 |
| Universe / eligibility filters | Individual issue or an entire sector/industry | 11 |
| Market / regime filter | Not found in this text (no trend filter, unlike p.8) | - |
| Setup conditions | Watch the D line (slower) and price move into overbought (over 80) or oversold (under 20). Use with RSI "in conjunction". | 11 |
| Entry trigger & order type | Consider buying an issue below the 20 line "and is starting to move up with increased volume". Order type not found in this text. | 11 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Consider selling when the indicator moves above 80 | 11 |
| Exits: trailing / time / signal | Same as above; no other exits | 11 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| %K formula | 100*(CP-L14)/(H14-L14); CP = latest close, L14 / H14 = lowest / highest price of the 14 previous sessions | days, weeks or months | 11 |
| %D formula | Not found in this text (formula image missing) | none | 11 |
| Overbought / oversold | 80 / 20 | RSI-style 30 / 70 mentioned | 11 |
| "Increased volume" threshold | Not found in this text | none | - |

**Key quotes**
- "Fourteen is the mathematical number most often used in the time mode." [p. 11]
- "The investor needs to consider selling the stock when the indicator moves above the 80 levels." [p. 11]
- "consider buying an issue that is below the 20 line and is starting to move up with increased volume" [p. 11]

**Pseudocode**
```
k = 100*(close - LL(14,low))/(HH(14,high) - LL(14,low))
d = SMA(k,3)                                         # ASSUMPTION: %D formula not found in text
buy  = d[t-1]<20 and d[t]>d[t-1] and vol[t] > SMA(vol,20)    # ASSUMPTION for "increased volume"
sell = d[t]>80
```

**Ambiguities & assumptions**
- Tension between pages: p.8 buys only after dropping below 20 and rising back above it, within an uptrend; p.11 says "consider buying" while still below 20 once it starts moving up with increased volume, and "consider selling" on any move above 80 (p.8 says 80+ rallies in an uptrend are "less consequential"). ASSUMPTION: 2.7 is primary; 2.8 tested as a variant (earlier entry, no trend filter, volume confirmation).
- %D formula missing. ASSUMPTION: 3-period SMA of %K, flagged as not from this text.
- Text says "(CP - L14)/(H14 - L14)" uses "14 previous" sessions; whether the current bar is included is not stated. ASSUMPTION: include current bar.
- "Starting to move up" undefined. ASSUMPTION: indicator greater than prior bar.

### 2.9 Ichimoku Chikou span cross

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following signal | 10 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text on this signal (see 2.10 for cloud context) | - |
| Setup conditions | Chikou span = today's closing price projected back 26 days; used as a support/resistance aid | 10 |
| Entry trigger & order type | Chikou span crosses the price bottom-up = buy signal. Order type not found in this text. | 10 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Chikou crossing price top-down = sell signal | 10 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Chikou displacement | 26 periods back | none | 10 |

**Key quotes**
- "Chikou span calculation: today's closing price projected back 26 days on the chart." [p. 10]
- "If the Chikou Span or the green line crosses the price in the bottom-up direction, that is a buy signal." [p. 10]
- "If the green line crosses the price from the top-down, that is a sell signal." [p. 10]

**Pseudocode**
```
# chikou plotted at bar t-26 has value close[t]
# "crosses the price" compared with price at the bar where chikou is plotted
cross_up   = close[t] > close[t-26] and close[t-1] <= close[t-27]
cross_down = close[t] < close[t-26] and close[t-1] >= close[t-27]
enter_long = cross_up ; exit_long = cross_down      # ASSUMPTION exit
```

**Ambiguities & assumptions**
- Which price the Chikou crosses (close, or the candle high/low) is not stated. ASSUMPTION: close[t] vs close[t-26] (equivalent to a 26-bar momentum sign change).
- Take care of look-ahead: the plotted position is in the past; no future data is used by the formula above.
- Exit is only the opposite signal. ASSUMPTION: exit on cross_down.

### 2.10 Ichimoku Kumo / Kijun / Tenkan context rules

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (components and bias rules) | 10 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Bullish when Senkou Span A above Senkou Span B, bearish vice versa. Cloud angle and thickness indicate strength; thin cloud is weak and prices "tend to break through". Kumo twists in future clouds = potential reversal. | 10 |
| Setup conditions | Price above Kijun-sen: could continue higher; below: could keep dropping. Tenkan-sen moving up/down = trending; horizontal = ranging. Price above the cloud: top line first support, bottom line second support. | 10 |
| Entry trigger & order type | Not found in this text (no explicit entry from these elements other than the Chikou cross in 2.9) | - |
| Initial stop-loss | Not found in this text. Kijun-sen "can be used as a trailing stop line" | 10 |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Kijun-sen as trailing stop line (precise rule not given) | 10 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Tenkan-sen | (highest high + lowest low)/2 over 9 periods | none | 10 |
| Kijun-sen | (highest high + lowest low)/2 over 26 periods | none | 10 |
| Senkou span A | (Tenkan-sen + Kijun-sen)/2 plotted 26 periods ahead | none | 10 |
| Senkou span B | (highest high + lowest low)/2 over 52 periods, plotted 26 ahead | none | 10 |
| Chikou span | close shifted 26 periods back | none | 10 |
| Cloud thickness threshold ("thin") | Not found in this text | none | - |

**Key quotes**
- "Tenkan-sen calculation: (highest high + lowest low)/2 for the last 9 periods." [p. 10]
- "Senkou span B calculation: (highest high + lowest low)/2 calculated over the past 52 time periods and plotted 26 periods ahead." [p. 10]
- "Generally, markets are bullish when Senkou Span A is above Senkou Span B and vice versa when markets are bearish." [p. 10]
- "can be used as a trailing stop line" [p. 10]

**Pseudocode**
```
tenkan = (HH9+LL9)/2 ; kijun = (HH26+LL26)/2
spanA[t+26] = (tenkan[t]+kijun[t])/2 ; spanB[t+26] = (HH52+LL52)/2
cloud_top[t] = max(spanA[t], spanB[t]) ; cloud_bot[t] = min(...)   # values as computed 26 bars earlier
bull_regime = spanA[t] > spanB[t] and close > cloud_top
long_filter = bull_regime and close > kijun
exit_trail  = close < kijun                           # ASSUMPTION
```

**Ambiguities & assumptions**
- No entry rule. ASSUMPTION: combine as filters for 2.9 (long only if close above cloud top and close above Kijun).
- Trailing stop mechanics (close vs intraday, ratcheting) not given. ASSUMPTION: exit at next open when close < Kijun-sen.
- "Thin cloud" undefined. ASSUMPTION: thickness < 1 ATR(14) of price.
- Tenkan/Kijun cross is not mentioned as a signal in this text (not found in this text).

## 3. Risk & money-management rules

Not found in this text. The text contains no stop-loss, position size, risk-per-trade, max exposure or drawdown rule. The only risk-related statements: the RSI overbought/oversold assumption "is dangerous" on its own [p. 7]; traders may use several indicators "in tandem" [p. 1]; test indicators in a demo account and "Pick the ones you like the most, and leave the rest" [p. 9]; Kijun-sen "can be used as a trailing stop line" [p. 10].

Proposed ASSUMPTION defaults for testing only: 2-3% of equity risk per trade with 2x ATR(14) initial stop; max 10 concurrent positions; equal-risk sizing.

## 4. Non-codable guidance

- Combine several indicators and optionally subjective chart-pattern analysis to form trade ideas [p. 1].
- Choose indicators that "work best for them" and become familiar with them [p. 1]; trial them in a demo account [p. 9].
- OBV vs A/D: "OBV will work better in some cases and A/D will work better in others" [p. 3] (no selection criterion).
- RSI divergence (indicator moves opposite to price: trend weakening, could reverse) [p. 7], and RSI as support/resistance regime (holds above 30 in uptrends, below 70 in downtrends) [p. 7]: stated without thresholds or windows; use as discretionary context or as flags with ASSUMPTION windows.
- OBV/A/D divergence (see 2.1, 2.2) is only partly codable because windows are undefined.
- Ichimoku: kumo twists, cloud angle, thick vs thin cloud, Kumo shadows [p. 10]; Tenkan "turning line" flat = ranging [p. 10].
- Stochastics on a sector as a whole (14 months of industry range) [p. 11]; use together with RSI [p. 11].
- New investors should concentrate on the basics of stochastics rather than "tweaking" [p. 11].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLC and volume (adjusted for splits and bonuses) for all signals. No delivery %, index or fundamentals needed. Optional: NIFTYBEES for a market filter (not in the text).
- **Testability with our data:** all rules (2.1-2.10) are backtestable on 2005-2026 daily data including delisted names. The text's weekly/monthly mentions can be tested by resampling. Nothing needs data we do not have. The %D formula is not in this text and must be fixed by ASSUMPTION.
- **Market-structure differences:**
  - Short signals (MACD below zero, Stochastic downtrend, ADX downtrend, Aroon downtrend, Chikou cross-down) cannot be traded in the NSE cash market overnight. ASSUMPTION: treat bearish signals as exit-only for long positions.
  - Costs: STT, brokerage and about 0.1% slippage; oscillator re-cross systems trade often, so net-of-cost testing matters. ASSUMPTION: 0.1% slippage each side plus statutory costs.
  - Circuit limits and low liquidity in small caps: ASSUMPTION: filter to stocks with 20-day median turnover above a set rupee threshold (e.g. INR 5 crore) and skip signal days where the stock is at its circuit limit.
  - Entry at next-day open after a signal close avoids look-ahead.
  - Text is US-oriented (dollar example [p. 11]) but indicators are market-agnostic.

## 6. Verdict

- **Codeability:** Partly. Signal conditions for MACD, RSI, Stochastic, ADX, Aroon and Ichimoku are codable, but lookbacks (MACD, RSI, ADX), trend definitions, volume thresholds, the %D formula, and all exits/stops/sizing are absent, so a coder must supply them.
- **Priority for backtesting:** Low. It is a basic indicator primer with no claimed edge, no tested results and no full rules; useful only as a library of baseline signals to benchmark against better-specified books.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the standard lookbacks (MACD 12/26/9, RSI 14, ADX 14, %D smoothing) as the author's; they are not in this text, and the p.8 vs p.11 stochastic rules differ (re-cross above 20 inside an uptrend vs buy while below 20 turning up on volume).
  2. Implementing the p.8 stochastic or the MACD zero-line rule as symmetric long/short systems; NSE cash allows no overnight shorts, so the short side must become exit-only.
  3. Look-ahead in Ichimoku (Senkou spans plotted 26 periods ahead and Chikou plotted 26 back): the cloud at bar t must come from values computed 26 bars earlier, and the Chikou cross compares close[t] with close[t-26].
