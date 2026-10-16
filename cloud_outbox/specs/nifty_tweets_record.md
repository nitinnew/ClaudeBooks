# Nifty Tweet record – From July '18 to March '19 (12 months record) — Ranajay Banerjee (@ranajayb)

- **Source file:** Google Drive invest/NIFTY Tweets 12 months record.pdf (55 pages)
- **Text file used:** text/nifty_tweets_record.txt  (page basis: pdf_pages (RapidOCR of screenshots)). The PDF's own text layer held only the compiler's "NIFTY level at that date / COMMENTS" lines; the tweets themselves are screenshots, so the coordinator OCR'd every page with RapidOCR. The text file therefore contains both tweet text and compiler comments. OCR quality is poor in places: spaces are often dropped inside tweets (e.g. "Thelogicbehindmytargetof12000"), chart axis labels and numbers appear as noise, and "COMMENTS" is sometimes misread ("cOMMENTS"). Quotes below are verbatim including OCR spacing.
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not any printed page number)
  - N is taken ONLY from the nearest `[[PAGE N]]` marker above the passage.
  - Checked with `verify_citations.py specs/nifty_tweets_record.md text/nifty_tweets_record.txt`.
- **Coverage:** Read lines 1-1388 (the whole text file) in two sequential chunks (1-700, 701-1388), reaching the last marker `[[PAGE 55]]`. Nothing skipped. OCR caveats as above. Pages that are mostly chart-axis noise (the tweet text is a few lines; the rest is repeated chart labels): p. 1, 3, 4 (re-posted 10 Jul chart), p. 13, 14, 16 (2-hour chart), p. 34, 36, 37, 42, 43 (same 11 Nov 30-minute chart re-posted), p. 40, p. 48, 49, 50 (Diametric chart), p. 52, 53, 55 (Feb 2019 daily chart). Chart contents (wave labels, annotated levels) are only partly recoverable; only levels that appear in the tweet text or the compiler comments are used here. Page 21 and p. 54 have no compiler comment. Several tweets carry no "NIFTY level at that date" line (p. 9, 16, 21, 22, 26-28, 30-32, 36-39, 42-44, 47, 49-50, 52-54). *Coordinator check: the text substitutes a full-page RapidOCR pass for the PDF text layer, which held only the compiler's level/comment lines on 32 of 55 pages. The coordinator re-ran verify_citations (19/19 ok) and an exact-page strict check (0 off-by-one). 18 unquoted table citations were spot-checked by grep (levels 11900, 11150-200/11250, 10800, 9700, 10430, 10793, 10740-80, 25150, 78.6%, 61.8%, 11236, 10923, 10105, 11270, among others), plus 8 method-element pages; all matched. Re-tallying the call table gives 18 Hit / 4 Partial / 9 Miss / 2 Unscored over 33 rows, which agrees with section 2.2(d).*

## 1. The method in brief

This is a self-compiled FORECAST TRACK RECORD of about 8 months of public tweets (10 Jul 2018 to 6 Mar 2019, despite the "12 months" in the title), not a rulebook. The author, Ranajay Banerjee, is a discretionary chartist who uses Neowave / Elliott wave counts (triangle corrections, ending diagonals, rising wedges, flats, running corrections, W-X-Y, "Diametric" patterns), support/resistance bands and confluence zones, Fibonacci retracements, price and time symmetry (equal-size legs, C = A, Y = W), analogue comparisons with earlier bear markets (2008, 2010-11, 2015-16), a "Fast Fall" setup using the 20 and 50 EMA, and time calculations. Instruments are Nifty, BankNifty, USDINR and Midcap/Smallcap indices; tweets carry charts from firecharts.blogspot.com [p. 1]. The compiler (not named) appends "NIFTY level at that date" and a COMMENTS line saying what happened next; these comments are the only "results" in the document.

The central story: a 12000 / 11900 target from a triangle count (Jul 2018) [p. 1], a switch to "Bear market possible for next 12 months" on 21 Sep 2018 [p. 7], a correct call of the 10800-900 and 10300-400 breakdowns and the 10005 low [p. 8, 11, 17], a profitable bear-market-rally long from 10420-10 in Nov 2018 [p. 34, 43], then confusion and a bearish stand that failed in Dec 2018 [p. 45-47], and a recovery to 11300 in Feb-Mar 2019 anticipated from 16 Feb [p. 51].

Selection bias warning: the compiler chose which tweets to include and wrote all verdicts afterwards; no one independent verified the list. Many tweets are phrased as conditional ("IF true", "not the only possibility") and many levels are given as zones, so "hit" is generous. The hit/miss tally in 2.2 is my own count of the compiler's comments and is not a statistically meaningful hit rate.

## 2. Strategies

Only one component is even partly codable: the stated level-break / support-resistance / EMA-cross triggers (2.1). The Neowave/Elliott content and the forecast table are discretionary and are recorded in 2.2 as a non-codable note so a reader can compute a hit rate.

### 2.1 Stated level-break triggers (Partly codable proxy; ASSUMPTION: generalised from one-off Nifty levels)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Discretionary swing/support-resistance calls on the Nifty index; codable only as level-break / support-hold triggers | 11, 34 |
| Timeframe & holding period | Days to weeks (targets reached within 1-3 weeks of the 11 Nov 2018 long; "tweet" horizons of 1-3 sessions, 2-3 weeks, 6-8 weeks, months) | 32, 34, 24, 31 |
| Universe / eligibility filters | Nifty 50 index (also BankNifty, USDINR, Midcap 100, Smallcap 100 mentioned); no stock-level rules | 1, 2, 25, 26 |
| Market / regime filter | Bearish scenario stated to survive while Nifty trades below 11900 (as of 21 Sep 2018); bearish stand to be reconsidered on strength above 10740-80 and 20 EMA crossing above 50 EMA negates the "Fast Fall" setup | 7, 46 |
| Setup conditions | (a) Long: 10490 not broken downward, then dip near 10420-10 expected; (b) support zones named in advance (e.g. 10800 +/-20, 10300-400, 10000-9700, 10620); (c) Fibonacci retracement of a small upmove: hold at 61.8% (80% theoretical, not preferred) for the next short-term rally; (d) after weak monthly close, 10850-800 break invites 10300-400 | 34, 15, 11, 24, 51, 28 |
| Entry trigger & order type | Long: buy a dip near 10420-10 (limit/dip-buy implied); Short: "Any recovery towards 11150-200 may invite selling with SL above 11250"; Long (Feb 2019): "Friday long" with SL under 10620 for a rally to 11270-80; confirmation triggers: break below 10490 (Dec 2018), break above 10923 within 2 sessions (Jan 2019) | 34, 11, 51, 53, 45, 48 |
| Initial stop-loss | Long from 10420-10: 40-50 pts; short: above 11250; Feb 2019 long: invalid below 10620 (SL triggered) | 34, 11, 53 |
| Exits: profit-taking | Chart targets 10680 / 10810 / 10910 for the Nov 2018 rally; Jan 2019: 11100 or even 11400; Feb 2019: 11270-80 (spot) / 11290-11300; Nifty ST pullback target 10700 (Oct 2018) | 34, 48, 50, 51, 24 |
| Exits: trailing / time / signal | "Time to follow the rise with tight SL (individual choice)" once the first target (10680) was achieved; no numeric trail given | 37 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text (one remark: buying in wave 2 of C is "safer as SL gets much closer") | 27 |
| Portfolio limits (max positions, correlation, heat) | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Bear-scenario ceiling (Sep 2018) | 11900 | Break below 10800-900 "major boost for the bears" | 7 |
| Support band on 7-8 Sep 2018 | 11310-11230 (typo corrected from 10310-10230) | "THE support" later 11250-30 | 5, 6 |
| Short-entry zone / short SL | Recovery to 11150-200; SL above 11250 | - | 11 |
| Major support Oct 2018 | 10800 +/-20 | 10300-400, then 10000-9700 | 15, 17 |
| Nov 2018 long dip-buy zone | 10420-10 | 10430-20 invited on a break below 10490 | 34, 35 |
| Nov 2018 long stop | 40-50 pts | "tight SL (individual choice)" after first target | 34, 37 |
| Nov 2018 long hold level | 10490 not broken downward | intraday 10540-20 needs to hold, "Below 10520, picture changes" | 34, 36 |
| Nov 2018 targets | 10680 / 10810 / 10910 | 10793 / 10860 / 10927 (2 Nov tweet, different chart) | 34, 30 |
| Fast Fall setup | MA 20-50 around 10700; invalidation 10950 | wait for 20 EMA crossing above 50 EMA to negate | 45, 46 |
| Reconsider-bearish level | Strength above 10740-80 | - | 46 |
| Dec 2018 / Jan 2019 confirmation levels | Break below 10490 (Fri 7 Dec); break above 10923 within next 2 sessions (6 Jan) | Bulls look for break above 10900 | 45, 48, 49 |
| Bull-survives floor (Jan 2019) | Break below 10600 negates new-high chance | - | 48 |
| Feb 2019 pivot | 10620 (Friday low); below = trending move down possible; above = rally to 11270-80 / 11290-11300 | revised to 11236-38 confluence on 6 Mar (low was 10586) | 51, 53, 55 |
| Fibonacci retrace levels watched | 38.2%, 50%, 61.8% (80% theoretical limit) | 78.6% observed in BankNifty | 28, 29 |
| BankNifty trigger | Above 25150, target 25900 or higher; Nifty above 10300, target 10700 | - | 27 |
| Moving averages | 20 EMA, 50 EMA | - | 45, 46 |

**Key quotes** (short, verbatim)

- "bearish scenario survives" [p. 7] (full tweet context: the author says this holds as long as Nifty is below 119o0 in OCR text)
- "Canexpectlargebreakdownonlybelowthatzone." [p. 4]
- "canbeboughtwith40-50ptsSL" [p. 34]
- "TARGETS-10680/10810/10910" [p. 34]
- "Below10520,picturechanges." [p. 36]
- "NowtimetofollowtherisewithtightSL" [p. 37]
- "Need a triggerbefore thinkingof shorts." [p. 43]
- "requiredintheformofabreakbelow10490" [p. 45]
- "Alert: Fast Fall setup in MA 20-50 around 10700." [p. 45]
- "Invalidation point - 10950" [p. 45]
- "Iwouldwaitfor20emacrossingabove50ema" [p. 46]
- "below10600isseen,chancesofanewhighsurvive" [p. 48]
- "Below10620-Trendingmovedownpossible" [p. 51]
- "This count will be invalid below 10620. My Friday long Sl will be triggered." [p. 53]
- "Nifty bounced from our support/long entry level of 10105" [p. 29]

**Pseudocode** (ASSUMPTION: generalises the author's one-off levels into reusable triggers; the author never states these as rules; data = daily OHLC of the index proxy, EMA20, EMA50)

```
# Generic "support-hold dip-buy" (from the 11 Nov 2018 trade, p.34, 37)
inputs: S_hold (level that must not be broken downward, e.g. 10490),
        Z_lo, Z_hi (dip-buy zone, e.g. 10410, 10420),
        T1, T2, T3 (targets, e.g. 10680, 10810, 10910),
        SL_pts = 45  # 40-50
each day t:
  if no position and close[t-1] > S_hold and low[t] <= Z_hi and low[t] >= Z_lo - tolerance:
      buy at Z_hi (ASSUMPTION: limit order at top of the zone)
      stop = entry - SL_pts
  if in position:
      if low[t] <= stop: exit at stop
      if high[t] >= T1: after T1 move stop to entry or tighter (ASSUMPTION; book only says "tight SL")
      exit remaining at T2/T3 (ASSUMPTION: scale out equally)

# Regime / invalidation filters
bearish_scenario_alive = close < 11900            # as of Sep 2018 only
fast_fall_active = (EMA20 < EMA50) and region_near 10700  # negated when EMA20 crosses above EMA50
reconsider_bear = close > 10740..10780

# Pivot-day rule (Feb 2019, p.51, 53)
L = low of Friday
if close > L and prior scenario bullish: long, SL just below L, target 11270-80
if close < L: scenario invalid, exit long (SL triggered); bearish trend move possible
```

**Ambiguities & assumptions**

- All levels are Nifty-specific and date-specific; the book gives no generalisable parameters. ASSUMPTION: parameterise as percentages of the index (e.g. SL 40-50 pts is about 0.4-0.5% of 10450); this is untested by the author.
- "Break" and "hold" are never defined (intraday low vs close, how many points). ASSUMPTION: use daily close for breaks, daily low for tests of support.
- Entry order type is not given. ASSUMPTION: limit buy at the top of the dip zone.
- Targets come from chart annotations that are partly lost in OCR (p. 34). Only 10680/10810/10910 are reliably readable; no position split is given. ASSUMPTION: equal thirds.
- "Fast Fall setup" is named but not defined in this text beyond "MA 20-50 around 10700" [p. 45]; its short-side exits and sizing are not found in this book. ASSUMPTION: treat as "EMA20 below EMA50 and price within 2% below EMA50 means no new longs" and do not backtest as a short.
- Conflicting versions: the Sep 7 tweet gave 10310-10230 as support, corrected the next day to 11310-11230 [p. 4, 5]. ASSUMPTION: use the corrected 11310-11230. The Feb 2019 pivot 10620 was later revised to a 11236-38 confluence because the bounce came from 10586 [p. 55].
- Shorting: the author does not say how shorts are implemented. Not found in this text.

### 2.2 Forecast track record and Neowave / Elliott method (NOT codable; non-codable note)

Neowave / Elliott counting (triangle corrections, ending diagonals, rising wedges, flats, running corrections, Diametric, W-X-Y, time calculations) is discretionary, and the author himself says that wave labelling is sometimes impossible [p. 33, 41, 53]. No codable proxy is claimed for those elements; the only level-break proxies are in 2.1.

**(a) Method elements stated as rules in the tweets**

| # | Method element (paraphrase unless quoted) | Page |
|---|---|---|
| M1 | Rising Wedge: pattern implication matters; a valid Rising Wedge gives a target of 80-100% retracement, so ask whether you expect that much before marking it; an earlier "Rising Wedge" marking was withdrawn | 2 |
| M2 | Triangle (Neowave) projection: A to E leg size 1219-1225 pts, thrust projected 3800-4000 pts from 7894 giving 11694-11894 (target stated as 12000, 11900 actually); perfect channel touch points prohibit counting the 2009 rally as impulsive | 1 |
| M3 | Cyclical studies: September-October flagged as a time to be cautious | 3 |
| M4 | Channel boundary logic: swing low at the upper boundary of the major red channel; if it fails, a confluence support band; large breakdown expected only below it | 4 |
| M5 | A weak monthly close generally indicates finding a short-term bottom in October/November | 11 |
| M6 | Equality of bounces/drops across history (2011: 766 pts bounce after 1161 pts drop in 14 weeks; 2015: 715 pts after 1122 pts in 15 weeks); three complete rallies of equal magnitude cannot be ignored | 18, 21 |
| M7 | Bear-market durations from top to lowest level: 2015-16 = 12 months, 2010-11 = 14, 2008 = 10; the 2018 bear market judged young at 2 months | 22 |
| M8 | Price action near equality of two drops (first drop -891 pts, second drop -941 pts, 61.8% of 1561 = 965): band 9820-9745 watched | 23 |
| M9 | Flat formations in Nifty and BankNifty: "1 of C" going on, stronger above 10300 and 25150; buying in wave 2 of C is safer as SL gets much closer | 26, 27 |
| M10 | Fibonacci retracement of the small up-move from the lows (50%, 61.8%); Nifty needs to hold 61.8% (80% theoretically but not preferably) | 28, 29 |
| M11 | Retracement after the first decline in a bear market: 2015 61%, 2011 66%, 2008 57%; 2018 only 44% at that time; 66% would come at 11163 | 39 |
| M12 | Irregular flat: a dip toward 10420-00 expected before the next rally; despite the channel break, no down momentum and overlapping price action suggest a correction | 34 |
| M13 | Running correction: if 10510-500 holds, the whole correction from the 2 Nov high of 10606 can be a Running Correction (very bullish) | 35 |
| M14 | Fall from 3 to 4 achieving equality with fall from 1 to 2 at 10434, unfilled gap area 10432-42, last swing low 10442: confluence = significant support zone 10430-40 | 40 |
| M15 | "Mix waves": when 10 Elliottists give 10 different counts, stay clear of short-term EW counts and look for clues elsewhere | 41 |
| M16 | Fast Fall setup using the 20/50 EMA around 10700; 20 EMA crossing above 50 EMA negates it | 45, 46 |
| M17 | Diametric (7-legged) pattern from price and time symmetry between legs in a congestion zone; if true the corrective rally may extend to 11100 or 11400 | 48 |
| M18 | Symmetry: C = A at 11272 and Y = W at 11270; "There are many valid counts at any single moment" and symmetry is the guiding light | 52, 53 |
| M19 | Time calculations: volatility squeeze for the next 3 months, next trending move expected January 2019; B/2 sideways for a couple of months, C/3 in January/February 2019 (both marked as failed by the compiler) | 12, 14, 13 |
| M20 | Wave principle remark: in the 5th wave the line is not supposed to be broken except in an ending diagonal; the tweet's chart text is heavily garbled by OCR | 38 |

**(b) Table of the calls** (verdict column = my classification of the compiler's COMMENTS text: Hit / Partial / Miss; "Unscored" = no comment on a testable forecast. Compiler wording is quoted only where verbatim.)

| ID | Date | Level (as stated) | Forecast | Compiler comment (paraphrase) | Verdict | Page |
|---|---|---|---|---|---|---|
| C1 | 10 Jul 2018 | Nifty 10947 | Target 12000 (11900 actually) from Neowave triangle; 31 Aug tweet: first target achieved | Nifty made a high of 11760 in next 6 weeks (11900 not reached) | Partial | 1, 3 |
| C2 | 9 Aug 2018 | USDINR 68.90 | USDINR strength, 73-75 not improbable in coming months | USDINR high 74.50 8 weeks later | Hit | 2 |
| C3 | 3 Sep 2018 | Nifty 11582 | Sep-Oct a good time to be cautious | Nifty crashed to 10005 by end-October | Hit | 3 |
| C4 | 7 Sep 2018 | Nifty 11589 | 11394 low = channel boundary; if it fails, 11310-11230 support (typo-corrected); large breakdown only below | Bounce 11250 to 11523, then 11230 broken in next 3 sessions | Hit | 4, 5 |
| C5 | 7 Sep 2018 | USDINR 72.10 | Higher probability of consolidation 70.50-72.00; alternative: breakout to 73.10-73.30 | Alternative (lower probability) materialised | Miss | 5 |
| C6 | 8 Sep 2018 | Nifty 11515 | Support band worked, 11600 immediate target, larger uptrend intact, 11250-30 is THE support | Support of 11250-30 gave way in next 3 sessions, large breakdown signalled | Miss (on the 11600 / uptrend-intact part) | 6 |
| C7 | 21 Sep 2018 | Nifty 11234 | "Bear market possible for next 12 months"; bearish while below 11900; break below 10800-900 major boost for bears | Comment only quotes the blog article; no outcome stated in this text | Unscored | 7 |
| C8 | 22 Sep 2018 | Nifty 11143 | 10800-900 the last bastion, should give way in next few weeks | Low of day 10869, then sharp bounce, but 10800 broken in next 8 sessions | Hit | 8 |
| C9 | 28 Sep 2018 | Nifty 10930 | Weak monthly close: ST bottom Oct/Nov; 10850-800 breaks, inviting 10300-400; recovery to 11150-200 invites selling, SL above 11250 | 10300 tested in next 4 sessions | Hit | 11 |
| C10 | 28 Sep 2018 | Nifty 10930 | Volatility squeeze next 3 months, sideways, next trending move January 2019; immediate ST bottom in a week or two | 550+ pt bounce from 10139 in 8 sessions but actual bottom took two more weeks; "Thetimecalculationdidn'twork." | Miss | 12, 13 |
| C11 | 28 Sep 2018 | Nifty 10930 | 2-hour chart preferred path: bounce to 11200 | Bounce curtailed to 11050 before next major decline | Partial | 13 |
| C12 | 29 Sep 2018 | Nifty 10930 | Sideways B/2 for a couple of months after A/1, then C/3 in Jan/Feb 2019 | "Thetimecalculationdidn'tworkout." | Miss | 14 |
| C13 | 1 Oct 2018 | Nifty 11008 | Close to major support around 10800 (+/-20); price action important | Low of day 10823; support gave way as expected in next couple of sessions | Hit | 15 |
| C14 | 4 Oct 2018 | Nifty 10599 | Admits expecting bounce to 11100-200 then 10800 break (bounce limited to 11050); now 10300-400 calling; failure to hold opens 10000-9700 | 10300 tested in next 2 sessions; bottomed at 10005 three weeks later | Hit | 16, 17 |
| C15 | 10 Oct 2018 | Nifty 10301 | Curious about price action near 10480 and 10550 | Nifty crashed from 10480 to 10139 in next 2 sessions | Hit | 18 |
| C16 | 10 Oct 2018 | Nifty 10460 | 10199 may not hold; real bottom preferably a Triangle with another down move and fresh low first | 10199 broke to 10139, rallied to 10710 in 4 sessions; fresh low came within two weeks | Hit | 19 |
| C17 | 10 Oct 2018 | Nifty 10460 | Gut feeling: range 10200-10xxx for a few days | "Thisspeculationturned outtobetotallywrong" | Miss | 20 |
| C18 | 23 Oct 2018 | Nifty 10147 | Watch equality band 9820-9745 (second drop equal to first) | Nifty bottomed at 10005; lower supports did not come into play | Miss | 23 |
| C19 | 26 Oct 2018 | Nifty 10030 | Reached major support band 10000-9700; major trend down but short-term pullback toward 10700 in 2-3 weeks | Bottomed at 10005, rallied to 10700 in next 3 weeks | Hit | 24 |
| C20 | 28 Oct 2018 | Midcap 100 16257 / Smallcap 100 5748 | 2008 the only parallel; further 14-15% / 20% drop possible (chart text garbled); expectations are for 2019 | Next week Midcap 100 -4.65% and Smallcap 100 -6.65%, "much more downside still open" (one-week follow-up only) | Unscored | 25 |
| C21 | 30-31 Oct 2018 | Nifty 10387 (31 Oct) | Flat formations; 1 of C; Nifty target 10700+, BankNifty 25900+; Nifty must hold 61.8% retrace | Nifty bounced from "our support/long entry level of 10105" and closed much higher | Hit | 26, 27, 28, 29 |
| C22 | 9 Nov 2018 | Nifty 10585 | Two phases in the market; a month or two of the unlabelable phase may begin any day now | One of the most complex corrective periods began within a couple of sessions and lasted to last week of February | Hit | 33 |
| C23 | 11 Nov 2018 | Nifty 10585 | If 10490 not broken, upward momentum; dip near 10420-10 buyable with 40-50 pts SL; irregular flat; targets 10680/10810/10910 | Corrected to 10440 in 2 sessions then rallied to 10774 in 5 sessions | Hit | 34 |
| C24 | 12 Nov 2018 | Nifty 10482 | Watch 10510-500: if held, Running Correction (very bullish); break below 10490 may invite 10430-20 | Broke below 10490 but bounced from 10440 | Hit (the lower scenario) | 35 |
| C25 | 13-16 Nov 2018 | not stated | 10440 low: scenario worked as expected; first target 10680 achieved ("The trade has been awarding") | Author's own follow-up; no compiler comment | Hit (author's own statement) | 36, 37 |
| C26 | 20 Nov 2018 | not stated | Near second target 10810; high of 10775 then turned down; upside momentum lost | Author's own follow-up | Partial (10810 missed by 35 pts) | 38 |
| C27 | 22 Nov 2018 | Nifty 10527 | Confluence 10430-40 significant support zone | Nifty bounced from 10490 to 10841 (zone itself not tested) | Hit (bounce) | 40 |
| C28 | 29-30 Nov 2018 | not stated | 30 pts short of 3rd target (10910); "Still see this as a bear market rally"; 30 Nov: "All targetsachieved." | Author's own follow-up; 6 Dec: third target 10910 met and 30 more points before the rally ended | Hit | 42, 43, 44 |
| C29 | 7 Dec 2018 | Nifty 10601 | Probable Diametric finished; confirmation = break below 10490 on Friday | 10490 broken then reclaimed, both decisively, in a single session; "Me, totally puzzled." | Miss | 45 |
| C30 | 11 Dec 2018 | Nifty 10488 | Move for 9100 in coming months is on, invalidation 10950; bounce limited to 10700; Fast Fall setup | "Trying to understand the moves but all the signs failing. Confusion increases." | Miss | 45 |
| C31 | 12 Dec 2018 | Nifty 10549 | Wait for 20 EMA above 50 EMA to negate; strength above 10740-80 demands reconsideration | 10740-80 broken above in next couple of sessions, negating the bearish bias | Miss | 46 |
| C32 | 6 Jan 2019 | Nifty 10727 | Bear rally not negated; new high survives until break below 10600; Diametric; confirm with break above 10923 in next 2 sessions; 11100 or even 11400 | "None of the levels worked but the path of least resistance was getting clear. Up." | Partial | 48 |
| C33 | 16 Feb 2019 | Nifty 10724 | Friday low 10620 significant; above it rally to 11270-80 / 11290-11300 (C = A at 11272, Y = W at 11270); below it trending move down | 10620 broken by a few points to 10586 in next 2 sessions before expected rally; 11300 came in 16 sessions (repeated 6 Mar with level 10687) | Hit (but the 10620 invalidation was breached and the author's long SL was triggered) | 51, 52, 53, 55 |

Tweets with a testable view but no compiler comment (not counted in the tally): 22-26 Sep 2018 "another dip" and "bulls should remain scared unless Nifty touches 11250" [p. 9, 10]; 22 Oct 2018 bear-market duration comparison (compiler: "12th month going on now") [p. 22]; 23 Oct 2018 triangle/wave A idea [p. 24]; 30 Oct 2018 "Defending 10000 ... is going to give in" [p. 26]; 2 Nov 2018 sellers in 10750-10950 with targets 10793/10860/10927 [p. 30]; 2 Nov 2018 range 10000-11000 for 6-8 weeks [p. 31]; 3 and 9 Nov 2018 up-move continuing to 10700-60 [p. 32]; 21 Nov 2018 66% retrace at 11163 [p. 39]; 30 Nov 2018 wait for a trigger before shorts [p. 43]; 9 Jan 2019 breakout imminent, path of least resistance up [p. 49]; 16 Jan 2019 "now for 11100 or even 11400" [p. 50]; 21 Feb 2019 "can't take any convincing stand" [p. 54].

**(c) The compiler's and author's own admissions of misses or confusion**

| Admission | Page |
|---|---|
| Typo in the support band (10310-10230 should be 11310-11230) | 5 |
| "Thetimecalculationdidn'twork." (volatility squeeze / January move) | 13 |
| "Thetimecalculationdidn'tworkout." (B/2 sideways, C/3 Jan/Feb) | 14 |
| "Iunderestimated theviciousnessofthebearmarketscenario"; expected the 10800 break after a bounce to 11100-200 but the bounce stopped at 11050 | 16 |
| Gut-feeling range call "turned out to be totally wrong" | 20 |
| "Starting to get confused with the waves at this point." | 41 |
| "Me, totally puzzled." (10490 broken and reclaimed) | 45 |
| "Trying to understand the moves but all the signs failing." | 45 |
| "Reconsidering personal directional stand at this point." | 46 |
| "Admitting my confusion here and taking a leave from the market." | 47 |
| Bounce came from 10586 not 10620, so the confluence zone was modified to 11236-38 | 55 |

**(d) Tally (my count of the 33 rows in table b)**

- Hit: 18 (C2, C3, C4, C8, C9, C13, C14, C15, C16, C19, C21, C22, C23, C24, C25, C27, C28, C33)
- Partial: 4 (C1, C11, C26, C32)
- Miss: 9 (C5, C6, C10, C12, C17, C18, C29, C30, C31)
- Unscored: 2 (C7, C20), plus the unscored tweets listed above
- Raw hit rate of scored rows: 18 / 31 = 58%; hits plus partials 22 / 31 = 71%. Caveats: self-compiled, selected by the compiler, many calls were conditional or zone-based, several rows (C25, C26, C28) rest on the author's own follow-up tweet rather than a compiler comment, the Hit/Miss classification is mine, and rows are not independent (C10 and C12 are the same time call; C3, C8, C9, C13, C14 are all the same Oct 2018 decline). The Oct 2018 bearish calls cluster in one regime; the Dec 2018 bearish call failed.

## 3. Risk & money-management rules

- Long from 10420-10 with 40-50 pts SL [p. 34]; the Feb 2019 long was stopped out on a break of 10620 ("My Friday long Sl will be triggered") [p. 53, 54].
- Short on recovery to 11150-200 with SL above 11250 [p. 11].
- After the first target, follow the rise with a tight SL, "individual choice" [p. 37].
- Buying in wave 2 of C is safer as SL gets much closer [p. 27].
- Caution flags: wide resistance zone 10700-11000 so be cautious with longs [p. 30, 37].
- No position size, risk per trade, drawdown limit or exposure rule is stated. Not found in this text.

## 4. Non-codable guidance

- Disclaimers: "Remember my usual disclaimers" and "Definitely not the only possibility" accompany many calls [p. 1, 13].
- "If not acquainted with EW, please ignore this tweet" [p. 32].
- Two phases of market: waves recognisable and not; stay clear of short-term EW counts in the latter [p. 33, 41].
- "There are many valid counts at any single moment"; the author's guiding light is symmetry [p. 53].
- Admission that the market may "slap me hard" and move against the bearish bias [p. 9].
- Respond to critics: the author states he had been among the biggest bulls earlier and that three complete rallies of equal magnitude cannot be ignored [p. 21].
- Stepping away from the market when no clarity [p. 47, 54].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Nifty 50 index daily OHLC (USDINR, BankNifty, Midcap 100, Smallcap 100 only for the non-codable calls); 20 and 50 EMA computed from closes.
- **Testability with our data:** Nifty index history exists only from 2024, so the 2018-19 calls cannot be replayed on the index; NIFTYBEES (ETF) or an equal-weight index from the stock panel is the proxy for 2005-2026. The calls themselves cannot be backtested: they are one-off, level-specific, partly conditional, and Neowave/Elliott counts are discretionary. At most the generic ideas in 2.1 (support-hold dip-buy with 40-50 pt SL, 20/50 EMA regime flag, pivot-day high/low rule) can be tested on NIFTYBEES 2005-2026; that would test our proxy, not the author. The author's forecasts can only be audited as a record (table 2.2b), not as a system.
- **Market-structure differences:** The Nifty cannot be shorted in the NSE cash market overnight. ASSUMPTION: implement the bearish calls only as "stay in cash / exit longs", not as shorts; implement longs on NIFTYBEES. NIFTYBEES prices are about one-tenth of the index level, so level-based parameters must be scaled (ASSUMPTION: use percentage distances from a reference level rather than absolute index points). STT, brokerage and about 0.1% slippage apply; 40-50 pt stops (about 0.4-0.5%) are of similar size to round-trip costs plus slippage on an ETF, so net results will be sensitive.

## 6. Verdict

- **Codeability:** Not codable as a system; Partly for the level-break triggers only. Neowave / Elliott counts, time calculations and zone judgments are discretionary, and no sizing or exit system is stated.
- **Priority for backtesting:** Low. It is a ~8-month, self-selected forecast record of one analyst on one index, with no systematic rule set; use it as a qualitative reference and as a source of hypotheses (support-hold dip-buy, EMA20/50 regime flag, retracement of 61.8% as support).
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the record as a rulebook or computing a hit rate from it as if unbiased; the tweets were selected by an unnamed compiler and verdicts are post hoc.
  2. Hard-coding the Nifty levels (10490, 10620, 11900 etc.) as universal rules, or applying index points directly to NIFTYBEES (scale mismatch).
  3. Pretending the wave counts, "Fast Fall" or time projections are codable, or implementing short signals that the NSE cash market cannot execute overnight.
