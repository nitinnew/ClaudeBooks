# Telegram files Oct 2021 (bundle) — Mark Rose; others unnamed

- **Source file:** Telegram upload bundle, Oct 2021 (uploaded 2021-10-14 with the "Murthy sir" course files; flagged as possibly part of "C3 Murthy sir notes", which were never processed). Four files:
  - `5_6183711123267649981.pdf`, pp. 1-22: "Everything you wanted to know about candlestick charts" by Mark Rose (Thames Publishing Ltd, 2011; the Trader’s Bulletin Weekly Candlestick Cheat Sheet is p. 22; copyright notice p. 21) [p. 1] [p. 21]
  - `5_6183711123267649982` (PDF), pp. 23-44: "Candlestick Patterns – 21 easy Patterns (And what they mean)". The author is NOT named anywhere in the text. [p. 23]
  - `5_6134027418328891773.pptx`, pp. 45-60: "Basics of Stock Market and Trading — Exponential Moving Averages" (16 slides, presenter unnamed) [p. 45]
  - `5_6120919946940645703.pptx`, pp. 61-73: "Basics of Stock Market and Trading — Moving Averages Introduction" (13 slides, presenter unnamed; quotes "my mentor" without naming him) [p. 62]
- **Text file used:** text/telegram_files_oct21.txt  (page basis: pdf_pages for pp. 1-44; slides, one page per slide, for pp. 45-73)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (continuous numbering across all four files)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Page numbers printed in the Rose PDF's own headers/contents are the same as the markers for pp. 1-22 but were not relied on.
  - Before finishing, `verify_citations.py` was run on this spec.
- **Coverage:** Read lines 1-1513 (the whole file) in three sequential chunks; last marker reached was [[PAGE 73]]. Six OCR'd images were read: p. 51 (IBM SMA/EMA chart), pp. 58-59 (HUL 15-min 20 EMA / 20 SMA / 50 SMA charts), pp. 70-72 (three MA-crossover illustrations; p. 70 OCR is garbled and p. 72 is partly garbled). All candlestick diagrams in the two PDFs are images with no text, so shapes are known only from the prose. Page 21 is a legal disclaimer, page 60 and 73 are "Thank you" slides. Not processed: the byte-identical-size duplicate `5_6134027418328891773(1).pptx`. *Coordinator check: the two PDFs come from their text layers and the two pptx from slide XML plus RapidOCR of embedded images (one page per slide). The coordinator re-ran verify_citations (71/71 ok) and an exact-page strict check (0 off-by-one), and confirmed all 22 field tables have exactly the 12 template rows. Spot-checked by grep: hanging man 'bullish impulse' p.36 vs Rose p.12/22, 2x wick rule p.11/13, midpoint rules p.17-33, 5/35 EMA and Murphy p.49, 10-day MA p.65, 'Market is maya' p.62, sideways caveat p.72; all matched. The inventory flagged this item as a possible part of the 'Murthy sir' course notes; those notes were never processed here, so this spec duplicates no other spec.*

## 1. The method in brief

This bundle is not one method. It is (a) two candlestick pattern primers (Mark Rose, pp. 1-22; an unnamed 21-pattern guide, pp. 23-44) and (b) two beginner moving-average decks (pp. 45-73). Rose's thesis: candlesticks give "visual and very intuitive" clues, some patterns (morning/evening star) are "among the most reliable" and others (harami) are unreliable on their own, and candles "are not best used in isolation" but should be combined with simple technical analysis and a successful trading strategy [p. 4] [p. 15] [p. 10] [p. 20]. The 21-pattern guide groups patterns into doji, short-body and long-body candles and cites unspecified "statistical studies" as "pretty convincing" [p. 23]. Neither PDF gives any win rate, test result, stop, target or position size.

The decks cover SMA and EMA arithmetic, EMA lag, MA lengths (5-20 short, 50 medium, 100-200 long), the 5-day/35-day EMA and 50-day/200-day SMA crossover systems quoted from John Murphy, MA position as a bullish/bearish cue, MA support/resistance, and crossover signals that fail in sideways markets [p. 47] [p. 49] [p. 52] [p. 67] [p. 72]. No backtest results are given. The only market data shown are an IBM daily chart (2010) and HUL 15-minute NSE charts (Nov 2020), used for illustration [p. 51] [p. 58].

All candlestick and MA rules below are therefore pattern definitions with (mostly) discretionary context. Every numeric threshold needed to code them (what is "long", "small", "downtrend") is an `ASSUMPTION:` and not the author's.

## 2. Strategies

**Shared helper definitions and global backtest assumptions (all `ASSUMPTION:`, none are the authors').** The sources give no numeric thresholds, entry orders, stops or exits for any candlestick pattern, so every 2.x below reuses these.

- `body=|C-O|`, `top=max(O,C)`, `bot=min(O,C)`, `rng=H-L`, `upper=H-top`, `lower=bot-L`, `green: C>O`, `red: C<O`, `avgbody=mean(body over previous 10 bars)`.
- `LONG(i): body[i] >= 1.0*avgbody`; `SMALL(i): body[i] <= 0.5*avgbody`; `DOJI(i): rng[i]>0 and body[i] <= 0.05*rng[i]`.
- `DOWNTREND(i): C[i] < SMA(C,20)[i] and SMA(C,20)[i] < SMA(C,20)[i-5]`; `UPTREND(i)` is the mirror image. (Rose says only that a hammer is "found in a downtrend" [p. 11]; no trend definition is given.)
- G-ENTRY: signal is detected at the close of the last pattern bar; where the author asks for confirmation, at the close of the confirmation bar; buy at next day's open (long patterns only).
- G-STOP: long stop = low of the pattern (lowest low of the pattern bars). G-EXIT: sell at the open after a bearish signal from section 2 appears, or after 10 bars, whichever first.
- G-NSE: bearish patterns are used only as exit signals for existing longs or as an avoid-entry filter, because the NSE cash market has no overnight shorting (intraday short is possible but out of scope here).

### 2.1 Doji at a price-channel edge (Rose)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Reversal/indecision candle used with a channel (other) | 7 |
| Timeframe & holding period | Not found in this text (any timeframe: "Whatever trading timescale you work on") | 20 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Doji near the edge of a price channel; "in conjunction with other indicators" | 7 |
| Setup conditions | Open and close the same or almost the same; shadows vary; neither bulls nor bears in control | 7 |
| Entry trigger & order type | Not found in this text. Doji at the top of a channel "could indicate a bearish correction" (the bottom case is the implied mirror, not stated) | 7 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Doji body threshold | "same (or almost the same)" | not quantified | 7 |
| Channel definition | "price channel" | not defined | 7 |
| Doji role | reversal (Rose, cheat sheet) | "both a reversal pattern and a continuation pattern" (21-pattern guide) | 22, 24 |

**Key quotes**
- "It’s a sign of indecision in the market, and could (in conjunction with other indicators)" [p. 7]
- "if a doji appears at the top of a channel" [p. 7]
- "The doji can be both a reversal pattern and a continuation pattern." [p. 24]

**Pseudocode**
```
chan_hi = highest(H,20)[i-1]; chan_lo = lowest(L,20)[i-1]      # ASSUMPTION channel
if DOJI(i) and H[i] >= chan_hi*0.99: flag BEARISH_WARNING (exit/avoid long)
if DOJI(i) and L[i] <= chan_lo*1.01: flag BULLISH_WARNING (candidate long, needs confirmation next bar green close > H[i])
```

**Ambiguities & assumptions**: "price channel" undefined. ASSUMPTION: 20-day high/low channel, 1% proximity. The bottom-of-channel case is not stated by the author. ASSUMPTION: symmetric. Confirmation by the next bar is the generic Rose advice for single-candle patterns [p. 11]; applied here by ASSUMPTION.

### 2.2 Harami, bullish and bearish (Rose)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal | 9 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Bearish harami after an upward trend ("upward trend is running out of steam"); bullish is the flipside | 9 |
| Setup conditions | Small body "of the opposite colour, completely contained by the body of the previous session"; opposite colours "not essential" but more reliable; a shadow beyond the prior candle is tolerated by some | 9, 10 |
| Entry trigger & order type | Not found in this text. "It is best to look for confirmation and to combine the harami with other longer-term patterns" | 10 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Containment | second body inside first body | shadow may extend beyond (some traders reject) | 9, 10 |
| Colours | opposite (preferred) | same colour allowed | 9 |
| Reliability | low alone | "doesn't always live up to its hype" | 10 |
| Follow-up | often several days of "congestion" or "consolidation" | | 10 |

**Key quotes**
- "A harami is a two-session reversal pattern" [p. 9]
- "It is not essential for the two candles to be opposite colours, but this tends to give a more reliable" [p. 9]
- "A harami on its own says “the chart MIGHT reverse.”" [p. 10]
- "It is best to look for confirmation and to combine the harami with other longer-term patterns." [p. 10]

**Pseudocode**
```
inside = top[i] < top[i-1] and bot[i] > bot[i-1]       # strict containment of bodies; ASSUMPTION strict
bull_harami = DOWNTREND(i-1) and red[i-1] and LONG(i-1) and green[i] and SMALL(i) and inside
bear_harami = UPTREND(i-1) and green[i-1] and LONG(i-1) and red[i] and SMALL(i) and inside
# ASSUMPTION confirmation: bull needs C[i+1] > H[i]; bear needs C[i+1] < L[i]; then G-ENTRY / G-EXIT
```

**Ambiguities & assumptions**: Text is internally uneven on colour (not essential vs preferred). ASSUMPTION: require opposite colours (the more reliable form). "Small" undefined. ASSUMPTION: SMALL(i). Confirmation rule not specified beyond "look for confirmation". ASSUMPTION as in pseudocode. The cheat sheet restates the bullish harami as a reversal indicated by contained opposite-colour body [p. 22].

### 2.3 Harami cross (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal (bullish or bearish) | 26 |
| Timeframe & holding period | "most accurate on a daily chart" | 26 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | First candle "brings the market to the high or low" (i.e. a move to an extreme) | 26 |
| Setup conditions | Next candle is a doji lying inside the range of the previous real body | 26 |
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
| Timeframe | daily | | 26 |
| Containment | doji inside the previous real body | | 26 |

**Key quotes**
- "The next candle is a doji which lies inside the range of the real body of the previous candle." [p. 26]
- "This is another turning point candlestick pattern which most accurate on a daily chart." [p. 26]

**Pseudocode**
```
cross_harami_bull = DOWNTREND(i-1) and red[i-1] and LONG(i-1) and DOJI(i) and top[i] < top[i-1] and bot[i] > bot[i-1]
cross_harami_bear = mirror (UPTREND, green first candle)
# bull: G-ENTRY next open; bear: exit signal
```

**Ambiguities & assumptions**: "inside the range of the real body" could mean the doji's whole range (H-L) or just its body; ASSUMPTION: the doji body is inside the first body (with a doji, body is tiny, so the two nearly coincide). The first candle's size and colour are not stated. ASSUMPTION: long, in the trend's direction. No confirmation stated; ASSUMPTION: none required.

### 2.4 Hammer and Hanging Man (Rose, with the contrary version in the 21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle reversal | 11 |
| Timeframe & holding period | Not found in this text (examples are EUR/USD and FTSE 1-minute) | 11, 12 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Hammer: "found in a downtrend"; hanging man: same shape "found in an uptrend" | 11, 12 |
| Setup conditions | "long lower wick, short body, and little or no upper wick"; lower wick "at least two times longer than the body"; colour not required, but green/white hammer and red/black hanging man are stronger | 11, 12 |
| Entry trigger & order type | "wait for next candle to confirm that buyers are in control" (hammer); example confirmed by a green candle opening above the hammer's body; hanging man: next candle confirms | 11, 12 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lower wick / body | >= 2x | "the longer, the better" | 11 |
| Upper wick | little or none | | 11 |
| Optional confirmer | Stochastics oversold (hammer) / overbought (hanging man) in the examples | no thresholds | 11, 12 |
| 21-pattern guide hammer | price moves lower after open, rallies to close "significantly higher than the low"; "at the start or during a decline" | | 34 |

**Key quotes**
- "Strictly speaking, the lower wick should be at" [p. 11]
- "A hammer: is found in a downtrend, and signals a bullish reversal." [p. 11]
- "As with all single candlestick patterns, we should wait for next candle to" [p. 11]
- "A hanging man: is the same shape as hammer, but found in an uptrend." [p. 12]
- "It forms when the price drops after opening to form a long shadow, then price rallies to close at the highs of the" [p. 36]

**Pseudocode**
```
hammer_shape = lower[i] >= 2*body[i] and upper[i] <= 0.1*rng[i] and body[i] > 0   # ASSUMPTION 0.1
hammer       = DOWNTREND(i) and hammer_shape and C[i+1] > C[i] and O[i+1] > top[i]  # confirmation per Rose example; ASSUMPTION
hanging_man  = UPTREND(i) and hammer_shape and C[i+1] < bot[i]                       # ASSUMPTION confirmation
hammer -> G-ENTRY; hanging_man -> G-EXIT
```

**Ambiguities & assumptions**: Contradiction. Rose (p. 12 and cheat sheet p. 22) treats the hanging man as bearish in an uptrend. The 21-pattern guide (p. 36) calls the hanging man "an indication of a market ready to rally! Showing a bullish impulse" and describes it as closing at the candle's high, which in practice is the same shape as the hammer. ASSUMPTION: follow Rose (bearish, uptrend context) as it is consistent between two pages and with the cheat sheet; treat p. 36 as an author error. The 21-pattern guide (p. 34) also says a hammer can occur "during" a decline (not only at the low). ASSUMPTION: require the DOWNTREND filter. The exact confirmation test (next candle's colour/gap) is only illustrated. Wick thresholds beyond 2x are not given.

### 2.5 Inverted Hammer and Shooting Star (Rose, with 21-pattern guide variants)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle reversal | 13 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Inverted hammer: "after a downtrend or at the bottom of a period of consolidation"; shooting star: "after an uptrend or at the top of a period of consolidation" | 13 |
| Setup conditions | Small body; upper wick at least twice the body; lower wick negligible; body colour does not matter | 13 |
| Entry trigger & order type | Inverted hammer: "The reversal isn’t confirmed until you have a bullish candle in the next period" | 13 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Shooting star: "a trader should close any long positions or get ready to short the market" (21-pattern guide) | 38 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Upper wick / body | >= 2x | | 13 |
| Lower wick | negligible | | 13 |
| Shooting star open (21-pattern guide) | gaps higher on open, rallies to a high, closes only slightly above the open | | 38 |
| Inverted hammer (21-pattern guide) | "at the end of a decline"; text says it closes "significantly lower than the low" (garbled) | | 35 |

**Key quotes**
- "the body size is small, that the upper wick is" [p. 13]
- "The reversal isn’t confirmed until you have a bullish" [p. 13]
- "It is signaling that a top is in place and a trader" [p. 38]

**Pseudocode**
```
star_shape = upper[i] >= 2*body[i] and lower[i] <= 0.1*rng[i] and SMALL(i)    # ASSUMPTION
inv_hammer    = DOWNTREND(i) and star_shape and green[i+1] and C[i+1] > H[i]  # ASSUMPTION confirm
shooting_star = UPTREND(i)   and star_shape                                     # exit signal for longs
```

**Ambiguities & assumptions**: The 21-pattern guide's inverted-hammer text ("close significantly lower than the low") is self-contradictory; ASSUMPTION: follow Rose's shape. Only the inverted hammer has a stated confirmation (bullish next candle); none for the shooting star. The 21-pattern guide's shooting star requires an opening gap, which Rose does not. ASSUMPTION: no gap required (looser).

### 2.6 Engulfing, bullish and bearish (Rose; 21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal | 14 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Bearish engulfing at the end of an uptrend; bullish at the end of a downtrend | 41 |
| Setup conditions | "The body of the second must engulf the body of the first, and must be the opposite colour"; first candle smaller (small real body); second long, ideally short shadows | 14, 41 |
| Entry trigger & order type | Not found in this text (no confirmation required) | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Engulf test | second body engulfs first body | | 14 |
| Strength gauge | number of prior candles swallowed; "The more ‘swallowed candles’, the more powerful" | no numbers | 41 |

**Key quotes**
- "An engulfing pattern signals a reversal, and can be bullish or bearish." [p. 14]
- "The strength of the reversal can be gauged based on how many of the previous candles that the engulfing candle" [p. 41]
- "This is on of the strong reversal candlestick patterns." [p. 41]

**Pseudocode**
```
bull_eng = DOWNTREND(i-1) and red[i-1] and green[i] and top[i] >= top[i-1] and bot[i] <= bot[i-1] and body[i] > body[i-1]
bear_eng = UPTREND(i-1)   and green[i-1] and red[i] and top[i] >= top[i-1] and bot[i] <= bot[i-1] and body[i] > body[i-1]
swallowed = count of prior bars k where top[k]<=top[i] and bot[k]>=bot[i], contiguous back from i-1   # strength score
```

**Ambiguities & assumptions**: Whether body-edge equality counts as engulfing is unstated; ASSUMPTION: allow equality. Rose notes the bearish example "could indicate a reversal or period of stagnation" [p. 14]. Entry confirmation not stated. ASSUMPTION: none.

### 2.7 Piercing Line and Dark Cloud Cover (Rose; 21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Two-candle reversal, weaker than engulfing | 17 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Piercing line occurs in a downtrend; dark cloud cover in an uptrend | 17 |
| Setup conditions | Piercing: strong red candle, then a candle opening below its close and closing above the midpoint of the previous candle. Dark cloud: red candle opens above the previous candle's close, then retreats below its midpoint | 17 |
| Entry trigger & order type | Not found in this text. Authors say only "cause to pause": a minor top or bottom, or consolidation, may follow | 17 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Penetration of first body | "at least halfway" (midpoint) | "The further the close ... cuts into the body ... the more valid" | 17 |
| First candle | strong/long; dark cloud per 21-pattern guide: long green | | 17, 40 |
| Second candle open | piercing: below the first close (21-pattern guide: "at new lows"); dark cloud: above prior close (21-pattern guide: "opens higher") | | 17, 40, 42 |

**Key quotes**
- "it should close at least halfway into the real body of" [p. 17]
- "As a reversal signal, these are not as strong as engulfing candles." [p. 17]
- "The next candle opens higher but reverses and declines, the candle then closes below the center of the first candle." [p. 40]
- "The next candle opens at new lows but rallies to close at a point which ‘pierces through the centerline of the" [p. 42]

**Pseudocode**
```
mid = (O[i-1]+C[i-1])/2
piercing = DOWNTREND(i-1) and red[i-1] and LONG(i-1) and O[i] < C[i-1] and C[i] > mid and C[i] < O[i-1]
dark_cloud = UPTREND(i-1) and green[i-1] and LONG(i-1) and O[i] > C[i-1] and C[i] < mid and C[i] > O[i-1]
depth = (C[i]-C[i-1])/(O[i-1]-C[i-1])  # for piercing: higher depth = stronger
```

**Ambiguities & assumptions**: Rose's dark cloud description says "a red candle opens above the previous candle’s closing price" [p. 17], the 21-pattern guide says the first candle is long green [p. 40]. ASSUMPTION: first candle in the trend direction, long. "Not completely engulf" implies close within the body (above O[i-1] for piercing); coded that way. "New lows" (p. 42) vs "opens below its close" (p. 17): ASSUMPTION: use "opens below the first close" (looser; Rose).

### 2.8 Morning Star and Evening Star (Rose)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle reversal | 15 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Previous bar a strong bar in the direction of the trend (down for morning star, up for evening star) | 15 |
| Setup conditions | Morning star: strongly down candle; second candle small real body not touching the prior real body; third strongly up. Evening star is the reverse. Cheat sheet: second "gaps below first’s close and trades in a small range" | 15, 22 |
| Entry trigger & order type | Third candle itself completes the pattern; Rose's own example text says the following strong candle "confirms" the signal | 15 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Star body | "small", must not touch the first real body (gap) | | 15 |
| First/third candle | "strongly" down/up | not quantified | 15 |
| Reliability | "among the most reliable candlestick signals" | | 15 |

**Key quotes**
- "The morning star and the evening star patterns are among the most" [p. 15]
- "candle that is strongly down. The second candle’s real body" [p. 15]
- "should be small and should not touch the prior candle’s real" [p. 15]

**Pseudocode**
```
morning = DOWNTREND(i-2) and red[i-2] and LONG(i-2) and SMALL(i-1) and top[i-1] < bot[i-2] and green[i] and LONG(i)
evening = UPTREND(i-2) and green[i-2] and LONG(i-2) and SMALL(i-1) and bot[i-1] > top[i-2] and red[i] and LONG(i)
# morning -> G-ENTRY next open; evening -> G-EXIT
```

**Ambiguities & assumptions**: "Strongly" is unquantified (LONG used). The third candle's required depth into candle 1 is not given by Rose; the 21-pattern guide's midpoint close rule is in 2.9 and is NOT assumed here. Rose's chart paragraph labels an evening-star example as confirming "the morning star signal" [p. 15], an apparent slip; the shape rule is unaffected.

### 2.9 Morning/Evening Star variants with doji or short-body middle candle (21-pattern guide)
Four entries in the guide share one rule set, differing only in the middle candle (doji vs short real body), so they are grouped here.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle reversal (Morning Star Doji, Evening Star Doji, Morning Star, Evening Star) | 28, 29, 32, 33 |
| Timeframe & holding period | "three day pattern" (daily) | 28, 32 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Morning: first candle is a clear downtrend candle with long body; evening: uptrend, long body | 28, 29 |
| Setup conditions | Day 2 opens lower (morning) / higher (evening) than day 1 and trades in a "very narrow price range" (doji version) or with a "short real body" (non-doji version); day 3 reverses | 28, 29, 32, 33 |
| Entry trigger & order type | Day 3 "should close at or above the midpoint of the first" (morning) / "at or below the midpoint" (evening) | 28, 29 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Day-3 close | >= midpoint of day-1 body (morning) / <= midpoint (evening) | | 28, 29 |
| Day-2 body | doji (-Doji versions) or short real body | | 28, 32 |

**Key quotes**
- "The last day reverses prices higher and should close at or above the midpoint of the first." [p. 28]
- "And the last day reverses lower and should close at or below the midpoint of the first candle." [p. 29]
- "Similar to the doji version, except the middle candle has a short body." [p. 32]

**Pseudocode**
```
mid1 = (O[i-2]+C[i-2])/2
morning2 = DOWNTREND(i-2) and red[i-2] and LONG(i-2) and O[i-1] < C[i-2] and (DOJI(i-1) or SMALL(i-1)) and green[i] and C[i] >= mid1
evening2 = UPTREND(i-2) and green[i-2] and LONG(i-2) and O[i-1] > C[i-2] and (DOJI(i-1) or SMALL(i-1)) and red[i] and C[i] <= mid1
```

**Ambiguities & assumptions**: "Opens lower" is vs the prior close (ASSUMPTION). Midpoint is of day-1's real body (ASSUMPTION; text says "midpoint of the first" candle). Note a 21-pattern guide page for the plain Morning/Evening star has no gap requirement, in contrast to Rose's non-touching bodies in 2.8; both versions are recorded and may be tested separately.

### 2.10 Three White Soldiers and Three Black Crows (Rose)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle continuation/reversal (strong momentum) | 16 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Crows "within an upward trend"; soldiers "within a downtrend" | 16 |
| Setup conditions | Three long red (black) candles with lower and lower closes (crows); three strong green (white) candles (soldiers); cheat sheet: "Three long white sessions with higher closes each day" | 16, 22 |
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
| Number of candles | 3 | | 16 |
| Candle size | "long"/"strong" | not quantified | 16 |
| Closes | monotonic: higher (soldiers) / lower (crows) | | 16, 22 |

**Key quotes**
- "Three long red (or black) candlesticks with lower and lower closes appear" [p. 16]
- "They show powerful selling action which strongly suggest that more selling is" [p. 16]
- "three strong green (or white)" [p. 16]

**Pseudocode**
```
soldiers = DOWNTREND(i-3) and all(green[k] and LONG(k) for k in i-2..i) and C[i-2]<C[i-1]<C[i]
crows    = UPTREND(i-3)   and all(red[k]   and LONG(k) for k in i-2..i) and C[i-2]>C[i-1]>C[i]
```

**Ambiguities & assumptions**: Opening location of each candle (within the previous body or not) is not stated by Rose (the 21-pattern guide's version is 2.11). Rose's example is a crows pattern inside a rising triangle ending in a break of "long-term support at 10536" [p. 16]; no systematic follow-through measurement given.

### 2.11 Three Green Soldiers (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle bullish reversal | 44 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | "signaling an uptrend is about to take off" (so it appears after weakness; trend not defined) | 44 |
| Setup conditions | Three green candles; "each consecutive candle opens within the real body of the previous candle"; each close brings the market to new highs | 44 |
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
| Candles | 3 green | | 44 |
| Open location | within prior real body | | 44 |
| Close | new high each day | | 44 |

**Key quotes**
- "The three candles are green, each consecutive candle opens within the real body of the previous candle." [p. 44]
- "The close of each day brings the market to new highs, signaling an uptrend is about to take off." [p. 44]

**Pseudocode**
```
tgs = all(green[k] for k in i-2..i) and O[i-1] in (bot[i-2],top[i-2]) and O[i] in (bot[i-1],top[i-1]) and C[i-2]<C[i-1]<C[i] and C[i] > max(H[i-10..i-3])  # last clause ASSUMPTION for "new highs"
```

**Ambiguities & assumptions**: "New highs" scope (vs prior bars, vs a 10-day window) unstated. ASSUMPTION: 10-day high. Candle size not stated.

### 2.12 Abandoned Baby (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle reversal ("pretty rare" but "pretty reliable") | 25 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | "can occur at the end of a run in prices" | 25 |
| Setup conditions | Middle candle is a doji that gapped away from the previous candle; the final candle gaps back in the opposite direction; clear gaps between the doji's shadow and the shadows of both the first and third candles | 25 |
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
| Gap definition | doji's shadow does not overlap the shadows of candles 1 and 3 | | 25 |

**Key quotes**
- "It is pretty rare to find, but it is pretty reliable when it does happen." [p. 25]
- "The gaps leave a clear distance between the shadow of the doji candle and both shadows of the first and third" [p. 25]

**Pseudocode**
```
bull_baby = DOWNTREND(i-2) and DOJI(i-1) and H[i-1] < L[i-2] and L[i] > H[i-1]
bear_baby = UPTREND(i-2)   and DOJI(i-1) and L[i-1] > H[i-2] and H[i] < L[i-1]
```

**Ambiguities & assumptions**: Colours and size of candles 1 and 3 are not stated. ASSUMPTION: not required. Gaps are rare in liquid NSE daily data but common in small caps; check frequency. No rule for entry timing beyond G-ENTRY.

### 2.13 Dragonfly Doji (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle reversal | 27 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | "normally appears at reversals" (direction not stated; shape implies bullish, ASSUMPTION) | 27 |
| Setup conditions | Open and close "at or near the high of the day"; shadow can vary but "usually quite long" | 27 |
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
| Open/close vs high | "at or near the high" | not quantified | 27 |
| Claim | "does point to large moves ahead" | | 27 |

**Key quotes**
- "The Dragonfly doji is quite a powerful reversal indicator and does point to large moves ahead." [p. 27]
- "The open and close of the candle are at or near the high of the day." [p. 27]

**Pseudocode**
```
dragonfly = DOJI(i) and (H[i]-top[i]) <= 0.1*rng[i] and DOWNTREND(i)      # ASSUMPTION 0.1, downtrend context
```

**Ambiguities & assumptions**: Direction and trend context are not stated. ASSUMPTION: bullish in a downtrend. Confirmation not stated.

### 2.14 Gravestone Doji (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle bearish reversal / continuation | 30 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | "more often found within the downtrend, signaling that the downtrend is set to continue" | 30 |
| Setup conditions | Shadow any length; open and close "at or near the low of the day" | 30 |
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
| Open/close vs low | "at or near the low" | not quantified | 30 |

**Key quotes**
- "It can be a bearish reversal pattern, but is more often found within the downtrend, signaling that the downtrend is" [p. 30]

**Pseudocode**
```
gravestone = DOJI(i) and (bot[i]-L[i]) <= 0.1*rng[i]      # ASSUMPTION 0.1
if gravestone and UPTREND(i): exit-signal for longs;  if gravestone and DOWNTREND(i): avoid long entries
```

**Ambiguities & assumptions**: The guide gives both a reversal and a continuation reading without a rule to choose. ASSUMPTION: use the trend context as in the pseudocode.

### 2.15 Long-shadow candles (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle directional bias (continuation or lead into move) | 31 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Long top shadow with short lower shadow: buyers dominate. Long lower shadow with short upper shadow: sellers dominate | 31 |
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
| "Long"/"short" shadow | not defined | | 31 |

**Key quotes**
- "Long shadows are on of the more reliable candlestick patterns." [p. 31]
- "Candles with a long top shadow and short lower shadow show us that buyers dominate the market" [p. 31]

**Pseudocode**
```
long_top = upper[i] >= 2*body[i] and lower[i] <= 0.25*upper[i]     # guide says: bullish bias   (ASSUMPTION thresholds)
long_low = lower[i] >= 2*body[i] and upper[i] <= 0.25*lower[i]     # guide says: bearish bias
```

**Ambiguities & assumptions**: Direct contradiction with Rose: a long upper wick is a shooting star / inverted hammer (reversal down or confirmation-needed up) and a long lower wick is a hammer (bullish) [p. 11] [p. 13], whereas the 21-pattern guide says long top shadow = buyers dominate (bullish) and long lower shadow = sellers dominate (bearish) [p. 31]. ASSUMPTION: the guide's p. 31 rule is the opposite of standard interpretation and of Rose; test it as a separate, low-priority variant and flag it as probably transposed. Do not mix with 2.4/2.5.

### 2.16 Spinning Top (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Single-candle indecision / trend-following | 37 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Short real body with equal upper and lower shadows | 37 |
| Entry trigger & order type | Not found in this text. "the market will tend to move away from the spinning top quite rapidly" (direction not stated) | 37 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Shadow equality | "equal upper and lower shadow" | tolerance not given | 37 |

**Key quotes**
- "So it is part of the trend following group of candlestick" [p. 37]
- "The candle forms with a short real body and an equal upper and lower shadow." [p. 37]

**Pseudocode**
```
spinning = SMALL(i) and body[i]>0 and abs(upper[i]-lower[i]) <= 0.25*rng[i]    # ASSUMPTION tolerance
# ASSUMPTION: after a spinning top in an uptrend, expect continuation: hold; test next-day direction vs prior trend
```

**Ambiguities & assumptions**: Direction after the pattern is not specified; "trend following group" is read by ASSUMPTION as continuation of the prior trend. Rose's cheat sheet has no spinning top.

### 2.17 Upside Gap Two Crows (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle bearish pattern that usually signals a corrective move within an uptrend | 39 |
| Timeframe & holding period | "3 daily candles" | 39 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Uptrend (implied by "corrective reversal within an uptrend") | 39 |
| Setup conditions | Long green day 1; day 2 opens with an upward gap and has a small real body; day 3 long red that engulfs day 2, but closes above day 1's open | 39 |
| Entry trigger & order type | Not found in this text; the guide says it is "hard to trade" | 39 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Day-3 close | above open of day 1 | | 39 |

**Key quotes**
- "therefore it is hard to trade but can be used more as an indication the the trend is set to" [p. 39]
- "The final candle is a long red candle which engulfs the second candle, but the close of the day remains above the" [p. 39]

**Pseudocode**
```
utc = UPTREND(i-2) and green[i-2] and LONG(i-2) and O[i-1] > H[i-2] and SMALL(i-1) and red[i] and LONG(i) and top[i-1]<=O[i] and bot[i-1]>=C[i] and C[i] > O[i-2]
# Use as a trend-continuation tag, not an entry (per guide)
```

**Ambiguities & assumptions**: Whether "upward gap" is to the high or the close of day 1 is unstated (ASSUMPTION: above day 1's high). Contradictory role: listed as bearish but used as a continuation indicator. ASSUMPTION: no trade signal, tag only.

### 2.18 Candlestick Sandwich (21-pattern guide)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Three-candle bullish reversal | 43 |
| Timeframe & holding period | "three day’s action" | 43 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text (reversal implies preceding weakness) | - |
| Setup conditions | Two red candles surround one green candle; closes of both red candles "must be very close" | 43 |
| Entry trigger & order type | Not found in this text. Close level acts as "a support base to trade off" | 43 |
| Initial stop-loss | Not found in this text (implied: below the support base) | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Closes of red candles | "very close" | not quantified | 43 |

**Key quotes**
- "The pattern forms with two red candles surrounding one green candle in the middle, creating a sandwich!" [p. 43]
- "The closing prices of both red candles must be very close, this action creates a support base to trade off." [p. 43]

**Pseudocode**
```
sandwich = red[i-2] and green[i-1] and red[i] and abs(C[i]-C[i-2]) <= 0.003*C[i]     # ASSUMPTION 0.3%
if sandwich: support = C[i]; go long next open; stop = support*(1-0.01) # ASSUMPTION
```

**Ambiguities & assumptions**: No trend, size, or gap conditions given. ASSUMPTION: require DOWNTREND(i-2). The text says "bullish reversal" for a pattern whose third candle is red, so the entry may be taken on the following bar. ASSUMPTION: enter only if C[i+1] > C[i].

### 2.19 Moving-average position as bullish/bearish regime (decks)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend filter / regime | 67, 68 |
| Timeframe & holding period | Not found in this text (decks mention yearly down to 1-minute periods) | 64 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | This IS the regime rule: smaller MA above larger MA = bullish; below = bearish | 67 |
| Setup conditions | Two-MA version (p. 67 table) and single-MA version: price below a moving average, only shorts; price trending higher, longs; below the 10-period MA, no long | 67, 68 |
| Entry trigger & order type | "Smaller MA which is below larger MA beginning to rise and cross over above larger MA": "Time to enter long positions"; order type not found | 67 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Smaller MA above larger "beginning to fall and cross over below larger MA": "Caution to be careful with your long (Buy position)". MAs "can help you gauge when to exit a trade and help limit your risk" | 67, 69 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Single-MA length | 10-period (example for the no-long rule) | "pick one moving average and stick with it" | 68 |
| MA type | not stated for the position rule | SMA or EMA | 64, 46 |
| Smaller/larger pair | not stated | 50/200 SMA widely used; 5/35 EMA | 66, 49 |

**Key quotes**
- "If the stock is currently trading below a moving average then you clearly should only take on a short position" [p. 68]
- "When a stock is below its 10-period moving average under no circumstances, one should take a long position." [p. 68]
- "Do yourself a favor, pick one moving average and stick with it." [p. 68]
- "Moving averages are not the holy grail of trading." [p. 69]

**Pseudocode**
```
bull_regime = SMA(C,50)[i] > SMA(C,200)[i]          # ASSUMPTION pair
long_allowed = C[i] > MA10[i]  (rule p.68)  and (bull_regime if two-MA variant)
# Use as filter on other 2.x long signals: block longs when C[i] <= SMA(C,10)[i]
```

**Ambiguities & assumptions**: The decks state both a two-MA and a one-MA rule without choosing. ASSUMPTION: test both separately. Which MA length (other than the 10-period example) is unspecified. ASSUMPTION: 10 and 50/200. "Should only take on a short position" is not usable in NSE cash for overnight (section 5); ASSUMPTION: treat as "no long".

### 2.20 Moving-average crossover signals, including the sideways-market caveat (decks)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following crossover | 66 |
| Timeframe & holding period | Not found in this text. Illustrated on 15-minute HUL (NSE) charts | 58 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | "Sideway Market No Profit In M_A.Crossover StrategY" (OCR of slide, noisy) | 72 |
| Setup conditions | Short-term MA crossing the longer-term MA: "Usually cross over of the moving average lines gives clue to the trend of the price either towards bullish side or bearish side" | 66 |
| Entry trigger & order type | Buy signal at the shorter MA crossing above the longer; sell signal at crossing below (slide has "Buy Signal" and "Sell Signal" labels); order type not found | 67, 71 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Opposite crossover (caution/exit long) | 67 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Common pair | 50-day and 200-day SMA | "Many traders prefer to use the combination of moving averages" | 66 |
| Chart example | 20 SMA and 20 EMA each vs 50 SMA on HUL 15-min | | 58, 59 |
| Slide 70 labels (OCR garbled) | SMA 50 = short-term trend; SMA 100 = medium-term trend (inferred); "Below SMA 200 in Down Trend" | OCR unreliable | 70 |

**Key quotes**
- "Usually cross over of the moving average lines gives clue to the trend of the price either towards bullish side or bearish side." [p. 66]
- "Smaller MA which is below larger MA beginning to rise and cross over abovelarger MA" [p. 67]
- Slide labels (OCR) read Sell Signal and Buy Signal [p. 71]

**Pseudocode**
```
fast, slow = SMA(C,50), SMA(C,200)         # ASSUMPTION pair (the only pair named for SMA crossovers)
buy  = fast[i-1] <= slow[i-1] and fast[i] > slow[i]
sell = fast[i-1] >= slow[i-1] and fast[i] < slow[i]
# optional sideways filter (ASSUMPTION): skip buy if abs(slow[i]-slow[i-20])/slow[i] < 0.02
```

**Ambiguities & assumptions**: No thresholds for "sideways" are given. ASSUMPTION: slope filter above. Test on EMA and SMA versions separately. Slide p. 70 OCR is unusable for parameter extraction. The p. 58-59 OCR shows both "20EMAcrossing50sma" and "20 SMA crossing 50sma" markers on HUL 15-minute charts, apparently illustrating that the EMA crosses earlier; no outcome numbers.

### 2.21 EMA 5/35 crossover and SMA 50/200 crossover systems (EMA deck)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following crossover (John Murphy quote) | 49 |
| Timeframe & holding period | 5/35 EMA "short-term"; 50/200 SMA "medium-term, perhaps even long-term" | 49 |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Not found in this text (see 2.20 for the sideways caveat) | - |
| Setup conditions | EMA lengths: 5-20 short-term trend, 50 medium term, 100-200 long term | 49 |
| Entry trigger & order type | Not stated; the quoted passage only names the systems. By the crossover logic of 2.20 | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text. Intraday remark: "Entry can be slow" with SMA, EMA "exit has to be fast" | 57 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Short-term EMA pair | 5-day and 35-day | 5-20 for short-term trend | 49 |
| Medium/long pair | 50-day and 200-day SMA | 100-200 long term | 49 |
| EMA multiplier | 2/(N+1) | N=10 gives 0.1818 | 47 |

**Key quotes**
- "A system using a 5-day EMA and 35-day EMA would be deemed short-term." [p. 49]
- "A system using a 50-day SMA and 200-day SMA would be deemed medium-term, perhaps even long-term...... John Murphy" [p. 49]
- "Short moving averages are like speedboats - nimble and quick to change." [p. 48]

**Pseudocode**
```
ema5, ema35 = EMA(C,5), EMA(C,35)
enter_long when ema5 crosses above ema35;  exit when ema5 crosses below ema35         # ASSUMPTION
sma50, sma200 = SMA(C,50), SMA(C,200); same logic as second system                   # ASSUMPTION
# EMA seed = SMA(first N closes); EMA_t = (C_t - EMA_{t-1})*2/(N+1) + EMA_{t-1}      # per p.46-47
```

**Ambiguities & assumptions**: The source describes the systems only by length; it gives no entry/exit text, so the crossover trigger is an ASSUMPTION (the text elsewhere supports crossovers as buy/sell signals [p. 67] [p. 71]). The deck's own remark that the 5/35 pair is short-term and the 50/200 is medium/long-term is the only parameter evidence. EMA seeding by SMA matters for early bars only.

### 2.22 Moving averages as support and resistance (EMA deck)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Support/resistance bounce | 52 |
| Timeframe & holding period | Not found in this text | - |
| Universe / eligibility filters | Not found in this text | - |
| Market / regime filter | Uptrend for support; downtrend for resistance | 52 |
| Setup conditions | Short-term uptrend "might find support near the 20-day simple moving average"; long-term uptrend near the 200-day SMA; SMAs "may be better suited" than EMAs to identify support/resistance | 50, 52 |
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
| Short-term support MA | 20-day SMA | | 52 |
| Long-term support MA | 200-day SMA | "most popular long-term moving average" | 52 |
| MA type | SMA | EMA less suited | 50 |

**Key quotes**
- "Moving averages can also act as support in an uptrend and resistance in a downtrend." [p. 52]
- "In fact, the 200-day moving average may offer support or resistance simply because it is so widely used." [p. 52]
- "simple moving averages may be better suited to identify support or resistance levels." [p. 50]

**Pseudocode**
```
uptrend = SMA(C,20)[i] > SMA(C,50)[i]                                # ASSUMPTION regime
touch   = L[i] <= SMA(C,20)[i]*1.005 and C[i] > SMA(C,20)[i]         # ASSUMPTION band 0.5%
buy at next open if uptrend and touch;  stop = L[i]; symmetric for 200 SMA
```

**Ambiguities & assumptions**: No definition of "near" support, no entry or exit. All numeric values here are ASSUMPTION.

## 3. Risk & money-management rules

The bundle contains no position-sizing, per-trade risk, stop-loss distance, drawdown or exposure rule. What is stated:
- Candlesticks "are not best used in isolation. Combine them with simple pieces of technical analysis" [p. 20].
- Moving averages "can help you gauge when to exit a trade and help limit your risk" [p. 69].
- Intraday: SMA is slow and steady; EMA is fast, "exit has to be fast as we have to save our money" [p. 57].
- Generic disclaimer: "never risk more than you can afford to lose" [p. 21].
- Not found in this text: risk per trade, max positions, stop distance, targets, pyramiding.

## 4. Non-codable guidance and definitions

- Candle anatomy: a candle shows what happened over the period, not only the open or close; line charts suit the big picture [p. 3] [p. 6].
- Quick test: dark cloud cover down, morning star up, three black crows down [p. 4].
- Marubozu: long candle with no wicks; green/white = strong buyer conviction, red/black = eager sellers; in practice may have a short wick; cheat sheet [p. 22] calls it "Continuation: a sign that the trend is maintaining momentum" [p. 22]. Codable only with an assumed wick threshold; not given its own 2.x because no entry rule exists.
- Doji definition (equal open/close) is in 2.1 and [p. 24].
- Candlestick pattern spotting "can be addictive"; do not lose sight of other technical analysis [p. 20].
- History (Homma, Sakata rules, Nison 1991) is background only [p. 19].
- 21-pattern guide's claim of accuracy from "statistical studies" is unsupported in the text [p. 23].
- EMA formula (definition): seed with SMA of N periods; multiplier 2/(N+1) (0.1818 for N=10); EMA = (Close - previous EMA) x multiplier + previous EMA [p. 46] [p. 47]. SMA: sum of N closes divided by N; the deck's worked 10-day example runs 5.5, 6.5, 7.5, 8.5, 9.5 [p. 64] [p. 65].
- MA lag: longer MAs lag more ("speedboats" vs "ocean tankers"); EMAs turn before SMAs [p. 48] [p. 50]; IBM chart illustrates the 50-day EMA turning up ahead of the 50-day SMA [p. 51].
- The four "pillars" listed: Moving Averages, MACD, Stochastic, Bollinger Band; no rules given [p. 63].
- Indicator discussion: indicators confirm and simplify but lag [p. 53] [p. 54] [p. 56]; "Every indicator has a vulnerability" [p. 56]; "Each trader must find indicators that work for them and produce a profit" [p. 53].
- Mentor quote: "Market is maya" (mentor unnamed) [p. 62].
- Rose's chart commentary uses Stochastics overbought/oversold as confirmation but gives no levels [p. 11] [p. 12].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily OHLC (adjusted) for all patterns and MAs; volume is mentioned only in passing and not required; no delivery %, index or fundamentals required. Intraday (15-minute) data would be needed to mimic the HUL examples [p. 58]; we have daily only.
- **Testability with our data:** All rules are backtestable on 2005-2026 daily OHLC once thresholds are assumed; candle-pattern and MA edge can be measured as forward-return event studies on ~3,700 stocks. Intraday claims (EMA vs SMA for intraday, 1-minute examples) cannot be tested. No fundamentals involved. Index filter, if used, via NIFTYBEES or an equal-weight panel index (pre-2024).
- **Market-structure differences:**
  - No overnight shorting in cash: bearish patterns (harami, hanging man, shooting star, dark cloud, evening star, crows, gravestone, upside gap two crows) are used only as exit/avoid signals. ASSUMPTION.
  - Circuit limits and illiquid small caps create artificial gaps and dojis, distorting abandoned baby, upside-gap, and star patterns. ASSUMPTION: restrict to stocks with traded value above a minimum (for example top 500 by 60-day turnover).
  - Costs: STT, brokerage and ~0.1% slippage will swamp short-hold pattern edges; ASSUMPTION: report results net of costs and for 5-, 10- and 20-day holds.
  - Entry at next open (G-ENTRY) is realistic; same-day-close entries are not.
  - Timeframe for the daily-only data: all patterns tested on daily candles (explicit for harami cross and upside gap two crows).

## 6. Verdict

- **Codeability:** Partly. Pattern shapes are describable, but "long", "small", "trend", "confirmation" and every exit are undefined; only EMA/SMA formulas and MA position/crossover logic are precise.
- **Priority for backtesting:** Low-Medium. No author performance evidence; Rose himself says patterns are unreliable alone. A cheap event-study across all patterns is worthwhile, and MA crossover (2.20/2.21) and MA-filter (2.19) are the most useful to test as filters on other systems.
- **Top 3 things a coder is most likely to get wrong:**
  1. Taking textbook definitions of thresholds (body/wick ratios, trend) as the authors' own, when only Rose's 2x wick rule is stated.
  2. Mixing the contradicting sources: hanging man bearish (Rose, p. 12) vs bullish (p. 36), and long-shadow bias (p. 31) vs hammer/shooting star (pp. 11, 13), and opening-gap requirements in star patterns (2.8 vs 2.9).
  3. Coding short signals on NSE cash, and trading the "sideways market" crossover failure (p. 72) without a regime filter.
