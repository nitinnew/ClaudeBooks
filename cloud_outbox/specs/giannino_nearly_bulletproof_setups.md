# Bulletproof Setups: 29 Proven Stock Market Trading Strategies — Matt Giannino

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/Private/Nearly_Bulletproof_Setups_29_Proven_Stock_Market_Trading_Strategies.pdf` (file id `140JjKQNL87fgx677ofWvrFD_0FyCFSZx`, 1,156,617 bytes). The title page reads "BULLETPROOF SETUPS — 29 Proven Stock Market Training Strategies"; © 2020 Matt Giannino, ISBN 978-1-7345540-2-1 (e-book) [p. 1–2]. The inventory listed the author as "Steve Burns?"; key renamed from `burns_nearly_bulletproof_setups`.
- **Text file used:** text/giannino_nearly_bulletproof_setups.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter. (Here the printed page numbers happen to equal the PDF index.)
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/giannino_nearly_bulletproof_setups.md text/giannino_nearly_bulletproof_setups.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 126]]. All 126 pages have text. Every setup's chart (with the numbered entry/stop/exit labels the text refers to) is an image, so "entry #1", "black line" etc. can only be interpreted from the prose. Front matter (author story [p. 11–16]), promotions [p. 120–121] and disclaimer [p. 122–125] contain no rules.

## 1. The method in brief

A visual catalogue of 29 chart setups by a US options/day trader, grouped into Levels 1–3. The author says most are "different ways of getting into pullbacks" in a strong trend, with few reversal setups [p. 18–19]; nearly all "require a very strong trend" [p. 20]; each can be inverted for the short side ("Flip the Book Upside Down") [p. 19]. Every setup gives "Where to Enter" (often a risky and a safer entry), "Where to Place Stop" (usually "below support or above resistance lines") and "Where to Take Profit" (usually a standard three-tier exit: first consolidation zone or 50% retracement / 100% retracement / trend continuation). Stop size is tied to the expected gain: "The amount traders risk is fully dependent on how much they think they can make." with reward:risk 1:2–1:3 (e.g. risk 3–5% to make 10%) [p. 20–21]. Setups are said to work on any timeframe but better on higher ones [p. 21]; the text mixes daily, intraday and options examples (US stocks, SPY, Amazon) [p. 109, 112]. There are **no numeric parameters** for most setups (no MA lengths except 10/50/100/200 mentions, no Bollinger settings, no volume thresholds) and **no evidence** beyond single chart examples and an unsourced "91.4%" gap-fill statistic [p. 29].

## 2. Strategies

Common rules applied unless a setup says otherwise (cited once here):

- **Standard exit** (setups 12, 14, 16, 17, 18, 19, 20, 25, 27): "The best short-term exit is the first consolidation zone or 50% retracement of the prior move. The mid-term exit is going to be a 100% retracement of the preceding move." [p. 65]
- **Standard stop:** "The stop loss should be placed below support or above resistance lines." [p. 39] with size per the reward:risk rule [p. 20–21].
- **Daily-bar interpretation:** ASSUMPTION for all setups: daily bars; "strong trend" = close > SMA50 > SMA200 and 63-day return > 15% (long side); "consolidation zone" = most recent 5–20-day range with width < 1.5× ATR(20)×√n; "50% retracement of the prior move" = midpoint of the most recent swing measured from swing low to swing high (for longs entered after a pullback, the target is the prior swing high = "100% retracement").
- Long side only for NSE (Section 5); bearish/short variants are listed but not specified.

Each setup below is given in a compact table (fields the book does not address are omitted and listed as "not stated" in Ambiguities).

### 2.1 Setup 1 — Gap fill or bounce (Level 1)

| Field | Rule | Page |
|---|---|---|
| Type | mean-reversion (gap fill) / bounce | 28 |
| Setup | A price gap and a stock heading into it; confirmation = price enters the gap | 28–29 |
| Entry | Long: once price enters the gap (gap-up left above). Short (gap-and-go): after the first candle, stop near its open | 29–30 |
| Stop | Below (long) / above (short) the gap's starting line | 30 |
| Exit | Gap-fill: when the gap fills (far edge); gap-and-go: scale out as momentum slows | 29–30 |

- "Studies have been done that show 91.4% (Bioequity.com) of gaps eventually get filled, which tells the power of the gap fill strategy." [p. 29]
- "Once price enters the gap, we usually see a move to the top of the gap." [p. 30]

### 2.2 Setup 2 — Engulfing candle momentum play (Level 1)

| Field | Rule | Page |
|---|---|---|
| Type | momentum / continuation | 31 |
| Setup | Candle whose range engulfs the previous candle's body; usually followed by ≥ 1 candle in the same direction; fails in directionless markets | 31–32 |
| Entry | Better: close of the engulfing candle / open of the next (entry #1); risky: as soon as it passes the prior candle's high (entry #2) | 33 |
| Stop | "no lower than ⅓ the candle body" | 33 |
| Exit | Fixed-percentage trailing stop | 33 |

- "For this place, your stop-loss is best no lower than ⅓ the candle body." [p. 33]

### 2.3 Setup 3 — Continuation off open (Level 1)

| Field | Rule | Page |
|---|---|---|
| Type | momentum / continuation | 34 |
| Setup | A trend begins with a candle much larger than recent candles; next candle must not trade much below its close | 34–35 |
| Entry | Open of the next candle (entry #1); or close of the large candle to avoid gaps (entry #2); skip if it gaps far higher | 36 |
| Stop | Below the close of the large bullish candle | 36 |
| Exit | Trailing stop; "best used on a larger time frame" | 35–36 |

- "The stop loss should be placed below the close of the first bullish candle (or below the open of the entry candle)." [p. 36]

### 2.4 Setup 4 — Channel support/resistance bounces (Level 1)

| Field | Rule | Page |
|---|---|---|
| Type | mean-reversion (range/channel) | 37 |
| Setup | Ascending, descending or flat channel; most reliable in the first 2–3 touches; draw resistance through two highs, parallel line through the lowest low | 37–38 |
| Entry | Long at touches of the channel bottom | 38 |
| Stop | Below support | 39 |
| Exit | Top of channel, or halfway | 39 |

### 2.5 Setup 5 — Post-trend pullback pops (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | trend-following pullback | 41 |
| Setup | After a strong (bullish) trend, a consolidation channel forms; gap-downs near channel support get bought | 41–42 |
| Entry | #1 first gap-down, right after price reverses up from the open; #2 at channel support | 43 |
| Stop | Below the open/low of day (#1); below support (#2) | 43 |
| Exit | Channel resistance | 43 |

### 2.6 Setup 6 — W bottom (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | reversal (double bottom) | 44 |
| Setup | Downtrend, first bounce, second bottom at an equal or higher low | 44–45 |
| Entry | First green candle on the second bottom; lower-risk: the consolidation candles after the reversal | 45–46 |
| Stop | Below support (the bottom) | 46 |
| Exit | Short-term: the W's middle peak; swing: 50% retracement of the prior downtrend; long-term: 100% retracement | 46 |

- "Short term traders will take profit in the middle of the W resistance (highest point between the two bottoms). Swing traders will take profit around the 50% retracement of the previous downtrend." [p. 46]

### 2.7 Setup 7 — MACD buy signal (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | trend reversal / trend-following | 47 |
| Setup | After a large trend (wide MACD line separation); only a clear crossover; longs only when both MACD lines are above zero | 47–48 |
| Entry | MACD line crosses above signal line | 49 |
| Stop | A fixed percentage below entry | 49 |
| Exit | Opposite MACD cross | 49 |

- "Traders will also only take bullish positions when the two moving averages are above the zero line" [p. 48]

### 2.8 Setup 8 — Bottom Bollinger Band pullback (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | trend-following pullback | 50 |
| Setup | Strong trend riding between the upper band and midline; first real sell-off touches the lower band | 50 |
| Entry | Risky: first lower-band touch; better: once the stock stops making new lows (gap up, bottoming/green candle) | 51–52 |
| Stop | Below the lowest part of the move, with wiggle room | 51 |
| Exit | Short-term: middle band or 50% retracement; mid-term: prior high | 52 |

- "The best short-term target is the mid bollinger band or the 50% retracement of the prior move." [p. 52]

### 2.9 Setup 9 — Cup and handle (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | breakout / reversal | 53 |
| Setup | Prior trend, rounded cup with progressively shallower drops, small breakout, handle (wedge/descending channel); bigger cup → bigger breakout; handle optional | 53–55 |
| Entry | Upper portion of the cup (#1) or handle support (#2) | 55 |
| Stop | Below the cup support arc (#1) / handle support line (#2) | 55 |
| Exit | Prior consolidation levels (short-term); full retracement of the preceding move (long-term) | 55 |

### 2.10 Setup 10 — High-volume-node profit zone (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | support/resistance from volume profile (mainly an exit tool) | 56 |
| Setup | Volume-profile peaks act as support/resistance; zone shifts with chart zoom | 56–57 |
| Entry | Long above a high-volume node | 58 |
| Stop | Below support | 58 |
| Exit | At the next high-volume node peak | 58 |

- "These are great for getting more details on a current trade but not great for planning trades." [p. 57]

### 2.11 Setup 11 — Short squeeze end of trend (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | momentum (long before) / reversal (short after) | 59 |
| Setup | Months-long tight range, volume picks up, series of "pops", final capitulation-volume spike then swift drop | 59 |
| Entry | Long at consolidation zones before the squeeze; short at the first bearish candle after capitulation | 61 |
| Stop | Short: above prior highs | 61 |
| Exit | Long: when volume doubles or triples | 61–62 |

### 2.12 Setup 12 — Resistance/support rejection (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | mean-reversion at S/R | 63 |
| Setup | Prior horizontal level touched multiple times; thin-bodied, wicky "toppy" candles at the level; third touch tends to break | 63–64 |
| Entry | Risky: first touch of support; safer: the rejection (higher-low wick, next candles moving up) | 65 |
| Stop / Exit | Standard | 65 |

- "The typical rule is on the third touch of an important level; we usually see a follow-through that level." [p. 64]

### 2.13 Setup 13 — Failed moving-average breakthrough (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | trend-following pullback | 66 |
| Setup | Up-sloping fast MA (the 10 MA) in a trend; a pullback candle cuts through it but closes back above / doesn't stay below | 66–68 |
| Entry | Risky: at the break of the 10 MA; safer: the candle after one closes back above the 10 MA | 68 |
| Stop | Below the moving average | 68 |
| Exit | Day traders: shortly after the bounce; longer: prior highs, trend continuation, or close crossing the 10 MA | 68 |

- "When the candlestick closes on top of the moving average, this will offer traders a safer place to enter, which will be during the very next candle" [p. 68]

### 2.14 Setup 14 — Pennant or wedge pullback breakout (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | breakout / continuation | 69 |
| Setup | Converging pullback after a trend; breakout near the apex, either direction possible | 69–70 |
| Entry | Risky: support touches; or wait for the breakout (entry #1) | 70 |
| Stop / Exit | Standard; note many take profit at mid-pattern or the prior high | 70–71 |

### 2.15 Setup 15 — Moving-average crossover (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | trend change | 72 |
| Setup | After a steep trend, fast MA crosses slow (10/50 or 50/200); best on steep trends; retest/rejection of the MAs often follows | 72–73 |
| Entry | (Shown short) price crosses the 10 MA (#1, #2); fast/slow cross (#3); retest/rejection of MAs (#4) | 74 |
| Stop | Beyond the moving-average lines | 74 |
| Exit | Mirror of the entry: price re-crossing the 10 MA, the opposite cross, or a retest/rejection | 74 |

- "This could be the 10 MA (moving average) and 50 MA, or the 50 MA and the 200 MA." [p. 72]

### 2.16 Setup 16 — Support/resistance break and retest (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | breakout / breakdown with retest | 75 |
| Setup | Level defined by ≥ 2 holds; break, then retest and rejection of the level from the other side | 75 |
| Entry | #1 at the break; #2 (safer) retest and rejection | 76–77 |
| Stop | Just beyond the level (exit on a reversal back through it) | 76 |
| Exit | Standard | 77 |

- "It is at a retest and reject of a predefined level." [p. 75]

### 2.17 Setup 17 — Inside candle reversal (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | reversal / range breakout | 78 |
| Setup | Trend slowly dies into tiny candles inside the first (mother) candle's range; more inside candles → bigger breakout | 78–79 |
| Entry | Risky: touch of the inside-range support; safer: confirmed breakout from the range | 79 |
| Stop / Exit | Standard | 80 |

### 2.18 Setup 18 — Bollinger Band squeeze (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | volatility breakout | 81 |
| Setup | Consolidation after a trend; bands contract; move usually in the prior trend's direction | 81–82 |
| Entry | Risky: before breakout; safer: once price breaks out | 82–83 |
| Stop / Exit | Standard | 83 |

### 2.19 Setup 19 — Indicator divergence and reversal (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | reversal | 84 |
| Setup | New price low with a higher indicator low (RSI favoured; author's proprietary "Market Mover" indicator in the example); only extreme readings | 84–85 |
| Entry | Needs other evidence (e.g. trendline support) | 86 |
| Stop / Exit | Stop "vague and not defined"; standard exit | 86 |

### 2.20 Setup 20 — Head and shoulders (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | reversal (shown bearish) | 87 |
| Setup | Left shoulder consolidation, higher head, drop back to the left-shoulder level, right-shoulder consolidation | 87–88 |
| Entry | Risky: in the right-shoulder consolidation; safer: break of it | 89 |
| Stop / Exit | Beyond the left shoulder's wicks; standard exit | 88–89 |

### 2.21 Setup 21 — 3-bar play (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | momentum / continuation | 90 |
| Setup | Bar 1 "igniting bar" with a larger body than most prior candles and volume; bar 2 "baby bar" whose range stays in the top third of bar 1's range | 90–91 |
| Entry | Bar 3, when it breaks the highs of the previous two bars | 92 |
| Stop | Below the low of the baby bar | 92 |
| Exit | Quick: before the close of the confirmation candle (day-trade); can ride if volume builds | 91–92 |

- "If the range of the baby bar stays above the top third of the range of the igniting bar, this will setup perfectly for a continuation with the confirmation candle." [p. 90]
- "The stop loss should be placed below the low of the baby bar." [p. 92]

### 2.22 Setup 22 — Copy-cat candles (Level 2)

| Field | Rule | Page |
|---|---|---|
| Type | reversal | 93 |
| Setup | Very long candles (ideally news-driven, low price structure) drop; bottoming candles appear | 93–94 |
| Entry | When price enters the range of the large opposing candle (breakout); risky: at support before | 95 |
| Stop | Below the bottom low | 95 |
| Exit | Top of the body of the prior long (opposing) candle | 96 |

### 2.23 Setup 23 — Flat moving-average magnets (Level 3)

| Field | Rule | Page |
|---|---|---|
| Type | mean-reversion (range) | 98 |
| Setup | Several MAs flat and close together; extremes revert to the MA cluster | 98–99 |
| Entry | Long: price below all flat MAs, then a bottoming candle (thin body, long wicks) followed by a large green candle | 100 |
| Stop | "vague and not easily defined" | 100 |
| Exit | When price crosses one, two or three of the MAs | 100 |

### 2.24 Setup 24 — Channel breakout and fall back (Level 3)

| Field | Rule | Page |
|---|---|---|
| Type | momentum (long) / fade (short) | 101 |
| Setup | Upward channel; price breaks above it, then usually fades back in | 101–102 |
| Entry | Long: channel breakout (#1) or touch of the old channel line after breakout (#2); short: fade back inside | 103 |
| Stop / Exit | Standard stop; short exit at channel bottom or middle | 103 |

### 2.25 Setup 25 — Channel breakdown and retest (Level 3)

| Field | Rule | Page |
|---|---|---|
| Type | breakdown (short) | 104 |
| Setup | Ascending channel shows lower highs, breaks down; retest of the channel line from below and rejection | 104–105 |
| Entry | #1 break of channel; #2 retest/rejection | 106 |
| Stop / Exit | Beyond the channel line; standard exit | 106 |

### 2.26 Setup 26 — Moving average and Bollinger Band squeeze (Level 3)

| Field | Rule | Page |
|---|---|---|
| Type | volatility breakout / continuation | 107 |
| Setup | After a trend: 2–3 MAs (e.g. 10/50/100) converge and flatten (never all sloping down) while Bollinger Bands squeeze; volume very low | 107–108 |
| Entry | Safer: on breakout; best: pullback after the breakout to the 10 MA (#2) | 108–109 |
| Stop | Below the slowest MA (#1) / below the fastest MA (#2) (colour labels contradictory, see Ambiguities) | 110 |
| Exit | Upper Bollinger Band touch (#2) or price crossing the 10 MA (#1) | 110 |

- "These moving averages must never slope down together; this is going to be huge support for the stock during the pullback." [p. 107]
- "The best place to take profit is when price touches the upper bollinger (exit #2) band or when price crosses the ten moving average (exit #1)." [p. 110]

### 2.27 Setup 27 — Trend pullback and bounce off the 200 moving average (Level 3)

| Field | Rule | Page |
|---|---|---|
| Type | trend-following pullback | 111 |
| Setup | Strong trend with 10/50/200 MAs sloping up; first large pullback reaches the rising 200 MA with buyer confirmation | 111 |
| Entry | As close to the 200 MA as possible | 113 |
| Stop | Below the 200 MA | 113 |
| Exit | Standard | 113 |

- "This only works if the 200 moving average is sloping up at the time of the pullback and we see confirmation that buyers are coming in." [p. 111]

### 2.28 Setup 28 — Reversal and 10 moving-average curl (Level 3)

| Field | Rule | Page |
|---|---|---|
| Type | reversal | 114 |
| Setup | Strong down-trend, a bottom, a pop above the 10 MA; the 10 MA flattens and price sits on it for several candles | 114–115 |
| Entry | When price sits on the flattened 10 MA, ideally the 2nd or 3rd candle of support | 116 |
| Stop | Below the 10 MA | 116 |
| Exit | Middle Bollinger Band (short-term), upper band (long-term), or 50/100% retracement | 116 |

- "it is important to note that it is better to wait for the second or third candle to find support on the moving average." [p. 116]

### 2.29 Setup 29 — Moving-average twist (Level 3)

| Field | Rule | Page |
|---|---|---|
| Type | trend-following / continuation | 117 |
| Setup | After a trend, MAs converge or cross (twist) in a flat consolidation, then re-stack in bullish order (fast > medium > slow) with faster ones sloping up | 117–118 |
| Entry | When MAs stack in bullish order | 119 |
| Stop | Below the slowest MA | 119 |
| Exit | When the MAs cross / a new order begins | 119 |

- "The best place to enter long positions is when moving averages stack up in a bullish order (slow, medium, fast - bottom to top), as seen by the long entry above." [p. 119]

**Parameters (book-wide)**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Reward:risk | ≥ 1:2, preferably 1:3 | — | 8, 21 |
| Risk for 10% target | 3–5% | — | 21 |
| MA lengths named | 10, 50, 100, 200 | 10/50 or 50/200 for crossovers | 72, 107, 111 |
| Swing holding | 1–10 days | — | 9 |
| Trailing stop | fixed % (5% example) | — | 9, 33 |
| Channel reliability | first 2–3 touches | — | 38 |

**Key quotes (book-wide)**

- "All of these plays, with few exceptions, require a very strong trend to find consistent success." [p. 20]
- "Using simple math, if a trader plans on making 10%, they can risk 3-5% depending on the risk reward ratio chosen." [p. 21]
- "The majority of these setups are just different ways of getting into pullbacks in the market" [p. 19]

**Pseudocode** (daily bars; only the setups with enough definition to code — 2, 3, 7, 8, 13, 21, 26, 27, 28, 29; all long-only)

```
strong_up_t = C > SMA50 > SMA200 and SMA200 rising(20d) and C/C_{t-63} - 1 > 0.15         # ASSUMPTION
R = entry-stop; target default = entry + 2.5*R (between 1:2 and 1:3, ASSUMPTION) unless setup gives a level

S2  engulf:  C_t>O_t and O_t<=min(O,C)_{t-1} and C_t>=max(O,C)_{t-1} and H_t>H_{t-1}; enter O_{t+1}
             stop = O_t + (C_t-O_t)*2/3   # "no lower than 1/3 the candle body" read as: risk at most 1/3 of the body (ASSUMPTION)
             exit: 5% trailing stop from highest close
S3  cont:    body_t >= 2*mean(|C-O|, 20) and C_t>O_t; enter O_{t+1} unless O_{t+1} > C_t*1.02; stop = C_t*0.995; 5% trail
S7  MACD:    MACD(12,26,9) line crosses above signal and both > 0 (after a 20-day decline >10%, ASSUMPTION "large trend")
             stop entry*0.95 (ASSUMPTION "certain percentage"); exit on opposite cross
S8  BB pull: strong_up; L_t <= BBlo(20,2)_t; enter at first C > H_{t-1} within 5 days; stop = min L since touch *0.99;
             T1 = BBmid (half), T2 = prior swing high (rest)
S13 MA10:    strong_up; EMA10/SMA10 rising; L_t < MA10_t and C_t >= MA10_t → enter O_{t+1}; stop = MA10*0.98; exit close < MA10 or prior high
S21 3-bar:   body_1 >= 2*mean body(20) and V_1 >= 1.5*ADV20; L_2 >= L_1 + (2/3)*(H_1-L_1); H_2 <= H_1 (ASSUMPTION);
             day 3 buy-stop at max(H_1,H_2); stop = L_2; exit at close of day 3 (book: quick exit) — variant 5% trail
S26 MA+BB:   SMA10, SMA50, SMA100 within 2% of each other, none of the three sloping down;
             BB(20,2) width in lowest 10% of last 120 days; breakout C > BBup → watch; enter at first touch of MA10 within 10 days
             stop = MA10*0.98; exit at BBup touch (variant: close < MA10)
S27 200MA:   strong_up (all of 10/50/200 rising) ; L_t <= SMA200_t*1.01 and C_t > SMA200_t and C_t > O_t; enter O_{t+1}
             stop = SMA200*0.97 ; T = 50% then 100% retracement of the decline (prior high)
S28 curl:    63-day return < -15%; C > MA10 for >= 3 days; |slope(MA10,5)| < 0.3%/day; L touches MA10 on day 2-3 → enter close
             stop = MA10*0.98; T1 = BBmid, T2 = BBup
S29 twist:   MAs 10/50/100 crossed each other >= 2 times in last 30 days (consolidation) and now EMA10 > SMA50 > SMA100 with EMA10 rising
             enter C_t on the first day of the bullish stack; stop = SMA100*0.99; exit when any of the three crosses (order breaks)
```

**Ambiguities & assumptions**

- **No numeric parameters** for most setups: MA type and length (only 10/50/100/200 named, never SMA vs EMA), Bollinger settings, "strong trend", "large candle", "consolidation zone". ASSUMPTION: as in the pseudocode; SMA unless stated, BB(20,2).
- **Stop sizing rule** ties risk to the expected gain [p. 20–21] rather than to the chart, but each setup also gives a chart level ("below support"). ASSUMPTION: use the chart level and skip trades where reward:risk to the first target < 2.
- **Setup 2 stop** ("no lower than ⅓ the candle body" [p. 33]) is ambiguous (⅓ from the top or bottom). ASSUMPTION: risk no more than ⅓ of the body measured down from the close.
- **Setup 26 stop colours** contradict the earlier colour key (10-yellow/50-blue/100-red [p. 107] vs. "slowest moving average (yellow)" and "fastest moving average (purple)" [p. 110]). ASSUMPTION: slowest = 100, fastest = 10.
- **Setup 29** says to enter when MAs stack "slow, medium, fast - bottom to top" [p. 119]; the MA lengths are not given (colours only). ASSUMPTION: 10/50/100.
- **Intraday content:** setups 1, 2, 5, 13 and 21 are described partly for day trading (enter "during" a candle, exit before the candle closes) [p. 32, 43, 68, 92]. Daily-bar tests approximate these.
- **Proprietary indicator**: setup 19's example uses the author's "Market Mover" indicator [p. 85]; ASSUMPTION: RSI(14) divergence instead.
- **Volume** is mentioned (3-bar igniting bar, short squeeze, MA/BB squeeze) without thresholds. ASSUMPTION: 1.5× 20-day average where required.

## 3. Risk & money-management rules

- Every trade needs an exit plan with a stop loss and a profit zone [p. 20].
- Reward:risk above 1:2, preferably 1:3 [p. 8, 21]; risk 3–5% for a 10% expected move [p. 21].
- Trailing stops: fixed percentage that rises with price (5% example) [p. 9, 33].
- Scale into and out of positions to improve average prices [p. 8].
- No per-trade capital-risk percentage or portfolio limit is given.

## 4. Non-codable guidance

- Trade with momentum; "nail the pullback" rather than call reversals [p. 18–19].
- Higher timeframes are more reliable; expect less accuracy on lower ones [p. 21].
- Look for indecision candles (small bodies, wicks on both ends) as confirmation at pullbacks [p. 26].
- Execution and emotional control are half of the result [p. 21–22].
- Options straddles/strangles are suggested around squeezes [p. 82, 109, 118–119] — out of scope.

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV; SMA/EMA 10/50/100/200; Bollinger Bands; MACD; RSI; volume profile (setup 10, not in our data as such but derivable approximately from daily volume by price bins).
- **Testability with our data:** The ten setups in the pseudocode are backtestable on 2005–2026 daily prices. Setups 4, 5, 6, 9, 12, 14, 16, 17, 19, 20, 22, 23, 24 need pattern/trendline/channel detection with heavy assumptions; setups 10 and 11 need volume-profile or capitulation definitions; setups 1, 11 (short side), 20, 25 are shown as shorts or gap-fades.
- **Market-structure differences:**
  - Written for US stocks and options; no overnight shorting in the NSE cash market, so all short/bearish variants (11 short, 15 as shown, 20, 25, and the "flip the book" inversions) are excluded. ASSUMPTION: test long mirror images only where the book itself describes the long version.
  - Gaps: NSE opening auctions and circuit limits affect gap-fill (setup 1) and gap-entry setups. ASSUMPTION: skip entries on stocks hitting upper circuit; fill at open.
  - Costs: STT, brokerage, ~0.1% slippage; several setups (3-bar play, continuation off open) are short-holding and cost-sensitive.
  - Add a liquidity floor (not in the book). ASSUMPTION: 20-day average traded value ≥ Rs. 1 crore.

## 6. Verdict

- **Codeability:** Partly. About ten setups can be coded with assumed parameters; the rest are discretionary chart-pattern reads with no numeric rules, and even the codable ones lack MA types, band settings and volume thresholds.
- **Priority for backtesting:** Low. A generic US day-trader catalogue with no parameters and no evidence; its codable setups (200-MA bounce, BB pullback, MACD above zero, MA stack, 3-bar play) duplicate rules already specified more precisely in other books (Burns, Ladha, Shah, More).
- **Top 3 things a coder is most likely to get wrong**
  1. Treating the setups as short-side-neutral: the book shows several as shorts and tells the reader to "flip" the rest; on NSE only the long versions apply.
  2. Using a fixed percentage stop everywhere: the book places stops at chart levels (below support, below the baby bar, below the 200 MA) and then checks the reward:risk.
  3. Taking MACD crosses anywhere: the book's version requires a prior large trend, a clear cross, and both MACD lines above zero for longs [p. 47–48].
