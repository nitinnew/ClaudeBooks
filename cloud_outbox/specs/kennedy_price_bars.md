# How To Trade the Highest Probability Opportunities: Price Bars and Chart Patterns — Jeffrey Kennedy (Elliott Wave International eCourse book, 2009; webinar of Oct 22, 2008)

- **Source file:** Google Drive `Jeffrey Kennedy - How To Trade the Highest Probability Opportunities_ Price Bars and Chart Patterns.pdf` (file id `1GTwVTqwW_jupge1D2lrVf7XP3kFsThS8`, 3,436,070 bytes), 47 PDF pages with a text layer.
- **Text file used:** text/kennedy_price_bars.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index; printed page = PDF page − 2). Always take N from the marker.
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/kennedy_price_bars.md text/kennedy_price_bars.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Every page read sequentially, [[PAGE 1]] to [[PAGE 47]]. This revision (correction 4) re-read the whole text before rewriting.
  - Nothing was skimmed or skipped.
  - Figures are images and not readable; the caption text beside each figure was read, and the rules are taken from that text.
  - Ch. 6 Q&A includes an Elliott-wave corrective-channel example [p. 43–44]. It is discretionary and is captured in section 4.
  - [[PAGE 47]] is the colophon (publisher, ISBN).

## 1. The method in brief

Kennedy teaches "technical analysis in its purest form": no Elliott waves, indicators or trendlines, only open-high-low-close bars [p. 3].

**Three steps before every trade** [p. 32]:
1. **Identify the trend from swings.** Higher highs and higher lows mean up; lower highs and lower lows mean down; sideways means neutral, where you stand aside [p. 4–5, 9, 19].
2. **Map natural support and resistance:**
   - prior highs and lows;
   - congestion zones;
   - hard and soft gaps, measured from the close of the bar before the gap [p. 12–15, 43].
3. **Read the substructure of the price bars** to time the end of countertrend moves [p. 32]:
   - where the close sits in the bar's range;
   - inside and outside bars;
   - double key reversals and his own named patterns: Arrow, Popgun, failed new high/low, and The Zone.

**Key and critical levels.** Within a trend, the most recent swing is the "key" level and the swing before it is the "critical" level. A break of key means "protect profits / raise stops"; a break of critical means the trend has changed [p. 8–11].

**Timeframe and evidence.** The method is timeframe-agnostic, from 1-minute to monthly [p. 26]. The author prefers 5-minute over 1-minute bars for intraday trading [p. 45]. Evidence is chart examples only: 2008 futures (Dow/S&P/Nasdaq minis, soybeans, sugar, coffee, cocoa), US stocks (Apple, Microsoft, T3 Energy, Forrester) and EUR/USD. No statistics are given. The only quantified outcome is the Microsoft Popgun, entered at about 29 for a move to nearly 38 [p. 37].

**Exits.** Every setup has a defined next-bar entry and initial stop. No profit target or exit rule is given anywhere in the book beyond the key/critical swing-level framework (2.7) [p. 11, 41].

## 2. Strategies

Common definitions, used by every subsection below:

- **Bar:** a bar of any period (O, H, L, C) [p. 20].
- **Inside bar:** H < previous H and L > previous L, strictly. "It can’t be equal to a prior bar’s high/low." [p. 46]
- **Outside bar:** H > previous H and L < previous L, strictly [p. 24, 46].
- **Entry convention:** the trigger is always a *close* beyond a level, and entry is on the next bar [p. 33, 36, 38, 40, 41].

### 2.1 Multiple inside bars breakout

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout (volatility contraction → expansion) | 24–25 |
| Timeframe & holding period | Any timeframe ("one-minute price chart, a weekly, or a monthly"). Holding period not specified | 33 |
| Universe / eligibility filters | Any market (examples: e-mini Nasdaq 100, EUR/USD) | 28, 34 |
| Market / regime filter | Short side only "if the larger trend is down". The long side has no trend qualifier in the text. Neutral trend: "do nothing" | 19, 33 |
| Setup conditions | A "main" (mother) bar whose range encompasses the following bars. "Three or four" contained bars [p. 33]; "no less than three" [p. 45] | 33, 45 |
| Entry trigger & order type | Long: first close above the mother bar's high (the "setup bar" or "breakout bar"), then enter on the next bar. Short: first close below the mother bar's low, then enter on the next bar | 33 |
| Initial stop-loss | Long: the low of the bar preceding the setup bar. Short: the high of the bar preceding the setup bar | 33, 34 |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Not specified for this setup. General framework: protect profits on a key-level break; trend change on a critical-level break (see 2.7) | 11 |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Minimum contained (inside) bars | 3 | "three or four" in the schematic; a 5-min example uses "Double inside price bars (two price bars contained within the range of one)" | 33, 29, 45 |
| Inside-bar strictness | strict new extremes | equality not allowed | 46 |
| Trigger | close beyond mother high/low | — | 33 |
| Stop reference | bar preceding the setup bar | — | 33 |

**Key quotes**
- "Once prices close above the high of the bar that encompasses the subsequent bars, then you have a green light for the buy side." [p. 33]
- "You place your initial protective stop at a low of the bar preceding the setup bar." [p. 33]
- "As soon as you see the initial close below the low, that’s the green light to take a short position if the larger trend is down." [p. 33]
- "Enter on the next bar and set your initial protective stop at the high of the bar preceding the breakout, or setup, bar." [p. 33]
- "I like to see no less than three price bars for the multiple inside bar setup." [p. 45]

**Pseudocode**
```
inside_of(j, m) = H[j] < H[m] and L[j] > L[m]                 # strictly within mother bar m (p.46)
for each bar t:
    m = t - k  for the largest k >= 4 such that inside_of(j, m) for all j in m+1 .. t-1
    if count(m+1 .. t-1) >= 3:                                 # p.45
        if C[t] > H[m]:  enter_long  at O[t+1]; stop = L[t-1]  # setup bar = t (p.33)
        if C[t] < L[m] and trend(t) == DOWN:
                         enter_short at O[t+1]; stop = H[t-1]  # p.33
exit: see 2.7 overlay (ASSUMPTION)
```

**Ambiguities & assumptions**
- **Containment test.** The text says the bars are "encompassed by" the mother bar but does not say whether each child is inside its immediate predecessor or only inside the mother. ASSUMPTION: each child must be strictly inside the mother bar only.
- **Two contained bars.** The 5-minute example counts two contained bars as a valid signal [p. 29], but the Q&A says at least three [p. 45]. ASSUMPTION: use ≥3, the explicit answer; test 2 as a variant.
- **Trend filter is asymmetric.** It is stated only for the short side [p. 33]. ASSUMPTION: apply the trend filter symmetrically (longs only when trend ≠ DOWN), per "trade in the direction of the trend" [p. 5].
- **No exit is defined.** ASSUMPTION: use the 2.7 key/critical overlay (move the stop to the key swing level once one forms beyond entry; exit on a close beyond the critical level).

### 2.2 Double key reversal

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal | 25–26, 34 |
| Timeframe & holding period | Any (examples: daily S&P 500, British Pound, 1-min e-mini Nasdaq). Holding period not specified | 27–28, 34 |
| Universe / eligibility filters | Any market | 27, 34 |
| Market / regime filter | None stated. The S&P examples are in a downtrend; the British Pound example follows a short-term uptrend | 27, 34 |
| Setup conditions | Bullish: the bar makes a new low below the previous bar but closes above the prior two closes. Bearish: a new high above the previous bar, with the close below the prior two closes ("the lowest close of the three price bars") | 26, 34, 35 |
| Entry trigger & order type | Option 1: enter on the next bar ("sell the open" for shorts). Option 2 (short example): wait for "confirmation", a close below the low of the key-reversal bar, then enter | 34, 35 |
| Initial stop-loss | Long: the low of the key-reversal bar. Short: its high; "a few more ticks" beyond is optional | 34, 35 |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Not specified (see 2.7) | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Closes compared | prior 2 closes | single key reversal = prior 1 close (author relies "more on multiple signals") | 26–27 |
| Entry | next bar open | or on a confirmation close beyond the KR bar's opposite extreme | 34–35 |
| Stop buffer | 0 | "a few more ticks" optional | 35 |

**Key quotes**
- "In a double bearish key reversal, prices make a new high, but the close is below the prior two closes." [p. 26]
- "A double key reversal occurs when markets make a new low below the previous bar but the close of that bar is above the prior two closes." [p. 34]
- "Once you see a double key reversal developing, look to go long on the next bar and make the low of the key reversal bar your protective stop." [p. 34]
- "That’s a signal to sell the open while placing the protective stop at the high." [p. 35]
- "Or you could wait until you have confirmation, which would be a close below the low of the key reversal bar, and then enter at that point again with a stop at the high." [p. 35]
- "I rely more on multiple signals rather than just the single key reversals." [p. 27]

**Pseudocode**
```
bull_dkr(t) = L[t] < L[t-1] and C[t] > max(C[t-1], C[t-2])
bear_dkr(t) = H[t] > H[t-1] and C[t] < min(C[t-1], C[t-2])
variant A (immediate):  bull -> long at O[t+1], stop L[t];  bear -> short at O[t+1], stop H[t]
variant B (confirmed):  bear -> first later close < L[t] (within N bars, ASSUMPTION N=3) -> short at O[next], stop H[t]
                        bull -> first later close > H[t] (mirror, ASSUMPTION) -> long at O[next], stop L[t]
```

**Ambiguities & assumptions**
- **"New low below the previous bar".** Read literally, L[t] < L[t−1]; it is not required to be a swing low. ASSUMPTION: the literal one-bar comparison; test a "lowest low of N bars" variant.
- **Confirmation variant.** It is described only for the short side [p. 35]. ASSUMPTION: mirror it for longs, with a 3-bar validity window.
- **The DKR is a reversal pattern but no trend filter is stated.** ASSUMPTION: test with and without requiring the DKR to be against the short-term swing direction.

### 2.3 Popgun

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout (contraction then expansion) | 25 |
| Timeframe & holding period | Any. Intraday, he values 5-minute signals over 1- or 2-minute ones. A 1-min signal "may lead to only a five- or an eight-minute move"; a 5-min signal "may yield a 25-minute move or a 40-minute move" | 45 |
| Universe / eligibility filters | Any market (examples: Dow Jones, E-mini Dow 5-min, Microsoft daily, British Pound) | 27, 29, 34, 37 |
| Market / regime filter | None stated | — |
| Setup conditions | An inside bar followed immediately by an outside bar; strict new extremes | 25, 36, 46 |
| Entry trigger & order type | Bullish: a close above the high of the outside bar, then enter on the next bar. Bearish: the first close below the low of the outside bar, then enter on the next period | 36 |
| Initial stop-loss | Long: the low of the outside bar. Short: the high of the outside bar | 36 |
| Exits: profit-taking | Not specified (Microsoft example: entered ~29, moved to ~38 "over the next few weeks") | 37 |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pattern | inside bar then outside bar | — | 25 |
| Trigger | close beyond the outside bar's high/low | — | 36 |
| Stop | outside bar's opposite extreme | — | 36 |
| Preferred intraday bar | 5-minute | 1- and 2-minute valid but weaker | 45 |

**Key quotes**
- "The Popgun (shown on the right) is simply an inside bar followed by an outside bar" [p. 25]
- "Then comes a close above the high of the outside bar (marked with a black arrow and text)." [p. 36]
- "Enter your trade on the next position and put your initial protective stop at the low of the outside bar." [p. 36]
- "You will place your initial protective stop at the high of the outside bar." [p. 36]
- "we would have entered at about 29 for a move up to nearly 38 over the next few weeks." [p. 37]

**Pseudocode**
```
inside(i)  = H[i] < H[i-1] and L[i] > L[i-1]
outside(i) = H[i] > H[i-1] and L[i] < L[i-1]
if inside(o-1) and outside(o):                         # o = outside bar
    for t in o+1 .. o+W:                               # ASSUMPTION W = 5 bars validity
        if C[t] > H[o]: long  at O[t+1]; stop = L[o]; break
        if C[t] < L[o]: short at O[t+1]; stop = H[o]; break
```

**Ambiguities & assumptions**
- **How long the setup stays valid** after the outside bar is not stated. ASSUMPTION: 5 bars; cancel if the opposite trigger fires first.
- **Inside bar relative to what.** "Inside bar followed by an outside bar" leaves open whether the outside bar must engulf the inside bar only (its predecessor) or also the bar before. ASSUMPTION: the standard one-bar comparison for each.

### 2.4 Arrow

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | breakout (nested contraction) | 25 |
| Timeframe & holding period | Any (example: S&P daily). Holding period not specified | 28, 39 |
| Universe / eligibility filters | Any market | 28 |
| Market / regime filter | None stated. He prefers additional confirmation, e.g. an Elliott triangle implying "the larger trend is up" for a bullish Arrow | 46 |
| Setup conditions | Four bars. Bar one (the latest) is an inside bar of bar two; bar two lies within the combined range of bars three and four (the two bars before it) | 25, 28, 38 |
| Entry trigger & order type | Long: a close above the high of bar four, then go long on the following bar. Short: "the close below bar three" (example: "close clearly below the low of bar three"), then enter on the next bar | 38, 39 |
| Initial stop-loss | Long: the low of the inside bar (bar one). Short: the high of the inside bar (bar one) | 38, 39 |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified. He warns the S&P example's risk "would probably be quite huge and violate most money management rules" | 39 |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Bars in pattern | 4 | — | 25, 28 |
| Long trigger | close > high of bar four | — | 38 |
| Short trigger | close < (low of) bar three | — | 38, 39 |
| Stop | opposite extreme of bar one (the inside bar) | — | 38 |

**Key quotes**
- "The innermost bar of an Arrow (shown on the left) is an inside bar" [p. 25]
- "The second bar’s high is below the previous combined high, and the second bar’s low is above the previous combined low." [p. 25]
- "First, there is an inside bar (bar one) encompassed by bar two, which, in turn, is encompassed by the combined range of bars three and four." [p. 38]
- "On the buy side, once you see the Arrow form, you look for a close above the high of bar four." [p. 38]
- "you will set your initial protective stop at the low of the inside bar, bar one." [p. 38]
- "When prices close clearly below the low of bar three, you would look to initiate your position." [p. 39]

**Pseudocode**
```
# bars in time order: b4 = t-3, b3 = t-2, b2 = t-1, b1 = t   (b1 latest)
combined_high = max(H[t-3], H[t-2]); combined_low = min(L[t-3], L[t-2])
arrow(t) = inside(t)                                    # b1 inside b2
       and H[t-1] < combined_high and L[t-1] > combined_low   # b2 within b3+b4 (p.25)
if arrow(t):
    for s in t+1 .. t+W:                                # ASSUMPTION W = 5
        if C[s] > combined_high: long  at O[s+1]; stop = L[t]; break   # ASSUMPTION see below
        if C[s] < combined_low:  short at O[s+1]; stop = H[t]; break
```

**Ambiguities & assumptions**
- **Long and short triggers use different bars.** The long trigger is the high of bar four, the short trigger the low of bar three [p. 38–39]. With bars numbered backwards in time, bars three and four are simply the two earlier bars, so the asymmetry looks like an artefact of the schematic. ASSUMPTION: trigger on the combined range of bars three and four (max high / min low) for both directions. Test the literal version (bar-four high for longs, bar-three low for shorts) as a variant.
- **"Bar two encompassed by bar two's predecessor".** The p. 25 wording says bar two lies within "the combined range of the prior two bars", not inside bar three alone. ASSUMPTION: the combined-range test, as coded.
- **No risk cap is defined.** The text only calls a wide stop "huge" [p. 39]. ASSUMPTION: skip the trade if (entry − stop) > 2 × ATR(14); test with and without.

### 2.5 Failed new low / failed new high

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | reversal (failed retest of an extreme) | 39–40 |
| Timeframe & holding period | Any (example: 5-minute Dow mini). Holding period not specified | 40 |
| Universe / eligibility filters | Any market | 40 |
| Market / regime filter | None stated | — |
| Setup conditions | Long: price makes a low (the "low bar"), bounces, then comes back to make "another moderate new low". Zone = from the low bar's low down to (low − the low bar's range). The new low must stay within that zone; "if prices were to push beyond that range, I would stand aside". Short: mirror with the "high bar", zone = high + the high bar's range | 39, 40 |
| Entry trigger & order type | Long: after price pushes into the zone, a close above the high of the low bar, then join on the next bar. Short: a close below the low of the high bar, then enter on the next bar | 39, 40 |
| Initial stop-loss | Long: "the low of the low bar". Short: "the high of the high bar" | 40 |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Zone depth | 1 × range of the extreme bar | example: range 5 points → zone 5 points | 39–40 |
| Trigger | close beyond the extreme bar's opposite end | — | 39, 40 |
| Invalidation | price goes beyond the zone → stand aside | — | 40 |

**Key quotes**
- "The reason I call them failed new lows is that prices come down, make a new low, bounce, and then make another moderate new low." [p. 39]
- "To trade this kind of retest, take the range of the price bar of the previous low." [p. 39]
- "You might join the trade on the next bar, placing the initial protective stop at the low of the low bar." [p. 40]
- "Now, if prices were to push beyond that range, I would stand aside, because it means that something else is going on." [p. 40]
- "Enter on the next bar and place your initial protective stop at the high of the high bar." [p. 40]

**Pseudocode**
```
# long side
LB = most recent swing-low bar (ASSUMPTION: 5-bar pivot low: L[LB] = min(L[LB-2..LB+2]))
rng = H[LB] - L[LB]; zone_bottom = L[LB] - rng
after a bounce (ASSUMPTION: some bar after LB with H > H[LB]):
    wait for a bar r with L[r] < L[LB]                    # the "moderate new low"
    if any L[j] < zone_bottom for j >= r: cancel          # beyond zone -> stand aside (p.40)
    first later close C[s] > H[LB]: long at O[s+1]
        stop = L[LB]  (literal, p.40)  |  ASSUMPTION variant: min(L[r..s])
# short side mirrors with swing-high bar HB, zone_top = H[HB] + (H[HB]-L[HB])
```

**Ambiguities & assumptions**
- **The literal stop is below the original low**, but price has already traded below that low inside the zone, so the stop could be hit immediately or already be above market [p. 40]. ASSUMPTION: test both the literal stop at the original low and a stop at the new extreme low (or the zone bottom).
- **Swing and bounce are visual.** "Sizeable moves", "major swings that look distinct" [p. 7, 45]. ASSUMPTION: a 5-bar pivot, plus a bounce defined as a later bar's high above the low bar's high.
- **Mislabelled figure.** The text points to "Figure 5-13" for the failed-new-low example, apparently meaning Figure 5-14 [p. 39].
- **Trigger reference.** The p. 40 summary says "closing above the high of the low bar"; the Figure 5-16 caption says the same [p. 40]. The text does not say which bar after the new low must close above it. ASSUMPTION: the first close above the high of the original low bar.

### 2.6 The Zone (pullback into an extreme bar's range)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-continuation pullback / support–resistance test | 41 |
| Timeframe & holding period | Any (example: mini Dow futures intraday). Holding period not specified | 42 |
| Universe / eligibility filters | Any market | 42 |
| Market / regime filter | None stated. The schematic shows price making a low, rallying, then pulling back | 41 |
| Setup conditions | Long: prices "pull back into the range of the low bar of the preceding move to the downside". They need not reach the low itself. Short: prices push back up into the range of the prior high bar without making a failed new high | 41 |
| Entry trigger & order type | Long: "As soon as prices close above the range", take the position on the following bar. Short: "prices close below the low", then enter on the next bar | 41, 42 |
| Initial stop-loss | Long: "The low of the previous range". Short: "a stop at the high" | 41, 42 |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Not specified | — |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Zone | range (H–L) of the prior swing-extreme bar | — | 41 |
| Trigger | close beyond the zone (above for longs, below for shorts) | — | 41, 42 |
| Stop | low (long) / high (short) of the zone bar | — | 41, 42 |

**Key quotes**
- "They pull back into the range of the low bar of the preceding move to the downside." [p. 41]
- "As soon as prices close above the range, that’s a green light to go long and take your position on the following bar." [p. 41]
- "The low of the previous range would be your initial protective stop." [p. 41]
- "When prices close below the low of the range, that’s your signal to go short and place your stop at the high." [p. 42]

**Pseudocode**
```
LB = most recent swing-low bar (ASSUMPTION: 5-bar pivot); zone = [L[LB], H[LB]]
after a rally (ASSUMPTION: some bar with C > H[LB] after LB):
    pullback bar p with L[p] <= H[LB] and L[p] >= L[LB]        # enters zone, no new low
    first later close C[s] > H[LB]:  long at O[s+1]; stop = L[LB]
short mirror: HB swing-high bar; push into [L[HB], H[HB]] without H > H[HB]; close < L[HB] -> short, stop H[HB]
```

**Ambiguities & assumptions**
- **Which bar's range.** "The low bar of the preceding move to the downside" is not tied to a swing algorithm. ASSUMPTION: the bar holding the most recent 5-bar pivot low.
- **Pullback that undercuts the low.** If it does, the setup becomes 2.5 (failed new low). ASSUMPTION: zone entries that print below L[LB] are routed to 2.5.

### 2.7 Swing-structure trend, key/critical levels (regime filter and exit overlay)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | trend-following regime / stop management | 4, 8 |
| Timeframe & holding period | Trend "is a function of time"; choose the chart timeframe that matches your holding horizon | 6, 7, 43 |
| Universe / eligibility filters | Any market | — |
| Market / regime filter | Uptrend: higher highs and higher lows. Downtrend: lower highs and lower lows. Neutral (sideways between prior highs and lows): no position | 4, 5, 9, 19 |
| Setup conditions | Mark the last two swings: the most recent swing low (uptrend) is "key", the swing before it is "critical". Mirror for downtrends (key / critical resistance) | 8 |
| Entry trigger & order type | Trade only in the trend's direction ("If the trend is up, the long side needs to be played"). Entries come from 2.1–2.6. A break of critical resistance in a downtrend "signals the development of a new uptrend" | 7, 11 |
| Initial stop-loss | n/a (overlay) | — |
| Exits: profit-taking | Break of the key level: "lock in profits, protect open profits or even raise your stops" | 11 |
| Exits: trailing / time / signal | Break of the critical level means "the beginning of a new trend" (exit / stand aside or reverse) | 8, 10, 11 |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Swings tracked | 2 (key, critical) | — | 8 |
| Swing size | visual ("sizeable moves", "major swings that look distinct") | ignore small moves | 7, 45 |
| S/R tolerance | "within just a few percentage points" of the prior extreme still counts | — | 12 |

**Key quotes**
- "an uptrend is a series of higher highs and higher lows, and that a downtrend is a series of lower highs and lower lows." [p. 4]
- "In other words, go back two swings." [p. 8]
- "Usually, a price move that goes that far indicates the beginning of a new trend." [p. 8]
- "Then, as a trader, your appropriate actions would be to lock in profits, protect open profits or even raise your stops." [p. 11]
- "If the trend is up, the long side needs to be played." [p. 7]
- "If prices are moving sideways in a neutral trend, remind yourself to do nothing." [p. 19]

**Pseudocode**
```
swings = zigzag(H, L, threshold)        # ASSUMPTION: threshold = 2 x ATR(14) (or 5% on daily stocks)
trend = UP   if last two swing highs rising and last two swing lows rising
        DOWN if both falling ; else NEUTRAL
in an open long (trend UP):
    key = most recent swing low; critical = the swing low before it
    on close < key:      stop = max(stop, L of breaking bar) (ASSUMPTION "raise stop") or take partial profit
    on close < critical: exit long; trend := NEUTRAL/DOWN
mirror for shorts with swing highs
```

**Ambiguities & assumptions**
- **Swing identification is visual and timeframe-dependent** [p. 7, 45]. ASSUMPTION: an ATR-based zigzag (2 × ATR(14)); test 1.5–3 × ATR.
- **"Protect profits / raise stops" is not quantified.** ASSUMPTION: on a key-level break, move the stop to the low of the breaking bar; on a critical-level break, exit.
- **Break definition.** "Take out" is undefined (intrabar vs close). ASSUMPTION: a close beyond the level, consistent with the close-based entries.

### 2.8 Close-location bar bias (next-session direction)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | short-term continuation (bar-structure forecast) | 21–22 |
| Timeframe & holding period | Next session ("the next trading session", "the following day"); also monthly bar → next month | 22, 23 |
| Universe / eligibility filters | Any market | — |
| Market / regime filter | Used to time entries within the trend at the end of corrective phases | 32 |
| Setup conditions | Bull bias: the close is in the upper 20% of the bar's range; or the open and close are both in the upper part of the range; or the open is at the low and the close at the high. Bear bias: the mirror (lower 20% or 10%; open = high). Indecision: open and close near each other at mid-range | 21, 22, 23, 31 |
| Entry trigger & order type | No order rule; stated as a forecast ("my bet is that there will be a new high above the close") | 22 |
| Initial stop-loss | Not specified | — |
| Exits: profit-taking | Not specified | — |
| Exits: trailing / time / signal | Not specified (the forecast horizon is the next session) | 22 |
| Position sizing | Not specified | — |
| Adding to / pyramiding | Not specified | — |
| Portfolio limits | Not specified | — |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Close-location band | top/bottom 20% of range | "lower 20% or 10%" | 22 |
| Horizon | next session | next month for a monthly bar | 22, 23 |

**Key quotes**
- "Closes don’t lie, and they are the most important item on the price chart." [p. 21]
- "if markets close in the lower 20% or 10% of a price bar, that means that the bears or the sellers have good control of that market." [p. 22]
- "Conversely, if the markets close in the upper 20 percent, then the buyers, or the bulls, have good control of the market." [p. 22]
- "For instance, looking at the price bar on the left, my bet is that there will be a new high above the close." [p. 22]
- "These types of price bars are common prior to a big move in price or a news event." [p. 23]

**Pseudocode**
```
clv(t) = (C[t] - L[t]) / (H[t] - L[t])          # 0 = close at low, 1 = close at high
bull(t) = clv(t) >= 0.80 ; bear(t) = clv(t) <= 0.20     # 0.90/0.10 variant (p.22)
test: P(H[t+1] > C[t] | bull(t)), P(L[t+1] < C[t] | bear(t)), and next-bar return vs unconditional
use as filter: allow 2.1–2.6 longs only if the setup bar's clv >= 0.5 (ASSUMPTION)
```

**Ambiguities & assumptions**
- **Stated as a probability forecast, not a trading rule.** The outcome test ("new high above the close" vs a higher close) is not defined. ASSUMPTION: measure both, the next-bar high exceeding the close and the next-bar return.
- **Upper and lower "portion" for doji bars are not quantified** [p. 21]. ASSUMPTION: both open and close in the top (or bottom) third of the range.

### Non-codable / no-rule patterns (summary)

| Pattern | What the book says | Why no rule | Page |
|---|---|---|---|
| Single key reversal | New high with close below the prior close (bearish), or mirror | Author relies on double versions | 26–27 |
| Island reversal | A gap one way, a cluster, then a gap back; occurs at turning points | No entry/stop rule given | 26 |
| Double outside bars | Rare; volatility at turning points | No trade rule | 24 |
| Mid-range open/close bars | Indecision, often before big moves or news | Context only | 23, 30, 31 |
| Hard/soft gaps as S/R | A soft gap: low above the prior close; S/R level = the close before the gap | Context for 2.6/2.7 | 14, 43 |

## 3. Risk & money-management rules

- **Defined initial stop per setup:** each setup carries a stop at a bar extreme. No account-level risk-per-trade percentage is given anywhere in the book [p. 33–42].
- **Oversized risk:** avoid setups where the stop distance is excessive; the Arrow example "would probably be quite huge and violate most money management rules" [p. 39].
- **Key/critical swing breaks:** a key-level break means protect profits or raise stops; a critical-level break means a trend change [p. 8, 11].
- **Neutral markets:** "sometimes taking no position at all is actually the most profitable position you can take, particularly if you’re caught in a neutral trend" [p. 9]. A neutral trend means do nothing [p. 19].
- **Position sizing, pyramiding and portfolio limits:** not specified anywhere in the book.

## 4. Non-codable guidance

- Pick the chart timeframe from your holding horizon; trend "is a function of time" [p. 6, 43].
- Support and resistance are ranges, not lines; expect "false pushes, first attempts and second attempts" [p. 16].
- A level matters more the longer it has existed: hours = a little, months = much more [p. 12].
- Former support becomes resistance and vice versa [p. 13, 15].
- Countertrend moves tend to end at prior support (in uptrends) or resistance (in downtrends) [p. 15].
- The Elliott "corrective price channel" (parallel lines off the extremes, plus a midline) is a discretionary supplement [p. 44]. He also checks Elliott patterns before trading the bar patterns [p. 46].

## 5. Adapting to NSE (Indian equities)

- **Data required:** OHLC only.
  - Daily bars for the 2005–2026 NSE stock panel.
  - Intraday 5-minute bars for index futures and F&O stocks, if available.
  - Nifty proxy (NIFTYBEES before 2024) for an index-level trend filter.
- **Testability with our data**
  - 2.1–2.8 can all be **backtested on daily NSE OHLC 2005–2026**: purely price-based, with the swing and zone ASSUMPTIONS.
  - The intraday versions (the author's preferred 5-minute Popgun, Arrow and DKR) need intraday data we may not have.
  - Nothing needs fundamentals.
- **Market-structure differences**
  - **Gap risk.** "Enter on the next bar" = the next day's open on daily bars. NSE opens frequently gap beyond the trigger, so model fills at the open. ASSUMPTION: skip the trade if the open is beyond the initial stop.
  - **No overnight shorting in the cash market.** Short setups (2.1–2.6 short side) can be tested only as intraday trades in cash or as positional trades in F&O stocks/futures. ASSUMPTION: run the daily backtests long-only on the cash panel, and test shorts separately on F&O names.
  - **Circuit limits.** Bars that close at the upper/lower circuit are untradeable at the next open in some cases. ASSUMPTION: exclude signals where the setup bar closed at a circuit limit.
  - **Costs.** Apply STT + brokerage + ~0.1% slippage per side. Many of these setups have tight stops (one bar's range), so costs are a large fraction of risk. ASSUMPTION: require stop distance ≥ 3 × round-trip cost.
  - **Liquidity.** ASSUMPTION: restrict to stocks with 20-day median turnover above a liquidity floor (e.g. ₹5 crore/day) to keep bar patterns meaningful.

## 6. Verdict

- **Codeability:** Fully codable for 2.1–2.6. Partly codable for 2.7 (swing detection must be assumed) and 2.8 (a forecast, not an order rule). Definitions, next-bar entries and stops are precise, but no exits or targets are given.
- **Priority for backtesting:** Medium. The setups are cheap to code and testable on the daily NSE panel. The double key reversal (2.2) and the multiple-inside-bar breakout (2.1) have the clearest rules. Results will depend heavily on the assumed exit (2.7 overlay).
- **Top 3 things a coder is most likely to get wrong**
  1. Allowing equal highs or lows in inside/outside-bar tests. Kennedy requires strict new extremes [p. 46].
  2. Entering intrabar on the breakout. Every setup needs a *close* beyond the trigger, with entry on the next bar [p. 33, 36, 41].
  3. Treating 2 contained bars as a multiple-inside-bar setup, or taking shorts without the downtrend condition [p. 33, 45].
