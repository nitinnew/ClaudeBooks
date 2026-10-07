# QGLP — Motilal Oswal 25th Annual Wealth Creation Study (2020), "The QGLP Checklist: 25 questions, 25 frameworks", plus the QGLP Booklet — Raamdeo Agrawal / Motilal Oswal

- **Source file:** Google Drive: invest/qglp motilal 2020.pdf (pages 1-118) + invest/QGLP-Booklet.pdf (pages 119-130). The two PDFs are concatenated in one text file with continuous page numbering: `[[PAGE 1]]`-`[[PAGE 118]]` is the 25th Annual Wealth Creation Study (Dec 2020, authors Raamdeo Agrawal and Shrinath Mithanthaya); `[[PAGE 119]]`-`[[PAGE 130]]` (from line 22262) is the separate QGLP Booklet (a Motilal Oswal AMC brochure).
- **Text file used:** text/motilal_qglp.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. The report's own printed page numbers (running headers, table of contents p. 1-113) are offset by about 2 from the PDF index and are NOT used here.
  - Before finishing, `python ../work/bin/verify_citations.py specs/motilal_qglp.md text/motilal_qglp.txt` was run; see the end of the task report for the result.
- **Coverage:** Read lines 1-22449 (the whole file) in sequential chunks; last marker reached `[[PAGE 130]]`. Pages with no extractable text: 35 (image-only; this is the page that holds "Framework #2", the DFCF-to-equity value model, so that content is missing), 118, 120, 129, 130 (empty). Pages with only a divider, title or "NOTES": 4, 30, 116, 119. Page 117 is regulatory disclosures only; page 128 is a legal disclaimer. Pages 20-29 (Appendices 1-5, 1995-2020 rankings) and pages 103-107 (Appendices 1-3, 2015-20 rankings) are pure data tables; they were read, but they contain no screens or rules and are not turned into strategies. The booklet text (p. 121-127) has lost its spaces and the big Q/G/L/P letters; it is still legible. No chapter containing trading/investing rules was skipped. Reading done by a Sonnet sub-agent. The coordinator re-ran the verifier and an exact-page check, spot-checked 10 unquoted table citations, and read pages 112-130 itself (the agent's notes log stopped at line 21700), adding the booklet's qualitative QGLP criteria (pp. 122-126) to section 4.

## 1. The method in brief

This is a discretionary, bottom-up, long-only stock-picking philosophy, not a mechanical system. Motilal Oswal's "QGLP" stands for Quality (of business and of management), Growth (in earnings), Longevity (of both quality and growth) and reasonable Price [p. 37]. "QGL" is the value component, which is then compared with "P" to see whether there is an adequate value-price gap [p. 37]. The 2020 theme study turns this into a checklist of 25 questions (Business Q1-8, Growth Q9-10, Management Q11-19, Price Q20-24, Risk Q25) [p. 40], each paired with a named framework (Lindy effect, Great/Good/Gruesome, Emergence and Endurance, Terms of Trade, DuPont, Porter's Five Forces, CAP and GAP, 100x, Mid-to-Mega, PEG, Payback and others). The firm says the checklist "is by no means gospel" and is a work in progress [p. 31]. It is aimed at holding "healthy compounders over the medium-to-long term" [p. 36]; there is no short-term trading component.

The claimed edge is that long-run stock returns follow earnings power and growth: "Stock returns are slaves of earnings power and growth. In the very long run, valuations matter less" [p. 1]. Evidence offered is historical and ex post: (a) of the top 500 listed companies in 1995 only 100 beat the Sensex (9.2% CAGR) over 25 years [p. 5]; (b) equal-weight INR 1 mn in the top 25 fastest wealth creators of 1995-2020 grew to INR 162 mn (23% CAGR) [p. 6]; (c) 63 of the 100 wealth creators are consumer-facing [p. 9]; (d) midcaps (market-cap rank 101-250) are the hunting ground for the next large caps, about 15 crossing over to the top 100 every year [p. 72]; (e) for 2015-20 the "Wealthex" index of top-100 wealth creators returned 12% CAGR vs 1% for the Sensex [p. 94]; (f) valuation screens (PEG < 1, Payback < 1) historically gave the best alpha [p. 83, p. 100]. All of these are computed on the winners with hindsight (perfect foresight of the next 5 years' profits), so they are descriptive, not out-of-sample tests. The study was written for Indian equities (BSE Sensex benchmark, Capitaline data).

## 2. Strategies

The book describes one philosophy with many separable screens and frameworks. Each distinct, separately testable piece that has quantified rules is listed below as its own strategy. Purely qualitative frameworks (moat, integrity, culture, succession) are folded into the checklist strategy (2.1) as "judgement overlays" and are listed in Section 4.

### 2.1 QGLP 25-question checklist (composite stock-selection process)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality-growth at reasonable price; fundamental, long-only, bottom-up stock picking | 31, 32, 37 |
| Timeframe & holding period | "healthy compounders over the medium-to-long term"; longer holding gives a higher compounding exponent; stock prices "often reflect 10-20 years of value-creating cash flows" | 36, 125 |
| Universe / eligibility filters | Listed Indian equities. Idea sources (screeners, brokers, media) only generate ideas; every idea must pass the checklist. Business must be understandable (Q2): if you cannot describe how it makes money, abandon it. Stock must be reasonably liquid (Q24): free-float market cap and average daily trading volume. Avoid "Gruesome" companies (very high capital intensity, low/falling RoE, no moat) however cheap | 38, 42, 45, 84 |
| Market / regime filter | None for entry. Macro/market view is deliberately not used (bottom-up). Book does give context: valuation vs long-period averages (Sensex P/E 18x average; market cap/GDP 60% average), but states no rule | 32, 17, 18 |
| Setup conditions | Q3 Profitability: RoE consistently > 13% (13% is the book's "threshold Cost of Equity"); "Emergence" = RoE > 13% for the first time or after a long break. Q4: low Debtors/Creditors (favourable terms of trade); operating cash flow positive and not significantly below PAT; no sustained negative FCF. Q6 DuPont: monitor PAT margin, asset turnover and leverage trends. Q7: sector structure score from Porter's Five Forces: score >= 3 attractive, <= 2.5 needs a sharp strategy; prefer non-over-regulated. Q9-10: large addressable market, credible growth plan, healthy EPS growth for next 3 years at least. Q11: no sharp practices, preferably full tax-paying, healthy dividend payout. Q18: significant promoter holding. Q19: very high promoter pledge is a red flag. Q20-21: financial model with 3-year estimates; "QGL" confirmed. Q22-23: reasonable valuation and margin of safety | 43, 47, 51, 55, 63, 74, 81, 82, 83 |
| Entry trigger & order type | No technical trigger or order type. Buy when QGL is confirmed and price is below assessed value with adequate margin of safety ("buying them only if there is adequate Margin of Safety"). Valuation tools: peer and own-history P/E, intrinsic P/E = Payout / (k-g), PEG (2.6) and Payback (2.6) | 33, 82, 83 |
| Initial stop-loss | Not found in this book. The only protection is margin of safety and avoiding gruesome/low-integrity companies | 33, 45 |
| Exits: profit-taking | Not found in this book (no sell rule or price target). Commodity/cyclical stocks: "sell too soon" in the squeeze phase | 110 |
| Exits: trailing / time / signal | Not stated. By implication, re-run the risk checklist (Q25) and exit if the thesis breaks: moat breached by disruptive competition, drastic regulatory change or capital misallocation; key-man or succession problem | 58, 84, 86, 87 |
| Position sizing | Not specified for the checklist. Separately, Study 21 says "Opportunities for big bets come seldom" and prescribes focused investing (asymmetric payoff, create edge, bet big) with no numeric weights | 114 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book. Study 21: clear portfolio goal, superior selection, rational allocation, active monitoring | 114 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| RoE hurdle ("threshold Cost of Equity") | 13% | 15% quoted in Study 18 summary ("cost of equity is 15%") | 43, 113 |
| Five Forces sector score, attractive | >= 3 | <= 2.5 needs sharp strategy; table range 1.0 to 5.0 | 55, 56 |
| PEG | <= 1.5 "near-certain" superior returns | < 1x best (alpha 19%); > 3x worst (-10%) | 83 |
| Payback ratio (mkt cap / next-5y PAT) | < 1x | > 3x worst (-12%) | 83 |
| Estimates horizon | at least 3 years | PEG uses 2/3/5 years | 82, 83 |
| Financial leverage (DuPont screen) | assets/equity < 2 (debt/equity not > 1) | | 51 |
| Max promoter pledge | "very high ... caution" (no number) | | 81 |
| Promoter holding | "significant ... depending on circumstances"; banks capped at 26% by regulation | | 81 |

**Key quotes**
- "Our threshold Cost of Equity is 13%." [p. 43]
- "Avoid investing in gruesome companies no matter how cheap they appear." [p. 45]
- "Sectors with score of 3 or higher are attractive" [p. 55]
- "Buying them only if there is adequate Margin of Safety" [p. 33]
- "No sustained negative Free Cash Flow i.e. the company is not a capital guzzler." [p. 47]
- "a very high level of pledge should be viewed with caution" [p. 81]
- "Average daily trading volume in the stock to ascertain liquidity." [p. 84]
- "The checklist shared here is by no means gospel." [p. 31]

**Pseudocode** (quantitative subset only; qualitative gates are manual flags)
```
# Data: roe_fy[1..5], ocf, pat, fcf, debtors, creditors, de_ratio, pledge_pct, promoter_pct,
#       sector_five_forces_score (table p.56), eps_est or trailing pat_cagr, pe_ttm, mcap, close, volume
for stock in universe:
    if not liquid(stock): continue                              # Q24
    if min(roe_fy[-5:]) <= 0.13: continue                       # Q3 (ASSUMPTION: 5 yrs, 13%)
    if ocf[-1] <= 0 or ocf_5y_sum < 0.7*pat_5y_sum: continue    # Q4 (ASSUMPTION 0.7)
    if count_consecutive(fcf < 0) >= 3: continue                # Q4 (ASSUMPTION 3)
    if de_ratio > 1: continue                                   # p.51
    if sector_score[stock.sector] < 3: continue                 # Q7
    if pledge_pct > PLEDGE_MAX: continue                        # Q19 (ASSUMPTION 25%)
    if peg(stock) > 1.5 or payback(stock) >= 1: continue        # Q22 (see 2.6)
    candidates.append(stock)
rank candidates by peg ascending; hold equal weight; manual overlay for Q1,2,8,11-17,25
```

**Ambiguities & assumptions**
- The cost-of-equity hurdle is 13% on p. 43 but 15% in the Study 18 summary on p. 113 (and the 25-for-25 screen uses 15% average RoE, p. 19). ASSUMPTION: use 13% for "profitable" (Q3, the checklist's own number) and 15% as a tighter sensitivity run.
- "Consistently", "not significantly lower than PAT", "sustained negative FCF", "very high pledge" and "significant promoter holding" have no numbers. ASSUMPTION: 5-year window; OCF >= 0.7 x PAT; FCF negative in 3 consecutive years excluded; pledge > 25% excluded.
- Q8-Q17 and Q25 (moat, management integrity, competence, culture, succession, risks) are judgement questions; not found in this book as numeric tests. ASSUMPTION: treated as not codable; the backtest uses only the quantitative subset.
- No exit, stop or sizing rule is given. ASSUMPTION: annual rebalance; exit when a stock fails any codable gate for two consecutive annual checks; equal weight.

### 2.2 "25-for-25" shortlist funnel
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality-growth stock-selection funnel (midcap, consumer-facing) | 18, 19 |
| Timeframe & holding period | Shortlist of stocks "likely to deliver handsome returns over the next 25 years" | 18 |
| Universe / eligibility filters | Start with 150 midcaps, i.e. companies ranked 101 to 250 by current market cap. Prefer consumer-facing companies with secular business models: eliminate Auto ancillaries, Capital Goods, Chemicals, Oil & Gas and Realty (150 to 114 companies) | 18 |
| Market / regime filter | None | - |
| Setup conditions | (3) last 5-year average RoE > 15% (114 to 63); (4) judged business potential and management potential, both must qualify (63 to 28); (5) market leaders from these 28 (13 remain); (6) add 5 beneficiaries of Value Migration regardless of leadership (total 18); (7) add 6 large-cap financial leaders ("size begets size") (24); (8) add one pure digital play even if it fails some filters (25) | 19 |
| Entry trigger & order type | Not a trading rule; a watch-list. Valuation is explicitly ignored: "So we ignored the same in the shortlisting process" | 19 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book (25 names listed, no weights) | 19 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | 25 stocks | 19 |

The step-1 observations behind the funnel (top 25 wealth creators of 1995-2020): almost all were small-to-mid in 1995, consumer-facing, very profitable (average base RoE 17%), market leaders (top 3), and had high-integrity management [p. 18].

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Market-cap rank band | 101 to 250 | | 18 |
| Sectors excluded | Auto ancillaries, Capital Goods, Chemicals, Oil & Gas, Realty | | 18 |
| 5-year average RoE | > 15% | 17% average base RoE observed for past winners | 18, 19 |
| Funnel counts | 150, 114, 63, 28, 13, 18, 24, 25 | | 18, 19 |
| Market leadership | top 3 in sector (from step 1 and Mid-to-Mega) | | 18, 73 |
| Valuation | ignored | | 19 |

**Key quotes**
- "We started with a list of 150 midcaps i.e. companies ranked 101 to 250 by current market cap." [p. 18]
- "we chose companies with last 5-year average RoE greater than 15%" [p. 19]
- "So we eliminated cyclical businesses like Auto ancillaries, Capital Goods, Chemicals, Oil & Gas and Realty." [p. 18]
- "We believe in the very long run, valuations matter less." [p. 19]

**Pseudocode**
```
# Data: mcap_rank (point-in-time), sector, roe_fy[1..5], leader_flag (manual), value_migration_flag (manual)
S = [s for s in universe if 101 <= mcap_rank(s) <= 250]
S = [s for s in S if s.sector not in {AutoAncillary, CapitalGoods, Chemicals, OilGas, Realty}]
S = [s for s in S if mean(roe_fy[-5:]) > 0.15]
# steps 4-8 are judgement: business/mgmt potential, leadership, value migration, financial large caps, digital play
portfolio = quantitative S (after step 3); equal weight; rebalance annually
```

**Ambiguities & assumptions**
- Steps 4-8 (potential, leadership, value migration, financials, digital) are judgement; the book does not give tests. ASSUMPTION: backtest only steps 1-3; proxy "leadership" as top-3 by sales in sector when fundamentals exist.
- "Current market cap" ranking uses a market-cap series we do not have historically. ASSUMPTION: proxy rank by average daily traded value rank or by price x latest shares from the 2026 snapshot (forward test only).
- No holding or exit rule: ASSUMPTION: annual re-screen, equal weight.

### 2.3 Mid-to-Mega (MQGLP with leadership)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Growth-quality, rank-migration (mid-cap leaders) | 72, 73 |
| Timeframe & holding period | Rolling 5-year windows; "over the next five years, about 15 of these stocks will cross over to the Mega category" | 99 |
| Universe / eligibility filters | Mega = market-cap rank 1-100; Mid = 101-250; Mini = below 250. Hunting ground is the Mid category (150 stocks). Must be market leader, ranked among the top 3 in their sector | 72, 73, 99 |
| Market / regime filter | None | - |
| Setup conditions | "MQGLP with leadership inside": Midsize + Quality + Growth + Longevity + Price | 73 |
| Entry trigger & order type | Buy Mid-rank leaders that pass QGLP; no order type. Book lists current Mid stocks showing leadership as an example list | 73 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Natural exit implied by migration to Mega rank, but no explicit rule | 72 |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

Author's results: every year about 15 stocks cross from Mid to Mega, a "strike rate of 10%" [p. 72]. 1995-2020: 10 Mids became Mega with 21% average return CAGR vs 9.2% for the Sensex; of 100 Mega companies in 1995 only 32 stayed Mega, 45 fell to Mini with -3% CAGR [p. 14]. 2015-20: 14 Mids became Mega with 20-22% average CAGR vs about 1% for the Sensex; 72 stayed Mid (0% CAGR) and 64 slipped to Mini (-25%) [p. 97, p. 98]. 23 Minis became Mid with 21% CAGR [p. 97].

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Mid band | market-cap rank 101-250 | "Next 150 stocks by market cap rank" | 14, 72 |
| Mega band | rank 1-100 | | 72 |
| Leadership | top 3 in sector | | 73 |
| Evaluation window | 5 years | 25 years in the 1995-2020 matrix | 14, 97 |
| Strike rate | 10% (15 of 150 per year) | | 72 |

**Key quotes**
- "Every year, about 15 stocks crossover from Mid to Mega, also implying a healthy strike rate of 10%." [p. 72]
- "Another key dimension of Mid to Mega is market leadership i.e. ranked among the top 3 in their respective sectors." [p. 73]
- "The most potent and focused hunting ground for high-performing stocks is the Mid category" [p. 99]

**Pseudocode**
```
each rebalance date t (annual, ASSUMPTION: end-March):
    rank all stocks by mcap_proxy at t
    mid = ranks 101..250
    leaders = [s in mid if sector_rank(s) <= 3]            # leadership by sales or mcap within sector
    pick = leaders that also pass 2.1 quality gates (RoE>13%, low leverage)   # fundamentals: forward test only
    hold equal-weight 5 years or until rank <= 100 (ASSUMPTION), re-evaluate annually
# Price-only variant (backtestable 2005-2026): mid-rank = rank by 60-day average traded value (proxy);
# test whether stocks in proxy ranks 101-250 migrate to <=100 and their forward 5y return vs NIFTYBEES
```

**Ambiguities & assumptions**
- The book gives no exit rule. ASSUMPTION: hold up to 5 years (the study window), exit early if the stock leaves the top 250 (rank > 250) at an annual check.
- "Quality, Growth, Longevity, Price" inside MQGLP are not numerically defined here. ASSUMPTION: reuse 2.1 gates and 2.6 valuation.
- Rank crossovers are computed ex post; picking the 15 future crossovers is not possible in real time, only the 150-stock pool.

### 2.4 SQGLP "100x" small-cap framework
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Growth-quality, small-cap multibagger | 72, 114 |
| Timeframe & holding period | 100-fold rise "may take longer than 3, 5, or even 10 years"; target 100x in about 20 years (26% CAGR) instead of the index's 30 years (17% CAGR) | 72, 114 |
| Universe / eligibility filters | S = small: "market cap ideally around US$1 billion or INR 75 billion" | 72 |
| Market / regime filter | None | - |
| Setup conditions | S + Quality + Growth + Longevity + Price (SQGLP); multibagger traits from Study 5: high-growth business with tailwind, huge opportunity, great business economics, outstanding management with unquestionable integrity, significant re-rating potential | 72, 109 |
| Entry trigger & order type | "purchased with a five-year payback outlook of <1" (Study 5) | 109 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Not found in this book. "Patience is the rarest" quality is cited | 72 |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Size | about US$1 bn / INR 75 bn market cap | | 72 |
| Payback ratio at purchase | < 1 (5-year) | | 109 |
| Target return | 100x in 20 years = 26% CAGR | benchmark index 100x in 30 years = 17% CAGR | 114 |

**Key quotes**
- "S stands for small i.e. market cap ideally around US$1 billion or INR 75 billion." [p. 72]
- "smart investors should target to achieve 100x in less time, say, 20 years (26% CAGR)" [p. 114]
- "purchased with a five-year payback outlook of <1, has a good chance of being a big winner" [p. 109]

**Pseudocode**
```
small = [s for s in universe if mcap(s) between ~0.5*INR75bn and ~2*INR75bn]    # ASSUMPTION band
q = [s in small if mean(roe_fy[-5:]) > 0.13 and de_ratio < 1]                     # 2.1 gates
g = [s in q if pat_cagr_3y >= 0.25]                                               # ASSUMPTION: path to 26% CAGR
p = [s in g if payback(s) < 1]                                                    # est. from realised or consensus PAT
hold equal weight, review annually
```

**Ambiguities & assumptions**
- "Ideally around" INR 75 billion is not a band. ASSUMPTION: INR 35-150 bn market cap.
- Growth threshold is not stated; the 26% CAGR target is for the stock price, not earnings. ASSUMPTION: 3-year PAT CAGR >= 25%.
- Payback < 1 needs 5-year forward profits; book's tests use realised profits (hindsight). ASSUMPTION: use consensus or a 3-year model extrapolated; flagged as non-point-in-time.

### 2.5 DuPont improving-fundamentals screener (Q6)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Fundamental momentum / quality screen (mechanical) | 51 |
| Timeframe & holding period | 5-year comparison (2015 vs 2020); returns measured over the same 5 years | 51 |
| Universe / eligibility filters | Top 500 companies (by market cap) in 2015 | 51 |
| Market / regime filter | None | - |
| Setup conditions | 2020 PAT margin > 2015 PAT margin; 2020 asset turnover > 2015 asset turnover; leverage (assets/net worth) < 2, i.e. debt-equity not > 1 | 51 |
| Entry trigger & order type | Screen result is the buy list (the book computed it ex post for 2015-20) | 51 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book (results are an equal-weight average) | 51 |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | 17 of 500 passed | 51 |

Author's result: only 17 of 500 passed; 15 of 17 outperformed; average return 15% vs 1% for the Sensex over 2015-20 [p. 51]. Note the screen was applied with 2020 data to returns of 2015-20, so it uses end-of-period fundamentals (look-ahead).

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| PAT margin change | 2020 > 2015 | | 51 |
| Asset turnover change | 2020 > 2015 | | 51 |
| Leverage (assets / net worth) | < 2 | debt-equity not > 1 | 51 |
| Universe | top 500 | | 51 |
| Window | 5 years | | 51 |

**Key quotes**
- "2020 PAT Margin > 2015 PAT Margin" [p. 51]
- "Leverage <2 i.e. Debt equity not > 1." [p. 51]
- "Only 17 out of 500 companies met the above criteria." [p. 51]
- "Rising margin and asset turn with healthy leverage is a sound formula for investing success" [p. 51]
- "Wealth creators tend to exhibit rising PAT margin, stable asset turnover and a falling gearing" [p. 108]

**Pseudocode**
```
# Data: pat, sales, total_assets, net_worth (annual), universe = top 500 by mcap at t0
at each t0 (annual): for s in universe:
    m0,m1 = pat/sales at t0, t0+N ; a0,a1 = sales/assets ; lev = assets/net_worth at t0
    # book version (look-ahead): compare t0 vs t0+5 and test forward return over same window.
    # tradable version: compare latest FY vs FY-3 (ASSUMPTION: 3y) and buy after results are published.
    if m1 > m0 and a1 > a0 and lev_latest < 2: buy
equal weight; rebalance annually; hold 1 year
```

**Ambiguities & assumptions**
- The book's test is non-tradable (uses the end-of-window fundamentals and the window's returns). ASSUMPTION: shift to a trailing comparison and enter only after the second year's results are public (lag 60 days after fiscal year-end).
- "Leverage" is defined both as assets/net worth < 2 and as "debt equity not > 1"; these are equivalent only if there are no non-debt liabilities. ASSUMPTION: use assets/net worth < 2.
- Window length for a live screen: not found in this book. ASSUMPTION: 3 years.

### 2.6 Valuation gate: PEG and Payback ("what works")
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value/valuation filter applied to quality-growth names | 83, 100 |
| Timeframe & holding period | 5-year forward earnings; evaluations over 5-year windows | 83, 100 |
| Universe / eligibility filters | Applied to stocks already passing QGL (checklist Q21 then Q22); the empirical tests are on top-100 wealth creators | 82, 100 |
| Market / regime filter | None | - |
| Setup conditions | PEG = trailing-12-month P/E / earnings CAGR for next 2/3/5 years; Payback = market cap / next 5 years' PAT. "Clearly, lower the PEG the better" | 83 |
| Entry trigger & order type | PEG <= 1.5 "near-certain formula for superior returns"; Payback < 1x likewise; stricter PEG < 1x is "solid formula for superior returns" | 83, 100 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

Pricing heuristic table (what works / what doesn't; alpha), from the 23rd study [p. 83]: PEG < 1x +19% / > 3x -10%; Payback < 1x +17% / > 3x -12%; Price/Book < 1x +6% (> 3x unclear); Price/Sales < 1x +6% / > 3x -6%; P/E < 10x +5% / > 50x -14%; P/E relative to market < 1x +4% / > 2x -8%. Booklet list of pricing tools: discount to historical P/E band, P/B discount, PEG, DCF, replacement-value discount, popular/unpopular idea, payback ratio, dividend yield [p. 126].

2015-20 results among the 100 wealth creators, with 5-year perfect-foresight earnings [p. 100, p. 101]: PEG < 1: 34 companies, price CAGR 20% (average of all 100 is 12%); PEG 1-2: 15 companies, 12%; PEG 2-3: 15 companies, 10%; PEG > 3: 30 companies, 12%. Payback < 1: 13 companies, 16%; 1-2: 26 companies, 19% (best this time, "for the first time ever" Payback < 1 was not the highest); > 3: 48 companies, 12%. P/E < 10: 5 companies, 16%; P/B < 1: 4 companies, 39%; P/S < 1: 20 companies, 18% [p. 101].

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| PEG cut-off | <= 1.5x (Framework #24); < 1x (empirical) | > 3x avoid | 83, 100 |
| Payback cut-off | < 1x | 1-2x best in 2015-20; > 3x avoid | 83, 100 |
| P/E cut-off | < 10x | > 50x avoid | 83, 101 |
| P/B cut-off | < 1x | | 83, 101 |
| P/S cut-off | < 1x | > 3x avoid | 83, 101 |
| Forward growth horizon | 2, 3 or 5 years | | 83 |

**Key quotes**
- "PEG of 1.5x or lower is a near-certain formula for superior returns." [p. 83]
- "Payback Ratio of less than 1x is a near-certain formula for superior returns." [p. 83]
- "Payback Ratio = Market Cap ÷ Next 5 years' PAT" [p. 83]
- "Payback ratio < 1 fails to offer the highest return for the first time ever" [p. 100]
- "We have used perfect foresight of 5 years' earnings to calculate PEG." [p. 100]

**Pseudocode**
```
# Data: pe_ttm, mcap, pat_next_5y (consensus/model) or realised (hindsight), eps_cagr_next_n
peg = pe_ttm / (100 * eps_cagr_next_n)       # growth in % points
payback = mcap / sum(pat_next_5y)
buy_candidate if peg <= 1.5 (or < 1 strict) and payback < 1
# backtest variant (hindsight): use realised 5y PAT after the date, report as upper bound only
```

**Ambiguities & assumptions**
- The book's PEG and Payback results use realised future profits for a set of past winners (selection and look-ahead bias). They cannot be reproduced as a live signal. ASSUMPTION: for a clean test use trailing 3-year PAT CAGR as the growth term; mark results as a proxy.
- PEG <= 1.5 (Framework #24) vs PEG < 1 (empirical): both stated; ASSUMPTION: test both thresholds.
- Which "growth" (EPS vs PAT, 2/3/5 years): the book says "Earnings CAGR for next 2/3/5 years" [p. 83]. ASSUMPTION: 3 years.

### 2.7 Blue Chip dividend screen (Study 16 summary)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality-income / value (mechanical) | 113 |
| Timeframe & holding period | Not found in this book | - |
| Universe / eligibility filters | Six criteria: (1) 20 years of uninterrupted dividends; (2) dividends raised in at least 5 of last 12 years; (3) earnings growth in at least 7 of last 12 years; (4) average RoE of at least 15% for the last 12 years; (5) at least 5 million shares; (6) owned by at least 80 institutional investors | 113 |
| Market / regime filter | None | - |
| Setup conditions | All six criteria hold | 113 |
| Entry trigger & order type | Two buy signals: (1) dividend yield higher than 10-year median AND P/E lower than 10-year median; (2) dividend yield greater than 3% | 113 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Uninterrupted dividends | 20 years | | 113 |
| Dividend raised | >= 5 of last 12 years | | 113 |
| Earnings growth years | >= 7 of last 12 | | 113 |
| Average RoE | >= 15% over 12 years | | 113 |
| Shares outstanding | >= 5 million | | 113 |
| Institutional holders | >= 80 | | 113 |
| Dividend yield trigger | > 3% | or yield > 10y median and P/E < 10y median | 113 |

**Key quotes**
- "Six criteria help shortlist high-quality Blue Chips" [p. 113]
- "Dividend yield greater than 3%." [p. 113]
- "Dividend yield higher than 10-year median and PE lower than 10-year median" [p. 113]

**Pseudocode**
```
# Data: dividend history 20y (point-in-time snapshots from 2026 only), eps history 12y, roe 12y, shares, inst_holders
eligible = div_years_uninterrupted>=20 and div_up_years_12>=5 and eps_up_years_12>=7 and mean(roe_12)>=0.15 and shares>=5e6 and inst>=80
buy = eligible and ((dy > median_dy_10y and pe < median_pe_10y) or dy > 0.03)
```

**Ambiguities & assumptions**
- Only a summary is given (the full study is not in this file). No exit, sizing or holding rule: not found in this book. ASSUMPTION: hold until the buy condition fails and yield falls below 10-year median.
- Institutional-holder count is not available in our data. ASSUMPTION: drop criterion 6 or proxy with traded value.

### 2.8 Consistent Wealth Creator ranking (price-based rolling outperformance)
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality-persistence factor (price-only, mechanical) | 5 |
| Timeframe & holding period | 25-year study, 23 rolling 3-year periods; the 5-year study uses appearance count in the last 10 annual studies | 5, 89 |
| Universe / eligibility filters | Top 500 companies by market cap in the base year; must have outperformed the benchmark over the full period (to be a wealth creator) | 5 |
| Market / regime filter | None | - |
| Setup conditions | Consistency count = number of rolling 3-year periods in which the stock outperforms the Sensex; rank by count, ties broken by higher price CAGR | 5 |
| Entry trigger & order type | Ranking, not a trading signal; the book uses it to describe winners (hindsight) | 5, 8 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

Related ranks in the same study: "Fastest" = price CAGR rank among those beating the benchmark (100 companies beat 9.2%); "Biggest" = absolute wealth created (change in market cap adjusted for equity issuance); "All-round" = sum of Fastest, Biggest and Consistent ranks, ties by higher price CAGR [p. 5]. For 2015-20: Consistent = number of appearances in the past 10 annual studies, then 10-year price CAGR [p. 89]. Top consistent: Kotak Mahindra Bank (21 of 23 periods) [p. 7].

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Rolling window | 3 years | | 5 |
| Number of periods | 23 (1995-98 to 2017-20) | 10 annual studies for the 5-year version | 5, 89 |
| Benchmark | BSE Sensex | | 5 |
| Tie-break | higher price CAGR | | 5 |

**Key quotes**
- "we rank the companies based on the highest number of rolling 3-year periods in which the companies outperform the corresponding Sensex performance" [p. 5]
- "Kotak Mahindra Bank is the most Consistent Wealth Creator between 1995 and 2020." [p. 7]
- "Where the number is same, higher the Price CAGR, higher is the rank." [p. 5]

**Pseudocode**
```
# Data: adjusted close, benchmark = NIFTYBEES (or equal-weight index from panel)
for each stock s at date t: for k in range(N_PERIODS):      # rolling 3y windows ending at annual marks
    win_return(s,k) = close[end_k]/close[start_k]-1 ; bench_return(k)
    beat(s,k) = win_return > bench_return
consistency(s,t) = sum(beat(s,k) for the last N_PERIODS windows)
buy top decile by (consistency, then 25y or 10y price CAGR); hold 1 year; rebalance annually
```

**Ambiguities & assumptions**
- In the book the ranking is computed after the full period (look-ahead), then described as wealth creators; no forward test is shown. ASSUMPTION: run the same ranking using only past windows and test forward 1-year returns.
- Start of the rolling windows (March year-end) and benchmark total return vs price: price. ASSUMPTION: March year-ends; benchmark NIFTYBEES.
- Consistency over fewer than 23 periods for newer stocks: not found in this book. ASSUMPTION: require at least 8 windows (a minimum 10-year history).

### 2.9 Winner Categories and Category Winners
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Sector-growth plus quality leader (top-down sector screen feeding bottom-up pick) | 67, 112 |
| Timeframe & holding period | 10-year example (2010-2020); long term | 67 |
| Universe / eligibility filters | Winner Categories: sectors (1) expected to grow at least 1.5x nominal GDP growth and (2) consolidated (not too many players). Category Winners: companies in Winner Categories with entry barriers/competitive advantage and great management | 67, 112 |
| Market / regime filter | None | - |
| Setup conditions | Winner Category + Category Winner | 67 |
| Entry trigger & order type | "Winning investments happen when Category Winners are bought at reasonable valuation" (reasonable but not necessarily cheap); example: Eicher Motors bought at P/E 21x in March 2010 returned 35% CAGR to FY20 vs 5% for the Sensex | 67, 112 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Not found in this book | - |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Sector growth hurdle | >= 1.5 x nominal GDP growth | example: 21% vs 12% nominal GDP | 67 |
| Consolidation | "only a handful of players" (no number) | | 67 |
| Valuation | "reasonable" (example P/E 21x) | | 67, 112 |

**Key quotes**
- "Expected to grow at least 1.5x nominal GDP growth; and" [p. 67]
- "Winning investments happen when Category Winners are bought at reasonable valuation." [p. 67]
- "Winning Investments are made when Category Winner stocks are bought at reasonable (but not necessarily cheap) valuations." [p. 112]

**Pseudocode**
```
# Data: sector revenue series (sum of constituents), nominal GDP growth, market-share concentration (e.g. HHI or top-5 share)
for sector in sectors: if sector_sales_cagr_3y >= 1.5 * nominal_gdp_growth and top5_share >= X:   # ASSUMPTION X = 60%
    for s in leaders(sector, top 2-3 by sales): if passes 2.1 gates and pe_ttm <= 1.0 * 5y_median_pe: buy
```

**Ambiguities & assumptions**
- The book never defines "consolidated" numerically. ASSUMPTION: top-5 sales share >= 60%.
- "Reasonable valuation" has no threshold here. ASSUMPTION: PEG <= 1.5 (2.6).
- Growth is "expected" (forward); a backtest must use trailing growth as a proxy.

### 2.10 Large unpopular turnaround
| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Contrarian / event-driven value in large caps (Partly codable) | 73 |
| Timeframe & holding period | Example: FY13 to FY17 (4 years) | 73 |
| Universe / eligibility filters | Large companies "unpopular in the markets" due to business-cycle downturn, adverse regulatory change or perceived weak management | 73 |
| Market / regime filter | None | - |
| Setup conditions | Large company trading at a depressed market cap relative to its revenue and with an identifiable catalyst; HPCL example: end-FY13 revenue over INR 2 trillion, market cap under INR 100 bn | 73 |
| Entry trigger & order type | Not found in this book (the catalyst, e.g. deregulation of diesel prices in October 2014, is event-based) | 73 |
| Initial stop-loss | Not found in this book | - |
| Exits: profit-taking | Not found in this book (HPCL: PAT rose 16x and stock 5.5x in 4 years, 53% CAGR) | 73 |
| Exits: trailing / time / signal | Not found in this book | - |
| Position sizing | Not found in this book | - |
| Adding to / pyramiding | Not found in this book | - |
| Portfolio limits (max positions, correlation, heat) | Not found in this book | - |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Market cap / sales (HPCL example) | < 0.05 (less than INR 100 bn on over INR 2 trillion revenue) | | 73 |
| Result in example | PAT up 16x, price up 5.5x, 53% CAGR | | 73 |

**Key quotes**
- "Many large companies become unpopular in the markets due to various reasons" [p. 73]
- "In the 4 years between FY13 and FY17, HPCL's PAT rose 16x and stock price 5.5x" [p. 73]

**Pseudocode**
```
# Price-only proxy (testable): large cap (top 100 by traded value) with 3y relative return < -X% vs benchmark and P/S in bottom quintile of its own history
# then hold 3-4 years. Fundamental catalyst flag is manual.
```

**Ambiguities & assumptions**
- Pure anecdote with one worked example; no screen is given. ASSUMPTION: price-only proxy: top-100 traded-value stocks whose price is in the bottom decile of 3-year relative return and above their 52-week low by 20%; hold up to 4 years. Low priority.

## 3. Risk & money-management rules

The book is a stock-selection philosophy; it states no stop-loss, risk per trade or drawdown rule. What it does state:
- **Margin of safety:** buy only when price is "meaningfully lower than the assessed value to account for potential risks" [p. 33]; a "true Margin of Safety" must be demonstrable by figures [p. 84]. This is the main risk control.
- **Avoid permanent loss:** avoid Gruesome companies (high growth that consumes capital) however cheap [p. 45]; avoid "Quality Traps" and "Growth Traps" and invest only in True Wealth Creators [p. 38]; management with low integrity is an "obvious avoid" ("Race to Zero") [p. 77].
- **Concentration and sizing:** "Focused Investing" with big bets when opportunities are rare; Kelly insights (asymmetric payoff, create edge, bet big); no weights given [p. 114]. 2015-20 top-10 stocks were 63% of wealth created, flagged as market polarisation [p. 91].
- **Liquidity:** only reasonably liquid stocks (free-float market cap, average daily volume) [p. 84].
- **Promoter pledge:** very high pledge is a red flag because lenders may liquidate and hit the price [p. 81].
- **Risk checklist (Q25):** economic/sector slowdown (B2C less vulnerable than B2B/B2G), adverse change in competition (e.g. Hero MotoCorp after Honda split), digital/technology disruption, adverse regulation (e.g. Glaxo's price control), capital misallocation (mega acquisitions gave muted returns), key-man and succession risk [p. 84, p. 85, p. 86, p. 87].
- **Mid/small-cap caution:** "Speed thrills, but at times, kills; drive with caution"; management integrity separates enduring winners from transitory multibaggers [p. 92].
- **Commodity stocks:** "sell too soon" because squeezes are not permanent [p. 110].
- **Mega-cap churn:** only 32 of the top 100 companies of 1995 were still in the top 100 in 2020; 45 fell below rank 250 [p. 14]. This supports periodic re-screening.

## 4. Non-codable guidance

- QGLP Booklet (coordinator addition): Quality Business = sustained competitive advantage "measured by high return ratios", industry leadership, monopoly/duopoly/oligopoly structure, secular consumer-facing business, "limited use of leverage" [p. 122]; Quality Management = industry-leading margins, rational capital allocation, regular dividends, innovation, honesty and disclosure [p. 123]; Growth only adds value when return on capital exceeds cost of capital; look for large addressable market, market-share gains, margin levers [p. 124]; Longevity = long competitive-advantage period and 10-15 years of growth potential [p. 125]; Price tools listed: historical P/E band discount, P/B discount, PEG, DCF, replacement-value discount, popular/unpopular, Payback, dividend yield, with no thresholds given [p. 126]. These are qualitative and add no numeric rule beyond sections 2.1 and 2.6.
- Checklist is "a work-in-progress" to be "constantly improved" and applied "before every investment decision" [p. 31]. Ideas from screeners, brokers or media "merely generate stock ideas" [p. 38].
- Management integrity: 360-degree feedback from customers, employees (current and ex), dealers, suppliers, competitors; look for the "moment of integrity"; watch auditors' reports, top management changes and pledged shares; sharp practices (earnings manipulation, cash-flow shenanigans, related-party transactions) [p. 75, p. 76].
- Management competence, growth mindset, capital allocation, organisation depth, culture (avoid toxic culture), succession plan, skin in the game [p. 77, p. 78, p. 79, p. 80, p. 81].
- Moat sources (brand, patents, distribution, switching costs, scale) and what breaches a moat; Lindy effect (prefer older firms); CAP/GAP (long CAP and long GAP names are secular, high GAP names are cyclical) [p. 41, p. 58, p. 62, p. 63].
- Psychology: patience is "the rarest" of vision, courage and patience; compounding rewards long holding [p. 36, p. 72].
- Market commentary (2020): profits-to-GDP at lows, Sensex EPS flat FY14-20, valuations high (market cap near 100% of GDP vs 60% average), "expect the market to track nominal GDP growth of 10-12%" [p. 16, p. 17, p. 18].
- Forget markets, think stocks; G = R (earnings growth roughly equals return, especially for portfolios) [p. 90, p. 94].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily adjusted close, volume (OHLCV) for the full ~3,700-stock panel including delisted names; benchmark NIFTYBEES (or an equal-weight index built from the panel); fundamentals fields: market cap (shares x price), RoE, PAT, sales, total assets, net worth, debt/equity, operating cash flow, capex/FCF, debtors, creditors, dividend history, promoter holding, promoter pledge, sector tag, analyst or model EPS estimates; free-float market cap. Delivery % is not used by the book.
- **Testability with our data:**
  - Backtestable on 2005-2026 prices alone: 2.8 (rolling 3-year relative-outperformance consistency vs NIFTYBEES or equal-weight index); price-rank proxies for 2.3 (rank by traded value as a proxy for market-cap rank) and a price-only proxy of 2.10; reproducing the Mega/Mid/Mini crossover statistics using a market-cap proxy.
  - Forward-test only (point-in-time fundamentals exist only from Feb 2026, 3-year growth from May 2026): 2.1, 2.2, 2.4, 2.5, 2.6, 2.7, 2.9 (all need RoE, margins, leverage, cash flow, PEG/Payback inputs).
  - Needs data we do not have: consensus 3-to-5-year earnings estimates (PEG and Payback as the book defines them), institutional-holder counts (2.7), qualitative judgement fields (leadership, moat, management integrity, value migration, Five Forces scores for new sectors; the Five Forces table on p. 56 gives scores for about 50 sectors).
- **Market-structure differences:** the study is already NSE/BSE and long-only, so no short or futures issues. Concerns: (a) the book uses BSE Sensex; ASSUMPTION: NIFTYBEES (Nifty 50) or an equal-weight panel index as the benchmark. (b) Market-cap rank is not available historically; ASSUMPTION: use traded-value rank (60-day average of close x volume) as the proxy and treat the results as approximate. (c) Small caps (2.4, around INR 75 bn market cap) have circuit limits and low liquidity; ASSUMPTION: minimum 20-day average traded value of INR 1 crore, position cap at 1-2% of ADV, and 0.1% slippage plus STT and brokerage per trade (low turnover, annual rebalance, so costs are small). (d) Long holding periods mean delivery-based STT (0.1% both sides) is the relevant cost; ASSUMPTION: 0.25% round-trip taxes and brokerage plus 0.1% slippage each side. (e) Survivorship: the book's wealth-creator rankings are conditioned on survival; our panel includes delisted stocks, so the headline results will probably be weaker than the book's (the book itself says 60 of the top 100 of 1995 failed to beat the Sensex [p. 10]).

## 6. Verdict

- **Codeability:** Partly. The quantitative subset (RoE > 13-15%, leverage, PEG, Payback, DuPont trend, mcap-rank bands, dividend screens, rolling consistency) is codable; moat, management integrity, culture, succession, and leadership are judgement and are not defined numerically. No entry timing, stop, exit or sizing rules exist.
- **Priority for backtesting:** Medium. It is a well-known quality-growth tilt suited to India and the price-based pieces (2.8, rank-migration proxy) can be tested today, but the fundamental screens can only be forward-tested from 2026 and the book's evidence is ex post with perfect foresight.
- **Top 3 things a coder is most likely to get wrong:**
  1. Reproducing the book's numbers with look-ahead (PEG and Payback with realised 5-year profits, wealth-creator lists built from end-of-period results, the DuPont test on end-of-window data). These are not tradable; every live signal must use only data available at the decision date, with a reporting lag.
  2. Mixing up the RoE hurdle (13% Q3 vs 15% in Study 18 and the 25-for-25 screen) and the three different size definitions (Mid = rank 101-250; "S" = about INR 75 bn; 25-for-25 uses rank 101-250 after removing five cyclical sectors) and treating "valuations don't matter" (25-for-25, p. 19) as consistent with the checklist's PEG/Payback gate (Q22).
  3. Assuming the book has exit, stop or sizing rules. It has none; adding an arbitrary stop-loss or trading frequency changes a long-horizon (5-25 year) compounding approach into a different strategy and will understate its returns.
