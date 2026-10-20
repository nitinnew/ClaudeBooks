# The Basics of the Elliott Wave Principle — Robert R. Prechter, Jr.

- **Source file:** Google Drive "The Basics Of Elliot Wave Principle - Robert R Prechter(1).pdf" (46 pages). Published by New Classics Library / Elliott Wave International; copyright 1995-2004, editions: First Aug 1995, Second Feb 1996, Third Apr 2000, Fourth Jun 2004, "August 2007" [p. 3].
- **Text file used:** text/prechter_basics_elliott.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage. Printed page numbers (running headers, contents) are offset by about 1 and are not used.
  - Verified with `verify_citations.py`.
- **Coverage:** Read the entire text file, lines 1-1240, in 2 sequential chunks; last marker reached `[[PAGE 46]]`. Pages 1 and 46 are blank; pp. 21, 24 and 34 are figure pages with almost no text (wave diagrams are images and are not in the text, so every figure referenced is unseen); p. 14 (degree label table), pp. 4-7 (contents, foreword, author bio) and pp. 44-45 (DVD advertisement) were read but contain no rules. Nothing garbled. *Coordinator check: the coordinator re-ran verify_citations (45/45 ok) and an exact-page strict check (0 off-by-one), and confirmed the five field tables have exactly the 12 template rows. Spot-checked by grep: hard rules (100% retracement, wave 3 not shortest, no overlap) p.15, alternation p.27/31, throw-over p.29, stop at the invalidation level p.31, 61.8% / 38.2% ratios p.33-40, Subminuette claim p.16, 'Guru of the Decade' p.7; all matched.*

## 1. The method in brief
The Wave Principle (R.N. Elliott) claims that crowd behaviour trends and reverses in recognisable, fractal patterns: progress takes the form of five waves (three motive waves, 1, 3, 5, separated by two corrective waves, 2 and 4), and every motive wave is followed by a three-wave (or variant) correction A-B-C, at every degree of trend [p. 8, p. 9, p. 10]. Motive waves (5-wave) move with the next-larger trend; corrective waves (3-wave or variation) move against it [p. 12]. Nine degrees are named, Grand Supercycle down to Subminuette [p. 13]. The booklet gives a small set of inviolable "rules" and a larger set of tendencies called "guidelines" (extension, truncation, alternation, equality, channeling, personality, ratios) [p. 15, p. 16], then Fibonacci retracement and multiple relationships [p. 36, p. 37, p. 38, p. 39, p. 40]. The stated practical goal is to "identify market lows suitable for entering positions on the long side and market highs offering the opportunity to take profits or enter the short side" [p. 30]. Timeframe is any degree, from hourly charts to multi-decade (DJIA was Elliott's main research tool) [p. 8, p. 13]; the book is a primer and defers to Frost & Prechter's *Elliott Wave Principle* for full detail [p. 41].

The text contains no complete mechanical trading system: no entry order types, no position sizing, no portfolio rules, no backtest. Wave identification is explicitly interpretive: "two or more valid wave interpretations are usually acceptable" and the analyst keeps a preferred and an alternate count [p. 30, p. 31]. Only the hard rules, the Fibonacci ratios and channel construction are geometric enough to code, and only on a swing-pivot proxy that the book does not define.

**Track-record claims (claims only, no data given):** forecasts of "stunning accuracy" earned awards [p. 5]; Frost and Prechter's 1978 book forecast a roaring 1980s bull market followed by a record bear market [p. 5]; the author "set a record in the options division of the U.S. Trading Championship" in 1984 [p. 7]; "Guru of the Decade" in 1989 [p. 7]. One illustration of ratios: DJIA wave I 1932-37 gained 371.6% and wave III 1942-66 gained 971.7%, "2.618 times as much" [p. 37]. The author states he found "but one instance above Subminuette degree" where a rule appeared broken [p. 16]. None of this is verifiable or backtestable from the text.

## 2. Strategies
The text yields five partly codable components. They are building blocks on a swing-pivot proxy rather than a self-contained system. Every one depends on the pivot proxy (ASSUMPTION, defined once below), because the book never defines how swings or degrees are to be detected.

**Shared ASSUMPTION (pivot proxy):** Pivots P0, P1, ..., Pn are alternating swing highs and lows from a percentage-reversal zigzag filter on daily closes (or on high/low) with reversal threshold R (default 12%; scan 8-20%). Leg i is the move P(i-1) to P(i). A bullish 5-pivot candidate uses P0 (low), P1 (high = end of wave 1), P2 (low = end of wave 2), P3 (high), P4 (low), P5 (high). The book gives no such definition; lengths are measured in log price (percentage terms), because the book says Fibonacci impulse relationships "usually occur in percentage terms" [p. 37] and wave 3 must be shortest or not "on a greater percentage movement" basis [p. 15].

### 2.1 Impulse hard-rule validator (filter on a pivot sequence)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: structural filter / pattern validator (used to qualify or reject a candidate 5-wave count; not a stand-alone entry system) | 15 |
| Timeframe & holding period | Any degree; "from the smallest wiggle on an hourly chart" upward. No holding period given. | 13 |
| Universe / eligibility filters | Rules hold for "all non-leveraged cash markets"; overlap in futures is "usually confined to daily and intraday price fluctuations and even then is rare". No liquidity or stock filters given. | 15 |
| Market / regime filter | Not found in this text. Waves are labelled relative to the next-larger trend (motive if same direction, corrective if opposite), but no objective regime filter is given. | 12 |
| Setup conditions | A 5-pivot impulse is valid only if all hold: (1) wave 2 retraces less than 100% of wave 1; (2) wave 3 travels beyond the end of wave 1; (3) wave 3 is never the shortest of waves 1, 3, 5 (tested in percentage terms; almost always also holds arithmetically); (4) wave 4 retraces less than 100% of wave 3; (5) wave 4 does not enter the price territory of wave 1 (no overlap). Exception: diagonal triangles (mostly fifth waves) where wave 4 almost always overlaps wave 1. Additionally wave 5 should normally exceed the end of wave 3 unless it is a truncation (five-wave fifth). | 15, 18, 19 |
| Entry trigger & order type | Not found in this text (rule set only validates a count). | - |
| Initial stop-loss | Generic: Wave Principle "provides a built-in objective method for placing a loss-limiting stop"; if the market moves beyond what the completed pattern allows, "the conclusion is wrong". Specific levels are implied by the rules (below start of wave 1 for a long entered after wave 1; below end of wave 1 for a long entered in wave 4) but the book does not spell out stop prices. | 31 |
| Exits: profit-taking | Not found in this text for this component. | - |
| Exits: trailing / time / signal | Count invalidation: any violation of rules (1)-(5) kills the count. A truncated fifth "will often cut short an expected target". | 18, 31 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Wave 2 max retracement of wave 1 | < 100% | none | 15 |
| Wave 4 max retracement of wave 3 | < 100% | none | 15 |
| Wave 4 overlap of wave 1 territory | not allowed in impulse | allowed in diagonal triangle (leading/ending) | 15, 19 |
| Wave 3 vs waves 1 and 5 | never the shortest (percentage basis) | "often the longest" | 15 |
| Extension | one and only one of waves 1, 3, 5 in vast majority of impulses | third wave of an extended third often extends | 17 |
| Pivot reversal threshold R | not in book | ASSUMPTION: 12%, scan 8-20% | - |
| Overlap tolerance for daily data | not in book (cash markets: none) | ASSUMPTION: strict on closes, test also strict on intraday lows | 15 |

**Key quotes**
- "100% of wave 1, and wave 4 always retraces less than 100%" [p. 15]
- "Wave 3, moreover, always travels beyond the" [p. 15]
- "is often the longest and never the shortest among the three" [p. 15]
- "wave 3 undergoes a greater percentage movement than" [p. 15]
- "overlapping is usually confined to daily and intraday price fluctuations" [p. 15]
- "A rule should never be disregarded." [p. 16]
- "provides a built-in objective method for placing a" [p. 31]
- "the conclusion is wrong, and any funds at risk can be" [p. 31]

**Pseudocode**
```
# inputs: pivots[] from zigzag(R) on daily close (ASSUMPTION), alternating H/L
# candidate bullish impulse: P0 low, P1 high, P2 low, P3 high, P4 low, (P5 high optional)
def valid_impulse_bull(P0,P1,P2,P3,P4,P5=None):
    L1 = ln(P1/P0)                       # percentage-basis lengths
    L3 = ln(P3/P2)
    if not (P2 > P0): return False       # wave 2 < 100% of wave 1
    if not (P3 > P1): return False       # wave 3 beyond end of wave 1
    if not (P4 > P2): return False       # wave 4 < 100% of wave 3
    if not (P4 > P1): return False       # no overlap of wave 4 with wave 1
    if P5 is not None:
        L5 = ln(P5/P4)
        if L3 < L1 and L3 < L5: return False   # wave 3 not shortest
        truncated = P5 <= P3                     # flag only; book says needs 5 subwaves
    return True
# bearish: mirror all inequalities
# use: reject a candidate count as soon as a rule is violated -> exit/stop
```

**Ambiguities & assumptions**
- Pivots and degree are not defined. ASSUMPTION: single-degree zigzag with threshold R; each R gives one "degree".
- Wave 3 "never the shortest" is stated in percentage terms [p. 15]; ASSUMPTION: use log lengths as the test; also log the arithmetic test.
- The text states wave 4 does not overlap wave 1 for cash markets but allows rare daily/intraday overlap in leveraged futures [p. 15]. ASSUMPTION: NSE cash equities, so no overlap tolerance.
- Diagonal triangles allow overlap and are subdivided 3-3-3-3-3 (ending) or 5-3-5-3-5 (leading) [p. 42]; a pivot proxy cannot distinguish them from invalid impulses. ASSUMPTION: treat an overlap as a reject, and optionally tag it "possible ending diagonal" if it is in the fifth position and converging.
- Whether a "truncated fifth" is valid depends on verifying five subwaves [p. 18]; not testable on a single-degree proxy. ASSUMPTION: flag only.
- Rule violations on a proxy will be frequent because the proxy is not the author's count; the author says he found one rule breach above Subminuette [p. 16]. A coder should expect the filter to be far noisier than the author's claim.

### 2.2 Wave-2 / wave-4 pullback entry zones (Fibonacci retracement + alternation + previous-fourth-wave depth)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: pullback entry within a rule-valid impulse (trend-continuation) | 30 |
| Timeframe & holding period | Any degree; no holding period given. | 13 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Not found in this text; the setup is conditioned on a valid wave 1 (and wave 3 for wave 4) impulse count. | - |
| Setup conditions | Long after a completed wave 1 (or wave 3) when the retracing correction reaches a Fibonacci zone: sharp corrections (wave 2 of an impulse, wave B of a zigzag, wave X in multiple zigzag) "more often" retrace 61.8% or 50% of the previous wave; sideways corrections (especially wave 4) retrace 38.2% of the previous impulse wave. Alternation: if wave 2 is sharp, expect wave 4 sideways, and vice versa. Depth: corrections, especially fourth waves, tend to register maximum retracement within the span of the previous fourth wave of one lesser degree, most commonly near its terminus. Sharp corrections are almost always zigzags and never make a new price extreme beyond the end of the prior impulse wave; sideways corrections usually do. | 36, 27, 28 |
| Entry trigger & order type | Not found in this text (the book names zones, not triggers or order types). | - |
| Initial stop-loss | Not specified numerically. Implied by rules: a long taken in wave 2 is wrong if price retraces 100% of wave 1 (below the wave 1 start); a long taken in wave 4 is wrong if price enters wave 1 territory. The book states generically that stops are placed where the pattern is invalidated. | 15, 31 |
| Exits: profit-taking | Targets from Fibonacci multiples (see 2.3). | 37, 38 |
| Exits: trailing / time / signal | Count invalidation exit (see 2.1). | 31 |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Sharp-correction retracement (wave 2, B, X) | 61.8% or 50% of previous wave | "more often" only; not exhaustive | 36 |
| Sideways-correction retracement (wave 4) | 38.2% of previous impulse wave | "more often" only | 36 |
| Retracement measure | percentage terms (stated for impulse multiples; for retracements not stated) | arithmetic vs log not specified for retracements | 37 |
| Depth guideline | max retracement within span of previous fourth wave of one lesser degree, near its terminus | none | 28 |
| Zone tolerance around Fib level | not in book | ASSUMPTION: +/- 3 percentage points of retracement | - |
| Alternation test | sharp vs sideways (sharp = no price extreme at/beyond prior impulse end; sideways = contains one) | none | 27, 43 |

**Key quotes**
- "corrections tend more often to retrace 61.8% or 50% of the" [p. 36]
- "retrace 38.2% of the previous impulse wave, particularly" [p. 36]
- "The guideline of alternation states that if wave two of" [p. 27]
- "retracement within the span of travel of the previous fourth" [p. 28]
- "Corrective patterns typically terminate in this area." [p. 43]
- "Retracements are where most analysts place their fo-" [p. 37]
- "Far more reliable, however, are relationships between" [p. 37]

**Pseudocode**
```
# Long only (NSE cash). Given valid P0..P3 (wave 1 = P0->P1, wave 2 in progress after P1)
# wave-2 pullback entry:
ret2 = (P1 - low_since_P1) / (P1 - P0)          # use log prices (ASSUMPTION)
zone2 = [0.50-tol, 0.618+tol]
if ret2 reaches zone2 and low_since_P1 > P0:    # <100% rule
    trigger = close > high of last N bars (N=3, ASSUMPTION) or pivot confirmation
    entry = next open after trigger
    stop  = P0 * (1 - slip)                      # ASSUMPTION: invalidation level
# wave-4 pullback entry (given valid P0..P3, wave 4 in progress after P3)
ret4 = (P3 - low_since_P3) / (P3 - P2)
zone4 = [0.382-tol, 0.382+tol]                   # also test 0.236-0.50 band
if ret4 in zone4 and low_since_P3 > P1:         # no overlap with wave 1
    entry as above; stop = P1 (ASSUMPTION)
# alternation filter (optional): if wave 2 was sharp (ret2 >= 0.5) prefer wave-4 sideways zone; vice versa
# previous-fourth-wave support (optional): level = low of the wave-4 subleg of wave 3 (needs lower-degree pivots, R/3 ASSUMPTION)
```

**Ambiguities & assumptions**
- The book gives retracement tendencies ("more often"), not exclusive rules; no tolerance bands. ASSUMPTION: +/- 3 pts around the level, scan 2-5.
- "Sharp" vs "sideways" is defined by geometry afterwards (price extreme beyond prior impulse end) [p. 43], so it cannot be known in real time. ASSUMPTION: use wave 2 shape (depth >= 50%) as a proxy for alternation.
- No entry trigger or order type. ASSUMPTION: confirm with a lower-degree pivot reversal (reversal of R/3) then buy next open.
- Stop levels are implied by the rules but not stated; see 2.1.
- "Previous fourth wave of one lesser degree" needs a second pivot degree. ASSUMPTION: R/3 zigzag.
- The book itself says retracement ratios are less reliable than multiples between alternate waves [p. 37]; test accordingly.

### 2.3 Fibonacci projection targets (waves 3, 5, and corrective wave C)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: price-target projection (profit-taking levels) | 37 |
| Timeframe & holding period | Any degree; no holding period given. | 13 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | Impulse multiples (usually in percentage terms): when wave 3 is extended, waves 1 and 5 tend toward equality or a .618 relationship; all three motive waves tend to be related by equality, 1.618 or 2.618 (inverses .618, .382). Wave 5 is sometimes related by a Fibonacci ratio to the length of waves 1 through 3. If wave 1 is extended, wave 2 often divides the whole impulse at the Golden Section. Unless wave 1 is extended, wave 4 often divides the impulse range at the Golden Section, the latter portion being .382 of the total when wave 5 is not extended and .618 when it is. Corrective multiples: zigzag wave C usually equals wave A, not uncommonly 1.618 or .618 of A (same for second zigzag vs first in a double zigzag); regular flat A, B, C approximately equal; expanded flat wave C usually 1.618 of A, often ending beyond the end of A by .618 of A, rarely 2.618; expanded-flat wave B sometimes 1.236 or 1.382 of A; triangle: at least two alternate waves related by .618 (e = .618c, c = .618a, d = .618b; expanding triangle 1.618); wave 4 often equal or Fibonacci to wave 2 in range. | 37, 38, 39, 40 |
| Entry trigger & order type | Not found in this text (projections are targets, not entries). | - |
| Initial stop-loss | Not found in this text for this component. | - |
| Exits: profit-taking | Take profit near the projected level; a retracement after a fifth wave "often has double resistance at the same level: the end of the preceding fourth wave and the .382 retracement point". A truncated fifth cuts a target short. | 38, 18 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Wave 5 vs wave 1 (wave 3 extended) | equality or 0.618 | - | 37 |
| Wave 3 vs wave 1 | equality, 1.618, 2.618 | "tend to"; example DJIA wave III = 2.618 x wave I | 37 |
| Wave 5 vs waves 1-3 net | "sometimes related by the Fibonacci ratio" (ratio unspecified) | 0.382, 0.618, 1.0, 1.618 (ASSUMPTION grid) | 38 |
| Wave 4 Golden Section: later portion of range | 0.382 (wave 5 not extended); 0.618 (wave 5 extended) | only when wave 1 not extended | 38 |
| Zigzag C vs A | 1.0 usually | 1.618 or 0.618 "not uncommonly" | 38 |
| Expanded flat C vs A | 1.618 | C beyond end of A by 0.618 of A; 2.618 rare; B = 1.236 or 1.382 of A | 39, 40 |
| Triangle alternate waves | 0.618 (contracting); 1.618 (expanding) | - | 40 |
| Wave 4 vs wave 2 | equality or Fibonacci (range) | percentage terms | 40 |

**Key quotes**
- "equality or a .618 relationship, as illustrated in Figure 26." [p. 37]
- "1937 gained 371.6%, while wave III from 1942 to 1966" [p. 37]
- "ratio to the length of wave 1 through wave 3, as illustrated" [p. 38]
- "wave 4 often divides the price range of an impulse wave" [p. 38]
- "In a zigzag, the length of wave C is usually equal to" [p. 38]
- "wave C is usually 1.618 times the length of wave A." [p. 39]
- "wave e = .618c, wave c = .618a, or wave d = .618b" [p. 40]
- "Finally, wave 4 quite commonly spans a gross or net" [p. 40]

**Pseudocode**
```
# lengths in log price. Long-only use: wave 3 and wave 5 projections.
L1 = ln(P1/P0); L3 = ln(P3/P2)
# Target for wave 3 (from end of wave 2 = P2):
T3 = {1.0, 1.618, 2.618} * L1   -> price = P2 * exp(m * L1)
# Target for wave 5 (from end of wave 4 = P4), wave 3 extended (L3 > max(L1)):
T5_a = P4 * exp(1.0 * L1);  T5_b = P4 * exp(0.618 * L1)
# wave 5 from net wave 1-3 length (ratio unspecified, ASSUMPTION 0.382/0.618/1.0)
Lnet = ln(P3/P0); T5_c = P4 * exp(r * Lnet)
# Golden-section wave 5 target (wave 1 not extended; ASSUMPTION about what "latter portion" means):
#   wave-5 not extended: P4 splits P0..P5 so that P5-P4 = 0.382*(P5-P0)  ->  P5 = P0 + (P4-P0)/0.618
#   wave-5 extended:      P5-P4 = 0.618*(P5-P0)                         ->  P5 = P0 + (P4-P0)/0.382
# Corrective wave C (from end of B): T_C = P_B - k * (P_A_start - P_A_end) in log, k in {1.0, 0.618, 1.618}
# exit rule: sell all/partial when high >= nearest projected level; clusters of >=2 levels within 1.5% = stronger
```

**Ambiguities & assumptions**
- The book does not say which multiple applies to which wave in a given case, and says the relationships "increase dramatically in utility when used together" [p. 40]. ASSUMPTION: use a target cluster (at least 2 coinciding projections) as the exit level; otherwise exit at the lowest.
- "Wave 5 ... Fibonacci ratio to the length of wave 1 through wave 3" [p. 38]: the ratio is not given. ASSUMPTION: grid 0.382/0.618/1.0.
- Wave 4 Golden Section reading ("the latter portion is .382 of the total distance") is ambiguous about whether "latter portion" is the wave-4-to-wave-5 leg. ASSUMPTION: yes, as in the pseudocode.
- Percentage vs arithmetic basis: book says "usually" percentage terms [p. 37]. ASSUMPTION: log lengths.
- The projections are only targets: no entry, stop or sizing. Combine with 2.2 for entries.

### 2.4 Channel projection of wave 5 with volume "throw-over" test
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: trend-channel target / exhaustion filter | 28 |
| Timeframe & holding period | Any degree; no holding period given. | 13 |
| Universe / eligibility filters | Volume rules apply to fifth waves "below Primary degree" (not defined in price terms); at Primary degree or larger, fifth-wave volume is naturally higher. | 29, 30 |
| Market / regime filter | Not found in this text. | - |
| Setup conditions | Parallel channels mark upper and lower boundaries of impulse waves. Draw the base line by connecting the ends of waves 2 and 4; draw the upper parallel through the peak of wave 3 (normal waves 1 and 3) to forecast the end of wave 5. If wave 3 is abnormally strong (almost vertical), a parallel through the top of wave 1 is "more useful". Check on both arithmetic and semilog scales and switch if price does not sit neatly in the channel. Draw the channel in advance. Volume: if the fifth wave approaches the upper trendline on declining volume, it will meet or fall short of it; if volume is heavy, expect a possible penetration ("throw-over"); same in declining markets. In a normal fifth wave volume is lower than in the third wave; if equal or higher, an extension of the fifth is in force. | 28, 29 |
| Entry trigger & order type | Not found in this text. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Sell in the vicinity of the upper channel line when fifth-wave volume is declining; allow for a throw-over (price beyond the line) when volume is heavy. | 29 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Base line | line through ends of waves 2 and 4 (P2, P4) | - | 29 |
| Upper parallel anchor | peak of wave 3 (normal); top of wave 1 if wave 3 abnormally strong | "almost vertical" undefined | 29 |
| Price scale | arithmetic and semilog both | "switch to the other scale" | 29 |
| Fifth-wave volume vs third-wave volume | lower in normal fifth; equal or higher means fifth extension | - | 29 |
| "Abnormally strong" wave 3 threshold | not in book | ASSUMPTION: L3 > 2.618 x L1 | - |
| "Approaches" band for upper line | not in book | ASSUMPTION: within 2% of line | - |
| Volume comparison window | not in book | ASSUMPTION: mean volume of wave 5 so far vs mean volume of wave 3 | - |

**Key quotes**
- "To draw a proper channel, first connect the ends of" [p. 29]
- "the upper parallel most accurately forecasts the end of wave" [p. 29]
- "trendline on declining volume, it is an indication that the" [p. 29]
- "indicates a possible penetration of the upper line, which" [p. 29]
- "tends to be less than in third waves." [p. 29]
- "Analysts should draw them" [p. 28]

**Pseudocode**
```
# base line through P2 and P4 (log-price version = semilog; also arithmetic)
slope = (P4 - P2) / (t4 - t2)          # on chosen scale
base(t) = P2 + slope*(t - t2)
offset  = P3 - base(t3)                 # normal case: parallel through wave-3 peak
if L3 > 2.618*L1:  offset = P1 - base(t1)   # ASSUMPTION for "abnormally strong"
upper(t) = base(t) + offset
# during wave 5 (after P4 confirmed as pivot):
vol5 = mean(volume since t4); vol3 = mean(volume t2..t3)
if close >= upper(t)*(1-0.02):
    if vol5 < vol3: exit long at upper(t)      # expect meet or fall short
    else:           allow overshoot: exit on first close back below upper(t) (throw-over; ASSUMPTION)
```

**Ambiguities & assumptions**
- The book says the arithmetic-vs-semilog question is "unresolved" [p. 29]. ASSUMPTION: compute both and use the one with the lower price-to-line residual over P1..P4.
- The book does not give a numeric definition of "abnormally strong" wave 3, "approaches", or "heavy" volume. See Parameters.
- The volume comparison is stated for fifth waves below Primary degree; degree is not mapped to timeframe. ASSUMPTION: use R-based pivots of all sizes.
- No entry rule is given; this component only produces exits/targets.

### 2.5 Three-swing corrective geometry classifier (zigzag / flat / triangle) with C-wave targets
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: pattern classifier (filter for correction type, to condition expected correction end) | 19 |
| Timeframe & holding period | Any degree; no holding period given. | 13 |
| Universe / eligibility filters | Not found in this text. | - |
| Market / regime filter | Flats "participate in periods involving a strong larger trend" and "virtually always precede or follow extensions"; the stronger the trend the briefer the flat; fourth waves frequently flats, second waves rarely. | 22, 23 |
| Setup conditions | Zigzag (5-3-5): top of wave B noticeably lower than start of wave A (bull market correction); C usually well beyond A's end. Regular flat (3-3-5): B ends about at the start of A; C ends slightly past the end of A. Expanded flat: B beyond the start of A and C substantially beyond the end of A (contains a price extreme beyond the preceding impulse wave); "far more common" than regular. Running flat: B well beyond start of A and C falls short of the end of A (rare). Triangles: overlapping five-wave 3-3-3-3-3 with decreasing volume and volatility; occur before the final actionary wave, as wave 4, B, or final X; wave b may exceed the start of a (running triangle). Combinations: at most one zigzag and one triangle in a combination; triangle only as final component. | 20, 22, 23, 25, 26 |
| Entry trigger & order type | Not found in this text. | - |
| Initial stop-loss | Not found in this text. | - |
| Exits: profit-taking | Use C-wave multiples in 2.3. | 38, 39 |
| Exits: trailing / time / signal | Not found in this text. | - |
| Position sizing | Not found in this text. | - |
| Adding to / pyramiding | Not found in this text. | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text. | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Zigzag B vs A start (bull-market correction) | B top noticeably lower than A start | "noticeably" undefined; ASSUMPTION: B retraces < 90% of A | 20 |
| Regular flat B | about at start of A | ASSUMPTION: B retraces 90-105% of A | 23 |
| Regular flat C | slightly past end of A | ASSUMPTION: C ends 0-10% of A beyond A's end | 23 |
| Expanded flat | B beyond start of A; C substantially beyond end of A | B = 1.236 or 1.382 of A; C = 1.618 of A | 23, 39, 40 |
| Running flat | B well beyond start of A; C short of end of A | rare | 23 |
| Triangle ratio | alternate waves related by 0.618 (1.618 expanding) | - | 40 |

**Key quotes**
- "The top of wave B is noticeably lower than the start of wave A," [p. 20]
- "terminates near the start of wave A." [p. 22]
- "correction, wave B terminates about at the level of the" [p. 23]
- "but wave C fails to" [p. 23]
- "Triangles are overlapping five wave affairs that" [p. 23]
- "there is never more than one zigzag in a combination." [p. 26]

**Pseudocode**
```
# given three bear-leg pivots A0 (start), A1 (end of A), B (end of B), C (end of C) after an up-impulse
ra = A0 - A1                       # wave A length
b_ret = (B - A1) / ra              # B retrace of A
c_ext = (A1 - C) / ra              # C length relative to A
if b_ret < 0.90 (ASSUMPTION): label = "zigzag-like"; expected c_ext ~ 1.0 (0.618, 1.618)
elif 0.90 <= b_ret <= 1.05:  label = "regular flat"; expected c_ext ~ 1.0-1.1
elif b_ret > 1.05:           label = "expanded flat"; expected c_ext ~ 1.618 (or 1.0 + 0.618)
# running flat: b_ret > 1.05 and c_ext < 1.0
# use label for alternation expectations and for the C-wave target in 2.3
```

**Ambiguities & assumptions**
- Zigzag vs flat is defined by internal subdivision (5-3-5 vs 3-3-5) [p. 20, p. 22], which a pivot proxy at one degree cannot see. The classification above uses the B/A ratio only; ASSUMPTION and noisy.
- The numeric boundaries are not in the text (only qualitative words such as "about", "slight", "noticeably"). ASSUMPTION values listed in Parameters.
- Triangles, double/triple threes and wave labels W/X/Y/Z are not reliably codable on a proxy; left as discretionary.
- The text gives no trade rule for corrections; the classifier merely modifies expectations for 2.2 and 2.3.

### 2.6 Wave identification (non-codable note)
Counting waves, assigning degree, deciding impulse vs diagonal vs correction, choosing the preferred and alternate counts, and verifying subwave counts (needed to confirm a truncation or a diagonal) are interpretive and cannot be coded from this text [p. 30, p. 31]. The author recommends deductive reasoning: knowing what the rules disallow, "whatever remains must be the most likely course" [p. 31]. When no count is preferred, wait until it resolves [p. 31]. The invalidation levels implied by the rules are the only codable portion and are captured in 2.1.

## 3. Risk & money-management rules
- Stops: the Wave Principle supplies "a built-in objective method for placing a loss-limiting stop": place it where the count would be wrong; if the market moves beyond what the apparently completed pattern allows, the position is closed [p. 31].
- Accept that "any approach that can identify high odds for a fairly specific outcome will produce a losing bet some of the time" [p. 30].
- Use an alternate count as a backup plan if the preferred scenario fails [p. 31].
- Position sizing, risk per trade, portfolio heat, maximum positions, drawdown rules: not found in this text.

## 4. Non-codable guidance
- Wave Principle gives "an objective means of assessing the relative probabilities" of future paths; several valid interpretations normally coexist; prefer the count satisfying the most guidelines, keep the next best as alternate [p. 30].
- If no clearly preferred interpretation, wait until the count resolves; later waves clarify earlier ones and the probability of a turning point can rise to nearly 100% [p. 31].
- Use deductive elimination by the rules (extensions, alternation, overlap, channeling, volume) [p. 31].
- Wave personality is mentioned as a guideline [p. 16] but is not described in this text (Frost & Prechter and the DVD series are referenced) [p. 41, p. 45].
- Several guidelines should be used together; "as several are simultaneously applicable in almost every situation" [p. 40].
- Corrective waves are "less clearly identifiable than motive waves" and more varied [p. 20].
- Wave degree notation and labels are discretionary conventions [p. 13, p. 14].
- Waves are not necessarily repetitive in time or amplitude [p. 8].

## 5. Adapting to NSE (Indian equities)
- **Data required:** Daily OHLC for pivot detection; daily volume (for the throw-over test in 2.4); optionally NIFTYBEES or an equal-weight index from the stock panel for index-level counts. No delivery % or fundamentals needed.
- **Testability with our data:** All five components are backtestable on 2005-2026 daily prices if the pivot proxy is accepted. They are tests of the author's rules on a mechanical proxy, not of the author's discretionary counts. The booklet's claimed accuracy cannot be tested. Index-level counts before 2024 need NIFTYBEES or an equal-weight index. Intraday/hourly degrees are not testable (daily only).
- **Market-structure differences:**
  - ASSUMPTION: long-only (no overnight shorting in the cash market); bearish mirror rules in the book are used only as exit signals.
  - ASSUMPTION: apply to liquid stocks only (e.g. median daily traded value above a threshold such as INR 5 crore) since small-cap pivots and circuit-limit days distort percentage reversals; treat circuit-locked days as non-tradable.
  - ASSUMPTION: the book says the no-overlap rule holds for cash markets [p. 15], which suits NSE cash stocks; apply it strictly.
  - ASSUMPTION: round-trip cost about 0.1% slippage plus STT and brokerage; with low-degree (small R) waves costs will dominate, so use R of 10% or more.
  - ASSUMPTION: use split/bonus-adjusted prices (as provided) so that pivots and Fibonacci ratios are not distorted; use log lengths because the book says relationships are in percentage terms [p. 37].

## 6. Verdict
- **Codeability:** Partly. The hard rules, Fibonacci ratios and channel construction are geometric and codable on a pivot proxy, but the book's wave counting, degree assignment and subwave verification are discretionary, and no entry, sizing or portfolio rules exist.
- **Priority for backtesting:** Low. There is no complete system and no reported test results; the codable parts need many assumptions (pivot threshold, tolerances, entry trigger) and the author's edge comes from discretionary counting. Medium only if used as an add-on filter/target set to an existing swing-trading system.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating a single-threshold zigzag as the author's "waves": the proxy has no degree, no subwave check, so rule violations and false impulses will be common, and results say little about the Wave Principle.
  2. Applying the rules in arithmetic instead of percentage (log) terms, and applying wave-3-not-shortest and no-overlap tests to the wrong pivot set or after the fact (look-ahead: pivots are only confirmed after a reversal of R, and "sharp vs sideways" is only known after the correction ends).
  3. Treating Fibonacci retracements and multiples as exact levels or rules: the book states them as tendencies ("more often", "usually", "sometimes"), without tolerances; only the hard rules in 2.1 are "rules".
