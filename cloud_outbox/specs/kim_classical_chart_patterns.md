# Trading Stocks Using Classical Chart Patterns — Brian B. Kim (self-published, 2014)

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/Trading Stocks Using Classical Chart Patterns by Brian Kim.pdf` (file id `1np_5QF1MmrhHD3aGK6--ccpfXrwNY7TK`, 6,269,562 bytes), 316 PDF pages with a text layer. The charts (Figures 1–97) are images; only the surrounding text was read.
- **Text file used:** text/kim_classical_chart_patterns.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/kim_classical_chart_patterns.md text/kim_classical_chart_patterns.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 316]]: Part I (goal, trading vs gambling, detachment, tools), Part II (Ch. 5–30, every pattern chapter plus earnings, out-of-position, profit-taking, diversification, routine, index and moving-average chapters) and Part III (conclusion, reading list, disclaimer). No chapter was skipped. The figure images could not be read; where a rule depends on a figure, the spec uses only what the text says about it.

## 1. The method in brief

Kim trades Edwards & Magee / Peter Brandt classical patterns on US stocks and index ETFs, using daily charts for decisions and weekly charts for context [p. 34]. The method is discretionary in pattern recognition but has precise trade mechanics:

1. **Patterns traded:**
   - H&S top and bottom, and continuation H&S.
   - Rectangles.
   - Ascending, descending and symmetrical triangles.
   - Pennants.
   - Rising and falling wedges.
   - Flags and channels ("giant flags").
   - H&S top failure.
   - Double bottoms (lows ≥ 2 months apart).
   - Horn bottoms.
   - Diamonds.
   - Patterns within patterns.
2. **Entry:** Wait for a *decisive close* beyond the boundary and enter manually near the close of the breakout day. Buy-stops are used only occasionally [p. 51–52].
3. **Stop:** Brandt's **last day rule**. For a long, place the stop just below the low of the last day that traded below the boundary. If that is too close (gap or little intraday overlap), use the prior day's close or low instead [p. 41–42, 143].
4. **Sizing:** Risk 0.4–0.8% of the account per trade (≤ 1% generally, ≤ 1.5% for the very best). Shares = risk $ ÷ (entry − stop), rounded down [p. 40, 49, 65].
5. **Target:** The measured move (pattern height projected from the breakout). Take most or all profits there; partial profits at halfway are allowed [p. 45, 258–259].
6. **Earnings:** Never enter just before earnings, and exit before the report. If holding through it, keep at most ⅓ of the position, and only when sitting on a profit [p. 95, 106, 120, 248].
7. **Retests:** Re-enter after a stop-out by a retest that didn't close back inside the pattern. Allow at most two attempts [p. 78, 129].
8. **Chasing:** If the breakout bar makes the risk too large, skip it or use a reduced size. Never chase with full size, and never re-attempt a chased trade [p. 251–255].
9. **Regime:** Trade with the index direction. Trade little when the indices are range-bound [p. 294–295, 304].

No backtest statistics are given. Kim stresses that "perfect"-looking patterns still fail most of the time [p. 33] and that losing streaks of 20–30 trades must be survivable [p. 222].

## 2. Strategies

### 2.1 Classical-pattern breakout: close entry, last-day-rule stop, measured-move exit

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | pattern breakout (long and short) | 33, 40–52 |
| Timeframe & holding period | Daily bars for entry and exit; weekly chart for context. Holds last from days to months (until the target, the stop, or the next earnings report) | 34, 106, 258–260 |
| Universe / eligibility filters | Avoid stocks whose daily volume is often < 50,000 shares (< 100,000 = "thinly traded"); beginners only ≥ 200,000 average daily volume; thin stocks at ≤ 30–40% of normal size; extra caution with low-priced, volatile stocks | 57, 63, 111 |
| Market / regime filter | See 2.4: mostly long in rising markets, mostly short in falling markets; trade little in range-bound markets | 40, 294–295 |
| Setup conditions | A well-formed textbook pattern ("clearly defined and easy to spot"). For reversal patterns, a prior trend to reverse. H&S: 3 peaks, head highest, shoulders overlapping in price, neckline from the left-shoulder low to the head low. Double bottom: lows ≥ 2 months apart (E&M: ≥ 1 month, ~20% rise between them). Horn bottom: major low, then two higher lows separated by two higher highs, with overlapping declines. More boundary touches are better; patterns with horizontal boundaries are preferred over slanting ones | 33–34, 83, 96, 158, 201, 204, 206 |
| Entry trigger & order type | A decisive close beyond the boundary; buy (or short) near the close of the breakout day. Buy-stop or sell-stop entries are optional and best with smaller size (gap and false-breakout risk). For symmetrical triangles and other slanting boundaries, some traders also require a close beyond a significant prior high or low inside the pattern | 51–52, 87, 97, 241–242 |
| Initial stop-loss | Last day rule: long = just below the low of the last day that traded below the boundary; short = just above the high of the last day that traded above it. If the breakout day gapped or had little trading inside the pattern: just beyond the prior day's close, or its low or high, or just inside the boundary. Buffer: a few cents (2–5 cents) | 41–42, 77, 89, 143, 186, 230 |
| Position sizing | Risk 0.4–0.8% of the account (professionals ≤ 1%; ≤ 1.5% even for the best set-ups). Shares = floor(risk $ ÷ |entry − stop|), rounded down. If the stop distance is wide (e.g. 5–10% of the position), cut the size so the account risk stays fixed | 40, 43, 49, 65, 141–143 |
| Take-profit / target | Measured move = pattern height at its widest, projected from the breakout point (a "minimum" move, but only a guideline). Exit all or most of the position at the target; partial profits at the halfway mark are allowed | 45, 84, 88, 258–259 |
| Earnings rule | Find the next earnings date as soon as the pattern matures. Do not enter just before earnings; exit the whole position before the release. Exception: when sitting on a substantial profit, keep at most ⅓ (elsewhere 20–30%). After the release, a decisive post-earnings close is a valid entry | 88, 95, 106, 120, 168, 248, 278 |
| Re-entry | If stopped out by a retest that did not close decisively back inside the pattern, re-enter near the close of the day that re-closes outside it, with the stop below the retest low. A third try is rare; almost always stop after two | 78, 120, 129, 132, 187, 285 |
| Chasing / out of position | If the risk to the stop is > ~8–10% of the position after a strong breakout bar, skip it or buy ⅓–½ size. When chasing, don't re-attempt after a stop-out | 133, 141, 153, 253, 255 |
| Second-chance entries | Retest of the boundary; a small continuation pennant or flag after the breakout (see 2.3) | 151, 234 |
| Re-entry after target | Usually no re-entry once the target has been hit and price has come back to the boundary; if trading the retest, use a smaller size | 103, 263 |
| Time management | Give trades time while in profit or only slightly red. If price stalls sideways > 3 weeks with no continuation pattern, cut to ½ to free capital. Channel breakouts: exit if there is no immediate follow-through. Some traders use a time stop | 168–169, 181, 239 |
| Portfolio limits | ≤ 7–8% of the account per position; diversify across trades | 267 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Risk per trade | 0.4–0.8% of the account | ≤ 1%; ≤ 1.5% max for the best patterns | 40, 65 |
| Stop placement | last day rule | prior day's close or low/high; just inside the boundary | 41–42, 143 |
| Stop buffer | 2–5 cents | 1 cent | 230 |
| Position cap | 7–8% of the account | — | 267 |
| Liquidity floor | ADV ≥ 50,000 shares | beginners ≥ 200,000; thin stocks at 30–40% size | 57, 63 |
| Hold through earnings | 0% | ≤ ⅓ of the original (≤ 20–30%) if in profit | 95, 120 |
| Max attempts per pattern | 2 | 3 rarely | 78, 129 |
| Max risk when chasing | position risk ≤ ~8% of position → reduced size so loss < 1% of capital | 10% "too much" | 153, 255 |
| Stall rule | > 3 weeks sideways → halve | exit fully if better set-ups exist | 169 |
| Double-bottom spacing | ≥ 2 months | E&M ≥ 1 month (2–3 typical), ~20% rise | 201 |
| Flags | several days to 2 weeks best | E&M ≤ 2–3 weeks; "giant flags" of months | 172 |

**Key quotes**

- "A H&S top is completed when prices decisively close below the neckline after forming the right shoulder." [p. 33]
- "I always check the weekly chart to get a sense of the overall context in which a pattern is forming." [p. 34]
- "I think most traders and especially beginners should not risk more than 0.4% to 0.8% of their account on a trade." [p. 40]
- "For long trades, we place our stop just below the low of the last day in which prices traded below the breakout boundary." [p. 41]
- "Thus, there are advantages to waiting towards the end of the trading day to see if prices will close decisively above the pattern boundary and then manually entering a trade." [p. 52]
- "And I usually avoid stocks whose daily volume is often under 50,000 shares" [p. 57]
- "I recommend beginners to trade only stocks whose average daily volume is at least 200,000 shares." [p. 63]
- "I would still not risk more than 1.5% of my account even on such a promising pattern" [p. 65]
- "I will always consider re-entering a trade if I am stopped out by a retest where prices do not decisively close below the breakout boundary." [p. 78]
- "We should almost always move on after two attempts." [p. 78]
- "then we should gamble with just a small portion of our original position, say, no more than 20% to 30%." [p. 95]
- "a breakout from a symmetrical triangle is not a true breakout until it closes above a signiﬁcant prior high." [p. 97]
- "We should not hold a position through an earnings release, no matter how promising the chart pattern and how clean the breakout." [p. 106]
- "I would have reentered this trade around the closing price of the retest day and set my stop just below the retest low." [p. 120]
- "Some possible places for our stop orders are: (1) just under the pattern’s upper boundary, (2) just under the closing price of the day before breakout, or (3) just under the low price of the day before breakout." [p. 143]
- "I think 10% is too much to risk no matter how exciting the set-up and breakout." [p. 153]
- "My personal requirement for double bottoms and tops is that the two lows or peaks be at least two months apart." [p. 201]
- "a major low followed by two higher lows intervened by two higher highs." [p. 204]
- "I almost always exit my entire position in a stock that is about to release its quarterly earnings report." [p. 248]
- "And when I chase, my rule is to not attempt another trade if I get stopped out." [p. 255]
- "I almost always take proﬁts on my entire position if a price target is hit." [p. 258]
- "I usually commit at most no more than 7-8% of my account to a single position." [p. 267]

**Pseudocode** (daily bars; long side shown, short is the mirror image)

```
# pattern detection is the hard part: a detector must output for each pattern P
#   upper boundary line U(t), lower boundary L(t), height Hgt (widest), type (reversal/continuation), touches
eligible(s,d): SMA(V,50) >= 200_000 (ASSUMPTION: book's beginner floor; 50_000 for "experienced")
               and C_d >= Rs.50 (ASSUMPTION for "low-priced" caution)
               and regime(d) allows longs (2.4)
               and no earnings date within next 5 sessions (ASSUMPTION for "just before earnings")
signal(d):   C_d > U(d) * (1 + k)            # k = decisive-close threshold, ASSUMPTION k = 1% or 0.5*ATR
             and for slanting U: optional C_d > max(H inside pattern)   # stricter variant [p. 97, 241]
entry:       buy at close d (MOC / last 15 min)
stop:        j = last day <= d with L_j < U(j)                # last day rule
             stop = L_j - buffer                               # buffer = 0.1% (ASSUMPTION for 2-5 cents)
             if gap breakout (L_d > U(d)) or (U(d)-L_d) tiny: stop = min(C_{d-1}, L_{d-1}) - buffer
risk_pct_pos = (entry - stop)/entry
size:        qty = floor(0.006*equity / (entry - stop))       # 0.6% mid of 0.4-0.8%
             qty = min(qty, floor(0.075*equity/entry))         # 7-8% position cap
             if thin (SMA(V,50) < 100_000): qty *= 0.35
             if risk_pct_pos > 0.08: skip  (or qty *= 0.33..0.5 with no re-attempt flag)
target:      T = U_breakout + Hgt ; at T sell 100% (variant: 2/3, trail rest on original stop)
             variant: sell 1/3 at U_breakout + Hgt/2
earnings:    exit all at close of the session before earnings
             (variant: keep 1/3 if unrealised gain >= 10%, ASSUMPTION for "substantial")
retest re-entry: if stopped and C_r > U(r) (re-close outside) within 10 sessions and attempts < 2:
                 buy at close r, stop = min(L over retest) - buffer
stall:       if > 15 sessions since entry with range < 1.5*ATR and no new high: sell 50%
```

**Ambiguities & assumptions**

- "Decisive close" is never quantified. ASSUMPTION: close ≥ 1% (or ≥ 0.5 ATR) beyond the boundary. Test a range of 0.25–2%.
- Pattern recognition (H&S, triangles, wedges, flags, diamonds, horns) is visual and judgement-based. Kim himself draws alternative interpretations of the same chart [p. 81–83, 96]. A coder must choose a detector (for example, swing-point based boundary fitting with ≥ 2 touches per line, and ≥ 3 preferred). Results will depend heavily on it.
- "Just before earnings" and "a substantial profit" are not quantified. ASSUMPTION: no entries within 5 sessions of earnings; hold ⅓ through earnings only if the gain is ≥ 10%.
- Stop buffer: 2–5 cents on US stocks. ASSUMPTION for NSE: 0.1% or 1 tick × 5.

### 2.2 H&S top failure (long when a would-be top fails)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | failed-pattern reversal (long) | 138, 188 |
| Setup conditions | After an advance, a potential H&S top forms (left shoulder, head, right shoulder), and price does not close below the neckline | 188, 194 |
| Entry trigger | A decisive close above the high of the right shoulder; buy near the close (a breakout gap strengthens the signal) | 188, 192, 194 |
| Initial stop-loss | Somewhere below the low of the breakout day (Avago: risk < 1% of the position) | 192 |
| Confirmation | The former right-shoulder high then acts as support | 166, 195 |
| Related | Overlapping H&S (the right shoulder of the top becomes the left shoulder of a continuation H&S bottom); H&S bottom failure (the mirror image) | 191, 196, 200 |
| Exit | As 2.1 (target, earnings rule) | 192 |

**Key quotes**

- "A decisive close above the right shoulder can provide a buying opportunity." [p. 188]
- "I have found H&S top and bottom failures to be particularly useful trading tools." [p. 191]

**Pseudocode**

```
detect potential H&S top (LS, Head, RS) after >= 20% advance (ASSUMPTION), neckline NL not closed below
signal: C_d > max(H over RS) * (1+k)
entry at close d ; stop = L_d - buffer (or last-day rule vs RS high) ; size, earnings, exits as 2.1
cancel setup if close < NL first (then the H&S top itself is the short signal of 2.1)
```

### 2.3 Continuation pennant / flag after a breakout (second-chance entry)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | continuation breakout | 115, 147–155, 172 |
| Setup conditions | After a strong run or a breakout (including an untradeable gap breakout), a small pennant (small symmetrical triangle) or flag (small rectangle or parallelogram, sloping against the trend) forms. The best are several days to 2 weeks long; volume declines during formation | 115, 151, 172, 176 |
| Entry trigger & order type | A close beyond the pennant or flag boundary near the close. Variant: a buy-stop just above the preliminary upper boundary, with a sell-stop just below the preliminary lower boundary | 154–155, 257 |
| Initial stop-loss | Last day rule, or the opposite side of the pennant | 154, 257 |
| Rationale | Kim finds breakouts from small pennants and flags have a high success rate and a quicker follow-through | 257 |
| Channels ("giant flags") | Tradable, but exit if there is no immediate, decisive follow-through | 180–181, 185 |
| Exit | As 2.1 | — |

**Key quotes**

- "It has been my experience that small ﬂags ranging from several days to two weeks are often the best trades." [p. 172]
- "Thus, I move on if there is no immediate and decisive follow through after the breakout from the channel." [p. 181]
- "I have found that breakouts from small pennants and ﬂags have a high success rate." [p. 257]

**Pseudocode**

```
pole: close-to-close gain >= 15% within 15 sessions (ASSUMPTION) or a 2.1 breakout within last 20 sessions
flag/pennant: next 3..10 sessions, range (Hmax-Lmin)/C <= 1.5*ATR(20)/C*3 (ASSUMPTION), SMA(V,5) < SMA(V,20)
entry: buy-stop at Hmax + tick (variant) or close > Hmax*(1+k) -> buy at close
stop: Lmin - buffer (pennant low) ; size per 2.1 ; target = flag breakout + pole height (E&M convention, ASSUMPTION — book only says flags "often start another strong move")
```

### 2.4 Index regime filter (trade with the market; sit out ranges)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | market regime filter | 40, 294–305 |
| Rule | Most stocks move with the market: take mostly long set-ups in a rising market and mostly short set-ups in a falling one. Counter-trend trades are sparing exceptions (E&M: "partial insurance") | 294 |
| Range-bound market | Breakouts fail more often; trade as little as possible, or trade only the index ETFs (QQQ, SPY, IWM, DIA) on their own patterns | 295, 304 |
| Capital deployment | Deploy the bulk of capital when the major indices break out of trading ranges | 304 |
| Index trades | Same pattern rules applied to the ETFs (e.g., QQQ continuation diamond, SPY continuation H&S bottom) | 295–303 |
| Moving averages | Only the 50- and 200-day SMAs, as secondary support/resistance references; they do not change the entry decision | 306–309 |

**Key quotes**

- "That means we should trade mostly long set-ups in a rising market and mostly short set-ups in a declining market." [p. 294]
- "Therefore, I try to trade as little as possible in a range-bound market." [p. 295]
- "But I think it is better to deploy the bulk of our trading capital when the major indices are breaking out of trading ranges and possibly starting a run." [p. 304]
- "I use only two indicators: the 50-day and 200-day simple moving averages." [p. 306]

**Pseudocode**

```
idx = NIFTY 50 (and NIFTY 500)   # ASSUMPTION for SPY/QQQ/IWM/DIA
trend_up   = idx close > SMA(idx,200) and SMA(idx,50) rising   # ASSUMPTION: book gives no numeric trend test
range_mkt  = (max(H,60)-min(L,60))/C < 8% (ASSUMPTION) and not breakout of that range
longs allowed if trend_up ; shorts if trend_down ; if range_mkt: max 2 open positions or index-ETF patterns only
deploy_full when idx closes above its 60-day range high
```

## 3. Risk & money-management rules

- Risk management is the priority. Assume every trade will fail [p. 237].
- Risk 0.4–0.8% per trade; ≤ 1.5% even for the best patterns. Shares = risk ÷ stop distance, rounded down [p. 40, 49, 65].
- Position ≤ 7–8% of the account; always diversify, because overnight gaps of 13–50% happen (Texas Industries lost 3× the planned risk) [p. 53, 238–239, 267].
- Thin stocks: avoid ADV < 50,000 shares; use 30–40% size when they must be traded [p. 57, 63].
- Exit before earnings [p. 106, 248].
- Chase only at reduced size, keeping the loss < 1% of capital; never re-attempt a chased trade [p. 255].
- No more than two attempts on one pattern [p. 78].
- Losing streaks of 20–30+ must not drain the account. In a slump, return to basics rather than seeking a "perfect system" [p. 221–222].
- After a run of losses ("cycle of pain and greed"), exit and take days or weeks off [p. 260].

## 4. Non-codable guidance

- Believe the price action, not your bias. Kim's own missed trades (Chicago Bridge & Iron, the QQQ diamond, TRW) came from refusing to accept breakouts against his opinion [p. 108, 217–218, 299–300].
- Enter, set the stop, and stop watching; micromanaging after entry leads to selling at retests [p. 124, 280–281].
- Routine:
  - Keep a 700–800-stock watch list, cycled every 1–2 weeks.
  - Sort charts into urgency folders: daily checks for imminent breakouts, every 3–4 days for medium, and every 7–10 days otherwise.
  - Keep drawing and redrawing preliminary boundaries.
  [p. 268–269, 274, 277]
- Pattern within a pattern: a small pattern breaking out inside a larger one gives an earlier, lower-risk entry [p. 92, 223–229].
- The apex of a symmetrical triangle can act as later support (E&M) [p. 272].
- Bigger and longer patterns are preferred, because they tend to have more staying power [p. 211].
- Don't rationalise with tuned moving averages (the "35-day MA" example) [p. 307].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV, weekly bars, corporate-results calendar (BSE/NSE board-meeting dates), index series (NIFTY 50, NIFTY 500, and sector indices for context).
- **Testability with our data:** The trade mechanics (2.1 close entry, last-day stop, risk sizing, measured target, earnings exit, two-attempt re-entry) are fully testable once a pattern detector exists. The detector is the main build effort. Start with horizontal-boundary patterns (rectangles, ascending and descending triangles, H&S with near-flat necklines), which Kim himself prefers [p. 83, 160].
- **Market-structure differences:**
  - Liquidity floor in value rather than shares (ASSUMPTION): 50-day median traded value ≥ Rs. 5 crore (beginner tier ≥ Rs. 20 crore).
  - Results dates are known from board-meeting intimations, usually ≥ 2 working days ahead; use them for the earnings exit.
  - Circuit limits (5/10/20%) can produce gap breakouts that are untradeable at the close. Treat an upper-circuit close as "out of position" (skip).
  - Shorting cash equities overnight is not possible. Short-side rules apply only to F&O stocks via futures (lot sizes distort risk sizing), or are dropped.
  - Stop buffer: 1–5 ticks (Rs. 0.05 tick) or 0.1%.

## 6. Verdict

- **Codeability:** Partial. Entry timing, stop, sizing, target, earnings, re-entry, chase and regime rules are explicit and codeable. The pattern identification itself is discretionary and visual, with no geometric tolerances given (touches, slope, symmetry, "decisive").
- **Priority for backtesting:** Medium-High. It is the most complete trade-management wrapper for classical patterns so far: last-day stop, fixed-fractional risk, measured exit, earnings blackout and a two-attempt rule. It can be bolted onto any pattern detector (for example, rectangles and ascending triangles from Bulkowski-style detectors), and the earnings-exit and chase rules are cheap, testable overlays.
- **Top 3 things a coder is most likely to get wrong**
  1. Placing the stop at a fixed % or below the pattern low instead of the **last day rule** (below the low of the last bar that still traded inside the pattern). Also missing the gap fallback to the prior day's close or low [p. 41–42, 143].
  2. Holding through earnings, or entering just before them. Kim exits the whole position before every report, keeping at most ⅓ and only when well in profit [p. 106, 120, 248].
  3. Sizing by a fixed position % rather than by account risk ÷ stop distance (capped at 7–8% of equity). Also chasing wide breakout bars at full size instead of skipping or cutting size and forbidding a re-attempt [p. 40, 49, 255, 267].
