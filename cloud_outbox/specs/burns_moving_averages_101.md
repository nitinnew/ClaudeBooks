# Moving Averages 101: A Companion Guide — Steve & Holly Burns

- **Source file:** Google Drive `invest/Moving_Averages_101_Incredible_Signals_That_Will_Make_You_Money.pdf` (file id `1w6BOJmUlmdxBr3UdvMYQOdKd5ULIYvxH`, 4,440,238 bytes; a second copy of 4,441,629 bytes is in `WhatsApp Documents`). © 2015 Stolly Media, LLC [p. 4].
- **Text file used:** text/burns_moving_averages_101.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter. (This ePub-style PDF has no printed page numbers.)
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/burns_moving_averages_101.md text/burns_moving_averages_101.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 78]]. Page 1 is the cover (no text). All charts ($TSLA, $SPY, $FB, $USO, $QQQ, $PCLN, $INDU) are images; only their captions in the running text are available. Testimonials, ads and reading lists [p. 6–8, 76–78] contain no rules.

## 1. The method in brief

A short course on six daily moving averages, each given a role in an "answer key" [p. 12–13]: 5-day EMA (strong momentum / end-of-day trailing stop), 10-day EMA (short-term trend), 21-day EMA (intermediate trend, "last line of support in a volatile uptrend"), 50-day SMA (leading-stock pullback support, "Buy the dip" level), 100-day SMA (deeper pullback, best with RSI 30–35), and 200-day SMA ("Bull above, Bear below"). Moving averages are used to time entries at breaks or bounces; exits are preferably taken with RSI (sell longs near RSI 70, cover shorts near 30) rather than waiting for price to return to the average [p. 36, 43, 74]. Crossover systems (e.g. 10/30 EMA) are presented as the only standalone mechanical version; single averages "don’t typically backtest well as standalone systems" [p. 68]. Designed for US stocks, stock-index ETFs and commodities on daily bars, holding from 5–10 days (5 EMA) to weeks/months (50/100 SMA) [p. 17, 25]. Risk: 1% of capital per trade [p. 26, 63, 74].

Evidence: chart anecdotes only (TSLA +$45 over 29 days [p. 33]; QQQ 10/30 EMA cross avoided 2008 [p. 62]); a claim that long-only crossover systems "can decreases drawdowns by 50% or more" [p. 66]. No backtest tables.

## 2. Strategies

Common definitions used below: `SMA_n`, `EMA_n` on daily closes; `RSI` = 14-period (period not stated, see Ambiguities); "close under X" = end-of-day stop executed at the next open (the book also allows exit at the same close, see 2.1 Ambiguities). Shorts in the book are excluded for NSE (Section 5) but recorded where stated.

### 2.1 200-day SMA breakout with laddered trailing stop

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / breakout | 20–21, 51 |
| Timeframe & holding period | Daily; weeks to months (the 200-day "first break" can start a bull market) | 51, 55 |
| Universe / eligibility filters | Stocks, stock indexes; growth stocks especially | 52 |
| Market / regime filter | The break above the 200-day SMA is itself the regime change | 50–51 |
| Setup conditions | Price below the 200-day SMA (e.g. after a bear market), then breaks above | 51 |
| Entry trigger & order type | "first break, and close above the 200"; alternatives: buy on the break, or wait for confirmation on the next day's open or close | 51, 57 |
| Initial stop-loss | End-of-day: a close back below the 200-day SMA | 20, 73 |
| Exits: profit-taking | Variant B: target RSI 65 | 73 |
| Exits: trailing / time / signal | Variant A (ladder): if price breaks above the 50-day SMA, move stop to a close below the 50-day; then to the 10-day EMA; finally to a close below the 5-day EMA. Variant B: trailing stop = close under the 10-day EMA | 20–21, 73 |
| Position sizing | Position size so the stop loses ≤ 1% of total capital | 26, 74 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Key quotes**

- "Enter using the 200 day SMA, and if the trade trends in your favor, exit and lock in profits after the 5 day EMA is lost and not recovered by the end of the day." [p. 20]
- "Then, if prices breaks above the 50 day SMA, move your stop to a close below the 50 day. Then to the 10 day EMA, and finally to a close below the 5 day EMA." [p. 21]
- "an entry on the first break, and close above the 200, presents the trader with a good risk/reward entry at the beginning of the next possible bull market." [p. 51]
- "Enter on a break and close above the 200 day SMA, stop loss is a close back under the 200 day. If it trends the trailing stop could be a close back under the 10 day EMA with a target of the 65 RSI on the daily chart." [p. 73]

**Pseudocode**

```
entry_t  = C_{t-1} <= SMA200_{t-1} and C_t > SMA200_t                    # break and close above
          (variant: require C_{t-1} < SMA200 for >= 20 sessions, "after a long bear market"; ASSUMPTION)
buy at C_t (variant: O_{t+1})
stop_level = SMA200 ; stage = 0
each day after entry:
  if stage==0 and C > SMA50: stage=1, stop_level=SMA50
  if stage==1 and position in profit and C > EMA10 for 5+ days: stage=2, stop_level=EMA10   # ASSUMPTION: when to step to EMA10
  if stage==2 and C/EMA5 - 1 > 0.05: stage=3, stop_level=EMA5                               # ASSUMPTION: "late in a trend"
  exit at next open if C < stop_level
Variant B: stop SMA200, trail EMA10 once C > EMA10 ... , take profit when RSI14 >= 65
size = floor(0.01*equity / (entry - SMA200_t))  capped at 20% of equity (ASSUMPTION)
```

**Ambiguities & assumptions**

- **When to step the ladder** from the 50-day to the 10-day and 5-day lines: only "late in a trend" [p. 20]. ASSUMPTION: as in pseudocode; test the pure 50-day trail as a simpler variant.
- **Entry confirmation**: on the break, at the close, or next day [p. 51, 57]. ASSUMPTION: close above; next-open fill as variant.
- **Distance of stop**: the 200-day can be far below entry at the first close above it only if price gapped; normally the stop is close. Sizing therefore can give very large positions. ASSUMPTION: cap at 20% of equity.

### 2.2 50-day SMA bounce (buy the dip in an uptrend)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following pullback | 13, 42–43 |
| Timeframe & holding period | Daily; weeks to months | 40, 43 |
| Universe / eligibility filters | Leading growth stocks / "monster stocks" under accumulation; stock indexes in bull markets | 40–41, 52 |
| Market / regime filter | Markets trading above the 50-day SMA ("thinking buy the dip"); first pullback has the best odds — the more a level is tested the likelier it breaks | 42–43 |
| Setup conditions | Strong uptrend pulls back to the 50-day SMA | 13 |
| Entry trigger & order type | "Enter a stock as it bounces off the 50 day SMA" | 73 |
| Initial stop-loss | A close back under the 50-day SMA | 73 |
| Exits: profit-taking | Target RSI 70 | 74 |
| Exits: trailing / time / signal | Trailing stop in a trend: a close under the 10-day EMA | 73–74 |
| Position sizing | ≤ 1% of capital lost if stopped | 74 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Key quotes**

- "50 day SMA: This is the line that strong leading stocks typically pull back to." [p. 13]
- "Markets generally bounce on the first pullback to this line. However, the more a support levels is tested the greater the odds are that it can be broken" [p. 42]
- "Enter a stock as it bounces off the 50 day SMA. Stop loss is a close back under the 50 day SMA." [p. 73]
- "Trailing stop in a trend is a close under the 10 day EMA. Target is the 70 RSI." [p. 73]

**Pseudocode**

```
uptrend_t  = C > SMA50 for at least 20 of last 30 sessions and SMA50_t > SMA50_{t-10}     # ASSUMPTION
touch      = L_t <= SMA50_t * 1.01 and C_t > SMA50_t                                      # ASSUMPTION: within 1%, closes above
bounce     = touch and C_t > O_t                                                           # ASSUMPTION: up close confirms bounce
first_test = no prior touch of SMA50 in last 40 sessions (variant filter)
buy at C_t ; stop = close < SMA50 → exit next open
trail: once C > EMA10, exit next open if C < EMA10 ; target: sell at close when RSI14 >= 70
size: 1% risk on (entry - SMA50*0.99), cap 20% equity
```

**Ambiguities & assumptions**

- **"Bounces off"** has no numeric definition [p. 73]. ASSUMPTION: low within 1% of the 50-day and an up close above it.
- **Trail activation**: the 10-day EMA trail applies "in a trend" [p. 73]. ASSUMPTION: active once a close above the 10-day EMA follows entry.

### 2.3 100-day SMA dip-buy with oversold RSI

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following pullback (deeper dip) | 44–45 |
| Timeframe & holding period | Daily swing trade | 45 |
| Universe / eligibility filters | Stocks and stock indexes in a long-term uptrend; higher highs and higher lows | 44, 46 |
| Market / regime filter | Bull market / long-term uptrend; the 50-day support has been lost | 44–45, 48 |
| Setup conditions | Price at or near the 100-day SMA, ideally coinciding with RSI 30–35 and a bullish MACD crossover ("triple convergence"); a bounce may come before price reaches the 100-day | 44–46, 48 |
| Entry trigger & order type | Buy at the 100-day SMA support (end-of-day decision); re-enter on a close back above the 100-day after a stop-out | 45 |
| Initial stop-loss | A close under the 100-day SMA | 45 |
| Exits: profit-taking | Not specific in the chapter; book-wide exit near RSI 70 | 74 |
| Exits: trailing / time / signal | Trailing stops to maximise winners (not specified) | 46 |
| Position sizing | 1% risk | 74 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Stop using the 100-day on a chart after repeated breaks | 46–48 |

**Key quotes**

- "When the 100 day SMA coincided with the 30 RSI, the odds were greatly increased for a winning trade." [p. 44]
- "I will stop out of a long position with a close under the 100 day SMA and will reenter the trade on a close back above the 100 day SMA." [p. 45]
- "If the 100 day SMA coincides with the oversold levels of 30-35 RSI, it presents a good risk/reward ratio entry in most markets" [p. 48]

**Pseudocode**

```
regime: C > SMA200 and SMA200 rising (20-day slope > 0)                    # ASSUMPTION: "long term uptrend"
setup_t = L_t <= SMA100_t*1.02 and C_t >= SMA100_t and RSI14_t <= 35       # ASSUMPTION: within 2%
          (variant +MACD(12,26,9) line crossing above signal within last 3 days)
buy at C_t; stop: close < SMA100 → exit next open; re-entry: close back > SMA100 (max 2 re-entries per dip, ASSUMPTION)
exit: RSI14 >= 70 at close (book-wide target), or close < EMA10 after RSI > 50 (ASSUMPTION)
```

**Ambiguities & assumptions**

- **Profit exit** is not given in this chapter. ASSUMPTION: the book-wide RSI 70 target [p. 74].
- **RSI 30–35 coinciding with a 100-day touch** may be rare in a stock still above its 200-day. ASSUMPTION: test the plain 100-day touch, then the RSI ≤ 35 and MACD filters as layers.
- **Re-entry limit** not stated ("Price can move around a key moving average many times before trending" [p. 45]). ASSUMPTION: two re-entries.

### 2.4 RSI 34 dip above the 200-day SMA (index swing trade)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | mean-reversion in an uptrend | 74 |
| Timeframe & holding period | Daily swing (days) | 74 |
| Universe / eligibility filters | Stock index (ETF) | 74 |
| Market / regime filter | Index above its 200-day SMA | 74 |
| Setup conditions | RSI at 34 | 74 |
| Entry trigger & order type | Enter at RSI 34 | 74 |
| Initial stop-loss | A close below RSI 30 | 74 |
| Exits: profit-taking | Target RSI 50 | 74 |
| Exits: trailing / time / signal | Trailing stop = close below the previous day's low | 74 |
| Position sizing | 1% risk | 74 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Key quotes**

- "Enter when a stock index is at a 34 RSI but still over the 200 day SMA." [p. 74]
- "Your initial stop loss is a close below the 30 RSI. Your trailing stop is a close below the previous day’s low of day. Your target is the 50 RSI." [p. 74]
- "swing traders should not be buying long positions under the 30 RSI." [p. 56]

**Pseudocode**

```
index proxy (NIFTYBEES / equal-weight panel index)
entry_t = C_t > SMA200_t and RSI14_t <= 34 and RSI14_{t-1} > 34 → buy at C_t
exit at close when: RSI14 >= 50 (target) | RSI14 < 30 (stop) | C_t < L_{t-1} (trail)
# ASSUMPTION: trailing stop active from day 2
```

**Ambiguities & assumptions**

- The stop (close below RSI 30) and the trail (close below prior low) can both fire on day 1; the book doesn't order them. ASSUMPTION: trail active from the second day.
- **Elsewhere** the author says he "will step in and take a long trade if the rare 30 RSI level is reached" [p. 45] but also stops out when RSI closes below 30 [p. 69]. ASSUMPTION: entry band 30 < RSI ≤ 34.

### 2.5 10-day EMA momentum with 50/200-day filter

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / momentum | 27–29, 41 |
| Timeframe & holding period | Daily; days to weeks | 28 |
| Universe / eligibility filters | Markets that trend; avoid stocks whose daily range crosses the 10-EMA repeatedly / high volatility | 27–28, 31 |
| Market / regime filter | Long only above the 200-day SMA; possible rule: also above the 50-day SMA | 28, 41 |
| Setup conditions | Momentum ignition: gap, break over a longer MA, or large candle | 29 |
| Entry trigger & order type | Price breaks above the 10-day EMA while above the 50-day SMA (end of day) | 41 |
| Initial stop-loss | End-of-day close under the 10-day EMA | 27–28 |
| Exits: profit-taking | Lock in profit near RSI 70 | 28–30 |
| Exits: trailing / time / signal | Close under the 10-day EMA | 27–28 |
| Position sizing | 1% risk | 26, 74 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Limit the number of trades per month (5-EMA chapter) | 26 |

**Key quotes**

- "The 10 day EMA can be used as a long signal only if the long term trend is up as measured by the 200 day SMA" [p. 28]
- "A possible trading rule could be to go long on a stock when the price broke over the 10 day EMA, and was also trading over the 50 day SMA." [p. 41]
- "The 30 RSI is a great place to lock in short trades, and the 70 RSI is a great place to lock in long trades." [p. 28]
- "This line is not usable in markets that have big daily ranges that take prices through the 10 EMA repeatedly on the daily chart." [p. 27]

**Pseudocode**

```
filter_t = C_t > SMA50_t and C_t > SMA200_t
noise_t  = count(days in last 20 where L < EMA10 < H) >= 10                 # ASSUMPTION: skip when the line sits inside the bars
entry: filter and not noise and C_{t-1} <= EMA10_{t-1} and C_t > EMA10_t → buy at C_t
exit next open after C < EMA10 ; or sell at close when RSI14 >= 70
```

**Ambiguities & assumptions**

- **Noise filter** ("can’t be used if it is inside the intraday price movements for days in a row" [p. 31]) has no threshold. ASSUMPTION: skip when the EMA10 lies inside the day's range on ≥ 10 of the last 20 days.
- **Combined break** of 10-EMA and 50-SMA increases odds [p. 28]. Variant: require both crossed within 3 days.

### 2.6 50-day breakout held with a 21-day EMA stop

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / breakout | 33 |
| Timeframe & holding period | Daily; weeks (TSLA example 29 days) | 33 |
| Universe / eligibility filters | Volatile "monster" stocks, IPOs | 33–35 |
| Market / regime filter | Intermediate uptrend: closes consistently above the 21-day EMA | 38 |
| Setup conditions | Price below the 50-day | 33 |
| Entry trigger & order type | Buy the break over the 50-day | 33 |
| Initial stop-loss | End of day: a close under the 21-day EMA | 33 |
| Exits: profit-taking | Sell longs as price approaches RSI 70 "regardless of what moving average I am using" | 36 |
| Exits: trailing / time / signal | Close under the 21-day EMA | 33–34 |
| Position sizing | 1% risk | 74 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Key quotes**

- "Buying the break over the 50 day with an end of day stop of a close under the 21 day EMA, would have caught about a $45 move on $TSLA." [p. 33]
- "when price approaches the 70 RSI, I look to sell my long positions regardless of what moving average I am using." [p. 36]

**Pseudocode**

```
entry: C_{t-1} <= SMA50_{t-1} and C_t > SMA50_t and C_t > EMA21_t → buy C_t
exit next open after C < EMA21 ; variant exit at close when RSI14 >= 70
```

**Ambiguities & assumptions**

- "approaches the 70 RSI" [p. 36]. ASSUMPTION: RSI ≥ 68 at close; 70 as variant.
- Whether the 50-day here is SMA (chapter 6) — yes, the book's 50 is an SMA [p. 12–14].

### 2.7 Moving-average crossover systems

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following | 58 |
| Timeframe & holding period | Daily; trend length | 58–59 |
| Universe / eligibility filters | Any; stock index ETFs, growth stocks (smaller size), commodities | 59, 63 |
| Market / regime filter | Long-side signals only when the market is above the 200-day SMA; optional cash when volatility/VIX is high or after a series of losses | 59–60, 67 |
| Setup conditions | Pairs to test: 5/20 SMA, 5 EMA/50 SMA, 10/20 EMA, 10/50 EMA, 15/30 EMA, 15/150 EMA, 10/200 SMA, 50/200 SMA; worked system 10/30 EMA | 60 |
| Entry trigger & order type | Short MA crosses over long MA (end of day); filters: MACD on bullish side, RSI > 50; skip breakouts when RSI > 65 | 58, 60, 71 |
| Initial stop-loss | The reverse cross | 58 |
| Exits: profit-taking | Discretionary variant (10/50 EMA): exit long when RSI goes over 70 | 65 |
| Exits: trailing / time / signal | Exit when the short MA crosses back under the long MA | 58 |
| Position sizing | Each loss ≤ 1% of total capital; smaller size in volatile growth stocks | 63 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Worked pair | 10 EMA / 30 EMA | eight others listed | 60 |
| Long-only filter | market > 200-day SMA | — | 59, 72 |
| RSI filter | > 50 for longs | skip if > 65 | 71 |
| Discretionary exit | RSI > 70 | — | 65 |
| Golden cross | 50 SMA over 200 SMA | — | 64 |

**Key quotes**

- "You go long when the 10 day EMA crosses over the 30 day, and exit the long and go short when the 10 day goes back under the 30 day." [p. 60]
- "Traders can have filters so they only trade the long side of crossover signals when the shorter term moving average crosses over the longer term, if their market is trading over the 200 day SMA" [p. 59]
- "You do not take breakouts over key moving averages when RSI is over 65 due to the skewed risk/return ratio." [p. 71]
- "Keep drawdowns small by trading a position size that keeps each individual loss to 1% of your total trading capital." [p. 63]
- "You would enter long as the 10 day EMA crossed back over the 50 day EMA and exit as the RSI went over 70" [p. 65]

**Pseudocode**

```
for (fast, slow) in [(EMA10,EMA30)] + listed pairs:
  long entry at C_t when fast crosses above slow and [market proxy > SMA200] and [RSI14 > 50] and [RSI14 <= 65] and [MACD > signal]
  exit at C_t when fast crosses below slow   (variant 10/50 EMA: exit when RSI14 > 70)
  no shorts (NSE cash); flat when below
size: 1% of equity / notional stop; ASSUMPTION notional stop = 2×ATR(20); cap 20% of equity
```

**Ambiguities & assumptions**

- **Sizing with a cross-based exit**: no price stop exists, so "1% loss" can't be computed exactly [p. 63]. ASSUMPTION: notional 2×ATR(20) stop for sizing.
- **Which filters** are part of the base system: the 10/30 EMA example is unfiltered [p. 60]; filters are listed as options [p. 71–72]. ASSUMPTION: base = unfiltered long-only; add the 200-day filter, then RSI/MACD.

## 3. Risk & money-management rules

- Position size so a stop-out loses at most 1% of total trading capital; a winning trade may make 3% or more [p. 74].
- With end-of-day stops, size small enough that a sudden volatility expansion doesn't exceed 1%; use an emergency intraday stop if down 1% of capital [p. 26].
- Limit the number of trades per month and take only the highest-upside setups [p. 26].
- Smaller size in volatile growth stocks than in index ETFs [p. 63].
- Optional "stay in cash" signal on high volatility, range expansion, or after a losing streak [p. 60, 67].
- Don't hold longs below the 200-day SMA ("Bad things happen to long positions under the 200 day SMA") [p. 57].

## 4. Non-codable guidance

- Moving averages work best in low-volatility trends and fail in tight ranges and high volatility [p. 13, 17–18].
- Choose the average that the specific stock has respected historically [p. 25, 54].
- Prefer multiple confirmations (MA + RSI + MACD) [p. 46–47, 69].
- Stick with a backtested system through losing streaks; don't abandon it after bad short-term results [p. 61, 63].
- Trade through earnings only if your rules allow it [p. 65].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLC closes for SMA 50/100/200, EMA 5/10/21/30/50; RSI(14); MACD(12,26,9); index proxy for regime and for 2.4.
- **Testability with our data:** All seven strategies are backtestable on 2005–2026 daily prices; no fundamentals needed. Strategy 2.4 needs an index: Nifty only from 2024, so ASSUMPTION: use NIFTYBEES (listed 2002) or an equal-weight panel index. The VIX filter [p. 67] could use India VIX, which is not in our data; ASSUMPTION: replace with 20-day realised volatility of the index proxy above its 1-year 80th percentile.
- **Market-structure differences:**
  - Written for US stocks/ETFs/commodities. The short-side rules (200-day loss shorts [p. 54, 56], always-in crossover [p. 59–60], RSI 51 index short [p. 74]) cannot be held overnight in the NSE cash market. ASSUMPTION: long-only; treat short signals as "go to cash".
  - End-of-day stops on a close below an average fill at the next open; gaps and circuit limits can make losses exceed 1%. ASSUMPTION: model next-open fills; skip entries on upper-circuit closes.
  - Costs: STT, brokerage and ~0.1% slippage. Short-MA systems (5/10 EMA) trade often; report net.
  - RSI 70/30 thresholds were described for US big-cap indexes [p. 30, 36]; the author says levels "could vary in different markets so backtest" [p. 74]. ASSUMPTION: keep 70/30 as base, test 65/35.

## 6. Verdict

- **Codeability:** Fully. Every setup is defined by moving-average and RSI levels on daily closes; only "bounce", "near" and ladder-stepping need numeric defaults.
- **Priority for backtesting:** Medium. Simple, standard rules that are cheap to test as baselines (and partly overlap with other books' 50-day/200-day rules), but the book offers no performance evidence of its own.
- **Top 3 things a coder is most likely to get wrong**
  1. Using intraday touches for stops: nearly every stop in the book is end-of-day ("a close under"), executed next day [p. 16, 45].
  2. Mixing SMA and EMA: 5/10/21 are EMAs, 50/100/200 are SMAs [p. 12–14].
  3. Letting winners ride back to the entry average instead of exiting near RSI 70 (65 for the 200-day variant); the RSI exit is the book's main profit-taking rule [p. 36, 73–74].
