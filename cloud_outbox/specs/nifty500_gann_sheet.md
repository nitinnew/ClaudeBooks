# Copy of NIFTY 500 GANN (Google Sheet) — author not stated

- **Source file:** Google Drive invest/"Copy of NIFTY 500 GANN" (Google Sheet, 2 worksheets: "Nifty500" and "Historical DATA")
- **Text file used:** text/nifty500_gann_sheet.txt  (page basis: sheets, one [[PAGE N]] per worksheet; the coordinator exported the sheet as .xlsx and dumped every non-empty cell as "CELL =formula | cached value")
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file. Here p. 1 = worksheet "Nifty500", p. 2 = worksheet "Historical DATA". Cell references (e.g. X6) are always within the sheet of the cited page. GOOGLEFINANCE formulas appear wrapped as IFERROR(__xludf.DUMMYFUNCTION("..."), cached value). Date serials are Excel day numbers (44545 = 15 Dec 2021).
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage.
- **Coverage:** Read lines 1-579 (the whole file) and reached the last marker, [[PAGE 2]]. Page basis is "sheets". Sheet 1 ("Nifty500") is dumped cell by cell only for rows 1-11; rows 12-504 (the rest of the Nifty 500 stocks) are summarised by the coordinator in one note [p. 1], not dumped cell by cell, so I rely on that note for the claim that they repeat the same formula pattern. Sheet 2 ("Historical DATA") is dumped in full. Nothing was garbled or skimmed. The sheet has no prose: no explanatory text, author, or trade commentary. Reading done by a Sonnet sub-agent. Text preparation by the coordinator: the Google Sheet was exported as .xlsx and every non-empty cell dumped with its formula and cached value (a CSV export showed only #N/A because the cells depend on live GOOGLEFINANCE calls). Because verify_citations.py recognises only 4 of the cell-line quotes, the coordinator ran its own exact-page check on all 36 quoted cell lines (36 ok, 0 wrong page, 0 not found; appended to the verify log) and re-computed the M15 average (1.0219 with the five zero cells, 1.1981 without), confirming the sub-agent's finding.

## 1. The method in brief

This is a spreadsheet, not a book, and it states no philosophy or evidence. It does two things. (a) It builds a "Gann square-root" grid for each Nifty 500 stock and the two indices: take the all-time high (ATH) fetched from GOOGLEFINANCE since 01/12/1980, take its square root, and split that root into eighths with column labels 45d 1/8, 90d 1/4, 120d/1/3, 135d 3/8, 180d 1/2, 225d 5/8, 270d 3/4, 315d 7/8 and "1 GANN" (360 degrees) [p. 1]. The values are in price units, so for Nifty ATH 26373.2 the root is 162.398 and 1/8 of it is 20.30 [p. 1]. A column "3 punch Between Following points" points at the 3/4 and 7/8 levels, and a "Dynamic high low" column points at one of the fractions (1/3 for NIFTY and BANK NIFTY, 1/8 for the stocks shown) [p. 1].

(b) Under the heading "Futures Trading with Dynamic High/Low" it gives a fixed-point-offset rule block for NIFTY and BANK NIFTY futures: the user types a "dynamic high" or "dynamic low" price into an "Enter Data" cell and the sheet returns Get Ready, Entry, Stop and Target levels as constant point offsets from it [p. 1]. The same block is repeated on the second sheet, which also lists 28 daily Nifty bars (15 Dec 2021 to about 18 Jan 2022 by the serials), the daily High-Low range, and that range divided by SQRT(ATH) as "No. of GANN" [p. 2]. The sheet never says how the dynamic high/low is chosen, the chart timeframe, the holding period, position size, or any track record. Everything below that is not a literal formula is marked `ASSUMPTION:`.

## 2. Strategies

Four items are captured: 2.1 Nifty dynamic-high/low futures levels, 2.2 Bank Nifty variant (separate subsection because the offsets differ and the stop cell is hard-coded), 2.3 per-stock Gann square-root fraction grid, 2.4 daily range in GANN units (a diagnostic, no trade rule). 2.1/2.2 share the same structure but are kept separate because their parameters differ.

### 2.1 Nifty "Dynamic High/Low" futures levels (NIFTY block)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: fixed-offset reversal/pullback levels around a user-chosen swing extreme (the sheet gives levels only; direction is implied by "High" vs "Low" rows). | 1 |
| Timeframe & holding period | Not found in this text. The title says "Futures Trading", so Nifty futures are implied. | - |
| Universe / eligibility filters | NIFTY (index futures), one instrument. | 1 |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | User enters a dynamic HIGH price (row "High") or dynamic LOW price (row "Low") in the "Enter Data" cell (W6 for High, W7 for Low). How the dynamic high/low is picked is not stated. | 1 |
| Entry trigger & order type | High row: Get Ready = H - 45; Entry = Get Ready + 25 = H - 20. Low row: Get Ready = L + 45; Entry = Get Ready - 25 = L + 20. Order type not stated. The sheet does not say what price action must happen between Get Ready and Entry. | 1 |
| Initial stop-loss | High row: Stop = H + 5. Low row: Stop = L - 5 (i.e. 5 points beyond the entered extreme). | 1 |
| Exits: profit-taking | Target = Entry - 45 (High row, so H - 65); Target = Entry + 45 (Low row, so L + 65). | 1 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Get-ready offset from dynamic extreme (Nifty) | 45 points (High: -45, Low: +45) | none | 1 |
| Entry offset from Get Ready (Nifty) | 25 points (High: +25, Low: -25), i.e. 20 points from the extreme | none | 1 |
| Stop offset from dynamic extreme (Nifty) | 5 points beyond (High: +5, Low: -5) | none | 1 |
| Target offset from Entry (Nifty) | 45 points (High: -45, Low: +45) | none | 1 |
| Dynamic high/low definition | Not found in this text (manual input) | - | - |
| Timeframe | Not found in this text | - | - |
| Position size | Not found in this text | - | - |

**Key quotes**
- "V4  | Futures Trading with Dynamic High/Low" [p. 1]
- "X6 =W6-45 | -45" [p. 1]
- "Y6 =X6+25 | -20" [p. 1]
- "Z6 =W6+5 | 5" [p. 1]
- "AA6 =Y6-45 | -65" [p. 1]
- "X7 =W7+45 | 45" [p. 1]
- "Y7 =X7-25 | 20" [p. 1]
- "Z7 =W7-5 | -5" [p. 1]
- "AA7 =Y7+45 | 65" [p. 1]
- The same block is duplicated at the sheet-2 cells "R7 =Q7-45 | -45" and "U8 =S8+45 | 65" [p. 2]. The cached values (-45, -20, 5, -65 and 45, 20, -5, 65) are the offsets because the Enter Data cells W6/W7 (Q7/Q8 on sheet 2) are empty.

**Pseudocode**

```
# inputs: H (dynamic high) or L (dynamic low), price in index points
if side == "HIGH":                # sheet row 6
    get_ready = H - 45
    entry     = get_ready + 25    # = H - 20
    stop      = H + 5
    target    = entry - 45        # = H - 65
    # implied direction: SHORT (stop above H, target below entry)  [ASSUMPTION]
if side == "LOW":                 # sheet row 7
    get_ready = L + 45
    entry     = get_ready - 25    # = L + 20
    stop      = L - 5
    target    = entry + 45        # = L + 65
    # implied direction: LONG       [ASSUMPTION]
# risk = 25 points (entry-to-stop), reward = 45 points -> R:R = 1.8
```

**Ambiguities & assumptions**
- Direction is not stated. Because the stop is beyond the extreme and the target is further from it, the levels only make sense as SHORT after a dynamic high and LONG after a dynamic low. `ASSUMPTION:` HIGH row = short, LOW row = long.
- Role of "Get Ready" is not stated. Note Entry (H-20) is ABOVE Get Ready (H-45) on the High row, so Get Ready is an extreme in the move away from the high and Entry is a bounce back toward it (25 points). `ASSUMPTION:` the setup is armed once price has travelled at least 45 points away from the extreme (Get Ready touched), then the trade enters when price retraces 25 points back toward the extreme to H-20 (a sell-the-bounce on the High row, mirrored for the Low row). Alternative literal reading: Get Ready is just an alert level with no trigger role; the entry is at the Entry level whenever touched.
- How the dynamic high/low is selected (swing definition, lookback, intraday vs daily) is not found in this text. `ASSUMPTION:` the dynamic high/low is the highest high / lowest low of the prior N=20 daily bars, updated each day; test N in {5, 10, 20}. This is our invention, not the sheet's.
- Timeframe not stated. Offsets of 45/25/5 points on a ~17,000 to 26,000 index are very small (0.1-0.3%), which fits an intraday timeframe, not daily bars. `ASSUMPTION:` intraday intent; on daily bars the rule cannot be tested faithfully (see section 5).
- Order of Entry/Stop/Target within one daily bar is unknowable on OHLC data. `ASSUMPTION:` if a bar touches both stop and target, count the stop first (worst case); if it touches the entry and the target but not the stop, fill at entry and take the target only if the bar's open is not beyond entry (otherwise use the open as the fill).
- Stop is expressed as 5 points beyond the extreme, tighter than the entry (25 points risk from entry). If the extreme is exceeded by more than 5 points the setup is invalidated; no re-entry rule is given.
- Cost/slippage is not modelled in the sheet; at 25 points risk, brokerage and slippage matter.

### 2.2 Bank Nifty "Dynamic High/Low" futures levels (BANK NIFTY block)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: same fixed-offset pullback/reversal structure as 2.1 with larger offsets. | 1 |
| Timeframe & holding period | Not found in this text. | - |
| Universe / eligibility filters | BANK NIFTY (index futures). | 1 |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | User enters a dynamic HIGH (row "High", W10) or dynamic LOW (row "Low", W11). Selection of the extreme is not stated. | 1 |
| Entry trigger & order type | High row: Get Ready = H - 68; Entry = Get Ready + 35 = H - 33. Low row: Get Ready = L + 68; Entry = Get Ready - 35 = L + 33. Order type not stated. | 1 |
| Initial stop-loss | The Stop cells hold the constants 10 (High row, Z10) and -10 (Low row, Z11), NOT a formula off the entered extreme. Intended meaning (stop 10 points beyond the extreme, H + 10 / L - 10) is an inference. | 1 |
| Exits: profit-taking | Target = Entry - 45 (High row: H - 78); Target = Entry + 45 (Low row: L + 78). | 1 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Get-ready offset (Bank Nifty) | 68 points | none | 1 |
| Entry offset from Get Ready (Bank Nifty) | 35 points (entry 33 from extreme) | none | 1 |
| Stop value (Bank Nifty) | constant 10 (High) / -10 (Low) | none | 1 |
| Target offset from Entry (Bank Nifty) | 45 points (same as Nifty) | none | 1 |
| Dynamic high/low definition, timeframe, size | Not found in this text | - | - |

**Key quotes**
- "X10 =W10-68 | -68" [p. 1]
- "Y10 =X10+35 | -33" [p. 1]
- "Z10  | 10.0" [p. 1]
- "AA10 =Y10-45 | -78" [p. 1]
- "X11 =W11+68 | 68" [p. 1]
- "Y11 =X11-35 | 33" [p. 1]
- "Z11  | -10.0" [p. 1]
- "AA11 =Y11+45 | 78" [p. 1]
- Sheet 2 duplicate: "T11  | 10.0" and "U12 =S12+45 | 78" [p. 2]

**Pseudocode**

```
if side == "HIGH":                # sheet row 10
    get_ready = H - 68
    entry     = get_ready + 35    # = H - 33
    stop      = H + 10            # sheet stores literal 10 (see ambiguity)
    target    = entry - 45        # = H - 78
if side == "LOW":                 # sheet row 11
    get_ready = L + 68
    entry     = get_ready - 35    # = L + 33
    stop      = L - 10            # sheet stores literal -10
    target    = entry + 45        # = L + 78
# risk = 43 points (entry to H+10), reward = 45 -> R:R about 1.05  [if stop = extreme +/- 10]
```

**Ambiguities & assumptions**
- Stop cell: Z10 and Z11 are hard-coded numbers, whereas the Nifty block uses =W6+5 and =W7-5. Read literally, the stop is the price 10 (or -10), which is meaningless on an index near 50,000+. `ASSUMPTION:` it is an incomplete formula and the intent is extreme +/- 10 points, by analogy with the Nifty block. With that, risk is 43 and reward 45 (R:R about 1.05); if instead the stop is 10 points from entry, R:R is 4.5. Test both.
- All other ambiguities (direction, Get-Ready role, dynamic extreme definition, timeframe, intraday ordering) are identical to 2.1 and take the same `ASSUMPTION:` defaults. The target offset of 45 is not scaled to the larger Bank Nifty offsets in the sheet.
- Bank Nifty values are about 2.3 times Nifty's (ATH 61764.85 vs 26373.2 [p. 1]); offsets of 68/35 are therefore about 0.1% of the price, comparable to Nifty's.

### 2.3 Per-stock Gann square-root fraction grid (support/resistance levels)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: static level grid (support/resistance); no trade rule is given. | 1 |
| Timeframe & holding period | Not found in this text. | - |
| Universe / eligibility filters | Nifty 500 constituents plus NIFTY_50 and NIFTY_Bank; sheet rows 12-504 repeat the same formula pattern (coordinator note). | 1 |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | Per stock: ATL = MIN of GOOGLEFINANCE daily LOW since 01/12/1980; ATH = MAX of daily HIGH since 01/12/1980; SQRT = SQRT(ATH); levels = SQRT x {1/8, 1/4, 1/3, 3/8, 1/2, 5/8, 3/4, 7/8, 1}. A column "3 punch Between Following points" references the 3/4 and 7/8 levels; "Dynamic high low" references the 1/3 level (indices) or 1/8 level (stocks). | 1 |
| Entry trigger & order type | Not found in this text. A "CURRENT PRICE" column (U1) exists but the dump shows no formula for it in rows 1-11. | 1 |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| ATH lookback start | 01/12/1980 (GOOGLEFINANCE, daily, to TODAY()) | none | 1 |
| Fractions of SQRT(ATH) | 1/8, 1/4, 1/3, 3/8, 1/2, 5/8, 3/4, 7/8, 1 (labelled 45d, 90d, 120d, 135d, 180d, 225d, 270d, 315d, 360d) | none | 1 |
| "3 punch" levels | 3/4 and 7/8 of SQRT (column R = O, S = P value) | none | 1 |
| "Dynamic high low" column | Indices: 1/3 level (T2 =K2); stocks shown: 1/8 level (T4 =I4) | none | 1 |
| Units | Levels are in the same units as the SQRT of price (rupees^0.5 scaled values), e.g. Nifty 1 GANN = 162.398 | - | 1 |

**Key quotes**
- "H2 =SQRT(G2) | 162.3982759" [p. 1]
- "I2 =H2/8 | 20.29978448" [p. 1]
- "K2 =H2/3 | 54.13275862" [p. 1]
- "L2 =H2*3/8 | 60.89935344" [p. 1]
- "N2 =H2*5/8 | 101.4989224" [p. 1]
- "Q2 =H2 | 162.3982759" [p. 1]
- "R1  | 3 punch Between Following points" [p. 1]
- "R2 =O2 | 121.7987069" [p. 1]
- "T2 =K2 | 54.13275862" [p. 1]
- "T4 =I4 | 25.26623859" [p. 1]
- "MAX(INDEX(GOOGLEFINANCE(C2, ""high"", ""01/12/1980"", TODAY(), 7), , 2))" [p. 1]
- Sheet 2 repeats the Nifty grid with a HIGH row (levels = E5 - fraction) and a LOW row (levels = E6 + fraction): "F5 =E5-F4 | -20.29978448" and "F6 =E6+F4 | 20.29978448" under the label "Q4  | Type Dynamic High / low" [p. 2]

**Pseudocode**

```
# per stock, per date t:
ATH_t = max(High[0..t])                 # ATH over available history (sheet: since 1980 via GOOGLEFINANCE)
ATL_t = min(Low[0..t])
R     = sqrt(ATH_t)
for f in [1/8, 1/4, 1/3, 3/8, 1/2, 5/8, 3/4, 7/8, 1]:
    step_f = R * f                      # a DISTANCE in price units, not a price
# Sheet-2 usage with an anchor price A (dynamic high or low):
#   from a dynamic HIGH:  level_f = A - step_f   (support grid below the high)
#   from a dynamic LOW :  level_f = A + step_f   (resistance grid above the low)
# Stock-sheet usage: steps listed per stock; how they are compared with CURRENT PRICE is not given.
# Trade rule: NOT in the sheet.
# ASSUMPTION (test only): treat (A +/- step_f) as S/R; long on a close above a level reached from below
#   by +1 step, exit at the next step; stop one step_1/8 below the entry level. Mark as our invention.
```

**Ambiguities & assumptions**
- The levels are distances (root of price scaled by fraction), not prices. On the stock sheet they are only meaningful if added to / subtracted from an anchor (as on sheet 2), but the stock rows contain no anchor column in rows 1-11 [p. 1]. `ASSUMPTION:` the anchor is a swing high or low chosen by the user, as in sheet 2.
- ATH source differs from ours: the sheet uses GOOGLEFINANCE since 1980 [p. 1]; our data starts in 2005, so for stocks whose true high was before 2005 the ATH (and all levels) will differ. Also the sheet's ATH is the cached live value on the day of export (Nifty 26373.2); the ATH changes with time, so levels must be recomputed daily or at a fixed schedule in a backtest to avoid look-ahead (use only data up to t).
- The `R` and `S` columns "3 punch" label has no explanation. `ASSUMPTION:` it marks the 3/4 and 7/8 steps as the strongest zone.
- Several cells are hard-coded or inconsistent in the Bank Nifty row (H3-Q3 are values, not formulas, T3 is a value) and column T differs between rows (1/3 for indices, 1/8 for stocks). Treat T as a per-row picked step, not a rule.
- Some ATL/ATH lookups return errors (F7 "#N/A" for ACC [p. 1]); the coordinator note says 442 of the rows have cached numeric SQRT, so about 58 rows have no value.

### 2.4 Daily range in GANN units ("No. of GANN") — diagnostic

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: volatility/range measure, not a trade system. | 2 |
| Timeframe & holding period | Daily bars of NIFTY_50, fetched with start date C8 = 44545 (15 Dec 2021) and end date C9 = 44584 (23 Jan 2022); 28 daily rows are listed. | 2 |
| Universe / eligibility filters | NIFTY_50 only (ticker cell C10). | 2 |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | High minus Low (J) divided by SQRT(ATH) (E4); average of the column (M15). | 2 |
| Entry trigger & order type | Not found in this text. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Range unit | SQRT(ATH of Nifty) = 162.398 | none | 2 |
| Sample | 28 daily bars 15 Dec 2021 onward, plus today's live bar (row 47) | none | 2 |
| Average "Gann" | M15 = AVERAGE(K13:K47) = 1.02188 | none | 2 |

**Key quotes**
- "J13 =D13-E13 | 159" [p. 2]
- "K13 =J13/$E$4 | 0.9790744339" [p. 2]
- "M15 =AVERAGE(K13:K47) | 1.02187951" [p. 2]
- "C8  | 44545.0" [p. 2]

**Pseudocode**

```
gann_unit = sqrt(ATH_nifty)
for each day: n_gann = (High - Low) / gann_unit
avg_gann = mean(n_gann over window)
```

**Ambiguities & assumptions**
- The average range M15 includes the five zero cells K41:K45, which are not data (J41:K45 = 0), and today's live bar K47, so it averages 34 cells. The mean of the 28 real days is about 1.19 (my recomputation from the dumped K13:K40), not 1.02. This is likely an error in the sheet, not intended.
- Interpretation: one "GANN" is about one typical daily Nifty range in December 2021 to January 2022, so the sheet may be suggesting that a day's range is roughly one square-root unit. No rule is attached. `ASSUMPTION:` use only as a descriptive stat; the same measure on a stock panel is ATR-like scaling by sqrt(ATH).
- Dates: the serial values have a 0.64583 fraction (15:30 IST) [p. 2], meaning each row is the daily bar stamped at close time.

## 3. Risk & money-management rules

- Only implied risk per trade, in points, from the sheet's offsets: Nifty entry-to-stop 25 points vs 45 target (R:R 1.8) [p. 1]; Bank Nifty entry-to-stop about 43 points if the stop is extreme + 10, vs 45 target (R:R about 1.05) [p. 1]. The Bank Nifty stop cells are literal constants [p. 1].
- Not found in this text: risk per trade, position size, lots, max exposure, drawdown rules, number of concurrent trades.

## 4. Non-codable guidance

- The choice of the "dynamic high" and "dynamic low" is manual (the user types it into "Enter Data") [p. 1].
- No psychology or discipline guidance is in the sheet; no prose at all.

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily OHLC (High, Low, Close) for each stock for the ATH/ATL grid; Nifty / Bank Nifty index High, Low for the 2.1/2.2 levels. Intraday data and futures prices for faithful testing of 2.1/2.2. Volume not needed (the sheet shows 0 volume for the index [p. 2]).
- **Testability with our data:**
  - 2.3 (per-stock grid): can be computed on our 2005-2026 daily panel. Our ATH comes from our own history from 2005 and will differ from the sheet's GOOGLEFINANCE since-1980 ATH [p. 1]; compute ATH as a running maximum of High up to the prior day to avoid look-ahead. Because the sheet states no trade rule, any backtest is our own rule (`ASSUMPTION:`) and cannot be called a test of the sheet's method.
  - 2.1/2.2 (futures points offsets): the offsets (45/25/5 points; 68/35/10 points) are tiny (about 0.1-0.3% of the index) and intended for futures, likely intraday. We have no futures data and Nifty index history only from 2024; before that only NIFTYBEES, whose price (about 1/100 of Nifty) means points offsets do not transfer. `ASSUMPTION:` to approximate on NIFTYBEES, convert offsets to percent of the index level at the time (e.g. 45/17,000 = 0.26%) and apply to ETF price; this is a different, scaled rule.
  - On daily OHLC bars the order of Get Ready / Entry / Stop / Target touches inside a day is ambiguous. `ASSUMPTION:` Get Ready, Entry, Stop and Target can be evaluated only in the sequence required (Get Ready first, then Entry), bar by bar, with at most one state change per bar to be conservative: arm on bar t, enter from bar t+1; on a bar touching both stop and target, take the stop.
  - 2.4: computable on index history from 2024 or on NIFTYBEES with sqrt(ATH) scaling; low value.
- **Market-structure differences:**
  - Index futures levels are in points; our cash-market universe cannot short overnight. `ASSUMPTION:` test only the LOW (long) rows in the cash market and treat the HIGH (short) rows as signals to exit/avoid. Futures shorts cannot be tested with our data.
  - Circuit limits, STT, brokerage and about 0.1% slippage: a 25-point Nifty trade is about 0.15% of price, so costs of roughly 0.1% per side would remove most of the edge in a naive test.
  - Corporate actions: our prices are split/bonus-adjusted; GOOGLEFINANCE since 1980 may give unadjusted highs (for example 3M India ATH 40856.5 [p. 1]); use adjusted highs.

## 6. Verdict

- **Codeability:** Partly. The level formulas (offsets and sqrt fractions) are fully specified and trivial to code, but the sheet gives no definition of the dynamic high/low, direction, timeframe, order of triggers, stop for Bank Nifty, or position size, so no complete trading system can be coded without our own assumptions.
- **Priority for backtesting:** Low. No stated edge or evidence; futures/intraday-based; our data cannot test it directly; the per-stock grid has no trade rule.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the Gann fractions as prices rather than distances (SQRT(ATH) x fraction is added to or subtracted from an anchor), and using a since-1980 or look-ahead ATH instead of a running ATH from our own data.
  2. Taking the Bank Nifty stop literally (a fixed 10/-10 price) instead of recognising the hard-coded cell, and mis-ordering Get Ready (H-45/H-68) vs Entry (H-20/H-33) so that entry sits between the get-ready and the extreme, not beyond it.
  3. Applying the point offsets to NIFTYBEES or daily bars and assuming intraday trigger ordering; the offsets are about 0.1-0.3% and only meaningful on index futures intraday.
