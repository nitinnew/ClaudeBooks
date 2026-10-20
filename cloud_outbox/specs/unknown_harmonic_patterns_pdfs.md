# Harmonic pattern cheat sheets — neoHarmonics.com; Emmanuel Nyemera, PhD

- **Source file:** "HARMONICS PATTERNS.pdf" (548 KB, www.neoHarmonics.com ratio cheat sheet) and "harmonicpatterns.pdf" (754 KB, "Harmonic Patterns: A subset of M & W Patterns from books written by Larry Pesavento, Scott Carney, Jim Kane and others", by Emmanuel Nyemera, PhD)
- **Text file used:** text/unknown_harmonic_patterns_pdfs.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not a printed page number)
  - pp. 1-3 = HARMONICS PATTERNS.pdf; pp. 4-9 = harmonicpatterns.pdf.
- **Coverage:** Read lines 1-524 (the whole file) in one read; last marker reached `[[PAGE 9]]`. Pages 1-2 are image-only pages that were RapidOCR'd (numbers are present but their position is scrambled). Page 3 has a real text layer (two small tables, the most reliable page). Pages 4-9 each have a short text layer of pattern titles only, followed by a "[page image OCR]" dump of the ratio diagrams. Caveat: in the OCR the ratio-to-leg mapping (XA / AB / BC / CD / XD) is mostly NOT recoverable. Ratios are assigned to a leg below only where (a) page 3's text layer pairs them, or (b) the OCR attaches a label to the number (e.g. `1.618AB=CD`, p. 8). Nothing was filled from general knowledge of harmonic trading. Nothing was skimmed. *Coordinator check: HARMONICS PATTERNS.pdf pp.1-2 are image-only and were RapidOCR'd. On harmonicpatterns.pdf (pp.4-9) the coordinator OCR'd every page image in addition to the short text layer, because the ratios exist only in the diagrams. verify_citations checks only quotes of 15+ characters (3/3 ok), so the coordinator ran its own exact whitespace-insensitive check of all 14 quoted fragments against their cited pages: 14 ok, 0 miss (appended to the verify log). The three field tables have exactly the 12 template rows.*

## 1. The method in brief
These two PDFs are ratio cheat sheets for "harmonic" XABCD / ABCD chart patterns (Gartley, Bat, Alternate Bat, Butterfly, Crab, Deep Crab, Cypher, Shark, 5-0, Three Drives, AB=CD variants), each drawn bullish and bearish [p. 1] [p. 2]. The second file describes itself as "A subset of M & W Patterns" taken from books by Pesavento, Carney, Kane and others [p. 4]. Page 3 is a plain-text "Harmonic Pattern Guide" giving the B-point retracement of the XA leg per pattern, and a C-point retracement to BC-projection table [p. 3].

There is no prose. The text contains no entry trigger, stop-loss, profit target, position-sizing rule, timeframe, market or track record. The only commentary is two W.D. Gann quotations on page 1 and page 2 (cycles repeat; use all of your tools and rules) [p. 1] [p. 2]. This resource is therefore a pattern-detection (geometry) spec only, not a trading system. In the sections below, "D" means the pattern completion point.

## 2. Strategies
Three recoverable pattern-detection filters are captured. All others are in the section 4.1 table. None of them is a complete trading strategy: entry, stop and exit are "Not found in this text" and every one of those rows is therefore `-`.

### 2.1 C-point retracement to BC-projection pairing table
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: pattern-detection filter (geometry only; not a trading rule) | 3 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | A table pairs a "C Point Retrace" with a "BC Projection": 0.382 -> 2.41-2.618; 0.500 -> 2.00; 0.618 -> 1.618; 0.707 -> 1.41; 0.786 -> 1.27; 0.886 -> 1.13. Which leg C retraces and which leg is projected is not stated in the text. | 3 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| C retrace -> BC projection pairs | (0.382, 2.41-2.618), (0.500, 2.00), (0.618, 1.618), (0.707, 1.41), (0.786, 1.27), (0.886, 1.13) | six pairs only | 3 |
| Tolerance on a ratio | Not found in this text | - | - |
| Swing-pivot definition | Not found in this text | - | - |

**Key quotes**
- "C Point Retrace" and "BC Projection" are the two column headings of the table [p. 3].
- "C point does not break A" is the condition printed with the XABCD group [p. 3].

**Pseudocode**
```
# pivots: alternating swing highs/lows from a zigzag (ASSUMPTION: see Ambiguities)
given pivots A, B, C (bullish: A=low, B=high, C=higher low; bearish mirrored)
c_ret = abs(C - B) / abs(B - A)                 # ASSUMPTION: C retraces the AB leg
if C beyond A: reject                            # "C point does not break A"
find table row r in {0.382,0.500,0.618,0.707,0.786,0.886} with |c_ret - r| <= tol
proj_lo, proj_hi = row projection (single value => lo = hi)
D_lo = C -/+ proj_lo * abs(B - C)   ;  D_hi = C -/+ proj_hi * abs(B - C)   # ASSUMPTION: projection of BC measured from C
output: candidate D zone [D_lo, D_hi]            # no entry/stop/exit exists in the text
```

**Ambiguities & assumptions**
- The text does not say which leg C retraces or which leg is projected. ASSUMPTION: C retraces AB and "BC Projection" means CD as a multiple of BC, measured from C in the direction away from B.
- The pairs are arithmetically reciprocal (e.g. 0.618 <-> 1.618, 0.500 <-> 2.00, 0.786 <-> 1.27 as printed). This agrees with the AB=CD idea of 2.3 but the text does not say so. ASSUMPTION: treat as an independent check only.
- 0.382 pairs with a range (2.41-2.618) while the others are single values. ASSUMPTION: single value +/- tol (default 3%); the 0.382 row is the range as printed.
- Tolerance and pivot definition: not found in this text. ASSUMPTION: zigzag of N% (default 5% on daily closes) and tol = 3%.
- Entry, stop and target: not found in this text. ASSUMPTION: any trading rule would have to be supplied by the tester (e.g. enter next open after D zone touched, stop beyond X/A); none is proposed by the author.

### 2.2 XABCD B-point retracement and D-point level, "C does not break A" group (Gartley, Bat, Alt Bat, Butterfly, Crab, Deep Crab)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: pattern-detection filter (geometry only; not a trading rule) | 3 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Page 3 heading "B Point Retrace of XA Leg" with "C point does not break A". Rows by B retrace: .382 -> Bat (-.886), Alternate Bat (-1.130), Crab (-1.618); .500 -> Bat (-.886), Crab (-1.618); .618 -> Gartley (-.786), Crab (-1.618); .786 -> Butterfly (1.27, 1.41, 1.618); .886 -> Deep Crab (1.618). Pages 1-2 and 4-5 show "0.382-0.886" for the third leg of all six patterns (leg not labelled) | 3, 1, 2, 4, 5 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Gartley: B retrace of XA ; D | B 0.618 ; D 0.786 | pp. 4 OCR also shows 0.618 and 0.786 in the Gartley block | 3, 4 |
| Bat: B retrace of XA ; D | B 0.382-0.50 ; D 0.886 | p. 3 lists Bat under rows .382 and .500 only; p. 4 OCR shows "0.382;0.50" and 0.886 in the Bat block | 3, 4 |
| Alternate Bat: B ; D | B 0.382 ; D 1.13 | p. 4 OCR shows 0.382 and 1.13 in the Alt Bat block | 3, 4 |
| Butterfly: B ; D | B 0.786 ; D 1.27-1.618 | p. 3 gives (1.27, 1.41, 1.618); p. 5 OCR shows "1.27;1.618" and 0.786 | 3, 5 |
| Crab: B ; D | B 0.382-0.618 ; D 1.618 | p. 3 lists Crab under rows .382, .500, .618; p. 5 OCR shows 0.382 and 0.618 in the Crab block | 3, 5 |
| Deep Crab: B ; D | B 0.886 ; D 1.618 | p. 5 OCR shows "B0.886" in the Deep Crab block | 3, 5 |
| C retrace (leg not labelled) | 0.382-0.886 for all six | appears 3 times per page on p. 1 and p. 2 for each trio of patterns | 1, 2 |
| C must not break A | yes | - | 3 |

**Key quotes**
- "B Point Retrace of XA Leg" [p. 3]
- "C point does not break A" [p. 3]
- ".786 (1.27, 1.41, 1.618 Butterfly)" [p. 3]
- ".886 (1.618 Deep Crab)" [p. 3]
- "0.382;0.50" in the Bat block [p. 4]
- "B0.886" in the Deep Crab block [p. 5]

**Pseudocode**
```
# pivots X,A,B,C,D from zigzag (ASSUMPTION), bullish: X low, A high, B higher low, C lower high, D low
xa = abs(A - X)
b_ret = abs(A - B) / xa                      # B retrace of XA
if C beyond A: reject                        # "C point does not break A"
c_ret = abs(C - B) / abs(A - B)              # ASSUMPTION: the unlabelled 0.382-0.886 is C retrace of AB
if not (0.382 <= c_ret <= 0.886): reject
d_xa = abs(A - D) / xa                       # ASSUMPTION: p.3 dash values are D relative to XA
table = {Gartley:(B=[0.618],D=[0.786]), Bat:(B=[0.382,0.50],D=[0.886]),
         AltBat:(B=[0.382],D=[1.13]), Butterfly:(B=[0.786],D=[1.27,1.41,1.618]),
         Crab:(B=[0.382,0.50,0.618],D=[1.618]), DeepCrab:(B=[0.886],D=[1.618])}
label = pattern whose B set contains b_ret (within tol) and whose D set contains d_xa (within tol)
```

**Ambiguities & assumptions**
- Page 3 prints rows such as ".382 / -.886 Bat / -1.130 Alternate Bat / -1.618 Crab" without saying what the dashed numbers are. Two readings: (a) the dashed number is the D level relative to XA, (b) it is the upper end of a B range. ASSUMPTION: reading (a), because the same patterns recur under successive B rows and pp. 4-5 OCR shows "0.382;0.50" in the Bat block and "B0.886" in the Deep Crab block, which fits (a) and not a Bat B range of .382-.886. This is the weakest point: treat the result as Partly codable.
- Butterfly D: p. 3 gives 1.27, 1.41 and 1.618; p. 5 OCR shows only "1.27;1.618". ASSUMPTION: use 1.27-1.618 and keep 1.41 inside it.
- The OCR in pp. 4-5 shows additional third-leg numbers (for example 1.27, 1.618, 2.0, 2.618, 3.618) which are not assigned to a leg here. See 4.1.
- C-leg 0.382-0.886: leg and base not labelled. ASSUMPTION: retrace of AB, as in 2.1.
- Bullish and bearish versions are mirror images (same numbers on p. 1 and p. 2). ASSUMPTION: bearish = mirrored; on NSE cash only the bullish (long) side is tradable overnight.
- Ratio tolerance, pivot definition, entry/stop/target: not found in this text. ASSUMPTION: tol 3%, zigzag 5% daily-close swings.

### 2.3 AB=CD family (CD as a multiple of AB)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: pattern-detection filter (geometry only; not a trading rule) | 8 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Labelled variants: AB=CD (CD = 1.0 x AB); "1.27AB=CD" and "1.618AB=CD" (Alternate ABCD); ".786AB=CD" and ".618AB=CD" (Other Alternate ABCD). Page 1/2 percent labels agree: 100%, 127%, 161.8% | 8, 1, 2 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| CD / AB multiple | 1.0 | 0.618, 0.786, 1.0, 1.27, 1.618 | 8 |
| CD / AB as percent (p. 1 AB=CD, Ext, Alt AB=CD) | 100%, 127%, 161.8% | - | 1, 2 |
| C retrace of AB (leg and pattern link not labelled) | 0.618-0.786 seen near AB=CD | 0.382-0.886 also seen on p. 1; "0.618; 0.786" on p. 7 impulse block | 1, 7 |
| BC projection (not labelled) | 1.13-2.618 seen near AB=CD Ext | pair with the 2.1 table instead | 1 |
| Variants with no text distinction | Impulse (measured move), Corrective (reciprocal), ABCD inside leg of higher ABCD, Back-to-back ABCDs | difference lies only in the diagrams | 7, 8, 9 |

**Key quotes**
- "1.618AB=CD" [p. 8]
- "1.27AB=CD" [p. 8]
- ".786AB=CD" [p. 8]
- ".618AB=CD" [p. 8]
- "Bullish AB =CD" [p. 1]
- "Corrective (or reciprocal) AB=CD" [p. 7]

**Pseudocode**
```
# pivots A,B,C,D from zigzag (ASSUMPTION), bullish: A high, B low, C higher low, D low
ab = abs(A - B) ; cd = abs(C - D)
ratio = cd / ab
valid if ratio within tol of any of {0.618, 0.786, 1.0, 1.27, 1.618}
optional: c_ret = abs(C - B)/ab in [0.618, 0.786]     # ASSUMPTION, see below
label: 1.0 -> "AB=CD"; 1.27/1.618 -> "Alternate ABCD"; 0.618/0.786 -> "Other Alternate ABCD"
```

**Ambiguities & assumptions**
- The label `1.618AB=CD` is read as CD = 1.618 x AB. ASSUMPTION: this reading (the text only shows the glued label).
- Whether the "Alternate" 1.27 / 1.618 versions require a particular C retracement is not recoverable. ASSUMPTION: no C-retrace condition by default; the 0.618-0.786 filter is optional.
- Impulse versus corrective AB=CD, nested ABCD and back-to-back ABCD differ only in drawings; no numbers beyond the above can be extracted. ASSUMPTION: not separable from price alone, so one detector covers all.
- Entry, stop, target, tolerance, pivot definition: not found in this text. ASSUMPTION: tol 3%, zigzag 5%.

## 3. Risk & money-management rules
Not found in this text. There is no risk per trade, stop, sizing or exposure rule anywhere in the two PDFs. The only commentary is the Gann quotation "Use ALL of your tools" [p. 2].

## 4. Non-codable guidance
- Page 1 carries a Gann quotation that cycle theory or harmonic analysis is the only thing we can rely on to ascertain the future (OCR text is garbled) [p. 1].
- Page 2 carries a Gann quotation: "Use ALL of your tools" and all of your rules, all of the time [p. 2].
- Pattern recognition from the diagrams (which pivot is X, A, B, C, D, impulse versus corrective, nested ABCD) is visual and only the numbers above are in the text [p. 7] [p. 8] [p. 9].

### 4.1 Patterns whose ratios are not recoverable from the OCR

| Pattern | Pages | Ratios seen (verbatim OCR values) | Why not codable |
|---|---|---|---|
| Cypher | 1, 2, 7 | p. 1 (block shared with Shark and 5-0): 1.13-1.618, 1.618-2.24, 0.50, 0.786, 0.886-1.13, 0.382-0.618. p. 2: 0.786, 0.886-1.13, 0.382, 1.414, 1.13-1.618. p. 7 (Cypher-only block): 78.6%, 38.2, 113-141.4%, 2-61.8%, 61.8%, 38.2%, 78.6% | Leg assignment not recoverable from OCR. The p. 7 percentages are the cleanest set, but p. 1/2 show a different range (1.13-1.618, 1.414), and which number belongs to B, C and D is not stated. |
| Shark | 1, 2, 3, 6 | p. 3 text layer: "C point breaks A", 1.13-1.618 (expanding megaphone), -.886, -1.130. p. 6: 1.13-1.618, 0.886, 0.886, 1.13-1.618. p. 1/2: 0.886-1.13, 1.13-1.618, 1.618-2.24 | Page 3 pairs numbers with "Shark" but does not state whether 1.13-1.618 is B or C and what -.886 / -1.130 refer to; not recoverable from OCR. |
| 5-0 | 1, 2, 6 | 1.13-1.618, 1.618-2.24, 0.50, 1.618 (p. 6: "1.618-", "1.13-", "0.50") | Leg assignment not recoverable from OCR (diagram numbers scrambled). |
| Three Drives (bottom/top) | 1, 2, 6 | p. 6: 1.618, 1.27, 1.618, 1.27, 1.618, 1.618, 2, 3, 1. p. 1/2: 0.618-0.786, 1.13-2.618, 127%, 161.8%, 100% (shared with AB=CD blocks) | Retracement versus extension per drive not recoverable; numbers shared with neighbouring blocks. |
| Gartley, Bat, Alt Bat, Butterfly, Crab, Deep Crab: BC projection (CD/BC) | 1, 2, 4, 5 | p. 1/2: 1.272-1.618, 1.618-2.618, 2.0-3.618. p. 4: Gartley block 1.27, 1.618; Bat block 1.618, 2.618; Alt Bat block "2.0; 3.618". p. 5: Butterfly 1.618, 2.618; Crab 3.618, 1.618, and "48" (garbled); Deep Crab "2.618; 3.618" | Block membership is by OCR order only, and the value is not labelled as BC or XA; not recoverable from OCR. Only D relative to XA (2.2) is used. |
| Alternate AB=CD, AB=CD Ext (percent form) | 1, 2 | 100%, 127%, 161.8%, 1.13-2.618, 0.382-0.886, 0.618-0.786 | Already covered by 2.3 for the CD/AB multiples; the other ranges cannot be tied to a leg. |

## 5. Adapting to NSE (Indian equities)
- **Data required:** Daily OHLC only (highs and lows for swing pivots); volume is not mentioned in the text. No delivery %, index or fundamentals needed.
- **Testability with our data:** Pattern detection (2.1, 2.2, 2.3) can be run on the 2005-2026 daily panel for every stock including delisted ones. A pattern-hit study (forward return after D zone is reached) is testable, but the text supplies no entry, stop or exit, so those must be invented by the tester and are not the author's rules. Fundamentals and Nifty history are irrelevant.
- **Market-structure differences:**
  - No overnight shorting: bearish patterns can be used only as a long-exit signal or in futures. ASSUMPTION: test bullish patterns only on cash equities.
  - The sheets are drawn for generic charts; daily bars on NSE stocks are subject to circuit limits (a limit-up/down day can distort a pivot). ASSUMPTION: skip stocks on circuit days for pivot detection.
  - STT, brokerage and about 0.1% slippage matter if patterns fire often. ASSUMPTION: apply 0.1% slippage each side.
  - Pivot definition drives everything. ASSUMPTION: zigzag with a 5% reversal threshold on daily closes; also test 3% and 8%.
  - ASSUMPTION: tolerance 3% on every ratio; sweep 1-5%.

## 6. Verdict
- **Codeability:** Partly codable: three ratio-set pattern-detection filters (2.1, 2.2, 2.3) can be written, but no trading rules exist and most pattern ratios (Cypher, Shark, 5-0, Three Drives) cannot be assigned to legs from the OCR.
- **Priority for backtesting:** Low: there are no entry, stop or exit rules, no evidence of edge, and discretionary pivot choice dominates results.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the page-3 dash values (e.g. "-.886 Bat") as D levels versus B ranges without noticing it is an ASSUMPTION, and filling the unrecoverable patterns (Cypher, Shark, 5-0) from outside knowledge.
  2. Using hindsight in pivot detection: a zigzag pivot is confirmed only after the reversal, so D cannot be known on the bar it forms.
  3. Assuming the OCR numbers on pp. 1-2 and 4-9 are leg-ordered; they are not, and numbers shared across several patterns on one page are easily assigned to the wrong pattern.
