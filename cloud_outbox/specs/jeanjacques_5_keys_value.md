# The 5 Keys to Value Investing — J. Dennis Jean-Jacques (McGraw-Hill, 2003)

- **Source file:** Google Drive `Phone Backup Aug 2025/WhatsApp Documents/The 5 Keys to Value Investing (J. Dennis Jean-Jacques).pdf` (file id 1UY7H64so5Py5V8DyQoEmF661nV0JqRRO, 2,733,670 bytes), 256 PDF pages, 250 with a text layer.
- **Text file used:** text/jeanjacques_5_keys_value.txt  (page basis: pdf_pages)
- **Page references:** `[p. N]` = the `[[PAGE N]]` marker in the text file (PDF page index, not the printed page number)
  - Take N ONLY from the nearest `[[PAGE N]]` marker above the passage. Never use page numbers printed in the book's running headers, table of contents or index; they are offset by the front matter.
  - When unsure, confirm with `grep -n` on the text file and take the nearest preceding marker.
  - Before finishing, run `python ../work/bin/verify_citations.py specs/jeanjacques_5_keys_value.md text/jeanjacques_5_keys_value.txt` from the cloud_outbox folder.
- **Coverage:** Every page was read sequentially from [[PAGE 1]] to the last marker, [[PAGE 256]]. Pages 1, 5, 9 and 11 are blank or "intentionally left blank". Image-only or chart-only pages whose text is empty or only captions: [[PAGE 115]] to [[PAGE 116]] (Value Line page for Thermo Electron, Exhibit 4.2), plus the chart exhibits on [[PAGE 112]] (Thermo organisation chart), [[PAGE 117]] (stock chart, Exhibit 4.3), [[PAGE 34]] (Exhibit 1.2) and [[PAGE 138]] (Maytag price chart, Exhibit 5.2); their captions were read, the plotted values were not. Financial tables (Herman Miller income statement, cash flow, balance sheet, [[PAGE 93]] to [[PAGE 95]]; Maytag and Pactiv 10-K excerpts) were read through the flattened text and were not transcribed. The Index ([[PAGE 246]] to [[PAGE 256]]) was only scanned with keyword searches (margin of safety, screen, sell, buy, portfolio, dollar cost averaging) because it contains page pointers only, not rules; the last pages are the author biography. Appendices B (analyst recommendations), C (Moody's EBITDA failings), D (Thermo Electron's January 2000 restructuring press release, [[PAGE 225]] to [[PAGE 231]], case-study source material for the catalyst discussion) and E (SEC form descriptions) were read in full and contain no trading rules. Reading done by a Sonnet sub-agent; coordinator re-checked the citations and read Appendix D itself to confirm the Coverage line.

## 1. The method in brief

Jean-Jacques, an ex-Fidelity and Mutual Series analyst, presents "value investing" as a philosophy of buying businesses, not trading stocks: "Good Business + Excellent Price = Adequate Return over Time" [p. 22]. The framework is the "Five Keys of Value": (1) is this a good business run by smart people, (2) what is it worth, (3) how attractive is the price and what should I pay, (4) how realistic is the most effective catalyst, (5) what is my margin of safety at my purchase price [p. 36]. The intended horizon is "two to three years" to close a discount to fair value [p. 36], with 3 to 5 years named as the appropriate maximum holding period [p. 186]. The portfolio is concentrated (10 to 20 names, "preferably 15") [p. 199]. The author states no index-beating objective: he wants "adequate and consistent performance" [p. 12].

The claimed edge is behavioural and analytical: markets overshoot on fear and greed, volatility is "opportunity" not risk, and a buyer who pays well below a triangulated fair value, with a floor price ("margin of safety") based on assets, take-private values or replacement cost, and a catalyst to close the gap, earns satisfactory returns [p. 31, 33, 34]. He explicitly dismisses market timing and prediction of economic variables [p. 32, 128].

**Evidence presented.** There is no aggregate track record, no backtest and no statistics in the book. Evidence is a set of ten anecdotal case studies from the author's own career (all US stocks, 1994 to 2000). Each gives buy price, fair value, safety price, upside and downside:

| Case | Entry price | Fair value | Safety price | Upside / downside quoted | Page |
|---|---|---|---|---|---|
| Varian Associates (1998) | $33 (40% below $55) | $55 | $29 | 67% up, 12% down | 41, 43 |
| Thermo Electron (1998/99) | $14 | $30 | about $10.50 margin | 114% up, 25% down | 113, 114 |
| Maytag (Mar 2000) | $29 or lower | $50 | $24 | 72% up, 17% down; sold Oct 2000 in the low $30s | 133, 136, 139 |
| FDX / FedEx (late 1998) | below $22 | $45 (up to $60) | not stated | sold at $42, +68% | 129 |
| RH Donnelley (1998) | $16 | $28 to $32 | $13 | 75% up, 19% down | 147 |
| Network Associates (1999) | $15 | $27 to $33 | $12.50 | 100% up, 17% down; over 90% return realised | 150, 151 |
| Sybron International (Apr 2000) | $25 | $37 to $43 | $22 | 60% up, 12% down | 154 |
| Newhall Land (1994) | below $15, below adjusted book | not stated | adjusted book value | doubled in about 3 years | 155, 157 |
| Eaton (2000) | $53 | $73 to $77 (DCF $76) | about $50 | 43% up, 6% down | 159 |
| Pactiv (2000) | $9 | $17.83 | $7.50 | not stated as a %; stock bought at half of fair value | 160, 162, 163 |
| Herman Miller (Feb 1999) | $17 | $26.04 | not stated | exit began at $26 about 18 months later | 90, 91, 92 |

These are survivorship-selected illustrations, not a test. The book never reports a losing trade except the Maytag exit ("the catalysts proved ineffective") [p. 136].

## 2. Strategies

The book is a discretionary framework. Seven separately testable rule sets are extracted below (2.1 to 2.7), plus a catalyst/event strategy (2.8) that is only partly codable. Non-codable analytical material (management assessment, the vertical, ROE-decomposition and cash-flow approaches to analysing a business, SEC filing reading, reading earnings releases) is summarised in the non-codable table at the end of this section and in Section 4.

### 2.1 Five Keys composite buy rule (price at least 40% below fair value, near the safety floor)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value, with margin of safety and a catalyst (event-informed). | 22, 36 |
| Timeframe & holding period | Discount large enough "to generate adequate returns in two to three years"; 3 to 5 years is "ample time"; Mr. Market may deliver fair value early. | 36, 165, 186 |
| Universe / eligibility filters | Companies passing Key 1 (good business, smart and shareholder-aligned management, strong or clean balance sheet) and understood by the investor; avoids businesses with "uncertainty". Value traps excluded. Technology mostly avoided unless priced at or below net cash. | 36, 130, 143, 163, 35 |
| Market / regime filter | None required; the author refuses to predict the market. Bull markets: put the emphasis on catalysts; bear markets: margin of safety is paramount. Screening depth differs by market (see 2.5). | 128, 170, 171 |
| Setup conditions | (a) Fair value from a triangulation of three tools (2.2). (b) Price at a discount of 40% or more to fair value. (c) A margin-of-safety (floor) price, set from assets, replacement cost or take-private value (2.3), well below the buy price (Varian: floor $29 vs buy $33; Maytag floor $24 vs buy $29). (d) A named catalyst of adequate potency (2.8). (e) Skewed risk/reward: the case studies quote upside of 43% to 114% against downside of 6% to 25%. | 41, 43, 114, 136, 147, 151, 154, 159 |
| Entry trigger & order type | Buy when the market price falls to or below the pre-set "reasonable price to pay"; wait and "never chase a stock". Order type not specified (limit-style behaviour implied). May scale in (2.7). | 39, 172 |
| Initial stop-loss | Not specified. The safety price is a valuation floor used to size downside, not a stop-loss. The Maytag exit (low $30s) came while the stock was above the $24 floor, on thesis failure. | 136, 139 |
| Exits: profit-taking | Sell at fair value; may sell early when the market reaches fair value early (buy $10, target $20 within a year, market offers $20 after six months: may sell). Maytag: sold a few shares at $41 "to lock in some profits". Herman Miller: began to exit at the $26 fair value. | 165, 138, 91, 186 |
| Exits: trailing / time / signal | Sell when (1) fundamentals deteriorate or assets are permanently impaired, (2) fair value is reached, (3) the catalyst is unlikely or proven ineffective (Maytag: given "several quarters", sold after one year). No trailing stop. A finite exit point is advised. | 186, 136 |
| Position sizing | Not specified as a rule. "Allocate wisely, invest more in the companies you like best"; positions are smaller when the market only lets you buy a small amount; DCA example of 50 shares at $15 and 100 or more at $13. | 199, 186, 172 |
| Adding to / pyramiding | Add on weakness if fundamentals and the thesis are unchanged ("more shares are purchased"). No pyramiding on strength; DCA "does not work well in bull markets". | 179, 172 |
| Portfolio limits (max positions, correlation, heat) | 10 to 20 holdings, preferably 15, for a nonprofessional; 5 to 10 for an individual (Buffett view); 15 or more for clubs and professionals; spread across industries and opportunity types. No heat or correlation cap. | 199, 197, 198 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Minimum discount to fair value at purchase | 40% (Varian: $33 vs $55) | "at least 40-percent discount to fair value" in the screening blueprint | 41, 195 |
| Margin-of-safety (floor) price vs buy price | Varian floor $29 (buy $33, 12% down); Maytag $24 (buy $29, 17% down) | Downside quoted in cases from 6% to 25% | 43, 136, 114, 159 |
| Minimum upside / downside skew | Not stated as a rule; cases show about 2x to 5x | Up 43% to 114%, down 6% to 25% | 114, 159 |
| Target holding period | 2 to 3 years for the return | 3 to 5 years cap; 5 to 10 years is "too long in the modern era" | 36, 186 |
| Number of positions | 15 | 10 to 20; 5 to 10 | 199, 197 |
| Catalyst waiting period | "several quarters"; sold after one year | Newhall: waited 3 years (cheap to adjusted book value) | 136, 157 |

**Key quotes**

- "to buy solid businesses at exceptional prices in order to achieve adequate after-tax returns over a long period" [p. 21]
- "Ninety percent of successful investing is buying right." [p. 33]
- "if I wanted a 40-percent discount or more for what I deemed to be fair value for the company at the time, $33 per share would be the best price" [p. 41]
- "Never chase a stock." [p. 39]
- "The company reaches its fair value." [p. 186]
- "My ongoing research reveals deterioration of the business fundamentals or permanent impairment to the assets of the firm." [p. 186]
- "The catalyst that I identified prior to making the investment is unlikely to materialize, or is proven ineffective." [p. 186]
- "if a value investor buys a company at $10 per share and expects to sell at $20 per share within a year" [p. 165]
- "I reassessed my margin of safety level and recommended that we sell our stake in the company in the low $30s" [p. 139]
- "Own between 10 and 20 but preferably 15 good businesses at excellent prices." [p. 199]

**Pseudocode**

```
# Requires: FV (fair value per share, from 2.2), FLOOR (safety price, from 2.3), catalyst_score (2.8)
for each stock s on each rebalance date t:
    if not passes_quality_filters(s, t):            # 2.6
        continue
    fv    = fair_value(s, t)                        # 2.2
    floor = safety_floor(s, t)                      # 2.3
    buy_px = 0.60 * fv                              # 40% discount
    if buy_px <= floor: continue                    # buy price must be above the floor
    if price(s,t) <= buy_px and catalyst_ok(s,t) and (price - floor)/price <= MAX_DOWNSIDE:
        candidate.append(s)   # MAX_DOWNSIDE ASSUMPTION 0.25
rank candidates by (fv/price - 1) / ((price - floor)/price)   # upside/downside ratio
open up to 15 positions, equal weight (or overweight best ideas, ASSUMPTION: max 10% each)
EXIT for each holding:
    if price >= fv:                         sell all
    elif thesis_broken(s):                  sell all   # fundamentals worsen, asset impairment
    elif catalyst_failed(s) or held_days > 3 years (or 5 years max): sell all
```

**Ambiguities & assumptions**
- Fair value is a judgement blend (2.2); the book gives no formula for the weights. ASSUMPTION: simple average of the available tools, as Herman Miller and Pactiv do [p. 92, 162].
- The 40% discount is quoted as the author's personal Varian threshold and in the screening blueprint [p. 41, 195]; other cases buy at discounts of 36% to 50%. ASSUMPTION: 40%.
- No stop-loss: the safety price is explicitly not a stop. ASSUMPTION: for backtests add a catastrophic stop at the floor price (safety level) as a sensitivity run only, flagged as not from the book.
- Position size is not specified. ASSUMPTION: equal weight over about 15 positions (1/15, roughly 6.7%).
- The book also says a high buy "at private-market valuations" can be bought above the 40% discount (Eaton at 43% upside) [p. 159]. ASSUMPTION: require the combination discount at least 30% and floor within 25% of price when a catalyst is present; test 40% as the pure version.

### 2.2 Fair value by triangulation (three tools averaged)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value (valuation rule that feeds 2.1). | 72 |
| Timeframe & holding period | Fair value is an exit target for roughly a 1 to 3 year holding. | 36, 91 |
| Universe / eligibility filters | Tool choice depends on the situation: P/E for sound companies without near-term capex; DCF only for non-cyclical, stable-risk firms (not cyclicals, acquirers, restructurings, hidden assets); EV/EBITDA family for negative or depressed earnings; P/B where ROE is high and P/B low; PEG and revenue multiples avoided or used only rarely. | 75, 89, 78, 77, 84, 82 |
| Market / regime filter | Not specified. Uses normalised (mid-cycle) earnings for cyclicals; historical valuation range used for cyclicals only. | 127, 160 |
| Setup conditions | Compute three valuations from different categories (comparison, asset, transaction) and take the simple average. Herman Miller: P/E $1,870m, DCF $2,550m, take-out $2,221m, average $2,214m, divided by 85m shares = $26.04. | 72, 92 |
| Entry trigger & order type | Not applicable (feeds 2.1). | 41 |
| Initial stop-loss | Not specified. | |
| Exits: profit-taking | Fair value is the sell target (see 2.1). | 186 |
| Exits: trailing / time / signal | Re-estimate fair value when fundamentals change; not specified as a schedule. | 186 |
| Position sizing | Not specified. | |
| Adding to / pyramiding | Not specified. | |
| Portfolio limits (max positions, correlation, heat) | Not specified. | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Number of tools | 3 ("triangulates") | comparison, asset and transaction categories | 72 |
| Historical P/E fair multiple (Herman Miller) | 14x | Maytag: 8.5x P/E on estimated EPS $3.50 as buy price | 90, 133 |
| DCF horizon | 5 to 7 years | 3 years too short; beyond 10 too long | 87 |
| DCF discount rate | Pactiv 10%; Eaton 9%; Buffett uses the long-term Treasury rate | WACC = E/Cap*Ec + D/Cap*Dc*(1-Tr) | 162, 159, 86, 87 |
| DCF terminal growth | 3% (Pactiv) | not otherwise stated | 162 |
| Free cash flow definition | Net income + depreciation + amortisation - capital expenditures | EBITDA less capex used in multiples | 86, 91 |
| Enterprise value | Market value + total debt - cash | | 78 |
| Take-out (deal) multiple | Herman Miller 8.0x EBITDA; Pactiv 8 to 10x operating cash flow; RH Donnelley 8 to 9x EV/OCF (deal at 13x); Varian 5.5x EV/pretax cash flow as a floor | | 92, 162, 147, 41 |
| Sum-of-the-parts multiples (Eaton stub) | 7x industrial/commercial, 4x auto and truck, 5x fluid power, on operating cash flow | | 159 |
| Normalised earnings | Pactiv: at least $1.00 per share vs $0.55 reported | | 160 |

**Key quotes**

- "the value investor triangulates a valuation" [p. 72]
- "Many investors use a five- to seven-year time frame when determining the value of an enterprise using the DCF approach" [p. 87]
- "This is done by taking the company’s market value, adding its total debt, and then subtracting the cash." [p. 78]
- "Most value investors do not use PEG ratios." [p. 84]
- "Companies in which value investors are most interested are those with a high ROE" [p. 77]
- "value investors would perhaps rather keep their investment dollars in cash" [p. 74]

**Pseudocode**

```
def fair_value(s, t):
    vals = []
    # (1) comparison tool: historical or twin P/E on normalised EPS
    eps_norm = mean(EPS[s, last 3 fiscal years])         # ASSUMPTION; book says "normalized"
    vals.append(hist_PE_median(s, 5y) * eps_norm)         # Herman Miller used 14x
    # (2) asset/intrinsic tool: DCF on FCF = NI + D&A - capex
    if not is_cyclical(s) and not acquirer(s):
        fcf = NI + DA - capex
        vals.append( dcf(fcf, years=5..7, r=0.09..0.10, g_terminal=0.03) / shares )
    # (3) transaction tool: take-out multiple on EBITDA / operating cash flow
    ev = take_out_multiple(sector) * EBITDA_next
    vals.append( (ev - debt + cash) / shares )
    return mean(vals)       # simple average
```

**Ambiguities & assumptions**
- Twin companies, take-out multiples and "normalised" earnings require judgement and a deals database. ASSUMPTION: use the sector median EV/EBITDA of the stock's own history in place of deals data (the book itself accepts "historical valuation" as a tool [p. 41, 127]).
- Tools are chosen per business; no mechanical selection rule. ASSUMPTION: P/E + EV/EBITDA + DCF, drop DCF for cyclicals (the book's own exclusion list [p. 88]).
- DCF discount rate varies (9%, 10%, risk-free). ASSUMPTION: 10%.
- The book rates fair value per share excluding growth expectations in places (FedEx $45 vs $60 with growth) [p. 129]. ASSUMPTION: use the lower number.

### 2.3 Margin-of-safety floor from asset values (liquidation, replacement and take-private)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value / asset-based downside floor. | 120 |
| Timeframe & holding period | Applies as long as the position is held; reassess at each earnings release. | 136, 179 |
| Universe / eligibility filters | Method depends on industry: liquidation value in declining industries; replacement value in stable industries; take-private floor for companies with strong free cash flow; sum-of-the-parts for "something for free". Avoid companies rated B or lower on Value Line financial strength unless you do your own debt analysis. Shun uncertainty. | 121, 126, 124, 130 |
| Market / regime filter | Margin of safety "paramount in a down market". | 171 |
| Setup conditions | Haircut each balance-sheet item and subtract all liabilities (Exhibit 5.1, Maytag): cash 100%, receivables 70% (60 to 90% range), inventory 70%, PP&E 90%, other assets 80%; add a dividend-stream value (dividend / cost of equity 8.5%); subtract debt; divide by shares. Result $24 vs price $29. | 134, 135 |
| Entry trigger & order type | The buy price is set above the floor so that the downside is small (6% to 25% in the cases). | 136, 159 |
| Initial stop-loss | Not specified; the floor is the expected worst case, not a stop. | |
| Exits: profit-taking | Not applicable. | |
| Exits: trailing / time / signal | If the stock trades below the floor "for a length of time", a buyer, break-up or liquidation becomes likely; if floor is breached because the assets are impaired, re-evaluate the business. | 38, 41 |
| Position sizing | Not specified. | |
| Adding to / pyramiding | Not specified. | |
| Portfolio limits (max positions, correlation, heat) | Not specified. | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Liquidation haircut on PP&E and inventory | 20% (generic goods) to 80% (specific goods); goodwill and intangibles excluded | | 121 |
| Receivables value | 70% (Maytag, low end because of expected downturn) | 60% to 90% | 134, 135 |
| Inventory value | 70% (Maytag: commodity-like) | "relatively high" for commodity inventories | 134, 135 |
| PP&E value | 90% (Maytag) | | 135 |
| Other assets | 80% (Maytag); prepaid pension and intangible pension assets 0 | | 135 |
| Goodwill value | 0 by default | 10% to 60% of reported goodwill if a strong brand | 123, 124 |
| Dividend stream value | dividend / cost of equity (8.5%): $68m / 8.5% about $800m | | 135, 136 |
| Net-net (Graham) value | current assets less all liabilities, little value to PP&E | | 120 |
| Take-private floor | Varian 5.5x EV to pretax cash flow; floor sits above private-market multiple (5x) when public is at 8x | | 41, 126 |
| Value Line financial strength | B+ or better as a rule of thumb; B or less triggers a debt review | grades A++ to C | 54, 124 |
| Dividend yield example | $1.16 dividend: 3% at $40, 5% at $25 | not a stand-alone factor | 127 |

**Key quotes**

- "What is supporting the stock price at its current level?" [p. 120]
- "a price equal to the firm’s current assets less all liabilities" [p. 120]
- "discounts can range from 20 percent on generic goods, which can be used in other industries, to 80 percent for highly specific goods" [p. 121]
- "I would typically use 60 percent to 90 percent of the reported accounts receivable." [p. 134]
- "which can range from 10 percent to 60 percent of the value reported" [p. 124]
- "the price of the public company would hover above five times firm value" [p. 126]
- "particularly if the financial strength is rated a B or less by Value Line" [p. 124]

**Pseudocode**

```
def safety_floor(s, t):
    A = 1.00*cash + 0.70*receivables + 0.70*inventory + 0.90*PPE + 0.80*other_assets   # goodwill = 0
    A += dividend / 0.085                          # value of the dividend stream, if secure
    A -= total_liabilities_excluding_equity        # ASSUMPTION: all liabilities (incl. debt)
    return max(A, 0) / shares
# Net-net variant (Graham, p.120):
def net_net(s):  return (current_assets - total_liabilities) / shares
```

**Ambiguities & assumptions**
- The book gives the Maytag haircuts as industry judgements, not rules. ASSUMPTION: use the Maytag haircuts as defaults for non-financial companies; test liquidation haircuts of 20% and 80% as bounds.
- The Maytag exhibit adds dividends to assets and subtracts only debt (it keeps ongoing operating liabilities out of the exhibit) [p. 135]; the text says to deduct ongoing obligations, past obligations and long-term debt [p. 125]. The book is inconsistent. ASSUMPTION: subtract all liabilities (the more conservative text version).
- Take-private multiples need a deal dataset (not available). ASSUMPTION: skip this branch in backtests; use tangible book / net-net only.

### 2.4 Graham-style quantitative screen (the book's "Graham" criteria)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value, deep-value / defensive screen. | 27, 187 |
| Timeframe & holding period | Not specified in the screen. | |
| Universe / eligibility filters | Market capitalisation greater than the average company in the peer group; 20-year uninterrupted dividend record (first version, page 27). | 188, 27 |
| Market / regime filter | None. | |
| Setup conditions | Version A (p. 27): price no greater than 15x the average earnings of the past 3 years; current assets at least twice current liabilities; uninterrupted dividends for at least the past 20 years. Version B (p. 187 to 188): P/E below 15; price for the enterprise below 1.2x net tangible assets; assets to liabilities above 2 to 1; long-term debt not above 1.1x net current assets; market cap above peer average. | 27, 187, 188 |
| Entry trigger & order type | Buy stocks that pass all criteria (the author notes Graham "concentrated on price"). Order type not specified. | 188 |
| Initial stop-loss | Not specified. | |
| Exits: profit-taking | Not specified in this screen. | |
| Exits: trailing / time / signal | Not specified. | |
| Position sizing | Not specified. | |
| Adding to / pyramiding | Not specified. | |
| Portfolio limits (max positions, correlation, heat) | Not specified. | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| P/E (or price / 3-year average earnings) | below 15 (version B); 15x 3-year average earnings (version A) | | 187, 27 |
| Price / net tangible assets | below 1.2 | | 187 |
| Current assets / current liabilities | at least 2 (A: "at least twice"); B: assets to liabilities above 2:1 | | 27, 187 |
| Long-term debt / net current assets | not above 1.1 | | 188 |
| Dividend record | 20 uninterrupted years (version A only) | | 27 |
| Market cap | above peer-group average | | 188 |

**Key quotes**

- "with current assets at least twice current liabilities" [p. 27]
- "Price for the enterprise less than 1.2 times net tangible assets" [p. 187]
- "Assets-to-liabilities ratio must be greater than 2 to 1" [p. 187]
- "Long-term debt not greater than 1.1 times net current assets" [p. 188]
- "Price-to-earnings ratio less than 15 times" [p. 187]

**Pseudocode**

```
passes = (PE_3yr_avg <= 15) and (EV_or_price / net_tangible_assets_ps <= 1.2)
         and (current_assets / current_liabilities >= 2)
         and (long_term_debt <= 1.1 * (current_assets - current_liabilities))
         and (mcap >= peer_avg_mcap)
# optional: 20-year uninterrupted dividends (not available in our data)
buy all passes (equal weight, cap names at 20); exit rules from 2.8
```

**Ambiguities & assumptions**
- The author warns "it is best not to use certain numbers as a rule of thumb" [p. 195]; these are Graham's criteria quoted as illustration, not the author's own screen. ASSUMPTION: use as one candidate screen.
- "Assets-to-liabilities ratio" (total or current) is ambiguous in version B. ASSUMPTION: current ratio, as in version A.
- "Price for the enterprise" is read as market cap (or EV). ASSUMPTION: market cap / tangible book.
- Exit not defined. ASSUMPTION: use 2.8 sell rules (fair value from 2.2, or P/E above peer or 3-year time cap).

### 2.5 The book's screening blueprint (price-drawdown candidate list plus fundamental filters)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value / candidate generation (screen, then "search for value"). | 193, 195 |
| Timeframe & holding period | Not specified; ideas then go through the Five Keys. | 193 |
| Universe / eligibility filters | Good business: high ROE, earnings quality and growth, free cash flow, sustainable competitive advantage. Cheap price: depending on industry, P/E less than 15, price to sales less than 1.5, at or near private market valuations, and at least 40-percent discount to fair value. Margin of safety: pristine balance sheet, little debt relative to peers, tangible book value, near take-out or liquidation values. | 195 |
| Market / regime filter | Drawdown threshold depends on the market: 50% or more below the 52-week high in bull markets; 60% in bear and sideways markets. Bull/bear not defined. | 195 |
| Setup conditions | "Obtainable value": off 50% (bull) or 60% (bear/sideways) from the 52-week high; cyclical companies; industry leaders in commodity and low-tech industries. "Candidates for catalysts": extremely low margins in high-margin industries; trading at, near or below net cash; below net asset value. A WSJ-style scan: single-day or recent price declines of 25% or more, and industries down 20%. Example screen: health care, P/E below 15, debt to capitalisation below 40%, EV to operating cash flow below 6. | 195, 190, 193 |
| Entry trigger & order type | Screen only produces a watch list; purchase requires the Five Keys (2.1). | 193 |
| Initial stop-loss | Not specified. | |
| Exits: profit-taking | See 2.8. | |
| Exits: trailing / time / signal | See 2.8. | |
| Position sizing | Not specified. | |
| Adding to / pyramiding | Not specified. | |
| Portfolio limits (max positions, correlation, heat) | See 2.1 (15 names). | 199 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Drawdown from 52-week high (bull) | 50% or more | | 195 |
| Drawdown from 52-week high (bear or sideways) | 60% | | 195 |
| Single-day / recent decline flag | 25% or more | industry down 20% | 190 |
| Broad "buy day" | "Everything is down, say 5 percent to 10 percent" for short-lived reasons | sector drop of 20% in a day (homebuilders) | 166 |
| P/E | below 15 | industry dependent | 195 |
| P/S | below 1.5 | | 195 |
| Discount to fair value | at least 40% | | 195 |
| Debt / capitalisation | below 40% (example screen) | | 193 |
| EV / operating cash flow | below 6 (example screen) | | 193 |

**Key quotes**

- "Search for companies off 50 percent or more from 52-week highs in bull markets, and off 60 percent of highs in bear and sideway markets" [p. 195]
- "search for companies with price-to-earnings ratio less than 15, price to sales less than 1.5" [p. 195]
- "companies trading at, near, or below net cash on their balance sheets" [p. 195]
- "Search for companies with pristine balance sheets" [p. 195]
- "looking for companies with significant declines in price of say, 25 percent or more" [p. 190]
- "Everything is down, say 5 percent to 10 percent, for reasons that are often short-lived." [p. 166]
- "Buying a cyclical company with low valuation at the top of its cycle" [p. 163]

**Pseudocode**

```
# Price-only part (backtestable on 2005-2026 NSE prices):
dd = 1 - close[t] / rolling_max(high, 252)
regime = "bull" if index_close > index_SMA200 else "bear/sideways"     # ASSUMPTION
thr = 0.50 if regime == "bull" else 0.60
watchlist = {s : dd[s] >= thr and liquid(s) and not penny(s)}
# Optional fundamental overlays (forward-test only): PE<15, PS<1.5, debt/cap<40%, EV/OCF<6
# Watchlist then goes to Five Keys (2.1) or, for a purely mechanical test, equal-weight buy with exits from 2.8.
```

**Ambiguities & assumptions**
- "Off 50 percent from 52-week highs" is itself a deep-value proxy; bull/bear regime definition is absent. ASSUMPTION: index above or below its 200-day average.
- The drawdown screen alone does not filter value traps (the book warns about them [p. 163]). ASSUMPTION: add a quality filter (2.6) or require positive operating cash flow.
- "Absolute numbers... can be a very destructive element" [p. 195]: thresholds are illustrative. ASSUMPTION: test a grid around the quoted values.

### 2.6 Business-quality and accounting red-flag filters

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Quality / risk filter (exclusion rules). | 63 |
| Timeframe & holding period | Applied at purchase and at every quarterly report. | 179 |
| Universe / eligibility filters | Good business tests: consistent and strong free cash flow (cash-flow approach); ROE above cost of equity, with ROE decomposed (return on sales x asset turnover x leverage = ROE); EVA = after-tax operating income minus cost of capital x capital employed; interest coverage well above one; debt-to-capitalisation within industry norms; Value Line financial strength B+ or better. | 63, 60, 61, 65, 59, 54, 202 |
| Market / regime filter | None. | |
| Setup conditions | Red flags that call for closer investigation or exclusion: net income growing faster than operating cash flow; abnormal rise in inventory or receivables relative to sales growth; unexplained large write-offs or a large Q4 adjustment; an unusually low tax rate in a quarter; one-time items that recur; lending to customers; accounting policy differing from peers; management incentives purely on EPS. | 64, 63, 137, 178 |
| Entry trigger & order type | Not a trigger; a veto on candidates from 2.1, 2.4, 2.5. | |
| Initial stop-loss | Not specified. | |
| Exits: profit-taking | Not applicable. | |
| Exits: trailing / time / signal | Red flags appearing after purchase prompt a review and possibly a sale (Maytag: unexplained tax rate drop treated as "a red flag and a signal for further disappointments"). | 137, 186 |
| Position sizing | Not specified. | |
| Adding to / pyramiding | Not specified. | |
| Portfolio limits (max positions, correlation, heat) | Not specified. | |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Interest coverage (operating income / interest) | "a ratio of one" means risk of missing payments; healthy "well above one" | industry dependent | 60, 202 |
| Debt / capitalisation | industry specific; Pactiv fell from 60% to 52% | example screen below 40% | 183, 193 |
| ROE vs cost of equity | ROE greater than cost of equity | | 61 |
| Cost of capital used in EVA | 11% (Herman Miller) | | 68 |
| Value Line financial strength | B+ or better | B or less flagged | 54, 124 |
| Number of red flags | 15 listed | | 63, 64 |
| Management ownership | Chairman owning over 2% (Varian); required stock holding 3 to 5x salary (Pactiv) | | 40, 160 |

**Key quotes**

- "Net income is growing faster than cash flow from operations." [p. 64]
- "There is an abnormally high increase in inventory relative to sales growth." [p. 64]
- "Good businesses consistently produce ROEs greater than their equity cost of capital." [p. 61]
- "some value investors are interested in companies with a “B+” or better" [p. 54]

**Pseudocode**

```
flags = 0
flags += NI_growth_yoy > CFO_growth_yoy
flags += inventory_growth > sales_growth * 1.0        # "abnormally high" not quantified; ASSUMPTION: gap > 15 percentage points
flags += receivables_growth > sales_growth * 1.0      # same ASSUMPTION
flags += EBIT / interest_expense < 2                  # ASSUMPTION: "well above one" -> 2
flags += ROE < cost_of_equity                         # ASSUMPTION: 12% for NSE
flags += debt / (debt + equity) > 0.40
eligible = flags <= 1       # ASSUMPTION: the book gives no cut-off
```

**Ambiguities & assumptions**
- The book lists red flags as qualitative prompts, no thresholds. ASSUMPTION: thresholds as in the pseudocode, flagged as such.
- Items needing text (auditor opinion, footnotes, MD&A tone) are not codable and are skipped.

### 2.7 Staged ("dollar cost averaging") accumulation below a maximum price

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value, scale-in execution rule. | 172 |
| Timeframe & holding period | Accumulation phase of a position; length not specified. ASSUMPTION: weeks to months. | 171 |
| Universe / eligibility filters | Only for names that already pass 2.1 and whose thesis is unchanged. | 33 |
| Market / regime filter | Works best in volatile or jittery markets; "does not work well in bull markets". | 172 |
| Setup conditions | Fix a maximum reasonable price. Buy a small tranche at that price and larger tranches as the price falls (example $5,000 budget; reasonable price $15). | 172 |
| Entry trigger & order type | 50 shares at $15; 100 or more shares if the stock reaches $13. Never above $15. Order type not specified. | 172 |
| Initial stop-loss | Not specified. | |
| Exits: profit-taking | See 2.8. | |
| Exits: trailing / time / signal | Stop adding if the thesis changes. | 179 |
| Position sizing | Total budget per name set in advance ($5,000 in the example); tranche size grows as price falls. | 172 |
| Adding to / pyramiding | This is the add rule: add as price falls (averaging down), only while fundamentals are unchanged. | 33, 179 |
| Portfolio limits (max positions, correlation, heat) | See 2.1. Commission cost can make small tranches uneconomical. | 172 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Maximum price | $15 (example) = "reasonable price" | | 172 |
| First tranche | 50 shares at $15 (about 15% of $5,000) | | 172 |
| Second tranche | 100 or more shares at $13 | | 172 |
| Cap on cost per share | never more than the reasonable price | | 172 |

**Key quotes**

- "If the stock trades at $15, you may decide to purchase 50 shares at this price, while buying 100 or more shares if the stock reaches $13 per share." [p. 172]
- "not paying more than their reasonable price" [p. 172]
- "Dollar cost averaging, however, does not work well in bull markets" [p. 172]

**Pseudocode**

```
budget = target_weight * equity
max_px = 0.60 * fair_value                      # from 2.1
tranche_levels = [max_px, 0.87 * max_px, 0.75 * max_px]   # 15, 13, ... ASSUMPTION: 13/15 = 0.867
tranche_frac   = [0.15, 0.30, 0.55]                       # ASSUMPTION from 50 sh vs 100+ sh
for each level: if low <= level and thesis_ok: buy tranche_frac * budget at level
never buy above max_px
```

**Ambiguities & assumptions**
- The book gives one numerical example only. ASSUMPTION: three tranches at 0%, -13% and -25% from the maximum price, weights 15/30/55.
- No rule for averaging down when fundamentals are deteriorating beyond "reasons ... have not changed". ASSUMPTION: stop adding when 2.6 red flags rise.

### 2.8 Sell discipline, holding-period cap and catalyst test (event-driven component, partly codable)

| Field | Rule (as stated by the author) | Page |
|---|---|---|
| Type | Value exit rules plus event-driven catalysts. | 186, 97 |
| Timeframe & holding period | 3 to 5 years cap; "a finite exit point"; 5 to 10 years too long; the return target is within two to three years. | 186, 36 |
| Universe / eligibility filters | Positions already held; catalysts are "firm value" catalysts (merger or acquisition, spin-off, asset sale, buyback, new management, restructuring, activist, liquidation), not "stock" catalysts (splits, sector rotation). | 97, 98, 99 |
| Market / regime filter | None; but a market at greed levels leads to selling positions near fair value. | 165 |
| Setup conditions | Catalyst list and effectiveness: new management (CEO change); new strategy; efficiency; cost cuts (be skeptical: "the bigger the promise, the greater the skepticism"); lower tax rate; working capital reduction; capex cuts; share buybacks; spin-offs and carve-outs; split-offs; asset sales; full or partial liquidation (stock well below liquidating value); activists (13D; CalPERS list); industry M&A; time (end of a temporary negative). | 99 to 111, 101 |
| Entry trigger & order type | Thermo Electron was bought on the day a new CEO was announced (3/15/1999), after a four-month wait with price, value and safety already set; Maytag after five months of due diligence. | 114, 137 |
| Initial stop-loss | Not specified. | |
| Exits: profit-taking | At fair value; partial sales to lock profits (a few shares at $41 on takeover talk); sell early if the market pays fair value early. | 186, 138, 165 |
| Exits: trailing / time / signal | Sell on: deterioration or impairment; fair value reached; catalyst "unlikely to materialize, or is proven ineffective". Maytag: five reasons to sell (price, volume, distribution, tax rate surprise, criticism of CEO) after one year. | 186, 136, 137 |
| Position sizing | Not specified. | |
| Adding to / pyramiding | Not specified. | |
| Portfolio limits (max positions, correlation, heat) | See 2.1. | 199 |

**Parameters**

| Parameter | Book's value | Range or alternatives mentioned | Page |
|---|---|---|---|
| Maximum holding period | 3 to 5 years | buy-and-hold 5 to 10 years described as "may be too long" | 186 |
| Time to give a catalyst | "several quarters"; one year in Maytag | | 136 |
| Event window examples | Spin-off takes 6 to 8 months (Sybron) or about a year (Varian) | | 152, 39 |
| Buyback example size | $100 million at average $8.50 (Pactiv) | | 181 |
| Activist screen (CalPERS) | poor 3-year stock return; inefficient capital allocation; poor governance | | 109 |
| Price reaction on announcement | Varian +19% on spin-off news ($36 to $43); not chased | | 39 |

**Key quotes**

- "However, it is important to establish a finite exit point" [p. 186]
- "many investors consider 3 to 5 years ample time to allow companies to generate adequate returns" [p. 186]
- "After monitoring the company for one year, by October of 2000, I had sold the stock." [p. 136]
- "This book, however, focuses on firm value catalysts" [p. 97]

**Pseudocode**

```
for each holding h on each date t:
    if price >= fair_value(h): sell
    elif thesis_broken(h):     sell        # red flags from 2.6 rise, ROE collapse, new debt
    elif t - entry_date > 3 * 365 days (up to 5 years): sell
    elif catalyst_expected_date(h) < t - 365 and price < entry_price * 1.15: sell    # ASSUMPTION
# Event overlays (need corporate-action data): buy only after the event is announced if (price <= 0.60 * fv)
```

**Ambiguities & assumptions**
- "Potency" of catalysts is a judgement; no scoring rule. ASSUMPTION: treat a catalyst as present if an event type from the list (CEO change, buyback announcement, spin-off, large asset sale) occurred in the last 12 months. Event data not in our dataset.
- Time-based exit for failed catalysts is not numerical (Maytag one year). ASSUMPTION: 12 months with no re-rating.
- 3-year vs 5-year cap are alternatives. ASSUMPTION: 3 years (book's "perhaps more appropriate" is "3 to 5").

**Non-codable analytical material (summary table, allowed for non-codable content)**

| Topic | What the book says | Page |
|---|---|---|
| Management assessment | Compare annual reports year by year and against competitors; check whether promises were kept; EVA incentives; insider ownership. | 64, 65 |
| Vertical (income statement) assessment | Industry (Porter five forces), competitive position, cost, operating cost control, tax, debt analysis. | 55 to 60 |
| Quarterly earnings review | Three steps: trends in the numbers; get behind the numbers; re-check reasons for ownership. | 177, 179 |
| Mr. Market and economic awareness | Watch interest rates, corporate profits, inflation; do not predict; think cyclically. | 165 to 170 |
| Ideas from media and networks | WSJ, Barron's, IBD, 13D list, insider transactions, value-fund holdings. | 189 to 193 |

## 3. Risk & money-management rules

- Risk is defined as "an adverse and permanent change in the intrinsic value of the company", not price volatility; volatility is opportunity [p. 33].
- Total risk is business risk plus general market risk; focus on business risk, do not predict market risk [p. 128].
- Margin of safety is the main risk control; it "is not a guarantee" [p. 119]. Buy where downside (price to floor) is small relative to upside: 6% to 25% downside in cases [p. 114, 159].
- No stop-loss rule exists. Exits are fundamental (thesis broken, fair value, catalyst failed) [p. 186].
- Diversification: 10 to 20 names, preferably 15 [p. 199]; a study cited that most diversification benefit is gained by 16 stocks, and about 85% with 15 [p. 197]; hold names across different industries and investment types (restructuring, cyclical, high growth) [p. 198]. Buffett's 5 to 10 is quoted [p. 198].
- Be ready for volatility of a concentrated portfolio [p. 196]; allocate more to best ideas [p. 199].
- Shun uncertainty (businesses one does not understand) [p. 130]; avoid value traps (cheap bad businesses, cyclicals at the top of the cycle, stocks bought only for a low dollar price, the "cheapest" in an industry without understanding the economics) [p. 163].
- Debt: B or less Value Line financial strength warrants a critical look; too much debt is a red flag [p. 124].
- Commissions: DCA can be uneconomical for small accounts [p. 172].
- Do not time the market; buy right and use dollar cost averaging only up to a maximum price [p. 171, 172].

## 4. Non-codable guidance

- Emotional discipline is "the foundation upon which all is built"; avoid believing what you want to believe, lack of courage and short-termism [p. 23, 24].
- Seven Fundamental Beliefs (the world is not ending; fear and greed; inflation is the true enemy and prediction is useless; good ideas exist even in bear markets; companies convert resources into shareholder value; buy right; volatility is opportunity) [p. 28 to 34].
- Value investors do not rely on charts or momentum; they distrust analysts' ratings (conflicts of interest, under 1% sell ratings) [p. 26, 204].
- Read SEC filings (10-K, MD&A, proxy, 8-K); keep a written list of reasons for owning each stock and review it at every quarterly report [p. 40, 179].
- Ownership is a verb: monitor, vote, attend annual meetings, hold management accountable [p. 173, 185].
- Keep a notebook of deal multiples; unsophisticated investors should not copy others' screens without understanding them [p. 40, 194].
- Golf analogy: practise with tools until you have a feel; patience and humility [p. 140, 141].
- Investors who lack knowledge of a business "should not be in the game" with it; diversification hedges against ignorance (Buffett) [p. 198].

## 5. Adapting to NSE (Indian equities)

- **Data required:**
  - Price-only (available 2005 to 2026): daily OHLCV, 52-week high/low and drawdown, 200-day average of an equal-weight stock-panel index or NIFTYBEES as the regime proxy, price at fair-value levels, liquidity (average traded value) and circuit-hit flags. Delivery % (recent years) can proxy accumulation but the book does not use it.
  - Fundamental snapshots (from Feb 2026; 3-year growth fields from May 2026): price/earnings, price/book, price/sales, EV, EBITDA, free cash flow (net income + D&A - capex), operating cash flow, net income, revenue, receivables, inventory, current assets and liabilities, cash, total debt, long-term debt, equity, ROE, ROA, interest coverage, debt/equity, dividends, shares outstanding, promoter holding (proxy for "management owns shares").
  - Not available: deal/transaction multiples, catalyst events (spin-offs, buybacks, CEO changes, 13D equivalents), Value Line grades, appraised asset values, multi-year normalised earnings history before 2026.
- **Testability with our data:**
  - Backtestable (2005 to 2026 prices): the 52-week-drawdown screen of 2.5 (50% / 60% off highs) as a pure price rule with exits at a time cap (3 years) or price targets such as recovery to the prior high; the DCA staging mechanics of 2.7 on price; the 25% decline and "5 to 10% market-down day" flags as event study triggers.
  - Forward-test only (fundamentals from Feb 2026, growth fields from May 2026): 2.1 (needs fair value), 2.2, 2.3, 2.4 (Graham screen), the fundamental legs of 2.5 and the red flags of 2.6; there is no point-in-time history so these cannot be backtested before 2026.
  - Needs data we do not have: catalyst identification (2.8), take-out multiples, qualitative management and business analysis, an independent "normalised earnings" series, replacement-cost adjustments to assets.
- **Market-structure differences and adaptations:**
  - The book targets US large and mid caps with cheap access to 10-Ks, Value Line and deal multiples. For NSE use screener-style fields. ASSUMPTION: replace Value Line B+ with a quantitative proxy (debt/equity below 0.5 and interest coverage above 3).
  - Long-only is natural; no shorting is needed (the book is long-only). Cash is held when no candidates are found (book: keep cash if the market is expensive [p. 74]).
  - Circuit limits: a stock off 50% to 60% from its high may be in lower circuit bands (5% or 10%) and illiquid; entries and exits may not fill. ASSUMPTION: skip stocks with an average daily value under INR 1 crore and limit orders to 5% of average volume.
  - Costs: STT on delivery (0.1% each side), brokerage and about 0.1% slippage; a 3-year hold makes this small; DCA tranches cost more but remain modest. ASSUMPTION: 0.3% round trip plus 0.1% slippage per side.
  - Promoter ownership replaces the Price criterion that management owns shares [p. 36]; NSE disclosure of pledged shares is a red flag proxy (not in the book).
  - Fiscal year ends in March; use trailing 12 months and delay fundamentals by about 45 days (reporting lag) in any later point-in-time test.
  - Small caps: the Indian value universe has many illiquid, promoter-controlled stocks (value traps in the book's sense [p. 163]). ASSUMPTION: filter to the top 1,000 by traded value.

## 6. Verdict

- **Codeability:** Partly. The framework is mostly discretionary (fair value, floor and catalyst judgement), but the screens (2.4, 2.5, 2.6), the haircut asset valuation (2.3), the average-of-three fair value (2.2), the sell and time rules (2.8) and the staging rule (2.7) can be mechanised with fundamentals and price.
- **Priority for backtesting:** Medium. The price-only drawdown screen (2.5) is backtestable now and is a known deep-value style, but the book's own edge (fair value, margin of safety, catalyst) cannot be backtested with our data and must be forward-tested from 2026.
- **Top 3 things a coder is most likely to get wrong:**
  1. Treating the 40% discount rule as mechanical: fair value is a judgement average of three tools, the buy price is also constrained by a separate safety floor and a catalyst; without these the strategy collapses into a pure cheap-stock screen full of value traps.
  2. Inventing a stop-loss: the book explicitly has none; the safety floor is a valuation estimate not a stop, and exits are fair value, thesis failure or the 3 to 5 year cap.
  3. Using forward-looking or restated fundamentals in a backtest (look-ahead bias), or applying the screening thresholds (P/E 15, P/S 1.5, 50% and 60% off highs) as hard rules when the author says they are only illustrative ("only a few absolute numbers are given") [p. 195].
