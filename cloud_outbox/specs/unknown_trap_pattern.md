# The Trap Pattern (report: "Why you SHOULD NOT buy shares of Goyal Aluminiums") — Riyank Arora (@RiyankArora_)

- **Source file:** Google Drive "The Trap Pattern.pdf" (5 pages, 1.25 MB, mostly chart images)
- **Text file used:** text/unknown_trap_pattern.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - Before finishing, run `python ../work/bin/verify_citations.py specs/unknown_trap_pattern.md text/unknown_trap_pattern.txt`.
- **Coverage:** Read lines 1-117 of text/unknown_trap_pattern.txt (the entire file), last `[[PAGE N]]` reached = 5. Nothing skimmed. The charts (Goyal Aluminiums, Vishal Fabrics, Steel Exchange of India, GKP Print and Packaging, Gala Global Products) are images and are NOT in the text; the "result below" on page 5 is an image that was not seen, so no outcome numbers for any example can be taken from the text except the ones quoted below.
- **Date (inference):** The document is undated. The latest dated item in the text is the 25 July 2022 tweet on page 4 and the "August 2022" Gala Global example on page 5, and page 5 speaks of the outcome as already known. INFERENCE: the report was written after August 2022, probably in the second half of 2022. The Goyal Aluminiums reference price is CMP 277.15 [p. 1], with no date.

## 1. The method in brief

A short single-author note (author claims 8 years of technical-analysis experience [p. 1]) warning against one Indian small-cap, Goyal Aluminiums, and defining a "trap pattern": a stock climbs like a staircase, about 1 to 2% (or more) every day, with volume mattering, but without consecutive upper circuits; the author claims such stocks then "come down with elevator", leaving no chance to exit, and fall at least 70-75% from the peak [p. 2, 3, 4]. For Goyal Aluminiums the author predicts at least 75% downside from the current price [p. 1].

The evidence presented is four chart examples (Vishal Fabrics Sept 2020, Steel Exchange of India Nov 2017, GKP Print and Packaging Nov 2017, Gala Global Products Aug 2022) shown as images. The only outcome stated in words is "at least 70-75%" crash [p. 4] and "we all know what was supposed to happen afterwards" [p. 5]. There is no backtest, no hit-rate, no count of false positives (stocks that staircased and did not collapse), and no entry/exit rules. Everything below is the author's claim, not a verified result. The note is best used as an AVOID / exit-filter hypothesis for small-cap staircase-rise stocks, and only as a short signal where shorting is possible.

## 2. Strategies

### 2.1 Trap pattern as an AVOID / exit filter (long-side use)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: pattern-based avoid / exit filter (anti-momentum warning). The author's instruction is "do not buy"; the exit part is not stated explicitly and is implied by "you won't be able to get out" | 1 |
| Timeframe & holding period | Daily bars (the pattern is described as a daily move). No holding period stated. Pump duration is unknown: "you don’t know how much the stock will be pumped" | 2, 4 |
| Universe / eligibility filters | Not found in this text (examples are illiquid-looking small caps; no market-cap, price or liquidity filter given) | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Stock moves up as a staircase, "1 to 2% or more, every day". Consecutive upper circuits do NOT qualify. "Volumes are a key too" (no volume rule given) | 2, 3 |
| Entry trigger & order type | No entry (this is an avoid filter). If used as a flag: flag the stock once the staircase condition is met; do not buy | 1 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Implied: exit while the staircase is still rising, because after the fall begins "you won't get exit". No exit trigger is defined | 1, 3 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Daily % gain | 1 to 2% | "1 to 2% or more" (no upper cap stated) | 2, 3 |
| Number of consecutive days | Not stated (ASSUMPTION below) | - | - |
| Lookback / pattern length | Not stated (ASSUMPTION below) | - | - |
| Circuit exclusion | Consecutive upper circuits do not qualify | no band size given | 2, 3 |
| Volume condition | "Volumes are a key too" (no threshold) | - | 2, 3 |
| Expected downside after collapse | At least 70-75% from the peak ("those levels") | Goyal Aluminiums: at least 75% from CMP 277.15 | 1, 4 |
| Examples | Vishal Fabrics (Sept 2020), Steel Exchange of India (Nov 2017), GKP Print and Packaging (Nov 2017), Gala Global Products (Aug 2022), Goyal Aluminiums (undated, CMP 277.15) | - | 1, 2, 3, 4, 5 |

**Examples and reported outcomes (all claims, charts are images not in the text)**

| Example | Date given | Outcome stated in text | Page |
|---|---|---|---|
| Goyal Aluminiums Limited | undated; CMP 277.15 | Prediction only: "at least 75% potential downside" | 1 |
| Vishal Fabrics | September 2020 | Staircase rise 1 to 2% daily; fall not described in text (in chart) | 2 |
| Steel Exchange of India (STEELXIND) | November 2017 | Rises "with stairs", falls "with elevator", no exit; magnitude not given in text | 3 |
| GKP Print and Packaging | chart "November 2017"; tweet dated 25 July 2022 | Generic claim that such stocks crash "at least 70-75%" from the dump levels | 4 |
| Gala Global Products Limited | August 2022 | "we all know what was supposed to happen afterwards"; result is an image | 5 |

Date oddity: page 4 gives the tweet date as 25 July 2022 but the chart period as November 2017, the same month as the Steel Exchange example. This may be a copy error; recorded as stated.

**Key quotes**
- "moving up 1 to 2% every day" [p. 2]
- "the stock moves 1 to 2% or more, every day" [p. 2]
- "Volumes are a key too." [p. 2]
- "comes down with elevator" [p. 3]
- "I am seeing at least 75% potential downside" [p. 1]
- "70-75% from those levels" [p. 4]
- "DO NOT BUY THIS SCRIPT" [p. 1]

**Pseudocode** (daily OHLCV, adjusted; every numeric parameter other than the 1-2% is an ASSUMPTION)
```
params: MIN_G = 0.01; MAX_G = none (or 0.05 as practical cap, ASSUMPTION);
        N = 15 trading days window; K = 12 of N days qualifying (ASSUMPTION);
        VOL_MULT = 1.5; MAXRUN_CIRCUIT = 2 (ASSUMPTION)

for each stock s, each day t:
    ret[d]  = close[d]/close[d-1] - 1                      for d in (t-N+1 .. t)
    up[d]   = ret[d] >= MIN_G                              # "1 to 2% or more"
    circ[d] = (ret[d] >= band_s[d] - 0.001)                # needs band (2/5/10/20%); see section 5
    # exclude circuit-driven runs
    if max consecutive run of circ[d] over window >= MAXRUN_CIRCUIT: not trap
    # staircase: mostly steady small gains, no big single-day spikes
    steady = count(up[d]) >= K and max(ret[d]) <= 0.05 (ASSUMPTION)
    # volume: "key" but unspecified
    vol_ok = mean(volume[t-N+1..t]) >= VOL_MULT * mean(volume[t-N-60..t-N])   # ASSUMPTION
    trap[t] = steady and vol_ok and not circuit-run
    if trap[t]: add s to AVOID list (no new long); if held, exit at next open (ASSUMPTION)
```

**Ambiguities & assumptions**
- Number of days / lookback: not found in this text. ASSUMPTION: window N = 15 trading days with at least 12 daily closes up >= 1%, to be tuned over 10-30 days.
- Upper bound of the daily move: "1 to 2% or more" has no cap. ASSUMPTION: cap single-day gains at 5% to separate a staircase from jump days; test with no cap too.
- Volume: "Volumes are a key too" gives no direction or threshold. ASSUMPTION: rising volume vs prior 60-day average >= 1.5x; also test delivery % where available. The direction (rising vs falling) is itself unknown.
- Circuit exclusion: "Consecutive upper circuits" has no count. ASSUMPTION: two or more consecutive closes at the band limit disqualify the window. Needs the stock's band history, which we probably do not have.
- How long the staircase must run before the stock is a "trap", and what price drop confirms the trap: not found in this text.
- Exit rule for stocks already held: not found in this text. ASSUMPTION: exit next open after the flag.
- Collapse magnitude "at least 70-75%" is a claim; no time frame (days/months) given for the fall.
- No filter against genuine uptrends (the pattern can also describe healthy small caps); false-positive rate not given.

### 2.2 Trap pattern as a short / fade signal (only where shorting exists)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: short / fade after a pump (implied; the author never says "short") | 1, 4 |
| Timeframe & holding period | Not stated. The author expects "at least 75%" downside but gives no time frame | 1 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Same staircase as 2.1: "1 to 2% or more, every day", not consecutive upper circuits, volume matters; then the stock is "DUMPED" | 2, 4 |
| Entry trigger & order type | Not found in this text. The author warns the fall gives no exit ("it will crash"), so a short would have to be entered at or before the dump; the trigger for the dump is not defined | 4 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Target implied: at least 70-75% fall from the peak levels (goal, not an order rule) | 4 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Expected fall | At least 70-75% from the dump level | Goyal: at least 75% from CMP 277.15 | 1, 4 |
| Dump trigger | Not stated | - | - |
| Stop / time stop | Not stated | - | - |

**Key quotes**
- "once the stock is DUMPED" [p. 4]
- "70-75% from those levels" [p. 4]
- "at least 75% potential downside" [p. 1]

**Pseudocode** (research-only; not executable in the NSE cash segment)
```
if trap[t] (from 2.1) and close[t] < max(high[t-N+1..t]) * (1 - DUMP_DD)   # DUMP_DD = 0.20, ASSUMPTION
   and not already short:
       enter short at next open     (only if shorting available: stock futures / intraday MIS)
       target = peak * 0.30         (70% fall, claim)
       stop   = peak (ASSUMPTION)
       time stop = 120 trading days (ASSUMPTION)
```
For backtesting in cash data, use a "paper short" (measure forward returns after the flag) instead of a tradable short.

**Ambiguities & assumptions**
- The author never states a short, entry trigger, stop or timeframe. All of that is ASSUMPTION.
- The text says the fall gives no exit, which also implies a short may be hit by circuit-limited (lower-circuit) days; fills may be impossible. ASSUMPTION: model gap-down fills at the next available price and add extra slippage.
- Whether the 70-75% is measured from the peak or from the price when the dump starts: "from those levels" is ambiguous. ASSUMPTION: measure from the highest close of the staircase.

## 3. Risk & money-management rules

Not found in this text beyond the warning not to buy and the claim that there is "no exit" once the fall starts [p. 1, 3]. No position size, stop or portfolio rule is given.

## 4. Non-codable guidance

- The author treats the call as chart-reading judgment ("price action and candlestick patterns") built on 8 years of experience [p. 1].
- Spotting the pattern is discretionary: the volume condition ("Volumes are a key too") and whether a staircase is "similar" are judged visually [p. 2, 5].
- "you don’t know how much the stock will be pumped" -> the author accepts that the top cannot be timed [p. 4].

## 5. Adapting to NSE (Indian equities)

- **Data required:** daily OHLCV (close-to-close % change, volume); delivery % for recent years (useful volume-quality proxy); per-stock circuit band (2/5/10/20%) history; optionally NIFTYBEES for a market regime check.
- **Testability with our data:** A forward-return study (event study) after the flag is fully testable on 2005-2026 daily prices including delisted stocks, which matters because trap stocks are often delisted or suspended. Circuit-hit detection is the weak point: the daily OHLC shows only the move, not the band, and the band changed over time and differs per stock (2/5/10/20%). We probably do not have the historical band, so circuit days can only be approximated (for example, close == high and return near a standard band value, or an identical open/high/low/close with low volume). Fundamentals are not needed. The Goyal Aluminiums prediction itself (CMP 277.15, 75% fall) cannot be verified from this text because the date is missing; it could be matched by finding the date when the close was 277.15 (ASSUMPTION: date after Aug 2022).
- **Market-structure differences:**
  - NSE cash has no overnight shorting, and these small caps are generally not in the F&O segment. So 2.2 is not tradable; use 2.1 as an avoid / exit filter, or measure the fall as an event study. ASSUMPTION: treat 2.2 as a paper short only.
  - Circuit limits mean the "no exit" claim is plausible (lower circuits lock sellers out). In a backtest, ASSUMPTION: if a stock closes at the lower band, the next-day exit fill is unavailable; assume exit at the following day's open with extra slippage.
  - ASM/GSM surveillance flags, trade-for-trade settlement and price-band cuts (often 5% or 2%) were introduced to curb such pumps; the pattern may behave differently by period. ASSUMPTION: evaluate pre-2018 and post-2018 separately.
  - Costs: STT, brokerage and about 0.1% slippage; for illiquid small caps use higher slippage (ASSUMPTION: 0.5-1%).
  - Liquidity: add a minimum traded value filter (ASSUMPTION) so tests are not dominated by untradeable days.

## 6. Verdict

- **Codeability:** Partly. The core rule (daily gain of 1-2% or more, no consecutive upper circuits, volume matters) is codable only after inventing the number of days, window and volume threshold; the circuit band is not in our data.
- **Priority for backtesting:** Low-Medium. Single-author forecast, no backtest, no parameters; but a cheap event study of "staircase then collapse" could be a useful avoid filter for a momentum portfolio.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the pattern as precisely defined: window length, count of up-days and volume rule are all invented (marked ASSUMPTION); results will depend heavily on them.
  2. Ignoring the circuit exclusion, or detecting it wrongly without the band history, so circuit-driven runs get mixed in with staircase runs.
  3. Survivorship / lookahead and fill realism: measuring the 70-75% fall from the peak (known only in hindsight) and assuming you can sell at the close of a lower-circuit day, or treating a short as tradable in NSE cash.
