# Investing ideas by Samit Vartak (session notes) — Samit Vartak (notes by an unnamed attendee)

- **Source file:** Google Drive invest/Samir Vartak session.pdf (8 pages). The file name and inventory spell the speaker "Samir"; the text itself says "Samit Vartak" on p. 1, and this spec uses the text's spelling.
- **Text file used:** text/vartak_session.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python verify_citations.py specs/vartak_session.md text/vartak_session.txt`. Fix every WRONG PAGE result, and re-check nearby unquoted citations for the same drift.
- **Coverage:** Read lines 1-327 of text/vartak_session.txt in full (one read); last marker reached was `[[PAGE 8]]`; nothing skimmed. These are a third-party attendee's informal, partly garbled notes of a talk and Q&A by Samit Vartak, not the speaker's own writing. Several figures (liquidity, market-cap bands) are garbled and are flagged as ambiguous below. Reading done by a Sonnet sub-agent. The coordinator read the whole text itself, re-ran the verifier and an exact-page check, confirmed every table citation against pp. 1-8, and added the ambiguity note on the garbled doubling-exit sentence.

## 1. The method in brief

The notes describe a concentrated, growth-focused equity approach for Indian companies, run as a portfolio of roughly 16-20 stocks, each held for a short multi-year horizon (not more than 3-4 years) while earnings compound at a minimum of 25% a year [p. 1]. The claimed edge is picking businesses with a competitive advantage that are gaining market share and growing faster than the index, with the expectation of about 2x in 3 years [p. 1, 3]. The aim is that a few winners (2-3 of 20, possibly 10x) carry the portfolio [p. 1]. The speaker says winners are rare ("we hardly get one or two multibaggers out of 15 companies") [p. 3]. Sectors are not predicted; leadership rotates each decade (building materials and speciality chemicals "at present") [p. 1, 5]. The speaker says the method is the same across large, mid, small and micro caps, with liquidity being the only difference [p. 6].

Buy decisions rest heavily on qualitative judgement: competitive advantage, market-share gain, management quality, supply-chain and competitor checks [p. 1, 4, 5, 8]. Sell decisions are also mostly discretionary: structural change or governance problems trigger an exit; poor results trigger analysis and a wait of two quarters; failing to double in 3-4 years triggers an exit; valuation is rarely a reason to sell [p. 3]. No track record or numerical backtest is presented in these notes; the only mention of backtesting is a general remark that it "helps" [p. 6]. The talk is delivered for Indian small/mid-cap growth investing and the PMS/AIF discussion shows the products are offered in India [p. 7].

## 2. Strategies

Only one separately testable strategy is described. The large-cap, mid-cap, small-cap and micro-cap portfolios are explicitly said to use the same parameters, differing only in liquidity [p. 6], so they are recorded as universe variants inside 2.1 rather than as separate strategies.

### 2.1 Concentrated growth portfolio (25% earnings growth, 3-4 year hold)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Growth / quality-growth, fundamentals-driven, concentrated, long-only. Not a price-pattern system. | 1, 6 |
| Timeframe & holding period | Holding period not more than 3 to 4 years; "buy and forget" is rejected; look 3 to 4 years ahead rather than at 10 years of history. Use a 3-4 year view then move on. | 1, 5, 6 |
| Universe / eligibility filters | Indian companies with competitive advantage and consistent profits; high quality, growing, gaining market share. Same parameters for large, mid, small and micro caps; liquidity is the only difference. Small cap is "below 5000 crore"; a figure of "6500 crore" is quoted for micro cap; "1000 crore" is quoted as the point where allocation gets difficult (garbled, see Ambiguities). Cash flow to profit generation and high return on equity are named as parameters. Loss-making or break-even new-age listings are hard to value and not adopted. | 1, 6 |
| Market / regime filter | Not found in this text. The speaker says not to time the market or control valuations. | 3 |
| Setup conditions | Minimum 25% earnings growth; growth above the index; market-share gain versus competitors; earnings growth higher than volume growth; margin improvement and capex growth needed for 25% growth; strict working-capital cycle; cash flow growth ahead of earnings growth (example: cash flow 250% vs earnings growth 150%); good return on invested capital. Expected to double in about 3 years. | 1, 2, 7 |
| Entry trigger & order type | Not found in this text. Selection is by own screener plus qualitative evaluation (financial history, desktop research, management contact, plant visit, competitor, vendor and distributor checks), then a decision. No price trigger or order type is given. | 8 |
| Initial stop-loss | Not found in this text. No price stop is stated; drawdowns of 30-40% are described as normal rides on the way to big winners. | 4 |
| Exits: profit-taking | Not found in this text as a target price. Valuation is rarely considered for exiting if the business delivers. Switch to a similar industry if a better opportunity at a lower price appears. | 3 |
| Exits: trailing / time / signal | (a) Doubling not achieved within 3-4 years: exit. (b) Holding period not more than 3-4 years. (c) Bad results: analyse and wait two quarters. (d) Structural change in the business or a governance problem: exit. (e) Cyclical businesses: take a much quicker call because stocks fall 30-40%. (f) If the sector tide has changed, exit. A higher-risk name is expected to triple in 4 years. | 1, 3, 5, 6 |
| Position sizing | 16 companies in one portfolio, 6 to 7% in each. Elsewhere about 20 stocks are cited as the portfolio size. | 1, 6 |
| Adding to / pyramiding | Not found in this text. The speaker notes it is hard to re-buy a stock after a large rise (Bajaj Finance example), and that slowing market share for a short period calls for patience, not selling. | 3, 7 |
| Portfolio limits (max positions, correlation, heat) | About 16 positions at 6-7% (or about 20 stocks); sectors should be different; small/mid-cap portfolios may keep one or two large caps for stability; large-cap exposure via passive strategy, active strategy in mid and small caps. | 1, 6 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Minimum earnings growth | 25% | Expecting 25% but it may deliver only 5% (reason to analyse) | 1, 3 |
| Maximum holding period | 3 to 4 years | "Look for 3 to 4 years and move on" | 1, 6 |
| Return objective per holding | Double (2x) in 3 to 4 years | 2x in 3 years; triple in 4 years for higher-risk names | 1, 3, 6 |
| Number of holdings | 16 companies | About 20 stocks (3 of 20 giving 10x); 15 companies mentioned in the multibagger remark | 1, 3, 6 |
| Weight per holding | 6 to 7% | - | 6 |
| Wait after bad results | Two quarters | - | 3 |
| Cyclical fall to avoid | Stock falls 30 to 40% | - | 3 |
| Cash flow vs earnings growth (illustration) | Cash flow 250% vs earnings growth 150% | - | 2 |
| Small-cap limit | Below 5000 crore | - | 6 |
| Micro-cap figure | 6500 crore (garbled) | - | 6 |
| Liquidity/allocation difficulty point | 1000 crore (garbled) | - | 6 |
| Large-cap inclusion in small/mid portfolio | One or two large caps | - | 6 |
| Drawdown tolerance | Falls of 30 to 40% multiple times on the way to 40-50x; market falls of 10-15% | - | 4 |
| Stop-loss | Not found in this text | - | - |

**Key quotes**

- "Always look for minimum 25% earnings growth" [p. 1]
- "Holding period should be not more than 3 to 4 years" [p. 1]
- "Never follow buy and forget stocks" [p. 1]
- "Sectors should be different and every decade changes" [p. 1]
- "If I invest 20 stocks and Iam decent good, understand them very well then 3 out of 20 gives" [p. 1]
- "Cash flow is 250% and earning growth is 150% then returns comes" [p. 2]
- "analyse what is going wrong and wait for two quarters" [p. 3]
- "If my standard of doubling in 3 to 4 years I will exit" [p. 3]
- "Valuations are rarely considered for exiting, specially if business delivers what we look for" [p. 3]
- "If I get better opportunity at Lower price I will switch to similar industry" [p. 3]
- "quicker call because stock falls 30 to 40 %" [p. 3]
- "Don’t try to control valuations or time the market" [p. 3]
- "If tide has changed exit, because so many moving parts in world for a sector to move in one" [p. 5]
- "Focus on certain parameters cash flow to profit generation, high return on equity and growth" [p. 6]
- "16 companies in one portfolio and then allocate 6 to 7 % in each company" [p. 6]
- "Liquidity is the only difference between core, small and micro portfolios" [p. 6]
- "Small cap is below 5000 crore" [p. 6]
- "Higher risk taken then higher returns in 4 years it has to triple." [p. 6]
- "Margin improves and capex growth is very imp wen we want 25% growth" [p. 7]
- "Identification phase is own screening and filtering proceeds for stocks to get in my screener" [p. 8]

**Pseudocode** (fundamental fields are forward-test only; see section 5. Fields: daily close/open/volume, market cap, trailing-twelve-month net profit (PAT) and its YoY growth, operating cash flow, ROE, sector tag.)

```
PARAMS: N = 16 ; W = 1/N (cap 7%) ; MIN_G = 0.25 ; MAX_HOLD_M = 48 ; REVIEW_M = 36
        TARGET_MULT = 2.0 ; WAIT_Q = 2 ; CYCLICAL_SECTORS = [list]; CYC_DD = 0.20 (ASSUMPTION)

each quarter-end (after results are published, point-in-time):
    candidates = []
    for s in universe(mcap_band, liquidity_ok):
        if PAT_yoy_growth(s) >= MIN_G
           and CFO_growth(s) >= PAT_yoy_growth(s)        # ASSUMPTION: encodes "cash flow ahead of earnings"
           and ROE(s) >= ROE_MIN                          # ASSUMPTION value
           and s not held:
            candidates.append(s)
    rank candidates by PAT_yoy_growth (ASSUMPTION: no ranking given in text)

    for p in holdings:
        age = months since entry
        # exit rules
        if age >= MAX_HOLD_M:                       exit(p)               # hold <= 3-4 yrs
        elif age >= REVIEW_M and close(p) < TARGET_MULT * entry_price(p): exit(p)   # not doubling
        elif bad_results(p) for WAIT_Q consecutive quarters (PAT_yoy_growth < MIN_G): exit(p)   # ASSUMPTION for "wait two quarters"
        elif p.sector in CYCLICAL_SECTORS and close(p) <= (1-CYC_DD)*max_close_since_entry(p): exit(p)  # ASSUMPTION
        # discretionary exits (structural change, governance) cannot be coded

    free_slots = N - len(holdings)
    buy top free_slots candidates at next session open, equal weight W (ASSUMPTION), skip if ADV constraint fails
```

**Ambiguities & assumptions**
- (Coordinator note) The exit sentence "If my standard of doubling in 3 to 4 years I will exit" [p. 3] is garbled in the notes. It can be read as "exit when the stock no longer meets my standard of doubling in 3-4 years" (a forward-looking thesis check) or as "exit once it has doubled in 3-4 years" (a profit target). The context (exit triggers listed alongside structural change and governance issues, and "Valuations are rarely considered for exiting" [p. 3]) favours the first reading. ASSUMPTION: treat it as a thesis-failure exit, not a profit target; test the profit-target reading as a variant.

- **Number of holdings: 20 vs 16.** The notes cite about 20 stocks for the target of 2-3 big winners [p. 1, p. 1 "I need at least 20 companies"] and later "16 companies in one portfolio ... 6 to 7 %" [p. 6]. 16 x 6-7% = 96-112%, so the 6-7% fits 16 names. ASSUMPTION: N = 16 with equal weight 6.25%, cap 7%; test N = 20 (5%) as a sensitivity.
- **Holding period vs doubling test.** The notes say hold "not more than 3 to 4 years" [p. 1] and exit if the stock has not doubled in 3-4 years [p. 3]. It is unstated whether a winner that has doubled is sold at the 4-year mark. ASSUMPTION: hard cap at 48 months, review at 36 months (exit if price is under 2x cost).
- **"Doubling" means price or earnings?** The text says "doubling amount in 3 years" [p. 1] (price/capital). ASSUMPTION: price (adjusted close) at least 2x the entry price.
- **Market-cap / liquidity bands are garbled.** "If liquidity issue goes above 1000 crore then it’s difficult to allocate" [p. 6] reads like a fund-size (AUM) limit for a strategy, not a stock threshold. "If we find more liquidity, then 6500 crore for micro cap" and "Small cap is below 5000 crore" [p. 6] are contradictory if both are market-cap caps (micro cap above small cap). ASSUMPTION: small cap = market cap below Rs 5,000 crore; micro cap = a sub-segment of small cap with a minimum average daily traded value filter we choose (suggested Rs 1 crore ADV, not from text); treat 6,500 crore and 1,000 crore as unusable and not coded.
- **Entry trigger.** Not found in this text. ASSUMPTION: buy at next session open after the signal date; no price filter.
- **Stop-loss.** Not found in this text. The speaker accepts 30-40% falls [p. 4]. ASSUMPTION: no price stop for non-cyclicals.
- **Bad-result handling.** The text says wait two quarters [p. 3] but not what happens after. ASSUMPTION: exit if growth is still below 25% after two further quarters.
- **Cyclical quick exit.** Text gives no threshold other than the 30-40% fall that makes them dangerous [p. 3]. ASSUMPTION: cyclical sector list is our own; trailing 20% drawdown exit (not from text).
- **Growth definition.** "Earnings growth" is not defined (PAT, EPS, yoy or multi-year). ASSUMPTION: trailing-twelve-month PAT growth yoy at least 25%; the 3-year growth field (available from May 2026) is a sensitivity.
- **Quality screens.** Cash flow to profit, high ROE [p. 6] and "return on investment in capital allocated" [p. 7] are named without thresholds. ASSUMPTION: CFO/PAT at least 1 and ROE at least 15% (illustrative, not from text).
- **Ranking / selection among qualifiers.** Not found in this text.
- **Rebalancing.** Not found in this text. ASSUMPTION: no rebalancing of weights between entries and exits.
- **Large-cap handling.** The notes say large-cap alpha is "extremely difficult", suggest passive for large caps and one or two large caps inside small/mid portfolios [p. 6]. ASSUMPTION: no separate large-cap strategy is coded.
- **Discretionary elements.** Competitive advantage, management quality, supply-chain and competitor checks, structural-story judgement [p. 5, 7, 8] cannot be coded.

## 3. Risk & money-management rules

- Position size 6-7% per company in a 16-company portfolio [p. 6]; about 20 stocks cited elsewhere [p. 1].
- Diversify across sectors; sector leadership changes each decade [p. 1].
- Diversify so that 2-3 holdings in 20 can produce the large winners; a single winner is not relied upon [p. 1].
- Small/mid-cap portfolios fluctuate more, so one or two large caps are included for stability [p. 6].
- No stop-loss is stated; 30-40% drawdowns are described as normal multiple times on the way to 40-50x rides, and 10-15% market falls are expected [p. 4].
- Cyclicals need quicker exits [p. 3].
- Time stop: exit if not doubled in 3-4 years [p. 3]; maximum hold 3-4 years [p. 1].
- Do not exit purely on valuation [p. 3]; do not time the market [p. 3].
- Higher-risk (turnaround or newly listed loss-making) names must be able to triple in 4 years to justify the risk [p. 6].
- Account-level drawdown limits, risk per trade, or total exposure caps: Not found in this text.

## 4. Non-codable guidance

- Do not predict which theme will play out; judge whether it is sustainable; pick 3-4 year views (export, IT, speciality chemicals, API, pharma, real estate, building materials) [p. 1, 5].
- Track competition and market-share gains constantly; market share gain is the main proof of quality (APL Apollo, Hawkins "cash cow" examples) [p. 1].
- Management: every promoter is unique; poor communicators can be excellent executors; check culture, micro-managing vs delegating, ability to execute what was promised [p. 4, 5].
- Look 3-4 years forward, not 10 years of history [p. 5].
- Selling is very hard; two errors: leaving too late and leaving too early; the costliest error is exiting a structural compounder that becomes a 100x or 1000x [p. 3, 7].
- Exit immediately on a structural change (Kaveri Seeds, Laopala examples) or a governance problem (J&K Bank example) [p. 3, 7].
- Bad results: analyse the cause; businesses are never a straight line [p. 3].
- Stay invested; recency bias leads investors to book profits early and be unable to re-enter (Bajaj Finance example) [p. 3].
- Client and investor expectations: most clients arrive late in the cycle; set expectations, lengthen the horizon [p. 4, 5].
- Prefer structural over cyclical businesses (Bajaj Finance vs Tata Steel example); cyclical alpha in 2011-2019 may not repeat [p. 5].
- New-age loss-making listings (Zomato, Nykaa) are hard to value, penetration is high, so not adopted at the time [p. 6].
- Continuous learning: study business models, why PE differs by business, review mistakes (misjudgement or probability) [p. 4].
- Deal sourcing: own screener, brokers, like-minded investors; then financial history, management calls, plant visits, competitor, vendor and distributor checks, local background checks [p. 8].
- Product structure (PMS vs AIF): PMS is open-ended with a Rs 2 crore minimum and holdings in the client's own demat; AIF is closed-ended with trust-level taxation [p. 7].
- Macro and sector commentary (real estate proxies, China chemicals, financials, autos, SaaS, PLI) is opinion and is not a rule [p. 2, 3].

## 5. Adapting to NSE (Indian equities)

- **Data required:** Daily adjusted OHLCV (entry/exit prices, 3-4 year holding checks, drawdown tests); market capitalisation and average daily traded value (liquidity bands); point-in-time fundamentals: quarterly and TTM net profit (PAT) and YoY growth, operating cash flow, ROE or ROCE, sales and margin, capex, sector tag (for the cyclical flag). Delivery % and index data are not required by the rules.
- **Testability with our data:**
  - Backtestable on 2005-2026 prices: the holding-period cap, "doubled in 3-4 years" time stop, cyclical trailing-drawdown exit (our assumption), equal-weight 16-name sizing mechanics, and the liquidity filter using traded value.
  - Forward-test only: the core entry screen (minimum 25% earnings growth, cash flow ahead of earnings, ROE, margin and capex improvement) and the "bad results, wait two quarters" rule, because our fundamentals are point-in-time snapshots only from Feb 2026 (3-year growth fields from May 2026). A historical backtest of these screens would need reconstructed fundamentals and would carry look-ahead bias. ASSUMPTION: a price-only proxy (for example, ranking by trailing 3-year price return among liquid small/mid caps) could test the portfolio mechanics on 2005-2026 data, clearly labelled as not the author's method.
  - Needs data we do not have: qualitative judgement (competitive advantage, management quality, supply-chain checks, structural-change calls), historical market-cap history for 2005-2023 beyond what prices imply, and any earnings history before 2026.
- **Market-structure differences:**
  - Long-only fits the NSE cash market (no overnight shorting needed).
  - Small and micro caps: circuit limits and thin liquidity limit entry and exit; ASSUMPTION: cap position size at a fraction (suggested 5-10%) of average daily traded value and allow multi-day fills.
  - Costs: STT, brokerage and about 0.1% slippage should be applied; low turnover (3-4 year holds) keeps costs modest.
  - Benchmark: Nifty index history is only from 2024; use NIFTYBEES or an equal-weight index from the stock panel to measure "growth above the index".
  - Survivorship: the panel includes delisted stocks, which is important because the strategy holds growth small caps that may fail.
  - Market-cap thresholds in rupee crore must be adjusted to the date of the test; ASSUMPTION: use percentile bands of the then-current universe rather than fixed 2026 values for historical tests.

## 6. Verdict

- **Codeability:** Partly. The sizing, time-stop and universe mechanics are codable, but the entry screen needs fundamentals we only hold from 2026, and the buy and many sell decisions in the notes are discretionary.
- **Priority for backtesting:** Low. The notes give few precise thresholds (25% growth, 6-7% weights, 3-4 years), no entry trigger or stop-loss, and the screen can only be forward-tested; a price-only proxy would not be the speaker's method.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the garbled liquidity/market-cap numbers (1000 crore, 5000 crore, 6500 crore) as clean stock-level bands; they are partly contradictory and may refer to fund capacity.
  2. Backtesting the 25% earnings-growth screen on history using fundamentals that were not point-in-time available (look-ahead bias).
  3. Mixing up the time rules: "not more than 3-4 years" holding, "doubling in 3-4 years" test, and "wait two quarters" after bad results are separate rules, and valuation is explicitly not an exit trigger.
