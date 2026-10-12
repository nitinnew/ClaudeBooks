# Indicator code bundle — TTM Squeeze clone (LazyBear), "ALL PURPOSE INDICATORS" (PTRS CPR & Camarilla), "BB with SD" (VMST Bollinger x3 + anchored BNF VWAP), "VWAP with SD BANDS" (VMST), vkcash watchlist — LazyBear (p. 1), Prasanna (p. 2), madhavbbs (pp. 3-4)

- **Source file:** Google Drive invest/: "TTM squeeze clone [LazyBear].txt", "Copy of ALL PURPOSE INDICATORS", "Copy of BB with SD", "Copy of VWAP with SD BANDS", "vkcash (7).txt"
- **Text file used:** text/indicator_code_notes.txt  (page basis: files, one [[PAGE N]] per source file). NOTE: these are TradingView Pine Script INDICATORS, not written strategies. The coordinator assembled the text: p. 1 = TTM squeeze (full script); p. 2 = PTRS CPR & Camarilla (inputs and all calculations verbatim; label/plot styling omitted; the "tomorrow" CPR/Camarilla blocks are summarised because they repeat the same formulas on the current HTF bar); p. 3 = VMST BB x3 + anchored Bank Nifty VWAP (calculations verbatim, UI code omitted); p. 4 = VMST VWAP + SD bands (calculations verbatim, UI code omitted); p. 5 = vkcash, a watchlist only, no rules.
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (here: one marker per source file, not a PDF page).
- **Coverage:** Read all 241 lines of the text file as first assembled (line 1 to the last line; the file is now 250 lines after the coordinator restored the definition lines noted below); last marker reached = [[PAGE 5]]; page basis = files (one [[PAGE N]] per source file). Nothing skimmed. Omitted by the coordinator, per the file headers: p. 2 label-drawing blocks (Round_it helper, label.new/label.delete) and plot()/fill() styling lines, and the "tomorrow" r11-r41/s11-s41/H11-H61/L11-L61 formulas (summarised as repeats of the current-bar formulas); pp. 3-4 watermark-table block, Round_it helper, label.new/label.delete lines and other UI code; p. 5 the several hundred watchlist symbols (only first and last symbols are shown). Reading done by a Sonnet sub-agent. The coordinator assembled the text from the five Drive files (Drive text view; UI-only code left out as stated in each page header), then restored four definition lines it had first left out (`islast` on p. 2; `fn_s1`, `before_time_range`/`start_time_range`, and the `sopen`/`avwap` plot lines on p. 3) and corrected the two spec bullets that had called them missing. Verifier and exact-page check re-run after the fix.

## 1. The method in brief

This bundle contains no written trading method. It is five files from a Drive "invest" folder: four TradingView Pine Script indicators and one watchlist. The indicators are (1) LazyBear's Squeeze Momentum clone: Bollinger Bands (20, 2.0) vs Keltner Channels (20, 1.5 x SMA of true range) with a linear-regression momentum histogram [p. 1]; (2) Prasanna's "PTRS CPR & Camarilla_Profess" all-purpose overlay: Central Pivot Range, classic pivots R1-R4/S1-S4, Camarilla H1-H6/L1-L6, previous high/low, price-action bar colouring, swing pivots, Bollinger, Trend Magic, SuperTrend, boring candles and four MAs [p. 2]; (3) madhavbbs "VMST BBx3": Bollinger 20 with 1/2/3 SD plus a Bank Nifty anchored VWAP built from futures volume or bank-stock weighted volume [p. 3]; (4) madhavbbs "VMST VWAP + StdDev Bands": VWAP +/- 1/2/3 x stdev(close, 34) [p. 4]. The watchlist [p. 5] is a symbol list with no rules.

The files contain no entry, exit, stop, sizing, timeframe or universe rules and no performance claims. The only signal-like definitions are squeeze on/off and the momentum histogram colour [p. 1], close outside the 3 SD band [p. 3], and the price-action bar colour conditions [p. 2]. Everything beyond that in Section 2 is clearly marked `ASSUMPTION:` and is not from the text.

## 2. Strategies

Each subsection below describes an indicator with its exact formula and parameters. None is a strategy as written; the "most common way to turn it into a signal" is always marked `ASSUMPTION:`.

### 2.1 Squeeze Momentum Indicator (LazyBear TTM-squeeze clone)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Volatility-compression / breakout indicator (squeeze state + momentum histogram). No trade rule in the text. | 1 |
| Timeframe & holding period | Not found in this text (script is timeframe-agnostic, `overlay=false` sub-pane). | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | Squeeze ON when both Bollinger bands are inside the Keltner channel: `lowerBB > lowerKC` and `upperBB < upperKC`. Squeeze OFF when both are outside. Otherwise "no squeeze". | 1 |
| Entry trigger & order type | Not found in this text. The histogram `val` is coloured lime (>0 and rising), green (>0 and falling), red (<0 and falling), maroon (<0 and rising); the zero-line cross is black when squeeze ON, blue when no squeeze, gray when squeeze OFF. ASSUMPTION: entry = first bar where squeeze goes OFF after at least one ON bar, long if `val > 0` (and rising), short if `val < 0` (and falling); market order at next open. | 1 |
| Initial stop-loss | Not found in this text. ASSUMPTION: for longs, the lower Keltner band (or the lowest low of the last 20 bars) at entry. | - |
| Exits: profit-taking | Not found in this text. | - |
| Exits: trailing / time / signal | Not found in this text. ASSUMPTION: exit longs when the histogram colour turns from lime to green (momentum stops rising) or `val` crosses below 0. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| BB Length (`length`) | 20 | none | 1 |
| BB MultFactor (`mult`) | 2.0 | none; v2 changelog says the multiplier was previously stuck at 1.5 | 1 |
| KC Length (`lengthKC`) | 20 | none | 1 |
| KC MultFactor (`multKC`) | 1.5 | none | 1 |
| Use TrueRange (KC) | true (else high - low) | boolean toggle | 1 |
| Source | close | none | 1 |
| Momentum linreg length / offset | lengthKC (20) / 0 | none | 1 |

**Key quotes**

- "v2 - fixed a typo, where BB multipler was always stuck at 1.5." [p. 1]
- "sqzOn = (lowerBB > lowerKC) and (upperBB < upperKC)" [p. 1]
- "sqzOff = (lowerBB < lowerKC) and (upperBB > upperKC)" [p. 1]
- "range = useTrueRange ? tr : (high - low)" [p. 1]
- "upperKC = ma + rangema * multKC" [p. 1]
- "val = linreg(source - avg(avg(highest(high, lengthKC), lowest(low, lengthKC)),sma(close,lengthKC)), lengthKC,0)" [p. 1]
- "bcolor = iff( val > 0, iff( val > nz(val[1]), lime, green), iff( val < nz(val[1]), red, maroon))" [p. 1]

**Pseudocode** (fields: open, high, low, close)

```
basis   = SMA(close, 20);  dev = 2.0 * STDEV(close, 20)   # population stdev as in Pine
upperBB = basis + dev;     lowerBB = basis - dev
ma      = SMA(close, 20)
tr      = max(high-low, abs(high-close[1]), abs(low-close[1]))
rangema = SMA(tr, 20)
upperKC = ma + 1.5*rangema; lowerKC = ma - 1.5*rangema
sqzOn   = lowerBB > lowerKC and upperBB < upperKC
sqzOff  = lowerBB < lowerKC and upperBB > upperKC
noSqz   = not sqzOn and not sqzOff
mid     = ( (HIGHEST(high,20)+LOWEST(low,20))/2 + SMA(close,20) ) / 2
val     = LINREG_endpoint( close - mid, 20 )          # value of the 20-bar least-squares line at the current bar (offset 0)
colour  = val>0 ? (val>val[1] ? lime : green) : (val<val[1] ? red : maroon)
# ASSUMPTION (not from text): long signal on bar t if sqzOn[t-1] and sqzOff[t] and val[t]>0 and val[t]>val[t-1]; exit when val < val[t-1] or val<0
```

**Ambiguities & assumptions**
- The text defines the indicator only; no signal. ASSUMPTION: the "squeeze fire" (ON -> OFF transition) with momentum sign as direction is the standard use; thresholds and exits above are unvalidated.
- `noSqz` is true when the bands touch exactly or one band is inside and the other outside; Pine's strict `>`/`<` is reproduced as is [p. 1].
- `val[1]` uses `nz()`, so on the first bar the previous value is 0 [p. 1]; a port should handle warm-up (first ~20 bars) explicitly.
- The script is old Pine (no `//@version`, `iff`, `type=bool`, `avg`); `linreg(x, n, 0)` returns the regression-line value at the latest bar. A port must replicate that exactly (not the slope).
- Stdev in Pine is the population standard deviation (ddof 0); pandas' default `std` is ddof 1 and will give slightly different bands. ASSUMPTION: use ddof 0.

### 2.2 PTRS CPR, pivots, Camarilla and all-purpose overlay (Prasanna)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Support/resistance level toolkit plus bar-pattern and trend overlays (other). No trade rule in the text. | 2 |
| Timeframe & holding period | Levels are computed from a higher timeframe (HTF) bar; "User Defined" default `'D'`, or "Auto" mapping (1m->30m, 3m->60m, 5m->240m, 15m to 240m->D, D->W, else 5W). Holding period not found in this text. | 2 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | Levels from the previous HTF bar's H, L, C: CPR (pivot, bc, tc), R1-R4, S1-S4, Camarilla H1-H6 / L1-L6, PDH/PDL. Bar colouring: dark cloud, bearish engulfing, bullish engulfing (definitions in quotes below). Optional overlays: swing pivots (period 10), Bollinger (20, 2.0), Trend Magic (CCI 20, ATR 1, mult 5), SuperTrend (factor 3, ATR 10), boring candles (body <= 50% of range), MAs 9/13/50/100. | 2 |
| Entry trigger & order type | Not found in this text. ASSUMPTION: commonly, long on a close above H3/H4 (breakout) or a bounce at L3 (reversal), and short on the mirror; or long when price is above a "narrow" CPR with SuperTrend = 1. None is tested or defined here. | - |
| Initial stop-loss | Not found in this text. ASSUMPTION: beyond the next Camarilla level (e.g. L4 for a long at L3). | - |
| Exits: profit-taking | Not found in this text. ASSUMPTION: next pivot/Camarilla level (pivot, R1, H3...). | - |
| Exits: trailing / time / signal | Not found in this text. The SuperTrend line `Tsl` and Trend Magic line `x` are defined and could serve as trailing lines (ASSUMPTION). | 2 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| HTF Method | 'User Defined' | 'Auto' or 'User Defined' | 2 |
| Time Frame (HTF) | 'D' | any resolution | 2 |
| Show Today CPR / R1-R4 & S1-S4 | false / false | toggles | 2 |
| Show Today Camarilla / Camarilla labels / PDH & PDL | true / true / true | toggles | 2 |
| Show Tomorrow CPR / pivots / Camarilla | false / false / false | toggles | 2 |
| Camarilla range factor | 1.1 with divisors 12, 6, 4, 2 | none | 2 |
| H6 extension | 1.168 x (H5 - H4) | none | 2 |
| Swing pivot period `prd` | 10 | 5 to 100 | 2 |
| BB length / source / StdDev | 20 / close / 2.0 | StdDev 0.001 to 50 | 2 |
| Trend Magic CCI period / ATR period / ATR multiplier | 20 / 1 / 5 | none; source hl2 | 2 |
| SuperTrend factor / ATR period | 3 / 10 | each 1 to 100; source hl2 | 2 |
| Boring candle body ratio | 50 (%) | 5 to 95 | 2 |
| MA-1..MA-4 type / period | EMA 9, EMA 13, EMA 50, EMA 100 | each SMA or EMA | 2 |

**Key quotes**

- "highhtf = security(syminfo.tickerid, HTF, high[1], lookahead = barmerge.lookahead_on)" [p. 2]
- "pivot = (highhtf + lowhtf + closehtf) / 3" [p. 2]
- "bc = (highhtf + lowhtf) / 2" [p. 2]
- "tc = (pivot - bc) + pivot" [p. 2]
- "r1 = 2 * pivot - lowhtf" [p. 2]
- "r2 = pivot + (highhtf - lowhtf)" [p. 2]
- "r3 = r1 + (highhtf - lowhtf)" [p. 2]
- "r4 = r3 + (r2 - r1)" [p. 2]
- "s1 = 2 * pivot - highhtf" [p. 2]
- "s4 = s3 - (s1 - s2)" [p. 2]
- "H5 = (highhtf / lowhtf) * closehtf" [p. 2]
- "H4 = closehtf + RANGE * 1.1/2" [p. 2]
- "H3 = closehtf + RANGE * 1.1/4" [p. 2]
- "L3 = closehtf - RANGE * 1.1/4" [p. 2]
- "H6 = H5 + 1.168 * (H5-H4)" [p. 2]
- "L5 = closehtf - (H5 - closehtf)" [p. 2]
- "highhtf1 = security(syminfo.tickerid, HTF, high[0], lookahead = barmerge.lookahead_on)" [p. 2]
- "DRKC = open[1] < close[1] ? open > high[1] ? close < close[1] - ((close[1] - open[1]) / 2) ? close > open[1] ? #dbff01 :na :na :na :na" [p. 2]
- "BrEng = close < open[1] ? low < low[1] ? high > high[1] ? open >= open[1] ? #FF7000 : na: na: na: na" [p. 2]
- "BuEng = low < low[1] ? high > high[1] ? open <= open[1] ? close > open[1] ? #00FF00  : na: na: na: na" [p. 2]
- "C2BR=(abs(open-close)*100/abs(high-low))" [p. 2]
- "Up=hl2-(Factor*atr(Pd))" [p. 2]
- "Trend := close > TrendDown[1] ? 1: close< TrendUp[1]? -1: nz(Trend[1],1)" [p. 2]
- "bufferDn= high + Multiplier * sma(tr,ATR)" [p. 2]

**Pseudocode** (fields: HTF-bar high, low, close of the previous period; open/high/low/close of the chart bar)

```
# Levels for the current period, from the PREVIOUS completed HTF bar (H, L, C)
P  = (H+L+C)/3;  BC = (H+L)/2;  TC = (P-BC)+P            # = 2P - BC
R1 = 2P - L; R2 = P + (H-L); R3 = R1 + (H-L); R4 = R3 + (R2-R1)
S1 = 2P - H; S2 = P - (H-L); S3 = S1 - (H-L); S4 = S3 - (S1-S2)
RNG = H-L
H5 = (H/L)*C
H4 = C + RNG*1.1/2; H3 = C + RNG*1.1/4; H2 = C + RNG*1.1/6; H1 = C + RNG*1.1/12
L1 = C - RNG*1.1/12; L2 = C - RNG*1.1/6; L3 = C - RNG*1.1/4; L4 = C - RNG*1.1/2
H6 = H5 + 1.168*(H5-H4); L5 = C - (H5-C); L6 = C - (H6-C)
PDH = H; PDL = L
# Bar patterns (on chart bars)
DarkCloud  = open[1]<close[1] and open>high[1] and close < close[1]-(close[1]-open[1])/2 and close>open[1]
BearEngulf = close<open[1] and low<low[1] and high>high[1] and open>=open[1]
BullEngulf = low<low[1] and high>high[1] and open<=open[1] and close>open[1]
Boring     = abs(open-close)*100/abs(high-low) <= 50
# SuperTrend(factor 3, ATR 10): Up=hl2-3*ATR10; Dn=hl2+3*ATR10
TrendUp   = close[1]>TrendUp[1]   ? max(Up,TrendUp[1])   : Up
TrendDown = close[1]<TrendDown[1] ? min(Dn,TrendDown[1]) : Dn
Trend     = close>TrendDown[1] ? 1 : close<TrendUp[1] ? -1 : Trend[1] (init 1)
# ASSUMPTION (not from text): long if Trend==1 and close>TC; exit when Trend flips to -1
```

**Ambiguities & assumptions**
- Look-ahead: the "today" block uses `high[1]`/`low[1]`/`close[1]` of the HTF with `lookahead_on`. This is the standard non-repainting idiom: each bar sees only the previous completed HTF bar [p. 2]. Safe in a backtest.
- Look-ahead risk: the "tomorrow" block uses `high[0]`/`low[0]`/`close[0]` with `lookahead_on` [p. 2]. On historical bars this returns the final H/L/C of the same HTF bar (for example the full day's close) while the bar is being plotted, and on the live bar it is the still-forming bar. Using these levels for trading the same day is look-ahead. They are valid only as levels for the NEXT HTF bar (shift them by one HTF bar). The formulas for r11..r41, s11..s41, H11..H61, L11..L61 are not shown in the text (summarised by the coordinator as repeats) [p. 2].
- Camarilla H3/L3 and H4/L4 use the 1.1/4 and 1.1/2 factors shown [p. 2]. H5 is a ratio formula `(H/L)*C` and H6 extends H4 to H5 by 1.168 [p. 2]; L6 mirrors H6 around C. Note that H1-H4 / L1-L4 are symmetric around C but H5/L5 are mirrored through C, not computed with the same ratio.
- `tc = (pivot - bc) + pivot` can be below `bc` (when the close is in the lower part of the range), so the CPR "top" and "bottom" labels may be inverted; a coder should use min/max for the CPR width. ASSUMPTION: CPR width = abs(tc - bc), and "narrow CPR" thresholds are not defined in the text.
- The price-action bar definitions do not test bar colour: BrEng requires only `close < open[1]`, `low < low[1]`, `high > high[1]`, `open >= open[1]`; BuEng requires `open <= open[1]` and `close > open[1]` [p. 2]. They are not textbook engulfing patterns. Implement exactly as written or label them differently. Dark cloud tests `close > open[1]` (so the close stays above the prior open) [p. 2].
- Swing high/low: `pivothigh(prd, prd)` / `pivotlow(prd, prd)` confirm a pivot only `prd` (10) bars later; plotting it at the pivot bar is look-ahead in a backtest. ASSUMPTION: assign the signal to bar pivot+10.
- The SuperTrend and Trend Magic blocks assign with `:=` to variables whose declarations are not in the supplied text (the coordinator omitted some lines), so initial values (e.g. `TrendUp`, `bufferUp`, `ph`) are not shown; the p. 2 text uses `fill(r30,r40,...)` without defining r30/r40 in the excerpt [p. 2]. Treat the excerpt as incomplete for direct compilation.
- Trend Magic with `ATR=1` uses `sma(tr, 1)`, i.e. the raw true range, and multiplier 5 [p. 2]; this is a very wide buffer (5 x TR) and differs from usual settings. Implement as written.
- VWAP option uses the built-in `vwap` [p. 2] (session-anchored, needs intraday data).

### 2.3 VMST Bollinger Bands x3 and anchored Bank Nifty VWAP (madhavbbs)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Volatility-band indicator plus anchored VWAP. Possibly mean-reversion or trend context; no trade rule in the text. | 3 |
| Timeframe & holding period | Chart timeframe (`res = timeframe.period`); VWAP anchor resolution default '1D'. Holding period not found in this text. | 3 |
| Universe / eligibility filters | Defaults to symbol 'NSE:BANKNIFTY' and futures volume symbol 'NSE:BANKNIFTY1!'. Otherwise not found in this text. | 3 |
| Market / regime filter | Not found in this text. The 1-sigma middle line colour (green if rising, red if falling, gray if flat) can be read as a trend filter. | 3 |
| Setup conditions | `a2u = close > upperc` (close above the 3 SD upper band) and `b2l = lowerc > close` (close below the 3 SD lower band). Middle line rising/falling flags `up1`/`down1`. | 3 |
| Entry trigger & order type | Not found in this text. ASSUMPTION: close outside the 3 SD band = either (a) mean-reversion fade back toward the basis, or (b) a strong trend extension; the text states neither. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. ASSUMPTION: for a fade, exit at the 20-period basis. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| BB length | 20 | none | 3 |
| BB multipliers | 1, 2, 3 (three bands, source close) | none | 3 |
| Symbol / futures volume symbol | NSE:BANKNIFTY / NSE:BANKNIFTY1! | user input | 3 |
| Use Future Volume | true | if false: weighted bank-stock volume | 3 |
| Anchor Resolution | '1D' | any timeframe | 3 |
| Manual anchoring / start time | false; 2021-06-21 09:00 | user input | 3 |
| Dev band multipliers 1-3 (VWAP) | 1, 2, 3 (declared, unused in the supplied code) | none | 3 |
| Bank stock volume weights | HDFCBANK .2829, ICICIBANK .2137, KOTAKBANK .1236, SBIN .1221, AXISBANK .1215, INDUSINDBK .0505, AUBANK .0185, BANDHANBNK .0184, FEDERALBNK .0154, IDFCFIRSTB .0138, PNB .0111, RBLBANK .0085 (sum 1.0000) | none | 3 |

**Key quotes**

- "[middlea, uppera, lowera] = ta.bb(close, 20, 1)" [p. 3]
- "[middlec, upperc, lowerc] = ta.bb(close, 20, 3)" [p. 3]
- "a2u = close > upperc" [p. 3]
- "b2l = lowerc > close" [p. 3]
- "up1 = middlea > middlea[1]" [p. 3]
- "tickerid = input.symbol('NSE:BANKNIFTY', title='Symbol')" [p. 3]
- "is_first = is_anchored ? start_time_range : na(t[1]) and not na(t) or t[1] < t" [p. 3]
- "cum_prcvol := is_first ? _hlc3 * _volume : _hlc3 * _volume + cum_prcvol[1]" [p. 3]
- "cum_prcvol2 := is_first ? math.pow(_hlc3, 2) * _volume : math.pow(_hlc3, 2) * _volume + cum_prcvol2[1]" [p. 3]
- "avwap := cum_prcvol / cum_vol" [p. 3]
- "plot(ta.vwap, color=ta.rising(ta.vwap, 2) ? #0022FC : #FC0400, style=plot.style_linebr, linewidth=2, title='VWAP')" [p. 3]

**Pseudocode** (fields: close; for the VWAP: high, low, close, volume of the index/future on an intraday chart)

```
mid, up1s, lo1s = SMA(close,20), mid+1*SD20, mid-1*SD20      # also 2 and 3 SD
up3 = mid + 3*STDEV(close,20); lo3 = mid - 3*STDEV(close,20)
a2u = close > up3 ; b2l = close < lo3
midRising = mid > mid[1]; midFalling = mid < mid[1]
# Anchored VWAP (anchor = new day when anchor_res='1D'; or user start time)
hlc3 = (high+low+close)/3
vol  = futuresVolume  OR  sum_i( w_i * volume_i )              # 12 bank stocks with the weights above
on anchor bar: cum_pv = hlc3*vol; cum_p2v = hlc3^2*vol; cum_v = vol
else:          cum_pv += hlc3*vol; cum_p2v += hlc3^2*vol; cum_v += vol
avwap = cum_pv / cum_v
# ASSUMPTION (not from text): VWAP stdev = sqrt(cum_p2v/cum_v - avwap^2); bands = avwap +/- k*stdev, k = 1,2,3
# ASSUMPTION (not from text): fade a2u/b2l back to mid, or stay with trend while mid rises; neither is stated
```

**Ambiguities & assumptions**
- Code issue: the script reads `show_stdevb` and `mult1`-`mult3` and accumulates `cum_prcvol2`, but never computes or plots the VWAP standard-deviation bands (coordinator note) [p. 3]. Those inputs are dead code in the supplied text. ASSUMPTION: the intended band is `sqrt(cum_p2v/cum_v - avwap^2)` times the multipliers; this is inferred from the accumulator, not stated.
- The script draws BOTH lines: the computed anchored Bank Nifty VWAP `plot(show_vwap ? avwap : na, ...)` and the built-in `plot(ta.vwap, ...)` of the chart symbol [p. 3]. (Coordinator correction: an earlier draft said `avwap` was not plotted; that line had been left out of the assembled text by the coordinator and has been restored.)
- `fn_s1(_sym, _res, _src)` is a thin `request.security` wrapper and `start_time_range` marks the first bar at or after the manual anchor time [p. 3]. (Coordinator correction: an earlier draft said these were undefined; their definitions had been left out of the assembled text by the coordinator and have been restored.) The variable named `tickerid` shadows the built-in `syminfo.tickerid`-style name.
- The `is_first` line mixes `na(t[1]) and not na(t) or t[1] < t` without parentheses; Pine's `and` binds tighter than `or`, so it reads (na(t[1]) and not na(t)) or (t[1] < t), which is the intended "new anchor period" test [p. 3].
- The bank-stock fallback multiplies each stock's volume by a fixed index weight [p. 3]; this is a share-volume proxy, not a true index volume.
- Colours `mycolor1`, `up1`, `down1`, `a2u`, `b2l` are computed but no plot or alert using them is in the supplied text; any signal usage is an assumption.

### 2.4 VMST VWAP + StdDev Bands (madhavbbs)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Volume-weighted level with deviation bands. Possibly mean-reversion around VWAP; no trade rule in the text. | 4 |
| Timeframe & holding period | Chart timeframe (intraday for a session VWAP); holding period not found in this text. | - |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | Bands at VWAP +/- 1, 2, 3 x stdev(close, 34). VWAP is coloured blue when rising over 2 bars, else red. | 4 |
| Entry trigger & order type | Not found in this text. ASSUMPTION: fade a close beyond SD2 or SD3 back toward VWAP, or buy a pullback to VWAP when it is rising. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Not found in this text. ASSUMPTION: VWAP. | - |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| VWAP 1 / 2 / 3 multipliers (`l1`, `l2`, `l3`) | 1.0 / 2.0 / 3 | user inputs | 4 |
| Stdev length (`length`) | 34 | user input | 4 |
| Source | close | none | 4 |
| VWAP | built-in `ta.vwap(src)` | none | 4 |

**Key quotes**

- "b = ta.vwap(src)" [p. 4]
- "length = input(34)" [p. 4]
- "SD1=(b + l1 * ta.stdev(src, length))" [p. 4]
- "SD31=(b - l3 * ta.stdev(src, length))" [p. 4]
- "plot(ta.vwap, color=ta.rising(ta.vwap, 2) ? #0022FC : #FC0400, style=plot.style_linebr, linewidth=2, title='VWAP')" [p. 4]

**Pseudocode** (fields: high, low, close, volume, session start)

```
b   = VWAP(close) anchored at session start  # sum(close*volume)/sum(volume) since the session open (per ta.vwap(src))
sd  = STDEV(close, 34)                         # plain stdev of the last 34 closes, NOT volume-weighted, NOT anchored
SD1 = b + 1*sd; SD2 = b + 2*sd; SD3 = b + 3*sd
SD11 = b - 1*sd; SD21 = b - 2*sd; SD31 = b - 3*sd
vwapColour = rising(b, 2) ? blue : red
# ASSUMPTION (not from text): long when close < SD21 and then closes back above it; exit at b
```

**Ambiguities & assumptions**
- The band width is the rolling 34-bar standard deviation of price, not the deviation around VWAP; it does not reset with the VWAP anchor and is unrelated to volume [p. 4]. Using it as "VWAP SD bands" is a design choice of the script, not the usual volume-weighted band.
- `ta.vwap(src)` with one argument takes the source and uses the default anchor (new session) [p. 4]; the chart must be intraday for this to be meaningful. On daily bars the built-in session VWAP resets each bar and equals the source (here, close or hlc3) so the bands collapse to close +/- k*stdev.
- The six SD lines are calculated (SD1..SD31) but their plot calls are not in the supplied text (UI code omitted by the coordinator); only the VWAP line is plotted in the supplied code [p. 4].
- `l1 = 1.0`, `l2 = 2.0`, `l3 = 3` are mixed float/int inputs; harmless.

### 2.5 vkcash watchlist (not codable)

p. 5 is a single comma-separated TradingView watchlist of several hundred symbols (mostly NSE:, some BSE:, plus BINANCE:BTCUSDT and NASDAQ:SFM), apparently grouped by sector, with no indicator code and no rules [p. 5]. It is not a strategy. It could at most serve as a user-defined stock universe; the selection criteria are Not found in this text. ASSUMPTION: do not use it as a backtest universe (survivorship: a hand-picked current list).

## 3. Risk & money-management rules

Not found in this text. None of the five files contains risk-per-trade, stop, sizing, drawdown or exposure rules [pp. 1-5].

## 4. Non-codable guidance

- The text contains no discretionary guidance. The only judgment-related content is the reading of the colours (histogram colours, VWAP blue/red) and the label/level display choices [pp. 1-4].
- The watchlist's sector grouping and symbol selection reflect the user's discretion and are undocumented [p. 5].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - Squeeze (2.1): daily or intraday OHLC (close, high, low for true range). Computable on daily data for all stocks.
  - CPR / pivots / Camarilla / PDH / PDL (2.2): previous-period H, L, C. For daily-bar CPR/Camarilla from the previous day's H/L/C, daily OHLC suffices. Weekly or monthly HTF levels can be built by resampling daily bars. Bar-pattern, boring-candle, MA, BB, Trend Magic (needs CCI), SuperTrend (needs ATR 10) and swing pivots need only OHLC.
  - Bollinger x3 (2.3): close only for the bands.
  - VWAP and VWAP SD (2.3, 2.4): intraday OHLCV bars. The Bank Nifty future volume (`NSE:BANKNIFTY1!`) and the bank-stock weights (p. 3) are not in our data.
- **Testability with our data:**
  - Backtestable on 2005-2026 daily data: squeeze on/off and momentum histogram, BB 1/2/3 SD, close outside 3 SD, SuperTrend, Trend Magic, MAs, boring candles, bar patterns, swing pivots (with confirmation delay), and daily-bar CPR / pivots / Camarilla computed from the previous day's H/L/C (non-repainting, equal to the `high[1]` idiom on p. 2).
  - Not testable: VWAP, VWAP SD bands and intraday use of Camarilla/CPR (we have daily only). On daily bars the built-in session VWAP degenerates (see 2.4). The anchored Bank Nifty VWAP needs intraday Bank Nifty or futures data and the index weights, which we do not have. Nifty index history starts only in 2024 and there is no Bank Nifty series listed in our data context (ASSUMPTION: not available).
  - No fundamentals or delivery % are used.
- **Market-structure differences:**
  - The scripts are chart overlays; any signal built on them has to be defined from scratch. ASSUMPTION: test the squeeze fire (2.1) and daily CPR/Camarilla level-touches (2.2) as separate hypotheses with a fixed entry next open, to be validated against the no-overnight-short constraint (long only in cash).
  - Short-side signals (negative momentum, S1-S4 / L3-L6 breakdowns, b2l fade shorts) cannot be executed as overnight shorts in the NSE cash market. ASSUMPTION: use them only as exit / avoid signals, or as intraday shorts (needs intraday data).
  - Circuit limits can prevent exits at stop levels (stocks locked at lower circuit), and Camarilla/pivot levels computed on circuit-limited days are distorted. STT, brokerage and about 0.1% slippage matter for level-touch strategies with small expected moves.
  - The p. 3 settings (Bank Nifty, bank-stock weights as of the author's date) are index-specific. ASSUMPTION: for stocks, run only the generic BB x3 (close, 20) bands.

## 6. Verdict

- **Codeability:** Fully for the indicators themselves given OHLCV; there is no strategy. There are no entry/exit/stop/sizing rules in any of the five files, and the watchlist has none either, so no complete strategy can be coded without assumptions.
- **Priority for backtesting:** Low. The text yields no testable method and no performance claims; the squeeze and daily CPR/Camarilla levels could be tested as generic indicator hypotheses only after a signal is defined (ASSUMPTION) separately.
- **Top 3 things a coder is most likely to get wrong:**
  1. Look-ahead in the p. 2 levels: the "today" block (`[1]`, lookahead on) is safe, but the "tomorrow" block (`[0]`, lookahead on) uses the still-forming/final HTF bar and the swing `pivothigh(10,10)` is confirmed 10 bars late; treating either as known in real time inflates results.
  2. Replicating Pine details: population stdev (ddof 0), `linreg(...,0)` end-point value, SMA of true range (not Wilder ATR) for the Keltner channel, `tc`/`bc` ordering, and the non-standard bearish/bullish engulfing conditions on p. 2.
  3. Assuming the p. 3 and p. 4 scripts draw volume-weighted VWAP SD bands: p. 3 never computes them (the cum_prcvol2 accumulator is unused), and p. 4 uses a plain 34-bar stdev of close around a session VWAP, which needs intraday data that daily bars cannot supply.
