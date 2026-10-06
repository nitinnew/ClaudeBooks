# Diamonds in the Dust: Consistent Compounding for Extraordinary Wealth Creation — Saurabh Mukherjea, Rakshit Ranjan, Salil Desai

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/Diamonds In The Dust by Saurabh Mukherjea.pdf` (file id 1QlyG540Bu1vMQZcztGEiWFsEu0VKzDWI)
- **Text file used:** text/mukherjea_diamonds_dust.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/<key>.md text/<key>.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read sequentially, every line 1-7705, last marker reached [[PAGE 259]]. Pages with no text at all: 1, 2, 20, 44, 104, 119, 152, 178, 200 (blank or image-only); pages 4, 45, 120, 153 hold only a publisher imprint or a bare chapter number. Nothing was skimmed or only scanned. Appendices read in full: Appendix 1 "The Marcellus Checklist" (p. 217-221: accounting-ratio, governance, bank/NBFC, competitive-advantage, capital-allocation and timing/pricing checklists), Appendix 2 "Sir John Kay's IBAS Framework" (p. 222-233: brands, architecture, innovation, strategic assets, with Amul, Maruti, Tata and BMW examples), Appendix 3 "Robert Kirby's Coffee Can Investing Method" (p. 234-242: the only mechanical stock screen and its back-test summary, plus footnotes on p. 254-255). Glossary (p. 243-244), Notes (p. 245-255), Acknowledgements (p. 256-257) and copyright (p. 258-259) were also read. Limitation: the charts and several tables are images with no text layer (examples: Exhibits 1-4, 7, 13-15, 63-64, 69-72, 77-82, and the per-iteration data of Exhibits 84-85 and the seven-stock list of Exhibit 87 on p. 237-242), so figures that exist only inside those images are not captured here. A few rotated header fragments (stray one- or two-letter lines) appear in the text layer and carry no content. Reading done by a Sonnet sub-agent; the coordinator re-ran the verifier and an exact-page check (one quote moved from [p. 53] to [p. 54]) and spot-checked 10 unquoted table citations.

## 1. The method in brief

Marcellus's "Consistent Compounding" is a long-only, buy-and-hold approach for Indian equities. The authors argue that returns in India come from (1) avoiding companies with unreliable accounts ("Credible Accounting"), (2) owning dominant franchises that earn return on capital far above the cost of capital for decades ("Competitive Advantage"), and (3) owning managements that redeploy free cash flow at high returns ("Capital Allocation") [p. 37-38]. They call the rare companies that pass all three "Type C" (under 1 per cent of listed stocks by count, with earnings growth of about 25 per cent a year) [p. 41]. Once such a stock is held, "when to buy" (market timing, P/E, valuation) is argued to be largely irrelevant, so the investor should stay invested for at least ten years [p. 179-182, 189-195]. CAPM and beta are rejected on Indian data: lower-beta, lower-volatility stocks gave higher returns [p. 34-35]. There are no price-based technical rules in this book; every selection rule is fundamental, and the horizon is ten years or more.

Evidence offered: (a) a mechanical "Coffee Can" screen (sales growth of at least 10 per cent in each of ten years plus pre-tax RoCE of at least 15 per cent, market cap at least Rs 100 crore, equal-weighted 10-25 stocks, held ten years untouched) that beat the benchmark in all but one of twenty back-tested iterations since 1991, with median annualised outperformance of 7 percentage points over the last nineteen years [p. 235-237]; (b) a 12-ratio forensic accounting model whose top five deciles beat the bottom three by 7 per cent a year over CY2016-20 [p. 56], and an 11-ratio bank/NBFC model whose top deciles beat the bottom by 33 percentage points a year [p. 111]; (c) Re 1 invested on 31 Dec 2000 growing to Rs 142.7 to Rs 532.2 for chosen compounders versus Rs 12.0 for the Sensex [p. 142, 145, 148, 171, 173]; (d) "Mr Gifted vs Mr Mortal" tests showing perfect annual timing adds only about 1 to 2 percentage points for these compounders [p. 184-191]. All results are the authors' own (Ace Equity data) and mostly hindsight-selected; costs and dividends treatment is noted case by case.

## 2. Strategies

Twelve separately testable rules are captured below. Sections 2.1-2.2 are the only fully mechanical portfolio constructions in the book; 2.3-2.8 are fundamental screens whose ratio definitions and cut-offs are only partly given; 2.9-2.12 are timing, valuation, allocation and risk-factor rules.

### 2.1 Coffee Can screen — non-financial companies (Kirby method, Indian version)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality/growth screen with ten-year buy-and-hold (Kirby "coffee can") | 234-235 |
| Timeframe & holding period | Leave the portfolio untouched for ten years regardless of interim performance; each yearly iteration lasts up to ten years; portfolio starts 30 June of every year | 235, 242, 240, 255 |
| Universe / eligibility filters | About 6,000 listed companies; keep those with market cap of at least Rs 100 crore (about 1,500, because data on smaller companies is "somewhat suspect"); then growth and RoCE filters below | 235-236 |
| Market / regime filter | None. Timing of entry is argued to be irrelevant | 179-182 |
| Setup conditions | (1) Sales growth of at least 10 per cent in each of ten consecutive years; (2) pre-tax RoCE (EBIT / capital employed) of at least 15 per cent over the same decade ("every year" per p. 242) | 236, 254, 242 |
| Entry trigger & order type | Buy all qualifying stocks together at the iteration start (30 June). Order type not specified | 242, 255 |
| Initial stop-loss | None | 242 |
| Exits: profit-taking | None; no trimming | 235, 242 |
| Exits: trailing / time / signal | Time exit only: hold up to ten years ("left untouched for the next ten years") | 242, 240 |
| Position sizing | Equal weight ("equal allocation of Rs 100" to each qualifying stock) | 242, 255 |
| Adding to / pyramiding | Not specified within an iteration; a new iteration is started each 30 June | 255 |
| Portfolio limits (max positions, correlation, heat) | 10-25 stocks; the July 2020 screen returned seven stocks | 235, 242 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Minimum market cap | Rs 100 crore | Not specified | 235 |
| Revenue growth filter | at least 10 per cent every year, 10 years | 13 per cent (nominal GDP) tried first but only six of ~1,500 passed; relaxed to 9.5 per cent in FY2018 once to admit Astral | 237, 255 |
| Return filter | pre-tax RoCE at least 15 per cent | derived as risk-free about 6.2 per cent plus equity risk premium 7-7.5 per cent | 236 |
| Look-back window | preceding ten years (e.g. FY2011-20) | Not specified | 236, 242 |
| Number of stocks | 10-25 | seven in the 2020 screen | 235, 242 |
| Holding period | ten years | results shown for holds of 3 and 5 years or more | 240-241 |
| Start date | 30 June each year | Not specified | 255 |
| Return measure | TSR (price change plus dividends and buybacks) | Not specified | 255 |

**Reported results**

| Result | Value | Page |
|---|---|---|
| Back-test history | data back to 1991; twenty iterations; over 150 years of cumulative portfolio history | 237, 240 |
| Iterations beating benchmark | all but one of twenty | 237 |
| Median annualised outperformance | 7 percentage points over the last nineteen years | 237 |
| Median portfolio return | 22-23 per cent a year for holding periods over three years | 240 |
| Probability of positive return | above 95 per cent if held three years or more; above 95 per cent chance of more than 6 per cent a year if held five years or more | 241 |
| Source of return | mostly EPS growth, not P/E re-rating | 239 |
| Stress periods | outperformed in 2008 (Lehman) and 2020 (COVID) | 237 |
| Rolling return study | July 2000 to December 2020, weekly rolling windows | 255 |

**Key quotes**
- "We use straightforward investment filters to identify 10–25 high-quality stocks," [p. 235]
- "and we then leave the portfolio untouched for a decade" [p. 235]
- "minimum market capitalization of Rs 100 crore" [p. 235]
- "we are looking for companies which have grown sales every single year for ten consecutive years by at least 10 per cent" [p. 254]
- "We use 15 per cent as a minimum because we believe that is the bare minimum" [p. 236]
- "needs to be invested equally in all the stocks mentioned in this list" [p. 242]
- "This portfolio should be left untouched for the next ten years" [p. 242]
- "The portfolio kicks off on 30 June of every year." [p. 255]
- "The sales growth filter has been relaxed to 9.5 per cent in FY2018 to include" [p. 255]
- "only six out of the nearly 1,500 firms" [p. 237]
- "median compounded annualized outperformance" [p. 237]
- "Kirby’s approach has outperformed benchmark indices over all but one of its twenty iterations" [p. 237]

**Pseudocode**
```
# Data: annual sales, EBIT, capital employed (debt + equity), market cap, dividends, price
for each June 30 (iteration year Y):
    universe = [s for s in listed if mcap(s, Y) >= Rs100cr and is_non_financial(s)]
    for s in universe:
        ok = True
        for fy in (Y-10 .. Y-1):                    # ten completed fiscal years
            if sales[fy]/sales[fy-1] - 1 < 0.10: ok = False
            if EBIT[fy] / capital_employed[fy] < 0.15: ok = False
        if ok: picks.append(s)
    weights = equal(picks)                          # book: 10-25 names typical
    buy(picks, weights, date=Y-06-30 or next trading day)
    hold until Y+10 (no sells, no rebalance)
    record TSR (price + dividends) vs benchmark
```

**Ambiguities & assumptions**
- Whether RoCE of 15 per cent must hold every year or on average over the decade. Text p. 236 says "over the preceding decade ... alongside generating" while p. 242 says "every year". ASSUMPTION: every year (p. 242 is the later, more explicit statement).
- Capital employed definition: p. 236 says sum of debt liabilities and shareholders' equity; opening, closing or average not specified. ASSUMPTION: closing balance.
- EBIT includes other income per the Chapter 5 footnote (p. 249). ASSUMPTION: apply the same here.
- Market cap measured at what date, and whether it must hold in the first year of the decade or at purchase: not specified. ASSUMPTION: at purchase date.
- Sales growth on net sales vs total income: not specified. ASSUMPTION: net sales.
- Whether the iteration is entered on 30 June or the following open: not specified. ASSUMPTION: next trading day close or open.
- A stock that fails (fraud, delisting) mid-hold is simply held; no replacement rule stated. ASSUMPTION: no replacement; treat delisted stock at last price.
- The authors loosened one cutoff (9.5 per cent) post hoc, so the published results contain some discretion [p. 255].

### 2.2 Coffee Can screen — banks and NBFCs (financial variant)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality/growth screen with ten-year buy-and-hold | 237 |
| Timeframe & holding period | Same as 2.1: ten years untouched | 242 |
| Universe / eligibility filters | Financial services companies with market cap above Rs 100 crore (same universe screen as 2.1; separate financial thresholds not given) | 235, 242 |
| Market / regime filter | None | 179-182 |
| Setup conditions | Return on equity (post-tax) of at least 15 per cent and loan growth of at least 15 per cent, "every year" over FY2011-20 | 237, 242 |
| Entry trigger & order type | As 2.1 | 255 |
| Initial stop-loss | None | 242 |
| Exits: profit-taking | None | 242 |
| Exits: trailing / time / signal | Time exit at ten years | 242 |
| Position sizing | Equal weight, pooled in the same portfolio as non-financials | 242 |
| Adding to / pyramiding | Not specified | 255 |
| Portfolio limits | 10-25 stocks overall | 235 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RoE | at least 15 per cent | RoE preferred to RoA since it also reflects how much the bank borrows | 237, 254 |
| Loan growth | at least 15 per cent a year | justified by 13 per cent average nominal GDP growth | 237 |
| Min market cap | Rs 100 crore | Not specified | 235 |

Separate back-test results for financials are Not specified; they are included in the combined results in 2.1.

**Key quotes**
- "For financial services stocks, we modify the filters of return on equity (RoE)" [p. 237]
- "a loan growth of at least 15 per cent is an indication of a bank’s ability" [p. 237]
- "fairer measure of the ability of banks and non-bank lenders to generate higher" [p. 237]
- "RoE OF 15 PER CENT" [p. 237]

**Pseudocode**
```
# Data: net profit, average equity (or closing), loans/advances, mcap
for each June 30:
    for s in financial_universe(mcap >= 100cr):
        ok = all(ROE[fy] >= 0.15 and loan_growth[fy] >= 0.15 for fy in last_10_fiscal_years)
        if ok: picks.append(s)
    merge with non-financial picks from 2.1; equal weight; hold 10 years
```

**Ambiguities & assumptions**
- Whether the ten-year "every year" test applies to RoE and loan growth like it does to 2.1: the text on p. 242 says "every year". ASSUMPTION: yes.
- RoE on average or closing equity: Not specified. ASSUMPTION: average equity.
- Classification of insurers, AMCs and brokers as "financial services": not stated. ASSUMPTION: lenders only (bank, NBFC, HFC), since filters refer to loan growth.

### 2.3 Level 1 forensic accounting model — non-financial companies (12-ratio decile rank)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality filter / negative screen (avoid poor accounting) | 54-56 |
| Timeframe & holding period | Annual statements; ratings for FY2015-19 tested against CY2016-20 returns; no re-rating frequency given | 56-57 |
| Universe / eligibility filters | Broad-based exchange indices (BSE500 examples); the model database holds time series for 1,300 of India's largest listed companies; non-financial companies only (banks use 2.4) | 36, 54-55 |
| Market / regime filter | None | Not specified |
| Setup conditions | Rank stocks on each of twelve forensic ratios, then a final decile ranking D1 (best) to D10 (worst) | 55-56 |
| Entry trigger & order type | Hold only D1-D5 ("Zone of Quality"); D6-D7 "best avoided"; D8-D10 "Zone of Thuggery" excluded | 56 |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | Drop a name if it falls below D5 on re-scoring (implied: "we typically eliminate the companies which score low") | 54 |
| Position sizing | Not specified | Not specified |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | None; about 40 per cent of companies in broad indices fail the quantitative screen | 54 |

**The twelve ratios.** The book names only these eight (Exhibit 12, repeated in Appendix 1); the other four are not found in this book.

| Check | Ratio | Book's rationale | Page |
|---|---|---|---|
| Income statement | Cash flow from operations (CFO) as % of EBITDA | aggressive revenue/earnings recognition; low trend means profit not turning into cash | 55, 217 |
| Income statement | Year-on-year volatility in depreciation rate | depreciation is a non-cash, easily manipulated charge | 55, 217 |
| Income statement | Change in reserves and surplus explained by profit/loss and dividends | direct write-offs against the balance sheet instead of the P&L | 55, 217 |
| Balance sheet | Yield on cash and cash equivalents | misstated cash or mis-utilised cash | 55, 217 |
| Balance sheet | Contingent liabilities as % of net worth (latest year) | off-balance-sheet risk | 55, 217 |
| Cash theft | Capital work in progress to gross block | high ratio means unsubstantiated capex | 55, 217 |
| Cash theft | Free cash flow (CFO plus cash flow from investing) to median revenues | cash siphoned or earnings not believable | 55, 218 |
| Auditor objectivity | Growth in auditors' remuneration to growth in revenues | faster growth raises concern about auditor independence | 56, 218 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of ratios | 12 | 8 named | 55 |
| Decile cut: keep | D1-D5 | Zone of Quality | 56 |
| Decile cut: avoid | D6-D7 centre, best avoided; D8-D10 Zone of Thuggery | Not specified | 56 |
| Share rejected | nearly 40 per cent of index companies | Not specified | 54 |
| Statement history required | Not specified for non-financials (at least six years for lenders, p. 110) | Not specified | 110 |
| Rank aggregation method | Not specified | Not specified | 56 |

**Reported results**

| Result | Value | Page |
|---|---|---|
| Zone of Quality vs Zone of Thuggery | 7 per cent a year outperformance over CY2016-20 | 56 |
| Fifty-three BSE500 names in D8-D10 each year FY2015-19 | average CAGR of minus 14 per cent over CY2016-20 vs BSE500 plus 11 per cent | 57 |
| BSE500 churn context | about 40 per cent of Dec-2009 members exited by 2019 for non-corporate-action reasons; only 18 per cent compounded above 15 per cent; 51 per cent were negative | 48-49 |
| Cox & Kings | D10 on the model for most of 2009-19 | 63 |

**Key quotes**
- "using a set of twelve ratios, that helps us grade companies on" [p. 55]
- "The top five deciles, i.e., D1 to D5, are generally where" [p. 56]
- "the bottom 30 per cent, i.e., D8 to D10, generally" [p. 56]
- "deciles lie somewhere in the centre of the quality gradient and are also best" [p. 56]
- "companies which score low on our forensic model" [p. 54]
- "by a significant 7 per cent per annum over CY2016–20" [p. 56]
- "negative CAGR of 14 per cent, against the benchmark BSE500’s 11 per cent" [p. 57]

**Pseudocode**
```
# Data: CFO, EBITDA, depreciation & gross block (rate = dep/avg gross block), reserves, PAT, dividends,
#       cash & equivalents, interest income, contingent liabilities, net worth, CWIP, gross block,
#       CFO, CFI, revenue, auditor remuneration
for each stock s, each year t:
    r1 = CFO/EBITDA                      (higher better; use multi-year average/trend)
    r2 = stdev of yoy change in dep rate (lower better)
    r3 = |delta reserves - (PAT - dividends)| / PAT   (lower better)
    r4 = interest income / avg cash      (higher better)
    r5 = contingent liab / net worth     (lower better)
    r6 = CWIP / gross block              (lower better)
    r7 = (CFO + CFI) / median(revenue)   (higher better)
    r8 = auditor_fee_growth - revenue_growth (lower better)
    # four more ratios not given in book: omit
    rank each ratio across universe -> 1..10 (D1 best)
    score = aggregate(ranks)             # method unspecified
    decile = rank(score) -> D1..D10
    eligible = decile <= D5
```

**Ambiguities & assumptions**
- Four of the twelve ratios are not given. ASSUMPTION: run with the eight named ratios only; flag the result as an approximation.
- Direction of each ratio (high or low is good) is not stated; implied from the rationale column. ASSUMPTION: as in the pseudocode.
- Aggregation (sum of ranks, average rank or other) is not given for non-financials; for lenders ranks are "cumulated" [p. 110]. ASSUMPTION: sum of decile ranks.
- Number of years per ratio and use of single-year vs multi-year averages is not specified, except that trend is mentioned for CFO/EBITDA [p. 217]. ASSUMPTION: five-year average.
- Treatment of ties and of companies with negative EBITDA or equity: not specified.
- Level 1 is a filter on stocks already deemed to be quality; the 7 per cent number compares zones, not a tradable portfolio.

### 2.4 Level 1 forensic accounting model — banks and NBFCs (11-ratio decile rank)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality filter / negative screen | 109-110 |
| Timeframe & holding period | At least six years of statements per company; tested over CY2016-20 | 110-111 |
| Universe / eligibility filters | Financial services companies; test universe of 95 with market cap above Rs 1,000 crore | 106 |
| Market / regime filter | None | Not specified |
| Setup conditions | Rank on eleven ratios individually into deciles D1 (best) to D10, cumulate the ranks, derive a final pecking order | 110 |
| Entry trigger & order type | Hold only the top three deciles ("Zone of Quality"); next three "Zone of Opacity"; bottom four "Zone of Thuggery" | 110 |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | Avoid poor-accounting lenders whether or not the fraud is public, and do not bottom-fish after exposure | 108 |
| Position sizing | Not specified | Not specified |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | Not specified | Not specified |

**The eleven ratios.** The book names six (Exhibit 53, repeated in Appendix 1) plus change in reserves as a percentage of PAT used in the DHFL case; the rest are not found in this book.

| Check | Ratio | Rationale | Page |
|---|---|---|---|
| Income statement | Treasury income as % of net interest income (NII) | aggressive booking of treasury gains; also look at volatility | 110, 114 |
| Income statement | Fee income as % of NII | high vs peers suggests aggressive lending for upfront fees | 110, 113 |
| Balance sheet | NPA volatility | inconsistent NPA recognition | 110 |
| Balance sheet | Provision as % of NPA | low means inadequate provisioning | 110 |
| Balance sheet | Contingent liabilities to net worth | off-balance-sheet risk | 110 |
| Auditor | Growth in auditor remuneration vs total interest income | auditor objectivity | 110 |
| Reserves (DHFL case) | Change in reserves as % of PAT (normally 100 per cent) | adjustments bypassing the P&L | 114 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of ratios | 11 | 6-7 named | 110 |
| History | at least 6 years | Not specified | 110 |
| Keep | top 3 deciles (D1-D3) | Not specified | 110 |
| Avoid | bottom 4 (D7-D10); middle 3 is "Opacity" | Not specified | 110 |
| Test universe | 95 financials, mcap above Rs 1,000 crore | Not specified | 106 |

**Reported results**

| Result | Value | Page |
|---|---|---|
| Zone of Quality vs Zone of Thuggery | 33 percentage points a year over CY2016-20 | 111 |
| High-quality vs poor-quality lenders | 13 per cent CAGR vs minus 20 per cent, CY2016-20 | 118 |
| Share of banks/NBFCs with poor accounting | about 70 per cent | 106 |
| DHFL | ranked D10 (worst among housing finance peers) on FY2013-18 reports; share fell 60 per cent in a day in Sept 2018; AAA to D within six months | 112, 117, 107 |

**Key quotes**
- "Our methodology is to evaluate eleven accounting ratios covering income" [p. 110]
- "using at least six years of historical financial statements" [p. 110]
- "These ranks are then cumulated across parameters to give a final pecking order" [p. 110]
- "next three as the ‘Zone of Opacity’ and the bottom four as the ‘Zone of" [p. 110]
- "points per annum over CY2016–20" [p. 111]
- "generated a 13 per cent CAGR return, vs a -20 per cent by financial" [p. 118]

**Pseudocode**
```
# Data (lenders): treasury income, fee income, NII, gross NPA series, provisions, contingent liabilities,
#                 net worth, auditor fees, total interest income, reserves, PAT
for each lender, using last >=6 fiscal years:
    treasury_pct = treasury_income / NII ;  fee_pct = fee_income / NII
    npa_vol = stdev(NPA ratio) ; prov_cov = provisions / NPA ; cont = contingent / net_worth
    aud = auditor_fee_growth - total_interest_income_growth ; res = delta_reserves / PAT
    decile-rank each (D1 best) ; sum ranks ; final decile
    hold only if final decile in {D1,D2,D3}
```

**Ambiguities & assumptions**
- Five of eleven ratios not found in this book. ASSUMPTION: use the seven named.
- Directions of each ratio are implied, not stated. ASSUMPTION: as in the table.
- Top-3 deciles rule for "Zone of Quality" vs the non-financial top-5: both stated. Kept separate.
- Whether the ranking is cross-sectional against all lenders or against peer subsets (e.g. housing finance peers for DHFL on p. 112): not specified. ASSUMPTION: all lenders together.

### 2.5 Retail annual-report "three crosses" screen

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality filter / negative screen for retail investors | 102-103 |
| Timeframe & holding period | Last three years of annual reports | 102-103 |
| Universe / eligibility filters | Any listed company the investor is considering; use consolidated statements | 102 |
| Market / regime filter | None | Not specified |
| Setup conditions | Cross 1: board largely promoter relatives and friends. Cross 2: CFO plus CFI not greater than zero. Cross 3: multiple large related-party transactions with promoter and family entities | 102-103 |
| Entry trigger & order type | Invest only if the company clears the checks; at three crosses "move on" | 103 |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | Not specified (re-test as new annual reports arrive is implied only) | Not specified |
| Position sizing | Not specified | Not specified |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | None | Not specified |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| CFO + CFI | must be greater than zero (consolidated) | Not specified | 102-103 |
| Years of reports | 3 | Not specified | 102 |
| Crosses to reject | three ("move on"); one and two crosses have no stated consequence | Not specified | 102-103 |
| Related-party "multiple large" | Not specified | Not specified | 103 |

**Key quotes**
- "Is the board of the company largely made up of relatives of the promoter" [p. 102]
- "In the cash flow statement in the consolidated financial statements of the" [p. 102]
- "greater than zero, then put a second cross against the company" [p. 103]
- "put a third cross against the company" [p. 103]
- "if you can read the last three years of annual reports of the" [p. 102]

**Pseudocode**
```
# Data: consolidated CFO, CFI (3 years); board composition; related-party note
crosses = 0
if promoter_relatives_share_of_board is "large": crosses += 1      # no number in book
if (CFO + CFI) <= 0 in the latest year (or 3-yr sum): crosses += 1
if large_related_party_txns: crosses += 1
reject if crosses >= 3 else keep (caution if crosses in {1,2})
```

**Ambiguities & assumptions**
- Whether CFO + CFI is tested for one year or each of three years: not specified. ASSUMPTION: three-year sum of (CFO + CFI) must be positive.
- No numeric test for board makeup or "multiple large" related-party transactions. ASSUMPTION: skip these two in a data-only backtest.
- The author says 1 cross is a warning only. ASSUMPTION: reject only at 3, but test a stricter reject-at-2 variant.

### 2.6 Level 2 accounting and governance red-flag checklist (deep-dive)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality filter / negative screen (checklist) | 61-62, 218 |
| Timeframe & holding period | Applied during deep-dive diligence, then monitored | 61 |
| Universe / eligibility filters | Companies that pass the Level 1 quantitative screen | 54 |
| Market / regime filter | None | Not specified |
| Setup conditions | Check list below; each item is a red flag when adverse | 62, 218 |
| Entry trigger & order type | Not specified | Not specified |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | Not specified | Not specified |
| Position sizing | Not specified | Not specified |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | None | Not specified |

**Checklist items** (all thresholds Not specified):

| Group | Items | Page |
|---|---|---|
| Advanced accounting | common-sized income statement vs peers; DuPont vs peers; R&D capitalisation vs P&L charge; goodwill as % of net worth; frequent changes in auditors; significant adverse comment in auditor's report; significant operations not audited by principal auditor; audit committee chaired by independent director or not; frequent changes in accounting periods | 62, 218 |
| Governance | related-party transactions; promoters' other business interests and stress there; M&A with promoter entities; promoter litigation; family structure and succession; pledge of promoter shareholding; insider buying and selling; promoter remuneration; frequency and necessity of equity dilution | 62, 218 |
| Fraud traits (Exhibit 11) | P&L glossier than balance sheet and cash flow; group companies in similar business; extensive related-party dealings; listed entity funding promoter ventures; high promoter pledge; consistent fall in promoter holding; off-balance-sheet liabilities and complex holding structures; repeated investment-banker engagements, frequent M&A and fund-raising; weak board; frequent changes of year-end, auditor, CFO | 53-54 |
| Case-study evidence | Cox & Kings promoter pledge rose to almost 70 per cent; goodwill 45-50 per cent of capital employed after FY2012; Amtek never had positive free cash flow in any year FY2003-14; Deccan Chronicle pledged 54 per cent | 82-83, 77, 95, 59 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Pledge level that fails | Not specified | C&K peaked near 70 per cent; Deccan Chronicle 54 per cent | 59, 82-83 |
| Goodwill / net worth cut | Not specified | C&K goodwill 50 per cent of capital employed (FY14) | 77 |
| Auditor tenure | Not specified | Amtek same auditor from at least FY2002 | 101 |
| Independent director tenure | Not specified | 16-18 years called "not ideal" | 101 |

**Key quotes**
- "Significant amounts of promoter holdings in the listed company" [p. 53]
- "Consistent reduction in promoters’ shareholding in the company" [p. 53]
- "Frequent changes in financial" [p. 54]
- "Goodwill as % of net worth" [p. 62]
- "Frequency and necessity of equity dilution" [p. 62]

**Pseudocode**
```
# Data (promoter pledge %, promoter holding trend, goodwill, net worth, auditor name history,
#       equity issuance events, related-party revenue share, year-end changes)
flags = 0
flags += promoter_pledge_pct > X          # X not in book
flags += promoter_holding_change_3y < 0   # "consistent reduction"
flags += goodwill / net_worth > Y         # Y not in book
flags += auditor_changes_5y >= 2
flags += equity_raises_5y >= 2
flags += related_party_rev_share > Z      # Z not in book (C&K 92% standalone)
exclude if flags >= K                     # K not in book
```

**Ambiguities & assumptions**
- The book gives no cut-offs. ASSUMPTION: use the values from its own cases as upper-bound illustrations only, and test a grid (pledge above 25 per cent, goodwill above 20 per cent of net worth, two or more auditor changes in five years) rather than treating any as the book's rule.
- "Insider buying and selling", "adverse auditor comment" and board quality cannot be coded from price/OHLCV data.

### 2.7 Consistent-Compounder quality profile (RoCE vs cost of capital, reinvestment, consistent free cash flow)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality / franchise screen (fundamental, ranking) | 121-124, 219-221 |
| Timeframe & holding period | Decade-plus, evaluated over ten years of data | 195-196 |
| Universe / eligibility filters | Non-financial companies for FCFE tests (financials excluded because FCFE is irrelevant for them) | 195 |
| Market / regime filter | None | Not specified |
| Setup conditions | (a) Long-term average RoCE above cost of capital; (b) RoCE well above peers (dominance of the profit pool); (c) high reinvestment rate of free cash flow; (d) positive free cash flow to equity in most years | 219-221, 123, 196 |
| Entry trigger & order type | Not specified | Not specified |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | Periodic "Lethargy Tests" (qualitative, see Section 4) | 148-151 |
| Position sizing | Not specified | Not specified |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | Not specified | Not specified |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Cost of capital for listed Indian firms | around 12-15 per cent | 15 per cent minimum RoCE used in the coffee can | 122, 236 |
| RoCE definition | EBIT / capital employed (pre-tax) | EBIT used instead of EBITDA because depreciation approximates maintenance capex | 154-155, 243 |
| Type C profile | RoCE far above cost of capital for decades; earnings growth about 25 per cent; dividend yield 2-3 per cent | Type B: earnings growth 10-12 per cent; Type A: no growth | 40-41 |
| Dominance test | one or two companies hold about 80 per cent of the sector profit pool | Not specified | 37 |
| Positive FCFE years (10-year window) | 7-10 years = "Best" bucket | 4-6 mid; 0-3 worst | 196 |
| Reinvestment rate | Hawkins 26 per cent vs TTK Prestige 80 per cent | formula not given | 124 |
| FCFE averaging | average of FY2008-10 vs FY2018-20 for growth | Not specified | 195 |
| Negative FCF test | in rolling 3-year windows, count negative-FCF instances over 10/20 years | Not specified | 221 |

**Reported results (Exhibit 74, non-financial BSE500 stocks, April 2010 to June 2020, CAGR)**

| Bucket (years of positive FCFE of 10) | Stocks | Average return | Page |
|---|---|---|---|
| Best (7-10) | 163 | 15.3 per cent | 196 |
| Mid (4-6) | 114 | 9.2 per cent | 196 |
| Worst (0-3) | 47 | 4.7 per cent | 196 |
| Total | 324 | 9.7 per cent | 196 |

Other results: in the BSE100 only 19 of 74 non-financial names had positive free cash flow in each of ten years [p. 195]; correlation between FCFE CAGR and ten-year share-price return was only 37.3 per cent for the BSE100 and 23.5 per cent for the BSE500 subset [p. 195-196]; for 31 consumer stocks in the BSE500, 77 per cent had positive FCFE in at least seven years and compounded about 23.4 per cent [p. 196-197]; auto and IT were exceptions (Vakrangee 38.7 per cent CAGR with FCFE in only three years, later down about 95 per cent) [p. 197-198]. Ten-year average pre-tax RoCE examples (FY11-20): Asian Paints 44.6 per cent, Pidilite 35.4, Maruti 21.6, Shree Cement 18.3, vs conglomerates 11.0-15.1 [p. 164-165].

**Key quotes**
- "a higher number of years of free cash generation corresponds" [p. 196]
- "compounding is to focus on consistent free cash generation" [p. 198]
- "Is the long-term average return on capital employed (RoCE) greater than the cost of capital?" [p. 219]
- "What is the consistency of free cash generation? In a rolling time-frame of three years, how many" [p. 221]
- "Firms that can sustain high RoCEs, along with a high rate of reinvestment of capital" [p. 123]
- "Earnings growth for such firms tends to be around 25 per cent per annum" [p. 41]
- "the cost of capital for most listed firms in India is around 12–15 per cent" [p. 122]
- "Free Cash Flow to Equity (FCFE) is the residual cash flow that remains after" [p. 251]

**Pseudocode**
```
# Data: EBIT, capital employed, CFO, capex, debt repayments/borrowings (for FCFE), sales, dividends
for s in non_financials:
    rocE_10y = mean(EBIT/CE over last 10y)
    pass_roce = rocE_10y >= 0.15                      # proxy for "above cost of capital"
    fcfe[y] = CFO - capex + net_borrowing             # "after capex and debt service" (p.251 fn7)
    n_pos = count(fcfe[y] > 0 for y in last 10)       # bucket: 7-10 best
    pass_fcf = n_pos >= 7
    keep = pass_roce and pass_fcf
rank survivors by ROCE and sales growth ; equal-weight top N ; hold >= 10y
```

**Ambiguities & assumptions**
- "Capital reinvestment rate" has no formula in the book. ASSUMPTION: (capex + change in working capital) / (CFO), but mark as unvalidated.
- The author never states a numeric cutoff for "high RoCE" beyond the 15 per cent minimum in Appendix 3 and 12-15 per cent cost of capital on p. 122. ASSUMPTION: 15 per cent.
- Ten-year windows need history our snapshot data lack.
- This section is partly an observation (more positive-FCFE years, higher return) rather than a prescribed screen; the buckets are post-hoc.

### 2.8 Capital-allocation red-flag screen

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality filter / negative screen (fundamental, mostly judgment) | 157-164, 220 |
| Timeframe & holding period | Ongoing review of a held compounder | 150-151 |
| Universe / eligibility filters | Companies already passing accounting and franchise screens | 157 |
| Market / regime filter | None | Not specified |
| Setup conditions | Judge the growth strategy on the Ansoff matrix, the quantum of capital allocated relative to net worth, funding by debt vs internal cash, overseas acquisitions, unrelated diversification, promoter's other businesses | 158-164, 173, 220 |
| Entry trigger & order type | Not specified | Not specified |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | Reassess when management starts large leveraged or unrelated expansion (e.g. RoCE structural decline after Corus, FY2008) | 168 |
| Position sizing | Not specified | Not specified |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | Not specified | Not specified |

**Parameters** (all numbers are case illustrations, none is a stated cut-off)

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Acquisition spend vs net worth | Tata Steel about Rs 58,000 crore over FY2005-08 vs net worth Rs 4,500 crore (Mar 2004) and market cap Rs 14,100 crore, debt-funded | Not specified | 167 |
| Overseas M&A as % of standalone operating cash flow | Godrej Consumer 112 per cent (FY11-18), Marico 46, Dabur 41, Pidilite 35 | Pidilite: 26 per cent over nine years in another passage | 162, 169 |
| Domestic bolt-ons, Pidilite | 11 per cent of operating cash flow, no debt; later adjacency about 7 per cent | Not specified | 169-170 |
| Standalone vs overseas RoCE | standalone RoCE often above 50 per cent; overseas below cost of capital | Not specified | 161-163 |
| Conglomerate vs focused 10-year RoCE | 11.0-15.1 per cent vs 18.3-44.6 per cent | Not specified | 164-165 |
| Kotak ING Vysya deal | share swap, dilution limited to 15 per cent | Not specified | 171 |

**Key quotes**
- "Growth outside core products and markets must be evaluated in the" [p. 177]
- "the quantum of capital the management is allocating towards it" [p. 159]
- "What is the quantum of capital being allocated towards the growth strategy? How much is it as a" [p. 220]
- "Does the growth strategy lead to a substantial increase in financial leverage?" [p. 220]
- "Is the company generating positive operating cash flow and free cash flow on a consistent basis?" [p. 220]
- "It is evident from the Ansoff Matrix that the riskiest strategy is ‘new products in" [p. 164]

**Pseudocode**
```
# Data: acquisition cash outflow, net worth, operating cash flow, debt change, goodwill, segment info
for each year:
    acq_ratio_nw = acquisition_spend / net_worth
    acq_ratio_ocf = acquisition_spend / CFO
    levered = (debt_increase / acquisition_spend) > 0.5            # threshold not in book
    flag = acq_ratio_nw > A or acq_ratio_ocf > B or levered        # A, B not in book
```

**Ambiguities & assumptions**
- No thresholds stated. ASSUMPTION: do not treat as a filter in the first backtest; use as a robustness overlay with a grid of cut-offs.
- Most of this is qualitative (Ansoff classification, adjacency judgement).

### 2.9 Fixed-date, price-blind annual investing (timing is redundant)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Systematic accumulation (dollar-cost-averaging variant); comparison of timed vs untimed entry | 181-191 |
| Timeframe & holding period | One purchase a year on a chosen date (1 January in the tests) for 5, 10 or 20 years; hold at least ten years | 182, 184-186 |
| Universe / eligibility filters | Pre-selected Consistent Compounders (Nestle India, Pidilite, Asian Paints, Abbott India, HDFC Bank); Sensex as benchmark | 187, 191 |
| Market / regime filter | None; "timing the overall market is not worth the effort" | 182 |
| Setup conditions | Equal rupee amount (Rs 10,000 per stock per year in the tests) | 184, 191 |
| Entry trigger & order type | Buy on first trading day of the year regardless of price | 184 |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | None; tests end 31 Dec 2020 | 185 |
| Position sizing | Equal amount each year per stock | 191 |
| Adding to / pyramiding | Annual additions are the design | 185 |
| Portfolio limits | five stocks in the combined test | 191 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Annual amount per stock | Rs 10,000 | Not specified | 184, 191 |
| Purchase date | 1 January (untimed); annual low (Mr Gifted); 52-week high (Mr Unlucky; five-stock test) | Not specified | 184, 190-191 |
| Horizons | 5, 10, 20, 30 years | Sensex 10-30 years | 182, 186 |

**Reported results**

| Test | Result | Page |
|---|---|---|
| Sensex, buy at 52-week low vs 1 January each year, 30 years to 2020 | 12.8 per cent vs 12.1 per cent (0.7 pp) | 181-182 |
| Sensex 20 years (2000-20) | 14.8 vs 13.2 per cent (1.6 pp) | 182 |
| Sensex 10 years (2010-20) | 13.7 vs 11.7 per cent (2.0 pp) | 182 |
| Nestle India 2011-20 (Rs 10,000 a year): perfect timing vs 1 January | 21.8 per cent vs 19.9 per cent | 185 |
| Nestle India 2001-20 | 22.1 vs 21.2 per cent | 186 |
| Nestle India, buying every year at the 52-week high ("Mr Unlucky") | 18.6 per cent | 190 |
| Pidilite, Asian Paints, Abbott, HDFC Bank, perfect-timing edge | 0.7 to 1.8 pp | 187 |
| Non-compounders: edge more than twice as large | Exhibit 72 | 188 |
| Five compounders bought every year at 52-week high, 2001-20 (equal amount each) | IRR 27.4 per cent vs Sensex 12.6 per cent | 191 |

**Key quotes**
- "timing the market does not make a material difference to" [p. 182]
- "invested an equal sum each year on the exact date when the Sensex was at its fifty-two-week" [p. 181]
- "implying compounding at a rate of 21.8 per cent over the ten-year period." [p. 185]
- "A healthy 18.6 per cent!" [p. 190]
- "amount of money in each of these five stocks every year" [p. 191]
- "your portfolio would have earned a healthy IRR of 27.4 per cent" [p. 191]

**Pseudocode**
```
# Data: daily close, split/bonus adjusted; list of pre-chosen stocks
for year in range(start, end):
    for s in stock_list:
        buy(s, amount=10000, date=first_trading_day(year))        # untimed arm
        buy(s, amount=10000, date=day_of_min_close(s, year))      # "Mr Gifted" arm
        buy(s, amount=10000, date=day_of_max_close_52w(s, year))  # "Mr Unlucky" arm
compute XIRR at end date for each arm; compare
```

**Ambiguities & assumptions**
- The stock list is hindsight-selected (known compounders as of 2001); an honest test must select stocks point-in-time. ASSUMPTION: apply the same untimed rule to point-in-time screens from 2.1.
- Dividends are excluded in the Nestle tests (portfolio values are price-only) [p. 185]; the Sensex tests mix TSR in other places. ASSUMPTION: price-only returns.
- "52-week high" for Mr Unlucky and the five-stock test: exact day definition not given. ASSUMPTION: highest close in the trailing 52 weeks on the purchase year's calendar.

### 2.10 Valuation rule: do not use P/E for timing; use long-horizon DCF

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Valuation / anti-valuation rule | 191-195 |
| Timeframe & holding period | Valuation over the full period of competitive advantage (25 years in the Asian Paints example) | 193 |
| Universe / eligibility filters | Consistent Compounders; for Type A and B stocks the authors say value investing (low P/E) still works | 39-40 |
| Market / regime filter | Starting valuations "have very little impact" on long-run returns in India (for compounders) | 39 |
| Setup conditions | Discount free cash flow to equity at cost of capital, forecast period long enough for the franchise; compare to market price | 191-194 |
| Entry trigger & order type | No P/E-based buy or sell trigger: "futile exercise" | 195 |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | Not specified | Not specified |
| Position sizing | Not specified | Not specified |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | Not specified | Not specified |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Terminal growth rate | 5 per cent is what most Indian practitioners use | Not specified | 193 |
| Cost of capital (Asian Paints, 1996) | 15 per cent | Not specified | 193 |
| Explicit forecast length | 10 years (conventional) vs 25 years (author) | 5, 7 or 10 years usual | 192-193 |
| Asian Paints worked example | FCFE CAGR 20.9 per cent FY1997-06; DCF value Rs 535 crore vs market cap Rs 1,374 crore; 25-year DCF Rs 2,001 crore; later FCFE CAGR 25.7 per cent FY2007-21 | | 193 |
| Asian Paints P/E in March 1996 | about 26x vs Sensex about 13x; intrinsic implied about 38x | | 194 |
| IRR if bought at 38x P/E in 1996 | 16.3 per cent (10 yrs), 21.1 (15), 22.8 (20), 23 (about 25) | | 194 |

**Key quotes**
- "Most practitioners in India typically use a 5 per cent terminal growth rate" [p. 193]
- "from Rs 535 crore to Rs 2,001 crore" [p. 193]
- "time your buys and sells based on just the PE of a stock is a futile exercise" [p. 195]
- "starting-period valuations have very little impact on long-medium-run investment returns in" [p. 39]
- "Asian Paints achieved a 25.7 per cent CAGR in FCFE" [p. 193]

**Pseudocode**
```
# Data: FCFE history, cost of capital r, growth g
value = sum(FCFE_t / (1+r)^t for t in 1..N) + TV/(1+r)^N,  TV = FCFE_N*(1+g)/(r-g)
# Book's claim: N=10 undervalues compounders; N~25 needed. No decision threshold given.
# For testing: signal-free; only use to check whether P/E percentile predicts forward return (book says it does not).
```

**Ambiguities & assumptions**
- The book states no buy/sell threshold relative to DCF value. ASSUMPTION: test P/E quintile at entry vs forward 5-10-year return as a null check of the author's claim, using forward-only fundamental snapshots.
- The book also says P/E matters for Type A/B stocks [p. 39-40] without a rule. ASSUMPTION: not tested.

### 2.11 Portfolio structure: rainy-day bucket plus equity bucket (CCP and Little Champs)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Asset allocation / portfolio construction | 201-209 |
| Timeframe & holding period | Ten years (Devika), fifteen years (Rajveer) | 201, 206-207 |
| Universe / eligibility filters | Equity bucket held in a portfolio screened for clean accounts, prudent capital allocation with strong free cash flow, and entry barriers; small caps held to about fifteen such stocks | 208-210 |
| Market / regime filter | None | Not specified |
| Setup conditions | First allocate near-term and emergency money to capital-preservation instruments (tax-free government bonds, about 6 per cent); the remainder goes to the equity portfolio | 201, 209 |
| Entry trigger & order type | Not specified | Not specified |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | Not specified | Not specified |
| Exits: trailing / time / signal | Not specified | Not specified |
| Position sizing | Examples: Rs 4 crore of Rs 9 crore to bonds, Rs 5 crore to equity; 60 per cent equity / 40 per cent tax-free bonds blend gave 13 per cent post-tax over ten years | 201, 206 |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | Little Champs small-cap portfolio of about fifteen stocks; cap bands: large above Rs 15,000 crore, mid Rs 3,000-15,000 crore, small below Rs 3,000 crore; baskets equal-weighted and rebalanced each July-end | 208, 252 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Rainy-day bucket sizing | by need; Rs 4 crore of Rs 9 crore in the example | Not specified | 201 |
| Equity target (CCP) | high-teens returns; volatility typically less than half that of Nifty50 | Not specified | 202 |
| Small-cap target | about 20 per cent earnings growth | Not specified | 209 |
| Cap-band rebalance | annually at July-end (research baskets) | Not specified | 252 |

**Reported results**

| Result | Value | Page |
|---|---|---|
| CCP stocks positive in 80 per cent of past 32 years vs 66 per cent for Sensex | histograms | 202-204 |
| 3-year rolling returns | negative only once in twenty years (period starting 2006) | 206 |
| 60/40 CCP + tax-free bonds, past decade | 13 per cent a year post-tax | 206 |
| Small caps | best deliver large outperformance, weakest lose wealth in under a year (Exhibit 82) | 208 |

**Key quotes**
- "An investor’s first allocation of her savings should relate to the quantum" [p. 209]
- "portfolio of fifteen such stocks" [p. 208]
- "typically, less than half that of the Nifty50 basis back-testing" [p. 202]
- "We classify companies with market cap of > Rs 15,000 crore as large cap," [p. 252]
- "invested 60 per cent of her corpus in the CCP ten years ago and the rest in tax-free" [p. 206]

**Pseudocode**
```
# Data: investor liabilities (not market data)
bond_bucket = near_term_needs ; equity_bucket = wealth - bond_bucket
equity_bucket -> screened portfolio (see 2.1-2.8), N between 10 and 25 (15 for small caps)
bucket by mcap: large > 15000cr; mid 3000-15000cr; small < 3000cr ; rebalance each July-end
```

**Ambiguities & assumptions**
- No formula for sizing the safe bucket. ASSUMPTION: fixed 20-40 per cent in cash/liquid ETF for backtest comparisons; not a book number.
- Cap bands are in 2021 rupees. ASSUMPTION: rescale by market-cap percentile (top 100, 101-250, below) for earlier years.
- The "CCP" itself is a proprietary portfolio; the book does not list its rules.

### 2.12 Low-beta / low-volatility tilt (author's empirical finding that CAPM fails in India)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Risk-factor observation (price-based), not a prescribed trade | 34-35 |
| Timeframe & holding period | 3, 5, 10 and 20 years ending March 2020 | 34-35 |
| Universe / eligibility filters | Nifty50 constituents as they stood 20, 10, 5 and 3 years earlier | 34 |
| Market / regime filter | None | Not specified |
| Setup conditions | Beta = covariance of stock with Nifty50 divided by variance of Nifty50, monthly returns, ten years (SBI example March 2010 to March 2020); volatility = standard deviation of monthly returns divided by CAGR | 34-35 |
| Entry trigger & order type | The author's conclusion is to prefer low-risk, low-beta, low-volatility stocks | 35 |
| Initial stop-loss | None | Not specified |
| Exits: profit-taking | None | Not specified |
| Exits: trailing / time / signal | Not specified | Not specified |
| Position sizing | Not specified | Not specified |
| Adding to / pyramiding | Not specified | Not specified |
| Portfolio limits | Not specified | Not specified |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Beta window | ten years of monthly returns | Not specified | 34 |
| Benchmark | Nifty50 | Not specified | 34 |
| Volatility measure | stdev of monthly returns / CAGR | Not specified | 35 |

**Reported results**

| Result | Value | Page |
|---|---|---|
| Top ten Nifty50 return generators over 20/10/5/3 years | average beta 0.8-0.9 | 34 |
| Correlation of beta with returns inside those groups | +0.22 (20-year cohort), -0.45 and -0.47 (3- and 5-year cohorts) | 34 |
| Ten highest-beta Nifty50 stocks at 31 March 2020 | average beta 1.4; underperformed the index over 3, 5, 10, 20 years; within-group correlation -0.35 and -0.39 | 34-35 |
| Volatility vs return | "strong negative correlation" | 35 |

**Key quotes**
- "the average beta of these stocks is between 0.8 and 0.9" [p. 34]
- "there seems to be strong evidence that lower beta leads to higher returns" [p. 35]
- "as measured by the standard deviation of monthly returns divided by the compounded annual returns" [p. 35]
- "monthly returns of SBI and Nifty50 for a period of ten years" [p. 34]

**Pseudocode**
```
# Data: daily close -> month-end returns; Nifty proxy (NIFTYBEES or equal-weight index)
for rebalance_date t:
    for s in liquid_universe:
        beta[s] = cov(r_s, r_mkt) / var(r_mkt)   # 120 months
        vol[s]  = stdev(r_s monthly) / CAGR_s
    long lowest-quintile beta (or vol) ; hold 1-5 years ; compare vs highest quintile
```

**Ambiguities & assumptions**
- The book offers this as a diagnosis of CAPM, not a trading rule, and shows only cohorts of large caps. ASSUMPTION: test a long-only low-beta/low-vol quintile as a derived hypothesis, clearly labelled as not the author's explicit strategy.
- Volatility divided by CAGR is undefined when CAGR is non-positive. ASSUMPTION: exclude those names.

## 3. Risk & money-management rules

The book has no position-level risk rules (no stop-losses, risk per trade or drawdown limits). Risk is managed by selection and by holding period:
- "Crush risk" in four ways: accounting risk (reject D6-D10 on the forensic model, p. 36, 56), revenue risk (prefer essential products, p. 36), profit risk (sectors where one or two companies hold about 80 per cent of the profit pool, p. 37), liquidity risk (tilt towards liquid stocks; average daily volume falls to about Rs 10 crore a day in the lower BSE100, p. 37).
- Hold for at least ten years; timing does not matter much with a long horizon (p. 182). Probability of positive return above 95 per cent if held three years or more in the coffee can back-test (p. 241).
- Do not "bottom fish" in companies with exposed accounting fraud; retail shareholding in Yes Bank and DHFL more than doubled after fraud became public and holders were diluted or wiped out (p. 107-108).
- Frauds leave little time to exit (Satyam fell about 78 per cent in a day, p. 47, 50; Yes Bank and DHFL fell 40 per cent within a month, p. 107), so avoid ex ante.
- Equal weight across 10-25 names (p. 235, 242); about fifteen for small caps (p. 208).
- Keep near-term and emergency money out of equities (p. 209).
- Account for friction: short-term capital gains tax 15 per cent and brokerage plus price impact of about 0.5 per cent even for Nifty50 stocks for institutions (p. 35).
- Beta is not a risk measure to optimise; lower beta and lower volatility went with higher returns (p. 35).
- Do not hold when management starts large leveraged or unrelated expansion; check quantum of capital relative to net worth (p. 167, 220).

## 4. Non-codable guidance

- Level 3 primary-data checks: speak to former employees, customers, suppliers, competitors; visit branches and factories (p. 62).
- "Lethargy Tests" for held compounders: competition, disruptions, evolution and capital misallocation, using annual reports plus channel and vendor checks (p. 148-151).
- IBAS competitive-advantage judgement: innovation, brand, architecture, strategic assets (p. 125-133, 222-233); brand proxies listed as warranty length, years in market, marketing spend relative to revenue, price premium (p. 224).
- Pricing-power test: if a rival offers Rs 70 against the incumbent's Rs 100, does the incumbent keep price and share? (p. 135). Market share alone is not pricing power (Indigo, Bharti Airtel, HUL and Colgate examples, p. 135-137).
- Succession planning framework: decentralisation, CXO tenure and quality, board independence, track record (p. 175-176).
- Behaviour: Test cricket analogy, patience, leaving good deliveries alone, visualisation and routine, growth mindset, self-review of mistakes (p. 12-19, 211-216); resist intervening in the portfolio (p. 235).
- The four myths (gold, real estate, debt funds, GDP growth drives equities) and that GDP growth does not predict returns (p. 25-32).
- Investor advice: if you cannot do forensic work, use a professional manager (p. 102, 103).
- Rajveer-type warning: small-cap quality needs deep diligence; the weakest small caps destroy wealth quickly (p. 207-208).

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - Prices: daily split/bonus-adjusted close, volume (for 2.9, 2.12, liquidity).
  - Fundamentals (annual, ten-year history for 2.1-2.2): net sales, EBIT (including other income), capital employed (debt plus equity), net profit, equity, loans/advances (banks), CFO, CFI, capex, EBITDA, depreciation, gross block, CWIP, cash and equivalents, interest income, contingent liabilities, net worth, reserves, dividends, auditor remuneration, goodwill, promoter pledge and holding, related-party sales.
  - Index: NIFTYBEES or equal-weight index from our panel; Nifty history only from 2024.
- **Testability with our data:**
  - Backtestable on 2005-2026 prices: 2.9 (fixed-date annual investing arms, if the stock list is point-in-time), 2.12 (beta/volatility), and the market-timing comparison in 2.9. These ignore dividends (our OHLCV has no dividend field) so total return is understated.
  - Forward-test only: 2.1-2.8 and 2.10, 2.11, because fundamentals are point-in-time only from Feb 2026 and 3-year growth fields only from May 2026. The book's own tests need ten years of history and cannot be recreated.
  - Needs data we do not have: ten years of sales/RoCE per company, shares outstanding (market cap), CFO/CFI statements, promoter pledge, related-party notes, auditor remuneration, NPA series. Level 3 and Lethargy Tests are not data.
- **Market-structure differences:**
  - Book is already built for Indian stocks (BSE500, Ace Equity), long-only, so no shorting issue. ASSUMPTION: implement all as long-only, delivery-based.
  - Costs: delivery STT, brokerage, about 0.1 per cent slippage; annual or no rebalancing keeps cost drag small. Dividends and 15 per cent short-term (and long-term) capital gains tax are not modelled. ASSUMPTION: report pre-tax.
  - Liquidity and circuits: small-cap quality names can hit circuits and are thin; the book itself warns about liquidity (p. 37). ASSUMPTION: require a minimum 3-month median daily traded value (for example Rs 1 crore) in our panel, instead of the book's Rs 100 crore market cap.
  - Market cap needs shares outstanding. ASSUMPTION: use the Feb 2026 snapshot's market cap where available; otherwise use traded-value rank as a proxy.
  - Delisted names: our panel includes them, which is what the forensic screens are meant to catch. Use delisting price as final value.
  - Entry date: Indian FY ends 31 March and results land by end-May; the book starts 30 June [p. 255]. ASSUMPTION: first trading day of July, using only data published by then (avoid look-ahead).
  - Sector split: banks and NBFCs use 2.2 and 2.4, not 2.1 and 2.3.

## 6. Verdict

- **Codeability:** Partly. The Coffee Can screen (2.1-2.2) is fully specified but needs ten-year company fundamentals; the forensic models are only half-specified (eight of twelve and six or seven of eleven ratios named, no aggregation rule); the rest is qualitative.
- **Priority for backtesting:** Medium. The Coffee Can screen is the single most testable and best-evidenced rule, but with our data it can only be forward-tested from 2026, so a long history is not obtainable; price-only parts (2.9, 2.12) are testable but are not the book's core edge.
- **Top 3 things a coder is most likely to get wrong:**
  1. The sales-growth filter is "at least 10 per cent in every one of ten years", not a ten-year CAGR; likewise RoCE at least 15 per cent each year (p. 254, 242). Using averages gives a much larger, weaker universe.
  2. Look-ahead and survivorship in fundamentals: using restated or later-published annual numbers, or testing on today's known compounders (the Nestle, Pidilite, Asian Paints, HDFC Bank, Abbott examples are hindsight picks, p. 191).
  3. Mixing financial and non-financial rules: banks and NBFCs use RoE and loan growth and a different forensic model with a different decile cut (top 3 vs top 5 deciles), and EBIT should include other income while capital employed means debt plus equity.
