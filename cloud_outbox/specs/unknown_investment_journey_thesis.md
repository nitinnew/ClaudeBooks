# Investment Journey Learning & Thesis — author not stated in the text

- **Source file:** Google Drive invest/Investment Journey Learning & Thesis_230716_220501.pdf
- **Text file used:** text/unknown_investment_journey_thesis.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - N is taken only from the nearest `[[PAGE N]]` marker above the passage.
- **Coverage:** Read all 262 lines, from line 1 to the last line, and reached the last marker `[[PAGE 13]]`. Page 13 has no text. Page 12 is only a disclaimer. Any images, charts or slide graphics in the PDF are not captured in the text. Nothing was skimmed. Reading done by a Sonnet sub-agent. The coordinator re-ran the verifier and an exact-page check and spot-checked 12 table citations (holdings 10-12 p. 3; leverage cap p. 4; 3-5 year view, ticket size, averaging up and DRHP/GMP p. 5; selling p. 6; ROCE and CAGR p. 7; mistakes p. 8; promoter stake and shareholding p. 9; be wrong fast p. 10; consolidations p. 11).

## 1. The method in brief
This is an Indian individual investor's slide notes (bullet points) on his investing journey. The author's name is not stated in the text. He started with IPO applications in college [p. 1], used borrowed money (bank loans and loans against shares) to apply for large IPO allotments such as Maruti (2003) and TCS (2004) [p. 2], and ended up with a "zoo" of 50-60 holdings [p. 3]. With a mentor and ValuePickr he cut this to about 10-12 holdings and made "big bets on quality small cap stocks" [p. 3].

The claimed edge is a concentrated, long-hold (3-5 year view) portfolio of undiscovered, low-PE, zero-institutional-holding small/mid caps. The stocks have a large opportunity size, high ROCE, an ethical first-generation promoter with a high stake, and low debt [p. 5, 7, 9]. The multibagger case is "when both EPS & PE rises" [p. 5]. IPOs are treated as fertile ground, bought on listing [p. 5]. The author reports no performance numbers or track record, only anecdotes (examples of multibaggers and sales) [p. 5, 6]. Most content is qualitative. Only a few items are rule-like (holding count, leverage cap, checklist, sell triggers).

## 2. Strategies

### 2.1 Concentrated quality small/mid-cap portfolio (checklist-based)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Growth / quality, concentrated, long-hold (fundamental, discretionary) | 3, 5 |
| Timeframe & holding period | "Have a 3-5 year POV for any stock"; long consolidations are expected before multibaggers | 5, 11 |
| Universe / eligibility filters | Undiscovered quality small/midcap, large opportunity size, low PE, zero institutional holding. Checklist: ethical promoter, big opportunity size, good ROCE, low valuation (marketcap and PE), expected CAGR at least 20-25%, first-gen entrepreneur with execution record, high promoter stake (at least 55-70%), low debt, leader in a fast-expanding segment. Promoter preferably well educated, in his 40s, with a support network | 5, 7, 9 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Checklist above must be met. Prepare a short investment-thesis note. Go through the quarterly shareholding pattern on BSE. PE-player or savvy-investor holdings are a positive. First listing in a sector is a positive | 7, 9 |
| Entry trigger & order type | Not found in this text (no price trigger). Do homework and speak to management, then buy | 4 |
| Initial stop-loss | Not found in this text. Only a principle: "Be wrong as fast as you can" (avoid big losses) | 10 |
| Exits: profit-taking | Not found in this text. Selling is discretionary: "Learn the art of selling & sell" | 6 |
| Exits: trailing / time / signal | Sell when (a) something better is found, (b) the story changes (e.g. new CMD), (c) overvaluation (examples: Astral at 400 and 60 PE; Page Ind at 13000), (d) unethical behaviour or management incompetence (e.g. NPA recognition issues). Also sell if performance deteriorates | 6, 8 |
| Position sizing | Allocation is "most important"; take big bets, with at least a minimum ticket size per stock. Exact weights not given | 3, 5, 11 |
| Adding to / pyramiding | "Average on upside once co executes" (author bought one stock 32 times) | 5 |
| Portfolio limits (max positions, correlation, heat) | About 10-12 holdings. "Having too many stocks in your PF" is listed as a mistake. Leverage cap 115-120% of PF (see 3) | 3, 8 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of holdings | 10-12 | Earlier 50-60 (judged too many) | 3 |
| Expected earnings CAGR | at least 20-25% | - | 7 |
| Promoter holding | at least 55-70% | "High promoter stake" (no number) on p. 7 | 9 |
| Institutional holding | zero | - | 5 |
| PE | "low" (no number) | - | 5, 7 |
| Opportunity size / market cap | large opportunity vs low market cap (no numbers) | - | 5, 9 |
| ROCE | "good" (no number) | - | 7 |
| Debt | "low" (no number) | - | 7 |
| Holding horizon | 3-5 years | - | 5 |
| Promoter age | 40s | - | 9 |

**Key quotes**
- "Reduced my holdings from 50-60 to around 10-12" [p. 3]
- "Learnt allocation most important" [p. 3]
- "Have a 3-5 year POV for any stock" [p. 5]
- "low PE stock & zero instl holding" [p. 5]
- "CAGR expected to be in range of atleast 20-25%" [p. 7]
- "High promoter stake of atleast 55-70%" [p. 9]
- "Average on upside once co executes" [p. 5]
- "Learn the art of selling & sell" [p. 6]
- "Be wrong as fast as you can" [p. 10]

**Pseudocode** (forward-test only; fundamentals are available only from Feb 2026)
```
each rebalance date (e.g. quarterly):
  universe = NSE stocks with mcap in small/mid band            # ASSUMPTION band
  candidates = universe where
      promoter_holding >= 55
      AND institutional_holding == 0 (or <= 1)                 # ASSUMPTION tolerance
      AND ROCE >= 15                                           # ASSUMPTION; book says "good"
      AND debt_to_equity <= 0.5                                # ASSUMPTION; book says "low"
      AND PE <= universe_median_PE                             # ASSUMPTION; book says "low"
      AND earnings_growth_3y >= 20
  rank candidates by earnings_growth_3y (or composite)         # ASSUMPTION; no ranking given
  hold top 10-12, equal weight                                 # ASSUMPTION; weights not given
  exit a holding if it leaves candidates for 2 consecutive quarters
      OR promoter_holding falls below 55
      OR PE > 2 x entry PE                                     # ASSUMPTION for "overvaluation"
  optional add: if price > cost AND last 2 quarters EPS growth > 0, add 1/3 position   # ASSUMPTION for "average on upside"
```

**Ambiguities & assumptions**
- Most criteria are qualitative (ethics, "fire in belly", management quality, 80% of the bet is on people [p. 7]). They cannot be coded. ASSUMPTION: only the quantitative proxies (promoter stake, ROCE, debt, PE, growth, institutional holding) are coded.
- No numbers for "low PE", "good ROCE" or "low debt". ASSUMPTION: use the thresholds in the pseudocode above.
- Promoter stake appears as "High" on p. 7 and at least 55-70% on p. 9. ASSUMPTION: use at least 55%.
- No entry price trigger, stop-loss or profit target. ASSUMPTION: no stop; exit only on the fundamental or valuation rules above. A price stop would be a deviation from the text.
- Position weights are not stated beyond "big bets". ASSUMPTION: equal weight.
- "Not found in this book": the market-cap definition of small/mid cap, the rebalance frequency, and the sell-for-better-idea rule (needs a comparison metric).

### 2.2 Buy IPOs on listing
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Event-driven / IPO-listing growth bet | 5 |
| Timeframe & holding period | Then held under the 3-5 year view (2.1) | 5 |
| Universe / eligibility filters | Quality IPOs only. Avoid "junk IPOs with listing gain perspective". Study the DRHP beforehand. "Biases against them" should be ignored | 5, 8 |
| Market / regime filter | Not found in this text | - |
| Setup conditions | Same quality checklist as 2.1; DRHP study. GMP (grey market premium) is mentioned as a route to bet big | 5, 7 |
| Entry trigger & order type | Buy on listing, or "thru GMP" | 5 |
| Initial stop-loss | Not found in this text | - |
| Exits: profit-taking | Not found in this text | - |
| Exits: trailing / time / signal | Same sell triggers as 2.1 | 6 |
| Position sizing | "Bet big", with at least a minimum ticket size | 5 |
| Adding to / pyramiding | Average on upside once the company executes | 5 |
| Portfolio limits (max positions, correlation, heat) | Part of the 10-12 holdings | 3 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Entry timing | listing day | via GMP (pre-listing) | 5 |
| IPO quality filter | not quantified | DRHP study | 5 |

**Key quotes**
- "IPOs are fertile ground for finding such gems" [p. 5]
- "bet big on listing or thru GMP" [p. 5]
- "Applying in junk IPOs with listing gain perspective" [p. 8]

**Pseudocode** (price-only proxy; the quality screen needs fundamentals, which are forward-test only)
```
for each stock with first trading date d0 (listing):
  if quality_screen(stock) passes:             # fundamentals/DRHP; not backtestable
     buy at close of d0 (or open of d0+1)      # ASSUMPTION: listing day open is not reliably buyable
     hold per 2.1 exit rules
Price-only baseline: buy all new listings at close of d0, equal weight, hold 3 years (tests the author's claim crudely).
```

**Ambiguities & assumptions**
- "Quality" cannot be coded from prices. ASSUMPTION: baseline test buys all listings, and the quality screen can only be forward-tested.
- Whether to buy the listing-day open or close is not stated. ASSUMPTION: close of listing day.
- Allotment, GMP and the ability to pick up shares at listing are not testable with our data.

## 3. Risk & money-management rules
| Rule | Page |
|---|---|
| Leverage: "Don't overdo it but one can have leverage max till 115-120% of your PF". The leverage should earn more than the loan interest | 4, 2 |
| Leverage is "a double edge sword"; build experience and confidence first | 4 |
| Leverage was used mainly for IPOs; leverage lets you buy immediately without selling something | 4 |
| Concentration: about 10-12 holdings; too many stocks is a mistake | 3, 8 |
| Allocate at least a minimum ticket size to a stock; not betting big despite conviction is a mistake | 5, 8, 11 |
| Avoid big losses: "Be wrong as fast as you can" | 10 |
| Do not sell out too soon on small gains; do not hold deteriorating companies | 8 |
| Prepare a checklist before buying and try to adhere to it | 7 |

## 4. Non-codable guidance
- Find a mentor 10-15 years ahead of you; network; ignore negative non-achievers [p. 4, 11].
- Scuttlebutt is most important; speak to management after lots of homework [p. 4].
- Temperament and patience are most important [p. 5].
- Master your emotions; remove distractions (TV, politics, watching prices all day) [p. 10].
- "Inactivity pays a lot"; take decisions, since scared money doesn't make money [p. 10].
- Avoid price anchoring and preconceived biases (for example against PSU companies) [p. 8].
- Main losses come from buying low-quality scrips in favourable business conditions [p. 11].
- Owner-operator managements make better decisions [p. 11].
- Most multibaggers have long consolidation periods [p. 11].
- Page 12 is a disclaimer that the views are biased and not a stock recommendation [p. 12].

## 5. Adapting to NSE (Indian equities)
- **Data required:** Daily OHLCV (listing date, price history for IPO baseline); fundamentals (promoter holding %, institutional holding %, ROCE, debt/equity, PE, 3-year earnings growth, market cap); IPO listing date/price.
- **Testability with our data:**
  - Backtestable (2005-2026 prices): only the crude "buy all new listings at listing close, hold N years" baseline for 2.2, and generic concentrated-portfolio statistics (10-12 equal-weight holdings).
  - Forward-test only: the 2.1 fundamental screen (fundamentals are point-in-time only from Feb 2026, 3-year growth fields from May 2026).
  - Cannot be tested with our data: leverage (loans against shares, IDBI/HDFC financing, 115-120% cap), IPO allotment tactics (multiple demat accounts, firm allotment, DRHP reading, GMP), scuttlebutt, management meetings, promoter ethics, and shareholding-pattern details (institutional holding history).
- **Market-structure differences:**
  - Small-cap liquidity and circuit limits make "buy immediately" and 32 repeated purchases hard at scale. ASSUMPTION: cap position size at a small fraction of average daily traded value.
  - STT, brokerage and about 0.1% slippage apply; the author's long holding period makes costs minor.
  - Listing-day buying faces circuit bands on new listings. ASSUMPTION: buy at listing close only if not locked at upper circuit.
  - Leverage cannot be backtested; any test should be unlevered.

## 6. Verdict
- **Codeability:** Partly. Only a few quantitative proxies (holding count, promoter stake, growth, listing date) are codable; the core edge (people, ethics, scuttlebutt) is discretionary.
- **Priority for backtesting:** Low. There is no entry/exit price rule, no track record, and the fundamentals can only be forward-tested.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating qualitative checklist items as hard thresholds and inventing numbers (low PE, good ROCE) that the text does not give.
  2. Backtesting with fundamentals that are not point-in-time before 2026 (look-ahead bias), or ignoring survivorship.
  3. Including leverage (115-120%) or IPO allotment advantages in a backtest, or assuming listing-day fills at the open despite circuit limits.
