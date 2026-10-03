# How to Make Money with Breakout Trading (1st edition) — Indrazith Shantharaj

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/How_to_Make_Money_with_Breakout_Trading_by_Indrazith_Shantharaj.pdf` (file id `10e9Vnec57KWeQZqiBJasixF-6GUamInE`, 1,956,908 bytes; a z-lib copy is in the same folder). First published 2020 [p. 2]; preface dated July 2020 [p. 8].
- **Text file used:** text/shantharaj_breakout_trading.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/shantharaj_breakout_trading.md text/shantharaj_breakout_trading.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 68]]. Page 1 (cover) and 68 are blank of text. All chart images (Images 1.1–5.2) are images; only captions and prose are available. Note: the inventory asked to extract the 2.0 edition first and compare; the 2.0 edition (`shantharaj_breakout_trading_2`, 29 MB) is `blocked_size`, so no comparison is possible in the cloud.

## 1. The method in brief

A single long-only swing system for Indian retail traders, holding 2 days to 2 weeks [p. 7]. Draw a resistance trend line on a 6–12-month daily chart through at least two peaks, with a slope under 45° and every peak respecting the line [p. 17–25]. Buy only when a breakout candle shows four qualities: (1) big relative to the stock's average candle, (2) breaks out in one day ("quick time"), (3) little selling wick (close in the top 20% of the day's range), (4) a volume spike, ideally after some days of consolidation [p. 29–36]. Entry is a stop-market order just above the breakout candle's high the next day (skip if the stock opens > 2% above the prior high); the stop goes just below the breakout candle's low; the target depends on context (start of the down trend line, width of the sideways range, or 1:2 / trailing at all-time highs), and the trade is taken only if reward:risk ≥ 2 [p. 38–40]. The distinctive rule is an aggressive early trail: if the day after the breakout is a small or selling candle, move the stop to that day's low [p. 40–47]. Size: 10% of capital per trade, ≤ 5 trades (≤ 50% deployed) for beginners [p. 51–52].

Evidence: chart examples only, and the author's claim that the trail cuts losses "by 75-90%" on failed breakouts [p. 47]. He says the system can't be scanned algorithmically because trend lines are drawn by hand [p. 60].

## 2. Strategies

### 2.1 Resistance trend-line breakout with four-quality candle filter

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout | 26 |
| Timeframe & holding period | Daily chart, 6 months–1 year of data; hold 2 days to 2 weeks | 7, 17 |
| Universe / eligibility filters | NSE equities (cash); avoid operator-driven stocks and stocks without smooth price action (many wicks, many gaps, no-trade days) | 15–17, 22 |
| Market / regime filter | None as a filter; works best in uptrends and sideways markets, few trades and many breakevens in downtrends | 54 |
| Setup conditions | Resistance trend line through ≥ 2 peaks (more peaks = stronger), slope < 45°, all peaks respect the line; preferably some days of consolidation before the breakout. Breakout candle: big vs. the stock's average candle; closes beyond the line in one day; selling wick < 20% of the day's range (close in the top 20%); volume spike | 17–21, 29–35 |
| Entry trigger & order type | Next day: SL-M buy order a few ticks above the breakout candle's high; never buy below that high; skip if the stock opens > 2% above the prior day's high (even if it later comes back); if it opens < 2% above, buy at market | 38, 47–48, 57 |
| Initial stop-loss | A few ticks below the breakout candle's low | 38–39 |
| Exits: profit-taking | Down-trend breakout: target the start of the trend line / topmost swing. Sideways: target = range width. All-time high: 1:2 R:R or trail below each swing low. Take the trade only if R:R ≥ 1:2. After experience: exit 75% at target, trail 25% | 38–40, 48 |
| Exits: trailing / time / signal | If the day after the breakout is a small candle, doji or selling candle, trail the stop to that day's low; if another big up candle, trail to its low; after 2–3 days, trail below a bearish engulfing / big selling pin bar low; otherwise below the next swing low; the 25% remainder trails below the target-day low or swing lows | 40–47, 58 |
| Position sizing | 10% of capital per trade regardless of stop distance (risk ends up 0.5–2%) | 51 |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Beginners: ≤ 50% of capital deployed, i.e. ≤ 5 trades (plus 25% remainders); shortlist only 2–3 new candidates per day | 47, 51–52, 57 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Chart lookback | 6–12 months daily | — | 17 |
| Trend-line touches | ≥ 2 peaks | 3–8 = stronger | 17–19 |
| Trend-line slope | < 45° | — | 19 |
| Selling wick | < 20% of day's range | — | 33 |
| Gap filter | skip if open > 2% above prior high | — | 38 |
| Minimum R:R | 1:2 | — | 38–39 |
| Partial exit | 75% at target, 25% trailed | 100% at target for beginners | 47–48 |
| Capital per trade | 10% | — | 51 |
| Max deployed | 50% (5 trades) | — | 51–52 |
| Holding | 2 days – 2 weeks | — | 7 |

**Key quotes**

- "You should connect a minimum of 2 peaks to consider it as a valid trend line." [p. 17]
- "Ideally, the trend line that shows less to the medium slope (less than 45 degrees) is the safer bet" [p. 19]
- "The four things mentioned below are essential to separate a real breakout from fake ones:" [p. 29]
- "In this system, we always refer to the daily chart. Hence, the breakout should happen in one single day." [p. 31]
- "If you need a specific reference, then you can consider that the selling wick should be less than 20% of the entire body of the candle." [p. 33]
- "As shown in Image 4.1, Entry should come just a few ticks above the high of the breakout candle." [p. 38]
- "Stop-loss will be a few ticks below the low of the breakout candle." [p. 38]
- "Only opt to take the trade if it shows a minimum of 1:2 Risk- Reward." [p. 38]
- "Also, avoid the trade if it opens above 2% from the previous day high as it increases the stop-loss points and also it might attract profit booking." [p. 38]
- "It is better to trail below the low of the current day candle, as shown in Image 4.5." [p. 41]
- "instead of exiting 100% position at target, exit only 75% of the position at target." [p. 48]
- "For one trade, use only 10% of your capital irrespective of the risk." [p. 51]

**Pseudocode** (daily bars)

```
# --- resistance trend line (author draws by hand; coder's approximation) ---
pivots: swing highs with k = 5 over last 126–252 sessions
line through the two most recent swing highs H_a (earlier) and H_b (later) with H_b <= H_a (falling or flat line), or a flat line through ≥2 highs within 1.5%
require: all swing highs between a and t lie at or below the line (+0.5% tolerance); slope_pct_per_bar such that angle < 45° on a
         normalised chart → ASSUMPTION: |slope| <= 0.5% of price per bar; ≥ 2 touches (prefer ≥ 3)
smooth price action: median(upper+lower wick share) over 60 days < 0.6 and gap days (|O/C_prev-1|>2%) <= 5 of 60 (ASSUMPTION)
# --- breakout candle on day t ---
crosses: C_t > line_t and C_{t-1} <= line_{t-1}
big:     (H_t - L_t) >= 1.5 * mean(H-L, 20)  and  C_t > O_t                                   # ASSUMPTION "big"
wick:    (H_t - C_t) <= 0.20 * (H_t - L_t)
volume:  V_t >= 1.5 * SMA(V,20)_{t-1}                                                         # ASSUMPTION "good volume"
consolidation bonus: (max(H)-min(L))/min(L) over t-10..t-1 <= 0.08 (variant filter)
# --- order on t+1 ---
skip if O_{t+1} > H_t*1.02
trigger: H_{t+1} >= H_t + tick → fill = max(O_{t+1}, H_t + tick)
stop0 = L_t - tick
target: downtrend line → price at line start (H_a); sideways → H_t + (range top - range bottom); ATH → fill + 2*(fill - stop0)
take only if (target - fill) >= 2*(fill - stop0)
# --- management ---
day t+1 (entry day) close: if small candle (|C-O| < 0.5*mean body 20) or C < O: stop = L_{t+1}; if big up candle: stop = L_{t+1}
days t+2..t+4: if bearish engulfing or upper-wick >= 2/3 range: stop = L of that day
afterwards: stop = latest 5-bar swing low
at target: sell 75% (beginner variant 100%); remainder stop = L of target day, then swing lows
time stop: exit at close of session 10 if neither target nor stop (ASSUMPTION from "2 weeks")
size: shares = floor(0.10*equity / fill); max 5 concurrent positions (+25% remainders)
```

**Ambiguities & assumptions**

- **Trend lines are hand-drawn** and "subjective and art" [p. 21, 25]; the author says no scan exists [p. 60]. ASSUMPTION: pivot-based line with tolerance; results depend heavily on this.
- **Wick rule wording**: "less than 20% of the entire body of the candle" but the worked example uses the day's range (low 100, high 110, close above 108) [p. 33]. ASSUMPTION: 20% of the high–low range (the example).
- **"Big" candle and "good volume"** are relative to the stock's average with no number [p. 30, 34–35]. ASSUMPTION: range ≥ 1.5× 20-day average range; volume ≥ 1.5× 20-day average.
- **Trail on the entry day** — the book trails to the low of the day after the breakout when that day is small, a doji or a selling candle [p. 41–46], and also after a big up candle [p. 58]. Since entry happens on that same day, the stop effectively moves to the entry day's low at its close. ASSUMPTION: always move the stop to the entry day's low at the close of the entry day.
- **No time stop** is given beyond the 2-week holding horizon [p. 7]. ASSUMPTION: exit at the close of session 10.
- **Support breaks / shorts** are excluded by the author for Indian retail traders [p. 22, 56].

## 3. Risk & money-management rules

- Before every trade know entry, stop, target, rupee risk and portfolio risk [p. 37].
- 10% of capital per trade (risk 0.5–2% depending on stop depth) [p. 51].
- Beginners: ≤ 50% of capital deployed (≤ 5 trades) until they have traded through all four market stages (about 2 years) [p. 51–54].
- Avoid trading after significant drawdowns or several successive failed trades [p. 63].
- Start small even with large capital [p. 57].

## 4. Non-codable guidance

- Follow "smart money": consolidation with repeated defended lows before a breakout [p. 13–14].
- "Be RIGID about our RULES and FLEXIBLE about our EXPECTATIONS" [p. 54].
- Keep a journal; review failed trades [p. 48].
- Practise drawing trend lines on 100 charts [p. 61].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV only.
- **Testability with our data:** Backtestable on 2005–2026 daily prices once trend lines are detected algorithmically; no index or fundamentals needed.
- **Market-structure differences:**
  - Written for NSE cash equities, long-only (the author notes shorts can't be carried overnight in equity) [p. 56]; fits our constraints directly.
  - Circuit limits: a breakout candle closing at the upper circuit has no selling wick by construction; the next day may open > 2% above (skipped by the book's own gap rule).
  - Costs: STT, brokerage, ~0.1% slippage; stops at the breakout candle's low are often tight (1–4%), so costs are material; report net.
  - ASSUMPTION: liquidity floor 20-day average traded value ≥ Rs. 1 crore; avoid stocks with frequent no-trade days ("operator stocks") [p. 16–17].

## 6. Verdict

- **Codeability:** Partly. Candle filters, entry, stop, gap rule, R:R check, trail and sizing are explicit; trend-line drawing is discretionary by the author's own statement.
- **Priority for backtesting:** Medium. A clear NSE-specific breakout system with a distinctive next-day trailing rule worth testing, but the core trend-line step needs an approximation and the evidence is anecdotal; the 2.0 edition (blocked) may refine it.
- **Top 3 things a coder is most likely to get wrong**
  1. Entering at the breakout candle's close: entry is a stop order above its high the **next** day, cancelled if the open is > 2% above the prior high [p. 38].
  2. Keeping the initial stop through a weak follow-up day: the system moves the stop to the entry-day low immediately when the day after the breakout is small or bearish [p. 41].
  3. Ignoring the R:R gate: trades whose context target (trend-line start or range width) is less than 2× the stop distance are skipped [p. 38–39].
