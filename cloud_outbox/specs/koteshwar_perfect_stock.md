# The Perfect Stock — Brad Koteshwar (AuthorHouse, 2004)

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/The Perfect Stock by Brad Koteshwar.pdf` (file id `1HVQXOufI5-i5SjvfXxA27unI3vXJnEvA`, 1,114,902 bytes), 178 PDF pages with a text layer. A second copy, "The Perfect Stock_ How A 7000% Move...pdf" (1,062,072 bytes), was not opened; it is presumed to be the same book.
- **Text file used:** text/koteshwar_perfect_stock.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index; the book has no printed page numbers)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/koteshwar_perfect_stock.md text/koteshwar_perfect_stock.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 178]]. Charts 1–8 are images; only their numbered captions are available.

## 1. The method in brief

The book is a novel ("a work of fiction") about Taser (TASR) stock's 7,065% run from April 2003 to April 2004. The author says the dates match TASR's real prices, without split adjustment [p. 3, 8]. The trading method sits in the trade journals of two fictional "professionals":

- **Boyd Hunt** (new-high pyramiding):
  - Test-buy about 20% of capital with a buy-stop just above a new all-time high that follows a huge-volume high, with a standard 10% stop.
  - Add larger pieces, each time the stock clears its prior high after a reaction (finally on 50% margin), re-setting the 10% stop below each add.
  - In the final run, trail the stop $1–2 below the prior week's low.
  - Sell out near the close of the "exhaust" day: the heaviest volume ever with little price change [p. 79–89, 110–113].
- **Roger Stonybrooke** (late-stage pool):
  - After a long run, wait for the first reaction that reaches the 50-day moving average.
  - Buy equal tranches at each further +$10 rise, with a 10% stop under the average cost; add the rest on a breakout to new highs.
  - Hold at most 10 weeks; exit, and also go short, on the exhaust day.
  - Cover half the short at the 50-day MA and the rest within two weeks [p. 92–103, 170–174].
- **The narrator's own short:** short at the exhaust day's close with a 10% stop, and cover when weekly volume has fallen three weeks in a row and the weekly decline is slowing [p. 105–110, 144–147].

Evidence is a single example (TASR), dramatised; the book contains no statistics.

## 2. Strategies

### 2.1 New-high test buy and pyramid (Boyd Hunt)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout / trend-following, pyramiding | 79–89 |
| Timeframe & holding period | Daily entry triggers; weekly charts for management; held ~6.5 months (Oct 2003 – Apr 2004). The narrator's usual winners last 8–26 weeks | 81, 110, 170 |
| Universe / eligibility filters | A stock "in a clearly visible trend". Small float and accumulation evidence: an all-time high on ~5× average volume, the highest volume in 52 weeks | 13, 80 |
| Market / regime filter | Buy only during market uptrends; stay in cash during downtrends or uncertain trends; 5–10 trades a year | 29 |
| Setup conditions | Stock makes an all-time high on huge volume, then moves sideways ~2 weeks without giving back gains | 80 |
| Entry trigger & order type | Buy-stop just above the latest all-time high (e.g. $32.68 vs. the Sep-17 high); size ≈ 20% of capital as a "test case" | 69, 79–80 |
| Initial stop-loss | Sell-stop 10% below the buy price, GTC, placed immediately | 70, 80–81 |
| Adding to / pyramiding | After the first quick advance (ideally ≥ 20% within 4 weeks), wait for a reaction; when the stock again clears its prior high, buy-stop a larger add (~4× the test size). The next add after another reaction and new high uses 50% margin. After each add, reset the stop 10% below the latest buy price | 71, 81–84 |
| Exits: trailing / signal | In the final up-leg (4 strong up-weeks), trail the stop $1–2 below the prior week's low. After a severe reaction, a stop $2 below that reaction-week's low | 85, 113 |
| Exits: profit-taking | Sell everything at market near the close of the exhaust day: highest one-day volume with little net price change (TASR: open $351, high $385, close ≈ open, 9–10M shares) | 86, 108–110 |
| Position sizing | Test buy ≤ 20% of capital, recomputed on remaining capital after losses | 69–71 |
| Portfolio limits | 5–10 trades a year; long periods in cash | 29, 170 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Test size | 20% of capital | — | 69 |
| Stop | 10% below the latest buy | "Some folks use 8%" | 70 |
| Accumulation volume cue | ≈ 5× average daily volume at the new high; highest in 52 weeks | — | 80 |
| Follow-through test | ≥ 20% gain within 4 weeks of the test buy | "usually (but not always)" | 71 |
| Add size | ~4× the test, then margin-funded 50% of equity | — | 82–84 |
| Final trail | $1 below the prior week's low | $2 below the reaction-week low | 85, 113 |

**Key quotes**

- "Reason: New all time highs after clearing the Sep 17th new high that was made on huge volume." [p. 80]
- "Reason: SOP 10% stop-loss" [p. 80]
- "the first buy would be no more than 20% or $20,000 worth of stock." [p. 69]
- "Usually (but not always), a winner starts off with a quick 20% or more move within the first four weeks of the test buy." [p. 71]
- "Daily charts would probably show many false short-term violent moves that will help eliminate weaker holders of the stock." [p. 81]
- "The point at which he started moving his sell-stops to a $1 below the prior week’s low price." [p. 113]
- "Look for a close with very little percentage change in prices on a daily basis accompanied by the heaviest one day volume of shares traded." [p. 86]

**Pseudocode** (daily bars, weekly management)

```
setup: H_t = all-time high and V_t >= 5*SMA(V,50) and V_t = max(V, 252)   # accumulation high
then: within ~10 sessions no close below the prior breakout level (sideways)  # ASSUMPTION
entry1: buy-stop at ATH + tick, qty = 0.20*equity/price ; stop = 0.90*fill
if close >= 1.20*fill1 within 20 sessions: mark "winner"
add_k: after a pullback (low < prior swing high*0.85, ASSUMPTION), buy-stop at prior high + tick, qty ~ 4x initial (then margin 50%)
       stop_all = 0.90 * fill_k
final run: once 2+ consecutive strong up-weeks after the last add, stop = prior week low - 1 (weekly)
exhaust exit: on day d with V_d = max(V, all history) and |C_d - O_d|/O_d <= 1% -> sell at close
```

**Ambiguities & assumptions**

- "Huge volume", "sideways" and "reaction" are not quantified beyond the single example. ASSUMPTION: thresholds as in the pseudocode.
- Re-setting the stop 10% below the latest add can sit above the average cost; that is the book's intent ("He still would be ahead") [p. 82].

### 2.2 Exhaust-day short and decelerating-volume cover (narrator / Stonybrooke)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | blow-off top reversal (short) | 105–110, 144–147 |
| Setup conditions | After a parabolic run (weekly gains of +$42–48 three weeks running), a day with the highest one-day volume ever and hardly any net gain. Sister stocks in the sector already collapsing | 86, 97, 106 |
| Entry trigger & order type | Short at market near the close of the exhaust day (narrator checked 30 minutes before the close) | 108–109 |
| Initial stop-loss | Buy-stop ~10% above the entry (narrator: entry $351, stop $385 = the day's high) | 109–110 |
| Exits | Cover when weekly volume has fallen 3 consecutive weeks and the weekly loss has decelerated to ~flat; or cover half at the first 50-day MA support and the rest ~2 weeks later; close the whole operation within ~4 weeks | 99–100, 145, 171 |
| Holding period | ~4 weeks | 145, 171 |

**Key quotes**

- "Look for the highest one day trade volume with hardly any gains. That is the first sign to go short." [p. 106]
- "I saw that the volume had fallen for 3 consecutive weeks from 41 million to 14.5 million to 8.4 million shares." [p. 145]
- "He had covered at an average price of $207/share on half his positions." [p. 171]

**Pseudocode**

```
exhaust day d: V_d = max(V, history) and |C_d - O_d|/O_d <= 0.01 and stock up >= 100% in 13 weeks (ASSUMPTION)
short at C_d ; stop = max(H_d, 1.10*C_d)
cover rule A: weekly vol falling 3 weeks in a row and |weekly change| <= 1% -> cover at the next open
cover rule B: cover 50% when Low <= SMA(C,50); remainder after 2 more weeks; max hold 4-5 weeks
```

### 2.3 Late-stage 50-day-MA pullback pool (Stonybrooke)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | momentum continuation (late stage) | 92–103 |
| Universe / eligibility filters | Liquidity big enough for the pool: daily traded value ≫ position (TASR ≈ $200M/day vs. a $12M pool); a near-monopoly product story | 92, 94 |
| Setup conditions | After a long uptrend in which no prior reaction reached the 50-day MA, the first reaction finds support at the 50-day MA. Before it, a turnover day ≥ 2× the float on the high (accumulation nearing distribution) | 93–94 |
| Entry trigger | First tranche when price rises from the 50-day-MA support (≈ $145 → buy $150), then an equal $-amount tranche at each +$10 advance (≈ +6–7%) up to the prior high, then the remaining half of the pool on a breakout to new highs | 94–95 |
| Initial stop-loss | Sell-stop 10% below the running average cost (updated after each tranche); mental floor to start liquidating at $170 vs. a $187.67 average | 94–95 |
| Exits | Sell everything on the exhaust day (see 2.2); maximum 10 weeks in any operation | 94, 100, 170 |
| Position sizing | Pool split 50% into six equal tranches + 50% on the new-high breakout | 94–95 |

**Key quotes**

- "The reaction low found support at the stock‘s 50 day moving average." [p. 93]
- "None of the prior reactions had reached the 50-day line." [p. 94]
- "Roger never committed funds into a position beyond 10 weeks in duration." [p. 94]
- "His accumulation followed a simple path of adding positions at every $10 price advance." [p. 94]

**Pseudocode**

```
cond: stock up >= 300% in 52 weeks; first time since trend start that Low <= SMA(C,50) (within 2%), then a close above it
t1: buy 1/12 of budget at close > SMA50 ; then buy 1/12 at each +6.5% above t1 price until the prior high (6 tranches)
t7: buy remaining 1/2 on a close above the prior all-time high
stop: 0.90 * average cost (recomputed) ; time stop: 10 weeks from t1 ; exhaust-day exit as 2.2
```

## 3. Risk & money-management rules

- Pre-set a 10% stop-loss GTC on every entry; never watch the tape intraday [p. 13, 25–26, 70].
- Test positions of ≤ 20% of capital, recomputed after losses. Five straight 10% losses cost only about 8% of capital [p. 69–71].
- Add only to winners, never average down; use margin only late in a proven move [p. 26, 83].
- 5–10 trades a year, cash during downtrends: "Cash is king" [p. 13, 29].
- Accept a ~30% win rate. A few big winners carry the year ("80% of the profit is made in 20% of the trades") [p. 69, 150].
- Avoid shorting a stock still making higher highs; the book's "Shorty" lost 82% that way [p. 120–125].

## 4. Non-codable guidance

- Insider cycle: IPO, then the underwriter supports reactions, then an uptrend ("reaction always less than the move up"), then distribution into news at the top [p. 28–29, 41–42].
- Stocks at new highs have no overhead supply; the market is forward-looking, so news confirms the move after the fact [p. 25, 45].
- Charts show whether heavy buying or selling is happening; they don't predict. Indicator studies (MACD, stochastics) are of little use to big winners [p. 47, 150].
- Seasonality: heavy retail buying in January and around the April tax deadline; TASR topped two trading days after the deadline [p. 151–152].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV (all-time high, 50-day MA, volume records), weekly aggregation, NIFTY trend for the regime filter.
- **Testability with our data:** fully backtestable on 2005–2026 daily data for 2.1 and 2.3. 2.2 (short) requires F&O stocks only.
- **Market-structure differences:**
  - Cash equity can't be shorted overnight. Test the 2.2 signal as an exit rule (and as a long-avoidance filter), or with stock futures for F&O names.
  - 50% margin pyramiding: test unlevered; treat margin as a variant.
  - Upper-circuit stocks may never print a calm, high-volume "exhaust" day; add a fallback exit (weekly close below the prior week's low).
  - Liquidity floor (ASSUMPTION): 20-day median traded value ≥ Rs. 5 crore so that pyramid adds are fillable.

## 6. Verdict

- **Codeability:** Partly. Entry, stops, trailing and exhaust rules are explicit enough; "huge volume", "reaction" and "sideways" need thresholds.
- **Priority for backtesting:** Medium. A Darvas/Livermore-style new-high pyramid with a concrete exhaust-day exit and a 50-day-MA late-stage add, but derived from one fictionalised example. Test 2.1 with the 2.2 exhaust exit as the main candidate.
- **Top 3 things a coder is most likely to get wrong**
  1. Using one stop for the whole pyramid at the original entry: the stop is reset 10% below each new add [p. 82, 84].
  2. Taking the exhaust signal from price alone. It requires the highest volume in the stock's history AND a near-zero net change on the day [p. 86, 106].
  3. Managing the trend on daily bars. Reactions are judged on weekly charts, and the final trailing stop uses the prior week's low [p. 81, 113].
