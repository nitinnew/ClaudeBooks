# Elliott Wave Techniques Simplified — Bennett A. McDowell (McGraw-Hill, 2016; TradersCoach.com; foreword by Stanley Dash)

- **Source file:** Google Drive `ELLIOTT WAVE TECHNIQUES SIMPLIFIED - BENNETT A McDOWELL.pdf` (271 PDF pages with a text layer)
- **Text file used:** text/mcdowell_elliott_simplified.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number; the printed number is roughly PDF page minus 13 in the body, but every N below was taken from the marker)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in running headers, the table of contents or the index.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python ../work/bin/verify_citations.py specs/mcdowell_elliott_simplified.md text/mcdowell_elliott_simplified.txt`.
- **Coverage:** Read the whole text sequentially, lines 1–7960, from `[[PAGE 1]]` to `[[PAGE 271]]` (last page reached: 271). This includes the foreword, introduction, Chapters 1–9, Appendices A and B, the "cheat sheet" page ([p. 221]), the full Glossary ([p. 222]–[p. 259]), Notes, Index and About the Author. Nothing was skimmed. *Coordinator check: the coordinator re-ran verify_citations (40/40 ok) and an exact-page strict check (0 off-by-one). 2.1-2.4 each have the 12 template field rows (2.4 adds a separate MPM score table). 12 unquoted citations were spot-checked by grep and page read: price oscillator 5/35 on the low p.100, 144-bar lookback p.101-102, RSI 9 with 80/20 bands and the ~75% claim p.113, 1.618 Wave 3 target p.64, Wave 4 38.2-61.8% p.65/77, the 70/15/15 retracement stats p.77/84, 2% money-management cap p.243 (glossary) and p.182 (student), student 77% / payout 2.6 p.182 vs table 70.59% / 0.84 p.183, 'subjectivity' p.184, 'fully defined' p.203; all matched.*
  - Blank pages: 1 (empty), 5, 9, 11, 129, 147 ("This page intentionally left blank").
  - Chart-only pages (the chart is an image; only a figure caption is in the text layer, no rules): 74, 75, 86, 88, 90, 91, 95, 103, 105, 107, 108, 110, 111, 112, 115, 116, 118, 121, 123, 124, 125, 126, 127, 135, 136, 137, 138, 140, 141, 142, 143, 145, 155, 156, 157, 161, 162, 163, 168, 169, 170, 176, 177, 179, 180. Page 48 holds only two optical-illusion figure captions. The captions were read and used where they state a rule (for example [p. 86], [p. 88]).
  - Page 183 is a TradeStation performance printout (a table of numbers) and was read in full.
  - Pages 6–7 (contents), 260–261 (notes) and 262–269 (index) contain no rules; they were read but are not used for citations.

## 1. The method in brief

McDowell is a trading coach who sells the ART (Applied Reality Trading) software. He teaches a "classic plus modern" Elliott Wave count. The classic part is price structure (the 5-wave impulse with ABC corrections), Fibonacci retracement and extension zones, and volume by wave [p. 60–61]. The modern part is three indicators: a price-oscillator histogram (the OWL), a 9-period RSI with 80/20 bands (the PTF) and multiple-time-frame alignment [p. 99]. A scoring worksheet, the McDowell Probability Matrix (MPM), turns six judgments (each scored 0–5, total 0–30) into a stated "probability" that a wave count is right [p. 150, 152]. The edge claimed is that Wave 3 is where the bulk of profits are made [p. 14], and that the count can be made less subjective by combining the classic and modern readings [p. 98–99].

The book separates a **forecast** (the Elliott count, called an "ungrounded assessment") from the **trading system** (entries, stops, exits, called "grounded assessments"). The forecast is only meant to filter direction; the entry and stop rules always take priority [p. 131–132]. Elliott counting itself stays discretionary: the book says to pass on any chart without a clear count [p. 144, 171]. The student chapter states that the author "doesn't offer a fully defined trading system with rigid rules" [p. 203]. The only step-by-step rule sets are two chapter-8 trade setups (flat-bottom channel breakout, and "catching Wave 5"), plus scattered wave rules and Fibonacci statistics. Entry and exit signals proper are the proprietary ART Pyramid Trading Point (PTP) signals, which are not defined in enough detail to code [p. 249–251].

**Timeframe and markets:** stated as any market and any time frame, from 1-minute to yearly charts [p. 15–16, 119–120]. Position traders can use end-of-day data [p. 15]. Examples are US stocks, ETFs, futures and the DJIA.

**Evidence and track record (claims only, no backtest in the book):**
- The author says his charts predicted the 2008 one-day 1,000-point DJIA drop [p. 8, 102–106].
- He says he has relied on Elliott Wave for 20 years [p. 15, 153].
- He claims the RSI(9) 80/20 band rule is "approximately 75 percent accurate" [p. 113].
- Wave-statistics percentages (for example, 70% of Wave 4 retracements ending at 38.2–61.8% of Wave 3) are given with no source or sample [p. 77–78].
- A student (Dean Jenkins) reports 2014 results of 77% winners and a payout ratio of 2.6 in the text [p. 182], but his TradeStation printout shows 70.59% winners, profit factor 2.02, 136 trades and a ratio of average win to average loss of 0.84 [p. 183]. The two do not agree.

## 2. Strategies

Ratings: **Fully** = every entry, stop and exit element is stated or has a stated default. **Partly** = entry or stop is stated but a key element is discretionary. Only the two chapter-8 setups and the Wave 3 entry rule come close to codable; the Elliott wave labelling itself needs an `ASSUMPTION:` zigzag proxy.

| # | Strategy | Codable | Pages |
|---|---|---|---|
| 2.1 | Wave 3 entry after a Wave 1–2 (classic rules, zigzag proxy) | Partly | 63–65, 77, 92, 101 |
| 2.2 | Flat-bottom channel breakout (bullish; bearish mirror) | Partly (closest to Fully) | 158–160, 226 |
| 2.3 | "Catching Wave 5" after a Fibonacci Wave 4 (bullish; bearish mirror) | Partly | 78, 85, 160, 164–166 |
| 2.4 | Modern-indicator filters (OWL histogram, RSI(9) 80/20, higher time frame) and the MPM score | Partly (filters, not a standalone trade) | 99–102, 113–120, 150–153 |
| 2.5 | Setups the book describes without codable rules (Wave C of Wave 4, pennant breakout, Wave 1, ART signals) | Not codable | 67–68, 166–167, 223–224, 249–251 |

### 2.1 Wave 3 entry after a Wave 1–2 (classic rules, zigzag proxy)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following (buy the start of Wave 3; Wave 3 is the most tradeable wave) | 14, 65 |
| Timeframe & holding period | Any time frame; Wave 3 is to be treated as a trend trade, not a small swing trade; hold as long as possible, or take profit at the 1.618 target | 64, 65 |
| Universe / eligibility filters | Only charts with a clear count; if the count is not clear, move to another chart | 73, 171 |
| Market / regime filter | Trade only in the direction of Waves 1, 3, 5 on the higher time frame (one Fibonacci degree up); for daily charts the higher frame is weekly (and monthly) | 78, 120 |
| Setup conditions | Wave 2 corrects Wave 1 but never goes beyond the start of Wave 1; Wave 2 retraces 23.6% to 100% of Wave 1 (stats: 15% retrace 23.6–38.2%, 70% retrace 38.2–61.8%, 15% retrace 61.8–100%); volume lower in Wave 2 than Wave 1; histogram pulls back close to zero in Wave 2; Wave 3 not the shortest of 1, 3, 5 | 64, 77, 92, 94, 101 |
| Entry trigger & order type | Wait for price to exceed the final price level of Wave 1; any bar beyond it must be Wave 3 and that is the signal Wave 2 is over. Order type not stated; the book says to base entries and exits on your own entry and exit signals | 64, 77 |
| Initial stop-loss | Not found in this text for a Wave 3 entry (only the invalidation rule that Wave 2 never goes past the start of Wave 1, and the general rule to use stops) | 64, 209 |
| Exits: profit-taking | Draw a Fibonacci extension from the start of Wave 1 to the end of Wave 1 and then the end of Wave 2; target is 1.618 (price can go beyond); stats: Wave 3 is 161.8–175% of Wave 1 in 45% of cases, 175–261.8% in 30%, 100–161.8% in 15%, over 261.8% in 10%. Some students exit all at 1.618; the author also says to hold for the whole wave | 64, 65, 77 |
| Exits: trailing / time / signal | Not found for Wave 3 (the trailing-stop rules in the book are in 2.2 and 2.3). Wave 4 follows Wave 3, so get out during Wave 3 | 64 |
| Position sizing | Trade size set by the distance from entry to stop; never more than 2% of the risk account on one trade (glossary); adjust size when the stop is further away | 85, 233, 243 |
| Adding to / pyramiding | Scale in only if the trade is already profitable; scaling out is 30% of the position when the rules say so | 253 |
| Portfolio limits (max positions, correlation, heat) | Diversify across markets and sectors; no position limit stated | 243 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Wave 2 retracement of Wave 1 | 23.6% to 100% (never beyond start of Wave 1) | 70% of cases 38.2–61.8%; the Figure 4.2 caption says 38.2–100% | 64, 77, 84 |
| Wave 3 target | 1.618 × Wave 1, projected from the end of Wave 2 | other extension levels 1.382, 1.5, 1.618; stats up to 2.618 | 64, 77, 83 |
| Wave 3 length rule | Wave 3 is never the shortest of Waves 1, 3, 5 | - | 92 |
| Volume | Wave 3 has the highest volume; Wave 2 lower than Wave 1 | - | 64, 94 |
| OWL histogram | Wave 3 = highest (or deepest) histogram within last 144 bars | 144 bars | 101, 102 |
| Max risk per trade | 2% of the risk account | - | 243 |
| Scale-out size | 30% of position | - | 253 |

**Key quotes**
- "You must wait for Wave 3 to exceed the final price level of Wave 1." [p. 64]
- "Wave 2 never retraces more than 100 percent of the length of Wave 1." [p. 64]
- "Look for 1.618. That is your target for prices to reach in Wave 3." [p. 64]
- "You want to get out sometime during Wave 3" [p. 64]
- "hold on to your position for as long as possible" [p. 65]
- "Wave 3 cannot be the shortest of the three impulse waves" [p. 92]
- "Always base your trade entries and exits using your own set of trading entry and exit signals." [p. 77]

**Pseudocode** (long side only; `ASSUMPTION:` zigzag proxy for the wave labels; fields used: daily open, high, low, close, volume)
```
params: ZZ = zigzag reversal threshold (ASSUMPTION: 3 * ATR(14), confirmed pivots only)
        TICK = 0.05 INR (ASSUMPTION), RISK_PCT = 0.02, TARGET_MULT = 1.618
        OSC = EMA(low,5) - EMA(low,35)            # ASSUMPTION: OWL histogram, see 2.4
each day t after close, using only pivots confirmed by t:
  take the last three confirmed pivots  P0 (swing low), P1 (swing high), P2 (swing low)   # W1 = P0->P1, W2 = P1->P2
  W1len = P1.high - P0.low
  retr  = (P1.high - P2.low) / W1len
  require P2.low > P0.low                       # Wave 2 never beyond start of Wave 1   [p. 64]
  require 0.236 <= retr < 1.0                   # [p. 64]
  require mean(volume, P1..P2) < mean(volume, P0..P1)   # [p. 64]
  require higher-time-frame (weekly) trend up   # ASSUMPTION: weekly OSC > 0 or weekly close > 30-week SMA  [p. 78, 120]
  arm buy-stop at P1.high + TICK                # Wave 3 begins when price exceeds the end of Wave 1  [p. 64]
on next days: if high >= buy-stop: entry = max(open, buy-stop)
  stop   = P2.low - TICK                        # ASSUMPTION; book gives none for Wave 3
  target = P2.low + TARGET_MULT * W1len         # [p. 64]
  size   = floor(RISK_PCT * equity / (entry - stop))   # [p. 243]
  variant A: sell all at target.   variant B: sell 30% at target [p. 253], trail the rest with the higher-low stop from 2.2 [p. 159]
  cancel the arm if price closes below P2.low before the trigger
```

**Ambiguities & assumptions**
- The book never says how to find the start of Wave 1, only that it "is rarely obvious at its inception" [p. 63]. `ASSUMPTION:` a confirmed zigzag pivot sequence stands in for the count; the result will differ from what the author would label by eye.
- No stop is given for a Wave 3 entry. `ASSUMPTION:` stop one tick below the Wave 2 low; the wider alternative is the start of Wave 1, which is the absolute invalidation level [p. 64].
- Exit: the book gives two incompatible instructions: exit around 1.618 [p. 64] and hold the whole wave [p. 65]. `ASSUMPTION:` test both variants (A and B above).
- The target projection is stated loosely (extension "from the start of Wave 1 to the end of Wave 1, then to the end of Wave 2") [p. 64]. `ASSUMPTION:` target = end of Wave 2 + 1.618 × Wave 1 length.
- The 23.6% lower limit for Wave 2: shallower pullbacks are not addressed. `ASSUMPTION:` ignore them.
- Order type is not stated. `ASSUMPTION:` buy-stop at the Wave 1 high.
- No minimum Wave 3 volume test is given for the entry day. `ASSUMPTION:` none.

### 2.2 Flat-bottom channel breakout (bullish; bearish mirror)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Breakout (base breakout meant to catch Wave 3 of a new trend); also the author's "favorite" setup | 154, 158 |
| Timeframe & holding period | Any time frame and market; the examples are daily charts; ride the trend while stops trail upward | 154, 159 |
| Universe / eligibility filters | Scan for bracketed or channelled markets (the author uses his ART Scanner); the market should be after a big trend down, preferably after a completed bearish Wave 5 | 154, 158 |
| Market / regime filter | None stated beyond the prior big downtrend; oscillator histogram must be bullish at entry (see Setup) | 158 |
| Setup conditions | (1) channel after a big down-trend; (2) channel narrow and at least 20 price bars long (longer and narrower is better); (3) mark resistance (channel top) and support (channel bottom); (4) price breaks above the channel top (the channel breakout); (5) after the breakout, a higher low and then a higher high must form; (6) price-oscillator histogram (or OWL) positive, above zero | 158 |
| Entry trigger & order type | Initiate the trade when price goes above the second higher high (or, with ART software, on a bullish Pyramid Trading Point entry signal). Order type not stated | 158 |
| Initial stop-loss | Below the higher low; or, if close enough, at the low of the channel where the support line is | 158 |
| Exits: profit-taking | Not found in this text for this setup (the book says only that the breakout can give "huge" gains) | 154 |
| Exits: trailing / time / signal | Trail the stop in subsequent higher lows (or use the ART Pyramid Trading Point signals) | 159 |
| Position sizing | Not stated for this setup; general rule: size from entry-to-stop distance, max 2% of account per trade | 233, 243 |
| Adding to / pyramiding | Not found for this setup (general: scale in only when already profitable; the PTP signals are used by the author for scaling) | 253 |
| Portfolio limits (max positions, correlation, heat) | Not found | - |

Bearish mirror [p. 159–160]: channel after a big trend up, preferably after a bullish Wave 5; break below the channel bottom; wait for a lower high and then a lower low; initiate on a break of the second lower low; histogram negative below zero; initial stop above the lower high or at the channel top if close; trail stops in subsequent lower highs.

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Minimum channel length | 20 price bars | longer is better | 158, 226 |
| Channel width | "narrow" (no number) | narrower is better | 158 |
| Breakout reference | channel top (resistance line) | - | 158 |
| Confirmation sequence | higher low, then higher high, entry above second higher high | - | 158 |
| Oscillator filter | price oscillator histogram above zero (settings 5 / 35, source low) | OWL software | 100, 158 |
| Initial stop | below the higher low, or channel low if close | - | 158 |
| Trailing stop | subsequent higher lows | ART PTP exit signal | 159 |

**Key quotes**
- "The channel needs to be narrow and at least 20 price bars long." [p. 158]
- "wait for a higher low and then a higher high after the channel breakout before initiating a trade" [p. 158]
- "The trade should be initiated when prices go above the second higher high." [p. 158]
- "Initial stop-loss goes below the higher low" [p. 158]
- "Trail your stops in subsequent higher lows" [p. 159]
- "A sharp change in price movement after the market has traded sideways for at least 20 price bars." [p. 226]

**Pseudocode** (long side only; fields: daily open, high, low, close, volume)
```
params: N_MIN = 20; NARROW = (channelHigh - channelLow) / mean(close) <= 0.15      # ASSUMPTION: book gives no number
        PRIOR_DROP = close at channel start <= 0.70 * max(close, prior 144 bars)   # ASSUMPTION for 'big trend down'
        TICK = 0.05, RISK_PCT = 0.02
for each stock, each day t:
  find the longest window of >= N_MIN bars ending at t-1 where NARROW holds; chTop = max(high), chBot = min(low)   # [p. 158]
  require PRIOR_DROP                                  # [p. 158]
  breakout bar b = first day with close > chTop       # ASSUMPTION: close basis (book: alarm when price breaks above the line)
  after b: track swing lows and swing highs (3-bar fractals; ASSUMPTION)
  HL = first swing low after b with low > chBot       # 'higher low'  [p. 158]
  H1 = highest high since b                           # first high of the sequence
  armed once HL exists; buy-stop = max(high since b, post-HL swing high) + TICK     # ASSUMPTION: 'second higher high' read as the high that follows the higher low
  require OSC(t) > 0                                  # OWL histogram bullish  [p. 158]
  on trigger: entry = max(open, buy-stop)
  stop = HL.low - TICK  (if (entry - chBot) < (entry - stop) * 1.25 then stop = chBot - TICK)     # 'if close enough' ASSUMPTION
  size = floor(RISK_PCT * equity / (entry - stop))
  trail: stop = max(stop, most recent confirmed swing low - TICK)                # [p. 159]
  exit when low <= stop
  cancel setup if close < chBot before the trigger fires, or 30 bars pass without entry (ASSUMPTION)
```

**Ambiguities & assumptions**
- "Second higher high" is not defined. The sequence is breakout, higher low, higher high, then "go above the second higher high" [p. 158]. Two readings: (a) enter when price exceeds the post-pullback high (the high that follows the higher low); (b) enter when price exceeds a further swing high after two successive higher highs. `ASSUMPTION:` reading (a); test (b) as a variant.
- "Narrow" has no number. `ASSUMPTION:` channel range at most 15% of the mean close.
- "Big trend down" has no number. `ASSUMPTION:` close at the channel start at most 70% of the 144-bar high close.
- "Higher low" relative to what is not stated. `ASSUMPTION:` higher than the channel low.
- No profit target and no sizing rule is given for this setup. `ASSUMPTION:` trailing exit only; sizing by the 2% rule [p. 243].
- Bearish text contains a slip: it says initiate when price goes "above the second lower low" [p. 159]; the sense requires "below". `ASSUMPTION:` below.
- The scanner used by the author (ART Scanner) is not described. The glossary defines a bracketed market as one that has been in a range for more than 20 bars [p. 226].

### 2.3 "Catching Wave 5" after a Fibonacci Wave 4 (bullish; bearish mirror)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Trend-following re-entry (buy the end of a Wave 4 pullback to ride Wave 5) | 160, 164 |
| Timeframe & holding period | Any time frame; the examples are daily charts; stay in until the trailing stop is hit | 160, 165 |
| Universe / eligibility filters | A clearly identified recent Wave 3 (bullish for longs); scan for candidates | 164 |
| Market / regime filter | Trade only in the direction of Waves 1, 3, 5 on the higher time frame (one Fibonacci degree up); price-oscillator histogram bullish | 78, 164 |
| Setup conditions | (1) identify the most recent bullish Wave 3; (2) draw the Wave 4 retracement zone using the end of Wave 2 and the end of Wave 3; (3) wait for a pullback into the 38.2% to 61.8% zone; (4) if it does not reach the zone or exceeds 75%, do not trade; (5) look for bullishness to return; (6) histogram positive; (7) draw the Wave 5 extension zone 61.8% to 100%; (8) wait for a higher low then a higher high after the Wave 4 low | 164 |
| Entry trigger & order type | Initiate when price goes above the second higher high (or on an ART bullish Pyramid Trading Point entry signal); the earlier summary says take the trade when momentum comes back and takes out a key level of resistance. Order type not stated. Require at least 2:1 reward-to-risk against the Wave 5 target zone | 160, 164, 165 |
| Initial stop-loss | Below the bottom of Wave 4, or the most recent key support formed after Wave 4; summary rule: one tick on the other side of Wave 4. Alternative for entries made at the Wave 4 retracement itself: stop around or beyond the 61.8% retracement, with smaller size | 78, 85, 160, 165 |
| Exits: profit-taking | The Wave 5 target zone is the 61.8%–100% extension (anchors: end of Wave 2, end of Wave 3, end of Wave 4); stats: 70% of Wave 5s end 61.8–100%, 15% end 38.2–61.8%, 15% end 100–161.8%; lock in profit before the target zone is reached | 78, 85, 164 |
| Exits: trailing / time / signal | Trail under key support levels, especially after Wave B (in Wave 4) is breached; once inside the Wave 5 target zone, trail with the three-bar-back stop (stop at the low of the third bar to the left of current prices) and exit 100% when price falls below that low (or on an ART exit signal) | 165 |
| Position sizing | Size from the stop distance; if the stop is beyond the 61.8% retracement the size must be lowered; max 2% of the account per trade | 85, 233, 243 |
| Adding to / pyramiding | Once sure you are in Wave 5, add to the position using any grounded assessment signal | 78 |
| Portfolio limits (max positions, correlation, heat) | Not found | - |

Bearish mirror [p. 165–166]: most recent bearish Wave 3; bullish correction into the 38.2–61.8% zone; bearish momentum returns; histogram negative; lower high then lower low; initiate below the second lower low; stop above the top of Wave 4; trail above key levels; three-bar-back stop at the high of the third bar; exit 100% on a break of that high.

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Wave 4 retracement zone | 38.2% to 61.8% of Wave 3 (anchors: end of Wave 2, end of Wave 3) | 15% shallower (23.6–38.2%), 15% deeper (61.8–76.4%); beyond 76.4% usually means a Wave 2, not a Wave 4 | 77, 87 |
| No-trade limit | pullback outside the zone or beyond 75% | - | 164 |
| Wave 5 extension zone | 61.8% to 100% (anchors: end of Wave 2, end of Wave 3, end of Wave 4) | 0.618, 1.0, 1.618 levels | 78, 85, 87 |
| Minimum reward-to-risk | 2:1 | author calls 3:1 excellent | 160, 252 |
| Trailing stop in target zone | three-bar-back | ART exit signal | 165 |
| Oscillator filter | histogram above zero (long) | - | 164 |

**Key quotes**
- "If the retracement does not reach the high probability target zone or exceeds 75 percent, do not trade" [p. 164]
- "I suggest at least a 2:1 reward-to-risk ratio." [p. 160]
- "place your stop-loss exit one tick on the other side of Wave 4" [p. 160]
- "Place your initial stop-loss exit below the bottom of Wave 4" [p. 165]
- "trail your stops aggressively using the three-bar-back stop-loss method" [p. 165]
- "set your stop beyond the 61.8 percent retracement level" [p. 85]
- "Failed Wave 5s do occur." [p. 85]

**Pseudocode** (long side only; `ASSUMPTION:` zigzag pivots label the waves)
```
params: ZZ = 3 * ATR(14) zigzag; TICK = 0.05; RISK_PCT = 0.02; MIN_RR = 2.0
find the latest bullish impulse: confirmed pivots  A (end of W2 low), B (end of W3 high)   # W3 = A->B  [p. 164]
  require OSC high within the leg A->B is the highest OSC in the last 144 bars          # 'Wave 3' test  [p. 101]
  require B.high > prior swing high (the Wave 1 top)                                    # ASSUMPTION: W3 exceeds W1
after B: low of the correction Lw4 = lowest low since B
  retr = (B.high - Lw4) / (B.high - A.low)
  invalidate if retr > 0.75                                          # [p. 164]
  require retr >= 0.382  (the pullback must have reached the zone)   # [p. 164]
  after Lw4: wait for a higher low (HL) and then a higher high (HH) with OSC > 0     # [p. 164]
  buy-stop = HH.high + TICK (second-higher-high reading as in 2.2)
  stop = Lw4 - TICK
  Wave5 zone: T_lo = Lw4 + 0.618 * (B.high - A.low);  T_hi = Lw4 + 1.0 * (B.high - A.low)   # 3-anchor extension  ASSUMPTION
  require (T_lo - entry) / (entry - stop) >= MIN_RR        # [p. 160]
  size = floor(RISK_PCT * equity / (entry - stop))
  after entry: stop = max(stop, last confirmed swing low - TICK)
  once high >= T_lo: stop = low of the bar three bars back, updated every bar          # [p. 165]
  exit all when low <= stop
```

**Ambiguities & assumptions**
- The three-point extension is not given as a formula. `ASSUMPTION:` target = end of Wave 4 + ratio × (end of Wave 3 − end of Wave 2), as a standard three-point (trend-based) Fibonacci extension, ratio 0.618 to 1.0.
- The book says the Wave 5 statistics apply to "Wave 3 patterns" in two places [p. 78, 85]; this is read as a typo for Wave 5.
- Stop: three versions (below the bottom of Wave 4 [p. 165]; one tick beyond Wave 4 [p. 160]; beyond the 61.8% retracement for early entries [p. 85]). `ASSUMPTION:` one tick below the Wave 4 low, because the entry is taken after the higher-high confirmation.
- A retracement of 62–75% passes the 75% test [p. 164] but the author calls 61.8–76.4% an exception requiring a re-evaluation [p. 87]. `ASSUMPTION:` allow 38.2–75%.
- "Three-bar-back": the stop sits at the low of the third bar to the left of current prices [p. 165]. `ASSUMPTION:` low of bar t−3 as of each new bar, only ever raised.
- Bearish text slip: exit "if stop trade when prices go above the low of this third price bar" [p. 166] should read the high. `ASSUMPTION:` high.
- Order type and the pre-target stop trail are loosely specified ("key levels of support"). `ASSUMPTION:` confirmed 3-bar swing lows.
- The statistics in the book (70% / 15% / 15%) are asserted without any sample or source.

### 2.4 Modern-indicator filters (OWL histogram, RSI(9) 80/20, higher time frame) and the MPM score

This is a set of confirmation tools, not a standalone entry. It can be coded as filters on 2.1–2.3, and the two indicator claims are testable on their own.

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Filter / confirmation overlay (trend-following) | 99, 132 |
| Timeframe & holding period | Any; the higher time frame should be at least three to five intervals apart (daily to weekly to monthly) | 120 |
| Universe / eligibility filters | Only charts with a clear price structure; otherwise pass | 117, 144 |
| Market / regime filter | Trade only in the direction of the higher-time-frame wave; if the higher frame shows a Wave 3 in force, a daily Wave 4 is a minor Wave 4 | 78, 122 |
| Setup conditions | Price oscillator histogram: Wave 3 has the highest (long) or deepest (short) histogram of the last 144 bars; Wave 5 has a smaller histogram than Wave 3 (divergence); a Wave 4 histogram points in the Wave 4 direction. RSI(9): a close beyond the 80 or 20 band means about 75% chance of a new high or low; Wave 5 usually does not pierce the band; Wave 5 usually ends with RSI between the bands. Volume: Wave 3 highest, Waves 2/4/5 lower | 94, 101, 102, 113, 114, 139 |
| Entry trigger & order type | Not found (the indicators confirm a count; entries come from the user's own system) | 82, 131 |
| Initial stop-loss | Not found | - |
| Exits: profit-taking | Not found | - |
| Exits: trailing / time / signal | Divergence (price new extreme, histogram not) signals trend exhaustion; no mechanical exit given | 101 |
| Position sizing | Not found for the filters; the MPM score is not mapped to size | 153 |
| Adding to / pyramiding | Not found | - |
| Portfolio limits (max positions, correlation, heat) | Not found | - |

**MPM scoring.** Six categories, each scored 0–5 by judgment: (1) price structure clear (classic); (2) oscillator histogram clear (modern); (3) volume correct for each wave (classic); (4) Fibonacci levels holding (classic); (5) RSI clear (modern); (6) multiple-time-frame alignment (modern). Total 0–30 [p. 150]. Interpretation [p. 152]:

| Total score | Label | Stated chance wave count is right |
|---|---|---|
| 0–9 | Minimal | 0–49% |
| 10–13 | Poor | 50–54% |
| 14–18 | Moderate | 55–60% |
| 19–22 | Good | 61–69% |
| 23–27 | High | 70–79% |
| 28–30 | Outstanding | 80–99% |

The author says he cannot give the score at which to trade: "I cannot tell you which score to use for your own personal trading." [p. 153] He only advises against trading a low score.

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Price oscillator short length | 5 | some platforms swap short and long; use the order that gives a positive histogram in bull trends | 100 |
| Price oscillator long length | 35 | - | 100 |
| Price oscillator source | low | - | 100 |
| Plot | histogram | - | 100 |
| Lookback for the Wave 3 histogram extreme | 144 bars | 144 is a Fibonacci number; about 4.8 months of daily bars | 101, 102 |
| RSI length / price | 9 on the close | - | 113 |
| RSI bands | upper 80, lower 20 | Wilder's 70/30 and 80/20 are the standard uses, which the author does not use | 109, 113 |
| RSI band-pierce claim | about 75% chance of higher highs (above 80) or lower lows (below 20); fails 25% of the time | - | 114, 117 |
| Higher time frame pairs | daily to weekly; weekly to monthly; 60-minute to 180-minute or daily | at least 3–5 intervals apart | 119, 120 |
| MPM entry threshold | not given | - | 153 |

**Key quotes**
- "Find either the highest or deepest histogram within the last 144 price bars" [p. 101]
- "RSI length set to 9 on the close" [p. 113]
- "there is approximately a 75 percent chance that higher highs will eventually occur" [p. 114]
- "Wave 5 usually ends on a neutral RSI" [p. 139]
- "A good rule is that if, for whatever reason, you cannot get a clear read on what the count is, don’t trade it." [p. 117]
- "Ungrounded assessments never supersede grounded assessments." [p. 132]

**Pseudocode**
```
OSC  = EMA(low, 5) - EMA(low, 35)                # ASSUMPTION: EMA and absolute (not %) difference; book says only 'price oscillator histogram'  [p. 100]
RSI9 = RSI(close, 9);  UP = RSI9 > 80;  DN = RSI9 < 20      # [p. 113]
W3_bar_long  = argmax(OSC over last 144 bars)    # [p. 101]
W3_bar_short = argmin(OSC over last 144 bars)
divergence_long  = (high_t makes a new high vs the W3 high) and (OSC_t < OSC at W3)       # Wave 5 signature  [p. 101-102]
rsi_continuation_event = first close with RSI9 > 80 after RSI9 was <= 80; test: does price later exceed that bar's high? (book claims ~75%)   # [p. 114]
HTF_ok = weekly OSC sign agrees with the trade direction       # ASSUMPTION; book: trade in direction of higher-frame impulsive wave [p. 78]
MPM: not computable in full (price structure and Fibonacci-hold scores are judgment); proxy score = (OSC rule met) + (volume rule met) + (RSI rule met) + HTF_ok   # ASSUMPTION
```

**Ambiguities & assumptions**
- The oscillator type (simple or exponential averages, absolute or percent) is not stated; the glossary defines the percentage price oscillator histogram as the difference between two moving averages, expressed in percent or absolute terms [p. 248]. `ASSUMPTION:` EMA, absolute difference.
- There is no signal line: the histogram is the oscillator itself. `ASSUMPTION:` as above.
- "Secret settings" are given as 5/35 on the low [p. 100] and RSI 9 with 80/20 [p. 113]; the book sells software (OWL, PTF) that is said to do more [p. 128], and those extras are not described. Not found in this book.
- MPM sub-scores 0–5 have no scoring guide. `ASSUMPTION:` rule-met = 1, not met = 0, scaled to a 4-point proxy.
- Multiple time frame alignment is labelled classic on p. 133 and p. 151 and modern on p. 99, p. 144 and p. 150.
- The RSI 75% claim is a probability that a higher high "eventually" occurs, with no time limit [p. 114]. `ASSUMPTION:` test several horizons (20, 60, 144 bars).

### 2.5 Setups described without codable rules (not codable)

- **Wave C of Wave 4 ("exception to the caution rule").** Enter right after Wave B if the Fibonacci Wave 4 target zone allows a profit on Wave C; the opportunity occurs "when Wave B completely retraces to the final Wave 3 price level"; advanced, needs experience [p. 68]. Wave B is usually 50% of A and below 76.4% [p. 69], which conflicts with a full retracement to the Wave 3 level. Wave C is 1, 1.618 or 2.618 times Wave A [p. 69]. No entry, stop or exit is given. Not codable.
- **Pennant breakout.** Pennants form in Waves 2 and 4; "If you see one in Wave 2, take it" [p. 166]; the break usually follows the direction of Wave 1 [p. 167]. No pennant definition, entry or stop. The book elsewhere tells the reader to stay away from complex corrections [p. 67–68], and pennants belong to complex corrections [p. 71], so the two statements conflict. Not codable.
- **Trading Wave 1, Wave 5 beyond 2.3, or Wave 2 / Wave 4 pullbacks.** The tradable waves are listed as 1, 3, 5 and Wave C of Wave 4 [p. 66, 76]. The book recommends not trading Waves 2 and 4 [p. 67]. No Wave 1 entry rule is given other than the flat-bottom breakout.
- **ART signals.** The ART Pyramid Trading Point (apex = entry, base leg = stop, "confirmed" when price moves beyond the apex) is defined only in the glossary and its calculation is not given [p. 250–251]; neither are the 1B and 2B reversal signals [p. 223–224]. ART bar classification is stated: close in the upper half of the bar is a bull bar, lower half a bear bar [p. 223]; an elongated bar is at least one-third longer than the previous three to five bars [p. 223]. These are codable bar tags but no setup is built on them in this text. The glossary adds that trend exhaustion "generally occurs after four to five consecutive Primary Pyramid Trading Points in the same direction" [p. 258]. Not codable.
- **Fibonacci time extensions** (clusters of vertical time lines at pivots) are said to help find reversals [p. 83, 89]; no numeric rule. The author says Fibonacci studies are "not intended to provide the primary indications for timing trade entries and exits" [p. 82]. Not codable.

## 3. Risk & money-management rules

- Risk no more than 2% of the "risk account" on any one trade; this is the glossary definition of money management, together with proper trade size and diversification across markets and sectors [p. 243]. A student reports never being exposed to more than a 2% loss of his account on any trade [p. 182].
- Trade size comes from the stop distance: "The distance between your entry and your exit will determine what your trade size will be." [p. 233] Pick the exit before entering [p. 256]. The author sells a Trade Size Calculator for this [p. 220]; the formula itself is only in his other book [p. 149].
- If the stop must be further away (for example beyond the 61.8% retracement), lower the position size [p. 85].
- Always use stops and place them before the trade; never move a stop to take a bigger loss [p. 209]. Keep stops in force when a wave count fails [p. 78]. Avoid trades whose count is unclear [p. 144].
- Minimum reward-to-risk of 2:1 for a Wave 5 entry [p. 160]; 3:1 is "excellent" given more winners than losers [p. 252].
- Scale in only when the trade is already profitable; scaling out means exiting 30% of the position when the rules say so [p. 253]. Take profit on a "hyperbolic" move by scaling out [p. 238].
- Even a system that wins only 50% of the time can be profitable with good risk control and larger wins than losses [p. 182].
- Day trading: set a daily loss limit of about three maximum-risk trades [p. 212]; evaluate each trade independently [p. 212]. (Not applicable to the daily-bar setups above.)
- Testing: use the same account size and risk control as in live trading [p. 204]; test on a simulation account before live trading, and retest after every change [p. 205–206]. Paper trade while learning [p. 17].
- The book defers the money-management formulas to the author's other book, A Trader's Money Management System [p. 149]. No drawdown stop, portfolio heat or maximum-position rule is given in this book. Not found in this book.

## 4. Non-codable guidance

- Wave counting is judgment. The author says so himself ("there is always some subjectivity involved") [p. 184], and says that most Elliotticians do not agree on counts [p. 189]. Alternate counts are acceptable when both point the same way and the user's entry system gives a signal [p. 78, 131]; if the alternate count conflicts, scrub the trade [p. 144].
- Skip messy markets: "If you don’t see a clear wave count, then move on to another chart!" [p. 171]. Messy charts are usually complex corrections [p. 146, 171]. Only about 5–10% of scanned charts are interesting enough to analyze [p. 185, 195].
- The Elliott forecast is only a direction filter; entries and stops come from price (grounded assessments) [p. 131–132]. News is peripheral information [p. 192]; avoid target fixation [p. 193].
- Alternation, wave structure of corrections (flat, irregular, triangle) and subwave counts (5-3-5) are described in words with figure examples that are images [p. 67–72].
- Watch-list workflow ("stalking" trades): put a mature Wave 3 on a watch list, set a price alert at the projected Wave 4 zone, then another at the level confirming Wave 5, and re-evaluate when each alert fires [p. 195].
- Psychology: awareness of emotional triggers [p. 56]; paper trade until a profitable rule set exists [p. 57]; do not trade money needed for short-term income [p. 209–210]; do not trade when upset [p. 209]; coaching is recommended [p. 185, 205]. Do not mix in unrelated indicators such as MACD or stochastics [p. 201]; do not system-hop [p. 200].
- The book recommends developing your own entry and exit rules and testing them [p. 203].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - Daily adjusted OHLC and volume for each stock (all of the book's rules use only price and volume).
  - Weekly and monthly bars derived from the daily series for the higher-time-frame filter.
  - A tick size for the "one tick" stop offset (0.05 INR on NSE cash equities is the usual tick; `ASSUMPTION:`).
  - Delivery %, Nifty history and fundamentals are not used by the book.
- **Testability with our data:**
  - Backtestable on 2005–2026 prices: the flat-bottom channel breakout (2.2) once the thresholds are fixed; the Wave 3 entry (2.1) and Wave 5 entry (2.3) only through a zigzag proxy; the OWL histogram and RSI(9) tests (2.4), including the 75% band-pierce claim.
  - Not testable as the author intends: any rule that depends on visual wave labelling, the MPM subjective scores, Fibonacci time clusters and the ART Pyramid Trading Point signals.
  - Delisted stocks are in the panel, which helps because breakouts from long bases often fail and drop out of indexes.
- **Market-structure differences and proposed adaptations:**
  - No overnight shorting in the cash market. `ASSUMPTION:` test only the long (bullish) versions of 2.1–2.3; the bearish mirrors need futures or intraday shorting and are out of scope.
  - Circuit limits: a stock can lock at the upper circuit through a breakout level, so a buy-stop fill at the level may not occur. `ASSUMPTION:` fill at the next day's open if the day opens above the stop, and skip signals on days with a locked circuit.
  - Costs: STT, brokerage and about 0.1% slippage. The wave-based setups are low-turnover on daily bars, so costs matter less, but the 2:1 reward-to-risk filter [p. 160] is measured before costs. `ASSUMPTION:` apply costs to every round trip.
  - Liquidity: small-cap breakouts from tight 20-bar bases are common and often thin. `ASSUMPTION:` require a minimum 20-day median traded value (for example, INR 1 crore) and cap position size at a small fraction of average daily volume. The book gives no liquidity filter.
  - Regime: the book gives no market filter. `ASSUMPTION:` optional test with NIFTYBEES above its 200-day average, kept as a separate variant so it is not blamed on the book.
  - The book's examples are US stocks, ETFs and futures, with the 2000 bear market and 2008 crash as cases [p. 66, 102]. Gaps are common in Indian single stocks; use open-price fills for gap-through stops.

## 6. Verdict

- **Codeability:** Partly. The wave rules (Wave 2 not beyond the start of Wave 1, Wave 3 not the shortest, Wave 4 not overlapping Wave 1 [p. 92]), the Fibonacci zones, the histogram and RSI settings and the two chapter-8 setups can be written as code. The wave labelling that these rules depend on is discretionary, and the proprietary ART entry and exit signals are not specified.
- **Priority for backtesting:** Low to Medium. Medium for the flat-bottom channel breakout (2.2) as a generic 20-bar base breakout with a higher-low confirmation and a higher-low trailing stop. Low for the Elliott-count strategies (2.1, 2.3) because only a zigzag proxy can be tested and the author's statistics are unsourced.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating a zigzag swing sequence as the author's wave count. The author expects a clear five-wave picture and skips messy charts [p. 171], so a mechanical labeller will trade many setups he would reject, and the reported hit rates will not apply.
  2. Misreading the entry sequence "higher low, then higher high, enter above the second higher high" [p. 158, 164], and the oscillator settings (5 / 35 on the low, histogram; reversed on some platforms [p. 100]). Both change which bars qualify.
  3. Mixing up the three Wave 5 and Wave 4 anchor sets: Wave 4 retracement uses the end of Wave 2 and the end of Wave 3; Wave 5 extension uses the ends of Waves 2, 3 and 4 [p. 221]; Wave 3 extension uses the start and end of Wave 1 [p. 221], and the book's own typo ("Wave 3 patterns" for Wave 5 statistics [p. 78]) and bearish-mirror typos [p. 159, 166] should not be copied into code.
