# The 20 EMA: How To Use The 20-Period Exponential Moving Average To Find Short-Term Explosive Stock Moves — Jayesh Shah

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/Private/THE_20_EMA_How_To_Use_The_20_Period_Exponential_Moving_Average_To....pdf` (file id `1Nueb8fa6yFJXzi1-xINjVVziGFEZn6Ju`, 3,664,225 bytes). The inventory listed this as Steve Burns; the title page names **Jayesh Shah** [p. 3], so the key is `shah_20_ema` (was `burns_20_ema`). No year printed; the author's trades are dated November–December 2022 [p. 34].
- **Text file used:** text/shah_20_ema.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter. (This ePub-style PDF has no printed page numbers.)
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/shah_20_ema.md text/shah_20_ema.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 40]]. Pages 1–2, 9, 17, 19, 21 and 27 are images with no text (cover, review screenshots, setup diagrams). All charts are images (from chartink.com); only the running text describing them is available.

## 1. The method in brief

One setup for Indian stocks, traded over a few days to 2–3 weeks [p. 11]: a stock that has been below its 20-day EMA crosses above it and makes a swing high (the "20 EMA pivot"); the pullback from that pivot must hold **at or above** the 20 EMA (any break below disqualifies the setup); buy when price breaks above the pivot, ideally on at least double the previous month's average volume, with an initial stop just under the breakout bar's low [p. 16–22, 26, 33]. Exits: four alternatives — warning candle (long red candle, long upper wick, doji at the top), trailing stop under each prior day's low, fixed 10–15% target with 10% stop, or "always in profit" (sell half at ~10%, move stop to entry on the rest, exit the rest on a warning candle) [p. 26–32]. The author's own routine combines them: half off at 10–15%, rest on a warning candle, trailing stop for sluggish movers [p. 33].

Evidence: chart examples (Salasar +42% in 9 days; Dhanbank +47% in 2 weeks; Skipper +70% in 14 days [p. 22–25]) and three of the author's trades (UCO Bank +100% in a month, Skipper +12%/+16%, FACT +52% on the second half [p. 34–36]). Failed examples are shown only where the 20-EMA rule was broken (DYCL, DCAL, Power Mech B) [p. 23, 37–39]. No statistics.

## 2. Strategies

### 2.1 20-EMA pivot breakout

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout (pullback-continuation) | 16 |
| Timeframe & holding period | Daily; a few days to 2–3 weeks | 11 |
| Universe / eligibility filters | Indian stocks; scan for stocks "just above 20 EMA"; optional 200 EMA for the major trend only (not used in the setup) | 12, 33 |
| Market / regime filter | None stated | — |
| Setup conditions | Step 1: after trading below the 20 EMA for days/weeks, price breaks above it, halts and reverses — that high is the 20 EMA pivot. Step 2: the pullback must halt at or above the 20 EMA; if price falls below the 20 EMA, remove it from the watchlist. Small candles / dojis and drying volume near the 20 EMA are positive | 16–20, 25, 34 |
| Entry trigger & order type | Buy as soon as price breaches the pivot (price alert ~1 point above the pivot), on the breakout day; skip if price gaps far above the pivot, action is erratic, or breakout volume is feeble; volume on breakout ≥ 2× the previous month's average ("I never ignore this rule"); no GTC buy orders | 20, 22, 33, 35 |
| Initial stop-loss | 1 point (rupee) under the low of the breakout bar; never lowered | 22, 26 |
| Exits: profit-taking | (a) Fixed: target 10–15% with 10% stop; (b) Always-in-profit: sell half at ~10% (author: 10–15%), stop on the rest raised to the purchase price; (c) consider exiting fully at 30–40% after taking half | 32–33 |
| Exits: trailing / time / signal | (d) Warning candle: exit on a long red candle, a candle with a long upper wick, or a doji after a sharp up move; (e) trailing stop below each prior day's low (used for sluggish 1–2%/day movers) | 26–31, 33 |
| Position sizing | Not stated | — |
| Adding to / pyramiding | Not stated (re-entry on a later pivot breakout shown in examples) | 35 |
| Portfolio limits | Not stated | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Moving average | 20-period EMA (not SMA) | 8 EMA "too volatile" | 12 |
| Breakout volume | ≥ 2× previous month's average | "the higher the better" | 22, 33 |
| Initial stop | 1 point below breakout-bar low | 10% (fixed-exit variant) | 26, 32 |
| First target | 10–15% (sell half) | 10% in worked example | 32–33 |
| Full exit | 30–40% gain | — | 32 |
| Max chase | skip if "gapped up way above" the pivot; EOD scans often 10–12% above → too late | — | 33 |

**Key quotes**

- "Here we need to find a stock that, after trading for a few days or a few weeks below the  20 MA, breaches it to the upside. After breaching the 20 MA from below, it should halt at some point and reverse. This high point is our 20 MA PIVOT." [p. 16]
- "The stock MUST halt its downward move at or above the 20 EMA at any cost." [p. 18]
- "Never forget the rule here: If the stock falls below the 20 EMA, remove it from your watchlist." [p. 20]
- "Buy the stock as soon as it breaches the pivot point created above the 20 EMA." [p. 20]
- "Buy on the day of the breakout. Keep an initial stop loss below the low of the breakout candle." [p. 22]
- "I recommend keeping an initial stop loss placed 1 point under the breakout bar." [p. 26]
- "Volume on the breakout day should be at least double the average volume of the stock for the last month before the breakout. I never ignore this rule." [p. 33]
- "I take half of my position out at a 10-15 percent gain. For the remaining half, I wait for a warning candle to appear on the daily chart" [p. 33]
- "The best solution is to sell half of your position at 110. This way you have booked a 10 percent profit on half of your position. Now raise your stop loss to your purchase price on the remaining half of your position." [p. 32]
- "Here you trail your stop loss below the low of each higher candle formed and get out as soon as the price breaches the low of the previous day's candle." [p. 30–31]

**Pseudocode** (daily bars)

```
E = EMA(C, 20); VAVG = SMA(V, 21) shifted 1 (previous month)
# Step 1: cross-up after being below
cross_day c: C_c > E_c and C_{c-k} < E_{c-k} for k in 1..5            # ASSUMPTION: >= 5 prior closes below ("a few days")
# pivot: first swing high after c: H_p = max(H_{c..p}) and H_{p+1} < H_p and H_{p+2} < H_p   (2-bar confirmation, ASSUMPTION)
P = H_p
# Step 2: pullback holds the EMA
valid while every bar after p: C >= E (and L >= E*0.99)                # ASSUMPTION: closes at/above EMA; tolerate intraday pierce <=1%
                                                                        # book: "never crossed below" → strict variant: L >= E
invalidate if C < E (remove from watchlist); expire after 30 sessions (ASSUMPTION)
# Step 3: breakout
trigger day t: H_t > P and V_t >= 2*VAVG_t
   skip if O_t > P*1.05                                                 # ASSUMPTION: "gapped up way above"
   fill = max(O_t, P*1.002)                                             # alert ~1 point above pivot
stop = L_t - tick_buffer (≈ 1 rupee; ASSUMPTION: max(1.0, 0.5% of price) for high-priced stocks)
exits (test separately):
 A fixed:  target = entry*1.10 (alt 1.15), stop = entry*0.90
 B always-in-profit: at entry*1.10 sell 50%, stop on rest = entry; rest exits on warning candle (D) or entry*1.35
 C trail:  from day t+1, stop_t = L_{t-1}; exit intraday when L_t < L_{t-1} (fill at min(O_t, L_{t-1}))
 D warning candle (close-based, exit at close):
     long red:     C<O and (O-C) >= 2*avg(|C-O|,20)
     upper wick:   H - max(O,C) >= 2*|C-O| and H - max(O,C) >= 0.5*(H-L)
     doji at top:  |C-O| <= 0.1*(H-L) and C >= entry*1.10                # "after a sharp up move" (ASSUMPTION threshold)
author's mix (base case): B with C when the advance is "sluggish" (avg daily gain < 2% over 3 days, ASSUMPTION)
size: ASSUMPTION 1% equity risk on (fill - stop), cap 20% of equity
```

**Ambiguities & assumptions**

- **Strictness of "at or above"**: "halt its downward move at or above the 20 EMA" [p. 18], "never crossed below it" [p. 39] vs. examples where the pullback "halted exactly at 20 EMA" [p. 24] and candles "closed below" disqualify [p. 36]. ASSUMPTION: base case closes ≥ EMA20 with lows ≤ 1% below tolerated; strict variant uses lows.
- **"1 point under the breakout bar"** [p. 26] is a rupee amount on low-priced stocks (UCO Bank Rs 17 → stop 15.50 under a 15.70 low [p. 34]). ASSUMPTION: max(Rs 1, 0.5% of price).
- **Volume rule** is from the author's earlier book but called inviolable here [p. 33]; yet his Skipper second entry is justified on "good volume" only [p. 35]. ASSUMPTION: ≥ 2× previous 21-session average.
- **Entry timing**: intraday alert above the pivot [p. 33]; daily data can only fill at max(open, pivot). The author warns EOD-scan entries the next day are often "too late" [p. 33]. ASSUMPTION: stop-order fill at the pivot breach; variant enters at the close only if close ≤ 5% above the pivot.
- **Warning candles** are described qualitatively [p. 28–29]. ASSUMPTION: thresholds in pseudocode.
- **No position sizing** rule. ASSUMPTION: 1% risk.
- **Re-entries**: examples show taking a second pivot breakout after missing the first (Skipper P-2) [p. 35]. ASSUMPTION: allow re-entry on each new valid pivot.

## 3. Risk & money-management rules

- Decide initial stop and profit-taking plan before entry [p. 26].
- Never lower the stop; a break of the breakout bar's low means the breakout failed [p. 26].
- Raise the stop to entry after the first partial profit [p. 32]; FACT example raises to the next pivot after the second breakout [p. 36].
- No position-size or portfolio rule is given.

## 4. Non-codable guidance

- Watch behaviour days to months before a breakout; the strength of a breakout depends on what happens before it [p. 16].
- Don't buy the first pullback or a reversal candle at the 20 EMA; wait for the pivot break [p. 23–24].
- Avoid GTC buy orders that fill on morning gap-ups that later reverse [p. 35].
- Master one setup; study 50–100 charts [p. 25, 37, 39].
- T+2 settlement prevented selling on day 2 at the time [p. 34] (now T+1 in India).

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV only (EMA20, volume average); optional EMA200.
- **Testability with our data:** Fully backtestable on 2005–2026 daily prices; no index or fundamental data needed.
- **Market-structure differences:**
  - Written for NSE (chartink/topstockresearch screens, Indian examples). Long-only, fits the cash market.
  - Upper circuits: the author could not buy Skipper on a circuit-locked breakout day [p. 35]. ASSUMPTION: no fill if the breakout day opens and closes at the upper band; next-day entry only if ≤ 5% above the pivot.
  - Many examples are low-priced, high-volume stocks (UCO Bank Rs 17, Dhanbank Rs 17) [p. 23, 34]. ASSUMPTION: liquidity floor of 20-day average traded value ≥ Rs 1 crore; report results by price bucket.
  - Costs: STT, brokerage, ~0.1% slippage per side; breakout-day slippage can be larger (UCO filled 6% above the pivot [p. 34]). ASSUMPTION: model 0.3% extra entry slippage on breakout fills as a sensitivity.

## 6. Verdict

- **Codeability:** Fully. The three-step setup, the volume rule and the stop are mechanical; only pivot confirmation, "at or above" tolerance and warning-candle shapes need numeric defaults.
- **Priority for backtesting:** High. NSE-specific, single mechanical daily setup with a clear invalidation rule and explicit exits, testable on our full price history at low cost.
- **Top 3 things a coder is most likely to get wrong**
  1. Allowing a pullback that closes below the 20 EMA: that permanently disqualifies the pivot [p. 20, 23].
  2. Defining the pivot as any recent high: it must be the swing high formed **after** the stock crossed up through the 20 EMA from below [p. 16].
  3. Using an SMA, or the 2× volume rule against the breakout day's own average: it is a 20 **EMA** and the volume is compared with the **previous month's** average [p. 12, 33].
