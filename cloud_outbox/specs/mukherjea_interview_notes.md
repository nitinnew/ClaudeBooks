# Notes of Interviews by Saurabh Mukherjea (Oct 2021 compilation) — Saurabh Mukherjea (talks), notes by Venkatesh Jayaraman (@EWFA_)

- **Source file:** Google Drive invest/Notes from Interviews of Saurabh Mukherjea_Oct2021 (1).pdf (30 pages)
- **Text file used:** text/mukherjea_interview_notes.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/<key>.md text/<key>.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read text lines 1-1101 (entire file), last `[[PAGE 30]]` reached. These are third-party notes (by Venkatesh Jayaraman, @EWFA_) of three Saurabh Mukherjea talks, not the author's own text: MOCA 2020 (Marcellus Investment Managers, March 2020; pp. 1-7), EDGE Institute Masterclass (August 2021; pp. 7-24), and the TEDxGateway webinar "India: From License Raj to Monopoly Raj" (September 2021; pp. 24-30). Page ranges checked against the text (talk 1 ends at the top of p. 7, talk 2 runs p. 7 to the opening of p. 24, talk 3 starts on p. 24). Nothing was skipped except passages with no investing rules (Relaxo/Asian Paints narrative detail is summarised, not transcribed; crypto, telecom-data-governance and "tragedy of commons" remarks are noted only in Section 4). The notes are loose and contain note-taker uncertainties (e.g. "Not clear" flags). Reading done by a Sonnet sub-agent (notes log covers lines 1-1101). The coordinator re-ran the verifier and an exact-page check and spot-checked 12 table citations (Ratio 7 p. 2; Coffee Can 10%/15% p. 3; 13 stocks, 2-year research, BSE500 entrants and 3-year flight path p. 6; 30-35 to 15 stocks p. 7; US recession rule pp. 8-9; ITC sale p. 20; do not time markets p. 28; three questions p. 29).

## 1. The method in brief
Mukherjea (Marcellus) runs two PMS products described here: **Consistent Compounders** (BSE500 universe) and **Little Champs** (companies below the BSE500) [p. 1]. The philosophy has three layers: (1) forensic accounting to eliminate suspect companies (he claims 80% of listed companies are suspect, 10 accounting-trap ratios applied each December to the top 1500 stocks) [p. 1, p. 2]; (2) conservative capital allocation, with free cash flow reinvested in the same business; and (3) "Himalayan" barriers to entry, i.e. a dominant monopoly/duopoly in an essential daily-life product [p. 1, p. 6]. The claimed edge is that about 20-25 Indian monopolists earn ~45% RoC against a ~15% cost of capital, so FCF of ~30% of capital employed lets them reinvest ~2/3 and compound profits near 20% regardless of macro [p. 3, p. 10, p. 11]. Reported results: Coffee Can-style screen "compound minimum at 20%" [p. 3]; Consistent Compounders ~25% returns with low volatility, 13 stocks, very low turnover [p. 6]; Little Champs screen 26% CAGR, refined portfolio 30% with Nifty-like volatility [p. 7]; BSE500 entrants compounded 50-55% pa over a 3-year path ("discovery effect") [p. 6]. All are the speaker's own claims, with no audited detail.

The notes add a macro overlay (US recession in year T implies an India boom in T+1, 4/4 cases, via cheap oil and cheap money) [p. 8, p. 9], sector theses (financial services, agriculture, speciality chemicals) [p. 17, p. 18], and the retail three-question checklist (clean accounts, ROCE of 15% over a decade, dominance) [p. 29]. He repeatedly says he does not time the market [p. 19, p. 21, p. 28]. Overlap: the Coffee Can screen and forensic screens also appear in the separate spec for "Diamonds in the Dust" (key mukherjea_diamonds_dust); every rule below is based only on THIS text, which is much less detailed (only one of the 10 forensic ratios is named). Fundamental screens can only be forward-tested on our data.

## 2. Strategies

### 2.1 Forensic accounting screen (exclusion filter)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Other: quality / fraud-avoidance exclusion filter (used as a gate for 2.3 and 2.4) | 1, 2 |
| Timeframe & holding period | Re-applied once a year in December; holding period not stated for the filter itself | 2 |
| Universe / eligibility filters | Top 1500 stocks in India | 2 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | 10 ratios, "each of these is a trap"; count how many traps each company fails; more traps failed = less interested. Only Ratio 7 is specified: growth in auditor's fees / growth in revenues (fees growing consistently faster than revenue over the last 6-7 years; example fees growing twice as fast). Other 9 ratios: not found in this text | 2 |
| Entry trigger & order type | Not a trade trigger. Output: roughly 70 BSE500 companies with clean books are the starting point for Consistent Compounders | 2 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Implied: avoid/drop companies that fail many traps; exact cut-off not given | 2 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of traps (ratios) | 10 | - | 2 |
| Universe size | Top 1500 stocks | - | 2 |
| Re-run frequency | Every December | - | 2 |
| Ratio 7 lookback | 6-7 years | - | 2 |
| Ratio 7 failing example | Fees growth about 2x revenue growth | no threshold stated | 2 |
| Max traps allowed | Not found in this text | - | - |
| Clean BSE500 names | about 70 | - | 2 |
| Share of listed cos suspect | 80% (also "nearly 50%" in the 2021 talk) | 80% vs 50% | 1, 24 |

**Key quotes**
- "every year in December, we apply these" [p. 2]
- "The more traps the company fails, the more thuggery in the business and less interested we" [p. 2]
- "in the BSE500 world, there are roughly 70 companies whose" [p. 2]
- "Consider the example of Ratio 7" [p. 2]

**Pseudocode**
```
each December:
  U = top 1500 stocks by market cap
  for s in U:
     traps_failed[s] = count of the 10 ratio tests failed   # only test 7 known
     test7_fail = (avg growth in auditor fees over 6-7y) > (avg growth in revenue over 6-7y)   # needs auditor fees
  clean = {s : traps_failed[s] <= K}      # K not given
```
Data requirements: auditor fees, revenue, and the other 9 undisclosed ratios.

**Ambiguities & assumptions**
- Nine of ten ratios not found in this text; ASSUMPTION: only Ratio 7 is codable; the diamonds_dust spec may supply others but that is out of scope here.
- "Fees growing faster than revenue" is a qualitative statement; ASSUMPTION: fail if 6-year CAGR of auditor fees exceeds 1.5x the 6-year revenue CAGR (the text's example is 2x; 1.5x is our own choice and should be tested over 1.5x-2x).
- Auditor fees may not be in our fundamentals; ASSUMPTION: untestable unless the field exists.
- Max traps allowed K not given; ASSUMPTION: K=0, i.e. exclude any company failing the one testable ratio.

### 2.2 Coffee Can screen (simplest retail version)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality / growth-compounder (buy-and-hold fundamental screen) | 3 |
| Timeframe & holding period | 10-year fundamental history; hold long term (compounding; "10x in 10 years") | 3, 6 |
| Universe / eligibility filters | Not stated explicitly for this screen; 10 years of data required. ASSUMPTION: listed NSE stocks with 10 years of history | 3 |
| Market / regime filter | None; "do not time the markets" | 28 |
| Setup conditions | (1) Revenue growth at least 10% every year for the last 10 years, year on year, not CAGR; (2) ROCE above 15% in every single year for the last 10 years | 3 |
| Entry trigger & order type | Buy all passers (about 15 pass). Order type not found in this text | 3 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text (implied: sell only if the screen is failed or thesis breaks) | - |
| Position sizing | "If you invest in all the 15" (equal weight implied); not stated | 3 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | About 15 names pass | 3 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Revenue growth floor | 10% per year | must be year-on-year, not CAGR | 3 |
| ROCE floor | 15% | every year | 3 |
| Lookback | 10 years | - | 3 |
| Claimed result | min 20% compounding, lower volatility | - | 3 |
| Passers | about 15 | - | 3 |

**Key quotes**
- "Revenue growth is min 10% every year for the last 10 years" [p. 3]
- "ROCE > 15% for every single year for the last 10 years." [p. 3]
- "Barely 15 companies pass this test." [p. 3]

**Pseudocode**
```
for s in universe:
   ok = all(rev[s][y] / rev[s][y-1] - 1 >= 0.10 for y in last 10 fiscal years)
        and all(ROCE[s][y] > 0.15 for y in last 10 fiscal years)
buy equal-weight all ok; hold; re-screen annually (ASSUMPTION)
```
Data requirements: 10 years of annual revenue and ROCE per stock (ROCE = EBIT / capital employed per p. 10).

**Ambiguities & assumptions**
- Whether "last 10 years" means 10 annual growth rates (11 revenue points); ASSUMPTION: 10 consecutive annual growth rates.
- Rebalancing and exit rule not found in this text; ASSUMPTION: annual re-screen, drop failures.
- Our fundamentals start Feb 2026 so this cannot be backtested; ASSUMPTION: forward test only, or build a ROCE history from the vendor's annual fields if available.

### 2.3 Consistent Compounders (BSE500 monopoly portfolio)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality / monopoly compounder (concentrated buy-and-hold) | 1, 6 |
| Timeframe & holding period | Very long; double the business every 3-5 years, "10x in 10 years"; "Very little buying and selling" | 3, 6 |
| Universe / eligibility filters | BSE500; forensic screen leaves about 70 clean companies; then clean-and-hungry managements in essential daily-life products with 1-2 players taking ~85% of profits; passes Coffee Can screen (see 2.2) | 1, 2, 3 |
| Market / regime filter | None; "We are not trying to time the cycle" | 19 |
| Setup conditions | (1) Promoter not a "chor", books clean; (2) product essential for day-to-day life in India; (3) barriers to entry "as high as Himalayas". Also high RoC vs cost of capital, FCF reinvested in the business, promoter still hungry. "PE is not the right metrics" | 6, 1, 2 |
| Entry trigger & order type | Qualitative: after about 2 years of work figuring out barriers to entry. No price trigger | 6 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Sold ITC because the surplus cash was not being reinvested to compound at 20% (expected 15%) | 20 |
| Position sizing | Skewed towards passers that are also monopolies; weights not given | 3 |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | 13 stocks held; only 25 stocks in the investable universe | 6 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Holdings | 13 | universe of 25 | 6 |
| Claimed return | 25% | - | 6 |
| Typical RoC of monopolists | 45% (EBIT / total capital employed) | 30% called respectable in India | 10 |
| Cost of capital used | 15% | - | 3, 10 |
| Payout / reinvest split | 1/3 dividend, 2/3 reinvested (about 20% growth) | - | 10 |
| Target compounding | 20% | 20-25% | 20, 29 |
| Sell trigger example | ITC: compounding 15% vs 20% target | - | 20 |

**Key quotes**
- "Promoter should not be Chor, books have to clean" [p. 6]
- "The barriers to entry should be as high as Himalayas" [p. 6]
- "we skew the portfolio towards" [p. 3]
- "Very little buying and selling is done" [p. 6]
- "We are not trying to time the cycle" [p. 19]

**Pseudocode**
```
U = BSE500 members
U1 = forensic_clean(U)                 # 2.1, ~70 names
U2 = coffee_can(U1)                    # 2.2, ~15 names
U3 = manual_monopoly_flag(U2)          # barriers to entry: NOT codable
portfolio = overweight(U3) ; hold with minimal turnover ; exit on thesis break (e.g. reinvestment stalls)
```
Data requirements: BSE500 membership history, fundamentals for 2.1-2.2, a manual monopoly list.

**Ambiguities & assumptions**
- Monopoly/barrier judgment is discretionary ("takes nearly 2 years to figure out"); ASSUMPTION: proxy by high-and-stable ROCE plus top-2 profit share within an industry, if an industry code exists.
- Position weights not given; ASSUMPTION: equal weight.
- Exit rule beyond the ITC example not found in this text; ASSUMPTION: exit on failing the Coffee Can screen for two consecutive years.
- The text says "13 such stocks" and "25 stocks" as the universe in a 2020 talk; the 2021 talks cite "20-25" monopolists. ASSUMPTION: use the 13 holdings as the target size.

### 2.4 Little Champs (sub-BSE500 small-cap quality)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Growth-quality small cap with "discovery effect" | 6 |
| Timeframe & holding period | Multi-year; BSE500 entrants studied on a 3-year flight path | 6 |
| Universe / eligibility filters | Step 1: market cap below USD 500 million (i.e. below the BSE500 cut-off, then stated as about 3500 crore) | 6 |
| Market / regime filter | None found | - |
| Setup conditions | Step 2: forensic screen ("Half the world gets wiped of here"). Step 3: above median on each parameter and top 20% on overall score. Parameters: 6 years of consistent revenue growth, which generated higher profit margin, which generated better RoC, accompanied by improved working capital (margin, asset turnover, working capital). Step 4: bottom-up research. Step 5: third-party/channel checks and management. Refine 30-35 passers to about 15 with Hidden Champions traits (essential input to a large company, giving bargaining power; only one of "4 traits" is given) | 6, 7 |
| Entry trigger & order type | Qualitative after steps 4-5; no price trigger | 6 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text (discovery re-rating to about 3x book is the thesis) | 6 |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | About 15 stocks (cannot identify 50) | 6 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Market cap ceiling | USD 500 million | BSE500 bottom about 3500 crore; example small cap 2000 crore | 6 |
| Forensic screen | pass/fail, removes about half | - | 6 |
| Score cut-off | Above median on each parameter; top 20% overall | - | 6 |
| Revenue growth lookback | 6 years consistently | - | 6 |
| Screen output | 30-35 stocks | refined to 15 | 7 |
| Claimed returns | Screen 26% CAGR; final portfolio 30% with Nifty-like volatility | - | 7 |
| Discovery premium | Below BSE500 trades near book value; after discovery about 3x book | - | 6 |

**Key quotes**
- "Step 1: The universe with MCap < 500 Million USD" [p. 6]
- "Step 2: Forensic screen to eliminate companies with poor accounting quality" [p. 6]
- "Step 3: Above median on each parameter Top 20% on overall score" [p. 6]
- "We look for 6 years revenue growth consistently," [p. 6]
- "Such a filter gives a return of 26% CAGR." [p. 7]
- "The screen shows up 30-35 stocks" [p. 7]

**Pseudocode**
```
U = stocks with mcap < USD 500m (not in BSE500)
U = forensic_clean(U)                       # 2.1
for each s: compute rev_growth_6y (every year positive), margin trend, ROCE trend, WC-days trend
score = rank-average of parameters ; keep s if every parameter > median and score in top 20%
candidates = ~30-35 ; manual refinement to ~15 (NOT codable)
```
Data requirements: market cap, revenue history, EBIT margin, ROCE, working-capital days (6 years each).

**Ambiguities & assumptions**
- "Parameter" list and weights not given; ASSUMPTION: four parameters = revenue growth, EBIT margin, ROCE, working capital days (inverted).
- "6 years consistently" is undefined; ASSUMPTION: revenue up in each of the last 6 years, margin and ROCE higher than 6 years ago.
- Forensic screen is mostly not found in this text (see 2.1); ASSUMPTION: skip or use Ratio 7 only.
- Steps 4-5 are discretionary; ASSUMPTION: replace by taking top 15 by composite score.
- USD 500m is not converted in the text beyond "3500 Crores"; ASSUMPTION: use INR 3,500 crore as a market cap proxy.

### 2.5 BSE500-entrant "discovery effect" screen
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Event / size-migration momentum with re-rating | 6, 12, 13 |
| Timeframe & holding period | 3 year "flight path" after entry; up to a 10-year re-rating path | 6, 13 |
| Universe / eligibility filters | Companies approaching or entering the BSE500 bottom (about 3500 crore / USD 500m); about 50 enter each year | 6, 12 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Small caps at PE below 15 are re-rated about 3x as market cap crosses about USD 3bn (foreign investors/PE discover them); priced near book before discovery. Quality overlay from 2.4 preferred | 6, 13 |
| Entry trigger & order type | Buy before discovery (when the company is small and "not many know about it") ; no precise trigger | 6 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Study window of 3 years after entry | 6 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| BSE500 entrants per year | 50 | - | 6, 12 |
| Entrant return | 50-55% pa over 3 years | - | 6 |
| Pre-discovery PE | below 15 | - | 13 |
| Re-rating | about 3x book value / PE triples | - | 6, 13 |
| Size thresholds | 2000 cr (unknown), 3500 cr (BSE500 floor), USD 3bn (global discovery) | - | 6, 13 |

**Key quotes**
- "every year 50 stocks enter the BSE 500" [p. 6]
- "3 year flight path, these companies compounded around 50 to 55% pa." [p. 6]
- "it goes to 3 times book value" [p. 6]
- "When it is small cap, the PE multiple is less than 15." [p. 13]

**Pseudocode**
```
each year-end:
   rank all stocks by market cap; entrants = stocks that moved into the top 500 by mcap this year
   buy entrants at the entry date; hold 3 years; compare to equal-weight universe
```
Data requirements: market cap (shares outstanding history) or an approximation of BSE500 membership.

**Ambiguities & assumptions**
- BSE500 membership is not in our data; ASSUMPTION: approximate by rank 500 by traded value or float market cap in the 3,700 stock panel.
- Entry timing (before vs after entering) is not specified; ASSUMPTION: buy on the first trading day after annual rank crossing, equal weight, hold 3 years.
- Look-ahead warning: the 50-55% is measured on stocks that did enter (selection bias); a backtest must pick candidates before entry.

### 2.6 Retail three-question checklist (clean accounts, ROCE, dominance)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality checklist for direct investing | 29, 30 |
| Timeframe & holding period | Decades; "10x in 10 years and 100x in 20 years" | 29 |
| Universe / eligibility filters | Any Indian listed stock; read the last 3 annual reports | 29 |
| Market / regime filter | None: "do not time the markets" | 28 |
| Setup conditions | (1) Clean accounts: board largely friends/relatives of promoter is a red flag; long Related Party Transactions section needs analysis; (2) Sensible capital allocation: ROCE at least 15% consistently for nearly a decade, else walk away; (3) Dominance: if a competitor offered the same product much cheaper and the company would lose market share, do not invest. Do not confuse high market share with dominance | 29, 30 |
| Entry trigger & order type | Not found in this text | - |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Not found in this text | - |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| ROCE minimum | 15% | "nearly a decade" | 29 |
| Reinvestment return target | 20 to 25% | - | 29 |
| Annual reports to read | last 3 | - | 29 |
| Skepticism flags | media-claimed network effects or barriers; airlines as example of no cash flow | - | 30 |
| Early red flag | promoters with lots of private jets (host's view) | - | 29 |

**Key quotes**
- "Is the board of the company largely made of friends and relatives of the promoter." [p. 29]
- "it is not 15% consistently for nearly a decade, walk away from the company" [p. 29]
- "will the company lose the market share" [p. 29]
- "One should not confuse with high market share with dominance." [p. 30]
- "be very sceptical" [p. 30]

**Pseudocode**
```
pass = (ROCE >= 15% in ~9-10 of last 10 years)       # codable
       and not (related_party_flag or board_independence_flag)   # needs governance data (not in our data)
       and dominance_judgment                                     # NOT codable
```
Data requirements: 10-year ROCE; board composition and related-party transaction disclosures.

**Ambiguities & assumptions**
- "Nearly a decade" is vague (versus "every single year" in 2.2); ASSUMPTION: 9 of 10 years, tested against 10 of 10.
- Governance and dominance tests are judgmental; ASSUMPTION: only the ROCE test is coded.
- No entry, exit or sizing rule; ASSUMPTION: combine with 2.2 mechanics.

### 2.7 US-recession lead macro overlay (India boom filter)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Macro regime filter | 8, 9 |
| Timeframe & holding period | Boom lasts about 3 years (5 years for 1982-87, 4 for 1993-97, 5 for 2003-08, about 3 for 2009-11) | 8, 9 |
| Universe / eligibility filters | Applies to the Indian economy/equities; beneficiaries are giant monopolies, not cyclicals | 9 |
| Market / regime filter | US recession in year T implies India boom begins in year T+1; no US recession means no India boom | 8, 9 |
| Setup conditions | US recession lowers crude 50-80% (about 3% GDP stimulus) and cuts bond yield about 2.5%, passed on by RBI | 9 |
| Entry trigger & order type | Not found in this text. Cyclical stocks (real estate, road, construction) are warned against: "It may not work." | 9 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Peak signal (discretionary): labour and industrial land prices up about 20%, RBI hikes 2-3%; "none of us can time the markets" | 21, 22 |
| Position sizing | Not found in this text | - |
| Adding to / pyramiding | Not found in this text | - |
| Portfolio limits | Not found in this text | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Lead | 1 year after US recession | - | 8 |
| Boom years cited | 1982, 1993, 2003-04, 2009 | - | 8, 9 |
| Hit rate claimed | 4/4 | - | 9 |
| Crude fall in recession | 50-80% | - | 9 |
| Yield fall | about 2.5% | - | 9 |
| Peak signals | 20% land/labour rise; RBI 2-3% hikes | - | 22 |

**Key quotes**
- "Whenever US goes into recession in Year T, the boom in India begins in Year T+1." [p. 8]
- "This rule is a 100% success rate i.e. 4/4." [p. 9]
- "It may not work." [p. 9]
- "When labour market and industrial land prices roar up, they go up by 20%, it is a time of max" [p. 22]

**Pseudocode**
```
us_recession_years = external list (NBER, not in our data)
boom_start = T+1 for each recession year T ; regime_on for boom_start .. +3y
if regime_on: go long equal-weight Nifty proxy (NIFTYBEES / equal-weight panel) else cash   # ASSUMPTION
```
Data requirements: US recession dates (external hard-coded), NIFTYBEES.

**Ambiguities & assumptions**
- The text gives no trade rule; the recession-to-boom link is a macro observation (n=4). ASSUMPTION: test long NIFTYBEES during T+1..T+3 vs buy and hold, 2005-2026 contains only about 2008-09 and 2020 recessions, so n=2; low statistical value.
- Period lengths conflict (the "typical 3-year" boom vs 4-5-year spans listed); ASSUMPTION: 3 years.
- The author himself says the beneficiaries are monopolies, not the broad market; ASSUMPTION: test overlay only as a regime on 2.2/2.3 allocation.

## 3. Risk & money-management rules
- No stop-losses, position sizing formulae, or drawdown rules are given anywhere in the notes. Risk is managed by avoiding fraud (forensic screen) [p. 2], buying only high-ROCE franchises [p. 29], and low turnover [p. 6].
- Concentration: 13 stocks in Consistent Compounders [p. 6]; about 15 in Little Champs [p. 6]; claimed volatility lower than a G-Sec bond for the first and equal to Nifty for the second [p. 6, p. 7].
- Do not time the market or cycle; the risk is "the rug pulled" under you if you try [p. 19, p. 21, p. 28].
- Avoid physical-asset heavy household allocation; if unable to pick stocks, hold the index, and stock picking is preferable to index [p. 29].
- Transaction costs of 3-5% are cited as eating returns in the context of overseas investing [p. 23].

## 4. Non-codable guidance
- Barriers to entry take about 2 years of research to verify; "No research report or TV broadcast" will provide it [p. 6].
- Independent thought beats mainstream wisdom: "When everybody outsourced, why did not Relaxo do it?" [p. 24]
- Monopolist companies are low-profile and avoid media; do not expect a CEO interview [p. 8].
- Scepticism of media-projected network effects/barriers (Swiggy/Zomato/new-economy discussion) [p. 30]; telecom not owned because no sustained return above cost of capital in 21 years [p. 22].
- Sector theses: financial services (PSU banks losing share; financialisation of the 95% physical-asset household wealth), agriculture (monopolisation from mandi to retail), speciality chemicals [p. 17, p. 18]; decline of conglomerates in favour of monoline specialists [p. 21, p. 28]; small companies choose to sell out, wind up or become contract manufacturers [p. 23, p. 28].
- Cheap-PE stocks and PSUs are a distraction versus growth [p. 19]; high valuation is secondary to franchise quality [p. 6].
- Case studies (Asian Paints working-capital cycle 8 days vs Berger 45 and Akzo 105; Relaxo receivable days 90 down to 30) illustrate the barrier concept [p. 5, p. 14].
- Companies moving to the next niche while generating FCF (Pidilite, Page Industries) [p. 20].

## 5. Adapting to NSE (Indian equities)
- **Data required:** Daily OHLCV and market cap (shares outstanding) for rank-based BSE500 approximation; annual revenue, EBIT, capital employed (ROCE), FCF, working-capital days, auditor fees (for ratio 7), related-party and board data (probably unavailable); NIFTYBEES for regime tests; US recession dates (external).
- **Testability with our data:** The market-cap rank/entrant idea (2.5) and size cut-offs can be approximated with price data and shares outstanding, and tested 2005-2026 (bias: BSE500 membership is not available). The Coffee Can, Consistent Compounders, Little Champs and forensic screens require 10 years of point-in-time fundamentals, which exist only from Feb 2026 (3-year growth fields from May 2026), so they can only be forward-tested. The monopoly judgment, channel checks, governance tests and 9 of the 10 forensic ratios are not found in this text or not in our data. The 2.7 macro overlay has n=2 recessions in our window.
- **Market-structure differences:** The method is long-only and buy-and-hold on Indian equities, so no shorting issue arises. ASSUMPTION: use equal-weight with annual rebalancing to limit costs (STT, brokerage, about 0.1% slippage). Small-cap (Little Champs) universe has liquidity and circuit-limit risk; ASSUMPTION: add a minimum average daily traded value filter (not in the text). The discovery re-rating thresholds are in INR/USD market cap and need adjusting for index drift over 2005-2026; ASSUMPTION: use rank (about the 500th largest) rather than fixed rupee values.

## 6. Verdict
- **Codeability:** Partly. The numeric screens (Coffee Can, ROCE and revenue growth, market cap ceilings, ratio 7) are codable, but monopoly/barrier judgment, forensic ratios 1-6 and 8-10, governance checks and exits are discretionary or missing, and the notes are second-hand.
- **Priority for backtesting:** Medium. Coffee Can screening (2.2) and the size-entrant effect (2.5) are cheap to test and overlap with the Diamonds in the Dust spec; the rest cannot be backtested before 2026.
- **Top 3 things a coder is most likely to get wrong:**
  1. Using CAGR instead of year-on-year growth (10% in every one of 10 years) and testing ROCE as an average rather than every year [p. 3].
  2. Treating the Consistent Compounders/Little Champs portfolios as fully mechanical: the barrier-to-entry, channel-check and management steps are manual, and the selection-biased claimed returns (25%, 26%, 30%, 50-55%) cannot be reproduced from the screens alone [p. 6, p. 7].
  3. Introducing look-ahead and survivorship bias in the BSE500 "entrant" test (selecting stocks that entered, then measuring their return) or using the 4/4 US-recession rule as a tradable signal [p. 6, p. 9].
