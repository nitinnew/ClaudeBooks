# The Complete TurtleTrader — Michael W. Covel

- **Source file:** Google Drive `invest/Tech/The Complete Turtle Trader ( PDFDrive ).pdf` (file id `1aswN_lc1NO1J3Bmojeva1jR5yQfKMXg0`, 4,042,677 bytes; HarperCollins paperback/ePub edition, ePub © Sept 2010, ISBN 978-0-061-74061-9 [p. 323])
- **Text file used:** text/covel_complete_turtletrader.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter. (This ePub's own index states its page numbers do not match [p. 233].)
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/covel_complete_turtletrader.md text/covel_complete_turtletrader.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 323]]. 290 of 323 PDF pages have a text layer. All tables and charts are images with no text: Table 2.1, 5.1, 5.2, 5.6, 5.8, 5.10–5.18, Charts 5.3–5.9, Table 7.1, 7.2, 8.1, 11.1, 13.1 and Appendix III/IV performance tables [p. 39–40, 81–112, 138, 145, 173, 194, 288–314]. Their numbers (e.g. the live-cattle pyramiding P&L tables, the initial Turtle market list, monthly returns) are therefore NOT available to this spec. Endnotes/index [p. 212–248] read but contain no rules.

## 1. The method in brief

This is a narrative history of Richard Dennis's 1983–84 "Turtle" experiment, not a manual, but chapter 5 ("The Rules", [p. 79–113]) lays out the trading rules as Covel reconstructed them. The method is pure price trend following: buy breakouts to new N-day highs and sell short breakouts to new N-day lows in a diversified portfolio of liquid markets, size every position by recent volatility ("N", the 20-day average true range) so each unit risks about 2% of current equity, pyramid up to 4–5 units into winners, exit on a 2N hard stop or a shorter opposite breakout, and cut size after drawdowns [p. 83–112]. The claimed edge is that winners are "many multiples larger" than losers even with a low win rate [p. 80]; Covel quotes Parker that the style has about "40% winners" and makes money on roughly 10% of trades [p. 183]. Designed for futures (bonds, currencies, grains, metals, energy, stock indexes), daily bars, holding weeks to months [p. 65, 111].

Evidence in the book is anecdotal or in image tables: Dennis said the Turtles grossed about $150 million for him over four years [p. 148]; the Turtles were "down 50 percent each on average six months into the program" in year one [p. 123]; a Turtle research group found that combining S1 and S2 produced worst-case drawdowns of about -80% rather than -50%, leading Dennis to cut all position sizes by 50% in an April 23, 1986 memo [p. 142–143]. Year-by-year Turtle and successor-fund returns are in image tables only [p. 138, 173, 288–314].

## 2. Strategies

### 2.1 System One (S1) — 20-day breakout with "last trade" filter

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / breakout | 65, 83 |
| Timeframe & holding period | Daily bars; four-week (20 trading day) entry, two-week (10 trading day) exit; holding period not stated (weeks) | 85 |
| Universe / eligibility filters | Liquid markets with "some inherent volatility"; diversified; avoid holding many highly correlated markets | 111 |
| Market / regime filter | None. Turtles traded long and short with "no bias to being long or short" | 83 |
| Setup conditions | **Filter:** skip the S1 signal if the *last* S1 breakout signal (taken or only theoretical, long or short) was a winner; take it if the previous trade was a 2N loss. Direction of the previous trade is irrelevant | 85 |
| Entry trigger & order type | Buy when price makes a new 20-day high; sell short at a new 20-day low. Enter on the breakout itself; do not wait for a retracement | 69, 75, 85 |
| Initial stop-loss | 2N from entry (hard stop), whichever of 2N stop or breakout exit is hit first | 96, 110 |
| Exits: profit-taking | None (no targets) | 88 |
| Exits: trailing / time / signal | Exit long on a 10-day low (exit short on a 10-day high) | 85 |
| Position sizing | 1 unit = 2% of current equity ÷ (2N × point value), rounded down | 95–96 |
| Adding to / pyramiding | Add a unit every 1N in favour, max 5 units; raise all stops to 2N below the newest unit | 100 |
| Portfolio limits (max positions, correlation, heat) | 4–5 units per market; unit limits per sector and for total portfolio (numbers not given); correlated markets count as one; long/short netting rule | 95, 98, 111–112 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry breakout | 20 days ("four-week") | "Feel free to experiment on breakout lengths"; Donchian used 2 weeks | 85–86, 65 |
| Exit breakout | 10 days ("two-week") | — | 85 |
| N (volatility) | 20-day moving average of true range | 15-day ATR in a reader tip | 93 |
| Stop | 2N | 3N in a worked example | 96, 99 |
| Risk per unit | 2% of current equity | 1.5% ("reduce your risk") | 95–96, 99 |
| Pyramid step | 1N | — (see ASSUMPTION on "V2N") | 100 |
| Max units per market | 5 | "four to five units" | 98, 100 |

**Key quotes**

- "System One (S1) used a four-week price breakout for entry and a two-week price breakout in the opposite direction of the entry breakout for an exit." [p. 85]
- "A two-week low was a ten-day breakout—counting trading days only." [p. 85]
- "The Turtles ignored the System One four-week breakout signal if the last four-week breakout signal was a winner." [p. 85]
- "However, if the trade before a current four-week breakout was a 2N loss, they could take the breakout" [p. 85]
- "The Turtles were not to wait for a retracement." [p. 75]
- "The Turtles were instructed to take whichever stop hit first." [p. 110]

**Pseudocode** (daily OHLC per instrument; all signals computed on day t's close, orders for day t+1 unless noted)

```
TR_t   = max(H_t - L_t, |C_{t-1} - H_t|, |C_{t-1} - L_t|)
N_t    = SMA(TR, 20)_t                          # book: 20-day MA of true range
HH20_t = max(H_{t-20..t-1});  LL20_t = min(L_{t-20..t-1})
HH10_t = max(H_{t-10..t-1});  LL10_t = min(L_{t-10..t-1})

theoretical_S1_trade: track every S1 signal as if taken (entry at breakout, exit at 2N stop or 10-day opposite breakout)
last_S1_winner = (most recent completed theoretical S1 trade had P&L > 0)

if flat:
    if H_t >= HH20_t and not last_S1_winner:   enter long, stop-order at HH20_t (intraday)   # ASSUMPTION: stop order at breakout level
    elif L_t <= LL20_t and not last_S1_winner: enter short (futures only)
unit_size = floor( (risk_pct * equity_now) / (2 * N_entry * point_value) )
stop      = entry - 2*N_entry  (long)
pyramid: next_add = last_entry + 1*N_entry; on each add, all stops = newest_entry - 2*N_entry; max 5 units
exit long when L_t <= LL10_t (stop order at LL10_t) or price <= stop, whichever first
```

**Ambiguities & assumptions**

- **N length.** The text says the Turtles took "a twenty-day moving average of true ranges" [p. 93], but the reader tip on the same page says "take the last fifteen true ranges". ASSUMPTION: use 20 for the Turtle rules (that is what the Turtles did); treat 15 as Covel's suggestion.
- **"Four-week" vs 20/55 days.** S1 is described as a "new twenty-day high or low" [p. 69] and as a "four-week" breakout [p. 85]; the 55-day breakout is described first as the generic Turtle entry [p. 83]. ASSUMPTION: S1 = 20 trading days, S2 = 55 trading days.
- **First-day stop "V2N".** The text reads "They set their stops at V2N on the first day of trading and from that point forward, 2N stops were used" [p. 100]. "V2N" is an OCR/typesetting artefact (most likely "½N"). Elsewhere the stop is plainly 2N [p. 96, 110]. ASSUMPTION: initial stop 2N; record the ½N first-day variant as a sensitivity test only.
- **Stop adjustment while pyramiding.** Two statements: stops on all units move to the newest unit's 2N stop [p. 100], and "Turtle stops were adjusted to break even with each 1N market move up" [p. 106]. In the worked example the stops follow the first rule [p. 102–106]. ASSUMPTION: follow the worked example.
- **Filter definition of "winner".** The book does not say whether "winner" is judged on the 10-day exit, the 2N stop, or both. ASSUMPTION: a theoretical S1 trade with the full S1 exit logic (2N stop or 10-day exit, whichever first), P&L > 0 = winner.
- **Entry price.** The book does not say whether entry is intraday at the breakout level or next open. ASSUMPTION: stop order at the prior 20-day high; if the day opens above it (gap), fill at the open.
- **Unit limits per sector/portfolio.** Mentioned but no numbers are given in the text (the table is an image) [p. 95, 98]. ASSUMPTION: see Section 3.
- **Half the money in each system.** "The Turtles typically put half of their money toward each system." [p. 86] — but individual Turtles chose (Carr combined both, Gordon preferred S1) [p. 86]. ASSUMPTION: test S1 and S2 separately and as a 50/50 split.

### 2.2 System Two (S2) — 55-day breakout, 20-day exit

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / breakout | 83, 85 |
| Timeframe & holding period | Daily; 55-day ("eleven-week") entry, 20-day ("four-week") exit; longer-term than S1 | 85 |
| Universe / eligibility filters | Same as S1 | 111 |
| Market / regime filter | None | 83 |
| Setup conditions | No filter. S2 is also the fail-safe entry for a big trend that S1's filter skipped | 85 |
| Entry trigger & order type | Buy at a new 55-day high; sell short at a new 55-day low | 83, 85 |
| Initial stop-loss | 2N | 96, 110 |
| Exits: profit-taking | None | 88 |
| Exits: trailing / time / signal | Exit long on a 20-day low; exit short on a 20-day high | 85, 90 |
| Position sizing | Same unit formula as S1 | 95–96 |
| Adding to / pyramiding | Same as S1 (1N steps, max 5 units) | 100 |
| Portfolio limits | Same as S1 | 98, 111–112 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry breakout | 55 days ("eleven-week") | "Do traders use other values beyond twenty and fifty-five days for entry? Yes." | 85–86 |
| Exit breakout | 20 days | — | 85 |
| Others | As S1 | | |

**Key quotes**

- "It used an eleven-week breakout (fifty-five days) for an entry signal and a four-week breakout (twenty days) in the opposite direction for an exit." [p. 85]
- "If a stock or futures contract made a fifty-five-day breakout to the upside (long), meaning that its current price was the highest price of the last fifty-five days, Turtles would buy." [p. 83]
- "This fail-safe System Two breakout was how the Turtles kept from missing big trends that were filtered out." [p. 85]

**Pseudocode**

```
HH55_t = max(H_{t-55..t-1});  LL55_t = min(L_{t-55..t-1});  LL20_t, HH20_t as S1
if flat and H_t >= HH55_t: enter long (stop order at HH55_t)
unit sizing, 2N stop, 1N pyramiding: as S1
exit long when L_t <= LL20_t or price <= stop
```

**Ambiguities & assumptions**

- **Combining S1 and S2.** When both systems signal on the same day, the risk doubles; the Turtles' own testing found this produced -80% worst-case drawdowns and Dennis halved all position sizes [p. 142–143]. ASSUMPTION: when running S1+S2 together, a market may hold at most one combined position (max 5 units total), or halve the unit risk (memo rule); test both.
- Re-entry after an S2 loss is allowed (the Eurodollar example re-enters short after a losing first breakout) [p. 90–91]. ASSUMPTION: no cooling-off period.

### 2.3 Donchian two-week stop-and-reverse rule (historical baseline)

Covel quotes Richard Donchian's 1960 "weekly trading rule" as the precursor of Turtle trading [p. 65–66]. It is separately testable.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following / breakout, always-in (stop and reverse) | 65–66 |
| Timeframe & holding period | Weekly price extremes (two previous calendar weeks); positions held until reversal | 65–66 |
| Universe / eligibility filters | Commodities ("the optimum number of weeks varies by commodity") | 65 |
| Market / regime filter | None | 65 |
| Setup conditions | None | 65 |
| Entry trigger & order type | Price above high of two previous calendar weeks → cover shorts and buy; below the low → liquidate longs and sell short | 65–66 |
| Initial stop-loss | The opposite breakout (stop and reverse) | 66 |
| Exits | Opposite two-week breakout | 66 |
| Position sizing | Not stated | — |
| Adding to / pyramiding | Not stated | — |
| Portfolio limits | Not stated | — |

**Key quote**

- "When the price moves above the high of two previous calendar weeks (the optimum number of weeks varies by commodity), cover your short positions and buy." [p. 65]

**Pseudocode**

```
WH2 = max(High over the two previous complete calendar weeks); WL2 = min(Low over same)
if price > WH2: close short, go long
if price < WL2: close long, go short (NSE cash: go flat — see Section 5)
```

**Ambiguities & assumptions**

- Sizing is not given. ASSUMPTION: use the Turtle unit formula (2% / 2N) so results are comparable with S1/S2.
- Covel notes in the Afterword that Curtis Faith's Acceleration Capital ran "simply the venerable Donchian trend trading system, unchanged" [p. 262]; no parameters given.

### 2.4 Random entry with Turtle exits (robustness test)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | other (exit-management test) | 92 |
| Entry trigger | Random entries | 92 |
| Exits / stops / sizing | Turtle risk management and exits (2N stop, breakout exit, N-based sizing) | 92 |

**Key quotes**

- "If you initiate purely randomly, you do surprisingly well with a good liquidation criterion." [p. 92]
- "Dennis actually challenged the Turtles to randomly enter the market and then manage their trades after getting in." [p. 92]

**Pseudocode**

```
each day for each flat market: with probability p enter long (or long/short coin flip on futures)
ASSUMPTION: p chosen so that average trade frequency matches S2; run 1,000 seeds
manage with 2N stop + 20-day opposite-breakout exit + Turtle sizing; compare distribution to S2
```

**Ambiguities & assumptions**

- The book gives no entry probability, number of trials or results. ASSUMPTION as above. This is a test of the exit/sizing engine, not a tradable system.

## 3. Risk & money-management rules

- **Unit size:** risk a fixed 2% of capital on hand per trade; each 2% bet is a "unit" [p. 95]. Contracts = (2% × equity) ÷ (2N × point value), rounded down; worked corn example gives 2.67 → 2 contracts [p. 96]. Examples also show 1.5% risk and a 3N stop [p. 99].
- **Use current equity, not starting equity.** "If the Turtles started with $100,000 but now had $90,000 … they had to risk 2 percent of their current $90,000" [p. 72]. Open-trade vs closed equity is irrelevant ("a bookkeeper's artifact") [p. 72]. Unit size is recalculated every day from current equity [p. 95].
- **Max units:** 4–5 per market; pyramid maximum 5 [p. 98, 100].
- **Correlation:** highly correlated markets count as the same position, e.g. "Buying one unit in the Dow and then buying one unit in the S&P is like having two units in either market alone." [p. 111]
- **Long/short netting:** total unit risk = larger side − (smaller side ÷ 2), e.g. 4 long and 3 short = 2.5 units of risk [p. 112].
- **Drawdown rule:** "For every 10 percent in drawdown in their account, Turtles cut their trading unit risk by 20 percent." [p. 108] (2.0% → 1.6% at an 11% drawdown → 1.28% at 22%) [p. 108]. Size is restored as equity recovers [p. 108] (pace of restoration not specified).
- **Leverage halving memo (1986):** after testing, Dennis ordered all Turtles to trade at 50% of prior size because they "have been trading as much as twice as big as we thought" [p. 142–143].
- **Program loss limit (individual):** Gordon recalls "don't lose more than $50,000 doing it" applied to the discretionary "System Three" account [p. 86].
- **Expectation:** Edge = (win% × avg win) − (loss% × avg loss); the Turtles were expected to know their edge [p. 80–81].

## 4. Non-codable guidance

- Follow the rules mechanically; same situation → same action regardless of who you are or how you feel [p. 70–71].
- "Memory-less trading": decisions should not depend on how you got to the current equity or entry price [p. 71, 74].
- Keep taking signals after a string of losses (Paul Tudor Jones example, ~10 consecutive 2% losses before a winner) [p. 73].
- Ignore fundamentals and news; trade price only [p. 66–67, 83].
- Accept that most profits come in short bursts; the group was often down 30% before a few weeks of big gains [p. 126].
- Robustness: small parameter changes should not change results much; keep variables few [p. 86–87].
- Dennis's own discretionary overrides and over-leverage, not the rules, caused his 1988 and 2000 blow-ups [p. 145–148, 169].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLC (open, high, low, close) per stock; adjusted prices (split/bonus) for N and breakouts; equal-weight index or NIFTYBEES only if a regime filter is added (none in the book). No volume, delivery % or fundamentals needed.
- **Testability with our data:** S1, S2, Donchian and random-entry tests are fully backtestable on 2005–2026 NSE prices (long side). No forward-test-only parts.
- **Market-structure differences:**
  - Built for futures, long and short, across ~30 diversified markets [p. 122]. NSE cash has no overnight shorting → ASSUMPTION: long-only; a short signal = stay flat. Expect much weaker results in bear markets (2008, 2020) than the book's long/short context.
  - "Point value" → ASSUMPTION: shares = floor(2% × equity ÷ (2 × N_rupees)), N in rupees per share.
  - Correlation rule → ASSUMPTION: cap units per NSE sector (e.g. max 6 units per sector) and total open risk (e.g. max 12 units, i.e. ≤24% equity at 2N), since the book's sector/portfolio caps are in an unreadable table.
  - Universe → ASSUMPTION: top 200–500 stocks by 3-month median traded value, price > ₹20, to avoid illiquid small caps; rebalance universe monthly.
  - Circuit limits: a stock locked at upper circuit may not fill a breakout buy; locked at lower circuit cannot exit at the stop → ASSUMPTION: skip entries on a day the stock closes at upper circuit; exit at next tradable open after a lower-circuit lock.
  - Costs: apply STT, brokerage and ~0.1% slippage each side; breakout systems trade often (many small losses), so costs matter.
  - Gaps: Indian stocks gap through stops on results days → ASSUMPTION: fill stops at the worse of stop price and open.

## 6. Verdict

- **Codeability:** Fully codable for S1, S2 and the Donchian rule; the rules are mechanical and fully specified except for the ambiguities listed (N length, "V2N", portfolio caps).
- **Priority for backtesting:** High — a canonical breakout/trend system, cheap to implement on daily NSE data, and a useful benchmark for every other breakout spec.
- **Top 3 things a coder is most likely to get wrong**
  1. The S1 filter must use the last *theoretical* S1 trade (whether or not it was taken), and "winner" must be decided with the full S1 exit logic.
  2. Unit size must use *current* equity, the N at entry, and be recomputed daily; the drawdown rule then cuts unit risk 20% per 10% drawdown.
  3. Breakout levels must exclude today's bar (highest high of the prior 20/55 days), and when running S1 and S2 together the double-signal days double the risk unless capped (the 1986 memo).
